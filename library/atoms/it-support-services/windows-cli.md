---
atom_id: windows-cli
title: Windows Command Line and PowerShell
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::1.5
  - google-it-support::c3m1
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - file-management
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to navigate the file system, manage files, and run common administrative commands using both CMD and PowerShell.

## Content stub

- **CMD basics:** cd, dir, copy, move, del, mkdir, rmdir; absolute vs. relative paths; wildcards
- **Network commands:** ping, ipconfig, netstat, tracert, nslookup — reading the output
- **System commands:** sfc /scannow, chkdsk, diskpart, taskkill, shutdown; running as administrator
- **PowerShell intro:** cmdlet syntax (Verb-Noun), pipeline, Get-Help, Get-Command; why PS is preferred over CMD
- **PowerShell for IT:** Get-Process, Stop-Process, Get-Service, Start-Service, Get-EventLog; real admin use cases
- **Scripting preview:** .bat and .ps1 scripts; running scripts with Set-ExecutionPolicy; automating repetitive tasks

## Assessment stub

- CMD lab: navigate to a folder, create files, list contents, and delete — using only keyboard commands
- PowerShell task: write a one-liner that lists all running services and outputs to a text file
- Short answer: why would a tech use PowerShell instead of CMD for a complex administrative task?
