#!/usr/bin/env python3
"""Verify the mechanical invariants of atom sidecars.

Sidecars live at `library/<cluster>/<subcluster>/atoms/<atom-id>/` alongside
the canonical `<atom-id>.md` stub. See `library/_schemas/atom-sidecars/` for
conventions. This script checks the invariants that can be mechanized — not
the qualitative "traces to the LO" judgment, which stays with the reviewer.

Usage:
    python3 scripts/verify_atom_sidecars.py --atom body-systems-overview
    python3 scripts/verify_atom_sidecars.py --subcluster physical-health
    python3 scripts/verify_atom_sidecars.py --all

Checks performed per atom (when a sidecar folder exists):
  1. Folder layout — atom-id folder adjacent to <atom-id>.md
  2. Front-matter sanity — every sidecar's atom_id/atom_serial/sidecar match
     the stub; status in {ai-draft, reviewed, published}
  3. Count fields match reality — word_count, example_count,
     misconception_count, asset_count, source_count, term_count, item_count
  4. book.md word count within schema bounds for atom's difficulty
  5. Every vocab term in vocabulary.csv appears at least once in book.md
  6. Every citation [key] in book/examples/misconceptions resolves to a
     sources.md H3 entry
  7. Every misconception in misconceptions.md is addressed by at least
     one question-bank item (via misconception_addressed field)
  8. vocabulary.csv parses cleanly (no malformed rows)
  9. question-bank.yaml parses cleanly
 10. Bloat signals — warn (not fail) when vocab > 20 terms, questions > 15,
     media assets > 8

Exit code: 0 on pass, 1 if any atom has failures. Warnings don't fail.
"""
import argparse
import csv
import io
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LIB = REPO / "library"

# Word-count bounds per atom difficulty (from schema book.md)
WORD_BOUNDS = {
    "1": (1500, 2500),
    "2": (2000, 3000),
    "3": (2500, 3500),
}

# Bloat thresholds (warnings)
BLOAT = {
    "vocab_terms": 20,
    "question_items": 15,
    "media_assets": 8,
}

