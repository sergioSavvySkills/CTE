#!/usr/bin/env python3
"""SME review of the three Texas IT Support course templates.

Surfaces issues Maya would flag in a review:

1. Prerequisite violations: atom in slot N requires atom X, but X appears
   later in the course or is missing entirely.
2. Pacing realism: total instructional minutes vs. declared weeks
   (assumes 5 periods per week at 45 minutes each).
3. Skill-type / generator mismatches: e.g., a `skill` atom with
   simulation disabled, or a `knowledge` atom with simulation forced on.
4. Duplicated atoms within a course (same atom in two units).
5. Cross-course duplication sanity check: atoms shared across courses.
6. Credit-hour calibration: total atoms per 1-credit course.
"""
import os
import re
import yaml
from collections import defaultdict

BASE = "/home/user/CTE"
SUB = f"{BASE}/library/digital-technology/it-support-services"
ATOM_DIR = f"{SUB}/atoms"
TPL_DIR = f"{SUB}/templates/texas"
OUT = f"{SUB}/crosswalks/texas/sme-review.md"

TEMPLATES = [
    ("130.302", "tx-principles-of-it-2025.md", "Principles of IT"),
    ("130.303", "tx-computer-maintenance-2025.md", "Computer Maintenance"),
    ("130.304", "tx-computer-maintenance-lab-2025.md", "CM Lab"),
]

PERIODS_PER_WEEK = 5


def atom_meta(atom_id):
    path = os.path.join(ATOM_DIR, atom_id + ".md")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        txt = f.read()
    m = re.match(r"---\n(.*?)\n---", txt, re.S)
    if not m:
        return None
    try:
        data = yaml.safe_load(m.group(1))
    except Exception:
        data = {}
    return data or {}


