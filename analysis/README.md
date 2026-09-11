# Analysis

The JSON files under `output/` are the aggregate findings the skills quote. Every skill reference cites the file and the block a figure came from, so any number in the skills can be traced to the table behind it.

Each file holds counts, medians and percentile tables for one topic: benchmarks, percentiles, entry-method mix, prize economics, timing and the calendar, industries and verticals, organizer history, thresholds, templates and campaign types. `benchmarks.md` is a readable summary of `benchmarks.json`.

Two rules hold across all of them:

- **Aggregates only.** No row describes fewer than five distinct businesses, so no row describes one company. Groups below that floor are counted and not described.
- **Description, not cause.** Every figure says what campaigns did, never what caused a result. The skills state that alongside the numbers.

Sample sizes sit next to every figure. Where a field is missing on some campaigns the count for that figure is lower, and the file carries its own `n`.
