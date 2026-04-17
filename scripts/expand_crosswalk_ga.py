#!/usr/bin/env python3
"""Append direct atom -> Georgia standard rows to crosswalk.csv
to close gaps where atoms cover standards but no credential chain exists.

All rows have:
  state=georgia, source=ai-draft, framework_version=2021-03-04
"""
import csv
from pathlib import Path

FW = Path("/home/user/CTE/library/digital-technology/data-science-ai/crosswalks/georgia/state-framework.csv")
CW = Path("/home/user/CTE/library/digital-technology/data-science-ai/crosswalks/georgia/crosswalk.csv")
ATOMS_DIR = Path("/home/user/CTE/library/digital-technology/data-science-ai/atoms")

VERSION = "2021-03-04"

# Shorthand: employability atoms map to 1.N across all three course prefixes
EMP_ATOMS = [
    ("professional-communication-skills", "1.1"),
    ("creativity-and-innovation-workplace", "1.2"),
    ("critical-thinking-for-career-planning", "1.3"),
    ("work-readiness-and-professional-traits", "1.4"),
    ("teamwork-in-technology-workplace", "1.5"),
    ("professional-image-presentation", "1.6"),
]

CTSO_OVERVIEW = "career-technical-student-organizations-overview"
CTSO_PARTICIPATION = "ctso-participation-and-competitions"

ROWS = []

def add(atom_id, std, strength, rationale):
    ROWS.append((atom_id, "georgia", std, strength, rationale, "ai-draft", "", "", VERSION))

# ================= Employability 1.1-1.6 across all three courses =================
for course_prefix in ("IT-FAI", "IT-AIC", "IT-AIA"):
    for atom, sub in EMP_ATOMS:
        add(atom, f"{course_prefix}-{sub}", "primary",
            "Atom directly teaches this CTAE employability standard")

# ================= CTSO (IT-FAI-9.*, IT-AIC-8.*, IT-AIA-8.*) =================
for course_prefix, parent in (("IT-FAI", 9), ("IT-AIC", 8), ("IT-AIA", 8)):
    add(CTSO_OVERVIEW, f"{course_prefix}-{parent}.1", "primary",
        "Atom introduces CTSO goals, mission, and objectives")
    for sub in (2, 3, 4, 5):
        add(CTSO_PARTICIPATION, f"{course_prefix}-{parent}.{sub}", "primary",
            "Atom covers CTSO opportunities, leadership, and competitions")

# ================= Foundations: AI intro (IT-FAI-2) =================
add("what-is-artificial-intelligence", "IT-FAI-2.1", "primary",
    "Atom defines AI and reflects on current state")
add("history-of-ai-evolution", "IT-FAI-2.2", "primary",
    "Atom describes AI history and evolution over time")
add("history-of-ai-evolution", "IT-FAI-2.3", "primary",
    "Atom identifies early AI examples and contributors")

# ================= IT-FAI-3.4 (AI in art) =================
add("ai-in-art-and-creative-fields", "IT-FAI-3.4", "primary",
    "Atom analyzes AI's impact on art and creative fields")

# ================= IT-AIC-2.1 (AI influence on history/events) =================
add("history-of-ai-evolution", "IT-AIC-2.1", "primary",
    "Atom summarizes AI's influence on historical and contemporary events")
add("ai-industry-trends", "IT-AIC-2.1", "supporting",
    "Atom covers contemporary AI developments shaping events")

# ================= IT-AIC-3.6 (investigate daily AI) =================
add("investigating-ai-in-daily-life", "IT-AIC-3.6", "primary",
    "Atom directly teaches investigating daily-use AI types")

