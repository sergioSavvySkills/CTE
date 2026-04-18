---
atom_id: active-directory-basics
title: Active Directory Concepts and User Management
subcluster: it-support-services
credential_objectives:
  - google-it-support::c4m4
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - user-permissions-and-acls
  - windows-features-and-tools
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to navigate Active Directory Users and Computers to create users, groups, and OUs, and explain the role of the domain controller.

## Content stub

- **AD concepts:** domain (authentication boundary), domain controller (DC) holds the directory; forest and tree for multi-domain orgs
- **AD objects:** users, security groups vs. distribution groups, computers, OUs (organizational units) — containers for applying policy
- **User management in ADUC:** create user accounts, set attributes (name, UPN, department), add to security groups, reset passwords, disable accounts
- **CN and DN notation:** how AD names objects in the directory tree; why it matters for scripting and troubleshooting

## Assessment stub

- Lab: create an OU, add 3 user accounts to it, place them in a security group
- Short answer: a new employee can log in but cannot access shared drives — where in AD do you look first?
