---
atom_id: electronic-health-records-basics
atom_serial: HHS-PH-0008
sidecar: book
status: ai-draft
word_count: 1928
author: claude
reviewer:
review_date:
---

# Electronic Health Records — What They Are and How to Use Them Safely

## Why this matters

A patient arrives at the emergency department in the middle of the
night. She cannot remember the name of her heart medication, she is too
short of breath to hold a conversation, and her usual clinic is closed.
Within thirty seconds, the triage nurse pulls up her full medication
list, her last echocardiogram, and an allergy warning on penicillin from
a visit two years ago at a different hospital. None of that was possible
in the paper-chart era. That single lookup is what an **electronic
health record** was built to do — carry a patient's clinical story with
them from setting to setting so the next clinician does not have to
start from scratch [ONC-EHR].

The same system that makes care safer also creates new ways to cause
harm. A click in the wrong patient's chart, a note that carried last
week's story forward into today's encounter, a password shared "just
this once" with a colleague — each is a documented EHR-era harm pattern
[AHRQ-EHR-Safety, ISMP-CopyPaste]. This atom teaches three things you
need to work in a charted-everything environment: what an EHR is,
where information lives inside it, and the safe-practice rules that
keep your entries trustworthy and your access appropriate.

## What you should already know

You should have worked through *HIPAA and patient confidentiality*
before this atom. That prior work covers the legal framework of
protected health information, the privacy rule, and what "minimum
necessary" access means. This atom assumes you already know that
patient information is protected and focuses instead on the
documentation and access habits that live on top of those rules. If
you can state the privacy rule, you are ready to chart under it.

## Core concept

### What an EHR is — and what it is not

An **electronic health record** is a digital, longitudinal record of a
patient's health information that is designed to be shared across
providers and care settings [ONC-EHR]. Every encounter — a primary-care
visit, a hospital admission, a specialist consult, a home-health nurse
visit — writes into the same record. Over a decade, it accumulates a
medical history that no single clinician could reconstruct from memory.

An **electronic medical record** is the older, narrower cousin. An EMR
is a digital chart that lives inside one facility's system, replacing
the paper chart but not traveling with the patient between providers
[ONC-EHR]. Many clinicians and vendors use *EMR* and *EHR* interchangeably
in everyday speech, but the distinction is worth keeping: an EMR
digitizes one clinic's filing cabinet, while an EHR is built to share.
Federal "meaningful use" incentive programs in the 2010s pushed U.S.
providers from EMR-shaped systems toward true EHRs, which is why most
hospitals today run something closer to the second definition.

### Typical chart sections — where to look for what

A clinician who opens an EHR for the first time sees a wall of panels.
Every vendor's interface looks slightly different, but the underlying
sections are the same across systems. Knowing the section names is what
lets you navigate any EHR after a short orientation.

- **Demographics** — name, date of birth, medical record number,
  contact information, emergency contact, insurance. This is how the
  record is identified; a mismatch here is the first sign of a
  wrong-patient problem.
- **Problem list** — the running list of active and resolved diagnoses
  [TJC-Documentation]. Opening the **problem list** is usually the
  first thing a clinician does on a new encounter; it answers *what is
  this patient being treated for?*
- **Allergies** — documented drug, food, and environmental allergies
  with reaction details. Drives automatic drug-allergy alerts during
  ordering.
- **Medications** — current and past medications, including doses,
  routes, and frequencies. Paired with allergies and the problem list,
  this is the clinical core of a reconciled chart.
- **Orders** — active instructions for medications, labs, imaging,
  diet, and activity. An **order** is a clinician's written instruction
  that other staff carry out once it is signed.
- **Progress notes** — dated narrative entries from each encounter.
  A **progress note** records what the clinician observed, thought,
  and did, and becomes part of the permanent record [TJC-Documentation].
- **Results** — returned labs and diagnostic studies, usually with a
  reference range and a flag for abnormal values.
- **Vitals and flowsheets** — a **flowsheet** is a grid that records
  repeated measurements across time (vital signs, intake and output,
  pain scores). The flowsheet is where trends become visible.
- **Imaging** — radiology orders, the images themselves, and the
  radiologist's report.

You do not have to memorize a vendor's menu map. You have to recognize
that every EHR organizes these eight or nine section-types, and that
the quickest way to get oriented on a new system is to find them.

### Charting basics — the rules the record has to follow

Documentation is not free writing; it has accreditation standards
attached. The Joint Commission, which accredits most U.S. hospitals,
sets expectations that every entry be timely, objective, legible (no
longer an issue in typed records, but very much an issue in free-text
notes that omit context), and unambiguously attributable to one author
[TJC-Documentation]. Four rules carry most of the weight:

1. **Objective language.** Write what you observed and what the
   patient reported, in neutral terms. *"Patient rates pain 7/10 and
   is guarding left abdomen"* is objective; *"patient seems
   uncomfortable"* is not.
2. **Time-stamped entries.** The EHR time-stamps automatically; your
   job is not to backdate or forward-date when you write late.
3. **Correct, do not erase.** If you made an error, the chart must
   show both the original entry and the correction, with the reason
   — never overwritten so the first version disappears. Every EHR has
   an amendment workflow for this.
4. **Every entry signed.** Each note, order, or chart edit carries the
   author's electronic signature. An unsigned note is not yet part of
   the legal record.

