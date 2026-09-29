# Sports Research

**Pipeline update, 2026-09-29.** The user authorized non-Markdown research code and data in this repository. [Implementation and gates](PIPELINE_IMPLEMENTATION_2026-09-29.md) and the [research workspace](research/README.md) govern the new p-ranked pilot. Historical cards remain learning-only; six combined logs and the P-523 continuation rule remain in force.

A disciplined, **market-blind** framework for researching sports events, issuing probability forecasts before the start, and settling them against the official record. It covers MLB, NPB/KBO, basketball (NBA, WNBA, NBL and more), the NHL, soccer, tennis, cricket, AFL, NRL, rugby union and the NFL.

**The 2026-09-28 Markdown-only phase is historical.** Root operating rules remain Markdown, and the user-authorized `research/` workspace now contains code, data, tests and run receipts.

> **Evidence status (2026-09-28).** Every issued forecast is **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. No model or card method is prospectively validated. The prospective baseline and RM-1 gates are at **0**, and `C-RULE-FREEZE` is in force. The historical seed comparison (29 decisions from 9 cards) is card Brier 0.2461 against a population baseline of 0.2360, and its interval spans zero. Forecasting stays `SPORTS_ONLY / MARKET_BLIND`.

## Start here (for the model and for people)

1. **[`CURRENT_RULES.md`](CURRENT_RULES.md)**: the operating manual. It covers the non-negotiables, the workflow, the card, every live rule, the recurring mistakes and custody.
2. **The sport file's §0 page** (`RULES_<SPORT>.md`): the live rules for that sport.
3. **[`PROBABILITY_TOOLKIT.md`](PROBABILITY_TOOLKIT.md)**: every calculation by hand:
   - normal, Poisson and negative binomial tables;
   - the hand-computed team baseline TB-1-MD;
   - the RM-1 ranking table;
   - Elo, departures and scoring.
4. **[`CARD_AND_LOG_TEMPLATES.md`](CARD_AND_LOG_TEMPLATES.md)**: the card, the settlement block, the Part 6 working layout, the universe table and the self-audit.
5. **[`SOURCES.md`](SOURCES.md)**: one source register, re-verified by live request on 2026-09-28, with access modes.
6. **[`PROMPTS.md`](PROMPTS.md)**: the standard prompts for continuing Part 6, carding a game, settling, reconciling and reviewing.

## How a forecast works

