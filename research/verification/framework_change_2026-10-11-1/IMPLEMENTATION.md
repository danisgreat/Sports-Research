# Implementation: better prompts, trustworthy logs and measurable predictions

**Release:** MDS-2026.10.11-v10.0 / CR-2026.10.11-R1 / SCV-2026.10.11-v6. **Date:** October 11, 2026, Australia/Sydney. **Source revision:** `2d6d86350ce4d6bd9f4ae0f34a42351e71ff0e4b`.

This release replaces all eight active prompts and aligns their authority, selection, templates, settlement, scoring and verification instructions. It implements document controls, not a fitted prediction system. Existing cards, Combined Logs, raw result CSVs, dated retrospectives and original probabilities remain unchanged. New numerical baselines and shadows have no prospective results yet.

## 1. Evidence and interpretation

The [October 11 retrospective](../retrospective_2026-10-11/RETROSPECTIVE_REPORT.md) and [cohort tables](../retrospective_2026-10-11/COHORT_TABLES.md) report 20 new settled cards, 34/40 primary wins, zero original-gate passes, mechanically protected top-two pairs on every card, no paired baseline rows and only one ISO week. Its seven proposals RET-01–RET-07 are the main input here. Earlier dependencies come from the [October 9 register](../../../FRAMEWORK_RETROSPECTIVE_2026-10-09.md), [learning index](../../../LEARNINGS_INDEX.md) and [hypothesis register](../../../HYPOTHESIS_REGISTER.md).

These are source-reported results; this change does not re-audit every sporting result. A high hit rate on easier chosen lines is not evidence of improved event forecasts. Conversely, the retrospective's in-sample climatology skill of −0.03 does not prove there is no possible out-of-sample skill. The correct conclusion is **predictive improvement is not established**. Four high-confidence losses do not themselves establish miscalibration, and numeric blame shares in individual retrospections are not identifiable estimates.

## 2. What is implemented now

| Area | Before | Active v10 behavior |
|---|---|---|
| Prompt usability | Game core hidden in mini-creation prompt | Complete game prompt with all sport blocks; separate creation task |
| Authority | Current-main-only wording conflicts with local authority; opening headers treated as current | Local/pinned-remote provenance explicit; historical opening snapshots reconciled to current entries/state |
| Primary ranking | Descending p and minimum-joint Rank 2 contradict | P_ORDER_V2 primary order; alternatives explicitly frozen shadows; policy cohorts separated |
| Candidate quality | Mandatory four numeric probabilities | Up to four supported rows; qualitative/NO_FORECAST preserved without fabricated numbers |
| Evaluation | Hit-rate headline with no pregame comparator | Same-line frozen league baseline field, paired proper-score headline or NOT_COMPUTABLE |
| Settlement | Missing evidence forced into VOID | UNRESOLVED_EVIDENCE queue; genuine void conditions distinct; original grades preserved |
| Sensitivity | Rank flips ignored below 0.25 SD | Any-size flip disclosed; large adjustment separately labelled |
| Time | Research completion used as pregame proxy | Cutoff, completion, actual issue, recheck and scheduled lead separate |
| Import | Three-card sample and incomplete duplicate/recovery handling | Full original-core/block comparison, exact-prefix check, idempotent mapping and scoped recovery |
| Review | Loose cohort/calibration/probability comparisons | Coverage, policy, timing, evidence, exact-line baseline and dependency-aware diagnostics |

These changes are authorized integrity/measurement repairs, not promotions based on 20 results. The original 62%/4-point gate, 58% floor and 90% selection ceiling remain provisional. The numerical values have not been optimized or declared validated.

## 3. All seven latest recommendations

Status vocabulary: DOCUMENTED_ACTIVE means instructions/templates changed and checked; SHADOW_READY means recording instructions exist but no empirical test has run; DATA_PENDING means the required source work has not been performed; BLOCKED_DESIGN means a predictive acceptance design still lacks required inputs. None means predictive success.

