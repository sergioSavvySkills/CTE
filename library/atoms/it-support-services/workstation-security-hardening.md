---
atom_id: workstation-security-hardening
title: Workstation Security and Hardening
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::2.7
  - google-it-support::c5m5
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - windows-security-settings
  - device-security-practices
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to apply a workstation hardening checklist including removing unnecessary software, configuring security policies, and verifying baseline security.

## Content stub

- **Hardening principles:** reduce attack surface; disable unnecessary services, features, and accounts; apply least privilege
- **Remove unnecessary software:** uninstall unused apps, disable optional Windows features, remove bloatware
- **Configure security policies:** screen lock timeout, account lockout, audit logging, restrict USB storage
- **Application control:** Software Restriction Policies or AppLocker; whitelisting approved applications
- **Host-based firewall:** verify enabled, review inbound rules, block unused ports
- **Baseline and verification:** security baseline tools (LGPO, CIS benchmarks); scanning with baseline compliance tool

## Assessment stub

- Hardening lab: apply a provided CIS-inspired checklist to a Windows VM and document each change
- Before/after scan: run a vulnerability scan before and after hardening; count the reduction in findings
- Short answer: what is the purpose of application whitelisting and what is its main operational drawback?
