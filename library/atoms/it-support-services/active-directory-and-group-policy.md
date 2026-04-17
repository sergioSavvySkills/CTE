---
atom_id: active-directory-and-group-policy
title: Active Directory and Group Policy
subcluster: it-support-services
credential_objectives:
  - google-it-support::c4m4
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 3
prerequisites:
  - user-permissions-and-acls
  - windows-features-and-tools
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to navigate Active Directory to manage users, groups, and OUs, and explain how Group Policy applies settings across a domain.

## Content stub

- **Active Directory concepts:** domain, forest, tree; domain controller; AD as a centralized directory for authentication and authorization
- **AD objects:** users, groups (security vs. distribution), computers, OUs (organizational units); CN, DN notation
- **User and group management:** creating users, setting attributes, adding to groups, resetting passwords, disabling accounts in ADUC
- **Group Policy Objects:** GPO scope: site, domain, OU; policy inheritance; blocking inheritance; enforcing GPOs; RSOP
- **Common GPO use cases:** password policy, screen lock, software deployment, drive mapping, desktop wallpaper, restricting Control Panel
- **LDAP and AD queries:** what LDAP is; using AD search (dsquery, PowerShell Get-ADUser); filtering by attribute

## Assessment stub

- AD lab: create an OU, create 3 user accounts, add them to a security group, and apply a GPO to the OU
- GPO troubleshoot: use gpresult /r to determine which policies are applying to a user
- Short answer: a new employee can log in but cannot access shared drives — where in AD do you look first?
