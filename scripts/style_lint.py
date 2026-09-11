#!/usr/bin/env python3
"""Style rules on every Markdown file: no em dash, no semicolon outside code, no curly quotes, no "rather than" or
"instead of" outside tables and the last-pass rule. Exit 1 on a hit. Run in CI and before a commit."""
import os, re, sys

# Kept in step with CONTRAST in evals/style_check.py. These drifted apart once, and the repo shipped a
# subject line ("You did not win, but here is X% off") that the answer checker fails. A rule the prose
# breaks is a rule the answers learn to break.
CONTRAST = re.compile(r"\b(rather than|instead of)\b|\bnot \w+(?: \w+){0,4}, (?:but|it's|it is)\b|\binstead\b\s*[.,]", re.I)
# Two rates under one in one sentence is arithmetic homework. A single price (0.79 USD) reads fine.
BARE_RATE = re.compile(r"(?<![\w.`$])0\.\d+(?![\w%`])[^|\n]{0,80}?(?<![\w.`$])0\.\d+(?![\w%`])")

def check(path):
    """Root docs also take Stu Case headings, because they are the pages a reader meets on GitHub."""
    root_doc = os.path.dirname(os.path.abspath(path)) == os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    hits = []; code = False
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        if line.strip().startswith("```"): code = not code; continue
        if code or line.startswith("|") or "last pass" in line.lower(): continue
        quoted = '"rather than"' in line or '"instead of"' in line or "no semicolons" in line
        if "—" in line: hits.append((n, "em dash"))
        if ";" in line and "&" not in line and not quoted: hits.append((n, "semicolon"))
        if any(ch in line for ch in "“”‘’"): hits.append((n, "curly quote"))
        # Gleam's words take a capital in prose. A URL is not prose, and a capital there is a 404.
        if URL_CAP.search(line): hits.append((n, "capital inside a URL"))
        if CONTRAST.search(line) and not quoted: hits.append((n, "contrast pivot"))
        m = BARE_RATE.search(line) if "/references/" in path.replace(os.sep, "/") else None
        if m and "USD" not in m.group(0) and "$" not in m.group(0):
            hits.append((n, "two rates under one in a sentence, say them per 100"))
        if root_doc and line.startswith("#"):
            bad = stu_case_problem(re.sub(r"^#+\s*", "", line))
            if bad: hits.append((n, f"heading not Stu Case: {bad}"))
    return hits

URL_CAP = re.compile(r"https?://[^\s)\]`]*(?:Prize|Winner|Entrant|Contestant|Action|Impression|Conversion|Entry|Entries)")

SMALL = {"a", "an", "the", "and", "or", "but", "of", "in", "on", "at", "to", "by", "for", "as"}

def stu_case_problem(heading):
    """Stu Case: every word capitalised except articles, conjunctions and prepositions of three letters or fewer.
    The first and last word always go up. Returns the first offending word, or None."""
    h = heading.strip()
    if " " not in h or re.fullmatch(r"[a-z0-9._/-]+", h): return None  # a slug or a filename is a name, not a heading
    words = [w for w in re.split(r"\s+", h) if w]
    for i, w in enumerate(words):
        core = re.sub(r"^[^A-Za-z]+|[^A-Za-z]+$", "", w)
        if not core or core.isupper() or "`" in w or any(c.isupper() for c in core[1:]):
            continue
        first_last = i == 0 or i == len(words) - 1
        low = core.lower()
        if low in SMALL and not first_last:
            if core[0].isupper(): return w
        elif not core[0].isupper():
            return w
    return None

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
