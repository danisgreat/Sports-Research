<!-- BEGIN CANONICAL RESEARCH P-618 -->
## P-618 — BASEBALL / KBO semi-playoff Game 3 · KIA Tigers @ LG Twins · 2026-10-20
Import: 2026-10-21T01:07:13+11:00; prompt 4 NEW_CANONICAL_EVENT. Local event key `LOCAL-20261018Q7N4T9B2-G0004` → canonical **P-618**; native identity KBO gameId 20261020HTLG0. Source mini `20261018Q7N4T9B2`, frozen source SHA-256 `89146dbb66e2e49206a92bad4e049bd3d27b701b055f42d8403e259cae8dc85d` (172,799 bytes). Card core SHA-256 `09ffa77ae2533f196c165ed372a5b17b3204df6e9150b5fd0e1f18f23bca9bed` (38,730 bytes) = the exact bytes between the local BEGIN/END CARD marker lines (source offsets 130665–169395); markers and headings outside them remain in the preserved source. Original method, probabilities, ranks, statuses, timing and gaps are literal; any NOT_ASSIGNED / PENDING wording inside the core is historical. Import is not a forecast timestamp and confers no certification.

# Card · LOCAL-20261018Q7N4T9B2-G0004 · BASEBALL · KIA Tigers @ LG Twins · KBO 2026 Semi-playoff Game 3 · 2026-10-20

**Authority:** `PUBLISHED_MAIN_PINNED` at `3e29a58693e2ed02ff862e9bf0f751af2feadee1`; MDS/P `v22.2` / CR `2026.10.17-R6` / SEL `2026.10.12-v3`; `research/prompts/1_GAME_CARD.md` + `research/prompts/1_sports/BASEBALL.md` and current baseball rules. **Status:** `READ_ONLY_DRAFT / NOT_ISSUED / OWNER_SAVE_PENDING / INFORMATION_INCOMPLETE`. **Canonical:** `NOT_ASSIGNED / PROMPT_4_IMPORT`; **local ordinal:** G0004 is *proposed*, not an authorised allocation; last observed previous mini's nominated writer lease expired 2026-10-19, and no owner handover/renewal or concurrent mini reconciliation has been verified. **SPORTS_ONLY / MARKET_BLIND / ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY.** No retrospective, settlement, GitHub write, ML/RL run, market/odds research or target game outcome used. All figures below are independent illustrative analyst estimates, not calibrated probabilities.

## Original owner request — preserved

> Upcoming Baseball Game: KIA Tigers @ LG Twins, Korea KBO,
> Estimated Game Time Start: 20 October 2026, 8:30 PM AEDT (can be delayed so continue the process as normal)
>
> Do comprehensive and accurate research, based on the instructions in the documents/drive. Provide the best 4 picks in order from most likely to least likely, for players and/or teams or anything else and pick your own picks, making the decision based on all the instructions and information provided in the documents. Provide accurate and detailed reasoning, based on the research and instructions. Always seek to find the latest starting and available players and players on the injury list or rested, and factor that into calculations. Refer to the GitHub main branch repo and associated documents.
>
> Tigers ML
> Twins ML
> Combined Total: Over 9.5 Runs
> Combined Total: Under 9.5 Runs
>
> Add a potential game winner as well, and make no mistakes, no hallucinations, and, importantly, be honest and accurate. Don't do a retrospective yet. Add all sources of information.
> Accuracy, source quality, transparency, and compliance with the GitHub methodology on the main branch, and take accuracy over speed. if your analysis goes beyond the start time, I would rather you take a long time than rush it and be wrong, so take as long as you need, this is strict instructions. if your analysis goes beyond the start time. @GitHub

## A1. Identity, authority and time

| Field | Evidence / state |
|---|---|
| League / stage | 2026 KBO postseason, 준플레이오프 / semi-playoff, best-of-five **Game 3**, not regular season or Korean Series |
| Sides | Away KIA Tigers, home LG Twins; exact orientation important for last-bat/home and walk-off |
| Venue | Seoul Jamsil Baseball Stadium, Republic of Korea; outdoors |
| Scheduled time | Tuesday 2026-10-20, **18:30 KST (UTC+09:00)** = **20:30 AEDT (UTC+11:00)** = **09:30 UTC** |
| Official fixture/source | https://eng.koreabaseball.com/Schedule/DailySchedule.aspx ; https://www.koreabaseball.com/Schedule/Schedule.aspx?date=202610 ; https://www.tving.com/sports/kbo |
| Official game number | Semi-PO G3, 20 October, Jamsil; database-native gameId NOT_RETRIEVED; distinguish 17/18 October G1/G2 and Oct 3–5 regular-season matches |
| Series entering game | KIA up 2–0: Game 1 2026-10-17, LG 1–5 KIA; Game 2 2026-10-18, LG 3–6 KIA, confirmed at official KBO English schedule |
| Timing | User local time at request approx 20:24 AEDT; official scheduled first pitch 20:30 AEDT; hand research continued after scheduled start. **READ_ONLY_DRAFT / POST_SCHEDULED_START_ASSEMBLY**; actual first pitch/uninterrupted first-availability for every source NOT VERIFIED; no claim of pre-start-issued prediction |
| Outcome exposure | The target's score or subsequent events were not used for the analysis; a KBO scoreboard search exhibited a pregame/top-first-inning 0–0 placeholder without a completed state; exclude its state/score entirely from features |
| Duplicate check | Prior available local G0001 Nagoya–Okayama, G0002 TNT–Converge, G0003 Osasuna–Racing are different events. Existing historical P-533 KIA @ LG (Oct 3, regular season) is **not** Oct 20 semi-playoff G3. Private minis not verifiable. |
| Source hierarchy | KBO official field-owner → original reported manager batting orders / Yonhap, Newsis, News1 → independently maintained Yagoonara dated team log; lineage overlap is flagged |
| Read receipt | Published `main` SHA printed above; source controls inspected: BASEBALL sport file §§1–7, prompt 1 core, current rule head, RULES_BASEBALL live §0, SELECTION_RULES §§1–5, league-profile admission, probability toolkit §3, baseline and historical/availability/research-completion protocols; previous 718-line active document opened, footer and three local records read. No unverified local controls applied. |

