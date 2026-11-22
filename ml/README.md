# `ml/` — forecasting, custody, evaluation and workshop code

This is the only directory in the repository where code lives. Active daily operation is **ONE-CHAT-v3** ([RUNBOOK](../research/one_chat/RUNBOOK.md), [EVALUATION_PLAN_v29.0](../research/external/EVALUATION_PLAN_v29.0.md)); fitted models remain separate from cards until promoted (`ML-SEP-v1`).

## Active commands (`ONE-CHAT-v3`, `HPPV-v1`, `CARD-TRAIN-v1`, `KIT-v1`, `STATE-v1`)

```text
python -m ml one-chat prepare --message CHAT1.txt --mini MINI21 --out <prep>/MINI21
python -m ml one-chat register-requests --folder <prep>/MINI21
python -m ml one-chat seal --watch <minis_dir>                                         # or --card FILE [...]
python -m ml one-chat intake --from-seals --out research/one_chat/intake/<run>
python -m ml one-chat score --intake <intakes> --outcomes <outcomes> --out research/one_chat/scores/<run>
python -m ml one-chat power --out <dir>                                                # registered simulation power study
python -m ml historical-pre-event run|verify|append|backtest                           # Track H (HPPV-v1, separate from Track P)
python -m ml card-training run|verify --out research/card_training/<run>               # CARD-TRAIN-v1 walk-forward study
python -m ml kit verify|params|sha                                                     # calculation kit (ml/kit/sr_kit.py)
python -m ml deep-loss check|tally                                                     # deep loss register
python -m ml state [--write | --restamp]                                               # sync CURRENT_STATE.md, README.md, prompts
python -m pytest ml/tests                                                              # full regression suite
```

**HPPV-v1 (Track H):** [Operator guide and schemas](../research/verification/historical_pre_event_v1/README.md). The frozen 685-card census, reviewed custody evidence, exact endpoints, independent outcomes, same-contract benchmarks and event-level statistics never feed the Track P prospective registry.

## Legacy workshop & retained commands

