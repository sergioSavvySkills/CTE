---
atom_id: healthcare-regulatory-agencies
atom_serial: HHS-PH-0016
sidecar: examples
status: ai-draft
example_count: 4
author: claude
reviewer:
review_date:
---

# Worked examples — healthcare-regulatory-agencies

## Example 1 — Tracing a 60-second IV start back to four agencies

**Scenario:** A nurse on a med-surg unit is preparing to start a
peripheral IV on a patient in contact precautions. In about a
minute she checks two identifiers, foams her hands, puts on a gown
and gloves, scans the medication bar code, starts the line, and
documents the event in the chart.

**What to work out:** For each step, identify which agency's rule
or recommendation primarily drives the practice.

**Step-by-step:**

1. Checking two patient identifiers before touching the patient.
   This is the Joint Commission's first National Patient Safety
   Goal, "improve the accuracy of patient identification"
   [TJC-About]. It is enforced through **accreditation**, not
   federal law.
2. Hand hygiene before patient contact. The five-moments framework
   the unit teaches is a WHO **guideline** [WHO-About], reinforced
   by CDC infection-control guidance and adopted into Joint
   Commission standards.
3. Gown and gloves for contact precautions. The CDC
   **transmission-based precaution** category for this patient
   drives the specific gear choice [CDC-About]. The broader duty
   of the employer to supply **personal protective equipment** at
   no cost to the worker is an OSHA Bloodborne Pathogens
   requirement [OSHA-BBP].
4. Scanning the medication bar code. Bar-code medication
   administration uses labels required under FDA regulation of
   drug packaging [FDA-About], combined with Joint Commission
   medication-safety expectations.
5. Documenting the IV start. Documentation supports the Joint
   Commission tracer methodology, which will follow this patient's
   chart during a survey, and provides the record used if a later
   safety review is triggered.

**Answer:** The single sequence pulls in at least four agencies —
Joint Commission (identification, medication safety), WHO and CDC
(hand hygiene and precautions), OSHA (PPE supply to worker), and
FDA (drug labeling and bar-coding).

**Why it matters:** Any ordinary clinical task involves rules from
multiple agencies layered on top of each other. Seeing the layers
is what lets you answer "why do we do it this way?" without
memorizing a rulebook.

## Example 2 — Responding to a sentinel event

**Scenario:** At a Joint Commission-accredited hospital, a patient
scheduled for a right-knee arthroscopy wakes up in recovery to find
the procedure was performed on the left knee. The quality department
is notified within an hour.

**What to work out:** Name the relevant category, the required
response, and which agency's expectations drive each piece.

**Step-by-step:**

1. Classify the event. A wrong-site surgery reaches the patient and
   causes permanent harm; it meets the Joint Commission definition
   of a **sentinel event** [TJC-About].
2. Immediate patient response. Clinicians stabilize the patient,
   disclose the event, and document what happened. The disclosure
   expectation is part of Joint Commission standards and state
   licensing rules; the specific language is shaped by the
   hospital's policy.
3. Root-cause analysis. The hospital convenes a team to conduct a
   root-cause analysis within the Joint Commission's expected
   timeframe. The team reconstructs the pre-incision time-out, the
   site-marking process, and the surgical scheduling to find the
   system failures — not to assign individual blame.
4. System changes. The team revises the time-out protocol, adds a
   second site-verification step, and retrains staff. Joint
   Commission's Universal Protocol for preventing wrong-site
   surgery is the reference standard.
5. External reporting. The hospital reports the event through state
   channels if state law requires it, and may voluntarily report to
   The Joint Commission. This is distinct from an OSHA report,
   which would apply only if a worker had been injured, and from
   an FDA **medical device reporting** submission, which would
   apply only if a device malfunction contributed.

**Answer:** A wrong-site surgery is a **sentinel event** triggering
Joint Commission-driven root-cause analysis and system change, with
state licensing and internal policy layering on top.

