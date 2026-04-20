# Course Templates — Texas Physical Health

**Status:** DRAFT — one template authored (Principles of Health Science).
Additional Subchapter I courses pending. Promote each template's
`status:` to `active` after the coverage report is clean and SME sign-off
is recorded.

## Published templates

| template_id | course_name | course_code | credit | credential_targets |
|---|---|:-:|:-:|---|
| `tx-principles-of-health-science-2022` | Principles of Health Science | 127.403 | 1 | — (L1 pre-credential) |

## Planned templates (not yet authored)

| course_name | course_code | credit | notes |
|---|---|:-:|---|
| Practicum in Health Science | 127.414 | 2 | Adopted 2015 |
| Health Science Theory | 127.422 | 1 | Adopted 2021 |
| Anatomy and Physiology | 127.423 | 1 | Adopted 2021 |
| Medical Assistant | 127.427 | 1 | Adopted 2021 |
| Medical Terminology | §127.4xx | 1 | Section TBD |
| Pharmacology | §127.4xx | 1 | Section TBD |
| Medical Microbiology | §127.4xx | 1 | Section TBD |
| Pathophysiology | §127.4xx | 1 | Section TBD |
| World Health Research | §127.4xx | 1 | Section TBD |
| Mathematics for Medical Professionals | §127.4xx | 1 | Section TBD |

Exact section numbers for the unbuilt courses will be confirmed via Cornell
LII / txrules.elaws.us when their crosswalks and templates are built.

## Pacing convention

Every atom is a **45-minute period**. Traditional-schedule teachers run
one atom per day; 4×4 or A/B block teachers combine two atoms into one
block day. This follows the Texas-common denominator between traditional
(~45 min) and block (~90 min) schedules.

## Course relationships

- **127.403 Principles of Health Science** is a stand-alone L1 survey for
  grades 9-10. It has no industry credential anchor and no corequisite.
- Higher-level courses (127.422 Theory, 127.423 A&P, 127.427 Medical
  Assistant, etc.) typically require PoHS or equivalent as prerequisite
  per local district practice, though not always per TAC.
- Subchapter I does not currently require a paired theory/lab split
  comparable to IT Support Services' 130.303/130.304 pairing.

## What counts as "lab" in this product

All lab content is generated digitally:

- `simulation: true` produces a self-contained HTML virtual lab.
  Clinical skill atoms (hand hygiene, PPE, body mechanics) use step-
  ordering interactives, demo videos, and scenario branching.
- `classwork: applied_task` produces an in-browser problem-solving brief.
- `classwork: discussion` drives asynchronous forum/branching-scenario
  prompts — used heavily in the Ethics/Law unit where student response
  and reasoning matter more than a correct key.

Physical equipment — cleanroom trays, manikins, BP cuffs, hospital beds —
is never a prerequisite for delivering this course.

## Dependency chain

```
library/healthcare-human-services/physical-health/
  crosswalks/texas/state-framework.csv      (ingested)
    → crosswalks/texas/crosswalk.csv        (AI draft + SME review)
      → crosswalks/texas/coverage-report.md (gaps → atom requests)
        → atoms/                            (atoms authored)
          → templates/texas/                (slots filled)   ← you are here
```

## Next steps for each template

1. Run the coverage report to verify every §127.4xx(c) statement maps to
   at least one slot in its matching template.
2. SME review pass on unit ordering and pacing.
3. Flip `status: draft` → `status: active` and tag the framework_version
   field with the TAC citation (e.g., "2015 adopted; amended 4/7/2022, 47
   TexReg 1677").

## Current SME sign-off

- `tx-principles-of-health-science-2022` — crosswalk and atoms
  **SME-approved round 3.1** (maya-delgado, 2026-04-20). Template itself
  remains `status: draft` until unit sequencing and performance-task
  placement are reviewed.
