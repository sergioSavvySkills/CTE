# Course Templates — Texas IT Support & Services

**Status:** DRAFT — three templates authored and awaiting Maya/SME review.
Promote each template's `status:` field to `active` after the coverage
report is clean.

## Published templates

| template_id | course_name | course_code | credit | credential_targets |
|---|---|:-:|:-:|---|
| `tx-principles-of-it-2025` | Principles of Information Technology | 130.302 | 1 | CompTIA ITF+ |
| `tx-computer-maintenance-2025` | Computer Maintenance | 130.303 | 1 | CompTIA A+ Core 1 |
| `tx-computer-maintenance-lab-2025` | Computer Maintenance Lab | 130.304 | 1 | CompTIA A+ Core 1 |

## Pacing convention

Every atom is a **45-minute period**. Traditional-schedule teachers run
one atom per day; 4×4 or A/B block teachers combine two atoms into one
block day. This choice follows the Texas-common denominator between
traditional (~45 min) and block (~90 min) schedules documented by TEA.

## Course relationships

- **130.302 Principles of IT** is a stand-alone survey course (grades 9–10).
- **130.303 Computer Maintenance** and **130.304 Computer Maintenance Lab**
  must be taken **concurrently** per 19 TAC §130.304. The theory template
  (130.303) provides lessons/videos/quizzes; the Lab template (130.304)
  provides simulations/virtual labs/applied tasks — both drawing from
  the same IT Support atom library.

## What counts as "lab" in our product

All lab content is generated digitally:

- `simulation: true` produces a self-contained HTML virtual lab.
- `classwork: applied_task` produces a problem-solving brief students
  complete in-browser.
- Operating-system installation, CLI work, and network configuration
  run in browser-based VMs or simulators.

Teachers with physical hardware can supplement, but no school needs a
workbench, test bench, or spare-parts budget to deliver these courses.

## Dependency chain

```
library/digital-technology/it-support-services/
  crosswalks/texas/state-framework.csv (ingested)
    → crosswalks/texas/crosswalk.csv (AI draft + Maya review)
      → crosswalks/texas/coverage-report.md (gaps → atom requests)
        → atoms/ (atoms authored)
          → templates/texas/ (slots filled) ← you are here
```

## Next steps for each template

1. Run the coverage report to verify every TEKS maps to at least one
   slot in its matching template.
2. SME review pass on unit ordering and pacing.
3. Flip `status: draft` → `status: active` and tag a framework version.