*The sections below describe the retained historical workshop, `PICKS_V2` reference/ledger lane (`MLSCOPE-v3`), and earlier `EXT-v2`/`EXT-v3` commands. Retired one-off scripts (`ml/studies/*`, `ml/evaluation/primary_replay.py`, `ml/historical_backfill.py`, `ml/historical_identity.py`) were pruned on 19 November 2026 and remain recoverable at [`cb97bbc2a`](../HISTORICAL_LINK_INDEX.md#pruning--2026-11-19-retired-docs--unreferenced-ml-modules).*

## Run

```text
python -m pip install -r ml/requirements.txt
python -m pytest ml/tests                          # 40+ checks; C-ML-01..18 of the framework's §12
python -m ml discover                              # optional reviewed-history discovery; empty when no root exists
python -m ml run-all --workers 8                   # every modellable competition, card calibration, decision lab, STATUS
python -m ml competition "Basketball/NBL" "Soccer/Premier League"   # selected competitions by archive path
python -m ml cards | decision-lab | index
```

Intermediate full predictions are written outside the repository to `ML_CACHE` (default `../Sports-Research-workshop-cache`). Pinned versions used for the committed outputs are in [requirements.txt](requirements.txt); every output records Python, numpy, pandas and scipy versions, the SHA-256 of the code and of the archive files it read.

## One process for every competition

The workshop has no list of "main leagues". `ml/config.py` walks `research/reviewed_history/<Sport>/<Competition>/` and, for every folder:

1. **Classifies it.**
   - header-only;
   - alias copy (ACTIVE_FILE_INDEX §2);
   - single-game subset (a final modelled inside its parent);
   - suspected default dates (over 25% of dated games on one month-day, so the known-at rule cannot be applied);
   - unsupported sport or endpoint (tennis, field hockey, multi-day cricket);
   - modellable.
2. **Detects its columns.** It finds score columns or score text, the stage vocabulary, IDs, decision/overtime/shootout/extras columns, cricket innings columns and the period format.
3. **Takes sport rules from one table** (`SPORT_RULES`):
   - engine: Dixon–Coles for soccer; count models for ice hockey and baseball; joint normal for basketball, Australian rules, American football and both rugby codes; the first-innings ladder for limited-overs cricket;
   - endpoint, extra-time rule, winner bonus and overs cap.
   Basketball's extra-period fraction is read from the competition's own period format (48 or 40 minutes).
4. **Chooses seasons from the competition's own history.**
   - Eligible seasons have at least half the median recent evaluation-game count (minimum 20).
   - The last 3 eligible seasons are test seasons; the 2 before them are tune seasons.
   - The fit window spans three editions: three seasons for a league, about 9–12 years for a quadrennial tournament.
   - Fewer than 4 eligible seasons gives `NOT_MODELLED: insufficient history`.
   - Evaluation uses the regular season where one exists, and all competitive games for tournaments.
5. **Runs an integrity gate on the competition's own rows** (`integrity_warnings`). A blank field is missing data, not a warning.
   - `OVERTIME_FIELD_IMPLAUSIBLE`: an overtime/decision field filled on at least 90% of recent rows (at least 500 games) that shows extra time in under 1% of games. Genuine leagues here show 4–25%; an always-"No" field is the default-value pattern of the fabricated builds quarantined on 2026-10-12.
   - `IMPLAUSIBLE_SCORE_DISPERSION`: a season whose margin SD is below 0.4 × the competition's median.
   - Placeholder rows are removed before any count or fit. A 0–0 final is dropped as `zero_zero_placeholder` except in soccer and ice hockey (genuine results) and in baseball rows that record extra innings (a scoreless tie). Found on 2026-10-14:
     - VFL 2021: 64 rows (the cancelled season);
     - WAFL 2021: 96 rows;
     - MLB 2001: 32 rows;
     - KBO 2008–2014: about 50 a season;
     - AFL 2014: 10 rows.
   - A competition that passes development with a warning becomes `DATA_HOLD`, not `SHADOW_CANDIDATE`, until its rows are verified at the field owner.
6. **Picks comparators.**
   - `BASELINE_LEAGUE_V1` always.
   - TB-1 with the toolkit's validated constants where §4.3 lists the league.
   - Otherwise `CALIBRATED_PREV_EDITION`: the toolkit's arithmetic and the nearest sport's k, with home edge and widths from the competition's previous edition, by replaying TB-1 through it game by game. A first pass with the nearest sport's constants alone was rejected: it made TB-1 *worse than the league-only baseline* in some competitions (Danish Metal Ligaen), which would have made the "beats both comparators" bar easier outside the validated leagues.
   - Cricket is compared with its own C0 and C1.
7. **Runs the same rolling-origin backtest, verdict rule and writers.**
   - Model IDs are `<SPORT CODE>-<COMPETITION>-<ENGINE>-r1`, for example `BKB-NBL-JOINT-r1`, `SOC-PREMIER-LEAGUE-DC-r1` or `CRT20-IPL-FI-r1`.
   - A competition added to the archive later is picked up by the next run with no code change, as long as its sport is in `SPORT_RULES` and its files use recognisable columns.
   - Facts a results file cannot show (franchise renames) go in `OVERRIDES`.

## Current history reporting (21 October 2026)

`python -m ml card-history --out <new-folder>` combines the historical rank log with supported inventories discovered under `research/verification/mini_import_*/`. It reads all numbered Combined Log parts, including parts 8, 10 and later; no import cutoff is hard-coded. Effective settlement inventories take precedence over original-row inventories within one package. Unknown schemas, duplicate effective contracts and overlapping packages require explicit reconciliation.

The output includes `CARD_ROWS.csv`, `CANONICAL_COVERAGE.csv` and `CARD_HISTORY.md`. Coverage and primary scores are separated by probability cohort; research-only analyst values are diagnostic and excluded from primary scores and calibration. Canonical records with no contract rows are shown for review, including legitimate pending/no-forecast records. Original ranks, grades and missing baselines remain literal. This does not infer issuance timing, operator action or prospective eligibility, or rewrite the historical rank log.

The receipt hashes all discovered inventories, mapping files and log parts; missing optional files are marked MISSING. Changed inputs or source during the run reject the report. See [the repair and measured checks](../research/verification/history_reporting_2026-10-21-1/IMPLEMENTATION.md). This reporting code changes the aggregate `ml/` digest; prior model/release receipts keep their original digest and are not regenerated or promoted by this work.

## Layout

| Module | What it does |
|---|---|
| `core/distributions.py` | `ScoreGrid`: one joint score distribution per game; winner, handicap, total and push masses; extra-time resolution; coherent winner reweighting; discrete CRPS |
| `core/metrics.py` | Brier, log loss, half-sum multiclass Brier, reliability bins, Brier decomposition, logistic calibration slope, week-block paired t-intervals (SCORING §5), card-cluster bootstrap |
| `config.py` | Competition discovery, column detection, sport rules, season selection, comparator choice |
| `data/archive.py` | Loads any discovered competition; AFL- and NFL-style score-text parsers checked against the archive's own total and margin columns; hockey OT/SO and baseball extras from whichever columns exist; drops and counts every unusable row |
| `models/gaussian.py` | Joint-normal team ratings (basketball, AFL, NFL, NRL); optional NFL key-number reweighting |
| `models/count.py` | Dixon–Coles / Poisson ratings (EPL, NHL regulation, MLB with negative-binomial dispersion); promoted-team prior |
| `models/baseline.py` | The two comparators: `BASELINE_LEAGUE_V1` (league only) and TB-1 coded exactly as PROBABILITY_TOOLKIT §4 |
| `models/cricket.py` | Limited-overs first-innings ladder C0 → C1 → C2 (+ pre-toss mixture), any T20 or one-day competition |
| `evaluation/backtest.py` | Rolling-origin backtest: weekly refits from earlier games only; tuning on tune seasons only |
| `evaluation/report.py`, `writers.py` | Paired comparisons, development verdict, recalibration experiment, Markdown/CSV writers |
| `evaluation/card_calibration.py` | Calibration audit of the cards' own stated probabilities |
| `decision/` | Firewalled paper study: de-vig (multiplicative, power, Shin), shrunk fractional Kelly, LinTS bandit, full-information learner |
| `shadow/lane.py` | Freeze → commit hash → reveal after start → settle; market-column guard |
| `research_ingest.py` | LEARN-v1 store: deduplicated events, result/statistic revisions, availability snapshots, quarantine, receipts; primary HISTORY bridge |
| `features.py` | FEAT-v1 point-in-time features with true n and missingness; frozen snapshots |
| `training_admission.py` | Immutable, reproducible training releases; candidate linkage; exclusion reasons |
| `models/basketball_features.py` | BKB-FEATURE-RIDGE-C1 challenger and its chronological ablation against the exact V3 experts |
| `evaluation/v3_backtest.py` | V3-equivalent rolling-origin backtest and per-event expert ledger |
| `hedge.py` | Learning-rate, forgetting, ESS-floor, AdaHedge and contextual weighting study; regime alerts |
| `calibration.py` | Chronological calibration study; coherent grid raking |
| `evaluation/prospective.py` | Hash-chained shadow ledger; paired champion/candidate evaluation; dispositions |
| `learning_status.py` | Learning counters and evidence-aware review triggers |
| `registry.py` | Hash-chained model registry with transition rules |

## Rules this code enforces

- **No leakage:** a training row on or after the fit date raises (`decay_weights`).
- **No silent fallback:** a failed fit raises `FitError` and the row is `NOT_ISSUED:FIT_FAILED`. An unseen team gets a labelled prior (`NEW_TEAM_PRIOR`). A Dixon–Coles rho outside the pair's valid domain is clamped and flagged `RHO_CLAMPED`.
- **One distribution per game:** every contract is a function of one `ScoreGrid`; masses are checked to sum to one.
- **Market-free outputs:** `assert_no_market_columns` refuses odds, line or price columns in anything that enters the repository.
- **Hyperparameters on tune seasons only:** a value chosen on a grid boundary has its axis extended and is re-tuned (declared before test results were read).
- **No JSON, pickles or notebooks.**

Primary inference/settlement CLI: `python -m ml primary predict --help` / `python -m ml primary settle --help`. This actually fits/reloads saved distributions and uses delayed sporting feedback; it does not run the staking lab. Source-known-at history, reviewed field/endpoint evidence, actual run receipts and immutable outputs required.

**Mandatory online history:** [HISTORICAL_SOURCE_PROTOCOL](../HISTORICAL_SOURCE_PROTOCOL.md) applies to every sport and competition. Every game history is researched and verified online, regardless of local data, with reviewed web rows usable in the named primary input scope; shared archive maintenance is separate. Source/known-at checks and unsupported-model limits remain.


**Research retention before model availability (RETAIN-v1).** [RESEARCH_RETENTION_PROTOCOL](../RESEARCH_PROTOCOL.md#part-c-research_retention_protocol) supersedes EXEC-v1's model prerequisite for recording/import. Write every identified researched event under its stable local event key and canonically retain it through verified prompt-4 import even if the model/adapter/runtime/module/baseline/calibration/receipt is absent or failed. Use RESEARCH_ONLY_NO_MODEL, explicit execution reason and blank nonexistent artifact paths; keep model p_card NOT_ESTIMATED and supported analyst_p NOT_PRIMARY. Missing ML never by itself blocks the ID or a source-backed settlement. Retain verified settled labels for future model development with source/known-at/revision/feature status; only actual frozen experts can supply Hedge losses. Never invent probabilities, execution, final scores or pregame timing. Identity/custody/write conflicts remain real blockers.


**Model use and mandatory running-log record (current local-key rule).** Use exact-scope model mechanisms when executable and retain a verified attempt. Append every researched card under its stable local event key, update/read back the mini and return its complete updated Markdown. Missing models retain RESEARCH_ONLY_NO_MODEL with the real reason. Canonical P-IDs are assigned only by prompt 4 after duplicate reconciliation; never allocate or reserve one during pregame research. CYCLE-v1 is a separately versioned experimental runtime under FORECAST_CYCLE_PROTOCOL.

See [RETAIN-v1](../RESEARCH_PROTOCOL.md#part-c-research_retention_protocol). This is an editorial clarification of the existing two-path behavior; no model, numerical policy or format change.

## Tennis singles: separate experimental development lane

`python -m ml tennis predict|verify|settle` runs the independently versioned [`TENNIS_EXPERIMENTAL_HEDGE_V1`](TENNIS_EXPERIMENTAL.md) model (`tennis_primary.py`): hierarchical surface-specific serve/return estimates, a chronological Elo expert, exact best-of-3/5 match/game-score distributions, full-information Hedge feedback and source-bound immutable forecast receipts. [`test_tennis_primary.py`](tests/test_tennis_primary.py) contains synthetic unit/integration checks. **This is not certified, has no real-data prospective validation and is not yet part of the `MODEL_ASSISTED_PRIMARY_V3` tennis adapter.** The existing primary tennis `NOT_IMPLEMENTED` disposition remains truthful until separately authorised, validated integration. Do not merge its rows into the primary performance cohort or rewrite past cards.

## LEARN-v1 learning pipeline

[LEARNING_PIPELINE_PROTOCOL](../ML_PIPELINE.md#part-c-learning_pipeline_protocol) (16 October 2026) connects research to learning without changing PRIMARY_HEDGE_MIX_V3. Every command writes a new output or appends to an append-only file, with receipts:

```text
python -m ml ingest add --export RESEARCH_EXPORT/<key> --store research/learning_store [--dry-run]
python -m ml ingest history --store research/learning_store --competition C --endpoint E --horizon ISO --exclude-event ID --out HISTORY.csv
python -m ml features --store research/learning_store --competition C --endpoint E --home H --away A --as-of ISO [--snapshot ...]
python -m ml training build --store research/learning_store --competition C --endpoint E --release-id R --out-root research/training_releases [--candidates research/training_candidates]
python -m ml training verify --release research/training_releases/R
python -m ml bkb-features ablate --release ... --competition-source COMPETITION_SOURCE.csv --tune-start ISO --test-start ISO --out DIR
python -m ml v3-backtest --store research/learning_store --competition-source COMPETITION_SOURCE.csv --eval-start ISO --out DIR
python -m ml hedge-study --ledger DIR/LEDGER.csv --tune-end ISO --out DIR2
python -m ml calibration --predictions PRED.csv --tune-start ISO --tune-end ISO --out DIR
python -m ml prospective freeze|verify|evaluate ...
python -m ml learning-status --store research/learning_store --review-log research/learning_status/REVIEW_LOG.csv [...]
python -m ml registry verify|current|append ...
python -m ml capability [--out CAPABILITY_RECEIPT.csv]
python -m ml baseline --request REQUEST.csv --history HISTORY.csv --contracts CONTRACTS.csv --out BASELINE.csv
python -m ml prospective rows --bundle DIR --kind primary|tennis --role CHAMPION|CANDIDATE --out ROWS.csv
python -m ml card-history --rank-log research/data/GAME_PREDICTION_RANK_LOG.csv --out DIR
python -m ml pregame run --mini MINI.md --game GAME.csv --lines LINES.csv --capture SOURCE.txt --confirm-no-outcome-seen   # prompt 1, after the card
python -m ml pregame status | compare-card --release R.csv --out DIR   # lane progress (8 weeks / 50 games) and card v model
python -m ml.chat pack --out DIR_OUTSIDE_REPO           # CHAT-EXEC-v1 runtime pack for a web-chat sandbox
python -m ml.chat run --game GAME.csv --lines LINES.csv --capture SOURCE.txt --out OUT --confirm-no-outcome-seen
python -m ml.chat accept --attempt UPLOAD.zip --local-key LOCAL-<MINI_KEY>-G0001 [--freeze-basis commit]
```

Tests: `test_learning_store.py` (dedup, quarantine, revisions, interrupted ingest, point-in-time features, reproducible releases), `test_learning_models.py` (challenger coherence and leakage guard, identical-game ablation, Hedge schedules against V3, delayed feedback, V3-equivalent backtest, calibration and grid raking), `test_learning_governance.py` (shadow ledger, paired evaluation and power, registry transitions, review clocks), `test_card_history_tools.py` (sport/family rules, effective-grade precedence, collision detection, Rank-1 tests, capability receipt, baseline equality with V3, shadow adapters), `test_learning_lifecycle.py` (one synthetic competition from duplicate minis through forecast, settlement, feedback, correction, release and counters) and `test_prompt_consistency.py`. All use synthetic EXAMPLE data. They establish mechanics, not predictive quality. No real-data ablation, backtest or study has been run yet.


## Pregame shadow and release scope (22 October 2026)

`ml/pregame.py` runs the cycle in this repository after the analyst card is written (MLSCOPE-v2; MLSCOPE-v3 adds the `reference` subcommand before the card and re-uses its result): it refuses unless the card's markers are in the mini and every `card_p` is printed in the card, records NOT_RUN_NO_RELEASE / NOT_RUN_STALE_RELEASE / NOT_RUN_INPUT_REFUSED honestly, and freezes the model, league baseline and card p_card on identical contract keys. `ml/code_identity.py` defines the release code digest as the import closure of `ml.cycle` and `ml.workflow` (RELEASE-SCOPE-v1), so editing files outside it no longer retires a release; `test_pregame.py` checks the closure against the modules actually loaded. Details: [FORECAST_CYCLE_PROTOCOL](../REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol).

## Connected game workflow (CYCLE-v1)

**Executable forecast cycle (CYCLE-v1).** Apply [FORECAST_CYCLE_PROTOCOL](../REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol). New contextual forecasts use MODEL_ASSISTED_CYCLE_V1 with a frozen exact-competition release, actual execution receipt, identical-contract baseline shadows and verified settlement feedback. Existing V3/tennis adapters retain their own cohorts; missing/unsupported inputs require a real failure receipt and retained research. This statistical/procedure release authorises experimental execution, not predictive qualification.

`python -m ml.workflow research --help` is the stdlib failure-receipt entry point. `python -m ml cycle release|verify|settle|evaluate` connects exact-scope store data, contextual models, delayed sporting feedback and paired prospective evaluation. Older no-real-data and empty-store statements above describe their dated releases; current status is in CURRENT_STATE.

## Reference stage, picks block, ledger, simulators and league lane (22 October 2026, v24.0)

These modules sit outside the release import closure (`ml/code_identity.py`), so adding or editing them does not retire a frozen release; editing a closure file does.

| Command | What it does | Module |
|---|---|---|
| `python -m ml reference tier --competition C` | Tier A/B/C and the declared reference with its evidence (REFERENCE_CHOICE.csv) | `ml/reference.py` |
| `python -m ml reference standings --competition C --cache DIR` | Reads the ESPN standings feed into `STANDINGS.csv` with a receipt | `ml/reference.py` |
| `python -m ml reference width --competition C` | The width floor ladder (competition row, family prior +10%) | `ml/reference.py` |
| `python -m ml reference run --game … --lines … [--standings …] --confirm-no-outcome-seen` | Reference stage for TB-2-MD / TB-1-MD or the league-only baseline; flags such as `TB2_NOT_TESTED_FOR_COMPETITION`, `LM_PRIOR_BLEND` and `KEY_NUMBERS_NOT_MODELLED` | `ml/reference.py` |
| `python -m ml pregame reference …` / `pregame run …` | Reference stage for a release reference, then the card freeze that re-uses the executed reference (MLSCOPE-v3); `compare-card --champion CARD\|TB2` | `ml/pregame.py` |
| `python -m ml card lint --mini M --key K` | Lints the `PICKS_V2` block (mass sums, complements, z consistency, width floors, abstain rule, ceiling 0.90) | `ml/picks.py` |
| `python -m ml ledger add\|verify\|score\|coverage` | Append-only adjustment ledger, λ, paired scoring against every reference, width coverage | `ml/ledger.py` |
| `python -m ml release-gate --competition C` | G1-G6 data-quality gate on the learning store before a release | `ml/releasegate.py` |
| `python -m ml backfill-basketball` | Two-lineage NBA finals backfill into the learning store | `ml/backfill_basketball.py` |
| `python -m ml context-study` | Walk-forward development study of contextual features and the reference forms | `ml/context_study.py` |
| `python -m ml league-day freeze\|settle` | Daily league lane: freeze reference, baseline, release and TB-2-MD rows for every game of a date; settle them from verified finals | `ml/league_day.py` |
| `python -m ml sim <baseball\|tennis\|hockey\|cricket\|props> …` | Simulators with seed, N and Monte Carlo error; NOT_VALIDATED until `structure_check` passes (SIMULATION_PROTOCOL) | `ml/sim/` |

Benchmarks load through `ml/benchmarks.py`, which refuses any price column. Tests: `test_reference.py`, `test_picks_ledger.py`, `test_releasegate.py`, `test_backfill_basketball.py`, `test_context_study.py`, `test_league_day.py`, `test_sim.py` and the additions to `test_pregame.py`.

## Retained unpublished v24.13 additions (11 November 2026)

| Command | What it does | Module |
|---|---|---|
| `python -m ml external event-key\|check\|merge` | Shared event key for research chats; checks a LANE_RETURN block; merges returns into corroborated evidence, conflicts, pooled prices and the chats' access log (EXT-v2) | `ml/external.py` |
| `python -m ml kit verify\|params\|sha` | Re-runs a chat's KIT_RECEIPT with the repository kit; rebuilds the kit's parameter files and fills Part A gaps | `ml/kit/cli.py`, `ml/kit/params.py` |
| (upload to a chat) | The self-contained calculation kit: one engine per sport, receipts (KIT-v1) | `ml/kit/sr_kit.py` |
| `python -m ml bulk-history soccer\|cricket --cache DIR` | Open bulk history (openfootball, Cricsheet) through the checked fetcher; raw bodies stay outside the repository (BULK-v1) | `ml/bulk_history.py` |
| `python -m ml pooled soccer --out DIR` | One recipe per sport, tuned on some competitions and judged on held-out ones (POOLED-v1) | `ml/pooled.py` |
| `python -m ml sim-check baseball\|hockey\|cricket\|tennis --out DIR` | Structural and held-out checks for the simulators (SIM-VALID-v1) | `ml/sim/validate.py` |
| `python -m ml history-pack --competition C --team T --as-of D --out DIR` | A side's dated games and L5/L10/L15/L20/season windows from the history the repository holds (PACK-v1) | `ml/history_pack.py` |
| `python -m ml source-audit --url U --reader R`, `--lists DIR`, `--sport-slices DIR` | Per-reader access (SRC-ALT-v3), the weekly reader lists and the chats' per-sport source files | `ml/source_audit.py` |

Changed: `ml/reference.py` (LEAGUE-KEY-v2: a league name selects constants only inside its own sport; OT-PERIODS-v1: basketball overtime as real extra periods, flag `OT_PERIODS_V1` on every receipt), `ml/core/distributions.py` (`ScoreGrid.resolve_ties_periods`), `ml/picks.py` (`rank_scope`, `event_key`, `external_runs`, `external_disagreement`), `ml/learning_log.py` (LINEUP-CAPTURE-v1: availability rows for both sides). None of these files is in the forecast cycle's import closure, so no release is retired. Tests: `ml/tests/test_release_v24_13.py`.


## Retained v24.14 external-lane integrity commands

`python -m ml external package-check` validates the legacy upload package (`init`/`packet`/`intake`/`status`/`review-source`/`admit`/`append-card`/`bind-card`/`evaluate`). See [EXTERNAL_RESEARCH_PROTOCOL.md](../EXTERNAL_RESEARCH_PROTOCOL.md) and [research/verification/framework_change_2026-11-11-2/IMPLEMENTATION.md](../research/verification/framework_change_2026-11-11-2/IMPLEMENTATION.md). Takes no new game under ONE-CHAT-v3.

## One chat per game, deep loss register, versions (v25.0)

```text
python -m ml one-chat intake --drop FOLDER --out research/one_chat/intake/<run>      read the ONECHAT_V1 blocks of an owner drop
python -m ml one-chat score --intake research/one_chat/intake/* --outcomes OUTCOMES.csv [...] --out research/one_chat/scores/<run> [--on-request | --cohort COHORT.csv]
python -m ml one-chat template --sport Basketball                                    an empty block with the sport's FACTS rows
python -m ml deep-loss check | tally                                                 the deep loss register and its pattern tally
python -m ml learning-status ... --card-rows research/card_training/<run>/ROWS.csv   review clocks counted on card games
python -m ml state --restamp                                                         print VERSIONS.csv into the prompts and CORE
```

## Sealing and the anytime verdict (v26.0)

```text
python -m ml one-chat seal --card FILE [FILE ...] [--no-push]    commit and push card files before play; records GitHub's push time
python -m ml one-chat receipts                                   refresh GitHub push times into research/one_chat/sealed/PUSH_RECEIPTS.csv
python -m ml one-chat score ... [--captures DIR]                 committed inputs only; prints the verdict, e-value and lower bound
python -m ml one-chat history --rows ROWS.csv --out DIR          the same test on historical cards (context only)
```
