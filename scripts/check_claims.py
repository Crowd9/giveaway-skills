#!/usr/bin/env python3
"""Check the sentences that interpret a generated table against the table itself. Exit 1 on a contradiction.

The tables are rebuilt from the data. The sentences beside them are written by hand, and when the data moves
underneath, the sentence keeps its old direction. That is not a hypothetical: when the benchmark floor went
from 1,000 Entrants to 100 the all-campaign typical fell to 492, and five sentences in hooks-and-themes.md
were left saying a group sat below typical when the rebuilt table put it above. One of them told a store its
own campaign shape underperformed, when the table has it at 47% above typical on Entrants.

check_data.py guards a table cell going blank or a block rendering nothing. This guards the sentence that
reads the table. It looks at one shape, the one that broke:

    - **Row label** ... above/below the typical figure ... on <metric>

and compares the direction with the row, against the table's baseline row where it has one, or against 1.00
where the column is a value index. A claim it cannot resolve confidently is left alone, because a checker
that guesses is worse than no checker.

  python3 scripts/check_claims.py
  python3 scripts/check_claims.py --self-test
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# words in a sentence that name a column, mapped to the words a header uses
METRICS = {
    "entrants": "entrants", "size": "entrants", "crowd": "entrants",
    "conversion rate": "conversion rate", "share to enter": "conversion rate",
    "value index": "value index",
    "referrals": "referrals",
    "actions per entrant": "actions per entrant",
}
UP = r"(?:above|higher than|more than|over)"
DOWN = r"(?:below|under|lower than|fewer than|less than)"
BASE = r"(?:the )?(?:all-campaign )?(?:typical|baseline)(?: figures?)?"


def num(s):
    s = s.strip().split("(")[0].strip().rstrip("%")
    try:
        return float(s.replace(",", ""))
    except ValueError:
        return None


# longest first, so "Referrals % of Entrants" is referrals and never Entrants
COLUMNS = ["actions per entrant", "conversion rate", "value index", "referrals", "entrants"]


def column(header):
    """Which metric a table header names, or None."""
    for c in COLUMNS:
        if c in header:
            return c
    return None


def tables(text):
    """Every generated table, as (headers, {row label: {metric: value}}, baseline row or None)."""
    out = []
    for m in re.finditer(r"<!-- generated:\w+ -->\n(.*?)\n<!-- /generated -->", text, re.S):
        rows = [l for l in m.group(1).split("\n") if l.startswith("|")]
        if len(rows) < 3:
            continue
        head = [c.strip().lower() for c in rows[0].strip("|").split("|")]
        data, base = {}, None
        for r in rows[2:]:
            cells = [c.strip() for c in r.strip("|").split("|")]
            if len(cells) != len(head):
                continue
            label = re.sub(r"\*|\(.*?\)", "", cells[0]).strip().lower()
            vals = {}
            for h, c in zip(head[1:], cells[1:]):
                v = num(c)
                if v is not None:
                    key = column(h)
                    if key:
                        vals[key] = v
            data[label] = vals
            if "all campaigns" in label or "baseline" in label:
                base = vals
        if data:
            out.append((data, base))
    return out


def singular(w):
    """rstrip("s") turns "launches" into "launche", which matches nothing. Take one ending off, once."""
    if w.endswith("es") and len(w) > 3:
        return w[:-2]
    if w.endswith("s") and len(w) > 2:
        return w[:-1]
    return w


def stem(s):
    """Fold a label so 'Product launch' matches the prose's 'Product launches'."""
    s = re.sub(r"[^a-z ]", " ", s.lower())
    return " ".join(singular(w) for w in s.split() if w not in ("or", "and", "the", "a"))


def check(path):
    with open(path, encoding="utf-8") as resource:
        text = resource.read()
    tabs = tables(text)
    if not tabs:
        return []
    hits, ingen = [], False
    for n, line in enumerate(text.split("\n"), 1):
        if line.startswith("<!-- generated:"):
            ingen = True; continue
        if line.startswith("<!-- /generated"):
            ingen = False; continue
        if ingen or line.startswith("|"):
            continue
        if not line.startswith("- **"):
            continue
        for label_raw, clause in clauses(line):
            hits += claims(label_raw, clause, tabs, path, n)
    return hits


