---
atom_id: ethics-of-technology-in-healthcare
atom_serial: HHS-PH-0009
sidecar: examples
status: ai-draft
example_count: 4
author: claude
reviewer:
review_date:
---

# Worked examples — ethics-of-technology-in-healthcare

Each example asks: *which of the four principles is this technology
strengthening, which is it straining, and who bears the trade-off?*
The goal is fluent four-principle reasoning about a specific case, not
a deep dive into how the technology works.

## Example 1 — Sepsis AI in the emergency department

**Scenario:** A hospital adopts a diagnostic AI that scores the
probability of sepsis for every patient admitted to the emergency
department. After three months, the quality team reports two findings:
patients flagged by the tool are seen by a physician 22 minutes faster
on average, and the flag fires less often for Black patients than for
white patients with the same vital signs [WHO-AIEthics].

**What to work out:** Which principles is the AI serving, which is it
straining, and what is the ethical next step?

**Step-by-step:**

1. **Beneficence — served.** Faster evaluation is a clinical win. The
   22-minute reduction translates into earlier antibiotics and better
   outcomes on average.
2. **Non-maleficence — strained.** For the subgroup the flag
   under-fires on, the tool substitutes worse-than-baseline triage for
   ordinary triage. That is a harm caused by the technology, not fixed
   by it.
3. **Justice — strained.** The benefit is landing on one group and the
   risk on another. That is the textbook shape of a justice problem
   [Beauchamp-Childress].
4. **Accountability — ambiguous.** If a missed case leads to a bad
   outcome, is the developer, the hospital, or the physician
   responsible? The hospital contracted for the tool; the developer
   trained it; the physician acted on it.
5. **Next step.** Keep the tool only if the subgroup gap can be closed
   (retrain, recalibrate, or override algorithmically). In the interim,
   clinicians must not let the absence of a flag outweigh their own
   judgment.

**Answer:** The AI serves beneficence on average but strains
non-maleficence and justice for a specific subgroup, and accountability
is unsettled. The ethical response is to fix the bias before continued
use, not to remove the tool reflexively or keep it as-is.

**Why it matters:** This is the shape of almost every real AI-in-
healthcare case: average wins and subgroup losses. Healthcare workers
who cannot articulate both sides cannot advocate for patients the tool
is failing.

## Example 2 — Consumer smartwatch flags atrial fibrillation

**Scenario:** An 18-year-old's smartwatch sends a notification at
2 a.m. warning of an irregular heart rhythm. They spend the night
anxious, visit urgent care in the morning, receive a 12-lead ECG, and
are told the rhythm is normal and the watch was wrong [FDA-AIML].

**What to work out:** Did the wearable help or harm, and which principle
carries the analysis?

**Step-by-step:**

1. **Beneficence — intended.** The watch is designed to catch a real
   problem early. Some users genuinely benefit from early detection.
2. **Non-maleficence — strained in this case.** A false alarm caused a
   night of anxiety, an unnecessary clinic visit, a co-pay, and several
   hours of lost sleep. That is harm, even though no one intended it.
3. **Autonomy — partially served, partially strained.** The user chose
   to wear the device and to act on its alerts, which serves autonomy.
   But the terms of service for the app send de-identified data to the
   manufacturer, and the user did not read those terms. That is
   consent in form but not in substance.
4. **Justice — present in background.** Wearables cost money. Users
   who can afford them receive the benefit and the harm; users who
   cannot, do not.
5. **Correct framing of the device.** The watch is a screening tool, not
   a diagnostic one. A single alert is a reason to check in, not a
   diagnosis.

**Answer:** The benefit of early detection is real but comes with a
false-alarm cost paid by the user. Pretending the device is diagnostic
amplifies that cost.

**Why it matters:** Patients increasingly arrive with wearable data.
Healthcare workers need to validate the concern (beneficence) without
treating the consumer-grade reading as a clinical measurement
(non-maleficence). The **wearable** is a starting point for a
conversation, not an end point.

## Example 3 — Direct-to-consumer genetic test reveals a family secret

**Scenario:** A 23-year-old buys a direct-to-consumer genetic test as a
birthday gift. Three weeks later the report shows that the person
listed as her father on her birth certificate is not her biological
father. She did not expect this; her parents did not consent to her
taking the test.

**What to work out:** Which ethical principles are stressed, and what
protections existed or failed?

**Step-by-step:**

1. **Autonomy — served for the test-taker.** She consented to her own
   test.
2. **Autonomy — strained for her parents.** Her genetic result reveals
   information about her biological parents who never consented to any
   test [NIH-PrivacyGenomics]. Genetic data is inherently familial.
3. **Informed consent — incomplete.** A consent form that covers the
   test-taker's own data does not fully cover the implications for
   relatives. Companies now include warnings, but warnings are not
   consent from the people whose data is inferred.
4. **Non-maleficence — real harm.** Disclosure of non-paternity has
   caused divorces, estrangement, and psychological harm in documented
   cases.
5. **Justice — background.** Genetic databases over-represent European-
   descent populations, so interpretations of the same variant are more
   accurate for some customers than for others.
6. **Legal backstop is limited.** GINA does not apply to direct-to-
   consumer companies' terms of service, and does not cover life
   insurance [GINA-Law]. The user is protected less than she may
   assume.

**Answer:** The principle most stressed is autonomy — not the
test-taker's autonomy, but the relatives' autonomy over information
they never chose to disclose. Informed consent for genetic testing has
to cover family implications to be meaningful.

**Why it matters:** Direct-to-consumer testing is now cheap and common,
and healthcare workers field the questions that arise when results
surprise families. Naming whose autonomy is at stake is the first move.

## Example 4 — Ventilator decision without an advance directive

**Scenario:** A 78-year-old patient is admitted after a large stroke and
placed on a ventilator. She is unconscious and has no **advance
directive**. Her three adult children meet with the ICU team after
72 hours: one wants to continue life support indefinitely, one wants to
withdraw it today, one is unsure.

**What to work out:** Which principles are in play, and how should the
team proceed?

**Step-by-step:**

1. **Autonomy — the center of the case.** Autonomy still belongs to the
   patient; she simply cannot express it. Without an advance directive,
   the team and family must reconstruct her wishes from prior
   conversations, values, and written evidence [Hastings-EOL].
2. **Beneficence and non-maleficence — balanced against each other.**
   Continued life support may extend life (beneficence) or may extend a
   dying process the patient would have rejected (non-maleficence).
   Which one it is depends on what *she* would have wanted.
3. **Justice — ICU resources.** ICU beds and ventilators are finite.
   Allocation pressure does not override autonomy, but it does make
   avoidable prolongation an ethical issue beyond the one patient.
4. **Family role — witnesses, not voters.** Children who disagree are
   not casting votes. Each is offering evidence about their mother's
   values, and an ethics consult or palliative-care team helps weigh
   the evidence.
5. **Correct next step.** The team documents what is known of the
   patient's prior wishes, requests an ethics consultation, and
   schedules a family meeting structured around her values rather than
   the children's preferences.

**Answer:** The principle at stake is autonomy, reconstructed from
evidence; **life-sustaining technology** decisions without an advance
directive are the hardest version of the four-principles case, and
procedural safeguards (ethics consult, structured family meeting) exist
precisely because no single person can decide cleanly.

**Why it matters:** End-of-life technology forces every principle into
the same room. Healthcare workers who can name the principle at stake —
and can distinguish between the patient's autonomy and the family's
preferences — help the team avoid both reflexive continuation and
reflexive withdrawal.
