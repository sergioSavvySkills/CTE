---
template_id: tx-computer-maintenance-2025
state: TX
course_name: Computer Maintenance
course_code: 130.303
subcluster: it-support-services
grade_band: HS
credit_hours: 1
credential_targets:
  - comptia-a-plus
framework_version: 2015 Adopted
status: draft
reviewer:
review_date:
---

# Computer Maintenance (TX 130.303)

The theory half of the Computer Maintenance / Computer Maintenance Lab
pair. Per 19 TAC §130.304 the Lab course must be taken concurrently, so
this template leans on lessons, videos, and formative quizzes while the
companion Lab template handles the hands-on simulations against the same
atom sequence. Aligned primarily to CompTIA A+ Core 1 objectives.

```yaml
units:
  - unit_id: u01
    title: "Professional Practice in Computer Technology"
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
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u02
    title: "Troubleshooting Methodology"
    weeks: 1
    slots:
      - slot: 1
        atom_id: troubleshooting-methodology
        generate:
          lesson: true
          classwork: guided_practice
          quiz: exit_ticket
          simulation: false
          video: true
      - slot: 2
        atom_id: documentation-and-ticketing-systems
      - slot: 3
        atom_id: change-management
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u03
    title: "Digital Logic and Data Representation"
    weeks: 2
    slots:
      - slot: 1
        atom_id: binary-number-systems
        generate:
          lesson: true
          classwork: guided_practice
          quiz: exit_ticket
          simulation: false
          video: true
      - slot: 2
        atom_id: fundamental-data-types
      - slot: 3
        atom_id: computing-units-of-measure
      - slot: 4
        atom_id: input-processing-output-storage
    unit_generate:
      game: true
      summative_quiz: true
      performance_task: false

  - unit_id: u04
    title: "Motherboards, CPUs, and RAM"
    weeks: 2
    slots:
      - slot: 1
        atom_id: internal-components
      - slot: 2
        atom_id: ram-fundamentals
      - slot: 3
        atom_id: motherboard-and-cpu-installation
        generate:
          lesson: true
          classwork: guided_practice
          quiz: exit_ticket
          simulation: false
          video: true
      - slot: 4
        atom_id: troubleshoot-motherboards-ram-cpus
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u05
    title: "Storage, Display, and Power"
    weeks: 2
    slots:
      - slot: 1
        atom_id: storage-technologies
      - slot: 2
        atom_id: troubleshoot-storage
      - slot: 3
        atom_id: display-components
      - slot: 4
        atom_id: troubleshoot-display
      - slot: 5
        atom_id: power-supplies
    unit_generate:
      game: true
      summative_quiz: true
      performance_task: false

  - unit_id: u06
    title: "Peripherals, Cables, and Printers"
    weeks: 2
    slots:
      - slot: 1
        atom_id: peripheral-devices
      - slot: 2
        atom_id: cables-and-connectors
      - slot: 3
        atom_id: printers-and-maintenance
      - slot: 4
        atom_id: troubleshoot-printers
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u07
    title: "Mobile Device Hardware"
    weeks: 1
    slots:
      - slot: 1
        atom_id: mobile-device-hardware
      - slot: 2
        atom_id: troubleshoot-mobile-hardware
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u08
    title: "Operating System Fundamentals"
    weeks: 2
    slots:
      - slot: 1
        atom_id: operating-systems-overview
      - slot: 2
        atom_id: windows-editions
      - slot: 3
        atom_id: windows-features-and-tools
      - slot: 4
        atom_id: windows-settings
      - slot: 5
        atom_id: macos-features
      - slot: 6
        atom_id: linux-features
      - slot: 7
        atom_id: process-management
      - slot: 8
        atom_id: troubleshoot-windows
    unit_generate:
      game: true
      summative_quiz: true
      performance_task: false

  - unit_id: u09
    title: "Applications, Licensing, and Virtualization"
    weeks: 2
    slots:
      - slot: 1
        atom_id: application-installation
      - slot: 2
        atom_id: software-licensing
      - slot: 3
        atom_id: virtualization-concepts
      - slot: 4
        atom_id: cloud-computing
      - slot: 5
        atom_id: application-architecture-and-delivery-models
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u10
    title: "Networking for Computer Technicians"
    weeks: 2
    slots:
      - slot: 1
        atom_id: networking-fundamentals
      - slot: 2
        atom_id: tcp-udp-protocols
      - slot: 3
        atom_id: ip-addressing-and-subnetting
      - slot: 4
        atom_id: wireless-technologies
      - slot: 5
        atom_id: internet-service-types
      - slot: 6
        atom_id: networking-tools
      - slot: 7
        atom_id: network-troubleshooting
    unit_generate:
      game: true
      summative_quiz: true
      performance_task: false

  - unit_id: u11
    title: "Emerging Technologies in Computing"
    weeks: 1
    slots:
      - slot: 1
        atom_id: ai-concepts-in-it
      - slot: 2
        atom_id: it-environmental-impacts
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true
```

## Pacing summary

Eleven units across ~21 weeks. The schedule deliberately front-loads
professionalism and troubleshooting methodology so every subsequent
hardware unit can model the six-step process. A single capstone
performance task in U11 (e.g., "recommend a computer system for a given
use case") integrates hardware, OS, and emerging-tech knowledge.

## Coverage note

TEKS coverage for the 38 standards under 130.303 is derived through the
slot → atom → credential → state crosswalk chain. Run the coverage
report to confirm every TEKS maps to at least one slot before promoting
to `status: active`. Pair this template with `tx-computer-maintenance-lab-2025`
for the concurrent lab half of the course.
