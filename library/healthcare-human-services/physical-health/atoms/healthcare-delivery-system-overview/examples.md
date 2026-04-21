---
atom_id: healthcare-delivery-system-overview
atom_serial: HHS-PH-0014
sidecar: examples
status: ai-draft
example_count: 4
author: claude
reviewer:
review_date:
---

# Worked examples — healthcare-delivery-system-overview

## Example 1 — Older adult with a hip fracture

**Scenario:** An 82-year-old woman falls at home and cannot get up.
Her daughter calls 911. She is hospitalized, has surgery, and
eventually returns home. She has Medicare and a private supplemental
(Medigap) plan.

**What to work out:** Trace her path across care settings, name the
transitions, and identify which payer(s) cover which steps.

**Step-by-step:**

1. Home → EMS → emergency department. Local EMS (a **care setting**
   in its own right) responds and transports her. The receiving
   hospital's emergency department is the first clinical setting:
   high-**acuity** care, billed to **Medicare** Part B as a physician
   service and Part A for the facility once she is admitted
   [CMS-About].
2. Emergency department → inpatient surgical unit. Admission for
   hip repair. This is **acute care**. Medicare Part A covers the
   hospital stay; the supplemental plan picks up deductibles and
   coinsurance. This is also the first **care transition** — her
   medication list is reconciled, orders change, and the hand-off
   from the ED team to the surgical team is a known risk point
   [AHRQ-Transitions].
3. Hospital → skilled nursing facility. After a few days on the
   surgical floor, she is discharged to a skilled nursing facility
   for rehabilitation — **post-acute care**. Medicare Part A covers
   a limited number of days in a qualifying facility. The
   hospital-to-SNF hand-off is the transition most associated with
   readmission risk; discharge paperwork, new medications, and
   follow-up appointments are all on the line [AHRQ-Transitions].
4. SNF → home with home health. Once she can bear weight and
   manage stairs, she is discharged home. Home health nurses and
   physical therapists visit to continue rehabilitation in the home
   setting. Medicare covers home-health services under eligibility
   rules; the supplemental plan covers cost-sharing.
5. Home → **primary care** follow-up. Two weeks after discharge,
   her primary-care clinician sees her in clinic to review
   medications, check the surgical site, and coordinate any new
   specialty referrals. This visit is part of the **continuum of
   care** loop that prevents problems from becoming the next
   emergency.

**Answer:** Five settings (EMS, ED, inpatient acute, SNF, home with
home health, primary care), four care transitions, two payers
(Medicare as primary with Part A and Part B components; a private
supplemental plan as secondary).

**Why it matters:** A single "hip fracture" is not one event; it is
a sequence. Every transition is a seam where the system can either
coordinate or fail. Mapping the sequence is the core skill the
atom's learning objective asks for.

## Example 2 — Child with asthma in a mixed-coverage family

**Scenario:** A 7-year-old boy has persistent asthma. His mother has
employer-based private insurance through her job; he is also
enrolled in **CHIP**. He has one primary-care clinician, an
allergist, and occasionally ends up in the emergency department
during severe flares.

**What to work out:** Identify which settings and which payers are
involved across a year of routine and urgent care.

**Step-by-step:**

1. Routine primary care. Quarterly visits at a pediatric primary-
   care office review inhaler technique, growth, and school
   attendance. Primary care is first-contact and continuing care
   [KFF-Overview]. The mother's private plan is billed first; CHIP
   acts as a secondary payer for cost-sharing the private plan does
   not cover.
2. Specialty care. An allergist sees him once or twice a year to
   adjust maintenance therapy. Specialty care is a distinct phase of
   the **continuum of care** — focused expertise on a specific
   condition — and it lives in an outpatient clinic rather than a
   hospital.
3. Acute flare during a viral infection. The child is short of
   breath late at night. The family can reach either an urgent
   care or the emergency department; the primary-care office is
   closed. Because respiratory distress in a 7-year-old can escalate
   quickly, the **acuity** match is the emergency department, not
   urgent care.
4. Return to primary care. A few days after discharge, the
   primary-care office calls the family for a post-ED check — this
   is the **care transition** from acute care back to primary care.
   Asthma action plans and medication adjustments happen here.
5. Access barrier check. The family's neighborhood has good
   broadband, so **telehealth** follow-up is an option for
   medication checks between flares. Translation services are not
   needed because the family speaks English. Transportation is not
   a barrier because the mother has a car. If any of those changed
   — a move to a rural county, a first-generation family without
   English fluency, loss of the car — the same clinical picture
   could yield very different outcomes [RWJF-SDOH, NASEM-Access].

**Answer:** Three main settings (primary care, specialty clinic,
emergency department) with telehealth as a supplement, two payers
working together (private plan plus CHIP), and a continuum that runs
prevention → primary → specialty → acute → back to primary over
repeated cycles.

**Why it matters:** A single patient can have several payers at once,
and most chronic-disease care lives in the seams between primary,
specialty, and acute care. Seeing the pieces as one continuum is
what lets a clinician or care coordinator prevent the next ED visit.

## Example 3 — Adult with diabetes in a rural shortage area

