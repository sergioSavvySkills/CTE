---
template_id: tx-principles-of-health-science-2022
state: TX
course_name: Principles of Health Science
course_code: 127.403
subcluster: physical-health
grade_band: HS
credit_hours: 1
credential_targets: []
framework_version: 2015 adopted; amended 4/7/2022 (47 TexReg 1677)
status: draft
reviewer:
review_date:
---

# Principles of Health Science (TX §127.403)

Broad survey of the five health science systems (therapeutic, diagnostic,
health informatics, support services, biotechnology research and development)
for grades 9-10. Builds the foundation students need before specializing in
Anatomy and Physiology (§127.423), Health Science Theory (§127.422), Medical
Terminology, or Health Science Clinical.

PoHS has **no anchor industry credential** at L1 — it is pre-credential
preparation — so `credential_targets` is empty. Career awareness and
professionalism are woven through the course rather than leading to a
specific exam.

Every atom is a 45-minute period; block-schedule teachers combine two
atoms per day. The course is delivered **digitally end-to-end**: all lab
content runs as simulations or applied tasks in the browser. Physical
supplies are never required. Skill atoms (hand hygiene, PPE) are assessed
via video-demo walkthroughs, step-ordering interactives, and scenario-based
mastery checks — no in-person check-off.

§127.403(c)(1) employability elements are **threaded throughout the course**,
not a front-loaded filler unit: `professionalism-and-employability-in-healthcare`
in u01 introduces the standards, then cross-unit performance tasks and applied
tasks continue to exercise them — u02 team-collaboration rubrics (c1B
cooperate as team member), u04 communication-precision prompts (c1A express
ideas clearly), u05 discussion-based ethical reasoning (c1A precise
language), u07 safety-response protocols (c1C employer expectations and
work habits), and the u08 capstone rubric (all three).

## Unit ordering rationale

**Units 1-2 build motivation and context** (who works in healthcare, what
the career paths look like, how the team functions) before any clinical
content. **Unit 3 is the science spine** — homeostasis, Maslow, and
lifespan anchor later modules on wellness (u06), ethics (u05), and safety
(u07). **Unit 4 front-loads medical vocabulary and communication** so
later units can use medical terms, interpret data, and read technical
material without re-teaching. **Unit 5 (ethics/law) sits in the middle** —
heaviest cognitive load placed after students have tools to work with it.
**Units 6-7** deliver the humanistic and safety halves of practice.
**Unit 8 closes the loop** — healthcare technology spans all 5 systems,
adds data interpretation, and ties back to Unit 1 careers.

Performance tasks anchor the four units where an integrated project
delivers more than any single atom can: the **Career Pathway Portfolio**
(u01), the **Ethics Case Analysis** (u05, mid-course integrator that
pulls in u01-u04 context), the **Safety Scenario Response** (u07), and
the **Technology Systems Map capstone** (u08). The u08 capstone PT is
explicitly integrative — its rubric requires students to cite evidence
from the science, communication, ethics, wellness, and safety units, not
just the technology unit content.

```yaml
units:
  - unit_id: u01
    title: "Entering Health Science"
    weeks: 2
    slots:
      - slot: 1
        atom_id: professionalism-and-employability-in-healthcare
      - slot: 2
        atom_id: healthcare-careers-and-pathways
      - slot: 3
        atom_id: history-of-healthcare
        generate:
          lesson: true
          classwork: guided_practice
          quiz: exit_ticket
          simulation: false
          video: true
      - slot: 4
        atom_id: health-economics-and-government-impact
        generate:
          lesson: true
          classwork: guided_practice
          quiz: exit_ticket
          simulation: false
          video: true
      - slot: 5
        atom_id: healthcare-delivery-system-overview
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true

  - unit_id: u02
    title: "The Healthcare Team"
    weeks: 2
    slots:
      - slot: 1
        atom_id: healthcare-team-roles
      - slot: 2
        atom_id: professional-organizations-and-credentialing
      - slot: 3
        atom_id: leadership-and-teamwork-in-healthcare
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u03
    title: "How the Body Works"
    weeks: 3
    slots:
      - slot: 1
        atom_id: body-organization-and-directional-terms
      - slot: 2
        atom_id: body-systems-overview
      - slot: 3
        atom_id: homeostasis-and-biological-processes
        generate:
          lesson: true
          classwork: guided_practice
          quiz: exit_ticket
          simulation: false
          video: true
      - slot: 4
        atom_id: maslows-hierarchy-and-patient-needs
        generate:
          lesson: true
          classwork: guided_practice
          quiz: exit_ticket
          simulation: false
          video: true
      - slot: 5
        atom_id: lifespan-development-stages
    unit_generate:
      game: true
      summative_quiz: true
      performance_task: false

  - unit_id: u04
    title: "Communicating in Healthcare"
    weeks: 3
    slots:
      - slot: 1
        atom_id: medical-terminology-word-parts
      - slot: 2
        atom_id: common-medical-abbreviations
      - slot: 3
        atom_id: therapeutic-communication
      - slot: 4
        atom_id: conflict-resolution-in-healthcare
      - slot: 5
        atom_id: technical-communication-in-health-science
    unit_generate:
      game: true
      summative_quiz: true
      performance_task: false

  - unit_id: u05
    title: "Ethics, Law, and Patient Rights"
    weeks: 4
    slots:
      - slot: 1
        atom_id: professional-ethics-in-healthcare
        generate:
          lesson: true
          classwork: discussion
          quiz: exit_ticket
          simulation: false
          video: false
      - slot: 2
        atom_id: hipaa-and-patient-confidentiality
      - slot: 3
        atom_id: patient-rights-and-informed-consent
        generate:
          lesson: true
          classwork: discussion
          quiz: exit_ticket
          simulation: false
          video: false
      - slot: 4
        atom_id: scope-of-practice-and-licensure
        generate:
          lesson: true
          classwork: discussion
          quiz: exit_ticket
          simulation: false
          video: false
      - slot: 5
        atom_id: malpractice-negligence-and-laws
        generate:
          lesson: true
          classwork: discussion
          quiz: exit_ticket
          simulation: false
          video: false
      - slot: 6
        atom_id: ethics-of-technology-in-healthcare
        generate:
          lesson: true
          classwork: discussion
          quiz: exit_ticket
          simulation: false
          video: true
    unit_generate:
      game: true
      summative_quiz: true
      performance_task: true

  - unit_id: u06
    title: "Wellness, Relationships, and Cultural Practice"
    weeks: 2
    slots:
      - slot: 1
        atom_id: wellness-and-disease-prevention
      - slot: 2
        atom_id: healthy-relationships-and-wellbeing
      - slot: 3
        atom_id: cultural-competence-in-healthcare
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u07
    title: "Safety and Infection Control"
    weeks: 3
    slots:
      - slot: 1
        atom_id: healthcare-regulatory-agencies
      - slot: 2
        atom_id: standard-precautions-and-chain-of-infection
      - slot: 3
        atom_id: hand-hygiene-technique
      - slot: 4
        atom_id: personal-protective-equipment-use
      - slot: 5
        atom_id: fire-and-emergency-safety
      - slot: 6
        atom_id: body-mechanics-and-safe-patient-handling
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true

  - unit_id: u08
    title: "Healthcare Technology and Data"
    weeks: 3
    slots:
      - slot: 1
        atom_id: healthcare-equipment-and-malfunction-reporting
      - slot: 2
        atom_id: electronic-health-records-basics
      - slot: 3
        atom_id: vital-signs-overview
      - slot: 4
        atom_id: applied-math-and-data-in-health-science
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true
```

