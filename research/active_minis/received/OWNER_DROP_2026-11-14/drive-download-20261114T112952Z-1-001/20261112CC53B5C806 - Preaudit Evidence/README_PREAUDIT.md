# Pre-audit package — sports research mini 20261112CC53B5C806

**Source-of-truth mini:** `original_files/PREDICTION_MINI_RUNNING_LOG_20261112CC53B5C806.md`

**Packaging:** assembled from currently available conversation files on 14 November 2026; original files are copied **without modification**. The ZIP was built locally. No GitHub writes were performed during packaging.

**Mini identity:** `20261112CC53B5C806`; nine local event cards, `G0001`–`G0009`; next local key `G0010`; 9 pending events; no formal primary probabilities, canonical P-ID allocations, issuance, freezes or settlements.

**Current mini SHA-256:** `9da07f291fe663b9a5c41792613c0419fa0820081a6912c6564b9de7ae4ac5b5`; **size:** `246441` bytes.

## Folder structure

- `original_files/`: the complete current mini, 6 prior-stage mini snapshots, initial snapshot, available separate card drafts, model source scripts, model diagnostic outputs, evidence datasets, and append receipts.
- `extracted_cards/`: nine card blocks extracted *byte-for-byte* from the current mini, with a trailing newline if not already present. These are for audit convenience; the mini is authoritative.
- `SHA256_MANIFEST.csv`: SHA-256 and byte sizes of the two directories' files, plus the check JSON recorded before creating the ZIP.
- `PREAUDIT_CHECKS.json`: local inventory, structural checks, snapshot integrity and receipt checks.

## Event crosswalk

| Card | Fixture | Available script | Result JSON | Append receipt |
|---|---|---|---|---|
| G0001 | Svrčina vs Virtanen (tennis) | Yes | Yes | Yes |
| G0002 | Torpedo vs Arlan (ice hockey) | Yes | Yes | **Not found** |
| G0003 | Tirante vs Shevchenko (tennis) | Yes | Yes | Yes |
| G0004 | Geelong vs Perth (WNBL) | Yes | Yes | Yes |
| G0005 | Wonju vs Suwon (KBL) | Yes | Yes | Yes |
| G0006 | Kawasaki vs Saga (B.League) | Yes | Yes | Yes |
| G0007 | Motor České Budějovice U20 vs Liberec U20 | Yes | Yes | Yes |
| G0008 | Piros vs Altmaier (tennis) | Yes | Yes | Yes |
| G0009 | Tabilo vs Tirante (tennis) | Yes | Yes | Yes |

## Pre-audit exceptions / limitations

1. G0002 has no separate append receipt in the available files (although the card and simulation artifacts are present).
2. The request-intake Markdown table contains a stray malformed heading/row near original line 81, splitting the table. The unmodified original is retained; this package does not correct the source.
3. The mini is CHAT_LOCAL_DRAFT / NOT_ISSUED: no repository issue/freeze, canonical P-ID or settlement; numeric diagnostics are not calibrated primary probabilities.
4. Actual pre-start timing and some injury/lineup/medical/source-known-at fields are unresolved in multiple cards. Pre-audit should check those card-specific gaps.
5. Repository-side HEAD, remote state and code execution environment are not reproduced by this archive; source scripts and stored results are included but not rerun.

## Scope of verification

Checked the file inventory, extractable card start/end markers, sequence and footer, source-file SHA-256, append-receipt SHA against available snapshots, card-block preservation across six prior-stage snapshots, and JSON parseability. This is **not** an independent sports-data, code-reproducibility, model-calibration, operator-settlement or repository-state audit.

The original local mini is **not changed**; any corrections should be assessed and recorded as dated addenda under the governing workflow rather than silently overwriting source evidence.
