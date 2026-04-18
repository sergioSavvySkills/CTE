---
atom_id: dhcp-configuration
title: DHCP Configuration and Troubleshooting
subcluster: it-support-services
credential_objectives:
  - google-it-support::c2m4
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - dns-fundamentals
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to explain the DHCP lease process, configure a scope with exclusions, create a reservation, and diagnose DHCP failures.

## Content stub

- **DORA process:** Discover (client broadcasts) → Offer (server proposes IP) → Request (client accepts) → Acknowledge (server confirms lease)
- **Scope and exclusions:** the range of IPs the server hands out; exclusions reserve IPs for static assignment (servers, printers)
- **DHCP reservations:** bind a specific IP to a MAC address so the same device always gets the same IP without manual static config
- **Failure scenarios:** DHCP unavailable → Windows assigns APIPA (169.254.x.x); wrong scope → wrong subnet; rogue DHCP server gives bad gateway

## Assessment stub

- Scenario: a new network printer must always receive 192.168.1.50 — configure a DHCP reservation; explain why reservation is preferred over a static IP on the device
- Short answer: a user's PC shows IP 169.254.12.34 — what does this tell you and what do you check first?
