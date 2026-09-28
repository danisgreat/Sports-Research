# Sports Research

A disciplined, **market-blind** framework for researching sports events, issuing probability forecasts before the start, and settling them against the official record. It covers MLB, NPB/KBO, basketball (NBA, WNBA, NBL and more), the NHL, soccer, tennis, cricket, AFL, NRL, rugby union and the NFL.

**From 2026-09-28 this repository contains Markdown files only.** Every rule, calculation, template and source the forecasting model needs is in the `.md` files at the root.

> **Evidence status (2026-09-28).** Every issued forecast is **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. No model or card method is prospectively validated. The prospective baseline and RM-1 gates are at **0**, and `C-RULE-FREEZE` is in force. The historical seed comparison (29 decisions from 9 cards) is card Brier 0.2461 against a population baseline of 0.2360, and its interval spans zero. Forecasting stays `SPORTS_ONLY / MARKET_BLIND`.

## Start here (for the model and for people)

1. **[`CURRENT_RULES.md`](CURRENT_RULES.md)**: the operating manual. It covers the non-negotiables, the workflow, the card, every live rule, the recurring mistakes and custody.
2. **The sport file's §0 page** (`RULES_<SPORT>.md`): the live rules for that sport.
3. **[`PROBABILITY_TOOLKIT.md`](PROBABILITY_TOOLKIT.md)**: every calculation by hand:
   - normal, Poisson and negative binomial tables;
   - the hand-computed team baseline TB-1-MD;
   - the RM-1 ranking table;
   - Elo, departures and scoring.
4. **[`CARD_AND_LOG_TEMPLATES.md`](CARD_AND_LOG_TEMPLATES.md)**: the card, the settlement block, the mini log, the universe table and the self-audit.
5. **[`SOURCES.md`](SOURCES.md)**: one source register, re-verified by live request on 2026-09-28, with access modes.
6. **[`PROMPTS.md`](PROMPTS.md)**: the standard prompts for starting a mini log, carding a game, settling, importing and reviewing.

## How a forecast works

```text
identity + state ─► contract (lines quarantined) ─► official participants, weather, evidence
   ─► BASELINE_P and TB-1-MD ─► one joint distribution (centre, width, family masses, reference row)
   ─► each row's p, by hand from the toolkit ─► RM-1 q and tier ─► rank by q ─► self-audit ─► freeze ─► log before delivery
   ─► settle from 3 independent lineages (read from the feed) ─► lineup diff, z, p and q grades ─► retrospective ─► TESTING lessons
```

**Principles:**
- evidence comes from field owners, never from markets;
- a stated probability must come from a printed distribution;
- a single game never creates a rule;
- a claim about skill has to beat a baseline;
- a rule changes only when a preregistered, held-out test says it is better.

## Repository map

| Area | Files |
|---|---|
| Operating documents (what the model reads) | `CURRENT_RULES.md`, `PROBABILITY_TOOLKIT.md`, `CARD_AND_LOG_TEMPLATES.md`, `SOURCES.md`, `PROMPTS.md`, `RULES_<SPORT>.md` ×10, `LEAGUE_RULES_CRICKET.md`, `LEAGUE_RULES_SOCCER.md`, `BASE_RATES_REGISTER.md`, `LEARNINGS_INDEX.md` |
| Records | `PREDICTION_LOG_COMBINED*.md` (Parts 1–4 closed; Part 5 active), `GAME_LOG_STATUS_CURRENT.md`, `prediction logs/` (historical and mini logs), `SKILL_BASELINE_LEDGER.md`, `MARKET_BENCHMARK_LEDGER.md` (operator, post-settlement only) |
| Evidence and history | `LEARNING_REGISTER.md`, `CHANGELOG.md`; removed research and review material remains in Git history |
| Archived combined-log snapshots | `prediction logs/` |
| Version and freeze receipt | `METHOD.md` (header), the current `CONTROL_MANIFEST_*.md` |
| Maintainer guidance | `SCORING_AND_VALIDATION.md`, `CONTRIBUTING.md` |

## Current state

The active log's top snapshot is the only authority for queue state and the next ID.

| Item | State |
|---|---|
| Active canonical log | [Part 5](PREDICTION_LOG_COMBINED_5.md) (P-482 onward); Parts 1–4 are closed |
| Next canonical ID | **On hold.** P-518–P-522 are reserved while they are reconciled ([status](GAME_LOG_STATUS_CURRENT.md)). New cards use TMP IDs until the snapshot names the next number |
| Freeze receipt | The manifest named in [`METHOD.md`](METHOD.md) |
| Prospective gates | `C-BASELINE-SKILL` 0/100 · `T-RM1-PROSPECTIVE` 0/25 cards · `C-MARKET-BENCHMARK` 0/100 · **`C-RULE-FREEZE` in force** |
| Validated anchors | **TB-1-MD** beats the population on sides and results in the NBA, WNBA, NBL, NFL, AFL, EPL, La Liga, Bundesliga, Serie A and Ligue 1, and on totals in the NBA, WNBA, La Liga and Bundesliga. It is at least as accurate as the old tool in every league (`PROBABILITY_TOOLKIT.md` §4.3–§4.4) |
| Predictability | STRONG (≥ 0.70) favourites exist mainly in AFL and basketball sides, less in the NFL and NRL, rarely in the NHL, and never in MLB (`BASE_RATES_REGISTER.md` §7.8) |
| Legacy settled rows | Historical extraction records were removed from the current tree; no issued row is performance-eligible |

## Canonical custody

| Part | Coverage | Custody |
|---|---|---|
| [Part 1](PREDICTION_LOG_COMBINED.md) | P-001–P-271 | Closed; settlement corrections only |
| [Part 2](PREDICTION_LOG_COMBINED_2.md) | P-272–P-332 | Closed |
| [Part 3](PREDICTION_LOG_COMBINED_3.md) | P-333–P-423; P-372 reserved | Closed |
| [Part 4](PREDICTION_LOG_COMBINED_4.md) | P-424–P-481 | Closed |
| [Part 5](PREDICTION_LOG_COMBINED_5.md) | P-482 onward | Active: canonical through P-517; P-518–P-522 reserved pending reconciliation |

## For maintainers

After editing a governance file, update the Markdown freeze receipt and its pointer in `METHOD.md`, then check the Markdown files and current custody state. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Honesty boundary

- Issued forecasts, ranks and probabilities are never rewritten; corrections are appended.
- Missing lineups, timestamps, probabilities or records are recorded as missing, never invented.
- Every stated probability is an `UNVALIDATED_SUBJECTIVE` output of the card's own printed distribution.
- No record here supports a performance, calibration, ROI or value claim. The first honest yardstick is the baseline ledger, and it has not been beaten yet.

## Licence

All rights reserved; see [`LICENSE.md`](LICENSE.md). Sports data remains subject to its providers' terms.
