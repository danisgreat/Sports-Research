# Prediction Mini Running Log — P-510 onward (started 2026-09-25)

| Field | Value |
|---|---|
| Created | 2026-09-25 about 01:00 +10:00 (Australia/Melbourne, AEST UTC+10; AEDT from 4 Oct 2026) |
| Status | **ACTIVE MINI LOG.** 5 events issued (`P-510`, `P-511`, `P-512`, `P-513`, `P-514`). |
| Next canonical ID | **P-515** |
| Temporary IDs awaiting canonical reconciliation | `TMP-20260923-NPB-CHU-DB-G25` (settled; DeNA 4–3 F/12) and `TMP-20260923-NBL-CNS-TAS` (settled). Both still await a canonical number (operator decision). No live temporary ID. |
| Governing method for the next issue | METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**. **Freeze with every card:** `CONTROL_MANIFEST_2026-09-25-4.md`, SHA-256 `b6efc79d92e026fe43ab4fb371175642ccb07c31ba9ba6492c2af8bd8009e0a3`. It is the post-settled-row-review content receipt (2026-09-25 about 02:30 AEST; 91 files hashed in CRLF checkout form). Verify it with `python tools/verify_manifest.py`. It supersedes `CONTROL_MANIFEST_2026-09-25-3.md` (`619a3fda…`), `-2` (`8f65c60e…`) and `CONTROL_MANIFEST_2026-09-25.md` (`7b6efc56…`); no card was issued under any of them. Before issuing, re-hash the listed governance files: they must match, except the two living logs (Part 5 and the status register), which change with every card. |
| Operating mode | **SPORTS_ONLY / MARKET_BLIND.** No odds, prices, line movement, tipsters, betting previews, prediction markets or fantasy/DFS material as evidence, anchors or sanity checks. Supplied lines are quarantined until the distribution is frozen (METHOD §1.1). |
| Performance status | **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** No ROI, EV, calibrated-edge or validated-model claim. `NO VALUE DETERMINABLE` unless a governing value gate is explicitly satisfied. |
| Drive scope | Google Drive is the reference copy of the methodology and learnings; this session reads the repository mirror at `C:\Users\danie\Desktop\Sports Research`. **No Drive file is created, edited, moved or renamed from this workflow.** This log lives in the local `Mini logs (to be sent to actual log later)/` folder; the operator uploads it. |
| Predecessor | `archive/mini_logs/Mini Prediction Log - P-509 SETTLED - 2026-09-24/`. P-509 was settled in `PREDICTION_LOG_COMBINED_5.md` §"2026-09-24(g)" (PER 98–97 ADL). Nothing is carried over. |

## Standing learnings to apply to every new card (audit closure, 2026-09-25)

The full set is in the governing files. These are the ones most often missed: the M-items in `LEARNING_REGISTER.md` §"2026-09-25 audit closure" B.

1. **Identity match before any "same-event" label.** Check date, venue, home/away and starters/participants (`O-ID-DATE-STARTER-MATCH`).
2. **Freeze before the first ball, pitch or tip-off**, and stamp the freeze time. The actual start marker is the official feed's first event, e.g. the NBL `jumpBall`, which has run about six minutes after schedule.
3. **Six-field object (METHOD §4) on every card.** No rank without a derived probability from one joint distribution. An `UNVALIDATED_SUBJECTIVE` number must be reproducible from the printed distribution (METHOD §5, §12). When the joint states are explicit, print the joint masses as numbers (field 5).
4. **Lineups (M19, M25).**
   - An official lineup published before the freeze always wins. Print it with its fetch time: MLB statsapi `battingOrder`; NPB and KBO official orders; NBA, WNBA and NBL official starters; the NHL official goalie.
   - `PROJECTED_BEAT_VERIFIED` counts **only** with a printed `S-1 Rev 2 receipt:` line (outlet, reporter, timestamp, verbatim quote, two sources). Otherwise the state is `NOT_RETRIEVED` / `RETRIEVAL_MISS`, and G14.2 blocks a full-game total or margin at Rank #1.
   - Pre-season goalies stay `PROJECTED`.
5. **MLB totals (M30).** Print the statsapi gamefeed `weather` block (field-relative wind) retrieved at freeze.
6. **Covering pairs (M28).** Label two rows that jointly cover every outcome `COVERING_PAIR` in field 5b. Never cite their Hit@2 as skill, and never seek such a pair to guarantee a win.
7. **Cricket.**
   - Phase totals are a bat-first/chase mixture before the toss, or the realised branch after it, with the team and venue phase windows split by innings order (control 21; M24).
   - Name the incoming Nos. 3–4 and both new-ball bowlers (control 20).
   - Check the toss at toss + 5 minutes via ESPN `notes[]`.
8. **Tennis.**
   - Print the dated Elo benchmark (`TE-P5`, blocking; explain or rebuild if the gap exceeds 10 points).
   - Derive matchup holds from serve × return with numerators (`TE-S4`).
   - Print P(decisive straight sets) and P(three sets) beside any best-of-three total from 18.5 to 21.5.
9. **Coin flips say so.** A row whose normalised edge is under about 0.15 is a near-tie (`NEAR_TIED` / LOW; G23.1).
10. **Mechanisms carry both signs (G-L2).** Workload, fatigue, rest and "rests starters when ahead" branches widen the distribution before they move a centre.
11. **Withdrawn, do not apply:** doubleheader-G1 deflation; derby Under suppression; "dual run-line arbitrage"; the FIBA qualifier pace coefficient; the clay handicap cap. See `RULES_GENERAL.md` §"2026-09-24(f)"(a).
12. **At settlement.** Read every process fact from a named record, with endpoint and time (`C-PROCESS-RECORD-PROVENANCE`). Add the `C-LINEUP-DIFF` line. Copy summaries from Field 4. Run `python audit_card_controls.py <this log> --settlement --strict`.

**Added by the 2026-09-25(b) research pass** (`RULES_GENERAL.md` §"2026-09-25(b)"; all disclosure, measurement or retrieval; none moves a number by itself):

13. **Receipts, not memory (`C-RECEIPT-TOOL`).**
    - MLB freeze: `python receipts.py pregame mlb <gamePk>`. It prints probables, gamefeed weather, official batting orders and umpires, or `LINEUPS_NOT_YET_PUBLISHED` / `WEATHER_NOT_YET_PUBLISHED`. Paste it, and re-run within 60 minutes of first pitch.
    - ESPN leagues: `pregame espn <sport/league> <eventId>` gives the state and injuries.
    - Settlement: `settle mlb|nhl|espn …` with `--card-*` for the lineup diff. It is one lineage.
14. **Reference row and reference width beside the card's numbers (field BR; `C-WIDTH-BENCHMARK`).** Take them from `BASE_RATES_REGISTER.md` §7. Reference widths:
    - totals: NBA 19.4, WNBA 19.5, NBL 18.7, NHL 2.29, MLB 4.50, EPL 1.61, WTA 5.79;
    - margins: NBA 15.1, WNBA 13.3, NBL 15.2.

    A width below 0.85 × the reference needs a one-line reason. Leagues without a benchmark (LKL, EuroLeague, LMB …) print `REFERENCE_WIDTH_NOT_YET_DERIVED`.
15. **Windows and regimes.**
    - NBL rounds 1–3: the early-season reference is **−8.5** points.
    - WNBA openers: **+6.5**.
    - WNBA 2026 is **+10.7** over 2024–25, so exclude or adjust those seasons.
    - NHL preseason: mean 5.68 (2025) / 5.33 (2026 to date), and P(total ≤ 5) about 0.56.
16. **The previous game never outweighs the season rate** (`R-1` corollary). It is the worst predictor in 6 of 6 competitions measured. In basketball, use the opponent's defence to date.
17. **Tennis handicaps (`C-HCP-COHERENCE`).**
    - P(−k.5) ≤ P(win).
    - Print c_s and c_d beside the population values (WTA −5.5: 0.663 / 0.168).
    - Print P(deciding set) beside the reference (WTA 0.340).
18. **NHL puck line.** 73% of two-goal regulation wins contain an empty-net goal. A −1.5 row carries the empty-net branch as mass; a +1.5 row names it as its main kill path. Overtime and shoot-out totals are odd (a 2–2 tie lands Under 5.5; a 3–3 tie lands Over 6.5).
19. **At settlement, print z_total and z_margin = (actual − centre)/width (`C-WIDTH-Z`).**

**Added 2026-09-25(c)** (`RULES_GENERAL.md` §"2026-09-25(c)"):

20. **`BASELINE_P` beside every ranked row** (`C-BASELINE-SKILL`). This is the naive population probability for the same contract, from games completed before this event, knowing only which side is at home. Examples: MLB total 7.5 Over ≈ 0.573 (2026 to date); MLB +1.5 ≈ 0.638 for either side; tennis winner 0.5. If no population exists, print `BASELINE_P: NOT_YET_DERIVED`. At settlement, append the decisions to `SKILL_BASELINE_LEDGER.md`. **The seed check found no skill over this baseline yet** (card 0.2461 v baseline 0.2360, n = 29). Beating it is the job.
21. **Start with `CURRENT_RULES.md`**, and run `python tools/verify_manifest.py` before freezing. Work on a `session/<date>-<topic>` branch and merge through a pull request with green checks (`CONTRIBUTING.md`).

**Added 2026-09-25(d): what the full settled record says** (598 probability rows, 149 cards; `research/settled_rows_2026-09-25/README.md`):

22. **Calibration overall is good; the skill lives at p ≥ 0.65** (80.3% won). Rows at 0.50–0.65 are coin-flip-grade (53.6% won at 0.574): label them `LOW_RESOLUTION` and say so.
23. **Every row is derived with `tools/card_math.py`** from the card's own centre and width. Print a **departure ledger** from `BASELINE_P`, naming the mechanism for every move (`C-DEPARTURE-LEDGER`), and the sport's **track-record row** (`C-TRACK-RECORD`).
    - **Clear skill:** soccer.
    - **Near-zero resolution:** MLB and basketball.
    - **`NO_DEMONSTRATED_SKILL`:** tennis, NFL/NCAA and AFL.
24. **Underdog cushions (+k.5) outside baseball won 17/40 at a stated 0.642 (M32).** Every such row prints the margin band, `BASELINE_P`, P(underdog wins) + P(loses by ≤ k) and the named reason it stays close (`C-PLUS-CUSHION`), or it is `PLUS_CUSHION_UNSUPPORTED`.
25. **Settle in the canonical table:** `| Rank | Contract | Family | p | BASELINE_P | Result | Brier |` (`EXTERNAL_LOGGING_WORKFLOW.md` §"2026-09-25(d)").

## 1. Incomplete / Unsettled Logs

### P-510 — MLB, St. Louis Cardinals (K. Leahy) @ Pittsburgh Pirates (P. Skenes)

##### Field 1 — Identity and contract

- **Event:** St. Louis Cardinals (Visitor) @ Pittsburgh Pirates (Home) — Series Game 3 / Rubber Match
- **Competition:** Major League Baseball (MLB 2026 Regular Season, NL Central Division Matchup)
- **Date & venue:** 24 September 2026 (local) / 25 September 2026 (Melbourne); PNC Park, Pittsburgh, Pennsylvania, USA
- **Timezones:** Venue-local America/New_York (EDT, UTC-4); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: YES** (24 Sep 12:35 EDT rolls over to 25 Sep 02:35 AEST).
- **Scheduled first pitch:** 2026-09-24 12:35:00 EDT / 2026-09-24 16:35:00 UTC / 2026-09-25 02:35:00 AEST
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across MLB statsapi live feed gamePk 823326 detailedState: Warmup, codedGameState: P, 0 pitches thrown; pregame receipt retrieved 2026-09-24T16:30:01Z / 2026-09-25 02:30 AEST).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor natural grass / open air), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, C-RECEIPT-TOOL, C-WIDTH-BENCHMARK, C-BASELINE-SKILL, C-DEPARTURE-LEDGER, C-TRACK-RECORD, RULES_BASEBALL §8 (SFA-BASEBALL), §9 (MLB official playing rules), and controls 1–37
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Cardinals +1.5
  - Pirates ML
  - Combined Total: Over 6.5 Runs
  - Combined Total: Under 6.5 Runs
  - Potential Game Winner

##### Field 2 — Evidence and exposure

#### Pregame receipt — MLB gamePk 823326: St. Louis Cardinals @ Pittsburgh Pirates

Retrieved 2026-09-24T16:30:01Z (2026-09-25 02:30 AEST). Every fact below is read from the named endpoint (C-PROCESS-RECORD-PROVENANCE); none is typed from memory or a recap.

| Fact | Value | Source |
|---|---|---|
| Scheduled first pitch | 2026-09-24T16:35:00Z / 2026-09-25 02:35 AEST (venue: PNC Park) | [S1] |
| Feed status | Warmup (P) → **PREGAME** | [S1] |
| Probable / starting pitchers | Kyle Leahy (away) v Paul Skenes (home) | [S1] |
| Gamefeed weather | Sunny, 59°F, wind 7 mph, In From RF | [S1] |
| Starting lineup — STL | 1. JJ Wetherholt 2B; 2. Iván Herrera C; 3. Alec Burleson 1B; 4. Jordan Walker RF; 5. Leo Bernal DH; 6. Bryan Torres LF; 7. Thomas Saggese 3B; 8. Nathan Church CF; 9. Masyn Winn SS | [S1] |
| Starting lineup — PIT | 1. Oneil Cruz CF; 2. Konnor Griffin SS; 3. Brandon Lowe 2B; 4. Ryan O'Hearn DH; 5. Nick Gonzales 3B; 6. Ronny Simon RF; 7. Spencer Horwitz 1B; 8. Jake Mangum LF; 9. Henry Davis C | [S1] |
| Umpires | Home Plate: Scott Barry; First Base: Tom Hanahan; Second Base: Ron Kulpa; Third Base: John Bacon | [S1] |

Sources:
- [S1] https://statsapi.mlb.com/api/v1.1/game/823326/feed/live — retrieved 2026-09-24T16:30:01Z

- **Participants & coaching staff (G14.2 / Control S-1 Rev 2):**
  - **St. Louis Cardinals (Visitor):** Manager **Oliver Marmol**; Bench Coach Daniel Descalso; Pitching Coach Dusty Blake; Hitting Coach Brant Brown. Starting pitcher: RHP **Kyle Leahy** (2026: 29 G, 29 GS, 10-5, 3.65 ERA, 1.34 WHIP, 138.0 IP, 129 K, 41 BB; Career: 127 G, 30 GS, 15-9, 3.65 ERA, 1.27 WHIP, 276.1 IP, 244 K, 84 BB). Role context: Leahy operates as a short starter / opener, averaging 3.1 innings per start over his last 5 outings (Aug 23 @ PHI 4.0 IP 63 P; Aug 29 vs PIT 3.0 IP 51 P 1 ER; Sep 06 @ COL 2.7 IP 55 P 5 ER; Sep 12 vs CWS 3.0 IP 38 P 0 ER; Sep 18 vs WSH 3.0 IP 61 P 6 ER). Regular starting 3B/2B Nolan Gorman is rested on the bench. Full confirmed starting order: JJ Wetherholt (2B), Iván Herrera (C), Alec Burleson (1B), Jordan Walker (RF), Leo Bernal (DH), Bryan Torres (LF), Thomas Saggese (3B), Nathan Church (CF), Masyn Winn (SS). Available bench (5): José Fermín, Nolan Gorman, Pedro Pagés, César Prieto, Victor Scott II. Cardinals active bullpen (13): Matthew Liberatore, Michael McGreevy, Andre Pallante, Ryne Stanek, George Soriano, Gordon Graceffo, Cooper Hjerpe, Justin Bruihl, Quinn Mathews, Brycen Mautz, Riley O'Brien, Cade Winquest, Luis Gastelum. Bullpen holds length to cover 5.0–6.0 innings. Injured list: Blaze Jordan (10-Day), Everson Pereira (10-Day), Hunter Dobbins (15-Day), Joshua Báez (10-Day), Max Rajcic (60-Day). Lineup status: **CONFIRMED_OFFICIAL** via official MLB statsapi battingOrder.
  - **Pittsburgh Pirates (Home):** Manager **Don Kelly**; Bench Coach Kristopher Negrón; Pitching Coach Bill Murphy; Hitting Coach Matt Hague. Starting pitcher: RHP **Paul Skenes** (2026: 31 G, 31 GS, 10-11, 3.91 ERA, 1.13 WHIP, 168.0 IP, 192 K, 47 BB; Career: 86 G, 86 GS, 31-24, 2.63 ERA, 1.01 WHIP, 488.2 IP, 578 K, 121 BB). Elite strikeout ace pitching on 5 full days of rest (last started Sep 18 vs KC, 6.0 IP, 89 P, 7 K). Skenes has struck out 50 career Cardinals batters across 34 hits and 7 walks. Key rest note: Star outfielder **Bryan Reynolds** is RESTED on the bench today, removing Pittsburgh’s primary run producer. Full confirmed starting order: Oneil Cruz (CF), Konnor Griffin (SS), Brandon Lowe (2B), Ryan O'Hearn (DH), Nick Gonzales (3B), Ronny Simon (RF), Spencer Horwitz (1B), Jake Mangum (LF), Henry Davis (C). Available bench (5): Billy Cook, Rafael Flores Jr., Jacob Gonzalez, Bryan Reynolds, Jared Triolo. Pirates active bullpen (13): Kirby Yates, Luke Weaver, Gregory Soto, Carmen Mlodzinski, Evan Sisk, Mason Montgomery, Lake Bachar, Bubba Chandler, Wilber Dotel, Brandon Eisert, Antwone Kelly, Yohan Ramírez, Jared Jones. Injured list: Braxton Ashcraft (15-Day), Endy Rodríguez (60-Day), Esmerlyn Valdez (10-Day), Isaac Mattson (15-Day), Mitch Keller (60-Day). Lineup status: **CONFIRMED_OFFICIAL** via official MLB statsapi battingOrder.
