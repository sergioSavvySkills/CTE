---
atom_id: user-permissions-and-acls
title: User Accounts, Permissions, and ACLs
subcluster: it-support-services
credential_objectives:
  - google-it-support::c3m2
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - file-management
  - windows-features-and-tools
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to create and manage user accounts, assign NTFS and share permissions, and explain how ACLs control access to resources.

## Content stub

- **User account types:** local vs. domain accounts; Administrator vs. Standard; built-in accounts (Guest, DefaultAccount)
- **Windows user management:** Local Users and Groups MMC; net user command; creating, disabling, and deleting accounts
- **NTFS permissions:** Read, Write, Modify, Full Control, List; explicit vs. inherited; how deny overrides allow
- **Share permissions:** Full Control, Change, Read; how share and NTFS permissions combine (most restrictive wins)
- **ACL structure:** DACL vs. SACL; ACEs (access control entries); viewing with icacls command
- **Principle of least privilege:** give users only the access they need; auditing access; removing stale accounts

## Assessment stub

- Lab: create a folder, set NTFS permissions for three different users, and verify each user's access
- icacls exercise: use icacls to view and modify permissions on a test folder from the command line
- Short answer: a user has Read NTFS permission but Full Control share permission — what can they actually do?
