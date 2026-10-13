<!-- BEGIN CARD P-579 -->
## Card · P-579 · BASKETBALL / Liga ACB · La Laguna Tenerife @ UCAM Murcia · 2026-10-11

- **Working ID:** `P-579 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`
- **Event key:** `ACB:2026-27:UCAM-LLT-20261011:2026-10-11`
- **Native event ID:** `NOT_VERIFIED` (official match center lists the dated pairing, but match ID unavailable)
- **Sport:** `Basketball`
- **League:** `Spain Liga ACB / Liga Endesa 2026–27, Round 3`
- **Tracking alias:** `LOCAL-20261011-P-579-ACB-LLT-UCM`
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO`
- **Timing state:** `LATE_START_UNVERIFIED`
- **Research completed:** `2026-10-11T21:31:23+11:00`
- **Scheduled start:** `2026-10-11T21:30:00+11:00` (12:30 CEST, venue-local; actual first jump NOT_VERIFIED)
- **Endpoint:** `Four 10-minute FIBA/ACB regulation quarters + every 5-minute overtime period until winner; all listed totals/handicaps include OT, score integer points, no half-point push; operator-specific action terms UNKNOWN_DEFINITION`
- **Distribution object:** `basketball_acb_shrunk_pace_joint_normal_ot_v1` — `1,000,000` seeded draws `20261011579`; game pace 75.3486, base team PPP Murcia 1.16230 and Tenerife 1.14793, home ±1.30 pts, Murcia Boum branch −0.70 pts, Tenerife availability −1.20 pts and travel −0.40 pts; regulation total/margin SDs 19.7/14.8 points, independent latent T/M normals, nearest-integer score rounding; tied-regulation scores played through Poisson(9.8) overtime per team repeatedly; no borrowed NBA profile
- **Expected score:** `points, full game incl. OT; SDs from terminal score simulation — UCAM Murcia 88.46 (SD 12.40) · La Laguna Tenerife 83.85 (SD 12.52) · combined 172.31 (SD 20.03) · margin Murcia − Tenerife +4.61 (SD 14.83)`
- **Regime flags:** `EARLY_SEASON` (two games per team; no ACB-specific recommended multiplier in BASE_RATES; estimated additional uncertainty in 19.7/14.8 widths, not fitted)
- **Retirement rule:** `N/A (basketball; player injury exit stays in team outcome)`
- **Listed-pitcher rule:** `N/A (basketball)`
- **Abandonment rule:** `FRAMEWORK_DEFAULT: postponed/cancelled/no league-recognised final = VOID; otherwise official terminal score governs; bookmaker terms unknown`
- **Settlement fields:** `Full-time final points, quarter scores, OT flag/OT scores, official five starters, minutes, inactive players (provider: acb.com exact-match box score; fallback FIBA LiveStats and independent structured scores)`
- **Capture due:** `2026-10-12T09:30:00+11:00`
- **Rules read:** `METHOD, CURRENT_RULES §§1-9, SELECTION_RULES §§1-6, RULES_BASKETBALL §§0,3,8, PROBABILITY_TOOLKIT §§1.2-1.3, BASE_RATES_REGISTER §§3,7.1 (NBA/WNBA/NBL ONLY, not applied as ACB scoring priors), LEAGUE_PROFILES Basketball (no ACB row), SOURCES §3.2 (ACB official site and live.acb.com), ARCHIVE_USE_GUIDE §§1-5, CARD_AND_LOG_TEMPLATES §§3,3a,4,7; GitHub main read only`
- **Archive check:** `ARCHIVE_UNAVAILABLE: Previous Sports Results/Basketball/Liga ACB/2024/2024_games.csv and /2025/2025_games.csv each hold only a one-line header, zero games; 2026/2026_games.csv NOT_FOUND. Team-2025/26 + two current-game official/source-linked stats substituted; league-wide 2026–27 archive NOT_USED.`
- **Evidence quotes:** `RTVC 2026-10-10 @ 2026-10-11T21:31:23+11:00 — "En la enfermería, el club confirma la baja de larga duración de Rokas Giedraitis"; RTVC — "Xabi López-Arostegui, por una contractura lumbar, y TJ Bamba, por un proceso gripal, son duda"; RTVC — "Souley Boum es duda por una sobrecarga"; UCAM official — "recibe este domingo (12:30 h)".`

### Decision block

**Distribution:** `basketball_acb_shrunk_pace_joint_normal_ot_v1` — pace 75.3486, combined matchup PPP 2.31024 before adjustments, home +1.3 / −1.3, availability Murcia −0.7 / Tenerife −1.2, travel Tenerife −0.4; total/margin normal (SD 19.7,14.8), linked terminal-score grid and simulated OT on regulation ties.

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED (replaces supplied 170.5 totals) | Combined total points **Under 197.5** — full game incl. OT | 89.66% | FROM_DISTRIBUTION:basketball_acb_shrunk_pace_joint_normal_ot_v1 | Early-season pooled matchup total around 172, conservative 20-point SD | Exceptional offence, explosive fourth quarter or OT produces 198+ |
| 2 | PICK | ANALYST_DERIVED (replaces supplied 170.5 totals) | Combined total points **Over 147.5** — full game incl. OT | 89.34% | FROM_DISTRIBUTION:basketball_acb_shrunk_pace_joint_normal_ot_v1 | Wide lower bracket spans current offence and typical ACB scoring | Low-efficiency game, Boum out, Tenerife reduced rotation, 147 or fewer |
| 3 | INFORMATIONAL | ANALYST_DERIVED (replaces Murcia −5.5) | UCAM Murcia **+13.5** point handicap — full game incl. OT | 88.91% | FROM_DISTRIBUTION:basketball_acb_shrunk_pace_joint_normal_ot_v1 | Home Murcia 62% favourite, substantial but unverified cushion | Tenerife wins by 14+ |
| 4 | INFORMATIONAL | ANALYST_DERIVED (replaces 170.5 total) | Combined total points **Over 148.5** — full game incl. OT | 88.39% | FROM_DISTRIBUTION:basketball_acb_shrunk_pace_joint_normal_ot_v1 | Near-duplicate, slightly narrower Over lower-tail threshold | 148 points or fewer |

**P(Rank 1 and Rank 2 both lose):** 0.0% by construction — Under 197.5 loses only on ≥198; Over 147.5 loses only on ≤147.
**Rank 1 − Rank 2 gap:** 0.32 percentage points.
**Rank-1 gate:** RANK1_UNSTABLE — p_card 89.66%; best non-complementary alternative 89.34%; margin 0.32 points (requires ≥4.00).
**Adjustment dependence:** NONE_BY_0.25_SD_THRESHOLD (home +1.3, Murcia availability −0.7, Tenerife availability −1.2 and fatigue −0.4 are each <0.25 SD; removing availability assumptions may reverse rank order within the top two).
**Supplied rows not selected:** Murcia −5.5 47.92%; Tenerife +5.5 52.08%; combined Over 170.5 53.44%; combined Under 170.5 46.56%.
**Potential winner:** UCAM Murcia — 62.19% (full game incl. OT); Tenerife 37.81%.

### Appendix

#### A1. Identity, timing and state
- Official UCAM team fixture Sunday Oct 11, 12:30 CEST, venue Palacio de Deportes Murcia = AEDT Oct 11 21:30; official acb.com lists UCM–LLT, round 3. Home UCAM, away Tenerife, both 1–1. Research completed 2026-10-11T21:31:23+11:00; scheduled jump not yet verified independently; research state `LATE_START_UNVERIFIED` (before schedule when issued: NO). No live or post-result in-game facts were read or used. If actual jump already occurred or starters change, issue A8 addendum without editing this card.
- Exact operator-specific spread/total settlement terms `UNKNOWN_DEFINITION`. Sources restricted to league/team reporting, historical stats and user-supplied contract thresholds; betting/odds and tipster predictions excluded.

#### A2. Supplied contracts (reference only, Rule P4)
- UCAM Murcia −5.5: 47.9154% (needs Murcia win by 6+); Tenerife +5.5: 52.0846% (Tenerife wins or loses by ≤5); sum = 100.0000%.
- Over 170.5: 53.4419%; Under 170.5: 46.5581%; sum = 100.0000%.

#### A3. Evidence summary
- **Model base:** 2025–26 ACB club-specific possession/PPP histories and each team's first two 2026–27 ACB games, with **75% prior +25% current-season** blend. League-wide ACB fitted profile is **NOT_AVAILABLE**; NBA/NBL/EuroLeague scoring SDs and OT rates are **not transferred**. Team-specific prior and uncertain normal widths are documented.
- **2026–27 input:** Murcia 177 for/178 against in two games; Tenerife 160 for/156 against. <https://www.ucamdeportes.com/ucamcb>; <https://rtvc.es/ucam-murcia-vs-la-laguna-tenerife-jornada-3-liga-endesa-11-octubre-2026/>.
- **Possessions (FGA − OREB + TOV + 0.44 × FTA, both sides averaged):** Murcia current 79.05 and 2025–26 77.49; Tenerife current 73.07 and 2025–26 72.73. Shrunk Murcia 77.881, Tenerife 72.816; projected game **75.3486 possessions**. Source numeric tables: <https://www.basketball-reference.com/international/teams/murcia/2027.html>, <https://www.basketball-reference.com/international/teams/canarias/2027.html>, 2025–26 analogous /2026.html pages. Prior data may include 2025–26 OT games, contributing slight exposure noise.
- **Shrunk per-100-possession offensive/defensive rates:** Murcia ORtg 116.603, DRtg 110.015; Tenerife ORtg 119.572, DRtg 115.855; based on 2025–26 (Murcia 3113 PF/2876 PA, Tenerife 3040 PF/2940 PA) and 2026–27 through round 2 (Murcia 177/178, Tenerife 160/156). Current opponent strength and schedule were not fully adjusted beyond blending two teams' offensive and defensive rates; `OPPONENT_ADJUSTMENT_PARTIAL`.
- **Rotation gates:** RTVC Oct 10 confirmed Rokas Giedraitis long-term OUT; Xabi López-Arostegui (lower back) and TJ Bamba (illness) QUESTIONABLE; Souley Boum (load) QUESTIONABLE after missing UCAM's Oct 7 European game; Howard Sant-Roos in adductor recovery. Official matchday starting fives and active roster not retrieved at cutoff. No starter-specific minutes budget verified. <https://rtvc.es/ucam-murcia-vs-la-laguna-tenerife-jornada-3-liga-endesa-11-octubre-2026/>.
- **Named current scorers (two-game sample):** Souley Boum 16.5 PPG, approx 21.5 min; Marcelinho Huertas 14.5 PPG and 5.0 APG; Jean-Marc Pansa roughly 10 RPG, Tim Abromaitis 8 RPG. These are exposure context, not confirmed starts or target props.
- **Context:** UCAM last league result beat Barça 100–94; Tenerife beat Unicaja 80–75; UCAM beat Varese 85–58 Oct 7 in the Champions League, Tenerife fell 77–89 to London Lions Oct 6 EuroCup; Tenerife's third away fixture in eight days supports limited travel/fatigue variance, not guaranteed lower pace. The prior Murcia–Tenerife meeting at this venue was 86–80 Apr 25 2026, context only.

#### A4. Event distribution (single-score-grid authority)
1. Source columns per team-season: `FG/FGA, FT/FTA, OREB, TOV, PTS, Opp equivalents`; possession estimate `FGA−OREB+TOV+0.44 FTA` / games, then average with opponent estimate. **Murcia 2025–26**: own FGA2298, ORB426, TO424, FTA766, 3113 PF; opp FGA2236, ORB412, TO445, FTA835, 2876 PA across 34 matches. **Tenerife 2025–26** own FGA2085, ORB303, TO360, FTA736, PF3040; opp FGA2090, ORB348, TO407, FTA752, PA2940, 34 games. **Murcia 2026–27 pregame**: own FGA142, ORB28, TO25, FTA45, PF177; opp FGA134, ORB24, TO21, FTA60, PA178 in 2 games. **Tenerife 2026–27**: own FGA135, ORB18, TO15, FTA29, PF160; opp FGA118, ORB19, TO34, FTA33, PA156, 2 games.
2. Shrink 2026–27 two-game pace and ORtg/DRtg **25% to current, 75% to 2025–26**. Venue/opponent pace = average 77.8813 and 72.8159 = **75.3486**. Murcia ORtg/DRtg per possession **1.16603 / 1.10015**; Tenerife **1.19572 / 1.15855**. Head-to-head opponent adjustment: Murcia base PPP=(Murcia OR+Tenerife DR)/2=**1.16229**; Tenerife base=(Tenerife OR+Murcia DR)/2=**1.14793**.
3. Base regulation Murcia **87.5770** pts; Tenerife **86.4953** pts. Home venue +1.30 Murcia and −1.30 Tenerife (zero net total, +2.6 margin; analyst), Boum unresolved minutes expected adjustment −0.70 Murcia (analyst, 50% low-minute/inactive possibility), Tenerife Giedraitis and other doubts combined −1.20 Tenerife (analyst); tight three-away-game travel −0.40 Tenerife (analyst). Regulation centres **88.1770 Murcia, 83.5953 Tenerife** (total 171.7722). These corrections are not fitted ACB effect sizes. Max absolute centre impact per adjustment 1.3, below 0.25 × SD14.8=3.70 margin, and 0.25 × SD19.7=4.925 total.
4. Simulate N=1,000,000 with seed `20261011579`: independent `T_reg ~ Normal(171.77225, 19.7)` and `M_reg=Murcia−Tenerife ~ Normal(4.58167,14.8)`; team points = round nearest integer (T±M)/2, clamp each to ≥0; regulation ties receive independent Poisson(9.8) OT scoring added per team until untied. Modelled OT share **2.5546%**, not imported from NBA/NBL and not verified against a genuine ACB season; this is a substantial model limitation. Terminal distribution: Murcia **88.458** (SD 12.405); Tenerife **83.849** (SD 12.515); total **172.307** (SD 20.027); margin **+4.608** (SD 14.831); score correlation **0.292**. All ranks, winner and supplied prices from this single terminal grid, no adjustments afterward.
5. Conditional sensitivity: **If Boum is confirmed available** and plays a meaningful share rather than the lower-minute branch, Murcia could score +0.7 to +1.5 beyond base; **if all Tenerife doubtful players appear**, Tenerife +1.2 and the travel −0.4 may diminish; without availability/travel adjustments regulation total rises +2.30 to approximately 174.07, shifting the 197.5 Under down and 147.5 Over up, likely reversing Rank 1–2; same picks remain top two, but their ordering is unstable. Retain sensitivity as qualitative unless rerunning the grid; not an updated issued forecast.

#### A5. Priced ladder (excerpt; all full game incl. OT)
| Proposition | p_card | Complement |
|---|---:|---:|
| Total Under 197.5 | 89.6559% | Over 197.5 10.3441% |
| Total Under 196.5 | 88.7022% | Over 196.5 11.2978% |
| Total Under 198.5 | 90.4924% | Over 198.5 9.5076% — exceeds 90% selection ceiling |
| Total Over 147.5 | 89.3386% | Under 147.5 10.6614% |
| Total Over 146.5 | 90.2579% | Under 146.5 9.7421% — exceeds 90% selection ceiling |
| Total Over 148.5 | 88.3921% | Under 148.5 11.6079% |
| Murcia +13.5 | 88.9096% | Tenerife −13.5 11.0904% |
| Total Over 148.5 | 88.3921% | Under 148.5 11.6079% |
| Murcia −5.5 | 47.9154% | Tenerife +5.5 52.0846% |
| Total Over 170.5 | 53.4419% | Under 170.5 46.5581% |

#### A6. Adjustments
| Name | Target | Size | SD units | Prior basis |
|---|---|---:|---:|---|
| Home venue Murcia | MUR score | +1.30 pts | +0.088 margin SD | analyst_judgement |
| Away venue Tenerife | TEN score | −1.30 pts | −0.088 margin SD | analyst_judgement |
| Boum unconfirmed minutes | MUR score | −0.70 pts | −0.047 margin SD | analyst_judgement |
| Giedraitis OUT and two Tenerife doubtful | TEN score | −1.20 pts | −0.081 margin SD | analyst_judgement |
| Tenerife 3rd away fixture / 8 days | TEN score | −0.40 pts | −0.027 margin SD | analyst_judgement |

**Adjustments:** five small judgement shifts; no single shift exceeds 0.25 total or margin SD; if all injury assumptions are removed, Rank 1/2 ordering could reverse. Original pair membership may stay the same; no formal adjustment-dependent 0.25 SD flag.

#### A7. Family checks and basketball controls
- Score distribution coherence: Murcia outright 62.1906%; Tenerife outright 37.8094%; sum 100.0000%. Murcia −5.5 47.9154% ≤ outright Murcia; Tenerife +5.5 52.0846% ≥ Tenerife outright 37.8094%. Complements for supplied two handicap rows and two totals sum 100%.
- Totals centre **pace × efficiency explicitly derived**: projected pace 75.3486 × (1.16229 + 1.14793) + home ±0 net −0.70 Murcia −1.20 Tenerife −0.40 travel = 171.7722 regulation, + modeled OT about 0.535 points => terminal total 172.307. Never hand-enter 170.5 target into the centre. One uncertain player shift at a time is width/mixture, not certainty.
- Three-point and shot allocation: Murcia hit 23/71 3PA (32.4%) in two games; Tenerife hit 23/55 (41.8%) and has 15 turnovers vs Murcia 25 through two. Opponent context and 2-game small samples shrink. Murcia OREB28 vs Tenerife18; short-run eFG and shooting variance are model-width drivers, no forced upward total shift. Team leaders/usage/minutes incomplete; any rotation-sensitive Rank 1 capped at provisional confidence.
- Rank 1 + Rank 2 are brackets: both fail probability 0% by construction, despite potential severe forecast error on either threshold; no claim this implies reliable edge or availability of both lines. Wide non-supplied thresholds require user-side availability confirmation. No +/-1.5 baseball family check applies. The plus-cushion basketball check: Murcia +13.5 cushion is far wider than the common +3.5 band, so no close-game inference is made; check P(Murcia outright)+P(loses by 1–13) = 88.9096% and compare outright 62.1906%.
- Rotation uncertainty: official starting fives NOT_PUBLISHED/NOT_RETRIEVED; no reliable ~20-minute player-by-player participation grid. Injuries from dated reporting only. Venue history/16 straight UCAM home league victories is descriptive and not a guarantee; older H2H personnel continuity low. ACB 2026-27 40-minute regulation + five-minute overtime, full score endpoint resolved.
- Regime: two ACB games each, so `EARLY_SEASON`; NBL-specific −8.5 early-season multiplier is **not applied** to Liga ACB. ACB total/margin SDs 19.7/14.8 are analyst-estimated and unvalidated; no league row. The correct status is `LEARNING_ONLY / NOT_CERTIFIED`.

#### A8. Sources and venue-local timing
1. UCAM official future fixture, match date 11 Oct 2026 12:30 CEST at Palacio de Deportes: <https://www.ucamdeportes.com/ucamcb/proximos-partidos> — accessed 2026-10-11T21:31:23+11:00 (21:xx AEDT / 12:xx CEST).
2. ACB official club team schedule and first two scores: <https://acb.com/es/liga/equipos/la-laguna-tenerife-28/partidos?categoria=played_matches&filtro=temporada>, <https://acb.com/es/liga/equipos/ucam-murcia-12> — accessed 2026-10-11T21:31:23+11:00.
3. RTVC Oct10 owner-attributed game preview and injuries <https://rtvc.es/ucam-murcia-vs-la-laguna-tenerife-jornada-3-liga-endesa-11-octubre-2026/> — accessed 2026-10-11T21:31:23+11:00; partial field-owner reporting, starter status unverified.
4. Murcia official match preview <https://www.ucamdeportes.com/ucamcb/noticias/el-ucam-murcia-busca-el-pleno-semanal-ante-la-laguna-tenerife> — accessed 2026-10-11T21:31:23+11:00; match stage, form, three-point tendencies, last H2H.
5. Source stats <https://www.basketball-reference.com/international/teams/murcia/2027.html>, <https://www.basketball-reference.com/international/teams/canarias/2027.html>, <https://www.basketball-reference.com/international/teams/murcia/2026.html>, <https://www.basketball-reference.com/international/teams/canarias/2026.html> — structured search previews accessible (direct site browser may block 403), the four team/opponent count tables were printed and used; historical current-date cutoff before Oct11. Independent lineage of game data not guaranteed.
6. GitHub `danisgreat/Sports-Research` main snapshot as at prior current-session reading, read-only. ACB archive: only headers for 2024/2025; 2026 missing. Verification receipt at 2026-10-11T21:31:23+11:00.

#### A9. Integrity and custody
`SPORTS_ONLY_MARKET_BLIND: PASS` · `OBSERVED_IN_GAME_OUTCOME_USED: NO` · `SETTLEMENT: NOT_PERFORMED` · `ACB_OWN_LEAGUE_PROFILE: NOT_AVAILABLE` · `STARTERS_NOT_CONFIRMED` · `SOURCE_STATUS: EARLY_PREGAME_PROJECTION` · `RANK1_UNSTABLE` · `CANONICAL_IMPORT: PENDING` · `TIMING_STATE: LATE_START_UNVERIFIED`.
<!-- END CARD P-579 -->
