---
atom_id: oop-classes-objects-instances
title: OOP Fundamentals: Classes, Objects, Instances
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::3.4
skill_type: both
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - programming-paradigms-overview
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to define a class, instantiate objects from it, and distinguish between a class and its instances.

## Content stub

- **Class as a blueprint:** a class defines what kind of object you can make — attributes (data) and methods (behavior)
- **Instance:** a specific object created from a class; each instance has its own attribute values
- **Writing a class in Python:** `class Dog:` — then methods start with `def name(self, ...):`
- **__init__ constructor:** called automatically on `Dog('Rex')`; usually assigns initial attribute values
- **self:** refers to the specific instance inside a method — how methods read/write that instance's data
- **Class vs instance mental model:** `class Dog:` is the Dog blueprint; `rex = Dog('Rex')` is one real dog

## Assessment stub

- Write a `Student` class with name and grade attributes and a `.promote()` method that increments grade
- Create 3 instances of `Student` and verify each has independent state
- Short answer: why does `self` appear as the first parameter of every method?
