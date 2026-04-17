---
atom_id: wireless-security-protocols
title: Wireless Security Protocols (WPA2, WPA3)
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::2.3
skill_type: knowledge
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - wireless-network-installation
  - encryption-fundamentals
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to compare wireless security protocols, configure WPA2/WPA3, and explain why older protocols are vulnerable.

## Content stub

- **WEP weaknesses:** static keys, weak RC4 implementation, cracked in minutes; never use
- **WPA and WPA2:** TKIP (WPA) → AES-CCMP (WPA2); Personal (PSK) vs. Enterprise (RADIUS); WPA2 still widely deployed
- **WPA3:** SAE replaces PSK; forward secrecy; 192-bit enterprise mode; WPA3 transition mode for mixed clients
- **Enterprise authentication:** 802.1X, RADIUS server, EAP variants (PEAP, EAP-TLS); certificates vs. credentials
- **Common wireless attacks:** evil twin, deauth attack, PMKID attack on WPA2; why WPA3 mitigates these
- **Best practices:** disable WPS, use WPA3 where possible, strong PSK, separate IoT VLAN, monitor for rogue APs

## Assessment stub

- Protocol timeline: arrange WEP/WPA/WPA2/WPA3 chronologically and describe the key improvement each added
- Lab: configure a router with WPA3-SAE and connect a client; verify the security mode in client adapter settings
- Short answer: why is WPA2-Personal weaker than WPA2-Enterprise?
