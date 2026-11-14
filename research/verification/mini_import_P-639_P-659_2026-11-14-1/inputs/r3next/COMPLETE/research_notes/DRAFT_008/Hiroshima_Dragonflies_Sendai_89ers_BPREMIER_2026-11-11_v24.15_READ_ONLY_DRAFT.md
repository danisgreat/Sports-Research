# Hiroshima Dragonflies vs Sendai 89ers — v24.15 read-only pregame research draft

**Draft:** `DRAFT-008`; proposed organization only, NOT assigned to `G0008`, EV2 identity or canonical P-ID. **Capture UTC:** `2026-11-11T10:01:39+00:00`. **Read-only GitHub HEAD:** `4d8bd1771d20974bcbfc7c694a009cd44e95a693`. **Controls:** MDS-2026.11.11-v24.15 / CR-2026.11.11-R3 / P-2026.11.11-v24.13 / SEL-v4 / SCV-v12 / EXT-v3 / REQ-v5. **Mode:** SINGLE_CHAT_RESEARCH / READ_ONLY_DRAFT, not a completed FULL_FIVE external package. No results or target-game live scores inspected.

**Custody:** `NOT_ISSUED / NOT_SETTLED / NO_STRONG_PICK / ABSTAIN / UNCALIBRATED_QUALITATIVE`. Not a pre-start published numerical card. Time of source page reading was earlier in same interaction, but exact per-URL audit and timestamp receipts are not retained; do not claim certified issuance before tip-off.

## A1 — Identity, scheduled time and exact endpoints

- **Home:** Hiroshima Dragonflies, **Away:** Sendai 89ers, B.LEAGUE PREMIER 2026–27 regular season, Japan; official match **ScheduleKey 506574**, at **Hiroshima Green Arena**, Hiroshima, Japan.
- Official start **2026-11-11 19:05 JST / 21:05 AEDT / 10:05 UTC**, matching supplied estimate; independently matched B.League and both clubs' schedules. Actual first play/delay not confirmed.
- Contracts assume full game **four 10-minute quarters plus any overtime** under `BK-OT-1`, no tie settlement. Winner/handicap/total after overtime. Spread ±2.5 and total 170.5 have no integer push in a normally completed basketball game. Abandonment/void operator definitions not supplied. Rank scope `SUPPLIED_ONLY`.

## A2 — Exact supplied contracts and actions

| Original contract | Decisive full-game state | Qualitative direction | Numeric v24.15 status |
|---|---|---|---|
| Hiroshima Dragonflies -2.5 | Hiroshima by ≥3 including OT | Borderline; home/rest advantage vs tight matchup | `UNPRICED / NOT_VALIDATED` |
| Sendai 89ers +2.5 | Sendai wins or loses by ≤2 including OT | Plausible alternative to Hiroshima -2.5; very narrow | `UNPRICED / NOT_VALIDATED` |
| Combined Over 170.5 points | ≥171 points including OT | Risk: recent Sendai perimeter explosion | `UNPRICED / NOT_VALIDATED` |
| Combined Under 170.5 points | ≤170 points including OT | **Primary qualitative lean** | `UNPRICED / NOT_VALIDATED` |

**Informational winner:** Hiroshima **slight** due stronger season, venue and rest; the margin is not sufficient to express a clear handicap edge. **Forced single supplied choice:** Under 170.5, LOW confidence. **Formal ranking:** NONE; no rank-1 pass, no computed `p_card`, `W/P/L`, expected value, baseline, exact receipt or simulation. `NO_STRONG_PICK / ABSTAIN` remains formal.

## A3 — Dated historical form, as observed before 11 November

**Hiroshima**, 13–1 season, 90.4 scored / 79.1 conceded per game. Six most recent dated completed games (Hiroshima points first):

| Date JST | Opponent | Score | Combined | W/L |
|---|---|---:|---:|---|
| 2026-10-21 | vs Akita | 98–84 | 182 | W |
| 2026-10-24 | vs Hokkaido | 93–96 | 189 | L |
| 2026-10-26 | @ Yokohama BC | 90–64 | 154 | W |
| 2026-10-31 | @ Shimane | 95–88 | 183 | W |
| 2026-11-01 | @ Shimane | 74–73 | 147 | W |
| 2026-11-06 | vs Nagasaki | 80–73 | 153 | W |

**Sendai**, 12–4 season, 87.6 scored / 79.8 conceded per game. Six most recent dated completed games (Sendai points first):

| Date JST | Opponent | Score | Combined | W/L |
|---|---|---:|---:|---|
| 2026-10-24 | @ Kawasaki | 93–82 | 175 | W |
| 2026-10-26 | @ Shimane | 86–85 | 171 | W |
| 2026-10-31 | vs Tokyo SR | 73–80 | 153 | L |
| 2026-11-01 | vs Tokyo SR | 87–79 | 166 | W |
| 2026-11-06 | vs Alvark Tokyo | 96–69 | 165 | W |
| 2026-11-09 | @ Nagasaki | 107–87 | 194 | W |

