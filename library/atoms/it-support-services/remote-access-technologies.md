---
atom_id: remote-access-technologies
title: Remote Access Technologies
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::4.8
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - networking-fundamentals
  - encryption-fundamentals
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to compare remote access technologies, configure a VPN connection, and use remote support tools to assist end users.

## Content stub

- **VPN types:** site-to-site (connecting two offices), client-to-site (remote worker); split tunneling
- **VPN protocols:** IPSec/IKEv2, OpenVPN, WireGuard, SSL/TLS VPN; L2TP (legacy); which to recommend today
- **RDP and SSH:** RDP for Windows GUI remote; SSH for Linux/network device CLI; security hardening for each
- **Remote support tools:** TeamViewer, AnyDesk, SCCM Remote Control; attended vs. unattended; session recording
- **Zero trust network access:** replacing VPN for many orgs; identity-aware proxy; least-privilege access per application
- **Remote access security:** MFA requirement, session timeout, logging, geofencing; risks of exposed RDP port

## Assessment stub

- VPN configuration lab: configure a client-to-site VPN on a Windows PC and verify the tunnel
- Protocol comparison table: compare IPSec, OpenVPN, and WireGuard on security, speed, and ease of setup
- Short answer: why is exposing RDP directly to the internet a significant security risk?
