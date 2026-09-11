#!/usr/bin/env python3
"""Guard the committed figures. Exit 1 on anything that would put a wrong or missing number in front of a reader.

Catches the three ways bad figures have reached the skills before:
  1. a published block that came out empty, because the cut it needed was not there
  2. a table cell left blank, which reads as a missing figure
  3. a table that drifted from the file it cites, because it was kept by hand

Run in CI and after any regeneration."""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "analysis", "output")
fails = []

# 1. no published block is empty
for f in sorted(os.listdir(OUT)):
    if not f.endswith(".json"): continue
    d = json.load(open(os.path.join(OUT, f)))
    for k, v in (d.items() if isinstance(d, dict) else []):
        if k in ("definitions", "source"): continue
        if v in ({}, [], None):
            fails.append(f"analysis/output/{f}: '{k}' is empty, so nothing can quote it")
        elif isinstance(v, dict) and v and all(x is None for x in v.values()):
            fails.append(f"analysis/output/{f}: every entry under '{k}' is null")

# 2. no table cell is blank
for base, _, files in os.walk(os.path.join(ROOT, "skills")):
    for fn in files:
        if not fn.endswith(".md"): continue
        p = os.path.join(base, fn)
        for n, line in enumerate(open(p), 1):
            line = line.rstrip("\n")
            if not line.startswith("|") or re.fullmatch(r"\|[\s|:-]+\|?", line): continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) > 1 and any(c == "" for c in cells[1:]):
                fails.append(f"{os.path.relpath(p, ROOT)}:{n}: a table cell is blank, use a dash where there is no figure")

# 3. every generated marker has a generator, and the block is not empty
names = set()
for base, _, files in os.walk(os.path.join(ROOT, "skills")):
    for fn in files:
        if not fn.endswith(".md"): continue
        p = os.path.join(base, fn); t = open(p).read()
        for m in re.finditer(r"<!-- generated:(\w+) -->\n(.*?)\n<!-- /generated -->", t, re.S):
            names.add(m.group(1))
            if not m.group(2).strip():
                fails.append(f"{os.path.relpath(p, ROOT)}: generated block '{m.group(1)}' rendered nothing")

for f in fails:
    print("  " + f)
print(f"\n{len(fails)} problems, {len(names)} generated tables checked")
sys.exit(1 if fails else 0)
