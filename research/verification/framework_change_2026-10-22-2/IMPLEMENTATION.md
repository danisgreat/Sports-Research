# Implementation — framework change 2026-10-22-2 (v24.0)

**MDS-2026.10.22-v24.0 / CR-2026.10.22-R2 / SCV-2026.10.22-v12 / SEL-2026.10.22-v4 / P-2026.10.22-v24.0 · REFMODEL-v1 · LEDGER-v1 · PICKS-v2 · MLSCOPE-v3 · GOV-v2.** Base `main` ba6f0e25c (the review commit). Mode `LOCAL_WORKING_TREE`. [Proposal](CHANGE_PROPOSAL.md) · [Review](../review_2026-10-22_framework_revamp/REPORT.md).

This record states what exists, what was measured and what was not done. Where a number is a development result it says so.

## What changed

### Code (`ml/`; all new modules are outside the release closure)

| File | Change |
|---|---|
| `ml/reference.py` (new) | Tiers (`tier`), declared reference (`reference_choice`), parameter rows, family priors, width floors; TB-1-MD constants for NBA, WNBA, NBL, NFL, AFL, NRL (normal) and five soccer leagues (Poisson); the average and additive (TB-2-MD) forms; league-mean prior blend (n·current + 200·prior)/(n + 200); price rows for winner, handicap and total from one grid; ESPN standings reader with receipt; `run` (reference stage; refuses a release-model reference and points to `pregame reference`); flags `TB2_NOT_TESTED_FOR_COMPETITION`, `LM_PRIOR_BLEND`, `TB1_EARLY_SEASON`, `STALE_PROFILE`, `KEY_NUMBERS_NOT_MODELLED` (NFL); receipt writer; CLI `standings|tier|width|run` |
| `ml/pregame.py` | `reference` subcommand (stage REFERENCE) and `run` re-using an executed reference (stage REFERENCE_REUSED); champions `CARD` and `TB2_MD_REFERENCE`; `compare-card --champion`; `status` counts reference-paired settled rows; receipt field `stage` |
| `ml/picks.py` (new) | Parser and linter of the `PICKS_V2` block: mass sums, complements, z consistency, width floors, abstain rule, ceiling 0.90, information-row rule, ordering; CLI `card lint` |
| `ml/ledger.py` (new) | Append-only adjustment ledger (29 columns), λ estimator, paired scoring against reference, baseline, line-implied, frozen model and benchmark, width coverage; CLI `ledger add|verify|score|coverage` |
| `ml/benchmarks.py` (new) | Benchmark loader that refuses price columns and requires an entry after the verified final |
| `ml/releasegate.py` (new) | Data-quality gates G1 to G6 on the learning store; CLI `release-gate` |
| `ml/backfill_basketball.py` (new) | Two-lineage NBA finals backfill (ESPN scoreboard and Basketball-Reference monthly pages), per-game dispositions, store ingest |
| `ml/context_study.py` (new) | Walk-forward study of the reference forms and context features (label available one day after the game, stated assumption) |
| `ml/league_day.py` (new) | Daily league lane: `freeze` writes cycle model, baseline and TB-2-MD rows for every game of a date; `settle` backfills the day's finals and settles every bundle (idempotent `_REV1`) |
| `ml/sim/` (new) | `core`, `baseball`, `tennis` (exact recursion), `hockey`, `cricket`, `props`, `cli`; seed, N ≥ 100,000 for a card, Monte Carlo error printed; baseball and hockey ship a `structure_check`, props a `coverage` test, tennis is an exact recursion; every simulator is `NOT_VALIDATED` |
| `ml/run.py` | Registers `reference`, `ledger`, `card`, `sim`, `release-gate`, `backfill-basketball`, `context-study`, `league-day` |
| `ml/tests/` | New: `test_reference.py`, `test_picks_ledger.py`, `test_releasegate.py`, `test_backfill_basketball.py`, `test_context_study.py`, `test_league_day.py`, `test_sim.py`. Changed: `test_pregame.py` (reference stage, reuse, champions), `test_prompt_consistency.py` (v24.0 titles, reference-first ordering) |

**Release scope check.** No file in the `ml.cycle` / `ml.workflow` import closure was edited. The closure digest is still `0563ffd604c9db8127a6bd24bfcadf409f6b979f37210d24523ed5007dabb829`, the digest frozen in NHL-CYCLE-4, MLB-CYCLE-4 and NBA-CYCLE-1, so none of the three releases is stale.

### Releases and data