def clauses(line):
    """Each bold label in a bullet, with the text it owns up to the next bold label."""
    parts = re.split(r"\*\*(.+?)\*\*", line)
    return [(parts[i], parts[i + 1]) for i in range(1, len(parts) - 1, 2)]


def claims(label_raw, clause, tabs, path, n):
        hits = []
        label = stem(label_raw)
        for data, base in tabs:
            row = next((v for k, v in data.items() if stem(k) == label), None)
            if not row:
                continue
            for word, metric in METRICS.items():
                if metric not in row:
                    continue
                # "sits below the typical figure on Entrants", "above typical on value index"
                for direction, pat in (("up", UP), ("down", DOWN)):
                    if not re.search(pat + r"[^.]{0,40}" + BASE + r"[^.]{0,60}\b" + re.escape(word) + r"\b", clause, re.I):
                        continue
                    ref = 1.0 if metric == "value index" else (base or {}).get(metric)
                    if ref is None:
                        continue
                    actual = "up" if row[metric] > ref else "down"
                    if actual != direction and abs(row[metric] - ref) > ref * 0.02:
                        hits.append(f"{os.path.relpath(path, ROOT)}:{n}: \"{label_raw}\" says {direction} on "
                                    f"{metric}, the table says {row[metric]} against {ref}")
        return hits


# ---- the always-loaded body ----------------------------------------------------------------
#
# A SKILL.md body is in context every time the skill runs, and nothing checked it. The worst
# figure in the repo lived there for months: "campaigns with 11 or more methods drew a quarter
# fewer Entrants and about 32 of every 100 entered, against about 48" where the table it cited
# says 17% MORE Entrants at 31 against 44. It was found by an eval, not a check.
#
# A bare number carries no identity, so checking one against a whole file proves nothing. Two
# things here are identifying enough to gate on:
#   a pair, "519 against 443", where both must sit in one column of one table in the file the
#     line itself names, and
#   a distinctive value, three digits or a decimal, which must appear in that named file.
# A figure on a line naming no reference is reported and never fails, because the citation
# habit is being adopted a line at a time.

# the six size-band edges, the population and a year are structural, stated once in the shared
# evidence block, so a line repeating one is not quoting an uncited finding
STRUCTURAL = {"100", "250", "500", "1000", "2500", "10000", "117348", "117300",
              "2024", "2025", "2026", "2027", "2028", "2029", "2030"}

SKILL_NUM = re.compile(r"(?<![\w.])(\d[\d,]*(?:\.\d+)?)\s*(%?)")
SKILL_REF = re.compile(r"`references/([a-z0-9-]+\.md)`")
# the repo already cites aggregates this way in its reference files, so a skill body may too
SKILL_OUT = re.compile(r"`analysis/output/([a-z_]+\.json)`")
EXTRACTED_COUNTS = re.compile(r"\[Extracted from ([\d,]+) campaigns and ([\d,]+) businesses\b[^\]]*\]")


def check_extracted(path, root):
    """Check bracketed population counts only against one explicitly cited distribution."""
    hits = []
    with open(path, encoding="utf-8") as source:
        for n, line in enumerate(source, 1):
            counts = EXTRACTED_COUNTS.findall(line)
            outs = set(SKILL_OUT.findall(line))
            if len(counts) != 1 or len(outs) != 1:
                continue
            out = next(iter(outs))
            fp = os.path.join(root, "analysis", "output", out)
            if not os.path.exists(fp):
                continue
            with open(fp, encoding="utf-8") as aggregate:
                data = json.load(aggregate)
            distribution = data.get("distribution") if isinstance(data, dict) else None
            if not isinstance(distribution, dict) or not all(
                    type(distribution.get(key)) is int for key in ("campaigns", "businesses")):
                continue
            for key, stated in zip(("campaigns", "businesses"), counts[0]):
                if int(stated.replace(",", "")) != distribution[key]:
                    hits.append(f"{os.path.relpath(path, root)}:{n}: extracted {key} count {stated} "
                                f"disagrees with {out} distribution.{key} ({distribution[key]:,})")
    return hits


# ---- suppressed groups in cited blocks ----------------------------------------------------

