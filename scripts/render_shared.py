#!/usr/bin/env python3
"""Write the rules every skill shares into every skill, from one copy of each.

Ten skills kept the same rules by hand and they drifted. The answer style had ten checksums on the day
all ten were edited. The dataset scope had five wordings, three of them saying the data starts at 1,000
Entrants when it starts at 101, so three skills told the reader their campaign was too small to compare.
A rule worded ten ways is ten rules, and nothing in the repo could say which differences were meant.

Each shared block lives in one file under scripts/ and is written into every skill between markers:

    <!-- generated:NAME -->
    ...
    <!-- /generated -->

Anything a single skill needs of its own sits outside the markers, under the same heading, where a
re-render leaves it alone. That is where a skill's own evidence limits and its own questions live.

  python3 scripts/render_shared.py            # rewrite every skill
  python3 scripts/render_shared.py --check    # exit 1 if a copy has drifted (CI)

A skill missing a block's markers is an error, not something to guess at: adding a block to a skill is a
deliberate act, because it decides what that skill tells the reader.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# block name -> the file holding the one copy
BLOCKS = {
    "answer_style": "scripts/answer-style.md",
    "asking": "scripts/asking.md",
    "evidence_scope": "scripts/evidence-scope.md",
}

# whole files copied into every skill, so a skill folder installed on its own still has them.
# The answer style is forty-odd rules. Measured across 40 answers, a model self-checking them by
# reading still left about 10 style faults per 1,000 words, most of them the contrast sentences the
# rules ban twice over. The checker catches those deterministically in one command, so it ships.
FILES = {"scripts/style_check.py": "evals/style_check.py"}
BANNER = ("# Generated from evals/style_check.py by scripts/render_shared.py. Edit the source, never this copy.\n"
          "# Run it on a draft answer before sending: python3 scripts/style_check.py draft.txt\n")


def block_re(name):
    return re.compile(r"(<!-- generated:" + re.escape(name) + r" -->\n).*?(<!-- /generated -->\n)", re.S)


def main():
    check = "--check" in sys.argv
    sources = {}
    for name, path in BLOCKS.items():
        text = open(os.path.join(ROOT, path), encoding="utf-8").read()
        sources[name] = text if text.endswith("\n") else text + "\n"

    copies = {}
    for dest, src in FILES.items():
        body = open(os.path.join(ROOT, src), encoding="utf-8").read()
        first, _, rest = body.partition("\n")
        copies[dest] = first + "\n" + BANNER + rest if first.startswith("#!") else BANNER + body

    drifted, written, missing = [], 0, []
    for skill in sorted(glob.glob(os.path.join(ROOT, "skills", "*", ""))):
        for dest, body in copies.items():
            path = os.path.join(skill, dest)
            if os.path.exists(path) and open(path, encoding="utf-8").read() == body:
                continue
            rel = os.path.relpath(path, ROOT)
            if check:
                drifted.append(rel)
            else:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                open(path, "w", encoding="utf-8").write(body)
                os.chmod(path, 0o755)
                written += 1

    for f in sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md"))):
        rel = os.path.relpath(f, ROOT)
        text = new = open(f, encoding="utf-8").read()
        for name, body in sources.items():
            pat = block_re(name)
            if not pat.search(new):
                missing.append(f"{rel}: no '{name}' block")
                continue
            new = pat.sub(lambda m: m.group(1) + body + m.group(2), new)
        if new == text:
            continue
        if check:
            drifted.append(rel)
        else:
            open(f, "w", encoding="utf-8").write(new)
            written += 1

    for m in missing:
        print(f"ERROR {m}")
    if check:
        for d in drifted:
            print(f"  {d}: a shared block differs from its source under scripts/")
        print(f"{len(drifted)} skills out of date" if drifted else "shared blocks in sync across all skills")
        return 1 if (drifted or missing) else 0
    print(f"{written} skills rewritten" if written else "shared blocks already in sync")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
