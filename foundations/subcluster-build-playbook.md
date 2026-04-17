# Playbook: From Subcluster Name → Complete Lesson Templates

## Context

This is the process we followed to turn `it-support-services` (just a
name in the cluster taxonomy) into three publishable Texas CTE course
templates with 100% TEKS coverage. The playbook captures every step in
order, the tools used, and the key decisions. It's the reference for
repeating the build for any other subcluster — by itself, or with
multiple states stacked on top.

End state of one pass: a subcluster folder that contains a shared atom
library, credential objective CSVs, a state-framework + crosswalk, and
one course template per state course code — all wired so the automated
reports (coverage, SME review, standards quality) pass.

---

## Prerequisites

- The subcluster folder exists at `library/<cluster>/<subcluster>/`
  with at minimum `_index.md` (scope) and `credentials/_index.csv`
  (list of anchor credentials). Most subclusters already have these.
- A target state whose CTE standards we'll align to.

---

## Phase 1 — Credentials (the backbone)

**Goal:** Turn the list in `credentials/_index.csv` into individual
per-credential objective files that the crosswalk will reference.

1. Read `library/<cluster>/<subcluster>/_index.md` to internalize scope.
2. For each row in `credentials/_index.csv`, ingest that credential's
   exam objectives into a CSV:
   `library/<cluster>/<subcluster>/credentials/<credential-id>.csv`
   with columns:
   `credential_id, domain_code, domain_name, domain_weight_pct, objective_code, objective_statement`.
   Source of truth is the vendor's official objectives PDF/URL listed
   in `_index.csv`.
3. Decide **anchor credentials** (1–3 per subcluster) — the IBCs that
   will drive the atom library. For IT Support these were CompTIA
   ITF+, CompTIA A+ (Core 1 + Core 2), and Google IT Support.

**Reusable reference:** `library/digital-technology/it-support-services/credentials/` has the finished shape.

---

## Phase 2 — State framework ingest

**Goal:** Capture the state's CTE standards in a machine-readable CSV.

1. Create folder: `library/<cluster>/<subcluster>/crosswalks/<state>/`.
2. Ingest the state's standards into `state-framework.csv` with this
   exact header (see `library/_schemas/crosswalk.md`):
   `standard_code, course_name, course_code, grade_band, standard_text, framework_version, notes`.
   For Texas we got 154 TEKS rows across 3 course codes (130.302 /
   130.303 / 130.304).
3. Write a brief `state-framework.md` that lists each course code, its
   credit hours, the TEKS count, and any legal quirks (e.g., 19 TAC
   §130.304 requires 130.304 to run concurrent with 130.303).

**Output:** `crosswalks/<state>/{state-framework.csv, state-framework.md}`.

---

## Phase 3 — Draft credential → standard crosswalk (AI)

**Goal:** Map each state standard to one or more credential objectives
so the atom library we'll build inherits coverage automatically.

1. AI drafts rows in `crosswalks/<state>/crosswalk.csv` with header:
   `atom_id, state, standard_code, alignment_strength, rationale, source, reviewer, review_date, framework_version`.
   At this stage `atom_id` holds a credential objective key
   (e.g. `comptia-itf-plus::1.1`); atom rows are added in Phase 6.
2. Expect partial coverage — many state TEKS have no clean credential
   match (career exploration, soft skills, state-specific topics).
   That's fine; those gaps get closed later with direct atom→TEKS rows.

---

## Phase 4 — Author the atom library

**Goal:** Industry-neutral content units that any state can reuse.
Every anchor-credential objective gets at least one atom.

1. Plan atoms in batches (~10 per batch to avoid API timeout). Each
   batch lives in a JSON data file (`data_bN.json`) with one entry per
   atom: id, title, creds, skill_type, mins, diff, prereqs, obj,
   content[], assess[].
2. Run `python3 gen_atoms.py data_bN.json` to emit markdown files into
   `library/<cluster>/<subcluster>/atoms/`. `gen_atoms.py` is the
   reusable generator — update the `BASE` constant at the top to point
   at the target subcluster's atoms folder.
3. Each atom file has YAML frontmatter (atom_id, title, subcluster,
   credential_objectives, skill_type {knowledge|skill|both}, grade_band,
   estimated_minutes, difficulty, prerequisites, status) + Learning
   objective + Content stub + Assessment stub. See
   `library/_schemas/atom.md`.
4. Target ~100–150 atoms for a subcluster with 2–3 anchor credentials.

**Reusable generator:** `gen_atoms.py` (repo root).

---

## Phase 5 — Course templates

**Goal:** Sequence the atoms into units that map to each state course
code. Templates are recipes, not content.