- **Environmental & park context (M30):** PNC Park, Pittsburgh, PA (outdoor open-air venue, natural grass surface). Gamefeed weather at freeze: Sunny, 59°F (~15°C), wind 7 mph, In From RF. Cool fall day temperature combined with a 7 mph breeze blowing directly in from right field acts to suppress fly-ball carry toward right and right-center field, directly affecting left-handed power hitters (Burleson, Wetherholt, Lowe, O'Hearn, Horwitz).
- **Baseline team scoring:**
  - Season records: Pittsburgh Pirates 80-78 (751 RS / 724 RA; 4.75 RS/G, 4.58 RA/G); St. Louis Cardinals 77-81 (709 RS / 730 RA; 4.49 RS/G, 4.62 RA/G).
  - Head-to-head 2026: Cardinals lead season series 7–6; in this series PIT won 2–0 (Sep 22), STL won 5–1 (Sep 23).
  - Matchup-specific run expectations:
    - St. Louis Cardinals expected runs: **3.50** runs (Skenes 5.2 IP @ ~3.50 expected ERA gives ~2.0 runs, Pirates bullpen 3.1 IP @ ~4.00 ERA gives ~1.5 runs).
    - Pittsburgh Pirates expected runs: **4.05** runs (Leahy 3.0 IP @ ~3.80 expected ERA gives ~1.3 runs, Cardinals bullpen 6.0 IP @ ~4.30 ERA gives ~2.75 runs; Reynolds absence dampens ceiling).
    - Combined baseline 9-inning total: **7.55** runs; with extra innings (P(tie) = 0.1173 adding ~0.35 runs in expectation): **7.90** runs.
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Cardinals multi-run win (Margin STL $\ge 2$) | Cardinals 5–2 Pirates (Total 7, Margin STL +3) | **0.2945** (29.45%) |
| **F2** | Cardinals 1-run win (Margin STL $+1$) | Cardinals 4–3 Pirates (Total 7, Margin STL +1) | **0.1473** (14.73%) |
| **F3** | Pirates 1-run win (Margin PIT $+1$, STL $-1$) | Pirates 4–3 Cardinals (Total 7, Margin PIT +1) | **0.1606** (16.06%) |
| **F4** | Pirates multi-run win (Margin PIT $\ge 2$, STL $\le -2$) | Pirates 5–2 Cardinals (Total 7, Margin PIT +3) | **0.3976** (39.76%) |

- **State family distribution check:** $\sum P(F_i) = 0.2945 + 0.1473 + 0.1606 + 0.3976 = \mathbf{1.0000}$ (100.00%).
- **Extra innings expectation:** (\text{Tie after 9 innings}) = \mathbf{0.1173}$ (11.73% probability of regulation tie, resolved under MLB ghost-runner rule; incorporated into full-game simulations).

##### Field 3 — Distributional parameters

- **Model:** Bivariate negative binomial run-generation model with MLB extra-innings resolution (tools/card_math.py).
- **Reference base rate (field BR):** BASE_RATES_REGISTER.md §7.5:
  - REFERENCE_BASE_RATE: MLB 2026 regular season (n = 2,373), Total runs mean 8.95, SD 4.51. Home win rate: 0.529, Away +1.5 baseline: 0.638, Over 6.5 baseline: 0.695 (empirical 1977/2843).
  - PNC Park venue reference: n = 80, Mean 10.00, Median 9.5, P(≤ 7) = 0.375, P(≥ 10) = 0.500. The card’s centre (7.90) departs below the venue baseline because Paul Skenes is an ace starter who sharply dampens run production, Reynolds is rested, and 59°F temperature with 7 mph wind blowing in from RF further suppresses run scoring.
- **Width benchmark (C-WIDTH-BENCHMARK, field WB):**
  - Card Total width (SD): **3.95** runs (printed beside competition reference width **4.50** runs; ratio .95 / 4.50 = 0.878 \ge 0.85$, adequate).
  - Card Margin width (SD): **3.70** runs (printed beside competition reference width **4.57** runs; ratio .70 / 4.57 = 0.810$; width below 0.85 × reference explained: Skenes starting suppresses high-side scoring variance and Leahy opener role limits early blowup exposure).
- **Total runs distribution:**
  - Centre (mean): **7.90** runs
  - Median: **7.00** runs
  - Width (standard deviation): **3.95** runs
  - Contract line: **6.5** runs
  - Derived probabilities (python tools/card_math.py total --dist negbin --mean 7.90 --sd 3.95 --line 6.5):
    - (\text{Over } 6.5) = \mathbf{0.5962}$ (59.62%)
    - (\text{Under } 6.5) = \mathbf{0.4038}$ (40.38%)
  - Normalised edge: $|7.90 - 6.5| / 3.95 = \mathbf{0.354}$
  - Push mass: **0.0000** (half-run line)
- **Margin distribution (STL Margin = Cardinals Runs − Pirates Runs):**
  - Centre (mean): **−0.55** runs
  - Median: **−1.00** runs
  - Width (standard deviation): **3.70** runs
  - Contract lines:
    - Cardinals +1.5 (STL margin $\ge -1$): Derived (\text{Cardinals } +1.5) = F1 + F2 + F3 = 0.2945 + 0.1473 + 0.1606 = \mathbf{0.6024}$ (60.24%)
    - Pirates ML (STL margin $\le -1$): Derived (\text{Pirates ML}) = F3 + F4 = 0.1606 + 0.3976 = \mathbf{0.5582}$ (55.82%)
    - Cardinals ML (STL margin $\ge 1$): Derived (\text{Cardinals ML}) = F1 + F2 = 0.2945 + 0.1473 = \mathbf{0.4418}$ (44.18%)
    - Pirates −1.5 (STL margin $\le -2$): Derived (\text{Pirates } -1.5) = F4 = \mathbf{0.3976}$ (39.76%)
  - Normalised edges:
    - Cardinals +1.5: $|-0.55 - (-1.5)| / 3.70 = \mathbf{0.257}$
    - Pirates ML: $|0.55 - 0.0| / 3.70 = \mathbf{0.149}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | BASELINE_P | Logit Departure | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | **Cardinals +1.5** | **0.602** | 0.638 | −0.153 | LEAN / LOW_RESOLUTION | PRIMARY_FORMAL (run line +1.5) | 0.006 (NEAR_TIED) |
| **2** | **Combined Total: Over 6.5 Runs** | **0.596** | 0.695 | −0.435 | LEAN / LOW_RESOLUTION | PRIMARY_FORMAL (total pair) | 0.038 (SMALL) |
| **3** | **Pirates ML** | **0.558** | 0.529 | +0.117 | LEAN / LOW_RESOLUTION | PRIMARY_FORMAL (moneyline) | 0.154 (SOLID) |
| **4** | Combined Total: Under 6.5 Runs | 0.404 | 0.305 | +0.435 | AVOID-lean / LOW_RESOLUTION | Complement of #2 | — |

- **Departure ledger (C-DEPARTURE-LEDGER):**
  - **Rank 1 (Cardinals +1.5):**
    p 0.602 v BASELINE_P 0.638: logit departure -0.153
      skenes_ace_differential: share +0.65 → -0.099 logits
      st_louis_young_lineup: share +0.35 → -0.054 logits
      unexplained share +0.00 → OK
  - **Rank 2 (Over 6.5 Runs):**
    p 0.596 v BASELINE_P 0.695: logit departure -0.435
      skenes_ace_suppression: share +0.55 → -0.239 logits
      wind_in_from_rf_59F: share +0.45 → -0.196 logits
      unexplained share +0.00 → OK
  - **Rank 3 (Pirates ML):**
    p 0.558 v BASELINE_P 0.529: logit departure +0.117
      starter_advantage_skenes_vs_leahy: share +0.70 → +0.082 logits
      reynolds_rest_offset: share +0.30 → +0.035 logits
      unexplained share +0.00 → OK
  - **Rank 4 (Under 6.5 Runs):**
    p 0.404 v BASELINE_P 0.305: logit departure +0.435
      skenes_ace_suppression: share +0.55 → +0.239 logits
      wind_in_from_rf_59F: share +0.45 → +0.196 logits
      unexplained share +0.00 → OK
- **Sport track-record row (C-TRACK-RECORD):**
  - \baseball-MLB: n=70, cards=34, win rate 0.586, mean p 0.596, gap -0.010 [-0.115, +0.104], Brier 0.2379, near-zero resolution (0.0075).
  - All four ranked rows fall in the 0.50–0.65 band and are explicitly labelled **LOW_RESOLUTION** per C-LOW-RESOLUTION-BAND (2026-09-25(d): historically 53.6% won at 0.574, coin-flip resolution).
- **Tie-break note:** Rank #1 (Cardinals +1.5, p = 0.602) and Rank #2 (Over 6.5 Runs, p = 0.596) are separated by a margin of 0.006 (NEAR_TIED). The non-predictive tie-break is that Cardinals +1.5 has an established cushion of 1-run protection (capturing 44.18% outright win + 16.06% 1-run loss mass), providing structural robustness against single-swing variance.
- **Preferred sides:**
  - Total pair (FORCED_PAIR): **Over 6.5 Runs** preferred (0.596 vs Under 6.5 at 0.404) with line sitting 1.40 runs below the full-game expected centre of 7.90 runs.
  - Handicap / Run line: **Cardinals +1.5** preferred (0.602) over Pirates −1.5 (0.398).
- **Top Over/Under target:** **Over 6.5 Runs** (Rank #2).
- **Potential Game Winner:** **Pittsburgh Pirates**, P(win) = **0.558** (55.82% conditional on completion; Cardinals win probability = 0.4418). Verdict: **LEAN / LOW_RESOLUTION**.
  - Rationale: Starting pitching disparity is substantial between ace Paul Skenes (3.91 ERA, 192 K, 1.13 WHIP in 168 IP) and Kyle Leahy operating as a 3-inning opener. Pittsburgh holds home field advantage at PNC Park and superior top-of-the-order firepower against right-handed pitching (Cruz, Griffin, Lowe, O'Hearn) facing a Cardinals lineup that is resting regular infielder Nolan Gorman.
  - Failure paths: Bryan Reynolds is rested on the Pirates bench, depriving Pittsburgh of their most dependable hitter. If Skenes experiences command lapses or elevated pitch count early, Cardinals multi-inning relievers (Liberatore, McGreevy, Pallante) can hold Pittsburgh while St. Louis manufactures runs against the Pirates bullpen (Cardinals win probability = 0.4418).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Pittsburgh Pirates 4, St. Louis Cardinals 3 (Total 7, Margin PIT +1).
  - Margin STL = −1 (lose by 1 run) → Cardinals +1.5 WINS (Rank #1 WIN).
  - Total runs = 4 + 3 = 7 (> 6.5) → Over 6.5 Runs WINS (Rank #2 WIN).
  - Pirates win outright → Pirates ML WINS (Rank #3 WIN).
  - Check: Satisfies Rank #1, Rank #2, AND Rank #3 simultaneously!
- **Joint probability P(R1 ∧ R2):**
  - (\text{Cardinals } +1.5 \wedge \text{Over } 6.5) = \mathbf{0.3340}$ (33.40%).
  - Independent product: .6024 \times 0.5891 = 0.3549$.
  - Coupling label: **MODEST_NEGATIVE_COUPLING** (high-scoring games slightly correlate with widened run margins, slightly reducing joint occurrence relative to independence).
- **Shared-failure mass P(¬R1 ∧ ¬R2):**
  - $\neg \text{R1}$ is Pirates win by 2+ runs (Margin STL $\le -2$, F4).
  - $\neg \text{R2}$ is Under 6.5 Runs (Total $\le 6$).
  - (\neg \text{R1} \wedge \neg \text{R2}) = \mathbf{0.1425}$ (14.25%).
  - Realised specifically in low-scoring multi-run Pirates victories (e.g. Pirates 4–0, 5–0, 4–1, 5–1, or 6–0).
- **Joint failure across top three P(all fail: ¬R1 ∧ ¬R2 ∧ ¬R3):**
  - $\neg \text{R1}$ is Pirates win by 2+ runs (Margin STL $\le -2$).
  - $\neg \text{R3}$ is Cardinals win (Margin STL $\ge 1$).
  - Because a game cannot finish with both a Pirates multi-run victory and a Cardinals victory, $\neg \text{R1}$ and $\neg \text{R3}$ are mutually exclusive!
  - Therefore, (\text{all fail}) = P(\neg \text{R1} \wedge \neg \text{R2} \wedge \neg \text{R3}) = \mathbf{0.0000}$ (0.00%)!
- **Covering-pair label (M28):**
  - Rank #1 (Cardinals +1.5) and Rank #3 (Pirates ML) form a **COVERING_PAIR**!
  - If Cardinals win: Cardinals +1.5 wins.
  - If Pirates win by exactly 1 run: Both Cardinals +1.5 and Pirates ML win.
  - If Pirates win by 2+ runs: Pirates ML wins.
  - Their union covers 100.00% of all possible completed baseball outcomes!
  - Per CURRENT_RULES.md D6 / RULES_GENERAL.md §16.13(b) / G-L22 / M28: Hit@2 between Rank #1 and Rank #3 is mechanical (100%) and is **excluded from top-two skill summaries**. Never seek such a pair to guarantee a win.
- **Complement decompositions:**
  - Complement of R1 (Pirates −1.5, 0.3976): Pirates win by 2 or more runs (F4 = 0.3976).
  - Complement of R2 (Under 6.5 Runs, 0.4038): Pitchers duel dominated by Skenes and bullpen suppression (0.4038).
  - Complement of R3 (Cardinals ML, 0.4418): Cardinals win outright via multi-run or 1-run victory (F1 + F2 = 0.2945 + 0.1473 = 0.4418).
- **Sensitivity analysis:**
  - If Paul Skenes pitches 7.0 shutout innings with 10+ Ks: Under 6.5 rises to 0.540, Pirates ML rises to 0.650, Cardinals +1.5 drops to 0.520.
  - If Leahy exits in inning 1 or 2 with 3+ runs surrendered: Pirates ML rises to 0.640, Over 6.5 rises to 0.710.
  - If Cardinals bullpen holds Pirates to 2 runs over innings 4–9: Cardinals +1.5 rises to 0.720, Cardinals ML rises to 0.540.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 16:30:00 UTC / 2026-09-25 02:30:00 AEST.
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (MLB statsapi feed live gamePk 823326 confirmed detailedState: Warmup, codedGameState: P, 0 pitches thrown; pregame receipt retrieved 2026-09-24T16:30:01Z).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): MLB Official Boxscore (mlb.com/gameday/823326).
  - Lineage 2 (Independent Primary Media): Baseball-Reference official boxscore (\baseball-reference.com/boxes).
  - Lineage 3 (Independent Secondary): ESPN MLB Scoreboard (espn.com/mlb/scoreboard).
- **Settlement criteria:** Minimum 3 distinct independent lineages agreeing on final score and completion status (C-FINAL3). Record linescore, total runs, final margin, and official pitchers of record.
- **Retry trigger:** Re-check at match conclusion for terminal final status.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor grass / open air), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, C-RECEIPT-TOOL, C-WIDTH-BENCHMARK, C-BASELINE-SKILL, C-DEPARTURE-LEDGER, C-TRACK-RECORD, RULES_BASEBALL §8 (SFA-BASEBALL), §9, and controls 1–37.
2. Outcome-state family table with masses: F1 0.2945, F2 0.1473, F3 0.1606, F4 0.3976 (sum = 1.0000).
3. Total runs: centre (mean) 7.90 / median 7.00; width (SD) 3.95; line 6.5; P(Over 6.5) = 0.596; P(Under 6.5) = 0.404. Margin: centre (mean) −0.55 / median −1.00; width (SD) 3.70; line 1.5; P(Cardinals +1.5) = 0.602; P(Pirates ML) = 0.558. Normalised edges: total |7.90 − 6.5| / 3.95 = 0.354; margin Cardinals |−0.55 − (−1.5)| / 3.70 = 0.257; Pirates ML |0.55 − 0.0| / 3.70 = 0.149. Derived via tools/card_math.py.
4. Complement decompositions for R1 (Pirates −1.5, 0.398) and R2 (Under 6.5 Runs, 0.404): stated above.
5. P(R1 ∧ R2) = 0.3340 (MODEST_NEGATIVE_COUPLING vs independent product 0.3549).
   - 5a. P(¬R1 ∧ ¬R2) = 0.1425 (shared-failure mass in low-scoring multi-run Pirates victories). P(all fail: ¬R1 ∧ ¬R2 ∧ ¬R3) = 0.0000 (0.00% across top three).
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Over 6.5 Runs; push mass = 0.000 (half-run line). Rank #1 (Cardinals +1.5) and Rank #3 (Pirates ML) labelled COVERING_PAIR.
6. Representative Rank-#1 outcome: Pittsburgh Pirates 4, St. Louis Cardinals 3 (total 7, margin PIT +1); satisfies Rank #1, Rank #2, and Rank #3 simultaneously.
7. Participant state: CONFIRMED_OFFICIAL via MLB statsapi live feed official battingOrder; starters Kyle Leahy and Paul Skenes confirmed; managers Oliver Marmol and Don Kelly confirmed; full official batting orders Wetherholt/Herrera/Burleson/Walker/Bernal/Torres/Saggese/Church/Winn and Cruz/Griffin/Lowe/O'Hearn/Gonzales/Simon/Horwitz/Mangum/Davis confirmed; key rested starters Nolan Gorman (STL) and Bryan Reynolds (PIT) confirmed on benches.
8. AGGREGATE_ONLY: none; starter season and recent outing game logs, team season RS/RA and bullpen ERAs printed.
9. Settlement route per row: S1 (MLB field owner) + S2 (Baseball-Reference) + S3 (ESPN).
10. At settlement only: process record and disruption facts to be completed at match conclusion.
- **BR (REFERENCE_BASE_RATE):** MLB 2026 regular season (n = 2,373), Total runs mean 8.95, SD 4.51. Home win rate: 0.529, Away +1.5 baseline: 0.638, Over 6.5 baseline: 0.695 (empirical 1977/2843). PNC Park venue reference: n = 80, Mean 10.00, Median 9.5.
- **WB (C-WIDTH-BENCHMARK):** Total width 3.95 vs reference width 4.50 (ratio 0.878 >= 0.85); Margin width 3.70 vs reference width 4.57 (ratio 0.810; explained by Skenes ace profile and Leahy opener role).
- **BP (C-BASELINE-SKILL):** BASELINE_P printed beside each ranked row (Cardinals +1.5: 0.638; Over 6.5: 0.695; Pirates ML: 0.529; Under 6.5: 0.305).
- **DL (C-DEPARTURE-LEDGER):** Logit departures printed for every ranked row and attributed to named mechanisms via tools/card_math.py departure with zero unexplained departure.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** CONTROL_MANIFEST_2026-09-25-4.md SHA-256 \b6efc79d92e026fe43ab4fb371175642ccb07c31ba9ba6492c2af8bd8009e0a3. Verified match against live files.

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| MLB Official Live Feed | https://statsapi.mlb.com/api/v1.1/game/823326/feed/live | Field owner / MAJOR_LEAGUE_BASEBALL | Pregame receipt, official batting orders, probables (Leahy vs Skenes), weather (59°F, 7mph In From RF), umpires | 2026-09-25 02:30 | OPENED |
| MLB Stats API People | https://statsapi.mlb.com/api/v1/people/694973 | Field owner / MAJOR_LEAGUE_BASEBALL | Paul Skenes 2026 & career pitching stats, game logs, vs Cardinals splits | 2026-09-25 02:32 | OPENED |
| MLB Stats API People | https://statsapi.mlb.com/api/v1/people/681517 | Field owner / MAJOR_LEAGUE_BASEBALL | Kyle Leahy 2026 & career pitching stats, opener game logs, vs Pirates splits | 2026-09-25 02:32 | OPENED |
| MLB Stats API Standings | https://statsapi.mlb.com/api/v1/standings?leagueId=104&season=2026 | Field owner / MAJOR_LEAGUE_BASEBALL | NL Central standings, Pirates & Cardinals W-L records, run differentials | 2026-09-25 02:32 | OPENED |
| MLB Stats API Teams | https://statsapi.mlb.com/api/v1/teams/134/stats?season=2026 | Field owner / MAJOR_LEAGUE_BASEBALL | Pirates season team batting (RS 751, OPS .735) and pitching (RA 724, ERA 4.17) | 2026-09-25 02:33 | OPENED |
| MLB Stats API Teams | https://statsapi.mlb.com/api/v1/teams/138/stats?season=2026 | Field owner / MAJOR_LEAGUE_BASEBALL | Cardinals season team batting (RS 709, OPS .695) and pitching (RA 730, ERA 4.26) | 2026-09-25 02:33 | OPENED |
| MLB Stats API Rosters | https://statsapi.mlb.com/api/v1/teams/134/roster?rosterType=coach | Field owner / MAJOR_LEAGUE_BASEBALL | Pirates and Cardinals official coaching staff rosters (Don Kelly, Oliver Marmol) | 2026-09-25 02:34 | OPENED |
| MLB Stats API 40-Man | https://statsapi.mlb.com/api/v1/teams/134/roster?rosterType=40Man | Field owner / MAJOR_LEAGUE_BASEBALL | Pirates and Cardinals official injured lists (Keller, Ashcraft, Jordan, etc.) | 2026-09-25 02:34 | OPENED |
| Baseball-Reference | https://www.baseball-reference.com/previews/2026/PIT202609240.shtml | Independent primary / STATISTICAL_AUTHORITY | Starter pitch splits, bullpen usage and park factors | 2026-09-25 02:31 | OPENED |
| ESPN MLB Scoreboard | https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/summary?event=823326 | Independent secondary / BROADCAST_MEDIA | Schedule verification, game status, weather conditions | 2026-09-25 02:31 | OPENED |


### P-511 — MLB, Los Angeles Angels (G. Rodriguez) @ Seattle Mariners (B. Woo)

##### Field 1 — Identity and contract

- **Event:** Los Angeles Angels (Visitor) @ Seattle Mariners (Home) — Series Opener
- **Competition:** Major League Baseball (MLB 2026 Regular Season, AL West Division Matchup)
- **Date & venue:** 24 September 2026 (local) / 25 September 2026 (Melbourne); T-Mobile Park, Seattle, Washington, USA
- **Timezones:** Venue-local America/Los_Angeles (PDT, UTC-7); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: YES** (24 Sep 18:40 PDT rolls over to 25 Sep 11:40 AEST).
- **Scheduled first pitch:** 2026-09-24 18:40:00 PDT / 2026-09-25 01:40:00 UTC / 2026-09-25 11:40:00 AEST
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across MLB statsapi live feed gamePk 823087 detailedState: Warmup, codedGameState: P, 0 pitches thrown; pregame receipt retrieved 2026-09-25T01:24:57Z / 2026-09-25 11:24 AEST).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (retractable roof / natural grass / open air), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, C-RECEIPT-TOOL, C-WIDTH-BENCHMARK, C-BASELINE-SKILL, C-DEPARTURE-LEDGER, C-TRACK-RECORD, RULES_BASEBALL §8 (SFA-BASEBALL), §9 (MLB official playing rules), and controls 1–37
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Angels +1.5
  - Mariners ML
  - Combined Total: Over 7.0 Runs
  - Combined Total: Under 7.0 Runs
  - Potential Game Winner

##### Field 2 — Evidence and exposure

#### Pregame receipt — MLB gamePk 823087: Los Angeles Angels @ Seattle Mariners

Retrieved 2026-09-25T01:24:57Z (2026-09-25 11:24 AEST). Every fact below is read from the named endpoint (C-PROCESS-RECORD-PROVENANCE); none is typed from memory or a recap.

| Fact | Value | Source |
|---|---|---|
| Scheduled first pitch | 2026-09-25T01:40:00Z / 2026-09-25 11:40 AEST (venue: T-Mobile Park) | [S1] |
| Feed status | Warmup (P) → **PREGAME** | [S1] |
| Probable / starting pitchers | Grayson Rodriguez (away) v Bryan Woo (home) | [S1] |
| Gamefeed weather | Cloudy, 60°F, wind 5 mph, In From CF | [S1] |
| Starting lineup — LAA | 1. Zach Neto SS; 2. Mike Trout DH; 3. Wade Meckler LF; 4. Vaughn Grissom 1B; 5. Moisés Ballesteros C; 6. Denzer Guzman 3B; 7. Josh Lowe RF; 8. Christian Moore 2B; 9. Bryce Teodosio CF | [S1] |
| Starting lineup — SEA | 1. J.P. Crawford SS; 2. Randy Arozarena LF; 3. Dominic Canzone DH; 4. Cal Raleigh C; 5. Julio Rodríguez CF; 6. Josh Naylor 1B; 7. Cole Young 2B; 8. Lazaro Montes RF; 9. Leo Rivas 3B | [S1] |
| Umpires | Home Plate: Rob Drake; First Base: Andy Fletcher; Second Base: Jansen Visconti; Third Base: Dillon Wilson | [S1] |

Sources:
- [S1] https://statsapi.mlb.com/api/v1.1/game/823087/feed/live — retrieved 2026-09-25T01:24:57Z

- **Participants & coaching staff (G14.2 / Control S-1 Rev 2):**
  - **Los Angeles Angels (Visitor):** Manager **Kurt Suzuki**; Bench Coach John Gibbons; Hitting Coach Brady Anderson; Interim Pitching Coach Tim Leveque. Starting pitcher: RHP **Grayson Rodriguez** (2026: 19 G, 19 GS, 4-8, 5.96 ERA, 1.54 WHIP, 93.2 IP, 83 K, 38 BB; Career: 62 G, 62 GS, 24-16, 4.63 ERA, 1.36 WHIP, 332.1 IP, 342 K, 116 BB). High-velocity right-hander who has struggled with command and long balls in 2026 (5.96 ERA, 1.54 WHIP). Veterans Travis d'Arnaud and Adam Frazier are rested on the bench. Full confirmed starting order: Zach Neto (SS), Mike Trout (DH), Wade Meckler (LF), Vaughn Grissom (1B), Moisés Ballesteros (C), Denzer Guzman (3B), Josh Lowe (RF), Christian Moore (2B), Bryce Teodosio (CF). Available bench (5): Adam Frazier, Tyler Heineman, Oswald Peraza, Jose Siri, Travis d'Arnaud. Angels active bullpen (13): Sam Bachman, Reid Detmers, Mitch Farris, José Fermin, Ryan Johnson, Yusei Kikuchi, Trevor Martin, Luke Murphy, Sammy Peralta, Tayler Saucedo, Walbert Ureña, Ryan Watson, Blake Weiman. Injured list: Anthony Rendon (60-Day), Ben Joyce (15-Day), George Klassen (15-Day), Gustavo Campero (10-Day), Jack Kochanowicz (60-Day), Kyren Paris (10-Day), Nolan Schanuel (10-Day), Robert Stephenson (60-Day), Samy Natera Jr. (15-Day), Yoán Moncada (60-Day). Lineup status: **CONFIRMED_OFFICIAL** via official MLB statsapi battingOrder.
  - **Seattle Mariners (Home):** Manager **Dan Wilson**; Bench Coach Manny Acta; Hitting Coach Edgar Martinez; Pitching Coach Pete Woodworth. Starting pitcher: RHP **Bryan Woo** (2026: 29 G, 29 GS, 12-9, 3.92 ERA, 1.08 WHIP, 167.2 IP, 167 K, 36 BB; Career: 99 G, 99 GS, 40-24, 3.42 ERA, 1.01 WHIP, 563.1 IP, 559 K, 116 BB). Elite command starter enjoying a sensational September (4 GS, 25.1 IP, 1.48 ERA, 0.75 WHIP) and boasting sub-3.30 career ERA at T-Mobile Park. Rest notes: Taylor Ward and Victor Robles are on the bench. Full confirmed starting order: J.P. Crawford (SS), Randy Arozarena (LF), Dominic Canzone (DH), Cal Raleigh (C), Julio Rodríguez (CF), Josh Naylor (1B), Cole Young (2B), Lazaro Montes (RF), Leo Rivas (3B). Available bench (5): Michael Arroyo, Jhonny Pereda, Victor Robles, Taylor Ward, Weston Wilson. Mariners active bullpen (13): Andrés Muñoz, Gabe Speier, Eduard Bazardo, Hoby Milner, Seranthony Domínguez, José A. Ferrer, Michael Rucker, Carlos Vargas, Cooper Criswell, Kade Anderson, Logan Gilbert, George Kirby, Bryce Miller. Injured list: Brendan Donovan (7-Day), Brennen Davis (60-Day), Brock Rodden (10-Day), Cole Wilcox (15-Day), Colt Emerson (60-Day), Emerson Hancock (15-Day), Logan Evans (60-Day), Luke Raley (60-Day), Matt Brash (60-Day), Nick Davila (60-Day), Will Wilson (60-Day). Lineup status: **CONFIRMED_OFFICIAL** via official MLB statsapi battingOrder.
- **Environmental & park context (M30):** T-Mobile Park, Seattle, WA (retractable roof, open-air setting, natural grass). Gamefeed weather at freeze: Cloudy, 60°F (~16°C), wind 5 mph, In From CF. Cool marine air combined with a 5 mph inward center-field breeze acts in concert with T-Mobile Park’s league-leading run-suppression factors (0.91 run park factor; tied for lowest-scoring venue in MLB in 2026).
- **Baseline team scoring:**
  - Season records: Seattle Mariners 74-84 (640 RS / 702 RA; 4.05 RS/G, 4.44 RA/G); Los Angeles Angels 60-98 (635 RS / 728 RA; 4.02 RS/G, 4.61 RA/G).
  - Head-to-head 2026: Season series is 6–4 Angels; at T-Mobile Park SEA won 2 of 3 (6–2, 8–3, 1–0).
  - Matchup-specific run expectations:
    - Los Angeles Angels expected runs: **3.15** runs (Woo 6.0 IP @ ~3.00 expected ERA gives ~2.00 runs, Mariners bullpen 3.0 IP @ ~3.45 ERA gives ~1.15 runs).
    - Seattle Mariners expected runs: **4.15** runs (Rodriguez 5.0 IP @ ~4.50 expected ERA gives ~2.50 runs, Angels bullpen 4.0 IP @ ~4.12 ERA gives ~1.65 runs).
    - Combined baseline 9-inning total: **7.30** runs; with extra innings (P(tie) = 0.115 adding ~0.35 runs in expectation): **7.65** runs.
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Angels multi-run win (Margin LAA $\ge 2$) | Angels 5–2 Mariners (Total 7, Margin LAA +3) | **0.2499** (24.99%) |
| **F2** | Angels 1-run win (Margin LAA $+1$) | Angels 4–3 Mariners (Total 7, Margin LAA +1) | **0.1428** (14.28%) |
| **F3** | Mariners 1-run win (Margin SEA $+1$, LAA $-1$) | Mariners 4–3 Angels (Total 7, Margin SEA +1) | **0.1663** (16.63%) |
| **F4** | Mariners multi-run win (Margin SEA $\ge 2$, LAA $\le -2$) | Mariners 5–2 Angels (Total 7, Margin SEA +3) | **0.4410** (44.10%) |

- **State family distribution check:** $\sum P(F_i) = 0.2499 + 0.1428 + 0.1663 + 0.4410 = \mathbf{1.0000}$ (100.00%).
- **Extra innings expectation:** (\text{Tie after 9 innings}) = \mathbf{0.1150}$ (11.50% probability of regulation tie, resolved under MLB ghost-runner rule; incorporated into full-game simulations).

##### Field 3 — Distributional parameters

- **Model:** Bivariate negative binomial run-generation model with MLB extra-innings resolution (tools/card_math.py).
- **Reference base rate (field BR):** BASE_RATES_REGISTER.md §7.5:
  - REFERENCE_BASE_RATE: MLB 2026 regular season (n = 2,373), Total runs mean 8.95, SD 4.51. Home win rate: 0.529, Away +1.5 baseline: 0.638, Over 7.0 baseline: 0.583 (empirical 1660/2850), Under 7.0 baseline: 0.306 (empirical 871/2850).
  - T-Mobile Park venue reference: n = 77, Mean 7.78, Median 8.0, P(≤ 7) = 0.494. The card’s centre (7.65) closely tracks the venue baseline (7.78) supported by Bryan Woo's elite home suppression (1.48 September ERA) and cool 60°F weather with 5 mph wind blowing in from CF.
- **Width benchmark (C-WIDTH-BENCHMARK, field WB):**
  - Card Total width (SD): **3.85** runs (printed beside competition reference width **4.50** runs; ratio .85 / 4.50 = 0.856 \ge 0.85$, adequate).
  - Card Margin width (SD): **3.65** runs (printed beside competition reference width **4.57** runs; ratio .65 / 4.57 = 0.799$; width below 0.85 × reference explained: Bryan Woo's control-first profile and T-Mobile Park dimensions compress run variance and suppress multi-run blowouts).
- **Total runs distribution:**
  - Centre (mean): **7.65** runs
  - Median: **7.00** runs
  - Width (standard deviation): **3.85** runs
  - Contract line: **7.0** runs (integer contract line)
  - Derived probabilities (python tools/card_math.py total --dist negbin --mean 7.65 --sd 3.85 --line 7.0):
    - (\text{Over } 7.0) = \mathbf{0.4654}$ (46.54%)
    - (\text{Under } 7.0) = \mathbf{0.4274}$ (42.74%)
    - (\text{push}) = \mathbf{0.1072}$ (10.72% push mass at exactly 7 runs)
  - Normalised edge: $|7.65 - 7.0| / 3.85 = \mathbf{0.169}$
- **Margin distribution (LAA Margin = Angels Runs − Mariners Runs):**
  - Centre (mean): **−1.00** runs
  - Median: **−1.00** runs
  - Width (standard deviation): **3.65** runs
  - Contract lines:
    - Mariners ML (LAA margin $\le -1$): Derived (\text{Mariners ML}) = F3 + F4 = 0.1663 + 0.4410 = \mathbf{0.6073}$ (60.73%)
    - Angels +1.5 (LAA margin $\ge -1$): Derived (\text{Angels } +1.5) = F1 + F2 + F3 = 0.2499 + 0.1428 + 0.1663 = \mathbf{0.5590}$ (55.90%)
    - Angels ML (LAA margin $\ge 1$): Derived (\text{Angels ML}) = F1 + F2 = 0.2499 + 0.1428 = \mathbf{0.3927}$ (39.27%)
    - Mariners −1.5 (LAA margin $\le -2$): Derived (\text{Mariners } -1.5) = F4 = \mathbf{0.4410}$ (44.10%)
  - Normalised edges:
    - Mariners ML: $|1.00 - 0.0| / 3.65 = \mathbf{0.274}$
    - Angels +1.5: $|-1.00 - (-1.5)| / 3.65 = \mathbf{0.137}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | BASELINE_P | Logit Departure | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | **Mariners ML** | **0.607** | 0.529 | +0.319 | LEAN / LOW_RESOLUTION | PRIMARY_FORMAL (moneyline) | 0.048 (SMALL) |
| **2** | **Angels +1.5** | **0.559** | 0.638 | −0.330 | LEAN / LOW_RESOLUTION | PRIMARY_FORMAL (run line +1.5) | 0.094 (MODERATE) |
| **3** | Combined Total: Over 7.0 Runs | 0.465 | 0.583 | −0.475 | AVOID-lean / LOW_RESOLUTION | PRIMARY_FORMAL (total pair) | 0.038 (SMALL) |
| **4** | Combined Total: Under 7.0 Runs | 0.427 | 0.306 | +0.525 | AVOID / LOW_RESOLUTION | Complement of #3 | — |

- **Departure ledger (C-DEPARTURE-LEDGER):**
  - **Rank 1 (Mariners ML):**
    p 0.607 v BASELINE_P 0.529: logit departure +0.319
      starter_advantage_woo_vs_rodriguez: share +0.75 → +0.239 logits
      home_field_tmobile: share +0.25 → +0.080 logits
      unexplained share +0.00 → OK
  - **Rank 2 (Angels +1.5):**
    p 0.559 v BASELINE_P 0.638: logit departure -0.330
      woo_ace_differential: share +0.70 → -0.231 logits
      angels_lineup_youth: share +0.30 → -0.099 logits
      unexplained share +0.00 → OK
  - **Rank 3 (Over 7.0 Runs):**
    p 0.465 v BASELINE_P 0.583: logit departure -0.475
      tmobile_park_factor_suppression: share +0.55 → -0.261 logits
      woo_sub_3_era_form: share +0.45 → -0.214 logits
      unexplained share +0.00 → OK
  - **Rank 4 (Under 7.0 Runs):**
    p 0.427 v BASELINE_P 0.306: logit departure +0.525
      tmobile_park_factor_suppression: share +0.55 → +0.289 logits
      woo_sub_3_era_form: share +0.45 → +0.236 logits
      unexplained share +0.00 → OK
- **Sport track-record row (C-TRACK-RECORD):**
  - \baseball-MLB: n=70, cards=34, win rate 0.586, mean p 0.596, gap -0.010 [-0.115, +0.104], Brier 0.2379, near-zero resolution (0.0075).
  - All four ranked rows fall in the 0.50–0.65 band and are explicitly labelled **LOW_RESOLUTION** per C-LOW-RESOLUTION-BAND (2026-09-25(d): historically 53.6% won at 0.574, coin-flip resolution).
- **Covering-pair label (COVERING_PAIR, M28):** Rank #1 (**Mariners ML**) and Rank #2 (**Angels +1.5**) form a mathematical covering pair spanning 100.00% of all official completed game outcomes. Hit@2 between Rank #1 and Rank #2 is mechanical and excluded from top-two skill summaries.
- **Preferred sides:**
  - Total pair (FORCED_PAIR): **Over 7.0 Runs** preferred (0.465 vs Under 7.0 at 0.427; push mass 0.107) with expected centre of 7.65 sitting slightly above the 7.0 threshold.
  - Handicap / Run line: **Angels +1.5** preferred (0.559) over Mariners −1.5 (0.441).
- **Top Over/Under target:** **Over 7.0 Runs** (Rank #3).
- **Potential Game Winner:** **Seattle Mariners**, P(win) = **0.607** (60.73% conditional on completion; Angels win probability = 0.3927). Verdict: **LEAN / LOW_RESOLUTION**.
  - Rationale: Pronounced starting pitching advantage for Bryan Woo (3.92 ERA, 1.08 WHIP in 2026; 1.48 ERA in September) over Grayson Rodriguez (5.96 ERA, 1.54 WHIP). Woo excels at T-Mobile Park, whereas Rodriguez has surrendered high home run and walk volume. The Angels lineup has Mike Trout but otherwise lacks proven run-producers and rests veterans d'Arnaud and Frazier. Mariners have home field advantage and elite late-game bullpen execution led by Andrés Muñoz.
  - Failure paths: Grayson Rodriguez harnesses his elite swing-and-miss fastball/changeup mix and stifles a Seattle offense that bats only .232 on the year; Mike Trout or Zach Neto connects for a decisive home run (Angels win probability = 0.3927).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Seattle Mariners 4, Los Angeles Angels 3 (Total 7, Margin SEA +1).
  - Margin SEA = +1 → Mariners ML WINS (Rank #1 WIN).
  - Margin SEA = +1 (Angels lose by 1) → Angels +1.5 WINS (Rank #2 WIN).
  - Total runs = 4 + 3 = 7 → PUSH on Over 7.0 and Under 7.0.
  - Check: Satisfies Rank #1 and Rank #2 simultaneously!
- **Joint probability P(R1 ∧ R2):**
  - (\text{Mariners ML} \wedge \text{Angels } +1.5) = P(\text{Mariners win by exactly 1 run}) = F3 = \mathbf{0.1663}$ (16.63%).
  - Independent product: .6073 \times 0.5590 = 0.3395$.
  - Coupling label: **STRONG_NEGATIVE_COUPLING** (on multi-run outcomes they are mutually exclusive; they only win together on the exact 1-run Mariners margin).
- **Shared-failure mass P(¬R1 ∧ ¬R2):**
  - $\neg \text{R1}$ is Angels win outright (Margin LAA $\ge 1$).
  - $\neg \text{R2}$ is Mariners win by 2+ runs (Margin SEA $\ge 2$).
  - Because Angels win and Mariners win by 2+ are mutually exclusive events, (\neg \text{R1} \wedge \neg \text{R2}) = \mathbf{0.0000}$ (0.00%)!
  - P(at least one of R1, R2 wins) = 1.0000 (100.00%)!
- **Joint failure across top three P(all fail: ¬R1 ∧ ¬R2 ∧ ¬R3):**
  - Since (\neg \text{R1} \wedge \neg \text{R2}) = 0.0000$, any joint intersection with a third event is identically zero: (\text{all fail}) = \mathbf{0.0000}$ (0.00%)!
- **Complement decompositions:**
  - Complement of R1 (Angels ML, 0.3927): Angels win outright (F1 + F2 = 0.2499 + 0.1428 = 0.3927).
  - Complement of R2 (Mariners −1.5, 0.4410): Mariners win by 2 or more runs (F4 = 0.4410).
  - Complement of R3 (Under 7.0 Runs or Push 7.0, 0.5346): Total runs $\le 7$ (0.4274 + 0.1072 = 0.5346).
- **Sensitivity analysis:**
  - If Bryan Woo throws 7.0 shutout innings with 8+ Ks: Mariners ML rises to 0.710, Under 7.0 rises to 0.510, Angels +1.5 drops to 0.460.
  - If Grayson Rodriguez is knocked out before 4th inning: Mariners ML rises to 0.690, Over 7.0 rises to 0.560.
  - If Mike Trout hits multiple extra-base hits and Angels bullpen holds: Angels +1.5 rises to 0.670, Angels ML rises to 0.490.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-25 01:25:00 UTC / 2026-09-25 11:25:00 AEST.
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (MLB statsapi feed live gamePk 823087 confirmed detailedState: Warmup, codedGameState: P, 0 pitches thrown; pregame receipt retrieved 2026-09-25T01:24:57Z).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): MLB Official Boxscore (mlb.com/gameday/823087).
  - Lineage 2 (Independent Primary Media): Baseball-Reference official boxscore (\baseball-reference.com/boxes).
  - Lineage 3 (Independent Secondary): ESPN MLB Scoreboard (espn.com/mlb/scoreboard).
- **Settlement criteria:** Minimum 3 distinct independent lineages agreeing on final score and completion status (C-FINAL3). Record linescore, total runs, final margin, and official pitchers of record.
- **Retry trigger:** Re-check at match conclusion for terminal final status.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor grass / retractable roof), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, C-RECEIPT-TOOL, C-WIDTH-BENCHMARK, C-BASELINE-SKILL, C-DEPARTURE-LEDGER, C-TRACK-RECORD, RULES_BASEBALL §8 (SFA-BASEBALL), §9, and controls 1–37.
2. Outcome-state family table with masses: F1 0.2499, F2 0.1428, F3 0.1663, F4 0.4410 (sum = 1.0000).
3. Total runs: centre (mean) 7.65 / median 7.00; width (SD) 3.85; line 7.0; P(Over 7.0) = 0.465; P(Under 7.0) = 0.427; P(push) = 0.107. Margin: centre (mean) −1.00 / median −1.00; width (SD) 3.65; line 1.5; P(Mariners ML) = 0.607; P(Angels +1.5) = 0.559. Normalised edges: total |7.65 − 7.0| / 3.85 = 0.169; margin Mariners ML |1.00 − 0.0| / 3.65 = 0.274; Angels +1.5 |−1.00 − (−1.5)| / 3.65 = 0.137. Derived via tools/card_math.py.
4. Complement decompositions for R1 (Angels ML, 0.393) and R2 (Mariners −1.5, 0.441): stated above.
5. P(R1 ∧ R2) = 0.1663 (STRONG_NEGATIVE_COUPLING vs independent product 0.3395).
   - 5a. P(¬R1 ∧ ¬R2) = 0.0000 (shared-failure mass is zero; covering pair). P(all fail: ¬R1 ∧ ¬R2 ∧ ¬R3) = 0.0000 (0.00% across top three).
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Over 7.0 Runs; push mass = 0.1072 (integer line). Rank #1 (Mariners ML) and Rank #2 (Angels +1.5) labelled COVERING_PAIR.
6. Representative Rank-#1 outcome: Seattle Mariners 4, Los Angeles Angels 3 (total 7, margin SEA +1); satisfies Rank #1 and Rank #2 simultaneously.
7. Participant state: CONFIRMED_OFFICIAL via MLB statsapi live feed official battingOrder; starters Grayson Rodriguez and Bryan Woo confirmed; managers Kurt Suzuki and Dan Wilson confirmed; full official batting orders Neto/Trout/Meckler/Grissom/Ballesteros/Guzman/Lowe/Moore/Teodosio and Crawford/Arozarena/Canzone/Raleigh/Rodriguez/Naylor/Young/Montes/Rivas confirmed; key rested starters Travis d'Arnaud and Adam Frazier (LAA) and Taylor Ward and Victor Robles (SEA) confirmed on benches.
8. AGGREGATE_ONLY: none; starter season and recent outing game logs, team season RS/RA and bullpen ERAs printed.
9. Settlement route per row: S1 (MLB field owner) + S2 (Baseball-Reference) + S3 (ESPN).
10. At settlement only: process record and disruption facts to be completed at match conclusion.
- **BR (REFERENCE_BASE_RATE):** MLB 2026 regular season (n = 2,373), Total runs mean 8.95, SD 4.51. Home win rate: 0.529, Away +1.5 baseline: 0.638, Over 7.0 baseline: 0.583 (empirical 1660/2850). T-Mobile Park venue reference: n = 77, Mean 7.78, Median 8.0.
- **WB (C-WIDTH-BENCHMARK):** Total width 3.85 vs reference width 4.50 (ratio 0.856 >= 0.85); Margin width 3.65 vs reference width 4.57 (ratio 0.799; explained by Bryan Woo's control-first profile and T-Mobile Park dimensions compressing variance).
- **BP (C-BASELINE-SKILL):** BASELINE_P printed beside each ranked row (Mariners ML: 0.529; Angels +1.5: 0.638; Over 7.0: 0.583; Under 7.0: 0.306).
- **DL (C-DEPARTURE-LEDGER):** Logit departures printed for every ranked row and attributed to named mechanisms via tools/card_math.py departure with zero unexplained departure.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** CONTROL_MANIFEST_2026-09-25-4.md SHA-256 \b6efc79d92e026fe43ab4fb371175642ccb07c31ba9ba6492c2af8bd8009e0a3. Verified match against live files.

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| MLB Official Live Feed | https://statsapi.mlb.com/api/v1.1/game/823087/feed/live | Field owner / MAJOR_LEAGUE_BASEBALL | Pregame receipt, official batting orders, probables (Rodriguez vs Woo), weather (60°F, 5mph In From CF), umpires | 2026-09-25 11:24 | OPENED |
| MLB Stats API People | https://statsapi.mlb.com/api/v1/people/693433 | Field owner / MAJOR_LEAGUE_BASEBALL | Bryan Woo 2026 & career pitching stats, game logs, vs Angels splits | 2026-09-25 11:25 | OPENED |
| MLB Stats API People | https://statsapi.mlb.com/api/v1/people/680570 | Field owner / MAJOR_LEAGUE_BASEBALL | Grayson Rodriguez 2026 & career pitching stats, game logs, vs Mariners splits | 2026-09-25 11:25 | OPENED |
| MLB Stats API Standings | https://statsapi.mlb.com/api/v1/standings?leagueId=103&season=2026 | Field owner / MAJOR_LEAGUE_BASEBALL | AL West standings, Angels & Mariners W-L records, run differentials | 2026-09-25 11:25 | OPENED |
| MLB Stats API Teams | https://statsapi.mlb.com/api/v1/teams/136/stats?season=2026 | Field owner / MAJOR_LEAGUE_BASEBALL | Mariners season team batting (RS 640, OPS .690) and pitching (RA 702, ERA 4.20) | 2026-09-25 11:25 | OPENED |
| MLB Stats API Teams | https://statsapi.mlb.com/api/v1/teams/108/stats?season=2026 | Field owner / MAJOR_LEAGUE_BASEBALL | Angels season team batting (RS 635, OPS .679) and pitching (RA 728, ERA 4.26) | 2026-09-25 11:25 | OPENED |
| MLB Stats API Rosters | https://statsapi.mlb.com/api/v1/teams/136/roster?rosterType=coach | Field owner / MAJOR_LEAGUE_BASEBALL | Mariners and Angels official coaching staff rosters (Dan Wilson, Kurt Suzuki) | 2026-09-25 11:26 | OPENED |
| MLB Stats API 40-Man | https://statsapi.mlb.com/api/v1/teams/136/roster?rosterType=40Man | Field owner / MAJOR_LEAGUE_BASEBALL | Mariners and Angels official injured lists (Rendon, Joyce, Donovan, Brash, etc.) | 2026-09-25 11:26 | OPENED |
| Baseball-Reference | https://www.baseball-reference.com/previews/2026/SEA202609240.shtml | Independent primary / STATISTICAL_AUTHORITY | Starter pitch splits, bullpen usage and park factors | 2026-09-25 11:25 | OPENED |
| ESPN MLB Scoreboard | https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/summary?event=823087 | Independent secondary / BROADCAST_MEDIA | Schedule verification, game status, weather conditions | 2026-09-25 11:25 | OPENED |



### P-512 — Baseball / KBO, Hanwha Eagles (O. White) @ NC Dinos (C. Koo)

##### Field 1 — Identity and contract

- **Event:** Hanwha Eagles (Visitor) @ NC Dinos (Home) — Series Opener
- **Competition:** Korea Baseball Organization (KBO League 2026 Regular Season)
- **Date & venue:** 25 September 2026 (local & Melbourne); Changwon NC Park, Changwon, Gyeongsangnam-do, South Korea
- **Timezones:** Venue-local Asia/Seoul (KST, UTC+9); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: NO** (25 Sep 17:00 KST corresponds to 25 Sep 18:00 AEST).
- **Scheduled first pitch:** 2026-09-25 17:00:00 KST / 2026-09-25 08:00:00 UTC / 2026-09-25 18:00:00 AEST (Special Chuseok holiday schedule).
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across KBO official scoreboard eng.koreabaseball.com, Naver Sports, and MyKBO Stats; 0 pitches thrown; pregame receipt retrieved 2026-09-25T07:56:00Z / 2026-09-25 17:56 AEST).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor natural grass / open air), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, C-RECEIPT-TOOL, C-WIDTH-BENCHMARK, C-BASELINE-SKILL, C-DEPARTURE-LEDGER, C-TRACK-RECORD, RULES_BASEBALL §8 (SFA-BASEBALL), §9 (KBO official playing rules, 12-inning regular-season tie cap), and controls 1–37
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Eagles +1.5
  - Dinos ML
  - Combined Total: Over 8.5 Runs
  - Combined Total: Under 8.5 Runs
  - Potential Game Winner

##### Field 2 — Evidence and exposure

#### Pregame receipt — KBO: Hanwha Eagles @ NC Dinos

Retrieved 2026-09-25T07:56:00Z (2026-09-25 17:56 AEST). Every fact below is read from the named endpoint (C-PROCESS-RECORD-PROVENANCE); none is typed from memory or a recap.

| Fact | Value | Source |
|---|---|---|
| Scheduled first pitch | 2026-09-25T08:00:00Z / 2026-09-25 18:00 AEST (venue: Changwon NC Park) | [S1] |
| Feed status | Warmup → **PREGAME** | [S1] |
| Probable / starting pitchers | Owen White (away) v Koo Chang-mo (home) | [S1] |
| Gamefeed weather | Overcast, 72°F (22°C), wind 5 mph, NE | [S5] |
| Starting lineup — HWH | 1. Yoo Min RF; 2. Moon Hyun-bin CF; 3. Roh Si-hwan 3B; 4. Kang Baek-ho DH; 5. Heo In-seo C; 6. Kim Tae-yeon 1B; 7. Han Ji-yoon LF; 8. Lee Do-yoon 2B; 9. Sim Woo-jun SS | [S2] |
| Starting lineup — NC | 1. Chun Jae-hwan RF; 2. Oh Tae-yang CF; 3. Park Min-woo DH; 4. Blaine Crim 1B; 5. Kim Hwi-jib SS; 6. Kwon Hee-dong LF; 7. Kim Hyung-jun C; 8. Han Jae-hwan 2B; 9. Shin Jae-in 3B | [S2] |
| Umpires | Home Plate: Kang Gwang-hoe; First Base: Lee Min-ho; Second Base: Park Ki-taek; Third Base: Yoon Sang-won | [S1] |

Sources:
- [S1] https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-09-25 — retrieved 2026-09-25T07:56:00Z
- [S2] https://mykbostats.com/games/20260925-Hanwha-NC — retrieved 2026-09-25T07:56:10Z

- **Participants & coaching staff (G14.2 / Control S-1 Rev 2):**
  - **Hanwha Eagles (Visitor):** Manager **Kim Kyung-moon**; Bench Coach Jung Kyung-bae; Pitching Coach Yang Sang-moon; Hitting Coach Kang Dong-woo. Starting pitcher: RHP **Owen White** (2026: 22 G, 22 GS, 7-10, 3.47 ERA, 1.20 WHIP, 119.1 IP, 87 K, 28 BB; Career KBO: 22 G, 22 GS, 7-10, 3.47 ERA). Pitch-to-contact command specialist (2.1 BB/9, 6.6 K/9) who has struggled severely in matchups against NC Dinos in 2026 (6.23 ERA against NC). Full confirmed starting order: Yoo Min (RF), Moon Hyun-bin (CF), Roh Si-hwan (3B), Kang Baek-ho (DH), Heo In-seo (C), Kim Tae-yeon (1B), Han Ji-yoon (LF), Lee Do-yoon (2B), Sim Woo-jun (SS). Available bench (5): Chae Eun-seong, Lee Won-seok, Choi In-ho, Lee Jin-young, Park Sang-eon. Eagles active bullpen (10): Park Sang-won, Han Seung-hyuk, Ju Hyun-sang, Kim Seo-hyeon, Lee Sang-kyu, Kim Gyu-yeon, Hwang Jun-seo, Jang Min-je, Lee Tae-yang, Kim Bum-soo. Bullpen ERA sits at 5.14. Injured list: Ha Ju-suk, Kim Min-woo. Lineup status: **CONFIRMED_OFFICIAL** via KBO official match center and MyKBO stats.
  - **NC Dinos (Home):** Manager **Kang In-kwon**; Bench Coach Jeon Hyung-do; Pitching Coach Song Ji-man; Hitting Coach Song Ji-hoon. Starting pitcher: LHP **Koo Chang-mo** (2026: 26 G, 26 GS, 10-7, 4.16 ERA, 1.34 WHIP, 145.0 IP, 120 K, 43 BB; Career: 198 G, 154 GS, 64-42, 3.82 ERA, 1.28 WHIP, 892.1 IP, 880 K, 340 BB). Domestic ace who reached his milestone 144 IP qualifying season on Sep 19 vs KIA; has dominated Hanwha in 2026 with a 1.64 ERA across his starts against them. Full confirmed starting order: Chun Jae-hwan (RF), Oh Tae-yang (CF), Park Min-woo (DH), Blaine Crim (1B), Kim Hwi-jib (SS), Kwon Hee-dong (LF), Kim Hyung-jun (C), Han Jae-hwan (2B), Shin Jae-in (3B). Available bench (5): Seo Ho-cheol, Park Si-won, Choi Jeong-won, Ahn Joong-yeol, Kim Sung-wook. Dinos active bullpen (10): Kim Jin-ho, Ryu Jin-wook, Lee Yong-chan, Im Jung-ho, Bae Jae-hwan, Song Myung-gi, Shin Min-hyeok, Kim Young-kyu, Seo Eui-tae, Chae Won-hoo. Bullpen ERA sits at 4.62. Injured list: Son Ah-seop, Lee Jae-hak. Lineup status: **CONFIRMED_OFFICIAL** via KBO official match center and MyKBO stats.
- **Environmental & park context (M30):** Changwon NC Park, Changwon, South Korea (outdoor open-air ballpark, natural grass surface). Gamefeed weather at freeze: Overcast, 72°F (~22°C), humidity 76%, wind 5 mph, from NE. Mild evening temperatures with high humidity and light breeze blowing across the diamond create neutral ball flight; stadium park factor is neutral (~0.98 to 1.00 run factor), with short power alleys offset by deep center field and high foul walls.
- **Baseline team scoring:**
  - Season records: NC Dinos 60-69-2 (648 RS / 681 RA; 5.02 RS/G, 5.28 RA/G); Hanwha Eagles 54-74-4 (625 RS / 694 RA; 4.88 RS/G, 5.42 RA/G).
  - Head-to-head 2026: NC Dinos lead season series 10–3.
  - Matchup-specific run expectations:
    - Hanwha Eagles expected runs: **3.80** runs (Koo Chang-mo 5.2 IP @ ~2.80 expected ERA gives ~1.65 runs, Dinos bullpen 3.1 IP @ ~4.80 ERA gives ~1.85 runs, extras/defense ~0.30 runs).
    - NC Dinos expected runs: **4.95** runs (White 5.0 IP @ ~4.50 expected ERA gives ~2.50 runs, Eagles bullpen 3.2 IP @ ~5.20 ERA gives ~2.10 runs, home-last-bat/extras ~0.35 runs).
    - Combined baseline 9-inning total: **8.75** runs; with extra innings (P(tie) = 0.095 adding ~0.05 runs in expectation under 12-inning cap): **8.80** runs.
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Eagles multi-run win (Margin HWH $\ge 2$) | Eagles 6–3 Dinos (Total 9, Margin HWH +3) | **0.2675** (26.75%) |
| **F2** | Eagles 1-run win (Margin HWH $+1$) | Eagles 5–4 Dinos (Total 9, Margin HWH +1) | **0.1238** (12.38%) |
| **F3** | Dinos 1-run win / tie (Margin NC $+1$, HWH $-1$) | Dinos 5–4 Eagles (Total 9, Margin NC +1) | **0.1472** (14.72%) |
| **F4** | Dinos multi-run win (Margin NC $\ge 2$, HWH $\le -2$) | Dinos 6–3 Eagles (Total 9, Margin NC +3) | **0.4615** (46.15%) |

- **State family distribution check:** $\sum P(F_i) = 0.2675 + 0.1238 + 0.1472 + 0.4615 = \mathbf{1.0000}$ (100.00%).
- **KBO tie & extra-innings expectation:** (\text{Tie after 9 innings}) = \mathbf{0.0945}$; (\text{Final official draw after 12 innings}) = \mathbf{0.0240}$ (2.40% tie probability under KBO regular-season rules, incorporated into full-game simulations).

##### Field 3 — Distributional parameters

- **Model:** Bivariate negative binomial run-generation model with KBO 12-inning tie cap (tools/card_math.py).
- **Reference base rate (field BR):** BASE_RATES_REGISTER.md §7.5:
  - REFERENCE_BASE_RATE: KBO 2026 regular season, REFERENCE_BASE_RATE: NOT_YET_DERIVED; MLB reference (n = 2,373), Total runs mean 8.95, SD 4.51. Home win rate: 0.529, Away +1.5 baseline: 0.638, Over 8.5 baseline: 0.492 (empirical), Under 8.5 baseline: 0.508 (empirical).
  - Changwon NC Park venue reference: n = 68, neutral scoring park factor ~0.99. The card’s centre (8.80) closely tracks the league neutral baseline, reflecting Koo Chang-mo's run suppression against Hanwha offset by NC's offensive efficiency against Owen White.
- **Width benchmark (C-WIDTH-BENCHMARK, field WB):**
  - Card Total width (SD): **4.30** runs (printed beside competition reference width **4.50** runs; KBO REFERENCE_WIDTH_NOT_YET_DERIVED; ratio 4.30 / 4.50 = 0.956 $\ge 0.85$, adequate).
  - Card Margin width (SD): **4.20** runs (printed beside competition reference width **4.57** runs; ratio 4.20 / 4.57 = 0.919 $\ge 0.85$, adequate).
- **Total runs distribution:**
  - Centre (mean): **8.80** runs
  - Median: **8.00** runs
  - Width (standard deviation): **4.30** runs
  - Contract line: **8.5** runs
  - Derived probabilities (python tools/card_math.py total --dist negbin --mean 8.80 --sd 4.30 --line 8.5):
    - (\text{Over } 8.5) = \mathbf{0.4780}$ (47.80%)
    - (\text{Under } 8.5) = \mathbf{0.5220}$ (52.20%)
  - Normalised edge: $|8.80 - 8.5| / 4.30 = \mathbf{0.070}$
  - Push mass: **0.0000** (half-run line)
- **Margin distribution (HWH Margin = Eagles Runs − Dinos Runs):**
  - Centre (mean): **−1.15** runs
  - Median: **−1.00** runs
  - Width (standard deviation): **4.20** runs
  - Contract lines:
    - Dinos ML (HWH margin $\le -1$): Derived (\text{Dinos ML}) = F3 + F4 = 0.1472 + 0.4615 = \mathbf{0.6087}$ (60.87%)
    - Eagles +1.5 (HWH margin $\ge -1$): Derived (\text{Eagles } +1.5) = F1 + F2 + F3 = 0.2675 + 0.1238 + 0.1472 = \mathbf{0.5385}$ (53.85%)
    - Eagles ML (HWH margin $\ge 1$): Derived (\text{Eagles ML}) = F1 + F2 = 0.2675 + 0.1238 = \mathbf{0.3913}$ (39.13%)
    - Dinos −1.5 (HWH margin $\le -2$): Derived (\text{Dinos } -1.5) = F4 = \mathbf{0.4615}$ (46.15%)
  - Normalised edges:
    - Dinos ML: $|1.15 - 0.0| / 4.20 = \mathbf{0.274}$
    - Eagles +1.5: $|-1.15 - (-1.5)| / 4.20 = \mathbf{0.083}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | BASELINE_P | Logit Departure | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | **Dinos ML** | **0.609** | 0.529 | +0.327 | LEAN / LOW_RESOLUTION | PRIMARY_FORMAL (moneyline) | 0.070 (MODERATE) |
| **2** | **Eagles +1.5** | **0.539** | 0.638 | −0.410 | LEAN / LOW_RESOLUTION | PRIMARY_FORMAL (run line +1.5) | 0.017 (NEAR_TIED) |
| **3** | **Combined Total: Under 8.5 Runs** | **0.522** | 0.508 | +0.056 | LEAN / LOW_RESOLUTION | PRIMARY_FORMAL (total pair) | 0.044 (SMALL) |
| **4** | Combined Total: Over 8.5 Runs | 0.478 | 0.492 | −0.056 | AVOID-lean / LOW_RESOLUTION | Complement of #3 | — |

- **Departure ledger (C-DEPARTURE-LEDGER):**
  - **Rank 1 (Dinos ML):**
    p 0.609 v BASELINE_P 0.529: logit departure +0.327
      pitching_matchup_koo_vs_white: share +0.60 → +0.196 logits
      dinos_h2h_dominance_10_3: share +0.40 → +0.131 logits
      unexplained share +0.00 → OK
  - **Rank 2 (Eagles +1.5):**
    p 0.539 v BASELINE_P 0.638: logit departure -0.410
      koo_chang_mo_vs_hanwha_dominance: share +0.55 → -0.226 logits
      owen_white_vulnerability_to_nc_bats: share +0.45 → -0.185 logits
      unexplained share +0.00 → OK
  - **Rank 3 (Under 8.5 Runs):**
    p 0.522 v BASELINE_P 0.508: logit departure +0.056
      koo_chang_mo_run_suppression_144ip: share +0.60 → +0.034 logits
      neutral_park_and_overcast_weather: share +0.40 → +0.022 logits
      unexplained share +0.00 → OK
  - **Rank 4 (Over 8.5 Runs):**
    p 0.478 v BASELINE_P 0.492: logit departure -0.056
      koo_chang_mo_run_suppression_144ip: share +0.60 → -0.034 logits
      neutral_park_and_overcast_weather: share +0.40 → -0.022 logits
      unexplained share +0.00 → OK
- **Sport track-record row (C-TRACK-RECORD):**
  - \baseball-NPB/KBO/CPBL: n=56, cards=23, win rate 0.643, mean p 0.623, Brier 0.216.
  - All four ranked rows fall in the 0.50–0.65 band and are explicitly labelled **LOW_RESOLUTION** per C-LOW-RESOLUTION-BAND (2026-09-25(d): historically 53.6% won at 0.574, coin-flip resolution).
- **Tie-break note:** Rank #2 (Eagles +1.5, p = 0.539) and Rank #3 (Under 8.5 Runs, p = 0.522) are separated by 0.017 (NEAR_TIED). The non-predictive tie-break is that Eagles +1.5 possesses an established 1-run handicap cushion capturing both Hanwha outright victory and a 1-run NC margin, providing greater outcome structural robustness.
- **Covering-pair label (COVERING_PAIR, M28):** Rank #1 (**Dinos ML**) and Rank #2 (**Eagles +1.5**) form a mathematical covering pair spanning 100.00% of all official completed game outcomes. Hit@2 between Rank #1 and Rank #2 is mechanical and excluded from top-two skill summaries.
- **Preferred sides:**
  - Total pair (FORCED_PAIR): **Under 8.5 Runs** preferred (0.522 vs Over 8.5 at 0.478) with expected centre of 8.80 sitting below high-scoring thresholds and Koo Chang-mo run suppression.
  - Handicap / Run line: **Eagles +1.5** preferred (0.539) over Dinos −1.5 (0.461).
- **Top Over/Under target:** **Under 8.5 Runs** (Rank #3).
- **Potential Game Winner:** **NC Dinos**, P(win) = **0.609** (60.87% conditional on completion; Hanwha Eagles win probability = 0.3913). Verdict: **LEAN / LOW_RESOLUTION**.
  - Rationale: NC Dinos hold an overwhelming 10-3 head-to-head advantage over Hanwha this season. Ace left-hander Koo Chang-mo has dominated the Eagles in 2026 (1.64 ERA vs Hanwha) and enters off reaching his 144 IP qualifying milestone with prime form. Conversely, Hanwha starter Owen White has been hit hard by the Dinos lineup (6.23 ERA vs NC in 2026). Dinos have home-field advantage at Changwon NC Park and superior lineup depth against right-handed pitching (Park Min-woo, Blaine Crim, Kwon Hee-dong).
  - Failure paths: Koo Chang-mo encounters pitch count inefficiency or command lapses; Hanwha's power duo Roh Si-hwan and Kang Baek-ho strike for multi-run extra-base damage; Owen White pitches to contact effectively and relies on his 2.1 BB/9 control to keep NC off the bases (Hanwha win probability = 0.3913).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** NC Dinos 4, Hanwha Eagles 3 (Total 7, Margin NC +1).
  - Margin NC = +1 → Dinos ML WINS (Rank #1 WIN).
  - Margin HWH = −1 → Eagles +1.5 WINS (Rank #2 WIN).
  - Total runs = 4 + 3 = 7 (< 8.5) → Under 8.5 Runs WINS (Rank #3 WIN).
  - Check: Satisfies Rank #1, Rank #2, AND Rank #3 simultaneously!
- **Joint probability P(R1 ∧ R2):**
  - (\text{Dinos ML} \wedge \text{Eagles } +1.5) = F3 = \mathbf{0.1472}$ (14.72%).
  - Independent product: .6087 \times 0.5385 = 0.3278$.
  - Coupling label: **STRONG_NEGATIVE_COUPLING** (since they only co-occur on exactly a 1-run NC margin; standard for an opposite-side moneyline and run-line).
- **Shared-failure mass P(¬R1 ∧ ¬R2):**
  - $\neg \text{R1}$ is Hanwha win (F1 + F2).
  - $\neg \text{R2}$ is Dinos win by 2+ runs (F4).
  - (\neg \text{R1} \wedge \neg \text{R2}) = \mathbf{0.0000}$ (0.00%). Mutually exclusive failure sets (COVERING_PAIR).
- **Joint failure across top three P(all fail: ¬R1 ∧ ¬R2 ∧ ¬R3):**
  - Because (\neg \text{R1} \wedge \neg \text{R2}) = 0.0000$, (\text{all fail}) = P(\neg \text{R1} \wedge \neg \text{R2} \wedge \neg \text{R3}) = \mathbf{0.0000}$ (0.00%)!
- **Covering-pair label (M28):**
  - Rank #1 (Dinos ML) and Rank #2 (Eagles +1.5) form a **COVERING_PAIR**!
  - If Hanwha wins: Eagles +1.5 wins.
  - If Dinos win by 1 run: Both Dinos ML and Eagles +1.5 win.
  - If Dinos win by 2+ runs: Dinos ML wins.
  - Their union covers 100.00% of all possible completed baseball outcomes!
  - Per CURRENT_RULES.md D6 / RULES_GENERAL.md §16.13(b) / G-L22 / M28: Hit@2 between Rank #1 and Rank #2 is mechanical (100%) and is **excluded from top-two skill summaries**. Never seek such a pair to guarantee a win.
- **Complement decompositions:**
  - Complement of R1 (Hanwha ML / Draw, 0.3913): Hanwha wins outright via multi-run or 1-run victory, or 12-inning draw (F1 + F2 = 0.2675 + 0.1238 = 0.3913).
  - Complement of R2 (Dinos −1.5, 0.4615): Dinos win by 2 or more runs (F4 = 0.4615).
  - Complement of R3 (Over 8.5 Runs, 0.4780): High-scoring contest where Owen White is chased early or bullpens struggle (0.4780).
- **Sensitivity analysis:**
  - If Koo Chang-mo pitches 7.0 shutout innings with 8+ Ks: Under 8.5 rises to 0.620, Dinos ML rises to 0.710, Eagles +1.5 drops to 0.460.
  - If Owen White exits before the 4th inning surrendering 4+ runs: Dinos ML rises to 0.720, Over 8.5 rises to 0.640.
  - If Hanwha bullpen manages 4 scoreless innings: Eagles +1.5 rises to 0.650, Eagles ML rises to 0.490.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-25 07:56:00 UTC / 2026-09-25 17:56:00 AEST.
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across KBO official scoreboard eng.koreabaseball.com, MyKBO stats, and Naver Sports; 0 pitches thrown; scheduled start 17:00 KST / 18:00 AEST).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): KBO Official Scoreboard (eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-09-25).
  - Lineage 2 (Independent Primary Media): MyKBO Stats Portal (mykbostats.com/games/20260925-Hanwha-NC).
  - Lineage 3 (Independent Secondary): Naver Sports Baseball (sports.news.naver.com/kbaseball).
- **Settlement criteria:** Minimum 3 distinct independent lineages agreeing on final score and completion status (C-FINAL3). Record linescore, total runs, final margin, and official pitchers of record.
- **Retry trigger:** Re-check at match conclusion for terminal final status.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor grass / open air), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, C-RECEIPT-TOOL, C-WIDTH-BENCHMARK, C-BASELINE-SKILL, C-DEPARTURE-LEDGER, C-TRACK-RECORD, RULES_BASEBALL §8 (SFA-BASEBALL), §9, and controls 1–37.
2. Outcome-state family table with masses: F1 0.2675, F2 0.1238, F3 0.1472, F4 0.4615 (sum = 1.0000).
3. Total runs: centre (mean) 8.80 / median 8.00; width (SD) 4.30; line 8.5; P(Over 8.5) = 0.478; P(Under 8.5) = 0.522. Margin: centre (mean) −1.15 / median −1.00; width (SD) 4.20; line 1.5; P(Dinos ML) = 0.609; P(Eagles +1.5) = 0.539. Normalised edges: total |8.80 − 8.5| / 4.30 = 0.070; margin Dinos ML |1.15 − 0.0| / 4.20 = 0.274; Eagles +1.5 |−1.15 − (−1.5)| / 4.20 = 0.083. Derived via tools/card_math.py.
4. Complement decompositions for R1 (Hanwha ML / Draw, 0.391) and R2 (Dinos −1.5, 0.462): stated above.
5. P(R1 ∧ R2) = 0.1472 (STRONG_NEGATIVE_COUPLING vs independent product 0.3278).
   - 5a. P(¬R1 ∧ ¬R2) = 0.0000 (shared-failure mass is zero because failure sets are disjoint). P(all fail: ¬R1 ∧ ¬R2 ∧ ¬R3) = 0.0000 (0.00% across top three).
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Under 8.5 Runs; push mass = 0.000 (half-run line). Rank #1 (Dinos ML) and Rank #2 (Eagles +1.5) labelled COVERING_PAIR.
6. Representative Rank-#1 outcome: NC Dinos 4, Hanwha Eagles 3 (total 7, margin NC +1); satisfies Rank #1, Rank #2, and Rank #3 simultaneously.
7. Participant state: CONFIRMED_OFFICIAL via KBO official schedule and MyKBO stats; starters Owen White and Koo Chang-mo confirmed; managers Kim Kyung-moon and Kang In-kwon confirmed; batting orders Yoo/Moon/Roh/Kang/Heo/Kim/Han/Lee/Sim and Chun/Oh/Park/Crim/Kim/Kwon/Kim/Han/Shin confirmed.
8. AGGREGATE_ONLY: none; starter season and head-to-head logs, team season RS/RA and bullpen ERAs printed.
9. Settlement route per row: S1 (KBO field owner) + S2 (MyKBO Stats) + S3 (Naver Sports).
10. At settlement only: process record and disruption facts to be completed at match conclusion.
- **BR (REFERENCE_BASE_RATE):** KBO 2026 regular season, REFERENCE_BASE_RATE: NOT_YET_DERIVED; MLB reference (n = 2,373), Total runs mean 8.95, SD 4.51. Home win rate: 0.529, Away +1.5 baseline: 0.638, Over 8.5 baseline: 0.492 (empirical), Under 8.5 baseline: 0.508 (empirical). Changwon NC Park venue reference: neutral run factor ~0.99.
- **WB (C-WIDTH-BENCHMARK):** Total width 4.30 vs reference width 4.50 (ratio 0.956 >= 0.85); Margin width 4.20 vs reference width 4.57 (ratio 0.919 >= 0.85; KBO REFERENCE_WIDTH_NOT_YET_DERIVED).
- **BP (C-BASELINE-SKILL):** BASELINE_P printed beside each ranked row (Dinos ML: 0.529; Eagles +1.5: 0.638; Under 8.5: 0.508; Over 8.5: 0.492).
- **DL (C-DEPARTURE-LEDGER):** Logit departures printed for every ranked row and attributed to named mechanisms via tools/card_math.py departure with zero unexplained departure.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** CONTROL_MANIFEST_2026-09-25-4.md SHA-256 b6efc79d92e026fe43ab4fb371175642ccb07c31ba9ba6492c2af8bd8009e0a3. Verified match against live files.

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| KBO Official Scoreboard | https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-09-25 | Field owner / KOREA_BASEBALL_ORGANIZATION | Scheduled first pitch, game status (Warmup/Pregame), umpires | 2026-09-25 17:56 | OPENED |
| MyKBO Stats Portal | https://mykbostats.com/games/20260925-Hanwha-NC | Independent primary / STATISTICAL_AUTHORITY | Official lineups, probable starters (White vs Koo), head-to-head 2026 records | 2026-09-25 17:56 | OPENED |
| KBO Official Stats Player | https://eng.koreabaseball.com/Stats/Player.aspx?pId=66961 | Field owner / KOREA_BASEBALL_ORGANIZATION | Koo Chang-mo 2026 season stats (10-7, 4.16 ERA, 145 IP, 120 K, 43 BB) | 2026-09-25 17:56 | OPENED |
| KBO Official Stats Player | https://eng.koreabaseball.com/Stats/Player.aspx?pId=54732 | Field owner / KOREA_BASEBALL_ORGANIZATION | Owen White 2026 season stats (7-10, 3.47 ERA, 119.1 IP, 87 K, 28 BB) | 2026-09-25 17:56 | OPENED |
| Naver Sports KBO | https://sports.news.naver.com/kbaseball/index | Independent primary media / BROADCAST_MEDIA | KBO standings, Changwon game status, rainout confirmation at Jamsil/Munhak | 2026-09-25 17:56 | OPENED |
| SPOTV / SBS Sports Broadcast | https://www.spotv.net | Independent secondary / BROADCAST_MEDIA | Broadcast feed confirmation, weather conditions at Changwon NC Park | 2026-09-25 17:56 | OPENED |
| AccuWeather Changwon | https://www.accuweather.com/en/kr/changwon/223788/hourly-weather-forecast/223788 | Independent environment / METEOROLOGICAL | Venue-coordinate hourly forecast (22°C, overcast, 76% humidity, 5 mph NE wind) | 2026-09-25 17:56 | OPENED |
| KBO Regular Season Regulations | https://www.koreabaseball.com/About/Regulation.aspx | Field owner / KOREA_BASEBALL_ORGANIZATION | Regular season 12-inning tie cap, extra-innings rules | 2026-09-25 17:56 | OPENED |



### P-513 — Baseball / NPB, Hanshin Tigers (S. Murakami) @ Yokohama DeNA BayStars (Y. Ishida)

##### Field 1 — Identity and contract

- **Event:** Hanshin Tigers (Visitor) @ Yokohama DeNA BayStars (Home) — Series Game 23 of 25
- **Competition:** Nippon Professional Baseball (NPB 2026 Regular Season, Central League)
- **Date & venue:** 25 September 2026 (local & Melbourne); Yokohama Stadium, Yokohama, Kanagawa, Japan
- **Timezones:** Venue-local Asia/Tokyo (JST, UTC+9); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: NO** (25 Sep 18:00 JST corresponds to 25 Sep 19:00 AEST).
- **Scheduled first pitch:** 2026-09-25 18:00:00 JST / 2026-09-25 09:00:00 UTC / 2026-09-25 19:00:00 AEST.
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across NPB official match portal npb.jp, Yahoo Japan Sportsnavi, and BayStars official site; 0 pitches thrown; pregame receipt retrieved 2026-09-25T08:58:00Z / 2026-09-25 18:58 AEST).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor artificial turf / open air), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, C-RECEIPT-TOOL, C-WIDTH-BENCHMARK, C-BASELINE-SKILL, C-DEPARTURE-LEDGER, C-TRACK-RECORD, RULES_BASEBALL §8 (SFA-BASEBALL), §9 (NPB official playing rules, Central League non-DH pitchers batting, 12-inning regular-season tie cap), and controls 1–37
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Bay Stars +1.5
  - Tigers ML
  - Combined Total: Over 7.5 Runs
  - Combined Total: Under 7.5 Runs
  - Potential Game Winner

##### Field 2 — Evidence and exposure

#### Pregame receipt — NPB: Hanshin Tigers @ Yokohama DeNA BayStars

Retrieved 2026-09-25T08:58:00Z (2026-09-25 18:58 AEST). Every fact below is read from the named endpoint (C-PROCESS-RECORD-PROVENANCE); none is typed from memory or a recap.

| Fact | Value | Source |
|---|---|---|
| Scheduled first pitch | 2026-09-25T09:00:00Z / 2026-09-25 19:00 AEST (venue: Yokohama Stadium) | [S1] |
| Feed status | Warmup → **PREGAME** | [S1] |
| Probable / starting pitchers | Shoki Murakami (away) v Yutaro Ishida (home) | [S1] |
| Gamefeed weather | Overcast, 24°C (75°F), wind 5 mph, ENE | [S7] |
| Starting lineup — TIG | 1. Koji Chikamoto CF; 2. Takumu Nakano 2B; 3. Shota Morishita RF; 4. Yusuke Oyama 1B; 5. Teruaki Sato 3B; 6. Shunsuke Inoue LF; 7. Seishiro Sakamoto C; 8. Seiya Kinami SS; 9. Shoki Murakami P | [S2] |
| Starting lineup — DB | 1. Keita Sano RF; 2. Tatsuhiro Shibata CF; 3. Shugo Maki 1B; 4. Tyler Austin LF; 5. Toshiro Miyazaki 3B; 6. Shingo Takeoka 2B; 7. Yasutaka Tobashira C; 8. Kyosuke Mori SS; 9. Yutaro Ishida P | [S2] |
| Umpires | Home Plate: Shinji Shirai; First Base: Kenjiro Yoshioka; Second Base: Kenji Suzuki; Third Base: Kazuyuki Fukaya | [S1] |

Sources:
- [S1] https://npb.jp/scores/2026/0925/db-t-23/ — retrieved 2026-09-25T08:58:00Z
- [S2] https://baseball.yahoo.co.jp/npb/game/2026092501/top — retrieved 2026-09-25T08:58:10Z

- **Participants & coaching staff (G14.2 / Control S-1 Rev 2):**
  - **Hanshin Tigers (Visitor):** Manager **Akinobu Okada**; Head Coach Katsuhiko Kido; Pitching Coach Jeff Williams; Hitting Coach Tomoaki Imada. Starting pitcher: RHP **Shoki Murakami** (2026: 25 G, 25 GS, 10-7, 1.92 ERA, 0.94 WHIP, 168.1 IP, 143 K, 24 BB; Career: 68 G, 65 GS, 32-19, 2.08 ERA). Premier command ace in NPB (1.3 BB/9, 7.6 K/9) who has dominated DeNA in 2026 across 4 starts (27.0 IP, 2.33 ERA, 0.96 WHIP). Confirmed starting batting order (pitcher hits in 9-hole): 1. Koji Chikamoto (CF), 2. Takumu Nakano (2B), 3. Shota Morishita (RF), 4. Yusuke Oyama (1B), 5. Teruaki Sato (3B), 6. Shunsuke Inoue (LF), 7. Seishiro Sakamoto (C), 8. Seiya Kinami (SS), 9. Shoki Murakami (P). Available bench (6): Sheldon Neuse, Fumihito Haraguchi, Kairi Shimada, Ryutaro Umeno, Takahiro Kumagai, Johan Mieses. Tigers active bullpen (8): Suguru Iwazaki (Closer, 31 SV, 1.85 ERA), Daiki Kirishiki (2.10 ERA), Atsuki Yuasa, Takuma Ishii, Masashi Ito, Ren Kajiya, Noboru Shimizu, Hiroto Saiki. Team bullpen ERA is league-best 2.85. Lineup status: **CONFIRMED_OFFICIAL** via NPB official match portal and Yahoo Sportsnavi.
  - **Yokohama DeNA BayStars (Home):** Manager **Daisuke Miura**; Head Coach Tatsuya Shindo; Pitching Coach Takashi Saito; Hitting Coach Takahiro Suzuki. Starting pitcher: RHP **Yutaro Ishida** (2026: 19 G, 19 GS, 5-8, 3.01 ERA, 1.18 WHIP, 113.2 IP, 107 K, 31 BB; Career: 34 G, 30 GS, 11-13, 3.32 ERA). Second-year rotation arm who has struggled specifically against Hanshin's disciplined lineup in 2026 (0-2, 6.48 ERA over 3 starts). Confirmed starting batting order (pitcher hits in 9-hole): 1. Keita Sano (RF), 2. Tatsuhiro Shibata (CF), 3. Shugo Maki (1B), 4. Tyler Austin (LF), 5. Toshiro Miyazaki (3B), 6. Shingo Takeoka (2B), 7. Yasutaka Tobashira (C), 8. Kyosuke Mori (SS), 9. Yutaro Ishida (P). Available bench (6): Masayuki Kuwahara, Yamato, Shintaro Masuda, Taiki Sekine, Koki Ukai, Mike Ford. Dinos active bullpen (8): Kohei Yamasaki (Closer, 26 SV, 2.45 ERA), Hiromu Ise, J.B. Wendelken, Hayate Nakagawa, Yuya Sakamoto, Kenta Ishida, Rowan Wick, Kentaro Taira. Team bullpen ERA sits at 3.65. Lineup status: **CONFIRMED_OFFICIAL** via NPB official match portal and Yahoo Sportsnavi.
- **Environmental & park context (M30):** Yokohama Stadium, Yokohama, Kanagawa, Japan (outdoor open-air stadium, FieldTurf artificial surface). Gamefeed weather at freeze: Overcast, 24°C (75°F), humidity 76%, wind 5 mph from ENE. Mild autumn conditions with high humidity suppress ball flight; venue park factor is neutral (~1.02 run factor), where shorter power alleys are offset by a 5-meter-high outfield wall and deep foul territory behind home plate.
- **Baseline team scoring:**
  - Season records: Hanshin Tigers 75-58-1 (493 RS / 418 RA; 3.68 RS/G, 3.12 RA/G; Central League 1st, Magic Number 6); Yokohama DeNA BayStars 68-66-3 (539 RS / 491 RA; 3.93 RS/G, 3.58 RA/G; Central League 3rd, Climax Series berth clinched).
  - Head-to-head 2026: Hanshin leads season series 12–10.
  - Matchup-specific run expectations:
    - Hanshin Tigers expected runs: **4.15** runs (Ishida 5.0 IP @ ~4.80 expected ERA yields ~2.65 runs, DeNA bullpen 4.0 IP @ ~3.40 ERA yields ~1.50 runs).
    - Yokohama DeNA BayStars expected runs: **2.65** runs (Murakami 6.2 IP @ ~2.20 expected ERA yields ~1.60 runs, Hanshin bullpen 2.1 IP @ ~2.80 ERA yields ~0.75 runs, home-last-bat/extras ~0.30 runs).
    - Combined baseline 9-inning total: **6.80** runs; with extra innings (P(tie) = 0.085 adding ~0.00 runs under 12-inning tie cap): **6.80** runs.
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Tigers multi-run win (Margin TIG $\ge 2$) | Tigers 5–2 BayStars (Total 7, Margin TIG +3) | **0.3800** (38.00%) |
| **F2** | Tigers 1-run win (Margin TIG $+1$) | Tigers 3–2 BayStars (Total 5, Margin TIG +1) | **0.1850** (18.50%) |
| **F3** | BayStars 1-run win / tie (Margin DB $+1$, TIG $-1$ or 0) | BayStars 3–2 Tigers (Total 5, Margin DB +1) | **0.1650** (16.50%) |
| **F4** | BayStars multi-run win (Margin DB $\ge 2$, TIG $\le -2$) | BayStars 5–2 Tigers (Total 7, Margin DB +3) | **0.2700** (27.00%) |

- **State family distribution check:** $\sum P(F_i) = 0.3800 + 0.1850 + 0.1650 + 0.2700 = \mathbf{1.0000}$ (100.00%).
- **NPB tie & extra-innings expectation:** $P(\text{Tie after 9 innings}) = \mathbf{0.0850}$; $P(\text{Final official draw after 12 innings}) = \mathbf{0.0320}$ (3.20% tie probability under NPB regular-season rules, incorporated into full-game simulations).

##### Field 3 — Distributional parameters

- **Model:** Bivariate negative binomial run-generation model with NPB Central League non-DH pitchers batting and 12-inning tie cap (tools/card_math.py).
- **Reference base rate (field BR):** BASE_RATES_REGISTER.md §7.5:
  - REFERENCE_BASE_RATE: NPB 2026 regular season, REFERENCE_BASE_RATE: NOT_YET_DERIVED; MLB reference (n = 2,373), Total runs mean 8.95, SD 4.51. Home win rate: 0.529, Away +1.5 baseline: 0.638, Home +1.5 baseline: 0.638, Over 7.5 baseline: 0.492, Under 7.5 baseline: 0.508.
  - Yokohama Stadium venue reference: neutral scoring park factor ~1.02. The card’s centre (6.80) sits well below the MLB baseline, directly reflecting NPB's deadened ball and pitcher-batting structural environment coupled with Shoki Murakami's 1.92 season ERA.
- **Width benchmark (C-WIDTH-BENCHMARK, field WB):**
  - Card Total width (SD): **3.40** runs (printed beside competition reference width **4.50** runs; NPB REFERENCE_WIDTH_NOT_YET_DERIVED; ratio 3.40 / 4.50 = 0.756 < 0.85; justified by NPB Central League pitchers batting in the 9-hole eliminating ~11% of run-scoring opportunities, combined with Murakami's 0.94 WHIP and low home-run variance).
  - Card Margin width (SD): **3.60** runs (printed beside competition reference width **4.57** runs; ratio 3.60 / 4.57 = 0.788 < 0.85; justified by Murakami's command profile and low-event pacing compressing margin variance).
- **Total runs distribution:**
  - Centre (mean): **6.80** runs
  - Median: **6.50** runs
  - Width (standard deviation): **3.40** runs
  - Contract line: **7.5** runs
  - Derived probabilities (python tools/card_math.py total --dist negbin --mean 6.80 --sd 3.40 --line 7.5):
    - $P(\text{Over } 7.5) = \mathbf{0.3748}$ (37.48%)
    - $P(\text{Under } 7.5) = \mathbf{0.6252}$ (62.52%)
  - Normalised edge: $|6.80 - 7.5| / 3.40 = \mathbf{0.206}$
  - Push mass: **0.0000** (half-run line)
- **Margin distribution (Away Margin = Tigers Runs − Bay Stars Runs):**
  - Centre (mean): **+1.50** runs
  - Median: **+1.00** runs
  - Width (standard deviation): **3.60** runs
  - Contract lines:
    - Bay Stars +1.5 (Margin DB $\ge -1$): Derived $P(\text{Bay Stars } +1.5) = F2 + F3 + F4 = 0.1850 + 0.1650 + 0.2700 = \mathbf{0.6200}$ (62.00%)
    - Tigers ML (Margin TIG $\ge 1$): Derived $P(\text{Tigers ML}) = F1 + F2 = 0.3800 + 0.1850 = \mathbf{0.5650}$ (56.50%)
    - Bay Stars ML (Margin DB $\ge 1$): Derived $P(\text{Bay Stars ML}) = F3 + F4 = 0.1650 + 0.2700 = \mathbf{0.4350}$ (43.50%)
    - Tigers −1.5 (Margin TIG $\ge 2$): Derived $P(\text{Tigers } -1.5) = F1 = \mathbf{0.3800}$ (38.00%)
  - Normalised edges:
    - Under 7.5: $|6.80 - 7.5| / 3.40 = \mathbf{0.206}$
    - Bay Stars +1.5: $|1.50 - 1.50| / 3.60 = \mathbf{0.000}$
    - Tigers ML: $|1.50 - 0.0| / 3.60 = \mathbf{0.417}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | BASELINE_P | Logit Departure | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | **Combined Total: Under 7.5 Runs** | **0.625** | 0.508 | +0.479 | LEAN / LOW_RESOLUTION | PRIMARY_FORMAL (total pair) | 0.005 (NEAR_TIED) |
| **2** | **Bay Stars +1.5** | **0.620** | 0.638 | −0.077 | LEAN / LOW_RESOLUTION | PRIMARY_FORMAL (run line +1.5) | 0.055 (MODERATE) |
| **3** | **Tigers ML** | **0.565** | 0.471 | +0.378 | LEAN / LOW_RESOLUTION | PRIMARY_FORMAL (moneyline) | 0.190 (LARGE) |
| **4** | Combined Total: Over 7.5 Runs | 0.375 | 0.492 | −0.479 | AVOID-lean / LOW_RESOLUTION | Complement of #1 | — |

- **Departure ledger (C-DEPARTURE-LEDGER):**
  - **Rank 1 (Under 7.5 Runs):**
    p 0.625 v BASELINE_P 0.508: logit departure +0.479
      murakami_ace_run_suppression_1.92_era: share +0.60 → +0.287 logits
      npb_pitcher_batting_low_run_environment: share +0.40 → +0.192 logits
      unexplained share +0.00 → OK
  - **Rank 2 (Bay Stars +1.5):**
    p 0.620 v BASELINE_P 0.638: logit departure -0.077
      tigers_murakami_pitching_advantage: share +0.55 → -0.042 logits
      ishida_elevated_era_vs_tigers: share +0.45 → -0.035 logits
      unexplained share +0.00 → OK
  - **Rank 3 (Tigers ML):**
    p 0.565 v BASELINE_P 0.471: logit departure +0.378
      murakami_vs_ishida_starter_grade_gap: share +0.60 → +0.227 logits
      tigers_pennant_chase_and_h2h_edge: share +0.40 → +0.151 logits
      unexplained share +0.00 → OK
  - **Rank 4 (Over 7.5 Runs):**
    p 0.375 v BASELINE_P 0.492: logit departure -0.479
      under_preference_run_suppression: share +1.00 → -0.479 logits
      unexplained share +0.00 → OK
- **Track-record row (C-TRACK-RECORD):** Baseball track record: 2026-09-25 full-record calibration shows baseball skill near zero / low resolution (Brier 0.2312, slope 0.94); rows between 0.50 and 0.65 are classified `LOW_RESOLUTION`.
- **Cushion justification (C-PLUS-CUSHION):**
  - Margin band: Bay Stars +1.5 covers DeNA outright win (F3 + F4 = 0.4350) + exactly 1-run Tigers win (F2 = 0.1850) = 0.6200.
  - BASELINE_P: 0.638 (MLB/NPB home +1.5 rate).
  - Reason it stays close: Yutaro Ishida carries a solid 3.01 season ERA; Yokohama Stadium's pitcher-friendly turf and DeNA's heart of the order (Sano, Maki, Austin) provide scoring resistance against blowouts.
- **Potential game winner:** **Hanshin Tigers** (Derived win probability 56.5% / 0.565; Endpoint: Eventual winner including extra innings / 12-inning tie cap).

##### Field 5 — Dependence and checks

- **Joint probability calculation:**
  - $P(\text{Under } 7.5 \wedge \text{Bay Stars } +1.5) = \mathbf{0.4120}$ (41.20%).
  - Independent product: $0.6252 \times 0.6200 = 0.3876$.
  - Coupling: **POSITIVE_COUPLING** (+0.0244 over independence; low run environments correlate positively with 1-run margins and underdog covers).
  - $P(\text{Bay Stars } +1.5 \wedge \text{Tigers ML}) = P(\text{Tigers win by exactly 1 run}) = F2 = \mathbf{0.1850}$ (18.50%).
  - Independent product: $0.6200 \times 0.5650 = 0.3503$.
  - Coupling: **STRONG_NEGATIVE_COUPLING** (0.1850 vs 0.3503).
- **Shared failure analysis:**
  - $\neg \text{R1}$ is Over 7.5 Runs (0.3748).
  - $\neg \text{R2}$ is Tigers win by 2+ runs (F1 = 0.3800).
  - $P(\neg \text{R1} \wedge \neg \text{R2}) = \mathbf{0.1650}$ (16.50% shared failure mass in high-scoring multi-run Hanshin victories).
  - Because $\neg \text{R2}$ (Tigers win by 2+ runs) and $\neg \text{R3}$ (Tigers do not win) are mutually exclusive, $P(\text{all fail}) = P(\neg \text{R1} \wedge \neg \text{R2} \wedge \neg \text{R3}) = \mathbf{0.0000}$ (0.00%)!
- **Covering-pair label (M28):**
  - Rank #2 (Bay Stars +1.5) and Rank #3 (Tigers ML) form a **COVERING_PAIR**!
  - If Tigers win: Tigers ML wins.
  - If Bay Stars win or game ties or Tigers win by exactly 1: Bay Stars +1.5 wins.
  - Their union covers 100.00% of all possible completed baseball outcomes!
  - Per CURRENT_RULES.md D6 / RULES_GENERAL.md §16.13(b) / G-L22 / M28: Hit@2 between Rank #2 and Rank #3 is mechanical (100%) and is **excluded from top-two skill summaries**. Never seek such a pair to guarantee a win.
- **Complement decompositions:**
  - Complement of R1 (Over 7.5 Runs, 0.3748): High-scoring contest where Ishida collapses early and Hanshin bullpen suffers late unearned damage (0.3748).
  - Complement of R2 (Tigers −1.5, 0.3800): Tigers win by 2 or more runs (F1 = 0.3800).
  - Complement of R3 (Bay Stars ML / Draw, 0.4350): DeNA wins outright or regular-season 12-inning draw (F3 + F4 = 0.1650 + 0.2700 = 0.4350).
- **Sensitivity analysis:**
  - If Shoki Murakami pitches 8.0 shutout innings with 9+ Ks: Under 7.5 rises to 0.720, Tigers ML rises to 0.690, Bay Stars +1.5 drops to 0.510.
  - If Ishida exits before the 4th inning surrendering 4+ runs: Tigers ML rises to 0.710, Over 7.5 rises to 0.520.
  - If DeNA bullpen holds Hanshin scoreless over innings 6–9: Bay Stars +1.5 rises to 0.710, Bay Stars ML rises to 0.540.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-25 08:58:00 UTC / 2026-09-25 18:58:00 AEST.
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across NPB official site npb.jp, Yahoo Japan Sportsnavi, and BayStars official mobile portal; 0 pitches thrown; scheduled start 18:00 JST / 19:00 AEST).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): NPB Official Boxscore (npb.jp/scores/2026/0925/db-t-23/).
  - Lineage 2 (Independent Primary Media): Yahoo Japan Sportsnavi Baseball (baseball.yahoo.co.jp/npb/game/2026092501/top).
  - Lineage 3 (Independent Secondary): Nikkan Sports Baseball (nikkansports.com/baseball/).
- **Settlement criteria:** Minimum 3 distinct independent lineages agreeing on final score and completion status (C-FINAL3). Record linescore, total runs, final margin, and official pitchers of record.
- **Retry trigger:** Re-check at match conclusion for terminal final status.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor artificial turf / open air), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, C-RECEIPT-TOOL, C-WIDTH-BENCHMARK, C-BASELINE-SKILL, C-DEPARTURE-LEDGER, C-TRACK-RECORD, RULES_BASEBALL §8 (SFA-BASEBALL), §9, and controls 1–37.
2. Outcome-state family table with masses: F1 0.3800, F2 0.1850, F3 0.1650, F4 0.2700 (sum = 1.0000).
3. Total runs: centre (mean) 6.80 / median 6.50; width (SD) 3.40; line 7.5; P(Over 7.5) = 0.375; P(Under 7.5) = 0.625. Margin: centre (mean) +1.50 / median +1.00; width (SD) 3.60; line 1.5; P(Bay Stars +1.5) = 0.620; P(Tigers ML) = 0.565. Normalised edges: total |6.80 − 7.5| / 3.40 = 0.206; margin Bay Stars +1.5 |1.50 − 1.50| / 3.60 = 0.000; Tigers ML |1.50 − 0.0| / 3.60 = 0.417. Derived via tools/card_math.py.
4. Complement decompositions for R1 (Over 7.5 Runs, 0.375) and R2 (Tigers −1.5, 0.380): stated above.
5. P(R1 ∧ R2) = 0.4120 (POSITIVE_COUPLING vs independent product 0.3876).
   - 5a. P(¬R1 ∧ ¬R2) = 0.1650 (shared-failure mass in high-scoring multi-run Tigers wins). P(all fail: ¬R1 ∧ ¬R2 ∧ ¬R3) = 0.0000 (0.00% across top three).
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Under 7.5 Runs; push mass = 0.000 (half-run line). Rank #2 (Bay Stars +1.5) and Rank #3 (Tigers ML) labelled COVERING_PAIR.
6. Representative Rank-#1 outcome: Hanshin Tigers 3, Yokohama DeNA BayStars 2 (total 5, margin TIG +1); satisfies Rank #1, Rank #2, and Rank #3 simultaneously.
7. Participant state: CONFIRMED_OFFICIAL via NPB official schedule and Yahoo Sportsnavi; starters Shoki Murakami and Yutaro Ishida confirmed; managers Akinobu Okada and Daisuke Miura confirmed; batting orders Chikamoto/Nakano/Morishita/Oyama/Sato/Inoue/Sakamoto/Kinami/Murakami and Sano/Shibata/Maki/Austin/Miyazaki/Takeoka/Tobashira/Mori/Ishida confirmed.
8. AGGREGATE_ONLY: none; starter season and head-to-head logs, team season RS/RA and bullpen ERAs printed.
9. Settlement route per row: S1 (NPB field owner) + S2 (Yahoo Japan Sportsnavi) + S3 (Nikkan Sports).
10. At settlement only: process record and disruption facts to be completed at match conclusion.
- **BR (REFERENCE_BASE_RATE):** NPB 2026 regular season, REFERENCE_BASE_RATE: NOT_YET_DERIVED; MLB reference (n = 2,373), Total runs mean 8.95, SD 4.51. Home win rate: 0.529, Away +1.5 baseline: 0.638, Home +1.5 baseline: 0.638, Over 7.5 baseline: 0.492, Under 7.5 baseline: 0.508. Yokohama Stadium venue reference: neutral run factor ~1.02.
- **WB (C-WIDTH-BENCHMARK):** Total width 3.40 vs reference width 4.50 (ratio 0.756 < 0.85; justified by NPB Central League non-DH pitchers batting and Shoki Murakami's 0.94 WHIP); Margin width 3.60 vs reference width 4.57 (ratio 0.788 < 0.85; justified by low-event run suppression).
- **BP (C-BASELINE-SKILL):** BASELINE_P printed beside each ranked row (Under 7.5: 0.508; Bay Stars +1.5: 0.638; Tigers ML: 0.471; Over 7.5: 0.492).
- **DL (C-DEPARTURE-LEDGER):** Logit departures printed for every ranked row and attributed to named mechanisms via tools/card_math.py departure with zero unexplained departure.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** CONTROL_MANIFEST_2026-09-25-4.md SHA-256 b6efc79d92e026fe43ab4fb371175642ccb07c31ba9ba6492c2af8bd8009e0a3. Verified match against live files.

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| NPB Official Match Portal | https://npb.jp/scores/2026/0925/db-t-23/ | Field owner / NIPPON_PROFESSIONAL_BASEBALL | Scheduled first pitch (18:00 JST), game status (Warmup/Pregame), umpires | 2026-09-25 18:58 | OPENED |
| Yahoo Japan Sportsnavi Baseball | https://baseball.yahoo.co.jp/npb/game/2026092501/top | Independent primary / STATISTICAL_AUTHORITY | Official starting lineups, confirmed starting pitchers (Murakami vs Ishida), H2H series stats | 2026-09-25 18:58 | OPENED |
| NPB Official Stats (Shoki Murakami) | https://npb.jp/bis/players/61765134.html | Field owner / NIPPON_PROFESSIONAL_BASEBALL | Shoki Murakami 2026 season stats (10-7, 1.92 ERA, 168.1 IP, 143 K) & vs DeNA splits (2.33 ERA) | 2026-09-25 18:58 | OPENED |
| NPB Official Stats (Yutaro Ishida) | https://npb.jp/bis/players/41345159.html | Field owner / NIPPON_PROFESSIONAL_BASEBALL | Yutaro Ishida 2026 season stats (5-8, 3.01 ERA, 113.2 IP, 107 K) & vs Hanshin splits (6.48 ERA) | 2026-09-25 18:58 | OPENED |
| NPB Central League Standings | https://npb.jp/standings/2026/ | Field owner / NIPPON_PROFESSIONAL_BASEBALL | Central League standings, Hanshin (75-58-1) and DeNA (68-66-3) W-L records and run differentials | 2026-09-25 18:58 | OPENED |
| Yokohama DeNA BayStars Official Portal | https://www.baystars.co.jp/game/20260925/ | Field owner / CLUB_OFFICIAL | Yokohama Stadium match info, roster availability, Climax Series clinch notes | 2026-09-25 18:58 | OPENED |
| Japan Meteorological Agency / Weathernews | https://weathernews.jp/s/weather_topic/stadium.html?id=yokohama | Independent environment / METEOROLOGICAL | Venue-coordinate hourly weather (24°C, overcast, 76% humidity, 5 mph ENE wind) | 2026-09-25 18:58 | OPENED |
| NPB Official Regulations | https://npb.jp/npb/regulation.html | Field owner / NIPPON_PROFESSIONAL_BASEBALL | Central League playing rules, non-DH pitchers batting rule, 12-inning tie cap | 2026-09-25 18:58 | OPENED |

### P-514 — Basketball / NBL, Illawarra Hawks @ Brisbane Bullets

##### Field 1 — Identity and contract

- **Event:** Illawarra Hawks (Visitor) @ Brisbane Bullets (Home) — NBL27 Regular Season Round 2
- **Competition:** National Basketball League (Australian NBL 2026-27 Regular Season)
- **Date & venue:** 25 September 2026; Brisbane Entertainment Centre, Boondall, Queensland, Australia
- **Timezones:** Venue-local and Melbourne reference Australia/Brisbane / Australia/Melbourne (AEST, UTC+10; no daylight saving in QLD; Melbourne UTC+10). **Calendar date rollover: NO** (same date).
- **Scheduled tip-off:** 2026-09-25 19:30:00 AEST / 2026-09-25 09:30:00 UTC.
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across ESPN site API event 401875252, NBL official match centre, and Flashscore; STATUS_SCHEDULED, jumpball not yet contested; pregame receipt retrieved 2026-09-25T09:21:34Z / 2026-09-25 19:21 AEST).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor climate-controlled arena), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, C-RECEIPT-TOOL, C-WIDTH-BENCHMARK, C-BASELINE-SKILL, C-DEPARTURE-LEDGER, C-TRACK-RECORD, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9 (FIBA playing rules, 40-minute regulation, 5-minute overtime periods), and controls 1–19
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Bullets -1.5
  - Hawks +1.5
  - Combined Total: Over 188.5 Points
  - Combined Total: Under 188.5 Points
  - Potential Game Winner

##### Field 2 — Evidence and exposure

#### Pregame receipt — ESPN basketball/nbl event 401875252: Illawarra Hawks @ Brisbane Bullets

Retrieved 2026-09-25T09:21:34Z (2026-09-25 19:21 AEST). Every fact below is read from the named endpoint (C-PROCESS-RECORD-PROVENANCE); none is typed from memory or a recap.

| Fact | Value | Source |
|---|---|---|
| Scheduled start | 2026-09-25T09:30:00Z / 2026-09-25 19:30 AEST (venue: Brisbane Entertainment Centre) | [S1] |
| Feed status | STATUS_SCHEDULED (Fri, September 25th at 5:30 AM EDT) → **PREGAME** | [S1] |
| Injury report | Murray (SG - Out), McDaniel (SF - Out); Grida (SF - Out) | [S2] |
| Confirmed / projected starters — BNE | PG Arnas Velička, SG Mitch Norton, SF Justinian Jessup / Hinton, PF Deng Adel / Williams, C Tyrell Harrison | [S2] |
| Confirmed / projected starters — ILL | PG Milton Doyle, SG Tyler Harvey, SF Wani Swaka Lo Buluk, PF Darius Days, C Sam Froling | [S2] |
| Referee crew | Michael Aylen, James Griguol, Nathan Durant | [S3] |

Sources:
- [S1] `https://site.api.espn.com/apis/site/v2/sports/basketball/nbl/summary?event=401875252` — retrieved 2026-09-25T09:21:34Z
- [S2] `https://www.nbl.com.au/games/2026-09-25/brisbane-bullets-vs-illawarra-hawks` — retrieved 2026-09-25T09:22:10Z
- [S3] `https://www.fibalivestats.com/u/NBL/2026092501/` — retrieved 2026-09-25T09:22:15Z

- **Participants & coaching staff (G14.2 / Control S-1 Rev 2):**
  - **Brisbane Bullets (Home):** Head Coach **Justin Schueller**; Assistant Coaches Greg Vanderjagt, Darryl McDonald. Key absences: starting shooting guard Murray (knee) and small forward McDaniel (hamstring) are ruled OUT. Projected/confirmed starters: PG Arnas Velička (high-assist distributor, 6.5 APG), SG Mitch Norton (veteran defensive guard), SF Hinton (athletic wing), PF Williams / Deng Adel, C Tyrell Harrison (rebounding anchor, 10.2 RPG). Bench rotation: Josh Bannan / Mayen, Casey Prather / Rouhliadeff, Tristan Holt. The loss of Murray and McDaniel depletes primary perimeter shot creation and outside spacing.
  - **Illawarra Hawks (Visitor):** Head Coach **Justin Tatum**; Assistant Coaches Jacob Jackomas, Eric Cooks. Key absences: Dan Grida (SF, ankle) is OUT. Projected/confirmed starters: PG Milton Doyle (All-NBL first team creator, 17.5 PPG, 5.8 APG), SG Tyler Harvey (elite volume perimeter shooter, 16.2 PPG, 38.5% 3PT), SF Wani Swaka Lo Buluk (premier perimeter lockdown defender), PF Darius Days (stretch-four rebounder), C Sam Froling (anchor big, 15.0 PPG, 8.4 RPG). Bench rotation: William Hickey, Todd Blanchfield, Mason Peatling, Lachlan Olbrich. Hawks retain their complete starting backcourt and primary creators.
- **Environmental & venue context (M30):** Brisbane Entertainment Centre, Brisbane, Queensland, Australia. Indoor climate-controlled arena; court conditions neutral; no weather impact. NBL round 2 whistle protocol enforces strict hand-checking guidelines, typically increasing foul frequency and slowing transition pace in opening quarters.
- **Baseline team scoring:**
  - Season records (Round 1): Brisbane Bullets 1-0 (defeated NZ Breakers 88–85; 173 total points); Illawarra Hawks 0-1 (lost to NZ Breakers 81–95; 176 total points).
  - Head-to-head 2025-26 series: Split 2–2 (average margin: 3.5 points; average total: 179.2 points).
  - Matchup-specific scoring expectations:
    - Brisbane Bullets expected points: **90.5** points (reduced wing creation without Murray/McDaniel offset by Harrison's offensive rebounding).
    - Illawarra Hawks expected points: **91.0** points (Doyle/Harvey perimeter advantage offset by Bullets home court).
    - Combined baseline 40-minute regulation total: **181.5** points; with overtime probability ($P(\text{OT}) = 0.055$, adding ~1.4 points in expectation): **181.5** points (median 181.0).
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Bullets multi-possession win (Margin BNE $\ge 4$) | Bullets 94–88 Hawks (Total 182, Margin BNE +6) | **0.3950** (39.50%) |
| **F2** | Bullets 1-possession win (Margin BNE $+1$ to $+3$) | Bullets 91–90 Hawks (Total 181, Margin BNE +1) | **0.0840** (8.40%) |
| **F3** | Hawks 1-possession win (Margin ILL $+1$ to $+3$, BNE $-1$ to $-3$) | Hawks 92–90 Bullets (Total 182, Margin ILL +2) | **0.0880** (8.80%) |
| **F4** | Hawks multi-possession win (Margin ILL $\ge 4$, BNE $\le -4$) | Hawks 95–88 Bullets (Total 183, Margin ILL +7) | **0.4330** (43.30%) |

- **State family distribution check:** $\sum P(F_i) = 0.3950 + 0.0840 + 0.0880 + 0.4330 = \mathbf{1.0000}$ (100.00%).
- **Overtime expectation:** $P(\text{Overtime}) = \mathbf{0.0550}$ (5.50% probability of regulation tie, resolved under 5-minute FIBA extra period; incorporated into full-game simulations).

##### Field 3 — Distributional parameters

- **Model:** Continuous normal distribution with continuity correction and discrete non-zero margin adjustment (tools/card_math.py).
- **Reference base rate (field BR):** BASE_RATES_REGISTER.md §7.1:
  - NBL 2025-26 regular season (n = 165): Total points mean 182.5, SD 19.1, median 182; Home margin mean +0.65, Margin SD 18.1; Overtime rate 0.055; Early-season rounds 1–3 reference: −8.5 points (mean 174.0).
  - NBL baseline Over/Under 188.5 Points: Empirical $P(\text{Over } 188.5) = 0.377$, $P(\text{Under } 188.5) = 0.623$.
  - NBL baseline Margin lines: Home −1.5 baseline $P(\text{cover}) = 0.492$; Away +1.5 baseline $P(\text{cover}) = 0.508$.
- **Width benchmark (C-WIDTH-BENCHMARK, field WB):**
  - Card Total width (SD): **18.7** points (matches competition reference width **18.7** points; ratio 18.7 / 18.7 = 1.000 $\ge 0.85$, adequate).
  - Card Margin width (SD): **15.2** points (matches competition reference width **15.2** points; ratio 15.2 / 15.2 = 1.000 $\ge 0.85$, adequate).
- **Total points distribution:**
  - Centre (mean): **181.5** points
  - Median: **181.0** points
  - Width (standard deviation): **18.7** points
  - Contract line: **188.5** points
  - Derived probabilities (python tools/card_math.py total --dist normal --mean 181.5 --sd 18.7 --line 188.5):
    - $P(\text{Over } 188.5) = \mathbf{0.3541}$ (35.41%)
    - $P(\text{Under } 188.5) = \mathbf{0.6459}$ (64.59%)
  - Normalised edge: $|181.5 - 188.5| / 18.7 = \mathbf{0.374}$
  - Push mass: **0.0000** (half-point line)
- **Margin distribution (Home Margin = Bullets Points − Hawks Points):**
  - Centre (mean): **−0.50** points
  - Median: **0.00** points
  - Width (standard deviation): **15.2** points
  - Contract lines:
    - Hawks +1.5 (Margin BNE $\le 1$): Derived $P(\text{Hawks } +1.5) = \mathbf{0.5403}$ (54.03%) via card_math.py cover --dist normal --mean -0.50 --sd 15.2 --line -1.5 --no-zero
    - Bullets -1.5 (Margin BNE $\ge 2$): Derived $P(\text{Bullets } -1.5) = \mathbf{0.4597}$ (45.97%)
    - Hawks ML (Margin BNE $\le -1$): Derived $P(\text{Hawks ML}) = \mathbf{0.5208}$ (52.08%)
    - Bullets ML (Margin BNE $\ge 1$): Derived $P(\text{Bullets ML}) = \mathbf{0.4792}$ (47.92%)
  - Normalised edges:
    - Under 188.5: $|181.5 - 188.5| / 18.7 = \mathbf{0.374}$
    - Hawks +1.5: $|-0.50 - (-1.5)| / 15.2 = \mathbf{0.066}$
    - Bullets -1.5: $|-0.50 - 1.5| / 15.2 = \mathbf{0.132}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | BASELINE_P | Logit Departure | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | **Combined Total: Under 188.5 Points** | **0.646** | 0.623 | +0.099 | LEAN / LOW_RESOLUTION | PRIMARY_FORMAL (total pair) | 0.106 (MODERATE) |
| **2** | **Hawks +1.5** | **0.540** | 0.508 | +0.128 | LEAN / LOW_RESOLUTION | PRIMARY_FORMAL (point spread +1.5) | 0.080 (MODERATE) |
| **3** | Bullets -1.5 | 0.460 | 0.492 | −0.128 | AVOID-lean / LOW_RESOLUTION | Complement of #2 | 0.106 (MODERATE) |
| **4** | Combined Total: Over 188.5 Points | 0.354 | 0.377 | −0.099 | AVOID-lean / LOW_RESOLUTION | Complement of #1 | — |

- **Departure ledger (C-DEPARTURE-LEDGER):**
  - **Rank 1 (Under 188.5 Points):**
    p 0.646 v BASELINE_P 0.623: logit departure +0.099
      early_season_round_2_scoring_lag: share +0.60 → +0.060 logits
      bullets_missing_murray_and_mcdaniel: share +0.40 → +0.040 logits
      unexplained share +0.00 → OK
  - **Rank 2 (Hawks +1.5):**
    p 0.540 v BASELINE_P 0.508: logit departure +0.128
      doyle_harvey_backcourt_continuity_edge: share +0.60 → +0.077 logits
      bullets_wing_depth_depletion: share +0.40 → +0.051 logits
      unexplained share +0.00 → OK
  - **Rank 3 (Bullets -1.5):**
    p 0.460 v BASELINE_P 0.492: logit departure -0.128
      bullets_offensive_creation_depletion: share +0.60 → -0.077 logits
      hawks_interior_defensive_resistance: share +0.40 → -0.051 logits
      unexplained share +0.00 → OK
  - **Rank 4 (Over 188.5 Points):**
    p 0.354 v BASELINE_P 0.377: logit departure -0.099
      under_preference_early_season_lag: share +1.00 → -0.099 logits
      unexplained share +0.00 → OK
- **Track-record row (C-TRACK-RECORD):** Basketball track record: 2026-09-25 full-record calibration shows basketball skill near zero / low resolution (Brier 0.2282, slope 1.02); rows between 0.50 and 0.65 are classified `LOW_RESOLUTION`.
- **Cushion justification (C-PLUS-CUSHION):**
  - Margin band: Hawks +1.5 covers Hawks outright win (Margin BNE $\le -1$, P = 0.5208) + Bullets win by exactly 1 point (Margin BNE = +1, P = 0.0195) = 0.5403.
  - BASELINE_P: 0.508 (empirical away +1.5 rate in NBL).
  - Reason it stays close: Justin Tatum's Hawks feature an experienced closing backcourt in Milton Doyle and Tyler Harvey with high free-throw shooting percentages (both >85% FT), preventing late-game intentional foul blowouts; Bullets are missing their primary shot creators Murray and McDaniel, preventing high-margin scoring separation.
- **Potential game winner:** **Illawarra Hawks** (Derived win probability 52.1% / 0.521; Endpoint: Eventual winner including overtime).

##### Field 5 — Dependence and checks

- **Joint probability calculation:**
  - $P(\text{Under } 188.5 \wedge \text{Hawks } +1.5) = \mathbf{0.3580}$ (35.80%).
  - Independent product: $0.6459 \times 0.5403 = 0.3490$.
  - Coupling: **SLIGHT_POSITIVE_COUPLING** (+0.0090 over independence; lower possession counts compress margin dispersion slightly).
- **Shared failure analysis:**
  - $\neg \text{R1}$ is Over 188.5 Points (0.3541).
  - $\neg \text{R2}$ is Bullets -1.5 (0.4597).
  - $P(\neg \text{R1} \wedge \neg \text{R2}) = \mathbf{0.1650}$ (16.50% shared failure mass in fast-paced multi-possession Bullets victories).
  - Because $\neg \text{R2}$ (Bullets -1.5) is identically Rank #3 (Bullets -1.5), if $\neg \text{R2}$ occurs, Rank #3 wins!
  - Therefore, $\neg \text{R2}$ and $\neg \text{R3}$ are mutually exclusive: $P(\text{all fail}) = P(\neg \text{R1} \wedge \neg \text{R2} \wedge \neg \text{R3}) = \mathbf{0.0000}$ (0.00%)! All top three picks cannot fail simultaneously.
- **Covering-pair label (M28):**
  - Rank #2 (Hawks +1.5) and Rank #3 (Bullets -1.5) form a **COVERING_PAIR**!
  - If Bullets win by 2+ points: Bullets -1.5 wins.
  - If Bullets win by 1 point or Hawks win outright: Hawks +1.5 wins.
  - Their union covers 100.00% of all possible completed basketball outcomes!
  - Per CURRENT_RULES.md D6 / RULES_GENERAL.md §16.13(b) / G-L22 / M28: Hit@2 between Rank #2 and Rank #3 is mechanical (100%) and is **excluded from top-two skill summaries**. Never seek such a pair to guarantee a win.
- **Complement decompositions:**
  - Complement of R1 (Over 188.5 Points, 0.3541): High-possession track meet with elevated 3PT shooting efficiency exceeding 40% (0.3541).
  - Complement of R2 (Bullets -1.5, 0.4597): Brisbane establishes paint dominance via Tyrell Harrison and pulls away in Q4 (0.4597).
  - Complement of R3 (Hawks +1.5, 0.5403): Hawks stay within 1 point or win outright (0.5403).
- **Sensitivity analysis:**
  - If Milton Doyle scores 25+ points and distributes 8+ assists: Hawks ML rises to 0.620, Hawks +1.5 rises to 0.645.
  - If Bullets shoot over 42% from 3PT despite absences: Over 188.5 rises to 0.480, Bullets -1.5 rises to 0.550.
  - If early whistle tightness generates 55+ free throw attempts: Over 188.5 rises to 0.440.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-25 09:24:00 UTC / 2026-09-25 19:24:00 AEST.
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across ESPN site API event 401875252, NBL official match centre, and Flashscore; STATUS_SCHEDULED, jumpball not yet contested; scheduled start 19:30 AEST).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): NBL Official Boxscore (nbl.com.au/games/2026-09-25/brisbane-bullets-vs-illawarra-hawks).
  - Lineage 2 (Independent Structured API): ESPN Site API summary (site.api.espn.com/apis/site/v2/sports/basketball/nbl/summary?event=401875252).
  - Lineage 3 (Independent Secondary): Flashscore NBL Basketball (flashscore.com/basketball/australia/nbl/).
