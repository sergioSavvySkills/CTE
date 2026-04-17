---
atom_id: network-configuration
title: Network Configuration Concepts (IP, DNS, DHCP)
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core1::2.4
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - ip-addressing-and-subnetting
  - dns-and-dhcp-services
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to configure network adapter settings including static and dynamic IP, DNS servers, and default gateway, and verify connectivity using command-line tools.

## Content stub

- **IPv4 address structure:** four octets; network vs. host portion; subnet mask in decimal and CIDR notation
- **Static vs. DHCP:** when to assign static IPs (servers, printers, routers) vs. let DHCP assign; lease time
- **Default gateway:** router's IP on the local subnet; how traffic leaves the LAN; what happens without a gateway
- **DNS configuration:** primary and secondary DNS; public DNS servers (8.8.8.8, 1.1.1.1); what happens when DNS is wrong
- **IPv6 basics:** 128-bit addresses; link-local, global unicast, loopback; dual-stack environments
- **Verification commands:** ipconfig /all, ping, tracert/traceroute, nslookup — reading the output

## Assessment stub

- Lab: configure a static IP, subnet mask, gateway, and DNS on a Windows VM and verify internet access
- Output reading: given ipconfig output, identify the IP, subnet mask, gateway, and lease expiry
- Short answer: a computer has an IP of 169.254.x.x — what does this indicate and how do you fix it?
