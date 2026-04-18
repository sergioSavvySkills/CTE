---
atom_id: network-monitoring-and-vuln-management
title: Network Monitoring and Vulnerability Management
subcluster: it-support-services
credential_objectives:
  - google-it-support::c5m4
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - network-segmentation-and-access-control
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to distinguish IDS from IPS, analyze a network log for anomalies, and interpret a basic vulnerability scan report.

## Content stub

- **IDS vs. IPS:** intrusion detection system alerts only; intrusion prevention system blocks automatically; both can be signature-based (known threats) or anomaly-based (deviation from baseline)
- **Log monitoring:** syslog aggregates network device logs; Windows Event Forwarding centralizes Windows logs; SIEM correlates logs across sources — look for repeated failed logins, unusual outbound ports, off-hours access
- **Vulnerability scanning:** Nessus, OpenVAS scan hosts for known CVEs; agent-based scans the host from inside; agentless scans from the network; scan output is a prioritized list of findings by severity

## Assessment stub

- Log analysis: given a syslog excerpt, identify two suspicious events and explain why each is anomalous
- Short answer: what is the key operational difference between an IDS and an IPS, and which would you choose for a production environment with low false-positive tolerance?
