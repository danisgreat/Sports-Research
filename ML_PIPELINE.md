# ML pipeline: workshop models, execution and the learning pipeline

**Consolidated 2026-11-07, CR-2026.11.07-R3.** The primary-prediction, ML-execution and learning-pipeline protocols were joined verbatim on 2026-11-07 (R2) and then rewritten (R3): contradictions with MLSCOPE-v3 and the v24 prompts are resolved, repetition is removed, and part and section numbers are unchanged. What changed and why: [consolidation report](research/verification/framework_change_2026-11-07-3/CONTRADICTIONS.md). Verbatim originals: [archive/consolidation_2026-11-07/merged_sources/](archive/consolidation_2026-11-07/merged_sources/). Versions in force: [CURRENT_STATE](CURRENT_STATE.md).

**How models reach a card today.** Only as the competition's declared reference (or challenger), frozen before the card, under MLSCOPE-v3 as defined in [REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol) (merged forecast-cycle section) and summarised in [CORE](CORE.md) §7. The card's p is ANALYST_PRIMARY_V1, the reference plus logged adjustments ([ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md)). Everything below serves that lane, the studies of prompts 6 and 8, or the legacy cohorts.

---

# Part A: PRIMARY_PREDICTION_PROTOCOL

*PRIMARY-2026.10.16-v3.3. **Status today: a historical cohort and a workshop tool.** Between 15 and 17 October 2026 the owner authorised experimental primary use of this runtime on cards (MODEL_ASSISTED_PRIMARY_V3 / PRIMARY_HEDGE_MIX_V3 / EXPERIMENTAL_PRIMARY_NOT_CERTIFIED; [review](research/verification/framework_change_2026-10-15-4/REVIEW.md)). MLSCOPE-v1 (17 October) ended model use in game cards, and MLSCOPE-v3 (22 October) lets models reach cards only as the frozen reference. New cards therefore never copy this runtime's PREDICTIONS.csv; MODEL_ASSISTED_PRIMARY_V3 cards keep their method and cohort, their bundles are settled with `primary settle`, and prompts 6 and 8 use the runtime for studies and baselines. PRIMARY_HEDGE_MIX_V3, its three experts, selection and scoring are unchanged.*

## Mandatory execution and log coverage

A MODEL_ASSISTED_PRIMARY_V3 forecast exists only with a verified successful bundle (`primary execute --out ATTEMPT`, bundle `ATTEMPT/BUNDLE`). Research-only cards need no executable, model or receipt; no model probability or expert loss is ever invented.

## 1. What produces a primary forecast

The [runtime](ml/primary.py) fits two exact-competition team-rating experts (90- and 365-day decay) and a separate league-only comparator, and combines their full score grids with full-information exponential weights (Hedge) into one coherent distribution. This is supervised sporting ML plus online expert aggregation, not an environment-control RL agent (no PPO or DQN), and there is no random expert draw. Brier convexity favours a mixture over a random draw with identical weights; it does not guarantee that Hedge beats another adaptive policy or a single expert, and no predictive qualification follows from it.

## 2. Horizon and input contract

