# Sports Research repair implementation report

**Updated:** 28 September 2026 (Australia/Sydney)

**Starting assessment:** 6.0/10 in the [comprehensive review](SPORTS_RESEARCH_COMPREHENSIVE_REVIEW.md). That is the review-time system/document rating, not forecast accuracy.

**Disposition:** integrity and measurement repairs implemented; historical card corrections and prospective performance validation remain gated by missing evidence.

## What changed

### Archived-rule cleanup and custody

At the user's explicit request, ten superseded standalone rule snapshots were deleted from `archive/drive_settlement_2026-09-21/before/`. Their exact former paths, byte lengths and SHA-256 digests are in the [deletion receipt](ARCHIVED_RULE_DELETION_RECEIPT.md). The active root rule files, historical audit reports, issued mini log, settlement sources and migration records were retained. The deletion is therefore auditable from the receipt and Git history; it does not silently erase the review trail.

### Strict legacy extraction

The settled-row extractor now uses exact normalized contract joins, quarantines conflicting card/rank groups instead of selecting a last occurrence, and retains unattributed occurrences in a separate file. It records decision-field provenance and eligibility reasons while keeping the output explicitly historical and learning-only. The current rebuild reports 1,188 retained rows from 308 cards, 556 with a parsed probability, 1,347 raw graded occurrences, 72 unattributed rows and 83 quarantined conflict groups. No extracted row is performance-eligible. P-518 and P-520 conflicts stay quarantined; P-519, P-521 and P-522 remain live-issued legacy rows.

### Versioned prospective evidence contract

Added `prospective_record.schema.json`, `RECORD_SCHEMA.md` and an initially empty `prospective_records.json`. Each decision now has a defined event, event-cluster, forecast, card, target, contract and settlement-revision identity; complete participant and contract terms; point-in-time cutoff and issue times; a hashed distribution; W/P/L(/V) masses; explicit frozen preferred-side and selection-policy fields; baseline provenance and training cutoff; model/control/code hashes; observed result and source receipts; pairing references; target weight; and missingness. The semantic validator requires the schema field set, and a regression test checks that the JSON Schema required set and executable required-field set stay aligned.

`tools/semantic_validation.py` rejects incomplete probability vectors, malformed times and hashes, mismatched baselines, wrong complement/push identities, invalid nested and joint event geometry, incoherent distribution queries, non-increasing ranks, and evidence receipts that do not substantiate their stated event/result. Shape validity is not eligibility: pregame timing, frozen selection, three distinct issue lineages, three distinct terminal lineages, matched baseline and verified terminal result are separately required.

`tools/prospective_eligibility.py` admits only a unique decision that passes those semantic and performance gates and exactly matches the human ledger's card, rank, contract, result, probabilities and baseline. Push/void-capable vectors remain outside the current binary baseline ledger rather than losing their mass. RM-1 q must reproduce from the shipped coefficient and source-code hashes and remains labeled row-calibrated, not joint.

### Scoring, extraction and status controls

`tools/calibration_report.py --eligible-only` now ignores eligibility claims as proof: it requires a strict structured-record join, exact identity/contract/result/p/baseline matches, verified binary outcome and RM-1 hash/reproduction checks. Its paired baseline requires the same event, target, contract, horizon and cutoff, and groups uncertainty by event-cluster ID. The default CSV report stays a legacy mixed-row diagnostic.

`tools/skill_baseline.py` labels its principal forecast and baseline Brier values as event-weighted, and distinguishes the decision-weighted row diagnostic. `tools/evidence_status.py` reads the versioned structured record file and the current RM-1 build instead of relying on the older permissive settled-row CSV. README, current rules, scoring, numerical program/register and research status pages now state that prospective gates are at zero, no scope is approved for performance claims, the freeze remains in force, and RM-1 q values cannot be multiplied into joint probabilities.

The 5 September pregame eligibility register now clearly identifies itself as a historical snapshot. Its two missing 12 September local references are explicitly marked unavailable; the current eligibility policy is linked without pretending that it recovers the missing audit text.

Each of the ten sport-specific rule-module headers and two active league-reference headers now point to the same competition/target capability table and live evidence-status command, so sport pages cannot imply a validation status that the central register does not support.

The live status command currently reports:

| Gate | Current progress | State |
|---|---|---|
| C-BASELINE-SKILL | 0 verified decisions / 0 cards | Accruing |
| T-RM1-PROSPECTIVE | 0 qualifying cards / 0 eligible decisions | Accruing |
| C-MARKET-BENCHMARK | 0 decisions / 0 cards | Accruing |
| C-EVENT-UNIVERSE | 1 universe, 12 events, 0 carded or skipped | 12 dispositions still missing |
| C-MLB-SHADOW | 0 frozen / 0 settled | Accruing |
| C-SPORT-SHADOW | 0 rows frozen / 0 settled | Accruing |
| C-RULE-FREEZE | Baseline and RM-1 gates open | In force |

These are workflow counters, not findings about predictive performance.

### P-518–P-522 source reconciliation

