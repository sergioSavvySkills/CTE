---
atom_id: troubleshoot-windows
title: Troubleshooting Windows OS
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::3.1
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 3
prerequisites:
  - windows-features-and-tools
  - windows-cli
  - troubleshooting-methodology
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to diagnose and resolve common Windows OS issues including boot failures, BSODs, application errors, and performance problems.

## Content stub

- **Boot failure types:** no bootable device (MBR/BCD corrupt), BOOTMGR missing, boot loop; WinRE access (F8/Shift+F8)
- **Windows Recovery Environment:** Startup Repair, System Restore, System Image Recovery, Command Prompt, Reset This PC
- **BSOD analysis:** reading stop codes, minidump files, WinDbg basics; common codes (IRQL_NOT_LESS_OR_EQUAL, PAGE_FAULT)
- **Application errors:** application won't start, crashes on launch; event viewer application log; compatibility mode; reinstall
- **Performance troubleshooting:** Task Manager bottleneck identification; disk cleanup; disabling startup items; SFC and DISM
- **User profile corruption:** can't log in, temp profile, fixing with regedit ProfileList or creating new profile

## Assessment stub

- Boot repair lab: break a VM's BCD and repair it using bootrec /fixbcd and /fixmbr from WinRE
- BSOD exercise: given a minidump analysis output, identify the failing driver
- Short answer: what is the difference between SFC /scannow and DISM /RestoreHealth?
