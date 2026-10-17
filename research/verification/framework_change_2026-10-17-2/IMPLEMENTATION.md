# Implementation — Google Drive exchange and mirror (DRIVE-v1)

**MDS-2026.10.17-v20.2 · CR-2026.10.17-R2 · P-2026.10.17-v20.2 · DRIVE-2026.10.17-v1 · PROCEDURE.** Owner instruction, 17 October 2026: "add a rule across the framework that the google drive can be used to upload the changes, https://drive.google.com/drive/folders/1ChlwkiOvd8c4MTaLC5BvkLniWogrm8Lj?usp=drive_link, and prompt 1 and 2 can refer to the google drive as well, push changes to both github and drive". Read at HEAD `b01b035b1` (equal to origin/main); the only uncommitted path was a peer's untracked `research/verified_history/2026-10-17-nba-gap-fill/`, which this change neither used nor staged.

## Before and after

| | Before | After |
|---|---|---|
| Sessions that cannot push (web chats) | Return the mini in the reply only; GitHub is read-only | May also upload complete files with an `UPLOAD_MANIFEST.md` to `uploads/<date>/<label>/` in the Drive folder; still return the mini in the reply |
| Prompts 1 and 2 | Name GitHub (REF-v1) as the only remote route | Also name the Drive folder for receipt-listed mirror reads, uploaded-but-uncommitted minis/packs, and uploads |
| Publication | Commit by path, push, verify the remote | The same, then mirror the committed bytes to Drive and rewrite `DRIVE_SYNC_RECEIPT.md` |
| Authority | GitHub `main` | Unchanged: GitHub `main`; a Drive file is never a commit, freeze or canonical record |

## Files

- New control: [GOOGLE_DRIVE_EXCHANGE_PROTOCOL](../../../GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md).
- DRIVE-v1 paragraph beside REF-v1: CURRENT_RULES §0, CURRENT_STATE, README, PROMPTS, ACTIVE_FILE_INDEX, CONTRIBUTING, COMMON_OPERATING_PROTOCOL. Publication steps: CURRENT_RULES §9, CONTRIBUTING step 7 and COMMON_OPERATING_PROTOCOL now end with the Drive mirror.
- Prompt 1: one header paragraph after the CHAT-EXEC-v1 paragraph, plus one clause in the mode line ("the only remote write allowed is a DRIVE-v1 upload to the Drive folder's `uploads/`"). Prompt 2: one paragraph after REF-v1 and the same clause.
- GITHUB_REFERENCE_PROTOCOL steps 5–6 point to the Drive route for uploaded-but-uncommitted files.
- Suite version P-2026.10.17-v20.2 in every prompt, README and DEPENDENCY_MAP; DEPENDENCY_MAP rows for prompts 1, 2 and COMMON add GOOGLE_DRIVE_EXCHANGE_PROTOCOL. CURRENT_STATE, CHANGELOG, `.gitattributes`.
- Originals: `archive/superseded_2026-10-17-2/` (19 files, ARCHIVE_HASHES.csv).

The DRIVE-v1 paragraph was not copied into METHOD, CARD_AND_LOG_TEMPLATES, PRIMARY_PREDICTION_PROTOCOL, RESEARCH_COMPLETION_PROTOCOL, VERIFICATION_PROTOCOL or ml/README, which also carry REF-v1. CURRENT_RULES §0 governs them, and COMMON_OPERATING_PROTOCOL carries the rule into every prompt.

## Drive folder at the start

The connected Google account owns the folder and can add files to it. It already held a copy of the repository's root documents and `ml/` and `research/` trees, uploaded on 17 October 2026 at about 08:08–08:10 UTC. Checked Drive sizes equal the committed sizes at `b01b035b1`; for example CURRENT_RULES is 40,894 bytes and CHANGELOG 130,614. The folder had no `DRIVE_SYNC_RECEIPT.md` and no `uploads/` subfolder. The Google Drive for desktop mount on this PC (`G:`) is signed in to a different account and does not show this folder, so connector uploads were the only write route available.

## Verification (measured)

See [VERIFICATION_CHECKS.csv](VERIFICATION_CHECKS.csv). Prompt consistency passed 24 tests. All eleven owner-entered prompt-1 Upcoming blocks are identical to the archived original. No edited control has CR bytes or control characters.

## Drive mirror of this commit

The mirror runs after the push, as section 5 of the protocol requires. Its result is recorded in `DRIVE_SYNC_RECEIPT.md` at the folder root, not here, because this file is committed before the mirror runs. Two committed files cannot be reproduced exactly through the connector in one call: prompt 1 (about 287 KB) and CHANGELOG (about 132 KB). The receipt lists those as "read from GitHub". Their stale Drive copies are moved to `_superseded/<short-sha>/`.

## Limits

- Drive adds an upload and read route only. It grants chats no GitHub write access, and an upload cannot make a CHAT-EXEC attempt PRE_START_VERIFIED.
- Connector uploads mirror the committed LF bytes and are checked by file size, not by a SHA-256 computed on Drive.
- Exact-byte mirroring of large files needs Google Drive for desktop signed in to the folder owner's account, or a browser upload.
