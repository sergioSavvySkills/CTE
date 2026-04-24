# Crosswalks Schema

Maps course lessons to Texas TEKS standards. AI-generated draft, human-reviewed.

## Folder convention

```
library/health-science/
  crosswalks/
    texas/
      state-framework.csv     # ingested TEKS standards (source of truth)
      state-framework.md      # human-readable overview of the framework
      crosswalk.csv           # lesson → standard mappings
      coverage-report.md      # TEKS covered per course
      sme-review.md           # automated review findings
```

## state-framework.csv columns

| column | description |
|---|---|
| standard_code | TEKS code (e.g. 127.403-c1A) |
| course_name | official course name |
| course_code | state course code (e.g. 127.403) |
| grade_band | 9-10 / 11-12 / 9-12 |
| standard_text | verbatim standard text |
| framework_version | e.g. 2015 adopted; amended 4/7/2022 |
| notes | anything unusual |

## crosswalk.csv columns

| column | description |
|---|---|
| lesson_id | references a lesson within a course folder |
| state | two-letter state code |
| standard_code | references state-framework.csv |
| alignment_strength | primary / supporting / tangential |
| rationale | one sentence explaining the alignment |
| source | ai-draft / human-authored |
| reviewer | name or initials |
| review_date | ISO date |
| framework_version | state framework version reviewed against |

## Alignment strength definitions

- **primary** — this lesson is the main instructional carrier for the standard.
- **supporting** — this lesson reinforces the standard but another lesson is also needed.
- **tangential** — the lesson touches the standard but was not authored to cover it.

## Rules

- Crosswalks never change lesson content.
- Every AI-generated entry must have a human reviewer before use in a course template.
- One lesson may align to multiple standards; one standard may require multiple lessons.
- Re-review when states revise their frameworks.
