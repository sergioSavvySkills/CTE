---
atom_id: python-functions-and-returns
title: Python Functions, Parameters, and Return Values
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::3.2
skill_type: both
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - python-control-flow
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to define Python functions with positional, keyword, and default parameters, return values, and reason about scope.

## Content stub

- **Defining a function:** `def greet(name):` — name is a parameter; the body runs on call
- **Return values:** `return x` sends a value back; without return, the function returns None
- **Parameter types:** positional, keyword, default values, *args, **kwargs
- **Scope:** variables inside a function are local; read-only access to outer scope; global keyword exists but avoid
- **Docstring:** first line of function body can document purpose/args/returns
- **Calling conventions:** `func(arg)`, `func(name='Ada')`, unpacking with `*lst`, `**dct`

## Assessment stub

- Write a function `average(nums)` with a docstring, handle empty list case, test on 3 inputs
- Debug: given a function that modifies a global variable, refactor to use parameters + return
- Short answer: what's the difference between positional and keyword arguments?