1. Read `library/_schemas/template.md` for the YAML shape (frontmatter
   + a single ```yaml block in the body containing `units:`).
2. For each state course code, create one template file at
   `library/<cluster>/<subcluster>/templates/<state>/<slug>.md`.
3. Frontmatter: `template_id, state, course_name, course_code,
   subcluster, grade_band, credit_hours, credential_targets,
   framework_version, status: draft`.
4. Body `units:` block:
   - Group atoms into 8–12 units per 1-credit course (23-ish weeks of
     instruction leaves slack for assessments, games, performance tasks).
   - Each slot is `{slot, atom_id}`. Default generators come from
     `skill_type` (knowledge → lesson+guided_practice+exit_ticket; skill
     → +simulation+applied_task). Override per slot as needed.
   - Unit-level generators: `game, summative_quiz, performance_task`.
5. Pacing convention: **45-minute atoms**. Block-schedule teachers
   combine two per day; traditional teachers run one per day. This
   matches the Texas-common denominator.

**Reference templates (start by copying one):**
- `library/digital-technology/it-support-services/templates/texas/tx-principles-of-it-2025.md` (broad survey)
- `tx-computer-maintenance-2025.md` (theory deep-dive)
- `tx-computer-maintenance-lab-2025.md` (hands-on companion)

---

## Phase 6 — Close coverage gaps (iterative)

**Goal:** Get to 100% TEKS coverage through the slot → atom →
credential → state chain.

1. Re-point the three report scripts at the target subcluster +
   state. Each has a `SUB` constant and (for coverage/sme) a
   `TEMPLATES` dict listing course codes and filenames:
   - `scripts/coverage_report.py`
   - `scripts/sme_review.py`
   - `scripts/standards_quality.py`
   (Currently IT-Support-hardcoded — parameterizing these via CLI args
   is a near-term cleanup opportunity.)
2. Run `python3 scripts/coverage_report.py`. Read
   `crosswalks/<state>/coverage-report.md` for uncovered TEKS.
3. Uncovered TEKS fall into two buckets:
   - **Crosswalk gap** (atom clearly covers it but crosswalk doesn't
     say so) → add a direct atom→TEKS row to `crosswalk.csv`. Use
     `scripts/expand_crosswalk.py` as the pattern (copy → edit the
     `ROWS` list for the new subcluster → run it once).
   - **Template gap** (no atom in the course covers it) → add the
     missing atom to the appropriate unit/slot in the template.
4. Loop until coverage hits 100% on all course codes.

**Expected first-pass number:** 40–60% coverage from the
credential-only chain, 100% after ~80 direct atom→TEKS rows + a
handful of template additions.

---

## Phase 7 — SME review and quality pass

**Goal:** Catch pedagogical issues before Maya gets the draft.

1. Run `python3 scripts/sme_review.py`. Produces
   `crosswalks/<state>/sme-review.md` flagging:
   - Prerequisite violations inside a course
   - Pacing realism (minutes vs. weeks declared)
   - Skill-type / generator mismatches
   - Duplicate atoms, weak unit-level generator choices
   - Cross-course atom sharing patterns
2. Fix every "prereq appears later in the same course" finding by
   reordering slots. "Prereq not in course" findings that are
   cross-course couplings (co-requisite) can be tolerated.
3. Run `python3 scripts/standards_quality.py` for alignment-depth
   quality: primary vs. supporting ratio, thin (single-atom) TEKS,
   orphan atoms, ai-draft vs. reviewed ratio. Fix obvious weaknesses
   before handing to Maya.

**Promotion criterion:** all three reports look clean → flip each
template's `status: draft` → `status: active`, set `reviewer` and
`review_date` after Maya signs off on `crosswalk.csv`.

---

## Critical files the playbook touches

| Purpose | Path |
|---|---|
| Cluster/subcluster scope | `library/<cluster>/<subcluster>/_index.md` |
| Anchor credential list | `library/<cluster>/<subcluster>/credentials/_index.csv` |
| Per-credential objectives | `library/<cluster>/<subcluster>/credentials/<cred>.csv` |
| State standards source | `library/<cluster>/<subcluster>/crosswalks/<state>/state-framework.csv` |
| Atom→TEKS crosswalk | `library/<cluster>/<subcluster>/crosswalks/<state>/crosswalk.csv` |
| Course templates | `library/<cluster>/<subcluster>/templates/<state>/<slug>.md` |
| Schemas | `library/_schemas/{atom,template,crosswalk}.md` |
| Reports | `library/<cluster>/<subcluster>/crosswalks/<state>/{coverage-report,sme-review}.md` |
| Generator | `gen_atoms.py` (repo root) |
| Report scripts | `scripts/{coverage_report,sme_review,standards_quality,expand_crosswalk}.py` |

---

## Variants

- **Adding another state to an existing subcluster** (atoms reused):
  skip Phase 4. Do Phases 2, 3, 5, 6, 7 only.
- **Adding another subcluster same state** (state framework already
  loaded for some other subcluster): still do everything — state TEKS
  are per-course-code so another subcluster will have different TEKS.
- **Authoring before state is chosen**: do Phases 1 and 4 only. Atoms
  are state-neutral; states can be layered on later.

---

## Verification

A successful build passes all three of these:

1. `python3 scripts/coverage_report.py` — 100% TEKS covered per course
   in the target state.
2. `python3 scripts/sme_review.py` — zero "prereq appears later in the
   same course" findings; remaining findings are documented as design
   intent or cross-course coupling.
3. `python3 scripts/standards_quality.py` — every TEKS has at least
   one `primary`-strength row; `Rev` column (reviewed rows) grows as
   Maya signs off.

After all three pass and Maya has reviewed a sample of crosswalk rows,
promote each template from `draft` to `active`.

---

## Open follow-ups for future passes (not part of this playbook)

- Parameterize the report scripts with `--subcluster` and `--state`
  CLI args so a second subcluster doesn't require editing hardcoded
  paths.
- Generalize `expand_crosswalk.py` to read its row list from JSON
  instead of Python source.
- Add a one-shot `scripts/new_state.sh <cluster> <sub> <state>` that
  scaffolds the empty crosswalks/<state>/ folder and drops the three
  scripts' config for that target.
