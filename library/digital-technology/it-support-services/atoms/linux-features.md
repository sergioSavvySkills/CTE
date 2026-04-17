---
atom_id: linux-features
title: Linux Client Features and Tools
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::1.9
skill_type: knowledge
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - operating-systems-overview
  - file-management
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to navigate a Linux desktop environment, use the terminal for common tasks, and identify how Linux differs from Windows and macOS in support scenarios.

## Content stub

- **Linux distributions:** Ubuntu, Fedora, Debian, CentOS/RHEL, Mint; desktop environments (GNOME, KDE, XFCE)
- **Linux file hierarchy:** / root, /home, /etc, /var, /usr, /tmp; everything is a file
- **Terminal fundamentals:** ls, pwd, cd, cp, mv, rm, mkdir, chmod, chown, sudo, man; case-sensitive commands
- **Package management:** apt/apt-get (Debian/Ubuntu), dnf/yum (RHEL/Fedora); installing, updating, removing software
- **Users and permissions:** rwx bits, numeric notation (755, 644), sudo vs root, /etc/passwd and /etc/sudoers
- **Linux support scenarios:** viewing logs (/var/log), checking processes (ps aux, top), managing services (systemctl)

## Assessment stub

- Terminal lab: complete a task sheet using only CLI (create user, install a package, set permissions)
- Log analysis: given a /var/log/syslog excerpt, identify the error and its likely cause
- Short answer: what command would you use to give a script execute permission for all users?
