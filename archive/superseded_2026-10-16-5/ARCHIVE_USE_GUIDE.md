# Online form calculations and evidence checks

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-9 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**HIST-2026.10.16-v3.** This compatibility filename now describes calculations on source-reviewed online rows. It requires no local results archive. [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) governs mandatory L5/L10/L15/L20 internet research and [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md) governs confirmed players. Old coverage counts/defect tables are historical only.

## Recipe R2: form windows

1. **Rows.**
   - For each side, list its dated competitive games before the cutoff, newest first. Research and verify every window online under HISTORICAL_SOURCE_PROTOCOL, including local-language organizer/federation/team archives. Do not use an unrelated major-league endpoint.
   - Exclude rows the online evidence identifies as duplicate listings, awarded results, forfeits or abandonments, and say so.
   - An undated row cannot enter a window.
2. **Windows.** L5, L10, L15 and L20 (true n if fewer), season to date, and an independently sourced current league level; retired profiles supply no value. For each, give scored, conceded and margin per game, plus the home/away split for L10 and L20. Print the table in template §3b.
3. **Season boundary.**
   - Previous-season games fill a window only when the current season has fewer games than the window. They are flagged.
   - Exclude them, and print the shorter n, when the side changed head coach, or when more than about 30% of its regular minutes or starts changed. Say which, with the source.
4. **Primary rate (equal weight, longer window).**
   - r = the L20 per-game mean, or season to date if longer and in the same regime.
   - Shrink it toward the league level: rate = (n × r + k × LM) ÷ (n + k). The constant k comes from PROBABILITY_TOOLKIT §4.3; use k = 2 where the league has none, and say so.
   - Do this separately for scored and conceded.
   - This is the rate that may enter the centre, as a listed adjustment.
   - Why equal weight over the longer window. This repository's historical out-of-sample checks ([RECENCY_AND_REBOUND.md](archive/historical_restored/RECENCY_AND_REBOUND.md) §4 and §7.2, one season each) found these RMSE changes for next-game team points against the league constant:

     | Window | NBA | WNBA | NBL | NHL | EPL |
     |---|---|---|---|---|---|
     | Last 1 | +35.7% | +28.2% | +18.0% | +39.9% | +37.6% |
     | Last 5 | +6.5% | +0.9% | −8.1% | +8.2% | +7.7% |
     | Last 10 | +1.9% | −1.7% | −10.4% | +3.4% | +2.2% |
     | Season to date | −1.1% | −4.2% | −7.7% | 0.0% | 0.0% |

     - Shorter windows were worse, monotonically, in the NBA, NHL and EPL, and the one-game window was the worst everywhere.
     - The NBL was the exception: last 10 beat season to date, consistent with scoring rising through its season.
     - In the NHL and EPL a half-way shrink to the league mean was the best simple predictor, so use a large k there.
     - For MLB starters' next-start earned runs: last 1 2.77, last 3 2.24, last 5 2.13, season 2.02, league 1.98 (L-20260919-04).
     - These are historical, single-season results. The comparison in step 5 tests them prospectively.
5. **Recency blend (printed as a comparison, not used for the pick).**
   - B = (L5 + L10 + L15 + L20) ÷ 4. This is a recency-weighted mean of the last 20 games, with weights per game of 0.1042 (games 1–5), 0.0542 (6–10), 0.0292 (11–15) and 0.0125 (16–20); its effective n is about 13.5.
   - Shrink it with the same k, using n = 13.5.
   - Print it beside the primary rate. Experiment FC11-FORM-v1 compares the two on settled games.
6. **Opponent context** (optional, recommended for basketball, where opponent defence improved RMSE by 7–11%):
   - For each game in the window, adjusted scored = scored − (opponent's conceded per game before that game − LM). Use the analogous formula for conceded.
   - Print the adjusted L20 mean beside the raw one.
   - If it is used, it is a listed adjustment, and the unadjusted pair is shown.
7. **Reading the windows.**
   - The windows overlap: they are one piece of evidence, counted once.
   - A gap between L5 and L20 is described, not traded on, unless a named, current mechanism explains it: an injury or return, a role or lineup change, a coach change, schedule density. There is no bounce-back or streak lean.
   - Disclose a short-window outlier as width, not as a centre shift.


## Current model and league comparisons

R2 arithmetic is retained as a disclosed team-form diagnostic. PRIMARY_PREDICTION_PROTOCOL governs the actual fitted distribution/mixture; no manual formula replaces it. Missing league/shrinkage inputs stay missing. Derive any league baseline/profile from a separate online-sourced exact-competition population, with true n, dates, endpoint, missingness and available_at. Do not reuse retired numeric profiles or treat a team window as a league population.

## Evidence receipt and integrity

Use the existing Archive check field as `ONLINE_HISTORY: <source URLs/evidence paths; rows read; dates; L5/L10/L15/L20 true n; exclusions; unresolved gaps>`. Its name is retained for format compatibility, not a folder-scan requirement. A3 carries row evidence. Settlement uses the official exact-game result and mandatory independent source corroboration. Retrospectives preserve original evidence and may add separately sourced comparisons.

Deduplicate IDs/reschedules/aliases; distinguish observed zero and unknown. Check score/period/total equations under actual era/endpoint without invented balancing values. Separate event, available and capture times. Classify fields OBSERVED, DERIVED, MISSING or CONFLICTING. Suspicious constants require source review. Prompt 7 applies only to explicitly authorized rebuild destinations, never implicit recreation.