### Official 2026 postseason endpoint — decisive contract distinction

KBO's 7 October 2026 official postseason release https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=12183 confirms **maximum 15 innings** and **a draw if still level after the 15th**. A drawn semi-playoff game is replayed after the series' nominal final scheduled game; there is no default MLB automatic runner. Official rules also describe suspended games and no ordinary rain-called result. Hence an ML proposition with unspecified operator settlement **cannot be certified as a two-way no-draw market**. Scenarios below assume *if draw then void* **only for conditional W/(W+L)**; a three-way ML, draw-as-loss, listed-pitcher, minimum-innings or suspended-game rule is **UNKNOWN_DEFINITION**. The O/U 9.5 endpoint is provisionally full-game scored runs including permitted extras, with suspended/void terms unknown. No extra-inning mass was empirically fitted.

## A2. Decision block and supplied-contract assessment

**Family universe frozen before pricing:** *Only* four supplied rows, using full-game KBO 15-inning-cap outcome (including extras, subject to missing operator action rules); no invented alternate ladder, pitcher/prop market, price, or operator definition. Two complementary pairs: KIA ML/LG ML on decisive outcomes; Over/Under 9.5 runs on the same full-game total.

| Rank | Exact owner contract | p_card / assessment | p_base | Probability status | Supporting / opposing evidence |
|---:|---|---:|---:|---|---|
| 1 | **Combined Total: Under 9.5 Runs** | **0.556** | 0.557 | CONDITIONAL SPORTING APPROX; `ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY` | Both teams' latest 20 games are lower scoring than season aggregate, two previous semi-PO games total 6 and 9; opposing: LG/KIA lineup power, Shirakawa uncertainty, extra-inning tail, 2026 league total 10.14 |
| 2 | **Tigers ML** | **0.533** of games decisive under tie-void action | 0.533 | CONDITIONAL ML ONLY; action `UNKNOWN_DEFINITION` | KIA league run differential, stronger L20, 2–0 semi-PO lead; opposing: LG home last bat, Carrasco's better ERA/WHIP, Shirakawa poor LG split, possible LG lefty/righty attack |
| 3 | **Twins ML** | **0.467** of games decisive under tie-void action | 0.467 | CONDITIONAL ML ONLY; action `UNKNOWN_DEFINITION` | Carrasco at home, return of Moon Sung-ju to posted XI, Jamsil advantage; opposing: LG low recent offense, KIA's left-handed lineup vs Carrasco, KIA run prevention |
| 4 | **Combined Total: Over 9.5 Runs** | **0.444** | 0.443 | CONDITIONAL SPORTING APPROX; `ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY` | 2026 KBO regular-season mean 10.14, KIA power/lefty matchup, Shirakawa 4.75 ERA; opposing: recent 20-game rates, postseason bullpen usage, possible low-run tails |

**Potential winner:** **KIA Tigers** by a narrow *conditional* decisive-game estimate of **53.3%** versus LG **46.7%**. This is not P(KIA wins unconditionally), as unmodelled 15-inning draw mass must be reported rather than made up. No numeric operator-verified moneyline is available; its unknown action term is an unresolved gate. **Illustrative score centre:** KIA around 4.9–5.0, LG around 4.5–4.6, total around 9.5. This is not a verified exact score or calibrated distribution.

**Formal qualification:** Rank 1 p 0.556 < provisional 0.62 requirement; best non-complementary alternative KIA ML p 0.533, lead 0.023 < 0.04. **GATE FAIL / NOT_CERTIFIED**, additionally held for `UNKNOWN_DEFINITION`, incomplete independent historical corroboration, no fitted KBO postseason dispersion, unverified full bench and no current venue weather capture. Rank 2 p 0.533 < 0.58 floor. Rank 3 is the conditional complement of Rank 2, Rank 4 complement of Rank 1. **These are ranked descriptions, not four non-contradictory picks.** Expected monetary value NOT COMPUTED: no supplied accepted price and sportsbook/odds data excluded by SPORTS_ONLY.

## A3. Online historical results and player evidence (known before 20 October)

**Full-season official anchor:** KBO final 2026 table as of the completed 144 regular games, https://eng.koreabaseball.com/Standings/TeamStandings.aspx, corroborated by https://m.koreabaseball.com/ at 00:00 KST Oct 20. KIA 79–63–2, RF 769, RA 664, AVG .271, ERA 4.27; LG 78–65–1, RF 723, RA 726, AVG .264, ERA 4.81. KIA RF/G=769/144=5.340, RA/G=664/144=4.611; LG RF/G=723/144=5.021, RA/G=726/144=5.042. **Source age:** final regular season; no postseason games mixed into season denominator.

