---
atom_id: file-management
title: File Management and File Systems
subcluster: it-support-services
credential_objectives: []
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 1
prerequisites:
  - operating-systems-overview
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to navigate a file system, create and organize files and folders, and describe how common file systems handle storage and permissions.

## Content stub

- **File system concepts:** directories and paths (absolute vs. relative); root directory; file extensions and types
- **Windows file systems:** NTFS (permissions, journaling, encryption), FAT32 (legacy, USB), exFAT (cross-platform large files)
- **Linux/macOS file systems:** ext4 (Linux default), APFS (macOS) — case-sensitive unlike Windows NTFS
- **File operations:** copy, move, rename, delete, search; recycle bin vs. permanent deletion; hidden files
- **Permissions basics:** owner/group/other on Linux; NTFS ACLs on Windows; why permissions matter
- **File organization best practices:** naming conventions, folder hierarchies, archiving vs. deleting old files

## Assessment stub

- Navigation lab: using only the CLI, create a folder structure with 3 levels and move files between them
- Permissions exercise: on a Linux VM, set a file so only the owner can read/write it
- Short answer: why is NTFS preferred over FAT32 for a Windows system drive?