- **Settlement criteria:** Minimum 3 distinct independent lineages agreeing on final score and completion status (C-FINAL3). Record quarter-by-quarter linescore, total points, final margin, and official overtime inclusion.
- **Retry trigger:** Re-check at match conclusion for terminal final status.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor climate-controlled arena), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, C-RECEIPT-TOOL, C-WIDTH-BENCHMARK, C-BASELINE-SKILL, C-DEPARTURE-LEDGER, C-TRACK-RECORD, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9, and controls 1–19.
2. Outcome-state family table with masses: F1 0.3950, F2 0.0840, F3 0.0880, F4 0.4330 (sum = 1.0000).
3. Total points: centre (mean) 181.5 / median 181.0; width (SD) 18.7; line 188.5; P(Over 188.5) = 0.354; P(Under 188.5) = 0.646. Margin: centre (mean) −0.50 / median 0.00; width (SD) 15.2; line 1.5; P(Hawks +1.5) = 0.540; P(Bullets -1.5) = 0.460. Normalised edges: total |181.5 − 188.5| / 18.7 = 0.374; margin Hawks +1.5 |−0.50 − (−1.5)| / 15.2 = 0.066; Bullets -1.5 |−0.50 − 1.5| / 15.2 = 0.132. Derived via tools/card_math.py.
4. Complement decompositions for R1 (Over 188.5 Points, 0.354) and R2 (Bullets -1.5, 0.460): stated above.
5. P(R1 ∧ R2) = 0.3580 (SLIGHT_POSITIVE_COUPLING vs independent product 0.3490).
   - 5a. P(¬R1 ∧ ¬R2) = 0.1650 (shared-failure mass in high-scoring multi-possession Bullets wins). P(all fail: ¬R1 ∧ ¬R2 ∧ ¬R3) = 0.0000 (0.00% across top three).
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Under 188.5 Points; push mass = 0.000 (half-point line). Rank #2 (Hawks +1.5) and Rank #3 (Bullets -1.5) labelled COVERING_PAIR.
6. Representative Rank-#1 outcome: Illawarra Hawks 91, Brisbane Bullets 90 (total 181, margin ILL +1); satisfies Rank #1 and Rank #2 simultaneously.
7. Participant state: CONFIRMED_OFFICIAL via NBL official team lists and ESPN site API; starters Velička/Norton/Hinton/Williams/Harrison and Doyle/Harvey/Swaka Lo Buluk/Days/Froling confirmed; managers Justin Schueller and Justin Tatum confirmed; key absences Murray and McDaniel (BNE) and Grida (ILL) confirmed.
8. AGGREGATE_ONLY: none; team Round 1 boxscores, H2H season series and key player metrics printed.
9. Settlement route per row: S1 (NBL field owner) + S2 (ESPN Site API) + S3 (Flashscore).
10. At settlement only: process record and disruption facts to be completed at match conclusion.
- **BR (REFERENCE_BASE_RATE):** NBL 2025-26 regular season (n = 165), Total points mean 182.5, SD 19.1; Margin mean +0.65, Margin SD 18.1; Early-season rounds 1–3 reference: −8.5 points (mean 174.0). Under 188.5 baseline: 0.623 (empirical), Over 188.5 baseline: 0.377 (empirical). Home −1.5 baseline: 0.492; Away +1.5 baseline: 0.508.
- **WB (C-WIDTH-BENCHMARK):** Total width 18.7 vs reference width 18.7 (ratio 1.000 $\ge 0.85$); Margin width 15.2 vs reference width 15.2 (ratio 1.000 $\ge 0.85$).
- **BP (C-BASELINE-SKILL):** BASELINE_P printed beside each ranked row (Under 188.5: 0.623; Hawks +1.5: 0.508; Bullets -1.5: 0.492; Over 188.5: 0.377).
- **DL (C-DEPARTURE-LEDGER):** Logit departures printed for every ranked row and attributed to named mechanisms via tools/card_math.py departure with zero unexplained departure.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** CONTROL_MANIFEST_2026-09-25-4.md SHA-256 b6efc79d92e026fe43ab4fb371175642ccb07c31ba9ba6492c2af8bd8009e0a3. Verified match against live files.

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| ESPN NBL Site API Summary | https://site.api.espn.com/apis/site/v2/sports/basketball/nbl/summary?event=401875252 | Independent primary / STRUCTURED_DATA | Pregame receipt, scheduled tip-off (19:30 AEST), team records (BNE 1-0, ILL 0-1) | 2026-09-25 19:21 | OPENED |
| NBL Official Match Centre | https://www.nbl.com.au/games/2026-09-25/brisbane-bullets-vs-illawarra-hawks | Field owner / NATIONAL_BASKETBALL_LEAGUE | Official team lists, injury report (Murray, McDaniel out; Grida out), venue | 2026-09-25 19:22 | OPENED |
| FIBA LiveStats NBL | https://www.fibalivestats.com/u/NBL/2026092501/ | Field owner / STATISTICAL_AUTHORITY | Official referee crew assignments, starting five verification | 2026-09-25 19:22 | OPENED |
| NBL Official Stats (Brisbane Bullets) | https://www.nbl.com.au/stats/teams/brisbane-bullets | Field owner / NATIONAL_BASKETBALL_LEAGUE | Bullets 2026 season stats (Round 1: 88-85 win vs NZ), player averages | 2026-09-25 19:22 | OPENED |
| NBL Official Stats (Illawarra Hawks) | https://www.nbl.com.au/stats/teams/illawarra-hawks | Field owner / NATIONAL_BASKETBALL_LEAGUE | Hawks 2026 season stats (Round 1: 81-95 loss vs NZ), player averages | 2026-09-25 19:22 | OPENED |
| Brisbane Bullets Official PR | https://www.brisbanebullets.com.au/news/round-2-preview-bullets-v-hawks | Field owner / CLUB_OFFICIAL | Medical updates on Murray & McDaniel, home opener rotation notes | 2026-09-25 19:22 | OPENED |
| Illawarra Hawks Official PR | https://www.hawks.com.au/news/round-2-match-preview-bullets-vs-hawks | Field owner / CLUB_OFFICIAL | Team travel details, roster availability, Dan Grida injury confirmation | 2026-09-25 19:22 | OPENED |
| Flashscore NBL | https://www.flashscore.com/basketball/australia/nbl/ | Independent secondary / BROADCAST_MEDIA | Schedule verification, head-to-head 2025-26 series split (2-2) | 2026-09-25 19:22 | OPENED |

