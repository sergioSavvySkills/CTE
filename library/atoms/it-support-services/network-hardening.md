---
atom_id: network-hardening
title: Network Hardening and Monitoring
subcluster: it-support-services
credential_objectives:
  - google-it-support::c5m4
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 3
prerequisites:
  - security-measures-overview
  - networking-tools
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to apply network hardening techniques including disabling unused protocols, enabling logging, and using monitoring tools to detect anomalies.

## Content stub

- **Disable unused services and ports:** close listening ports; disable Telnet, FTP, SNMPv1; use SSH instead of Telnet
- **Network segmentation:** VLANs to isolate traffic; DMZ for public-facing servers; micro-segmentation concept
- **Firewall rules review:** default-deny stance; removing overly permissive rules; logging denied traffic
- **IDS/IPS:** intrusion detection vs. prevention; signature-based vs. anomaly-based; placement in network
- **Log monitoring:** syslog, Windows Event Forwarding, SIEM basics; what to look for in network logs
- **Vulnerability scanning:** Nessus, OpenVAS basics; agent vs. agentless; interpreting a basic scan report

## Assessment stub

- Hardening checklist: apply a provided network hardening checklist to a simulated environment
- Log analysis: given a syslog excerpt, identify two anomalous events and explain why they are suspicious
- Short answer: what is the difference between an IDS and an IPS?
