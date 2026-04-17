---
atom_id: ip-addressing-and-subnetting
title: IP Addressing and Subnetting
subcluster: it-support-services
credential_objectives:
  - google-it-support::c2m2
skill_type: knowledge
grade_band: HS
estimated_minutes: 60
difficulty: 3
prerequisites:
  - binary-number-systems
  - networking-fundamentals
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to classify IPv4 addresses by class, determine network and host IDs from a subnet mask, and calculate the usable host range of a subnet.

## Content stub

- **IPv4 address classes:** Class A (1–126), B (128–191), C (192–223); private ranges (10.x, 172.16–31.x, 192.168.x); loopback 127.0.0.1
- **Subnet masks:** /8, /16, /24 CIDR; converting between CIDR and dotted-decimal; AND operation to find network ID
- **Subnetting math:** how many subnets / hosts: 2^n subnets, 2^h − 2 hosts; working through /26 and /28 examples
- **Broadcast and network addresses:** network address (all host bits = 0), broadcast (all host bits = 1); not assignable to hosts
- **VLSM concept:** variable-length subnet masking; fitting subnets of different sizes into an address space
- **IPv6 overview:** 128-bit hex notation; ::1 loopback; /64 prefix standard; why IPv6 was needed

## Assessment stub

- Subnetting worksheet: given five /24 networks to divide, calculate network address, broadcast, and host range for each
- Binary subnet: convert a /27 mask to binary and perform the AND operation with an IP
- Short answer: why are private IP ranges not routable on the public internet?
