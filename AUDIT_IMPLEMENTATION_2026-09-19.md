# Implementation ledger — 19 September 2026

Control revision **CR-2026.09.19-1**, method **MDS-2026.09.17-v4.1** (method text unchanged except §7; the control set changed, so the revision ID advances).

Covers: a user directive on over/under review, an empirical test of the rebound hypothesis, a direct test of social-media sources, and a sweep of prior audits for anything still unimplemented. All logs remain `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`. No forecast, rank, probability or canonical ID was altered.

---

## 1. User directive implemented

**The highest-ranked over/under selection now receives the same enhanced failure review as Rank #1 whenever it loses — and a push counts as a non-win.**

| Where | What |
|---|---|
| `METHOD.md` §7 | Two enhanced-review triggers defined: Rank #1, and the top over/under. Same form, same evidential standard. Explicit guard: this is retrospective scrutiny and licenses **no** hedging, probability shading, or refusal to rank a total |
| `SCORING_AND_VALIDATION.md` §3 | `TOP_OU_REVIEW` flag, identified **from issue-time ranks before any outcome is known**, recorded separately from the Rank-#1 flag so the two are independently countable |
| `UPCOMING_GAME_RESEARCH_GUIDE.md` | Settlement-protocol Step 5 trigger; §19 checklist line requiring the top O/U target to be named at issue |

Identifying the target at issue time is the load-bearing detail: choosing it after the result would let the review be steered.

## 2. Empirical work — new document `RECENCY_AND_REBOUND.md`, control `R-1`

The rebound hypothesis was **tested, not reasoned about**. MLB 2026: 4,594 team-games; 108 starters; 2,784 consecutive-start pairs; 2,244 out-of-sample predictions. Baselines are leave-two-out so the comparison is not contaminated by the games being tested.

| Result | Finding |
|---|---|
| Team rebound after a 0-run game | **−0.102** runs vs own baseline, 95% CI [−0.456, +0.251] — negative, not positive |
| High-calibre offences (top-10) after ≤2 runs | **−0.126**; bottom-10 −0.093. **Indistinguishable — calibre changes nothing** |
| Starter next-start ER after ≥6 ER | **−0.017**; strikeouts **−0.070** (they do not spike); elite starters **+0.003** |
| Lag-1 autocorrelation | **+0.019** team runs; **−0.037** starter ER |
| Out-of-sample RMSE by window | last-1 **2.7677** · last-3 2.2433 · last-5 2.1324 · season 2.0177 · league constant **1.9844** |
| Opponent vs own last game | opponent season runs-allowed R² **2.50%**; previous game R² **0.08%** |

`R-1`: recent results revise an estimated **rate** through a **named mechanism**; they never forecast a **deviation**. No rebound lean, no hangover lean, no "high calibre will correct it". Instantiated in all ten sport files with every non-MLB magnitude marked `NOT_YET_DERIVED`.

**A recorded success reclassified.** `P-453`'s Rank #1 rested on three-start form — the third-worst predictor measured — and won. Recorded as **directionally lucky**, not as validation. `P-443` and `P-449` won by using FIP/xERA to *override* recent results, which is the pattern the evidence supports.

## 3. Prior-audit sweep — what was still open, and its disposition

The [2026-09-17 model review](MODEL_REVIEW_2026-09-17.md) change set was verified by **running** its validation script, not by reading its claims.

| Item | Source | Disposition |
|---|---|---|
| Missing implementation ledger — six dangling links and the one failing validation assertion | `MODEL_REVIEW` §6 implementation | **CLOSED** — [`AUDIT_IMPLEMENTATION_2026-09-17.md`](AUDIT_IMPLEMENTATION_2026-09-17.md) created |
| `statsapi battingOrder` lineup route "proposed, **not yet demonstrated pre-game**" | `AUDIT_CHANGELOG_2026-09-11.md` | **CLOSED — demonstrated.** `hydrate=lineups` returns empty for `Scheduled` games and 9+9 once posted (verified 17 vs 19 Sep); `game/{pk}/boxscore` returns `battingOrder`, `bench` and `bullpen` by name. New `LINEUPS_NOT_YET_PUBLISHED` state distinguishes a publication schedule from a `RETRIEVAL_MISS` |
| Retro-tag ~86 pre-`L-095` lessons into the control taxonomy | `AUDIT_CHANGELOG_2026-09-06.md`, `L-095` | **RESOLVED — reframed, see §4.** Tagging historical *evidence rows* was the wrong unit; the *active controls* are what `L-096` needs, and those are now classified |
| All-history scorecard recomputation | `AUDIT_CHANGELOG_2026-09-05.md` | **Already closed** by the 2026-09-17 review (477 rows rebuilt; P-344 error found) |
| Scoring/ceilings/extras/`C-OU-GEOMETRY`/`H0`/trend-test/tennis-union/M0-M1 | `MODEL_REVIEW` §§3–4 | **Already implemented** — all confirmed by the 66 passing executable checks |

