# Root-document archive receipt — 14 October 2026

**Authority:** LOCAL_WORKING_TREE, `main`, base `5d754a426e0d864db314b88a818036a039cf255e`. User instruction: archive all ten documents marked ARCHIVE in the root review and push the changes. This is an EDITORIAL organisation/navigation change. Published method/control/scoring/selection/prompt versions remain unchanged. Required current rules, state, contribution and verification instructions were read.

## Scope and preservation

Exactly ten originals move to `archive/root_documents_2026-10-14`; six current navigation documents receive limited link/index/changelog updates with before-edit copies retained. Separate link recovery preserves the original root context without altering dated evidence. Four MOVE candidates and the RULES_NHL merge candidate stay in place. The supplied-first extended prompt remains untracked, byte-preserved and outside staging.

Raw archived bytes are checked against the pre-move working snapshots. Their staged Git blobs will be checked against the original root blobs, separately from raw bytes, because `core.autocrlf=true` normalises CRLF to LF. No attribute file or runtime is added. See the [archive custody inventory](../../../archive/root_documents_2026-10-14/README.md).

## Verification

| Check | Result | Evidence / limitation |
|---|---|---|
| Exact archive scope | PASS | All ten approved originals are absent from the root and present in the archive; root Markdown 50 -> 40. |
| Archived raw working identities | PASS | Full byte comparisons for all ten originals against pre-move snapshots; SHA-256/length/line-ending inventory in archive README. |
| Navigation snapshots | PASS | All six snapshots match pre-edit bytes. |
| Existing historical text | PASS | HISTORICAL_LINK_INDEX prior prefix and prior CHANGELOG entries unchanged. |
| Hypothesis content | PASS | HYPOTHESIS_REGISTER changes only the retrospective-reference link target. |
| Protected logs/status/scoreboard | PASS | 9 full raw-byte SHA-256 checks match their pre-change values. |
| Unrelated untracked work | PASS | 1 pre-existing untracked file(s) retain their original hashes and are excluded from staging. |
| Allowed tracked/new paths | PASS | Every changed tracked path and newly created file belongs to the explicit allowlist; existing unrelated untracked work excepted. |
| New/changed authored local links | PASS | 800 target-file checks; external URLs and existing fragment validity not re-audited. |
| Archived original link-context map | PASS | 294 recoverable source/target mappings; 80 unavailable/out-of-scope legacy targets remain explicit. Original evidence text is not rewritten. |
| Authored navigation whitespace | PASS | git diff --check on six edited root documents. Frozen original whitespace is preserved. |
| Staged committed identities | PASS | All ten archived staged blobs and six navigation-snapshot staged blobs equal their original base-commit root blobs byte-for-byte (LF-normalised Git representation). |
| Publication | AUTHORISED_PRE_COMMIT | Normal push is authorised. Actual commit/remote verification occurs after this pre-commit receipt is frozen and is reported in the final operator response. |

No prediction, probability, rank, grade, P-ID, raw dataset, selection threshold, experiment criterion or certification status changes. This receipt verifies archival/navigation custody, not predictive skill.