**Overlapping recent windows**. L10/L15/L20 cannot be completed from the six dated game rows opened here; their listed `n=6` below is **available coverage only**, not a claim of an actual last-10/-15/-20 sample. Do not extrapolate recent results to missing games.

| Window | Hiroshima n | W–L | PF | PA | Total avg | Under 170.5 | Sendai n | W–L | PF | PA | Total avg | Under 170.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| L5 | 5 | 4–1 | 86.4 | 78.8 | 165.2 | 3/5 | 5 | 4–1 | 89.8 | 80.0 | 169.8 | 3/5 |
| L6 | 6 | 5–1 | 88.3 | 79.7 | 168.0 | 3/6 | 6 | 5–1 | 90.3 | 80.3 | 170.7 | 3/6 |
| L10 | 6 | 5–1 | 88.3 | 79.7 | 168.0 | 3/6 | 6 | 5–1 | 90.3 | 80.3 | 170.7 | 3/6 |
| L15 | 6 | 5–1 | 88.3 | 79.7 | 168.0 | 3/6 | 6 | 5–1 | 90.3 | 80.3 | 170.7 | 3/6 |
| L20 | 6 | 5–1 | 88.3 | 79.7 | 168.0 | 3/6 | 6 | 5–1 | 90.3 | 80.3 | 170.7 | 3/6 |

League source for exact 2026–27 records and results: https://www.bleague.jp/club_detail/?TeamID=721 ; https://www.bleague.jp/club_detail/?TeamID=692. **Overall season rates** are full available sample 14 and 16 games; rolling windows are not independent.

## A4 — Scoring parameters and uncalibrated diagnostics

- Full season offence/opponent allowance cross-match: Hiroshima = (90.4 PF + 79.8 Sendai PA)/2 = **85.10**, Sendai = (87.6 PF + 79.1 Hiroshima PA)/2 = **83.35**. Unadjusted **total 168.45**, margin **Hiroshima +1.75**.
- L5 cross-match: Hiroshima = (86.4 + 80.0)/2 = **83.2**, Sendai = (89.8 + 78.8)/2 = **84.3**, unadjusted **total 167.5**, Sendai +1.1.
- These are **descriptive arithmetic only**, not the issued v24.15 `REFERENCE`, opponent-adjusted ORtg/DRtg, fitted team strengths or model score. Home/rest are not fitted numerical adjustments. Both totals (168.45 and 167.5) fall **below 170.5**, but only by ~2–3 points; expected volatility is much wider than the difference.
- Both teams season total means: Hiroshima **169.5** and Sendai **167.4**. A legacy historical B.League parameter row (`Basketball/B League`, mean 159.19, residual total SD 16.28) exists in v24.15 repository but has `HISTORICAL_DEVELOPMENT_UNADMITTED` status and **is not verified applicable** to the new B.PREMIER regime; no reference substitution or model-based primary price.
- Hiroshima shooting 48.9% FG / 34.6% 3P, 41.3 RPG, 11.5 turnovers; Sendai 45.4% FG / 36.4% 3P, 36.6 RPG, 10.6 turnovers. Opponent-adjusted pace, possession estimates and detailed on/off lineup effects not established; the comparison is descriptive.

## A5 — Team matchups and prior meetings

- Stronger season W/L and offensive rebounding profile for Hiroshima; stronger 3P percentage, blocks and steals for Sendai. Hiroshima home crowd and paint play against Sendai physical man-to-man pressure. Team-owned match-day preview identifies Sendai's **Jarrett Culver** and **Nathan Booth** as offensive focal points.
- Hiroshima star **Kofi Cockburn** ~20.9 PPG, 12.9 RPG in club player leaders; Dwayne Evans ~4.8 APG. Sendai **Jarrett Culver** ~27.3 PPG, 6.7 RPG; Sergio El Darwich ~5.9 APG. Not verified starters.
- Most recent H2Hs: 2025-11-16 Hiroshima 85–80 Sendai (**165 total**); 2025-11-15 Hiroshima 88–49 Sendai (**137**). Prior 2024–25 meetings: Hiroshima 94–84 (**178**) and 106–91 (**197**). Last four divided **2 Under/2 Over 170.5**; previous-season roster context reduces weight. Official team matchday preview: https://hiroshimadragonflies.com/lp/game_20261111/.
- **Calendar:** Hiroshima last competed Nov 6 (5 calendar days before this match), Sendai Nov 9 (2 calendar days before), with Sendai travelling after a Nagasaki away game. Any quantified fatigue or travel effect is NOT_ESTIMATED.

## A6 — Injury, lineup, bench and unknowns

