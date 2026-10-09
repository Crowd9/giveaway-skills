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
    return bool(counts) and all(type(count) is int or count is None for count in counts.values()) and not any(
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


# Parent/child conventions are explicit: naming similarity alone cannot establish
# equal populations. Each tuple names a parent table, a crossed table, and the
# component holding the parent label. Nested keys or |/: compound keys encode
# the two dimensions. A final bool declares disjoint CAMPAIGN cells for sums.
# Businesses can recur across campaign bands: their counts are NEVER summed.
CROSSED_TABLES = (
    ("by_niche", "niche_by_industry", 1, True),
    ("by_industry", "niche_by_industry", 0, True),
    ("by_industry", "by_industry_and_scale", 0, True),
    ("by_org_scale", "by_industry_and_scale", 1, True),
    ("by_industry", "employee_band_by_industry", 0, True),
    ("by_employee_band", "employee_band_by_industry", 1, True),
    ("by_youtube_subscribers", "youtube_subscribers_vs_views_per_video", 0, True),
    ("by_youtube_subscribers", "youtube_subscribers_vs_channel_age", 0, True),
    ("by_country", "industry_mix_by_country", 0, True),
    ("by_country", "selection_method_by_country", 0, True),
    ("by_country", "language_by_country", 0, True),
    ("by_country", "governing_law_by_country", 0, True),
    ("by_country", "skill_against_other", 0, True),
    ("by_template", "template_by_industry", 1, True),
    ("by_template", "template_by_country", 1, True),
    ("by_template", "industry_mix_by_template", 0, True),
    ("source_mix", "source_mix_by_band", 0, True),
    ("source_mix", "source_mix_first_campaign", 0, True),
    ("source_mix", "source_kind_by_industry", 1, True),
    ("source_mix", "template_by_organizer_tenure", 1, True),
    ("by_prize_category", "prize_category_by_industry", 1, True),
    ("by_industry_ordinary", "prize_category_by_industry", 0, True),
    ("by_launch_wording", "launch_wording_by_industry", 0, True),
    ("by_industry_ordinary", "launch_wording_by_industry", 1, True),
    ("by_start_month", "by_start_month_and_industry", 1, True),
    ("by_industry_ordinary", "by_start_month_and_industry", 0, True),
    ("value_curve", "value_curve_by_industry", 1, True),
    ("value_curve", "value_curve_by_tier", 1, True),
    ("value_curve", "bundles_by_value_band", 0, True),
    ("bundles", "bundles_by_value_band", 1, True),
    ("own_product", "own_product_by_industry", 1, True),
    ("own_product", "own_product_by_size_band", 1, True),
    ("audience_fit", "audience_fit_by_industry", 1, True),
    ("collaboration", "collaboration_by_industry", 1, True),
    ("outcomes_when_channel_over_10pct", "channel_quality_by_size_band", 0, True),
    ("channel_quantity_vs_quality", "channel_quality_by_size_band", 0, True),
    ("sequence_curve_all", "sequence_curve_by_first_band", 1, True),
    ("within_organizer_transition_by_seq", "within_organizer_transition_by_band_and_seq", 1, True),
    ("within_organizer_transition_by_band", "within_organizer_transition_by_band_and_seq", 0, True),
    ("within_organizer_transition_by_seq", "transition_by_gap_length_and_seq", 1, True),
)
FILTERED_TABLES = (
    ("by_industry", "by_industry_excluding_crypto"),
    ("by_industry", "stores_by_industry"),
    ("by_country", "by_country_1k_plus"),
    ("by_country", "terms_by_country"),
    ("by_band_all", "by_band"),
    ("by_template", "by_template_1k"),
    ("source_mix", "source_mix_1k"),
    ("region_all", "region_clean"),
    ("title_term_all", "title_term_clean"),
    ("overlap_all", "overlap_clean"),
    ("nth_campaign_all", "nth_campaign_clean"),
    ("industry_all", "industry_clean"),
    ("vertical_all", "vertical_clean"),
    ("recency_all", "recency_clean"),
)


def cohort_counts(row):
    """Canonical row support, excluding conditional counts and action counts."""
    if type(row) is int:
        return {"campaigns": row}
    if not isinstance(row, dict):
        return {}
    result = {}
    for kind, keys in (("campaigns", ("n", "campaigns")),
                       ("businesses", ("sites", "organizers", "businesses", "unique_organizers"))):
        for key in keys:
            if type(row.get(key)) is int:
                result[kind] = row[key]
                break
    return result


def crossed_rows(table):
    """Yield dimensions, mutable container and key for a two-axis table."""
    if not isinstance(table, dict):
        return
    for key, row in table.items():
        if key == SUPPRESSION_KEY:
            continue
        if "|" in key or ":" in key:
            yield re.split(r"[|:]", key), table, key
        elif isinstance(row, dict):
            for inner in row:
                if inner != SUPPRESSION_KEY:
                    yield [key, inner], row, inner


def residual_groups(value):
    """Known same-population relationships; yield parent and child locations.

    Sums use only declared disjoint campaign partitions, even when the published
    list omits cells. Positive residuals 1..4 are unsafe. A zero difference is an
    identical cohort, not a hidden person. Business differences are a conservative
    disclosure warning, NOT the distinct-business count of residual campaigns.
    General intersections, suppressed counts, rounded-share linear systems and
    cross-file populations without a documented common cohort need private
    membership-aware disclosure review. Passing this check is not that review.
    """
    rules = list(CROSSED_TABLES)
    for name in value:
        if name.startswith("yield_by_asset_and_"):
            rules.append(("yield_by_asset", name, 0,
                          name in {"yield_by_asset_and_band", "yield_by_asset_and_vertical", "yield_by_asset_and_industry"}))
    for parent_name, child_name, axis, partition in rules:
        parents = value.get(parent_name, {})
        if not isinstance(parents, dict):
            continue
        grouped = {}
        for dimensions, container, key in crossed_rows(value.get(child_name)):
            if len(dimensions) > axis:
                grouped.setdefault(dimensions[axis].strip(), []).append((container, key))
        for label, children in grouped.items():
            if label in parents:
                parent = parents[label]
                if child_name in {"yield_by_asset_and_mandatory", "yield_by_asset_and_position", "yield_by_asset_and_worth_tier"}:
                    parent = {key: val for key, val in parent.items() if key not in {"n", "campaigns"}} if isinstance(parent, dict) else parent
                yield parent, children, partition
    # Asset refinements hold asset|setting|band, whose parent is asset|band.
    parents = value.get("yield_by_asset_and_band", {})
    for name, table in value.items():
        if not name.startswith("yield_by_asset_and_") or not isinstance(table, dict):
            continue
        grouped = {}
        for key in table:
            dimensions = key.split("|")
            if len(dimensions) == 3:
                grouped.setdefault(dimensions[0] + "|" + dimensions[2], []).append((table, key))
        for label, children in grouped.items():
            if label in parents:
                # Mandatory/position refer to Actions: campaigns can recur.
                partition = name.rsplit("_", 1)[-1] in {"duration", "sharing", "structure", "count"}
                parent = parents[label]
                if name in {"yield_by_asset_and_mandatory", "yield_by_asset_and_position", "yield_by_asset_and_worth_tier"}:
                    parent = {key: val for key, val in parent.items() if key not in {"n", "campaigns"}} if isinstance(parent, dict) else parent
                yield parent, children, partition
    for parent_name, child_name in FILTERED_TABLES:
        parents, children = value.get(parent_name, {}), value.get(child_name, {})
        if isinstance(parents, dict) and isinstance(children, dict):
            for label in parents.keys() & children.keys() - {SUPPRESSION_KEY}:
                yield parents[label], [(children, label)], False
    # Channel-size crossings add industry or contestant-band to the channel band.
    for channel, parent_name in (("youtube", "by_youtube_subscribers"),
                                 ("discord", "by_discord_server_size"),
                                 ("telegram", "by_telegram_size")):
        parents = value.get(parent_name, {})
        for name in ("channel_size_within_industry", "channel_size_within_contestant_band"):
            grouped = {}
            channels = value.get(name, {})
            if not isinstance(channels, dict):
                continue
            for dims, container, key in crossed_rows(channels.get(channel)):
                grouped.setdefault(dims[-1], []).append((container, key))
            for label, children in grouped.items():
                if label in parents:
                    yield parents[label], children, True


    # The top-combinations wrapper carries a band/industry total of its own.
    for name in ("top_combinations_by_size_band", "top_combinations_by_industry"):
        grouped = {}
        for group in value.get(name, {}).values():
            if not isinstance(group, dict):
                continue
            cells = group.get("top_combinations", {})
            children = [(cells, key) for key in cells if key != SUPPRESSION_KEY]
            yield group, children, True
            for container, key in children:
                grouped.setdefault(key, []).append((container, key))
        for label, children in grouped.items():
            if label in value.get("top_combinations", {}):
                yield value["top_combinations"][label], children, True
    # Per-metric percentile support is a subset of that group's Entrant support.
    if isinstance(value.get("contestants"), dict) and "p" in value["contestants"]:
        for metric, row in value.items():
            if metric != "contestants" and isinstance(row, dict) and "p" in row:
                yield value["contestants"], [(value, metric)], False
    # Count maps embedded in a cohort are disjoint time/tier categories.
    for key in ("start_months", "start_years", "tier", "prize_count_distribution"):
        table = value.get(key)
        if isinstance(table, dict) and is_count_map(table):
            yield value, [(table, label) for label in table if label != SUPPRESSION_KEY], True


def corpus_residual_groups(corpus):
    """Cross-file cohorts verified against the generators, not fuzzy labels.

    country_cuts and indicators share the 100+ plausible-date base. Indicator
    filters only narrow it. Ordinary industry cuts share frame.py's exclusions;
    positive-entry and positive-impression filters narrow prize_timing totals.
    Industry enrichment tables are NOT interchangeable with these: they exclude
    aggregate hosts and use different dates/labels. Matching counts prove nothing.
    """
    country = corpus.get("country_cuts.json", {}).get("by_country", {})
    indicators = corpus.get("indicators.json", {})
    for name, indicator in indicators.items():
        if "by_country" not in name or name == "industry_mix_by_country":
            continue
        rows = indicator.get("rows", {})
        for label in country.keys() & rows.keys() - {SUPPRESSION_KEY}:
            yield country[label], [(rows, label)], False
    # Indicator industry cells partition the same country base.
    for label, rows in indicators.get("industry_mix_by_country", {}).get("rows", {}).items():
        if label in country and isinstance(rows, dict):
            yield country[label], [(rows, key) for key in rows if key != SUPPRESSION_KEY], True
    ordinary = corpus.get("prize_timing_cuts.json", {}).get("by_industry_ordinary", {})
    for filename, table_name in (
        ("roi_benchmarks.json", "by_industry"),
        ("roi_benchmarks.json", "by_vertical"),
        ("standouts.json", "industries"),
        ("comparisons.json", "vertical_all"),
        ("comparisons.json", "vertical_clean"),
        ("context_checks.json", "method_prevalence_top_vs_bottom_by_vertical"),
        ("standouts.json", "industries_by_label"),
        ("comparisons.json", "industry_all"),
        ("comparisons.json", "industry_clean"),
        ("vertical_profiles.json", "by_industry"),
        ("email_traffic.json", "email_share_by_industry"),
    ):
        rows = corpus.get(filename, {}).get(table_name, {})
        for label in ordinary.keys() & rows.keys() - {SUPPRESSION_KEY}:
            yield ordinary[label], [(rows, label)], False
    for name, metrics in corpus.get("percentiles.json", {}).get("groups", {}).items():
        kind, _, label = name.partition(":")
        if kind in {"industry", "vertical"} and label in ordinary and isinstance(metrics, dict):
            for metric in metrics:
                if metric != SUPPRESSION_KEY:
                    yield ordinary[label], [(metrics, metric)], False
    tiers = corpus.get("field_cuts.json", {}).get("by_tier", {})
    rows = corpus.get("email_traffic.json", {}).get("email_share_by_plan_tier", {})
    for label in tiers.keys() & rows.keys() - {SUPPRESSION_KEY}:
        yield tiers[label], [(rows, label)], False
    # Templates includes all ordinary starts; ROI additionally needs entries > 0.
    years = corpus.get("templates.json", {}).get("template_share_by_year", {})
    rows = corpus.get("roi_benchmarks.json", {}).get("by_start_year", {})
    for label in years.keys() & rows.keys() - {SUPPRESSION_KEY}:
        yield years[label], [(rows, label)], False


def corpus_residual_suppressions(corpus):
    return _residual_suppressions(corpus_residual_groups(corpus))


def residual_suppressions(value):
    """Return child locations to withhold in documented parent/subset tables."""
    return _residual_suppressions(residual_groups(value))


def _residual_suppressions(groups):
    result = []
    for parent, children, partition in groups:
        total = cohort_counts(parent)
        visible = [(container, key, cohort_counts(container[key])) for container, key in children
                   if cohort_counts(container[key])]
        for container, key, counts in visible:
            if any(0 < total[kind] - counts[kind] < FLOOR for kind in total.keys() & counts.keys()):
                result.append((container, key))
        if partition and "campaigns" in total and visible:
            remainder = total["campaigns"] - sum(counts.get("campaigns", 0) for _, _, counts in visible)
            if 0 < remainder < FLOOR:
                # Withhold another whole cell, including all its derived metrics.
                container, key, _ = min(visible, key=lambda item: item[2].get("campaigns", float("inf")))
                result.append((container, key))
    return result


def privacy_problems(value, path="$"):
    """Return failures without printing group labels, which may be private.

Zero-person cohorts may describe an empty exclusion category. They are accepted
only when every numeric statistic in that object is zero and its campaign count
is explicitly zero. A parent count never excuses a smaller nested subgroup.
"""
    problems = []
    if isinstance(value, dict):
        for index, _ in enumerate(residual_suppressions(value)):
            problems.append(f"{path}.residual[{index}]: parent minus published subset is below the privacy floor")
        for key in sorted(conditional_suppressions(value)):
            problems.append(f"{path}: {key} has conditional support below the privacy floor or withheld support")
        if is_count_map(value):
            for index, (key, count) in enumerate(value.items()):
                if key != SUPPRESSION_KEY and type(count) is int and 0 < count < FLOOR:
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
    corpus = {}
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
                aggregate = json.loads(content)
                corpus[Path(path).name] = aggregate
                problems.extend(privacy_problems(aggregate))
            except json.JSONDecodeError:
                problems.append("invalid aggregate JSON")
        for problem in problems:
            print(f"{path}: {problem}")
            failures += 1
    for index, _ in enumerate(corpus_residual_suppressions(corpus)):
        print(f"Cross-file residual[{index}]: parent minus published subset is below the privacy floor")
        failures += 1
    if not failures:
        print("Tracked-file privacy gate passed")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(check_committed_files())