Created a reconciliation register and source readback for all five issued IDs. They preserve the registered card IDs, compare the exact official events, record confirmed final-score/line-score facts, identify contradictions in the settlement/process narrative, and state what evidence is still needed. The register keeps all five IDs reserved and out of Part 5; the next canonical ID remains on hold.

The exact-event checks found a correct P-518 final score but incorrect supporting process details; P-519's issue event is AFLW match 8942 while the settlement cites 7412; P-520's official KBO scoreboard supports the 6–2 final but a durable game ID and complete source receipt are missing; P-521's ACB issue event 105378 is verified as 110–104; and P-522's issue event 105380 is 80–81 while its settlement cites 105379. Exact source links, verified fields and limitations are in [the readback](P518_P522_EXTERNAL_SOURCE_READBACK.md) and [the CSV register](P518_P522_RECONCILIATION_REGISTER.csv).

These are spot checks, not complete three-lineage resettlements. Only one upstream lineage is preserved for the current MLB extraction; several ACB endpoints may be the same lineage; and the issue-time identity, start-state, cutoff, baseline and preferred-selection evidence has not been reconstructed. The active P-518-onward mini log was left byte-for-byte unchanged at the previously archived worktree SHA-256 `C4D497BF339010EAE2FF5DF23A2D76290983585671666E74791618342565CF30`; the staged index snapshot is separately retained. No settlement correction was authored from the partial source set.

## Fix the remaining open gates in this order

1. **Close each P-518–P-522 source packet.** Retrieve the exact event from three independent upstream lineages for both issue-state claims and terminal settlement. Record source URL, retrieval time, exact event ID, upstream lineage, relevant fields and response hash or permitted snapshot. Verify the event state and actual start independently. A repeated page or syndicated copy is not a new lineage. If three lineages are not available, preserve the explicit limitation instead of claiming full verification.
2. **Append a settlement revision, never edit the issued forecast.** For each card, copy issued probabilities, rank, baseline and missingness from its frozen source; do not replace a missing baseline with 0.500. Recompute the exact contract result and score from the verified result, attach the source-field map, old/new values and reason, and preserve the original text. A process-detail correction does not itself change the outcome label.
3. **Reconcile canonical surfaces.** Only after the source packet and revision pass readback, update Part 5, `GAME_LOG_STATUS_CURRENT.md`, the reconciliation register and active mini-log pointer as a coordinated change. Retain aliases and source receipts. Confirm no issued probability, q, rank or baseline changed, then rebuild extraction and review row-by-row differences. Until this passes, keep P-518–P-522 reserved, do not reuse their IDs and do not advance the next ID.
4. **Resolve the declared event universe.** For each of the 12 currently missing events, record either a card that was frozen before start or a timestamped, reason-coded skip. Do not retroactively declare a card from an event already underway. Reconcile coverage to 100% only when every row has a valid disposition.
5. **Run the prospective issue-to-settlement pilot.** Before its first event, freeze the population, exact targets, preferred-side policy, baseline version/training cutoff, model and code hashes, primary event-weighted paired score, uncertainty method, stop rule, missing-data treatment and date window. Declare the universe first; issue only after pregame gates pass; retain skipped/missed events; settle from three lineages; add each complete decision to `prospective_records.json`; and require an exact ledger join. Maintain shadow records separately from card inputs.
6. **Review at preregistered checkpoints.** The current 100-decision/30-card baseline, 25-card RM-1 and 150-row/game shadow thresholds are review points, not proof thresholds. Apply their existing decision rules only after valid records reach them. Retain inconclusive and negative results. Do not alter model coefficients, widths, caps or rank overrides while `C-RULE-FREEZE` is in force.

## Verification performed

- Full root suite: 79 tests passed. Full tools suite: 169 tests passed, including schema/semantic parity, malformed-array handling, strict extraction, conflict quarantine, baseline identity, probability geometry, RM-1 code/coefficients, frozen preferred selection, and forged CSV eligibility flags.
- Repository hygiene: 688 tracked files checked, 0 problems. The strict five-card mini-log audit reports every blocking field printed on P-518–P-522; that is a completeness check only and does not verify truth, pregame timing, source lineage or eligibility.
- Current extractor rebuilt to the counts in `research/settled_rows_2026-09-28/generated/README.md`; the P-518 working file hash stayed unchanged at `C4D497BF339010EAE2FF5DF23A2D76290983585671666E74791618342565CF30`.
- The v1 schema parses as JSON and its required field set matches the semantic validator. The empty prospective register validates; `--eligible-only` returns no rows. The default 556-row calibration output is labeled a mixed historical diagnostic, has no exact paired baseline rows, and is not a performance claim.
- `tools/evidence_status.py --json` confirms zero qualified prospective records and the freeze remains in force.
- The old 27 September manifest is superseded; the current 28 September VALIDITY_REPAIR manifest is named in `METHOD.md` and verified as the current content receipt. Historical per-card mini-log receipts remain unchanged.

Passing these checks establishes that the repaired pipeline rejects the demonstrated data/identity failures. It does not establish forecast skill, fully correct the five recent settlements, or complete a prospective validation cycle.
