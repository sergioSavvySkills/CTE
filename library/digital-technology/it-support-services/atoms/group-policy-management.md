---
atom_id: group-policy-management
title: Group Policy Objects and LDAP Queries
subcluster: it-support-services
credential_objectives:
  - google-it-support::c4m4
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - active-directory-basics
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to create and link a GPO, explain policy inheritance, and use gpresult and RSOP to troubleshoot applied policies.

## Content stub

- **GPO scope:** site → domain → OU hierarchy; policy inheritance; blocking inheritance; enforcing GPOs override blocks
- **Common GPO use cases:** password complexity, screen lock timeout, drive mapping, software deployment, restricting Control Panel
- **RSOP and gpresult:** `gpresult /r` shows applied policies for current user/computer; Resultant Set of Policy confirms effective settings
- **LDAP basics:** AD is an LDAP directory; `dsquery` and `Get-ADUser` filter objects by attribute for bulk operations

## Assessment stub

- GPO lab: apply a screen-lock-timeout policy to an OU and verify with gpresult /r
- Short answer: a GPO applied at the domain level does not seem to apply to one OU — what two settings could explain this?
