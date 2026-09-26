# Sports Research

A disciplined, **market-blind** framework for researching sports events, issuing probability forecasts before the start, and settling them against the official record. It covers MLB, NPB/KBO, basketball (NBA, WNBA, NBL and more), the NHL, soccer, tennis, cricket, AFL, NRL, rugby union and the NFL. Everything is recorded in Markdown: every forecast, the evidence behind it, its settlement and every lesson learned.

> **Status.** Method **MDS-2026.09.19-v4.3** · control revision **CR-2026.09.21-3** · every record is **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. This is research, not betting advice. Forecasting is market-blind by design; the only market use is a post-settlement scoring benchmark (`C-MARKET-BENCHMARK`). **No forecasting model has been fitted and validated yet:** RM-1 (a ranking calibration) and TB-1 (a team baseline) are fitted layers, and the MLB pilot (`tools/mlb_model.py`) is tested code with no fit. The first card-versus-baseline check (`SKILL_BASELINE_LEDGER.md`) shows **no demonstrated skill yet over a naive population baseline**. From 2026-09-26, **`C-RULE-FREEZE`** holds new predictive rules until the evidence gates report: run `python tools/evidence_status.py`.

## Start here

1. **`python tools/evidence_status.py`**: where every preregistered test stands, and whether `C-RULE-FREEZE` is in force.
2. **[`CURRENT_RULES.md`](CURRENT_RULES.md)**: the live rules on one page, with the workflow, the card format, sport quick cards, the recurring-mistake list and the tools.
3. **The sport file's §0 live rules page**: every `RULES_<SPORT>.md` opens with a one-page consolidation of its live controls (2026-09-26). With `CURRENT_RULES.md` it is Tier 1 of the reading gate (`RULES_GENERAL.md` §1); the rest of each file is read by citation.
4. The active log's top snapshot, [`PREDICTION_LOG_COMBINED_5.md`](PREDICTION_LOG_COMBINED_5.md), for the next ID and open items, and the day's declared universe in `universe/`.
5. **[`LEARNINGS_INDEX.md`](LEARNINGS_INDEX.md)**: every lesson, test and recurring mistake, one line each, with its status.

## How it works

```text
identity + state ─► contract (lines quarantined) ─► official participants, weather, evidence
   ─► one joint outcome distribution (centre, width, family masses, reference row, BASELINE_P)
   ─► derive every row's probability ─► rank by probability ─► freeze (manifest SHA) ─► log before delivery
   ─► settle from 3 independent lineages ─► receipts, lineup diff, z-scores ─► retrospective ─► tested lessons
```

The framework's working principles:
- evidence comes from field owners, never from markets;
- a stated probability must come from a printed distribution;
- a single game never creates a rule;
- every claim about skill has to beat a baseline.

## Repository map

