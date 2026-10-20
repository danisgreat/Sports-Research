# Verification — import P-601–P-622

All checks below were actually run on 2026-10-21 (AEDT) unless marked otherwise. Helper scripts were kept outside the repository; the repository's own code was used only for `python -m ml primary verify-log --mini`.

## Import checks (VERIFICATION_PROTOCOL §3)

| # | Check | Result |
|---|---|---|
| 1 | Current state/status/Part 8 agree before import | PASS — highest P-600 / next P-601 / reserved P-518–P-522 / Part 8 zero originals; highest also recomputed from all `BEGIN CANONICAL RESEARCH` markers in Parts 1–8 |
| 2 | Exact frozen prefix in settled file | PASS — all six `PREDICTION_MINI_SETTLED` files start with their frozen mini; 79B3 prefix [0, 313,155) hashes to the declared `b7478342…ad7e`; all sources LF-only, no BOM |
| 3 | Inventory = new + exact existing + conflicts | PASS — 22 NEW_CANONICAL_EVENT, 0 existing, 0 conflicts; 1 HELD_INTAKE_DEFECT card section; addenda (2) and settlement revisions (26 imported, 1 held) accounted separately in SOURCE_UNIT_DISPOSITIONS.csv |
| 4 | Every imported core and source block compared | PASS — an independent script re-derived all 22 cores from the preserved `inputs/<mini>/ORIGINAL_MINI.md`, matched each inside its wrapper and at its IMPORT_READBACK range; all 28 addendum/settlement contents matched at recorded ranges; 24 package files re-hashed |
| 5 | Pre-import prefix byte-for-byte | PASS — Part 8 bytes [0, 5,047) equal the committed blob (`git show HEAD:…`); numstat 5,670 added / 0 deleted is supporting only |
| 6 | Sequential IDs; reserved untouched; reruns consume none | PASS — P-601…P-622 contiguous; no P-518–P-522 use; rerun test below |
| 7 | Status/next ID/queues reconcile | PASS after the state/status updates in this commit (highest P-622, next P-623) |
| 8 | Partial-write recovery | PASS (scratch test T3 below) |
| 9 | Markers (R19) | PASS — 100 markers in Part 8 after import, all balanced, no nesting, no duplicate revision keys, formats known |
| 10 | Pre-mutation recheck (R18) | PASS — HEAD, destination bytes/hash and planned suffix hash re-checked immediately before the append |
| 11 | Revisions (R17) | PASS — one parent chain per key: revision-1 (parent NONE) and, for P-603/P-604 corner keys and P-610/P-611, revision-2 (parent revision-1); no branches |

## Structural check of source minis

`python -m ml primary verify-log --mini`: 2026101710538263F6ED → `{'cards': 0}`; MELILL01 → `mini card markers orphaned/unbalanced` (real defect, held); 79B3 (frozen prefix), Q7N4, K9V4, X7Q4 → "a no-code mini needs one hand-derived analysis status per card" (wording non-conformance; hand check below). Hand check: one `MINI-LOG-FORMAT` marker per file; balanced local-key card markers (except the MELILL01 orphan); exactly one honest probability-method disposition per card (RESEARCH_ONLY_NO_MODEL ×11, ANALYST_PRIMARY_V1 ×11).

## Exercised cases (scratch copies of Part 8, never the repository file)

| Case | Expected | Observed |
|---|---|---|
| T1 valid plan | 22 new IDs P-601–P-622 | PASS |
| T2 apply, then exact rerun | rerun plans zero bytes, all units EXACT_EXISTING_SKIP | PASS — suffix 0 bytes, 50 skips, same IDs |
| T3 partial recovery (destination holds the first 9 wrappers) | plan only the remainder with the same IDs; result byte-identical to a full apply | PASS — 851,514 = 851,514 bytes, identical (after fixing a missing separator found by this test) |
| T3b torn write inside P-606 | block the batch | PASS — `PARTIAL_BLOCK` |
| T4 one byte corrupted inside imported P-605 | conflict | PASS — `CONFLICT … scoped recovery required` (after fixing the planner to hash actual destination bytes rather than trust the wrapper header — a defect this test found) |
| T5 concurrent edit between plan and apply | stop, file untouched | PASS — `PRE-MUTATION RECHECK FAILED: replan` |

## Publication

Staged by explicit path only (Part 8, CURRENT_STATE.md, GAME_LOG_STATUS_CURRENT.md, RESEARCH_SOURCE_REGISTER.md, this package). Not staged: `BASKETBALL.txt`, the owner's untracked `MINI LOGS TO BE SETTLED/` folder. Commit/push results are reported in the final message of the importing session (git history is the record).
