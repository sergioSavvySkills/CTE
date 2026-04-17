#!/usr/bin/env python3
"""SME review of course templates for a subcluster + state.

Surfaces issues a human SME would flag:
1. Prerequisite violations within a course (prereq appears later or missing).
2. Pacing realism: atom-minutes vs declared weeks.
3. Skill-type / generator mismatches.
4. Duplicated atoms within a course.
5. Cross-course atom sharing.
6. Unit-level generator smells (e.g., no summative_quiz).

Usage:
    python3 scripts/sme_review.py                          # IT-Support / Texas (default)
    python3 scripts/sme_review.py --sub data-science-ai --state georgia
"""
import argparse
import os
import re
import yaml
from collections import defaultdict

BASE = "/home/user/CTE"

CLUSTER_OF = {
    "it-support-services": "digital-technology",
    "data-science-ai": "digital-technology",
    "network-systems-cybersecurity": "digital-technology",
    "software-solutions": "digital-technology",
    "web-cloud": "digital-technology",
    "unmanned-vehicle-technology": "digital-technology",
}

PERIODS_PER_WEEK = 5


def atom_meta(atom_dir, atom_id):
    path = os.path.join(atom_dir, atom_id + ".md")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        txt = f.read()
    m = re.match(r"---\n(.*?)\n---", txt, re.S)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}


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


def review_course(code, fname, title, tpl_dir, atom_dir):
    tpl = parse_template(os.path.join(tpl_dir, fname))
    units = tpl["units"]

    ordered = []
    for ui, unit in enumerate(units):
        for si, slot in enumerate(unit.get("slots", []) or []):
            ordered.append((ui, si, slot["atom_id"], slot))

    meta_cache = {a: atom_meta(atom_dir, a) for _, _, a, _ in ordered}
    findings = []

    atom_first_pos = {}
    for idx, (_, _, aid, _) in enumerate(ordered):
        atom_first_pos.setdefault(aid, idx)
    for idx, (ui, si, aid, _) in enumerate(ordered):
        meta = meta_cache.get(aid) or {}
        for pre in meta.get("prerequisites") or []:
            pre_pos = atom_first_pos.get(pre)
            if pre_pos is None:
                findings.append(f"U{ui+1:02d} slot {si+1} `{aid}` requires `{pre}` — **prereq not in course**")
            elif pre_pos > idx:
                findings.append(f"U{ui+1:02d} slot {si+1} `{aid}` requires `{pre}` — **prereq appears later** at position {pre_pos+1}")

    total_minutes = sum(int((meta_cache.get(aid) or {}).get("estimated_minutes") or 45)
                       for _, _, aid, _ in ordered)
    declared_weeks = sum(u.get("weeks", 0) for u in units)
    available = declared_weeks * PERIODS_PER_WEEK * 45
    pacing_note = (
        f"**Pacing:** {len(ordered)} slots, {total_minutes} atom-minutes total, "
        f"{declared_weeks} declared weeks ({available} min @ {PERIODS_PER_WEEK}×45 min/week). "
        f"Slack for assessments/reviews: {available - total_minutes} min "
        f"({100 * (available - total_minutes) / available:.0f}%)."
        if available else f"**Pacing:** {len(ordered)} slots, {total_minutes} atom-minutes."
    )

    for ui, si, aid, slot in ordered:
        meta = meta_cache.get(aid) or {}
        st = meta.get("skill_type", "knowledge")
        gen = slot.get("generate") or {}
        sim = gen.get("simulation")
        if st == "knowledge" and sim is True:
            findings.append(f"U{ui+1:02d} slot {si+1} `{aid}` (skill_type=knowledge) forces `simulation: true` — unusual; confirm this is intentional")
        if st in ("skill", "both") and sim is False and gen:
            findings.append(f"U{ui+1:02d} slot {si+1} `{aid}` (skill_type={st}) has `simulation: false` — skill atom losing hands-on component")

    seen = {}
    for ui, si, aid, _ in ordered:
        if aid in seen:
            pui, psi = seen[aid]
            findings.append(f"U{ui+1:02d} slot {si+1} `{aid}` — **duplicate** (first appears U{pui+1:02d} slot {psi+1})")
        else:
            seen[aid] = (ui, si)

    for ui, unit in enumerate(units):
        ug = unit.get("unit_generate") or {}
        if not ug.get("summative_quiz", False):
            findings.append(f"U{ui+1:02d} `{unit.get('title','')}` has `summative_quiz: false` — unusual for a CTE unit")

    return {
        "code": code,
        "title": title,
        "unit_count": len(units),
        "slot_count": len(ordered),
        "total_minutes": total_minutes,
        "weeks": declared_weeks,
        "pacing": pacing_note,
        "findings": findings,
        "atoms": [a for _, _, a, _ in ordered],
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sub", default="it-support-services")
    p.add_argument("--state", default="texas")
    args = p.parse_args()

    cluster = CLUSTER_OF.get(args.sub)
    if not cluster:
        raise SystemExit(f"Unknown subcluster '{args.sub}'.")

    sub_dir = f"{BASE}/library/{cluster}/{args.sub}"
    atom_dir = f"{sub_dir}/atoms"
    tpl_dir = f"{sub_dir}/templates/{args.state}"
    out = f"{sub_dir}/crosswalks/{args.state}/sme-review.md"

    templates = []
    for fname in sorted(os.listdir(tpl_dir)):
        if not fname.endswith(".md") or fname.startswith("_"):
            continue
        meta = template_meta(os.path.join(tpl_dir, fname))
        templates.append((str(meta.get("course_code", "?")), fname, meta.get("course_name", "?")))

    reviews = [review_course(c, f, t, tpl_dir, atom_dir) for c, f, t in templates]

    lines = [
        f"# {args.sub} ({args.state}) — SME Review",
        "",
        "Automated first-pass review of course templates. Surfaces items a human",
        "SME (Maya) should confirm before promoting any template to `status: active`.",
        "Not every finding is a defect — some are intentional design choices that",
        "just need a sign-off.",
        "",
        "## How to read the findings",
        "",
        "**`prereq appears later`** — Real ordering bug within a course. Fix by",
        "reordering slots.",
        "",
        "**`prereq not in course`** — Usually expected cross-course coupling",
        "(prereq supplied by an earlier course in the pathway). Review only when",
        "the listed prereq wouldn't be covered elsewhere in the pathway.",
        "",
        "**`skill_type` / `simulation` mismatch** — Confirm intent. Deliberate",
        "overrides are fine; sloppy ones can degrade the lesson.",
        "",
    ]

    for r in reviews:
        lines += [
            f"## {r['code']} — {r['title']}",
            "",
            f"- Units: **{r['unit_count']}** — Slots: **{r['slot_count']}** — Weeks declared: **{r['weeks']}**",
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

    atom_to_courses = defaultdict(list)
    for r in reviews:
        for a in set(r["atoms"]):
            atom_to_courses[a].append(r["code"])
    shared = sorted(
        ((a, cs) for a, cs in atom_to_courses.items() if len(cs) > 1),
        key=lambda x: (-len(x[1]), x[0]),
    )
    lines += [
        "## Cross-course atom sharing",
        "",
        f"Total atoms used across the templates: **{len(atom_to_courses)}**.",
        f"Atoms shared by 2+ courses: **{len(shared)}**.",
        "",
    ]
    for a, cs in shared[:50]:
        lines.append(f"- `{a}` — in {', '.join(cs)}")
    if len(shared) > 50:
        lines.append(f"- ...and {len(shared) - 50} more")

    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write("\n".join(lines))
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
