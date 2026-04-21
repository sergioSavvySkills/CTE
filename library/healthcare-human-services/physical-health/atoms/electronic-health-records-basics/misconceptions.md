---
atom_id: electronic-health-records-basics
atom_serial: HHS-PH-0008
sidecar: misconceptions
status: ai-draft
misconception_count: 4
author: claude
reviewer:
review_date:
---

# Common misconceptions — electronic-health-records-basics

Each misconception below is a stable wrong model students return to
even after correction. Vocabulary gaps (forgetting the exact word
*flowsheet*) are not included — those get handled by drill, not by a
misconception slide.

## Misconception 1 — "Deleting a line in the chart makes it go away"

**What students often think:**
"If I type something into a progress note, notice it's wrong, and
delete it before I sign, then it's gone — the chart is clean." Students
treat an EHR like a word processor where backspace means disappearance.

**What's actually true:**
Healthcare charts run under a *correct-not-erase* rule
[TJC-Documentation]. Once you open a note and start typing, the EHR
tracks every keystroke and version. After a note is signed, corrections
happen through an amendment workflow that keeps both the original and
the edit visible. The **audit trail** records who viewed, entered, and
changed what, and when — and it cannot be turned off by the user
[HIPAA-Security]. The chart is a legal record, not a draft document.

**Why the confusion is natural:**
Every other digital writing tool students have used — email drafts,
Google Docs, text messages before sending — rewards the intuition that
delete means gone. EHRs deliberately reverse that intuition because
the chart is evidence.

**How to check whether a student has the correct model:**
Ask: *"You typed a medication dose in the wrong patient's chart,
noticed before signing, and hit delete. Is there any record that this
happened?"* A student with the correct model says yes — the audit
trail captured the entry and the deletion — and can describe the
amendment workflow as the right next step.

## Misconception 2 — "Copy-paste is just a time-saver with no downside"

**What students often think:**
"The last note on this patient is mostly right for today, so I'll paste
it in and tweak a few sentences. It saves me ten minutes." Students
see copy-paste as efficient documentation, not a safety issue.

**What's actually true:**
Copy-paste is a named, studied EHR harm pattern. Pasted text often
carries forward physical-exam findings, review-of-systems bullets, and
assessment language that no longer match today's patient; in safety
reviews, a **copy-paste error** has been tied to missed diagnoses,
propagated wrong information, and chart notes that contradict
themselves internally [ISMP-CopyPaste, AHRQ-EHR-Safety]. Some facilities
flag pasted text automatically; some ban the practice for key sections.
Paste sparingly and re-read what you pasted as if you had typed it
fresh.

**Why the confusion is natural:**
Copy-paste is genuinely efficient in almost every other domain
(reports, emails, code). Students import the habit from those settings
without seeing that a chart note is both a clinical-reasoning artifact
and a legal document — two roles that punish stale text in ways a memo
does not.

**How to check whether a student has the correct model:**
Show a progress note that includes a pasted chest-pain description
from a prior admission — and the patient's current complaint is
headache. Ask what is wrong. A student with the correct model names
the copy-paste pattern, flags the stale text as a safety issue, and
describes re-reading the pasted content before signing.

## Misconception 3 — "Only privacy officers read the audit log"

**What students often think:**
"The audit trail is a theoretical thing — nobody actually looks unless
there's a lawsuit." Students treat access logs as background
infrastructure, not a live deterrent.

**What's actually true:**
Audit logs are reviewed routinely, not only after a complaint
[HIPAA-Security]. High-profile patients (celebrities, co-workers,
patients in the news) trigger automated access reviews. Random samples,
family-member name matches, and access patterns that don't fit a
treatment relationship all draw attention. Clinicians are disciplined
and terminated over curiosity-driven chart snooping every year,
including looks at a neighbor's or co-worker's record — not just for
malicious breaches [AHRQ-EHR-Safety].

**Why the confusion is natural:**
The audit trail is invisible during normal use — there is no pop-up
that says "you have been logged." Students generalize from daily
experience (nothing visible happens when I click) to the wrong
conclusion (nothing invisible happens either).

**How to check whether a student has the correct model:**
Present a scenario: a clinician opens a neighbor's chart "just to see
if she's okay" after hearing an ambulance on the street. Ask what
record of that action exists and what the likely consequence is. A
student with the correct model names the **audit trail**, predicts
that a routine review or complaint will surface it, and names
discipline up to termination as a realistic consequence.

## Misconception 4 — "EHR and EMR are just two words for the same thing"

**What students often think:**
"The initials almost match, everyone uses them interchangeably, so the
distinction is word-policing." Students treat the two terms as
synonyms.

**What's actually true:**
The terms overlap in everyday speech but describe different designs.
An **electronic medical record** is a digital chart inside one
facility's system; an **electronic health record** is a longitudinal
record designed to be exchanged across providers and care settings
[ONC-EHR]. Federal incentive programs pushed U.S. providers from
EMR-shaped systems toward true EHRs because the ability to share —
**interoperability** — is what turns a digital chart into a clinical
asset at the next encounter [ONC-EHR]. The distinction matters because
it names what you should expect from the record: an EHR should
surface outside data; an EMR will not.

**Why the confusion is natural:**
Vendors, colleagues, and even some hospital policies use the terms
interchangeably. The near-identical initials (EMR, EHR) invite the
assumption that they are a spelling preference. Students are imitating
imprecise usage from their environment.

**How to check whether a student has the correct model:**
Ask: *"A clinic advertises that its system is an EMR. What should you
expect to be different from a system advertised as an EHR?"* A student
with the correct model names single-facility scope for the EMR and
cross-provider exchange for the EHR, and references meaningful-use or
interoperability as the reason the distinction exists.
