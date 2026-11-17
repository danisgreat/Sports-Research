# HPPV-v1 registration — adopted 17 November 2026

Owner-authorised implementation of the Historical Prospective Performance Validation
Framework proposal, against main `4e0cb198c50230d8e2abf2f1a976d92338301520`.
The proposal's eight stages are adopted as the separate **Track H**. These thresholds
are registered **after historical outcomes were observed**, not preregistered before
the events. No historical finding is a prospective certification.

## Frozen population and original-record rule

P-001–P-685, all 685 cards and all 3,150 contract rows in CARD-TRAIN-v1 run
2026-11-16-1. Its original input hashes and receipt remain binding. Preserve
the input Git blobs at the registered base commit, so later current-log growth
cannot alter or invalidate this frozen historical population. Full Git history
is required for regeneration. The original training CSVs and audit must match
the registered commit byte for byte. Preserve
3,082 admissions (1,291 probability, 1,791 outcome-only), 68 exclusions, all
losing, missing-p, unresolved and abstaining records. Census membership must not
depend on outcome. Unknown request-level abstention is reported as unknown.

The training rows and original source references are recovery candidates, not proof
of original issuance. Recover the earliest unaltered forecast, retain its exact raw
capture and SHA-256, and independently review a hash-bound literal transcription
of its card, row ID, rank, exact contract and original p. No revised forecast may
replace it. Preserve original methodological version; date-based eras are only proxies.
The module never rewrites canonical IDs, forecasts, ranks or source settlements.

## Evidence tiers

| Tier | Requirement | Use |
|---|---|---|
| A | Unchanged original, independently timestamped before verified actual first play, exact event and endpoint, no post-issue information | Strongest historical pre-event assessment; independent outcome still required for scoring |
| B | Recovered contemporaneous original, but timing or information integrity incomplete | Historical sensitivity, never headline skill |
| C | Preserved forecast/result context, original pre-event issuance unverified | Descriptive history and qualified learning |
| D | First recorded at/after first play, or known outcome exposure | Retrospective research only |
| E | Original forecast, identity or settlement too incomplete for reliable scoring | Retained, unscored with reason |

Default is C (unverified, not proven late). Incomplete original contracts are E.
All qualification revisions use the append-only, hash-chained evidence ledger.
Every superseded record is revalidated; every old classification remains in the
qualification history. Authentication of external captures is a reviewer task;
hashes establish identity, never original publication time. A written document date,
author-controlled git date or a post-event GitHub import cannot supply that proof.

## Admission and statistical protocol

Independent sporting results and documented grading rules are mandatory. Exact
event, selection, signed line, period, unit, overtime, probability basis and origin
must match the original, outcome and baseline. Score only decisive binary endpoints.
Pushes, voids, unresolved, unattainable and three-way endpoints remain unscored;
conditional decisive probabilities are never interpreted as unconditional ones.
User-supplied endpoints form the primary comparison. Analyst alternatives and unknown
origins cannot enlarge it. Retain duplicate contracts but score the earliest verified
issuance once; event IDs link repeated P-IDs from the same actual game.

Primary statistic: paired Brier advantage = baseline Brier minus original-forecast
Brier, averaged across eligible supplied contracts **within actual event**, then
equally across events. Two-sided 95% Student t interval across event means. Report
Brier skill score, log loss (only log loss clips p to [1e-15,1-1e-15]), event-weighted
calibration, Rank-1/Rank-2 accuracy, numeric coverage, explicit abstentions and unknown
request-level abstention frequency. Date, competition and connected-team block means
provide sensitivity intervals and block counts. Intervals with fewer than two units
are unavailable, never zero-width proof. Event n assumes independence between games;
block counts expose reduced effective independent units. Subgroup and chronological
tables are exploratory, separated by original method, era proxy, sport, competition,
contract family, actual event date and baseline class. No multiple-comparison
confirmatory claim is permitted. A pooled verdict covers only the observed policy mixture.

Benchmarks must be same-event/same-endpoint, sports-only and market-blind. Either
independently frozen no later than forecast issuance, or explicitly retrospective
sporting-data reconstruction. Require reviewed byte-bound recipe, feature, training
label and hyperparameter cutoffs no later than the information cutoff, itself no
later than original issue time. Retrospective selection/tuning must be outcome-blind.
Never reinterpret a constant 0.5 or approximate training base rate as verified
pre-event evidence. Reconstructed and frozen comparisons are separately reported.

## Historical verdict gates

All 685 cards/3,150 rows accounted for; Tier A plus independently verified decisive
outcomes and same-contract benchmark; at least 100 distinct paired events;
paired Brier advantage at least 0.01; game-level 95% lower bound strictly above 0;
known original methods separated and no unresolved admitted integrity defect.
These reporting thresholds do not guarantee a sport-specific conclusion.

| Verdict | Deterministic rule |
|---|---|
| HISTORICAL_EVIDENCE_INSUFFICIENT | No independently qualified decisive events |
| HISTORICAL_PRE_EVENT_ACCURACY_MEASURED | Authentic pre-event accuracy measurable but no paired benchmarks |
| HISTORICAL_SKILL_INCONCLUSIVE | Paired evidence exists but fewer than 100 events, or interval cannot resolve gates |
| HISTORICAL_PRE_EVENT_SKILL_SUPPORTED | At least 100 paired events, mean >=0.01 and lower 95% bound >0 |
| HISTORICAL_PERFORMANCE_NOT_SUPPORTED | At least 100 paired events and upper 95% bound <0.01 |

Score tables describe the exact methods, dates, competitions and endpoints covered.
Tier A alone is not evidence of comparative skill. Historical accuracy without p
does not become a probability forecast.

## Track P and model-study separation

ONE-CHAT-v3 / v27.0, its sealed registry, benchmark, evidence threshold, frozen
assessment prefix, sequential test and **400-game horizon remain unchanged**.
No historical observation, evidence count or verdict enters Track P. Report H and P
beside each other, never pool them. Query the current Track P score rather than
copying a stale count into a generated historical assessment.

The separate strict chronological ML backtest uses only timestamp-verified features
and training labels available before each evaluation cutoff, with a fixed recipe.
No hyperparameter tuning uses test outcomes. It is a retrospective algorithm study,
not proof that the model generated the original ChatGPT forecast. Existing
CARD-TRAIN-v1 approximate-time studies keep their existing evidence labels.

## Reproducibility and revisions

`python -m ml historical-pre-event run --out <new-directory>` writes an immutable run.
`verify --run <directory>` checks all input/output hashes, complete output inventory,
and byte-identical regeneration of every decision, score and report. The root
assessment files are the initial no-new-evidence run; retain them as the frozen
starting point and use new directories for future runs. No inferred Tier A or
reconstructed original probabilities are admitted by this implementation.
