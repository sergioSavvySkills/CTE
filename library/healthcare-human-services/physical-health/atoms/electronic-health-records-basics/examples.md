---
atom_id: electronic-health-records-basics
atom_serial: HHS-PH-0008
sidecar: examples
status: ai-draft
example_count: 4
author: claude
reviewer:
review_date:
---

# Worked examples — electronic-health-records-basics

Two procedural examples (navigate and document) and two reasoning
examples (audit a pasted note and apply the access rules) — the
skill_type for this atom is *both*, so the mix is deliberate. Each
example targets one of the atom's three LO parts: describe what an
EHR is, navigate common chart sections, apply safe-practice rules.

## Example 1 — Locating information across chart sections

**Scenario:** A medical assistant is rooming a returning patient. The
clinician will walk in in five minutes and needs a quick orientation.
The chart is open on a screen the student has never used before.

**What to work out:** Find five pieces of information the clinician
always wants first — active problems, current medications, allergies,
the last set of vitals, and the most recent progress note — using
only the section names, not the vendor's menu layout.

**Step-by-step:**

1. Open the **problem list** to see what conditions the patient is
   being treated for. This is usually pinned at the top of the chart
   summary [TJC-Documentation].
2. Open the medications section to see the current medication list,
   including doses and frequencies.
3. Open the allergies section. Confirm any drug allergies with the
   patient while you have them in the room.
4. Open the **flowsheet** to see the most recent vital signs and
   trend over the last several visits.
5. Open the most recent **progress note** to read what the clinician
   thought and did last time.

**Answer:** The orientation takes about two minutes. You walked to
five named sections without needing a map of the vendor's interface.

**Why it matters:** Every EHR organizes the same underlying sections.
If you learn the section *names* — problem list, medications,
allergies, flowsheet, progress note — you can get oriented on any
vendor's system after a short tour [ONC-EHR]. That transfer is the
whole point of learning EHR navigation at the category level.

## Example 2 — Writing a safe progress-note entry

**Scenario:** A home-health aide has just finished a blood-pressure
check on a patient and needs to add a short progress-note entry to
the EHR. The reading is 148/92. The patient says she took her
lisinopril this morning and reports a mild headache.

**What to work out:** Write a note that follows the charting rules —
objective language, time-stamped, signed, and amendable — in three
lines.

**Step-by-step:**

1. Open a new **progress note** on the correct patient. Verify two
   identifiers (name plus date of birth) before typing
   [AHRQ-EHR-Safety].
2. Write the observation in objective terms: *"BP 148/92 R arm
   seated. Patient reports taking 10 mg lisinopril this morning.
   Reports mild bifrontal headache, rates 3/10."*
3. Record the plan or action taken in one sentence: *"Reviewed BP
   log with patient. Will notify primary clinician of elevated
   reading."*
4. Let the EHR time-stamp the entry automatically; do not backdate.
5. Electronically sign the note. Unsigned notes are not yet part of
   the legal record [TJC-Documentation].

**Answer:** A three-line objective entry, time-stamped by the system,
signed by the author, and attached to the verified patient.

**Why it matters:** This is the shape of almost every short entry
you will write: verify the patient, observe in objective terms,
record the action, sign [TJC-Documentation]. If you later realize the
BP cuff was the wrong size, you cannot erase the entry — you use the
EHR's amendment workflow to add a correction, preserving both the
original and the fix.

## Example 3 — Auditing a progress note for copy-paste error

**Scenario:** A supervisor shows you today's progress note for a
68-year-old patient admitted for heart failure. The assessment
section reads:

> "HPI: Patient presents with 3-day history of crushing retrosternal
> chest pain radiating to left arm. Pain is 8/10, worse with exertion.
> Review of systems: no headache, no cough, no dyspnea on exertion.
> Assessment: Acute coronary syndrome, rule out MI."

Today the patient has no chest pain. She is short of breath with
exertion and has bilateral leg edema. Today's vitals show SpO2 92%
on room air. She was admitted last month for a heart attack; today
she has been admitted for a heart-failure exacerbation.

**What to work out:** Identify what is wrong with this note and name
the error pattern.

**Step-by-step:**

1. Compare the note's described findings to today's clinical picture.
   The note describes crushing chest pain and denies dyspnea; today's
   patient has no chest pain and has dyspnea. The note does not match
   the patient.
2. Name the pattern: this is a **copy-paste error**. Text was carried
   forward from the prior admission's HPI [ISMP-CopyPaste]. The
   language describes the earlier event, not today's.
3. List the downstream risks: the assessment line drives ordering
   (a rule-out MI workup rather than a heart-failure workup); a
   later reviewer may treat the pasted text as today's findings;
   the chart is internally inconsistent with the flowsheet
   [AHRQ-EHR-Safety].
4. Describe the fix: the author amends the note, removes the pasted
   HPI, writes a fresh HPI describing today's dyspnea and edema, and
   updates the assessment to reflect heart-failure exacerbation. The
   amendment preserves the original and the correction.

**Answer:** The note is a copy-paste error — prior-admission HPI
pasted into today's note — and must be amended with a fresh HPI and
a heart-failure-focused assessment.

**Why it matters:** Copy-paste errors are one of the most commonly
cited EHR harm patterns [ISMP-CopyPaste]. They are dangerous not
because pasted text is always wrong, but because stale text looks
exactly like current text to the next reader. Spotting the mismatch
is the habit.

## Example 4 — Applying the access rules to a curiosity-driven lookup

**Scenario:** A clinical assistant hears the ambulance pull up on her
street the night before, and the next morning recognizes a neighbor's
name on the patient census at her hospital. During a quiet moment
she opens the neighbor's chart "just to see if he's okay." She does
not write anything, does not talk to anyone, and closes the chart
after a minute. Later that week, the privacy officer calls her in.

**What to work out:** Explain, using the atom's access-rules concepts,
what happened and why the lookup was a violation even though no
information was disclosed.

**Step-by-step:**

1. Identify the rule that was broken. Access is governed by
   **role-based access**: each user has the permissions their
   treatment role requires and no more [HIPAA-Security]. The
   assistant had no treatment relationship with her neighbor. Her
   account had the technical permission to open the chart, but her
   role did not authorize her to do so.
2. Explain how the lookup surfaced. Every EHR runs an **audit trail**
   that records which user opened which chart and when
   [HIPAA-Security]. The privacy officer's routine review — or a
   complaint from the patient or the family — pulled her access log.
3. Address the "but I didn't tell anyone" defense. The violation is
   the unauthorized access, not the subsequent disclosure. Viewing a
   record without a treatment relationship is itself the breach
   [AHRQ-EHR-Safety].
4. Describe realistic consequences. Depending on the facility and the
   circumstances, outcomes range from mandatory retraining and a
   written warning to termination. Federal HIPAA penalties apply at
   the institution level; the prerequisite HIPAA atom covers those
   specifics.

**Answer:** The assistant committed an unauthorized-access violation
caught by the audit trail. Role-based access allows only
treatment-relationship lookups; curiosity is not a treatment
relationship, and the absence of disclosure does not undo the
breach.

**Why it matters:** The audit trail is the safe-access rule's
enforcement layer. Students who assume "nobody reads the logs"
discover otherwise in exactly this kind of scenario
[AHRQ-EHR-Safety]. Treating every chart view as logged — because it
is — is the habit the atom is teaching.
