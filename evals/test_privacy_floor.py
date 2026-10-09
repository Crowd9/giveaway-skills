"""Synthetic regression cases for the published aggregate privacy gate."""
import importlib.util
from pathlib import Path
import unittest


SPEC = importlib.util.spec_from_file_location(
    "privacy_floor", Path(__file__).resolve().parents[1] / "scripts/privacy_floor.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
privacy_problems = MODULE.privacy_problems


class PrivacyFloorTests(unittest.TestCase):
    def test_nested_dict_and_list_groups_do_not_inherit_parent_count(self):
        aggregate = {"businesses": 100, "values": [{"businesses": 4},
                     {"nested": {"organizers": 1}}]}
        self.assertEqual(len(privacy_problems(aggregate)), 2)

    def test_five_is_allowed_and_all_positive_counts_below_it_fail(self):
        for count in range(1, 5):
            self.assertTrue(privacy_problems({"businesses": count}))
        self.assertEqual(privacy_problems({"businesses": 5}), [])

    def test_aliases_and_comparison_subgroups(self):
        for key in ("unique_organizers", "unique_organizers_sites", "organisers",
                    "distinct_businesses", "organizers_offered", "organizers_top",
                    "organizers_rest", "organizers_with", "organizers_reached",
                    "organizers_top_stratified", "ordinary_organizers",
                    "n_businesses", "business_count", "distinct_business_count",
                    "n_organizers", "organizer_count", "sites"):
            self.assertTrue(privacy_problems({key: 4}), key)

    def test_campaign_volume_cannot_clear_business_floor(self):
        self.assertTrue(privacy_problems({"campaigns": 10000, "businesses": 1}))

    def test_ratios_are_not_business_counts(self):
        self.assertEqual(privacy_problems({"campaigns": 100, "n": 100,
            "business_plus_share": 0.1, "repeat_organizer_share": 0.2,
            "campaigns_per_organizer_mean": 2.5}), [])

    def test_single_campaign_email_conditional_is_withheld(self):
        row = {"n": 960, "sites": 13, "email_offered": 0.001, "email_uptake": 0.422}
        self.assertEqual(MODULE.conditional_suppressions(row), {"email_offered", "email_uptake"})
        self.assertTrue(privacy_problems(row))

    def test_tiny_cross_filters_and_small_complements(self):
        for row, fields in (
            ({"n": 517, "sites": 20, "judged_selection_share": 0.002}, {"judged_selection_share"}),
            ({"n": 47, "sites": 22, "business_plus_share": 0.021}, {"business_plus_share"}),
            ({"n": 100, "mandatory_share": 0.99, "completions_when_optional": 0.4},
             {"mandatory_share", "completions_when_optional"}),
        ):
            self.assertEqual(MODULE.conditional_suppressions(row), fields)

    def test_explicit_conditional_counts_and_exact_floor(self):
        self.assertIn("email_uptake", MODULE.conditional_suppressions(
            {"n": 100, "email_n": 4, "email_offered": 0.1, "email_uptake": 0.8}))
        self.assertEqual(MODULE.conditional_suppressions(
            {"n": 100, "email_n": 5, "email_offered": 0.049, "email_uptake": 0.8}), set())
        self.assertIn("uptake", MODULE.conditional_suppressions({"n_offered": 4, "uptake": 0.8}))
        self.assertIn("conditional_email_given_share", MODULE.conditional_suppressions(
            {"n_share": 4, "n_both": 4, "conditional_email_given_share": 0.8}))

    def test_null_shares_and_markers_cannot_license_restored_metrics(self):
        for row, field in (
            ({"n": 960, "email_offered": None, "email_uptake": 0.422}, "email_uptake"),
            ({"n": 100, "mandatory_share": None, "completions_when_optional": 0.4}, "completions_when_optional"),
        ):
            row["suppressed_below_floor"] = [field]
            self.assertIn(field, MODULE.conditional_suppressions(row))
            row[field] = None
            self.assertEqual(privacy_problems(row), [])

    def test_partition_and_overlapping_sum_cannot_reconstruct_hidden_share(self):
        row = {"n": 2053, "sites": 289, "free_share": 0.5, "pro_share": 0.3315,
               "business_share": 0.1666, "premium_share": None, "business_plus_share": 0.1685}
        self.assertIn("business_share", MODULE.conditional_suppressions(row))
        row["business_share"] = None
        self.assertEqual(MODULE.conditional_suppressions(row), set())
        self.assertIn("optin_on_share", MODULE.conditional_suppressions(
            {"n": 245, "optin_on_or_auto_share": 0.1714, "optin_on_share": 0.1592,
             "optin_auto_share": None}))
        self.assertTrue(MODULE.conditional_suppressions(
            {"n": 100, "template_share": 0.6, "own_copy_share": 0.39, "blank_share": None}))

    def test_nested_conditional_proportions_check_their_own_support(self):
        row = {"n": 5299, "question_share": 0.0902,
               "validated_given_question": 0.0021, "word_cap_changed_given_question": 0.0021}
        self.assertEqual(MODULE.conditional_suppressions(row),
                         {"validated_given_question", "word_cap_changed_given_question"})
        self.assertIn("validated_given_question", MODULE.conditional_suppressions(
            {"n": 1000, "question_share": 0.5, "validated_given_question": 0.996}))
        self.assertIn("conditional_email_given_share", MODULE.conditional_suppressions(
            {"n_share": 100, "n_both": 99, "conditional_email_given_share": 0.99}))

    def test_zero_support_cannot_publish_a_conditional_metric(self):
        self.assertIn("email_uptake", MODULE.conditional_suppressions(
            {"n": 100, "email_offered": 0.0, "email_uptake": 0.8}))

    def test_share_populations_and_unrelated_actions_are_not_conflated(self):
        for key in ("direct_share", "directory_impression_share", "baseline_share", "share_of_campaigns", "action_uptake"):
            self.assertEqual(privacy_problems({"n": 10, key: 0.01}), [])
        self.assertEqual(MODULE.conditional_suppressions(
            {"n": 65, "email_offered": 0.015, "action_uptake": 0.403}), {"email_offered"})

    def test_small_campaign_samples_fail_even_with_enough_businesses(self):
        for key in ("n", "campaigns", "clean_n", "n_offered", "n_both"):
            self.assertTrue(privacy_problems({key: 4, "businesses": 5}))

    def test_holi_month_buckets_do_not_inherit_five_businesses(self):
        holi = {"smaller_themes": {"Holi": {"n": 5, "organizers": 5,
                "start_months": {"Mar": 4, "Dec": 1}}}}
        problems = privacy_problems(holi)
        self.assertEqual(len(problems), 4)
        self.assertNotIn("Dec", " ".join(problems))
        self.assertNotIn("Holi", " ".join(problems))

    def test_count_maps_cover_arbitrary_bucket_labels(self):
        for dimension, label in (("weekday", "Mon"), ("country", "US"),
                ("niche", "art"), ("value_band", "100-250")):
            for count in range(1, 5):
                self.assertTrue(privacy_problems({dimension: {label: count}}))
            self.assertEqual(privacy_problems({dimension: {label: 5}}), [])

    def test_suppression_metadata_and_summary_statistics_are_not_buckets(self):
        for value in ({"Sep": 9, "suppressed_below_floor": 1},
                      {"suppressed_below_floor": 2},
                      {"n": 20, "min": 1, "p25": 2, "median": 3, "max": 4},
                      {"p25": 1, "p50": 2, "p75": 3}):
            self.assertEqual(privacy_problems(value), [])

    def test_sites_container_is_traversed_instead_of_treated_as_count(self):
        self.assertEqual(privacy_problems({"sites": {"large": {"n": 8}}}), [])
        self.assertTrue(privacy_problems({"sites": {"small": {"n": 4}}}))

    def test_prose_definitions_are_not_counts_but_numeric_groups_still_are(self):
        self.assertEqual(privacy_problems({"definitions": {"sites": "Distinct businesses"}}), [])
        self.assertTrue(privacy_problems({"definitions": {"sites": 4}}))

    def test_invalid_count_types_fail(self):
        for count in (None, True, "5", 5.0, -1):
            self.assertTrue(privacy_problems({"businesses": count}))

    def test_only_demonstrably_empty_zero_cohorts_are_allowed(self):
        self.assertEqual(privacy_problems({"campaigns": 0, "unique_organizers": 0,
            "stats": {"n": 0}, "years": {}, "share": None}), [])
        for group in ({"businesses": 0}, {"campaigns": 1, "businesses": 0},
                      {"campaigns": 0, "businesses": 0, "median": 1}):
            self.assertTrue(privacy_problems(group))

    def test_diagnostic_does_not_republish_group_label(self):
        problems = privacy_problems({"sensitive label": {"businesses": 1}})
        self.assertEqual(len(problems), 1)
        self.assertNotIn("sensitive label", problems[0])


class ResidualPrivacyTests(unittest.TestCase):
    def test_launchpad_parent_and_industry_subset_regression(self):
        data = {"by_niche": {"cryptocurrency launchpad": {"n": 244, "sites": 18}},
                "niche_by_industry": {"finance_crypto": {
                    "cryptocurrency launchpad": {"n": 243, "sites": 17, "email_offered": 0.041}}}}
        self.assertTrue(privacy_problems(data))
        subset = data["niche_by_industry"]["finance_crypto"]
        subset["cryptocurrency launchpad"] = None
        subset["suppressed_below_floor"] = ["cryptocurrency launchpad"]
        self.assertEqual(privacy_problems(data), [])

    def test_residual_sum_checks_even_when_no_single_child_is_close(self):
        data = {"by_niche": {"a": {"n": 100, "sites": 20}},
                "niche_by_industry": {"i": {"a": {"n": 51, "sites": 10}},
                                      "j": {"a": {"n": 47, "sites": 10}}}}
        self.assertTrue(MODULE.residual_suppressions(data))
        data["niche_by_industry"]["j"]["a"] = None
        self.assertEqual(MODULE.residual_suppressions(data), [])

    def test_business_counts_are_not_added_across_campaign_bands(self):
        data = {"yield_by_asset": {"email": {"campaigns": 100, "organizers": 20}},
                "yield_by_asset_and_band": {
                    "email|small": {"campaigns": 50, "organizers": 10},
                    "email|large": {"campaigns": 50, "organizers": 9}}}
        self.assertEqual(MODULE.residual_suppressions(data), [])

    def test_action_support_is_not_subtracted_from_campaign_support(self):
        data = {"yield_by_asset_and_band": {"email|small": {"campaigns": 100, "organizers": 20}},
                "yield_by_asset_and_mandatory": {
                    "email|optional|small": {"campaigns": 99, "organizers": 10}}}
        self.assertEqual(MODULE.residual_suppressions(data), [])
        data["yield_by_asset_and_mandatory"]["email|optional|small"]["organizers"] = 19
        self.assertTrue(MODULE.residual_suppressions(data))

    def test_zero_and_five_residuals_are_allowed(self):
        for n, businesses in ((100, 20), (95, 15)):
            data = {"by_country": {"a": {"n": 100, "sites": 20}},
                    "by_country_1k_plus": {"a": {"n": n, "sites": businesses}}}
            self.assertEqual(MODULE.residual_suppressions(data), [])

    def test_small_missing_month_is_not_recoverable_from_total(self):
        data = {"n": 20, "start_months": {"Jan": 19, "suppressed_below_floor": 1}}
        self.assertTrue(privacy_problems(data))
        data["start_months"]["Jan"] = None
        self.assertEqual(privacy_problems(data), [])

    def test_cross_file_country_indicator_and_duplicate_industry_totals(self):
        corpus = {"country_cuts.json": {"by_country": {"a": {"n": 100, "sites": 20}}},
                  "indicators.json": {"duration_by_country": {"rows": {"a": {"n": 99, "sites": 20}}}},
                  "prize_timing_cuts.json": {"by_industry_ordinary": {"food_drink": {"n": 100, "sites": 20}}},
                  "roi_benchmarks.json": {"by_vertical": {"food_drink": {"n": 99, "organizers": 19}}}}
        self.assertEqual(len(MODULE.corpus_residual_suppressions(corpus)), 2)

    def test_unrelated_equal_labels_do_not_imply_same_population(self):
        data = {"unrelated": {"a": {"n": 100, "sites": 20}},
                "another": {"a": {"n": 99, "sites": 19}}}
        self.assertEqual(MODULE.residual_suppressions(data), [])

    def test_percentile_metrics_and_installed_copy_keep_suppression(self):
        data = {"contestants": {"n": 100, "p": [10]},
                "duration_days": {"n": 98, "p": [5]}}
        self.assertTrue(MODULE.residual_suppressions(data))
        data["duration_days"] = None
        self.assertEqual(MODULE.residual_suppressions(data), [])
        root = Path(__file__).resolve().parents[1]
        import json
        source = json.loads((root / "analysis/output/percentiles.json").read_text())
        bundled = json.loads((root / "skills/giveaway-results-review/references/percentiles.json").read_text())
        self.assertEqual(source, bundled)
        self.assertIsNone(bundled["groups"]["vertical:food_drink"]["contestants"])

    def test_definitions_and_null_cells_do_not_crash_residual_registry(self):
        self.assertEqual(privacy_problems({"definitions": {
            "channel_size_within_industry": "Meaning of the metric"}}), [])
        data = {"by_niche": {"a": None}, "niche_by_industry": {"i": {"a": None}}}
        self.assertEqual(privacy_problems(data), [])


class CommittedFilePrivacyTests(unittest.TestCase):
    def check_file(self, path, content="", mode="100644"):
        return MODULE.committed_file_problems(path, content, mode)

    def test_csv_is_allowed_only_at_reviewed_example_paths(self):
        for path in MODULE.CSV_PATHS:
            self.assertEqual(self.check_file(path), [])
        for path in ("analysis/export.csv", "examples/data.csv",
                     "skills/giveaway-random-draw/examples/new.csv"):
            self.assertTrue(self.check_file(path))

    def test_reserved_email_domains_are_scoped_to_fixture_paths(self):
        address = "synthetic" + "@" + "example.com"
        for path in MODULE.EMAIL_FIXTURE_PATHS:
            self.assertEqual(self.check_file(path, address), [])
        for path in ("README.md", "analysis/output/aggregate.json",
                     "skills/giveaway-random-draw/references/drawing.md"):
            self.assertTrue(self.check_file(path, address))

    def test_non_reserved_domains_require_existing_values_and_paths(self):
        for path, addresses in MODULE.EXTRA_EMAILS.items():
            for address in addresses:
                self.assertEqual(self.check_file(path, address), [])
                self.assertTrue(self.check_file("README.md", address))
        for domain in ("x.com", "mailinator.com", "gleam.io", "anthropic.com"):
            address = "unreviewed" + "@" + domain
            for path in MODULE.EMAIL_FIXTURE_PATHS:
                self.assertTrue(self.check_file(path, address))

    def test_escaped_newline_does_not_change_fixture_email(self):
        path = "skills/giveaway-random-draw/scripts/draw.py"
        address = "a" + "@" + "x.com"
        self.assertEqual(self.check_file(path, r"\n" + address), [])

    def test_all_ipv4_addresses_fail_even_in_fixtures(self):
        for octets in ((1, 2, 3, 4), (0, 0, 0, 0), (127, 0, 0, 1),
                       (192, 0, 2, 1)):
            address = ".".join(map(str, octets))
            for path in ("README.md", *MODULE.EMAIL_FIXTURE_PATHS):
                problems = self.check_file(path, address)
                self.assertTrue(problems)
                self.assertNotIn(address, " ".join(problems))

    def test_symlinks_and_unexpected_types_fail(self):
        self.assertTrue(self.check_file("README.md", mode="120000"))
        self.assertTrue(self.check_file("data.parquet"))
        self.assertEqual(self.check_file("LICENSE"), [])
        self.assertEqual(self.check_file(".gitignore"), [])

    def test_diagnostics_do_not_republish_email_values(self):
        address = "unreviewed" + "@" + "example.org"
        problems = self.check_file("README.md", address)
        self.assertTrue(problems)
        self.assertNotIn(address, " ".join(problems))


if __name__ == "__main__":
    unittest.main()