- `research/cycle_releases/NBA-CYCLE-1.csv` (SHA-256 `82688ea9a3369d93e63abaf7d24c3868e7568b2fe5eef876d995c695d2540eef`), `EXPERIMENTAL_NOT_QUALIFIED`, 0 prospective events, row added to `CURRENT_RELEASES.csv`.
- Learning store: ingests 8 to 10 add 3,693 verified NBA finals (seasons 2023-24, 2024-25 and 2025-26) from two lineages. Every provider-A game has a disposition in `RECONCILIATION.csv` of its evidence folder; unmatched or conflicting games are NOT_INGESTED with a reason. `known_at` is the retrieval time, so these rows cannot enter a historical pregame replay.
- `research/competition_parameters/COMPETITION_PARAMETERS.csv` (28 competitions and 8 family priors) and `REFERENCE_CHOICE.csv`.
- `research/effect_tables/EFFECT_TABLES.csv` (22 rows) and `REST_EFFECT_MEASUREMENT.csv`.
- `research/adjustment_ledger/ADJUSTMENT_LEDGER.csv` (header only).
- Evidence folders here: `nba_backfill/`, `nba_dev_study_2023_24/`, `_2024_25/`, `_2025_26/`, `nhl_dev_study_2024_25/`, `nba_hedge_ledger_2023_26.csv`, `nba_hedge_study/`.

### Controls

