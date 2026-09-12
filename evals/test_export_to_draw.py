"""Synthetic integration check for the Actions export to weighted draw path."""
import contextlib
import csv
import importlib.util
import io
import shlex
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


export = module("gleam_export", "skills/giveaway-results-review/scripts/gleam_export.py")
draw = module("draw", "skills/giveaway-random-draw/scripts/draw.py")


review = module("review", "skills/giveaway-results-review/scripts/review.py")


class ExportToDrawTests(unittest.TestCase):
    def test_earned_weights_survive_conversion_and_missing_weights_block_it(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "actions.csv"
            destination = Path(directory) / "entrants.csv"
            def write(weight):
                with source.open("w", newline="") as stream:
                    writer = csv.writer(stream)
                    writer.writerow(["Email", "Status", "Action", "Entries"])
                    writer.writerows([["a@example.com", "Valid", "Subscribe", "1.25"],
                                      ["a@example.com", "Valid", "Visit", weight],
                                      ["b@example.org", "Valid", "Visit", "2"],
                                      ["c@example.org", "Invalid", "Visit", "4"]])
            write("2.5")
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(export.main([str(source), "--entrants-csv", str(destination)]), 0)
            rows, column, _ = draw.load_entries(str(destination), "email")
            entrants, _, _, invalid, _ = draw.prepare(rows, column, "entries", set())
            self.assertEqual(invalid, 0)
            self.assertEqual([e["weight"] for e in entrants], [3.75, 2.0])
            self.assertEqual(sum(e["weight"] for e in entrants), export.load(source)["entries"])
            class Args:
                actions_csv = None
            command = export.review_command(export.load(source), Args)
            arguments = shlex.split(command.split(" #")[0])[2:]
            arguments[arguments.index("--impressions") + 1] = "100"
            audit = str(Path(directory) / "audit.json")
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(review.main(arguments), 0)
                self.assertEqual(draw.main(["draw", str(destination), "--id-column", "email",
                    "--weight-column", "entries", "--winners", "1", "--backups", "1",
                    "--seed", "integration-test-seed", "--audit", audit]), 0)
                self.assertEqual(draw.main(["verify", audit, "--input", str(destination)]), 0)
            destination.unlink()
            write("")
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(export.load(source)["unweighted_rows"], 1)
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                export.main([str(source), "--entrants-csv", str(destination)])
            self.assertEqual(error.exception.code, 2)
            self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
