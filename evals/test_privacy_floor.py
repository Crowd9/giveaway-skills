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
                    "n_organizers", "organizer_count"):
            self.assertTrue(privacy_problems({key: 4}), key)

    def test_campaign_volume_cannot_clear_business_floor(self):
        self.assertTrue(privacy_problems({"campaigns": 10000, "businesses": 1}))

    def test_ratios_and_campaign_counts_are_not_business_counts(self):
        self.assertEqual(privacy_problems({"campaigns": 1, "n": 1,
            "business_plus_share": 0.1, "repeat_organizer_share": 0.2,
            "campaigns_per_organizer_mean": 2.5}), [])

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


if __name__ == "__main__":
    unittest.main()