### Provenance disclosure — a mistake made during this sweep

Re-running the validation script **regenerated `audit_2026-09-17_implementation/RESULTS.md`**, overwriting the only recorded copy of the `CR-2026.09.17-1` control-manifest hash. That value is **not recoverable**: `BASELINE.md` and `before/` preserve the *pre*-17-September state, not the post-edit manifest, and no other document quoted it.

**Impact: none on any forecast.** No issued card freezes a control hash — Part 4 ends at `P-451` and `P-452` is unissued — so nothing downstream referenced it. The control set has since changed anyway, which is why this ledger opens **CR-2026.09.19-1** rather than trying to restore a superseded value.

**Root cause fixed, so this cannot recur.** `VALIDATION.md` hardcoded both the revision label and a 23-file manifest that predated `RECENCY_AND_REBOUND.md`. Two corrections were made to that script: the manifest now includes `RECENCY_AND_REBOUND.md` (24 files), and the emitted label is now **read live from `METHOD.md`** instead of being a literal. A re-run therefore self-labels correctly and cannot silently misattribute a hash to a superseded revision again. Confirmed: the script now reports **67 checks passed** and emits `CR-2026.09.19-1` with the matching 24-file hash. Editing an audit artefact is normally out of bounds — this was a correction to a self-mislabelling script, not a change to any recorded evidence, finding or result, and it is disclosed here.

## 4. `L-095` / `L-096` control taxonomy — the deferral resolved

Deferred since 2026-09-06 and referenced by an active authority, so it could not simply be dropped. But the unit was wrong.

`L-096` (control-effectiveness review) needs **controls** classified by consequence-of-failure. It does not need 86 historical *lesson rows* tagged — those are evidence, and `METHOD.md` §9 is explicit that dated retrospectives and archived text are evidence, not active instructions. `METHOD.md` §4 has meanwhile superseded the taxonomy's forward function for new cards, splitting failures into blocking versus evidence-grade-capping.

**Disposition:** the **currently active controls** are classified in `CONTROLS.md` §"2026-09-19(b)", aligned to METHOD §4's split. Retro-tagging the 86 historical lesson rows is **closed as not-to-be-done**, with that reasoning recorded, rather than left as a standing backlog item that no one will ever clear. `L-096` is executable for the first time.

## 5. Source findings

| Route | Result |
|---|---|
| X / Twitter | HTTP 200 but a **login wall** — 1,644 characters visible, zero post content; syndication lane 0 bytes; `r.jina.ai` **403 abuse-blocked**; nitter dead |
| Reddit | `.json` 403; `old.reddit` serves an interstitial |
| Bluesky | API works; **6 of 6 sports handles failed identity.** `jeffpassan.bsky.social` is a squatter posting *"I continue to not be Jeff Passan"* (Nov 2024); `fabrizioromano.bsky.social` is a different Fabrizio posting in Turkish (Jul 2023) |

Controls **`S-1`** (durable-identifier identity, recency, field-owner corroboration, verbatim quotation — all four) and **`S-2`** (press conferences are availability/workload/role evidence, never a signed adjustment to a modelled rate) added to `SOURCES.md` and `DATA_SOURCE_REGISTER.md`.

**Structured lanes added instead:** MLB `hydrate=lineups`, `boxscore` `battingOrder`/`bench`/`bullpen`, `people/{id}.mlbDebutDate`, ESPN cricket `debuts[]`. Debutant gates (`LOW_SERVICE_SAMPLE`, `NO_PRIOR_FORMAT_RECORD`, `NO_COMPETITION_SAMPLE`) added — a six-day rookie batted sixth for the Dodgers in `P-455` unflagged. Cricket pitch ladder extended to rung 7 (preceding same-venue match, recorded as a *different* strip) and rung 8 (toss broadcast).

## 6. Control manifest — CR-2026.09.19-1

