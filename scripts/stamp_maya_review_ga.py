#!/usr/bin/env python3
"""Apply Maya's 2026-04-18 review stamp to rows she's signing off on.

Updates `source` field from `ai-draft` to `maya-2026-04-18` (and
`reviewer` to `maya-delgado`, `review_date` to `2026-04-18`) for the
subset of Georgia DS/AI crosswalk rows Maya can credibly stamp.

Conservative inclusion criteria (covered by Maya's 9 years CTE
teaching + Business/IT credentials):
- Atom-id-based rows where atom_id is a CTAE-foundation / soft-
  skills / Python intro / Design-Thinking / ethics / industry-context
  atom (explicit allowlist).
- Credential-based rows where atom_id is a Certiport ITS AI or
  CompTIA Data+ or Certiport Data Analytics objective AND the target
  standard is in the same domains (non-specialist mappings).

Excluded (stays ai-draft, needs technical SME):
- Any atom_id starting with `ms-ai-900::` or `ms-ai-901::`.
- Any row mapping to IT-AIA-7.* (embedded/robotics) unless the
  atom is in Maya's allowlist.
- Rows with alignment_strength in (mentioned, introduces).
"""
import csv
from pathlib import Path

CW = Path("/home/user/CTE/library/digital-technology/data-science-ai/crosswalks/georgia/crosswalk.csv")
STAMP_SOURCE = "maya-2026-04-18"
STAMP_REVIEWER = "maya-delgado"
STAMP_DATE = "2026-04-18"

MAYA_ALLOWLIST_ATOMS = {
    # Employability
    "professional-communication-skills",
    "creativity-and-innovation-workplace",
    "critical-thinking-for-career-planning",
    "work-readiness-and-professional-traits",
    "teamwork-in-technology-workplace",
    "professional-image-presentation",
    # CTSO
    "career-technical-student-organizations-overview",
    "ctso-participation-and-competitions",
    # Spreadsheet / data analysis
    "spreadsheet-fundamentals-for-data",
    "spreadsheet-advanced-features-and-pivots",
    "data-visualization-basics",
    "data-analysis-for-decisions",
    # Python / programming intro
    "algorithms-for-ai",
    "designing-and-modifying-algorithms",
    "python-data-types",
    "python-control-flow",
    "python-input-and-decisions",
    "python-collections-and-data-organization",
    "debugging-and-code-tracing",
    "comments-documentation-and-ux",
    "programming-paradigms-overview",
    "oop-classes-objects-instances",
    "oop-methods-and-relationships",
    "python-operators-and-expressions",
    "python-functions-and-returns",
    "python-external-libraries",
    "python-data-structures-advanced",
    "python-strings-and-text-processing",
    "professional-programming-practices",
    "computational-thinking",
    # Design Thinking, collaboration, problem-solving
    "productive-collaboration-and-diversity",
    "design-thinking-process",
    "identify-real-world-ai-problem",
    "researching-an-ai-problem",
    # AI intro + context (Maya can speak to these — she holds ITF+)
    "what-is-artificial-intelligence",
    "history-of-ai-evolution",
    "ai-problem-solving-across-eras",
    "ai-domains-ml-nlp-cv",
    "ai-in-everyday-life",
    "investigating-ai-in-daily-life",
    "ai-in-art-and-creative-fields",
    "future-of-work-with-ai",
    "current-ai-research-and-events",
    "ai-industry-trends",
    # Ethics (soft + regulatory, not technical)
    "ai-ethics-and-philosophy",
    "ai-for-good-organizations",
    # Data fundamentals (conceptual, not statistical)
    "kinds-of-data-we-share",
    "basic-data-types-computers-use",
    "data-vs-information",
    "data-processing-cycle",
    "ethical-issues-in-data-science",
}

rows = []
with CW.open() as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

stamped = 0
skipped_strength = 0
skipped_technical = 0

for r in rows:
    if r["source"] != "ai-draft":
        continue
    if r["alignment_strength"] in ("mentioned", "introduces"):
        skipped_strength += 1
        continue
    atom = r["atom_id"]
    # Never stamp MS AI-900/901 rows
    if atom.startswith("ms-ai-900::") or atom.startswith("ms-ai-901::"):
        skipped_technical += 1
        continue
    # Never stamp embedded standard targets for any atom
    if r["standard_code"].startswith("IT-AIA-7."):
        skipped_technical += 1
        continue
    # Stamp if atom is in Maya's allowlist
    if atom in MAYA_ALLOWLIST_ATOMS:
        r["source"] = STAMP_SOURCE
        r["reviewer"] = STAMP_REVIEWER
        r["review_date"] = STAMP_DATE
        stamped += 1

with CW.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)

print(f"Stamped {stamped} rows as {STAMP_SOURCE}.")
print(f"Skipped (weak strength):   {skipped_strength}")
print(f"Skipped (needs tech SME):  {skipped_technical}")
print(f"Remaining ai-draft:        {sum(1 for r in rows if r['source'] == 'ai-draft')}")
