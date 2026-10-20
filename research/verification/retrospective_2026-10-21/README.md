# Retrospective 2026-10-21 — P-601 to P-622

Start with [RETROSPECTIVE_REPORT.md](RETROSPECTIVE_REPORT.md).

- [DATA_INVENTORY.md](DATA_INVENTORY.md) — scope (written before analysis), receipts, per-ID inventory.
- [COHORT_TABLES.md](COHORT_TABLES.md), [COHORT_ROWS.csv](COHORT_ROWS.csv) — row-level cohort tables (102 rows).
- [HISTORY/](HISTORY/CARD_HISTORY.md) — `python -m ml card-history` on the committed rank log (through P-600).
- [LEARN_EXPORT/](LEARN_EXPORT/) — the exact export ingested as `ingest_seq` 7 (`EXPORT/GAME_OBSERVATIONS.csv`, `EXPORT/TEAM_GAME_STATS.csv`) and `CAPTURE_INVENTORY.csv`. The captures themselves are outside the repository.
- [TRAINING_CANDIDATES.csv](TRAINING_CANDIDATES.csv) — label-candidate plan and exclusions. The candidates are in `research/training_candidates/`.
- [SHADOW_SETTLEMENT/](SHADOW_SETTLEMENT/) — `primary settle` output for the one unpaired local shadow.
- [LEARNING_STATUS/](LEARNING_STATUS/LEARNING_STATUS.md) — counters after the ingest and the review rows.
- [IMPLEMENTATION_CHECKS.md](IMPLEMENTATION_CHECKS.md) — every check that was run.