**Why it matters:** Safety cultures are built on what happens after
a harm event. Knowing the category (sentinel event) and the
expected response (root-cause analysis, not punishment) is how a
healthcare worker participates in that culture rather than hiding
from it.

## Example 3 — Hand-hygiene audit in an outpatient clinic

**Scenario:** A federally qualified health center conducts a monthly
hand-hygiene audit. Observers watch staff for 20 minutes each and
record each opportunity to perform hand hygiene and whether it was
actually performed. The clinic's compliance rate is 78%.

**What to work out:** Which agencies' expectations are being
audited, and what daily practices the audit is checking.

**Step-by-step:**

1. Identify the rule source. Hand hygiene is a core **guideline**
   from WHO and CDC rather than an OSHA regulation
   [WHO-About, CDC-About]. The clinic's internal policy is the
   legally relevant document; it turns the guideline into an
   enforceable expectation for staff.
2. Identify the audit framework. The five-moments observation
   method comes from WHO and is the standard in most U.S.
   accredited settings.
3. Identify the accreditation driver. For any clinic seeking or
   maintaining accreditation, hand-hygiene performance is part of
   the Joint Commission's focus on healthcare-associated infection
   reduction [TJC-About].
4. Interpret the number. A 78% rate is below the clinic's target.
   The correct response is to identify the moments (often "before
   patient contact" and "after touching patient surroundings")
   where misses cluster and to target training and supply access,
   not to punish specific staff.
5. Note the limits. The audit does not measure patient outcomes
   directly. Linking the rate to infection outcomes requires the
   clinic's infection-surveillance program, which follows a
   **standard precaution** framework rather than an OSHA rule.

**Answer:** The audit is driven primarily by WHO and CDC hand-
hygiene guidelines and Joint Commission accreditation expectations,
with the clinic's internal policy acting as the enforceable
instrument.

**Why it matters:** Most daily safety practices are WHO or CDC
guidelines first and enforceable rules second. Recognizing the
source helps you read an audit report and push for the right
improvement, rather than assuming every number is a federal
compliance issue.

## Example 4 — Needlestick on an orthopedic floor

**Scenario:** A new nurse is drawing blood on an orthopedic floor
when the patient shifts and the used needle sticks the nurse's
thumb through her glove. She immediately washes the site and
reports the event to her charge nurse.

**What to work out:** Which agencies drive the response, and what
the nurse and the employer are required to do.

**Step-by-step:**

1. Classify the event. This is an occupational exposure to a
   potential **bloodborne pathogen**, which falls squarely under
   OSHA's Bloodborne Pathogens standard, 29 CFR 1910.1030
   [OSHA-BBP].
2. Employer duty. The employer must have a written exposure-control
   plan that specifies immediate steps: source-patient testing
   (when consented and permitted), baseline testing for the
   exposed worker, evaluation for post-exposure prophylaxis, and
   documentation. This is a federal **regulation**, not a
   guideline.
3. Nurse's immediate care. The nurse is evaluated by employee
   health or the emergency department per the written plan. She is
   offered hepatitis B vaccination if not already up to date, again
   under OSHA rules.
4. Engineering-control review. The event triggers a look at
   whether safer-sharps devices were in use as required, and
   whether sharps containers were available and not overfilled at
   point of use. All of these are OSHA requirements on the
   employer.
5. Separate layers that do not apply. The patient has not been
   harmed, so no Joint Commission **sentinel event** process is
   needed. No FDA **medical device reporting** is required unless
   the needle device itself is suspected to have failed. The
   **immunization schedule** and **outbreak response** framing from
   CDC are not relevant; this is a worker-protection problem.

**Answer:** A healthcare-worker needlestick is governed primarily
by OSHA's Bloodborne Pathogens standard, with internal employee-
health and hepatitis B vaccination processes flowing from that
**regulation**.

**Why it matters:** When a nurse is stuck, a useful mental move is
*"Whose rule drives this?"* — OSHA. Knowing the agency tells you
which forms exist, which protections you are entitled to, and who
enforces them if anything goes wrong.
