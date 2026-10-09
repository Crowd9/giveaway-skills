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
        self.assertEqual(privacy_problems({"campaigns": 5, "n": 5,
            "business_plus_share": 0.1, "repeat_organizer_share": 0.2,
            "campaigns_per_organizer_mean": 2.5}), [])

    def test_small_campaign_samples_fail_even_with_enough_businesses(self):
        for key in ("n", "campaigns", "clean_n"):
            self.assertTrue(privacy_problems({key: 4, "businesses": 5}))

    def test_holi_month_buckets_do_not_inherit_five_businesses(self):
        holi = {"smaller_themes": {"Holi": {"n": 5, "organizers": 5,
                "start_months": {"Mar": 4, "Dec": 1}}}}
        problems = privacy_problems(holi)
        self.assertEqual(len(problems), 2)
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
