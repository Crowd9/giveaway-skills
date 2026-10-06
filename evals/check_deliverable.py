#!/usr/bin/env python3
"""Check a saved answer against a case's `checks` in a skill's evals.json.
Usage: python3 evals/check_deliverable.py skills/NAME/evals/evals.json CASE_ID answer.txt
A check is {"contains": "literal"} or {"count": "regex", "min": N} (default 1, regex runs with re.M). Exit 1 on any miss."""
import json, re, sys

def run(checks, text):
    miss = []
    for c in checks:
        if "contains" in c:
            if c["contains"] not in text: miss.append(f'missing {c["contains"]!r}')
        else:
            n = len(re.findall(c["count"], text, re.M))
            if n < c.get("min", 1): miss.append(f'{c["count"]!r}: found {n}, need {c.get("min", 1)}')
    return miss

if __name__ == "__main__":
    path, case, ans = sys.argv[1:4]
    e = next(e for e in json.load(open(path))["evals"] if str(e["id"]) == case)
    miss = run(e.get("checks", []), open(ans).read())
    print(f"case {case}: {'PASS' if not miss else 'FAIL'} ({len(e.get('checks', []))} checks)")
    for m in miss: print("  " + m)
    sys.exit(1 if miss else 0)
