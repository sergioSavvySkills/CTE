---
template_id: tx-computer-maintenance-lab-2025
state: TX
course_name: Computer Maintenance Lab
course_code: 130.304
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

# Computer Maintenance Lab (TX 130.304)

The hands-on half of the Computer Maintenance / Computer Maintenance Lab
pair. Per 19 TAC §130.304, this course **must be taken concurrently with
Computer Maintenance (130.303)** — it is not stand-alone.

This template runs the same atom sequence as the theory course but
flips the generator mix: where the theory template produces lessons
and videos, the Lab template produces **virtual labs, simulations, and
applied tasks**. All "lab" work is generated digitally (no physical
workbench required): component-identification simulators, virtual PC
assembly, live OS installation in a browser VM, packet-capture in a
simulated network, etc.

Lab-only atoms (diagnostic tools, OS install, BIOS flashing, backup &
recovery, disaster-recovery planning) are added in the units where they
reinforce the concurrent theory material.

```yaml
units:
  - unit_id: u01
    title: "Safety, Ethics, and the Work Order"
    weeks: 2
    slots:
      - slot: 1
        atom_id: it-safety-procedures
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 2
        atom_id: work-behaviors-professional-standards
      - slot: 3
        atom_id: professional-communication-it
      - slot: 4
        atom_id: documentation-and-ticketing-systems
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 5
        atom_id: change-management
      - slot: 6
        atom_id: it-environmental-impacts
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true

  - unit_id: u02
    title: "Applied Troubleshooting Methodology"
    weeks: 1
    slots:
      - slot: 1
        atom_id: troubleshooting-methodology
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 2
        atom_id: critical-thinking-problem-solving
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u03
    title: "Component Identification and System Assembly"
    weeks: 3
    slots:
      - slot: 1
        atom_id: hardware-components-overview
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 2
        atom_id: internal-components
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 3
        atom_id: motherboard-and-cpu-installation
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 4
        atom_id: ram-fundamentals
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 5
        atom_id: power-supplies
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 6
        atom_id: troubleshoot-motherboards-ram-cpus
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

  - unit_id: u04
    title: "Storage, Displays, and Peripherals"
    weeks: 3
    slots:
      - slot: 1
        atom_id: storage-technologies
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 2
        atom_id: filesystems-and-partitioning
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 3
        atom_id: troubleshoot-storage
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 4
        atom_id: display-components
      - slot: 5
        atom_id: troubleshoot-display
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 6
        atom_id: peripheral-devices
      - slot: 7
        atom_id: cables-and-connectors
      - slot: 8
        atom_id: printers-and-maintenance
      - slot: 9
        atom_id: troubleshoot-printers
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true

  - unit_id: u05
    title: "Mobile Device Service"
    weeks: 1
    slots:
      - slot: 1
        atom_id: mobile-device-hardware
      - slot: 2
        atom_id: troubleshoot-mobile-hardware
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 3
        atom_id: troubleshoot-mobile-os
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
    title: "Operating System Installation and Maintenance"
    weeks: 3
    slots:
      - slot: 1
        atom_id: operating-systems-overview
      - slot: 2
        atom_id: os-installation
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 3
        atom_id: windows-features-and-tools
      - slot: 4
        atom_id: windows-cli
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 5
        atom_id: process-management
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 6
        atom_id: file-management
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 7
        atom_id: troubleshoot-windows
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
    title: "Application Installation and Licensing"
    weeks: 1
    slots:
      - slot: 1
        atom_id: application-installation
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 2
        atom_id: software-licensing
      - slot: 3
        atom_id: virtualization-concepts
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

  - unit_id: u08
    title: "Network Configuration and Verification"
    weeks: 2
    slots:
      - slot: 1
        atom_id: networking-fundamentals
      - slot: 2
        atom_id: ip-addressing-and-subnetting
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 3
        atom_id: network-configuration
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 4
        atom_id: windows-client-networking
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 5
        atom_id: networking-tools
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 6
        atom_id: network-troubleshooting
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
    unit_generate:
      game: true
      summative_quiz: true
      performance_task: false

  - unit_id: u09
    title: "Security Software and System Hardening"
    weeks: 2
    slots:
      - slot: 1
        atom_id: windows-security-settings
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 2
        atom_id: malware-detection-and-removal
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 3
        atom_id: workstation-security-hardening
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

  - unit_id: u10
    title: "Backup, Recovery, and Disaster Planning"
    weeks: 2
    slots:
      - slot: 1
        atom_id: business-continuity-and-disaster-recovery
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: false
          video: true
      - slot: 2
        atom_id: data-destruction-and-disposal
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
      - slot: 3
        atom_id: remote-access-and-virtual-machines
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true
          video: false
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true
```

## Pacing summary

Ten units across ~22 weeks, weighted toward component assembly (U03),
peripheral service (U04), and OS installation (U06) — the three TEKS
clusters with the most explicit "demonstrate / install / diagnose"
verbs. Performance tasks appear in six units because the Lab course is
evaluated primarily on transfer to realistic service scenarios (build a
PC, repair a broken image, write a DR plan for a small business).

## Coverage note

TEKS coverage for the 50 standards under 130.304 is derived through the
slot → atom → credential → state crosswalk chain. Because this course
runs **concurrent with** 130.303, expect overlap in the derived TEKS
coverage — that is by design. Run the coverage report to confirm every
130.304 TEKS maps to at least one slot before promoting to `status:
active`.

## Why there are no physical labs

All "lab" content is generated digitally:

- **Simulations** = self-contained HTML virtual labs (e.g., drag-and-drop PC assembly, virtual BIOS, virtual disk-management console)
- **Applied tasks** = problem-solving briefs students complete in a browser-based environment
- **Virtual machines** for OS installation run in the browser (e.g., WebVM, in-browser QEMU, or linked cloud VM)

Teachers who do have physical lab equipment can supplement, but the
course is fully deliverable on a 1:1 laptop/Chromebook program with no
hardware budget.
