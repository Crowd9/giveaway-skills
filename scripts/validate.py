#!/usr/bin/env python3
"""Validate every skill: frontmatter, size, reference links, prose style, evals file. Exit 1 on any error."""
import glob, json, os, re, sys

MAX_LINES = 200
STYLE = [("em dash", "—"), ("semicolon in prose", ";"), ("curly quote", "[“”‘’]")]
errors, warnings = [], []

try:
    version_rows = re.findall(r"^\| ([a-z0-9-]+) \| (\S+) \|$", open("VERSIONS.md").read(), re.M)
    versions = dict(version_rows)
    if len(versions) != len(version_rows):
        errors.append("VERSIONS.md: duplicate skill version rows")
except OSError as ex:
    versions = {}
    errors.append(f"VERSIONS.md: cannot read version table ({ex})")

try:
    plugin_version = json.load(open(".claude-plugin/plugin.json"))["version"]
    marketplace_version = json.load(open(".claude-plugin/marketplace.json"))["metadata"]["version"]
    if not plugin_version or plugin_version != marketplace_version:
        errors.append("repo version: plugin.json and marketplace.json disagree or have an empty version")
except (OSError, ValueError, KeyError, TypeError) as ex:
    errors.append(f"repo version: cannot read manifest versions ({ex})")

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
    metadata = re.search(r"^metadata:[ \t]*\n((?:[ \t]+[^\n]*\n?)+)", fm, re.M)
    ver = re.search(r"^[ \t]+version:[ \t]*(\S+)", metadata.group(1), re.M) if metadata else None
    if not fname or fname.group(1).strip() != name: errors.append(f"{name}: frontmatter name must equal directory name")
    if not re.fullmatch(r"[a-z0-9]([a-z0-9-]{0,62}[a-z0-9])?", name) or "--" in name: errors.append(f"{name}: invalid name")
    if not desc or not 1 <= len(desc.group(1)) <= 1024: errors.append(f"{name}: description missing or over 1024 chars")
    if not ver or ver.group(1) in ('""', "''", "null", "~"): errors.append(f"{name}: no metadata.version")
    elif versions.get(name) != ver.group(1).strip("\"'"):
        errors.append(f"{name}: metadata.version disagrees with VERSIONS.md table")
    if len(text.splitlines()) >= MAX_LINES: errors.append(f"{name}: SKILL.md must be under {MAX_LINES} lines")
    for ref in set(re.findall(r"`(references/[a-z0-9-]+\.md)`", text)):
        if not os.path.exists(os.path.join(d, ref)): errors.append(f"{name}: {ref} referenced but missing")
    for md in glob.glob(d + "**/*.md", recursive=True):
        t = open(md).read()
        for i, l in prose_lines(t):
            for label, pat in STYLE:
                if re.search(pat, l) and "semicolons" not in l and "em dashes" not in l:
                    errors.append(f"{os.path.relpath(md)}:{i}: {label}")
    ev = os.path.join(d, "evals", "evals.json")
    if not os.path.exists(os.path.join(d, "evals", "cases.md")): errors.append(f"{name}: no evals/cases.md")
    if not os.path.exists(ev): errors.append(f"{name}: no evals/evals.json")
    else:
        try:
            j = json.load(open(ev)); assert j["skill_name"] == name and j["evals"]
            sys.path.insert(0, os.path.abspath("evals"))
            from check_deliverable import validate_cases
            validate_cases(j["evals"])
            for e in j["evals"]:
                assert {"id", "prompt", "expected_output", "assertions"} <= set(e)
                for c in e.get("checks", []):
                    assert (set(c) == {"contains"} and c["contains"]) or (set(c) == {"not_count"} and c["not_count"] and re.compile(c["not_count"])) or (set(c) <= {"count", "min"} and "count" in c and re.compile(c["count"]) and c.get("min", 1) >= 1), c
        except Exception as ex: errors.append(f"{name}: evals.json invalid ({ex})")

for w in warnings: print("warn ", w)
for e in errors: print("ERROR", e)
print(f"{len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
