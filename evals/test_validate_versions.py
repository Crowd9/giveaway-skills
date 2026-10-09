#!/usr/bin/env python3
"""Exercise release version mismatches without modifying the working tree."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class VersionValidationTests(unittest.TestCase):
    def test_version_mirrors(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ('skills', '.claude-plugin', 'analysis/output'):
                shutil.copytree(ROOT / name, root / name)
            (root / 'evals').mkdir()
            shutil.copy(ROOT / 'evals/check_deliverable.py', root / 'evals/check_deliverable.py')
            shutil.copy(ROOT / 'VERSIONS.md', root / 'VERSIONS.md')

            def validate():
                return subprocess.run(
                    [sys.executable, str(ROOT / 'scripts/validate.py')],
                    cwd=root, capture_output=True, text=True,
                )

            result = validate()
            self.assertEqual(result.returncode, 0, result.stdout)
            versions = root / 'VERSIONS.md'
            original = versions.read_text()
            lines = original.splitlines(keepends=True)
            row = next(i for i, line in enumerate(lines) if line.startswith('| giveaway-'))
            fields = lines[row].split('|')
            fields[2] = ' 999.0.0 '
            lines[row] = '|'.join(fields)
            versions.write_text(''.join(lines))
            result = validate()
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('metadata.version disagrees', result.stdout)
            versions.write_text(original)

            manifest = root / '.claude-plugin/marketplace.json'
            data = json.loads(manifest.read_text())
            data['metadata']['version'] = '999.0.0'
            manifest.write_text(json.dumps(data))
            result = validate()
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('repo version:', result.stdout)


if __name__ == '__main__':
    unittest.main()