**Historical table method:** latest 20 eligible *completed* matches including postseason Games 1–2, newest first, from the dated https://www.yagoonara.com/teams/2/gamelog and https://www.yagoonara.com/teams/4/gamelog with October independently checked against KBO https://eng.koreabaseball.com/Schedule/DailySchedule.aspx and individual match reports; September selections partially verified against 2026 September KBO match centre reports https://www.koreabaseball.com/Schedule/Schedule.aspx?date=202609. Yagoonara has a **conflicting overall game-count/record aggregate** relative to official 144; reject its season total, use only dated individual rows checked where independent evidence exists. Detailed independent corroboration of **all** 40 dated rows, all available-at timestamps, postponed/extra-inning tagging and every source collection chain **OPEN**, so HISTORY_INCOMPLETE rather than claiming fully corroborated n=20. W/L and regulation/extras endpoint per row not always independently closed. No unreviewed prior-result folder.

### KIA Tigers — latest 20 games; runs KIA–opponent (newest first)

| Date 2026 | Opponent | Location | Final score KIA–opponent | Status / source note |
|---|---|---|---:|---|
| Oct 18 | LG | Home Gwangju | 6–3 | Semi-PO G2, official KBO |
| Oct 17 | LG | Home Gwangju | 5–1 | Semi-PO G1, official KBO |
| Oct 12 | LG | Home Gwangju | 4–2 | Regular, Yagoonara + official |
| Oct 11 | Lotte | Home Gwangju | 1–4 | Regular |
| Oct 10 | SSG | Home Gwangju | 8–5 | Regular |
| Oct 09 | NC | Away Changwon | 7–2 | Regular |
| Oct 07 | Lotte | Away Sajik | 12–4 | Regular |
| Oct 06 | Samsung | Home Gwangju | 4–5 | Regular |
| Oct 05 | LG | Away Jamsil | 6–4 | Regular |
| Oct 04 | LG | Away Jamsil | 6–5 | Regular |
| Oct 03 | LG | Away Jamsil | 5–4 | Regular |
| Oct 01 | KT | Home Gwangju | 5–7 | Regular |
| Sep 30 | KT | Home Gwangju | 2–3 | Regular |
| Sep 29 | KT | Home Gwangju | 5–8 | Regular |
| Sep 26 | LG | Home Gwangju | 5–1 | Regular |
| Sep 23 | Doosan | Away Jamsil | 2–3 | Regular |
| Sep 20 | NC | Away Changwon | 8–6 | Regular |
| Sep 19 | NC | Away Changwon | 5–1 | Regular |
| Sep 17 | Kiwoom | Home Gwangju | 2–0 | Regular |
| Sep 15 | SSG | Away Munhak | 3–6 | Regular |

**KIA derived overlapping windows:** L5 n=5 RF 24/5 **4.80**, RA 15/5 **3.00**; L10 n=10 RF 59/10 **5.90**, RA 35/10 **3.50**; L15 n=15 RF 81/15 **5.40**, RA 58/15 **3.87**; L20 n=20 RF 101/20 **5.05**, RA 74/20 **3.70**. Every window includes latest games, overlap counted once. All 20 in current season; 2 postseason games segregated by flag. Dates Sep 15–Oct 18. Sourced rows are observed but row-level second-lineage closure incomplete.

### LG Twins — latest 20 games; runs LG–opponent (newest first)

| Date 2026 | Opponent | Location | Final score LG–opponent | Status / source note |
|---|---|---|---:|---|
| Oct 18 | KIA | Away Gwangju | 3–6 | Semi-PO G2, official KBO |
| Oct 17 | KIA | Away Gwangju | 1–5 | Semi-PO G1, official KBO |
| Oct 14 | Doosan | Home Jamsil | 4–1 | Wild Card, official KBO |
| Oct 12 | KIA | Away Gwangju | 2–4 | Regular |
| Oct 10 | Lotte | Away Sajik | 4–3 | Regular |
| Oct 09 | Lotte | Away Sajik | 1–9 | Regular |
| Oct 07 | Doosan | Home Jamsil | 7–5 | Regular |
| Oct 06 | NC | Home Jamsil | 6–1 | Regular |
| Oct 05 | KIA | Home Jamsil | 4–6 | Regular |
| Oct 04 | KIA | Home Jamsil | 5–6 | Regular |
| Oct 03 | KIA | Home Jamsil | 4–5 | Regular |
| Oct 01 | SSG | Away Munhak | 5–6 | Regular |
| Sep 30 | SSG | Away Munhak | 3–4 | Regular |
| Sep 29 | SSG | Away Munhak | 1–7 | Regular |
| Sep 26 | KIA | Away Gwangju | 1–5 | Regular |
| Sep 24 | Lotte | Home Jamsil | 4–6 | Regular |
| Sep 20 | Hanwha | Home Jamsil | 4–3 | Regular |
| Sep 19 | Hanwha | Home Jamsil | 2–1 | Regular |
| Sep 18 | KT | Away Suwon | 12–1 | Regular |
| Sep 16 | NC | Away Changwon | 9–2 | Regular |

