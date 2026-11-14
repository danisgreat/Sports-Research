# Urawa Red Diamonds vs Cerezo Osaka — 2026-11-11 — v24.15 research-only draft

**Local label:** `DRAFT-010`; **scope:** corrected match corresponding to earlier rejected `DRAFT-009` (Urawa vs Kashima). **Capture UTC:** `2026-11-11T10:25:51+00:00`. **GitHub main:** `4d8bd1771d20974bcbfc7c694a009cd44e95a693` (read-only). **Method:** `MDS-2026.11.11-v24.15`; `EXT-v3`; `P-2026.11.11-v24.13`. **State:** `READ_ONLY_DRAFT / NOT_ISSUED / NOT_SETTLED / NOT_PERFORMANCE_ELIGIBLE`. **Formal selection:** `NO_STRONG_PICK / ABSTAIN`. No frozen model or independent calibration, EV2 manifest, source-access audit receipts or official event allocation have been executed.

## A1. Event identity and chronology
- 2026/27 J.League Yamazaki Biscuit Levain Cup, quarterfinal **first leg**, Urawa Reds **HOME** vs Cerezo Osaka **AWAY**; Saitama Stadium 2002. Official kick-off 2026-11-11 19:30 JST = 2026-11-11 21:30 AEDT = 2026-11-11 10:30 UTC. Official match path `/en/match/leaguecup/2026/111102/` (path identity; not an independently retrieved native integer).
- Earlier `DRAFT-009` applied to nonexistent Urawa–Kashima fixture and must remain untouched. This is a distinct corrected valid request, not silent amendment of that invalid event.
- Source pages were reviewed before the stated kick-off; exact per-page capture timestamps were **not separately exported by the browser**, and are marked `NOT_CAPTURED` rather than invented. All sports results in this record have dates before 11 Nov. No match live or final score was accessed in research. Actual contemporaneous issue/freeze/publication evidence absent.
- Contract target: first-half 45'+stoppage, full-time 90'+stoppage only, no ET or penalties in first leg; regulation draw stands. Official rules: https://www.jleague.jp/news/article/35229/?navicode=leaguecup.

## A2. Exact supplied contracts (six directions; all unpriced)
| Exact contract | Period, endpoint, action | Qualitative direction | v24.15 numeric disposition |
|---|---|---|---|
| First half Over 0.5 goals | 1H regulation stoppage-inclusive, binary | **Preferred** | UNPRICED / NOT_VALIDATED — no exact-scope half-specific primary receipt |
| First half Under 0.5 goals | same | Oppose | UNPRICED / NOT_VALIDATED |
| Full-time Over 2.5 goals | 90 min stoppage-inclusive, binary | Marginal Over | UNPRICED / NOT_VALIDATED — no admitted corrected match goal distribution |
| Full-time Under 2.5 goals | same | Plausible due rotation / H2H | UNPRICED / NOT_VALIDATED |
| Total Over 10.5 corners | 90 min stoppage-inclusive, binary | No robust direction | UNPRICED / UNSUPPORTED — no competition-appropriate named combined-corners model |
| Total Under 10.5 corners | same | Marginal Under exploratory | UNPRICED / UNSUPPORTED — no competition-appropriate named combined-corners model |

`Rank scope = SUPPLIED_ONLY`. No p_card, W/P/L distribution, probabilities, ranks, comparative Brier, modeled score, simulations or selection ceiling asserted. The analyst language above is **not** a numerically issued primary selection.

## A3. Team availability, starts and benches
Two separate Japanese pregame lineup postings (`sakanowa.jp` / `uragi.com`) report the same **announced** first elevens. Official match-day eligibility/medical list was not independently confirmed from both clubs. Goalkeepers, outfield and available bench are stated as reported, not necessarily internally verified beyond lineup publications.

**Urawa XI:** GK Eisuke Arai (44); Yuta Miyamoto (2), Danilo Boza (3), Kota Kudo (15), Yoichi Naganuma (88); Tatsuki Seko (12), Renji Hidano (36), Hayato Ueki (37), Jumpei Hayakawa (39), Harumi Minamino (42); Ado Onaiwu (45). Bench Shusaku Nishikawa, Kenta Nemoto, Eiichi Katayama, Takuro Kaneko, Matheus Savio, Samuel Gustafson, Ryoma Watanabe, Kaito Yasui, Hiiro Komori. Coach Cho Kwi-jae.

**Cerezo XI:** GK Koto Abe (31); Javier Hernandez (15), Dion Cools (27), Travis Takahashi (97); Takumi Nakamura (2), Shunta Tanaka (10), Reiya Sakata (17), Kosei Okazawa (28), Yota Komi (41), Lucas Fernandes (77), Tomoki Uejo (7). Bench Ken Ishibo, Rikito Inoue, Kyohei Noborizato, Hayato Okuda, Ryosuke Hatanaka, Teppei Shiojiri, Solomon Sakuragawa, Thiago Andrade. Coach Pablo Machin.

