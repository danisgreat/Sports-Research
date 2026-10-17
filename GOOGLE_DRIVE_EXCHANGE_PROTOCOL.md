# Google Drive drop box (optional)

**DRIVE-2026.10.17-v2 · MDS-2026.10.17-v21.0 · CR-2026.10.17-R3 · P-2026.10.17-v21.0.** Owner instructions, 17 October 2026. The owner's Google Drive folder [Sports Research](https://drive.google.com/drive/folders/1ChlwkiOvd8c4MTaLC5BvkLniWogrm8Lj?usp=drive_link) (folder ID `1ChlwkiOvd8c4MTaLC5BvkLniWogrm8Lj`) may be used to upload changes. Nothing is ever required to be pushed or mirrored to it. DRIVE-v2 withdraws DRIVE-v1's mirror, sync receipt and push-to-both requirement. This PROCEDURE release changes no numerical policy, scoring, selection, ID or log format.

## 1. What the folder is

The folder is an optional drop box. A session that cannot push to GitHub, such as a ChatGPT or other web chat or a phone, may put its complete new or changed files in `uploads/` for a checkout session to import.

The folder is not a mirror and not a source of controls. It may still hold an older copy of repository files. That copy is unmaintained, and nothing reads it as authority. Controls always come from the latest `main` branch on GitHub ([GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md), [CURRENT_RULES](CURRENT_RULES.md) §0). A Drive file is not a commit, a canonical record, a freeze or a publication until a checkout session imports it into a commit on `origin/main`.

## 2. Uploading (optional)

1. Upload into `uploads/<YYYY-MM-DD>/<label>/`. The label is the mini key or local event key plus a short tool name, for example `LOCAL-NHL-1017-G0003_chatgpt`.
2. Upload complete files, never fragments or diffs alone. Prompt 1 uploads the complete updated mini `.md`; prompt 2 uploads the new mini.
3. Optionally add `UPLOAD_MANIFEST.md`: one row per file, with the intended repository path, the time with offset, the prompt, the local key and the GitHub commit SHA that was read.
4. Never upload credentials, cookies, API keys, raw odds captures or personal data the repository does not already hold. Do not change the folder's sharing.
5. An upload is not publication and not a freeze. The prompt still returns the complete updated Markdown in its reply.

## 3. Using an uploaded file

1. **Reading an upload.** Drive can supply what GitHub cannot (GITHUB_REFERENCE_PROTOCOL step 5): an active mini that was uploaded but never committed. Check its exact file name, Drive file ID, upload time and the mini key it claims before using it. Never merge two divergent copies by guessing; a conflict is a custody blocker under [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md).
2. **Importing.** A checkout session downloads the upload into a new empty directory outside the repository and treats it as untrusted data. It then applies the normal gates (prompt 4 for minis and cards, prompt 8 for control changes) and commits by path. Afterwards it may rename the upload folder with the suffix `__IMPORTED_<short-sha>`. Never delete uploads.

## 4. Limits

- Drive gives a chat no GitHub write permission and no new authority.
- Do not sync the repository's `.git` directory through Drive. Synced `desktop.ini` files inside `.git/refs` corrupt references.
- No rule here permits fabricated files, uploads or readbacks.