**LG derived overlapping windows:** L5 n=5 RF 14/5 **2.80**, RA 19/5 **3.80**; L10 n=10 RF 37/10 **3.70**, RA 46/10 **4.60**; L15 n=15 RF 51/15 **3.40**, RA 73/15 **4.87**; L20 n=20 RF 82/20 **4.10**, RA 86/20 **4.30**. All 20 in current season, with 1 Wild Card + 2 semi-PO, segregated. Dates Sep 16–Oct 18. Not independent league-average observations: multiple repeated KIA–LG games; KIA/LG form windows highly dependent. League strength-of-schedule correction NOT DERIVED (missing verified opponent contemporaneous ratings per historical row). Independent source row closure incomplete.

**Recent-form policy:** The four windows overlap and are **one** piece of evidence; only low-weight shrinkage of L20 influences the scenario centre, never a separately counted L5/L10/L15 trend adjustment. Season-average weakness of LG after KIA matchups may reflect opponent rather than sustainable own form. Published secondary site aggregate and full dates differ, so official season rates override the provider's cumulative season counts.

## A4. Current players, lineups, injuries and workload

### Announced Game 3 starting pitchers

| Team | Official starter | 2026 season | Admissible pregame availability/status |
|---|---|---|---|
| KIA | Keisho Shirakawa (right-handed) | 4–5, ERA **4.75**, IP **83⅓**, 69 K, WHIP **1.38** | KBO/TVING announced starter; sample includes reported 2 starts vs LG, 0–1, ERA 7.74; do not extrapolate from split |
| LG | Carlos Carrasco (right-handed) | 6–3, ERA **4.05**, IP **60**, 50 K, WHIP **1.03** | KBO/TVING announced starter; Oct 14 Wild Card vs Doosan 6 IP/1 ER; reported one prior KIA matchup 4⅓ IP, 4 ER; unverified game-day workload ceiling |

Sources: KBO's own 20 Oct Game 3 preview https://www.koreabaseball.com/MediaNews/News/Preview/View.aspx?bdSe=62578 ; TVING https://www.tving.com/sports/kbo ; original reporter 19 Oct https://www.news1.kr/sports/baseball/6324044 ; https://www.yagoonara.com/schedule/128564 . Season ERA and opponent splits cross-checked in KBO preview and Yagoonara but independent scoring collector lineage is uncertain.

### Announced batting orders, 20 October pregame (lineups published before scheduled first pitch)

| Slot | KIA Tigers, position | LG Twins, position |
|---:|---|---|
| 1 | Park Jeong-woo, CF (박정우) | Park Hae-min, CF (박해민) |
| 2 | Park Jae-hyeon, LF (박재현) | Oh Ji-hwan, SS (오지환) |
| 3 | Kim Do-yeong, 3B (김도영) | Austin Dean, DH (오스틴 딘) |
| 4 | Harold Castro, 1B (해럴드 카스트로) | Song Chan-eui, LF (송찬의) |
| 5 | Na Sung-bum, RF (나성범) | Moon Bo-gyeong, 3B (문보경) |
| 6 | Kim Sun-bin, DH (김선빈) | Moon Jeong-bin, 1B (문정빈) |
| 7 | Han Jun-su, C (한준수) | Moon Sung-ju, RF (문성주) |
| 8 | Kim Gyu-seong, 2B (김규성) | Park Dong-won, C (박동원) |
| 9 | Ha Ju-seok, SS (하주석) | Koo Bon-hyeok, 2B (구본혁) |

KIA lineup independently corroborated by Yonhap timestamped 17:36 KST https://www.yna.co.kr/view/AKR20261020155400007, Newsis https://mobile.newsis.com/view/NISX20261020_0003833884 and News1 https://www.news1.kr/sports/baseball/6326360 . LG lineup independently corroborated by Newsis https://www.newsis.com/view/NISX20261020_0003833694 , Chosun Sports https://www.sportschosun.com/baseball/2026-10-20/202610200100127350008264 and ISPlus https://isplus.com/article/view/isp202610200145 (16:13 KST). These are *manager-reported announced orders*, not a verified first-pitch plate-appearance participation log; the KBO exact official published batting-order page and bench list were not recovered.

**KIA match-specific player status:** Kim Do-yeong had been struck on the forearm in Game 2 but manager Lee Bum-ho reported no lingering issue and placed him 3rd in the announced lineup (Yonhap pregame 17:36 KST, not post-event proof). Manager deployed **seven left-handed hitters** to target Carrasco: reported 2026 allowed batting average to lefties **.267**, righties **.185** (Newsis Oct 20). Kim Ho-ryeong, who started Game 2, is not a Game 3 starter; manager explicitly identified him and Kim Tae-gun as bench/pinch-hitting options. KIA named Lee Eui-ri, Jeong Hae-yeong and Kim Tae-hyeong among potential pitching contingencies; those plans are conditional, NOT official inning-confirmed availability. Closer Jeon Sang-hyeon recorded saves in both Oct 17 and 18 games and had Oct 19 rest day; exact pitch counts/current readiness NOT_RETRIEVED. Sources KBO/Yonhap/Newsis + game results.

