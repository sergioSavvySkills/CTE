---
atom_id: dns-fundamentals
title: DNS Resolution and Record Types
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

Students will be able to trace a DNS resolution from browser to authoritative server, identify common DNS record types, and troubleshoot DNS failures.

## Content stub

- **DNS resolution process:** recursive resolver → root nameserver → TLD server → authoritative server; TTL caches the answer; browser cache is checked first
- **Common record types:** A (IPv4 address), AAAA (IPv6), CNAME (alias), MX (mail routing), PTR (reverse lookup), TXT (SPF/DKIM email auth)
- **DNS troubleshooting:** `nslookup` queries, `ipconfig /flushdns` clears Windows cache, checking `/etc/hosts` for local overrides
- **Split DNS:** internal zone resolves to private IP, external zone resolves to public IP — same hostname, different answers depending on where you query from

## Assessment stub

- DNS trace: use nslookup to query a domain and identify which server returned the authoritative answer
- Record matching: given 6 DNS scenarios, identify the correct record type to create
