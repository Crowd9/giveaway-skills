#!/usr/bin/env python3
"""Exercise each installed skill without repository files or sibling skills."""
import importlib.util
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('validate', ROOT / 'scripts/validate.py')
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


def missing_reads(skill):
    """Check packaged paths, allowing explicitly documented source provenance only."""
    document = skill / 'SKILL.md'
    text = document.read_text()
    missing = []
    targets = list(validator.link_targets(text))
    # Read instructions can name files outside the usual packaged directories.
    # Only explicit user inputs and optional project context are external reads.
    for line, context in enumerate(validator.visible_markdown(text).splitlines(), 1):
        if not re.search(r'\b(?:read|load|open)\b', context, re.I):
            continue
        for target in re.findall(r'`([^`\s]+\.[a-zA-Z0-9]+)`', context):
            optional_context = (
                target in {'.agents/product-marketing.md', '.claude/product-marketing.md'}
                and re.search(r'\bif\b.*\bexists\b', context, re.I)
            )
            user_input = re.search(
                r"\b(?:user[- ](?:supplied|provided)|(?:supplied|provided|attached) by the user)\b",
                context, re.I,
            )
            if not optional_context and not user_input:
                # A bare script name may refer back to its declared packaged path.
                declared = {path for _, path, _ in targets
                            if '/' not in target and Path(path).name == target
                            and (skill / path).is_file()}
                if len(declared) == 1:
                    target = declared.pop()
                targets.append((line, target, True))
    for line, target, _ in dict.fromkeys(targets):
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        path = unquote(parsed.path)
        # Repository aggregates are citations, not an instruction to load a file.
        # A read/load instruction still requires the data to be shipped.
        if path.startswith('analysis/output/'):
            context = text.splitlines()[line - 1]
            if not re.search(r'\b(?:read|load|open)\b', context, re.I):
                continue
        resolved = (skill / path).resolve() if path else document.resolve()
        if not resolved.is_relative_to(skill.resolve()) or not resolved.is_file():
            missing.append(f'{line}: {target}')
    return missing


class StandaloneInstallTests(unittest.TestCase):
    def test_each_skill_installs_alone(self):
        skills = sorted((ROOT / 'skills').glob('*/SKILL.md'))
        self.assertTrue(skills, 'no skills discovered')
        for source in skills:
            with self.subTest(skill=source.parent.name), tempfile.TemporaryDirectory() as temp:
                installed = Path(temp) / source.parent.name
                shutil.copytree(source.parent, installed, ignore=shutil.ignore_patterns('__pycache__'))
                self.assertEqual(missing_reads(installed), [], source.parent.name)
                scripts = sorted((installed / 'scripts').rglob('*.py'))
                self.assertTrue(scripts, f'{source.parent.name}: no scripts discovered')
                env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1',
                           PYTHONWARNINGS='error::ResourceWarning', TMPDIR=temp)
                # Remove caller-controlled import paths that could hide missing files.
                env.pop('PYTHONPATH', None)
                for script in scripts:
                    with self.subTest(script=str(script.relative_to(installed))):
                        result = subprocess.run(
                            [sys.executable, '-W', 'error::ResourceWarning', str(script), '--self-test'],
                            cwd=installed, env=env, capture_output=True, text=True, timeout=120,
                        )
                        output = result.stdout + result.stderr
                        self.assertEqual(result.returncode, 0, output)
                        self.assertNotIn('ResourceWarning', result.stderr, output)

    def test_missing_read_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            skill = Path(temp)
            (skill / 'SKILL.md').write_text('Read `references/missing.md`.\n')
            self.assertEqual(missing_reads(skill), ['1: references/missing.md'])

    def test_bare_and_parent_read_paths_are_checked(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill = root / 'skill'
            skill.mkdir()
            (root / 'outside.md').write_text('outside')
            doc = skill / 'SKILL.md'
            for instruction in ('Read `../outside.md`.', 'Load `extra.json`.'):
                with self.subTest(instruction=instruction):
                    doc.write_text(instruction)
                    self.assertEqual(len(missing_reads(skill)), 1)
            (skill / 'extra.json').write_text('{}')
            doc.write_text('Load `extra.json`.')
            self.assertEqual(missing_reads(skill), [])

    def test_optional_project_context_and_user_inputs_are_allowed(self):
        with tempfile.TemporaryDirectory() as temp:
            skill = Path(temp)
            doc = skill / 'SKILL.md'
            doc.write_text(
                'If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`), read it.\n'
                'Read the user-supplied `export.csv`.\n'
                'Load `site.json` provided by the user.\n'
            )
            self.assertEqual(missing_reads(skill), [])
            doc.write_text('Read `.agents/product-marketing.md`.')
            self.assertEqual(len(missing_reads(skill)), 1)

    def test_link_cannot_escape_install(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill = root / 'skill'
            skill.mkdir()
            (root / 'outside.md').write_text('outside')
            (skill / 'SKILL.md').write_text('Read [instructions](../outside.md).\n')
            self.assertEqual(missing_reads(skill), ['1: ../outside.md'])

    def test_source_citation_is_not_a_read(self):
        with tempfile.TemporaryDirectory() as temp:
            skill = Path(temp)
            doc = skill / 'SKILL.md'
            doc.write_text('Source: `analysis/output/benchmarks.json`.\n')
            self.assertEqual(missing_reads(skill), [])
            doc.write_text('Read `analysis/output/benchmarks.json`.\n')
            self.assertEqual(len(missing_reads(skill)), 1)

if __name__ == '__main__':
    unittest.main()
