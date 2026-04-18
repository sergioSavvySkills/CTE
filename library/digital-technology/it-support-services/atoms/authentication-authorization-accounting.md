---
atom_id: authentication-authorization-accounting
title: Authentication, Authorization, Accounting, and Non-Repudiation
subcluster: it-support-services
credential_objectives:
  - comptia-itf-plus::6.4
  - google-it-support::c5m3
skill_type: knowledge
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - cia-triad
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to distinguish authentication from authorization, explain accounting/auditing, and describe multi-factor authentication methods.

## Content stub

- **Authentication factors:** something you know (password), have (token/phone), are (biometrics); inherence factor
- **MFA and 2FA:** combining factors; TOTP apps (Google Authenticator), SMS (weaker), hardware keys (YubiKey)
- **Authorization:** access control after authentication; RBAC (role-based), ABAC, ACLs; principle of least privilege
- **Accounting/auditing:** logging who did what and when; event logs, SIEM systems; required for compliance
- **Non-repudiation:** cryptographic proof that an action was taken by a specific party; digital signatures
## Assessment stub

- Factor classification: given 10 authentication examples, identify the factor type for each
- MFA setup lab: configure a TOTP app on a test account and demonstrate the login process
- Short answer: what is the difference between authentication and authorization?