- The league's official 11 Nov updated injury register was checked; no **currently active** named Hiroshima/Sendai registrant confirmed from the listing. Historical entries under either club may represent closed previous seasons, not current active injuries. **Absence from the list does not confirm fitness.** Official roster-dressed and actual starting fives were NOT_VERIFIED; bench and coach late changes likewise.
- Specific impact of injuries, rest, opponent-adjusted possession pace, line-up combinations, late media status and match referees **NOT_ESTIMATED/NOT_VERIFIED**, and must not be scored as completed independent checks.
- Current team leaders identified in A5 are **season average players**, not formal confirmed starters; potential foul trouble, shooting volatility, and overtime are material to Under 170.5.

## A7 — Market-blind evidence & timing / release gates

- User-supplied lines are contract metadata only; **no betting odds, predictor model outputs or market prices used**. Sources restricted to official league/club match, stats, and league injury announcements. Source URLs: https://www.bleague.jp/en/game_detail/?ScheduleKey=506574&tab=1; https://www.bleague.jp/club_detail/?TeamID=721; https://www.bleague.jp/club_detail/?TeamID=692; https://hiroshimadragonflies.com/lp/game_20261111/; https://hiroshimadragonflies.com/schedule/list/?month=all&scheduledate=all&year=2026; https://www.89ers.jp/schedule/list/?month=all&year=2026; https://www.bleague.jp/news/injury.html.
- `SRC-ALT-v3` exact URL robots reader audit **NOT_EXECUTED**. Web browsing established readable pages but is not an audited `OPENED` permission receipt. Source collector mapping and exact known-at (per source) **NOT_VERIFIED**. No outcome exposure declared from target-game pages; scheduled fixture remained unscored on pages viewed.
- GitHub HEAD at research: 4d8bd1771d20974bcbfc7c694a009cd44e95a693; repository used strictly READ_ONLY. Reference tier CLI, official numeric evidence packet, full A1–A9 league L10/L15/L20, five research lanes, `SR-KIT-v24.15` calculation, official `PICKS_V2`, prestart `freeze-single`, lint and lease-held append are **NOT_RUN**; no P-ID or key issued. No pseudo-probability or Monte Carlo claim.
- The independent local research record is an **UNISSUED** note; actual pregame publication, full auditor path and host timing remain unsupported. Do not retroactively certify it after the official tipoff.

## A8 — Competing scenarios / qualitative selection analysis

1. **Controlled 160–170 total**: both season defences ~79–80 PA, Hiroshima's last two 153 and 147, and prior two meetings 165/137 support Under 170.5.
2. **High-scoring 175–195 total**: Sendai's recent 107–87 (194), long-range efficiency, and Hiroshima's earlier 93–96 (189) show Over remains viable. Overtime also increases exposure. Neither implied probability is computed.
3. **Close game (1–4 points)**: season cross-match margin Hiroshima +1.75 and last-five model flip to Sendai +1.1 show that -2.5 versus +2.5 is unstable to plausible venue/rest changes; **no strong spread**.
4. **Hiroshima separates**: 13–1 record, big-man rebounding and extra rest might create a >2-point home victory, but the necessary player and rest-effect parameters are unestimated.

**Preferred forced direction = Under 170.5, LOW confidence.** Neither spread nor total meets a numeric evidence-based rank gate; formal `NO_STRONG_PICK / ABSTAIN`.

## A9 — Research completion matrix and custody

| Required item | Status |
|---|---|
| Official fixture, native ID, home/away, local time and venue | VERIFIED (scheduled 19:05 JST =21:05 AEDT; game 506574) |
| Exact supplied spread/total + OT inclusive contract terms | CAPTURED; operator-specific void terms UNKNOWN |
| Season records/PPG/PA and most recent six dated results | VERIFIED against official team pages |
| True L5 window | COMPUTED; n=5 per team |
| True L10/L15/L20 windows | INCOMPLETE; only n=6 obtained from visible match histories |
| Head-to-head source and dates | VERIFIED four recent games from home club |
| Rest/travel calendar | CALENDAR VERIFIED, travel burden not quantified |
| Final starting fives, all absences, bench | NOT_VERIFIED; injury-register presence alone insufficient |
| Independent collector validation & exact URL source audits | NOT_RUN |
| Frozen reference, adjustment ledger, coherent goal/score grid, KIT receipt | NOT_RUN |
| Numeric probabilities and model qualification | NOT_ISSUED / UNPRICED on all four directions |
| PRESTART publication/lease-held official append and provenance | NOT_DONE |
| Results / settlement | **NOT_PERFORMED**, no scores checked |

**Source custody:** capture UTC `2026-11-11T10:01:39+00:00`; only original requested event and official past results were viewed; this note is first-party local research draft. Every earlier local mini byte preserved separately; GitHub remains unchanged.
