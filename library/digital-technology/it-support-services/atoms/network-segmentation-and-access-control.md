---
atom_id: network-segmentation-and-access-control
title: Network Segmentation and Access Control
subcluster: it-support-services
credential_objectives:
  - google-it-support::c5m4
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - security-measures-overview
  - networking-tools
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to apply network segmentation using VLANs and DMZ, configure a default-deny firewall stance, and disable unnecessary services.

## Content stub

- **Disable unused services and ports:** close listening ports, disable Telnet/FTP/SNMPv1; use SSH instead of Telnet; attack surface shrinks with every service removed
- **VLANs:** logically separate traffic on the same physical switch; isolate finance, IoT, guest networks from each other
- **DMZ:** public-facing servers (web, mail) in a separate zone between external firewall and internal network; breach of DMZ does not reach internal LAN
- **Firewall rules — default deny:** block everything, then allow only what is needed; remove overly permissive rules; log all denied traffic for review

## Assessment stub

- Hardening checklist: apply a provided network hardening checklist to a simulated router/switch environment
- Short answer: why does placing a web server in a DMZ limit the damage if it is compromised?
