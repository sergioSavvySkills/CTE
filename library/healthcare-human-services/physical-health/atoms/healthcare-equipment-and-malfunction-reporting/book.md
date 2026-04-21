---
atom_id: healthcare-equipment-and-malfunction-reporting
atom_serial: HHS-PH-0015
sidecar: book
status: ai-draft
word_count: 2033
author: claude
reviewer:
review_date:
---

# Healthcare Equipment and Malfunction Reporting

## Why this matters

An IV pump on a pediatric floor beeps twice and then shows a small
line of text: *occlusion — upstream.* The nurse who walks in has a
choice. She can silence the alarm and keep the infusion running. She
can unclip a kink she sees in the tubing and clear the alert. Or she
can stop, read the screen, realize the pump has been flashing the
same code for fifteen minutes, and pull it out of service. The right
move depends on whether she recognizes the pattern — is this a
routine nuisance alert, or a sign that the device is not delivering
the dose the chart says it is? [ECRI-AlertsList]

Every healthcare worker, from a first-day medical assistant to a
lab technologist, shares the same equipment floor. They also share a
common reporting backbone — a way to pull unsafe equipment from
service, a way to call for a repair, and a way to escalate when a
device may have harmed a patient [TJC-EC, FDA-MDR]. This atom gives
you three things: a map of the equipment you will meet across the
five health science systems, the visible signs that something is
wrong with a device, and the reporting path that every hospital
expects you to follow.

## What you should already know

You should already know what a healthcare facility is and roughly
what the five health science systems do: diagnostic, therapeutic,
health informatics, support services, and biotech research and
development. You do not need to know how any particular machine
works internally — imaging physics and analyzer chemistry live in
their own atoms. You also do not need biomed-technician skills; this
atom stops at the point where you recognize a problem and hand the
device off.

## Core concept

### Diagnostic equipment

Diagnostic equipment is what clinicians use to see what is happening
inside a patient. Imaging machines — X-ray, CT, MRI, and ultrasound —
produce pictures of bones, organs, and blood flow. Laboratory
analyzers run chemistry, hematology, and microbiology panels. A
12-lead EKG records the heart's electrical activity, and a
spirometer measures how much air a patient can move in and out of
the lungs. Point-of-care devices — the glucose meter at the bedside,
the urine pregnancy test in triage — bring a small lab result to
the patient in a minute or two [AAMI-DeviceSafety].

Signs that diagnostic equipment is failing often hide inside the
result it produces. A lab analyzer flashes an **error code** when a
reagent is low; an EKG cable with a cracked pin produces artifact
that a trained reader sees as wavy baseline rather than cardiac
signal; a glucose meter with an expired test strip returns a number
that looks plausible but is not. Do not trust a reading from a
device that is also showing an alert, and do not re-run the same
sample on the same suspect device hoping for a better number.

### Therapeutic equipment

Therapeutic equipment acts on the patient. IV pumps deliver fluids
and medications at programmed rates. Ventilators breathe for
patients who cannot. Defibrillators — both the automated external
defibrillator (AED) and the manual unit in a crash cart — deliver
a timed electrical shock. Hospital beds raise, lower, and weigh.
Dialysis machines filter blood for patients whose kidneys cannot.
Radiation-therapy units deliver precise doses to tumors.

Several of these are **critical devices**: a failure during use
could directly cause patient harm, so they get priority preventive
maintenance, redundancy (a second ventilator on standby, a backup
IV pump on the floor), and the tightest response when something
goes wrong [TJC-EC]. A defibrillator that fails a self-test at the
start of a shift is taken out of service immediately and replaced;
nobody waits for the next code to find out whether it will charge.

### Health informatics equipment

Health informatics equipment is how clinical information moves. An
EHR workstation is the most familiar example: the computer on wheels
or the wall-mounted terminal where a clinician opens the chart.
Barcode scanners verify that the medication about to be given matches
the order. Telemetry monitors display a patient's heart rhythm and
vital signs at a central station. Patient portals let patients read
their own record, and health information exchange (HIE) infrastructure
moves records between facilities [AAMI-DeviceSafety].

