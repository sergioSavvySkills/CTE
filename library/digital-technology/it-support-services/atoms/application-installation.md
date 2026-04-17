---
atom_id: application-installation
title: Installing Applications
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::1.10
  - google-it-support::c3m3
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 1
prerequisites:
  - os-installation
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to install, update, and remove applications on Windows, macOS, and Linux using multiple distribution methods.

## Content stub

- **Windows installers:** MSI vs. EXE; silent install flags (/quiet, /norestart); Programs and Features; Winget
- **macOS installation:** DMG drag-to-Applications; PKG installers; App Store; Homebrew for CLI tools
- **Linux package install:** apt install, dnf install; dpkg/rpm for local packages; dependencies and conflicts
- **Enterprise deployment:** Group Policy software deployment, SCCM/Intune, self-service portals
- **Application compatibility:** 32-bit vs. 64-bit; Windows compatibility mode; sandbox/container isolation
- **Uninstall and cleanup:** proper uninstall vs. just deleting; leftover registry entries; revo uninstaller approach

## Assessment stub

- Install lab: install, configure, and uninstall a specified application on Windows and Linux VMs
- Silent install script: write a Winget or apt command to install three tools in one command
- Short answer: what is the risk of downloading an installer from a random website instead of the vendor's official site?
