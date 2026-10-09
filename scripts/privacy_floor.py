"""Check business and campaign counts at every depth of published aggregate JSON.

This guard checks explicit counts, including subgroup counts on comparison rows.
It cannot recover missing distinct-business counts from campaign counts. Private
generators must calculate those counts and suppress small groups before export.
"""
import re


FLOOR = 5
COUNT_KEY = re.compile(
    r"^(?:sites|(?:n_(?:businesses|organizers|organisers))|"
    r"(?:(?:unique|distinct)_)?(?:business|organizer|organiser)_count|"
    r"(?:(?:unique|distinct|ordinary|clean|valued|collab)_)?"
    r"(?:businesses|organizers|organisers)"
    r"(?:_(?:count|sites|reached|offered|with|with_5_plus_campaigns|"
    r"top|rest|top_stratified|top_raw))?)$"
)


SUPPRESSION_KEY = "suppressed_below_floor"
SAMPLE_KEY = re.compile(r"^(?:n|campaigns|[a-z_]+_n|n_(?!businesses$|organizers$|organisers$)[a-z_]+)$")
STATISTIC_KEY = re.compile(
    r"^(?:min|max|median|mean|std|count|p[0-9]+|.*_(?:mean|median|share|ratio|percentile))$"
)


def is_count_map(value):
    """Recognize categorical integer counts, excluding summary-statistic objects.

    Labels may be months, years, countries, niches or numeric value bands. The
    suppression marker records removed bucket totals and is never a cohort.
    """
    counts = {key: count for key, count in value.items() if key != SUPPRESSION_KEY}
    return bool(counts) and all(type(count) is int for count in counts.values()) and not any(
        COUNT_KEY.fullmatch(key) or SAMPLE_KEY.fullmatch(key) or STATISTIC_KEY.fullmatch(key)
        for key in counts
    )


# Shares here are fractions of the campaigns in the sibling n/campaigns.
# *_offered pairs with *_uptake; *_share pairs with named conditional summaries
# below. n_<prefix>/<prefix>_n overrides a rounded share when present. Impression
# ratios, baseline rates and shares of a larger parent population are excluded.
NON_CAMPAIGN_SHARES = frozenset({
    "baseline_share", "direct_share", "invalid_share", "median_email_share", "action_uptake",
    "hosted_impression_share", "embed_impression_share", "directory_impression_share",
    "own_product_signal_prize_share", "prize_value_missing_share", "value_stated_share",
    "prize_value_stated_share", "share_of_campaigns", "share_of_prize_records",
    "share_of_country", "share_of_band", "share_of_stores",
    "share_of_tagged_email_impressions", "share_of_actions_worth_gt1",
})
DEPENDENTS = {
    "email_offered": ("email_uptake",),
    "referral_offered": ("referral_uptake",),
    "share_offered": ("referrals_per_contestant", "referral_entries_per_100_entrants_where_offered"),
    "mandatory_share": ("completions_when_mandatory",),
    "any_mandatory_share": ("mandatory_count_when_used_p50", "contestants_mandatory_p50"),
    "country_rule_share": ("contestants_restricted_p50", "impressions_per_contestant_restricted_p50"),
    "wallet_share": ("contestants_wallet_p50", "days_wallet_p50"),
    "question_share": ("validated_given_question", "word_cap_changed_given_question", "word_cap_p50", "contestants_with_question_p50"),
    "pool_stated_share": ("pool_usd_p50",),
    "secret_code_share": ("contestants_secret_p50",),
    "optin_on_or_auto_share": ("contestants_with_optin_p50",),
    "share_action_share": ("share_clicks_per_contestant_p50", "contestants_with_share_p50"),
    "english_share": ("contestants_english_p50",),
    "repeat_campaign_share": ("contestants_repeat_p50",),
    "weekend_start_share": ("contestants_weekend_p50",),
}
COMPLEMENTS = {
    "mandatory_share": ("completions_when_optional",),
    "any_mandatory_share": ("contestants_no_mandatory_p50",),
    "country_rule_share": ("contestants_open_p50", "impressions_per_contestant_open_p50"),
    "wallet_share": ("contestants_no_wallet_p50", "days_no_wallet_p50"),
    "question_share": ("contestants_without_question_p50",),
    "secret_code_share": ("contestants_no_secret_p50",),
    "optin_on_or_auto_share": ("contestants_without_optin_p50",),
    "share_action_share": ("contestants_without_share_p50",),
    "english_share": ("contestants_non_english_p50",),
    "repeat_campaign_share": ("contestants_first_p50",),
    "weekend_start_share": ("contestants_weekday_p50",),
}


def campaign_share(key):
    return key not in NON_CAMPAIGN_SHARES and not key.startswith(("n_", "conditional_")) and (
        key.endswith(("_share", "_offered")) or key.startswith(("share_", "action_", "terms_")))


