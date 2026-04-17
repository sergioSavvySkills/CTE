# Georgia Artificial Intelligence CTAE Pathway — Framework Reference

Georgia was the first U.S. state to adopt a dedicated secondary CTE
pathway for Artificial Intelligence. The pathway sits inside the
**Information Technology Career Cluster** and comprises three
sequential one-Carnegie-unit (1 credit) courses adopted March 4, 2021
by the Georgia Department of Education.

## Pathway courses

| # | Course Code | Course Name | Standards (leaves) | Prereq |
|---|---|---|---:|---|
| 1 | 11.44300 | Foundations of Artificial Intelligence | 57 | none |
| 2 | 11.44400 | Artificial Intelligence Concepts | 55 | 11.44300 |
| 3 | 11.44500 | Artificial Intelligence Applications | 41 | 11.44300 + 11.44400 |

Total: **153 leaf-level performance standards** across 25 parent
standards. Each course is 1 Carnegie unit (approx. 120–140 contact
hours / one school year). Grade band HS (9–12).

## Standard code structure

Georgia uses a three-letter course prefix and dotted decimal numbering:

- `IT-FAI-X.Y` — Foundations of AI (Course 1)
- `IT-AIC-X.Y` — AI Concepts (Course 2)
- `IT-AIA-X.Y` — AI Applications (Course 3)

Parent standards (e.g., `IT-FAI-4`) are topic buckets; the leaf
standards (`IT-FAI-4.1` … `IT-FAI-4.13`) are what the crosswalk and
coverage reports align to. The framework CSV stores only the leaves,
matching the convention we used for Texas TEKS `(c)(n)(A)` sub-element
rows.

## Common-to-all-courses standards

Every CTAE course in Georgia includes two boilerplate standards:

- `IT-***-1.*` (6 sub-elements) — **Employability skills** (written/
  verbal communication, creativity, critical thinking, work readiness
  traits, teamwork, professional image). Text is verbatim-identical
  across all three AI courses; only the code prefix changes.
- `IT-***-8.*` or `IT-***-9.*` (5 sub-elements) — **CTSO
  participation** (career-technical student organizations — for IT
  this is FBLA / TSA). Same verbatim text across all three courses.

These 11 standards × 3 courses = 33 rows of generic CTAE foundation
content. When building atoms, a single set of "CTAE foundations"
atoms can crosswalk to all nine copies.

## AI-specific subject matter (Course 1 — Foundations)

Parent standards 2–8 in `11.44300`:

- IT-FAI-2 — History and evolution of AI (4 leaves)
- IT-FAI-3 — Current AI applications (6 leaves)
- IT-FAI-4 — Algorithms and intro programming (13 leaves; heaviest)
- IT-FAI-5 — Data fundamentals and data-processing cycle (8 leaves)
- IT-FAI-6 — Spreadsheet-based data analysis (4 leaves)
- IT-FAI-7 — AI ethics, bias, privacy (6 leaves)
- IT-FAI-8 — Collaboration + Design Thinking (5 leaves)

## AI-specific subject matter (Course 2 — Concepts)

Parent standards 2–7 in `11.44400`:

- IT-AIC-2 — Historical & current AI developments (4 leaves)
- IT-AIC-3 — Classify supervised / unsupervised / reinforcement
  learning; train & evaluate ML models (6 leaves)
- IT-AIC-4 — Object-oriented programming for AI (16 leaves; heaviest)
- IT-AIC-5 — Data science, databases, data visualization, statistics
  (9 leaves)
- IT-AIC-6 — Ethics, bias, AI law / policy (6 leaves)
- IT-AIC-7 — Apply Design Thinking to AI problems (3 leaves)

## AI-specific subject matter (Course 3 — Applications)

Parent standards 2–7 in `11.44500`:

- IT-AIA-2 — Current AI developments, non-ML AI (3 leaves)
- IT-AIA-3 — AI dev tools: open-source and proprietary (4 leaves)
- IT-AIA-4 — Agile team development, IDEs, build & train ML models,
  portfolio (6 leaves)
- IT-AIA-5 — Datasets, training/validation/test split, Pandas, bias
  in data (9 leaves)
- IT-AIA-6 — Community problem-solving with AI + prototype (4 leaves)
- IT-AIA-7 — **Embedded AI / robotics** — circuits, sensors,
  microcontrollers, write code for a sensor-driven robot (4 leaves)
- End-of-pathway assessment is expected after mastery of this course.

## Academic standards integration

All three courses formally cross-reference the Georgia Standards of
Excellence ELA/Literacy standards for technical subjects:
**L9-10RST 1-10** (reading) and **L9-10WHST 1-10** (writing). These
are inherited standards, not additional rows in our framework CSV —
teachers integrate them through course activities.

## Recommended companion courses (from pathway sheet)

- Any Advanced Math course
- Any Business and Computer Science course
- Any Engineering course
- Any World Language

Not pathway-required, but strengthen the endorsement application.

## Source documents

Authoritative PDFs (Georgia Department of Education, mirrored at
ai4k12.org):

- Pathway overview: https://ai4k12.org/wp-content/uploads/artificialintelligencepathway.pdf
- Foundations of AI (11.44300): https://ai4k12.org/wp-content/uploads/Foundations-of-Artificial-Intelligence.pdf
- AI Concepts (11.44400): https://ai4k12.org/wp-content/uploads/Artificial-Intelligence-Concepts.pdf
- AI Applications (11.44500): https://ai4k12.org/wp-content/uploads/Artificial-Intelligence-Applications.pdf
- Pathway summary: https://ai4k12.org/georgias-ai-ctae-frameworks/
- GaDOE CTAE landing: https://gadoe.org/ctae/

`framework_version` in the CSV is set to `2021-03-04`, the adoption
date printed on each document. If Georgia revises these standards,
bump the version and re-run the coverage/SME reports.

## Known gaps in credential coverage (predicted for Phase 3)

Based on the subject matter above, we expect these standards families
will **not** map cleanly to our four anchor credentials (CompTIA
Data+, Certiport ITS Data Analytics, Certiport ITS AI, MS AI-900):

- IT-FAI-1 / IT-AIC-1 / IT-AIA-1 (employability) — generic CTAE
- IT-FAI-9 / IT-AIC-8 / IT-AIA-8 (CTSO) — generic CTAE
- IT-FAI-8 / IT-AIC-7 (Design Thinking) — not a credential topic
- IT-AIA-4.1 (Agile + GitHub) — none of our anchors cover SDLC
- IT-AIA-4.6 (online portfolio) — career-readiness, not credential
- IT-AIA-6.1–6.4 (community problem + prototype) — project-based,
  no credential analog
- IT-AIA-7.1–7.4 (embedded / robotics) — **unique to Georgia**; not
  covered by any anchor credential. Will require atoms authored
  fresh, or a supplementary credential (Arduino/Raspberry Pi
  certifications — not on Georgia's recommended cert list).

These gaps close via direct atom → standard crosswalk rows in
Step 6 of the plan.
