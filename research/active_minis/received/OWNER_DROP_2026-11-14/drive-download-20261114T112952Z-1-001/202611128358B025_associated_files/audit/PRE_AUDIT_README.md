# Sports-Research chat-local mini — pre-audit handoff

**MINI_KEY:** `202611128358B025`  
**Prepared:** 2026-11-14T20:27:11+11:00 (Melbourne local time)  
**Source authority:** read-only `danisgreat/Sports-Research` `main`, pinned in the mini to commit `008cedc4ff469e7a808292aa3667a7bffe22e273`. The repository itself was **not modified** for this package.

## Primary file

- `research/active_minis/202611128358B025.md` — **authoritative chat-local mini copy**. SHA-256: `a87c1cec9a5fcdea84ea22973864863f8fca4336ea8ea10ce974821be4c82498`. Original byte content retained; no edits were made during packaging.
- The original loose convenience file under `/mnt/data/PREDICTION_MINI_RUNNING_LOG_202611128358B025.md` matches this copy byte-for-byte; it is **not duplicated** in the ZIP.

## Contents

- **11** local research draft cards, G0001–G0011, with intake records. Next unused local key: `LOCAL-202611128358B025-G0012`.
- **11** Python calculation source files, mapped to individual events in `EVENT_INDEX.csv`.
- **3** JSON numeric output files (G0009, G0010, G0011). Earlier scripts have no separate JSON result files available in the current sandbox; their calculation documentation is within the mini itself.
- **8** historical mini snapshots: one initial setup snapshot and seven `before_G####` snapshots. Intermediate snapshots `before_G0002`, `before_G0003`, and `before_G0005` were **not available** in the current sandbox and are not invented or recreated.
- `EVENT_INDEX.csv` — event-to-supporting-file map.
- `STRUCTURAL_CHECKS.json` — automated, limited **pre-audit** structural checks and explicit non-checked areas.
- `FILE_MANIFEST.csv` — all packaged files with SHA-256 and sizes, excluding manifest and checksums themselves.
- `SHA256SUMS.txt` — relative-path checksums for every ZIP member except the checksum file itself.

## Preliminary integrity results (not a formal audit)

- Structural pre-check: **PASS**. `mini-log-10` format marker once; one cards section; one footer; 11 unique and paired draft begin/end markers; intake rows MATCH-001–MATCH-011 exactly once.
- Current active mini and loose convenience file: **byte-identical**.
- Seven historical `before_` snapshots contain a total of 48 earlier card blocks. Prior card text compared against current mini: **all exact matches**.
- Python files: **11/11 compile syntactically** (not executed/revalidated during packaging).
- JSON files: **3/3 parse**.

## Scope, custody and outstanding formal checks

This is **CHAT_LOCAL_ONLY / NOT_PUBLISHED / NOT_REPOSITORY_ISSUED** research; 11 draft records do **not** constitute 11 certified prospective predictions. The mini reports no canonical P-IDs, no owner-repository import, no independent settlement, no official model reference-stage execution, no freeze or linter receipts, and no GitHub commits/pushes. Local research numbers are explicitly uncalibrated scenario diagnostics. Do not treat source URLs in the mini as separately archived original source captures; those captures, official `ml` execution outputs, and external evidence bundles have not been supplied as independent files in this chat.

**For the receiving auditor:** Verify file integrity using `SHA256SUMS.txt`, independently open source links and verify as-of evidence, check timing/actual event state and input contamination, inspect scripts and recompute outputs, compare numerical claims to the card, validate contract endpoints/OT/availability, and then apply the repository's actual current procedures for audit, official freeze and (if separately authorised) canonical import. This package itself does not confer permission to write to GitHub.