# These two legacy sections predate source notes. Their current explicit
# citations establish the source for the exact same tables in older revisions.
LEGACY_YEAR_TABLES = {
    "skills/giveaway-prize-picker/references/roi-benchmarks.md",
    "skills/giveaway-results-review/references/benchmarks.md",
}


def check_suppressed(path, root):
    """Check tables in a citation's heading section and prose in its own paragraph.

    A heading of any level bounds a section. Within it, tables use the nearest
    citation paragraph (ties prefer a following source note). This avoids
    applying a later table's source to an earlier, unrelated table. Prose never
    inherits a citation across a blank line. Uncited blocks remain unchecked except the two documented legacy year tables.
    """
    with open(path, encoding="utf-8") as source:
        text = source.read()
    hits, cache = [], {}
    # Only an explicit label mapping in this document supplies a human alias.
    # Never guess that underscores, substrings or similar words name one group.
    aliases = {}
    for raw, human in re.findall(r"`([a-z][a-z0-9_]*)` \(([A-Za-z][A-Za-z /&,-]{1,60})\)", text):
        aliases.setdefault(raw.casefold(), set()).add(human.strip().casefold())
    for human, raw in re.findall(r"(?:^|\n)([A-Za-z][A-Za-z /&,-]{1,60}) \(`([a-z][a-z0-9_]*)`\)", text):
        aliases.setdefault(raw.casefold(), set()).add(human.strip().casefold())
    # The ROI reference also defines one-to-one aliases as "gaming is
    # gaming_esports, technology is electronics_tech". A list of several raw
    # groups is an aggregate, not a human name for any individual child.
    for human, raw in re.findall(
            r"\b([a-z][a-z0-9_]*) is ([a-z][a-z0-9]*_[a-z0-9_]+)"
            r"(?=,\s*[a-z][a-z0-9_]* is\b|[.)]|$)", text, re.I):
        aliases.setdefault(raw.casefold(), set()).add(human.casefold())
    lines = text.splitlines()
    headings = [-1] + [i for i, line in enumerate(lines) if re.match(r"^#{1,6}\s", line)] + [len(lines)]
    for start, end in zip(headings, headings[1:]):
        paragraphs, current = [], []
        for i in range(start + 1, end):
            if lines[i].strip():
                current.append(i)
            elif current:
                paragraphs.append(current)
                current = []
        if current:
            paragraphs.append(current)
        citations = []
        legacy = (os.path.relpath(path, root).replace(os.sep, "/") in LEGACY_YEAR_TABLES
                  and start >= 0 and lines[start].strip() == "## By start year"
                  and not any(SKILL_OUT.search(lines[i]) for i in range(start + 1, end)))
        if legacy:
            # A synthetic source paragraph supplies table scope only, never prose.
            paragraphs.append([])
        for indexes in paragraphs:
            paragraph = ("\n".join(lines[i] for i in indexes) if indexes else
                         "`analysis/output/roi_benchmarks.json` (`by_start_year`)")
            matches = list(SKILL_OUT.finditer(paragraph))
            groups, resolved = [], False
            for j, match in enumerate(matches):
                filename = match.group(1)
                if filename not in cache:
                    fp = os.path.join(root, "analysis", "output", filename)
                    if not os.path.isfile(fp):
                        cache[filename] = {}
                    else:
                        with open(fp, encoding="utf-8") as aggregate:
                            cache[filename] = json.load(aggregate)
                data = cache[filename]
                if not isinstance(data, dict):
                    continue
                tail = paragraph[match.end():matches[j + 1].start() if j + 1 < len(matches) else len(paragraph)]
                # Existing citations use backticks or parenthesized bare keys.
                keys = re.findall(r"`([a-z][a-z0-9_.]*)`", tail)
                for parenthesized in re.findall(r"\(([^)]*)\)", tail):
                    keys += re.findall(r"\b[a-z][a-z0-9_]*\b", parenthesized)
                for key in dict.fromkeys(keys):
                    node = data
                    for part in key.split("."):
                        node = node.get(part) if isinstance(node, dict) else None
                    if not isinstance(node, dict):
                        continue
                    resolved = True
                    labels = {str(k).casefold() for k, value in node.items() if value is None}
                    listed = node.get("suppressed_below_floor", [])
                    if isinstance(listed, list):
                        labels.update(str(k).casefold() for k in listed if isinstance(k, (str, int)))
                    labels |= {alias for label in labels for alias in aliases.get(label, ())}
                    for label in sorted(labels):
                        groups.append((filename, key, label))
            if resolved:
                citations.append((indexes or [end], groups))
            if groups:
                # Numeric labels alone are not figures. Remove all suppressed
                # labels before looking for another number in the same sentence.
                prose = "\n".join(lines[i] for i in indexes if not lines[i].lstrip().startswith("|"))
                prose = SKILL_OUT.sub("", prose)
                for sentence in re.split(r"(?<=[.!?])\s+", prose):
                    for filename, key, label in groups:
                        pattern = r"(?<!\w)" + re.escape(label) + r"(?!\w)"
                        if not re.search(pattern, sentence, re.I):
                            continue
                        remainder = sentence
                        for _, _, other in groups:
                            remainder = re.sub(r"(?<!\w)" + re.escape(other) + r"(?!\w)", "", remainder, flags=re.I)
                        if SKILL_NUM.search(remainder):
                            hits.append(f"{os.path.relpath(path, root)}:{indexes[0] + 1}: prose quotes suppressed "
                                        f"label {label!r} from {filename} ({key})")
        if not citations:
            continue
        # A table is one contiguous run of pipe rows; generated markers do not
        # change its scope. Formatting on a label does not change its identity.
        for match in re.finditer(r"(?m)^[ \t]*\|[^\n]*(?:\n[ \t]*\|[^\n]*)*", "\n".join(lines[start + 1:end])):
            row_start = start + 1 + "\n".join(lines[start + 1:end])[:match.start()].count("\n")
            rows = match.group().splitlines()
            row_end = row_start + len(rows) - 1
            indexes, groups = min(citations, key=lambda item: (
                min(abs(row_start - item[0][-1]), abs(item[0][0] - row_end)),
                item[0][0] < row_start))
            for offset, row in enumerate(rows):
                first = row.strip().strip("|").split("|", 1)[0].strip().strip("*` ").casefold()
                for filename, key, label in groups:
                    if first == label:
                        hits.append(f"{os.path.relpath(path, root)}:{row_start + offset + 1}: table quotes suppressed "
                                    f"label {label!r} from {filename} ({key})")
    return hits


