# Playbook: Texas Health Science — Course → Complete Templates

## Context

This playbook turns a Texas Health Science course (identified by TEKS code)
into a publishable course template with 100% TEKS coverage. The project is
organized course-first: each folder under `library/health-science/courses/`
corresponds to one TEKS course code.

End state of one pass: a course folder that feeds into shared atoms, credential
objective CSVs, a Texas state-framework + crosswalk, and a course template —
all wired so the automated reports (coverage, SME review, standards quality) pass.

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

## Phase 3 — Draft credential → TEKS crosswalk (AI)

**Goal:** Map each TEKS standard to one or more credential objectives.

1. AI drafts rows in `crosswalks/texas/crosswalk.csv` with header:
   `atom_id, state, standard_code, alignment_strength, rationale, source, reviewer, review_date, framework_version`.
   At this stage `atom_id` holds a credential objective key (e.g., `nha-ccma::1.1`);
   direct atom rows are added in Phase 6.
2. Expect 40–60% first-pass coverage; gaps closed later.

---

## Phase 4 — Author the atom library

**Goal:** Industry-neutral content units. Every anchor credential objective
gets at least one atom.

1. Plan atoms in batches (~10 per batch). Each batch lives in a JSON data
   file with one entry per atom: id, title, creds, skill_type, mins, diff,
   prereqs, obj, content[], assess[].
2. Run `python3 gen_atoms.py data_bN.json` to emit markdown files into
   `library/health-science/atoms/`.
   Update the `BASE` constant in `gen_atoms.py` to point at that folder.
3. Each atom: YAML frontmatter (atom_id, title, credential_objectives,
   skill_type, grade_band, estimated_minutes, difficulty, prerequisites,
   status) + Learning objective + Content stub + Assessment stub.
   See `library/_schemas/atom.md`.
4. Target ~100–150 atoms for the full Health Science pathway.

**Generator:** `gen_atoms.py` (repo root).

---

## Phase 5 — Course templates

**Goal:** Sequence atoms into units that map to each TEKS course code.

1. Read `library/_schemas/template.md` for the YAML shape.
2. For each TEKS course code, create one template at
   `library/health-science/templates/texas/<slug>.md`.
3. Frontmatter: `template_id, state, course_name, course_code,
   grade_band, credit_hours, credential_targets, framework_version, status: draft`.
4. Body `units:` block:
   - Group atoms into 8–12 units per 1-credit course (~18–20 instructional weeks).
   - Each slot: `{slot, atom_id}`. Default generators from `skill_type`.
   - 130.204 (2 credits): 16–20 units with simulation-heavy slots.
5. Pacing convention: **45-minute atoms** (standard Texas period length).

---

## Phase 6 — Close coverage gaps (iterative)

**Goal:** 100% TEKS coverage via slot → atom → credential → TEKS chain.

1. Update the three report scripts to point at `library/health-science/`:
   - `scripts/coverage_report.py`
   - `scripts/sme_review.py`
   - `scripts/standards_quality.py`
2. Run `python3 scripts/coverage_report.py`. Read
   `crosswalks/texas/coverage-report.md` for uncovered TEKS.
3. Fix gaps:
   - **Crosswalk gap:** add direct atom→TEKS row to `crosswalk.csv`.
   - **Template gap:** add missing atom to the appropriate unit/slot.
4. Loop until 100% on all course codes.

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
| Course templates | `library/health-science/templates/texas/<slug>.md` |
| Atoms | `library/health-science/atoms/<atom-id>.md` |
| Schemas | `library/_schemas/{atom,template,crosswalk}.md` |
| Reports | `library/health-science/crosswalks/texas/{coverage-report,sme-review}.md` |
| Generator | `gen_atoms.py` (repo root) |
| Report scripts | `scripts/{coverage_report,sme_review,standards_quality}.py` |

---

## Variants

- **Adding a second state:** skip Phase 4. Do Phases 2, 3, 5, 6, 7 only.
- **Adding a specialty course** (e.g., Dental Assisting 130.xxx): add the
  course folder, run all 7 phases. Reuse atoms from the shared `atoms/` folder
  where they overlap.
- **Authoring before state is chosen:** do Phases 1 and 4 only.

---

## Verification

1. `python3 scripts/coverage_report.py` — 100% TEKS per course code.
2. `python3 scripts/sme_review.py` — zero unresolved prereq violations.
3. `python3 scripts/standards_quality.py` — every TEKS has ≥1 primary-strength row.

After all three pass and Maya reviews a sample of crosswalk rows, promote
each template from `draft` to `active`.