| ID / decision | Implementation and files | Acceptance and limits | Status / next task |
|---|---|---|---|
| RET-01 — adapt | Prompt 7 and LEAGUE_PROFILES require a defined NBL regular-season 2025-26/2026-27 source cohort, coverage/endpoint checks, old/new profile comparison and effective date; prompt 1 flags stale profiles | No universal +16.8 correction from three games. No acceptance merely because mean-error CI includes zero or mean absolute z falls in 0.6–1.0. Compare refreshed versus old prior prospectively on identical events with predeclared bias tolerance and paired proper/score-error metrics | Freshness control DOCUMENTED_ACTIVE; NBL collection/profile replacement DATA_PENDING; prospective promotion BLOCKED_DESIGN |
| RET-02 — adopt measurement, refine comparator | SELECTION_RULES §9, game/settlement templates and scoring freeze BASELINE_LEAGUE_V1, same line/endpoint/action, source window and independent league-only parameters; scoreboard shows paired coverage first | Existing RET-02 floor of 40 events/8 weeks is minimum collection, not power proof. Exact recipe and original p required; zero paired rows means NOT_COMPUTABLE. Baseline recomputation discrepancy triggers repair/versioning, not deletion of inconvenient baseline fields | DOCUMENTED_ACTIVE; prospective rows 0; actual skill untested |
| RET-03 — shadow only | Original gate plus SHADOW_GATE_RET03 excluding same-quantity alternatives, same numerical thresholds, explicit alternative key; no retrospective PASS relabels | Preserve original registration. A pass-rate target is feasibility, not skill. Compare paired-event selection/coverage/calibration with adequate PASS/UNSTABLE counts and a predeclared meaningful effect. No promotion just because a wide CI contains stated p | SHADOW_READY; ≥8 weeks and ≥30 shadow-PASS as original floor; formal power/precision design pending |
| RET-04 — shadow, not hard primary rule | Quantity keys, SHADOW_R2_RET04 and separate SHADOW_R2_XCARD6 frozen with probabilities/baselines/joints; primary p ordering remains unambiguous | Different quantity does not guarantee independent or non-covering losses. Score exact losing sets; keep unconditional versus both-decisive denominators consistent. Do not compare a realised frequency to a Wilson interval around an assumed mean as though it were observed binomial evidence | SHADOW_READY; original 40-event/4-week floor retained as collection target; promotion BLOCKED_DESIGN |
| RET-05 — adopt labels/coverage, not suppression | Actual issue-time lead band and verified event state are separate on card, settlement and scoreboard; late requested research remains retained | Monitor 90% buffered pregame over next 40 requested events as operational target with full denominator, not a selection filter. Official delays may allow PREGAME despite late scheduled lead. No dropping hard/late requests to improve metric | DOCUMENTED_ACTIVE; future monitoring unrun |
| RET-06 — adapt timing and evidence | Official KBO terminal box first; stale route retained with fallback and a planned/actual retry around 12 h, source status/time explicit | Do not wait 12 h when an official final is already available. Do not call MyKBO independent automatically or label an unexecuted retry completed. Monitor ≥8 of next 10 at A as source-quality target; source failures trigger fallback/evidence gap, not forced grade | DOCUMENTED_ACTIVE procedure; route availability/retries/10-game target not tested here |
| RET-07 — adopt integrity checks | C4 checks all result masses, C5 actual gate arithmetic/alternative, C8 vocabulary; examples include missing mass, absent alternative and non-standard context | Zero violations is a correctness target; do not remove true checks because outcomes are inconvenient. Missing facts produce NOT_ASSESSABLE, not invented PASS. Forty future cards monitor execution, not present acceptance | DOCUMENTED_ACTIVE; worked fixtures checked; 40-card live compliance unrun |

## 4. Further high-value recommendations and learning controls

| Work item / origins | Concrete action | Proof/next dependency | Status |
|---|---|---|---|
| FC10-01 probability versus dependence ordering; PRD-01/02/04 | Freeze candidate generator/universe, deduplicate contract keys, primary p order, retain supplied exclusions and shadows | Rank inversion/partial-universe fixtures; future same-event policy comparison | DOCUMENTED_ACTIVE, predictive effect untested |
| FC10-02 missing outcome handling; GOV-03/04 | Separate unresolved field, event state, sporting definition and operator certification; retain evidence bounds | Bound-crossing, missing provider, unknown rule fixtures; no historical regrade in this release | DOCUMENTED_ACTIVE |
| FC10-03 adjustment sensitivity; PRD-05 | Flag every rank flip, list all adjustments, preserve unadjusted top two, avoid double effects | Below-0.25-SD flip walkthrough; prospective calibration still unknown | DOCUMENTED_ACTIVE |
| FC10-04 exact import and recovery; GOV-01/02/05 | All-block mapping/readback, original-prefix comparison, explicit historical headers, idempotent partial recovery | Manual duplicate/existing-card-new-addendum/interruption scenarios; actual importer is manual | DOCUMENTED_ACTIVE; not an automated transaction system |
| FC10-05 field capture; SRC-02/03/07 | Decisive extracts/times, exact settlement field, named capture action, actual scheduling status and dated environment reachability | Future source probes and real capture receipts needed; quote/git timing does not independently prove pregame publication | DOCUMENTED_ACTIVE; live source matrix refresh DATA_PENDING |
| FC10-06 archive integrity; SRC-05, DST-01/03/13 | Logical CSV records, missing versus zero, season/stage/event-grain/OT checks, field coverage and explicit priors | Prompt-7 targeted KBO extras/NBL freshness audits; no data rewrite now | DOCUMENTED_ACTIVE; data repairs DATA_PENDING |
| FC10-07 proper measurement; EVL-01/02/03/04/05 | Frozen same-row baselines; event then week aggregation; distinct policy/timing/rank cohorts; coverage sensitivity; no CI-containment proof | Toy paired-score arithmetic checked; original-cohort skill remains unavailable; sample-size inputs must be supplied before promotion | DOCUMENTED_ACTIVE; live paired evidence absent |
| FC10-08 process diagnosis; R1 and learning-register cautions | Review wins and losses alike, report knowability, no invented blame percentages or hindsight rank replacement | Synthetic loss with process/model uncertainty; no rule changes from one game | DOCUMENTED_ACTIVE |
| FC10-09 endpoint/coherence; DST-02/06/07/08/10/11/14 | Allowed ties, exact period/provider, unconditional pushes, proper chase overshoot, team-specific directional margins and no unsupported engine claims | Sport-block/endpoint check matrix; live competition conditions still require browsing per card | DOCUMENTED_ACTIVE documentation; calibrated distributions not built |
| FC10-10 source lineage; SRC-04 | Keep UNKNOWN/SHARED_FEED rather than counting websites; collect field-owner lineage evidence for active leagues | Needs current source-owner documentation and actual investigation, no assumed three-source quorum | DOCUMENTED_ACTIVE disclosure; lineage audit DATA_PENDING |
| FC10-11 concise card; PRD-08 | About 650-word decision block, full appendix; no competing byte target as a hidden gate | Format inspection; measure real future readability before changing target | DOCUMENTED_ACTIVE |
| Fitted/overdispersed models; DST-04/05/12/15, ML-01–10, ENG-01–03 | Maintain design only until explicit scope authorizes a runtime and adequate point-in-time datasets | Chronological TRAIN/TUNE/CALIBRATE/untouched TEST and future shadows; exact model artifact, reproducible arithmetic, calibrated endpoints and proper-score comparisons | SUSPENDED_MD_ONLY; no resurrection of old code claims |

