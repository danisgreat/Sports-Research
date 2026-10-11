<!-- BEGIN CARD P-572 -->
## Card · P-572 · Baseball / Korea KBO · KT Wiz @ Samsung Lions · 2026-10-11

- **Working ID:** `P-572 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`
- **Event key:** `KBO:2026:KT-SAM-DAEGU-20261011:2026-10-11`
- **Native event ID:** `NOT_VERIFIED` (secondary MyKBO local event 14035; not represented as a league-owned ID)
- **Sport:** `Baseball`
- **League:** `Korea KBO / 2026 regular-season makeup fixture (not postseason)`
- **Tracking alias:** `LOCAL-20261011-P-572-KBO-KT-SAM`
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO`
- **Timing state:** `PREGAME` (scheduled start 16:00 AEDT; researched before scheduled first pitch, official page displaying pregame; any subsequent delay or live-state change requires an addendum)
- **Research completed:** `2026-10-11T15:55:00+11:00` (AEDT; all model outputs completed before scheduled first pitch; source input snapshot 15:52:14 AEDT)
- **Scheduled start:** `2026-10-11T16:00:00+11:00` (14:00 KST; user-supplied 15:00 AEDT was ONE HOUR EARLY)
- **Endpoint:** `Official KBO regular-season final score; nominal 9 innings, up to 11 innings with potential tie; visiting KT bats first/top ninth, Samsung bottom ninth can be skipped if already leading, walk-off truncation; winner three-way away/home/tie. Supplied operator moneyline and action terms NOT_VERIFIED.`
- **Distribution object:** `kbo_nb_9inning_home_walkoff_11inning_extras_v1 — 9-inning potential μ KT=4.65, SAM=4.62 runs; NB team dispersion φ=0.290, shared lognormal environment σ=0.044; conditional bottom ninth and walkoffs; 10th/11th innings on ties, cap at 11; PCG64 seed 5722026 N=1,800,000; no post-first-pitch data.`
- **Expected score:** `runs, KBO official full final including potential 10th/11th innings, home bottom-inning suppression; Monte Carlo score SDs — KT Wiz 4.72 (SD 3.32) · Samsung Lions 4.40 (SD 3.00) · total 9.11 (SD 4.58) · margin KT − Samsung +0.32 (SD 4.36); regulation score before extras KT 4.65 + SAM 4.34=8.99; extras share +0.12 mean runs per game.`
- **Regime flags:** `NONE` (late regular-season, standings positions clinched; possible playoff-preservation rotation noted as unmeasured uncertainty, no invented rule multiplier)
- **Retirement rule:** `N/A`
- **Listed-pitcher rule:** `FRAMEWORK_DEFAULT: sporting result stands with an actual replacement starter, but a material pre-start pitcher change triggers a dated reforecast addendum; market operator action/listed-pitcher policy UNKNOWN_DEFINITION, cannot infer void/win from it.`
- **Abandonment rule:** `FRAMEWORK_DEFAULT: do not treat a partial score as final; defer or VOID if cancelled, suspended or abandoned without competition-certified final. Official KBO final marker controls. Operator early-termination contract unspecified.`
- **Settlement fields:** `Away/home official final runs, innings-by-inning line, completed-inning count, official tie/W/L, listed and actual starters, delays; provider KBO official ScoreBoard/GameCenter, fallback Naver Sports KBO structured box; capture from final live official KBO page.`
- **Capture due:** `2026-10-12T04:00:00+11:00` (12 h after start)
- **Rules read:** `CURRENT_STATE, METHOD, CURRENT_RULES §§1–9; SELECTION_RULES §§1–8; RULES_BASEBALL §0 BB-P1–P5 and §§3–5,7–9; PROBABILITY_TOOLKIT §§3,3.1; BASE_RATES_REGISTER §§3,5; LEAGUE_PROFILES KBO 2023–25 row; SOURCES §§1.4,3.1,3.15; ARCHIVE_USE_GUIDE §§1–6; CARD_AND_LOG_TEMPLATES §§2,3,3a,7; research/prompts/1_GAME_CARD.md, README`
- **Archive check:** `ARCHIVE_PARTIAL for 2026: current 2026 KBO yearly CSV not found at Previous Sports Results/Baseball/KBO/2026/2026_games.csv (404). Opened 2023/2024/2025 season CSV header + first record to confirm Date, Away/Home Score, Total Runs, Extra Innings, starter columns; LEAGUE_PROFILES KBO regular-season sample n=2182 (2023–2025), total mean 9.77, total SD 4.93, margin SD 4.79, φ=.290, σenv=.044, one-run 23.8%, tie 2.1%. No current-game or later observations taken from archive.`
- **Evidence quotes:** `KBO official schedule @ 2026-10-11T15:52:14+11:00: "10.11(일) 14:00 KT vs 삼성" (KST); KBO official game preview @ 2026-10-11T15:52:14+11:00: "후라도는 11일 대구삼성라이온즈파크에서 열리는 KT 위즈와의 홈경기에 선발 등판한다." (Jurado scheduled starting); same preview "이에 맞서는 KT의 선발 투수는 고영표다." (Ko listed starter); KBO official scoreboard @ 2026-10-11T15:52:14+11:00 showed 경기전 (before game); secondary Yakuku Yaru lineup page @ 2026-10-11T15:52:14+11:00 explicitly states "예상 라인업입니다" (projected order, not official) — BB-P2 not cleared.`

### Decision block

**Distribution:** `kbo_nb_9inning_home_walkoff_11inning_extras_v1`. Pre-last-inning means KT 4.65 and SAM 4.62; score-state and two possible extra innings produce final expected KT 4.72/SAM 4.40, total 9.11. NB overdispersion φ=.290, game lognormal effect σ=.044; KBO 11-inning tie rule. The 2023–25 archive profile total mean is 9.77. *All probabilities are uncalibrated analyst scenarios, not backtested.*

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED (wide visiting-run handicap replacing KT ML) | KT Wiz +4.5 runs — KBO official final including up to 11 innings/tie | 88.6% | FROM_DISTRIBUTION:kbo_nb_9inning_home_walkoff_11inning_extras_v1 | Expected KT−SAM +0.32, SD 4.36; KT offence 809/142, Ko–Jurado close starter comparison | Samsung wins by 5+; starter early exit, homer/bullpen asymmetric tail |
| 2 | PICK | ANALYST_DERIVED (wide lower-total threshold replacing supplied Over 7.5) | Combined total Over 4.5 runs — KBO official final including up to 11 innings | 86.0% | FROM_DISTRIBUTION:kbo_nb_9inning_home_walkoff_11inning_extras_v1 | 9.11 expected final total, KBO history 9.77; two strong offences | Both aces suppress the game to 0–4 runs, rain truncation if officially final |
| 3 | INFORMATIONAL | ANALYST_DERIVED (wide upper-total threshold replacing supplied Under 7.5) | Combined total Under 13.5 runs — KBO official final including up to 11 innings | 84.2% | FROM_DISTRIBUTION:kbo_nb_9inning_home_walkoff_11inning_extras_v1 | 9.11 centre, 4.58 modeled SD, two declared aces | Combined offences/bullpens produce 14+ |
| 4 | INFORMATIONAL | ANALYST_DERIVED (visiting handicap alternative replacing supplied KT ML) | KT Wiz +3.5 runs — KBO official final including up to 11 innings/tie | 83.7% | FROM_DISTRIBUTION:kbo_nb_9inning_home_walkoff_11inning_extras_v1 | KT season run differential +165, matchup near even, 11-inning tie possibility | Samsung wins by 4+ |

**P(Rank 1 and Rank 2 both lose):** `0.0% by construction`. KT +4.5 loses only if Samsung wins by five or more; a total of four runs or fewer cannot have a five-run margin.
**Rank 1 − Rank 2 gap:** `2.6 percentage points (88.6−86.0)`, but the highest *numeric* non-complementary alternative on the priced ladder is **Under 14.5=87.5%**, leaving only `1.1 points` against the formal gate; this is not a claim of BB-P2 source eligibility.
**Rank-1 gate:** `RANK1_UNSTABLE` — fails required ≥4pp separation (`SELECTION_RULES §2`); further `BB-P2: RETRIEVAL_MISS` blocks full-game runline or total from qualified Rank 1 because official *batting order* could not be verified. All four rows are exploratory, **not certified/qualified selections**.
**Adjustment dependence:** `NONE` (no separately imposed ≥0.25-SD measured post-anchor adjustment; input rates subjective and are explored in A6).
**Supplied rows not selected:** `KT Wiz ML: 49.0% outright; Samsung ML: 48.4%; terminal tie: 2.6% (KBO three-way; operator void-on-tie unknown). Samsung +1.5 runs 63.2%; Combined Over 7.5 runs 58.4%, Under 7.5 runs 41.6%, full final incl extras.`
**Potential winner:** `KT Wiz 49.0% outright, Samsung Lions 48.4%, tie 2.6%` (KBO official terminal end to 11 innings; KT by a very small margin, low-confidence near coin-flip; if operator voids draw, conditional KT win ≈50.3%, not a known contract).

### Appendix

#### A1. Identity, timing and state
- Official KBO game: Daegu Samsung Lions Park, Daegu; KT away, Samsung home, 11 Oct 2026 14:00 KST=16:00 AEDT. KBO regular-season postponed/makeup schedule extends to 12 Oct, not postseason. User's 15:00 AEDT conflicts with league-owned 14:00 KST (16:00 AEDT). Research snapshot `2026-10-11T15:52:14+11:00` before scheduled first pitch; KBO scoreboard displayed **경기전**.
- Season ranking KT first 88-49-5; Samsung second 83-56-3. Positions already sealed; individual pitching awards still in play, introducing an uncertain late-season incentive/rotation mix. No live result or in-game data used.
- KBO regular season nominal 9 innings, at most 11, tie permitted (since 2025); regulation tie unresolved through 10th/11th may end as tie. Samsung home ninth can be skipped or truncated as walk-off. No assumption of a postseason 15-inning rule for this regular-season match.

#### A2. Supplied contracts (reference only)
| Literal sporting proposition (as interpreted; operator terms unavailable) | p_card | Complement / three-way |
|---|---:|---|
| KT Wiz ML, outright KBO final | 49.0% | Samsung 48.4%; tie 2.6%. A sportsbook two-way draw void is UNKNOWN_DEFINITION |
| Samsung Lions +1.5, final | 63.2% | KT −1.5 36.8% |
| Combined total Over 7.5, final | 58.4% | Under 7.5 41.6% |
| Combined total Under 7.5, final | 41.6% | Over 7.5 58.4% |

#### A3. Pregame process evidence (not forecast tips, odds or betting prices)
- Official KBO preview declares **KT Ko Young-pyo** (28 starts, 14–7, ERA 3.38, 2.84 ERA vs Samsung in three meetings) against **Samsung Ariel Jurado** (23 starts, 9–2, ERA 3.27, 2.31 ERA vs KT in two meetings). Both confirmed as *announced* starters by KBO league-owned preview; actual first-pitch participation is not yet verified. Ko has personal 15th-win incentive, Jurado 10th win/percentage-title incentive.
- Team season totals from pregame MyKBO structured standings: KT 809 scored / 644 allowed in 142 games = 5.70 R/G, 4.54 RA/G; Samsung 801 / 653 in 142 = 5.64 R/G, 4.60 RA/G. KT team AVG .284 vs Samsung .274, season ERAs 4.17 vs 4.26; KT overall head-to-head 5–9 vs Samsung. This is not an opponent-adjusted player-by-player estimate.
- Both official starting batting orders **NOT VERIFIED**. A secondary 9-batter list explicitly says projected, not officially released: KT projected Choi Won-jun, Kim Min-hyeok, An Hyeon-min, Hilliard, Kim Hyun-soo; Samsung projected Kim Ji-chan, Kim Seong-yun, Park Seung-gyu, Diaz, Choi Hyoung-woo. These are not treated as official participation. KBO official scorecard did not provide an authenticated timestamped lineup for this retrieval; mark `RETRIEVAL_MISS`, not confirmed.
- Starter workloads: Ko roughly 167.7 IP / 28 starts ≈6.0 innings/start, WHIP ~1.09; Jurado roughly 6.1 per start, WHIP ~1.22 (secondary Yakuku Yaru). Pitch mix, velocities, pitch-specific change since last start, exact K/BB for Jurado, current reliever availability/high-leverage workload and handedness/opponent platoon splits: `NOT_VERIFIED`. Do not invent them.
- Last completed KT contest: 7 Oct home 9–3 vs Samsung; Samsung last completed contest: 9 Oct away 1–3 vs SSG. KT thus had about three clear off days, Samsung one. No fitted numeric rest adjustment from that alone; score/postseason stakes complicate bullpen deployment.
- Daegu 14:00 KST forecast approx 27°C, easterly wind 5 km/h, partly to mostly cloudy, low rain probability (MyKBO). **No stadium-relative wind direction** or validated current-season run park factor retrieved: venue/weather adjustment 0, widened uncertainty; heat and hitter-friendly narratives not turned into independent add-ons.

#### A4. Distribution and expected score derivation
- Pre-endpoint run budget: league KBO 2023–25 total mean 9.77. Pregame 2026 season team creation and prevention roughly 5.7/4.5 runs/game, but Ko and Jurado are materially below team-pitching ERAs. Analyst first-pass nine-inning *potential* KT μ=4.65, Samsung μ=4.62 (total 9.27). **Illustrative segment arithmetic**: KT versus Jurado 6.1 IP×3.27 earned R/9=2.22 ER, plus unearned allowance 0.30, 2.9 relief IP×4.5 analyst-proxy R/9=1.45, net opposition/venue/lineup allowance +0.68 =4.65. Samsung versus Ko 6.0 IP×3.38 ERA/9=2.25 ER +0.30 unearned, 3.0 relief IP×4.5 proxy R/9=1.50, net opponent/park/lineup allowance +0.57 =4.62. Relief proxy and residual allowance are **unfitted analyst inputs**, not claims about measured individual bullpen RA/9. Difference to archive 9.77 not attributed to a precise fitted starter causality.
- Sample each side's independent gamma-mixture latent scorer with shape 1/φ=3.4483, scale φ=0.290 and multiply both rates by common E~lognormal(−σ²/2,σ²), σ=.044. Conditional Poisson production with KT nine-inning mean 4.65×E×G_K and Samsung nine-inning potential 4.62×E×G_S; this implements NB dispersion with weak shared environment.
- Visiting KT bats nine innings. Samsung produces eight-inning Poisson plus a ninth only if not already ahead after visiting top nine. The model caps the bottom-ninth score at the amount required to win (walkoff). In a tie after nine, model the 10th and optionally 11th inning from the latent team rates/9, with a walk-off cap each home half. At 11-inning cap any remaining tie is terminal. Extra innings no automatic MLB runner-on-second rule assumed.
- One terminal array (PCG64 seed 5722026, N 1,800,000): final μ_KT=4.7159, μ_SAM=4.3958, μ_total=9.1117, μ_margin (KT−SAM)=+0.3201; sample SD_KT 3.3217, SD_SAM 2.9958, SD_total 4.5813, SD_margin 4.3622. Nine-inning scores μ_KT 4.6505, μ_SAM 4.3408, total 8.9913; +0.0654 KT and +0.0550 SAM extras, total +0.1204; P(tied nine)=9.78%, P(tied final)=2.62%.
- Winner grid P(KT win)=49.00%, P(SAM win)=48.38%, P(tie)=2.62%, sums 100.00%. Absolute one-run final margin 29.72%; absolute ≥2 run margin 67.66%; absolute ≥3 run 50.65%. Compare KBO 2023–25 one-run 23.8%, margin SD 4.79, total SD 4.93. **Model has excessive one-run mass and narrower margin/total tails than historic profile**. This is a structural under-dispersion/margin-family warning; do not present 88.6% as empirically calibrated.
- The runline and total settlement path uses official final score including potential extras and tied final; the supplied ML needs operator tie/action terms which were not provided.

#### A5. Priced ladder (excerpt; full final including allowed extras)
| Family | Proposition | p_card | Opposite/complement |
|---|---|---:|---:|
| Run line | KT +4.5 | 88.59% | Samsung −4.5 11.41% |
| Total | Under 14.5 | 87.48% | Over 14.5 12.52% |
| Total | Over 4.5 | 86.01% | Under 4.5 13.99% |
| Run line | Samsung +4.5 | 84.83% | KT −4.5 15.17% |
| Total | Under 13.5 | 84.19% | Over 13.5 15.81% |
| Run line | KT +3.5 | 83.70% | Samsung −3.5 16.30% |
| Total | Under 12.5 | 78.72% | Over 12.5 21.28% |
| Run line | KT +2.5 | 77.22% | Samsung −2.5 22.78% |
| Total | Over 5.5 | 76.53% | Under 5.5 23.47% |
| Total | Over 7.5 | 58.35% | Under 7.5 41.65% |
| Run line | Samsung +1.5 | 63.17% | KT −1.5 36.83% |
| Outright | KT win | 49.00% | Samsung 48.38%; draw 2.62% |
- Monotonicity confirmed within each family: Under14.5≥Under13.5≥Under12.5; Over4.5≥Over5.5≥Over7.5; KT+4.5≥KT+3.5≥KT+2.5. Printed complement pairs each sum 100.00%.

#### A6. Adjustments and sensitivity
| Name | Target | Size | SD units | Prior basis |
|---|---|---:|---:|---|
| Ace-starter/pitching run-budget shrink and relief allocation | Both *potential* nine-inning scorer means | Included in 4.65/4.62 anchoring; no separate post-anchor shift | Not identifiable independent shift | `analyst_judgement` |
| Park, heat, wind, short rest | Both run means | 0.00 separately | 0.00 | `analyst_judgement`; no validated venue-relative wind adjustment |
| Late-season clinched-seeding motivation and rotation | Both means and width | 0.00 systematic | 0.00 | `analyst_judgement`; uncertain usage modelled as residual scenario risk |
- `Adjustment dependence: NONE` under formal ≥0.25 SD independently applied after the anchor. Critical uncertain input is bullpen availability and pregame lineups; a ±1-run shift in either team's expected scoring is approximately 0.23 of model margin SD, comparable to the 1.1-point Rank-1 gap and may change selection order. Sensitivity was separately simulated with **300,000 common-seeded draws per scenario** (the original 1,800,000-draw card is unchanged): KT nine-inning potential rate −1.00 shifts KT+4.5 88.6→85.6%, Under14.5 87.5→92.3% (ineligible >90), and Under13.5 84.2→89.9%; the nominal top-two alternatives would reorder. Samsung rate +1.00 shifts KT+4.5 88.6→82.6% and Over4.5 86.0→89.3%, reversing their order. Both point to fragile Rank-1 selection; these are **scenario sensitivities, not fitted uncertainty intervals**.
- Source uncertainty means the broad Rank-1 handicap and overs are scenario outputs only; there is no valid qualified top two from BB-P2.

#### A7. Family, gating and endpoint checks
1. `BB-P1`: League-owned KBO preview specifically names Ko Young-pyo and Ariel Jurado, but actual plate/first pitch not yet handshaken. Starter change requires timestamped addendum; do not silently replace.
2. `BB-P2`: Complete official batting orders unconfirmed; secondary order explicitly projected. `RETRIEVAL_MISS` at snapshot. RULES_BASEBALL §0.1 G14.2 blocks all full-game runline/total candidates from *qualified Rank 1*. Ranked rows are exploratory, gated, not certified.
3. `BB-P3/P5`: Regular-season 9+possible10–11 innings, terminal tie, bottom-ninth / walkoff accounted; **do not use MLB ghost runner or a postseason 15-inning resolution**.
4. `BB-P4`: Operator contract action/listed-starter and final-draw rule unknown (`UNKNOWN_DEFINITION`). The source `KT Wiz ML` is not guaranteed two-way; three-way KBO win/tie/loss is printed.
5. **+1.5 run line:** Samsung +1.5 = P(Samsung wins or final draw) 51.00% + P(KT wins by exactly one) 12.17% = **63.17%**, below the 65% Rank-1 floor; the opposite KT −1.5 is 36.83%. KT +1.5 = P(KT win or draw) 51.62% + P(Samsung wins by exactly one) 17.55% = **69.17%**. Thus neither 1.5 cushion is a confident large-margin forecast. KBO historic one-run share 23.8% vs 29.7% from this model, a named structural diagnostic rather than hidden error.
6. `P(Rank1 and Rank2 both fail)=0% by geometry`, not independence or guaranteed external sporting profit. Raw Rank-1 gap 2.6 vs Rank2, but best non-complementary alternate Under14.5 87.48% gives margin 1.11pp <4.0 => `RANK1_UNSTABLE`.
7. `p_card` ceiling: all four below 90%; Rank 2 above 58%; ranks 3–4 informational; none certified; declared schedule and weather not converted into unsupported odds. No external price/market/preview-pick predictions used.
8. Rain/suspension: official KBO terminal marker required for grades; partial 5-inning score cannot be silently treated as complete sporting event without official decision and contract terms.

#### A8. Evidence sources / read time
1. KBO official fixture and official pregame ScoreBoard: https://www.koreabaseball.com/Schedule/Schedule.aspx?month=10&year=2026 and https://www.koreabaseball.com/Schedule/ScoreBoard.aspx?searchDate=2026-10-11 — scheduled date 14:00 KST Daegu, pregame state. Accessed `2026-10-11T15:52:14+11:00`.
2. KBO league-owned preview: https://www.koreabaseball.com/MediaNews/News/Preview/View.aspx?bdSe=62555 — named Ko and Jurado; 28 starts 14–7 ERA 3.38 and 23 starts 9–2 ERA 3.27; 2.84/2.31 opponent ERAs; accessed `2026-10-11T15:52:14+11:00`.
3. KBO schedule official release: https://koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=12172 — makeup regular-season game, Sunday 14:00; accessed `2026-10-11T15:52:14+11:00`.
4. MyKBO structured fixture https://pgtest.mykbostats.com/games/14035-KT-vs-Samsung-20261011 — pregame records, 2026 current standings/RF/RA, same-day local weather and venue; accessed `2026-10-11T15:52:14+11:00`.
5. Yakuku Yaru (non-official) https://yakuku-yaru.today/games/59152 — Ko/Jurado innings/WHIP; **explicit projected** batting order, NOT confirmed official; accessed `2026-10-11T15:52:14+11:00`.
6. Yonhap: https://en.yna.co.kr/view/AEN20260407002800315 — since 2025 KBO regular-season 11-inning cap; accessed `2026-10-11T15:52:14+11:00`.
7. Sports News official pregame pitcher list republished 2026-10-10: https://www.fnnews.com/news/202610102057585125 — independently supports Ko/Jurado; accessed `2026-10-11T15:52:14+11:00`.
8. `LEAGUE_PROFILES.md`, `BASE_RATES_REGISTER.md`, `PROBABILITY_TOOLKIT.md`, `ARCHIVE_USE_GUIDE.md`; repo past results 2023/2024/2025 CSV KBO headers (2026 path unavailable); repository HEAD `33d0ea0c1c70056db7c7fb0a07dec77a633e573f`. **No bookmaker odds or tipster probability used.**

#### A9. Integrity receipt
`SPORTS_ONLY_MARKET_BLIND: PASS` · `FIXTURE_KBO_OWNER: VERIFIED` · `PREGAME_CUTOFF_BEFORE_SCHEDULED_START: YES` · `BOTH_STARTERS_ANNOUNCED_BY_LEAGUE: YES` · `OFFICIAL_BATTING_ORDERS: NOT_VERIFIED` · `SOURCE_GATE_BB-P2: BLOCKS_QUALIFIED_RANK1` · `KBO_TIE_THREE_WAY: MODELED` · `P_CARD_COHERENCE: PASS` · `RANK1_GATE: RANK1_UNSTABLE` · `UNDERDISPERSION_VS_ARCHIVE: FLAGGED` · `PERFORMANCE_ELIGIBILITY: NOT_CERTIFIED` · `SETTLEMENT: NOT_PERFORMED` · `CANONICAL_IMPORT: PENDING` · `GITHUB_WRITES: NO`.
<!-- END CARD P-572 -->
