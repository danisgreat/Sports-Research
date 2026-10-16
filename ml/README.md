> **Primary ML/RL owner amendment (15 October 2026):** [PRIMARY_PREDICTION_PROTOCOL](../PRIMARY_PREDICTION_PROTOCOL.md) permits the separate receipt-bound primary runtime and its full-information sporting mixture (PRIMARY_HEDGE_MIX_V3, which replaced the Exp3 bandit on 15 October 2026). Older statements below barring all model card inputs describe the prior independent-manual lane and are superseded for this new named lane. Existing historical artifacts remain unqualified; market/decision-lab outputs stay excluded.

**Online history and confirmed players (HIST-2026.10.16-v2 / AVAIL-2026.10.16-v3).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](../GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

# `ml/` — primary sporting runtime and maintainer model workshop

**Repeat bug audit:** [implementation and coverage](../research/verification/ml_bug_audit_2026-10-14-1/IMPLEMENTATION.md) repairs source parsing, grids, chronology, failure handling, reports, shadow outcomes and decision mechanics. Read the [additional artifact admission notice](../research/model_shadow/BUG_AUDIT_ADMISSION_2026-10-14.md) before using old outputs with the new implementation. Fixed historical fit/grid smoke checks are not predictive validation; fresh model outputs need controlled regeneration.

**Historical workshop review (14 October 2026):** CR-2026.10.14-R3 / prompt suite v11.3. Current primary release is CR-2026.10.16-R2 / PRIMARY-2026.10.16-v3.3 / prompt suite v17.0 under PRIMARY_PREDICTION_PROTOCOL; `python -m ml.evaluation.primary_replay` runs the corrected historical policy proxy into a new V3 output folder; the old replay is recoverable at 869a4776e. Read the [actual implementation review](../research/verification/framework_change_2026-10-14-5/ML_WORKSHOP_REVIEW.md) and [artifact admission](../research/model_shadow/ARTIFACT_PROVENANCE.md). Historical model outputs retain their original generating source; corrected report replays have new receipts. No model is promoted. That historical review reported 60 executed checks; current primary/integrity test results are in the new primary verification report. Neither establishes predictive qualification.

**Authority:** CURRENT_RULES §0 (model workshop exception) and §5a (decision-lab firewall), CR-2026.10.14-R1; framework change [2026-10-14-3](../research/verification/framework_change_2026-10-14-3/IMPLEMENTATION.md); design in [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](../ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md).

This is the only place in the repository where code may live. A maintainer runs it. Prompts 1–3 now run/read the named source-reviewed primary runtime under PRIMARY_PREDICTION_PROTOCOL and retain the immutable bundle under `research/primary_predictions/` or the named mini evidence scope. Other workshop outputs remain separate under `research/model_shadow/`; its unadmitted forecasts and DECISION_LAB are not primary inputs. Every output carries its actual status/receipt.

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


**Research retention before model availability (RETAIN-v1).** [RESEARCH_RETENTION_PROTOCOL](../RESEARCH_RETENTION_PROTOCOL.md) supersedes EXEC-v1's model prerequisite for recording/import. Write every identified researched event under its reconciled working P-ID and canonically retain it through verified import even if the model/adapter/runtime/module/baseline/calibration/receipt is absent or failed. Use RESEARCH_ONLY_NO_MODEL, explicit execution reason and blank nonexistent artifact paths; keep model p_card NOT_ESTIMATED and supported analyst_p NOT_PRIMARY. Missing ML never by itself blocks the ID or a source-backed settlement. Retain verified settled labels for future model development with source/known-at/revision/feature status; only actual frozen experts can supply Hedge losses. Never invent probabilities, execution, final scores or pregame timing. Identity/custody/write conflicts remain real blockers.


**Model use and mandatory running-log record (owner clarification, 16 October 2026).** Use the supported ML/RL mechanisms when they are available for the exact sport, competition and endpoint. Whether a model exists or not, assign the reconciled permanent P-ID, append the researched game card to the active running mini-log, read it back and advance its footer. A missing sport-specific model must not leave an otherwise recordable game as intake-only, unissued or without an ID. With no verified model output, record RESEARCH_ONLY_NO_MODEL, the actual reason and supported analyst work; never invent model probabilities or receipts. Carry that same P-ID through verified canonical import; do not allocate another ID. Before an authorized import, the local card may truthfully say PENDING_IMPORT; that status never cancels its ID or running-log entry. Identity/allocation conflicts, frozen or inaccessible originals and real write failures still block only the affected mutation. Verified settlements remain available for future model development in both paths.

See [RETAIN-v1](../RESEARCH_RETENTION_PROTOCOL.md). This is an editorial clarification of the existing two-path behavior; no model, numerical policy or format change.

## Tennis singles: separate experimental development lane

`python -m ml tennis predict|verify|settle` runs the independently versioned [`TENNIS_EXPERIMENTAL_HEDGE_V1`](TENNIS_EXPERIMENTAL.md) model (`tennis_primary.py`): hierarchical surface-specific serve/return estimates, a chronological Elo expert, exact best-of-3/5 match/game-score distributions, full-information Hedge feedback and source-bound immutable forecast receipts. [`test_tennis_primary.py`](tests/test_tennis_primary.py) contains synthetic unit/integration checks. **This is not certified, has no real-data prospective validation and is not yet part of the `MODEL_ASSISTED_PRIMARY_V3` tennis adapter.** The existing primary tennis `NOT_IMPLEMENTED` disposition remains truthful until separately authorised, validated integration. Do not merge its rows into the primary performance cohort or rewrite past cards.

## LEARN-v1 learning pipeline

[LEARNING_PIPELINE_PROTOCOL](../LEARNING_PIPELINE_PROTOCOL.md) (16 October 2026) connects research to learning without changing PRIMARY_HEDGE_MIX_V3. Every command writes a new output or appends to an append-only file, with receipts:

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
python -m ml card-history --rank-log GAME_PREDICTION_RANK_LOG.csv --out DIR
```

Tests: `test_learning_store.py` (dedup, quarantine, revisions, interrupted ingest, point-in-time features, reproducible releases), `test_learning_models.py` (challenger coherence and leakage guard, identical-game ablation, Hedge schedules against V3, delayed feedback, V3-equivalent backtest, calibration and grid raking), `test_learning_governance.py` (shadow ledger, paired evaluation and power, registry transitions, review clocks), `test_card_history_tools.py` (sport/family rules, effective-grade precedence, collision detection, Rank-1 tests, capability receipt, baseline equality with V3, shadow adapters), `test_learning_lifecycle.py` (one synthetic competition from duplicate minis through forecast, settlement, feedback, correction, release and counters) and `test_prompt_consistency.py`. All use synthetic EXAMPLE data. They establish mechanics, not predictive quality. No real-data ablation, backtest or study has been run yet.
