**ML/RL scope (MLSCOPE-v2).** Owner instruction, 22 October 2026: models run where they are needed, beside the analyst card and never inside it. Prompt 1 researches the game online and prices every p_card as ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY from one declared distribution ([PROBABILITY_TOOLKIT](PROBABILITY_TOOLKIT.md); code may do the arithmetic, with every input and step printed). Only after the card is written to the mini does prompt 1 run the pregame model shadow, which freezes the model and league-baseline rows, and the card's own p_card, on the same contracts when the competition has an active release, or records NOT_RUN_NO_RELEASE. Model output never changes a card's p_card, ranks or picks. Prompt 3 settles the shadow with the card; prompt 6 ingests and evaluates; prompt 8 builds releases and decides promotion. A model is judged only after at least 8 weeks and 50 paired games; a progress review falls due when either is reached first. RL has no forecasting role: online expert weighting updates at settlement. Details: [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md). Supersedes MLSCOPE-v1, NOCODE-v1 and any older text that forbids code or models in prompts 1–5.

#**Executable forecast cycle (CYCLE-v1).** Apply [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md). New contextual forecasts use MODEL_ASSISTED_CYCLE_V1 with a frozen exact-competition release, actual execution receipt, identical-contract baseline shadows and verified settlement feedback. Existing V3/tennis adapters retain their own cohorts; missing/unsupported inputs require a real failure receipt and retained research. This statistical/procedure release authorises experimental execution, not predictive qualification.

 Learning pipeline: research → store → features → releases → models → prospective evidence

**LEARN-2026.10.16-v1.1 · MDS-2026.10.16-v20.0 · CR-2026.10.16-R7 · P-2026.10.16-v20.0.** Owner instruction, 16 October 2026: implement the necessary and better parts of the external improvement review so that every researched and settled game becomes reusable, point-in-time-safe learning data, and model changes depend on chronological and prospective evidence rather than on the arrival of new games. PROCEDURE + workshop code. **PRIMARY_HEDGE_MIX_V3, its η, experts, selection and scoring are unchanged.** Nothing here qualifies a model, changes an issued card, probability, rank, grade, ID or feedback row, or admits market data.