### Access controls — every chart view is logged

Getting into an EHR uses a unique login tied to you personally. No
shared passwords. The session auto-logs-off after a short idle period
so a walk-away workstation does not expose the chart. What you can see
and change is controlled by **role-based access**: each user is
granted only the chart permissions their job requires [HIPAA-Security].
A registration clerk can update demographics but cannot view a progress
note; a pharmacist can verify orders but cannot sign them.

The part students most often underestimate is the **audit trail**.
Every EHR automatically records which user opened, viewed, or changed
each chart, and when [HIPAA-Security]. Privacy officers can pull that
log at any time. A clinician who opens a neighbor's chart out of
curiosity, a family member's chart without a treatment relationship,
or a celebrity patient's chart to "just look" has left a time-stamped
fingerprint. Consequences run from mandatory retraining to termination
and, for egregious cases, federal penalties under the HIPAA framework
that the prerequisite atom covers.

### Common EHR errors — and how to avoid them

Four harm patterns come up repeatedly in EHR-safety literature, and
you will see each of them within the first few weeks of any clinical
rotation.

- **Copy-paste error.** Carrying text forward from a previous note
  is fast, but the story the text tells may no longer match today's
  patient [ISMP-CopyPaste]. A classic case: a chest-pain description
  from a prior admission gets cloned into every daily note for a
  week, long after the pain has resolved. Paste sparingly, and re-read
  what you pasted as if you had written it fresh.
- **Wrong-patient error.** When two or more charts are open at once,
  an order or note can land in the wrong one [AHRQ-EHR-Safety]. The
  safeguard is to verify two patient identifiers (name plus date of
  birth or medical record number) every time you start to chart.
- **Alert fatigue.** EHRs generate pop-up warnings for drug
  interactions, allergies, duplicate orders, and more. When most of
  those alerts are low-value, clinicians start clicking past them
  reflexively — and a real warning hides inside the stream of noise
  [AHRQ-EHR-Safety]. The fix is organizational (tune the alerts), but
  the personal habit is to slow down and read the alert before you
  dismiss it.
- **Upcoding.** Because documentation drives billing, there is
  pressure to document more than was done so a visit codes at a
  higher level. Upcoding is a compliance violation; chart what you
  did, not what the billing system rewards.

### Interoperability and the patient's role

A single EHR is only as useful as the records it can exchange with
others. **Interoperability** — the ability of different EHR systems
to exchange and use each other's patient data — is what lets the
emergency department in the opening paragraph see a specialist's
note from across town [ONC-EHR]. Health information exchanges
(HIEs) and modern data-exchange standards are the plumbing; you do
not need the plumbing details at this stage, only the concept that
records are meant to travel.

The patient is part of the system too. Federal rules now give
patients the right to read most of their own record through a
**patient portal** — a secure website or app that displays labs,
notes, medications, and appointment histories [ONC-PatientAccess].
Patients can message the care team, view results, and flag
inaccuracies. Treat the portal-facing patient as a documentation
reviewer: write every note as if the patient will read it this
evening, because many of them will.

## Worked through an example

Consider a medical assistant rooming a patient whose chart shows an
allergy to penicillin listed in the allergies section, a current
medication list with lisinopril on it, and a problem list that begins
with *type 2 diabetes mellitus.* Three separate tasks follow: confirm
the allergy with the patient, reconcile the medication list ("are you
still taking all of these?"), and enter today's vitals into the
flowsheet. Four worked examples — a navigation task, a progress-note
drill, a copy-paste audit, and an access-violation scenario — live in
`examples.md`.

## Common confusions

Students often treat an EHR like a word processor and assume a deleted
line is gone, or treat the audit trail as a theoretical privacy
feature that is rarely checked. Both models are wrong in ways that
cause real consequences. Students also conflate EHR and EMR, and
overestimate how much they can learn by clicking around in an
unfamiliar vendor's interface instead of learning the section-types.
Full corrections live in `misconceptions.md`.

## How this connects to other topics

This atom sits between *HIPAA and patient confidentiality* (the legal
frame) and the later atoms on documentation of *vital signs*,
*medication administration*, and clinical-informatics topics like FHIR
APIs and interoperability standards. The EHR is the shared artifact
every one of those atoms writes into; if you can navigate it safely
now, every downstream atom becomes easier.

## Key terms to remember

The anchor terms for this atom are **electronic health record**,
**electronic medical record**, **problem list**, **progress note**,
**flowsheet**, **order**, **audit trail**, **role-based access**,
**copy-paste error**, **wrong-patient error**, **alert fatigue**,
**patient portal**, and **interoperability**. They live next to this
file in `vocabulary.csv` with definitions, example sentences, and
flashcard metadata.

## Further reading

Citations in this book resolve to the keys listed in `sources.md`.
Start with ONC's *Benefits of EHRs* overview for the EHR concept and
meaningful-use history [ONC-EHR]. The Joint Commission's documentation
standards anchor the charting rules [TJC-Documentation]. ISMP's
copy-paste guidance and AHRQ's EHR-safety hub cover the common-error
patterns [ISMP-CopyPaste, AHRQ-EHR-Safety]. For the patient portal and
information-blocking rules, read ONC's *Information Blocking*
topic page [ONC-PatientAccess]. The HIPAA Security Rule summary
documents the access-log and role-based-access backbone
[HIPAA-Security].