# a figure describing a file that ships with the skill is checked by counting that file, which the
# reader can do as easily as the checker, so naming it is enough
SKILL_EX = re.compile(r"`examples/[a-z0-9-]+\.(?:csv|json)`")
# the left value must not be the end of a range: "250 to 500, against 779" compares 779 with a band,
# never 500 with 779
SKILL_PAIR = re.compile(r"(?<!to )(?<![\w.])(\d[\d,]*(?:\.\d+)?)\s*%?\s*(?:against|versus|vs\.?|compared with)\s*"
                        r"(?:about\s+|roughly\s+|around\s+)?(\d[\d,]*(?:\.\d+)?)")
# "of every 100 against 44" is a denominator and a value, never a pair
DENOM = re.compile(r"(?:per|of every|out of)\s+100\s*(?:,)?\s*(?:against|versus)", re.I)


def columns_of(text):
    """Every table column in a file, as a list of value sets, so a pair can be matched inside one."""
    cols = []
    for block in re.findall(r"(?:^|\n)((?:\|[^\n]*(?:\n|$))+)", text):
        rows = [r for r in block.split("\n") if r.startswith("|")]
        if len(rows) < 3:
            continue
        width = len(rows[0].strip("|").split("|"))
        for c in range(width):
            vals = set()
            for r in rows[2:]:
                cells = r.strip("|").split("|")
                if c < len(cells):
                    for m in re.finditer(r"(?<![\w.])(\d[\d,]*(?:\.\d+)?)", cells[c]):
                        vals.add(m.group(1).replace(",", ""))
            if vals:
                cols.append(vals)
    return cols


