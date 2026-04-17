---
atom_id: dns-and-dhcp-services
title: DNS and DHCP Services
subcluster: it-support-services
credential_objectives:
  - google-it-support::c2m4
skill_type: knowledge
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - networking-fundamentals
  - tcp-udp-protocols
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to explain how DNS resolves domain names to IP addresses and how DHCP automatically assigns network configuration to clients.

## Content stub

- **DNS resolution process:** recursive resolver → root → TLD → authoritative server; caching and TTL; browser cache
- **DNS record types:** A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), PTR (reverse lookup), TXT (SPF/DKIM)
- **DHCP operation:** DORA: Discover → Offer → Request → Acknowledge; lease time; scope and exclusions
- **DHCP reservation:** binding an IP to a MAC address; when to use static assignment vs. reservation
- **DNS troubleshooting:** nslookup queries, flushing DNS cache (ipconfig /flushdns), checking /etc/hosts
- **Split DNS:** internal vs. external DNS zones; why a hostname might resolve differently inside vs. outside the network

## Assessment stub

- DNS query trace: use nslookup to trace a domain resolution and describe each server involved
- DHCP scenario: a new printer must always get the same IP — explain two ways to achieve this
- Short answer: what happens if DHCP is unavailable when a Windows PC boots?
