---
atom_id: remote-desktop-and-support-tools
title: Remote Desktop and Remote Support Tools
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::4.8
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - vpn-and-remote-access
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to connect to a remote Windows machine via RDP, connect to a Linux/network device via SSH, and use a remote support tool to assist an end user.

## Content stub

- **RDP:** Windows GUI remote access; port 3389; Network Level Authentication (NLA); never expose RDP directly to the internet — use VPN or RD Gateway
- **SSH:** encrypted CLI access for Linux servers and network devices; port 22; key-based auth is more secure than passwords; common commands: `ssh user@host`, `scp`, `sftp`
- **Remote support tools:** TeamViewer, AnyDesk — attended (user present) vs. unattended access; session recording for audit trails
- **Security hardening:** change default RDP/SSH ports, disable password auth on SSH, require MFA for remote support sessions

## Assessment stub

- Lab: RDP into a Windows VM and SSH into a Linux VM; screenshot both successful connections
- Short answer: why is exposing RDP port 3389 directly to the internet a critical security risk?
