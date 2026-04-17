#!/usr/bin/env python3
"""Reusable atom generator — reads JSON data file, writes .md files.

Usage:
    python3 gen_atoms.py <data.json>                     # IT-Support (default)
    python3 gen_atoms.py <data.json> --sub <subcluster>  # any subcluster
"""
import argparse, json, os

CLUSTER_OF = {
    "it-support-services": "digital-technology",
    "data-science-ai": "digital-technology",
    "network-systems-cybersecurity": "digital-technology",
    "software-solutions": "digital-technology",
    "web-cloud": "digital-technology",
    "unmanned-vehicle-technology": "digital-technology",
}

T = """\
---
atom_id: {id}
title: {title}
subcluster: {sub}
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

def run(path, sub):
    cluster = CLUSTER_OF.get(sub)
    if not cluster:
        raise SystemExit(f"Unknown subcluster '{sub}'. Add it to CLUSTER_OF in gen_atoms.py.")
    base = f"/home/user/CTE/library/{cluster}/{sub}/atoms"
    os.makedirs(base, exist_ok=True)

    data = json.load(open(path))
    n = 0
    for a in data:
        fp = os.path.join(base, a["id"] + ".md")
        if os.path.exists(fp):
            print(f"SKIP: {a['id']}"); continue
        txt = T.format(
            id=a["id"], title=a["title"], sub=sub,
            creds=block(a.get("creds", [])),
            skill=a["skill"], mins=a["mins"], diff=a["diff"],
            prereqs=block(a.get("prereqs", [])),
            obj=a["obj"],
            content="\n".join(f"- **{h}:** {b}" for h, b in a["content"]),
            assess="\n".join(f"- {x}" for x in a["assess"]),
        )
        open(fp, "w").write(txt)
        print(f"WROTE: {a['id']}"); n += 1
    print(f"\nTotal: {n}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("data")
    p.add_argument("--sub", default="it-support-services")
    args = p.parse_args()
    run(args.data, args.sub)
