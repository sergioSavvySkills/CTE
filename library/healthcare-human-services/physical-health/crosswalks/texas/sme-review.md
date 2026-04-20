# SME Review — Texas Physical Health

**Reviewer:** maya-delgado (AI SME persona)  
**Review date:** 2026-04-20  
**Review round:** initial (round 1 of N)  
**Scope:** 127.402 Principles of Health Science — 22 atoms, 30 standards, 33 alignments

## Verdict

**Conditional approval, pending two fixes.**

Coverage and alignment quality are strong: 27 of 30 standards have a primary
atom, 3 standards have only supporting coverage. Atom scope, depth, and
assessment design meet the schema (15-60 min, industry-neutral, three
required sections present). The three coverage gaps (c1D, c2C, c7B) have
clear close-out paths specified in `coverage-report.md`.

Two issues must be resolved before this crosswalk is used for compliance or
scope-and-sequence decisions:

1. **TEKS text is AI-drafted.** Standard codes (c1A, c2B, etc.) and standard
   text in `state-framework.csv` are a best-effort reconstruction of what
   §127.402 KS statements typically contain, not the verbatim rule text.
   A human SME with authoritative TEA rule access (19 TAC Ch 127 Subchapter J)
   must verify every `standard_code` and `standard_text` field before this
   is used to establish TEKS compliance. Some numbering (e.g., c5E vs. c5D)
   may not match the adopted rule.

2. **2024 rule update not confirmed.** The framework version is marked
   "2022 Adopted" on the assumption Texas Ch 127 Subch J reached final
   adoption in 2022 with course-code effective dates in 2024. The actual
   adoption year, revision history, and effective dates must be verified.

## Alignment quality findings (atom-level)

| atom_id | finding |
|---|---|
| healthcare-delivery-system-overview | Strong c8A primary alignment. Supporting c1A is appropriate (careers-in-context). No issues. |
| healthcare-careers-and-pathways | Clean triple primary (c1A, c1B, c1C). Career-plan assessment directly supports c1C. No issues. |
| healthcare-team-roles | Appropriate c3C primary. Prereq on `healthcare-careers-and-pathways` is correct ordering. |
| medical-terminology-word-parts | Dual primary (c2A, c6C) is defensible — the atom teaches both the vocabulary and the decoding strategy. |
| common-medical-abbreviations | Primary c6D is clean (explicitly includes do-not-use list). Supporting c2A/c2C are appropriate. |
| body-organization-and-directional-terms | Clean c6A primary. Planes + cavities + directional pairs all present. |
| body-systems-overview | Clean c6B primary. 11 systems + function + disorder + interactions — complete. |
| professional-ethics-in-healthcare | Clean c4D primary. Four principles all present; dilemma assessment is rigorous. |
| hipaa-and-patient-confidentiality | Clean c4A primary. 18 identifiers mentioned; do-not-use list well-covered. |
| patient-rights-and-informed-consent | Clean c4B primary. Prereq on ethics atom is correct. |
| scope-of-practice-and-licensure | Clean c4C primary. Interstate/compact content is valuable addition. |
| standard-precautions-and-chain-of-infection | Clean c5A primary. Chain + transmission modes + transmission-based precautions — complete. |
| hand-hygiene-technique | Clean c5B primary. WHO Five Moments + soap-vs-ABHR decision logic present. Skill check required in assessment. |
| personal-protective-equipment-use | Clean c5C primary. Donning/doffing sequence explicit; fit-testing noted. |
| body-mechanics-and-safe-patient-handling | Clean c5D primary. Zero-lift policies + lift equipment decision logic present. |
| fire-and-emergency-safety | Clean c5E primary. RACE + PASS + codes + evacuation priorities — complete. |
| therapeutic-communication | Dual primary (c2B, c2D) is defensible — atom covers both technique and barriers. |
| cultural-competence-in-healthcare | Clean c8C primary. Competence-vs-humility distinction is excellent. |
| wellness-and-disease-prevention | Clean c8B primary. Primary/secondary/tertiary + USPSTF grading — strong. |
| vital-signs-overview | Clean c6E primary. Five vitals + normal ranges + pain as 5th — complete. |
| electronic-health-records-basics | Clean c7A primary. Supporting c2C and c7B are appropriate. |
| leadership-and-teamwork-in-healthcare | Dual primary (c3A, c3B) is defensible. SBAR + closed-loop + TeamSTEPPS + CUS — rigorous. |

No atom was rated as over- or under-scoped for its primary standard.
No atom was flagged as "supporting where it should be primary" or vice versa.

## Rationale quality

Crosswalk `rationale` field is populated on all 33 alignments with specific
atom-content references (not vague "atom covers standard X" phrasing).
Rationales connect specific atom elements to specific standard language.

## Known risks for downstream use

- **Standards text is approximate.** Any marketing, compliance report, or
  district-facing document built from this crosswalk must cite the
  authoritative TAC as source, not this file, until verification is complete.
- **No actual instructional content.** Atoms are schema-compliant stubs
  (learning objective + content outline + assessment ideas). They are not
  complete lessons. Any coverage claim must note "scaffolded atoms pending
  lesson authoring."
- **HOSA and industry credential alignments not yet mapped.** PoHS is a
  Level 1 course; credential objectives attach at L3-L4. No credential
  crosswalk is needed yet for this course.

## Recommended next steps

1. Human SME verification of `state-framework.csv` against published TAC Ch 127 Subch J text.
2. Build the 3 gap atoms (see `coverage-report.md`) to reach 100% primary coverage.
3. When L2-L4 courses in this sub-cluster are scoped, extend `state-framework.csv` and re-run this review.
4. Schedule round-2 review after gap atoms are added.

## Sign-off

- Reviewer: maya-delgado (AI SME persona)
- Date: 2026-04-20
- Round: 1
- Status: Conditional approval — proceed with atom build-out; block compliance/marketing use pending TEKS text verification.
