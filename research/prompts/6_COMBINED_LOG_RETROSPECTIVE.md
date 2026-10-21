# PROMPT 6 — Review cards and independently verified sporting shadows

**Local keys until settlement; updated mini after every game (MINI-v2).** Apply [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md). Research and mini creation (prompts 1–2) use stable local event keys and never assign or reserve canonical P-IDs. A canonical P-ID is assigned only in an event's settlement phase: prompt 3 settles the event and then runs the prompt-4 import, which assigns the ID. After each prompt-1 game request the repository agent appends the card to the active mini under `research/active_minis/`, updates intake and footer, reads the file back, and commits and pushes it. Preserve every owner-entered Upcoming game block and all earlier issued bytes. Formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](../../RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**P-2026.10.22-v23.0 · COHORT_RETROSPECTIVE · LOCAL_WORKING_TREE.** Read [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). Trigger: user request, about 30 newly settled cards, or a DUE/EARLY_REVIEW row from `python -m ml learning-status` (INTERIM about 100 and COMPREHENSIVE about 300 newly settled unique games; per-sport and per-competition clocks); none proves statistical sufficiency. Writes: a new uniquely named report, authorized scoreboard/state summaries, dated hypothesis amendments and CHANGELOG. No original log/grade/forecast, active rule/prompt or previous report changes. The decision lab is excluded.

**ML/RL scope (MLSCOPE-v2).** Owner instruction, 22 October 2026: models run where they are needed, beside the analyst card and never inside it. Prompt 1 researches the game online and prices every p_card as ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY from one declared distribution ([PROBABILITY_TOOLKIT](../../PROBABILITY_TOOLKIT.md); code may do the arithmetic, with every input and step printed). Only after the card is written to the mini does prompt 1 run the pregame model shadow, which freezes the model and league-baseline rows, and the card's own p_card, on the same contracts when the competition has an active release, or records NOT_RUN_NO_RELEASE. Model output never changes a card's p_card, ranks or picks. Prompt 3 settles the shadow with the card; prompt 6 ingests and evaluates; prompt 8 builds releases and decides promotion. A model is judged only after at least 8 weeks and 50 paired games; a progress review falls due when either is reached first. RL has no forecasting role: online expert weighting updates at settlement. Details: [FORECAST_CYCLE_PROTOCOL](../../FORECAST_CYCLE_PROTOCOL.md). Supersedes MLSCOPE-v1, NOCODE-v1 and any older text that forbids code or models in prompts 1–5.

**Execution environment (ENV-v2).** Owner instruction, 22 October 2026: every prompt, 1 to 8, runs in this repository as the repository agent (`LOCAL_WORKING_TREE`), with internet access for research. Controls are read from the local working tree; GitHub `main` is the published copy, and every run that changes files ends with a commit and push. The external-chat route (ENV-v1) is retired for new work; anything it produced earlier is still imported as before. Details: [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md).

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

## 1. Freeze scope and evidence

Read common controls/protocol, scoring, verification, hypotheses, latest completed retrospective/implementation, relevant learning/source/archive/profile sections and original cards/effective settlements. An unfinished draft is not a completed report. Print HEAD/dirty inventory, actual reading receipt and outcome exposure.

Write SCOPE before analysis: issue/event dates and IDs, policy/format versions, inclusion/exclusion, timing/gate/lead/evidence strata, original-baseline availability, prior exposure, comparisons and snapshot time. It is retrospective if outcomes were already seen. Include numeric, qualitative, NO_FORECAST, pending, unresolved, blocked and duplicate request coverage.

Create DATA_INVENTORY and row-level COHORT_TABLES joining original cards to effective revision chains. Inventory every included/excluded ID and source block; conflicting branches remain unresolved. Recover missing original p only from the actual frozen core, never a summary or hindsight interpretation.

## 2. Assess prediction with matching units

For every sport/competition/format/endpoint/policy represented, report its own counts; list small strata explicitly. Preserve version boundaries, ranks, primary/informational/shadow/reforecast cohorts and evidence classes.

Report:
- Each declared assisted cohort (V1/V2/V3) separately from independent manual/shadow cohorts, including mixture weights/η admission or historical action propensity as applicable, warm/feedback coverage and actual code/source/grid receipts. Compare sporting learning against frozen same-row baselines; never import staking rewards into card learning.
- Requests/retained events and numeric/baseline/settlement coverage; earlier missing intake means NOT_COMPUTABLE, not complete coverage. Include unresolved-case sensitivity.
- Original rank W/L/PUSH/VOID/UNRESOLVED, card classes and Hit@2 with exact denominators; mechanically protected pairs separately.
- Same-row paired Brier/log-loss differences, event and ISO-week means, events/weeks, justified uncertainty, headline A/B and sensitivity C/E evidence. In-sample climatology is descriptive. Missing paired evidence does not establish incremental skill; it does not prove none.
- Complete-range reliability bins and empty bins, event counts and calibration uncertainty; expected-score bias/MAE/RMSE and originally issued interval coverage. No z without original SD.
- Gate PASS/instability/precision and frozen RET03/RET04/XCARD6/RANK_DELTA/BASE_ONLY comparisons, original/unadjusted adjustments, form-window/mixture diagnostics and identical-line difficulty.
- Correctly conditioned joint losses; exact values versus bounds; actual issue state/lead and independent input horizon, separately scored CLEAN_PRE_START_INPUTS / POST_START_ISSUE versus pre-start-issued/unknown/outcome-exposed cohorts; no fixed research deadline, availability-search completion, source lineage, capture/review SLA and unresolved workload.
- Rank-1 deep reviews and matched-win process defects; mechanism known-at versus post-event explanation. One loss or short streak is not calibration proof.

