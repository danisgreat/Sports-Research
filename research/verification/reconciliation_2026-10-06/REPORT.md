# October 6 CSV Duplicate Cleanup and Archive Verification Report

## 1. Summary

A total of **102 redundant root-level CSV files** (51 ODI International + 51 Danish Metal Ligaen Ice Hockey) were verified against their exact canonical archive copies in `Previous Sports Results/`, confirmed for byte-for-byte SHA-256 match, and recycled.

No archive data was altered or deleted. Exactly **13,481 data rows** across 102 archive datasets (and their parallel category mirrors) remain preserved, verified, and active.

Both build scripts (`build_odi_international_all_years.py` and `build_metal_ligaen_all_years.py`) have been updated to write solely to their canonical `Previous Sports Results/` archive destinations, preventing future re-emergence of root export duplicates.

---

## 2. CSV Cleanup Audit

| Recycled Root Folder | Canonical Archive Destination | Category Mirror Destination | Files Recycled | Preserved Data Rows |
|---|---|---|---|---|
| `ODI_International_CSVs/` | `Previous Sports Results/Cricket One-Day Format/ODI International/<year>/<year>_games.csv` | `Previous Sports Results/Cricket One-Day Format/Men's ODI International/<year>/<year>_games.csv` | 51 | 4,428 |
| `Danish_Metal_Ligaen_Ice_Hockey_CSVs/` | `Previous Sports Results/Ice Hockey/Danish Metal Ligaen/<year>/<year>_games.csv` | `Previous Sports Results/Ice Hockey/Metal Ligaen/<year>/<year>_games.csv` | 51 | 9,053 |
| **Total** | — | — | **102** | **13,481** |

- **Verification Protocol:** Prior to removal, every single 1975–2025 file in the root directory was verified to have an identical SHA-256 cryptographic hash compared to both its destination and mirror locations in `Previous Sports Results/`.
- **Post-Removal Readback:** Following removal, all 102 target archive files and 102 mirror files were rechecked on disk. Every SHA-256 hash remained completely unaltered.
- **Recovery:** Files were sent to the Windows Recycle Bin and can be restored if needed.
- **Audit Artifacts:**
  - Plan: [`csv_cleanup_plan.json`](csv_cleanup_plan.json)
  - Execution Receipt: [`csv_cleanup_receipt.json`](csv_cleanup_receipt.json)
  - Script: [`cleanup.ps1`](cleanup.ps1)

---

## 3. Preservation of In-Tree Category Mirrors

In accordance with repository guidelines established in previous reconciliations (e.g. `BSL` and `Austria Basketball Bundesliga`):
- `Previous Sports Results/Cricket One-Day Format/ODI International/` and `Previous Sports Results/Cricket One-Day Format/Men's ODI International/` both remain intact as parallel category mirrors, ensuring full backwards compatibility for any query or script expecting either nomenclature.
- `Previous Sports Results/Ice Hockey/Danish Metal Ligaen/` and `Previous Sports Results/Ice Hockey/Metal Ligaen/` both remain intact.
- No root `*_CSVs` folders remain in the workspace.
