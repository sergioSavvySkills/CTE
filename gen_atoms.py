#!/usr/bin/env python3
"""Reusable atom generator — reads JSON data file, writes .md files"""
import json, os, sys

BASE = "/home/user/CTE/library/atoms/it-support-services"
os.makedirs(BASE, exist_ok=True)

T = """\
---
atom_id: {id}
title: {title}
subcluster: it-support-services
credential_objectives:{creds}
skill_type: {skill}
grade_band: HS
estimated_minutes: {mins}
difficulty: {diff}
prerequisites:{prereqs}
status: draft
reviewer:
review_date:
---

## Learning objective

{obj}

## Content stub

{content}

## Assessment stub

{assess}
"""

def block(items, prefix="  - "):
    return ("\n" + "".join(prefix + i + "\n" for i in items)).rstrip() if items else " []"

def run(path):
    data = json.load(open(path))
    n = 0
    for a in data:
        fp = os.path.join(BASE, a["id"] + ".md")
        if os.path.exists(fp):
            print(f"SKIP: {a['id']}"); continue
        txt = T.format(
            id=a["id"], title=a["title"],
            creds=block(a.get("creds", [])),
            skill=a["skill"], mins=a["mins"], diff=a["diff"],
            prereqs=block(a.get("prereqs", [])),
            obj=a["obj"],
            content="\n".join(f"- **{h}:** {b}" for h,b in a["content"]),
            assess="\n".join(f"- {x}" for x in a["assess"]),
        )
        open(fp, "w").write(txt)
        print(f"WROTE: {a['id']}"); n += 1
    print(f"\nTotal: {n}")

if __name__ == "__main__":
    run(sys.argv[1])
