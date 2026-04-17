---
atom_id: database-structures
title: Database Structures (Relational and Non-Relational)
subcluster: it-support-services
credential_objectives:
  - comptia-itf-plus::5.2
skill_type: knowledge
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - database-concepts
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to describe the structure of relational databases using tables, keys, and relationships, and compare relational to non-relational database types.

## Content stub

- **Tables, rows, columns:** relation = table; tuple = row; attribute = column; every row is unique (primary key)
- **Primary and foreign keys:** primary key uniquely identifies a row; foreign key links rows across tables; referential integrity
- **Relationships:** one-to-one, one-to-many, many-to-many; junction tables; ER diagram basics
- **Normalization:** 1NF/2NF/3NF — eliminating redundancy; why normalized data is easier to maintain
- **Non-relational (NoSQL):** document (MongoDB), key-value (Redis), column (Cassandra), graph; schema-flexible
- **When to use which:** relational for structured, transactional data; NoSQL for scale, flexibility, unstructured data

## Assessment stub

- ER diagram: given a scenario (school with students, courses, and grades), draw the entities and relationships
- Key identification: given a sample table, identify the primary key and any foreign keys
- Short answer: what problem does normalization solve?
