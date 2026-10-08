# Canonical import of settled mini P-550..P-556 — 2026-10-09

Mode `CANONICAL_SETTLED_MINI_IMPORT`. Base: local HEAD = `origin/main` = `1ffbd9f52c63926bf7b1f5df9796e37477c1e9a3` before any write. Active log: `prediction logs/PREDICTION_LOG_COMBINED_7.md`.

## What was imported

Seven original local cards were committed through the repository's transactional allocator (`research.operations.log_card commit`), then seven dated settlement/R1–R12 addenda were appended under the same IDs (`log_card addendum`; addenda consume no IDs). The allocator returned the expected IDs in order, with no collision and no duplicate:

| Canonical ID | Local ID | Event | Card commit record | Addendum commit record |
|---|---|---|---|---|
| P-550 | P-550 | Edmonton Oilers @ Anaheim Ducks (NHL, 2026020055) | `4e3960ae…269d` | `8911e3e7…bb33` |
| P-551 | P-551 | Adolfo Daniel Vallejo vs Valentin Royer (ATP Shanghai) | `11356c78…cbbb` | `108cb7c5…441a` |
| P-552 | P-552 | Cairns Taipans vs Brisbane Bullets (NBL27) | `268e5641…9628` | `63c57572…db17d` |
| P-553 | P-553 | Kobe Storks vs Chiba Jets (B.PREMIER, 506439) | `70ba263c…a987` | `752c8014…41dbf7` |
| P-554 | P-554 | Nagasaki Velca vs Shinshu Brave Warriors (B.PREMIER, 506440) | `5c6e3b6c…f4ab` | `c566319d…2805` |
| P-555 | P-555 | Vít Kopřiva vs Zizou Bergs (ATP Shanghai) | `8717fabe…f449` | `581a9b8e…3045` |
| P-556 | P-556 | Cameron Norrie vs Dalibor Svrčina (ATP Shanghai) | `d4744889…8d58` | `dfa37198…a18e` |

Hashes above are abbreviated; full 64-hex hashes, transaction IDs and projection/source hashes are in `CANONICAL_ID_MAPPING.csv` and `CANONICAL_IMPORT_MANIFEST.json`. Local ID equals canonical ID for all seven (identity mapping, no renumbering). Allocator `next-id`: **P-550 → P-557**.

## How originals were preserved

* Each card's retained source (`research/issued_research/P-5xx-<tx>.original.txt`) is the **byte-exact slice** of `PREDICTION_MINI_RUNNING_LOG_P-551_ONWARD_FROZEN.md` (SHA-256 `fc1c3b45…0415`, 175,096 B), located by heading and verified to be a substring of both the frozen mini and the settled mini (which begins with the frozen bytes). P-550's slice is also byte-identical to the older `P126_P549_ORIGINAL_MINI_FROZEN.md`. Nothing was reconstructed from summaries.
* The projection body in the Combined Log is the card text with only the original `## P-5xx —` heading line replaced by the allocator's canonical heading (the repository rejects a nested ID heading); all forecast text, probabilities, ranks and timestamps are unchanged. The 28 original `p_card` values were each re-found in the preserved card text.
* Each addendum source is the byte-exact settlement section from `PREDICTION_MINI_SETTLED_P-550_P-556.md` (SHA-256 `62447b56…05bfe3`). The projected addendum body adds one dated "canonical import note" (identity mapping; `PENDING_IMPORT` label superseded) followed by the section text verbatim.
* Analysis status label for all seven: `HISTORICAL_IMPORT_UNCALIBRATED_ORIGINAL_STATE_PRESERVED`; performance status `RESEARCH_ONLY_NOT_CERTIFIED` (allocator default). Sporting result, operator certification and performance eligibility remain separate; no event is made performance-eligible.

## Settlement diagnostics (re-derived from the imported addenda, not copied)

7 events, 28 ranked rows: **15 W / 13 L**, 0 push / void / no-action. Rank-1 wins 4/7, Rank-2 wins 3/7, Hit@2 5/7, Wins@2 7/14, mean NDCG@2 (full-slate ideal) **0.5162**, winner calls 4/7. All match `SETTLEMENT_MANIFEST.json` per event and in aggregate.

## Repository changes

* `prediction logs/PREDICTION_LOG_COMBINED_7.md`: 359,145 → 491,009 bytes, append-only (884 insertions, 0 deletions).
* `research/canonical_ledger.jsonl`: 78 → 106 records (+14 PREPARED/COMMITTED card pairs, +14 addendum pairs = 28 records), chain links intact.
* `research/issued_research/`: 28 new immutable files (7 card original+projection pairs, 7 addendum pairs).
* `GAME_LOG_STATUS_CURRENT.md`: rewritten by the allocator (`Next canonical ID: P-557`, seven new status rows, highest ID P-556; the superseded "Local source reservation" line for P-550 removed).
* `research/verification/settled_import_2026-10-09/`: packet inputs (with hashes), build sources/requests, and the six deliverables.

Not touched: methodology, existing forecasts, probabilities, ranks, model code, calibration, historical grades, the 65 older carryover reviews already in Combined Log 7, and unrelated working-tree edits (`SOURCES.md`, `research/src/control_manifest.py`, untracked data/scripts), none of which are staged.

See `VERIFICATION_REPORT.md`, `DUPLICATE_RECONCILIATION.md` and `UNRESOLVED_POST_IMPORT.md`.
