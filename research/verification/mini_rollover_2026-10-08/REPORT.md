# October 8 mini settlement, review and Combined Log 7 rollover

Authority: `origin/main` and local HEAD agreed on `de0edc6b0822e88edb7fccd4d11bc33011b5cceb`; remote main was checked again before canonical writes. The user's correction selects the latest log, Part 6, for the mini import. The supplied local-only prompt governs the local settlement output; the user separately authorized repository import, learning implementation, rollover and publication.

## Sporting settlement

Twelve new event cards P-538 through P-549 are retained exactly, with 144 dated retrospective sections. Ranked rows: **26 WIN, 19 LOSS, 4 UNKNOWN_DEFINITION** (49 total). All twelve terminal sporting results were found. Eleven cards have fully gradeable sporting rows. P-540's four retirement-dependent rows require the original operator action/retirement terms; Mannarino's advancement does not settle them. Two additional unranked P-549 complementary rows have one win and one loss, separately counted.

| ID | Verified sporting final | Ranked row outcomes |
|---|---|---|
| P-538 | Florida 2-1 Los Angeles, regulation | W / W / L / L |
| P-539 | Berrettini 6-7(3), 6-1, 6-4; games 18-12 | W / L / L / W |
| P-540 | Mannarino 6-3, 2-2 RET | UNKNOWN_DEFINITION x 4 |
| P-541 | Zhou 6-4, 3-6, 7-6(4); aggregate 16-16 | L / L / W / W |
| P-542 | Melbourne 96-91 Adelaide | W / W / W / W |
| P-543 | Hanshin 2-1 Hiroshima after 11 innings | W / W / W / L |
| P-544 | LG 7-5 Doosan | L / W / W / L |
| P-545 | Kiwoom 5-3 Hanwha | W / L / L / W |
| P-546 | KT 9-3 Samsung | W / L / W / L |
| P-547 | SSG 6-3 NC | L / W / L / W |
| P-548 | KCC 103-98 Korea Gas, four quarters | L / W / W / W |
| P-549 | Foshan 1-0 Guangxi; HT 0-0 | L / L / W / L / W |

These are literal sporting threshold grades, not operator-certified settlements. Original operator definitions, actual-start evidence, complete pre-cutoff source-body custody and three independently audited collections were not backfilled. All imported cards remain performance-ineligible. Source URLs, retrieval times, raw-body sizes/hashes and unresolved collection lineage are retained in `source_capture_manifest.json`; its 18 bodies are local-only in the Downloads settlement directory. New-event fresh sources do not close the 32 historical sporting/contract gaps or 21 other certification/reference pointers. The selected carryover preserves all 53 prior records verbatim and adds twelve new operator/certification records: 65 total. No historical carryover has been falsely closed.

Ranking diagnostics: Rank-1 **6/11**, Rank-2 **6/11**, Hit@2 **9/11**, Wins@2 **12/22**, mean NDCG@2 **0.545455**, sporting winner calls **9/12**. These dependent small-sample rows do not measure calibration or baseline skill. Brier/log-loss comparisons are not manufactured from missing approved baselines. Qualitative cards have no invented probabilities.

## Review and implemented learning

The supplied NDCG@2 for P-539 (1.000) and P-548 (0.63093) used an incomplete ideal ranking. Full frozen-slate relevance gives **0.6131471928** and **0.3868528072**, respectively; the earlier four-card mean becomes **0.7500**. The original supplied figures remain in the exact archived mini. A tested diagnostic implementation prevents this error and leaves unresolved/push/void slates unscored pending a defined policy.

Endpoint/source review confirms P-543's official 11-inning result; a stale pregame mirror and a secondary 1-1 row were not used for a full-game winner grade. The NBL club recap has an internal 94-91 introductory typo and a 96-91 conclusion; official league reporting agrees with 96-91. This source conflict remains disclosed. KBO inning sequences support score reconstruction; no bullpen, fatigue or injury mechanism is invented from final score alone. The supplementary Kiwoom NewsPim article is AI-assisted and does not establish source independence. Retrieved market/fantasy/preview search results were excluded from all forecast, grade and mechanism calculations; user-supplied lines remain contract metadata.

