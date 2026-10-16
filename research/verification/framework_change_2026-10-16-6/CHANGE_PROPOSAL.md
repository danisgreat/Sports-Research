# Change proposal: learning pipeline from the external improvement review (LEARN-v1)

**Instruction (owner, 16 October 2026):** "implement whatever is necessary and better from this suggested report. and push all changes to git main at the end", with the constraint that prompt 1's owner-entered Upcoming game lines stay unchanged and only text from each first "Read" onwards may change.

**Source:** an external read-only review of `main` at `ba4fefaee4c1` (*Sports Research — Comprehensive Improvement and Implementation Review*, 16 October 2026). Its factual claims were checked against the code before acting:

| Claim | Check | Result |
|---|---|---|
| `primary.py` fits team identity, prior scores and time decay; no availability effects | `model_features` receipt field, `_fit_models` | Confirmed |
| Hedge loss = mean of home-win Brier and over-league-line Brier (cricket: total only) | `expert_loss` | Confirmed |
| Provisional η = 2; no `research/primary_policy/ETA_ADMISSION.csv` | `DEFAULT_ETA`, file listing | Confirmed (no admitted table exists) |
| `research_learning` retains labels as candidates needing separate admission | module docstring and `feature_admission` field | Confirmed |
| The 41,752-game replay is not V3 validation | `primary_replay.py` docstring, PRIMARY_PREDICTION_PROTOCOL §5 | Confirmed |
| No GitHub Actions workflow; workflows prohibited | CONTRIBUTING | Confirmed |

**Class:** PROCEDURE (prompt minor bump to P-2026.10.16-v19.1, CR-R5) plus new workshop code under `ml/`. Selection, scoring, card/mini/settlement formats and PRIMARY_HEDGE_MIX_V3 are unchanged.

## Dispositions