def check_skill(path, root):
    """Figures in a SKILL.md body, against the reference each line names."""
    with open(path, encoding="utf-8") as resource:
        text = resource.read()
    skill_dir = os.path.dirname(path)
    cache = {}
    hard, notes, ingen, infront = [], [], False, False
    for n, line in enumerate(text.split("\n"), 1):
        # the frontmatter carries the version, 1.6.0, which reads as the figure 1.6 and is not a claim
        if n == 1 and line == "---":
            infront = True; continue
        if infront:
            infront = line != "---"; continue
        if line.startswith("<!-- generated:"):
            ingen = True; continue
        if line.startswith("<!-- /generated"):
            ingen = False; continue
        if ingen or line.startswith("#") or line.startswith("|"):
            continue
        # a figure inside a quoted example is teaching the model how to phrase a sentence, not stating a
        # finding, and SHA-256 names an algorithm. Neither is a citable claim, so strip them before looking.
        bare = re.sub(r'"[^"]*"', ' ', line)
        bare = re.sub(r"\bSHA-\d+", " ", bare)
        nums = [(a, b) for a, b in SKILL_NUM.findall(bare)]
        big = [a.replace(",", "") for a, b in nums
               if ("." in a or "," in a or len(a) >= 3) and float(a.replace(",", "")) > 1.5
               and a.replace(",", "") not in STRUCTURAL]
        if not big and not SKILL_PAIR.search(bare):
            continue
        refs = SKILL_REF.findall(line)
        outs = SKILL_OUT.findall(line)
        if SKILL_EX.search(line):
            continue
        # the repo labels a claim extracted, inferred or advice. A window chosen as practice, such as
        # reading outcomes at 30, 60 and 90 days, has no cut behind it and no citation to give, so a line
        # that says so is taken at its word.
        if "(advice" in line:
            continue
        if not refs and not outs:
            if big:
                notes.append(f"{os.path.relpath(path, root)}:{n}: {', '.join(sorted(set(big))[:4])} "
                             f"names no reference, so nothing can check it")
            continue
        # a line may cite several references, and the figure need only be in one of them
        plain, cols, named = set(), [], []
        for ref in refs:
            fp = os.path.join(skill_dir, "references", ref)
            if not os.path.exists(fp):
                continue
            if fp not in cache:
                with open(fp, encoding="utf-8") as resource:
                    body = resource.read()
                cache[fp] = (set(re.findall(r"(?<![\w.])(\d[\d,]*(?:\.\d+)?)", body.replace(",", ""))),
                             columns_of(body))
            p_, c_ = cache[fp]
            plain |= p_; cols += c_; named.append(ref)
        for out in outs:
            fp = os.path.join(root, "analysis", "output", out)
            if not os.path.exists(fp):
                continue
            if fp not in cache:
                import json as _json
                got = set()
                def _walk(o):
                    if isinstance(o, dict):
                        for v in o.values(): _walk(v)
                    elif isinstance(o, list):
                        for v in o: _walk(v)
                    elif isinstance(o, (int, float)) and not isinstance(o, bool):
                        got.add(("%f" % float(o)).rstrip("0").rstrip("."))
                        got.add(("%f" % (float(o) * 100)).rstrip("0").rstrip("."))
                with open(fp) as resource:
                    _walk(_json.load(resource))
                cache[fp] = (got, [])
            p_, _ = cache[fp]
            plain |= p_; named.append(out)
        if not named:
            continue
        where = " or ".join(named)
        for v in big:
            if v not in plain:
                hard.append(f"{os.path.relpath(path, root)}:{n}: {v} is in neither {where}, which this line cites")
        if not DENOM.search(bare):
            for a, b in SKILL_PAIR.findall(bare):
                a, b = a.replace(",", ""), b.replace(",", "")
                if not any(a in c and b in c for c in cols):
                    hard.append(f"{os.path.relpath(path, root)}:{n}: \"{a} against {b}\" is not one column of any "
                                f"table in {where}, so the two are not a matched pair")
    return hard, notes


