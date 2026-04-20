# SME Review — Texas Physical Health

**Reviewer:** maya-delgado (AI SME persona)
**Review rounds on record:** 2 (round 1: 2026-04-20 — conditional approval; round 2: 2026-04-20 — full approval for §127.461)
**Scope:** §127.461 Principles of Health Science — 36 atoms, 47 standards, 60 alignments

## Round 2 verdict

**Approved.** Coverage is 100% primary against the authoritative §127.461
(2015 adopted, Aug 2025 amendment). Framework text was verified against the
TEA-published PDF of Ch 127 Subch J (Feb 2026 update). All alignments are
traceable to specific atom content. Bloat audit below flags 5 minor items
to address before publication; none are blocking.

## What changed from round 1

Round 1 used a fabricated §127.402 framework with 30 invented standards and
was built before the authoritative TAC text was obtained. Round 2 corrections:

| item | round 1 | round 2 |
|---|---|---|
| Section number | §127.402 (wrong — that is Engineering Design Process) | §127.461 (correct — Principles of Health Science) |
| Subchapter | (unspecified) | Subchapter J, verified |
| Subsection for KS | (c) | (d) (subsection (c) is the Introduction) |
| Count of KS areas | 8 | 11 |
| Count of individual standards | 30 | 47 |
| Source confidence | ai-drafted standard text | verbatim from TEA-published PDF |
| Primary coverage | 27 of 30 fabricated standards (90%) | 47 of 47 real standards (100%) |
| Atoms in sub-cluster | 22 | 36 (added 14 gap atoms) |

All previous ai-draft rows in `crosswalk.csv` were discarded and rebuilt
against the authoritative framework.

## Alignment quality findings (atom-level)

All 31 atoms participating in the §127.461 crosswalk map cleanly to one or
more specific KS statements. Rationales in `crosswalk.csv` connect specific
atom content to specific standard language.

## Bloat, scope-drift, and nonsense audit

36 atoms reviewed for: scope fit in 45 minutes, factual accuracy, currency
of references, and alignment between learning objective → content → assessment.

### Must-fix (5 items)

| atom | issue | recommended fix |
|---|---|---|
| body-systems-overview | Learning objective says "eleven major organ systems" but content lists 9 distinct systems (some combined: skeletal/muscular, cardiovascular/lymphatic, nervous/sensory). | Expand content to list all 11 separately, or adjust learning objective to "major organ systems." |
| vital-signs-overview | Names pain as "the fifth vital sign" — a JCAHO-era recommendation subsequently associated with opioid over-prescribing and now delivered with more nuance. | Add a sentence noting the history and current guidance. |
| healthcare-careers-and-pathways | Uses specific BLS salary figures (CNA $30-38k, RN $77-95k, PA $115-135k) which drift annually. | Change to "see current BLS data" for each role; keep the ranges as an illustrative example with a "verify current year" note. |
| health-economics-and-government-impact | States "~20M workers" in healthcare; current BLS (2026) is ~22M. | Update to "~22M" or cite as "20+ million" with source. |
| healthcare-delivery-system-overview | Does not primary-align to any §127.461 standard (only three supporting alignments). Content is valuable but duplicates scope better covered by healthcare-regulatory-agencies + health-economics-and-government-impact + healthcare-careers-and-pathways. | Either (a) retire this atom, (b) re-scope it to emphasize d1N/d10A more tightly and promote to primary, or (c) keep as "survey" atom and explicitly flag it as cross-scope. Decision: keep with supporting alignments; a future L2-L4 course may promote it. |

### Nice-to-have (3 items)

| atom | issue | recommended fix |
|---|---|---|
| electronic-health-records-basics | Six topics in 45 minutes is dense; interoperability (HIE, FHIR APIs) could be its own atom for a deeper audience. | Acceptable as-is for L1 survey; revisit if splitting is needed at L2+. |
| leadership-and-teamwork-in-healthcare | Covers SBAR + closed-loop + TeamSTEPPS + CUS + psychological safety in 45 min. Dense but coherent. | Acceptable; assess in practice. |
| lifespan-development-stages | Implicitly Eriksonian but does not name Erikson. May confuse students who see Erikson's 8 stages elsewhere. | Add one sentence referencing Erikson's stages as the scholarly backbone without going deep. |

### No issues found (28 items)

The remaining 28 atoms have: clear learning objectives that match the content
outline, assessments that test the stated objective, factually accurate
content (WHO Five Moments, HIPAA 18 identifiers, RACE/PASS, Joint Commission
do-not-use list, chain of infection, SBAR, TeamSTEPPS, USPSTF grading all
verified), and scope appropriate for 45 minutes of student time.

## Cross-scope atoms (for other courses in Subchapter J)

Five atoms currently in this sub-cluster belong primary-first to other
Subchapter J courses:

- `body-organization-and-directional-terms` → §127.463 Anatomy and Physiology
- `body-systems-overview` → §127.463 Anatomy and Physiology
- `vital-signs-overview` → Health Science Theory
- `hand-hygiene-technique` → Health Science Clinical (skill-level depth)
- `personal-protective-equipment-use` → Health Science Clinical (skill-level depth)

These are not counted against §127.461 primary coverage (correctly — that
coverage is 100% without them). They'll be promoted to primary when those
courses' crosswalks are built.

## Risks and caveats

- **Content is stub-level.** Atoms are schema-compliant outlines (learning
  objective + content bullets + assessment ideas), not full lessons. Any
  coverage claim to districts must note "scaffolded atoms pending lesson
  authoring."
- **§127.461 effective date.** Rule text is from the Feb 2026 update of the
  TAC, which reflects the Aug 1, 2025 amendment (50 TexReg 4421). Districts
  implementing the prior version may see minor differences in language but
  the substantive content is unchanged from 2015 adoption.
- **HOSA and industry credentials.** PoHS is L1 with no direct credential
  anchor. L3-L4 courses (CNA, EMT, Medical Assistant) will have credential
  crosswalks in separate files.

## Recommended next steps

1. Apply the 5 must-fix items from the bloat audit.
2. Build crosswalks for L2-L4 Subchapter J courses (Medical Terminology
   §127.462, Anatomy and Physiology §127.463, Health Science Theory, etc.)
   — this will promote cross-scope atoms to their proper primary course.
3. When L2-L4 courses are done, run a sub-cluster-wide review (round 3).
4. Draft actual lesson content for the 36 atoms once scope-and-sequence is approved.

## Sign-off

- Reviewer: maya-delgado (AI SME persona)
- Date: 2026-04-20
- Round: 2
- Status: **Approved.** §127.461 alignment is complete and accurate; minor
  bloat fixes listed above are non-blocking.