Informatics-equipment failures are as dangerous as mechanical ones,
just quieter. A frozen EHR workstation means a nurse cannot sign off
a medication. A miscalibrated telemetry monitor shows a rhythm that
looks fine when the patient is actually in a dangerous arrhythmia.
When the scanners or workstations go down, the unit switches to its
**downtime procedure** — the pre-planned workflow (paper orders,
two-nurse paper verification, call-through-to-pharmacy) that the
floor uses until service returns.

### Support-services equipment

Support services keeps the building functional. Sterilizers (steam
autoclaves and low-temperature sterilizers) decontaminate
instruments between patients [CDC-SterilizationGuidelines].
Transport carts move patients and supplies; dietary carts move food
trays; laundry equipment handles linens at volumes a home washer
would buckle under. HVAC systems with HEPA filtration keep operating
rooms and isolation rooms at the right air pressure, temperature,
and cleanliness. Fire-suppression systems and the call-light system
at every bedside are also support-services equipment.

Failures here are easy to miss because they rarely alarm at the
bedside. A sterilizer that fails its weekly biological indicator
test means instruments that went through that load are not safe to
use on patients [CDC-SterilizationGuidelines]. A HEPA filter that
has not been changed on schedule means the isolation room is no
longer protecting the next patient. A stuck call-light button means
a patient with chest pain may not be able to reach a nurse. Support-
services equipment tends to fail silently, which is why preventive
checks and scheduled inspections matter more here than anywhere
else.

### Biotech research and development equipment

Biotech R&D equipment sits in the lab rather than at the bedside.
Centrifuges spin samples into layers by density. PCR thermocyclers
amplify DNA through controlled heating cycles. Flow cytometers
count and sort cells. Microscopes — light, fluorescence,
electron — let researchers see samples at scale. Biosafety cabinets
contain airborne pathogens and protect the worker who handles them
[CDC-SterilizationGuidelines].

A cracked centrifuge rotor, an unbalanced load spinning at 10,000
rpm, a biosafety-cabinet airflow alarm, or a PCR machine whose
heating block is out of calibration are all failures that can put
staff or results at risk. The same habits apply as at the bedside:
read the alert, stop using the device, label it, and file a repair
request.

### Signs of malfunction

A **malfunction** is any failure of equipment to operate as
designed. The visible signals cluster into five patterns:

- **Alarms.** Auditory or visual signals the device itself raises
  when a measurement or internal check is out of range. An **alarm**
  deserves a read before it deserves a silence; the message on the
  screen tells you whether the issue is physiological (the patient's
  heart rate is really high) or technical (a lead came off) [ECRI-AlertsList].
- **Error codes.** Short codes or numeric messages that identify
  a specific internal fault, usually listed in the manufacturer's
  manual. Do not attempt to clear an **error code** by power-cycling
  a device without reading what the code means.
- **Abnormal readings.** Values that do not fit the patient in front
  of you — a blood pressure of 60/40 on a chatty, walking patient —
  or do not match a second check on a different device. Trust your
  pattern recognition: when the number and the patient disagree,
  recheck with another instrument before you act on the number.
- **Physical damage.** Frayed power cords, cracked housings, bent
  probes, dented bed rails, cracked centrifuge rotors. Visible damage
  is a take-it-out-of-service signal by itself, even if the device
  still appears to power on.
- **Unexpected behavior.** The screen flickers, the pump delivers
  faster than programmed, the sterilizer's cycle time is shorter
  than it should be, the ventilator restarts on its own. Unexpected
  behavior is how subtle failures announce themselves.

### Reporting workflow

When you see one of those signs, the response is the same regardless
of department:

1. **Stop using the device.** If a patient is connected to it, switch
   to a backup device or a manual alternative before you address the
   failed equipment.
