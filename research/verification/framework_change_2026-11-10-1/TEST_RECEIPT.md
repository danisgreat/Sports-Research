# Test receipt — framework change 2026-11-10-1

- `python -m pytest ml/tests -q`, before any edit: **776 passed**, 543.55 s, exit code 0.
- `python -m pytest ml/tests -q`, after every edit: **776 passed**, 603.09 s, exit code 0.
- `python -m ml card-history --out <folder outside the repository>`, after every edit: 2,549 rows / 638 cards; `CARD_ROWS.csv` identical to the [published history](../historical_gap_resolution_2026-11-09-1/final_history_release/CARD_ROWS.csv), 0 rows differing.
- `python -m ml state`: highest P-638, next P-639, active mini 0 open cards, 0 UNRESOLVED effective settlements.

These confirm the implemented checks and that no row changed. They say nothing about sporting accuracy or predictive skill.
