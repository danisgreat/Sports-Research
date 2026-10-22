# Change proposal — framework change 2026-10-22-2

**Release:** MDS-2026.10.22-v24.0 / CR-2026.10.22-R2 / SCV-2026.10.22-v12 / SEL-2026.10.22-v4 / P-2026.10.22-v24.0 · REFMODEL-v1 · REFSEL-v1 · TIER-v1 · TB-2-MD · LEDGER-v1 · PICKS-v2 · BENCH-v1 · WIDTH-v1 · MLSCOPE-v3 · FASTCARD-v1 · SIM-v2 · GOV-v2 · STATFREEZE-v1 · RELEASE-SCOPE-v1 (unchanged).
**Class:** STATISTICAL + FORMAT + PROCEDURE (prompt major bump). Prompt 8, owner instruction.
**Review implemented:** [framework revamp review](../review_2026-10-22_framework_revamp/REPORT.md) (REV-01 to REV-22 and decisions D1 to D7).

## Owner instructions (22 October 2026, verbatim)

> completely rethink and revamp your approach to the framework, do comprehensive research on how each aspect of the prediction can be improved and how to better incorporate ML/RL, and how to incorporate simulations, what to research for and where to research it on the internet and how to comprehensively improve the framework across all sports and professions. Do your best and be honest and accurrate and comprehensive and provide a detailed and comprehensive report

> i need you to comprehensively implement each aspect of improvements mentioned and add/append/delete files in the current framework as needed, based on what the report stipulates, and push all changes to the main git branch at the ned

> comtimue implementation in its fullness

## Defects and evidence (from the review)

| # | Defect | Evidence |
|---|---|---|
| 1 | Cards lost to naive baselines while models beat them; the model was a shadow and never an input | Review §2.1; 0.2461 against 0.2360 (n = 29) in the 25 September repo review; card p diagnostics in [CARD_P_DIAGNOSTICS.csv](../review_2026-10-22_framework_revamp/CARD_P_DIAGNOSTICS.csv) |
| 2 | Hand adjustments had no measured size and no score, so the value of the research was unknowable | Review §2.2 and §4.2; no adjustment ledger existed |
| 3 | A hit rate on self-chosen lines measured line choice, not forecasting; the forced-pair record is mechanical | Review §4.7; a supplied slate of covering pairs reports 2W/2L whatever is forecast |
| 4 | Widths ran narrow | Review §4.4; width benchmarks in BASE_RATES_REGISTER §7 |
| 5 | The store held MLB and NHL only; no basketball, soccer or other lane could start | CURRENT_STATE (store view 7); 2026-10-21 review |
| 6 | The rulebook repeated the same paragraphs in 50 files and contradicted itself | 323 verbatim duplicates found (this change); review §2.2 RC7 |
| 7 | Simulation was used nowhere and its places of value were undocumented | [SIMULATION_REVIEW](../framework_change_2026-10-22-1/SIMULATION_REVIEW.md); review §7 |
| 8 | Cards were issued after the start (0 of 11 verified pre-start in the last cohort) | Review §2.1 (table row "Pre-start issue") |
| 9 | TB-1-MD halves the margin signal | Measured: calibration slope 2.12 (SE 0.10) on 3,603 NBA games |

## Decisions on the review's seven owner questions

The owner asked for every improvement to be implemented, so the review's recommended option was adopted for each question. Each is reversible by a prompt-8 change; none edits an issued record.

| # | Question | Adopted | Before → after |
|---|---|---|---|
| D1 | Market information | (a) line-implied 0.5 benchmark at settlement (BENCH-v1); (b) a no-vig close only if the owner supplies it, after settlement, as probabilities, through a loader that refuses price columns; (c) **not adopted**: the market line is not a prior and no price is searched for | No benchmark → a line-implied row in every ledger score; research stays price-blind (MARKET_BLIND) |
| D2 | Model role on cards | REFERENCE for the declared reference of each competition; ANCHOR **not adopted** (waits for a lane that passes) | Card first, model shadow after → reference frozen before the card; card = reference + logged adjustments; the card's own p frozen beside it |
| D3 | Scope | Any competition, with tiers A/B/C (TIER-v1) | Implicit → every card prints its tier; model work goes to the competitions the owner requests most (NBA first) |
| D4 | Governance | Consolidate (GOV-v2) | 50 files repeated boilerplate → CORE.md plus one-line pointers; statistical rules frozen for a season (STATFREEZE-v1) |
| D5 | Pick format | The new format (PICKS-v2) | Rank-1 gate, Rank-2 floor, top four, five shadows → probability for every supplied contract, most-likely list, information list, abstain flag, winner |
| D6 | Latency | Earlier requests where possible, a time budget and a fast card (FASTCARD-v1) | Research until done → fast card first when the full card cannot finish before the start |
| D7 | RL | Confirmed: no RL in forecasting; "ML and online learning" in the wording | Unchanged: Hedge weighting updates at settlement and stays a workshop model |

