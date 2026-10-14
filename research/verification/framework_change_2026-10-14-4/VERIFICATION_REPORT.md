# Verification — availability research update

**Date:** 14 October 2026, Australia/Sydney. **Authority:** LOCAL_WORKING_TREE, branch `ml-workshop-2026-10-14`, HEAD `3ab6d27fedb177add7cca5b41b14346107688ce3`. **Publication:** local only; no commit or push by this task.

## Verified scope and behaviour

| Check | Actual result |
|---|---|
| Original snapshots | All 25 archived documents match the pre-edit raw SHA-256 values in [BEFORE_FILES.csv](BEFORE_FILES.csv) |
| Active-document delta | 25 declared existing documents changed; [path list](CHANGED_PATHS.txt). Prior dirty changes preserved through archived working originals |
| Prompt coverage | All ten prompt-1 Evidence sections contain AVAIL-2026.10.14-v1; all nine old timing sentences were replaced by complete-search-first instructions; the basketball block already relied on the common timing rule |
| Sport coverage | Eleven operative RULES_<SPORT> references apply the cross-sport protocol, including separate ice-hockey/NHL documents |
| Control surfaces | CURRENT_RULES, CURRENT_STATE, METHOD, templates and README carry CR-2026.10.14-R2 |
| Prompt surfaces | CURRENT_STATE, README, PROMPTS, prompt 1 and prompt index carry P-2026.10.14-v11.2 |
| Compatibility | Procedure uses existing evidence/lineup/A3/A8/C20 outputs; mini-log-7, mini-settlement-6, selection and scoring versions retained |
| Added/changed links | New relative destinations checked against each file's directory; final pass resolves the verification-report link after this file was created. Old unrelated historical links were not silently repaired |
| New text/readback | All changed/new documents loaded in UTF-8; no replacement characters; fences balanced; new-line whitespace checked against preserved originals with `git diff --no-index --check` |
| Procedure cases | Eighteen [manual fixtures](FIXTURES.md) assessed; legitimate confirmation/N/A/unpublished cases and skipped-search/projection/conflict/late-exposure failures distinguished |
| Source evidence | [SOURCE_REVIEW.md](SOURCE_REVIEW.md) distinguishes official opened/indexed/discovery/blocked routes; no blanket all-league verification claim |
| Protected records | All snapshotted files outside `ml/` and `research/model_shadow/` retain their original hashes, including logs, issued originals, rank CSV, state-status register, scoreboard, prior reports, supplied prompt and design |
| Concurrent workshop work | Hash changes were detected within `ml/` and `research/model_shadow/` during another writer's work; [observations](CONCURRENT_CHANGES.csv). Those files were never targets of this task's edits and remain in place |
| Repository HEAD | Unchanged from this task's starting HEAD; no branch switch, reset, staging, commit or push performed |

At one verification checkpoint, 252 of the 360 pre-existing protected-file hashes matched and 108 differed, all within the concurrently changing workshop/output scopes. An earlier observation recorded 109 differences. These are time-specific observations, not evidence that this task modified those files. The exact original inventory remains readable. Protected records outside those scopes passed throughout.

## Corrections caught by verification

The first inline edit encountered PowerShell stdin character conversion and stopped at a Unicode heading. The complete intended edits were reconstructed from exact originals, partial edits were matched against expected content, and a UTF-8 helper outside the repository applied them successfully. The final prompt contains the correct §, en-dash and arrow characters.

An archive-index filename initially collided with the preserved original README. The index was moved to [ARCHIVE_RECEIPT.md](../../../archive/superseded_2026-10-14-4/ARCHIVE_RECEIPT.md), and the original README was reconstructed and verified against its pre-edit SHA-256. All 25 originals now match exactly. No protected issued record was affected by either correction.

Helpers were inline standard-library filesystem/hash/link checks and `C:\Users\danie\AppData\Local\Temp\availability_update_20261014.py`; no helper script was added to the repository. They verify structure and custody, not source truth or prediction accuracy.

## Prediction review and limits

The workshop and model-output files were being written concurrently. The initial inspected implementation copy contained a results placeholder and no STATUS page at its first check; later generated artifacts changed during this task. The [implementation review](IMPLEMENTATION.md) attributes claims to those inspected documents and does not certify a final workshop run or its predictive effect. No ML code/test suite was changed or rerun for this source/procedure update.

The completed update addresses avoidable lineup/bench/absence gaps through mandatory research, current-route discovery, local-language escalation and final rechecks. No actual game was supplied for an end-to-end live player audit. A genuinely unpublished lineup or incomplete public medical disclosure can still remain unconfirmed after complete research. An incomplete search now fails C20; honest missing evidence is retained with supported scenarios or qualitative/NO_FORECAST handling.

External chats use PUBLISHED_MAIN_PINNED by default. This local procedure takes effect for those chats only after it exists in their pinned published revision. Local runs explicitly using this working tree can apply it now. No forecast, grade, P-ID or fitted-model promotion was produced by this task.