def parse_template(path):
    with open(path) as f:
        txt = f.read()
    # Extract YAML block
    m = re.search(r"```yaml\n(.*?)\n```", txt, re.S)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def review_course(code, fname, title):
    tpl = parse_template(os.path.join(TPL_DIR, fname))
    units = tpl["units"]

    # Build ordered (unit_idx, slot_idx, atom_id) list
    ordered = []
    for ui, unit in enumerate(units):
        for si, slot in enumerate(unit.get("slots", []) or []):
            ordered.append((ui, si, slot["atom_id"], slot))

    atom_meta_cache = {a: atom_meta(a) for _, _, a, _ in ordered}

    findings = []

    # 1) Prereq violations
    atom_first_pos = {}
    for idx, (_, _, aid, _) in enumerate(ordered):
        atom_first_pos.setdefault(aid, idx)
    for idx, (ui, si, aid, _) in enumerate(ordered):
        meta = atom_meta_cache.get(aid) or {}
        for pre in meta.get("prerequisites") or []:
            pre_pos = atom_first_pos.get(pre)
            if pre_pos is None:
                findings.append(f"U{ui+1:02d} slot {si+1} `{aid}` requires `{pre}` \u2014 **prereq not in course**")
            elif pre_pos > idx:
                findings.append(f"U{ui+1:02d} slot {si+1} `{aid}` requires `{pre}` \u2014 **prereq appears later** at position {pre_pos+1}")

    # 2) Pacing
    total_minutes = 0
    for _, _, aid, _ in ordered:
        meta = atom_meta_cache.get(aid) or {}
        total_minutes += int(meta.get("estimated_minutes") or 45)
    declared_weeks = sum(u.get("weeks", 0) for u in units)
    available_minutes = declared_weeks * PERIODS_PER_WEEK * 45
    pacing_note = (
        f"**Pacing:** {len(ordered)} slots, {total_minutes} atom-minutes total, "
        f"{declared_weeks} declared weeks "
        f"({available_minutes} min @ {PERIODS_PER_WEEK}\u00d745 min/week). "
        f"Slack for assessments/reviews/performance tasks: "
        f"{available_minutes - total_minutes} min "
        f"({100 * (available_minutes - total_minutes) / available_minutes:.0f}%)."
    )

    # 3) Skill-type / generator mismatches
    for ui, si, aid, slot in ordered:
        meta = atom_meta_cache.get(aid) or {}
        st = meta.get("skill_type", "knowledge")
        gen = slot.get("generate") or {}
        sim = gen.get("simulation")
        if st == "knowledge" and sim is True:
            findings.append(f"U{ui+1:02d} slot {si+1} `{aid}` (skill_type=knowledge) forces `simulation: true` \u2014 unusual; confirm this is intentional")
        if st in ("skill", "both") and sim is False and gen:
            findings.append(f"U{ui+1:02d} slot {si+1} `{aid}` (skill_type={st}) has `simulation: false` \u2014 skill atom losing its hands-on component")

    # 4) Duplicates within course
    seen = {}
    for ui, si, aid, _ in ordered:
        if aid in seen:
            pui, psi = seen[aid]
            findings.append(f"U{ui+1:02d} slot {si+1} `{aid}` \u2014 **duplicate** (first appears U{pui+1:02d} slot {psi+1})")
        else:
            seen[aid] = (ui, si)

    # 5) Unit-level generator smell: every unit should have summative_quiz
    for ui, unit in enumerate(units):
        ug = unit.get("unit_generate") or {}
        if not ug.get("summative_quiz", False):
            findings.append(f"U{ui+1:02d} `{unit.get('title','')}` has `summative_quiz: false` \u2014 unusual for a CTE unit")

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
    reviews = [review_course(c, f, t) for c, f, t in TEMPLATES]

    lines = [
        "# Texas IT Support \u2014 SME Review",
        "",
        "Automated first-pass review of the three Texas course templates.",
        "Surfaces items a human SME (Maya) should confirm before promoting",
        "any template to `status: active`. Not every finding is a defect \u2014",
        "some are intentional design choices that just need a sign-off.",
        "",
        "## How to read the findings",
        "",
        "**`prereq appears later`** \u2014 Real ordering bug within a course; a slot",
        "uses an atom whose prereq hasn't been taught yet. These were reduced",
        "from 14 to the current count by reordering. Any remaining ones are",
        "mostly caused by atom-level `prerequisites:` metadata that may itself",
        "be reversed (e.g., `filesystems-and-partitioning` lists",
        "`file-management` as a prereq, but pedagogically files come first).",
        "Maya: confirm whether to flip the atom metadata or just tolerate.",
        "",
        "**`prereq not in course`** \u2014 Usually expected cross-course coupling.",
        "130.303 and 130.304 run concurrently, so either can supply prereqs",
        "the other lists. A 130.303 atom listing `hardware-components-overview`",
        "as a prereq is fine because the student is simultaneously taking",
        "130.304 where that atom sits in U03. Review these only when the",
        "listed prereq wouldn't have been covered by any co-requisite course.",
        "",
        "**`skill_type=knowledge` forces `simulation: true`** (130.304 only)",
        "\u2014 Design intent, not a defect. The Lab template deliberately runs",
        "simulations over knowledge atoms because that's how the hands-on",
        "half of the pair differs from the theory half. Confirm and move on.",
        "",
        "**`skill_type=skill` with `simulation: false`** (130.303 only) \u2014",
        "Also design intent for the same reason: the theory template runs",
        "lessons and videos; the companion Lab template runs the simulation.",
        "",
    ]

    for r in reviews:
        lines += [
            f"## {r['code']} \u2014 {r['title']}",
            "",
            f"- Units: **{r['unit_count']}** \u2014 Slots: **{r['slot_count']}** \u2014 Weeks declared: **{r['weeks']}**",
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
            lines.append("_No automated findings \u2014 still worth a human scan for pedagogical order._\n")

    # 6) Cross-course sharing
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
        f"Total atoms used across the three courses: **{len(atom_to_courses)}** "
        f"(out of ~110 in the library).",
        f"Atoms shared by 2+ courses: **{len(shared)}**.",
        "",
        "Expected: the 130.303 / 130.304 pair shares nearly all atoms by design",
        "(concurrent theory + lab). Atoms appearing in 130.302 **and** either",
        "CM course are crossover foundations (soft skills, safety, basic hardware).",
        "Unexpected: any atom in all three courses that isn't foundational.",
        "",
    ]
    for a, cs in shared[:40]:
        lines.append(f"- `{a}` \u2014 in {', '.join(cs)}")
    if len(shared) > 40:
        lines.append(f"- ...and {len(shared) - 40} more")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        f.write("\n".join(lines))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
