# Additional artifact admission notice — repeat bug audit

The [repeat implementation audit](../verification/ml_bug_audit_2026-10-14-1/IMPLEMENTATION.md) repairs source parsing/identity, legal cricket inputs, grids, fit failures, scoring/missingness, calibration, shadow settlement and paper decision mechanics. **Existing generated model artifacts are historical outputs of their recorded implementation. They are not outputs of this repaired implementation and must not be used as current predictions or prospective qualification.**

Their numerical values and receipts are preserved. Any claim about current performance requires an actual controlled regeneration with stable code/data/config, exact source admission and fresh receipts. Do not stamp a new source digest on the old values or inherit the old PASS status. The prior DATA_HOLD/no-card-input/no-promotion controls remain in force. Fixed-parameter smoke checks establish construction only, not predictive gain.

The new audit's EPL decision replay uses the existing historical prediction cache explicitly; it is not a retrained EPL forecaster or verified execution study. No RL benefit, prospective lane, card assistance or source certification is granted. The decision lab stays outside card reading gates.
