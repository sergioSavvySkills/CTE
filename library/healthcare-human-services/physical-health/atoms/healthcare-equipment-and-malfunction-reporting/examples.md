---
atom_id: healthcare-equipment-and-malfunction-reporting
atom_serial: HHS-PH-0015
sidecar: examples
status: ai-draft
example_count: 4
author: claude
reviewer:
review_date:
---

# Worked examples — healthcare-equipment-and-malfunction-reporting

Four reasoning walk-throughs, one per system category that matters for
day-one bedside habits, plus a support-services case. Each example
targets one of the atom's three LO parts (identify equipment across
the five systems, recognize malfunction signs, describe the reporting
path).

## Example 1 — Glucose meter on the medical-surgical floor

**Scenario:** A medical assistant uses a shared point-of-care
glucose meter for a morning blood-sugar check. The reading is 412
mg/dL on a patient whose last three readings have been in the 110s.
The patient feels fine and ate the same breakfast as yesterday.

**What to work out:** Identify what category of equipment this is,
decide whether to trust the reading, and describe the next actions.

**Step-by-step:**

1. Name the category. A glucose meter is point-of-care **diagnostic
   equipment** — the lightest end of the diagnostic system, used at
   the bedside to produce a single numeric result [AAMI-DeviceSafety].
2. Look for malfunction signs on the result itself. The number is
   out of pattern for this patient, the patient's symptoms do not
   fit a reading of 412 mg/dL, and the check ran on a shared device
   other floors have been using. Abnormal readings that disagree with
   the patient in front of you are a malfunction signal
   [ECRI-AlertsList]. Do not re-run the same sample on the same
   device.
3. Recheck with a different instrument. Draw a fresh fingerstick
   sample and run it on a different meter — either the backup on the
   floor or the lab's venous glucose. If the second reading is
   normal, the first device is the suspect.
4. Take the suspect meter out of service. Attach a **lockout tag**
   ("Do Not Use") and place it in the biomed drop-off location.
5. File a **work order** to biomed that names the device (asset tag
   or serial number), describes the discrepancy between the two
   meters, and notes the expired or miscalibrated strips as a
   possible cause.
6. If the first reading would have triggered action (e.g., an insulin
   order already keyed in based on the 412), file an **incident
   report** as a near-miss, even if no harm occurred.

**Answer:** The glucose meter reading is not trustworthy. Recheck on
another device, tag the suspect meter, work-order it to biomed, and
incident-report the near-miss if the bad number nearly drove
treatment.