Read with [PRIMARY_PREDICTION_PROTOCOL](PRIMARY_PREDICTION_PROTOCOL.md), [RESEARCH_RETENTION_PROTOCOL](RESEARCH_RETENTION_PROTOCOL.md), [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md), [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md) and [SCORING_AND_VALIDATION](SCORING_AND_VALIDATION.md). Code: [ml/](ml/README.md#learn-v1-learning-pipeline). Implementation record: [framework_change_2026-10-16-6](research/verification/framework_change_2026-10-16-6/IMPLEMENTATION.md).

## 1. Four auditable layers

| Layer | What it holds | Where | Tool |
|---|---|---|---|
| Research data | Every prior-game row, team statistic and availability snapshot actually opened, with source, known-at time and capture hash | per-card `RESEARCH_EXPORT/`, then the append-only store `research/learning_store/` | `python -m ml ingest` |
| Predictive models | V3 primary (unchanged); development challengers such as BKB-FEATURE-RIDGE-C1 | `ml/`; [MODEL_REGISTRY](research/model_registry/MODEL_REGISTRY.csv) | `python -m ml registry` |
| Online model selection | V3 Hedge; schedule/forgetting/context studies | backtest and study folders with receipts | `python -m ml v3-backtest`, `python -m ml hedge-study` |
| Prospective evaluation | Frozen pre-start shadow forecasts, paired champion/candidate scoring, review dispositions | `research/prospective/SHADOW_LEDGER.csv`, `research/learning_status/REVIEW_LOG.csv` | `python -m ml prospective`, `python -m ml learning-status` |

The mini-log and canonical-log workflow remains the evidence backbone. The store never replaces an original card or settlement.

## 2. Structured research export (prompt 1)

Alongside every new card, write `RESEARCH_EXPORT/<local event key>/` in the mini's evidence scope. Use the exact column sets below; an extra column (including any odds, price or market field) makes the file inadmissible. Every row carries `source_url` (HTTPS), `known_at` (the earliest time the value was demonstrably public, zone required), `retrieved_at`, `capture_path` and `capture_sha256` of the preserved capture. Captures stay outside the repository (CONTRIBUTING); their path and hash are recorded.

- `GAME_OBSERVATIONS.csv` — one row per prior game per opened source, for both sides' L5/L10/L15/L20 and any other history used: `competition,endpoint,native_event_id,season,event_at,home,away,venue,status,hs,as_,reg_hs,reg_as,decision,final_at,source_url,source_kind,published_at,retrieved_at,known_at,capture_path,capture_sha256,review_status,collected_by`. `status` FINAL / ABANDONED / FORFEIT / AWARDED / POSTPONED / CANCELLED; scores are integers for FINAL. `source_kind` WEB_RECOVERED, or WEB_CORRECTED for a reviewed correction. `review_status` RESEARCH_INPUT_REVIEWED once fields were checked; anything else is quarantined until reviewed.
- `TARGET_EVENT.csv` — the event being forecast: `competition,endpoint,native_event_id,season,scheduled_start,home,away,venue,source_url,known_at,capture_path,capture_sha256,collected_by`.
- `AVAILABILITY.csv` — dated snapshots for the target event: `competition,native_event_id,team,player,role,status,confirmation,published_at,retrieved_at,known_at,source_url,capture_path,capture_sha256,review_status,collected_by`. Role STARTER / BENCH / NOT_IN_SQUAD / UNKNOWN; status CONFIRMED_ACTIVE / CONFIRMED_OUT / DOUBTFUL / QUESTIONABLE / PROBABLE / PROJECTED / UNKNOWN; confirmation OFFICIAL_CONFIRMED / REPORTED / PROJECTED. A row without a publication time cannot be dated and is quarantined. A post-game box score is never evidence that a lineup was known before the game.
- `TEAM_GAME_STATS.csv` (where a box score was opened) — long format `competition,native_event_id,team,stat,value,source_url,source_kind,published_at,retrieved_at,known_at,capture_path,capture_sha256,review_status,collected_by`. Basketball: `POSSESSIONS`, or `FGA`, `ORB`, `TOV`, `FTA` from which possessions are derived and labelled DERIVED.

Validate with `python -m ml ingest add --export RESEARCH_EXPORT/<key> --store <copy of research/learning_store> --dry-run` when a runtime is available and record the quarantine count in A9. The export is a record of research already performed; it never changes the card. If it cannot be written, record `LEARN_EXPORT_NOT_WRITTEN` with the reason. Research completeness is still judged by RESEARCH_COMPLETION_PROTOCOL, not by the export.

## 3. The learning store (prompt 4 writes; prompts 1–3 dry-run only)

`research/learning_store/` is append-only CSV: EVENTS, EVENT_ALIASES, RESULTS (revisions), TEAM_GAME_STATS (revisions), PLAYER_AVAILABILITY (snapshots), SOURCE_OBSERVATIONS, QUARANTINE, FEATURE_SNAPSHOTS and INGEST_RECEIPTS. Only prompt 4 (verified canonical import) or an authorised prompt 8 change ingests into the shared store, so concurrent minis never race on it.

- **One event, many observations.** Identity is the competition plus native event ID. Without one, a date/participant surrogate is used, and a later native ID becomes an alias, not a second event. The same match researched in five minis is one training game with up to five source observations. Re-running an ingest adds nothing.
- **Conflicts are quarantined, never last-row-wins.** A disagreeing score, swapped orientation, endpoint mismatch, unreviewed row, retired-store source, failed hash or impossible chronology goes to QUARANTINE with the reason. Only a later reviewed `WEB_CORRECTED` observation creates a new result revision.
- **Point-in-time.** A revision's availability is the earliest `known_at` of the reviewed observations supporting it. Any view "as of" an instant uses only revisions, statistics and availability snapshots known by then, and games from an earlier UTC day. Information first available later cannot change an earlier feature vector or primary HISTORY (tested).
- **Atomic receipts.** INGEST_RECEIPTS is written last. Rows of an interrupted ingest stay invisible and their sequence number is never reused.
- **Primary bridge.** `python -m ml ingest history --store … --competition … --endpoint … --horizon <scheduled start> --exclude-event <target>` writes primary HISTORY.csv rows that pass `primary predict` admission (source_kind, evidence path and hash, known-at). The retired results store is not a source.

## 4. Point-in-time features (FEAT-2026.10.16-v1)

`python -m ml features` builds, for each side: L5/L10/L15/L20 points for/against/net with true n; possessions-based offensive/defensive rating and pace when every game in the window has sourced possessions; exponentially decayed form (half-life 8 games); opponent-adjusted L10 net; season baseline; venue split; rest days; confirmed starters, confirmed absences and lineup-confirmed flag from availability published by the horizon; and league scoring context. Every feature carries `__n` and `__missing`. Missing stays missing: no league-average fill, and no "all players available". Snapshots for a forecast ID are frozen once in FEATURE_SNAPSHOTS.csv with the store view and digest.

## 5. Training admission and immutable releases

`python -m ml training build --store … --competition … --endpoint … --release-id … --out-root research/training_releases [--candidates research/training_candidates]` admits one row per FINAL event (label = effective reviewed result in the recorded store view; features as of that event's own start) or records the exclusion: NO_REVIEWED_RESULT, NOT_FINAL, OPEN_QUARANTINE, INSUFFICIENT_HISTORY, or CANDIDATE_WITHOUT_STRUCTURED_HISTORY for a verified research_learning candidate whose history was never exported. The manifest fixes the store view, digest, feature specification, code hash and file hashes. `training verify` rebuilds the rows from the recorded view and requires identical bytes. A correction makes a new release. Existing releases are never overwritten. A release is training data only, not a model or a predictive claim.

## 6. Models, studies and what each may claim

- **Basketball challenger BKB-FEATURE-RIDGE-C1** (`python -m ml bkb-features ablate`). Regularised regression of regulation home/away points on FEAT-v1 features, with residual covariance giving one joint grid (V3 overtime handling) and an optional variance-preserving heavy-tail scale mixture. The ablation tunes each feature set (BASE, L5, L10, L20, DECAY, MULTI, FULL) on a tune window only. It then scores every set and the exact V3 experts on identical later games with weekly refits from rows whose labels were known by each Monday. It reports Brier, log loss, margin/total CRPS, 50/80/95% interval coverage and MAE, with paired week intervals. NBA, NBL and EuroLeague are separate releases; no pooling is enabled without held-out evidence that it helps the smaller league without harming the others.
- **V3-equivalent backtest** (`python -m ml v3-backtest`). Issues every evaluation event at its own start with the runtime's own fitting, 30-week warm start and delayed bundle-feedback precedence, at the provisional η. Evidence class HISTORICAL_V3_EQUIVALENT_BACKTEST_NOT_PROSPECTIVE. The preserved 41,752-game replay remains proxy evidence.
- **Hedge study** (`python -m ml hedge-study`). On a backtest ledger, compares fixed η values, AdaHedge, discounted (forgetting) Hedge, season reset, effective-sample-size floors and shrunk contextual weighting. Schedules are selected on the tune window only and evaluated afterwards against V3's η = 2. It reports weight-collapse diagnostics (mean ESS, share with a weight above 0.99) and Page–Hinkley regime alerts. A composite winner/margin/total loss may be studied only with weights fixed in advance. Mixture CRPS is reported as an upper bound.
- **Calibration study** (`python -m ml calibration`). Identity, prior-shrunk Platt, isotonic (≥200 rows) and competition-shrunk Platt are fitted only on earlier predictions whose outcomes were available, selected on a later window and evaluated after it. Grid recalibration rakes winner and over/under classes jointly so every contract stays a projection of one distribution. Status CALIBRATION_STUDY: nothing is applied to cards.
- **Full RL** stays out of scope. Forecasting does not control the outcome. A future sequential-decision study needs its own state, action, reward, budget and logged behaviour policy, separate from probability accuracy and behind the market firewall.

## 7. Prospective shadows, review levels and dispositions

**Shadow freeze.** `python -m ml prospective freeze` appends rows to the hash-chained SHADOW_LEDGER before the scheduled start. Each row records model, version, release, parameters, code hash, exact contract and probability. PRE_START_VERIFIED requires issue and freeze before the start. Commit the ledger before the start to claim publication. Shadows never appear on cards and consume no P-ID.

**Evaluation.** `python -m ml prospective evaluate` compares identical settled pre-start contracts only. Rows are averaged within event, then week, and the interval is a t-interval over weeks. It reports Brier, log loss, calibration slope/intercept, rank-1 accuracy, Hit@2, NDCG@2 and coverage. A preregistered minimum effect `delta` gives the weeks needed at 80% power. A result that cannot resolve it is INSUFFICIENT_EVIDENCE.

**Review levels** (workflow triggers, not sample-size guarantees):

| Level | Trigger | Prompt | May conclude |
|---|---|---|---|
| Mini settlement | each mini (about 40–50 games) | 3 | Outcomes, labels, feedback, data integrity, preliminary diagnostics. No superiority claim |
| Interim combined review | about 100 newly settled unique games (`INTERIM`) | 6 | Coverage, calibration warnings, failures, baselines; defects and controlled experiments |
| Comprehensive retrospective | about 300 newly settled unique games (`COMPREHENSIVE`) | 6 | All sports; per-sport eligibility; backtest/Hedge/calibration/challenger/shadow evidence; dispositions |
| Sport / competition clock | 100 per sport, 50 per competition (`SPORT`, `COMPETITION`) | 6 | That scope's model decision |

`python -m ml learning-status` derives the counters from verified artifacts: unique settled games, ML-admissible games, frozen model forecasts, Hedge feedback games and prospective evaluation games. It also reports games since the last review per scope and level. A material software defect, a source-quality failure or credible sustained deterioration in an `ALERTS.csv` row makes the scope EARLY_REVIEW. Every review appends to `research/learning_status/REVIEW_LOG.csv` exactly one disposition per reviewed scope: NO_CHANGE, DATA_REPAIR_REQUIRED, EXPERIMENTAL_RETRAIN, CALIBRATION_STUDY, PROSPECTIVE_SHADOW, PROMOTION_ELIGIBLE or INSUFFICIENT_EVIDENCE. Reaching a game count never promotes a model.

## 8. Registry, promotion and rollback

[MODEL_REGISTRY.csv](research/model_registry/MODEL_REGISTRY.csv) is append-only and hash-chained. Statuses: RESEARCH_ONLY_NO_MODEL, DEVELOPMENT_EXPERIMENT, HISTORICAL_BACKTEST, PROSPECTIVE_SHADOW, AUTHORISED_EXPERIMENTAL_PRIMARY, PROSPECTIVELY_QUALIFIED, RETIRED, ROLLED_BACK. PROSPECTIVELY_QUALIFIED requires an earlier PROSPECTIVE_SHADOW entry for the same version, a prospective report whose disposition is PROMOTION_ELIGIBLE, and an owner authority reference. A retired version cannot be reactivated. A rollback names the restored model:version. The order for any primary change is: admitted release → chronological ablation/backtest → calibration study → preregistered prospective shadow → PROMOTION_ELIGIBLE → owner decision → registry entry → PRIMARY_PREDICTION_PROTOCOL change through prompt 8. No registry row changes issued cards or grades.

## 9. Deliberately not done here

- **Continuous integration and branch protection.** Workflow files are prohibited (CONTRIBUTING). An owner amendment permitting a narrowly scoped `.github/workflows/` file, or external CI, plus GitHub branch protection, are owner decisions. Until then, run `python -m pytest ml/tests` before every ML publication (prompt 8).
- **Player impact ratings and roster continuity.** These need player-level game statistics that the store does not yet ingest. Availability enters only as confirmed counts and flags.
- **Contextual bandits, deep networks and pooled cross-league ratings.** Not built. Section 6 states the conditions under which they could be studied.
- **Any run on real data.** All new tools were exercised on synthetic EXAMPLE data. Real ablations, backtests and studies start once reviewed exports have been ingested, and each needs its own receipt.

## 10. Runtime capability, standalone baseline, shadow adapters and card history (v1.1, 16 October 2026)

Added after the full-history retrospective ([retrospective_2026-10-16-full](research/verification/retrospective_2026-10-16-full/RETROSPECTIVE_REPORT.md)), which found that no fitted model priced any of 599 cards and only four events carried a frozen same-row baseline:

- `python -m ml capability [--out CAPABILITY_RECEIPT.csv]` — the runtime receipt every card records before ML_NOT_RUN (Python, pinned libraries, checkout root, HEAD, code hash).
- `python -m ml baseline --request … --history … --contracts … [--competition-source …] --out BASELINE.csv` — BASELINE_LEAGUE_V1 on the card's exact contracts from reviewed history, identical to V3's LEAGUE_BASELINE expert (tested), usable when the full primary run cannot price the event. A comparator, never p_card.
- `python -m ml prospective rows --bundle … --kind primary|tennis --role CHAMPION|CANDIDATE --out ROWS.csv` — converts a verified V3 or tennis bundle into shadow-ledger rows (PRE_START_VERIFIED only when issued and converted before the start) for `prospective freeze`.
- `python -m ml card-history --rank-log … --out …` — the reproducible full-history card table for prompt 6.
