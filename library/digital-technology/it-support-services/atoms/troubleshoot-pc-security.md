---
atom_id: troubleshoot-pc-security
title: Troubleshooting PC Security Issues
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::3.4
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 3
prerequisites:
  - malware-detection-and-removal
  - windows-security-settings
  - troubleshooting-methodology
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to identify symptoms of PC security compromise, perform malware removal, and restore a system to a trusted state.

## Content stub

- **Infection symptoms:** slow performance, browser redirects, new toolbars, antivirus disabled, ransom note, encrypted files
- **Quarantine procedures:** isolate from network immediately; document symptoms; preserve evidence before cleaning
- **Safe Mode removal:** booting to Safe Mode with Networking; running anti-malware offline; removing stubborn malware
- **Browser hijack removal:** resetting browser settings, removing extensions, clearing DNS cache, flushing HOSTS file
- **Post-removal hardening:** patch the entry point, change credentials, enable MFA, verify backup integrity
- **When to reimage:** rootkits, persistent re-infection, ransomware without backup recovery, evidence preservation for forensics

## Assessment stub

- Removal walkthrough: given a scenario with specific symptoms, list the complete removal procedure step by step
- Lab: use Windows Defender offline scan on a VM and document findings
- Short answer: why is the first step of malware response to isolate the machine from the network?
