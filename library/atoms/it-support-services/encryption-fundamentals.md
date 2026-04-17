---
atom_id: encryption-fundamentals
title: Encryption Fundamentals
subcluster: it-support-services
credential_objectives:
  - comptia-itf-plus::6.6
  - google-it-support::c5m2
skill_type: knowledge
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - fundamental-data-types
  - cia-triad
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to explain symmetric and asymmetric encryption, describe how HTTPS uses both, and identify where encryption is applied in common IT scenarios.

## Content stub

- **Symmetric encryption:** same key encrypts and decrypts; AES-128/256; fast; key distribution problem
- **Asymmetric encryption:** key pair (public/private); RSA, ECC; slower; solves key distribution; used for key exchange and signatures
- **Hashing:** one-way function; MD5 (deprecated), SHA-256, bcrypt; file integrity verification; password storage
- **PKI basics:** certificates, Certificate Authorities, chain of trust; how a browser validates a website's cert
- **HTTPS/TLS:** TLS handshake: key exchange → session key → encrypted channel; certificate warnings
- **Encryption at rest vs. in transit:** disk encryption for stored data; TLS/VPN for data in motion; covering both gaps

## Assessment stub

- Concept matching: pair encryption terms (symmetric, hash, PKI, TLS) with real-world examples
- HTTPS investigation: use a browser to inspect a website's SSL certificate details and record expiry, issuer, and key algorithm
- Short answer: if hashing is one-way, how does a system verify a password at login?
