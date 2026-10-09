#!/usr/bin/env python3
"""review.py ships method-family medians as constants; keep them equal to benchmarks.json."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('review', ROOT / 'skills/giveaway-results-review/scripts/review.py')
review = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(review)
NAMES = {'visit': 'Visit a page or profile', 'follow': 'Follow or subscribe (free)', 'share': 'Share, repost or refer',
         'email': 'Email or newsletter signup', 'content': 'Post or create content'}


class ReviewConstantsTest(unittest.TestCase):
    def test_method_family_matches_source(self):
        with open(ROOT / 'analysis/output/benchmarks.json') as f:
            families = json.load(f)['ordinary_benchmark']['entry_methods']['families']
        self.assertEqual(set(review.METHOD_FAMILY), set(NAMES))
        for key, name in NAMES.items():
            src = families[name]
            self.assertEqual(review.METHOD_FAMILY[key], (src['uptake']['median'], src['uptake']['n'], src['campaigns']), key)


if __name__ == '__main__':
    unittest.main()