**Rotation:** Urawa starts reserve goalkeeper and rotates several attacking positions; Savio, Watanabe, Komori and Nishikawa on bench. Cerezo also makes several changes after 8 Nov Osaka derby. No clean official injury/absence matrix found: `UNKNOWN` is not `NONE`.
Source URLs: https://sakanowa.jp/topics/114463; https://uragi.com/?p=55530; https://www.cerezo.jp/news/2026-1110-1830/.

## A4. Form and historical windows (mixed J1, cup and Emperor's Cup — not identical competition)
Official J.League club records through 8 Nov 2026; true n limited by displayed current-season results (19 each). Over 2.5 is count of combined 90-min match goals >=3. **Club CK is corners won by that club**, not both clubs' total corners.

| Club / true n | W-D-L | GF/game | GA/game | Total goals/game | Over 2.5 count | Club corners taken/game |
|---|---:|---:|---:|---:|---:|---:|
| Urawa L5 | 3-1-1 | 1.60 | 1.80 | 3.40 | 4/5 | 6.00 |
| Cerezo L5 | 2-2-1 | 2.00 | 2.00 | 4.00 | 4/5 | 3.40 |
| Urawa L10 | 7-1-2 | 1.90 | 1.60 | 3.50 | 8/10 | 6.10 |
| Cerezo L10 | 5-3-2 | 1.90 | 1.70 | 3.60 | 7/10 | 3.90 |
| Urawa L15 | 11-1-3 | 2.00 | 1.53 | 3.53 | 12/15 | 5.73 |
| Cerezo L15 | 6-5-4 | 1.53 | 1.67 | 3.20 | 8/15 | 4.87 |
| Urawa L19 | 12-1-6 | 2.00 | 1.79 | 3.79 | 16/19 | 5.26 |
| Cerezo L19 | 9-5-5 | 1.53 | 1.58 | 3.11 | 11/19 | 4.63 |

Source records: https://www.jleague.jp/en/club/urawa/; https://www.jleague.jp/en/club/cosaka/. Windows L5/L10/L15/L19 overlap, so are not independent pieces of evidence. **L20 = n19 / one missing** from displayed 2026/27 record; do not present n19 as n20.

Recent five Urawa newest to oldest: Nov 8 Kobe 2–2, Oct 31 Kashiwa 0–4, Oct 28 Nagoya 2–1 (YLC), Oct 25 Nagasaki 1–0, Oct 21 Chiba 3–2. Recent five Cerezo: Nov 8 Gamba Osaka 3–2, Oct 31 Kashima 1–4, Oct 28 Mito 3–1 (YLC), Oct 25 Chiba 2–2, Oct 21 Nagoya 1–1.

**H2H last five, 2023–25:** July 2023 Cerezo 2–0 Urawa (2); June 2024 Cerezo 2–1 Urawa (3); Oct 2024 Urawa 0–1 Cerezo (1); March 2025 Cerezo 1–1 Urawa (2); May 2025 Urawa 0–0 Cerezo (0). 5-game total-goals sum = 8, mean **1.60**; Over 2.5 = 1/5. These historical games precede current coaches, lineups and two-leg cup context.

## A5. Competition reference, matchup and directional estimates
- J.League Cup **exact-competition numeric baseline: NOT_ESTIMATED**. Current repo `COMPETITION_PARAMETERS.csv` includes a **Soccer/J1 League** development row from 136 games of 2025 (2.1985 mean goals and 0.408 first-half share in kit) but **not a J.League Cup row**; it is a league-only development benchmark, not admitted exact competition prediction and not current 2026/27 form. No cross-league transplant of its probabilities.
- Current form shows 3.4 and 4.0 total goals/game in last five (and 3.5 / 3.6 in last ten); 4/5 for each above 2.5, compared to 1/5 from the old head-to-head. These conflict, so recent form direction is only tentative.
- Strong rotation and 1st-leg caution suggest wider uncertainty and could suppress first-half pace; dangerous attackers on bench can enter later. However both attacks have scored recently, so **first-half Over 0.5** is the preferred descriptive line, **FT Over 2.5** a secondary, riskier inclination.
- Corners: L5 corners **taken** Urawa 6.0/game, Cerezo 3.4/game, **not a forecast of 9.4 total match corners** because opponents and conceded corner profiles are not matched. L10 taken 6.1 and 3.9. No complete provider-defined 90-min combined CK or confidence distribution reconciled; both Over and Under 10.5 remain unpriced. Tentative Under bias is unfit for a ranked recommendation.
- No numeric Poisson/DC/half-state/corner counts or simulated forecasts asserted. Score: `NOT_ESTIMATED`, margin: `NOT_ESTIMATED`, joint failure `NOT_ESTIMATED`; baseline: `NONE` exact Cup.

