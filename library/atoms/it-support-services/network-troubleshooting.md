---
atom_id: network-troubleshooting
title: Network Troubleshooting
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core1::5.5
  - google-it-support::c2m6
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 3
prerequisites:
  - networking-tools
  - troubleshooting-methodology
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to apply a systematic troubleshooting approach to diagnose and resolve common network connectivity problems.

## Content stub

- **No connectivity symptoms:** 'no internet access' vs. 'limited connectivity' vs. 'unidentified network'; yellow triangle meanings
- **Layer-by-layer approach:** Physical (cable/link light) → IP config → gateway ping → DNS test → remote host ping
- **Common causes:** bad cable, wrong DHCP, IP conflict, DNS misconfiguration, blocked port, failed NIC
- **IP conflict resolution:** how APIPA addresses appear (169.254.x.x); releasing and renewing; finding the duplicate
- **Wireless-specific:** SSID not found, wrong password, driver issues, channel congestion, weak signal
- **Escalation triggers:** when the problem is upstream (ISP, firewall, managed switch) and should be escalated

## Assessment stub

- Scenario matrix: given 5 different connectivity symptoms, diagnose each using the layer-by-layer approach
- Lab: deliberately misconfigure a VM's network settings and then troubleshoot back to connectivity
- Documentation task: write a ticket closure note for a resolved IP conflict
