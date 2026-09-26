# Closing-line benchmark ledger (`C-MARKET-BENCHMARK`)

**Opened 2026-09-26.** **Status: LEARNING_ONLY / scoring-only / NOT PERFORMANCE_ELIGIBLE.** This ledger compares each settled decision's issued probability with the **closing market's no-vig probability for the same contract**. It exists because a naive population table (`SKILL_BASELINE_LEDGER.md`) is the weakest honest yardstick and the closing line is the strongest public one. It is a scoring comparison only. It is never a value, ROI or performance claim.

## The firewall (why this does not break `MARKET_BLIND`)

The framework's forecasting stays market-blind (`CURRENT_RULES.md` §A.1; `METHOD.md` §1.1). This ledger sits entirely **after** settlement:

1. **Who enters rows.** The operator, by hand, after the event is final. Agent sessions never fetch betting sites or odds feeds for any purpose, and never read this ledger while researching or building a card. The ledger is outside the reading gate (`RULES_GENERAL.md` §1).
2. **When.** `Entered (UTC)` must be later than `Settled (UTC)`. `tools/market_benchmark.py report` excludes any row entered before settlement as `INVALID_ENTRY_ORDER`.
3. **What is stored.** Only the no-vig closing probability and the de-vig method. Raw odds are never committed (`CONTRIBUTING.md`). Convert them with `python tools/market_benchmark.py devig --odds <all outcomes>` and record the printed probability.
4. **What it may not do.** No rule, weight, rank, width, retrospective or learning-register disposition may cite this ledger. It answers one question — where do the cards stand against the market? — and nothing else.

## Rules

1. **One row per issued decision**, with the same decision IDs as `SKILL_BASELINE_LEDGER.md`. A forced pair is counted once. Pushes are recorded as `P` and excluded from the Brier comparison.
2. **Card p** is copied from the issued Field 4 table (`C-SUMMARY-FROM-CARD`), never retyped.
3. **Market p** is the no-vig closing probability of the **exact** contract (same line, same period, same settlement terms). If the closing market for that exact line is not available, the row is not entered. Do not interpolate between lines.
4. **Method** is one of `multiplicative`, `power`, `shin`. Use one method consistently within a season and name it.
5. **Report** with `python tools/market_benchmark.py report`: paired Brier (card − market; negative means the card was better), by family, with a card-cluster bootstrap interval.
6. **Decision rule** (preregistered 2026-09-26). After **100 decisions from at least 30 cards**:
   - **Interval below 0:** "the cards beat the closing line on this sample." Still not a value claim.
   - **Interval spans 0:** "no demonstrated difference from the closing market."
   - **Interval above 0:** "the closing market is better calibrated than the cards." This is the expected result for most forecasters and is recorded plainly. It is a reason to lean harder on the population and team baselines, not to import prices.

## Rows

None yet. The first eligible rows are decisions from cards issued under `CONTROL_MANIFEST_2026-09-26.md` or later.

| Decision | Card | Rank | Contract (as issued) | Family | Card p | Market p (no-vig close) | Method | Settled (UTC) | Entered (UTC) | Result |
|---|---|---|---|---|---:|---:|---|---|---|---|