- **New documents:** [CORE](../../../CORE.md), [REFERENCE_MODEL_PROTOCOL](../../../REFERENCE_MODEL_PROTOCOL.md), [ADJUSTMENT_LEDGER_PROTOCOL](../../../ADJUSTMENT_LEDGER_PROTOCOL.md), [BENCHMARK_PROTOCOL](../../../BENCHMARK_PROTOCOL.md), [COMPETITION_PARAMETERS](../../../COMPETITION_PARAMETERS.md), [EFFECT_TABLES](../../../EFFECT_TABLES.md), [SIMULATION_PROTOCOL](../../../SIMULATION_PROTOCOL.md), [RESEARCH_CHECKLISTS](../../../RESEARCH_CHECKLISTS.md), [GAME_REQUEST_TEMPLATE](../../../GAME_REQUEST_TEMPLATE.md).
- **Rewritten or extended by hand:** FORECAST_CYCLE_PROTOCOL, ML_EXECUTION_PROTOCOL, EXECUTION_ENVIRONMENT_PROTOCOL, CURRENT_RULES, METHOD, SELECTION_RULES, SCORING_AND_VALIDATION (§12), PROBABILITY_TOOLKIT (TB-2-MD, §4.5), CARD_AND_LOG_TEMPLATES (PICKS_V2 and ledger sections), prompts 1 to 8, the eleven sport files (a CHECK-v1 line and a reference line each), COMMON_OPERATING_PROTOCOL, prompt README, DEPENDENCY_MAP (regenerated from the files), CURRENT_STATE, README, PROMPTS, CHANGELOG, ACTIVE_FILE_INDEX, HYPOTHESIS_REGISTER (REV-H1 to REV-H4), SOURCES (§2.5), LEARNING_PIPELINE_PROTOCOL (§11), ml/README, BASE_RATES_REGISTER and LEAGUE_PROFILES (pointers), ML_RL_IMPLEMENTATION_FRAMEWORK (update note).
- **Consolidation (GOV-v2):** a script run outside the repository replaced 323 verbatim boilerplate paragraphs (known bold titles, three or more identical copies, never in the definer's own file) in 51 documents with a one-line pointer to the definition and to CORE, saving 181,978 bytes. Custody and history files (GAME_LOG_STATUS_CURRENT, CHANGELOG, HISTORICAL_LINK_INDEX, VALIDATION_EVIDENCE, LEARNINGS_INDEX, LEARNING_REGISTER) were excluded, and line endings were preserved per file. Pre-consolidation copies were kept outside the repository during the run.
- **Prompt version:** P-2026.10.22-v24.0 in all eight prompts and the eleven sport files (tests require exactly one version per prompt).
- **Archive:** [archive/superseded_2026-10-22-2/](../../../archive/superseded_2026-10-22-2/), the committed bytes (`git show HEAD:path`) of the 71 tracked Markdown files this change replaced; each copy was verified equal to its blob. `.gitattributes` keeps the archive and the new evidence and data folders byte-exact.

## Measured

All numbers are development evidence on stored finals unless marked prospective; there is no prospective evidence yet.

| Result | Value | Where |
|---|---|---|
| TB-1-MD against TB-2-MD, NBA 2023-26 (3,603 games, season to date) | Brier 0.2189 → 0.2106; calibration slope 2.12 (SE 0.10) → 1.04 (SE 0.05) | REFERENCE_MODEL_PROTOCOL §5 |
| Same comparison, NHL 2024-25 (1,282) and MLB 2025 (344) | 0.2429 → 0.2417 and 0.2450 → 0.2427; intervals not computed | same |
| Hedge schedules on NBA (1,231 test events, 26 weeks) | Best schedule changes the common loss by −0.0019 (interval −0.0033 to −0.0005); schedule choice made on the tune window only; V3 unchanged | [nba_hedge_study](nba_hedge_study/RESULTS.md) |
| Rest (back-to-back) effect, NBA | Significant in sample, not out of sample → entered at half size, `MEASURED_NOT_CONFIRMED` | EFFECT_TABLES |
| Recalibration of the fitted model | Did not beat TB-2-MD | nba_dev_study folders |
| Simulators | Structure checks pass on illustrative parameters (baseball 28.6% one-run, 9.7% extras); no historical coverage test | `ml/sim/` tests |

## Verification

- **Full test suite:** `python -m pytest ml/tests` on the final working tree: **633 passed, 0 failed** in 440 s (the suite had 514 passing tests before this change). New and changed tests cover the reference stage and its refusals, TB-1 against TB-2 forms, the league-mean prior blend, tier and width ladders, the picks linter, the ledger and its scoring, the benchmark firewall, the release gate, the two-lineage reconciliation, the walk-forward study, the league-day lane, every simulator's structure and the prompt-suite consistency rules.
- **Prompt consistency:** 75 tests pass (one version per prompt, resolved links, dependency map equal to the files in both directions, reference-first ordering in prompt 1).
- **Release closure:** the digest is unchanged (`0563ffd6…b829`), so NHL-CYCLE-4, MLB-CYCLE-4 and NBA-CYCLE-1 verify against the working tree.
- **Live freeze, the first run of the daily league lane** (`python -m ml league-day freeze --competition "Basketball/NBA" --date 2026-10-22 --confirm-no-outcome-seen`, 2026-10-22 05:27 to 05:29 UTC, before either tip-off):

  | Local key | Game | Scheduled start (UTC) | Model | Reference | Reference p(home) | Reference p(over 229.5) |
  |---|---|---|---|---|---|---|
  | LOCAL-LEAGUE-NBA-20261022-G0001 | Cleveland Cavaliers @ Philadelphia 76ers | 2026-10-22 23:00 | EXECUTED | TB2-MD:NBA | 0.5978 | 0.3373 |
  | LOCAL-LEAGUE-NBA-20261022-G0002 | Denver Nuggets @ Oklahoma City Thunder | 2026-10-23 01:30 | EXECUTED | TB2-MD:NBA | 0.6485 | 0.4289 |

  `pregame status` then reads `NBA-CYCLE-1 frozen_events=2 pre_start_events=2 settled_events=0 state=ACCUMULATING`. These are lane rows, not cards: no analyst probability exists for them, and they settle with `league-day settle`. Early in a season the standings rest on a game or two, so the league-mean prior blend (`LM_PRIOR_BLEND`) and the early-season flag apply to these reference numbers; they are starting points, not forecasts of skill. The totals line is the competition's own verified mean, not a market line.

## Not done, and why

- **Soccer, AFL, NRL, NFL, cricket, tennis, rugby union:** no stored history and no release. They get TB-1-MD or TB-2-MD from the standings feed where constants exist (flagged `TB2_NOT_TESTED_FOR_COMPETITION`) and otherwise tier C with a league-only baseline or `NONE`. Prompt 7 owns building their history (the NBA backfill is the pattern).
- **Simulators (REV-12) and the props model (REV-11):** coded and tested for structure, not validated against real play-by-play or player data. Prompt text forbids using one for a card until `structure_check` passes on the competition's own history.
- **ANCHOR role (D2):** not adopted. A model becomes an anchor only after a lane passes the 8-week / 50-game decision floor with a paired interval below zero.
- **Market inputs (D1 c):** not adopted. No price, line or odds is searched for; the benchmark loader exists for owner-supplied comparators only.
- **Two research passes (REV-16):** deferred; it needs a populated ledger first.
- **Adjustment ledger:** empty. The first λ needs 40 adjusted rows; until then adjustments run at half size (HALF) and the hypotheses REV-H2 to REV-H4 are `BLOCKED_DESIGN`.
- **EuroLeague, ACB, NBL, WNBA, B.League, KBL basketball lanes:** no history ingested; only the NBA has a release and a lane.
- **Issued records:** nothing earlier was regraded, renumbered or rewritten; earlier cards keep the Rank-1 gate and Rank-2 floor they were issued under.

## Rollback

Every replaced Markdown file is archived byte for byte. The code is additive: reverting this commit restores the v23.0 behaviour, and NHL-CYCLE-4 / MLB-CYCLE-4 are unaffected because the release closure was not touched. The learning-store ingests are append-only and carry their own receipts.