## A6. Weather, scheduling and tactics
- Saitama regional forecast for 11 Nov: around 16C high, 2C low, essentially dry (0% precipitation in regional forecast); stadium-local source shows ~15C high, 3C low, ~10% chance of rain. No exact kick-off hour wind report obtained. Weather not established as major scoring adjustment.
- Both played Sunday 8 Nov: Urawa 2-2 Kobe, Cerezo 3-2 Gamba Osaka; short turnaround, both rotated. Match tonight first leg; next leg 15 Nov. Cerezo official preview notes a 4-4-2 pressing shape versus Gamba, but named starting formation tonight is `NOT_VERIFIED`.
- Cerezo coach explicitly says tie judged over 180 minutes, not just first-leg result. First-leg rules permit draw after 90, with extra time possible **only in second leg** if necessary.
Sources: https://www.japan.travel/en/weather/kanto/saitama/; https://www.cerezo.jp/news/2026-1110-1830/; https://www.jleague.jp/news/article/35229/?navicode=leaguecup.

## A7. Adjustments and sensitivity
No validated or competition-specific effect size for XI rotation, rest, home field, weather, corners or H2H; therefore no arbitrary signed numeric adjustment is made. Directional scenarios only: (low-tempo first leg) may favour 1H Under and FT Under; (pressing/high transition game) may favour Over 2.5 and 1H Over; (late introduction of stronger Urawa attackers) may concentrate late goals. Corner totals vary independently with possession and crosses: no numeric tail was inferred from goals.

## A8. Timing, original material, source and audit limitations
- Exact source access decisions / live robots audits / source lineage independence checks were not executed and source retrieval timestamps not exported individually. Two lineup URLs could share the same original team release; this is **not** two independent original team-sheet collectors.
- Pre-event fixture identity confirmed from J.League official match and Urawa club; H2H and all recent dates from J.League official; cup rules from official J.League; weather regional, not hourly stadium. No poststart score read. Outcome exposure `NONE_DECLARED` but no independently verified publication receipt.
- Required v24.15 external EV2 event manifest, FULL_FIVE lane packets, frozen SINGLE comparator, full collector/source-reviewed L5 primary receipt, effect ledger and GitHub writer lease not present in this ChatGPT research chat. Do not claim packet admission, pregame issuance, official local ordinal, or model validation.

## A9. Research completion matrix and disposition
| Check | Result | Reason |
|---|---|---|
| Exact event ID/schedule/competition | PASS | Official league and club match pages |
| First-leg 90-minute settlement | PASS | Official J.League rules |
| Both starting XI/benches | PARTIAL | Two dated published pregame lineup reports; final official medical and independent match sheets not recovered |
| Season/current-form true-n | PASS_DESCRIPTIVE | Official J.League all 19 displayed 2026/27 games, mixed competitions |
| Exact Cup goal baseline & 1H distribution | NOT_ESTIMATED | Cup parameter row absent, no accepted first-half goal data grid |
| Combined corners source/model | UNAVAILABLE | Official CK won available but not 90-minute matched corner distributions or valid count receipt |
| Match-window weather | PARTIAL | Daily Saitama forecast; exact time wind not resolved |
| Empirical qualification / primary receipt | NOT_RUN | No admitted numeric model |
| Pre-start card freeze/official writer | NOT_ISSUED | ChatGPT local research only, GitHub read-only |
| Match result / settlement | NOT_REQUESTED | No scores or grades inspected |

**FINAL QUALITATIVE:** first-half **Over 0.5 goals** is the single preferred direction with LOW–MODERATE confidence; full-time **Over 2.5** slight, corner **Under 10.5** very slight/not recommended. **FORMAL:** `NO_STRONG_PICK / ABSTAIN`, all six directions `UNPRICED`, no percentages. **NO SETTLEMENT**.

## Source URLs
- fixture: https://www.jleague.jp/en/match/leaguecup/2026/111102/
- cup_rules: https://www.jleague.jp/news/article/35229/?navicode=leaguecup
- home_results: https://www.jleague.jp/en/club/urawa/
- away_results: https://www.jleague.jp/en/club/cosaka/
- lineups: https://sakanowa.jp/topics/114463
- lineups_second: https://uragi.com/?p=55530
- cerezo_preview: https://www.cerezo.jp/news/2026-1110-1830/
- weather: https://www.japan.travel/en/weather/kanto/saitama/
- official_match: https://www.urawa-reds.co.jp/game/info/000052.html
- h2h: https://www.jleague.jp/en/match/leaguecup/2026/111102/