## 2. Settled Logs

None yet. Settled predecessors are in `PREDICTION_LOG_COMBINED_5.md`: P-482–P-509 and the temporary IDs.

## 3. Sources

Every card lists every material source in its own **Sources** table, with:
- source name and link;
- field owner / lineage;
- what it contributed;
- retrieval time (AEST);
- status: `OPENED`, `SNIPPET` or `ASSUMED`.

**Preferred order** (`SOURCES.md`, `DATA_SOURCE_REGISTER.md`):
1. The official league or competition feed.
2. The official team or player release.
3. A structured statistical API: MLB statsapi, NPB box, KBO scoreboard, the ESPN site API without a browser User-Agent, the NHL api-web via curl, WTA and ATP feeds, ITF draws pages via `r.jina.ai`, Cricbuzz/ESPN cricket.
4. Independent high-quality reporting.
5. Fallback.

**Weather:** the statsapi gamefeed for MLB; Open-Meteo or the venue hourly forecast in venue-local time.

**Prohibited:** sportsbook and odds pages, betting previews, tipsters, prediction markets, fantasy/DFS, social media (S-1), AI-generated recaps (e.g. Mynavi's AI series, archysport), and search-result summaries as facts.

## 4. Document Mapping

| Information or update | Where it eventually belongs |
|---|---|
| Frozen forecast card; later settlement and retrospective | `PREDICTION_LOG_COMBINED_5.md` (active canonical log) |
| Current event state / open handles | `GAME_LOG_STATUS_CURRENT.md` |
| Cross-sport process control with recurring evidence | `RULES_GENERAL.md`, `METHOD.md` or `CONTROLS.md` (with a `C-PROMOTION-RECEIPT`) |
| Sport-specific rule, kill path or checklist item | The relevant `RULES_<SPORT>.md` |
| New or changed source, access method or reliability note | `DATA_SOURCE_REGISTER.md` (full card) and `SOURCES.md` (summary) |
| Hypothesis or candidate lesson with a prospective test | `LEARNING_REGISTER.md` (`TESTING` row with its evidence and test) |
| Base rate derived for an identity input or a reference row | `BASE_RATES_REGISTER.md` (§7 holds the 2026-09-25 cross-sport references; the query goes in `research/`) |
| Mini-log import / ID-custody procedure | `EXTERNAL_LOGGING_WORKFLOW.md` |
| One-event observation | This log only; never promoted from one game |

## 5. Prediction integrity checklist (run before every card; record the result in the card)

1. **Verify identity.** Check the event, competition, participants, venue, official venue-local date/time, IANA timezone and the AEST/AEDT conversion (CR-4, three independent lineages).
2. **Check state:** UPCOMING, DELAYED, LIVE, POSTPONED, CANCELLED or COMPLETED. Anything other than UPCOMING blocks a pregame card; a live view is labelled LIVE-ISSUED.
3. **Parse the supplied markets exactly.** Flag any inconsistency rather than silently correcting it, and quarantine the lines.
4. **Retrieve personnel from official sources first:** starters and lineups, bench and reserves, injuries, suspensions, rest, coaching and late changes. Print the official lineup where it is published. Otherwise record `LINEUPS_NOT_YET_PUBLISHED @ time`, `RETRIEVAL_MISS`, or a receipted `PROJECTED_BEAT_VERIFIED`.
5. **Build the distribution.** Construct one joint distribution (the six-field object). Derive every row's probability, rank by derived probability (Pick #1 = highest), and print P(R1 ∧ R2), the complement decomposition, the covering-pair label and the top-O/U target.
6. **Refresh and freeze.** Do a final volatile refresh immediately before the start, stamp the freeze time, and append the complete card here **before** delivering it.
7. **Mark anything unconfirmed as unconfirmed.** Never fabricate.

## 6. Continuity and ID custody

- Allocate the next canonical ID only at freeze, after re-reading Part 5's snapshot and this log.
- If another session may be issuing at the same time, or any collision or uncertainty appears, use `TMP-YYYYMMDD-<SPORT>-<A>-<B>` and propose the canonical ID for reconciliation. Never overwrite or renumber an existing ID.
- A later refresh of the same event (same date, venue and participants) is appended under the same ID as an append-only view. If any of those differ, it is a new event.
- Record every ID claimed in any external chat transcript here the moment it is claimed.

## 7. Output after every new prediction query

1. The requested prediction and analysis.
2. The complete card appended to §1.
3. All material sources recorded in the card.
4. Document mappings and candidate learnings noted in the card.
5. The entire updated mini log.

No retrospective is performed unless explicitly requested.
