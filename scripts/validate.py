#!/usr/bin/env python3
"""Validate every skill: frontmatter, size, reference links, prose style, evals file. Exit 1 on any error."""
import glob, json, os, re, sys

MAX_LINES = 200
STYLE = [("em dash", "—"), ("semicolon in prose", ";"), ("curly quote", "[“”‘’]")]
errors, warnings = [], []

def prose_lines(text):
    for i, l in enumerate(text.split("\n"), 1):
        if l.startswith("|") or l.startswith("    ") or l.startswith("```"): continue
        yield i, l

for d in sorted(glob.glob("skills/*/")):
    name = os.path.basename(d.rstrip("/"))
    f = os.path.join(d, "SKILL.md")
    if not os.path.exists(f): errors.append(f"{name}: missing SKILL.md"); continue
    text = open(f).read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m: errors.append(f"{name}: missing frontmatter"); continue
    fm = m.group(1)
    fname = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    ver = re.search(r"^\s+version:\s*(\S+)$", fm, re.M)
    if not fname or fname.group(1).strip() != name: errors.append(f"{name}: frontmatter name must equal directory name")
    if not re.fullmatch(r"[a-z0-9]([a-z0-9-]{0,62}[a-z0-9])?", name) or "--" in name: errors.append(f"{name}: invalid name")
    if not desc or not 1 <= len(desc.group(1)) <= 1024: errors.append(f"{name}: description missing or over 1024 chars")
    if not ver: warnings.append(f"{name}: no metadata.version")
    if text.count("\n") > MAX_LINES: warnings.append(f"{name}: SKILL.md over {MAX_LINES} lines")
    for ref in set(re.findall(r"`(references/[a-z0-9-]+\.md)`", text)):
        if not os.path.exists(os.path.join(d, ref)): errors.append(f"{name}: {ref} referenced but missing")
    for md in glob.glob(d + "**/*.md", recursive=True):
        t = open(md).read()
        for i, l in prose_lines(t):
            for label, pat in STYLE:
                if re.search(pat, l) and "semicolons" not in l and "em dashes" not in l:
                    errors.append(f"{os.path.relpath(md)}:{i}: {label}")
    ev = os.path.join(d, "evals", "evals.json")
    if not os.path.exists(ev): warnings.append(f"{name}: no evals/evals.json")
    else:
        try:
            j = json.load(open(ev)); assert j["skill_name"] == name and j["evals"]
            for e in j["evals"]: assert {"id", "prompt", "expected_output", "assertions"} <= set(e)
        except Exception as ex: errors.append(f"{name}: evals.json invalid ({ex})")

for w in warnings: print("warn ", w)
for e in errors: print("ERROR", e)
print(f"{len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
