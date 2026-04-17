---
atom_id: windows-client-networking
title: Windows Client Networking Features
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::1.7
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - network-configuration
  - windows-features-and-tools
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to configure and verify Windows network adapter settings, share resources, and use Windows networking tools to diagnose connectivity.

## Content stub

- **Network adapter properties:** IPv4/IPv6 settings, DNS, gateway; enabling/disabling adapters; adapter priority
- **Network profiles:** Public, Private, Domain — firewall rules tied to each; changing profile type
- **Windows Firewall:** inbound/outbound rules; allowing an app through; advanced settings; resetting defaults
- **File and printer sharing:** enabling sharing, setting share permissions, accessing UNC paths (\\server\share)
- **HomeGroup successor:** Workgroup vs. domain; Network and Sharing Center; mapping network drives
- **VPN client:** built-in Windows VPN; L2TP, SSTP, IKEv2 protocols; connecting and verifying

## Assessment stub

- Lab: configure a static IP, verify it in ipconfig, ping the gateway, then revert to DHCP
- Sharing lab: create a shared folder, set permissions, and access it from another VM via UNC path
- Short answer: why should a laptop use the Public profile on a coffee shop Wi-Fi?
