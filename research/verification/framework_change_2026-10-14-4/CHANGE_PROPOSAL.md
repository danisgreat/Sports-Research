# Change proposal — comprehensive availability research

**Date:** 14 October 2026, Australia/Sydney. **Authority:** LOCAL_WORKING_TREE, branch `ml-workshop-2026-10-14`, base HEAD `3ab6d27fedb177add7cca5b41b14346107688ce3`.

## User instruction

“review the changes in regards to improving the prediction, can you update the sources of information for the confirmed starters and bench players and injury list for all the sports leagues where needed because certain sport leagues, so that when a game log is launched, it never comes to having the lineups infomration as being unconfirmed, At the very least ensure teh rules do comprehensive research to confirm this wehna game log requests for a game, especially when the game is for a competition that may be obscure”

## Findings and intended behaviour

Existing CURRENT_RULES §5 and prompt 1 require confirmation/recheck but do not define a complete, cross-sport search before an operator reports LINEUP_UNCONFIRMED. SOURCES §3.11 has useful fallbacks, with dated access claims and gaps for obscure competitions. Rosters, injury reports and starting-role evidence can be conflated; probable starters and incomplete bench lists cannot be promoted to confirmation. No source can guarantee that every league publishes all three fields before every request.

Implement the user's minimum enforceable requirement: mandatory comprehensive research for both sides and each relevant field, with authoritative sources, original club releases, eligibility/discipline, local-language discovery, structured fallback and final late-change recheck. Preserve truthful missingness and supported mixture/qualitative/NO_FORECAST handling when sources remain absent. An incomplete search fails the process audit.

## Scope and class

Class: **PROCEDURE + source maintenance**. Existing card evidence receipt, lineup-state metadata, A3/A8 and C20 hold the more detailed work. No new top-level field, probability/selection rule, score or mini schema is introduced. Control becomes CR-2026.10.14-R2; prompt suite becomes P-2026.10.14-v11.2. Method MDS-2026.10.12-v11.0, scoring SCV-2026.10.12-v7, selection SEL-2026.10.12-v3 and formats remain unchanged.

Allowed changes: ROSTER_AVAILABILITY_PROTOCOL.md; CURRENT_RULES/STATE, METHOD, SOURCES, templates, verification, prompt 1/index, PROMPTS, README, ACTIVE_FILE_INDEX, CHANGELOG, operative RULES_<SPORT> references and two synthetic examples. Add this dated change folder and byte-preserved originals under archive/superseded_2026-10-14-4. No publication is requested or performed by this task.

Preserve the pre-existing workshop and its dirty changes, prior implementation/design reports, all model code/artifacts, logs, issued originals, raw archive data, hypotheses, grades and IDs. Original working bytes, including unpublished workshop changes, are the archive baseline: [BEFORE_FILES.csv](BEFORE_FILES.csv). Other protected file hashes: [PRESERVE_FILES.csv](PRESERVE_FILES.csv). Starting inventory: [STATUS_BEFORE.txt](STATUS_BEFORE.txt).

## Verification and rollback

Verify archived originals against their exact raw working hashes; check only intended additions/replacements against those snapshots; read all changed files; verify new relative links and current version surfaces; ensure each of ten sport sections applies the protocol; exercise positive/negative/edge-case manual fixtures; check whitespace and preservation hashes. These are process checks, not prospective predictive validation.

Rollback only this change's byte deltas against its preserved baseline, keeping later concurrent edits and all previous workshop work. Never reset the branch, replace it with main, or overwrite another writer's active changes.
