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
**Unit 8 closes the loop** — healthcare technology spans all 5 systems
and ties back to Unit 1 careers.

Performance tasks anchor the four units where an integrated project
delivers more than any single atom can: the **Career Pathway Portfolio**
(u01), the **Ethics Case Analysis** (u05), the **Safety Scenario Response**
(u07), and the **Technology Systems Map** capstone (u08).

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
      - slot: 6
        atom_id: applied-math-and-data-in-health-science
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
        atom_id: scope-of-practice-and-licensure
        generate:
          lesson: true
          classwork: discussion
          quiz: exit_ticket
          simulation: false
          video: false
      - slot: 4
        atom_id: malpractice-negligence-and-laws
        generate:
          lesson: true
          classwork: discussion
          quiz: exit_ticket
          simulation: false
          video: false
      - slot: 5
        atom_id: ethics-of-technology-in-healthcare
        generate:
          lesson: true
          classwork: discussion
          quiz: exit_ticket
          simulation: false
          video: true
      - slot: 6
        atom_id: patient-rights-and-informed-consent
        generate:
          lesson: true
          classwork: discussion
          quiz: exit_ticket
          simulation: false
          video: false
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
    title: "Healthcare Technology"
    weeks: 2
    slots:
      - slot: 1
        atom_id: healthcare-equipment-and-malfunction-reporting
      - slot: 2
        atom_id: electronic-health-records-basics
      - slot: 3
        atom_id: vital-signs-overview
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true
```

## Pacing summary

Eight units spanning ~21 weeks of instruction, leaving ~15 weeks across a
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

## Atom inventory in this template

| unit | slots | primary atoms | supporting / cross-scope |
|---|---|---|---|
| u01 Entering Health Science | 5 | professionalism-and-employability, healthcare-careers-and-pathways, history-of-healthcare, health-economics-and-government-impact | healthcare-delivery-system-overview |
| u02 The Healthcare Team | 3 | healthcare-team-roles, professional-organizations-and-credentialing, leadership-and-teamwork-in-healthcare | — |
| u03 How the Body Works | 5 | homeostasis-and-biological-processes, maslows-hierarchy-and-patient-needs, lifespan-development-stages | body-organization-and-directional-terms, body-systems-overview |
| u04 Communicating in Healthcare | 6 | medical-terminology-word-parts, therapeutic-communication, conflict-resolution-in-healthcare, technical-communication-in-health-science, applied-math-and-data-in-health-science | common-medical-abbreviations |
| u05 Ethics, Law, and Patient Rights | 6 | professional-ethics-in-healthcare, scope-of-practice-and-licensure, malpractice-negligence-and-laws, ethics-of-technology-in-healthcare, patient-rights-and-informed-consent | hipaa-and-patient-confidentiality |
| u06 Wellness, Relationships, and Cultural Practice | 3 | wellness-and-disease-prevention, healthy-relationships-and-wellbeing, cultural-competence-in-healthcare | — |
| u07 Safety and Infection Control | 6 | healthcare-regulatory-agencies, standard-precautions-and-chain-of-infection, fire-and-emergency-safety, body-mechanics-and-safe-patient-handling | hand-hygiene-technique, personal-protective-equipment-use |
| u08 Healthcare Technology | 3 | healthcare-equipment-and-malfunction-reporting | electronic-health-records-basics, vital-signs-overview |
| **total** | **37** | **26 primary** | **11 support/cross-scope** |

All 37 atoms in the sub-cluster are sequenced by this template.
