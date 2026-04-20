#!/usr/bin/env python3
"""Assign and verify hierarchy-encoded atom serials.

Serials are in the format `<CLUSTER>-<SUBCLUSTER>-<NNNN>` (e.g., HHS-PH-0042),
where the cluster and sub-cluster codes are drawn from
`library/_schemas/atom-serial-codes.csv`. Serials are additive — the existing
kebab-case `atom_id` stays as the primary reference in templates, crosswalks,
scripts, and data files.

Usage:
    python3 scripts/assign_atom_serials.py --assign --subcluster physical-health
    python3 scripts/assign_atom_serials.py --next physical-health
    python3 scripts/assign_atom_serials.py --verify

Modes:
    --assign --subcluster <slug>  Assign sequential serials (alphabetical by
                                  atom_id) to any atoms in the sub-cluster
                                  missing `atom_serial`. Writes back to each
                                  atom's front-matter and appends to the
                                  sub-cluster's _serials.csv manifest.
                                  Idempotent — atoms already serialized are
                                  left untouched.
    --next <slug>                 Print the next available serial for the
                                  named sub-cluster (max existing + 1).
    --verify                      Walk all atom files under library/. Confirm
                                  every atom_serial is well-formed, matches
                                  its file path, and is unique within its
                                  sub-cluster. Non-zero exit on violation.
"""
import argparse
import csv
import datetime as dt
import os
import re
import sys
from collections import defaultdict

BASE = "/home/user/CTE"
CODES_CSV = os.path.join(BASE, "library/_schemas/atom-serial-codes.csv")
SERIAL_RE = re.compile(r"^([A-Z]{2,4})-([A-Z]{2,4})-(\d{4})$")


def load_codes():
    """Return two dicts: subcluster_slug -> code, and code pair -> slug pair."""
    sub_to_code = {}
    cluster_to_code = {}
    sub_to_cluster = {}
    with open(CODES_CSV) as f:
        for r in csv.DictReader(f):
            if r["level"] == "cluster":
                cluster_to_code[r["slug"]] = r["code"]
            elif r["level"] == "subcluster":
                sub_to_code[r["slug"]] = r["code"]
                # parent_code is the cluster code — translate back to slug
                sub_to_cluster[r["slug"]] = [
                    slug for slug, code in cluster_to_code.items() if code == r["parent_code"]
                ][0]
    return cluster_to_code, sub_to_code, sub_to_cluster


def subcluster_dir(cluster_slug, subcluster_slug):
    return os.path.join(BASE, "library", cluster_slug, subcluster_slug, "atoms")


def list_atom_files(atoms_dir):
    """Return sorted list of atom .md filenames (excluding _index.md)."""
    if not os.path.isdir(atoms_dir):
        return []
    return sorted(
        f for f in os.listdir(atoms_dir)
        if f.endswith(".md") and f != "_index.md"
    )


def parse_frontmatter(path):
    """Return (frontmatter_text, body_text, atom_id, atom_serial or None)."""
    with open(path) as f:
        content = f.read()
    m = re.match(r"^---\n(.*?\n)---\n(.*)$", content, re.S)
    if not m:
        raise ValueError(f"No YAML front-matter in {path}")
    fm, body = m.group(1), m.group(2)
    aid_m = re.search(r"^atom_id:\s*(\S+)", fm, re.M)
    atom_id = aid_m.group(1) if aid_m else None
    ser_m = re.search(r"^atom_serial:\s*(\S+)", fm, re.M)
    atom_serial = ser_m.group(1) if ser_m else None
    return fm, body, atom_id, atom_serial


def inject_serial(fm_text, serial):
    """Insert `atom_serial: <serial>` immediately after the atom_id line."""
    new_line = f"atom_serial: {serial}"
    lines = fm_text.splitlines(keepends=True)
    out = []
    inserted = False
    for line in lines:
        out.append(line)
        if not inserted and re.match(r"^atom_id:", line):
            out.append(new_line + "\n")
            inserted = True
    if not inserted:
        raise ValueError("atom_id line not found in front-matter")
    return "".join(out)


def write_atom(path, fm_text, body):
    with open(path, "w") as f:
        f.write("---\n" + fm_text + "---\n" + body)


def load_manifest(manifest_path):
    if not os.path.exists(manifest_path):
        return []
    with open(manifest_path) as f:
        return list(csv.DictReader(f))


def write_manifest(manifest_path, rows):
    with open(manifest_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["atom_serial", "atom_id", "assigned_date", "retired"])
        w.writeheader()
        for r in rows:
            w.writerow(r)


def cmd_assign(subcluster_slug):
    cluster_to_code, sub_to_code, sub_to_cluster = load_codes()
    if subcluster_slug not in sub_to_code:
        sys.exit(f"ERROR: sub-cluster '{subcluster_slug}' not in {CODES_CSV}")
    cluster_slug = sub_to_cluster[subcluster_slug]
    cluster_code = cluster_to_code[cluster_slug]
    sub_code = sub_to_code[subcluster_slug]
    atoms_dir = subcluster_dir(cluster_slug, subcluster_slug)
    manifest_path = os.path.join(atoms_dir, "_serials.csv")

    manifest = load_manifest(manifest_path)
    existing_serials = {r["atom_serial"] for r in manifest}
    next_num = max(
        (int(s.split("-")[-1]) for s in existing_serials), default=0
    ) + 1

    today = dt.date.today().isoformat()
    newly_assigned = []

    for fname in list_atom_files(atoms_dir):
        path = os.path.join(atoms_dir, fname)
        fm, body, atom_id, existing_serial = parse_frontmatter(path)
        if existing_serial:
            continue  # idempotent
        serial = f"{cluster_code}-{sub_code}-{next_num:04d}"
        next_num += 1
        new_fm = inject_serial(fm, serial)
        write_atom(path, new_fm, body)
        manifest.append({
            "atom_serial": serial,
            "atom_id": atom_id,
            "assigned_date": today,
            "retired": "false",
        })
        newly_assigned.append((serial, atom_id))

    write_manifest(manifest_path, manifest)
    if newly_assigned:
        print(f"Assigned {len(newly_assigned)} serials in {subcluster_slug}:")
        for s, a in newly_assigned:
            print(f"  {s}  {a}")
    else:
        print(f"No new serials needed; {subcluster_slug} already fully serialized.")


