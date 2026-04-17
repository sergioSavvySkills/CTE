---
atom_id: database-queries
title: Database Interfaces and Query Languages
subcluster: it-support-services
credential_objectives:
  - comptia-itf-plus::5.3
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - database-structures
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to write basic SQL queries to retrieve, filter, and sort data, and describe how non-technical users interact with databases through application interfaces.

## Content stub

- **SQL SELECT basics:** SELECT columns FROM table; * wildcard; aliases; running queries in a client tool
- **Filtering with WHERE:** comparison operators, AND/OR/NOT, LIKE for pattern matching, NULL handling
- **Sorting and limiting:** ORDER BY ASC/DESC; LIMIT/TOP; why result order isn't guaranteed without ORDER BY
- **Aggregates:** COUNT, SUM, AVG, MIN, MAX; GROUP BY; HAVING to filter groups
- **JOINs overview:** INNER JOIN to combine related tables; concept of LEFT JOIN; reading a query with two tables
- **Application interfaces:** forms, reports, dashboards as front-ends to databases; why end users rarely write SQL

## Assessment stub

- SQL lab: run five provided queries against a sample database and record the results
- Write a query: given a table schema, write a query to find all employees in a specific department sorted by salary
- Short answer: what is the difference between WHERE and HAVING?