def self_test():
    """A planted inversion must fail, and the file as it stands must pass."""
    import tempfile
    table = "| Group | Entrants |\n|---|---|\n| First | 382 |\n| All | 492 |"
    for prefix in ("", "Reference\n\n"):
        for suffix in ("", "\n"):
            assert columns_of(prefix + table + suffix) == [{"382", "492"}], \
                "table boundary dropped a cited value"
    with tempfile.TemporaryDirectory() as root:
        os.makedirs(os.path.join(root, "analysis", "output"))
        fixture = os.path.join(root, "analysis", "output", "roi_benchmarks.json")
        with open(fixture, "w", encoding="utf-8") as aggregate:
            json.dump({"by_start_year": {"2020": None, "2022": {"n": 50},
                                       "suppressed_below_floor": ["2021"]},
                       "other": {"2020": {"n": 50}},
                       "by_type": {"retail_store": None, "suppressed_below_floor": 1}}, aggregate)
        reference = os.path.join(root, "reference.md")
        source_note = "Source: `analysis/output/roi_benchmarks.json` (`by_start_year`)."
        table = "| Year | Campaigns |\n|---|---|\n| 2022 | 50 |"
        def suppressed(text, path=reference):
            with open(path, "w", encoding="utf-8") as resource:
                resource.write(text)
            return check_suppressed(path, root)
        current = "## By start year\n\n" + table + "\n\n" + source_note
        assert not suppressed(current), "published year row should pass"
        mapped = ("`retail_store` (Retail shops)\n\n| Type | Campaigns |\n|---|---|\n| RETAIL SHOPS | 50 |\n\n"
                  "Source: `analysis/output/roi_benchmarks.json` (`by_type`).")
        assert len(suppressed(mapped)) == 1, "explicit human label mapping missed"
        assert not suppressed(mapped.replace("`retail_store` (Retail shops)", "")), "unguessed human form matched"
        prose_mapping = mapped.replace("`retail_store` (Retail shops)", "Retail is retail_store, technology is electronics_tech.").replace("RETAIL SHOPS", "Retail")
        assert len(suppressed(prose_mapping)) == 1, "explicit 'human is raw_key' mapping missed"
        grouped_mapping = prose_mapping.replace("Retail is retail_store, technology", "Retail is retail_store, online_store and mall_store, technology")
        assert not suppressed(grouped_mapping), "aggregate mapping treated as one suppressed child"
        assert len(suppressed(current.replace("| 2022 |", "| 2020 |"))) == 1, "null year row missed"
        assert len(suppressed(current.replace("| 2022 |", "| 2021 |"))) == 1, "listed year row missed"
        assert len(suppressed(current.replace("`by_start_year`", "by_start_year").replace(
            "| 2022 |", "| 2020 |"))) == 1, "bare citation key missed"
        assert len(suppressed("2020 drew 500 Entrants. " + source_note)) == 1, "suppressed prose missed"
        assert not suppressed("2020 is not published. " + source_note), "label alone is not a figure"
        assert not suppressed("2020 and 2021 are not published. " + source_note), "year list is not a figure"
        assert not suppressed("2020 drew 500 Entrants.\n\n" + source_note), "prose crossed paragraph"
        assert not suppressed(source_note + "\n\n## Other\n\n" + table.replace("2022", "2020")), "citation crossed heading"
        assert not suppressed(current + "\n\n" + table.replace("2022", "2020") +
                              "\n\nSource: `analysis/output/roi_benchmarks.json` (`other`)."), "citation crossed table source"
        for relative in LEGACY_YEAR_TABLES:
            legacy_path = os.path.join(root, relative)
            os.makedirs(os.path.dirname(legacy_path), exist_ok=True)
            legacy = current.replace("2022", "2020").replace(source_note, "")
            assert len(suppressed(legacy, legacy_path)) == 1, "legacy suppressed year missed"
            assert not suppressed(legacy), "legacy exception leaked to an unrelated path"
    with tempfile.TemporaryDirectory() as root:
        os.makedirs(os.path.join(root, "analysis", "output"))
        fp = os.path.join(root, "analysis", "output", "sample.json")
        tmp = os.path.join(root, "reference.md")
        with open(fp, "w", encoding="utf-8") as aggregate:
            json.dump({"distribution": {"campaigns": 1234, "businesses": 56}}, aggregate)
        def extracted(text):
            with open(tmp, "w", encoding="utf-8") as reference:
                reference.write(text)
            return check_extracted(tmp, root)
        valid = "[Extracted from 1,234 campaigns and 56 businesses, `analysis/output/sample.json`.]"
        assert not extracted(valid), "matching extracted population should pass"
        assert len(extracted(valid.replace("1,234", "1,235"))) == 1, "stale campaign count was missed"
        assert len(extracted(valid.replace("56 businesses", "57 businesses"))) == 1, "stale business count was missed"
        stale = valid.replace("1,234", "9,999")
        assert not extracted(stale.replace("`analysis/output/sample.json`", "no citation")), "uncited counts must be skipped"
        assert not extracted(stale + " `analysis/output/other.json`"), "multiple cited sources must be skipped"
        with open(fp, "w", encoding="utf-8") as aggregate:
            json.dump({"distribution": [{"campaigns": 1234, "businesses": 56}]}, aggregate)
        assert not extracted(stale), "ambiguous distribution must be skipped"
    src = os.path.join(ROOT, "skills", "giveaway-idea-generator", "references", "hooks-and-themes.md")
    assert not check(src), f"the live file should be clean: {check(src)}"
    with open(src, encoding="utf-8") as resource:
        text = resource.read()
    # Anchor on the shape of the sentence, never on its figures. Pinning the exact numbers meant every honest
    # correction to the prose broke this self-test, and it stayed broken through several pushes because the
    # gate sweep ran the checks without running their self-tests.
    planted, n_sub = re.subn(
        r"- \*\*Product launches\*\* draw a little more crowd than typical at [\d,]+ Entrants against [\d,]+,",
        "- **Product launches** sit below the typical figure on Entrants,", text, count=1)
    assert n_sub == 1, "the planted fault did not apply, the sentence has moved"
    tmp = os.path.join(ROOT, ".planted-check.md")
    with open(tmp, "w") as resource:
        resource.write(planted)
    try:
        found = check(tmp)
        assert found, "a planted inversion was not caught, so this check proves nothing"
    finally:
        os.remove(tmp)
    # the worst figure this repo has shipped, replanted: the line cites mix-by-objective.md and the
    # pair it states is in no column of it
    sk = os.path.join(ROOT, "skills", "giveaway-entry-method-planner", "SKILL.md")
    with open(sk, encoding="utf-8") as resource:
        body = resource.read()
    planted = body.replace(
        "6. **Check friction.**",
        "6. **Check friction.** Extracted: campaigns with 11 or more methods drew a quarter fewer Entrants and "
        "about 32 of every 100 entered, against about 48 for campaigns with 1 to 3 methods, and 1,760 Entrants "
        "against 2,305 (`references/mix-by-objective.md`).", 1)
    assert planted != body, "the friction step has moved, replant the fault somewhere real"
    tmp = sk + ".planted"
    with open(tmp, "w") as resource:
        resource.write(planted)
    try:
        hard, _ = check_skill(tmp, ROOT)
        assert hard, "a replanted stale pair in a skill body was not caught, so this check proves nothing"
    finally:
        os.remove(tmp)
    live_hard = []
    for f in sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md"))):
        live_hard += check_skill(f, ROOT)[0]
    assert not live_hard, f"the skills as they stand should be clean: {live_hard}"
    for pattern in ("skills/*/SKILL.md", "skills/*/references/*.md"):
        for path in glob.glob(os.path.join(ROOT, pattern)):
            assert not check_suppressed(path, ROOT), f"live suppressed claims: {check_suppressed(path, ROOT)}"
    print("self-test passed")
    return 0


def main():
    if "--self-test" in sys.argv:
        return self_test()
    bad, extracted_bad, suppressed_bad = [], [], []
    for f in sorted(glob.glob(os.path.join(ROOT, "skills", "*", "references", "*.md"))):
        bad += check(f)
        extracted_bad += check_extracted(f, ROOT)
        suppressed_bad += check_suppressed(f, ROOT)
    skill_bad, skill_notes = [], []
    for f in sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md"))):
        suppressed_bad += check_suppressed(f, ROOT)
        h, n = check_skill(f, ROOT)
        skill_bad += h; skill_notes += n
    for n in skill_notes:
        print("  note: " + n)
    for b in bad + skill_bad + extracted_bad + suppressed_bad:
        print("  " + b)
    print(f"\n{len(bad)} sentences contradict the table they read, {len(skill_bad)} figures in a skill body "
          f"disagree with the reference it cites, {len(skill_notes)} uncited figures in a skill body, "
          f"{len(extracted_bad)} extracted population counts disagree with their cited distribution, "
          f"{len(suppressed_bad)} claims quote suppressed groups")
    return 1 if (bad or skill_bad or extracted_bad or suppressed_bad) else 0


if __name__ == "__main__":
    sys.exit(main())