Use event/week dependence, repeated teams, serial drift, missingness, multiplicity and unequal task difficulty in the interpretation. Fewer than eight weeks is INSUFFICIENT_EVIDENCE under current scoring; eight is a floor, not a power calculation. No invented bootstrap or sample-size number.

## 3. Audit sporting shadows separately

After manual settlement, inspect permitted sporting model/forecast/receipt/result files. Match exact model/config/data identities, scope and contract to independently frozen pre-start forecasts with retained publication/cutoff evidence and effective settlement. A generated historical prediction or local receipt alone is not prospective.

Keep HISTORICAL_DEVELOPMENT, unverified/reconstructed shadows and PROSPECTIVE_SHADOW separate. Invalid gates receive an exclusion reason and retained inventory. Compare manual and model probabilities only on identical frozen event/line/endpoint with genuine independent issuance; assisted/exposed analysis is a distinct policy. Model rows never offset primary losses or inflate independent n.

Assess distribution/calibration/coverage against strong frozen baselines and registered meaningful effects/precision/stop rules. A SHADOW_CANDIDATE, passing tests or a wide interval containing slope 1 is not qualified. Recommend but do not implement/promote a model here; prompt 8 handles authorized changes. Never use decision-lab results in card learning.

## 4. Recommend, verify and publish

For each finding record evidence, actual defect/mechanism, exact proposed change/files, dependencies, owner/task, status, acceptance/rollback and prospective design inputs. Separate implemented controls, data readiness, registration, measured experiment result and release. Preserve old hypotheses and append versioned amendments. Unknown power inputs mean BLOCKED_DESIGN / SAMPLE_SIZE_NOT_ESTIMATED.

Produce RETROSPECTIVE_REPORT with complete inventory, cohort calculations, supported findings/limits and priorities. Reconcile all totals and independently check representative arithmetic. Update authorized summaries without changing grades or claiming new qualification.

Publish exact paths under invoked-task authorization, fetch and verify remote artifacts. Return scope, paired-data sufficiency, results/coverage, exclusions/unresolved queues, findings, test priorities and commit/remote status.


Under RESEARCH_COMPLETION_PROTOCOL, report research completion, numerical ML/analyst availability and issuance separately. Audit early exits caused by model/calibration, lineup, timing or mini blockers against the actual work, not the presence of a NO_FORECAST label. Keep automatic NOT_PRIMARY analyst comparisons out of model T2/feedback and prospective model claims; do not restamp old cards with a new completion receipt.

## Research retention and execution disposition (RETAIN-v1)

**Retain the research (RETAIN-v3).** Record the full research and its ANALYST_PRIMARY_V1 probabilities (or a bounded range / UNCALIBRATED_QUALITATIVE / NO_FORECAST row with the reason) under a stable local event key, and append the card, intake row and footer to the active mini after every game request (ENV-v2). The card never waits for or depends on a model; a model shadow run after the card (MLSCOPE-v2) is recorded beside it. Canonical P-ID assignment happens only in the settlement phase (prompt 3, through the prompt-4 import). Settle original contracts and keep verified outcomes for prompt 6 learning; never invent probabilities, sources or pregame timing. C21 checks that the probability method, inputs and arithmetic are disclosed; C22 checks updated-document delivery.

Audit every included game and mini manifest: requested/card/executed/failed/not-run counts, exact sport/competition/endpoint, fitted versus unavailable baselines, warm/feedback learning counts and terminal feedback retained/pending/blocked. Verify EXEC-v1 records; keep historical missingness separate. Missing baselines remove only paired-score rows, never otherwise supported inference or source-backed learning. Report the actual Hedge mechanism and unsupported adapters; do not call it a trained control-RL policy or infer skill from execution coverage.


**Local research record and updated-document delivery (owner update, 16 October 2026).** Use a stable local event key during research and local settlement; do not assign, reserve or advance any canonical P-ID. Append the researched card, its intake row and footer to the active mini, read it back and commit it after each game request (ENV-v2). Canonical IDs are assigned only in the settlement phase, when prompt 3 hands the settled event to the prompt-4 import, which reconciles duplicates and identity and records the immutable local-to-canonical mapping. An already assigned canonical ID remains a reference, never a new pregame allocation. Preserve issued originals and actual timing. See MINI_LOG_IDENTITY_PROTOCOL.

See [RETAIN-v2](../../RESEARCH_RETENTION_PROTOCOL.md). This owner update changes local identity and delivery procedures; numerical model, selection and scoring formulas are unchanged.

