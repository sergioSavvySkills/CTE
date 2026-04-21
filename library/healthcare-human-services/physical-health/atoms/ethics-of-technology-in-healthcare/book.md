---
atom_id: ethics-of-technology-in-healthcare
atom_serial: HHS-PH-0009
sidecar: book
status: ai-draft
word_count: 2057
author: claude
reviewer:
review_date:
---

# Ethical Issues Raised by Healthcare Technology

## Why this matters

A clinic in rural Montana sees twice as many patients this year as last,
because a nurse practitioner 800 miles away now examines them by video. A
23-year-old receives a direct-to-consumer genetic test as a birthday gift
and, three weeks later, learns that her father is not her biological
father. A smartwatch pings an 18-year-old at 2 a.m. warning of an
irregular heartbeat, and the rest of the night is spent in a panic that
the cardiologist later calls a false alarm. A hospital's new diagnostic
AI flags chest X-rays for pneumonia — but it was trained on scans from
one hospital system, and the radiologists notice it misses cases in
patients who look different from the training set [WHO-AIEthics].

Each of those stories is a real benefit tangled with a real harm. Each
one puts a healthcare worker — maybe you, in a few years — in the middle.
The technology alone does not tell you what to do. The four **ethical
principles** you met in the prerequisite atom (**autonomy**,
**beneficence**, **non-maleficence**, **justice**) do. This atom walks
through five technology categories where those principles collide, and
teaches you to reason about each trade-off clearly enough to explain it
to a patient, a family, or a coworker [Beauchamp-Childress].

## What you should already know

You already know what the four principles are and can roughly define
each — that is the point of the prerequisite *professional ethics in
healthcare*. You also know the difference between a legal rule (what the
law demands) and an ethical rule (what the profession judges to be
right), and you know that the two overlap but are not the same. If
either of those feels shaky, revisit the prereq atom before reading on.
This atom does not re-derive the principles; it applies them.

## Core concept

### AI and machine learning in diagnosis

Diagnostic AI reads X-rays, predicts sepsis, suggests diabetic-retinopathy
referrals, and ranks the order radiologists should review scans. The
technology is real; so are the failures. Models inherit the patterns of
the data they were trained on, and when that data under-represents a
group, the model performs worse for that group. That pattern is called
**algorithmic bias**, and it has been documented in tools for skin
cancer, pulse oximetry, and risk scoring for hospital admission
[WHO-AIEthics].

Three ethical tensions follow. First, **autonomy**: does a patient know
that an algorithm helped make the decision about their care, and have
they consented? Second, **non-maleficence**: a biased model causes harm
that does not look like a clinician's mistake, but it is still harm.
Third, **accountability**: when the AI is wrong, who answers — the
developer, the hospital that bought it, the clinician who trusted the
output, or no one? Regulators are still working this out; the FDA
reviews some AI medical devices before market and is building
post-market monitoring, but the legal picture is evolving [FDA-AIML].

The out-of-scope question here is *how* a neural network learns. For this
atom, the model is a black box with inputs, outputs, and a training set.
You judge it on what goes in, what comes out, and who is affected.

### Genomics and genetic testing

A genetic test is not like a blood-sugar test. A blood-sugar reading tells
you about you, right now. A genetic result tells you about you, about
your biological relatives who never walked into the clinic, and about
risks that may or may not materialize over decades. Every principle
lights up [NIH-PrivacyGenomics].

**Autonomy** requires **informed consent** that covers what is tested,
what the result may reveal about family members, where the data is
stored, and who can see it. A minor donating a cheek swab cannot meaningfully
consent to their data being used for research in 2060.

**Justice** asks who benefits from genetic research — historically,
databases over-represent people of European descent, so the predictions
that come out of them fit those populations better [NIH-PrivacyGenomics].

**Non-maleficence** includes **genetic discrimination**: the fear that
an employer or insurer will use your results against you. The **Genetic
Information Nondiscrimination Act of 2008** (GINA) makes that illegal in
U.S. health insurance and employment — but GINA does not cover life
insurance, disability insurance, or long-term-care insurance, and it
does not apply to the U.S. military. A student who answers "GINA
protects you" is half right [GINA-Law].

The deep biology — how SNPs are typed, how CRISPR edits DNA — belongs to
biotech atoms. What belongs here is the ethical shape: your genome
reveals more than you, for longer than you will live, to more people than
you may realize.

### Telehealth and remote monitoring

**Telehealth** is a clinic visit that happens over video, phone, or
secure messaging. It expanded rapidly during the COVID-19 pandemic and
has stayed. The benefits are real: a patient in a rural county without a
cardiologist can now see one; a patient with a disability does not have
to arrange transportation; a working parent does not lose a day of pay
for a 15-minute visit [ATA-Telehealth].

The ethical trade-offs are equally real. **Justice** surfaces first
through the **digital divide**: telehealth only helps patients who have
broadband, a device, a private place to talk, and the digital skills to
use all three. The patients who most need the access expansion —
low-income, rural, elderly — are the most likely to lack those things.
A program that looks equitable from a city hospital's perspective can
widen inequities for the patients it meant to serve.

**Non-maleficence** shows up in exam quality. A clinician cannot
palpate an abdomen over video, cannot smell infection, cannot check skin
turgor. For some complaints, a video exam is adequate; for others, it is
not; the judgment of when to insist on an in-person visit is itself an
ethical act. **Autonomy** shows up in data streams from remote monitors
— a cardiac monitor sends readings 24/7, and the patient may not realize
how much of their body is being watched, or who sees it [ATA-Telehealth].
Licensure across state lines adds a legal wrinkle; state-by-state rules
are covered in the telemedicine practicum atom, not here.

