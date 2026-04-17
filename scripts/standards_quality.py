#!/usr/bin/env python3
"""Standards-match quality report.

Goes beyond "is every TEKS covered" to ask "how well is it covered":
- Primary vs supporting alignment ratio per course
- ai-draft vs reviewed source ratio per course
- Alignment depth: atoms per TEKS (1 = thin, 3+ = strong)
- Orphan atoms: atoms in template that hit zero TEKS (scope creep signal)
- Weak TEKS: standards covered only by supporting-strength rows
"""
import csv
import os
import re
from collections import defaultdict

BASE = "/home/user/CTE"
SUB = f"{BASE}/library/digital-technology/it-support-services"
ATOM_DIR = f"{SUB}/atoms"
FRAMEWORK = f"{SUB}/crosswalks/texas/state-framework.csv"
CROSSWALK = f"{SUB}/crosswalks/texas/crosswalk.csv"
TPL_DIR = f"{SUB}/templates/texas"

TEMPLATES = [
    ("130.302", "tx-principles-of-it-2025.md", "Principles of IT"),
    ("130.303", "tx-computer-maintenance-2025.md", "Computer Maintenance"),
    ("130.304", "tx-computer-maintenance-lab-2025.md", "CM Lab"),
]


def load_crosswalk():
    rows = []
    with open(CROSSWALK) as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def teks_by_course():
    out = defaultdict(list)
    with open(FRAMEWORK) as f:
        for r in csv.DictReader(f):
            out[r["course_code"]].append(r["standard_code"])
    return out


def atom_credentials(atom_id):
    path = os.path.join(ATOM_DIR, atom_id + ".md")
    with open(path) as f:
        txt = f.read()
    m = re.search(r"credential_objectives:(.*?)(?:\nskill_type:|\Z)", txt, re.S)
    if not m:
        return []
    return re.findall(r"-\s+([^\s\n]+)", m.group(1))


def template_atoms(path):
    with open(path) as f:
        return re.findall(r"atom_id:\s+([\w-]+)", f.read())


def main():
    rows = load_crosswalk()
    course_teks = teks_by_course()

    # key -> list of (standard_code, alignment_strength, source)
    key_to_rows = defaultdict(list)
    for r in rows:
        key_to_rows[r["atom_id"]].append(
            (r["standard_code"], r["alignment_strength"], r["source"])
        )

    print(f"{'Course':<34} {'TEKS':>4} {'Cov%':>5} {'Prim':>5} {'Supp':>5} {'Rev':>4} {'Drft':>4} {'Thin':>4}")
    print("-" * 72)

    for code, fname, title in TEMPLATES:
        atoms = template_atoms(os.path.join(TPL_DIR, fname))
        all_teks = set(course_teks[code])

        # teks -> list of (atom, strength, source)
        teks_hits = defaultdict(list)
        atom_hits_teks = defaultdict(set)
        for a in atoms:
            keys = [a] + atom_credentials(a)
            for k in keys:
                for std, strength, source in key_to_rows.get(k, []):
                    if std in all_teks:
                        teks_hits[std].append((a, strength, source))
                        atom_hits_teks[a].add(std)

        covered = set(teks_hits.keys())
        primary_teks = {t for t, hits in teks_hits.items() if any(h[1] == "primary" for h in hits)}
        supporting_only = {t for t in covered if t not in primary_teks}
        reviewed_teks = {t for t, hits in teks_hits.items() if any(h[2] != "ai-draft" for h in hits)}
        ai_draft_only = {t for t in covered if t not in reviewed_teks}
        thin_teks = {t for t, hits in teks_hits.items() if len(hits) == 1}
        orphan_atoms = [a for a in atoms if not atom_hits_teks[a]]

        pct = 100 * len(covered) / len(all_teks)
        print(
            f"{code + ' ' + title:<34} {len(all_teks):>4} {pct:>4.0f}% "
            f"{len(primary_teks):>5} {len(supporting_only):>5} "
            f"{len(reviewed_teks):>4} {len(ai_draft_only):>4} "
            f"{len(thin_teks):>4}"
        )

        if orphan_atoms:
            print(f"    orphan atoms (no TEKS hit): {len(orphan_atoms)} \u2014 {', '.join(orphan_atoms[:5])}" + (" ..." if len(orphan_atoms) > 5 else ""))
        if supporting_only:
            print(f"    supporting-only TEKS: {', '.join(sorted(supporting_only)[:5])}" + (" ..." if len(supporting_only) > 5 else ""))

    print()
    print("Legend:")
    print("  Prim = TEKS with at least one primary-strength row")
    print("  Supp = TEKS with only supporting-strength rows (weaker coverage)")
    print("  Rev  = TEKS backed by at least one reviewed (non-ai-draft) row")
    print("  Drft = TEKS backed only by ai-draft rows (pending SME review)")
    print("  Thin = TEKS hit by exactly one atom (single point of failure)")


if __name__ == "__main__":
    main()
