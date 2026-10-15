> **Primary ML/RL owner amendment (15 October 2026):** [PRIMARY_PREDICTION_PROTOCOL](../../PRIMARY_PREDICTION_PROTOCOL.md) permits the separate receipt-bound primary runtime and sporting bandit. Older statements below barring all model card inputs describe the prior independent-manual lane and are superseded for this new named lane. Existing historical artifacts remain unqualified; market/decision-lab outputs stay excluded.

# Model shadow lane (`research/model_shadow/`)

**Repeat audit notice:** [BUG_AUDIT_ADMISSION_2026-10-14.md](BUG_AUDIT_ADMISSION_2026-10-14.md) records additional code/data-definition repairs. Existing generated scores retain their historical receipts and are not current-model evidence. New fit/grid smoke checks do not promote any model.

**Authority:** CURRENT_RULES §0 (model workshop exception), §1 (reading-gate exclusion) and §5a (decision-lab firewall), CR-2026.10.14-R3; framework change [2026-10-14-3](../verification/framework_change_2026-10-14-3/IMPLEMENTATION.md). Code: [`ml/`](../../ml/README.md). Design: [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](../../ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md).

> **Ordinary shadow forecasts remain outside primary input selection.** Prompts 1–3 may run/read the separately named primary runtime/bundle under PRIMARY_PREDICTION_PROTOCOL, not substitute cached shadow probabilities. Prompts 3 and 6 may inspect matching shadows for admitted paired scoring. `DECISION_LAB/` stays excluded from card learning.

**Current admission override:** [ARTIFACT_PROVENANCE.md](ARTIFACT_PROVENANCE.md) reconciles generating source, incomplete execution and source admission. The index holds every numerical pass pending verification; original model cards preserve their earlier development wording.

## 1. What is here

| Path | Content |
|---|---|
| [STATUS.md](STATUS.md) | Generated table: every model, its development verdict and status |
| `<MODEL_ID>/MODEL_CARD.md` | Identity, endpoint, population, inputs, method, verdict, limits, receipt |
| `<MODEL_ID>/DEVELOPMENT_RESULTS.md` | Paired comparisons against `BASELINE_LEAGUE_V1` and TB-1 by test season; calibration; recalibration experiment; tuning |
| `<MODEL_ID>/PARAMETERS.md` | The latest fit as hand-applicable tables, with a worked example a reader can check by hand |
| `<MODEL_ID>/DEVELOPMENT_PREDICTIONS.csv` | Every development price (market-free) |
| [CARD_CALIBRATION/REPORT.md](CARD_CALIBRATION/REPORT.md) | Calibration audit of the issued cards' own stated probabilities (descriptive) |
| [DECISION_LAB/RESULTS.md](DECISION_LAB/RESULTS.md) | Firewalled paper study of staking policies; aggregates only |
| `<MODEL_ID>/FREEZE_RECEIPTS.md`, `SHADOW_FORECASTS_<yyyy>-W<ww>.csv`, `SHADOW_SETTLEMENTS.csv` | Created only when a registered prospective lane starts (none has started) |

Every generated file ends with a receipt: run time, repository HEAD, SHA-256 of the `ml/` code, SHA-256 of the archive files read, and library versions. A file that cannot be regenerated from its receipt is not valid.

**Model IDs.** `<SPORT CODE>-<COMPETITION>-<ENGINE>-r1` (for example `BKB-NBL-JOINT-r1`, `SOC-PREMIER-LEAGUE-DC-r1`, `CRT20-IPL-FI-r1`). Every competition folder in the archive is discovered by `python -m ml discover` and appears in [STATUS.md](STATUS.md), modelled or with the reason it is not (ml/README.md, "One process for every competition"). The IDs ending `-v1` that appear under this folder in commit `0e5685e57` were fabricated (invented parameters, future freeze times, empty-input hashes). That commit was reverted in `3ab6d27fe`, and those IDs are void.

## 2. Evidence classes and statuses

| Class | Meaning |
|---|---|
| `HISTORICAL_DEVELOPMENT` | Rolling-origin backtest on archive seasons that have been opened before: weekly refits from earlier games only, hyperparameters tuned on tune seasons only. It shows mechanics and plausibility, never prospective skill (SCORING_AND_VALIDATION §8). |
| `PROSPECTIVE_SHADOW` | Rows frozen before the event under §3 and settled from the feed. The only basis for promotion. |

| Status | Rule |
|---|---|
| `DEVELOPMENT_ONLY` | The development verdict failed. The model enters no lane. |
| `SHADOW_CANDIDATE` | The primary metric (home-win Brier) had a 95% week-block interval below 0 against **both** `BASELINE_LEAGUE_V1` and TB-1 in **every** test season, on rows with no integrity warning. It may enter a lane once its hypothesis is registered in HYPOTHESIS_REGISTER. |
| `DATA_HOLD` | Passed development, but the competition's rows failed an automatic integrity check (ml/README.md, step 5). No lane until the rows are verified against the field owner (prompt 7). |
| `RUN_FAILED` | The run raised an error, recorded in STATUS with its message. |
| `SHADOW` | A registered lane is running: frozen files and receipts exist. |
| `REFERENCE`, `ANCHOR` | Not used. Each needs a separate owner instruction after a stage-2 result (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5). |

## 3. Running a prospective lane: commit, then reveal

1. **Freeze.** `ml.shadow.lane.freeze(...)` prices every fixture of the window from one score grid per game. It writes `SHADOW_FORECASTS_<yyyy>-W<ww>.csv` **outside** the repository and returns the receipt line: file, bytes, real SHA-256, first scheduled start, freeze time and code hash.
2. **Commit the hash before the start.** Append that line to `<MODEL_ID>/FREEZE_RECEIPTS.md`; commit and push before the first scheduled start. Record the push time from the remote. A git commit time is not proof of issue time (CURRENT_RULES §9); the push time is recorded as corroboration only.
3. **Reveal after all package starts.** `ml.shadow.lane.reveal(path, model_id)` copies the file in only if all scheduled starts have passed and its SHA-256 equals the committed receipt.
4. **Settle.** `ml.shadow.lane.settle_rows(...)` calculates WIN/PUSH/LOSS/UNRESOLVED rows; the operator must preserve and validate append-only revision chains from final scores, with source and evidence grade (CURRENT_RULES §8). Missing evidence is `UNRESOLVED`, never VOID or LOSS.
5. **Score.** At prompt 6, use the same definitions as the cards (SCORING_AND_VALIDATION §1, §3–§5). Model rows never enter card cohorts or card win counts.

**Current-season data.** The archive's yearly files lag the live season. Before a freeze, the operator supplies the current season's completed results as a market-free CSV (`recent_results`) from a registered SOURCES route, and names it in the receipt.

## 4. Guards that apply to every file here

- No column carrying a price, line movement or market-derived probability (`assert_no_market_columns`; check C-ML-07).
- No JSON, pickles or notebooks.
- No hand-edited numbers in generated files. A correction is a re-run with a new receipt, and the earlier file stays in git history.
