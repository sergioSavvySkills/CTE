# Maya's Review — Data Science & AI / Georgia (2026-04-18)

First review pass on the Georgia DS/AI build (subcluster:
`data-science-ai`, state: Georgia CTAE 11.44300 / 11.44400 /
11.44500). Reviewed the three templates, the crosswalk, a sample of
atoms across content areas, and the three automated gate reports.

TL;DR: **Conditional approval.** Strong foundation. Three pedagogical
issues required fixes before I'm comfortable promoting anything to
`active`. **81 crosswalk rows stamped `maya-2026-04-18`** this pass;
294 still `ai-draft` (breakdown below). Templates stay at
`status: draft` pending Teacher Advisory Panel feedback.

After my fixes + stamping pass, coverage remains 100% / 100% / 100%
(Foundations / Concepts / Applications) and the three reviewed-row
counts (Rev column in the quality report) are **35 / 31 / 12**
standards per course with at least one Maya-signed row.

## What's good (keeping it short)

- **Atom-per-period pacing is realistic.** 45 minutes, one concept,
  one activity, one assessment. Matches how a real teacher plans.
- **Free tools first.** Teachable Machine, Google Colab, Hugging Face
  Spaces. Every one of these works on a Chromebook and doesn't need
  district procurement. That's the difference between a curriculum
  that gets adopted and one that sits on a shelf.
- **Ethics threaded, not bolted on.** `exploring-bias-with-teachable-
  machine` appears in the same unit as hands-on ML training — not
  quarantined into a one-week "responsible AI" unit at the end. This
  is how you actually teach it.
- **Design Thinking shows up in Foundations, not just the capstone.**
  Students get the vocabulary early; they use it later. Correct.
- **Standard 1 (employability) and Standard 9/8 (CTSO) atoms are
  fully aligned.** These are the boilerplate standards every CTAE
  course gets graded on — easy to half-ass. Not half-assed here.

## What needed fixing before sign-off

### 1. Foundations u04 was a ghost town (FIXED THIS PASS)

**Finding:** `u04 Training Your First AI Model` had 2 atoms across 2
declared weeks = 90 minutes of content for 10 class periods. That's
a 82% slack unit. No unit should be that hollow, and the one time in
the course students actually build something gets the least time.

**Fix applied:** Added three slots to u04 so students do the ML
training experience in depth rather than as a drive-by:
- `how-ai-uses-data-for-predictions` (moved back; its prereq
  `data-vs-information` now lives in u03 via reorder below)
- Performance-task time folded in explicitly

### 2. Foundations u03 and u06 prereq chain was backwards

**Finding:** `data-vs-information` (u06 slot 3) is the prereq for
`how-ai-uses-data-for-predictions` but the ML training unit (u04)
wanted to use it before u06. The automated SME check caught this and
the fix was to move `how-ai-uses-data-for-predictions` to u06. But
the real issue is pedagogical sequencing: **data fundamentals belong
before ML**, not after. Kids can't reason about what a model is
learning without knowing what data is.

**Fix applied:** Moved `data-vs-information` into u03 and restored a
proper u04 ML-training unit with `how-ai-uses-data-for-predictions`
where it belongs.

### 3. Applications u08 was cramming three terminal events into 2 weeks

**Finding:** `u08 Portfolio, CTSO, and End-of-Pathway Assessment` is
3 atoms, 2 weeks. The **End-of-Pathway Assessment** is a real
external exam in Georgia CTAE and the pathway's primary ROI signal.
Pairing it with portfolio polish and CTSO wrap-up means students
either skimp review or skimp portfolio. Both are consequential.

**Fix applied:** Split u08 into u08 (Portfolio + CTSO, 2 weeks) and
u09 (End-of-Pathway Assessment Review, 2 weeks). Pathway pacing
shifts from 19 declared weeks to 21 — still inside the ~23-week
Georgia school year with slack for mid-term disruption.

## Issues I'm flagging, not fixing this pass

### A. Embedded atoms have no credential chain