# ================= Foundations: Programming (IT-FAI-4.*) =================
add("algorithms-for-ai", "IT-FAI-4.1", "primary", "Teaches sequence/selection/iteration building blocks")
add("designing-and-modifying-algorithms", "IT-FAI-4.2", "primary", "Teaches modifying and creating algorithms")
add("designing-and-modifying-algorithms", "IT-FAI-4.4", "primary", "Teaches using an algorithm to build a program")
add("programming-paradigms-overview", "IT-FAI-4.6", "primary", "Defines functional/OOP/procedural/logic paradigms")
add("oop-classes-objects-instances", "IT-FAI-4.7", "primary", "Describes OOP principles")
add("programming-paradigms-overview", "IT-FAI-4.7", "supporting", "Introduces OOP as a paradigm")
add("python-control-flow", "IT-FAI-4.8", "primary", "Teaches creating programs with loops and conditionals")
add("python-input-and-decisions", "IT-FAI-4.9", "primary", "Teaches user/sensor input and decision-making")
add("python-collections-and-data-organization", "IT-FAI-4.10", "primary", "Teaches collecting and organizing different data types")
add("comments-documentation-and-ux", "IT-FAI-4.11", "primary", "Teaches commenting to document programs")
add("debugging-and-code-tracing", "IT-FAI-4.12", "primary", "Teaches tracing code and debugging")
add("comments-documentation-and-ux", "IT-FAI-4.13", "primary", "Teaches UX considerations in programming")

# ================= Foundations: Data (IT-FAI-5.*) =================
add("data-processing-cycle", "IT-FAI-5.4", "primary", "Teaches input-processing-output data cycle")
add("bits-and-binary-representation", "IT-FAI-5.5", "primary", "Teaches how computers store data in bits")
add("big-data-and-ai", "IT-FAI-5.6", "primary", "Defines Big Data and its role in AI")
add("how-ai-uses-data-for-predictions", "IT-FAI-5.7", "primary", "Teaches how AI uses data for predictions")
add("boolean-logic-for-ai", "IT-FAI-5.8", "primary", "Teaches logic and its use in AI programming")

# ================= Foundations: Spreadsheets (IT-FAI-6.*) =================
add("spreadsheet-fundamentals-for-data", "IT-FAI-6.1", "primary", "Teaches organizing data using spreadsheet tools")
add("spreadsheet-fundamentals-for-data", "IT-FAI-6.2", "primary", "Teaches preset spreadsheet functions for data manipulation")
add("spreadsheet-advanced-features-and-pivots", "IT-FAI-6.2", "supporting", "Covers advanced spreadsheet manipulation")

# ================= Foundations: Ethics (IT-FAI-7.2, 7.6) =================
add("exploring-bias-with-teachable-machine", "IT-FAI-7.2", "primary", "Directly teaches exploring ML bias with Teachable Machine")
add("ai-for-good-organizations", "IT-FAI-7.6", "primary", "Covers AI for Good Foundation and similar orgs")

# ================= Foundations + Concepts + Applications: Design Thinking =================
add("productive-collaboration-and-diversity", "IT-FAI-8.1", "primary", "Teaches collaboration, problem-solving, leadership")
add("productive-collaboration-and-diversity", "IT-FAI-8.2", "primary", "Teaches value of diversity in collaboration")
add("computational-thinking", "IT-FAI-8.3", "primary", "Teaches computational thinking skills")
add("design-thinking-process", "IT-FAI-8.4", "primary", "Teaches Design Thinking process steps")
add("design-thinking-process", "IT-FAI-8.5", "primary", "Applies Design Thinking to real-world problems")

add("design-thinking-process", "IT-AIC-7.2", "primary", "Uses Design Thinking for real-world AI problems")
add("identify-real-world-ai-problem", "IT-AIC-7.1", "primary", "Teaches identifying real-world problems for AI")
add("end-to-end-ai-project", "IT-AIC-7.3", "primary", "Applies programming/logic/data science to problems")
add("ai-for-good-organizations", "IT-AIC-6.6", "primary", "Research projects from AI for Good Foundation")

add("design-thinking-process", "IT-AIA-6.2", "primary", "Uses problem-solving process for community AI issue")
add("collaborative-ai-solution-design", "IT-AIA-6.3", "primary", "Collaboratively design AI solution for community problem")
add("prototyping-ai-solutions", "IT-AIA-6.3", "supporting", "Design through prototype approach")
# 6.1 and 6.4 likely already covered, will verify