**Scenario:** A 54-year-old man lives in a rural county designated
as a Health Professional Shortage Area. He has type 2 diabetes and
works for a small employer that does not offer insurance. He buys
coverage through the state's individual-market marketplace. The
nearest primary-care clinic is 25 miles away; the nearest
endocrinologist is 80 miles away.

**What to work out:** Identify which access barriers shape his care
and how settings and payers interact.

**Step-by-step:**

1. Name the access barriers. Geography is the first
   **access barrier**: he lives in a federally designated shortage
   area, so the provider-to-population ratio is below threshold
   [HRSA-ShortageAreas]. Transportation compounds geography — a
   25-mile drive is manageable in good weather, harder in winter or
   after a long shift. Cost is a barrier even with coverage: a
   bronze marketplace plan has a high deductible, which changes how
   often he fills prescriptions or schedules visits.
2. Primary-care setting. He sees a family nurse practitioner at the
   critical-access hospital's rural clinic. This is **primary care**
   in a rural setting — the same function as an urban primary-care
   office, delivered by whichever clinicians are actually present.
3. Specialty care via telehealth. Instead of an 80-mile drive each
   quarter, he sees the endocrinologist by video. **Telehealth** is
   a care setting within the existing system, not a parallel one;
   the visit is billed through his marketplace plan to the same
   practice that would have seen him in person [KFF-Overview]. This
   is also where digital access becomes an access barrier — if his
   home internet drops, the visit fails.
4. Acute event. After a year of skipped doses because of cost, he
   develops a foot ulcer that becomes infected. He drives himself
   to the critical-access hospital's emergency department and is
   admitted for IV antibiotics — **acute care**. Because the
   surgical capability he needs is not available locally, he is
   transferred 80 miles to a tertiary hospital. Transfer is itself
   a **care transition** with risk [AHRQ-Transitions].
5. Post-acute and return home. He spends several days at the
   tertiary hospital, then returns to a skilled nursing facility
   near home for IV therapy — **post-acute care** — before going
   home with home health for wound care. Each hand-off is a chance
   for medications and instructions to get lost; rural distance
   makes rapid follow-up harder.

**Answer:** Three barriers (geography, cost, digital access) layered
on the clinical picture; settings run from primary care through
telehealth specialty, to acute care across two hospitals, through
post-acute care and home health; one payer (the marketplace plan)
throughout.

**Why it matters:** Shortage-area patients do not have worse
outcomes because their disease is different. They have worse
outcomes because the system's seams are longer in rural counties,
and because access barriers compound [CDC-RuralHealth, NASEM-Access].
Seeing that is the second half of the atom's learning objective.

## Example 4 — End-of-life continuum for a cancer patient

**Scenario:** A 70-year-old woman is diagnosed with advanced cancer.
Over 18 months, her care moves from diagnosis through active
treatment, a hospitalization, a shift to comfort-focused care, and
finally hospice at home. She has Medicare; her adult son helps
coordinate her care.

**What to work out:** Map the full **continuum of care** from
prevention through end-of-life, name the settings and payers, and
identify the fragile transitions.

**Step-by-step:**

1. Screening and diagnosis. A routine screening exam at her
   primary-care clinic flags a finding that leads to a biopsy.
   Prevention and primary care are the first phases of the
   continuum [NASEM-Access]. Medicare Part B covers the outpatient
   workup.
2. Specialty and acute care. An oncologist (specialty care)
   manages chemotherapy at a hospital-affiliated infusion center.
   Mid-treatment, she is admitted for a serious infection — this
   is acute care, in an inpatient setting, billed to Medicare
   Part A. The hand-off between the oncology team and the
   inpatient hospitalist is a known **care transition** risk
   [AHRQ-Transitions].
3. Post-acute transition. After stabilization, she is discharged
   home with home health for IV-line care and fatigue management.
   Post-acute care is the bridge between the hospital and
   community, and Medicare covers qualifying home-health days.
4. Shift to comfort-focused care. Several months later, treatment
   stops working. Her oncologist and primary-care clinician
   together discuss goals with her and her son. The care plan
   shifts from cure to comfort. This is a transition the textbook
   often skips; in practice, it is one of the most important
   seams, and it has its own payer rules — Medicare has a defined
   hospice benefit that activates when eligibility criteria are
   met [CMS-About].
5. Hospice at home. Hospice in her home is the final setting. The
   hospice team — nurse, social worker, chaplain, aide — coordinates
   symptom control, family support, and end-of-life decisions.
   Medicare covers hospice services under its hospice benefit; her
   son manages logistics. The final transition is death itself, a
   seam the system is still learning to handle gracefully.

**Answer:** Six phases of the continuum (prevention → primary →
specialty → acute → post-acute → end-of-life), five or more
settings including telehealth check-ins between cycles, and one
primary payer (Medicare) with its hospice benefit activating at the
final phase.

**Why it matters:** Students often learn the continuum as a list of
words. A patient journey makes it a map with real decision points,
real seams, and real stakes. If a student can walk through this
example and name the transitions, they can do the first part of the
atom's learning objective in any case they encounter.
