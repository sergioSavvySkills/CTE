#!/usr/bin/env python3
"""Standards-match quality report for Texas Health Science.

Goes beyond "is every standard covered" to ask "how well is it covered":
- Primary vs supporting alignment ratio per course
- ai-draft vs reviewed source ratio per course
- Alignment depth: lessons per standard (1 = thin, 3+ = strong)
- Orphan lessons: lessons in template that hit zero standards (scope creep)
- Weak standards: covered only by supporting-strength rows

Usage:
    python3 scripts/standards_quality.py                  # defaults: Texas
    python3 scripts/standards_quality.py --state texas
"""
import argparse
import csv
import os
import re
import yaml
from collections import defaultdict

BASE = "/home/user/CTE"
PATHWAY_DIR = f"{BASE}/library/health-science"


def template_lessons(path):
    with open(path) as f:
        return re.findall(r"lesson_id:\s+([\w\.\-]+)", f.read())


def template_meta(path):
    with open(path) as f:
        txt = f.read()
    m = re.match(r"---\n(.*?)\n---", txt, re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--state", default="texas")
    args = p.parse_args()

    framework = f"{PATHWAY_DIR}/crosswalks/{args.state}/state-framework.csv"
    crosswalk = f"{PATHWAY_DIR}/crosswalks/{args.state}/crosswalk.csv"
    tpl_dir = f"{PATHWAY_DIR}/templates/{args.state}"

    standards_by_course = defaultdict(list)
    with open(framework) as f:
        for r in csv.DictReader(f):
            standards_by_course[r["course_code"]].append(r["standard_code"])

    rows = []
    with open(crosswalk) as f:
        rows = list(csv.DictReader(f))

    lesson_to_rows = defaultdict(list)
    for r in rows:
        lesson_to_rows[r["lesson_id"]].append(
            (r["standard_code"], r["alignment_strength"], r["source"])
        )

    templates = []
    for fname in sorted(os.listdir(tpl_dir)):
        if not fname.endswith(".md") or fname.startswith("_"):
            continue
        meta = template_meta(os.path.join(tpl_dir, fname))
        templates.append((str(meta.get("course_code", "?")), fname, meta.get("course_name", "?")))

    print(f"## health-science ({args.state}) — Standards Quality Report")
    print()
    print(f"{'Course':<50} {'Std':>4} {'Cov%':>5} {'Prim':>5} {'Supp':>5} {'Rev':>4} {'Drft':>4} {'Thin':>4}")
    print("-" * 86)

    for code, fname, title in templates:
        lessons = template_lessons(os.path.join(tpl_dir, fname))
        all_std = set(standards_by_course[code])

        std_hits = defaultdict(list)
        lesson_hits = defaultdict(set)
        for lesson in lessons:
            for std, strength, source in lesson_to_rows.get(lesson, []):
                if std in all_std:
                    std_hits[std].append((lesson, strength, source))
                    lesson_hits[lesson].add(std)

        covered = set(std_hits.keys())
        primary = {t for t, h in std_hits.items() if any(x[1] == "primary" for x in h)}
        supp_only = {t for t in covered if t not in primary}
        reviewed = {t for t, h in std_hits.items() if any(x[2] != "ai-draft" for x in h)}
        ai_only = {t for t in covered if t not in reviewed}
        thin = {t for t, h in std_hits.items() if len(h) == 1}
        orphans = [lesson for lesson in lessons if not lesson_hits[lesson]]

        pct = 100 * len(covered) / len(all_std) if all_std else 0
        label = f"{code} {title}"[:48]
        print(
            f"{label:<50} {len(all_std):>4} {pct:>4.0f}% "
            f"{len(primary):>5} {len(supp_only):>5} "
            f"{len(reviewed):>4} {len(ai_only):>4} "
            f"{len(thin):>4}"
        )
        if orphans:
            print(f"    orphan lessons (no standard hit): {len(orphans)} — {', '.join(orphans[:5])}" + (" ..." if len(orphans) > 5 else ""))
        if supp_only:
            print(f"    supporting-only standards: {', '.join(sorted(supp_only)[:5])}" + (" ..." if len(supp_only) > 5 else ""))

    print()
    print("Legend:")
    print("  Prim = standards with at least one primary-strength row")
    print("  Supp = standards with only supporting-strength rows (weaker)")
    print("  Rev  = standards backed by a reviewed (non-ai-draft) row")
    print("  Drft = standards backed only by ai-draft rows (pending SME)")
    print("  Thin = standards hit by exactly one lesson (single point of failure)")


if __name__ == "__main__":
    main()
