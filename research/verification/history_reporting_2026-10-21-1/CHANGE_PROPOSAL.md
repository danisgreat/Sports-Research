# History-reporting repair — 21 October 2026

Owner request: implement point 2 of the framework review, the history tool's omission of P-601–P-622. Authority: LOCAL_WORKING_TREE, main at `476def8e2`. Initial unrelated files: `BASKETBALL.txt` and `MINI LOGS TO BE SETTLED/`; preserve both.

Classification: reporting/integrity repair. No forecast, selection, scoring formula, probability threshold, prompt or model policy changes. Existing MDS/P/CR/SCV releases remain unchanged. This work does not establish predictive improvement.

Before: `card-history` named three historical inventories and Combined Log parts 1–7 explicitly. Its output stopped at P-600; the latest retrospective used an external helper script. Merely adding the latest inventory would also risk counting research-only probabilities as primary forecasts.

After: discover supported import inventories and numbered log parts on every invocation; preserve probability roles and source rows; report original primary slots and baseline coverage by cohort; expose canonical records without contract rows. Record all consumed inventories, mapping files and log parts in the receipt, and refuse unsupported schemas, duplicate effective contracts, ambiguous overlapping inventories and inputs changed during execution.

Scope: `ml/evaluation/card_history.py`, focused tests, workshop README, CHANGELOG, byte-preserved source backups and this verification package. Generated results go in a new folder. Do not refresh or overwrite GAME_PREDICTION_RANK_LOG.csv, canonical records, historical reports, model releases or owner minis. The derived report combines the historical rank log with imported rows directly.

Acceptance:

- P-601–P-622: all 102 contract rows from 22 cards, matching preserved probabilities, ranks, grades, dates, revisions and available baselines.
- Primary cohort: 11 cards, 50 rows, 22 primary slots, 11 WIN / 10 LOSS / 1 PUSH, decisive Brier 0.204092523809524, baseline coverage 8/50.
- Research-only cohort: 52 diagnostic rows, no primary slots or calibration contributions.
- Future import folders and two-digit log parts are discovered without a code edit; new canonical records with missing rows are visible.
- Focused tests, full workshop suite, an actual CLI run and output/receipt readback.

Rollback: restore only changed working documents/code from `archive/history_reporting_2026-10-21-1/`; remove this new generated report from active navigation if required. Preserve all original research, canonical records and historical reports. No publication is requested by this task.
