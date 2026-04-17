---
atom_id: windows-security-settings
title: Windows Security Settings
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::2.2
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - windows-features-and-tools
  - authentication-authorization-accounting
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to configure key Windows security settings including Windows Defender, firewall rules, BitLocker, and local security policies.

## Content stub

- **Windows Defender:** real-time protection, scheduled scans, exclusions, definitions update; integration with Microsoft 365
- **Windows Firewall:** inbound/outbound rules, profiles (Domain/Private/Public), allowing apps, blocking ports
- **BitLocker:** enabling on system and data drives, TPM requirement, recovery key management, suspend for updates
- **Local Security Policy:** password policy, account lockout, audit policy, user rights assignment, security options
- **UAC settings:** UAC levels, why UAC exists, application elevation, disabling UAC risks
- **Secure Boot and TPM:** UEFI Secure Boot preventing rootkits; TPM 2.0 for BitLocker and Windows 11

## Assessment stub

- Lab: configure Windows Defender exclusions, set a firewall rule to block a specific port, and verify the rule
- BitLocker lab: enable BitLocker on a secondary drive, note the recovery key, and decrypt the drive
- Short answer: what attack does Secure Boot prevent and how?
