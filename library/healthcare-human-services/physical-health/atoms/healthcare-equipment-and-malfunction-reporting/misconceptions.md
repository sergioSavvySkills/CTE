---
atom_id: healthcare-equipment-and-malfunction-reporting
atom_serial: HHS-PH-0015
sidecar: misconceptions
status: ai-draft
misconception_count: 4
author: claude
reviewer:
review_date:
---

# Common misconceptions — healthcare-equipment-and-malfunction-reporting

Each misconception below is a stable wrong model students return to
even after correction. Vocabulary gaps — forgetting what *MDR* stands
for, for example — are not included; drill handles those.

## Misconception 1 — "Silencing the alarm means the device is fine"

**What students often think:**
"The pump beeped, I hit the silence button, and the beeping stopped
— so the problem's resolved. I don't need to read the message." The
alarm is treated as a nuisance signal that just needs to be turned
off.

**What's actually true:**
An **alarm** is the device asking for attention, not the device
announcing that the problem is over [ECRI-AlertsList]. Silencing
only suppresses the sound; it does not fix the underlying fault,
and in many devices the cause stays active until someone addresses
it. A correct read-then-respond habit is: silence to protect the
patient's environment, then read the message on the screen, then
decide — is this patient physiology (a real heart-rate change), a
technical cause (a displaced lead, a kinked line), or an **error
code** pointing at the device itself? If the device is the
problem, pull it from service and file a **work order**
[TJC-EC, AAMI-DeviceSafety].

**Why the confusion is natural:**
Every other alarm in a student's daily life — a microwave timer, a
phone notification, a smoke detector battery chirp — is resolved by
silencing it. Hospital alarms invert that training: the sound is
secondary; the message is the signal. "Alarm fatigue" in the
literature is what this misconception looks like at scale.

**How to check whether a student has the correct model:**
Ask: *"An IV pump is alarming 'occlusion — downstream.' You silence
it and the beeping stops. Is the infusion safe to continue?"* A
student with the correct model says no — silencing does not clear
the occlusion — and describes reading the message, tracing the line
for a kink or backup, and switching to a backup pump if the cause
is not obvious.

## Misconception 2 — "If the machine still turns on, it's safe to use"

**What students often think:**
"The glucose meter has a cracked case, but it still powers on and
reads a strip — so I can finish the last few checks before sending
it in." Cosmetic or structural damage is treated as separate from
functional safety as long as the device boots.

**What's actually true:**
Visible physical damage is itself a take-it-out-of-service signal
regardless of whether the device appears to function. A cracked
housing can mean electrical leakage, a compromised fluid seal, or
an internal component that is no longer calibrated; a frayed power
cord can ignite or shock someone; a cracked centrifuge rotor is a
catastrophic-failure risk the next time it spins [AAMI-DeviceSafety,
TJC-EC]. Policy in every accredited facility — and the
**lockout/tagout** logic that backs it — is that a damaged device
gets the "Do Not Use" **lockout tag** and goes to **biomed**, full
stop [OSHA-LOTO]. The next clinician who picks it up has no way to
know what was wrong; the tag is how the system communicates.

**Why the confusion is natural:**
Consumer electronics teach the opposite lesson: a phone with a
cracked screen that still works is fine to keep using, and replacing
it feels wasteful. Healthcare equipment is held to a higher standard
because the failure mode is not *the device stops working* but
*the device gives a wrong reading or delivers the wrong dose.*
Students import the consumer intuition and have to unlearn it.

**How to check whether a student has the correct model:**
Show a photo (or describe) a glucose meter whose case is cracked
along the side but which still produces a reading. Ask whether to
use it for the next patient check and what the next action is. A
student with the correct model says no, tags the device, places it
in the biomed drop-off, and submits a work order.

## Misconception 3 — "'Report it' is one thing I do"

**What students often think:**
"If something goes wrong with a device, I tell my supervisor. That's
the report. It's one step." Reporting is collapsed into a single
conversation.

**What's actually true:**
Equipment reporting is a layered workflow, not a single action.
Three separate tracks can fire for the same event. The **work
order** goes to biomed so the device gets inspected and repaired
[TJC-EC, AAMI-DeviceSafety]. The internal **incident report** goes
to **risk management** so the facility can investigate patient harm
or near-misses and change workflows if needed [TJC-EC]. For a
device-related patient death or serious injury, the facility — not
the bedside clinician personally — files a **medical device
report** (MDR) with the FDA [FDA-MDR]. Which tracks fire depends on
what happened: a routine malfunction with no patient involvement is
usually just a work order; a malfunction that delayed care is a
work order plus an incident report; a serious device-related
injury is all three. Telling your supervisor is how the process
starts, not the end of it.

**Why the confusion is natural:**
In most school and workplace settings students have seen,
"reporting" really is one step — you tell a teacher or a manager
and the system takes over. Healthcare layers reporting across
multiple offices with different mandates (safety, regulation,
engineering) because each one does something the others cannot.
Students default to the one-step model until they are walked
through the three tracks.

**How to check whether a student has the correct model:**
Present a scenario: a ventilator shut down briefly on a critical
patient who was transferred to a backup circuit and survived, but
required rescue. Ask what reporting needs to happen and to whom. A
student with the correct model names all three tracks: a work
order to biomed, an incident report to risk management that same
shift, and an MDR submission that the facility will file with the
FDA because a device may have contributed to serious injury.

## Misconception 4 — "FDA only reviews devices before they go on sale"

**What students often think:**
"The FDA approves devices before they reach the market, and after
that it's up to hospitals and manufacturers to handle problems."
Post-market device oversight is invisible to the student.

**What's actually true:**
The FDA has a live post-market role. **Medical device reporting**
(MDR) is a mandatory federal program through which manufacturers,
importers, and hospital user facilities submit reports on
device-related patient deaths, serious injuries, and certain
malfunctions; the FDA aggregates those reports to detect patterns
that no single facility could see alone [FDA-MDR]. When the
evidence warrants it, the FDA and the manufacturer issue a device
recall — a notice that tells facilities in the field to remove,
fix, or stop using specific equipment [FDA-DeviceRecalls]. The
bedside clinician does not file the MDR personally; they file the
internal **incident report** that feeds risk management, which in
turn files the MDR. But the clinician's report is the source data
for the whole post-market surveillance system. Skipping the
internal report because "the FDA can't do anything anyway" is
exactly wrong — that report is how the FDA sees the problem.

**Why the confusion is natural:**
Drug-approval coverage in the news focuses on the pre-market
approval step, and students generalize that pattern to devices.
The post-market safety pipeline is slower and less visible, and the
acronym MDR rarely appears outside of healthcare settings.

**How to check whether a student has the correct model:**
Ask: *"A hospital files twelve incident reports in a year describing
the same brand of infusion pump over-delivering medication. How does
the FDA learn about this?"* A student with the correct model names
the MDR path — the hospital's risk management office files MDRs for
the serious injuries, the FDA aggregates reports across facilities,
and the FDA and manufacturer may issue a recall if the pattern is
confirmed [FDA-MDR, FDA-DeviceRecalls].