## 5. Sequence, ownership and deliverables

1. **This release — repository operator, prompt 8:** archive originals; align rules/scoring/prompts/templates/examples; register amendments; verify and publish. Acceptance is documented in VERIFICATION_REPORT, not sports performance.
2. **Next archive cycle — repository operator, prompt 7:** audit NBL current coverage and KBO extras; produce field-level source/coverage receipts and reviewed profile candidates. Do not silently change parameters used by already-issued cards. Live source probing/collection is a separate execution task, not claimed done by writing this plan.
3. **First future v10 mini — research operator, prompts 2/1:** record current versions, full request inventory, frozen baseline where possible, actual issue state and shadow alternatives. First actual issued v10 card is the prospective collection start; do not use this document's date as a fabricated issue.
4. **After each event — settlement operator, prompt 3:** capture exact fields, preserve original expectations, score original and shadow rows separately, retain gaps. Import operator uses prompt 4 and full-block readback.
5. **After enough new evidence — analyst, prompt 6:** report feasibility/coverage after 40 events; formal skill only when pre-registered same-scope sample/precision and weeks suffice. Eight weeks is not automatically enough. Existing RET floors remain explicitly floors.
6. **Any promotion — repository operator, prompt 8:** new prospective protocol/version and evidence-based decision. No threshold/weight tuning on the evaluation window. Failed designs are revised for a new future cohort; old failed results stay visible.

No wall-clock completion dates are promised for data collection or predictive tests. Lead time depends on fixture frequency, source availability and the required independent event/week sample.

## 6. Hypothesis and rollback policy

[HYPOTHESIS_REGISTER](../../../HYPOTHESIS_REGISTER.md) records FC10-BASELINE-v1, FC10-GATE-v1, FC10-PAIR-v1 and FC10-PROFILE-v1 alongside unchanged original RET/XCARD text. They freeze recording/comparison requirements now; incomplete power/equivalence inputs block promotion and must be amended before its evaluation cohort begins. Historical data inspected in these retrospectives are development data.

Rollback uses a forward document change with reason, version and effective time. Do not undo issued forecasts, grade history or publication history. Invalid baseline/source data suspends the affected comparison and is repaired under a new version, retaining excluded counts. A privacy/source-access failure stops that route, not evidence retention. A format/custody mismatch blocks the dependent write until corrected without changing earlier bytes.

## 7. Compatibility and boundaries

New formats mini-log-6/mini-settlement-5 add baseline, timing, candidate policy, shadows and unresolved evidence semantics. In-progress older minis finish unchanged; disclose missing fields instead of backfilling. A legacy no-evidence VOID stays a literal historical grade until a separate authorized settlement-review addendum, and does not silently become a new v10 result. Existing next canonical ID and active log remain unchanged by this release. Synthetic example IDs allocate nothing.

Validation here is a review of document consistency, sample arithmetic, fixtures, links, scope and archived copies. It is not a live source probe, executable importer test, model fit, calibration test or prediction-outcome validation.