**24 files** — the 23 in the previous manifest plus `RECENCY_AND_REBOUND.md`, which is control-class and must be covered. `VALIDATION.md`'s manifest and revision label were corrected in this pass (§3), so the script now computes over the same 24 files and emits the same value recorded in §7.

Files: `METHOD.md`, `SCORING_AND_VALIDATION.md`, `CONTROLS.md`, `RULES_GENERAL.md`, `RECENCY_AND_REBOUND.md`, `MODEL_IMPLEMENTATION_RECIPES.md`, `NUMERICAL_PROGRAM.md`, `NUMERICAL_TRAINING_SPEC.md`, `NUMERICAL_MODEL_REGISTER.md`, `MODEL_AND_DATA_SPEC.md`, `H0_DATASET_CARD.md`, `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, `BASE_RATES_REGISTER.md`, and the ten `RULES_<SPORT>.md` files.

The computed hash is recorded in §7 below and is reproduced independently by the validation script. Recompute before freezing it onto a card; if the bytes have changed, open a new revision rather than reusing this ID.

## 7. Recorded hash

**CR-2026.09.19-1**, 24-file manifest, computed 2026-09-19:

```
f0dd38836aa61bde0d12cd7e35dc2486bf31006f283f576739c723d3f699fcea
```

Recomputation snippet and the full file list are in `CONTROLS.md` §"2026-09-19(b)". This is a byte receipt over the control set at the moment of writing, not timestamp evidence. Recompute before freezing it onto a card; if it differs, open a new revision ID rather than reusing this one.

**Self-reference constraint.** This value is recorded **here and in `RESULTS.md`, both outside the manifest** — never inside `CONTROLS.md` or any other manifest file. Writing a manifest hash into a manifest file changes the bytes being hashed and invalidates the value as it is written. That loop was hit once during this pass and is documented so it is not reintroduced.

<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## Deep-research implementation pass — 2026-09-19(c)

### What was changed

1. Bumped forward authority to **MDS-2026.09.19-v4.2 / CR-2026.09.19-2 / SCV-2026.09.19-v2 / NTS-2026.09.19-v0.5 / NP-2026.09.19-v2** for new forecasts only.
2. Added a hard market/fantasy source firewall across METHOD, CONTROLS, SOURCES and the full source register. RotoWire, RotoGrinders and FPTrack are explicitly prohibited predictive sources.
3. Added threshold quarantine: user-supplied totals/spreads/alternate lines are contract metadata and cannot influence the independent forecast distribution before it is frozen.
4. Added source provenance/lineage fields, point-in-time `known_at <= cutoff` enforcement, stale-critical-state handling and independent-lineage requirements.
5. Added distribution-first validation: CRPS/RPS/log score where applicable, W/P/L Brier/log loss, RMSE/MAE, calibration and interval coverage, with chronological event-grouped evaluation and block-bootstrap uncertainty.
6. Strengthened training rules: fold-local preprocessing, separate CAL, one-time TEST, OOF-only stacking, systematic eligible-event universe and baseline-first model sequencing.
7. Added sport-specific source/model addenda to every active sport module and the soccer/cricket league-rule files.
8. Added executable [`prediction_preflight.py`](prediction_preflight.py) plus tests; `audit_card_controls.py` remains the complementary printed-card execution audit.
9. README no longer hard-codes a next prediction ID; current queue/ID must be read from the active log snapshot, preventing documentation drift.

### Why

The deep audit found that the project was stronger in governance than in empirical implementation. The highest-risk gaps were source contamination (fantasy/betting-adjacent sources in recent cards), subjective centre adjustments, control-version drift, insufficient executable provenance gates and the absence of a fitted/validated numerical model. These changes directly address those failure modes without pretending that documentation alone improves predictive accuracy.

### Expected benefit (not yet a measured gain)

Expected benefits are lower leakage/circularity, less market anchoring, better reproducibility, more honest uncertainty, stronger source independence and more coherent over/under/spread probabilities. **No improvement in win rate, Brier, calibration or RMSE is claimed yet.** Those claims require H0, chronological out-of-sample testing and prospective shadow evidence.

### Validation still required

- Build and quality-approve H0 with point-in-time source snapshots.
- Fit A0/A1 on frozen chronological folds and compare on proper scores.
- Calibrate only on CAL; open TEST once.
- Run prospective shadow forecasts with live source-latency/missingness monitoring.
- Promote only if the exact scope beats the simpler baseline with acceptable calibration/support and critical-slice behaviour.
## Deep-research implementation verification receipt — final local validation

- `prediction_preflight.py` added as a fail-closed executable control.
- `FORECAST_PREFLIGHT_MANIFEST.md` added with the required JSON contract/provenance schema.
- **15 unit tests pass**: valid manifest, betting-source rejection, fantasy-source rejection, discovery-only rejection, unadmitted-class rejection, historical-candidate live-critical rejection, post-cutoff rejection, stale-critical rejection, unknown-lineage rejection, insufficient-independent-source rejection, version mismatch, line visibility, market/line input-key leakage, line-before-freeze ordering, and the permitted two-independent-secondary fallback.
- `prediction_preflight.py` and `audit_card_controls.py` both pass Python compilation.
- These checks establish control implementation correctness only. They do **not** establish lower RMSE, higher hit rate, improved Brier/log loss or calibration. Those require H0 construction and frozen chronological out-of-sample/prospective validation.

## Final implementation/read-back closure — CR-2026.09.19-3

Current prospective authority after synchronization is **MDS-2026.09.19-v4.2 / CR-2026.09.19-3 / SCV-2026.09.19-v2 / NTS-2026.09.19-v0.5 / NP-2026.09.19-v2**.

CR-3 closes implementation drift found during the final read-back: active v4.1/v0.4 headers were synchronized, `MODEL_IMPLEMENTATION_RECIPES.md` and `H0_DATASET_CARD.md` were advanced to current design revisions, obsolete hard-coded `next P-372` workflow text was removed in favour of live Part-4/mini-log reconciliation, the active mini-log and preflight schema/executable were aligned to CR-3, and a fresh control receipt was generated.

This is a governance/consistency correction only. It does **not** create a fitted model and it does **not** demonstrate improved hit rate, winner accuracy, totals accuracy, Brier/log loss, CRPS, calibration or RMSE. Those remain empirical gates requiring an admitted H0 dataset, chronological training/tuning/calibration, untouched test evaluation and prospective shadow forecasts.

<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
## CR-2026.09.19-4 — universal three-source / timezone / terminal-state gate

**Current prospective authority:** **MDS-2026.09.19-v4.3 / CR-2026.09.19-4**.

This revision was opened after the P-469 false-final incident. A search-result summary was treated as if it proved a completed AFL result while opened live sources still showed the event in progress. CR-4 converts the correction into a cross-sport blocking control rather than an event-specific note.

### Implemented controls

1. Every new event/game log requires **at least three distinct reliable upstream source lineages**. Mirrors, syndicated copies, reposts, search snippets and generated summaries do not count as independent sources.
2. Where available, the verification set includes a field-owner exact-event source, another primary/team/participant source, and an independent high-quality secondary source.
3. Event identity now includes venue/host, official venue-local calendar date/time, IANA timezone, exact-date UTC offset, timezone-aware `Australia/Melbourne` conversion, correct AEST/AEDT label, and date-rollover state.
4. User-supplied start times are contract metadata until independently verified; discrepancies must be printed explicitly.
5. Event state is re-checked immediately before issue/refresh. Material source conflict produces `EVENT_STATE_CONFLICT` and fails closed.
6. Settlement requires **three independent reliable lineages** agreeing on exact event/date, explicit terminal state and final result. A score alone is insufficient and any credible live/in-progress source blocks settlement.
7. Search summaries/snippets can be discovery pointers only; they cannot establish finality.
8. Drive status transitions require a final pre-write state check and post-write read-back.
9. `prediction_preflight.py` was advanced to v4.3/CR-4 and now blocks fewer-than-three lineages, duplicate-lineage counting, invalid venue timezone, incorrect Melbourne conversion/AEST-AEDT label, incorrect date rollover, and non-pregame event state.
10. CR-4 regression suite: **15/15 tests pass**. This validates control behavior only, not predictive accuracy.

### Files updated

`README.md`, `METHOD.md`, `CONTROLS.md`, `RULES_GENERAL.md`, `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, `EXTERNAL_LOGGING_WORKFLOW.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `SCORING_AND_VALIDATION.md`, `AGENT_ROLE_AND_TASK.md`, all ten active `RULES_<SPORT>.md` modules, `FORECAST_PREFLIGHT_MANIFEST.md`, `prediction_preflight.py`, `test_prediction_preflight.py`, the active mini-log and the SHA-256 control manifest.

Historical cards retain their issued method/control version. No forecast probabilities or settlements are retrofitted by CR-4.