## Persistent sourcing and information closure (EXH-v1)

Audit requirement closure and source independence across the complete cohort, including wins and unresolved cases. Use newly discovered source routes for authorized field review, but do not backfill pregame facts or alter original grades. Record route discoveries, actual attempts, evidence limitations and proposals in the named report; shared register updates require declared scope. Process exhaustiveness is separate from complete information and predictive skill.

## ML/RL review (MLSCOPE-v2)

Prompt 1 freezes pregame shadows and prompt 3 settles them; this prompt reviews them. After the cohort's cards are imported:
1. Transcribe each imported card's Markdown learning record and settlement outcomes into the export columns of [LEARNING_PIPELINE_PROTOCOL](../../LEARNING_PIPELINE_PROTOCOL.md) §2 (keeping source and capture time), then ingest them with `python -m ml ingest add`; record every receipt and leave quarantined conflicts open.
2. Export verified research-only labels with `ml.research_learning`, settle any frozen model shadows and legacy bundles (`primary settle`, `cycle settle`) and append the package review rows to `research/learning_status/REVIEW_LOG.csv`; run `python -m ml learning-status`.
3. Report lane progress with `python -m ml pregame status`, then compare model against league baseline (`cycle evaluate`) and the ANALYST_PRIMARY_V1 card against the model on identical frozen rows (`python -m ml pregame compare-card`), with `card-history` for BASELINE_P. State coverage and power. A model is judged only when its lane has at least 8 settled weeks and 50 settled paired games; at whichever comes first, a progress review is due and reports INSUFFICIENT_EVIDENCE with the counts.
4. Model findings never edit an issued card. They reach the analyst card only as proposed Markdown changes (PROBABILITY_TOOLKIT constants, BASE_RATES_REGISTER rows, LEAGUE_PROFILES, rule text) implemented through prompt 8.

## Evaluation levels and model decisions (LEARN-v1)

Apply [LEARNING_PIPELINE_PROTOCOL](../../LEARNING_PIPELINE_PROTOCOL.md) §§6–8. State the level: INTERIM (about 100 newly settled unique games) or COMPREHENSIVE (about 300), plus every SPORT/COMPETITION clock that is due. Use the counters from `python -m ml learning-status`, never hand counts. Treat a tennis or minor-league scope separately from the combined count. For example, 300 combined games with 100 tennis matches is a tennis review on its own counts, and fewer still with frozen model forecasts or feedback.

- **Interim review:** audit data coverage, export/ingest quarantine, feature missingness, calibration warnings, model failures, rankings and baseline comparisons. Investigate defects and propose controlled experiments.
- **Comprehensive review:** cover all sports. Build or cite an immutable training release per studied scope and run (or cite receipts for) the V3-equivalent backtest, the Hedge schedule study, the calibration study, the basketball challenger ablation where basketball is in scope, and any prospective shadow evaluation with its preregistered `delta`. Keep tune and evaluation windows separate and never tune on the evaluated games.

For every reviewed sport and competition with a model, record exactly one disposition (NO_CHANGE, DATA_REPAIR_REQUIRED, EXPERIMENTAL_RETRAIN, CALIBRATION_STUDY, PROSPECTIVE_SHADOW, PROMOTION_ELIGIBLE or INSUFFICIENT_EVIDENCE) with its evidence, and append the rows to `research/learning_status/REVIEW_LOG.csv`. PROMOTION_ELIGIBLE needs a prospective evaluation report and is a recommendation to the owner, implemented only through prompt 8 and a registry entry. Reaching 100 or 300 games never by itself changes a model.

## Reproducible card history (v19.2)

Build every row-level cohort table with `python -m ml card-history --rank-log <committed rank log> --out <report folder>/HISTORY` instead of hand counts or one-off scripts: it joins the rank log, the effective final-settlement grades and the import inventories, dates and classifies every card, keeps NOT_PRIMARY analyst rows in their own cohort, flags historical ID collisions and reports slot rates, card classes, calibration, Rank-1 dependence tests and a collision-excluded sensitivity. Use the committed rank log (record its hash); an uncommitted refresh by another writer is noted, not used. Where a frozen same-row baseline is missing, report the coverage gap; never reconstruct a baseline after the outcome. See [LEARNING_PIPELINE_PROTOCOL](../../LEARNING_PIPELINE_PROTOCOL.md) §7.


**Connected cycle handoff (CYCLE-v1).** Apply [FORECAST_CYCLE_PROTOCOL](../../FORECAST_CYCLE_PROTOCOL.md). Preserve and verify actual workflow attempts and frozen version/contract identities. For contextual bundles, run `python -m ml cycle settle` with the verified structured settlement export into the authorised local/shared scope; preserve expert feedback and OUTCOMES.csv. Research-only labels never fabricate an expert loss. Prompt 4 re-ingests source exports idempotently into the shared store and records actual counts, quarantine and custody. Reconcile collided historical aliases by source/body addresses, never P-ID alone. Use `cycle evaluate` for frozen paired Brier/log-loss/calibration reports; insufficient future data remains INSUFFICIENT_EVIDENCE. No historical grade or model promotion follows automatically.