# ================= Concepts: OOP (IT-AIC-4.*) =================
add("computational-thinking", "IT-AIC-4.1", "primary", "Pattern matching and abstraction as CT building blocks")
add("programming-paradigms-overview", "IT-AIC-4.2", "primary", "Benefits and principles of OOP")
add("oop-classes-objects-instances", "IT-AIC-4.3", "primary", "Objects, instances, and their difference")
add("oop-methods-and-relationships", "IT-AIC-4.4", "primary", "Applying OOP to methods and combining classes")
add("python-operators-and-expressions", "IT-AIC-4.5", "primary", "Logical, relational, boolean, mathematical operators")
add("python-data-types", "IT-AIC-4.6", "primary", "Assigning and converting values across data types")
add("python-control-flow", "IT-AIC-4.7", "primary", "Control structures: conditionals, loops, functions")
add("python-functions-and-returns", "IT-AIC-4.8", "primary", "Functions with return values and parameters")
add("python-external-libraries", "IT-AIC-4.9", "primary", "Using external libraries in programs")
add("python-collections-and-data-organization", "IT-AIC-4.10", "primary", "Lists as ordered, indexed data series")
add("python-data-structures-advanced", "IT-AIC-4.11", "primary", "Selecting appropriate data structures")
add("python-data-structures-advanced", "IT-AIC-4.12", "primary", "Implementing data structures in functions")
add("python-functions-and-returns", "IT-AIC-4.13", "supporting", "Functions and their call effects")
add("python-strings-and-text-processing", "IT-AIC-4.14", "primary", "Constructing and implementing strings")

# ================= Concepts: Data Science (IT-AIC-5.*) =================
add("ethical-issues-in-data-science", "IT-AIC-5.2", "primary", "Identifies ethical issues in data science")
add("spreadsheets-vs-databases", "IT-AIC-5.4", "primary", "Comparing spreadsheet and database")
add("datasets-and-dataframes", "IT-AIC-5.6", "primary", "Defines dataset and DataFrame")
add("datasets-and-dataframes", "IT-AIC-5.1", "primary", "Identifies examples of data science in the world")
add("pandas-for-data-work", "IT-AIC-5.1", "supporting", "Shows DS in practice via Pandas")

# ================= Applications: Embedded (IT-AIA-7.*) =================
add("embedded-systems-and-sensors", "IT-AIA-7.1", "primary", "Teaches embedded components: circuits, sensors, microcontrollers, motors")
add("building-an-embedded-robot", "IT-AIA-7.2", "primary", "Assembles an embedded robotic system")
add("programming-a-sensor-driven-robot", "IT-AIA-7.3", "primary", "Writes program for sensor-driven robot")
add("debugging-hardware-issues", "IT-AIA-7.4", "primary", "Debugs hardware issues systematically")


# ================= Validation + write =================
fw_codes = set()
fw_name = {}
with FW.open() as f:
    for r in csv.DictReader(f):
        fw_codes.add(r["standard_code"])
        fw_name[r["standard_code"]] = r["course_code"]

atom_ids = {p.stem for p in ATOMS_DIR.glob("*.md") if not p.stem.startswith("_")}

bad_std = [r[2] for r in ROWS if r[2] not in fw_codes]
bad_atom = [r[0] for r in ROWS if r[0] not in atom_ids]
if bad_std:
    raise SystemExit(f"Bad standard codes: {bad_std[:5]}")
if bad_atom:
    raise SystemExit(f"Bad atom IDs: {bad_atom[:5]}")

# Dedupe against existing crosswalk rows
existing = set()
with CW.open() as f:
    for r in csv.DictReader(f):
        existing.add((r["atom_id"], r["standard_code"]))

new_rows = [r for r in ROWS if (r[0], r[2]) not in existing]

with CW.open("a", newline="") as f:
    w = csv.writer(f)
    for r in new_rows:
        w.writerow(r)

print(f"Appended {len(new_rows)} new crosswalk rows (de-duped from {len(ROWS)} total).")
print(f"Crosswalk size now: {sum(1 for _ in CW.open()) - 1} data rows.")