### Wearables and consumer health tech

A **wearable** is a consumer device — a smartwatch, a ring, a patch,
a headband — that collects continuous data about the body. Most of them
are not regulated as medical devices; a few are [FDA-AIML]. They sit in a
strange place: not a toy, not a diagnostic tool, and sold directly to the
user rather than prescribed.

Four ethical threads run through consumer health tech. First, data
accuracy: a smartwatch rhythm reading is not a 12-lead ECG, and treating
it as one leads to false reassurance or false alarm. Second, the
**beneficence** trap: a well-meaning notification can cause more stress
than the underlying risk it flagged. Third, **autonomy** through consent
for secondary use: the terms of service often give the manufacturer
rights to share de-identified data with researchers, advertisers, or
partners, and few users read those terms. Fourth, **justice** through
employer and insurer access: wellness programs that "reward" wearable
use with lower premiums pressure people to share data that they would
rather keep private, and people who cannot afford a device or lack the
steady schedule the program expects are penalized for circumstances
rather than choices.

### End-of-life technology

A patient in intensive care may be kept alive by **life-sustaining
technology** — mechanical ventilation, extracorporeal membrane
oxygenation (ECMO), dialysis, artificial nutrition and hydration through
a feeding tube. Each one is an engineering achievement. Each one also
raises the possibility that a body is being kept going past what the
person living in it would have wanted [Hastings-EOL].

The four principles collide hard here. **Autonomy** says the patient
decides — but the patient may be unconscious. That is why an
**advance directive** matters: a document, written earlier when the
patient could speak for themselves, that states what they want if they
cannot. **Beneficence** says extend life where life is possible.
**Non-maleficence** says do not impose a dying process that is itself
the harm. **Justice** asks how ICU beds, ECMO circuits, and staff time
are allocated when more patients need them than there are resources.
Those are not theoretical questions; they were lived in 2020 hospitals
in real time.

The prerequisite atom addresses the bioethics theory behind these
trade-offs; this atom names the technology and the principle it stresses.
State-by-state advance-directive law (do you need two witnesses, a notary,
both) is a legal question for a different atom.

### Applying the four principles

A simple habit carries you through every new technology you will meet in
a career: name the technology, name the principle it strengthens, and
name the principle it strains. Almost every ethical case in this field
fits that pattern. A wearable strengthens **beneficence** (the user may
catch a problem early) and strains **autonomy** (consent for data
sharing is buried in a click-through). Telehealth strengthens **justice**
(broader access in principle) and strains **justice** again (the digital
divide narrows access in practice) — two principles, same technology,
opposite directions.

When a case does not resolve cleanly, that is usually the sign that you
are looking at a real ethical problem, not a puzzle with a tidy answer.
Healthcare ethics committees exist precisely for the unresolved cases,
and a clear account of which principle is being served at what cost to
which other principle is the first step into one of those rooms
[Beauchamp-Childress].

Two habits sharpen the practice. First, name the people affected, not
just the technology — patients, family members, clinicians, and any
groups whose data trained the tool. Second, ask who bears the risk if
the technology is wrong, and whether that is the same group that
receives the benefit. When benefit and risk land on different people,
justice is almost always the principle in play.

## Worked through an example

A hospital adopts a diagnostic AI that scores the probability of sepsis
for every patient admitted to the emergency department. After three
months, nurses notice two things: patients flagged by the tool get seen
faster, and the flag fires less often for Black patients than for white
patients with the same vital signs. One measure is a win for
beneficence; the other is a loss for justice and non-maleficence. The
example is walked through step by step in `examples.md`, along with
cases on wearables, genetic testing, and end-of-life care.

## Common confusions

A few intuitions feel right but mislead. Students often think GINA
fully protects them, or that telehealth automatically improves access,
or that a wearable's readings are as reliable as a clinic's equipment,
or that end-of-life technology decisions are obvious once a family is
asked. Each of those is partially true and importantly incomplete.
Corrections and diagnostic probes live in `misconceptions.md`.

## How this connects to other topics

This atom sits downstream of *professional ethics in healthcare*
(which gave you the four principles) and upstream of the clinical
atoms in telemedicine, biotech research and development, and any
future informatics atom that deals with electronic health records and
patient-data exchange. The policy side connects to the legal atoms
that cover HIPAA, consent forms, and state-specific advance-directive
requirements. Students heading into IT or biotech careers will meet
these questions again from the developer's side; students heading into
direct-care careers will meet them from the patient's side.

## Key terms to remember

Five terms anchor this atom: **algorithmic bias**, **informed consent**,
**genetic discrimination**, **digital divide**, and **advance directive**.
Add the four principles — **autonomy**, **beneficence**, **non-maleficence**,
**justice** — and you have the vocabulary that every case analysis in
this field reuses. Supporting terms (**telehealth**, **wearable**,
**life-sustaining technology**, **accountability**) round out the set
and live with definitions and example sentences in `vocabulary.csv`.
Technical vocabulary specific to each technology (neural-net layers,
CRISPR guide RNAs, HL7 data formats) belongs in the deep-dive atoms for
those fields, not here.

## Further reading

Citations in this book resolve to keys in `sources.md`. For the
four-principles framework itself, Beauchamp and Childress's *Principles
of Biomedical Ethics* is the standard reference [Beauchamp-Childress].
For AI-specific ethics in a global health context, the World Health
Organization's 2021 guidance is current and free [WHO-AIEthics]. For the
U.S. genetic-nondiscrimination statute, the EEOC's plain-language
summary of GINA is the primary source [GINA-Law]. For end-of-life
technology questions, the Hastings Center's reports give the
richest treatment at a level a high-school student can follow
[Hastings-EOL].