| Area | Files |
|---|---|
| Live rules | [`CURRENT_RULES.md`](CURRENT_RULES.md) (summary) and each `RULES_<SPORT>.md` §0 live page → [`METHOD.md`](METHOD.md), [`RULES_GENERAL.md`](RULES_GENERAL.md), the rest of `RULES_<SPORT>.md`, [`LEAGUE_RULES_CRICKET.md`](LEAGUE_RULES_CRICKET.md), [`LEAGUE_RULES_SOCCER.md`](LEAGUE_RULES_SOCCER.md), [`CONTROLS.md`](CONTROLS.md) |
| Scoring and evidence of skill | [`SCORING_AND_VALIDATION.md`](SCORING_AND_VALIDATION.md) (§16: the measurement ladder), [`SKILL_BASELINE_LEDGER.md`](SKILL_BASELINE_LEDGER.md), [`MARKET_BENCHMARK_LEDGER.md`](MARKET_BENCHMARK_LEDGER.md) (post-settlement only), [`PERFORMANCE_ELIGIBILITY_POLICY.md`](PERFORMANCE_ELIGIBILITY_POLICY.md), `universe/` (declared event universes) |
| Reference data | [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md) (§7: cross-sport rates and width benchmarks), [`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md), [`research/`](research/base_rates_2026-09-25/README.md) (re-runnable queries) |
| Sources | [`SOURCES.md`](SOURCES.md) (quick), [`DATA_SOURCE_REGISTER.md`](DATA_SOURCE_REGISTER.md) (full) |
| Procedures | [`UPCOMING_GAME_RESEARCH_GUIDE.md`](UPCOMING_GAME_RESEARCH_GUIDE.md) (pregame), [`EXTERNAL_LOGGING_WORKFLOW.md`](EXTERNAL_LOGGING_WORKFLOW.md) (mini logs, settlement), [`AGENT_ROLE_AND_TASK.md`](AGENT_ROLE_AND_TASK.md) |
| Learning | [`LEARNINGS_INDEX.md`](LEARNINGS_INDEX.md) (one line per item, with status) → [`LEARNING_REGISTER.md`](LEARNING_REGISTER.md) (evidence; recurring mistakes M1–M34) |
| Logs | Parts 1–4 (closed) and [Part 5](PREDICTION_LOG_COMBINED_5.md) (active); [`GAME_LOG_STATUS_CURRENT.md`](GAME_LOG_STATUS_CURRENT.md) (state register); `Mini logs (to be sent to actual log later)/` (active mini log) |
| Numerical program (reduced-feature A0/A1 models for every sport, as code; validated where public results were reachable; shadow only) | [`NUMERICAL_PROGRAM.md`](NUMERICAL_PROGRAM.md), [`H0_DATASET_CARD.md`](H0_DATASET_CARD.md), [`NUMERICAL_MODEL_REGISTER.md`](NUMERICAL_MODEL_REGISTER.md), [`NUMERICAL_TRAINING_SPEC.md`](NUMERICAL_TRAINING_SPEC.md), [`MODEL_AND_DATA_SPEC.md`](MODEL_AND_DATA_SPEC.md), [`ALGORITHM_PORTFOLIO_AND_EVALUATION.md`](ALGORITHM_PORTFOLIO_AND_EVALUATION.md), [`MODEL_IMPLEMENTATION_RECIPES.md`](MODEL_IMPLEMENTATION_RECIPES.md), `tools/mlb_model.py`, [`research/mlb_shadow/`](research/mlb_shadow/README.md) |
| Freeze receipts | `CONTROL_MANIFEST_*.md` (the current one is named in `METHOD.md`'s header) |
| History | [`CHANGELOG.md`](CHANGELOG.md) (dated changes, including the former README body), `archive/` (implemented audits, archived mini logs, historical snapshots) |

## Quickstart

All tools are standard-library Python 3.10 or later. There is nothing to install.

**Before the day's first card**

```bash
python tools/evidence_status.py                                    # gates, and whether C-RULE-FREEZE is in force
python tools/slate_universe.py declare --date 2026-09-27 --league mlb --league epl   # C-EVENT-UNIVERSE
```

**Before issuing a card**

```bash
python tools/verify_manifest.py               # governance files match the current freeze receipt
python receipts.py pregame mlb 824703         # MLB: probables, official lineups, gamefeed weather, state
python receipts.py pregame espn basketball/nbl 401875254   # ESPN leagues: state, injury list
```

Print the reference row, reference width and `BASELINE_P` from [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md) §7. Build the six-field card ([`METHOD.md`](METHOD.md) §4) and append it to the active mini log before delivery.

**Straight after freezing a card (never shown on the card)**

```bash
python tools/mlb_model.py shadow --gamepk 824703 --total 8.5 --card P-518                          # MLB
python tools/sport_models.py shadow --league epl --event 740123 --date 2026-09-27 --card P-519 --total 2.5 --line -0.5   # every other sport
```

**At settlement**

```bash
python receipts.py settle mlb 824223 --card-home "Name A;Name B" --card-sp-home "Pitcher"
python receipts.py settle nhl 2026010034 --card-goalie-home "Goalie"
python receipts.py settle espn basketball/wnba 401857213 --card-away "A;B;C"
python audit_card_controls.py "<mini log>.md" --settlement --strict
python tools/skill_baseline.py                # prospective rows (counted) and seed rows (never counted), separately
python tools/slate_universe.py status universe/UNIVERSE_2026-09-27.json --log "<mini log>.md"
python tools/mlb_model.py settle && python tools/mlb_model.py score
python tools/sport_models.py settle && python tools/sport_models.py score
python tools/market_benchmark.py report       # operator-entered closing lines, after settlement only
```

**When building a card, and at each 25-card review**

```bash
python tools/card_math.py total --dist negbin --mean 8.4 --sd 3.97 --line 7.5       # rows from the card's own distribution
python tools/card_math.py cover --dist normal --mean 1.44 --sd 13.63 --line -1.5 --no-zero
python tools/card_math.py departure --p 0.613 --baseline 0.530 --mech "pace:0.6" --mech "lineup:0.4"
python tools/team_baseline.py predict --league nbl --home "Brisbane Bullets" --away "Illawarra Hawks" --date 2026-09-25 --total 188.5 --home-line -1.5
python tools/rank_model.py rank --sport nbl --row "Under 188.5=0.646" --row "Hawks +1.5=0.540" --row "Bullets -1.5=0.460" --row "Over 188.5=0.354"
python research/settled_rows_2026-09-25/extract_settled_rows.py && python tools/calibration_report.py
```

**Before committing** (CI runs the same checks: [`.github/workflows/checks.yml`](.github/workflows/checks.yml))

```bash
python -m unittest discover -s . -p "test_*.py"
python -m unittest discover -s tools -p "test_*.py"
python tools/repo_hygiene.py
python tools/verify_manifest.py
```

If you edited a governance file, regenerate the freeze receipt with `python tools/make_manifest.py --out CONTROL_MANIFEST_<date>.md --title "…" --note "…" --category <INTEGRITY|MEASUREMENT|DOCUMENTATION|VALIDITY_REPAIR|MODEL_CHANGE>` (one per issuing day; a `MODEL_CHANGE` needs the user's instruction while `C-RULE-FREEZE` is in force). Then repoint `METHOD.md` and the active mini log. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the branch and pull-request workflow.

## Current state

*The active log's top snapshot is the only authority for queue state and the next ID; this table is a convenience.*

| Item | State |
|---|---|
| Active canonical log | [Part 5](PREDICTION_LOG_COMBINED_5.md) (P-482 onward). Parts 1–4 are closed |
| Active mini log | `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-516 onward - 2026-09-25/` |
| Next canonical ID | See Part 5's snapshot (**P-518** as of 2026-09-26: P-510–P-515 imported in §"2026-09-25(f)"; P-516/P-517 assigned to the settled temporary IDs in §"2026-09-26(a)") |
| Temporary IDs | None open. `TMP-20260923-NPB-CHU-DB-G25` = **P-516**; `TMP-20260923-NBL-CNS-TAS` = **P-517** (2026-09-26(a)) |
| Freeze receipt | The manifest named in [`METHOD.md`](METHOD.md)'s header |
| Skill v baseline | Seed: card Brier 0.2461 v naive baseline 0.2360 (n = 29, 9 cards; interval spans 0). Prospective count 0 of 100 |
| Full-record calibration (rebuilt dataset, re-run 2026-09-26) | 411 decisions, 155 cards, **self-selected events**: Brier 0.2268, slope 1.01, skill +6.6% over the base rate. Skill lives at p ≥ 0.65 (about 80% won); 0.50–0.65 is coin-flip-grade (53.6%). Non-baseball underdog cushions are over-confident (17/40 at 0.642). Soccer has the strongest resolution (37 cards; interval spans 0); MLB and basketball near zero; tennis, NFL/NCAA and AFL none ([details](research/settled_rows_2026-09-25/README.md)) |
| Ranking and baselines (2026-09-25(e)) | **RM-1** calibrates each stated p into a ranking probability q, and cards rank by q. Held out: top-two wins +0.068 per card [+0.007, +0.128]; Rank 1 64.2% → 68.9% ([details](research/rank_model_2026-09-25e/README.md)). **TB-1** is a leak-free team-strength baseline with resolution for sides in NBA/WNBA/NBL/NFL/AFL/NRL/EPL, and none in MLB/NHL ([details](research/team_baseline_2026-09-25e/README.md)). Rank 1 is "far more likely to win than lose" only in the STRONG tier (q ≥ 0.70: 81% of decisions) |
| Numerical model | H0 not built ([`H0_DATASET_CARD.md`](H0_DATASET_CARD.md)). RM-1 and TB-1 are a calibration layer and a population baseline, not H0. RM-1 is **promising and unproven** (its cushion term was found on the data that validates it; [caveats](research/rank_model_2026-09-25e/README.md)). The MLB A0/A1 pilot is implemented and tested on synthetic data; it runs as a **prospective shadow** only (`C-MLB-SHADOW`) | **Every other sport (2026-09-26(c), (d))** has a reduced-feature A0/A1 model in `tools/sport_models.py`, with a blind shadow lane (`C-SPORT-SHADOW`, tennis and cricket included). On public results, A1 beat the league baseline on results and margins in soccer (five leagues), the NFL, AFL, NBA, WNBA and NHL. It beat TB-1 on results in the EPL, AFL, NBA, WNBA and NHL. On totals it helped in basketball and little elsewhere, and was worse in the NHL. Cricket (IPL) shows no skill. MLB, tennis and cricket each needed a re-selected parameter. NBL, NCAAF, NRL, rugby union, WTA, the Asian baseball leagues, non-IPL cricket and the smaller soccer competitions are not yet validated ([details](research/sport_models_2026-09-26/README.md)).
| Predictability across sports (2026-09-26(e)) | STRONG (≥ 0.70) favourites exist mainly in AFL and basketball sides (26–39% of games, 80–91% won), less in the NFL and NRL, rarely in the NHL, never in MLB ([map](BASE_RATES_REGISTER.md)). On 98 of their own contracts the cards were no worse than the team models (0.2438 v 0.2505), so the models stay a reference (`tools/model_anchor.py`, `REFERENCE`) ([details](research/predictability_2026-09-26/README.md)) |
| Evidence gates and rule freeze (2026-09-26) | `C-BASELINE-SKILL` 0/100, `T-RM1-PROSPECTIVE` 0/25 cards, `C-MARKET-BENCHMARK` 0/100, `C-MLB-SHADOW` 0/150 games, `C-SPORT-SHADOW` 0 rows, no universe declared yet. **`C-RULE-FREEZE` in force.** Live figures: `python tools/evidence_status.py` |

## Canonical custody

| Part | Coverage | Custody |
|---|---|---|
| [Part 1](PREDICTION_LOG_COMBINED.md) | P-001–P-271 | Closed; settlement corrections only, including the reopened P-255/P-256 period questions |
| [Part 2](PREDICTION_LOG_COMBINED_2.md) | P-272–P-332 | Closed; nine inherited primary follow-up handles |
| [Part 3](PREDICTION_LOG_COMBINED_3.md) | P-333–P-423; P-372 reserved | Closed; 13 primary follow-up handles |
| [Part 4](PREDICTION_LOG_COMBINED_4.md) | P-424–P-481 | Closed at P-481; unresolved follow-up handles are tracked in the status register |
| [Part 5](PREDICTION_LOG_COMBINED_5.md) | P-482 onward | **Active queue / next-ID authority** |

Older component logs, archived mini variants and dated audits are evidence; they are not instructions. Preserve canonical IDs and temporary aliases. [`EXTERNAL_LOGGING_WORKFLOW.md`](EXTERNAL_LOGGING_WORKFLOW.md) covers variant discovery, reconciliation and archiving.

## Honesty boundary

- Issued forecasts, ranks and probabilities are never rewritten; corrections are appended.
- Missing lineups, timestamps, probabilities or records are recorded as missing, never invented.
- Every stated probability is an `UNVALIDATED_SUBJECTIVE` output of the card's own printed distribution.
- No record in this repository supports a performance, calibration, ROI or value claim. The first honest yardstick is the baseline ledger, and it has not been beaten yet.

## Licence

All rights reserved; see [`LICENSE`](LICENSE). Sports data remains subject to its providers' terms. The repository stores only derived statistics and small trimmed test fixtures.
