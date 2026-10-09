"""Check distinct-business counts at every depth of published aggregate JSON.

This guard checks explicit counts, including subgroup counts on comparison rows.
It cannot recover missing distinct-business counts from campaign counts. Private
generators must calculate those counts and suppress small groups before export.
"""
import re


FLOOR = 5
COUNT_KEY = re.compile(
    r"^(?:(?:n_(?:businesses|organizers|organisers))|"
    r"(?:(?:unique|distinct)_)?(?:business|organizer|organiser)_count|"
    r"(?:(?:unique|distinct|ordinary|clean|valued|collab)_)?"
    r"(?:businesses|organizers|organisers)"
    r"(?:_(?:count|sites|reached|offered|with|with_5_plus_campaigns|"
    r"top|rest|top_stratified|top_raw))?)$"
)


def privacy_problems(value, path="$"):
    """Return failures without printing group labels, which may be private.

Zero-person cohorts may describe an empty exclusion category. They are accepted
only when every numeric statistic in that object is zero and its campaign count
is explicitly zero. A parent count never excuses a smaller nested subgroup.
"""
    problems = []
    if isinstance(value, dict):
        for key, count in value.items():
            if not COUNT_KEY.fullmatch(key):
                continue
            if type(count) is not int or count < 0:
                problems.append(f"{path}: {key} must be a nonnegative integer")
            elif count < FLOOR and not (count == 0 and _empty_cohort(value)):
                problems.append(f"{path}: {key} is below the five-business privacy floor")
        for index, child in enumerate(value.values()):
            problems.extend(privacy_problems(child, f"{path}.object[{index}]"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            problems.extend(privacy_problems(child, f"{path}[{index}]"))
    return problems


def _empty_cohort(value):
    def zero_stats(child):
        if isinstance(child, dict):
            return all(zero_stats(v) for v in child.values())
        if isinstance(child, list):
            return all(zero_stats(v) for v in child)
        if isinstance(child, (int, float)):
            return type(child) is not bool and child == 0
        return child is None

    return value.get("campaigns") == 0 and zero_stats(value)


# Synthetic data is confined to these reviewed examples and self-test fixtures.
CSV_PATHS = frozenset({
    "skills/giveaway-random-draw/examples/sample-entrants.csv",
    "skills/giveaway-results-review/examples/sample-actions-export.csv",
})
EMAIL_FIXTURE_PATHS = CSV_PATHS | frozenset({
    "evals/test_export_to_draw.py",
    "skills/giveaway-random-draw/scripts/draw.py",
    "skills/giveaway-results-review/scripts/campaign_report.py",
    "skills/giveaway-results-review/scripts/dashboard.py",
    "skills/giveaway-results-review/scripts/gleam_export.py",
})
# Non-reserved domains are accepted only for the existing literal fixtures.
EXTRA_EMAILS = {
    "skills/giveaway-random-draw/examples/sample-entrants.csv": {
        "freeprizes" + "@" + "mailinator.com",
    },
    "skills/giveaway-random-draw/scripts/draw.py": {
        local + "@" + "x.com" for local in ("a", "A", "b", "b+promo", "c", "d")
    } | {"x" + "@" + "mailinator.com"},
}
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}")
IPV4 = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")


def committed_file_problems(path, content, mode="100644"):
    """Check a tracked file without echoing potentially identifying values."""
    from pathlib import PurePosixPath

    problems = []
    suffix = PurePosixPath(path).suffix
    if not (path == "LICENSE" or path.endswith(".gitignore") or suffix in {
            ".md", ".json", ".py", ".txt", ".yml"} or path in CSV_PATHS):
        problems.append("unexpected file type or CSV outside reviewed examples")
    if mode == "120000":
        problems.append("committed symlink")
    # Python self-tests embed CSV lines with escaped newlines.
    for address in EMAIL.findall(content.replace("\\n", "\n")):
        domain = address.rsplit("@", 1)[1]
        if (path in EMAIL_FIXTURE_PATHS and domain in {"example.com", "example.org"}
                or address in EXTRA_EMAILS.get(path, ())):
            continue
        problems.append("email address outside reviewed synthetic fixtures")
        break
    # No tracked fixture currently needs an IP address, including localhost.
    if IPV4.search(content):
        problems.append("IP address found")
    return problems


def check_committed_files():
    """Inspect tracked working-tree contents so local and CI checks agree."""
    from pathlib import Path
    import subprocess

    root = Path(__file__).resolve().parents[1]
    records = subprocess.check_output(
        ["git", "ls-files", "--stage", "-z"], cwd=root
    ).decode().split("\0")
    failures = 0
    for record in filter(None, records):
        metadata, path = record.split("\t", 1)
        mode = metadata.split()[0]
        file = root / path
        if mode == "120000":
            content = ""  # Never follow a symlink to read external content.
        else:
            content = file.read_bytes().decode("utf-8", errors="replace")
        for problem in committed_file_problems(path, content, mode):
            print(f"{path}: {problem}")
            failures += 1
    if not failures:
        print("Tracked-file privacy gate passed")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(check_committed_files())
