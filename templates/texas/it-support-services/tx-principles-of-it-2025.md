---
template_id: tx-principles-of-it-2025
state: TX
course_name: Principles of Information Technology
course_code: 130.302
subcluster: it-support-services
grade_band: HS
credit_hours: 1
credential_targets:
  - comptia-itf-plus
framework_version: 2015 Adopted
status: draft
reviewer:
review_date:
---

# Principles of Information Technology (TX 130.302)

Broad survey of the IT field for grades 9–10. Builds digital-literacy
fundamentals and prepares students for CompTIA ITF+. Each atom is a
45-minute period; block-schedule teachers combine two atoms per day.

```yaml
units:
  - unit_id: u01
    title: "Professional Foundations and the IT Pathway"
    weeks: 2
    slots:
      - slot: 1
        atom_id: career-exploration-it-pathway
      - slot: 2
        atom_id: work-behaviors-professional-standards
      - slot: 3
        atom_id: professional-communication-it
      - slot: 4
        atom_id: leadership-and-teamwork-it
      - slot: 5
        atom_id: critical-thinking-problem-solving
      - slot: 6
        atom_id: it-safety-procedures
      - slot: 7
        atom_id: documentation-and-ticketing-systems
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true

  - unit_id: u02
    title: "How Computers Represent Information"
    weeks: 2
    slots:
      - slot: 1
        atom_id: input-processing-output-storage
      - slot: 2
        atom_id: binary-number-systems
        generate:
          lesson: true
          classwork: guided_practice
          quiz: exit_ticket
          simulation: false
          video: true
      - slot: 3
        atom_id: fundamental-data-types
      - slot: 4
        atom_id: computing-units-of-measure
    unit_generate:
      game: true
      summative_quiz: true
      performance_task: false

  - unit_id: u03
    title: "Hardware Components"
    weeks: 2
    slots:
      - slot: 1
        atom_id: hardware-components-overview
      - slot: 2
        atom_id: computing-devices-overview
      - slot: 3
        atom_id: internal-components
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 4
        atom_id: peripheral-devices
      - slot: 5
        atom_id: cables-and-connectors
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u04
    title: "Operating Systems and File Management"
    weeks: 2
    slots:
      - slot: 1
        atom_id: operating-systems-overview
      - slot: 2
        atom_id: windows-features-and-tools
      - slot: 3
        atom_id: file-management
      - slot: 4
        atom_id: filesystems-and-partitioning
      - slot: 5
        atom_id: application-installation
      - slot: 6
        atom_id: application-architecture-and-delivery-models
    unit_generate:
      game: true
      summative_quiz: true
      performance_task: false

  - unit_id: u05
    title: "Networking Fundamentals"
    weeks: 2
    slots:
      - slot: 1
        atom_id: networking-fundamentals
      - slot: 2
        atom_id: internet-service-types
      - slot: 3
        atom_id: networked-host-services
      - slot: 4
        atom_id: wireless-technologies
      - slot: 5
        atom_id: network-troubleshooting
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u06
    title: "Internet Safety, Security, and Ethics"
    weeks: 2
    slots:
      - slot: 1
        atom_id: web-browser-configuration
      - slot: 2
        atom_id: behavioral-security
      - slot: 3
        atom_id: social-engineering
      - slot: 4
        atom_id: browser-security-settings
      - slot: 5
        atom_id: password-best-practices
      - slot: 6
        atom_id: data-value-and-intellectual-property
      - slot: 7
        atom_id: software-licensing
      - slot: 8
        atom_id: malware-detection-and-removal
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
    unit_generate:
      game: true
      summative_quiz: true
      performance_task: true

  - unit_id: u07
    title: "Word Processing for Professional Documents"
    weeks: 1
    slots:
      - slot: 1
        atom_id: word-processing-fundamentals
      - slot: 2
        atom_id: creating-professional-documents
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u08
    title: "Spreadsheets and Data"
    weeks: 2
    slots:
      - slot: 1
        atom_id: spreadsheet-fundamentals
      - slot: 2
        atom_id: spreadsheet-functions
      - slot: 3
        atom_id: csv-files
      - slot: 4
        atom_id: advanced-spreadsheet-features
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true

  - unit_id: u09
    title: "Databases"
    weeks: 2
    slots:
      - slot: 1
        atom_id: database-concepts
      - slot: 2
        atom_id: database-structures
      - slot: 3
        atom_id: database-queries
    unit_generate:
      game: true
      summative_quiz: true
      performance_task: false

  - unit_id: u10
    title: "Presenting Information"
    weeks: 1
    slots:
      - slot: 1
        atom_id: presentation-software-fundamentals
      - slot: 2
        atom_id: creating-presentations
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u11
    title: "Programming and Algorithmic Thinking"
    weeks: 2
    slots:
      - slot: 1
        atom_id: algorithms-and-logic
        generate:
          lesson: true
          classwork: guided_practice
          quiz: exit_ticket
          simulation: false
          video: true
      - slot: 2
        atom_id: programming-concepts
      - slot: 3
        atom_id: programming-language-categories
      - slot: 4
        atom_id: ai-concepts-in-it
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u12
    title: "Web Design Capstone"
    weeks: 3
    slots:
      - slot: 1
        atom_id: web-design-terminology
      - slot: 2
        atom_id: visual-design-elements
      - slot: 3
        atom_id: design-principles
      - slot: 4
        atom_id: html-fundamentals
      - slot: 5
        atom_id: build-a-web-page
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true
```

## Pacing summary

Twelve units spanning ~23 weeks of instruction, leaving room for review,
state-testing windows, and semester exams across a 36-week year.
Performance tasks anchor four units (Professional Foundations, Security &
Ethics, Spreadsheets, and the Web Design capstone) where a multi-day
project reinforces transfer of learning.

## Coverage note

TEKS coverage is derived through the slot → atom → credential → state
crosswalk chain; this template does not hand-author standards mapping.
Run the coverage report to verify all 66 TEKS for 130.302 hit at least
one slot before promoting this template to `status: active`.
