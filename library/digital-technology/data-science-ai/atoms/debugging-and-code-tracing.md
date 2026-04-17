---
atom_id: debugging-and-code-tracing
title: Debugging and Tracing Code
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::3.2
skill_type: skill
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

Students will be able to trace code execution by hand, identify common bug patterns, and use print-debugging or a debugger to isolate errors.

## Content stub

- **Error types:** SyntaxError (code won't run), TypeError/ValueError (runtime), logic errors (wrong output, no crash)
- **Reading a traceback:** bottom line names the error; follow the arrows back up to find your own code
- **Print-debugging:** add print() at entry/exit of suspicious blocks; print variable values; remove when fixed
- **Code tracing by hand:** walk through line-by-line with a variable table; catches logic errors before you run
- **Using a debugger:** VS Code / PyCharm breakpoints; step over / into / out; watch expressions
- **Rubber-ducking:** explain your code to a toy or peer — often reveals the bug yourself

## Assessment stub

- Trace by hand: given a loop that's supposed to sum odd numbers 1-10 but outputs wrong, find the bug
- Lab: add 3 strategic print() statements to debug a broken function
- Reflection: describe a bug you found and fixed — how did you localize it?
