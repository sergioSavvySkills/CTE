---
atom_id: networking-tools
title: Networking Tools and Diagnostics
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core1::2.8
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - network-configuration
  - tcp-udp-protocols
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to use command-line and physical networking tools to gather information, test connectivity, and diagnose network problems.

## Content stub

- **ping:** ICMP echo request/reply; testing reachability; TTL values; interpreting packet loss
- **tracert/traceroute:** mapping the hop-by-hop path; identifying where packets are dropped or delayed
- **ipconfig/ifconfig/ip:** reading and releasing/renewing IP configuration on Windows and Linux
- **nslookup/dig:** querying DNS; checking A, MX, CNAME records; diagnosing DNS failures
- **netstat:** active connections, listening ports, routing table; spotting unexpected connections
- **Physical tools:** cable tester, toner probe/fox-and-hound, loopback plugs, Wi-Fi analyzer apps

## Assessment stub

- CLI lab: run ping, tracert, and nslookup on a live network and document the results
- Diagnose scenario: given tracert output that shows timeout at hop 3, identify where the failure is
- Short answer: what is the difference between ping and tracert?
