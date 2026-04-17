---
atom_id: introduction-to-sql-and-dbms
title: Introduction to SQL and DBMS
subcluster: data-science-ai
credential_objectives:
  - comptia-data-plus::2.2
skill_type: both
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - spreadsheets-vs-databases
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to describe what a DBMS is and write simple SQL SELECT queries with filtering and sorting.

## Content stub

- **DBMS role:** manages storage, concurrency, integrity, and query execution; examples: PostgreSQL, MySQL, SQLite, SQL Server
- **SELECT basics:** `SELECT column_list FROM table;` — the fundamental query
- **WHERE clause:** filter rows by a condition: `WHERE age > 18 AND city = 'Atlanta'`
- **ORDER BY and LIMIT:** sort results and cap how many rows come back
- **Joins preview:** combine rows from two tables on a matching key (covered in a later lesson)
- **SQL vs NoSQL:** SQL for structured relational data; NoSQL (MongoDB, Redis) for document/key-value/graph data

## Assessment stub

- Write 3 SQL queries against a students table: list all, filter by grade>80, order by last_name
- Lab: run the queries on an SQLite file in the browser or DB Browser
- Short answer: what is the role of a DBMS that a spreadsheet doesn't provide?