## Dispositions of the review's 22 recommendations

| REV | Disposition | Where |
|---|---|---|
| 01 Reference model before the card | ADOPT. Implemented as `ml/reference.py`, `pregame reference`, REFERENCE_CHOICE.csv. NBA, WNBA, NBL, NFL, AFL, NRL (TB-2-MD) and five soccer leagues (TB-1-MD) can run from the standings feed; NHL and MLB use their releases | REFERENCE_MODEL_PROTOCOL |
| 02 Adjustment ledger and effect tables | ADOPT. Ledger, 22 effect-table rows, λ estimator and half-size rule until 40 adjusted rows | ADJUSTMENT_LEDGER_PROTOCOL, EFFECT_TABLES |
| 03 Line-implied benchmark | ADOPT | `ml/ledger.py`, BENCHMARK_PROTOCOL |
| 04 No-vig close | PARTLY: loader and firewall built; nothing is fetched | `ml/benchmarks.py` |
| 05 Width floors | ADOPT: 28 competition rows and 8 family priors | COMPETITION_PARAMETERS |
| 06 Season releases and full-league shadows | PARTLY: NBA only (NBA-CYCLE-1, `league-day freeze|settle`). Soccer, NBL, EuroLeague, ACB have no history or release | FORECAST_CYCLE_PROTOCOL |
| 07 Ingest verified history | PARTLY: three NBA seasons, 3,693 finals on two lineages. Other competitions need the same backfill (prompt 7) | `ml/backfill_basketball.py` |
| 08 Governance consolidation | ADOPT (08a to 08e): CORE.md, card lint, season freeze, one definition per rule | CORE.md, `ml/picks.py` |
| 09 New pick format | ADOPT | SELECTION_RULES §0, `PICKS_V2` |
| 10 Calibration and λ | PARTLY: calibration checked in development (recalibration did not beat TB-2-MD); λ estimator built, no adjusted rows yet | `ml/ledger.py`, evidence folder |
| 11 Player-props engine | BUILT, NOT VALIDATED: `ml/sim/props.py` with coverage test code; no player data to validate it | SIMULATION_PROTOCOL |
| 12 Path simulators | BUILT, NOT VALIDATED: baseball, tennis (exact recursion), hockey, cricket | `ml/sim/` |
| 13 Tiers | ADOPT | `ml reference tier` |
| 14 Value-ranked checklists | ADOPT | RESEARCH_CHECKLISTS, one CHECK-v1 line per sport file |
| 15 Earlier requests, time budget, fast card | ADOPT as procedure; the owner controls request timing | REFERENCE_MODEL_PROTOCOL §7 |
| 16 Two independent research passes | DEFER (optional; owner's choice, needs the ledger first) | — |
| 17 Effect-size programme | PARTLY: 22 starter rows plus a rest-effect measurement on three NBA seasons | EFFECT_TABLES |
| 18 Monthly dashboard | ADOPT in prompt 6 | prompt 6 |
| 19 Hedge tuning study | DONE as a study: schedule gains of at most 0.002 on the common loss, development only; V3 unchanged | [nba_hedge_study](nba_hedge_study/RESULTS.md) |
| 20 External non-market benchmarks | ADOPT as post-settlement entries | BENCHMARK_PROTOCOL |
| 21 Request template | ADOPT | GAME_REQUEST_TEMPLATE |
| 22 Data-quality gates | ADOPT: `ml release-gate` G1 to G6 | `ml/releasegate.py` |

## Honest limits stated before implementation

- Every improvement is an expectation drawn from development evidence, not a demonstrated result. The first test is prospective: 8 settled weeks and 50 settled paired games per lane (unchanged floors).
- TB-2-MD fits no parameter, but its comparison with TB-1-MD is in-sample to date on stored finals; it is registered as REV-H1.
- Simulators are structurally coded and tested but NOT_VALIDATED: they have no historical coverage test against real play-by-play, so no card may use one.
- The measured NBA back-to-back effect is significant in sample and not out of sample, so it is sized at half.
- A lean on the mechanics: a reference that beats the old card baseline proves nothing about the analyst's adjustments; only the ledger can, and it starts empty.