Twelve testable hypotheses are hash-bound in `improvement_proposals.json` and the improvement register's **pending_retrospective_review_registers**. They do not alter the existing fixed fifteen-protocol experiment catalog. Their prospective cohort, candidate/comparator, source audits, power/sample plan and acceptance must be frozen before execution. No experiment has been run and no fitted parameter, qualification or model status has been changed from these twelve results. The implemented learnings are settlement arithmetic, source/endpoint missingness, full-slate ranking, dated-addendum custody and logging continuity.

## Canonical import and rollover

P-538 through P-549 were committed through the shared ledger lock into Part 6, using exact original event-section source substrings. Alias/readback footers, historical references and settlement addenda consumed no additional ID. Twelve separately journaled dated addenda retain their parent IDs. Duplicate addenda are idempotent and interrupted appends require recovery.

Previous active: `prediction logs/PREDICTION_LOG_COMBINED_6.md`. New active: `prediction logs/PREDICTION_LOG_COMBINED_7.md`. Highest committed: **P-549**. Next before and after empty rollover: **P-550**. The empty rollover changed no ledger bytes and consumed no ID. Part 6's opening prefix and its 141,740-byte special block remain unchanged; Parts 1 through 5 remain byte-identical. Configured header hashes cover generic current/prior active logs; future append projections carry their destination in the ledger. Recovery uses that recorded path rather than assuming the newest part.

`research/src/issue.py`, `workflow.py`, `acceptance.py` and model build receipts remain immutable. They are pinned numerical dependencies. Current entry points `research.operations.canonical_issue` and `research.operations.workflow` use isolated module namespaces to retain the frozen validator/transaction behavior with active-log custody and the common allocator. `log_card` defaults to the configured active file. Direct historical issuer/workflow CLIs are retained for reproduction, not current appends. Living docs/status and CI point to current operations; historical pointers and immutable control receipts keep their original meaning.

New selected control: **CR-2026.10.08-R2 / CONTROL_MANIFEST_2026-10-08-2.md**. Receipt 1 preserves the initial rollout checkpoint. Receipt 2 normalizes controlled runtime source/configuration line endings (LF/CRLF) and leaves raw evidence checks unchanged. The header and closing metadata retain their true R1 opening control; the living METHOD/status select R2. No additional ID is consumed.

## Verification and limits

Targeted rollover/research/addendum/metric regressions pass. The new readback verifies 12 exact original forecast substrings, 144 retrospective sections, 49 ranked rows, all 65 carryovers, legacy/active custody and all 18 local terminal bodies. Archive validation passes (407,796 canonical events), while retaining one documented source-body absence. All-log historical reconciliation passes with the new current carryover pointer. The original fifteen experiment measures pass.

A full working-tree test run has the two pre-existing model-build failures caused by the user's unrelated dirty `research/src/control_manifest.py`; strict custody reports the same acceptance failure, despite all 111 prior source bodies verifying locally. That file is preserved byte-for-byte and excluded from the commit. The isolated committed checkout passes **all 252 tests**, including the two line-ending tests. Selected R2 control verification passes **442 files, zero mismatches**. Current authoritative command receipts are in `committed_checks/control_r2`; earlier receipts retain their historical checkpoints. The working-tree R2 control check has exactly one mismatch, the preserved unrelated module. Clean-checkout evidence failures remain nonzero and are detailed below; no check was disabled or bypassed.

The original mini is 259,626 bytes, SHA-256 `972413bfa59b9a1a1807dc30e8e9bc50f02113ea9aab17ed57d1835ed060ebc8`. Local frozen original, settled copy, mapping, unresolved carryover and manifest are in `C:\Users\danie\Downloads\Mini Settlement - P-538 to P-549 - 2026-10-08`. The exact full provided source is also retained as `provided_mini.original.bin`. No original forecast or source was deleted.

## Committed-checkout publication limits

The committed checkout verifies canonical imports/projections, generic active-log custody, legacy Part-6 custody, dated addenda, current reconciliation, the unchanged fifteen experiment measures and the selected control freeze. Strict custody still fails: 59 of 111 historical bodies are published and 52 remain absent. The all-log verifier fails on the ignored `kfu_owner_20261005T110514549862Z_7a0771636e07.body`. Archive validation fails on the ignored `Previous Sports Results/_football_research/afl_api.json` (10,687,193 local bytes). These are pre-existing publication omissions, not fabricated recaptures or disabled checks. The same local archive check passes with its retained source gaps disclosed. Consequently **the operational rollover is verified, but full evidence/publication verification remains incomplete**. The unrelated local control-module edit remains byte-identical and uncommitted.
