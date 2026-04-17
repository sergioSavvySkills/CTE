# Crosswalks — Layer 2 Schema

Maps content atoms to state CTE standards. This layer is AI-generated
and human-reviewed. It never changes atom content.

## Folder convention

```
crosswalks/
  <state>/
    <subcluster>/
      state-framework.csv     # ingested state standards (source of truth)
      state-framework.md      # human-readable overview of the framework
      crosswalk.csv           # atom → standard mappings (draft + reviewed)
      coverage-report.md      # standards with no primary-strength atom
```

## state-framework.csv columns

| column | description |
|---|---|
| standard_code | state-assigned code (e.g. TX-IT-C1-S1) |
| course_name | official course name this standard belongs to |
| course_code | state course code |
| grade_band | HS / PS / Both |
| standard_text | verbatim standard text from state framework |
| framework_version | e.g. 2024-25 |
| notes | anything unusual about this standard |

## crosswalk.csv columns

| column | description |
|---|---|
| atom_id | references library/atoms/<subcluster>/<atom>.md |
| state | two-letter state code |
| standard_code | references state-framework.csv |
| alignment_strength | primary / supporting / tangential |
| rationale | one sentence explaining why this atom covers this standard |
| source | ai-draft / human-authored |
| reviewer | name or initials of human reviewer |
| review_date | ISO date |
| framework_version | state framework version this was reviewed against |

## Alignment strength definitions

- **primary** — this atom is the main instructional carrier for the standard.
  A student who masters this atom can demonstrate the standard.
- **supporting** — this atom reinforces the standard but a second atom
  is also needed for full coverage.
- **tangential** — the atom touches the standard but was not authored
  to cover it.

## Rules (from content-platform.md)

- Crosswalks never change atom content.
- Every AI-generated entry must have a human reviewer before it is
  used in a course template.
- One atom may align to multiple standards; one standard may require
  multiple atoms.
- Versioned per state framework version — re-review when states revise.
