#!/usr/bin/env python3
"""Exercise relative file links and heading anchors without repo mutations."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validate', ROOT / 'scripts/validate.py')
validate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate)


class LinkValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / 'skills/example'
        (self.skill / 'references').mkdir(parents=True)
        (self.skill / 'scripts').mkdir()
        (self.skill / 'evals').mkdir()
        (self.root / 'analysis/output').mkdir(parents=True)
        (self.skill / 'references/guide.md').write_text('# Hello, World!\n\n## Repeat\n## Repeat\n\nSetext\n------\n')
        (self.skill / 'scripts/run.py').write_text('')
        (self.skill / 'evals/cases.json').write_text('{}')
        (self.root / 'analysis/output/data.json').write_text('{}')
        self.document = self.skill / 'SKILL.md'

    def check(self, text, document=None):
        document = document or self.document
        document.write_text(text)
        return validate.check_links(document, self.root)

    def test_valid_paths_and_anchors(self):
        self.assertEqual(self.check('''# Local
[heading](#local) [guide](references/guide.md#hello-world)
[duplicate](references/guide.md#repeat-1) [setext](references/guide.md#setext)
`references/guide.md` `scripts/run.py --self-test` `evals/cases.json`
`analysis/output/data.json`
[reference][guide]
[guide]: references/guide.md#repeat "Title"
'''), [])

    def test_missing_paths_and_anchor(self):
        errors = self.check('''[missing](references/missing.md)
`references/absent.json` `scripts/absent.py` `evals/absent.json` `analysis/output/absent.json`
[anchor](references/guide.md#absent)
[reference][bad]
[bad]: references/no.md
''')
        self.assertEqual(len(errors), 8, errors)
        self.assertTrue(any('heading anchor missing' in error for error in errors))

    def test_reference_doc_uses_skill_paths_and_relative_links(self):
        self.assertEqual(self.check('`references/guide.md` [guide](guide.md#repeat)', self.skill / 'references/other.md'), [])

    def test_root_paths(self):
        self.assertEqual(self.check('[guide](skills/example/references/guide.md) `analysis/output/data.json`', self.root / 'README.md'), [])

    def test_external_and_examples(self):
        self.assertEqual(self.check('''[web](https://example.org/missing#anchor)
[mail](mailto:help) [network](//example.org/path)
`references/<name>.md` `analysis/output/...json`
Example:
```bash
python3 scripts/<name>.py [example](absent.md)
```
~~~markdown example
[example](absent.md) `references/missing.md`
~~~
'''), [])

    def test_multiline_links(self):
        self.assertEqual(self.check('[guide](\nreferences/guide.md#repeat\n)'), [])
        errors = self.check('[guide](\nreferences/missing.md\n)')
        self.assertEqual(len(errors), 1, errors)
        self.assertIn(':1:', errors[0])

    def test_multiline_reference_destinations(self):
        self.assertEqual(self.check('[guide]\n\n[guide]:\n  references/guide.md\n'), [])
        errors = self.check('[guide]\n\n[guide]:\n  references/missing.md\n')
        self.assertEqual(len(errors), 2, errors)

    def test_emphasis_heading_anchor(self):
        self.assertEqual(self.check('# Read _This_\n[heading](#read-this)'), [])
        self.assertIn('snake_case', validate.heading_anchors('# snake_case'))

    def test_real_commands_in_fences(self):
        self.assertEqual(self.check('```bash\npython3 scripts/run.py --self-test\n```'), [])
        self.assertEqual(len(self.check('```bash\npython3 scripts/missing.py\n```')), 1)
        self.assertEqual(self.check('```bash\npython3 scripts/<name>.py\n```'), [])

    def test_encoded_spaces_and_parentheses(self):
        (self.skill / 'references/a b(c).md').write_text('# A Heading\n')
        self.assertEqual(self.check('[one](references/a%20b(c).md#a-heading) [two](<references/a b(c).md#a-heading>)'), [])


if __name__ == '__main__':
    unittest.main()
