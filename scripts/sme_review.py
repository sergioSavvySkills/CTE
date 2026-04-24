#!/usr/bin/env python3
"""SME review of course templates for Texas Health Science.

Surfaces issues a human SME would flag:
1. Duplicated lessons within a course.
2. Cross-course lesson sharing.
3. Pacing realism: lesson count vs declared weeks.
4. Unit-level completeness (e.g., no summative_quiz).

Usage:
    python3 scripts/sme_review.py                  # defaults: Texas
    python3 scripts/sme_review.py --state texas
"""
import argparse
import os
import re
import yaml
from collections import defaultdict

BASE = "/home/user/CTE"
PATHWAY_DIR = f"{BASE}/library/health-science"

PERIODS_PER_WEEK = 5
MINS_PER_PERIOD = 45


def parse_template(path):
    with open(path) as f:
        txt = f.read()
    m = re.search(r"```yaml\n(.*?)\n```", txt, re.S)
    return yaml.safe_load(m.group(1)) if m else None


def template_meta(path):
    with open(path) as f:
        txt = f.read()
    m = re.match(r"---\n(.*?)\n---", txt, re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def review_course(code, fname, title, tpl_dir):
    tpl = parse_template(os.path.join(tpl_dir, fname))
    units = tpl["units"]

    ordered = []
    for ui, unit in enumerate(units):
        for si, slot in enumerate(unit.get("slots", []) or []):
            ordered.append((ui, si, slot["lesson_id"], slot))

    findings = []

    seen = {}
    for ui, si, lid, _ in ordered:
        if lid in seen:
            pui, psi = seen[lid]
            findings.append(f"U{ui+1:02d} slot {si+1} `{lid}` — **duplicate** (first appears U{pui+1:02d} slot {psi+1})")
        else:
            seen[lid] = (ui, si)

    declared_weeks = sum(u.get("weeks", 0) for u in units)
    available_mins = declared_weeks * PERIODS_PER_WEEK * MINS_PER_PERIOD
    lesson_mins = len(ordered) * MINS_PER_PERIOD
    pacing_note = (
        f"**Pacing:** {len(ordered)} lessons, {lesson_mins} estimated minutes total, "
        f"{declared_weeks} declared weeks ({available_mins} min @ {PERIODS_PER_WEEK}×{MINS_PER_PERIOD} min/week). "
        f"Slack for assessments/reviews: {available_mins - lesson_mins} min "
        f"({100 * (available_mins - lesson_mins) / available_mins:.0f}%)."
        if available_mins else f"**Pacing:** {len(ordered)} lessons."
    )

    for ui, unit in enumerate(units):
        ug = unit.get("unit_generate") or {}
        if not ug.get("summative_quiz", False):
            findings.append(f"U{ui+1:02d} `{unit.get('title','')}` has `summative_quiz: false` — unusual for a CTE unit")

    return {
        "code": code,
        "title": title,
        "unit_count": len(units),
        "slot_count": len(ordered),
        "weeks": declared_weeks,
        "pacing": pacing_note,
        "findings": findings,
        "lessons": [lid for _, _, lid, _ in ordered],
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--state", default="texas")
    args = p.parse_args()

    tpl_dir = f"{PATHWAY_DIR}/templates/{args.state}"
    out = f"{PATHWAY_DIR}/crosswalks/{args.state}/sme-review.md"

    templates = []
    for fname in sorted(os.listdir(tpl_dir)):
        if not fname.endswith(".md") or fname.startswith("_"):
            continue
        meta = template_meta(os.path.join(tpl_dir, fname))
        templates.append((str(meta.get("course_code", "?")), fname, meta.get("course_name", "?")))

    reviews = [review_course(c, f, t, tpl_dir) for c, f, t in templates]

    lines = [
        f"# health-science ({args.state}) — SME Review",
        "",
        "Automated first-pass review of course templates. Surfaces items a human",
        "SME (Maya) should confirm before promoting any template to `status: active`.",
        "Not every finding is a defect — some are intentional design choices that",
        "just need a sign-off.",
        "",
        "## How to read the findings",
        "",
        "**`duplicate`** — Same lesson appears more than once in a course. Usually",
        "a copy/paste error; occasionally intentional review.",
        "",
        "**`summative_quiz: false`** — Confirm intent. Every CTE unit normally",
        "ends with a summative assessment.",
        "",
    ]

    for r in reviews:
        lines += [
            f"## {r['code']} — {r['title']}",
            "",
            f"- Units: **{r['unit_count']}** — Lessons: **{r['slot_count']}** — Weeks declared: **{r['weeks']}**",
            f"- {r['pacing']}",
            "",
        ]
        if r["findings"]:
            lines.append("### Findings to review")
            lines.append("")
            for f in r["findings"]:
                lines.append(f"- {f}")
            lines.append("")
        else:
            lines.append("_No automated findings — still worth a human scan for pedagogical order._\n")

    lesson_to_courses = defaultdict(list)
    for r in reviews:
        for lesson in set(r["lessons"]):
            lesson_to_courses[lesson].append(r["code"])
    shared = sorted(
        ((lesson, cs) for lesson, cs in lesson_to_courses.items() if len(cs) > 1),
        key=lambda x: (-len(x[1]), x[0]),
    )
    lines += [
        "## Cross-course lesson sharing",
        "",
        f"Total lessons used across the templates: **{len(lesson_to_courses)}**.",
        f"Lessons shared by 2+ courses: **{len(shared)}**.",
        "",
    ]
    for lesson, cs in shared[:50]:
        lines.append(f"- `{lesson}` — in {', '.join(cs)}")
    if len(shared) > 50:
        lines.append(f"- ...and {len(shared) - 50} more")

    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write("\n".join(lines))
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
