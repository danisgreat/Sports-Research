# Sports Research mini — pre-audit handover

**Mini:** `20261112D3C239297F`  
**Scope:** Complete cumulative conversation-local mini and all *currently available* associated scenario source/result files, integrity receipts and saved historical pre-update snapshots.

## Inventory

| File group | Count |
|---|---:|
| Cumulative Markdown mini-log | 1 |
| Reproducible scenario source scripts (.py) | 11 |
| Scenario/model output data (.json) | 11 |
| Prior integrity receipts (.json) | 6 |
| Historical pre-update mini snapshots (.md) | 6 |
| **Original files bundled** | **35** |

## Local custody checks carried out

- Exact latest mini SHA-256 independently recalculated and compared with last integrity receipt: PASS.
- All 11 sequential `G0001`–`G0011` card markers and closing markers: PASS.
- All 11 local cards contain A1–A9 audit sections: PASS.
- Footer reports 11 cards and next local key `G0012`: PASS.
- All 11 scenario Python sources compile without executing them, and all 17 JSON originals parse: PASS.
- Six receipt-to-receipt historical mini digest transitions, including the latest current file: PASS.
- Four stored scenario output/source hash claims with associated available files: PASS.
- Six historical pre-append snapshots contain the expected number of earlier cards: PASS.

## Critical limitations for the auditor

1. **No official issuance.** All cards were created and preserved in a chat-local draft, not in the GitHub repository. No canonical IDs, repo branch writes, commits, pushes, releases, certified model runs, frozen references, ledger registration, official lint passes, or settlements are proven by this package.
2. **Research scenario probabilities are not validated.** The scenario outputs have not been independently benchmarked or calibrated. Source citations and original fixture claims require external re-verification before any performance assessment.
3. **Incomplete historical custody coverage.** Only six historical pre-update snapshots and six prior integrity receipts are currently available. They do not constitute a complete, signed transaction-level audit chain for all eleven requests.
4. **One referenced output is unavailable.** `tennis_illustrative_model_output.txt` is mentioned in the mini but was not found among the current session files. The corresponding G0001 calculation script and JSON are included.
5. **Repository rules are external.** Relevant governing controls were referenced at `danisgreat/Sports-Research` pinned `main` commit `008cedc4ff469e7a808292aa3667a7bffe22e273`; source repository controls are not separately reproduced in this package.
6. **No recalculation of the sports forecasts has been certified by this export.** The Python programs are distributed for the auditor to inspect and execute as appropriate; they were syntax-checked only here.

## Suggested pre-audit order

1. Verify `audit/SHA256SUMS.txt` against the extracted files and compare with `audit/FILE_MANIFEST.csv`.
2. Review `01_mini_log/` and `audit/CARD_INDEX.csv`, starting with the latest `G0011` and its A1–A9 section.
3. Use `02_scenario_calculations/Gnnnn/` scripts + JSON to reproduce all uncalibrated diagnostics with their declared seeds and assumptions.
4. Check `03_integrity_receipts/` and `04_custody_snapshots/` for prior file preservation and readback claims.
5. Compare sporting claims to independently retrieved source data and verify actual first-play times before any forecast cohort, settlement or calibration claims.

**Current mini SHA-256:** `fc276d2766f3e0dbff35af58aed2c2957baced5e4ee5b0a7fbf7f90d71b837ae`

**Packaging policy:** The 35 original inputs were read but not modified. Manifest/report/verify script were created only for this export; the GitHub repository was not accessed or changed by the packaging step.
