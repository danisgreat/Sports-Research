# Google Drive exchange and mirror

**DRIVE-2026.10.17-v1 · MDS-2026.10.17-v20.2 · CR-2026.10.17-R2 · P-2026.10.17-v20.2.** Standing owner instruction, 17 October 2026: the owner's Google Drive folder [Sports Research](https://drive.google.com/drive/folders/1ChlwkiOvd8c4MTaLC5BvkLniWogrm8Lj?usp=drive_link) (folder ID `1ChlwkiOvd8c4MTaLC5BvkLniWogrm8Lj`) may be used to upload changes, prompts 1 and 2 may refer to it, and every authorised publication goes to both GitHub and this folder. This PROCEDURE release changes access, upload and publication steps only. Numerical policy, scoring, selection, IDs and log formats are unchanged.

## 1. What the folder is

The folder has two roles.

- **Upload exchange.** A session that cannot push to GitHub, such as a ChatGPT or Claude.ai web chat or a phone, puts its complete new or changed files in `uploads/` for a checkout session to import.
- **Mirror.** A copy of the repository's working controls, prompts and small records at their repository-relative paths, refreshed after each push. A chat with a Google Drive connector can read it.

GitHub `main` stays the canonical record and the authority for controls ([GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md), [CURRENT_RULES](CURRENT_RULES.md) §0). A Drive file is not a commit, a canonical record, a freeze or a publication of record until a checkout session imports it into a commit on `origin/main`. Where a Drive mirror copy and GitHub `main` differ, GitHub `main` governs and the Drive copy is stale.

## 2. Reading from Drive

1. **Controls.** Read controls from the declared authority first: one pinned GitHub `main` commit (`PUBLISHED_MAIN_PINNED`) or the local working tree (`LOCAL_WORKING_TREE`). The Drive mirror is an extra route when those reads fail or are truncated. Before relying on a Drive control, open `DRIVE_SYNC_RECEIPT.md` at the folder root. It names the mirrored commit and lists each mirrored file's bytes and SHA-256. Use a Drive control only when the receipt lists it as current. Record the Drive file name and ID, the receipt's commit and the read time with offset in the reading receipt. A file the receipt does not list as current is unverified: say so and prefer GitHub.
2. **Uploaded but uncommitted files.** Drive can supply what GitHub cannot (GITHUB_REFERENCE_PROTOCOL step 5): an active mini, an owner-entered prompt-1 block, a runtime pack or a returned attempt that was uploaded but not yet committed. Use one only after checking its identity and custody: exact file name, Drive file ID, upload or modified time, bytes, SHA-256 where the upload manifest records one, and the mini key or local event key it claims. Never treat a Drive copy as newer than a committed original without that evidence. Never merge two divergent copies by guessing. A conflict is a custody blocker under [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md).
3. **Runtime pack.** Prompt 1 may take `SR_RUNTIME_<commit>.zip` from the folder's `runtime/` subfolder when the owner placed it there ([FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md), CHAT-EXEC-v1). `ml.chat` still refuses a pack whose commit or code digest does not match the active releases.

## 3. Uploading changes

Any session that produced changes but cannot push may upload them.

1. Upload into `uploads/<YYYY-MM-DD>/<label>/`, where the label is the local event key or mini key plus a short tool name, for example `LOCAL-NHL-1017-G0003_chatgpt`. Never upload to the folder root or over a mirror copy.
2. Keep repository-relative paths as subfolders, for example `research/active_minis/<mini>.md`, so the importer knows where each file belongs.
3. Upload complete files, never fragments or diffs alone. Prompt 1 uploads the complete updated mini `.md` (MINI-v1), its RESEARCH_EXPORT CSVs and, when the cycle ran, the unchanged CHAT-EXEC upload zip. Prompt 2 uploads the new mini and its header-only execution manifest.
4. Add `UPLOAD_MANIFEST.md` with one row per file: repository path, bytes, SHA-256 (or `NOT_COMPUTED`), creation time with offset, prompt/task, local key, the GitHub commit SHA that was read, and the statement that nothing was committed.
5. Never upload credentials, cookies, API keys, raw odds captures or personal data the repository does not already hold. Do not change the folder's sharing.
6. An upload is not a freeze. Upload time never makes a CHAT-EXEC attempt `PRE_START_VERIFIED`; only `python -m ml.chat accept` with the actual clock or a pushed-commit clock does. Upload as early as possible so the owner can accept before the scheduled start.
7. Uploading under this section is not publication (COMMON_OPERATING_PROTOCOL). The prompt still returns the complete updated Markdown in its reply.

## 4. Importing uploads

A session with a checkout (owner PC or coding agent) imports uploads.

1. Download each upload folder into a new empty directory outside the repository and treat it as untrusted data. Check bytes and SHA-256 against the manifest. Quarantine mismatches; do not repair them.
2. Apply the normal gates: `python -m ml.chat accept` for attempt zips, prompt 4 for minis and cards, prompt 8 for control changes, plus identity and custody checks. Stage only the gated files, by path.
3. Commit, push to `origin/main` without force and confirm HEAD equals `origin/main`.
4. Record each imported file (Drive file ID, SHA-256, repository path, commit, disposition) in the importing task's receipt. Then rename the Drive upload folder with the suffix `__IMPORTED_<short-sha>` or `__QUARANTINED`. Never delete uploads; the rename stops a later session from importing them twice.

## 5. Publishing to both GitHub and Drive

Every authorised publication ends with both steps.

1. **GitHub.** Commit by path, push to `origin/main` without force and verify the remote SHA, as before.
2. **Drive mirror.** Copy every new or changed Markdown, CSV or text control, prompt and small record in that commit to the same relative path in the folder, using the committed (GitHub) bytes. Move each replaced copy to `_superseded/<short-sha>/` or the Drive trash; never delete permanently. Then rewrite `DRIVE_SYNC_RECEIPT.md` with the commit SHA, the time with offset and, for each mirrored file, its path, bytes, SHA-256 and Drive file ID.
3. **Files that cannot be mirrored.** List changed files that could not be mirrored in the receipt, with the reason (for example, too large for the connector) and an instruction to read them from GitHub at that commit. Move their stale Drive copies to `_superseded/<short-sha>/` so no reader takes them as current.
4. **Routes.** Exact-byte routes are preferred: Google Drive for desktop signed in to the owner's account, or a browser folder upload. A connector upload counts only when the Drive file size equals the committed size. Bulky data (`research/verified_history/`, `archive/`, `Previous Sports Results/`) stays on GitHub unless the owner asks.
5. **Drive unavailable.** The GitHub push still stands. Record the Drive gap in the task receipt and leave `DRIVE_SYNC_RECEIPT.md` unchanged, so readers can see the mirror is behind.

## 6. Limits

- Drive gives a chat no GitHub write permission and no new authority. Reading code on Drive is not executing ML ([ML_EXECUTION_PROTOCOL](ML_EXECUTION_PROTOCOL.md)).
- Do not sync the repository's `.git` directory through Drive. Synced `desktop.ini` files inside `.git/refs` corrupt references.
- No rule here permits fabricated files, uploads, readbacks or sync receipts. Report what was actually uploaded, mirrored or left behind.
