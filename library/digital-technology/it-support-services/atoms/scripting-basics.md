---
atom_id: scripting-basics
title: Scripting Basics (Batch, Shell, PowerShell)
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::4.9
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - windows-cli
  - linux-features
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to read and write basic automation scripts in Batch, Bash, and PowerShell to automate repetitive IT tasks.

## Content stub

- **Why scripting:** automation saves time; consistency vs. manual steps; auditability; scaling IT operations
- **Batch scripting:** .bat files; variables (%VAR%), IF/ELSE, FOR loops; echo, pause, call; practical uses (mapped drives, cleanup)
- **Bash scripting:** #!/bin/bash shebang; variables ($VAR), if/then/fi, for loops, chmod +x; practical uses (backups, log rotation)
- **PowerShell scripting:** cmdlets, pipeline, $variables, foreach, if; Get-Content/Out-File; execution policy; practical admin scripts
- **Reading existing scripts:** following logic without being the author; identifying what a script does before running it
- **Script safety:** never run untrusted scripts; testing in a VM; commenting code; error handling with try/catch

## Assessment stub

- Script reading: given a 20-line PowerShell script, describe in plain English what it does
- Write a Batch script: create a .bat file that maps a network drive and logs the date/time to a text file
- Short answer: what does Set-ExecutionPolicy RemoteSigned do and why does it matter?
