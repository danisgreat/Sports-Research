# Verification: learning pipeline (LEARN-v1)

**Tests.** Baseline before any change: `python -m pytest ml/tests -q` gave **311 passed**. Final, after the last code edit: **367 passed in 325.87s** (311 existing + 56 new: 18 store/feature/release, 8 model/Hedge/backtest/calibration, 5 governance, 1 end-to-end lifecycle, 24 prompt consistency). An intermediate full run that overlapped a code edit had one failure: `test_execution.py::test_feedback_is_recomputed_…`. The primary runtime correctly refused to publish a bundle because the `ml/` source changed during inference. Re-run on stable source, `test_execution.py` passed 19/19, and the final run above passed in full.

All new tests use synthetic EXAMPLE data. They establish mechanics: deduplication, quarantine, revisions, point-in-time invariance, reproducible releases, identical-game comparisons, policy equivalence with V3 Hedge, delayed feedback, coherent raking, ledger and registry chains, power-aware dispositions and review clocks. They do not establish predictive quality. No real data was ingested, ablated, backtested, studied or calibrated.

| Check | Result |
|---|---|
| Every rejecting check has a valid companion case | Yes (e.g. quarantine reasons vs. clean ingest; late freeze vs. pre-start freeze; worse/insufficient/eligible dispositions; illegal vs. legal registry transitions) |
| Prompt 1 Upcoming blocks (heading through the line before the first Read), HEAD vs working | 11/11 byte-identical, including the populated basketball, cricket, tennis and American football blocks |
| Prompt 1 diff | 26 insertions, 2 instruction lines modified (Mode/Writes line, one basketball validation line) |
| LEARN-v1 paragraph in prompt 1 | 11 identical copies, one per sport workflow (tested) |
| Dependency map vs prompt texts, versions, relative links | Pass (`test_prompt_consistency.py`) |
| Stale current version tags outside history | None (remaining v19.0 mentions describe the v19.0 release) |
| Archived originals | 29 files in `archive/superseded_2026-10-16-6/`; SHA-256 equal to HEAD blobs, rechecked |
| CHANGELOG | New entry prepended; prior 122,684 bytes are an exact suffix (hash compared) |
| Protected paths (`prediction logs/`, GAME_LOG_STATUS_CURRENT, model_shadow, issued_research, active_minis, scoreboard, daily) | Unchanged |
| `git diff --check` | Clean |
| Registry | `python -m ml registry verify`: chain intact, 8 entries; no PROSPECTIVELY_QUALIFIED model |
| File types | Python only under `ml/`; Markdown/CSV elsewhere; no JSON, notebooks, workflows or binaries |
| Out of scope and unstaged | Pre-existing `.gitignore` edit, untracked `.claude/`, `.github/`, `.vscode/`, `desktop.ini` sync files and cache folders |

Highest P-600 / next P-601, PRIMARY_HEDGE_MIX_V3, selection, scoring and formats are unchanged.