**LG match-specific player status:** Moon Sung-ju starts for the first time this postseason after an injury-affected 2026; contemporaneous report lists 76 seasonal appearances, AVG .284, HR1, RBI21, OPS .693 (https://www.mt.co.kr/sports/2026/10/20/202610201531770170O). Hong Chang-ki and Lee Jae-won are **not in the Game 3 starting nine**, due to performance-based team selection; this is not proof of new medical absence. Oh Ji-hwan elevated to second, Song Chan-eui fourth, Moon Jeong-bin sixth. Manager discussed potential Carrasco→John Kennedy→Son Ju-young chain, but exact active-pitcher bench eligibility and pitch counts NOT independently retrieved. Sources LG manager local news https://www.news1.kr/sports/baseball/6326175 and https://www.yna.co.kr/view/AKR20261020141000007 .

**Roster completeness:** Both *announced* starting nine + both named starters are VERIFIED BY MULTIPLE PRESS SOURCES. Full official 28-person activated list (KBO playoff 30 registered, 28 active) / bench / unavailable illness/medical/discipline list / bullpen game-day readiness NOT FULLY VERIFIED, so `BENCH_PARTIAL / INJURIES_UNKNOWN_NOT_NONE`. Substitutions or last-minute scratches NOT independently checked in exact match centre at first pitch. No claim that omitted hitters are injured. Availability evidence times are publication times, *not* the actual lineups' first public availability.

## A5. Distribution, odds-free price arithmetic, sensitivities, departures

**League anchor, exact competition:** Full 2026 KBO regular season final official team table. Team runs sum: 825+806+821+679+769+719+688+723+706+565 = **7301**. Across 10 × 144 / 2 = **720 games**, mean **10.140 runs/game** (regular-season mixed stadiums/tie/extras). This is an independently evidenced exact-league rate, **not** a fitted 2026 KBO postseason total distribution; NO KBO postseason total SD/park coefficient available. The retired source-derived `LEAGUE_PROFILES` values are NOT ADMITTED under LP-v4. No MLB run rate is transferred to KBO.

**Season+L20 shrinkage:** Declared analyst k=60 season-equivalent games in denominator for an L20 weight 20/(20+60)=0.25, season weight .75; k **analyst scenario assumption**, not KBO-fitted. KIA RF/G .75(5.340)+.25(5.050)=**5.268**; KIA RA/G .75(4.611)+.25(3.700)=**4.383**. LG RF/G .75(5.021)+.25(4.100)=**4.791**; LG RA/G .75(5.042)+.25(4.300)=**4.857**. Opponent-adjusted *raw* pair using arithmetic scoring/conceding average: KIA (5.268+4.857)/2=**5.063**, LG (4.791+4.383)/2=**4.587**; raw total **9.650**, raw KIA margin **+0.476**. This is a transparent run-rate heuristic, not a possession/ERA or independently fitted generalized-linear model.

**Mechanism departure ledger (all scenarios, not data-fitted coefficients):** Jamsil's outdoor venue and unknown current weather could depress/increase run carry; no verified numeric 2026 Jamsil park factor, so do not assert a source-backed −X runs. Carrasco ERA 4.05 vs LG season 4.81 supports better run prevention, while 7 KIA LH batters with .267/.185 split offsets some of it; Shirakawa 4.75 vs KIA team 4.27 supports LG opportunity but poor 2-game LG split is too noisy to treat literally. Pen usage and 15-inning tail remain width and scenario effects without named numeric fitted coefficients. Home last-at-bat provides LG structural protection (late walk-off), but no sourced 2026 KBO exact-park home advantage coefficient. **No separate last-five adjustment**, no "due"/momentum or extrapolation of series 2–0 as a 2-run skill edge.

**Predeclared primary 25/50/25 low/base/high sporting scenarios** (all **illustrative assumptions**, not an admitted fitted KBO joint score model):

| Case | Weight | E(total runs), including possible extras | E(KIA margin) | Interpreted circumstance |
|---|---:|---:|---:|---|
| Low | .25 | **8.8** | **−0.30** | Carrasco lasts longer, LG home defence, suppressed early scoring |
| Base | .50 | **9.5** | **+0.40** | Balanced SP/bullpen, KIA recent run prevention partly persistent |
| High | .25 | **10.2** | **+1.10** | KIA platoon pressure/bullpen contribution outweighs starter uncertainty; longer upper-run tail |

Combined centres: E(T)=.25×8.8+.50×9.5+.25×10.2=**9.50**; E(M_KIA)=.25×(−.3)+.5×.4+.25×1.1=**+0.400**. E(KIA)=(9.5+.4)/2=**4.95**; E(LG)=(9.5−.4)/2=**4.55**. **Width assumptions:** σ(total)=**5.0 runs** using PROBABILITY_TOOLKIT §3 negative-binomial lookup approximation *as a shape only*, not KBO-calibrated; σ(margin)=**4.8 runs** using toolkit §1 normal Φ approximation *as a shape only*. Means in 0.25 steps linearly interpolated for totals. Team-run SDs and Cov(KIA,LG) **NOT_COMPUTED**: without a fitted joint environment/innings/last-bat score grid they cannot be honestly inferred from independent σ(T)/σ(M) guesses. Case variance contributes further uncertainty; no exact joint score distribution or simulation was executed. True skew, capped tie/extras and stop-when-home-wins can alter values.

**Total O/U 9.5 — reproducible hand calculation:** From toolkit SD=5.0 negative-binomial table at 9.5 line: P(O9.5 | μ=8.75)=.381, at 9=.401; μ=8.80 gives .381+(.05/.25)(.401−.381)=**.385**. At μ=9.50 P(O)=**.443**. At μ=10 P(O)=.487, μ=10.25 P(O)=.509; at μ=10.20 P(O)=.487+(.20/.25)(.509−.487)=**.5046**. Mixture O = .25×.385+.50×.443+.25×.5046 = **.4444**. Under = **1−.4444=.5556**. The line is half-run, so no total push in a normally completed scored game. `p_base(O)=.443`, `p_base(U)=.557`. Numerical table interpolation ε approximately .003 (a stated approximation, excludes model uncertainty); model uncertainty far exceeds ε.

**Decisive winner / ML arithmetic, conditional on no official 15-inning draw:** Signed KIA margin M normal approximation by scenario with σ=4.8 and means −0.30, +0.40, +1.10. Toolkit Φ: z=−.0625, .0833, .2292 → Φ(z) ≈ **.475, .533, .591**. Mixture P(KIA | game decisive) = .25×.475+.50×.533+.25×.591 = **.5330**; LG =1−.5330=**.4670**. `p_base=.533/.467`; ε≈.003. These are *conditional* price approximations that ignore the detailed last-bat/15-inning tie kernel; **P(draw in 15 innings)=NOT_ESTIMATED**. Unconditional W/P/L/V cannot be filled faithfully without P(draw) and the unspecified operator action. **Contract-definition gate open**; no false assert that P(KIA win)=.533 of all fixtures. Sensitivities: KIA decisive p .475–.591, LG .409–.525; Under U .615–.495, Over .385–.505 in low-to-high cases. Total centre vs line: line 9.5−μ 0 runs; signed margin z base .0833. Core 2026 League mean 10.14 is higher than scenario mean 9.50 by .64; fully attributed to recent lower-scoring L20/shrinkage, exact starter/venue differences and *assumed* postseason state, **not** a source-calibrated venue coefficient.

**Baseline and ranking controls:** `BASELINE_LEAGUE_V1` exact 2026 KBO, postseason semi-playoff, full game incl 15-inning tie/possible extras, same moneyline action and total line: **NOT_ESTIMATED** because an independently assembled complete same-era postseason distribution, tie convention and variance/total frequencies are absent. Observed league-only mean10.14 is *not* enough to fabricate p_baseleague. `TEAM_BASELINE_P`: NOT_COVERED for KBO. Original rank1 gate: p=.5556 < .62 and gap vs best non-complementary KIA conditional=.0226 < .04 → **FAIL / unqualified**; Rank2 floor p=.533 < .58 → FAIL. Gate retains conditional-v-unconditional comparability caveat; it cannot be formally scored without ML operator action. `SHADOW_GATE_RET03`: KIA ML=.533 non-complementary; same failure. `SHADOW_R2_RET04`: NONE at p≥.58; `SHADOW_R2_XCARD6`: NONE; `SHADOW_RANK_DELTA`: NONE (baseline missing); `SHADOW_BASE_ONLY`: same four approximate ranks. **Dependent risk:** Under and KIA ML share game states; no fitted joint score grid, so exact joint failure unavailable. If loss probabilities l_U=.4444 and l_KIA=.4670 *conditional on decisive*, provisional Frechet bound [max(0,.4444+.467−1), min(.4444,.467)] = **[0,.4444]** on a common decisive conditional space; this is not an exact unconditional joint because of unresolved tie mass. Never multiply these losses or claim mechanically protected.

**Contested assumptions requiring caution:** Scenario σ(total)=5.0 and σ(margin)=4.8, k=60 and low/base/high centres are analyst inputs, not statistically estimated. Small shifts of ±1 run move Under9.5 across ~50%; momentum/historic H2H cannot justify >62% forecast. No verified 2026 Jamsil park-specific total SD or current wind. Shut-off/suspended-game action and true postseason inning kernel may shift totals; not priced exactly.

## A6. Venue, environment, strategy and rules

- **Exact venue:** Jamsil, LG bats last, and cannot need the bottom ninth if ahead after KIA's ninth; walk-off and extra-inning score distributions are not the same as a neutral park. Home advantage is a mechanism, *not a calibrated numerical estimate*.
- **Series state:** KIA 2–0 best of five. LG must win to continue. KIA manager said he would consider quick removal of Shirakawa if innings 1–2 show problems and indicated possible relief appearances by Lee Eui-ri, Jeong Hae-yeong, Kim Tae-hyeong. The LG plan for Carrasco followed by relief arm(s) is reported but exact available bench and pitch limits incomplete. These alter tail/transition risks; exact branch masses UNKNOWN.
- **Rules:** postseason innings 1–9 standard; innings 10–15 max; tied after 15 recorded draw and played again later in series; no regulation-only assumption. Official series requires an eventual winner, but **Game 3** can itself end tied. 2026 KBO postseason disallows normal no-game/rain-called dispositions; suspended-game rule applies. The user's moneyline action on suspended/drawn match remains `UNKNOWN_DEFINITION`.
- **Weather:** no venue-specific 18:30 KST temperature/wind/rain forecast with source timestamp was reliably obtained; `WEATHER_NOT_RETRIEVED`, no directional scoring adjustment claimed.
- **Prohibited signals:** no betting odds, tips, market-implied p, market lines other than owner-supplied contracts, live event data or outcome exposure used. 20 October target game not inspected for scoring after request.

## A7. Issuance/custody and risk register

| Field | State / effect / next evidence |
|---|---|
| 2026 exact postseason park/total count distribution | OPEN: KBO game-level cohort with stage/period/ext identity, weather/venue; missing fitted same-line comparator, affects numeric precision |
| Starter pitch limit and immediate-relief branching | OPEN: official manager/club active-player statements, pitch logs and last-3 days bullpen innings; may shift centre and tail |
| Official game-day 28-player active bench / last-minute scratches | OPEN: KBO exact fixture's complete announced roster and timestamp; media nine corroborated, substitutes not fully verified |
| KIA Kim Do-yeong condition | Manager said fine and starts 3rd; no follow-up medical certificate needed to say *starter*, but long-term 100% fitness unproven |
| LG Moon Sung-ju | Announced starter, had injury-affected season; any innings/minutes cap unverified |
| Match status/first pitch | Scheduled 18:30 KST verified; draft assembly after; actual first pitch not used/verified; claim `POST_SCHEDULED_START` and `KNOWN_AT_PARTIAL` |
| KBO exact gameId/native match identity | Open but unique by stage/date/venue/opponents; do not join to regular season P-533 |
| Contract ML action & innings for totals | Open operator-specific draw/void/minimum-game/suspended/extra endpoints; do not interpret two-way ML as unconditional 100% |
| Outcome / settlement | PENDING_EVENT; NO retrospective, NO settlement, do not backfill final result |
| Mini custody and ordinal | Most recently accessible mini says last `G0003`, next proposed `G0004`. 2026-10-18 nominated lease expired 2026-10-19; owner save and subsequent writers not verified. G0004 research is a **standalone read-only draft only**, not a written authorised event |
| No current market quote | `EV_MONETARY_NOT_ESTIMATED`; no odds searched (SPORTS_ONLY) |

## A8. Evidence-source register and field-level attempted corroboration

| Source (URL) | Fields actually used | Publication / collection / known-at limitation |
|---|---|---|
| https://www.koreabaseball.com/Schedule/Schedule.aspx?date=202610 | Official exact fixture date/time/venue/stage and previous semi-PO G1; site temporarily displayed G2 0–0 while contemporaneous English schedule already final; do not treat stale 0–0 as G2 final | Official live page asynchronously cached; cross-check completed Oct18 via English site |
| https://eng.koreabaseball.com/Schedule/DailySchedule.aspx | Official Oct17 5–1 and Oct18 6–3 finals; Oct20 semi-playoff G3 identity | Site can expose 2-month-old cache; cited extract is the 2026 October version, do not blindly reuse older cached version |
| https://www.tving.com/sports/kbo | G3 18:30 and verified named Shirakawa/Carrasco starters | TVING had published pregame team matchup on 20 Oct around 12:40 KST; data-feed independence vs KBO uncertain |
| https://www.koreabaseball.com/MediaNews/News/Preview/View.aspx?bdSe=62578 | KBO Carrasco six-inning Wild Card, ERA and KIA opposition | Official editorial preview; data source vs scoring records likely KBO, not independent historical collector |
| https://eng.koreabaseball.com/Standings/TeamStandings.aspx | 2026 final 144-game official league and two teams' runs/allowed, ERA, W/L/D | Search result final season current; opened page may return old cached version (100 games). Final verified separately on Oct20 mobile KBO |
| https://m.koreabaseball.com/ | As-of-Oct20 00:00 KST final 144-game standings and semi-PO G1/G2 | Mobile KBO field owner mirrors same collector; independent *display*, not independent statistical observation |
| https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=12183 | Official postseason 15-inning tie cap, series, suspended game/no rain-called rules | Official 7 Oct statement, independently reported by Chosun/Newsis |
| https://www.news1.kr/sports/baseball/6324044 | 19 Oct named starting pitcher preview, Carrasco context, Shirakawa LG struggles | Independent reporting, pregame published |
| https://www.yna.co.kr/view/AKR20261020155400007 | KIA full Oct20 batting order, manager lefty rationale, bullpen plan, Kim Do-yeong fitness | Published Oct20 **17:36 KST**, before scheduled 18:30 |
| https://mobile.newsis.com/view/NISX20261020_0003833884 | KIA order independent story, Carrasco handedness .267/.185 splits, manager comments | Published Oct20 17:36:44 KST, pregame |
| https://www.news1.kr/sports/baseball/6326360 | KIA seven LH strategy, bench/pitcher notes | Published Oct20 17:43 KST, pregame |
| https://www.newsis.com/view/NISX20261020_0003833694 | LG full nine, announced batting order changes and manager reason | Published Oct20, pregame, exact fetch time unknown |
| https://isplus.com/article/view/isp202610200145 | LG full nine independent press and 16:13 KST publication | Pregame, checked against Newsis/Sports Chosun |
| https://www.sportschosun.com/baseball/2026-10-20/202610200100127350008264 | LG full nine independent Chosun Sports writer | Pregame; original reporting independence plausible but cannot guarantee |
| https://www.mt.co.kr/sports/2026/10/20/202610201531770170O | LG Moon Sung-ju return context and pinch-hitting/platoon points | Pregame, OSEN shared/syndication, not fully independent from original OSEN piece |
| https://www.yagoonara.com/teams/2/gamelog | 20 dated pre-event KIA scores | Yagoonara as structured KBO-derived provider; **cumulative count 156 conflicts with official 144**, treat only exact dated rows subject to source audit |
| https://www.yagoonara.com/teams/4/gamelog | 20 dated pre-event LG scores | Same provider and potential independent-row coverage gap; official spot-check Oct dates |
| https://www.yagoonara.com/teams/2/recent-games | G1/G2 finals and Oct dated schedule | Same Yagoonara lineage; not independent corroboration of gamelog |
| https://www.yagoonara.com/schedule/128564 | Both pitcher ERA/WHIP and KIA–LG prior games, probable lineup previews | Dated indexed third-party page contains **stale 'lineup not announced'**, so actual fresh press lineup supersedes; its AI prediction text/odds not consumed |
| https://www.koreabaseball.com/Schedule/Schedule.aspx?date=202609 | Historical September dated games; site missing some late cached scores | Field-owner list incompletely crawled; 40-row independent closure remains open |
| https://www.yagoonara.com/postseason/rules | Corroborates league 15-inning cap and active roster format | Derives from KBO official; same lineage, not new independent rule |
| https://www.newsis.com/view/NISX20261007_0003817884 | Independently reported exact postseason rules | 7 Oct report |

No URLs in this card are offered as bookmaker/odds sources. All source dates in titles/publications should be contrasted with actual same-event provenance; retrieving after the scheduled start does NOT imply pre-start availability, even if page says 20 October. Actual user request arrival estimated 20:24 AEDT based on chat time and KBO first pitch scheduled at 20:30; report *actual card completion* separately, do not backdate it. Source documentation is incomplete until every historical row/availability field is corroborated, exact kickoff status and custody reconciled.

## A9. Research-completion matrix / C1–C22 audit

| Step/requirement | Actual result | Closure |
|---|---|---|
| 1 Pinned GitHub authority and read scope | SHA confirmed, source sport/baseball/selection/template documents read; active mini G0001–G0003 read via actual file | PASS_FOR_PUBLISHED_MAIN |
| 2 Event identity/date/time/orientation | KBO official semi-PO G3 Jamsil 18:30 KST, 20:30 AEDT; native ID/actual pitch time open | PARTIAL |
| 2 Duplicate/custody/lease | Prior P-533 is different Oct3 regular-season KIA–LG; expired proposed lease / private minis unknown | `READ_ONLY_DRAFT / NOT_ISSUED` |
| 3 Historical L5/L10/L15/L20 | 20 dated matches each, true window n5/10/15/20; official Oct spot checks; secondary-provider cumulative conflict and independent per-row corroboration still open | `HISTORY_ASSEMBLED / INFORMATION_INCOMPLETE` |
| 3 Both sides exact players | Two starters and two full starting nines independently reported; exact official full bench/late scratches/absences unverified | `LINEUP_CONFIRMED_BY_MANAGER_REPORT / BENCH_PARTIAL` |
| 3 Starting pitcher and bullpen | Both starting SP season summaries, KIA/LG plan, several relief names, no complete last-game pitch counts | PARTIAL |
| 4 Exact KBO mean/rule and numerical estimate | Official 2026 scoring anchor derived, transparent season/L20 k-weight, negative-binomial total approximation, normal conditional decisive win; no fitted KBO width/coherent inning-by-inning joint, no exact tie mass | `UNCALIBRATED_ANALYST_PRIMARY / MODEL_INCOMPLETE` |
| 4 League-only same-line baseline | Source mean available; exact sampled KBO postseason line/outcome frequencies/SD absent | NOT_ESTIMATED |
| 5 All four owner contracts | All assessed with complements, example probabilities, alternatives, Rank1 gate and Rank2 floor; no qualified pair | `RESEARCH_ONLY / UNKNOWN_DEFINITION` |
| 5 Dependence/shadows | Frechet provisional bounds, original/RET03 gate, others NONE, no uncomputed correlation asserted | PARTIAL |
| 6 Venue/weather/rules/termination | Jamsil/15-inning draw and suspended known; weather and written ML operator action unknown | PARTIAL |
| 7 Full card + file custody | Full draft returned for owner-save, previous originals must be preserved; no authenticated active write to expired lease | `READ_ONLY_DRAFT / NOT_ISSUED` |
| Audit C1–C22 | Authority, fixtures, action flags, 4 rows and complements, arithmetic & C21 evidence explicit; C3 custody, C5 timing, C8 action, C9 history independence, C10 fitted run process, C12 baseline, C16 joint, C18 known-at, C20 bench and C22 owner save remain open | `INFORMATION_INCOMPLETE / NO_CERTIFIED_PICK` |

**Final status:** `INFORMATION_INCOMPLETE; UNCALIBRATED_ANALYST_PRIMARY; NO_FORECAST_CERTIFICATION; READ_ONLY_DRAFT; NOT_ISSUED; NO_CANONICAL_ID; OWNER_SAVE_AND_WRITER_LEASE_PENDING`. No automatic follow-up or scheduled task is running. Next evidence if owner invokes further work: verified original KBO roster/bench active list and game-id, all-row history corroboration, pre-start evidence times, expected inning/bullpen exposures, exact KBO postseason distribution, operator actions, weather, and any private writer/lease conflict. **Do not settle now or use target results to repair this pregame draft.**

**SPORTS_ONLY_MARKET_BLIND / OUTCOME_EXPOSURE: EXCLUDED / SETTLEMENT: NOT_PERFORMED / RETROSPECTIVE: NOT_PERFORMED / CANONICAL_IMPORT: PENDING.**
<!-- END CANONICAL RESEARCH P-618 -->
