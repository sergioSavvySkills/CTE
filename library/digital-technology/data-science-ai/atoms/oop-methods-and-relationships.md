---
atom_id: oop-methods-and-relationships
title: OOP Methods and Combining Classes
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::3.4
skill_type: both
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - oop-classes-objects-instances
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to declare methods on a class, call them on instances, and combine classes via composition or inheritance.

## Content stub

- **Declaring methods:** def inside class; takes `self`; can read/write self's attributes; returns a value or None
- **Instance methods vs static methods:** most methods act on instance data; static methods don't need self and belong to the class
- **Composition:** an object contains other objects (a Car HAS-A Engine); wire via attributes
- **Inheritance:** class Dog(Animal): — Dog inherits methods from Animal and can override them
- **When to use which:** favor composition for loose coupling; use inheritance only for clear IS-A relationships

## Assessment stub

- Given an `Animal` class with a `.speak()` method, write a `Dog` subclass that overrides `.speak()`
- Lab: build a `Classroom` that contains a list of `Student` objects and a `.class_average()` method
- Short answer: why do most style guides say 'prefer composition over inheritance'?
