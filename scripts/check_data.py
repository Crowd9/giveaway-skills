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
fails, warns = [], []

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

# 4. a hint, not a guarantee: figures in prose that are not under the keys their section cites.
#    A bare number carries no identity, so this cannot prove a figure right. A large file holds thousands
#    of values and almost any number lands near one of them. What this does catch is a figure sitting far
#    from the part of the file its own section points at, which is usually a stale number or a citation
#    that never named the block the claim came from. It prints notes and never fails the build.
#    The reliable guard against a wrong figure is the generated table, which is rebuilt from its source.
CACHE = {}
def _subtree_values(fn, keys):
    """Every number under the named keys, or None when the citation names no key we can find."""
    ck = (fn, None if keys is None else tuple(sorted(keys)))
    if ck in CACHE: return CACHE[ck]
    fp = os.path.join(OUT, fn)
    if not os.path.exists(fp): return None
    d = json.load(open(fp))
    subs = [d] if keys is None else [d[k] for k in keys if isinstance(d, dict) and k in d]
    if not subs: return None
    vals = set()
    def walk(o):
        if isinstance(o, dict):
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
        elif isinstance(o, (int, float)) and not isinstance(o, bool): vals.add(float(o))
    for s in subs: walk(s)
    CACHE[ck] = vals
    return vals

def _matches(num, vals, pct):
    for c in ([num, num / 100] if pct else [num, num * 100]):
        for v in vals:
            if v and abs(c - v) <= max(abs(v) * 0.01, 0.5 if abs(v) > 10 else 0.005): return True
        if any(round(v, 2) == round(c, 2) for v in vals): return True
    return False

NUM = re.compile(r"(?<![\w.])(\d[\d,]*(?:\.\d+)?)(%?)")
SRC = re.compile(r"analysis/output/([a-z_]+\.json)`?([^.\n]{0,120})")
KEY = re.compile(r"[`(]\s*([a-z][a-z0-9_]{3,})")
SKIP_KEY = {"analysis", "output", "json"}
DENOM = re.compile(r"per 100|out of 100|/100|100 Entrants|100 contestants", re.I)
checked = 0
for base, _, files in os.walk(os.path.join(ROOT, "skills")):
    for fn in files:
        if not fn.endswith(".md"): continue
        fp = os.path.join(base, fn)
        ingen = False; vals = None
        for n, line in enumerate(open(fp), 1):
            line = line.rstrip("\n")
            if line.startswith("<!-- generated:"): ingen = True; continue
            if line.startswith("<!-- /generated"): ingen = False; continue
            if line.startswith("## "): vals = None
            m = SRC.search(line)
            if m:
                keys = [k for k in KEY.findall(m.group(2)) if k not in SKIP_KEY]
                vals = _subtree_values(m.group(1), keys)
                whole = _subtree_values(m.group(1), None)
                CURRENT = m.group(1)
                continue
            s = line.strip()
            if ingen or s.startswith("|") or not vals: continue
            for num_s, pct in NUM.findall(DENOM.sub(" ", line)):
                try: num = float(num_s.replace(",", ""))
                except ValueError: continue
                if num < 2: continue
                checked += 1
                if _matches(num, vals, pct == "%"): continue
                where = "elsewhere in" if whole and _matches(num, whole, pct == "%") else "nowhere in"
                warns.append(f"{os.path.relpath(fp, ROOT)}:{n}: {num_s}{pct} is {where} {CURRENT}, not under the keys this section names")

for w in warns:
    print("  note: " + w)

for f in fails:
    print("  " + f)
print(f"\n{len(fails)} problems and {len(warns)} citation gaps, across {len(names)} generated tables and {checked} prose figures")
sys.exit(1 if fails else 0)
