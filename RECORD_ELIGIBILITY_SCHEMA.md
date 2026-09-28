# Prospective record and eligibility contract

**Current publication state, 2026-09-28:** zero verified performance-eligible decisions. All issued cards are `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`; `C-RULE-FREEZE` remains in force. This Markdown contract replaces the current-tree pointers to deleted `research/settled_rows_2026-09-28/RECORD_SCHEMA.md` and `CAPABILITY_STATUS.md` (parent Git blobs `587c7e39cca30fef3dd62c6d90e0b047888d2f00` and `a6ef62b0d5ccf016bfb0358686939253470c3f04`). It states what must be recorded; it does not claim that a machine validator or a prospective dataset exists in this Markdown-only tree.

## Grain and required fields

One row is one **issued target decision at one forecast freeze and one settlement revision**. A card can have several rows, and a sporting event can have several cards. Do not count correlated rows as independent events. Every prospective row needs:

| Group | Required content |
|---|---|
| Identity | Schema version; official event ID; event-cluster ID; immutable forecast ID; card ID; decision ID; target ID; contract ID; sport, competition, season, and official participant IDs. Names alone are insufficient identity keys. |
| Contract | Measure, period, line, side, units, overtime, draw, push, void, action and version terms, including exact settlement rules. |
| Freeze and selection | Timezone-aware input cutoff, latest input availability, issue time, verified actual start, rank, horizon, selection-policy version and `preferred_at_issue` frozen before the result. Do not derive preference from p or outcome later. |
| Forecast object | Distribution identity/type/SHA-256; exhaustive W/P/L masses and V when applicable; each mass in [0,1], total 1; stated p; q and its declared semantics. RM-1 q is `ROW_CALIBRATED_NOT_JOINT`. |
| Baseline and build | Literal issue-time `BASELINE_P` status, probability/vector if actually derived, exact event/target/contract/horizon/cutoff match, training cutoff, method/control/manifest/build hashes and ranking-model version/hash. Missing remains `NOT_YET_DERIVED`. |
| Source receipts | Issue and terminal reference/URL, retrieval timestamp, response hash, exact event/state/result and upstream lineage. Three pages copying one feed are one lineage. |
| Settlement revision | Observed value, W/P/L/V result, terminal state, revision ID, superseded revision when corrected, field-level source map, and missingness reasons. Issued p/q/rank/distribution are immutable. |
| Pairing and cohort | Complementary-pair ID, covering-pair ID, target weight, event-cluster weight and exclusions. Score a forced pair's frozen preferred choice once. |

## Admission decision

Require latest available input ≤ cutoff < issue < actual start for a pregame record, plus at least three independent pre-issue identity/state lineages and three independent post-start terminal lineages. A live-issued card retains its actual horizon and cannot be converted to pregame. Confirm exact contract, event and settlement revisions; compare every number and rank with the frozen issue. Require a same-contract baseline measured without future information. A valid-looking row alone never grants eligibility. Any missing timestamp, identity, baseline, independent lineage, or build receipt fails closed with an explicit reason.

Push-capable contracts need a vector-aware scoring method; binary p-versus-q comparisons remain blocked. RM-1 q is a ranking score, so multiplying q values or treating q as the card's event probability is invalid. The 100 decisions / 30 cards, 25 RM-1 cards and 150 shadow games mentioned in historical plans are review checkpoints, not proof thresholds. Evidence of prospective skill additionally needs a point-in-time cohort, a frozen comparator, chronological evaluation, calibration and uncertainty, critical-slice checks, and untouched blind shadow observations.

## Current capability by scope

| Scope | Historical evidence | Prospective approved state |
|---|---|---|
| Human card method and RM-1 | Historical mixed and selected diagnostics; 29 hindsight seed decisions in [Skill Baseline Ledger](SKILL_BASELINE_LEDGER.md), Brier 0.2461 versus population 0.2360 | None; zero eligible prospective rows |
| TB-1-MD | Aggregate historical evaluation and preregistration in [Validation Evidence](VALIDATION_EVIDENCE.md); game-level rerun inputs absent in current tree | Provisional reference only; no card performance claim |
| Reduced-feature sport models | Dated retrospective work for selected league/target cohorts in Git history, with mixed outcomes and selection limitations | No approved issued or performance model; no transfer to neighboring leagues |
| AFLW, ACB, NPB/KBO and other unsupported competition targets | Some card diagnostics or nearby-sport constants; no exact validated population baseline in the disputed P-518–P-522 record | `NOT_YET_DERIVED` where missing; no prospective scoring admission |

The deleted historical extractor reported 1,188 non-conflicted rows from 308 cards, including 556 probability rows, plus 72 unattributed rows and 83 card/rank conflicts. Those are parser counts, **not** verified unique decisions; its strict gate yielded zero eligible rows. The old `0.2268` retrospective score must not be called a prospective decision Brier. These historical counts are not regenerated in this tree.
