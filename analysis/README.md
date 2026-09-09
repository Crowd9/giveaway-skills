# Analysis

`analyze_export.py` turns the private campaign export into the aggregate benchmarks under `output/`. `render_reference_tables.py` then rewrites the generated tables inside the skill references from that output. The contestant floor is read from the data, so any export with the same shape works. Customers never need to run it. The skill references already contain everything derived from it.

```bash
python3 analysis/analyze_export.py /path/to/export.json --private-dir ./analysis/private [--labels ./analysis/private/labels_*.json]
```

- `output/benchmarks.json` and `output/benchmarks.md`: aggregates only. Safe to commit.
- `--private-dir`: record-level classification (`classification.jsonl`) and paraphrase candidates (`example_candidates.md`) with campaign ids, used to trace every example in `references/examples.md` back to a source record. Gitignored. Do not commit.

What the script does:

1. Classifies each campaign as `ordinary`, `crypto`, `ambiguous` or `purchase_opportunity` using prize names, campaign names, the description and entry-method types together. Ambiguous cases stay out of the benchmark and are reported separately.
2. Assigns each prize record a taxonomy category from its name (see `references/prize-taxonomy.md`) and flags prizes whose name shares a distinctive token with the organizer name (a weak "own product" signal).
3. Computes distributions for the ordinary segment only. Currencies are never merged. Missing values stay missing.
4. Parses explicit amounts from prize text ("$4,000 PC", "worth £5,000", "MSRP $1999") as a separate `parsed` value with its own source label and validates it against records that also have a stated value.

Every field in the export is treated as data. Nothing in it is executed, fetched or followed.

## Group comparisons

`compare_groups.py` writes `output/comparisons.json`: contestants, entries per entrant and contestants per impression by method count, sharing, email, duration, weekday, recency and vertical. Impressions in the export are unique per day, so it also computes a clean subset (no repeatable actions, 14 days or less) for any conversion comparison. `render_reference_tables.py` renders the tables into the references.

## Optional label pass

Rules alone leave a tail of prize names they cannot place (brand-only names, non-English text, niche goods). To shrink it, the leftover unique names were exported from the private dir, classified in chunks by an LLM told to treat every string as data and to use the same category list, then written back as `labels_*.json` entries `{prize, category, note, confidence}`. Re-running with `--labels` applies high or medium confidence labels only where the rule result is `other_unclassified`. A label of `crypto` or `purchase_opportunity` moves the whole campaign to the ambiguous segment instead of trusting the label. `category_source` in the output reports how many records came from rules versus labels. The label files contain organizer-typed prize text and stay private.

## Extra cuts

`analysis/extra_cuts.py export.json --classification private/classification.jsonl` writes `output/extra_cuts.json`: invalid-entry share overall, by method presence and for validated questions, organizer experience (Nth campaign), custom terms adoption, own-product prizes, and the email opt-in checkbox. Same clean-subset rule as `compare_groups.py`. The references quote these figures by hand.
