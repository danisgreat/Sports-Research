# Legacy root files (GOV-06)

Moved out of the repository root on 2026-10-09 so the root holds only documents, configuration and the canonical CSV.

| File | What it is | Status |
|---|---|---|
| `subagent_parser.js` | Browser-console helper that listed Panasonic/Foster's/Ansett Cup season pages for an AFL pre-season scrape | Unused; no code references it |
| `afl_preseason_data.json` | Output of that scrape (564 KB). Only the retired legacy builder (`research/custody/implementation_2026-10-01/…/build_afl_all_years.py`) read it; the current `research/src/build_afl_all_years.py` does not | Unused historical data |

Seven zero-byte placeholders (`apply_preseason_all.py`, `audit_preseason_results.py`, `build_and_apply_preseason.py`, `fetch_all_preseason.py`,
`test_afl_matches.py`, `test_aflw_matches.py`, `test_parser.py`) were deleted: they contained nothing, and the empty `test_*.py` files were
collected by pytest as vacuous tests. `validate_austria_bundesliga.py` moved to `research/src/` (run it from the repository root; it reads
`Austria_Bundesliga_Basketball_CSVs/` and `Previous Sports Results/` by relative path).