Four atoms in the IT-AIA-7 family (`embedded-systems-and-sensors`,
`building-an-embedded-robot`, `programming-a-sensor-driven-robot`,
`debugging-hardware-issues`) have `credential_objectives: []`.
Coverage is fine — direct atom→standard rows handle it — but there's
no portability to states that require credential alignment. Before
targeting Texas or Florida, find a credential for this family
(Arduino Certified Educator is the cheapest option; Raspberry Pi
Foundation certs exist but aren't widely recognized).

**Owner:** Sergio. Credential decision, not pedagogy.

### B. MS AI-900 is retiring June 30, 2026

AI-900 is listed as a `credential_target` on the Concepts and
Applications templates. Students starting fall 2025 will sit a
retiring exam. AI-901 (the successor) is already ingested in our
credentials folder but the crosswalk doesn't reference it, and
templates don't list it.

**Action:** Before fall 2026 cohort enrolls, do a second crosswalk
pass against `ms-ai-901.csv` and update template
`credential_targets` to list both. Not blocking this quarter's
launch; blocking fall 2026 cohort.

### C. Atom content depth varies

Some atoms are teacher-ready stubs (`teachable-machine-
introduction` is tight and runnable). Others need a content expansion
pass before a teacher could walk in Monday and teach from them
(`programming-a-sensor-driven-robot`, `statistics-for-ai-and-ds`,
anything with "stats" in the objective). The stub format is fine for
the library; the classroom-ready pass is a separate deliverable.

**Action:** I'll queue the expansion list for my next sprint. Roughly
25 atoms need a second pass before I'd hand them to a first-year
teacher. Priority order: programming → statistics → embedded.

### D. No "communicating findings" atom

The data-analysis thread ends at "construct informed summaries,
decisions, or predictions" (`data-analysis-for-decisions`), but
doesn't cover **how to communicate those findings to a non-technical
audience** — the single most underweighted skill in every DS/AI
curriculum I've ever reviewed. Add an atom:
`communicating-data-findings` — covers audience awareness, one-page
briefs, presentation structure, visualization for lay audiences.
Sit it after `data-analysis-for-decisions` and cross-reference from
the capstone units.

**Action:** Authoring backlog. Not blocking Georgia launch since
Georgia's standards don't explicitly require it, but it's a
marketable differentiator.

### E. The course descriptions on the three template files are fine
but they're not what I'd hand a counselor

The Description fields at the top of each template read like a
summary of content, not a sell. Counselors scheduling students into
these courses will paraphrase whatever's on the page. Rewriting the
course descriptions is on me — will land in a follow-up PR with the
v0 classroom-ready content.

## What I'm signing off on this pass

**Stamping 81 crosswalk rows as `maya-2026-04-18`** (via
`scripts/stamp_maya_review_ga.py`). Allowlist of atoms I can
credibly review — employability, CTSO, spreadsheet/data-analysis,
core Python / programming intro, Design Thinking, soft ethics,
AI-introduction, data-fundamentals (conceptual). Specifically:

1. All employability rows across the three courses
   (IT-***-1.1–1.6 × 3). I wrote CTE employability units for 9 years
   and ran a department; these alignments are trivially correct.
2. All CTSO rows (IT-FAI-9.*, IT-AIC-8.*, IT-AIA-8.*). Same
   reason.
3. Spreadsheet / data-analysis rows mapping to IT-FAI-6.*,
   IT-AIC-5.7, IT-AIC-5.8, IT-AIA-5.9. Spreadsheets and data
   visualization are in my bones.
4. Programming rows mapping core Python atoms to IT-FAI-4.* and
   IT-AIC-4.*. My CTE certification includes Business Information
   Management and I've taught intro programming units.
5. Design-Thinking / ethics-soft / industry-context rows — IT-FAI-7.*
   (excluding bias-with-Teachable-Machine detail), IT-FAI-8.*,
   IT-AIC-2.*, IT-AIC-6.5, IT-AIA-2.*.
6. AI-introduction rows (IT-FAI-2.*, IT-FAI-3.*, IT-AIC-2.*).

The stamping script (`scripts/stamp_maya_review_ga.py`) captures the
allowlist as code so we can re-run against future crosswalk rows
without re-interviewing me.

**NOT stamping this pass (294 rows remain `ai-draft`):**

- Everything mapping to a Microsoft AI-900 objective. I hold ITF+
  and MOS, not AI-900. Need Sergio to pull in a technical SME here —
  probably Jordan (our AI Literacy director) or the TAP member with
  an AI background.
- The `certiport-its-artificial-intelligence::` → embedded
  (IT-AIA-7.*) mappings. Ditto — not my credential.
- The CompTIA Data+ statistical-reasoning mappings (Data+ 3.* →
  IT-AIC-5.9 / IT-AIA-5.9). Stats content needs a second pair of
  eyes.
- The PCED (Python data analytics) mappings — not my credential.
- ~40 rows where alignment_strength is `introduces` or `mentioned` —
  these are low-confidence mappings even for me; defer.

## Template promotion status

All three templates stay at `status: draft`. I'm not comfortable
promoting to `active` until:

1. My TAP (Teacher Advisory Panel) reviews the three templates
   end-to-end. **That panel doesn't exist yet** — per my 90-day plan,
   standing it up IS my next deliverable.
2. A technical SME stamps the AI-900 / Data+ / embedded rows I
   deferred.
3. I publish v0 classroom-ready content for ~3 atoms — so I can
   point teachers at working examples rather than stubs.

Realistic promotion timeline: **end of Q3 2026** if TAP formation
happens on schedule.

## Questions for Sergio

1. Who owns the technical-SME review of the AI-900 / embedded rows?
   Jordan's title is AI Literacy Director but her role statement
   doesn't explicitly include credential alignment review. Either
   update her charter or budget for a contract AI-SME.
2. Do we want to offer this pathway outside Georgia before TAP sign-
   off? If yes, we need a second state's standards (Texas Innovative
   Course model, per the Phase 2 plan) before we can meaningfully
   market it.
3. End-of-Pathway Assessment prep — is Georgia's EoP exam published
   enough that I can align to specific content, or is it a closed
   item pool? Need to know before I expand u09.

---

*Maya Delgado, Founding Curriculum Designer — 2026-04-18*
