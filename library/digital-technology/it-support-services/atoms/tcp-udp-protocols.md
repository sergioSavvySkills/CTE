---
atom_id: tcp-udp-protocols
title: TCP/UDP Ports and Protocols
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core1::2.1
  - google-it-support::c2m3
skill_type: knowledge
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - networking-fundamentals
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to distinguish between TCP and UDP, identify well-known port numbers, and explain why port numbers matter for network troubleshooting.

## Content stub

- **TCP vs. UDP:** TCP: reliable, ordered, connection-oriented (3-way handshake); UDP: fast, connectionless, no guarantee
- **Ports and sockets:** port numbers 0–65535; well-known (0–1023), registered (1024–49151), dynamic (49152+); a socket = IP + port
- **Common TCP ports:** 20/21 FTP, 22 SSH, 23 Telnet, 25 SMTP, 80 HTTP, 110 POP3, 143 IMAP, 443 HTTPS, 3389 RDP
- **Common UDP ports:** 53 DNS, 67/68 DHCP, 69 TFTP, 123 NTP, 161/162 SNMP
- **Why protocols use TCP vs UDP:** real-time streaming → UDP; file transfer/email → TCP; DNS uses both
- **Firewall and port filtering:** how firewalls allow/block by port; port scanning with nmap; open vs. closed vs. filtered

## Assessment stub

- Port quiz: identify the protocol for 15 port numbers without notes
- Scenario: a user can browse websites (port 80) but cannot send email — which port is likely blocked?
- Wireshark/capture lab: capture a TCP handshake and identify the SYN, SYN-ACK, ACK packets
