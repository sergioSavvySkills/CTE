---
atom_id: os-installation
title: OS Installation and Upgrade Procedures
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::1.2
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - windows-editions
  - storage-technologies
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to perform a clean OS installation, configure initial settings, and execute an in-place upgrade while preserving user data.

## Content stub

- **Pre-installation planning:** hardware compatibility check, driver availability, TPM 2.0 for Win 11, disk space requirements
- **Installation media:** creating bootable USB (Rufus, Windows Media Creation Tool); ISO files; network PXE boot
- **Partition setup:** choosing the installation partition; GPT vs. MBR; EFI System Partition; wiping vs. keeping data
- **Attending the install:** language/region/keyboard, product key entry, custom vs. upgrade install, initial user setup
- **Post-install tasks:** driver installation order, Windows Update, removing bloatware, joining domain or Azure AD
- **In-place upgrade:** upgrade vs. clean install trade-offs; keeping files/apps/settings; rollback window (10 days)

## Assessment stub

- Lab: perform a clean Windows installation in a VM from ISO, complete post-install checklist
- Upgrade scenario: list the steps to upgrade Windows 10 Home to Windows 11 Pro in-place
- Short answer: why should drivers be installed before joining a domain after a clean install?
