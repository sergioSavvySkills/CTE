---
atom_id: vpn-and-remote-access
title: VPN Types and Protocols
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::4.8
skill_type: knowledge
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

Students will be able to compare VPN types and protocols, and configure a basic client-to-site VPN connection.

## Content stub

- **VPN types:** site-to-site (connects two office networks permanently), client-to-site (remote worker connects to HQ); split tunneling routes only corporate traffic through VPN
- **VPN protocols:** IPSec/IKEv2 (fast, native OS support), OpenVPN (open-source, flexible), WireGuard (modern, lightweight); L2TP is legacy — avoid
- **VPN security requirements:** MFA on VPN login, session timeout, connection logging, geofencing for high-risk locations
- **When VPN is not enough:** zero trust network access (ZTNA) as the modern alternative — identity-aware proxy, least-privilege per app

## Assessment stub

- Configuration lab: set up a client-to-site VPN connection on a Windows PC and verify the tunnel is active
- Protocol comparison: list IPSec/IKEv2, OpenVPN, and WireGuard — one advantage and one drawback each
