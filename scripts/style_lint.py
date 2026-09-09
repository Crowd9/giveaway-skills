#!/usr/bin/env python3
"""Style rules on every Markdown file: no em dash, no semicolon outside code, no curly quotes, no "rather than" or
"instead of" outside tables and the last-pass rule. Exit 1 on a hit. Run in CI and before a commit."""
import os, re, sys

CONTRAST = re.compile(r"\b(rather than|instead of)\b", re.I)

def check(path):
    hits = []; code = False
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        if line.strip().startswith("```"): code = not code; continue
        if code or line.startswith("|") or "last pass" in line.lower(): continue
        quoted = '"rather than"' in line or '"instead of"' in line or "no semicolons" in line
        if "—" in line: hits.append((n, "em dash"))
        if ";" in line and "&" not in line and not quoted: hits.append((n, "semicolon"))
        if any(ch in line for ch in "“”‘’"): hits.append((n, "curly quote"))
        if CONTRAST.search(line) and not quoted: hits.append((n, "contrast pivot"))
    return hits

def main():
    bad = 0
    for root, _, files in os.walk("."):
        if any(p in root for p in (".git", "node_modules", ".omc", ".private", ".remember", "analysis/output")): continue
        for f in files:
            if not f.endswith(".md"): continue
            p = os.path.join(root, f)
            for n, why in check(p): print(f"{p}:{n}: {why}"); bad += 1
    print("style ok" if not bad else f"{bad} style hits"); return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
