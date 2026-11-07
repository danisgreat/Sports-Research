# ML pipeline: workshop models, execution and the learning pipeline

**Merged 2026-11-07, CR-2026.11.07-R2 (FORMAT).** This document joins the files below, verbatim and in this order. Nothing was reworded. Each source's title line became its part heading. The banner paragraphs that every source repeated appear once, below. Links to the old files now point to their parts, and the originals are kept unchanged in [archive/consolidation_2026-11-07/merged_sources/](archive/consolidation_2026-11-07/merged_sources/).

| Part | Former file | Bytes | SHA-256 of the original |
|---|---|---:|---|
| [A](#part-a-primary_prediction_protocol) | `PRIMARY_PREDICTION_PROTOCOL.md` | 16,513 | `13231e68e0484ae8f95079a557ce95a34b81774fe03b2de63834071fc05c972e` |
| [B](#part-b-ml_execution_protocol) | `ML_EXECUTION_PROTOCOL.md` | 7,152 | `0d000bb193fd29b25462412c8d6dde4bd32ea614c88eff18bd05b8fab98e477e` |
| [C](#part-c-learning_pipeline_protocol) | `LEARNING_PIPELINE_PROTOCOL.md` | 18,164 | `cbc62472c83c479076552f75b8c5da849fe3d65f5a60dc929ab8ce98a704edab` |

**ML/RL scope (MLSCOPE-v3).** Defined in [FORECAST_CYCLE_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol); summarised in [CORE](CORE.md) §7.

**Executable forecast cycle (CYCLE-v1).** Defined in [FORECAST_CYCLE_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol); summarised in [CORE](CORE.md) §7.

**Local keys until settlement; updated mini after every game (MINI-v2).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](WORKFLOW.md#part-b-mini_log_identity_protocol); summarised in [CORE](CORE.md) §2.

**Persistent research and corroboration (EXH-v1).** Defined in [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_PROTOCOL.md#part-b-research_exhaustiveness_protocol); summarised in [CORE](CORE.md) §5.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** Defined in [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

**Required repository fallback (REF-v1).** Defined in [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md); summarised in [CORE](CORE.md) §1.

**Research retention before model availability (RETAIN-v2).** Defined in [RESEARCH_RETENTION_PROTOCOL](RESEARCH_PROTOCOL.md#part-c-research_retention_protocol); summarised in [CORE](CORE.md) §2.

**Local research record and updated-document delivery (owner update, 16 October 2026).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](WORKFLOW.md#part-b-mini_log_identity_protocol); summarised in [CORE](CORE.md) §2.

---

# Part A: PRIMARY_PREDICTION_PROTOCOL

*Formerly `PRIMARY_PREDICTION_PROTOCOL.md` (original title: Primary ML and online expert aggregation). Original kept unchanged at [archive/consolidation_2026-11-07/merged_sources/PRIMARY_PREDICTION_PROTOCOL.md](archive/consolidation_2026-11-07/merged_sources/PRIMARY_PREDICTION_PROTOCOL.md).*

**PRIMARY-2026.10.16-v3.3 · MDS-2026.10.16-v20.0 · CR-2026.10.16-R7 · SCV-2026.10.16-v11 · P-2026.10.16-v20.0.** Owner-authorised experimental primary use: MODEL_ASSISTED_PRIMARY_V3 / PRIMARY_HEDGE_MIX_V3 / EXPERIMENTAL_PRIMARY_NOT_CERTIFIED. [Review](research/verification/framework_change_2026-10-15-4/REVIEW.md). Prior controls and V2 remain recoverable in Git/archive; issued originals never migrate silently.

**Mandatory completion:** [RESEARCH_COMPLETION_PROTOCOL](RESEARCH_PROTOCOL.md#part-a-research_completion_protocol) governs the whole research deliverable. Uncalibrated status does not block authorised experimental inference. Missing/failed inference restricts numerical ML output only: complete source research, supported automatic analyst comparisons and every contract assessment, with the A9 completion matrix. No dependency failure permits an early research exit. The numerical V3 policy and runtime are unchanged.

## Mandatory execution and log coverage

Model-assisted forecasts use `primary execute --out ATTEMPT`, whose successful bundle is `ATTEMPT/BUNDLE`. Research-only cards need no executable/model/receipt: retain their honest disposition and future target eligibility under RETAIN-v1; no model probability or expert loss is invented. PRIMARY_HEDGE_MIX_V3, three experts, selection and scoring mathematics are unchanged.

## 1. What produces a primary forecast

Complete sporting/source/availability research and freeze the candidate recipe before pricing. The actual [runtime](ml/primary.py) fits two exact-competition team-rating experts (90/365-day decay) and a separate league-only comparator. Full-information exponential weights combine their entire score grids, producing one coherent primary distribution. Copy PREDICTIONS.csv probabilities/ranks and selected mixture moments into the original card. Do not replace them with subjective adjustments or historical cached forecasts.

This is supervised sporting ML plus online expert aggregation (Hedge). It is not a trained environment-control RL agent, PPO or DQN. Unlike V1 random selection, all experts' observable results inform the weights and there is no random expert draw/importance weighting. Brier convexity favours a mixture over a random draw **with identical weights**; it does not guarantee that Hedge beats a different adaptive policy or any single expert. No predictive qualification follows from the mathematical property.

## 2. Horizon and input contract

The evidence horizon remains the earliest of `scheduled_start` in the game log, actual `issue_at`, and verified `actual_start` when available. All times include zones. No separate runtime `cutoff` column. Preserve rescheduling evidence under [timing rules](RESEARCH_PROTOCOL.md#part-e-timing_research_protocol). Research may continue after start with proven pre-start information and truthful issue/exposure labels; there is no T-60/T-5 or other forced advance freeze. An unknown actual start stays TIMING_UNVERIFIED. A declared issue time/generated receipt is not independent proof of publication or outcome blindness.

```text
python -m ml primary predict --request REQUEST.csv --history HISTORY.csv --contracts CONTRACTS.csv --out research/primary_predictions/EVENT
python -m ml primary predict --request REQUEST.csv --history HISTORY.csv --contracts CONTRACTS.csv --feedback EFFECTIVE_FEEDBACK.csv --out research/primary_predictions/NEXT_EVENT
python -m ml primary settle --bundle research/primary_predictions/EVENT --home-score HOME --away-score AWAY --final-at ISO --available-at ISO --evidence CAPTURE --evidence-sha256 SHA256 --out NEW_FEEDBACK.csv
```

REQUEST.csv: one row, `event_id,competition,home,away,scheduled_start,issue_at,actual_start,endpoint,outcome_exposure,candidate_recipe`, optional `venue`. Competition is the exact sport/competition identity, matched to reviewed COMPETITION_SOURCE.csv; no archive discovery is required. `outcome_exposure=NONE_RECORDED` is an operator declaration; live/final outcome exposure blocks this unexposed full-event lane. Actual start may be blank. No odds/market/staking fields.

HISTORY.csv: `event_id,competition,endpoint,date,final_at,available_at,status,admission,source_url,evidence_path,evidence_sha256,season,home,away,hs,as_,reg_hs,reg_as,decision`, optional `stage`. Exact event IDs must be stable between history and feedback; reconcile native/P-ID aliases before preparing inputs. No target, duplicate, nonterminal, wrong-scope or malformed score rows. `status=FINAL`, `admission=RESEARCH_INPUT_REVIEWED`; exact field meanings and known-at times require actual source review. Date <= final <= available <= horizon, game date strictly before the horizon UTC day. Captures must exist and match SHA256; custody does not prove source truth, historical availability or field-owner certification. Late corrections are known from their actual availability, not game date.

Cricket adds `bat,bowl,venue,runs,legal_balls,wickets`. Coordinates are home=bat, away=bowl, hs=runs, as_=0 auxiliary, within scheduled legal balls/wickets; only full-length or all-out first innings. Request batting role must be verified. No invented chase, powerplay, second-innings or match-winner model. Cricket form separately counts batting and bowling observations rather than interpreting the auxiliary zero as a score.

CONTRACTS.csv: `contract_key,family,side,line,endpoint,definition,action`. Supported families winner/handicap/total with exact HOME/AWAY/DRAW or OVER/UNDER orientation. Winner action THREE_WAY_DRAW_LOSES or DRAW_PUSH; other families STANDARD_COMPLETED. FROZEN_FRAMEWORK_CONVENTION is conditional sporting action, not verified operator settlement. Unique keys and semantics required. Freeze every supplied/derived disposition; p>0.90 stays diagnostic, never clipped. Baseline is the league-only grid on identical contracts. Complete candidate-universe, family, precision, gate and joint checks remain operator responsibilities; CLI success is not automatic PASS. Baseball +1.5 Rank1 floor is enforced.

## 3. Point-in-time learning and parameter admission

Warm start uses the last 30 game-weeks of admitted history. Each week's experts fit only games dated earlier whose **final and source availability were known by that simulated Monday refit**. A source available at today's horizon cannot leak into an earlier simulated fit. At least 30 earlier games are required; unseen teams, failed fits and flagged expert grids do not supply partial loss vectors. Warm labels themselves must be available by the current horizon. WARM_START.csv retains each scored event, refit/availability time, league line and three losses; zero admitted learning events means uniform weights, not a claim of warm-start coverage.

Verified original-bundle feedback supplies full-information expert losses after final and availability. Home-win binary Brier plus over-the-frozen-league-line Brier are averaged; cricket uses the total question only. These are common sporting questions, distinct from original top-two contract performance. Primary pushes remain NOT_COMPUTED for top-two Brier, while evidenced common questions can still supply losses. Feedback takes precedence over an overlapping warm event: **one learning contribution per event**, although its known sporting result may still train the expert ratings. Conflicting history/feedback scores or participant orientation block the dependent forecast. Reconcile effective settlement revisions and aliases externally; duplicate feedback never becomes last-row-wins.

Weights ∝ exp(−η·(cumulative loss − minimum loss)), context policy|competition|endpoint. Default η=2 is **provisional, not tuned/validated for V3**. The old replay's tuning table is no longer loaded into primary predictions. An override must be separately admitted in `research/primary_policy/ETA_ADMISSION.csv` with `competition,policy,eta,tune_end,frozen_at,evidence_path,evidence_sha256`: exact current policy, one row, positive finite value, tune_end <= frozen_at <= horizon and matching evidence capture. No such admission is manufactured here. Future/unmatched parameters use a labelled default; malformed/conflicting admission fails. The table snapshot and hashes are retained. Statistical adequacy and source-known-at truth still require human review; a CSV label/hash is not qualification.

## 4. Immutable bundles and settlement

Each new event/revision uses a new output directory. Retain FORECAST.md, PREDICTIONS.csv, GRIDS.csv (three complete expert distributions), FORMS.csv (L5/L10/L15/L20 true counts), HISTORY.csv, CONTRACTS.csv, REQUEST.csv, FEEDBACK_INPUT.csv, MODEL_CONFIG.csv, WARM_START.csv, FEEDBACK_LOSSES.csv, ETA_ADMISSION.csv and RECEIPT.csv. Receipt includes policy/model/competition/endpoint, horizon/basis, declared issue/generated time, mixture weights/cumulative losses, η/admission/default, warm/feedback counts, actual input/config/output/code hashes, library versions and repository HEAD.

Verification rehashes every artifact, rejects duplicate/target learning events, checks ledger counts/summed losses, recomputes weights and re-mixes saved grids, checks primary W/P/L/p_decisive and same-row baseline, rejects nonfinite masses and binds identity/horizon to the saved request. The temporary bundle is verified before publication and changing code blocks publication. No existing directory is overwritten. V2 bundles can still be read/settled under their original policy; they do not silently train the V3 context.

Settle exact original keys first using official terminal fields and frozen definitions. `primary settle` verifies the original bundle/evidence capture and writes a new-only full-information feedback row; fractional/nonfinite/negative final scores are rejected, including feedback replays. Re-score every expert from frozen grids; preserve all-push primary missingness. Reconcile one effective revision chain before future learning. No pending, future, target-event or unsupported counterfactual label enters the weights. Source truth and operator terms are separate gates.

## 5. Scope, prediction evidence and honest failure

Supported exact competition configurations: joint-normal points, Dixon-Coles soccer regulation, count baseball/hockey, limited-overs cricket full first innings. Local endpoint/tie configuration governs; fit regulation before adding extras once. DATA_HOLD configuration, unsupported engine, unknown participant or failed/flagged fit blocks numerical primary use. No transfer of a major league's parameters to an obscure league. Tennis, field hockey, multi-day cricket and phase/player markets have no adapter here: retain NOT_IMPLEMENTED/NO_FORECAST and requested research. Remote agents lacking execution must seek an accessible actual runtime/verified exact-event bundle, record genuine capability failures, and complete the mandatory supported analyst comparison/qualitative analysis under RESEARCH_COMPLETION_PROTOCOL. ML_NOT_RUN/NO_FORECAST applies only to unavailable numerical ML rows; never invent a run or stop the rest of the analysis.

Current fitted features are team identity, prior scores and time decay. Confirmed starters, bench, injuries/illness/suspensions, tactical/format/weather evidence remain mandatory research; their effects are not fitted features. Material unsupported scenarios require qualitative/NO_FORECAST or a separately implemented/tested adapter. No silent hand mixture or form-centre overwrite. Historical manual, V1/V2/V3 assisted, independent shadow and market decision-lab cohorts stay separate; only each card's original top two count in its own T2 cohort.

The preserved 41,752-game replay reported better mean home-win Brier than random Exp3, but used different history/state/feedback and included DATA_HOLD leagues; its pooled interval treated competition-weeks as separate clusters, and its 200-seed comparator is Monte Carlo. It is **historical proxy evidence**, not a test or parameter qualification for this V3 runtime. Corrected replay code retains coverage, shared calendar-week pooling, failures and paired rows in a new output folder; old generated reports are never restamped. Passing tests establishes mechanics only. Prospective calibration, incremental advantage, practical-effect/power design and production readiness remain unproven/BLOCKED_DESIGN.

No odds, stakes, returns, CLV, fantasy, market moves or decision-lab inputs enter primary models, expert losses or ranks. `ml/decision/` remains a separate historical paper experiment. Actual primary execution is authorised; source truth and performance claims still need their own evidence.

## 6. Mandatory online historical research (HIST-v2)

[HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) requires online prior-game verification for every exact competition across all sports. Reviewed web rows can train the current model without a permanent archive refresh. Optional HISTORY source_kind=ARCHIVE_REVIEWED / WEB_RECOVERED / WEB_CORRECTED; unknown labels fail. The receipt records web/archive/unspecified row coverage. The original source/time/score/identity gates and V3 learning policy are unchanged.

For new events after store retirement, `primary predict --competition-source COMPETITION_SOURCE.csv` accepts one reviewed exact-scope metadata row, defined in the history protocol, instead of relying on that archive's discovered config. Every history row then needs an explicit source_kind. Metadata must match request, supported sport/endpoint/tie/innings/bonus configuration and source evidence known by the horizon. This does not release old DATA_HOLD data or models; it admits a fresh reviewed route and fresh row set. No unsupported engine is inferred from internet availability. The source config snapshot/hash is retained and checked against MODEL_CONFIG; old bundles without this optional sidecar remain readable. Research is performed by the operator/browser workflow, not an unattended built-in web scraper.

## 7. Relation to the learning pipeline (LEARN-v1)

[LEARNING_PIPELINE_PROTOCOL](#part-c-learning_pipeline_protocol) adds data, study and evidence layers around this runtime without changing it. HISTORY.csv may be generated from the reviewed learning store at the game-log scheduled start (`python -m ml ingest history`); the admission gates of §2 still apply to every row. The V3-equivalent backtest (`python -m ml v3-backtest`) reuses this runtime's fitting, warm-start and feedback functions to produce historical evidence for V3 itself. Hedge schedules, the basketball feature challenger and calibrators are studies. Any of them can affect primary cards only through a preregistered prospective shadow, a PROMOTION_ELIGIBLE evaluation, an owner decision, a [registry](research/model_registry/MODEL_REGISTRY.csv) entry and a prompt-8 change to this protocol. η stays the provisional default until a row is admitted under §3. Before any card records ML_NOT_RUN it keeps a `python -m ml capability` receipt (or the exact failing command and error), and when this runtime cannot price the event a same-line comparator from `python -m ml baseline` may still be frozen as BASELINE_P (LEARNING_PIPELINE_PROTOCOL §10).

---

# Part B: ML_EXECUTION_PROTOCOL

*Formerly `ML_EXECUTION_PROTOCOL.md` (original title: ML execution, research retention and future learning). Original kept unchanged at [archive/consolidation_2026-11-07/merged_sources/ML_EXECUTION_PROTOCOL.md](archive/consolidation_2026-11-07/merged_sources/ML_EXECUTION_PROTOCOL.md).*

**ML/RL scope (MLSCOPE-v3).** Owner instruction, 22 October 2026 (second instruction of the day, adopting the framework revamp review): models run where they are needed and a competition's declared reference model runs **before** the card. For a tier A competition whose declared reference is its release (NHL, MLB), prompt 1 freezes the model first (`python -m ml pregame reference`) and the card starts from that frozen number; where another reference is declared (the NBA's TB-2-MD) the release is frozen the same way as a challenger. Tier B and C competitions start from TB-2-MD, TB-1-MD or the league-only baseline (`python -m ml reference run`). The analyst's `p_card` (ANALYST_PRIMARY_V1) is that reference plus logged adjustments with sizes from the effect tables ([REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md), [ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md)); a frozen reference is never edited, and the card's own final p is frozen beside it by `python -m ml pregame run`. If no reference could run first, the model is only a post-card shadow and the card says so. Prompt 3 settles the card, then the frozen rows; prompt 6 ingests and evaluates; prompt 8 builds releases and decides promotion. A model is judged only on frozen, pushed, pre-start rows after at least 8 settled weeks and 50 settled paired games; a progress review falls due when either is reached first. A release is frozen for a season and edits outside the cycle's import closure never retire it. RL has no forecasting role: the online expert weighting that updates at settlement is online learning. Supersedes MLSCOPE-v2 (card first, model never feeds the card), MLSCOPE-v1 and NOCODE-v1 for cards under P-2026.10.22-v24.0 and later; earlier cards keep their method.

**EXEC-2026.10.16-v2 · MDS-2026.10.16-v20.0 · CR-2026.10.16-R7 · P-2026.10.16-v20.0.** [RESEARCH_RETENTION_PROTOCOL](RESEARCH_PROTOCOL.md#part-c-research_retention_protocol) controls recording/import independently of ML availability. This explicitly replaces EXEC-v1's missing-receipt issuance block. Use [GitHub main](https://github.com/danisgreat/Sports-Research/tree/main) when local repository files are inaccessible, under GITHUB_REFERENCE_PROTOCOL.

## 1. Execute when available, retain regardless

Attempt a supported actual primary run when accessible. Missing ML/RL adapter, ml module/interpreter, dependency/history/baseline/calibration or run receipt never by itself blocks a local-key research record or later prompt-4 canonical import. Use RESEARCH_ONLY_NO_MODEL with supported analyst_p/qualitative work and honest real timing; model p_card stays NOT_ESTIMATED. Record actual failures or NOT_RUN_CAPABILITY_BLOCKED / NOT_IMPLEMENTED / NOT_RUN_DATA_UNAVAILABLE. Never invent a successful run or a file to pass a check. Identity/ID/custody/write constraints remain.

```text
python -m ml primary execute --request REQUEST.csv --history HISTORY.csv --contracts CONTRACTS.csv --out ATTEMPT
python -m ml primary verify-execution --attempt ATTEMPT
python -m ml primary verify-log --manifest ML_EXECUTION_MANIFEST.csv --mini MINI.md
```

An actual execute attempt retains STARTED/INPUTS/EXECUTION and a successful BUNDLE where applicable. It fits its comparator from reviewed exact-competition history without a pre-existing profile. Real failed attempts exit nonzero. An interrupted attempt cannot be claimed successful; an honest no-model record can still be retained. Numerical V3 semantics and source admission are unchanged.

## 2. Honest manifest for each new card

New minis use mini-log-10 / mini-settlement-10; existing minis remain in their original format. Preserve the registered CSV header:

```csv
card_id,event_id,competition,endpoint,execution_path,execution_sha256,feedback_status,feedback_path,feedback_sha256,reason
```

For no actual bundle/attempt, leave execution_path/execution_sha256 empty; set feedback_status=NOT_APPLICABLE_NO_MODEL, blank feedback paths/hashes and the concrete reason. This is a valid research-only disposition, including a real No module named ml capability error. Do not place a nonexistent path in the manifest. If a path/hash is provided it must verify. MODEL_ASSISTED_PRIMARY_V3 requires actual successful execution. C21 verifies honesty and scope, not universal model availability. The verifier accepts mini-log-8/9; legacy formats use their original checks and explicit new record/disposition readback.

## 3. Settle every event and retain future targets

Canonical retention-only import can precede settlement. Preserve original card sources and timing; unreviewed outcomes stay PENDING_SETTLEMENT / OUTCOME_NOT_REVIEWED. Later settle the original contracts under the original local key, or the same mapped P-ID after prompt 4 with source/time/definition/revision evidence, regardless of whether a model existed.

For future model development, retain verified terminal labels and original research locally by local key; after prompt 4 assigns and verifies the canonical mapping, export RESEARCH_TRAINING_CANDIDATE with ml.research_learning under RESEARCH_RETENTION_PROTOCOL. Unknown features/known-at facts remain explicit; future training admission, deduplication, scope and effective revisions are separate. No model is required to retain these targets.

Only an actual original frozen model bundle supplies per-expert losses:

```text
python -m ml primary settle --bundle ATTEMPT/BUNDLE --home-score HOME --away-score AWAY --final-at ISO --available-at ISO --evidence CAPTURE --evidence-sha256 SHA256 --out NEW_FEEDBACK.csv
```

Keep actual expert feedback retained/pending/blocked dispositions where a model exists. Without a model, NOT_APPLICABLE_NO_MODEL applies to expert losses only; the event remains eligible for future source-reviewed label retention. Never backfill old predictions, Brier losses, propensities or rewards. Candidate targets cannot enter primary feedback directly.

The actual mechanism remains supervised scoring models plus Hedge, not a trained environment-control RL agent. Research IDs, source truth, numerical forecasting, training admission and prospective qualification are separate. All eleven game workflows and all eight lifecycle prompts follow this distinction.

---

# Part C: LEARNING_PIPELINE_PROTOCOL

*Formerly `LEARNING_PIPELINE_PROTOCOL.md` (original title: None). Original kept unchanged at [archive/consolidation_2026-11-07/merged_sources/LEARNING_PIPELINE_PROTOCOL.md](archive/consolidation_2026-11-07/merged_sources/LEARNING_PIPELINE_PROTOCOL.md).*

#**Executable forecast cycle (CYCLE-v1).** Apply [FORECAST_CYCLE_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol). New contextual forecasts use MODEL_ASSISTED_CYCLE_V1 with a frozen exact-competition release, actual execution receipt, identical-contract baseline shadows and verified settlement feedback. Existing V3/tennis adapters retain their own cohorts; missing/unsupported inputs require a real failure receipt and retained research. This statistical/procedure release authorises experimental execution, not predictive qualification.

 Learning pipeline: research → store → features → releases → models → prospective evidence

**LEARN-2026.10.16-v1.1 · MDS-2026.10.16-v20.0 · CR-2026.10.16-R7 · P-2026.10.16-v20.0.** Owner instruction, 16 October 2026: implement the necessary and better parts of the external improvement review so that every researched and settled game becomes reusable, point-in-time-safe learning data, and model changes depend on chronological and prospective evidence rather than on the arrival of new games. PROCEDURE + workshop code. **PRIMARY_HEDGE_MIX_V3, its η, experts, selection and scoring are unchanged.** Nothing here qualifies a model, changes an issued card, probability, rank, grade, ID or feedback row, or admits market data.

Read with [PRIMARY_PREDICTION_PROTOCOL](#part-a-primary_prediction_protocol), [RESEARCH_RETENTION_PROTOCOL](RESEARCH_PROTOCOL.md#part-c-research_retention_protocol), [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md), [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md) and [SCORING_AND_VALIDATION](SCORING_AND_VALIDATION.md). Code: [ml/](ml/README.md#learn-v1-learning-pipeline). Implementation record: [framework_change_2026-10-16-6](research/verification/framework_change_2026-10-16-6/IMPLEMENTATION.md).

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

## 11. Reference lane and adjustment ledger (v24.0, 22 October 2026)

The learning store gains a second consumer. Verified finals feed (a) the cycle release, (b) the TB-2-MD standings reference and (c) the width and effect tables ([COMPETITION_PARAMETERS](PARAMETERS.md#part-a-competition_parameters), [EFFECT_TABLES](PARAMETERS.md#part-b-effect_tables)). Rules: a competition needs two agreeing lineages and a passing `ml release-gate` before a release is frozen; a historical fact captured now is known now, never on its game date, so no context feature is fitted on history without a known-at time; the 2023-24 to 2025-26 NBA backfill (3,693 finals) is the first lane built this way and its release **NBA-CYCLE-1** is experimental with 0 prospective events. The adjustment ledger ([ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md)) is a separate append-only record of the analyst's departures from the reference; it feeds prompt 6's λ, never the store's training rows, until a prompt-8 decision says otherwise.
