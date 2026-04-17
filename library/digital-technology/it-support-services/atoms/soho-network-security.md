---
atom_id: soho-network-security
title: SOHO Network Security Settings
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::2.10
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - wireless-network-installation
  - wireless-security-protocols
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to configure a SOHO router with security best practices including changing defaults, enabling firewall, segmenting the network, and disabling insecure features.

## Content stub

- **Change default credentials:** admin username and password on router; firmware update; disabling remote management
- **SSID and encryption:** unique SSID, WPA3 or WPA2-AES, disable WEP/TKIP, disable WPS
- **Network segmentation:** guest network isolation; IoT VLAN; keeping trusted devices separate from visitors and smart devices
- **Firewall and port forwarding:** SPI firewall; only forward ports that are needed; UPnP risks; DMZ pitfalls
- **DHCP and DNS settings:** custom DNS (Pi-hole, 1.1.1.1); DHCP reservations for key devices; disabling unused services
- **Monitoring and logging:** router log review; connected device list; detecting unknown devices

## Assessment stub

- Router hardening lab: configure a consumer router (physical or simulated) against a provided security checklist
- Connected device audit: list all devices on a network and identify any that shouldn't be there
- Short answer: why should you disable UPnP on a home/small-office router?
