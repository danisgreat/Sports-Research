# Prediction Mini Running Log — P-516 onward (started 2026-09-25(e))

| Field | Value |
|---|---|
| Created | 2026-09-25 about 23:50 +10:00 (Australia/Melbourne, AEST UTC+10; AEDT from 4 Oct 2026) |
| Status | **OPEN — no events yet.** |
| Next canonical ID | **P-518** (P-516 and P-517 were assigned to the two settled temporary IDs on 2026-09-26; this folder's name predates that) |
| Temporary IDs awaiting canonical reconciliation | **None.** `TMP-20260923-NPB-CHU-DB-G25` = P-516 and `TMP-20260923-NBL-CNS-TAS` = P-517 (`PREDICTION_LOG_COMBINED_5.md` §"2026-09-26(a)"). |
| Governing method for the next issue | METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2** (§15, RM-1). **Freeze with every card:** `CONTROL_MANIFEST_2026-09-25-6.md`, SHA-256 `fe80cc60742349e7489e36d07ce89a044f51341c6dbc588f742089ca76a8602b` (2026-09-26 re-hash of the Rank-1/Rank-2 receipt `CONTROL_MANIFEST_2026-09-25-5.md` after the P-516/P-517 assignment; 103 files, CRLF form; no card was issued under -5). Verify it with `python tools/verify_manifest.py`. |
| Operating mode | **SPORTS_ONLY / MARKET_BLIND.** No odds, prices, line movement, tipsters, betting previews, prediction markets or fantasy/DFS material. |
| Performance status | **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** |
| Predecessor | `archive/mini_logs/Mini Prediction Log - P-510 to P-515 SETTLED - 2026-09-25/` (corrected, imported into `PREDICTION_LOG_COMBINED_5.md` §"2026-09-25(f)"). |

## New for every card from this log (2026-09-25(e); `CURRENT_RULES.md`)

1. **Field 4 prints stated p and RM-1 q for every row**, ranks them **by q**, and prints the `TOP2_QUALITY` line: `python tools/rank_model.py rank --sport <league> --row "<contract>=<p>" …`.
   - A `SIDE_FLIP` is capped at SUPPORTED and needs a reconciliation line.
   - Under `TOP2_COIN_FLIP`, the delivery says plainly that the top two are near coin flips.
   - `SLATE_ADVISORY` is optional.
2. **Covered leagues print `TEAM_BASELINE_P`** beside `BASELINE_P` (`python tools/team_baseline.py predict …`). Covered: NBA, WNBA, NBL, NFL, AFL, NRL and EPL; MLB and NHL print a no-resolution flag. The departure ledger anchors on it where TB-1 has resolution.
3. **A non-baseball, non-hockey, non-soccer +k.5 row** takes the population cover rate as its `BASELINE_P` (`BASE_RATES_REGISTER.md` §7.7(c)).
4. **Official starters before a lineup-dependent Rank 1** (G14.2). P-514 named three starters who did not play.
5. **Settlement is read from the feed** (`receipts.py settle …`, or a pasted endpoint response), never typed. Audit field `10n` checks the lineup diff against the card.
6. **The settlement table** is `| Rank | Contract | Family | p | q | BASELINE_P | TEAM_BASELINE_P | Result | Brier(p) | Brier(q) |`.

## 1. Incomplete / Unsettled Logs

None.

## 2. Temporary-ID / Canonical-ID Conflict Logs

None.

## 3. Fully Settled Logs

None yet.