## Pacing summary

Eight units spanning ~22 weeks of instruction, leaving ~14 weeks across a
36-week year for unit review, mid-term and final exams, state-testing
windows, and the four performance tasks (which expand beyond the slot
count of their host unit).

## Coverage note

TEKS coverage is derived through the slot → atom → crosswalk chain and is
not hand-authored in this template. Before promoting to `status: active`
run the coverage report against
`library/healthcare-human-services/physical-health/crosswalks/texas/crosswalk.csv`
to verify every §127.403(c) standard hits at least one slot. Current state
per SME round 3.1: **50 / 50 standards have a primary-aligned atom (100%).**

## Unit inventory — what's in each unit

| unit | title | weeks | primary atoms | supporting / cross-scope embedded | covers §127.403 KS areas |
|---|---|:-:|---|---|---|
| u01 | Entering Health Science | 2 | professionalism-and-employability-in-healthcare, healthcare-careers-and-pathways, history-of-healthcare, health-economics-and-government-impact | healthcare-delivery-system-overview | (c)(1), (c)(2)M-O, (c)(5), (c)(6), (c)(7)A |
| u02 | The Healthcare Team | 2 | healthcare-team-roles, professional-organizations-and-credentialing, leadership-and-teamwork-in-healthcare | — | (c)(4), (c)(7)B, (c)(8) |
| u03 | How the Body Works | 3 | homeostasis-and-biological-processes, maslows-hierarchy-and-patient-needs, lifespan-development-stages | body-organization-and-directional-terms, body-systems-overview | (c)(2)G, I, J |
| u04 | Communicating in Healthcare | 3 | medical-terminology-word-parts, therapeutic-communication, conflict-resolution-in-healthcare, technical-communication-in-health-science | common-medical-abbreviations | (c)(2)C-F, (c)(3) |
| u05 | Ethics, Law, and Patient Rights | 4 | professional-ethics-in-healthcare, patient-rights-and-informed-consent, scope-of-practice-and-licensure, malpractice-negligence-and-laws, ethics-of-technology-in-healthcare | hipaa-and-patient-confidentiality | (c)(9), (c)(10)A, D |
| u06 | Wellness, Relationships, and Cultural Practice | 2 | wellness-and-disease-prevention, healthy-relationships-and-wellbeing, cultural-competence-in-healthcare | — | (c)(2)K-L, P-Q, (c)(10)B, C, E |
| u07 | Safety and Infection Control | 3 | healthcare-regulatory-agencies, standard-precautions-and-chain-of-infection, fire-and-emergency-safety, body-mechanics-and-safe-patient-handling | hand-hygiene-technique, personal-protective-equipment-use | (c)(2)H, (c)(11) |
| u08 | Healthcare Technology and Data | 3 | healthcare-equipment-and-malfunction-reporting, applied-math-and-data-in-health-science | electronic-health-records-basics, vital-signs-overview | (c)(2)A-B, (c)(12) |
| **total** | | **22** | **28 primary atoms** | **9 support/cross-scope** | **all 12 KS areas covered** |

c1A-C (professional standards and employability) are introduced via
`professionalism-and-employability-in-healthcare` in u01 and then
reinforced through performance-task rubrics and applied tasks across
units 2, 4, 5, 7, and 8 — see the "threaded throughout the course" note
in the intro.

All 37 atoms in the sub-cluster are sequenced by this template.