The evidence horizon is the earliest of the game-log `scheduled_start`, the actual `issue_at` and a verified `actual_start`, all with zones; there is no separate `cutoff` column and no forced advance freeze ([RESEARCH_PROTOCOL](RESEARCH_PROTOCOL.md#part-e-timing_research_protocol) Part E). An unknown actual start is TIMING_UNVERIFIED; a declared issue time or generated receipt is not proof of publication or outcome blindness.

```text
python -m ml primary predict --request REQUEST.csv --history HISTORY.csv --contracts CONTRACTS.csv --out <new folder>
python -m ml primary predict --request REQUEST.csv --history HISTORY.csv --contracts CONTRACTS.csv --feedback EFFECTIVE_FEEDBACK.csv --out <new folder>
python -m ml primary settle --bundle <bundle> --home-score HOME --away-score AWAY --final-at ISO --available-at ISO --evidence CAPTURE --evidence-sha256 SHA256 --out NEW_FEEDBACK.csv
```

- **REQUEST.csv:** one row, `event_id,competition,home,away,scheduled_start,issue_at,actual_start,endpoint,outcome_exposure,candidate_recipe`, optional `venue`. Competition matches a reviewed COMPETITION_SOURCE.csv row. `outcome_exposure=NONE_RECORDED` is an operator declaration; live or final exposure blocks this lane. No odds, market or staking fields.
- **HISTORY.csv:** `event_id,competition,endpoint,date,final_at,available_at,status,admission,source_url,evidence_path,evidence_sha256,season,home,away,hs,as_,reg_hs,reg_as,decision`, optional `stage` and `source_kind` (ARCHIVE_REVIEWED, WEB_RECOVERED or WEB_CORRECTED; required with `--competition-source`). Stable event IDs (aliases reconciled first); no target, duplicate, non-terminal, wrong-scope or malformed rows; `status=FINAL`, `admission=RESEARCH_INPUT_REVIEWED`; date ≤ final ≤ available ≤ horizon, with the game date strictly before the horizon's UTC day; captures exist and match their hashes. Custody does not prove source truth; a late correction is known from its availability, not its game date. Cricket adds `bat,bowl,venue,runs,legal_balls,wickets` (home = batting side, only full-length or all-out first innings; no invented chase, powerplay, second-innings or match-winner model).
- **CONTRACTS.csv:** `contract_key,family,side,line,endpoint,definition,action`. Families winner, handicap and total with exact HOME/AWAY/DRAW or OVER/UNDER orientation; winner action THREE_WAY_DRAW_LOSES or DRAW_PUSH, other families STANDARD_COMPLETED. FROZEN_FRAMEWORK_CONVENTION is a sporting action, not verified operator settlement. p > 0.90 stays diagnostic, never clipped; the baseline is the league-only grid on identical contracts; CLI success is never an automatic family or selection pass.

## 3. Point-in-time learning and parameter admission

Warm start uses the last 30 game-weeks of admitted history; each simulated Monday refit uses only games whose final and source availability were known by that Monday, needs at least 30 earlier games, and excludes unseen teams, failed fits and flagged grids. WARM_START.csv keeps each scored event, its refit and availability time, the league line and the three losses; no admitted events means uniform weights.

Verified bundle feedback supplies full-information expert losses after final and availability: home-win Brier and over-the-frozen-league-line Brier, averaged (cricket: the total question only). Feedback takes precedence over an overlapping warm event, one learning contribution per event; conflicting scores or orientation block the dependent forecast; duplicate feedback is never last-row-wins.

Weights ∝ exp(−η·(cumulative loss − minimum loss)) by policy, competition and endpoint. **η = 2 is provisional, not tuned or validated for V3.** An override needs one admitted row in `research/primary_policy/ETA_ADMISSION.csv` (`competition,policy,eta,tune_end,frozen_at,evidence_path,evidence_sha256`; tune_end ≤ frozen_at ≤ horizon; matching evidence); none has been admitted. A CSV label or hash is not qualification.

## 4. Immutable bundles and settlement

Each event or revision writes a new folder with FORECAST.md, PREDICTIONS.csv, GRIDS.csv (the three expert distributions), FORMS.csv, HISTORY.csv, CONTRACTS.csv, REQUEST.csv, FEEDBACK_INPUT.csv, MODEL_CONFIG.csv, WARM_START.csv, FEEDBACK_LOSSES.csv, ETA_ADMISSION.csv and RECEIPT.csv (policy, model, competition, endpoint, horizon, issue and generated times, weights and losses, η source, counts, input, config, output and code hashes, library versions, HEAD). Verification rehashes every artifact, recomputes the weights and re-mixes the saved grids, checks the masses and the same-row baseline, and binds identity and horizon to the request; no folder is overwritten. V2 bundles are still readable and settled under their own policy.

Settle the exact original keys first from official terminal fields and frozen definitions; `primary settle` then verifies the bundle and evidence and writes a new feedback row (non-integer, negative or non-finite scores are rejected). Re-score every expert from frozen grids; reconcile one effective revision chain before any future learning. No pending, future, target-event or counterfactual label enters the weights.

## 5. Scope, prediction evidence and honest failure

Supported configurations: joint-normal points, Dixon–Coles soccer regulation, count models for baseball and hockey, and limited-overs cricket full first innings; fit regulation before adding extras once. A DATA_HOLD configuration, unsupported engine, unknown participant or failed fit blocks numeric use; a major league's parameters are never transferred to an obscure one. Tennis, field hockey, multi-day cricket and phase or player markets have no adapter here. Fitted features are team identity, prior scores and time decay only; lineups, injuries, tactics and weather are researched but not fitted.

The preserved 41,752-game replay (better mean home-win Brier than random Exp3) used different history, state and feedback, included DATA_HOLD leagues and pooled competition-weeks as separate clusters: it is **historical proxy evidence**, not a test of this runtime. Passing tests establishes mechanics only; prospective calibration, incremental advantage and production readiness are unproven. No odds, stakes, returns, CLV, fantasy, market moves or decision-lab inputs enter any model, loss or rank.

## 6. Mandatory online historical research (HIST-v2)

[HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) requires online prior-game verification for every competition; reviewed web rows can train the runtime without an archive refresh. `primary predict --competition-source COMPETITION_SOURCE.csv` accepts one reviewed exact-scope metadata row in place of a discovered archive configuration; every history row then states its `source_kind`, and the metadata must match the request, a supported configuration and evidence known by the horizon. This releases no old DATA_HOLD data. Research is done by the operator, not by an unattended scraper.

## 7. Relation to the learning pipeline (LEARN-v1)

Part C adds data, study and evidence layers around this runtime without changing it. HISTORY.csv may be generated from the reviewed learning store at a horizon (`python -m ml ingest history`), with §2's admission gates applying to every row. `python -m ml v3-backtest` reuses the runtime's fitting, warm-start and feedback functions as historical evidence. Hedge schedules, the basketball challenger and calibrators are studies (Part C §6).

---

# Part B: ML_EXECUTION_PROTOCOL

*EXEC-2026.10.16-v2, now applying to legacy and workshop runs only. For cards, the reference stage and the pregame freeze (MLSCOPE-v3, above) replace the "attempt a primary run" step, and new minis have no execution manifest (prompts 2 and 3). [RESEARCH_PROTOCOL](RESEARCH_PROTOCOL.md#part-c-research_retention_protocol) Part C controls recording and import independently of any model.*

## 1. Execute when available, retain regardless

A missing adapter, module, interpreter, dependency, history, baseline, calibration or receipt never blocks a local-key record or its later import. A card records its pregame freeze disposition (EXECUTED, NOT_RUN_NO_RELEASE, NOT_RUN_STALE_RELEASE, NOT_RUN_INPUT_REFUSED or FAILED; R36); a workshop or legacy run records its actual failure or NOT_RUN_CAPABILITY_BLOCKED / NOT_IMPLEMENTED / NOT_RUN_DATA_UNAVAILABLE. Never invent a run or a file to pass a check.

```text
python -m ml primary execute --request REQUEST.csv --history HISTORY.csv --contracts CONTRACTS.csv --out ATTEMPT
python -m ml primary verify-execution --attempt ATTEMPT
python -m ml primary verify-log --mini MINI.md [--manifest ML_EXECUTION_MANIFEST.csv]
```

An execute attempt keeps STARTED, INPUTS and EXECUTION and, on success, BUNDLE; a failed attempt exits non-zero, and an interrupted one is never claimed successful.

## 2. Honest manifest for each new card

*Legacy minis only.* A mini that already carries `ML_EXECUTION_MANIFEST.csv` keeps its registered header and one row per card:

```csv
card_id,event_id,competition,endpoint,execution_path,execution_sha256,feedback_status,feedback_path,feedback_sha256,reason
```

With no bundle, execution and feedback paths and hashes are blank, `feedback_status=NOT_APPLICABLE_NO_MODEL`, and the reason is concrete; a stated path must verify. MODEL_ASSISTED_PRIMARY_V3 requires actual successful execution. New mini-log-10 minis have no manifest: their model rows keep their own receipts.

## 3. Settle every event and retain future targets

Settle the original contracts under the original local key (or the mapped P-ID after prompt 4) with source, time, definition and revision evidence, whether or not a model existed. Verified terminal labels and research are kept locally and exported with `ml.research_learning` after prompt 4 has verified the canonical mapping (RESEARCH_PROTOCOL Part C §4).

Only a frozen model row or bundle supplies its own losses: `cycle settle` for cycle and pregame rows, `league-day settle` for league-day bundles, `primary settle` for legacy V3 bundles. Without one, NOT_APPLICABLE_NO_MODEL applies to expert losses only; the event stays eligible for label retention. Never backfill predictions, losses, propensities or rewards; candidate targets never enter feedback directly. Research IDs, source truth, forecasting, training admission and prospective qualification stay separate.

---

# Part C: LEARNING_PIPELINE_PROTOCOL

*LEARN-2026.10.16-v1.1, with the v24 reference lane (§11). Owner instruction, 16 October 2026: every researched and settled game becomes reusable, point-in-time-safe learning data, and model changes depend on chronological and prospective evidence. Nothing here qualifies a model, changes an issued card, probability, rank, grade, ID or feedback row, or admits market data. Code: [ml/](ml/README.md#learn-v1-learning-pipeline). Implementation: [framework_change_2026-10-16-6](research/verification/framework_change_2026-10-16-6/IMPLEMENTATION.md).*

## 1. Four auditable layers

| Layer | What it holds | Where | Tool |
|---|---|---|---|
| Research data | Every prior-game row, team statistic and availability snapshot actually opened, with source, known-at time and capture hash | `RESEARCH_EXPORT/` folders built by prompt 6, then the append-only store `research/learning_store/` | `python -m ml ingest` |
| Predictive models | Cycle releases (NBA-CYCLE-1, NHL, MLB), the TB-2-MD standings reference, the legacy V3 runtime and development challengers such as BKB-FEATURE-RIDGE-C1 | `ml/`, `research/cycle_releases/`; [MODEL_REGISTRY](research/model_registry/MODEL_REGISTRY.csv) | `python -m ml registry` |
| Online model selection | V3 Hedge; schedule, forgetting and context studies | Backtest and study folders with receipts | `python -m ml v3-backtest`, `python -m ml hedge-study` |
| Prospective evaluation | Frozen pre-start shadow and reference rows, paired champion and candidate scoring, review dispositions | `research/prospective/SHADOW_LEDGER.csv`, `research/learning_status/REVIEW_LOG.csv` | `python -m ml prospective`, `python -m ml learning-status` |

The mini-log and canonical-log workflow is the evidence backbone; the store never replaces an original card or settlement.

## 2. Structured research export (prompt 1)

*Who writes it: prompt 1 records its research rows as Markdown tables in the card (the learning record); after import, prompt 6 transcribes them into the export columns below and ingests them (prompt 6 step 1).* Use the exact column sets; an extra column (including any odds, price or market field) makes a file inadmissible. Every row carries `source_url` (HTTPS), `known_at` (the earliest time the value was demonstrably public, with zone), `retrieved_at`, `capture_path` and `capture_sha256` (captures stay outside the repository).

- `GAME_OBSERVATIONS.csv`: one row per prior game per opened source: `competition,endpoint,native_event_id,season,event_at,home,away,venue,status,hs,as_,reg_hs,reg_as,decision,final_at,source_url,source_kind,published_at,retrieved_at,known_at,capture_path,capture_sha256,review_status,collected_by`. Status FINAL, ABANDONED, FORFEIT, AWARDED, POSTPONED or CANCELLED (integer scores for FINAL); source_kind WEB_RECOVERED or WEB_CORRECTED; review_status RESEARCH_INPUT_REVIEWED once checked, otherwise quarantined.
- `TARGET_EVENT.csv`: `competition,endpoint,native_event_id,season,scheduled_start,home,away,venue,source_url,known_at,capture_path,capture_sha256,collected_by`.
- `AVAILABILITY.csv`: dated snapshots: `competition,native_event_id,team,player,role,status,confirmation,published_at,retrieved_at,known_at,source_url,capture_path,capture_sha256,review_status,collected_by`. Role STARTER, BENCH, NOT_IN_SQUAD or UNKNOWN; status CONFIRMED_ACTIVE, CONFIRMED_OUT, DOUBTFUL, QUESTIONABLE, PROBABLE, PROJECTED or UNKNOWN; confirmation OFFICIAL_CONFIRMED, REPORTED or PROJECTED. A row without a publication time is quarantined; a post-game box score never shows that a lineup was known before the game.
- `TEAM_GAME_STATS.csv` (where a box score was opened), long format: `competition,native_event_id,team,stat,value,source_url,source_kind,published_at,retrieved_at,known_at,capture_path,capture_sha256,review_status,collected_by`. Basketball: `POSSESSIONS`, or `FGA`, `ORB`, `TOV`, `FTA` with possessions derived and labelled DERIVED.

Validate with `python -m ml ingest add --export <folder> --store <copy of the store> --dry-run` and record the quarantine count. The export records research already done and never changes a card; if it cannot be built, record `LEARN_EXPORT_NOT_WRITTEN` with the reason.

## 3. The learning store (prompt 6 ingests; others dry-run only)

`research/learning_store/` is append-only CSV: EVENTS, EVENT_ALIASES, RESULTS (revisions), TEAM_GAME_STATS (revisions), PLAYER_AVAILABILITY (snapshots), SOURCE_OBSERVATIONS, QUARANTINE, FEATURE_SNAPSHOTS and INGEST_RECEIPTS. **Only prompt 6, or an authorised prompt 8 change, ingests into the shared store** (prompt 4 imports cards but never ingests: prompt 4 §"Import does not ingest"), so concurrent minis never race on it.

- **One event, many observations.** Identity is the competition plus native event ID (otherwise a date and participant surrogate, with a later native ID as an alias). The same match researched in five minis is one training game with up to five observations; re-running an ingest adds nothing.
- **Conflicts are quarantined, never last-row-wins.** A disagreeing score, swapped orientation, endpoint mismatch, unreviewed row, retired-store source, failed hash or impossible chronology goes to QUARANTINE with its reason; only a later reviewed `WEB_CORRECTED` observation creates a new result revision.
- **Point-in-time.** A revision's availability is the earliest `known_at` of its supporting observations; a view "as of" an instant uses only what was known by then and games from an earlier UTC day (tested).
- **Atomic receipts.** INGEST_RECEIPTS is written last; rows of an interrupted ingest stay invisible and its sequence number is never reused.
- **Bridges.** `python -m ml ingest history --store … --competition … --endpoint … --horizon <scheduled start> --exclude-event <target>` writes V3 HISTORY.csv rows that pass admission. Verified finals also feed the cycle releases, TB-2-MD and the parameter tables (§11). The retired results store is not a source.

## 4. Point-in-time features (FEAT-2026.10.16-v1)

`python -m ml features` builds for each side: L5/L10/L15/L20 points for, against and net with true n; possessions-based ratings and pace where every game in the window has sourced possessions; decayed form (half-life 8 games); opponent-adjusted L10 net; season baseline; venue split; rest days; confirmed starters, absences and a lineup-confirmed flag from availability published by the horizon; league scoring context. Every feature carries `__n` and `__missing`; missing stays missing (no league-average fill, no "all available"). A forecast's snapshot is frozen once in FEATURE_SNAPSHOTS.csv with the store view and digest.

## 5. Training admission and immutable releases

`python -m ml training build --store … --competition … --endpoint … --release-id … --out-root research/training_releases [--candidates research/training_candidates]` admits one row per FINAL event (label: the effective reviewed result in the recorded store view; features as of the event's own start) or records its exclusion: NO_REVIEWED_RESULT, NOT_FINAL, OPEN_QUARANTINE, INSUFFICIENT_HISTORY, or CANDIDATE_WITHOUT_STRUCTURED_HISTORY. The manifest fixes the store view, digest, feature specification, code hash and file hashes; `training verify` must rebuild identical bytes. A correction makes a new release; releases are never overwritten. A release is training data, not a model or a predictive claim.

## 6. Models, studies and what each may claim

- **Basketball challenger BKB-FEATURE-RIDGE-C1** (`python -m ml bkb-features ablate`): regularised regression of regulation points on FEAT-v1 features, with residual covariance giving one joint grid and an optional heavy-tail mixture; feature sets tuned on a tune window only and scored with the V3 experts on identical later games, weekly refits from rows known by each Monday; Brier, log loss, margin and total CRPS, 50/80/95% coverage, MAE and paired week intervals. NBA, NBL and EuroLeague stay separate releases without held-out evidence that pooling helps.
- **V3-equivalent backtest** (`python -m ml v3-backtest`): every evaluation event issued at its own start with the runtime's fitting, warm start and delayed feedback at the provisional η; evidence class HISTORICAL_V3_EQUIVALENT_BACKTEST_NOT_PROSPECTIVE.
- **Hedge study** (`python -m ml hedge-study`): fixed η, AdaHedge, discounted Hedge, season reset, ESS floors and shrunk contextual weighting, selected on the tune window and evaluated afterwards against η = 2, with weight-collapse diagnostics and Page–Hinkley alerts; a composite loss only with weights fixed in advance.
- **Calibration study** (`python -m ml calibration`): identity, prior-shrunk Platt, isotonic (≥ 200 rows) and competition-shrunk Platt, fitted on earlier predictions with known outcomes, selected later and evaluated after; grid recalibration keeps every contract a projection of one distribution. Status CALIBRATION_STUDY: nothing is applied to cards.
- **Full reinforcement learning** is out of scope: forecasting does not control the outcome. A sequential-decision study would need its own state, action, reward, budget and logged behaviour policy, behind the market firewall.

## 7. Prospective shadows, review levels and dispositions

**Shadow freeze.** `python -m ml prospective freeze` (and the pregame and league-day commands) append rows to the hash-chained SHADOW_LEDGER before the scheduled start: model, version, release, parameters, code hash, exact contract and probability. PRE_START_VERIFIED requires issue and freeze before the start, and the ledger must be committed before the start to claim publication. Shadow rows never appear on cards and consume no P-ID.

**Evaluation.** `python -m ml prospective evaluate` compares identical settled pre-start contracts only, averaged within event, then week, with a t-interval over weeks: Brier, log loss, calibration slope and intercept, rank-1 accuracy, Hit@2, NDCG@2 and coverage. A preregistered minimum effect gives the weeks needed at 80% power; a result that cannot resolve it is INSUFFICIENT_EVIDENCE.

**Review levels** (workflow triggers, not sample-size guarantees):

| Level | Trigger | Prompt | May conclude |
|---|---|---|---|
| Mini settlement | Each mini (about 40–50 games) | 3 | Outcomes, labels, feedback, data integrity, preliminary diagnostics; no superiority claim |
| Interim combined review | About 100 newly settled unique games (`INTERIM`) | 6 | Coverage, calibration warnings, failures, baselines; defects and controlled experiments |
| Comprehensive retrospective | About 300 newly settled unique games (`COMPREHENSIVE`) | 6 | All sports; per-sport eligibility; backtest, Hedge, calibration, challenger and shadow evidence; dispositions |
| Sport / competition clock | 100 per sport, 50 per competition (`SPORT`, `COMPETITION`) | 6 | That scope's model decision |

`python -m ml learning-status` derives the counters from verified artifacts (unique settled games, admissible games, frozen model forecasts, Hedge feedback games, prospective evaluation games, games since the last review). A material software defect, a source-quality failure or a sustained deterioration in `ALERTS.csv` makes the scope EARLY_REVIEW. Each review appends exactly one disposition per scope to REVIEW_LOG.csv: NO_CHANGE, DATA_REPAIR_REQUIRED, EXPERIMENTAL_RETRAIN, CALIBRATION_STUDY, PROSPECTIVE_SHADOW, PROMOTION_ELIGIBLE or INSUFFICIENT_EVIDENCE. Reaching a count never promotes a model.

## 8. Registry, promotion and rollback

[MODEL_REGISTRY.csv](research/model_registry/MODEL_REGISTRY.csv) is append-only and hash-chained. Statuses: RESEARCH_ONLY_NO_MODEL, DEVELOPMENT_EXPERIMENT, HISTORICAL_BACKTEST, PROSPECTIVE_SHADOW, AUTHORISED_EXPERIMENTAL_PRIMARY, PROSPECTIVELY_QUALIFIED, RETIRED, ROLLED_BACK. PROSPECTIVELY_QUALIFIED requires an earlier PROSPECTIVE_SHADOW entry for the same version, a prospective report with disposition PROMOTION_ELIGIBLE and an owner authority reference. A retired version cannot be reactivated; a rollback names the restored version. The order for any change to what reaches cards: admitted release → chronological ablation or backtest → calibration study → preregistered prospective shadow → PROMOTION_ELIGIBLE → owner decision → registry entry → a prompt-8 change to the declared reference (`research/competition_parameters/REFERENCE_CHOICE.csv` and REFERENCE_MODEL_PROTOCOL), at a season boundary or as a new lane (STATFREEZE-v1). No registry row changes an issued card or grade.

## 9. Deliberately not done here

- **Continuous integration and branch protection.** Workflow files are prohibited (CONTRIBUTING); a narrowly scoped `.github/workflows/` file, external CI or branch protection are owner decisions. Until then, run `python -m pytest ml/tests` before every ML publication.
- **Player impact ratings and roster continuity.** They need player-level game statistics that the store does not yet ingest; availability enters only as confirmed counts and flags (and on cards as ledger rows).
- **Contextual bandits, deep networks and pooled cross-league ratings.** Not built; §6 states the conditions for studying them.
- **Real-data coverage.** The tools were first exercised on synthetic EXAMPLE data. Real runs now exist for the NBA backfill (2023-24 to 2025-26, §11) and the NBA and NHL development studies of 22 October; every other competition's ablations, backtests and studies start only once its reviewed exports are ingested, each with its own receipt.

## 10. Runtime capability, standalone baseline, shadow adapters and card history (v1.1, 16 October 2026)

Added after the [full-history retrospective](research/verification/retrospective_2026-10-16-full/RETROSPECTIVE_REPORT.md), which found that no fitted model priced any of 599 cards and only four events had a frozen same-row baseline:

- `python -m ml capability [--out CAPABILITY_RECEIPT.csv]`: the runtime receipt (Python, pinned libraries, checkout root, HEAD, code hash) kept with any NOT_RUN disposition.
- `python -m ml baseline --request … --history … --contracts … [--competition-source …] --out BASELINE.csv`: BASELINE_LEAGUE_V1 on a card's exact contracts from reviewed history, identical to V3's league expert (tested); a comparator, never p_card.
- `python -m ml prospective rows --bundle … --kind primary|tennis --role CHAMPION|CANDIDATE --out ROWS.csv`: converts a verified V3 or tennis bundle into shadow-ledger rows (PRE_START_VERIFIED only when issued and converted before the start).
- `python -m ml card-history --rank-log research/data/GAME_PREDICTION_RANK_LOG.csv --out …`: the reproducible full-history card table for prompt 6.

## 11. Reference lane and adjustment ledger (v24.0, 22 October 2026)

Verified finals feed (a) the cycle releases, (b) the TB-2-MD standings reference and (c) the width and effect tables ([PARAMETERS](PARAMETERS.md#part-a-competition_parameters) Parts A and B). A competition needs two agreeing lineages and a passing `python -m ml release-gate` before a release is frozen. A historical fact captured now is known now, never on its game date, so no context feature is fitted on history without a known-at time. The 2023-24 to 2025-26 NBA backfill (3,693 finals) was the first lane built this way; its release NBA-CYCLE-1 is experimental, with 0 settled prospective events at its release. The adjustment ledger ([ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md)) is a separate append-only record of the analyst's departures from the reference; it feeds prompt 6's λ, never the store's training rows, until a prompt-8 decision says otherwise.
