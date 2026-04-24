# Playbook: Texas Health Science — Course → Complete Templates

## Context

This playbook turns a Texas Health Science course (identified by TEKS code)
into a publishable course template with 100% TEKS coverage. The project is
organized course-first: each folder under `library/health-science/courses/`
corresponds to one TEKS course code.

End state of one pass: a course folder with a textbook chapter and workbook
page per TEKS standard, a Texas state-framework + crosswalk, and a course
template — all wired so the automated reports (coverage, SME review, standards
quality) pass.

---

## Prerequisites

- The course folder exists at `library/health-science/courses/<course-slug>/`
  with at minimum `_index.md` (scope, TEKS code, credit hours).
- Credentials are listed in `library/health-science/credentials/_index.csv`.

---

## Phase 1 — Credentials (the backbone)

**Goal:** Turn the credential list into per-credential objective files.

1. Read `library/health-science/credentials/_index.csv` to identify anchor
   credentials (1–3 per pathway). For Texas Health Science these are likely
   NHA CCMA, NHA CPT, and CPR/BLS (confirm against current Texas IBC list).
2. For each anchor credential, ingest its exam objectives:
   `library/health-science/credentials/<credential-id>.csv`
   with columns:
   `credential_id, domain_code, domain_name, domain_weight_pct, objective_code, objective_statement`.
   Source: vendor's official objectives PDF/URL listed in `_index.csv`.

---

## Phase 2 — Texas TEKS ingest

**Goal:** Capture the Texas Health Science TEKS in a machine-readable CSV.

1. Create folder: `library/health-science/crosswalks/texas/`.
2. Ingest the TEKS into `state-framework.csv` with header:
   `standard_code, course_name, course_code, grade_band, standard_text, framework_version, notes`.
   Source: TEA Chapter 130 Health Science Technology (19 TAC §130).
3. Write `state-framework.md` listing each course code, credit hours, TEKS count,
   and any legal requirements (e.g., co-requisite rules between 130.203 and 130.204).

**Output:** `crosswalks/texas/{state-framework.csv, state-framework.md}`.

---

## Phase 3 — Author lessons (one per TEKS standard)

**Goal:** A textbook chapter and workbook page for every TEKS expectation.

1. For each standard in `state-framework.csv`, create:
   - `courses/<course-slug>/textbook/<standard-slug>.md` — instructional content
   - `courses/<course-slug>/workbook/<standard-slug>.md` — student practice and assessment
2. Use the standard code as the lesson ID (e.g., `127.403-c1A`).
3. Each textbook chapter: learning objective, instructional content covering the
   standard, vocabulary, examples.
4. Each workbook page: practice questions, applied tasks, assessment items tied
   to the standard.

**Output:** `courses/<course-slug>/textbook/` and `courses/<course-slug>/workbook/`,
one file per TEKS expectation.

---

## Phase 4 — Draft lesson → TEKS crosswalk (AI)

**Goal:** Map each lesson to one or more TEKS standards.

1. AI drafts rows in `crosswalks/texas/crosswalk.csv` with header:
   `lesson_id, state, standard_code, alignment_strength, rationale, source, reviewer, review_date, framework_version`.
   `lesson_id` references a lesson within a course folder (e.g., `127.403-c1A`).
2. `alignment_strength`: `primary` / `supporting` / `tangential`.
3. Expect 40–60% first-pass coverage; gaps closed in Phase 6.

---

## Phase 5 — Course templates

**Goal:** Sequence lessons into units that map to each TEKS course code.

1. For each TEKS course code, create one template at
   `library/health-science/templates/texas/<slug>.md`.
2. Frontmatter: `template_id, state, course_name, course_code,
   grade_band, credit_hours, credential_targets, framework_version, status: draft`.
3. Body `units:` block — group lessons into 8–12 units per 1-credit course
   (~18–20 instructional weeks). Each slot: `{slot, lesson_id}`.
4. 130.204 (2 credits): 16–20 units.
5. Pacing convention: **45-minute periods** (standard Texas period length).

---

## Phase 6 — Close coverage gaps (iterative)

**Goal:** 100% TEKS coverage via lesson → crosswalk → standard chain.

1. Run `python3 scripts/coverage_report.py`. Read
   `crosswalks/texas/coverage-report.md` for uncovered TEKS.
2. Fix gaps:
   - **Crosswalk gap:** add `lesson_id → standard_code` row to `crosswalk.csv`.
   - **Template gap:** add missing lesson to the appropriate unit/slot.
3. Loop until 100% on all course codes.

---

## Phase 7 — SME review and quality pass

**Goal:** Catch pedagogical issues before Maya reviews.

1. Run `python3 scripts/sme_review.py` → `crosswalks/texas/sme-review.md`.
   Fix prereq violations and pacing issues.
2. Run `python3 scripts/standards_quality.py` → alignment-depth quality.
   Every TEKS should have at least one `primary`-strength row.

**Promotion criterion:** all three reports clean → flip each template
`status: draft` → `status: active` after Maya signs off.

---

## Critical Files

| Purpose | Path |
|---|---|
| Course scope | `library/health-science/courses/<course-slug>/_index.md` |
| Credential list | `library/health-science/credentials/_index.csv` |
| Per-credential objectives | `library/health-science/credentials/<cred>.csv` |
| Texas TEKS source | `library/health-science/crosswalks/texas/state-framework.csv` |
| Crosswalk | `library/health-science/crosswalks/texas/crosswalk.csv` |
| Lessons (textbook) | `library/health-science/courses/<course-slug>/textbook/<standard-slug>.md` |
| Lessons (workbook) | `library/health-science/courses/<course-slug>/workbook/<standard-slug>.md` |
| Course templates | `library/health-science/templates/texas/<slug>.md` |
| Schemas | `library/_schemas/crosswalk.md` |
| Reports | `library/health-science/crosswalks/texas/{coverage-report,sme-review}.md` |
| Report scripts | `scripts/{coverage_report,sme_review,standards_quality}.py` |

---

## Variants

- **Adding a second state:** Do Phases 2, 4, 5, 6, 7 only. Reuse lessons from
  `courses/<course-slug>/` where they already cover the new state's standards.
- **Adding a specialty course** (e.g., Dental Assisting 130.xxx): add the
  course folder, run all 7 phases.
- **Authoring before state is chosen:** do Phases 1 and 3 only.

---

## Verification

1. `python3 scripts/coverage_report.py` — 100% TEKS per course code.
2. `python3 scripts/sme_review.py` — zero unresolved prereq violations.
3. `python3 scripts/standards_quality.py` — every TEKS has ≥1 primary-strength row.

After all three pass and Maya reviews a sample of crosswalk rows, promote
each template from `draft` to `active`.