2. **Label the device "Do Not Use."** Attach a **lockout tag** — the
   brightly colored "Do Not Use" label every unit stocks — and move
   the device to a clearly marked out-of-service location. This is the
   healthcare application of the **lockout/tagout** principle
   [OSHA-LOTO]: once an item is tagged, no one else may use it until
   it is cleared.
3. **File a work order.** A **work order** is the formal electronic
   request to the facility's **biomed** (clinical-engineering, sometimes
   called healthcare-technology-management) team. Describe what
   happened, which device (asset tag or serial number), and any error
   codes [AAMI-DeviceSafety, TJC-EC].
4. **If a patient was harmed or could have been harmed, file an
   incident report.** An **incident report** is the internal document
   that starts the **risk management** investigation. Near-misses
   count — the failure you caught before it reached the patient is
   exactly what risk management wants to see [TJC-EC].
5. **If a patient was seriously injured or died, the facility files
   an MDR.** **Medical device reporting** (**MDR**) is the federal
   FDA path for device-related patient harm at hospitals and other
   user facilities [FDA-MDR]. The MDR is not filed by the bedside
   clinician; risk management and the facility's regulatory team
   handle it. The clinician's job is to make sure the incident report
   and the device itself reach them quickly and intact.

Behind all of this sits **preventive maintenance** — the scheduled
inspection, cleaning, and testing cycles that biomed runs to catch
problems before they reach a patient [TJC-EC]. Preventive maintenance
is why most of the devices you use today will work today; the
reporting workflow is how the system learns from the ones that
don't.

## Worked through an example

Picture a nurse finishing a shift change who finds an IV pump
alarming *occlusion — downstream.* The tubing is not kinked. She
switches the patient to a backup pump, labels the first pump with a
"Do Not Use" tag, submits a work order describing the alarm, and
files an incident report because the infusion paused for an
unknown period. Risk management reviews the report the next day and
decides whether any patient harm occurred that would trigger MDR
filing. Four worked examples — a faulty glucose meter, a cracked
ventilator circuit, a sterilizer biological-indicator failure, and a
defibrillator that fails its self-test — live in `examples.md`.

## Common confusions

Students often assume that clearing an alarm is the same as fixing
the device, that cosmetic damage is not a safety issue if the
machine still powers on, and that "reporting" is one action rather
than two (internal incident report plus, when serious harm is
involved, the external FDA MDR). Full corrections and diagnostics
live in `misconceptions.md`.

## How this connects to other topics

This atom sits next to the electronic-health-records atom (the EHR
is itself informatics equipment with its own downtime procedure)
and the personal-protective-equipment atom. Deeper biomedical-
engineering troubleshooting lives in the biomed-technician track;
the FDA 510(k) / premarket-approval mechanics for getting a device
onto the market live in a regulatory atom; device cybersecurity
lives in the medical-device infosec atom. Everything here stops at
"recognize and report."

## Key terms to remember

The anchor terms for this atom are **malfunction**, **alarm**,
**error code**, **lockout tag**, **work order**, **biomed**,
**risk management**, **incident report**, **MDR**,
**medical device reporting**, **critical device**,
**preventive maintenance**, and **downtime procedure**. Each has a
row in `vocabulary.csv` with a definition, a sentence in context,
and flashcard metadata.

## Further reading

Citations in this book resolve to the keys listed in `sources.md`.
The FDA's MDR page anchors the federal reporting path [FDA-MDR], and
the FDA device-recalls page frames how wider-scale issues reach the
field [FDA-DeviceRecalls]. The Joint Commission's Environment of
Care standards set the hospital-side equipment-management
expectations [TJC-EC], AAMI publishes the professional-society
standards on medical instrumentation [AAMI-DeviceSafety], OSHA's
lockout/tagout rule covers the Do-Not-Use tagging mechanism
[OSHA-LOTO], and the CDC's disinfection-and-sterilization guideline
anchors the sterilizer and biosafety-cabinet pieces
[CDC-SterilizationGuidelines]. ECRI's Top 10 Health Technology
Hazards list gives year-over-year examples of the most common
real-world failures [ECRI-AlertsList].
