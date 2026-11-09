# Effective calibration readback

`card_calibration.load_rows()` now uses the same effective history and exclusions as card-history. No saved model-shadow artifact was overwritten.

- source: EFFECTIVE_HISTORY_VIEW
- rows: 2549
- with_numeric_p: 993
- decisive_with_p: 927
- excluded_numeric_rows: 66
- excluded_statuses: {'LOSS': 31, 'WIN': 31, 'PUSH': 4}

All four P509 learning-only rows and all P157 no-action labels are excluded. Original p/q/baselines are unchanged; this is a reporting repair, not predictive validation.