def conditional_suppressions(value):
    """Fields to withhold, using only support identifiable in this aggregate.

    Campaign support cannot certify five distinct businesses. Rounded shares are
    conservative estimates; private generators must use exact subgroup counts.
    Null shares remain withheld and cannot license a restored conditional metric.
    """
    fields = set()
    n = value.get("n", value.get("campaigns"))
    for key, share in value.items():
        if not campaign_share(key):
            continue
        prefix = key.rsplit("_", 1)[0]
        dependent = set(DEPENDENTS.get(key, ())) | {prefix + "_uptake"}
        count = value.get(prefix + "_n", value.get("n_" + prefix))
        support = count if type(count) is int else (
            n * share if type(n) is int and type(share) in (int, float) and 0 <= share <= 1 else None)
        if (support is not None and support < FLOOR) or share is None:
            fields.update(k for k in dependent if k in value and value[k] is not None)
        if share is None:
            fields.update(k for k in COMPLEMENTS.get(key, ()) if k in value and value[k] is not None)
        if type(n) is int and type(share) in (int, float) and 0 < share < 1:
            remaining = n - support
            if support < FLOOR or remaining < FLOOR:
                fields.add(key)
            if remaining < FLOOR:
                fields.update(k for k in COMPLEMENTS.get(key, ()) if k in value and value[k] is not None)
    # *_given_<condition> is a campaign proportion within the condition.
    # Its own numerator and complement need the floor too, even when the
    # condition as a whole has ample support (for example validated questions).
    for key, rate in value.items():
        if "_given_" not in key or type(rate) not in (int, float) or not 0 < rate < 1:
            continue
        condition = key.split("_given_", 1)[1]
        denominator = value.get("n_" + condition, value.get(condition + "_n"))
        if type(denominator) is not int:
            share = value.get(condition + "_share", value.get(condition + "_offered"))
            denominator = n * share if type(n) is int and type(share) in (int, float) else None
        if denominator is not None and (denominator * rate < FLOOR or denominator * (1 - rate) < FLOOR):
            fields.add(key)
    # Explicit denominator conventions cover uptake rows and pairwise methods.
    for key, metric in value.items():
        if metric is None:
            continue
        count_keys = []
        if key.endswith("_uptake"):
            prefix = key[:-7]
            count_keys = [prefix + "_n", "n_" + prefix]
        elif key == "uptake" or key == "uptake_ratio_to_baseline":
            count_keys = ["n_offered"]
        elif key.startswith("conditional_") and "_given_" in key:
            count_keys = ["n_" + key.split("_given_", 1)[1], "n_both"]
        elif key == "lift":
            count_keys = ["n_both"]
        if any(type(value.get(k)) is int and value[k] < FLOOR for k in count_keys):
            fields.add(key)
    # A single hidden member of a published partition or sum is recoverable.
    # Business+ is Business plus Premium, so hiding Business also protects a
    # suppressed Premium from both that sum and the four-tier total.
    for members in (
        ("business_share", "premium_share", "business_plus_share"),
        ("optin_on_share", "optin_auto_share", "optin_on_or_auto_share"),
        ("free_share", "pro_share", "business_share", "premium_share"),
        ("template_share", "own_copy_share", "blank_share"),
    ):
        if not all(k in value for k in members):
            continue
        hidden = [k for k in members if value[k] is None or k in fields]
        if len(hidden) == 1:
            candidates = [k for k in members if k not in hidden]
            fields.add(candidates[0])
    return fields


def privacy_problems(value, path="$"):
    """Return failures without printing group labels, which may be private.

Zero-person cohorts may describe an empty exclusion category. They are accepted
only when every numeric statistic in that object is zero and its campaign count
is explicitly zero. A parent count never excuses a smaller nested subgroup.
"""
    problems = []
    if isinstance(value, dict):
        for key in sorted(conditional_suppressions(value)):
            problems.append(f"{path}: {key} has conditional support below the privacy floor or withheld support")
        if is_count_map(value):
            for index, (key, count) in enumerate(value.items()):
                if key != SUPPRESSION_KEY and 0 < count < FLOOR:
                    problems.append(f"{path}.bucket[{index}]: campaign count is below the five-campaign privacy floor")
        for key, count in value.items():
            if SAMPLE_KEY.fullmatch(key) and type(count) is int and 0 < count < FLOOR:
                problems.append(f"{path}: {key} is below the five-campaign privacy floor")
            if not COUNT_KEY.fullmatch(key) or isinstance(count, (dict, list)):
                continue
            if type(count) is not int or count < 0:
                problems.append(f"{path}: {key} must be a nonnegative integer")
            elif count < FLOOR and not (count == 0 and _empty_cohort(value)):
                problems.append(f"{path}: {key} is below the five-business privacy floor")
        for index, (key, child) in enumerate(value.items()):
            if key == "definitions" and isinstance(child, dict) and all(
                    isinstance(description, str) for description in child.values()):
                continue
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
    import json
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
        problems = committed_file_problems(path, content, mode)
        if mode != "120000" and path.startswith("analysis/output/") and path.endswith(".json"):
            try:
                problems.extend(privacy_problems(json.loads(content)))
            except json.JSONDecodeError:
                problems.append("invalid aggregate JSON")
        for problem in problems:
            print(f"{path}: {problem}")
            failures += 1
    if not failures:
        print("Tracked-file privacy gate passed")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(check_committed_files())