```text
identity + state ─► contract (lines quarantined) ─► official participants, weather, evidence
   ─► BASELINE_P and TB-1-MD ─► one joint distribution (centre, width, family masses, reference row)
   ─► each row's p, by hand from the toolkit ─► RM-1 q and tier (inside its domain) ─► rank by q ─► core self-audit
   ─► freeze the CORE before the start ─► log before delivery ─► ANNEX of disclosures after the freeze
   ─► settle from 3 independent lineages (read from the feed) ─► lineup diff, z, p grades (q as the RM-1 diagnostic) ─► retrospective ─► parked lessons
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
| Records | `prediction logs/PREDICTION_LOG_COMBINED*.md` (six parts only: Parts 1–5 canonical history; Part 6 active working custody), `GAME_LOG_STATUS_CURRENT.md`, `SKILL_BASELINE_LEDGER.md`, `MARKET_BENCHMARK_LEDGER.md` (operator, post-settlement only) |
| Evidence and history | `LEARNING_REGISTER.md`, `CHANGELOG.md`; [validation evidence](VALIDATION_EVIDENCE.md), [P-518–P-522 reconciliation](P518_P522_RECONCILIATION.md), [historical link index](HISTORICAL_LINK_INDEX.md) |
| Archived combined-log snapshots | `prediction logs/` |
| Version and freeze receipt | `METHOD.md` (header), the current `CONTROL_MANIFEST_*.md` |
| Maintainer guidance | `SCORING_AND_VALIDATION.md`, `CONTRIBUTING.md`, [verification protocol](VERIFICATION_PROTOCOL.md) |

## Current state

Use Part 6's top custody note, Part 5's closed canonical snapshot and `GAME_LOG_STATUS_CURRENT.md` together for queue state and the next ID. The latest user-directed continuation starts at P-523.

| Item | State |
|---|---|
| Canonical through P-517 | [Part 5](prediction%20logs/PREDICTION_LOG_COMBINED_5.md); Parts 1–4 are closed. [Part 6](prediction%20logs/PREDICTION_LOG_COMBINED_6.md) continues new cards from P-523, with the P-518–P-522 source quarantined |
| Next new prediction ID | **P-523**, by the user's explicit continuation instruction. P-518–P-522 stay reserved under [reconciliation](P518_P522_RECONCILIATION.md); their status does not become verified because a later ID is issued |
| Freeze receipt | The manifest named in [`METHOD.md`](METHOD.md) |
| Prospective gates | `C-BASELINE-SKILL` 0/100 · `T-RM1-PROSPECTIVE` 0/25 cards · `C-MARKET-BENCHMARK` 0/100 · **`C-RULE-FREEZE` in force; rule inventory closed** (new lessons are parked, `CURRENT_RULES.md` §D9). The counts are preregistered read-out points, not proof thresholds |
| Issue timing | Cards freeze a **core** before the start and add an **annex** afterwards (`CURRENT_RULES.md` §B), because four of the five cards before 2026-09-28(e) finished after the start and could not count |
| Historical TB-1-MD evaluation | Aggregate results reported gains over population in several league and target cohorts ([source bundle](VALIDATION_EVIDENCE.md)). The current tree lacks game-level inputs for an independent rerun; these are provisional reference anchors, not demonstrated card-level skill. |
| Predictability | STRONG (≥ 0.70) favourites exist mainly in AFL and basketball sides, less in the NFL and NRL, rarely in the NHL, and never in MLB (`BASE_RATES_REGISTER.md` §7.8) |
| Legacy settled rows | Historical extraction records were removed from the current tree; no issued row is performance-eligible |

## Canonical custody

| Part | Coverage | Custody |
|---|---|---|
| [Part 1](prediction%20logs/PREDICTION_LOG_COMBINED.md) | P-001–P-271 | Closed; settlement corrections only |
| [Part 2](prediction%20logs/PREDICTION_LOG_COMBINED_2.md) | P-272–P-332 | Closed |
| [Part 3](prediction%20logs/PREDICTION_LOG_COMBINED_3.md) | P-333–P-423; P-372 reserved | Closed |
| [Part 4](prediction%20logs/PREDICTION_LOG_COMBINED_4.md) | P-424–P-481 | Closed |
| [Part 5](prediction%20logs/PREDICTION_LOG_COMBINED_5.md) | P-482–P-517 | Closed to new cards; canonical through P-517 |
| [Part 6](prediction%20logs/PREDICTION_LOG_COMBINED_6.md) | P-518–P-522 reserved; new cards P-523 onward | Active continuation; earlier unresolved records are not certified canonical imports or performance eligible |

## For maintainers

After editing a governance file, update the Markdown freeze receipt and its pointer in `METHOD.md`, then check the Markdown files and current custody state. See [Contributing](CONTRIBUTING.md) and the [verification protocol](VERIFICATION_PROTOCOL.md).

## Honesty boundary

- Issued forecasts, ranks and probabilities are never rewritten; corrections are appended.
- Missing lineups, timestamps, probabilities or records are recorded as missing, never invented.
- Every stated probability is an `UNVALIDATED_SUBJECTIVE` output of the card's own printed distribution.
- No record here supports a performance, calibration, ROI or value claim. The first honest yardstick is the baseline ledger, and it has not been beaten yet.

## Licence

All rights reserved; see [`LICENSE.md`](LICENSE.md). Sports data remains subject to its providers' terms.