def cmd_next(subcluster_slug):
    _, sub_to_code, sub_to_cluster = load_codes()
    if subcluster_slug not in sub_to_code:
        sys.exit(f"ERROR: sub-cluster '{subcluster_slug}' not in {CODES_CSV}")
    cluster_slug = sub_to_cluster[subcluster_slug]
    atoms_dir = subcluster_dir(cluster_slug, subcluster_slug)
    manifest_path = os.path.join(atoms_dir, "_serials.csv")
    manifest = load_manifest(manifest_path)
    existing = {r["atom_serial"] for r in manifest}
    next_num = max(
        (int(s.split("-")[-1]) for s in existing), default=0
    ) + 1
    cluster_to_code, _, _ = load_codes()
    cluster_code = cluster_to_code[cluster_slug]
    sub_code = sub_to_code[subcluster_slug]
    print(f"{cluster_code}-{sub_code}-{next_num:04d}")


def cmd_verify():
    cluster_to_code, sub_to_code, sub_to_cluster = load_codes()
    # sub_slug -> list of (path, atom_id, atom_serial)
    by_sub = defaultdict(list)
    violations = []

    # Walk library/ for atom files
    lib = os.path.join(BASE, "library")
    for cluster_slug in os.listdir(lib):
        cluster_path = os.path.join(lib, cluster_slug)
        if not os.path.isdir(cluster_path) or cluster_slug.startswith("_"):
            continue
        if cluster_slug == "taxonomy":
            continue
        for sub_slug in os.listdir(cluster_path):
            atoms_dir = os.path.join(cluster_path, sub_slug, "atoms")
            if not os.path.isdir(atoms_dir):
                continue
            for fname in list_atom_files(atoms_dir):
                path = os.path.join(atoms_dir, fname)
                try:
                    _, _, atom_id, serial = parse_frontmatter(path)
                except ValueError as e:
                    violations.append(f"PARSE ERROR {path}: {e}")
                    continue
                if not serial:
                    continue  # atom without serial is OK (not yet assigned)
                m = SERIAL_RE.match(serial)
                if not m:
                    violations.append(f"MALFORMED serial '{serial}' in {path}")
                    continue
                ccode, scode, _ = m.groups()
                # The atom's sub-cluster code should match its file path
                expected_scode = sub_to_code.get(sub_slug)
                if expected_scode and scode != expected_scode:
                    violations.append(
                        f"PATH MISMATCH {path}: serial says {scode}, path says {expected_scode}"
                    )
                # The atom's cluster code should match its file path
                expected_ccode = cluster_to_code.get(cluster_slug)
                if expected_ccode and ccode != expected_ccode:
                    violations.append(
                        f"CLUSTER MISMATCH {path}: serial says {ccode}, path says {expected_ccode}"
                    )
                by_sub[sub_slug].append((path, atom_id, serial))

    # Uniqueness within sub-cluster
    for sub_slug, rows in by_sub.items():
        seen = {}
        for path, atom_id, serial in rows:
            if serial in seen:
                violations.append(
                    f"DUPLICATE serial {serial}: {path} and {seen[serial]}"
                )
            seen[serial] = path

    # Manifest consistency: every serial in atom should be in its manifest once
    for sub_slug, rows in by_sub.items():
        if sub_slug not in sub_to_cluster:
            continue
        cluster_slug = sub_to_cluster[sub_slug]
        manifest_path = os.path.join(subcluster_dir(cluster_slug, sub_slug), "_serials.csv")
        manifest = load_manifest(manifest_path)
        manifest_serials = [r["atom_serial"] for r in manifest]
        manifest_set = set(manifest_serials)
        if len(manifest_serials) != len(manifest_set):
            violations.append(f"DUPLICATE row in {manifest_path}")
        for path, atom_id, serial in rows:
            if serial not in manifest_set:
                violations.append(
                    f"MISSING from manifest: {serial} ({atom_id}) not in {manifest_path}"
                )

    if violations:
        print(f"FAIL — {len(violations)} violations:")
        for v in violations:
            print(f"  {v}")
        sys.exit(1)
    total = sum(len(v) for v in by_sub.values())
    print(f"OK — {total} serials verified across {len(by_sub)} sub-clusters")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--assign", action="store_true", help="assign serials")
    p.add_argument("--subcluster", help="sub-cluster slug")
    p.add_argument("--next", help="print next available serial for sub-cluster slug")
    p.add_argument("--verify", action="store_true", help="verify all serials")
    args = p.parse_args()

    if args.assign:
        if not args.subcluster:
            p.error("--assign requires --subcluster")
        cmd_assign(args.subcluster)
    elif args.next:
        cmd_next(args.next)
    elif args.verify:
        cmd_verify()
    else:
        p.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