| # | Recommendation | Disposition | What was done / why not |
|---|---|---|---|
| 1 | Research-to-training pipeline | ADOPT (adapted) | `research_ingest.py` + `training_admission.py`. Input is a structured per-card RESEARCH_EXPORT rather than parsing card Markdown, which would be fragile and could silently misread issued text |
| 2 | Structured observation tables | ADOPT | EVENTS, RESULTS (revisions), TEAM_GAME_STATS (revisions), PLAYER_AVAILABILITY (snapshots), SOURCE_OBSERVATIONS, FEATURE_SNAPSHOTS, plus EVENT_ALIASES, QUARANTINE, INGEST_RECEIPTS |
| 3 | Point-in-time L5/L10/L15/L20 features | ADOPT | `features.py` FEAT-v1 with true n, missing indicators, decay, opponent adjustment, rest, venue, season, possessions, confirmed availability; invariance test |
| 4 | Field-level admission and missingness | ADOPT (partial) | Quarantine with reasons; missing values stay missing; no healthy-roster default. Per-feature acceptable-missingness thresholds DEFERRED until real coverage is known |
| 5 | Immutable releases | ADOPT | Recorded store view, digest, spec and code hashes; byte-identical rebuild; retired-store paths and ARCHIVE_REVIEWED rejected at ingest |
| 6 | Basketball feature-rich model | ADOPT challenger C | BKB-FEATURE-RIDGE-C1 (one joint grid, V3 overtime). Challenger D (hierarchical/GBM) DEFERRED pending data volume |
| 7 | Controlled cross-league learning | ADOPT as policy | One release per exact competition; pooling not implemented until held-out evidence supports it |
| 8 | Window ablations | ADOPT | BASE, L5, L10, L20, DECAY, MULTI, FULL tuned on tune window, scored on identical later games against the exact V3 experts |
| 9 | Quantitative rosters/injuries | ADAPT | Confirmed starters/absences/lineup flag from snapshots published by the horizon. Player impact ratings DEFERRED: no player-level statistics are ingested yet |
| 10 | Distribution tails | ADOPT | Variance-preserving scale-mixture option; 50/80/95% interval coverage; margin/total CRPS |
| 11 | Re-evaluate η | ADOPT as study | Fixed grid, AdaHedge, ESS floor, discounted Hedge; chronological selection; collapse diagnostics. V3 η unchanged (no admitted row) |
| 12 | Composite proper loss | ADOPT as study | `composite_losses` with preregistered weights; mixture CRPS reported as an upper bound; not deployed |
| 13 | Contextual weighting | ADOPT as study; bandit REJECTED for now | Shrunk per-context Hedge. A contextual bandit is unnecessary with full-information feedback |
| 14 | Forgetting and regime change | ADOPT as study | Discounted Hedge, season reset, Page–Hinkley pairwise alerts |
| 15 | Full RL separate | ADOPT (documented) | Out of scope; conditions recorded in LEARNING_PIPELINE_PROTOCOL §6 |
| 16 | Deployment-ready calibration | ADOPT as CALIBRATION_STUDY | Chronological identity/Platt/isotonic/hierarchical Platt; coherent grid raking; nothing applied to cards |
| 17 | True V3 chronological backtest | ADOPT (code) | `v3_backtest.py` uses the runtime's own functions. NOT RUN on real data: the results store is retired and the new store is empty |
| 18 | Sport/league/contract metrics | ADOPT | Brier, log loss, reliability slope, CRPS, MAE, rank-1, Hit@2, NDCG@2, coverage; competition/family/endpoint breakdown |
| 19 | Robust uncertainty | ADOPT | Event→week clustering, weeks-needed power from a preregistered effect, INSUFFICIENT_EVIDENCE |
| 20 | Prospective shadow testing | ADOPT | Hash-chained ledger, pre-start enforcement, paired evaluation |
| 21 | Three evaluation levels | ADOPT | Prompt 3 (mini), prompt 6 (interim ~100 / comprehensive ~300) |
| 22 | Learning counters | ADOPT | `learning_status.py`, derived from verified artifacts |
| 23 | Evidence-aware triggers and dispositions | ADOPT | Per-scope clocks, alerts → EARLY_REVIEW, disposition vocabulary enforced in REVIEW_LOG |
| 24 | End-to-end lifecycle validator | ADOPT | `test_learning_lifecycle.py`. Canonical-ID re-run safety is covered by the existing prompt-4/verify-log controls, not re-implemented |
| 25 | CI and protected releases | DEFER (owner decision) | Workflow files are prohibited by CONTRIBUTING; branch protection is a GitHub setting. The full test suite remains a prompt-8 publication gate |
| 26 | Model versioning and rollback | ADOPT | `registry.py` and a seeded MODEL_REGISTRY.csv recorded from Git history |
| 27 | Operational monitoring | ADAPT | Ingest receipts, quarantine reasons, counters and triggers. Source-retrieval failures stay in the EXH-v1 registers |
| 28 | Prompt duplication | ADOPT (non-destructive) | DEPENDENCY_MAP.md plus consistency tests. Duplicated text is not rewritten, which preserves standalone prompts and owner inputs |

## Before and after

- **Before:** verified research was retained in Markdown and as label candidates, with no structured, deduplicated or point-in-time reuse. The V3 policy had no V3-equivalent backtest. There were no learning counters, no review levels beyond prompt 6's ~30-card trigger, no registry and no prospective ledger.
- **After:** prompt 1 writes a structured export, and prompt 4 ingests it into an append-only store. Features and releases are reproducible. Challengers, backtests and studies exist with receipts. Prospective shadows are frozen and evaluated with power-aware dispositions, counters drive the review levels, and the registry records every model state. No issued record, numerical policy or format changed.

## Rollback

Revert this change's commit. The new folders contain no issued records, and the store is empty at release. Archived originals are in [archive/superseded_2026-10-16-6/](../../../archive/superseded_2026-10-16-6/ARCHIVE_HASHES.csv).
