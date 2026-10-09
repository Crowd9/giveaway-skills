#!/usr/bin/env python3
"""Check shared block rendering at Markdown file boundaries."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('render_shared', ROOT / 'scripts/render_shared.py')
renderer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(renderer)


class SharedBlockTests(unittest.TestCase):
    def test_closing_marker_at_eof(self):
        for ending in ('', '\n'):
            text = '<!-- generated:asking -->\nold\n<!-- /generated -->' + ending
            pattern = renderer.block_re('asking')
            self.assertIsNotNone(pattern.search(text))
            updated = pattern.sub(lambda m: m.group(1) + 'new\n' + m.group(2), text)
            self.assertEqual(updated, text.replace('old\n', 'new\n'))


if __name__ == '__main__':
    unittest.main()
