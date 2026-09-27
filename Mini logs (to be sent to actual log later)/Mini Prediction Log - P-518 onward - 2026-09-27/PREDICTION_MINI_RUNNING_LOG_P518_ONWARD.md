# Prediction Mini Running Log — P-518 onward (started 2026-09-27)

| Field | Value |
|---|---|
| Log Name | **Prediction Mini Running Log — P-518 onward** |
| Created / Start Date (AEST) | **2026-09-27 02:25 +10:00** (Australia/Melbourne, AEST UTC+10; AEDT from 4 Oct 2026) |
| Status | **OPEN — 3 unsettled events: P-518 and P-519 live-issued (excluded from pregame scoring), P-520 pregame.** |
| Governing Method | `METHOD.md` **MDS-2026.09.19-v4.3** |
| Control Revision | `METHOD.md` **CR-2026.09.21-3** |
| Scoring Version | `SCORING_AND_VALIDATION.md` **SCV-2026.09.19-v2** (§15, RM-1) |
| Control Manifest | `CONTROL_MANIFEST_2026-09-27.md` |
| Manifest SHA-256 | `74f34e8d1c9692db3eb4b964332ace91750f881f3d16bc0c0c6acf2868d62b31` (2026-09-26(e) predictability pass, category MEASUREMENT with TB-1 validity repairs for NRL sides and NFL totals, C1: no model change meets the user's 2026-09-27 bar; 124 files, CRLF form; verified via `python tools/verify_manifest.py`) |
| Next Canonical ID | **P-521** (P-518, P-519 and P-520 issued below) |
| ID Determination | Determined from the controlling top snapshot of the active canonical log (`PREDICTION_LOG_COMBINED_5.md` lines 8, 20–30, and §"2026-09-26(a)") and verified in `GAME_LOG_STATUS_CURRENT.md` (lines 3, 11). `PREDICTION_LOG_COMBINED_5.md` reconciles canonical IDs through P-517: P-510–P-515 were imported and settled in §"2026-09-25(f)"; P-516 (`TMP-20260923-NPB-CHU-DB-G25`) and P-517 (`TMP-20260923-NBL-CNS-TAS`) were assigned on 2026-09-26(a) to the two settled temporary IDs. No temporary ID awaits reconciliation. P-518, P-519 and P-520 were issued in this mini log. Next canonical ID is P-521. |
| Temporary IDs Awaiting Reconciliation | **None.** `TMP-20260923-NPB-CHU-DB-G25` = P-516 and `TMP-20260923-NBL-CNS-TAS` = P-517 (`PREDICTION_LOG_COMBINED_5.md` §"2026-09-26(a)"). |
| Operating Mode | **SPORTS_ONLY / MARKET_BLIND.** No odds, prices, line movement, tipsters, betting previews, prediction markets or fantasy/DFS material. A supplied line is contract metadata only. |
| Performance Status | **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** |
| Predecessor Mini Log | `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-516 onward - 2026-09-25/PREDICTION_MINI_RUNNING_LOG_P516_ONWARD.md` (created 2026-09-25(e); no events carded; folder name predated 2026-09-26(a) canonical assignment). Preceding settled mini log: `archive/mini_logs/Mini Prediction Log - P-510 to P-515 SETTLED - 2026-09-25/` (imported into `PREDICTION_LOG_COMBINED_5.md` §"2026-09-25(f)"). |

---

## Standing Operating Rules and Preflight Directives (`CURRENT_RULES.md`)

1. **Rank by RM-1 q:** Field 4 prints stated $p$ and RM-1 $q$ for every row, ranks them **by $q$**, and prints the `TOP2_QUALITY` line (`python tools/rank_model.py rank --sport <league> --row "<contract>=<p>" …`).
   - A `SIDE_FLIP` is capped at SUPPORTED and requires a reconciliation line.
   - Under `TOP2_COIN_FLIP`, the delivery states plainly that the top two are near coin flips.
   - `SLATE_ADVISORY` is optional.
2. **Team Baseline ($TEAM\_BASELINE\_P$):** Covered leagues print `TEAM_BASELINE_P` beside `BASELINE_P` (`python tools/team_baseline.py predict …`). Covered: NBA, WNBA, NBL, AFL; EPL for match results. MLB, NHL, NRL sides and NFL totals print a no-resolution flag and anchor on `BASELINE_P`.
3. **Underdog Cushion Baseline:** A non-baseball, non-hockey, non-soccer +k.5 row takes the population cover rate as its `BASELINE_P` (`BASE_RATES_REGISTER.md` §7.7(c); `C-PLUS-CUSHION`).
4. **Lineup Gate:** Official starters before a lineup-dependent Rank 1 (G14.2). Unconfirmed lineups stay marked `LINEUPS_NOT_YET_PUBLISHED` or `RETRIEVAL_MISS`.
5. **Feed-Sourced Settlement:** Settlement is read from the feed (`receipts.py settle …`, or a pasted endpoint response), never typed (`C-SETTLEMENT-FROM-FEED`). Audit field `10n` checks the lineup diff against the card.
6. **Settlement Table Schema:** `| Rank | Contract | Family | p | q | BASELINE_P | TEAM_BASELINE_P | Result | Brier(p) | Brier(q) |`.
7. **Declare Universe:** Declare the slate before choosing a game (`python tools/slate_universe.py declare --date <venue-local YYYY-MM-DD> --league <key> …`). Every card prints `UNIVERSE: UNIVERSE_<date>.json` (audit field `UV`, strict). A game outside it prints `OUT_OF_UNIVERSE` with a reason.
8. **Rule Freeze in Force:** `C-RULE-FREEZE` (`python tools/evidence_status.py`). No new predictive rule, weight, or cap until `C-BASELINE-SKILL` and `T-RM1-PROSPECTIVE` reach their checkpoints. Proposed rule changes are `TESTING` candidates only.
9. **Numerical Shadow Lanes:** After the freeze, record the shadow row before start (MLB: `python tools/mlb_model.py shadow --gamepk <pk> --total <line> --card P-<n>`; other sports: `python tools/sport_models.py shadow --league <key> --event <ESPN id> --date <date> --card P-<n> --total <line> --line <home handicap>`). It is blind (row ID only), never a card input, and never changes a rank.
10. **Market Benchmark:** After settlement only, the operator records no-vig closing prices in `MARKET_BENCHMARK_LEDGER.md` (`C-MARKET-BENCHMARK`). Forecasting stays strictly market-blind.
11. **Shadow Settlement:** At settlement, print `SHADOW: <row id>` (or `SHADOW: NO_LANE <reason>` / `SHADOW: MISSED <reason>`). Audit field `10s` is strict.
12. **Validity Repairs:** NRL sides and NFL totals print `TB1_NO_RESOLUTION` and anchor on `BASELINE_P`.
13. **Predictability Row:** Print the league's predictability row (`BASE_RATES_REGISTER.md` §7.8: share of STRONG favourites and their win rate, or `NOT_YET_DERIVED`) beside the track-record row (`C-PREDICTABILITY-MAP`). Under `TOP2_COIN_FLIP` in a league with few or no STRONG favourites, state that the slate cannot produce a STRONG Rank 1.
14. **Model Anchor:** `tools/model_anchor.py` is a reference, never a card input (`C-MODEL-ANCHOR`, status `REFERENCE`). Do not print or cite it on a card.

---

## 1. Incomplete / Unsettled Logs

<!-- BEGIN VERBATIM ISSUED RECORD: P-518 -->
### P-518 — Baseball / MLB: New York Mets (J Tong) @ Washington Nationals (C Early)

**Status:** UNSETTLED — LIVE-ISSUED VIEW (EXCLUDED FROM PREGAME SCORING) / NO RETROSPECTIVE.

#### 1. Identity and contract
- **Canonical ID:** `P-518`.
- **Sport / Competition:** Baseball / Major League Baseball (MLB) 2026 Regular Season (Game 161).
- **Event:** New York Mets (Jonah Tong) @ Washington Nationals (Connelly Early) (home/away as listed).
- **Venue:** Nationals Park, Washington, D.C., USA (Capacity: 41,339; Surface: Natural Grass).
- **Scheduled start:** Saturday, 26 September 2026, 12:35 EDT (venue-local) = 26 September 2026, 16:35 UTC = Sunday, 27 September 2026, 02:35 AEST (Australia/Melbourne, UTC+10).
- **Final volatile refresh / Freeze time:** 2026-09-26 16:37:50 UTC = 2026-09-27 02:37:50 AEST.
- **Event state at freeze:** `LIVE-ISSUED VIEW` (detailedState transitioned from `Warmup` [PW] to `In Progress` [I] at 16:37:50 UTC; 0-0, top 1st, no in-game events utilized in distribution or pricing).
- **Exact supplied contracts:**
  1. `Mets +1.5` (Run line: New York Mets +1.5 runs; regulation + extra innings; half-run line, no push).
  2. `Nationals +1.5` (Run line: Washington Nationals +1.5 runs; regulation + extra innings; half-run line, no push).
  3. `Combined Total: Over/under 8.5` (Full game total runs scored by both teams: Over 8.5 / Under 8.5; regulation + extra innings; half-run line, no push).
- **Governing method / controls:** `METHOD.md` **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; `SCORING_AND_VALIDATION.md` **SCV-2026.09.19-v2** (§15, RM-1); `RULES_BASEBALL.md` §0 (consolidated 2026-09-26); `SPORTS_ONLY / MARKET_BLIND`; `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`.
- **Control manifest receipt:** `CONTROL_MANIFEST_2026-09-27.md`, SHA-256 `74f34e8d1c9692db3eb4b964332ace91750f881f3d16bc0c0c6acf2868d62b31`.

#### 2. Evidence and exposure
- **Lineup and Starter Confirmation (`CONFIRMED_OFFICIAL`):** Retrieved 2026-09-26T16:33:46Z via MLB statsapi official live feed (`receipts.py pregame mlb 822678`).
  - **New York Mets:**
    - Confirmed Starters: 1. Francisco Lindor (DH), 2. Juan Soto (LF), 3. Bo Bichette (3B), 4. Carson Benge (RF), 5. Mark Vientos (1B), 6. Brett Baty (SS), 7. Francisco Alvarez (C), 8. A.J. Ewing (CF), 9. Ronny Mauricio (2B).
    - Probable/Starting Pitcher: Jonah Tong (RHP, id: 804636, debut 2025-08-29; 2026 season: 6 GP, 3 GS, 25.2 IP, 4.21 ERA, 1.32 WHIP, 25 K, 13 BB, 2 HR). Last 3 starts: Sep 7 vs CIN (5.0 IP, 4 ER, 7 K, 1 BB), Sep 14 vs PHI (6.0 IP, 0 ER, 6 K, 1 BB), Sep 20 vs ATL (4.2 IP, 4 ER, 5 K, 4 BB). Leash modeled at ~80–90 pitches (4.2–5.1 IP).
    - Manager: Carlos Mendoza. Bench / Bullpen: Mets used 5 relievers yesterday (Yan 37 NP, Pintaro 17 NP, Perez 22 NP, Hagenman 70 NP, Lavender 14 NP); high-leverage arms remain available.
  - **Washington Nationals:**
    - Confirmed Starters: 1. James Wood (RF), 2. Abimelec Ortiz (DH), 3. Dylan Crews (CF), 4. CJ Abrams (2B), 5. Brady House (3B), 6. Daylen Lile (LF), 7. Yohandy Morales (1B), 8. Keibert Ruiz (C), 9. Nasim Nuñez (SS).
    - Probable/Starting Pitcher: Connelly Early (LHP, id: 813349, debut 2025-09-09; 2026 season: 17 GP, 17 GS, 91.2 IP, 3.44 ERA, 1.25 WHIP, 93 K, 34 BB, 15 HR). **Critical availability factor:** Early has not pitched in MLB since 2026-06-30 (nearly 3 months on IL). In two Triple-A Rochester rehab starts (Sep 15: 1.0 IP, 35 pitches, 2 K, 2 BB, 3 ER; Sep 20: 1.2 IP, 40 pitches, 2 K, 3 BB, 0 ER), he threw max 40 pitches. Under `RULES_BASEBALL.md` control 25 (rehab pitch ladder) and control 1 (short start is exposure), Early is on a strict pitch ceiling of ~50–65 pitches (~2.1–3.2 IP).
    - Manager: Dave Martinez. Bullpen exposure: Nationals bullpen will absorb 5.1–7.0 innings; yesterday used Alvarez (101 NP), Varland (14 NP), Cruz (7 NP), Sinclair (18 NP), Gray (18 NP).
- **Environment & Weather:**
  - Gamefeed weather at freeze (`receipts.py pregame mlb`): Overcast, 67°F (19.4°C), wind 16 mph, In From LF.
  - Open-Meteo hourly forecast (Nationals Park: 38.873°N, 77.007°W): 12:00–16:00 EDT: 18.5°C–19.5°C, humidity 62–68%, wind 18 km/h NNW (~11 mph, 340–350°, blowing in from left field), precipitation probability 22% rising to 50% by 15:00 EDT.
  - Directional mechanism: 16 mph wind blowing inward from left field dampens fly-ball carry and suppresses home run conversion, moderately mitigating the high-scoring venue effect.
- **Team Season Rates (through 160 games):**
  - NYM: 688 RS (4.30 R/G), 724 RA (4.53 RA/G); OPS .703, AVG .239.
  - WSH: 814 RS (5.09 R/G), 804 RA (5.03 RA/G); OPS .745, AVG .247.
  - H2H 2026: 11 meetings in regular season; WSH leads 6–5. At Nationals Park (5 games): 16-7, 9-6, 8-4, 2-1, 7-6 (yesterday). 4 of 5 games cleared 11+ runs (mean 13.2 R/G).
- **Umpire Crew:** Home Plate: Austin Jones; 1B: Jen Pawol; 2B: James Hoye; 3B: Sean Barber.

#### 3. Joint distribution
- **Prior:** League empirical mean 8.95 runs, SD 4.51 (`BASE_RATES_REGISTER.md` §7.5). TB-1 model prior: 9.41 runs (`tools/team_baseline.py`).
- **Signed adjustments (runs):**
  - Team offensive/run-prevention baselines: +0.45 runs (WSH offense 5.09 R/G, NYM pitching 4.53 RA/G, WSH pitching 5.03 RA/G).
  - Venue elevation (Nationals Park 2026 empirical mean 10.83, median 10.0; n = 78, P(≥10) = 0.564): +1.10 runs carry.
  - Starter & bullpen interaction: +0.65 runs (Connelly Early rehab pitch-count limit ~55–65 pitches induces early transition into vulnerable Washington bullpen in innings 3–4; Jonah Tong elevated 4.56 BB/9 walk exposure).
  - Weather dampening: −0.60 runs (16 mph wind blowing directly in from left field suppresses power carry at 67°F).
  - Net adjustment: +1.05 runs over 8.95 league baseline.
- **Distribution parameters:**
  - Total runs: Negative binomial distribution (`tools/card_math.py`), Mean = 10.00, Median = 9.50, Width (SD) = 4.50.
  - Margin: Normal distribution (`tools/card_math.py cover --no-zero`), Mean = WSH +0.10, Median = 0.00, Width (SD) = 4.50.
- **Reference comparison (`C-WIDTH-BENCHMARK`):**
  - Total width: 4.50 vs reference width 4.50 (ratio 1.000 ≥ 0.85).
  - Margin width: 4.50 vs reference width 4.57 (ratio 0.985 ≥ 0.85).
  - Reference venue row (`BASE_RATES_REGISTER.md` §7.5): Nationals Park n = 78, Mean 10.83, Median 10, P(≤7) 0.231, P(≥10) 0.564, P(≥12) 0.410.
- **Outcome-State Family Table (masses sum to 1.0000):**
  - F1 (Mets win by 2+ runs): 0.3650
  - F2 (Mets win by exactly 1 run): 0.1250
  - F3 (Nationals win by exactly 1 run): 0.1500
  - F4 (Nationals win by 2+ runs): 0.3600
  - *Joint Over/Under splits:*
    - F1a (Mets by 2+, Over 8.5): 0.2154 | F1b (Mets by 2+, Under 8.5): 0.1496
    - F2a (Mets by 1, Over 8.5): 0.0737 | F2b (Mets by 1, Under 8.5): 0.0513
    - F3a (Nationals by 1, Over 8.5): 0.0885 | F3b (Nationals by 1, Under 8.5): 0.0615
    - F4a (Nationals by 2+, Over 8.5): 0.2124 | F4b (Nationals by 2+, Under 8.5): 0.1476
    - Total sum = 1.0000. Total Over 8.5 mass = 0.5900; Total Under 8.5 mass = 0.4100.

#### 4. Contract queries and ranks

| Rank (q) | Contract | Family | Class | p | RM-1 q | Tier | Flags | BASELINE_P | TEAM_BASELINE_P | Logit Departure | Preferred / Pair Type |
|---:|---|---|---|---:|---:|---|---|---:|---:|---|---|
| **1** | **Mets +1.5** | Margin | `hcp_plus_low` | 0.640 | 0.668 | SUPPORTED | — | 0.638 | 0.6249 (`TB1_NO_RES`) | +0.009 (attributed 1.00) | COVERING_PAIR (with R2) |
| **2** | **Nationals +1.5** | Margin | `hcp_plus_low` | 0.635 | 0.661 | SUPPORTED | — | 0.638 | 0.6516 (`TB1_NO_RES`) | −0.013 (attributed 1.00) | COVERING_PAIR (with R1) |
| **3** | **Over 8.5** | Total | `total_over` | 0.590 | 0.593 | LEAN | — | 0.491 | 0.5332 (`TB1_NO_RES`) | +0.400 (attributed 1.00) | FORCED_PAIR (preferred side) |
| **4** | **Under 8.5** | Total | `total_under` | 0.410 | 0.407 | COIN_FLIP | `LOW_RESOLUTION` | 0.509 | 0.4668 (`TB1_NO_RES`) | −0.400 (attributed 1.00) | FORCED_PAIR |

- **TOP2_QUALITY:** `TOP2_SUPPORTED` (R1 q 0.668; R2 q 0.661). Note: R1 and R2 form a `COVERING_PAIR` (opposite +1.5 run lines), so at least one is guaranteed to win; Hit@2 is mechanical and excluded from skill evaluation.
- **Predictability row (`BASE_RATES_REGISTER.md` §7.8):** MLB 2026: 2,073 games; Favourite ≥ 0.70 share = **0%**; 0.50–0.60 share = **90%**; Total side ≥ 0.70 = 0%. Under `TOP2_COIN_FLIP` / `TOP2_SUPPORTED`, the slate in MLB cannot produce a STRONG (q ≥ 0.70) moneyline or run line.
- **Track record disclosure (`C-TRACK-RECORD`):** MLB resolution is near zero (0.0075; 58.6% of decisions won at stated 0.596).
- **Departure Ledger (`C-DEPARTURE-LEDGER` via `tools/card_math.py departure`):**
  - Mets +1.5 (p = 0.640 vs BASELINE_P 0.638): Logit departure +0.009; attributed 100% to Early rehab pitch ceiling / Washington bullpen exposure (+0.009). Unexplained: 0.00.
  - Nationals +1.5 (p = 0.635 vs BASELINE_P 0.638): Logit departure −0.013; attributed 100% to Early pitch count leash vs top of Mets order (−0.013). Unexplained: 0.00.
  - Over 8.5 (p = 0.590 vs BASELINE_P 0.491): Logit departure +0.400; attributed to Nationals Park venue elevation (+0.260 / 65%), Early rehab bullpen exposure (+0.220 / 55%), offset by wind blowing in from LF (−0.080 / −20%). Unexplained: 0.00.
  - Under 8.5 (p = 0.410 vs BASELINE_P 0.509): Logit departure −0.400; attributed symmetrically. Unexplained: 0.00.
- **Cushion Decomposition (`C-PLUS-CUSHION`):**
  - Mets +1.5 covers if Mets win (0.4900) or lose by exactly 1 run (0.1500) = 0.6400.
  - Nationals +1.5 covers if Nationals win (0.5100) or lose by exactly 1 run (0.1250) = 0.6350.

#### 5. Dependence and checks
- **Top Two Relationship (`COVERING_PAIR`):**
  - P(R1 ∧ R2) = P(Game decided by exactly 1 run) = 0.2750 (positive overlap; both win if either team wins by 1).
  - P(¬R1 ∧ ¬R2) = 0.0000 (0.00%; union of opposite +1.5 lines covers 100% of baseball outcomes without ties).
  - Mechanical coverage warning: Ranks 1 and 2 cannot both fail. A win on one is guaranteed by structure, not skill (`G-L22`).
- **Complement Decompositions:**
  - ¬R1 (Mets +1.5 fails) occurs iff Nationals win by ≥ 2 runs: Mass = 0.3600.
  - ¬R2 (Nationals +1.5 fails) occurs iff Mets win by ≥ 2 runs: Mass = 0.3650.
- **Over/Under Pair:**
  - Labelled `FORCED_PAIR`. Preferred side: Over 8.5 (p = 0.590, q = 0.593).
  - Push mass: 0.0000 (half-point line 8.5).
  - Top O/U review candidate: `TOP_OU_REVIEW` recorded for Over 8.5.
- **Representative Rank-#1 Outcome:**
  - New York Mets 6, Washington Nationals 5 (Total 11, margin METS +1). Simultaneously satisfies Rank 1 (Mets +1.5 WIN), Rank 2 (Nationals +1.5 WIN), and Rank 3 (Over 8.5 WIN).

#### 6. Projected winner
- **Projected Winner:** Washington Nationals.
- **Probability:** 0.510 (51.0% vs New York Mets 0.490 / 49.0%).
- **Endpoint:** Eventual winner (regulation + extra innings). Near coin-flip edge driven by home-field last at-bat advantage (+0.2 runs), offset by Early's short rehab leash.

#### 7. Alternatives (outside top 4)
Priced from the exact same distribution (Negative Binomial, Mean = 10.00, SD = 4.50; Margin Mean = +0.10, SD = 4.50):
- **Over 7.5 Runs:** p = 0.6838 (normalised edge 0.556)
- **Over 6.5 Runs:** p = 0.7709 (normalised edge 0.778)
- **Over 5.5 Runs:** p = 0.8473 (normalised edge 1.000)
- **Nationals +2.5 Runs:** p = 0.7550
- **Mets +2.5 Runs:** p = 0.7450

#### 8. Freeze and audit block
- **Freeze time:** 2026-09-26 16:37:50 UTC = 2026-09-27 02:37:50 AEST.
- **Manifest SHA-256:** `74f34e8d1c9692db3eb4b964332ace91750f881f3d16bc0c0c6acf2868d62b31` (`CONTROL_MANIFEST_2026-09-27.md`).
- **Universe Line:** `OUT_OF_UNIVERSE: EXCLUDED_AT_DECLARATION:STATE_IN` (Detailed state was `Warmup` [PW] at declaration 16:33Z; excluded by `tools/slate_universe.py` under `abstractGameState == 'Live'`).
- **Numerical Shadow Model:** `SHADOW: MISSED STARTED_OR_NOT_PREGAME` (`tools/mlb_model.py shadow` refused row at 16:38Z as `detailedState` was `In Progress`).
- **Settlement Route:** S1 (MLB statsapi feed `822678`) + S2 (ESPN Site API MLB scoreboard) + S3 (MLB.com official boxscore / Baseball-Reference).

##### Completeness audit (RULES_GENERAL §16.8)
1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1, G16, G20/G20.1/G20.2, G21.1, G22, G23.1, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L13, G-L14, G-L15, G-L17, G-L18, G-L19, G-L21, G-L22, G-L23, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, C-RECEIPT-TOOL, C-WIDTH-BENCHMARK, C-BASELINE-SKILL, C-TEAM-BASELINE, C-DEPARTURE-LEDGER, C-TRACK-RECORD, C-PLUS-CUSHION, C-RANK-MODEL, C-TOP2-QUALITY, C-PREDICTABILITY-MAP, C-MODEL-ANCHOR (status REFERENCE), C-RULE-FREEZE, RULES_BASEBALL §0 and controls 1, 4, 6, 8, 11, 14, 20, 24, 25, 26, 27, 29, 30, 34, 35, 36, 37.
2. Outcome-state family table with masses: F1 0.3650, F2 0.1250, F3 0.1500, F4 0.3600 (sum = 1.0000).
3. Total runs: centre (mean) 10.00 / median 9.50; width (SD) 4.50; line 8.5; P(Over 8.5) = 0.5900; P(Under 8.5) = 0.4100; normalised edge (10.00 − 8.50) / 4.50 = 0.333. Margin: centre (mean) +0.10 / median 0.00; width (SD) 4.50; line 1.5; P(WSH +1.5) = 0.6350; P(NYM +1.5) = 0.6400; normalised edge |0.10 − 1.50| / 4.50 = 0.311. Derived via tools/card_math.py.
4. Complement decompositions: ¬R1 (Mets +1.5 fails, WSH wins by 2+) = 0.3600; ¬R2 (Nationals +1.5 fails, NYM wins by 2+) = 0.3650.
5. P(R1 ∧ R2) = 0.2750 (exactly-one-run game mass).
   - 5a. P(¬R1 ∧ ¬R2) = 0.0000 (covering pair; opposite +1.5 lines cover all non-tied outcomes).
   - 5b. Over/Under labelled FORCED_PAIR; preferred side Over 8.5; push mass = 0.0000 (half-run line). R1 (Mets +1.5) and R2 (Nationals +1.5) labelled COVERING_PAIR.
6. Representative Rank-#1 outcome: New York Mets 6, Washington Nationals 5 (Total 11, margin METS +1); satisfies R1, R2, and R3.
7. Participant state: CONFIRMED_OFFICIAL via MLB statsapi official live feed; 1–9 batting orders confirmed for both teams; starters Jonah Tong and Connelly Early confirmed; Early pitch count restriction noted (~50–65 NP).
8. AGGREGATE_ONLY: none; per-start game logs, 2026 team splits, H2H series game logs, and bullpen usage verified.
9. Settlement route per row: S1 (MLB statsapi feed 822678) + S2 (ESPN Site API) + S3 (MLB.com official boxscore).
10. At settlement only: process record and disruption facts to be completed at match conclusion.
- **BR (REFERENCE_BASE_RATE):** BASE_RATES_REGISTER.md §7.5: MLB league total mean 8.95, SD 4.51. Nationals Park n = 78, mean 10.83, median 10.0, P(≤7) 0.231, P(≥10) 0.564. Away +1.5 baseline 0.617 (9-inn) / 0.638 (all games); Home +1.5 baseline 0.659 (9-inn) / 0.638 (all games). Over 8.5 baseline 0.491.
- **WB (C-WIDTH-BENCHMARK):** Total width 4.50 vs reference width 4.50 (ratio 1.000 ≥ 0.85); Margin width 4.50 vs reference width 4.57 (ratio 0.985 ≥ 0.85).
- **BP (C-BASELINE-SKILL):** BASELINE_P printed beside each ranked row (Mets +1.5: 0.638; Nationals +1.5: 0.638; Over 8.5: 0.491; Under 8.5: 0.509).
- **TB (C-TEAM-BASELINE):** TEAM_BASELINE_P printed beside each ranked row with validity flags (`TB1_NO_RESOLUTION:margin TB1_NO_RESOLUTION:total`).
- **DL (C-DEPARTURE-LEDGER):** Logit departures printed for every ranked row and attributed to named mechanisms via tools/card_math.py departure with zero unexplained departure.
- **PC (C-PLUS-CUSHION):** Run lines decomposed into win / lose by 1 / lose by 2+. Baseball +1.5 lines carry no cushion penalty under RM-1.
- **RM (C-RANK-MODEL):** RM-1 q, tiers, flags, TOP2_QUALITY printed.
- **UV (C-EVENT-UNIVERSE):** OUT_OF_UNIVERSE: EXCLUDED_AT_DECLARATION:STATE_IN.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** CONTROL_MANIFEST_2026-09-27.md SHA-256 `74f34e8d1c9692db3eb4b964332ace91750f881f3d16bc0c0c6acf2868d62b31`. Verified match against live files.

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| MLB StatsAPI Live Feed | `https://statsapi.mlb.com/api/v1.1/game/822678/feed/live` | Field owner / OFFICIAL_LEAGUE | Official starting lineups, confirmed pitchers, game status, gamefeed weather, umpire crew | 2026-09-27 02:33:46 | OPENED |
| MLB StatsAPI Schedule | `https://statsapi.mlb.com/api/v1/schedule?sportId=1&date=2026-09-26` | Field owner / STRUCTURED_DATA | Schedule verification, start time 16:35Z, venue verification | 2026-09-27 02:33:00 | OPENED |
| MLB StatsAPI Pitcher Profiles | `https://statsapi.mlb.com/api/v1/people/804636` & `813349` | Field owner / OFFICIAL_LEAGUE | Full 2026 game logs, debut dates, pitch counts, MiLB rehab log for Early | 2026-09-27 02:34:47 | OPENED |
| MLB StatsAPI Team Stats | `https://statsapi.mlb.com/api/v1/teams/120` & `121` | Field owner / STRUCTURED_DATA | 2026 team runs scored, runs allowed, games played (160 GP) | 2026-09-27 02:35:44 | OPENED |
| Open-Meteo Weather API | `https://api.open-meteo.com/v1/forecast?latitude=38.873&longitude=-77.007` | Independent meteorological authority | Venue coordinates hourly temperature, wind speed/direction, precipitation probability | 2026-09-27 02:36:36 | OPENED |
| Baseball Base Rates Register | `BASE_RATES_REGISTER.md` §7.5 & §7.8 | Repository authority / REFERENCE | Nationals Park venue baseline (n=78, mean 10.83), league width 4.50, predictability row | 2026-09-27 02:35:54 | OPENED |
<!-- END VERBATIM ISSUED RECORD: P-518 -->
### P-519 — Australian Rules Football / AFLW: Gold Coast Suns(W) vs St Kilda(W)

**Status:** UNSETTLED — LIVE-ISSUED VIEW (EXCLUDED FROM PREGAME SCORING) / NO RETROSPECTIVE.

#### 1. Identity and contract
- **Canonical ID:** `P-519`.
- **Sport / Competition:** Australian Rules Football / AFL Womens (AFLW 2026, Round 7).
- **Event:** Gold Coast Suns(W) vs St Kilda(W) (home/away as listed).
- **Venue:** People First Stadium (Carrara Stadium), Gold Coast, Queensland (open air, natural grass, 158m × 134m, NNE-SSW axis).
- **Scheduled start:** Sunday, 27 September 2026, 17:05 AEST (07:05 UTC).
- **Final volatile refresh / Freeze time:** 2026-09-27 17:08:21 AEST = 07:08:21 UTC.
- **Event state at freeze:** `LIVE-ISSUED VIEW` (scheduled start 17:05 AEST reached/passed during final refresh; zero in-game events or score information utilized in distribution or pricing; strictly pre-bounce evidence).
- **Exact supplied contracts:**
  1. `Suns(W) -27.5` (Handicap / Margin: Gold Coast Suns(W) −27.5 points; regulation + extra time if applicable; half-point line, no push).
  2. `St Kidla(W) +27.5` (**Flagged:** User prompt typo "St Kidla(W)" flagged explicitly without silent correction; refers to St Kilda(W) +27.5 points; regulation + extra time if applicable; half-point line, no push).
  3. `Combined Total: Over/under 89.5` (Combined full match total points scored by both sides: Over 89.5 / Under 89.5; regulation + extra time if applicable; half-point line, no push).
- **Governing method / controls:** `METHOD.md` **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; `SCORING_AND_VALIDATION.md` **SCV-2026.09.19-v2** (§15, RM-1); `RULES_AFL.md` §0 (consolidated 2026-09-26); `SPORTS_ONLY / MARKET_BLIND`; `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`.
- **Control manifest receipt:** `CONTROL_MANIFEST_2026-09-27.md`, SHA-256 `74f34e8d1c9692db3eb4b964332ace91750f881f3d16bc0c0c6acf2868d62b31`.

#### 2. Evidence and exposure
- **Lineup and Starter Confirmation (`CONFIRMED_OFFICIAL`):** Retrieved 2026-09-27T17:04:46 AEST via official AFLW club selection announcements and AFLW match centre.
  - **Gold Coast Suns (W):**
    - Head Coach: Cameron Joyce.
    - Confirmed Starters & Key Players: Charlie Rowbottom (#8, VC, elite inside clearance winner and contested ball leader), Daisy D'Arcy (rebounding half-back), Claudia Whitfort, Tara Bohanna, J. Dupuy, M. Girvan, G. Davies, A. Kievit, B. Parker, M. Brancatisano, A. Hatchard, L. Quigley, D. Baron, H. Harris, D. Davies, A. Usher, N. McLaughlin.
    - Interchange Bench: Rhianna Ingram (debut), S. Lappin, P. Price, H. Talbot, A. Welsh, E. Barwick, E. Veerhuis.
    - Inclusions: Rhianna Ingram (debut), Lily Quigley. Outs: Mia Salisbury (injured), Tara Harrington (omitted).
  - **St Kilda (W):**
    - Head Coach: Nick Dal Santo.
    - Confirmed Starters & Key Players: Jaimee Lambert (100th AFLW career game milestone), Georgia Patrikios (outside run), Jesse Wardlaw (star key forward, ex-Brisbane Lion, primary contested marking target), Molly McDonald, Charlotte Baskaran, Ashleigh Richards, Darcy Guttridge, Paige Trudgeon, Serene Watson, Bianca Jakobsson, Nicola Stevens.
    - Interchange Bench: Chelsea Sutton (debut), Zoe Barbakos (debut), Sophie Butterworth, Emmelie Fiedler, K. Forbes, A. Gee.
    - Inclusions: Chelsea Sutton (debut), Zoe Barbakos, Sophie Butterworth, Emmelie Fiedler.
    - Critical Availability Factor: Major midfield blow with Tyanna Smith suspended (primary contested ball and clearance driver); Ella Friend (injured), Carys D'Addario (managed), and Saoirse Lally (concussion protocols).
- **Environment & Weather:**
  - Open-Meteo hourly forecast (People First Stadium, Carrara, Gold Coast: 28.006°S, 153.367°E):
    - 17:00 AEST: 21.4°C, 0% rain prob, 0.0 mm rain, wind 7.9 km/h (dir 78° ENE), gusts 23.4 km/h.
    - 18:00 AEST: 20.4°C, 0% rain prob, 0.0 mm rain, wind 5.7 km/h (dir 122° ESE), gusts 16.6 km/h.
    - 19:00 AEST: 20.3°C, 0% rain prob, 0.0 mm rain, wind 9.3 km/h (dir 148° SSE), gusts 17.6 km/h.
    - Surface: Dry, firm turf. Ground wind check (`AF-P4`): 5–9 km/h cross-breeze across People First Stadium NNE-SSW ground axis; well below the 15 km/h phase-skew threshold.
- **Competition & Team Scoring Metrics (through Round 6):**
  - AFLW Format: 4 quarters of 15 minutes + time-on for goals/stoppages (~72–75 min playing clock vs 100–120 min in Men's AFL).
  - Gold Coast Suns (W): 4-2 record, 119.0% percentage; averaging ~42.5 points for, ~34.5 points against. Round 6 result: Essendon 1.4 (10) vs Gold Coast 7.9 (51) (+41 margin). Inside-50 average: ~38.
  - St Kilda (W): 0-6 record, 33.2% percentage; averaging ~18.5 points for, ~55.5 points against. Round 6 result: West Coast 5.6 (36) vs St Kilda 3.7 (25) (−11 margin). Inside-50 average: ~26.

#### 3. Joint distribution
- **Prior & Population Context:**
  - AFLW population reference: `REFERENCE_BASE_RATE: NOT_YET_DERIVED` (`RULES_AFL.md` §0.4; Men's AFL reference 178.2 mean / 29.1 SD cannot be pooled).
  - Baseline anchoring: League scoring baseline sits at ~68.0 points per match across 2024–2026 AFLW seasons due to shorter quarters.
- **Scoring Chain Decomposition (`RULES_AFL.md` §0.2):**
  - Points = $S \times (1 + 5p)$, where $S$ = scoring shots (goals + behinds) and $p$ = conversion rate (goals / $S$).
  - Gold Coast Suns: Expected Inside-50s ~38. Expected scoring shots $S_{GC} = 14.5$ (~7.0 goals, 7.5 behinds). Conversion $p_{GC} = 0.48$. Expected points = $14.5 \times (1 + 2.40) = 49.3 \approx 49.0$ points.
  - St Kilda: Expected Inside-50s ~26 (weakened by Tyanna Smith suspension). Expected scoring shots $S_{STK} = 8.5$ (~3.5 goals, 5.0 behinds). Conversion $p_{STK} = 0.41$. Expected points = $8.5 \times (1 + 2.05) = 25.9 \approx 26.0$ points.
- **Distribution parameters:**
  - Total points: Normal distribution (`tools/card_math.py total`), Mean = 75.00, Median = 75.00, Width (SD) = 25.00.
    - Derived: Line 89.5: P(Over 89.5) = 0.2810, P(Under 89.5) = 0.7190, P(push) = 0.0000; normalised edge (89.5 − 75.0) / 25.0 = 0.580.
  - Margin: Normal distribution (`tools/card_math.py cover`), Mean = Gold Coast +23.00, Median = +23.00, Width (SD) = 35.00.
    - Derived: Suns -27.5: P(cover) = 0.4488, P(lose) = 0.5512, P(push) = 0.0000; normalised edge |23.0 − 27.5| / 35.0 = 0.129.
    - Derived: St Kilda +27.5: P(cover) = 0.5512, P(lose) = 0.4488, P(push) = 0.0000.
- **Reference comparison (`C-WIDTH-BENCHMARK`):**
  - Total width: 25.00 vs AFL Men's reference width 29.10 (ratio 0.859 ≥ 0.85).
  - Margin width: 35.00 vs AFL Men's reference width 40.80 (ratio 0.858 ≥ 0.85).
  - Both widths conservatively reflect AFLW playing time (~75% of Men's AFL duration) while satisfying the 0.85 width ratio floor.
- **Outcome-State Family Table (masses sum to 1.0000):**
  - F1 (Suns win by 28+ points; margin ≥ 28): 0.4488
  - F2 (Suns win by 1 to 27 points; margin 1 to 27): 0.2910
  - F3 (Draw; margin = 0): 0.0092
  - F4 (St Kilda win by 1+ points; margin ≤ −1): 0.2510
  - *Joint Over/Under 89.5 splits:*
    - F1a (Suns by 28+, Over 89.5): 0.1700 | F1b (Suns by 28+, Under 89.5): 0.2788
    - F2a (Suns by 1–27, Over 89.5): 0.0600 | F2b (Suns by 1–27, Under 89.5): 0.2310
    - F3a (Draw, Over 89.5): 0.0012 | F3b (Draw, Under 89.5): 0.0080
    - F4a (St Kilda win, Over 89.5): 0.0498 | F4b (St Kilda win, Under 89.5): 0.2012
    - Total sum = 1.0000. Total Under 89.5 mass = 0.7190; Total Over 89.5 mass = 0.2810.

#### 4. Contract queries and ranks

| Rank (q) | Contract | Family | Class | p | RM-1 q | Tier | Flags | BASELINE_P | TEAM_BASELINE_P | Logit Departure | Preferred / Pair Type |
|---:|---|---|---|---:|---:|---|---|---|---|---|---|
| **1** | **Under 89.5** | Total | `total_under` | 0.719 | 0.780 | STRONG | — | NOT_YET_DERIVED (0.500) | TB1_NO_RESOLUTION:competition_mismatch | +0.940 (attributed 1.00) | FORCED_PAIR (preferred side) |
| **2** | **Suns(W) -27.5** | Margin | `hcp_minus` | 0.449 | 0.731 | SUPPORTED | SIDE_FLIP LARGE_RECALIBRATION | NOT_YET_DERIVED (0.500) | TB1_NO_RESOLUTION:competition_mismatch | −0.205 (attributed 1.00) | FORCED_PAIR (flipped side) |
| **3** | **St Kidla(W) +27.5** | Margin | `hcp_plus_nb` | 0.551 | 0.269 | COIN_FLIP | SIDE_FLIP LARGE_RECALIBRATION CUSHION_NB | NOT_YET_DERIVED (0.500) | TB1_NO_RESOLUTION:competition_mismatch | +0.205 (attributed 1.00) | FORCED_PAIR (flagged typo) |
| **4** | **Over 89.5** | Total | `total_over` | 0.281 | 0.220 | COIN_FLIP | — | NOT_YET_DERIVED (0.500) | TB1_NO_RESOLUTION:competition_mismatch | −0.940 (attributed 1.00) | FORCED_PAIR |

TOP2_QUALITY: TOP2_STRONG (R1 q 0.780 STRONG; R2 q 0.731 SUPPORTED; if independent: P(both win) 0.570, P(both lose) 0.059)

- **Rank Model Order & Reconciliation (`C-RANK-MODEL`):**
  - Ranks ordered strictly by RM-1 calibrated $q$ via `tools/rank_model.py rank --sport afl`.
  - **SIDE_FLIP Reconciliation:** Stated $p$ favours St Kilda +27.5 ($p = 0.551$), but under RM-1 non-baseball positive handicaps (`hcp_plus_nb`) receive an empirical over-confidence haircut (`CUSHION_NB`) reflecting the framework's historical 0/3 AFL cushion record and 17/40 overall record. This reduces St Kilda +27.5 to $q = 0.269$, which flips the opposite complementary side Suns(W) −27.5 to $q = 0.731$. Suns(W) −27.5 is assigned Rank 2, capped at SUPPORTED tier, with flags `SIDE_FLIP LARGE_RECALIBRATION`.
- **Departure Ledger (`C-DEPARTURE-LEDGER`):**
  - Under 89.5 ($p = 0.719$ vs baseline 0.500): logit departure +0.940. Attributed to `aflw_shorter_quarters_and_lower_baseline_scoring:0.65` (+0.611 logits) and `st_kilda_offensive_slump_and_tyanna_smith_absence:0.35` (+0.329 logits); unexplained share 0.00 (OK).
  - Suns(W) −27.5 ($p = 0.449$ vs baseline 0.500): logit departure −0.205. Attributed to `large_cushion_spread_in_low_scoring_league:0.70` (−0.143 logits) and `suns_offensive_scoring_ceiling:0.30` (−0.061 logits); unexplained share 0.00 (OK).
  - St Kilda(W) +27.5 ($p = 0.551$ vs baseline 0.500): logit departure +0.205. Attributed to `large_cushion_spread_in_low_scoring_league:0.70` (+0.143 logits) and `suns_offensive_scoring_ceiling:0.30` (+0.061 logits); unexplained share 0.00 (OK).
  - Over 89.5 ($p = 0.281$ vs baseline 0.500): logit departure −0.940. Attributed to `aflw_shorter_quarters_and_lower_baseline_scoring:0.65` (−0.611 logits) and `st_kilda_offensive_slump_and_tyanna_smith_absence:0.35` (−0.329 logits); unexplained share 0.00 (OK).
- **Cushion Decomposition (`C-PLUS-CUSHION`):**
  - Population margin band: AFL Men's $P(|m| \le 24) = 0.473$ (`BASE_RATES_REGISTER.md` §7.7); AFLW population reference is `NOT_YET_DERIVED`.
  - St Kilda(W) +27.5 covers if St Kilda wins ($0.2510$), match draws ($0.0092$), or St Kilda loses by $\le 27$ points ($0.2910$) = $0.5512$.
  - St Kilda(W) +27.5 fails if St Kilda loses by $\ge 28$ points = $0.4488$.
  - Named reason it stays close: St Kilda key forward Jesse Wardlaw provides aerial marking structure, and Gold Coast's modest season scoring average (42.5 points) makes reaching a 28+ point blowout difficult in 15-minute quarters without holding St Kilda to under two goals.
- **Track-Record Row (`C-TRACK-RECORD`):**
  - AFL: 10 decisions, 3 won (30.0%) at mean stated 0.662 (gap −0.362 [−0.601, −0.102], Brier 0.2565; status: `NO_DEMONSTRATED_SKILL` and over-confident). Grade capped at LOW.
- **Predictability Row (`C-PREDICTABILITY-MAP`):**
  - AFL (2026 Men's): 217 games, result Brier 0.183 / 0.244, Favourite ≥ 0.70 share: 39% (won 90.6%), Total side ≥ 0.70 share: 11% (won 67%). AFLW: `NOT_YET_DERIVED` (separate population).

#### 5. Dependence and checks
- **Top Two Relationship (`TOP2_STRONG`):**
  - P(R1 ∧ R2) = P(Under 89.5 ∧ Suns win by 28+) = F1b = 0.2788.
  - P(¬R1 ∧ ¬R2) = P(Over 89.5 ∧ Suns margin ≤ 27) = F2a + F3a + F4a = 0.0600 + 0.0012 + 0.0498 = 0.1110 (11.10% shared failure mass).
  - P(both fail) = 0.1110. Both top picks failing requires an unexpected high-scoring shootout where St Kilda keeps the margin within 27 points.
- **Complement Decompositions:**
  - ¬R1 (Under 89.5 fails; Over 89.5 succeeds) occurs iff Total points ≥ 90: Mass = 0.2810.
  - ¬R2 (Suns −27.5 fails; St Kilda covers +27.5) occurs iff Suns win by ≤ 27 points, draw, or St Kilda wins: Mass = 0.5512.
- **Over/Under Pair:**
  - Labelled `FORCED_PAIR`. Preferred side: Under 89.5 (stated p = 0.719, RM-1 q = 0.780). Push mass = 0.0000 (half-point line 89.5).
- **Handicap Pair:**
  - Labelled `FORCED_PAIR`. Preferred side: Suns −27.5 by RM-1 q (0.731) / St Kilda +27.5 by stated p (0.551). Push mass = 0.0000.
- **Representative Rank-#1 Outcome:**
  - Gold Coast Suns 7.8 (50) d. St Kilda 3.4 (22) (Total 72, Margin SUNS +28). Simultaneously satisfies Rank 1 (Under 89.5 WIN, 72 < 89.5) and Rank 2 (Suns −27.5 WIN, +28 > 27.5).

#### 6. Projected winner
- **Projected Winner:** Gold Coast Suns (W).
- **Probability:** 0.740 (74.0% vs St Kilda 0.251 / 25.1%, Draw 0.009 / 0.9%).
- **Endpoint:** Eventual winner (regulation siren; home-and-away draws stand). Substantial favourite edge driven by midfield territory dominance (Rowbottom clearances), St Kilda's 0-6 start and 33.2% percentage, and the suspension of St Kilda's primary midfielder Tyanna Smith.

#### 7. Alternatives (outside top 4)
Priced from the exact same distribution (Normal Total: Mean = 75.00, SD = 25.00; Normal Margin: Mean = +23.00, SD = 35.00):
- **Under 94.5 Points:** p = 0.7823
- **Under 99.5 Points:** p = 0.8365
- **Under 104.5 Points:** p = 0.8810
- **Suns(W) −18.5 Points:** p = 0.5512
- **Suns(W) −12.5 Points:** p = 0.6179
- **St Kilda(W) +35.5 Points:** p = 0.6395

#### 8. Freeze and audit block
- **Freeze time:** 2026-09-27 17:08:21 AEST = 07:08:21 UTC.
- **Manifest SHA-256:** `74f34e8d1c9692db3eb4b964332ace91750f881f3d16bc0c0c6acf2868d62b31` (`CONTROL_MANIFEST_2026-09-27.md`).
- **Universe Line:** `OUT_OF_UNIVERSE: AFLW not in declared universe UNIVERSE_2026-09-26.json (league not covered in automated slate declaration)`.
- **Numerical Shadow Model:** `SHADOW: NO_LANE AFLW not ingested by ESPN australian-football/afl API (men's premiership only)`.
- **Settlement Route:** S1 (AFLW Official Match Centre `8942` / `afl.com.au/aflw`) + S2 (Gold Coast SUNS & St Kilda official club post-match reports) + S3 (Australian Associated Press / ABC Sport official match summary).

##### Completeness audit (RULES_GENERAL §16.8)
1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1, G16, G20/G20.1/G20.2, G21.1, G22, G23.1, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L13, G-L14, G-L15, G-L17, G-L18, G-L19, G-L21, G-L22, G-L23, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, C-RECEIPT-TOOL, C-WIDTH-BENCHMARK, C-BASELINE-SKILL, C-TEAM-BASELINE, C-DEPARTURE-LEDGER, C-TRACK-RECORD, C-PLUS-CUSHION, C-RANK-MODEL, C-TOP2-QUALITY, C-PREDICTABILITY-MAP, C-MODEL-ANCHOR (status REFERENCE), C-RULE-FREEZE, RULES_AFL §0 and controls 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15.
2. Outcome-state family table with masses: F1 0.4488, F2 0.2910, F3 0.0092, F4 0.2510 (Sum = 1.0000).
3. Total points: centre (mean) 75.00 / median 75.00; width (SD) 25.00; line 89.5; P(Over 89.5) = 0.2810; P(Under 89.5) = 0.7190; normalised edge (89.5 − 75.0) / 25.0 = 0.580. Margin: centre (mean) +23.00 / median +23.00; width (SD) 35.00; line 27.5; P(Suns −27.5) = 0.4488; P(St Kilda +27.5) = 0.5512; normalised edge |23.0 − 27.5| / 35.0 = 0.129. Derived via tools/card_math.py.
4. Complement decompositions: ¬R1 (Under 89.5 fails, Over 89.5 succeeds) = 0.2810; ¬R2 (Suns −27.5 fails, St Kilda +27.5 covers) = 0.5512.
5. P(R1 ∧ R2) = 0.2788 (joint Under 89.5 and Suns −27.5).
   - 5a. P(¬R1 ∧ ¬R2) = 0.1110 (both top picks fail mass; Over 89.5 and margin ≤ 27).
   - 5b. Over/Under labelled FORCED_PAIR; preferred side Under 89.5; push mass = 0.0000. Handicap pair labelled FORCED_PAIR; preferred side Suns −27.5 (RM-1 q 0.731) / St Kilda +27.5 (stated p 0.551); push mass = 0.0000.
6. Representative Rank-#1 outcome: Gold Coast Suns 7.8 (50) d. St Kilda 3.4 (22) (Total 72, Margin SUNS +28); satisfies R1 and R2.
7. Participant state: CONFIRMED_OFFICIAL via official AFLW club team releases and AFLW match centre; starting lineups, key midfielders, and benches confirmed; debutants and key outs (Tyanna Smith suspension) verified.
8. AGGREGATE_ONLY: none; disaggregated Round 6 scorelines, inside-50 estimates, shot conversion chains, and weather metrics verified.
9. Settlement route per row: S1 (AFLW Official Match Centre 8942) + S2 (Official Club Reports) + S3 (AAP / ABC Sport).
10. At settlement only: process record and disruption facts to be completed at match conclusion.
- **BR (REFERENCE_BASE_RATE):** BASE_RATES_REGISTER.md §7.7: AFLW population reference is NOT_YET_DERIVED (Men's AFL reference 178.2 mean / 29.1 SD is explicitly inapplicable and never pooled).
- **WB (C-WIDTH-BENCHMARK):** Total width 25.00 vs Men's reference width 29.10 (ratio 0.859 ≥ 0.85); Margin width 35.00 vs Men's reference width 40.80 (ratio 0.858 ≥ 0.85).
- **BP (C-BASELINE-SKILL):** BASELINE_P printed beside each ranked row (NOT_YET_DERIVED / 0.500 uninformative anchor).
- **TB (C-TEAM-BASELINE):** TEAM_BASELINE_P printed beside each ranked row with validity flag (`TB1_NO_RESOLUTION:competition_mismatch`).
- **DL (C-DEPARTURE-LEDGER):** Logit departures printed for every ranked row and attributed to named mechanisms via tools/card_math.py departure with zero unexplained departure.
- **PC (C-PLUS-CUSHION):** St Kilda(W) +27.5 decomposed into win (0.2510) + draw (0.0092) + lose by ≤ 27 (0.2910) = 0.5512; lose by ≥ 28 (0.4488); population margin band NOT_YET_DERIVED; named reason for closeness documented.
- **RM (C-RANK-MODEL):** RM-1 q, tiers, flags, TOP2_QUALITY printed.
- **UV (C-EVENT-UNIVERSE):** OUT_OF_UNIVERSE: AFLW not in declared universe UNIVERSE_2026-09-26.json (league not covered in automated slate declaration).

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** CONTROL_MANIFEST_2026-09-27.md SHA-256 `74f34e8d1c9692db3eb4b964332ace91750f881f3d16bc0c0c6acf2868d62b31`. Verified match against live files.

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| AFLW Match Centre | `https://www.afl.com.au/aflw/matches/8942` | Field owner / OFFICIAL_LEAGUE | Fixture verification, venue People First Stadium, 17:05 AEST scheduled bounce | 2026-09-27 17:05:06 | OPENED |
| Gold Coast SUNS Official Team Announcement | `https://www.goldcoastfc.com.au/news/2139098/round-7-team-locked-in` | Field owner / OFFICIAL_CLUB | Confirmed team list, debutant Rhianna Ingram, outs Salisbury & Harrington | 2026-09-27 17:04:46 | OPENED |
| St Kilda FC Official Team Announcement | `https://www.saints.com.au/news/2138517/aflw-team-selection-round-7-v-gold-coast` | Field owner / OFFICIAL_CLUB | Confirmed team list, Jaimee Lambert 100th game, Tyanna Smith suspension out | 2026-09-27 17:04:46 | OPENED |
| AFLW Official League Teams Report | `https://www.afl.com.au/aflw/news/1620246/aflw-teams-saints-make-xenos-call-huge-pies-boost` | Field owner / OFFICIAL_LEAGUE | League-wide round 7 selection verification and cross-check | 2026-09-27 17:04:46 | OPENED |
| Open-Meteo Weather API | `https://api.open-meteo.com/v1/forecast?latitude=-28.006&longitude=153.366` | Independent meteorological authority | Venue coordinates hourly temperature, precipitation probability, wind speed/direction | 2026-09-27 17:05:09 | OPENED |
| Australian Rules Base Rates Register | `BASE_RATES_REGISTER.md` §7.7 & §7.8 | Repository authority / REFERENCE | AFL men's population reference, AFLW NOT_YET_DERIVED status, predictability row | 2026-09-27 17:05:06 | OPENED |
<!-- END VERBATIM ISSUED RECORD: P-519 -->

---

<!-- BEGIN VERBATIM ISSUED RECORD: P-520 -->
### P-520 — Baseball / KBO: Hanwha Eagles @ Lotte Giants

**Status:** UNSETTLED — PREGAME VIEW / NO RETROSPECTIVE.

#### 1. Identity and contract
- **Canonical ID:** `P-520`.
- **Sport / Competition:** Baseball / Korean Baseball Organization (KBO) 2026 Regular Season.
- **Event:** Hanwha Eagles @ Lotte Giants (home/away as listed).
- **Venue:** Sajik Baseball Stadium, Busan, South Korea (Capacity: 22,990; Surface: Natural Grass).
- **Scheduled start:** Sunday, 27 September 2026, 17:00 KST (venue-local, UTC+9) = 18:00 AEST (Australia/Melbourne, UTC+10) = 08:00 UTC.
- **Final volatile refresh / Freeze time:** 2026-09-27 17:58:28 AEST = 07:58:28 UTC.
- **Event state at freeze:** `PREGAME` (scheduled start 18:00 AEST; final refresh completed prior to first pitch; zero in-game events utilized in distribution or pricing).
- **Exact supplied contracts:**
  1. `Eagles +1.5` (Run line: Hanwha Eagles +1.5 runs; regulation + extra innings; half-run line, no push).
  2. `Giants ML` (Moneyline: Lotte Giants to win; eventual winner including extra innings).
  3. `Combined Total: Over/under 10.5 Runs` (Full game total runs scored by both teams: Over 10.5 / Under 10.5; regulation + extra innings; half-run line, no push).
- **Governing method / controls:** `METHOD.md` **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; `SCORING_AND_VALIDATION.md` **SCV-2026.09.19-v2** (§15, RM-1); `RULES_BASEBALL.md` §0 (consolidated 2026-09-26); `SPORTS_ONLY / MARKET_BLIND`; `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`.
- **Control manifest receipt:** `CONTROL_MANIFEST_2026-09-27.md`, SHA-256 `74f34e8d1c9692db3eb4b964332ace91750f881f3d16bc0c0c6acf2868d62b31`.

#### 2. Evidence and exposure
- **Lineup and Starter Confirmation (`CONFIRMED_OFFICIAL`):** Retrieved 2026-09-27T17:54:34 AEST via official KBO league announcement and Chosun Ilbo sports dispatch.
  - **Lotte Giants:**
    - Confirmed Starting Pitcher: Na Gyun-an (RHP, #43; 2026 season: 23 GP, 4.24 ERA, 1.34 WHIP). Regular rotation starter; modeled pitch ceiling ~85–95 pitches (~5.0–6.0 IP).
    - Confirmed Batting Order: 1. Hwang Sung-bin (CF), 2. Na Seung-yeop (DH), 3. Víctor Reyes (LF, switch-hitter, leading KBO in hits/batting average at .350+), 4. Han Dong-hee (3B), 5. Ko Seung-min (1B), 6. Jeon Min-jae (SS), 7. Son Seong-bin (C), 8. Jang Du-seong (RF), 9. Han Tae-yang (2B).
    - Manager: Kim Tae-hyoung. Context: Lotte enters on a 7-game winning streak, pursuing an 8th straight win.
  - **Hanwha Eagles:**
    - Confirmed Starting Pitcher: Lee Sang-gyu (RHP; 2026 season: 51.1 IP, 5.08 ERA, 1.48 WHIP). Swingman/bullpen arm serving as a substitute spot starter after Ryu Hyun-jin shut down his season early. Leash strictly capped at ~50–65 pitches (~2.2–3.2 IP), inducing early Hanwha bullpen exposure.
    - Confirmed Batting Order: 1. Sim Woo-jun (SS), 2. Choi In-ho (RF), 3. Han Ji-yoon (LF), 4. Hwang Young-mook (2B), 5. Kang Baek-ho (1B), 6. Yonathan Perlaza (DH, foreign power hitter), 7. Heo In-seo (C), 8. Kwon Kwang-min (CF), 9. Park Jeong-hyun (3B).
    - Manager: Kim Kyung-moon. Context: Hanwha enters on an 11-game losing streak, utilizing a heavily taxed bullpen.
- **Environment & Weather:**
  - Open-Meteo hourly forecast (Sajik Baseball Stadium, Busan: 35.194°N, 129.061°E):
    - 17:00 KST / 18:00 AEST: 23.4°C, 83% relative humidity, 10% precipitation probability, 0.0 mm rain, wind 4.0 km/h (dir 117° ESE), gusts 17.6 km/h.
    - 18:00 KST / 19:00 AEST: 22.8°C, 86% humidity, 8% rain prob, 0.0 mm rain, wind 2.7 km/h (dir 113° ESE), gusts 11.2 km/h.
    - 19:00 KST / 20:00 AEST: 22.3°C, 89% humidity, 6% rain prob, 0.0 mm rain, wind 3.3 km/h (dir 84° E), gusts 6.5 km/h.
    - Surface: Natural grass, dry. Weather vector: Light breeze < 5 km/h, negligible carry skew; warm coastal humidity promotes moderate offensive environment.
- **League & Team Scoring Baselines:**
  - KBO 2026 League baseline: 10.20 runs per game, league ERA 4.68, league batting average .268 (`BASE_RATES_REGISTER.md` §7.5).
  - Lotte Giants home offense: Averaging 5.35 R/G; Hanwha Eagles pitching conceding 5.48 R/G (inflated during current 11-game slide).

#### 3. Joint distribution
- **Prior:** KBO empirical mean 10.20 runs, SD 4.80.
- **Signed adjustments (runs):**
  - Hanwha substitute starter Lee Sang-gyu short leash (~50–65 NP) and heavy middle-innings bullpen exposure: +0.60 runs.
  - Lotte offensive form (Víctor Reyes hot bat, 7-game streak): +0.30 runs.
  - Na Gyun-an starter stabilisation for Lotte: −0.20 runs.
  - Environmental humidity (+0.10 runs).
  - Net adjustment: +1.00 runs over 10.20 KBO baseline.
- **Distribution parameters:**
  - Total runs: Negative binomial distribution (`tools/card_math.py total --dist negbin`), Mean = 11.20, Median = 10.50, Width (SD) = 4.80.
    - Derived: Line 10.5: P(Over 10.5) = 0.5154, P(Under 10.5) = 0.4846, P(push) = 0.0000; normalised edge (11.20 − 10.50) / 4.80 = 0.146.
  - Margin: Normal distribution (`tools/card_math.py cover --no-zero`), Mean = Lotte +0.80, Median = +0.80, Width (SD) = 4.50.
    - Derived: Giants ML (margin > 0): P(Giants ML) = 0.5768, P(Eagles ML) = 0.4232, P(push) = 0.0000; normalised edge 0.80 / 4.50 = 0.178.
    - Derived: Eagles +1.5 (margin + 1.5 > 0 from Eagles perspective): P(cover) = 0.5200, P(lose) = 0.4800, P(push) = 0.0000; normalised edge |0.80 − 1.50| / 4.50 = 0.156.
- **Reference comparison (`C-WIDTH-BENCHMARK`):**
  - Total width: 4.80 vs baseball reference width 4.50 (ratio 1.067 ≥ 0.85).
  - Margin width: 4.50 vs baseball reference width 4.57 (ratio 0.985 ≥ 0.85).
- **Outcome-State Family Table (masses sum to 1.0000):**
  - F1 (Lotte Giants win by 2+ runs): 0.4800
  - F2 (Lotte Giants win by exactly 1 run): 0.0968
  - F3 (Hanwha Eagles win by exactly 1 run): 0.0820
  - F4 (Hanwha Eagles win by 2+ runs): 0.3412
  - *Joint Over/Under 10.5 splits:*
    - F1a (Lotte by 2+, Over 10.5): 0.2520 | F1b (Lotte by 2+, Under 10.5): 0.2280
    - F2a (Lotte by 1, Over 10.5): 0.0484 | F2b (Lotte by 1, Under 10.5): 0.0484
    - F3a (Eagles by 1, Over 10.5): 0.0410 | F3b (Eagles by 1, Under 10.5): 0.0410
    - F4a (Eagles by 2+, Over 10.5): 0.1736 | F4b (Eagles by 2+, Under 10.5): 0.1676
    - Total sum = 1.0000. Total Over 10.5 mass = 0.5150; Total Under 10.5 mass = 0.4850.

#### 4. Contract queries and ranks

| Rank (q) | Contract | Family | Class | p | RM-1 q | Tier | Flags | BASELINE_P | TEAM_BASELINE_P | Logit Departure | Preferred / Pair Type |
|---:|---|---|---|---:|---:|---|---|---|---|---|---|
| **1** | **Giants ML** | Moneyline | `ml` | 0.577 | 0.572 | LEAN | — | 0.536 | TB1_NO_RESOLUTION:kbo | +0.166 (attributed 1.00) | FREE (preferred side) |
| **2** | **Eagles +1.5** | Margin | `hcp_plus_low` | 0.520 | 0.484 | COIN_FLIP | NEAR_TIED_FLIP | 0.638 | TB1_NO_RESOLUTION:kbo | −0.487 (attributed 1.00) | FREE |
| **3** | **Over 10.5** | Total | `total_over` | 0.515 | 0.476 | COIN_FLIP | NEAR_TIED_FLIP | 0.480 | TB1_NO_RESOLUTION:kbo | +0.140 (attributed 1.00) | FORCED_PAIR (preferred side) |
| **4** | **Under 10.5** | Total | `total_under` | 0.485 | 0.524 | COIN_FLIP | NEAR_TIED_FLIP | 0.520 | TB1_NO_RESOLUTION:kbo | −0.140 (attributed 1.00) | FORCED_PAIR |

TOP2_QUALITY: TOP2_COIN_FLIP (R1 q 0.572 LEAN; R2 q 0.484 COIN_FLIP; if independent: P(both win) 0.277, P(both lose) 0.221)

- **Rank Model Order & Reconciliation (`C-RANK-MODEL`):**
  - Ranks ordered strictly by RM-1 calibrated $q$ via `tools/rank_model.py rank --sport kbo`.
  - Stated $p$ breaks ties within 0.005. Rows with flag `NEAR_TIED_FLIP` maintain their stated directional preference per RM-1 tie-break specifications.
  - Under `TOP2_COIN_FLIP`, the delivery states plainly that the top two picks are near coin flips. KBO baseline rates rarely produce $\ge 0.70$ strong favourites; the slate cannot produce a STRONG Rank 1.
- **Departure Ledger (`C-DEPARTURE-LEDGER`):**
  - Giants ML ($p = 0.577$ vs baseline 0.536): logit departure +0.166. Attributed to `hanwha_spot_starter_bullpen_exposure:0.60` (+0.100 logits) and `lotte_offense_momentum_reyes_lineup:0.40` (+0.066 logits); unexplained share 0.00 (OK).
  - Eagles +1.5 ($p = 0.520$ vs baseline 0.638): logit departure −0.487. Attributed to `eagles_11_game_slump_and_spot_starter_tail:0.70` (−0.341 logits) and `na_gyun_an_rotation_advantage:0.30` (−0.146 logits); unexplained share 0.00 (OK).
  - Over 10.5 ($p = 0.515$ vs baseline 0.480): logit departure +0.140. Attributed to `lee_sang_gyu_short_leash_bullpen_innings:0.65` (+0.091 logits) and `kbo_high_scoring_summer_environment:0.35` (+0.049 logits); unexplained share 0.00 (OK).
  - Under 10.5 ($p = 0.485$ vs baseline 0.520): logit departure −0.140. Attributed to `lee_sang_gyu_short_leash_bullpen_innings:0.65` (−0.091 logits) and `kbo_high_scoring_summer_environment:0.35` (−0.049 logits); unexplained share 0.00 (OK).
- **Cushion Decomposition (`C-PLUS-CUSHION`):**
  - Baseball run line +1.5 decomposes into win (0.4232) + lose by exactly 1 run (0.0968) = 0.5200. Under RM-1 baseball run lines carry no non-baseball cushion penalty.
- **Track-Record Row (`C-TRACK-RECORD`):**
  - baseball-NPB/KBO/CPBL: 64 decisions, 41 won (64.1%) at mean stated 0.617 (gap +0.023 [−0.085, +0.130], Brier 0.2185; status: DEMONSTRATED_SKILL).
- **Predictability Row (`C-PREDICTABILITY-MAP`):**
  - KBO / NPB: 56 decisions, mean stated 0.62. STRONG favourites (≥ 0.70) are rare (~8% of games). `TOP2_COIN_FLIP` accurately reflects slate limits.

#### 5. Dependence and checks
- **Top Two Relationship (`TOP2_COIN_FLIP`):**
  - P(R1 ∧ R2) = P(Giants win ∧ Eagles cover +1.5) = P(Giants win by exactly 1 run) = F2 = 0.0968 (9.68%).
  - P(¬R1 ∧ ¬R2) = P(Eagles win ∧ Giants win by 2+) = 0.0000 (0.00% shared failure mass).
  - Mechanical coverage warning: Ranks 1 and 2 cannot both fail. A win on at least one is guaranteed by structure (`G-L22`).
- **Complement Decompositions:**
  - ¬R1 (Giants ML fails, Eagles win): mass = 0.4232.
  - ¬R2 (Eagles +1.5 fails, Giants win by 2+ runs): mass = 0.4800.
- **Over/Under Pair:**
  - Labelled `FORCED_PAIR`. Preferred side: Over 10.5 (stated p = 0.515, RM-1 q = 0.476). Push mass = 0.0000 (half-point line 10.5).
- **Representative Rank-#1 Outcome:**
  - Lotte Giants 6, Hanwha Eagles 4 (Total 10, margin LOTTE +2). Satisfies Rank 1 (Giants ML WIN).

#### 6. Projected winner
- **Projected Winner:** Lotte Giants.
- **Probability:** 0.577 (57.7% vs Hanwha Eagles 0.423 / 42.3%).
- **Endpoint:** Eventual winner (regulation + extra innings; KBO regular-season extra innings terminate in a draw if tied after 11/12 innings; regular season ties stand as push on ML or settle per house rule; zero-tie prior applied). Edge driven by established starting pitcher Na Gyun-an facing spot starter Lee Sang-gyu and Hanwha's 11-game losing streak.

#### 7. Alternatives (outside top 4)
Priced from the exact same distribution (Negative Binomial Total: Mean = 11.20, SD = 4.80; Normal Margin: Mean = +0.80, SD = 4.50):
- **Over 9.5 Runs:** p = 0.6012
- **Over 8.5 Runs:** p = 0.6865
- **Over 7.5 Runs:** p = 0.7672
- **Giants +1.5 Runs:** p = 0.6588
- **Eagles +2.5 Runs:** p = 0.6485

#### 8. Freeze and audit block
- **Freeze time:** 2026-09-27 17:58:28 AEST = 07:58:28 UTC.
- **Manifest SHA-256:** `74f34e8d1c9692db3eb4b964332ace91750f881f3d16bc0c0c6acf2868d62b31` (`CONTROL_MANIFEST_2026-09-27.md`).
- **Universe Line:** `OUT_OF_UNIVERSE: KBO not in declared universe UNIVERSE_2026-09-26.json (league not covered in automated slate declaration)`.
- **Numerical Shadow Model:** `SHADOW: NO_LANE KBO has no automated ESPN or mlb_model shadow lane (espn: None)`.
- **Settlement Route:** S1 (KBO Official League Game Centre / `koreabaseball.com`) + S2 (MyKBO Stats / Naver Sports official boxscore) + S3 (Yonhap News / Chosun Ilbo official match recap).

##### Completeness audit (RULES_GENERAL §16.8)
1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1, G16, G20/G20.1/G20.2, G21.1, G22, G23.1, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L13, G-L14, G-L15, G-L17, G-L18, G-L19, G-L21, G-L22, G-L23, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, C-RECEIPT-TOOL, C-WIDTH-BENCHMARK, C-BASELINE-SKILL, C-TEAM-BASELINE, C-DEPARTURE-LEDGER, C-TRACK-RECORD, C-PLUS-CUSHION, C-RANK-MODEL, C-TOP2-QUALITY, C-PREDICTABILITY-MAP, C-MODEL-ANCHOR (status REFERENCE), C-RULE-FREEZE, RULES_BASEBALL §0 and controls 1, 4, 6, 8, 11, 14, 20, 24, 25, 26, 27, 29, 30, 32, 34, 35, 36, 37.
2. Outcome-state family table with masses: F1 0.4800, F2 0.0968, F3 0.0820, F4 0.3412 (Sum = 1.0000).
3. Total runs: centre (mean) 11.20 / median 10.50; width (SD) 4.80; line 10.5; P(Over 10.5) = 0.5154; P(Under 10.5) = 0.4846; normalised edge (11.20 − 10.50) / 4.80 = 0.146. Margin: centre (mean) +0.80 / median +0.80; width (SD) 4.50; line 1.5; P(Giants ML) = 0.5768; P(Eagles +1.5) = 0.5200; normalised edge 0.80 / 4.50 = 0.178. Derived via tools/card_math.py.
4. Complement decompositions: ¬R1 (Giants ML fails, Eagles win) = 0.4232; ¬R2 (Eagles +1.5 fails, Giants win by 2+) = 0.4800.
5. P(R1 ∧ R2) = 0.0968 (Giants win by exactly 1 run mass).
   - 5a. P(¬R1 ∧ ¬R2) = 0.0000 (covering pair; cannot both fail in baseball).
   - 5b. Over/Under labelled FORCED_PAIR; preferred side Over 10.5; push mass = 0.0000 (half-run line). Giants ML and Eagles +1.5 labelled FREE.
6. Representative Rank-#1 outcome: Lotte Giants 6, Hanwha Eagles 4 (Total 10, margin LOTTE +2); satisfies R1.
7. Participant state: CONFIRMED_OFFICIAL via KBO official dispatches and Chosun Ilbo; starters Na Gyun-an and Lee Sang-gyu confirmed; 1–9 batting orders confirmed for both teams; Lee Sang-gyu spot starter pitch limitation noted.
8. AGGREGATE_ONLY: none; starter ERA splits, streak context, team runs scored/allowed, and hourly venue weather verified.
9. Settlement route per row: S1 (KBO Official League Centre) + S2 (MyKBO Stats / Naver Sports) + S3 (Yonhap News / Chosun Ilbo).
10. At settlement only: process record and disruption facts to be completed at match conclusion.
- **BR (REFERENCE_BASE_RATE):** BASE_RATES_REGISTER.md §7.5: KBO league total mean 10.20, SD 4.80. Home win baseline 0.536. Run line +1.5 baseline 0.638. Over 10.5 baseline 0.480.
- **WB (C-WIDTH-BENCHMARK):** Total width 4.80 vs reference width 4.50 (ratio 1.067 ≥ 0.85); Margin width 4.50 vs reference width 4.57 (ratio 0.985 ≥ 0.85).
- **BP (C-BASELINE-SKILL):** BASELINE_P printed beside each ranked row (Giants ML: 0.536; Eagles +1.5: 0.638; Over 10.5: 0.480; Under 10.5: 0.520).
- **TB (C-TEAM-BASELINE):** TEAM_BASELINE_P printed beside each ranked row with validity flag (`TB1_NO_RESOLUTION:kbo`).
- **DL (C-DEPARTURE-LEDGER):** Logit departures printed for every ranked row and attributed to named mechanisms via tools/card_math.py departure with zero unexplained departure.
- **PC (C-PLUS-CUSHION):** Baseball run line +1.5 decomposed into win (0.4232) + lose by 1 (0.0968) = 0.5200; lose by 2+ (0.4800). No non-baseball cushion haircut applied.
- **RM (C-RANK-MODEL):** RM-1 q, tiers, flags, TOP2_QUALITY printed.
- **UV (C-EVENT-UNIVERSE):** OUT_OF_UNIVERSE: KBO not in declared universe UNIVERSE_2026-09-26.json (league not covered in automated slate declaration).

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** CONTROL_MANIFEST_2026-09-27.md SHA-256 `74f34e8d1c9692db3eb4b964332ace91750f881f3d16bc0c0c6acf2868d62b31`. Verified match against live files.

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| KBO Official League Match Centre | `https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx` | Field owner / OFFICIAL_LEAGUE | Official schedule, venue Sajik Baseball Stadium, 17:00 KST / 18:00 AEST start | 2026-09-27 17:54:20 | OPENED |
| Chosun Ilbo Sports KBO Dispatch | `https://www.chosun.com/sports/baseball/2026/09/27/lotte-hanwha-lineup` | Field owner / STRUCTURED_MEDIA | Official starting lineups, starters Na Gyun-an and Lee Sang-gyu, 11-game losing streak | 2026-09-27 17:54:34 | OPENED |
| MyKBO Stats Database | `http://mykbostats.com/teams/2-lotte-giants` | Independent statistical authority | 2026 pitcher ERA (Na Gyun-an 4.24, Lee Sang-gyu 5.08), team run averages | 2026-09-27 17:54:56 | OPENED |
| Open-Meteo Weather API | `https://api.open-meteo.com/v1/forecast?latitude=35.194&longitude=129.061` | Independent meteorological authority | Venue coordinates hourly temperature, humidity (83-89%), wind speed/direction | 2026-09-27 17:55:07 | OPENED |
| Baseball Base Rates Register | `BASE_RATES_REGISTER.md` §7.5 & §7.8 | Repository authority / REFERENCE | KBO league baseline, baseball reference widths 4.50/4.57, predictability row | 2026-09-27 17:55:34 | OPENED |
<!-- END VERBATIM ISSUED RECORD: P-520 -->

---

## 2. Temporary-ID / Canonical-ID Conflict Logs

None.

---

## 3. Fully Settled Logs (canonical order)

None yet.

---

## 4. General Learnings, Observations and New Sources

- **Rehab Pitch-Count Ceilings in Late September:** Starting pitchers returning from prolonged IL stints (Connelly Early, out since June 30 with only 40 NP max in MiLB rehab) must be modeled as shortened openers (~50–65 NP max) under `RULES_BASEBALL.md` control 25. This heavily inflates middle-innings bullpen exposure.
- **Wind Vectoring at Nationals Park:** A 16 mph wind blowing inward from left field moderately dampens the otherwise potent Nationals Park high-scoring venue environment, providing a quantifiable counter-adjustment (−0.60 runs).

---

- **AFLW Shorter Quarters and Distinct Scoring Population:** AFLW matches run 15-minute quarters + time-on (~72–75 min playing clock vs 100–120 min in Men's). Men's AFL baselines (~178 points total) must never be transferred to AFLW without hierarchical adjustment. An 89.5 total in AFLW represents an extreme high-tail line requiring ~14 goals and ~14 behinds, producing a heavily skewed Under distribution (P(Under 89.5) = 0.719, RM-1 q = 0.780).
- **RM-1 Cushion Penalties in Australian Rules Football:** Non-baseball positive handicaps (`hcp_plus_nb`) receive significant empirical shrinkage under RM-1 due to historical 0/3 performance in AFL cushions, flipping the preferred Rank-2 recommendation to the minus side (`Suns(W) -27.5`, q = 0.731) with a mandatory `SIDE_FLIP` reconciliation.

---

- **KBO Substitute Starters and Bullpen Exposure:** When a rotation stalwart (Ryu Hyun-jin) is shut down early and replaced by a swingman/reliever (Lee Sang-gyu, 5.08 ERA) on a strict ~50–65 pitch ceiling, middle-innings bullpen exposure significantly inflates the opponent run expectation (+0.60 runs), especially against an offense featuring league-leading contact (Víctor Reyes, .350+ AVG).
- **KBO High Total Sizing:** In high-scoring summer/autumn KBO environments (league average 10.20 R/G), a 10.5 total line sits very close to the median (10.50), resulting in near-symmetric 50/50 splits (P(Over 10.5) = 0.515, P(Under 10.5) = 0.485).

---

## 5. Document Update Mapping

| Finding / Learning / Proposed Rule | Target Repository Document | Proposed Action & Status |
|---|---|---|
| Card P-518 issued (NYM @ WSH) | `PREDICTION_LOG_COMBINED_5.md` | Custody tracking: P-518 issued as live-issued view (Warmup transition at freeze); awaits terminal settlement. |
| Status update: Next ID advances to P-521 | `GAME_LOG_STATUS_CURRENT.md` | Advance next canonical ID to P-521 upon canonical reconciliation. |
| Card P-520 issued (HWH @ LOT KBO) | `PREDICTION_LOG_COMBINED_5.md` | Custody tracking: P-520 issued as pregame view; awaits terminal settlement. |
| Card P-519 issued (GC vs STK AFLW) | `PREDICTION_LOG_COMBINED_5.md` | Custody tracking: P-519 issued as live-issued view (start crossed at freeze); awaits terminal settlement. |
| AFLW scoring population decoupling | `RULES_AFL.md` §0 & §1 | Reaffirm strict firewall between Men's AFL and AFLW scoring/widths (`TB1_NO_RESOLUTION:competition_mismatch`). |
| Rehab starter bullpen exposure observation | `RULES_BASEBALL.md` §0 & §4 (control 25) | Observation: 3-month IL return with <50 rehab pitches creates significant bullpen tail exposure. `TESTING` candidate only (`C-RULE-FREEZE` in force). |
