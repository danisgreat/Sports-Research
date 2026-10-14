# Verification — ML integrity and prompt release 2026-10-14-5

**Scope:** user-authorised cumulative workshop/availability/prompt changes and non-force main publication. Current control CR-2026.10.14-R3; suite P-2026.10.14-v11.3. Method, scoring, selection, mini/settlement formats and canonical IDs unchanged. [Review](ML_WORKSHOP_REVIEW.md), [implementation](IMPLEMENTATION.md), [manual fixtures](FIXTURES.md).

## Executed evidence

| Check | Observed result |
|---|---|
| Initial workshop suite | 48 passed before integrity repairs; passing did not expose all edge cases. |
| Final workshop suite | python -m pytest ml/tests -q: **60 passed in 5.94 seconds**. No source code changed after this run. |
| Corrected report runs | python -m ml cards and python -m ml decision-lab completed successfully. Actual receipts include run/completion times, generating digest and input hashes. Code digest 645d4b4de2e1291ad1c7b9135b4f37fafa34aead2be3ba8f69939ecf5f13b442. |
| Decision coverage | 1,730 evaluation matches; feasible warm-up season labels 2021–2022 then evaluation 2023–2025; same-day actions precede close-feedback updates. All four policies finish below starting bankroll; no RL benefit established. |
| Historical source identity | All 29 completed model cards record generating digest 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be, matching runtime source preserved at commit 980e60178ec1fb9af09b78dce8bb2f6b4cbd8897. Original receipt HEAD was dirty; this is recovery, not independent execution verification. |
| Historical artifact inventory | 115 model files inventoried in HISTORICAL_ARTIFACTS.csv. All recorded snapshots for 28 score-grid model folders match the currently read archive hashes (112 artifacts). IPL has three files and no aggregate archive hash in its old receipt; limitation retained. |
| Completed index | Administrative reconstruction from actual artifacts/discovery: 172 competitions; 25 DEVELOPMENT_ONLY, 4 DATA_HOLD, 1 RUN_INCOMPLETE, 142 NOT_MODELLED. Interrupted external batch ended exit 127; cause is not established. No invented ODI result. |
| Prompt structure | All eight active prompts use COMMON_OPERATING_PROTOCOL and v11.3; prompt 1 has exactly eleven separate Upcoming game blocks and complete sport workflows. Rugby league/union have separate rules/source/archive routes. |
| Availability controls | Full official/both-team/eligibility/medical/provider/local-language escalation and release-window/final check retained. Genuine unpublished selections stay uncertain. Prior source review distinguishes actual retrieval from discovery/unavailable routes. No live game was supplied for a full player audit. |
| Preserved originals | All 22 pre-edit operating snapshots match ORIGINALS.csv byte counts and SHA-256. Old report/card bytes copied under the release archive before actual report reruns. Git attributes preserve those forensic bytes. |
| Protected records | All 161 PROTECTED_RECORDS.csv paths match their pre-edit raw byte counts and hashes, including canonical logs/status, issued cards, scoreboard, rank CSV and inactive supplied-first draft. |
| Staged custody | All 47 archived operating snapshots from changes 4–5 and all 115 historical model blobs match their recorded raw SHA-256 in the staged index. New implementation whitespace checks pass with CR-at-EOL recognised; immutable originals/proposals retain their existing whitespace. Active IDs/score summaries and older changelog entries were checked against exact pre-edit backups, with incidental wording-update drift restored before publication. |
| Publication controls | Exact path staging, content/type/size review, staged whitespace check, main fast-forward, push and fetched remote readback are recorded in the additive PUBLICATION_RECEIPT.md after actual publication. No force push or historical rewrite. |

The verification helpers were external temporary Python files, including sports_release_artifacts_20261014.py and sports_release_docs_20261014.py, plus inline standard-library link/hash checks. The artifact helper reads actual MODEL_CARD/receipt/archive data, records existing identities and reconstructs an administrative index; it does not fit a model or create missing results. The document helper replaces the live placeholder and aligns navigation/versions without filling historical draft numbers.

## Interpretive and operational limits

Manual prompt fixtures are walkthroughs, not live executions. Tests validate their stated mechanics, not official-source truth, model calibration, prospective skill or economic execution. Original generated model scores are preserved; they are not stamped with the repaired source. Source timing and field-owner admission, exact current inputs, endpoint/support approximation, independent calibration and prospective freeze/settlement still need evidence. All four numerical passes remain DATA_HOLD; none is admitted as a card input.

The source-stability guard detects changed disk source during a controlled run; it is not a container/environment attestation. Package reveal waits for all starts; per-event selective reveal is not implemented. The settlement helper computes first revisions; the operator must preserve and validate later revision chains. Actual pregame publication cannot be inferred from a git timestamp. Execution quote/fill/settlement-time realism remains unverified in the paper decision study.

The final freeze review also checks calculation completion: a fit that crosses the first start is rejected without writing a frozen file, and a legitimate pre-start failure records the real completion timestamp and NOT_ISSUED status. Both cases pass executed regressions. Full default whitespace output includes preserved CRLF/legacy originals; these are not reformatted to make a cosmetic check pass.

Earlier dated working reports and their placeholders remain preserved, with additive status clarification and the live state pointing to this completed review. No issued forecast, rank, grade, permanent ID or raw archive dataset is changed. The independent manual-card policy stays in force. The supplied-first proposal is preserved as a reference and is not adopted over current P4.
