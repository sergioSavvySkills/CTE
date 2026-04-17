---
atom_id: device-security-practices
title: Device Security Best Practices
subcluster: it-support-services
credential_objectives:
  - comptia-itf-plus::6.2
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 1
prerequisites:
  - cia-triad
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to apply device security best practices including screen lock, patching, encryption, and physical security to protect endpoints.

## Content stub

- **Screen lock and authentication:** auto-lock timeout, strong PIN/password, biometrics; balancing convenience and security
- **Patch management:** OS and app updates; why patching matters; patch Tuesday; zero-day window
- **Endpoint encryption:** BitLocker (Windows), FileVault (macOS), LUKS (Linux); full-disk vs. file-level encryption
- **Physical security:** cable locks, privacy screens, clean-desk policy, securing server rooms; tailgating prevention
- **Mobile device policies:** remote wipe capability, MDM enrollment, disable unused features (Bluetooth/NFC)
- **Asset inventory:** tracking hardware; knowing what's on the network; decommissioning process

## Assessment stub

- Security audit checklist: evaluate a provided PC configuration against a best-practices checklist
- Lab: enable BitLocker on a Windows VM and document the recovery key storage process
- Short answer: why should BitLocker recovery keys not be stored on the same drive they protect?