**Why it matters:** Point-of-care devices fail quietly — the number
looks plausible. Your pattern recognition ("this doesn't fit the
patient") is the malfunction detector. The tag-and-work-order
workflow is the same for a $200 meter and a $200,000 imaging
machine.

## Example 2 — Ventilator circuit with a visible crack

**Scenario:** A respiratory therapist doing a morning check sees a
hairline crack along the connector of the ventilator circuit on a
stable ICU patient. The ventilator itself is displaying normal
pressures, the patient's oxygen saturation is 97%, and no alarm is
currently sounding.

**What to work out:** Decide whether to continue using the circuit,
and describe the actions that follow.

**Step-by-step:**

1. Name the category. The ventilator is **therapeutic equipment**
   and a **critical device** — failure during use could directly
   cause patient harm, so it gets the strictest response
   [TJC-EC, AAMI-DeviceSafety].
2. Identify the malfunction sign. Physical damage on a connector is
   a take-it-out-of-service signal on its own, even with normal
   readings and no active alarm. A crack can leak air, widen under
   pressure, or disconnect entirely.
3. Transition the patient to a safe circuit. Swap to a fresh
   ventilator circuit (or a backup ventilator if circuit swap is not
   possible at the bedside) before doing anything else. The patient
   is protected first, the device is handled second.
4. Remove the damaged circuit from service. Bag it, label the bag
   with a **lockout tag** so no one reuses it, and dispose or send
   to biomed per facility policy.
5. File a **work order** describing the defect; include the lot
   number on the circuit packaging if available so biomed and the
   manufacturer can trace other circuits from the same lot.
6. File an **incident report** to **risk management**. The patient
   was not harmed this time, but the device was in active use on a
   critical patient with a defect present — that is exactly the
   near-miss the incident-report system exists to capture [TJC-EC].

**Answer:** Switch to a fresh circuit immediately, tag the damaged
one, submit a work order, and file a near-miss incident report even
though the patient remained stable.

**Why it matters:** "Still powers on" and "nothing is alarming yet"
are not the same as *safe*. The lockout-tag-and-report workflow
captures the catch before it becomes a harm event, and the lot number
on the incident report is how a single facility's catch becomes a
field-wide warning [FDA-DeviceRecalls].

## Example 3 — Sterilizer fails its biological indicator test

**Scenario:** At the end of a sterilization cycle, central sterile
processing runs the weekly biological-indicator test and the
indicator grows — meaning the cycle did not kill the test
organisms. The sterilizer shows no **error code** and its printed
cycle parameters look normal. Twenty surgical instrument trays went
through that load overnight; three are already on the OR schedule
for this morning.

**What to work out:** Identify the category, name the malfunction,
and describe the reporting and recovery actions.

**Step-by-step:**

1. Name the category. A sterilizer is **support-services equipment**
   whose failure does not alarm at the bedside but affects every
   patient downstream [CDC-SterilizationGuidelines].
2. Identify the malfunction. A failed biological indicator means the
   cycle did not sterilize; the instruments in that load are not
   safe to use, regardless of what the cycle printout says
   [CDC-SterilizationGuidelines].
3. Quarantine the affected load. Pull every tray from that cycle
   before any of them reaches a patient. Mark each tray as "Do Not
   Use" and route back to central sterile for reprocessing.
4. Take the sterilizer out of service. Attach the **lockout tag**
   and submit a **work order** to **biomed** with the failed
   indicator result attached. The sterilizer stays down until biomed
   re-validates.
5. File an **incident report** to **risk management**. Even if the
   trays are caught before use, this is a near-miss; risk management
   decides whether any patients received instruments from the
   affected load and what to disclose [TJC-EC].
6. Switch the OR schedule to instruments from a validated
   sterilizer, or delay the cases. The **downtime procedure** for
   sterile processing covers this — borrowed trays, alternative
   instruments, or a pause on elective cases until a second
   sterilizer is online.

**Answer:** Pull the affected load, tag and work-order the
sterilizer, file an incident report, and fall back to the downtime
procedure for the OR schedule until the sterilizer is re-validated.

**Why it matters:** Support-services failures are the ones that fail
silent — no bedside alarm, no visible patient symptom. The biological
indicator exists because you cannot trust a cycle's printout alone
[CDC-SterilizationGuidelines]. The habit here — trust the indicator
over the printout, quarantine the load, tag the device — is the
whole support-services safety model in one scenario.

## Example 4 — AED fails its self-test at shift change

**Scenario:** At the start of a day shift, a nursing assistant
checks the hallway's automated external defibrillator (AED) as part
of routine preventive checks. The AED's status light is red, not
green, and its display shows an unreadable **error code**. The
pads-expiration sticker says the pads are still good.

**What to work out:** Describe the category, the malfunction, and
the response — including what has to happen immediately so the
hallway is not left uncovered.

**Step-by-step:**

1. Name the category. An AED is **therapeutic equipment** and a
   **critical device**; hallway units are required to be ready at
   all times [TJC-EC].
2. Identify the malfunction. A failed self-test or an unreadable
   error code means the AED cannot be trusted to deliver a shock.
   Do not attempt to use this unit on a real patient [AAMI-DeviceSafety,
   ECRI-AlertsList].
3. Replace the unit immediately. Pull a backup AED from the unit's
   stock (every floor keeps at least one) and swap it into the
   hallway bracket so the area is not without coverage while the
   broken unit is out.
4. Tag the broken AED. Attach a **lockout tag** ("Do Not Use") and
   move it to the biomed drop-off location; the device never goes
   back on the bracket until biomed has cleared it.
5. File a **work order** describing the self-test failure and the
   error code. AED repairs are priority tickets — **preventive
   maintenance** schedules exist to catch this before a code is
   called, but when preventive maintenance misses one, the work
   order is how the fix starts [TJC-EC].
6. Document the swap and notify the charge nurse and, per facility
   policy, the department manager. If the AED had been needed
   during the failure window, an **incident report** captures that;
   for a simple catch at self-test with no patient involved, the
   work order is the main artifact.

**Answer:** Swap in a backup AED to keep the hallway covered, tag
and work-order the broken unit, document the swap, and escalate per
policy.

**Why it matters:** Critical devices are checked *because* they can
fail silently — an AED sitting in a bracket looks the same whether
it works or not, which is why the shift-check and **preventive
maintenance** schedule exist [TJC-EC]. Your catch at the daily
check is the whole reason those schedules are required.