STATUSES = {"ai-draft", "reviewed", "published"}


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^(\w+):\s*(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip()
    return fm, m.group(2)


def read_atom_stub(stub_path):
    """Return dict of atom_id, atom_serial, difficulty, skill_type."""
    with open(stub_path) as f:
        fm, _ = parse_frontmatter(f.read())
    return fm or {}


def cite_keys(text):
    """Extract bracketed citation keys from prose."""
    out = set()
    for m in re.finditer(r"\[([^\]]+)\]", text):
        inner = m.group(1).replace("\n", " ").strip()
        # Skip non-citation bracketed text (e.g., item ids, option letters)
        if inner.startswith(("q0", "#", "http")) or inner in {
            "Option A",
            "Option B",
            "Option C",
            "Option D",
        }:
            continue
        for k in inner.split(","):
            k = k.strip()
            if k:
                out.add(k)
    return out


def verify_atom(sidecar_dir, stub_path):
    """Return (failures, warnings) lists of strings."""
    fails = []
    warns = []

    stub = read_atom_stub(stub_path)
    atom_id = stub.get("atom_id", sidecar_dir.name)
    atom_serial = stub.get("atom_serial", "")
    difficulty = stub.get("difficulty", "1")
    skill_type = stub.get("skill_type", "knowledge")

    expected_files = {
        "book.md",
        "vocabulary.csv",
        "examples.md",
        "misconceptions.md",
        "question-bank.yaml",
        "media-brief.md",
        "sources.md",
    }
    if skill_type == "skill":
        expected_files.add("rubric.md")

    present = {p.name for p in sidecar_dir.iterdir() if p.is_file()}

    # 1. Folder layout — sidecar folder name matches stub
    if sidecar_dir.name != atom_id:
        fails.append(f"folder name {sidecar_dir.name!r} != atom_id {atom_id!r}")

    # 2. Front-matter of each prose sidecar matches stub identity
    prose_files = ["book.md", "examples.md", "misconceptions.md", "media-brief.md", "sources.md"]
    for fname in prose_files:
        p = sidecar_dir / fname
        if not p.exists():
            continue
        with open(p) as f:
            fm, _ = parse_frontmatter(f.read())
        if not fm:
            fails.append(f"{fname}: no front-matter")
            continue
        if fm.get("atom_id") != atom_id:
            fails.append(f"{fname}: atom_id {fm.get('atom_id')!r} != {atom_id!r}")
        if fm.get("atom_serial") and fm.get("atom_serial") != atom_serial:
            fails.append(f"{fname}: atom_serial mismatch")
        if fm.get("status") not in STATUSES:
            fails.append(f"{fname}: status {fm.get('status')!r} not in {STATUSES}")

    # 3. Count fields vs. reality
    book_path = sidecar_dir / "book.md"
    book_body = ""
    book_wc = 0
    if book_path.exists():
        with open(book_path) as f:
            fm, body = parse_frontmatter(f.read())
        book_body = body
        book_wc = len(body.split())
        if fm:
            declared = fm.get("word_count")
            if declared and abs(int(declared) - book_wc) > 5:
                fails.append(f"book.md: word_count frontmatter {declared} != actual {book_wc}")
            lo, hi = WORD_BOUNDS.get(difficulty, (1500, 3500))
            if book_wc < lo or book_wc > hi:
                warns.append(
                    f"book.md: word count {book_wc} outside difficulty-{difficulty} bounds {lo}-{hi}"
                )

    ex_path = sidecar_dir / "examples.md"
    if ex_path.exists():
        with open(ex_path) as f:
            fm, body = parse_frontmatter(f.read())
        count = len(re.findall(r"^## Example \d+", body, re.M))
        declared = int(fm.get("example_count", -1)) if fm else -1
        if declared != count:
            fails.append(f"examples.md: example_count frontmatter {declared} != actual {count}")
        if count < 3 or count > 5:
            warns.append(f"examples.md: {count} examples (schema recommends 3-5)")

    mis_path = sidecar_dir / "misconceptions.md"
    mis_labels = []
    if mis_path.exists():
        with open(mis_path) as f:
            fm, body = parse_frontmatter(f.read())
        mis_labels = re.findall(r"^## (Misconception \d+)", body, re.M)
        declared = int(fm.get("misconception_count", -1)) if fm else -1
        if declared != len(mis_labels):
            fails.append(
                f"misconceptions.md: misconception_count {declared} != actual {len(mis_labels)}"
            )
        if len(mis_labels) < 3 or len(mis_labels) > 5:
            warns.append(f"misconceptions.md: {len(mis_labels)} (schema recommends 3-5)")

    mb_path = sidecar_dir / "media-brief.md"
    if mb_path.exists():
        with open(mb_path) as f:
            fm, body = parse_frontmatter(f.read())
        assets = len(re.findall(r"^\| m\d", body, re.M))
        declared = int(fm.get("asset_count", -1)) if fm else -1
        if declared != assets:
            fails.append(f"media-brief.md: asset_count {declared} != actual {assets}")
        if assets > BLOAT["media_assets"]:
            warns.append(f"media-brief.md: {assets} assets (> {BLOAT['media_assets']} = bloat signal)")

    src_path = sidecar_dir / "sources.md"
    src_keys = set()
    if src_path.exists():
        with open(src_path) as f:
            fm, body = parse_frontmatter(f.read())
        src_keys = set(re.findall(r"^### (.+)$", body, re.M))
        declared = int(fm.get("source_count", -1)) if fm else -1
        if declared != len(src_keys):
            fails.append(f"sources.md: source_count {declared} != actual {len(src_keys)}")

    vocab_path = sidecar_dir / "vocabulary.csv"
    vocab_terms = []
    if vocab_path.exists():
        with open(vocab_path) as f:
            content = f.read()
        lines = [l for l in content.splitlines() if not l.startswith("#") and l.strip()]
        try:
            reader = csv.DictReader(lines)
            rows = list(reader)
            vocab_terms = [r["term"] for r in rows if r.get("term")]
            # Check column count consistency
            reader2 = csv.reader(lines)
            header = next(reader2)
            bad_rows = [i for i, r in enumerate(reader2, 2) if len(r) != len(header)]
            if bad_rows:
                fails.append(
                    f"vocabulary.csv: {len(bad_rows)} rows with wrong column count (lines {bad_rows[:5]}...)"
                )
        except csv.Error as e:
            fails.append(f"vocabulary.csv: parse error {e}")
        tc_m = re.search(r"# term_count:\s*(\d+)", content)
        if tc_m and int(tc_m.group(1)) != len(vocab_terms):
            fails.append(
                f"vocabulary.csv: term_count comment {tc_m.group(1)} != actual {len(vocab_terms)}"
            )
        if len(vocab_terms) > BLOAT["vocab_terms"]:
            warns.append(
                f"vocabulary.csv: {len(vocab_terms)} terms (> {BLOAT['vocab_terms']} = bloat signal)"
            )

    qb_path = sidecar_dir / "question-bank.yaml"
    qb_items = []
    addressed_misconceptions = set()
    if qb_path.exists():
        try:
            import yaml

            with open(qb_path) as f:
                qb = yaml.safe_load(f)
            qb_items = qb.get("items", [])
            meta = qb.get("meta", {})
            declared = meta.get("item_count")
            if declared is not None and declared != len(qb_items):
                fails.append(
                    f"question-bank.yaml: item_count {declared} != actual {len(qb_items)}"
                )
            if len(qb_items) > BLOAT["question_items"]:
                warns.append(
                    f"question-bank.yaml: {len(qb_items)} items (> {BLOAT['question_items']} = bloat signal)"
                )
            for it in qb_items:
                if it.get("misconception_addressed"):
                    addressed_misconceptions.add(it["misconception_addressed"])
        except Exception as e:
            fails.append(f"question-bank.yaml: parse error {e}")

    # 5. vocab-in-book coverage
    if book_body and vocab_terms:
        book_lower = book_body.lower()
        missing = [t for t in vocab_terms if t.lower() not in book_lower]
        if missing:
            fails.append(f"vocabulary.csv: terms missing from book.md: {missing}")

    # 6. Citation resolution across prose files
    if src_keys:
        prose_cites = set()
        for fname in ("book.md", "examples.md", "misconceptions.md"):
            p = sidecar_dir / fname
            if p.exists():
                with open(p) as f:
                    prose_cites |= cite_keys(f.read())
        missing_src = prose_cites - src_keys
        unused_src = src_keys - prose_cites
        if missing_src:
            fails.append(f"sources.md: cited keys missing from sources: {sorted(missing_src)}")
        if unused_src:
            warns.append(f"sources.md: defined but uncited in prose: {sorted(unused_src)}")

    # 7. Misconception coverage
    if mis_labels:
        uncovered = [m for m in mis_labels if m not in addressed_misconceptions]
        if uncovered:
            fails.append(
                f"question-bank.yaml: misconceptions not addressed by any item: {uncovered}"
            )

    # Missing files
    missing_files = expected_files - present
    extra_files = present - expected_files
    if missing_files:
        warns.append(f"missing sidecar files: {sorted(missing_files)}")
    if extra_files:
        # Not a failure — atoms may have extras like rubric.md
        pass

    return fails, warns


def atoms_in_subcluster(subcluster_slug):
    """Return list of (sidecar_dir, stub_path) for atoms with sidecar folders."""
    out = []
    for cluster in LIB.iterdir():
        if not cluster.is_dir() or cluster.name.startswith("_"):
            continue
        sub = cluster / subcluster_slug
        atoms_dir = sub / "atoms"
        if not atoms_dir.is_dir():
            continue
        for entry in atoms_dir.iterdir():
            if entry.is_dir() and not entry.name.startswith("_"):
                stub = atoms_dir / f"{entry.name}.md"
                if stub.exists():
                    out.append((entry, stub))
    return out


def atoms_all():
    out = []
    for cluster in LIB.iterdir():
        if not cluster.is_dir() or cluster.name.startswith("_"):
            continue
        for sub in cluster.iterdir():
            if not sub.is_dir():
                continue
            atoms_dir = sub / "atoms"
            if not atoms_dir.is_dir():
                continue
            for entry in atoms_dir.iterdir():
                if entry.is_dir() and not entry.name.startswith("_"):
                    stub = atoms_dir / f"{entry.name}.md"
                    if stub.exists():
                        out.append((entry, stub))
    return out


def find_atom(atom_id):
    for sidecar_dir, stub in atoms_all():
        if sidecar_dir.name == atom_id:
            return sidecar_dir, stub
    return None


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--atom", help="verify a single atom by atom_id")
    p.add_argument("--subcluster", help="verify all atoms in a sub-cluster")
    p.add_argument("--all", action="store_true", help="verify every atom with sidecars")
    args = p.parse_args()

    if args.atom:
        hit = find_atom(args.atom)
        if not hit:
            sys.exit(f"no sidecar folder for atom {args.atom!r}")
        targets = [hit]
    elif args.subcluster:
        targets = atoms_in_subcluster(args.subcluster)
    elif args.all:
        targets = atoms_all()
    else:
        p.print_help()
        sys.exit(1)

    total_fails = 0
    total_warns = 0
    for sidecar_dir, stub in sorted(targets, key=lambda t: t[0].name):
        fails, warns = verify_atom(sidecar_dir, stub)
        status = "OK" if not fails else "FAIL"
        symbol = "✓" if not fails else "✗"
        summary = f"{symbol} {sidecar_dir.name}"
        if warns:
            summary += f"  ({len(warns)} warnings)"
        print(summary)
        for f in fails:
            print(f"    FAIL: {f}")
            total_fails += 1
        for w in warns:
            print(f"    warn: {w}")
            total_warns += 1

    print()
    print(f"Summary: {len(targets)} atoms checked, {total_fails} failures, {total_warns} warnings")
    sys.exit(1 if total_fails else 0)


if __name__ == "__main__":
    main()
