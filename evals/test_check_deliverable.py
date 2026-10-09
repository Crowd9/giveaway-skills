#!/usr/bin/env python3
"""Regression checks for eval status, negative checks and meaning-review handling."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from check_deliverable import assess, run, validate_cases

ROOT = Path(__file__).resolve().parents[1]


class DeliverableTests(unittest.TestCase):
    def test_empty_is_unassessed(self):
        self.assertEqual(assess({}, 'Anything')[0], 'UNASSESSED')

    def test_duplicate_ids(self):
        with self.assertRaisesRegex(ValueError, 'duplicate case ids'):
            validate_cases([{'id': 7}, {'id': '7'}])

    def test_negative_fixture(self):
        cases = json.loads((ROOT / 'skills/giveaway-random-draw/evals/evals.json').read_text())['evals']
        case = next(c for c in cases if c['id'] == 7)
        answer = (ROOT / 'evals/fixtures/fails_draw_correction.txt').read_text()
        self.assertEqual(run(case['checks'][:3], answer), [])
        status, misses, pending = assess(case, answer)
        self.assertEqual(status, 'FAIL')
        self.assertEqual(len(misses), 2)
        safe = 'Do not remove --weight-column. Do not reuse the known seed. Run draw.py commit and invalidate the old record.'
        self.assertEqual(run(case['checks'], safe), [])
        self.assertEqual(assess(case, safe)[0], 'UNASSESSED')
        # Each unsafe instruction alone must fail independently.
        for bad in ('Remove --weight-column.', 'Reuse the known seed.'):
            self.assertEqual(assess(case, safe + '\n' + bad)[0], 'FAIL')

    def test_meaning_reviews_are_explicit(self):
        case = {'review_checks': [{'id': 'meaning'}]}
        self.assertEqual(assess(case, 'answer')[0], 'UNASSESSED')
        self.assertEqual(assess(case, 'answer', {'meaning': {'passed': True, 'reason': 'Specific next action given'}})[0], 'PASS')
        self.assertEqual(assess(case, 'answer', {'meaning': {'passed': False, 'reason': 'Only generic advice'}})[0], 'FAIL')
        with self.assertRaises(ValueError):
            assess(case, 'answer', {'meaning': {'passed': 'false', 'reason': 'bad type'}})
        with self.assertRaises(ValueError):
            assess(case, 'answer', {'other': {'passed': True, 'reason': 'wrong id'}})

    def test_cli_unassessed_and_duplicate(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            answer = directory / 'answer.txt'
            answer.write_text('answer')
            cases = directory / 'evals.json'
            cases.write_text(json.dumps({'evals': [{'id': 1}]}))
            command = [sys.executable, str(ROOT / 'evals/check_deliverable.py'), str(cases), '1', str(answer)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn('UNASSESSED', result.stdout)
            cases.write_text(json.dumps({'evals': [{'id': 1}, {'id': '1'}]}))
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn('duplicate case ids', result.stdout)

    def test_all_case_schemas(self):
        for path in ROOT.glob('skills/*/evals/evals.json'):
            validate_cases(json.loads(path.read_text())['evals'])


if __name__ == '__main__':
    unittest.main()
