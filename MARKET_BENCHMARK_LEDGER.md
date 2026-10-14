# Closing-Line Market Benchmark Ledger (`MKT-BENCH-v1`)

**Authority:** MDS-2026.10.14-v11.1 Â· CR-2026.10.14-R3 Â· SCV-2026.10.14-v8.
**Framework change:** `2026-10-14-2` (Restored under Owner Decision D3-ii).
**Status:** `LEARNING_ONLY` / post-settlement scoring only / `NOT PERFORMANCE_ELIGIBLE`.

This ledger records post-settlement comparisons between issued card/model probabilities and the **closing market's no-vig probability for the exact identical contract**. It serves as an objective reference benchmark. It is never used for staking, value claims, betting advice, or live selection.

---

## The Firewall (Preserving `MARKET_BLIND`)

The framework's pregame research and forecast issuance remain strictly market-blind (`CURRENT_RULES.md` Â§5). This ledger operates exclusively **post-settlement**:

1. **Post-Settlement Entry Only:** Rows are entered strictly after the event is official and final. `Entered (UTC)` must be strictly later than `Settled (UTC)`. Any row entered prior to settlement is tagged `INVALID_ENTRY_ORDER` and purged.
2. **Reading-Gate Exclusion:** Agent sessions running Prompts 1, 2, and 3 must never open or read this ledger while researching or card-authoring.
3. **No Raw Odds:** Only the de-vigged closing probability and the conversion method are stored. Raw odds, lines, and volume are never committed.
   - De-vig methods: `multiplicative`, `power`, or `shin`.
4. **Zero Upstream Feedback:** No rule, weight, rank, probability width, or card recommendation may cite or be influenced by this ledger.

---

## Preregistered Benchmark Decision Rule

After $N \ge 100$ independent decisions across at least 30 cards/fixtures:
- **95% CI upper bound < 0:** "The forecasts demonstrate positive informational resolution relative to the closing market." (Descriptive only; never a value/staking claim).
- **95% CI spans 0:** "No demonstrated difference from the closing market."
- **95% CI lower bound > 0:** "The closing market is better calibrated than the forecasts." (Expected result; prompts conservative reliance on frozen baselines).

---

## Ledger Entries

| Decision ID | Card / Shadow ID | Rank | Contract (exact text) | Family | Model / Card p | Market p (no-vig close) | De-Vig Method | Settled (UTC) | Entered (UTC) | Result |
|---|---|---|---|---|---:|---:|---|---|---|---|
