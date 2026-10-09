#!/usr/bin/env python3
"""Validate every skill: frontmatter, size, reference links, prose style, evals file. Exit 1 on any error."""
import glob, html, json, os, re, sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

MAX_LINES = 200
STYLE = [("em dash", "—"), ("semicolon in prose", ";"), ("curly quote", "[“”‘’]")]

def visible_markdown(text):
    """Keep line numbers, but omit fenced code and HTML comments."""
    text = re.sub(r"<!--.*?-->", lambda m: "\n" * m[0].count("\n"), text, flags=re.S)
    lines, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            run = marker[1]
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence):
                fence = None
            lines.append("")
        else:
            lines.append("" if fence else line)
    return "\n".join(lines)


def heading_anchors(text):
    anchors, counts = set(), {}
    lines = visible_markdown(text).splitlines()
    for i, line in enumerate(lines):
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)(?:\s+#+)?\s*$", line)
        title = match[1] if match else None
        if title is None and i + 1 < len(lines) and re.fullmatch(r"\s{0,3}(?:=+|-+)\s*", lines[i + 1]) and line.strip():
            title = line.strip()
        if title is None:
            continue
        title = re.sub(r"!?\[([^]]*)\]\([^)]*\)", r"\1", title)
        title = html.unescape(re.sub(r"<[^>]+>", "", title)).lower()
        title = re.sub(r"(?<!\w)(_+)(.+?)\1(?!\w)", r"\2", title)
        slug = re.sub(r"[^\w\- ]", "", title, flags=re.UNICODE).replace(" ", "-")
        candidate = slug
        count = counts.get(slug, 0)
        while candidate in anchors:
            count += 1
            candidate = f"{slug}-{count}"
        counts[slug] = count
        anchors.add(candidate)
    return anchors


def link_targets(text):
    """Yield (line, target, is_code_path) for local-link candidates."""
    # Real commands in fences still need their shipped scripts. Example blocks
    # and tokens containing placeholders describe inputs, not dependencies.
    fence, example, commands, previous = None, False, False, ""
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            if fence is None:
                fence = marker[1]
                commands = marker[2].strip().split(" ")[0] in ("bash", "sh", "shell", "zsh", "console")
                example = bool(re.search(r"\bexamples?\b", previous + " " + marker[2], re.I))
            elif marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                fence = None
            continue
        if fence and commands and not example:
            for match in re.finditer(r"(?<![\w/])(?:references/|scripts/|evals/|analysis/output/)[^\s`\"',;]+", line):
                target = match[0]
                if not re.search(r"[<>*{}$]|\.\.\.", target):
                    yield number, target, True
        if not fence and line.strip():
            previous = line
    text = visible_markdown(text)
    # Markdown permits whitespace/newlines around an inline destination.
    multiline_prose = re.sub(r'`[^`]+`', lambda m: "\n" * m[0].count("\n"), text)
    for match in re.finditer(r'\]\(\s*(<[^>]+>|(?:[^\s()]|\([^()]*\))+)\s*(?:["\'][^\n]*?["\']\s*)?\)', multiline_prose):
        if "\n" in match[0]:
            yield multiline_prose[:match.start()].count("\n") + 1, match[1].strip('<>'), False
    definitions = {}
    for match in re.finditer(r'^ {0,3}\[([^]\n]+)\]:[ \t]*(?:\n[ \t]*)?(<[^>]*>|\S+)', text, re.M):
        definitions[' '.join(match[1].lower().split())] = match[2].strip('<>')
    for number, line in enumerate(text.splitlines(), 1):
        # Inline code may contain commands, so extract the path token only.
        for code in re.findall(r'`([^`]+)`', line):
            for match in re.finditer(r'(?<![\w/])(?:references/|scripts/|evals/|analysis/output/)[^\s`,;]+', code):
                target = match[0]
                if not re.search(r'[<>*{}]|\.\.\.', target):
                    yield number, target, True
        prose = re.sub(r'`[^`]+`', '', line)
        for match in re.finditer(r'\]\(\s*(<[^>]+>|(?:[^\s()]|\([^()]*\))+)\s*(?:["\'][^\n]*?["\']\s*)?\)', prose):
            yield number, match[1].strip('<>'), False
        if re.match(r'^\s{0,3}\[[^]]+\]:', prose):
            match = re.match(r'^\s{0,3}\[([^]]+)\]:', prose)
            key = ' '.join(match[1].lower().split())
            if key in definitions:
                yield number, definitions[key], False
            continue
        for match in re.finditer(r'(?<!!)\[([^]\n]+)\](?:\[([^]\n]*)\])?', prose):
            key = ' '.join((match[2] or match[1]).lower().split())
            if key in definitions:
                yield number, definitions[key], False


def check_links(document, root):
    document, root = Path(document).absolute(), Path(root).absolute()
    skill = next((parent for parent in document.parents if parent.parent == root / 'skills'), None)
    failures = []
    for number, target, code in link_targets(document.read_text()):
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or target.startswith('/'):
            continue
        path, anchor = unquote(parsed.path), unquote(parsed.fragment)
        if not path:
            resolved = document
        elif path.startswith('analysis/output/'):
            resolved = root / path
        elif skill and path.startswith(('references/', 'scripts/', 'evals/')):
            resolved = skill / path
        else:
            resolved = (root if code else document.parent) / path
        label = f'{document.relative_to(root)}:{number}: {target}'
        if not resolved.exists():
            failures.append(f'{label} referenced but missing')
        elif anchor and resolved.suffix.lower() == '.md' and anchor not in heading_anchors(resolved.read_text()):
            failures.append(f'{label} heading anchor missing')
    return list(dict.fromkeys(failures))


def main():
    errors, warnings = [], []

    try:
        version_rows = re.findall(r"^\| ([a-z0-9-]+) \| (\S+) \|$", Path("VERSIONS.md").read_text(), re.M)
        versions = dict(version_rows)
        if len(versions) != len(version_rows):
            errors.append("VERSIONS.md: duplicate skill version rows")
    except OSError as ex:
        versions = {}
        errors.append(f"VERSIONS.md: cannot read version table ({ex})")

    try:
        plugin_version = json.loads(Path(".claude-plugin/plugin.json").read_text())["version"]
        marketplace_version = json.loads(Path(".claude-plugin/marketplace.json").read_text())["metadata"]["version"]
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
        text = Path(f).read_text()
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
        for md in glob.glob(d + "**/*.md", recursive=True):
            t = Path(md).read_text()
            for i, l in prose_lines(t):
                for label, pat in STYLE:
                    if re.search(pat, l) and "semicolons" not in l and "em dashes" not in l:
                        errors.append(f"{os.path.relpath(md)}:{i}: {label}")
        ev = os.path.join(d, "evals", "evals.json")
        if not os.path.exists(os.path.join(d, "evals", "cases.md")): errors.append(f"{name}: no evals/cases.md")
        if not os.path.exists(ev): errors.append(f"{name}: no evals/evals.json")
        else:
            try:
                j = json.loads(Path(ev).read_text()); assert j["skill_name"] == name and j["evals"]
                sys.path.insert(0, os.path.abspath("evals"))
                from check_deliverable import validate_cases
                validate_cases(j["evals"])
                for e in j["evals"]:
                    assert {"id", "prompt", "expected_output", "assertions"} <= set(e)
                    for c in e.get("checks", []):
                        assert (set(c) == {"contains"} and c["contains"]) or (set(c) == {"not_count"} and c["not_count"] and re.compile(c["not_count"])) or (set(c) <= {"count", "min"} and "count" in c and re.compile(c["count"]) and c.get("min", 1) >= 1), c
            except Exception as ex: errors.append(f"{name}: evals.json invalid ({ex})")

    documents = [Path(name) for name in ("README.md", "CONTRIBUTING.md", "AGENTS.md") if Path(name).exists()]
    documents += list(Path("skills").glob("*/SKILL.md"))
    documents += list(Path("skills").glob("*/references/**/*.md"))
    for document in documents:
        errors.extend(check_links(document, Path.cwd()))

    for w in warnings: print("warn ", w)
    for e in errors: print("ERROR", e)
    print(f"{len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
