# Prediction Log 2

Status: **CLOSED FOR NEW FORECAST ISSUANCE — SETTLEMENT/RETROSPECTIVE RECORD REMAINS APPEND-ONLY**
Opened: **2026-08-25**
Current method: **MDS-2026.08.24-v2.1**
Predecessor: `PREDICTION_LOG.md`

## Current controlling snapshot

This is the controlling administrative snapshot for **Prediction Log 2 closeout**. Issued forecasts and prior settlements remain immutable. New forecasts move to **Prediction Log 3** beginning with `P-089`.

| Field | Current value |
|---|---|
| As of | 2026-08-26 17:58 Australia/Melbourne — P-077, P-083, P-085 and P-086 newly verified FINAL and settled in the closeout append below; P-081, P-082 and P-084 were already settled; P-087 and P-088 remain LIVE and are not fully graded |
| Next canonical ID | `P-089` — to be issued in Prediction Log 3 |
| Prediction Log 2 issued range | `P-067`–`P-088` |
| Closed/final disposition | P-067–P-086 are closed/settled, with P-086 explicitly performance-ineligible because its live state was not verified at issue |
| Carried unresolved queue | `P-087` LIVE — Sri Lanka first-innings target completed at 290 (Under 286.5 = LOSS), match-result target unresolved; `P-088` LIVE — latest verified specialist feed at closeout showed Howlers 3-5 Sikkim Boys at 72' |
| Numbering rule | Continue `P-###` sequentially across logs; do not reset |
| New forecast storage rule | Every new game from `P-089` onward goes to `PREDICTION_LOG_3.md` before user-facing delivery |
| Settlement rule | Carried P-087/P-088 settlements may be appended to Prediction Log 3 once authoritative finals are verified; never grade a live event |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` unless a future validated model legitimately runs |

## Standing intake rule

For every new game, the user supplies:

- the two teams/players;
- the available moneyline and/or alternate side lines;
- the available total Over/Under lines.

The analyst must then:

1. run the previous-log gate and verify any open predecessor/new-log events;
2. verify the new event identity, competition/format, scheduled start, venue, rules and current state;
3. freeze the exact supplied slate, targets, settlement geometry and information cutoff;
4. research current participants/availability, sport-native process evidence, matchup, venue/environment and relevant recent/comparable evidence;
5. build one coherent qualitative target corridor under the active method and map every supplied contract to it;
6. uniquely rank every valid unresolved supplied contract using `SUPPORTED`, `LEAN`, `FORCED RANK`, or `AVOID`;
7. identify a potential game/event winner independently;
8. disclose important unknowns, dependence, kill paths, source limitations and `NO VALUE DETERMINABLE` where the value gate is not met;
9. append the complete immutable forecast here **before** delivery;
10. after the event, append official settlement and retrospective without rewriting the issued forecast.

## Entry template

Each new game uses the next canonical heading:

`## P-### — [Event] — [State]`

and follows the active canonical schema in `UPCOMING_GAME_RESEARCH_GUIDE.md`, `AGENT_ROLE_AND_TASK.md`, `RULES_GENERAL.md`, `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`, and the relevant sport-specific rules file.

---

<!-- P-067 issued. Next canonical game is P-068. -->

## Carried predecessor queue settlement audit — P-064 through P-066

**Appended to Prediction Log 2:** 2026-08-25T19:22:30+10:00.  
**Record boundary:** the predecessor `PREDICTION_LOG.md` is unchanged/read-only. These settlements and retrospectives are recorded here because Prediction Log 2 is now the sole append target.

### P-064 settlement — Texas Rangers at Chicago White Sox, MLB

**Verified official final:** Texas Rangers **11**, Chicago White Sox **2**. MLB's game story records Texas reaching 11-2, including Corey Seager run-producing doubles, Jake Burger extra-base damage and Wyatt Langford's ninth-inning two-run homer.

| Original rank | Frozen contract | Outcome | Settlement note |
|---:|---|---|---|
| 1 | White Sox +1.5 | **LOSS** | Chicago lost by 9. |
| 2 | Under 9.5 runs | **LOSS** | 13 combined runs. |
| 3 | Rangers +1.5 | **WIN** | Texas won outright. |
| 4 | Over 7.0 runs | **WIN** | 13 combined; no push. |

**Potential winner:** Chicago White Sox — **LOSS**.

**Retrospective:** The issued card correctly identified José Urquidy's workload/current-quality uncertainty and Texas' contact route as live failure paths, but weighted them too lightly. Texas converted that ordinary kill path into repeated extra-base damage and then continued adding against the relief chain. The total and side errors were not caused by an identity, settlement or temporal-data defect. **Process grade: COMPLIANT — forecast/ranking miss, known-underweighted kill path.** Learning carried forward: starter recent run prevention and projected length cannot stand in for the full contact/HR/relief distribution, and a low-total thesis cannot independently justify the side. **Method change: none from one event.**

**Settlement source:** MLB game story, `https://www.mlb.com/stories/game/824557/`; MLB report, `https://www.mlb.com/news/joc-pederson-ejected-from-game-vs-white-sox`.

### P-065 settlement — Golden State Valkyries at Minnesota Lynx, WNBA

**Verified official final:** Golden State Valkyries **80**, Minnesota Lynx **66**; total **146**.

| Original rank | Frozen contract | Outcome | Settlement note |
|---:|---|---|---|
| 1 | Under 162.5 points | **WIN** | 146 combined. |
| 2 | Lynx -5.5 | **LOSS** | Minnesota lost outright by 14. |
| 3 | Valkyries +5.5 | **WIN** | Golden State won outright. |
| 4 | Over 162.5 points | **LOSS** | 146 combined. |

**Potential winner:** Minnesota Lynx — **LOSS**.

**Retrospective:** The scoring-suppression thesis was directionally correct, but the side model materially underweighted Minnesota's missing creation and Golden State's upset/separation branch. Golden State held Minnesota to a season-low 66 and won by 14; Cecilia Zandalasini led all scorers with 18 and four other Valkyries reached double figures. The historical Minnesota dominance was context, not protection. **Process grade: COMPLIANT — side/margin weighting miss, no demonstrated identity/source defect.** Learning carried forward: current role/creation availability must outrank historical series dominance when estimating the margin distribution. **Method change: none from one event.**

**Settlement source:** official WNBA recap, `https://www.wnba.com/watch/video/game-recap-golden-state-valkyries-80-minnesota-lynx-66-08-24-2026`; Valkyries official recap, `https://valkyries.wnba.com/news/gameday-recap-20260824`.

### P-066 settlement — Atlanta Dream at Los Angeles Sparks, WNBA

**Verified official final:** Atlanta Dream **78**, Los Angeles Sparks **71**; total **149**; Atlanta margin **+7**.

| Original rank | Frozen contract | Outcome | Settlement note |
|---:|---|---|---|
| 1 | Atlanta Dream -10.5 | **LOSS** | Atlanta won by 7, short of the required 11. |
| 2 | Under 181.5 points | **WIN** | 149 combined. |
| 3 | Los Angeles Sparks +10.5 | **WIN** | Los Angeles lost by only 7. |
| 4 | Over 181.5 points | **LOSS** | 149 combined. |

**Potential winner:** Atlanta Dream — **WIN**.

**Retrospective:** The lower-total branch was correctly identified and the outright winner was correct, but the card overextended Atlanta's class/recent-blowout evidence into an 11-point separation requirement. The rematch stayed close: Los Angeles led 37-36 at halftime before Atlanta won 78-71. Angel Reese's 26 rebounds were a major possession mechanism while the game never approached the prior meeting's scoring/separation profile. **Process grade: COMPLIANT — margin-threshold weighting miss, no demonstrated identity/source defect.** Learning carried forward: winner, large handicap and total are distinct thresholds; a prior blowout is not a reusable margin baseline without current separation evidence. **Method change: none from one event.**

**Settlement source:** official WNBA recap, `https://www.wnba.com/watch/video/game-recap-atlanta-dream-78-los-angeles-sparks-71-08-24-2026`; Dream official recap, `https://dream.wnba.com/news/historic-night-for-reese-as-dream-goes-4-0-on-west-coast-road-trip`.

**Carried predecessor disposition after this audit:** `P-064`, `P-065`, and `P-066` are **CLOSED / SETTLED**. No predecessor event remains open.

---

## P-067 — Doosan Bears at KT Wiz, KBO regular season — PRE-FIRST-PITCH FORECAST

**Record/view:** `P-067/V01`  
**Decision set:** `DS-P067-V01`  
**Candidate policy/origin:** `USER-SUPPLIED-ONLY-v1` / `USER_SUPPLIED`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / `E1-Q` qualitative  
**Request window:** 2026-08-25 approximately 19:17 Australia/Melbourne  
**Decision cutoff:** **2026-08-25T19:22:08+10:00 Australia/Melbourne / 18:22:08+09:00 Asia/Seoul**  
**Scheduled start:** **2026-08-25 18:30 Asia/Seoul / 19:30 Australia/Melbourne**  
**Official event:** 2026 Shinhan SOL KBO League, Doosan Bears at KT Wiz, season meeting 11, first game of a three-game series  
**Venue:** Suwon KT Wiz Park, Suwon, South Korea  
**GAME-STATE at cutoff:** **PREGAME** — the KBO schedule still displayed `DOOSAN : KT` for 18:30 at Suwon with no score, and a current game page separately stated that the game had not started.

### Previous-log gate

All three carried open predecessor IDs were verified final and settled above before this forecast. No live predecessor was graded prematurely. The predecessor file itself was not modified.

### Frozen targets and contract geometry

**Target IDs**
- `TGT-P067-MARGIN`: full-game official KBO final run margin, including the competition's permitted extra-inning/tie endpoint.
- `TGT-P067-RUNS`: combined official full-game runs through the KBO game endpoint.
- `TGT-P067-WINNER`: KT regulation/official full-game win event under KBO result rules.

**Operator/price status:** operator and odds were not supplied. Book-specific tie/refund, shortened-game/action, listed-pitcher and suspension terms are therefore `UNKNOWN_DEFINITION`. Research ranking assumes the official KBO final score is the sporting endpoint; no expected-value or staking claim is made.

| Candidate | Exact supplied contract | Sporting win interval under stated assumption | Geometry/dependence |
|---|---|---|---|
| C01 | Doosan Bears +1.5 | Doosan wins or loses by exactly 1 run; tie handling may be operator-specific | `DG-P067-MARGIN`; overlaps KT ML when KT wins by exactly 1. |
| C02 | KT Wiz ML | KT wins the official game; a KBO tie has operator-specific book treatment | `DG-P067-MARGIN`; not the complement of Bears +1.5. |
| C03 | Combined Over 8.5 | 9+ combined runs | `DG-P067-TOTAL`; overlaps Under 11.0 at totals 9-10. |
| C04 | Combined Under 11.0 | 10 or fewer wins; exactly 11 is a push under standard integer-total rules | `DG-P067-TOTAL`; overlaps Over 8.5 at totals 9-10. |

### Verified participants and high-priority process evidence

**Confirmed starters:** Doosan RHP **Choi Min-seok** (21 G, 11-3, 2.72 ERA) versus KT RHP **So Hyoung-jun** (16 G, 6-2, 3.39 ERA). Choi's latest start was 5 IP/2 R versus NC on Aug. 19. So's latest was a 5 IP/6 R loss to LG on Aug. 18. The official KBO preview reports Choi at 0-1, 4.91 ERA in two 2026 starts versus KT, but those starts were materially different (5 IP/5 R on May 26; 6 IP/1 R on June 18). So is 1-0 with a 2.25 ERA in two 2026 starts versus Doosan and 12-2 with a 1.96 career ERA against them. This matchup evidence is descriptive and shrunk; it is not treated as deterministic ownership.

**Confirmed batting orders reported pregame:**
- **Doosan:** Park Chan-ho SS; An Jae-seok 3B; Park Jun-sun 2B; Yang Eui-ji C; Kim Min-seok DH; Yunio Severino 1B; Kim Dae-han RF; Ryu Seung-min LF; Jung Soo-bin CF. Starter Choi Min-seok.
- **KT:** Choi Won-jun CF; Kim Sang-su 2B; Ahn Hyun-min RF; Sam Hilliard DH; Kim Hyun-soo 1B; Kwon Dong-jin SS; Heo Kyung-min 3B; Yoo Jun-gyu LF; Jo Dae-hyun C. Starter So Hyoung-jun.
Expanded rosters began today; Doosan added Kim Young-hyun, Kim Han-joong, Ryu Hyun-joon and Lim Jong-seong, while KT added Jang Sung-woo, Kim Min-seok, Son Min-seok and Yoo Jun-gyu. These additions widen bullpen/bench alternatives but do not by themselves supply a directional edge.

**Team baseline:** official KBO tables have KT first at **64-41-3 (.610)** and Doosan fifth at **58-50-4 (.537)**. KT owns the league's highest team batting average (**.279**), .363 OBP, .763 OPS and .304 RISP average, with 598 runs through 108 games. Doosan is at .270/.341/.736 with 522 runs through 112 games. The pitching side reverses: Doosan leads KBO with a **3.71 team ERA / 1.36 WHIP**, while KT is third at **4.38 / 1.42**. The season series is KT **6-3-1** over Doosan. These are baselines, not line probabilities.

**Weather/surface status:** a current game page lists cloudy conditions around 30°C with a 40% rain chance. That source is not the governing meteorological authority, so weather is retained as an uncertainty/possible delay or surface-state branch and is **not used directionally**. The official KBO schedule had not marked the game postponed at cutoff.

### D0 mechanism retrieval — process only, no outcome voting

| Historical case | Transferable mechanism | Material difference |
|---|---|---|
| P-016, Lotte-Kiwoom KBO | A low-scoring centre can still coexist with strong cushion geometry; score-centre error must not be confused with contract geometry. | Different clubs/starters/park and older state. |
| P-049, KIA-Doosan KBO | Separate run-suppression mechanism from exact score level; a correctly low total corridor can still be centred too high. | Different opponent and starter pairing. |
| P-054, Lotte-Kiwoom KBO | One-run margin geometry matters: +1.5 and opponent ML can overlap and must not be treated as opposites. | Different clubs and scoring environment. |

**D0 use:** representation and kill-path checks only. No analogue frequency or historical result is converted into a probability or weight.

### Underlying event forecast — KBO plate-appearance / starter-exit / relief-chain corridor

The matchup is unusually balanced across the two primary axes. **KT has the stronger offence, home field, current standings position and season-series edge; Doosan has the stronger overall run-prevention staff and the better season ERA from today's starter.** So's long Doosan track record supports KT's run-prevention branch, but his six-run last start prevents treating that history as a fixed rate. Choi's 2.72 ERA and low home-run allowance support a lower game centre, but KT's .304 RISP rate and stronger on-base/average profile make walks and clustered singles a real scoring route.

**Qualitative central corridor: roughly 7-10 combined runs**, with a one-run/two-run game occupying substantial central mass. This is a qualitative scenario corridor only, **not** a fitted numerical prediction interval.

### Scenario map

| Scenario | Mechanism | Contract effect |
|---|---|---|
| Lower | Both starters locate; Choi avoids free-pass clusters; So's ground/contact management versus Doosan persists; bullpens enter cleanly | Strongly helps **Under 11.0** and usually **Bears +1.5**; hurts Over 8.5. |
| Central | KT creates slightly more traffic/quality contact, but Choi keeps it bounded; Doosan scores 3-4 against So/relief; one-run or two-run KT edge | **Under 11.0** remains live; **Bears +1.5** and **KT ML** can both win on a one-run KT result; 9-10 runs also lets both total contracts win. |
| Upper | Choi's walk/contact branch converts against KT's RISP strength, or So repeats the LG wobble; early starter exit exposes middle relief; rain/surface disruption hurts command | Helps **Over 8.5**; threatens Under 11.0, especially at 12+; increases margin volatility. |
| Structural tail | KBO tie/extended extra innings, delayed start, or a bullpen/defensive-error cluster | Raises operator-definition uncertainty and can break the central total/margin assumptions. |

### Frozen ranking

| Rank | Candidate | Exact contract | Verdict | Evidence | Central mechanism | Strongest ordinary kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | C04 | **Combined Under 11.0 runs** | `LEAN` | MEDIUM-HIGH | High threshold relative to a two-quality-starter setup; Doosan owns the league's best team ERA, and So has repeatedly suppressed Doosan. | So's recent six-run wobble repeats and/or KT converts Choi walks/traffic into a multi-run inning; bullpen/extra-inning tail pushes game to 12+. | DG-P067-TOTAL | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | C01 | **Doosan Bears +1.5** | `LEAN` | MEDIUM | Choi/Doosan run prevention plus the +1.5 cushion protects every Doosan win and a one-run KT win; a close-game branch is structurally strong. | KT's superior offence and So's Doosan matchup history produce a clean 2+ run home separation. | DG-P067-MARGIN | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | C02 | **KT Wiz ML** | `LEAN` | MEDIUM | KT's stronger offence, home setting, 64-41-3 record, 6-3-1 season-series edge and So's historical suppression of Doosan give KT the narrow winner lean. | Choi's superior 2026 run prevention controls KT traffic and Doosan reaches So before KT's offence separates. | DG-P067-MARGIN | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | C03 | **Combined Over 8.5 runs** | `FORCED RANK` | MEDIUM-LOW | Nine or ten is a genuine overlap corridor if KT's offence creates normal traffic and Doosan contributes against So/relief. | Both starters work efficiently through 5-6 innings and the game stays in the 5-8 run band. | DG-P067-TOTAL | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

**Bottom-slot/swap test:** Over 8.5 is not a fade; 9-10 combined runs makes both supplied totals succeed. It remains fourth because the strongest verified event-specific inputs are the starter matchup and Doosan's league-best run prevention, which give a credible 7-8 run path that directly kills the Over while still comfortably winning Under 11.0.

### Potential winner

**KT Wiz — `LEAN`, MEDIUM evidence — alias of C02.** KT's superior offence/home position and So Hyoung-jun's strong Doosan history narrowly outweigh Choi Min-seok's better 2026 run-prevention line. **Strongest failure path:** Choi turns his season-level command/contact suppression into six efficient innings while Doosan scores first against So, making KT chase into Doosan's stronger staff.

### Validation and integrity boundary

No target-specific KBO numerical model has been fit, calibrated or validated. `H0` is not built. No probability was generated; no bookmaker odds were supplied; **value, expected return, stake, ROI and market edge are not determinable**. The most material unresolved field is operator-specific KBO tie/shortened-game/action settlement. Weather is also not used directionally because a government/official venue-local forecast was not independently verified at cutoff.

**Sources used:**
- KBO official daily schedule: `https://eng.koreabaseball.com/Schedule/DailySchedule.aspx`
- KBO official matchup preview: `https://www.koreabaseball.com/MediaNews/News/Preview/View.aspx?bdSe=62142`
- KBO official team batting: `https://www.koreabaseball.com/Record/Team/Hitter/BasicOld.aspx` and `Basic2.aspx`
- KBO official team pitching: `https://www.koreabaseball.com/Record/Team/Pitcher/BasicOld.aspx` and `Basic1.aspx`
- Pregame lineup report (OSEN via Nate): `https://sports.news.nate.com/view/20260825n27331`
- Current pre-start/weather cross-check: `https://www.yagoonara.com/schedule/19676`

**Result at append:** `OPEN — PREGAME / PRE-FIRST-PITCH`.


---

## P-068 — Hanwha Eagles at SSG Landers, KBO regular season — PRE-FIRST-PITCH FORECAST

**Record/view:** `P-068/V01`  
**Decision set:** `DS-P068-V01`  
**Candidate policy/origin:** `USER-SUPPLIED-ONLY-v1` / `USER_SUPPLIED`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / `E1-Q` qualitative  
**Request window:** 2026-08-25 approximately 19:24 Australia/Melbourne  
**Decision cutoff:** **2026-08-25T19:26:05+10:00 Australia/Melbourne / 18:26:05+09:00 Asia/Seoul**  
**Scheduled start:** **2026-08-25 18:30 Asia/Seoul / 19:30 Australia/Melbourne**  
**Official event:** 2026 Shinhan SOL KBO League, Hanwha Eagles at SSG Landers, regular-season meeting 12  
**Venue:** Incheon SSG Landers Field, Incheon, South Korea  
**GAME-STATE at cutoff:** **PREGAME** — KBO's official daily schedule still listed `HANWHA : SSG` for 18:30 at Munhak/Incheon without a score or postponement marker.

### Previous-log gate

`P-067` Doosan Bears at KT Wiz remained **PREGAME** at this cutoff and therefore was not settled, graded or retrospectively altered. It remains open. No older prediction log was modified.

### Frozen targets and contract geometry

**Target IDs**
- `TGT-P068-MARGIN`: official full-game Hanwha-minus-SSG run margin through the KBO game endpoint.
- `TGT-P068-RUNS`: combined official full-game runs through the KBO game endpoint.
- `TGT-P068-WINNER`: official full-game winner state, with KBO tie handling separated from sportsbook settlement.

**Operator/price status:** operator and decimal odds were not supplied. Book-specific tie/refund, shortened-game/action, listed-pitcher and suspension terms are `UNKNOWN_DEFINITION`; no value/EV conclusion is authorised.

| Candidate | Exact supplied contract | Sporting win interval under stated assumption | Geometry/dependence |
|---|---|---|---|
| C01 | Hanwha Eagles -1.5 | Hanwha wins by 2+ runs | `DG-P068-MARGIN`; exact opposite of C02 under the same full-game endpoint. |
| C02 | SSG Landers +1.5 | SSG wins/ties, or loses by exactly 1 run | `DG-P068-MARGIN`; exact opposite of C01 under the same full-game endpoint. |
| C03 | Combined Over 10.5 | 11+ combined runs | `DG-P068-TOTAL`; exact complement of C04. |
| C04 | Combined Under 10.5 | 10 or fewer combined runs | `DG-P068-TOTAL`; exact complement of C03. |

### Verified participants and high-priority process evidence

**Confirmed starters and lineups:** pregame reports published both starting nines and confirmed **Owen White** for Hanwha versus rookie **Kim Min-jun** for SSG. Hanwha's lineup is Kim Tae-yeon, Moon Hyun-bin, Han Ji-yoon, Kang Baek-ho, Noh Si-hwan, Chae Eun-seong, Heo In-seo, Lee Do-yoon and Shim Woo-jun. SSG counters with Jung Jun-jae, Park Seong-han, Guillermo Heredia, Jeon Eui-san, Kim Jae-hwan, Choi Ji-hoon, Jo Hyung-woo, Ahn Sang-hyun and Lim Geun-woo.

**Starter state:** White is **6-7, 3.11 ERA in 17 games/98⅓ IP** and has been strong against SSG in 2026: **2-0, 2.13 ERA in 12⅔ IP**. His latest start was 7 IP, 2 R against KIA. Kim is **5-2, 3.56 ERA in 11 games/55⅔ IP**, has not yet faced Hanwha this season, and is coming off 6 IP, 1 R versus Samsung. Recent reporting documents a run of quality starts and strong first-strike/command execution; that is a current-process positive but remains a small rookie sample.

**Team offence:** official KBO tables list Hanwha at **.276 AVG / .355 OBP / .432 SLG / .787 OPS with 632 runs and 132 HR in 109 games**, versus SSG at **.261 / .339 / .408 / .747 with 563 runs and 122 HR in 114 games**. Hanwha therefore carries the stronger season-long run-creation profile.

**Team run prevention:** official KBO pitching tables list Hanwha at **4.99 ERA / 1.53 WHIP** and SSG at **5.54 ERA / 1.58 WHIP**, the latter being the league's weakest team ERA at the cutoff. The current starter matchup is substantially better than either club's full-season staff line, so those team ERAs are not projected mechanically through the first six innings.

**Season-series context:** Hanwha leads the 2026 series **9-2**. This supports a matchup/regime prior only; it is not used as a mechanical vote. Several Hanwha wins were by multiple runs, but current starters/lineups control today's forecast.

**Roster changes:** expanded rosters began today. Hanwha added veteran reliever Joo Hyun-sang plus Jang Gyu-hyun, Choi Yoo-bin and Lee Do-hoon; SSG added Kim Jung-min, Kim Yo-sep, Lee Jun-gi and Shin Beom-su. The extra depth mainly widens late-game replacement options rather than creating a standalone directional signal.

**Weather:** Korea Meteorological Administration's Seoul/Incheon/Gyeonggi forecast called for possible showers through the **18:00-21:00** window, with local shower totals potentially material. The official KBO schedule had not marked this game postponed at cutoff. Weather is treated as a delay/command/surface-variance branch, **not** an automatic Over or Under signal.

### D0 mechanism retrieval — process only, no outcome voting

| Historical case | Transferable mechanism | Material difference |
|---|---|---|
| P-049, KIA-Doosan KBO | Strong starting pitching can create a lower central total even when the exact score centre is uncertain. | Different clubs, park and starter profiles. |
| P-054, Lotte-Kiwoom KBO | Side/winner and run-line thresholds must be separated; a likely winner does not automatically cover 1.5 runs. | Different clubs and current bullpen states. |
| P-053, DeNA-Yomiuri NPB | H2H/season history must not overpower direct starter and late-chain evidence. | Different league/rules population; mechanism only. |

**D0 use:** representation and kill-path checks only; no historical result frequency becomes a fitted probability or weight.

### Underlying event forecast — KBO plate-appearance / starter-exit / relief-chain corridor

Hanwha owns the stronger overall offensive profile and the clearer starting-pitcher matchup prior: White has been both effective overall and specifically strong against SSG, while SSG's season-long staff has allowed the most runs/earned-run pressure in the league. That creates a credible **Hanwha separation branch**, especially after Kim exits.

The counterweight is important: Kim's recent quality-start sequence is real current evidence, and if he keeps early counts under control he can hold Hanwha near the middle of its scoring distribution through five or six innings. That makes a one-run Hanwha win or even an SSG upset an ordinary, not exotic, failure path for `Eagles -1.5`.

For the total, the two starters pull the centre downward while both clubs' broader staff profiles and Hanwha's power/slugging create a substantial late upper tail. **Qualitative central corridor: roughly 7-10 combined runs**, with 11+ most plausibly arriving through early starter disruption, bullpen damage, walks/HR clustering, or weather-related command deterioration. This is a qualitative corridor, **not** a fitted probability interval.

### Scenario map

| Scenario | Mechanism | Contract effect |
|---|---|---|
| Lower | White's SSG matchup form persists; Kim continues his QS/command run; clean first six innings | Helps **Under 10.5** and keeps **SSG +1.5** live; weakens Hanwha -1.5 and Over. |
| Central | White suppresses SSG more effectively than Kim suppresses Hanwha; Hanwha reaches SSG middle relief and wins by 2-4 in an 8-10 run game | Best route for **Hanwha -1.5** and **Under 10.5** together. |
| Upper | Kim's rookie command slips against Hanwha's .787 OPS/132-HR offence, or White exits early; weak team bullpens allow clustered late scoring | Helps **Over 10.5** and can also create a wide Hanwha margin. |
| Structural tail | Shower delay, wet-ball command issues, defensive miscues, or KBO tie/extra-inning branch | Widens total and margin variance; raises operator-definition importance. |

### Frozen ranking

| Rank | Candidate | Exact contract | Verdict | Evidence | Central mechanism | Strongest ordinary kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | C01 | **Hanwha Eagles -1.5** | `LEAN` | MEDIUM | Better offence, White's stronger current/SSG-specific starter profile, SSG's league-worst season team ERA, and a 9-2 season-series edge create the clearest 2+ run separation branch. | Kim extends his QS run and holds Hanwha to 2-4 through six, turning the game into a one-run finish or SSG upset. | DG-P068-MARGIN | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | C04 | **Combined Under 10.5 runs** | `LEAN` | MEDIUM | Both starters are materially better than their clubs' season pitching baselines; White's SSG record and Kim's recent form support a controlled first half of the game. | Either starter exits early and the weak season-long relief environments plus Hanwha power create an 11+ run cluster. | DG-P068-TOTAL | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | C02 | **SSG Landers +1.5** | `FORCED RANK` | MEDIUM-LOW | Kim's current form and home setting make a close-game branch credible, and +1.5 protects an SSG win/tie or one-run loss. | White suppresses SSG and Hanwha reaches SSG's relief chain, producing the 2+ separation expected by C01. | DG-P068-MARGIN | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | C03 | **Combined Over 10.5 runs** | `AVOID` | MEDIUM-LOW | Hanwha's power and both clubs' poor season team ERAs provide a real 11+ tail, especially after the starters leave. | White and Kim both reach six innings near their recent quality level, leaving too little scoring exposure for 11+. | DG-P068-TOTAL | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

**Bottom-slot/swap test:** Over 10.5 is not impossible; the season-long run environments are permissive and the weather/bullpen branch can produce 11+. It remains fourth because today's named starters are materially better than those team-level ERA baselines and therefore reduce the central early-run path.

### Potential winner

**Hanwha Eagles — `LEAN`, MEDIUM evidence.** The winner call is driven by Hanwha's superior run creation, White's 3.11 ERA and 2.13 ERA versus SSG this season, plus SSG's weaker overall run prevention. **Strongest failure path:** Kim Min-jun continues his current command/QS sequence and SSG gets White into traffic early, forcing a close bullpen game where the -1.5 line and outright winner can diverge.

### Validation and integrity boundary

No target-specific KBO numerical model has been fit, calibrated or validated. `H0` remains unbuilt. No internal probability was generated or published. The user's lines were ranked by qualitative marginal win likelihood and robustness only. Because no operator/odds snapshot was supplied, **value, expected return, staking, ROI and market edge are not determinable**.

**Sources used:**
- KBO official daily schedule: `https://eng.koreabaseball.com/Schedule/DailySchedule.aspx`
- KBO official team batting tables: `https://www.koreabaseball.com/Record/Team/Hitter/BasicOld.aspx` and `https://www.koreabaseball.com/Record/Team/Hitter/Basic2.aspx`
- KBO official team pitching tables: `https://www.koreabaseball.com/Record/Team/Pitcher/BasicOld.aspx` and `https://www.koreabaseball.com/Record/Team/Pitcher/Basic1.aspx`
- KBO official preview: `https://web1.koreabaseball.com/MediaNews/News/Preview/View.aspx?bdSe=62139`
- Pregame lineup/starter report (OSEN): `https://sports.news.nate.com/view/20260825n27291`
- SSG lineup/expanded-roster report: `https://sports.news.nate.com/view/20260825n24943`
- Korea Meteorological Administration regional forecast: `https://www.weather.go.kr/w/forecast/overall/short-term.do?stnId=109`

**Result at append:** `OPEN — PREGAME / PRE-FIRST-PITCH`.


---

## P-069 — Lotte Giants at KIA Tigers, KBO regular season — PRE-FIRST-PITCH FORECAST

**Record/view:** `P-069/V01`  
**Decision set:** `DS-P069-V01`  
**Candidate policy/origin:** `USER-SUPPLIED-ONLY-v1` / `USER_SUPPLIED`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / `E1-Q` qualitative  
**Request window:** 2026-08-25 approximately 19:28 Australia/Melbourne  
**Decision cutoff:** **2026-08-25T19:28:00+10:00 Australia/Melbourne / 18:28:00+09:00 Asia/Seoul**  
**Scheduled start:** **2026-08-25 18:30 Asia/Seoul / 19:30 Australia/Melbourne**  
**Official event:** 2026 Shinhan SOL Bank KBO League, Lotte Giants at KIA Tigers, season meeting 13  
**Venue:** Gwangju-KIA Champions Field, Gwangju, South Korea  
**GAME-STATE at cutoff:** **PREGAME** — current schedule/state sources still listed the 18:30 game as scheduled/not started, with Beasley versus Shirakawa.

### Previous-log gate

`P-067` and `P-068` remained pregame at this cutoff, so neither was settled or retrospectively graded. No prior live/pregame record was altered.

### Frozen targets and contract geometry

**Target IDs**
- `TGT-P069-WINNER`: official KBO full-game winner through the competition endpoint, subject to operator-specific tie/action rules.
- `TGT-P069-RUNS`: combined official full-game runs through the KBO game endpoint.

**Operator/price status:** operator and odds were not supplied. Book-specific tie/refund, shortened-game/action, listed-pitcher and suspension terms are `UNKNOWN_DEFINITION`. Research ranking assumes the official KBO sporting result; no value/EV/staking claim is made.

| Candidate | Exact supplied contract | Sporting win interval under stated assumption | Geometry/dependence |
|---|---|---|---|
| C01 | Lotte Giants ML | Lotte wins the official game; KBO tie treatment is operator-specific | `DG-P069-WINNER`; not a strict binary complement of KIA ML because a tie is possible. |
| C02 | KIA Tigers ML | KIA wins the official game; KBO tie treatment is operator-specific | `DG-P069-WINNER`; not a strict binary complement of Lotte ML because a tie is possible. |
| C03 | Combined Over 9.5 | 10+ combined runs | `DG-P069-TOTAL`; exact half-run complement of C04. |
| C04 | Combined Under 9.5 | 9 or fewer combined runs | `DG-P069-TOTAL`; exact half-run complement of C03. |

### Verified participants and high-priority process evidence

**Confirmed starters:** Lotte RHP **Jeremy Beasley** (21 G, 8-5, 4.72 ERA) versus KIA RHP **Keisho Shirakawa** (11 G, 3-4, 4.44 ERA). Beasley previously faced KIA on April 24 and delivered **7 IP, 7 H, 11 K, 2 R** despite taking the loss. Shirakawa previously faced Lotte on June 4 and delivered **5 IP, 4 H, 2 BB, 4 K, 0 R**, earning the win. KBO's official preview also notes Shirakawa has allowed only **3 earned runs across his latest 16⅓ innings**, including 6⅓ IP/1 R in his prior start. These opponent samples are descriptive and shrunk, not treated as ownership.

**Confirmed batting orders reported pregame:**
- **Lotte:** Hwang Sung-bin CF; Na Seung-yeop DH; Victor Reyes LF; Han Dong-hee 3B; Go Seung-min 1B; Han Tae-yang 2B; Jeon Min-jae SS; Yoon Dong-hee RF; Son Seong-bin C. Starter Beasley.
- **KIA:** Park Jae-hyun CF; Harold Castro DH; Kim Do-young 3B; Na Sung-bum RF; Kim Sun-bin 2B; Oh Seon-woo LF; Han Jun-su C; Park Sang-jun 1B; Ha Joo-seok SS. Starter Shirakawa.

**Availability/roster note:** Lotte catcher **Son Seong-bin** returned to the starting lineup after a right-middle-finger injury evaluation found he could play with management. Expanded rosters began today; Lotte added Lee Ho-jun, Jung Dae-sun and Jung Hyun-soo, while KIA added Ju Hyo-sang, Byun Woo-hyuk, Park Sang-jun and Lee Chang-jin. These moves broaden bench/relief options but are not standalone directional signals.

**Team baseline:** current official KBO tables list KIA at **60-50-2 (.545)** and Lotte at **50-58-2 (.463)**. KIA owns the stronger season batting line: **.272 AVG / .346 OBP / .440 SLG / .786 OPS**, versus Lotte **.267 / .331 / .392 / .723**. Team pitching is much closer: KIA **4.39 ERA / 1.41 WHIP** versus Lotte **4.45 / 1.47**. KIA leads the season series **7-4-1**.

**Current form:** KBO's official preview reports both clubs at **8-4 in August**, tied for the month's best winning percentage at the time, while Lotte's August team batting average is **.302**. Therefore KIA's season-long advantage is real but should not be treated as an overwhelming current-form edge.

**Recent bullpen/tail context:** KIA lost its previous game 8-7 to Kiwoom after surrendering a five-run ninth-inning lead, including a walk-off grand slam. This is a real late-game variance warning, but one bullpen collapse is not projected as a stable new rate.

**Weather:** exact government match-window detail was not strong enough in the available search return to justify a directional adjustment. Weather is therefore `NOT_AVAILABLE_FOR_DIRECTION` on this card rather than inferred from generic conditions.

### D0 mechanism retrieval — process only, no outcome voting

| Historical case | Transferable mechanism | Material difference |
|---|---|---|
| P-049, KIA-Doosan KBO | Strong starter/run-prevention evidence can support a lower scoring centre even when exact score level is uncertain. | Different opponent and starters. |
| P-054, Lotte-Kiwoom KBO | Winner/side thresholds and total thresholds must remain separate; a close-game branch cannot be inferred from a low total alone. | Different matchup/park. |
| P-016, Lotte-Kiwoom KBO | A low scoring centre can coexist with substantial one-run/tie-margin uncertainty; contract geometry must remain explicit. | Different opponent/starter environment. |

**D0 use:** representation and kill-path checks only; no historical result frequency becomes a fitted probability or weight.

### Underlying event forecast — KBO plate-appearance / starter-exit / relief-chain corridor

KIA owns the stronger season-long offensive profile, home field and 7-4-1 season-series edge. Its middle order also carries more power/slugging threat than Lotte's season aggregate. That makes KIA the stronger outright-winner branch.

The main counterweight is meaningful. Lotte is one of KBO's hottest August offences, Beasley has already pitched well against KIA, and KIA's recent late-game collapse shows that a narrow KIA lead is not automatically secure. That keeps the winner call at `LEAN`, not `SUPPORTED`.

For the total, both named starters have already suppressed this opponent and Shirakawa enters in strong recent form. Lotte's .302 August batting and KIA's power create a legitimate 10+ run branch, especially after the starters leave, but the pregame starter matchup pulls the central path below an automatic shootout. **Qualitative central corridor: roughly 7-10 combined runs.** This is a qualitative scenario corridor, not a fitted probability interval.

### Scenario map

| Scenario | Mechanism | Contract effect |
|---|---|---|
| Lower | Beasley repeats his KIA command/strikeout outing; Shirakawa's recent form persists; both reach 6+ innings with limited traffic | Strongly helps **Under 9.5**; winner remains more side-dependent. |
| Central | KIA creates slightly more quality contact/traffic, Shirakawa keeps Lotte bounded, and KIA wins a competitive 4-3/5-3/5-4 type game | Helps **KIA ML** and usually **Under 9.5**. |
| Upper | Lotte's August .302 form gets to Shirakawa early or KIA's power reaches Beasley; both bullpens face high-leverage traffic | Helps **Over 9.5** and increases upset/late-swing risk. |
| Structural tail | Another KIA bullpen collapse, defensive-error/HR cluster, or extra-inning/tie branch | Raises total and winner variance; makes operator tie/action terms material. |

### Frozen ranking

| Rank | Candidate | Exact contract | Verdict | Evidence | Central mechanism | Strongest ordinary kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | C02 | **KIA Tigers ML** | `LEAN` | MEDIUM | Stronger season offence, home field, 60-50-2 record and 7-4-1 season-series edge; Shirakawa also enters in good form and has a scoreless prior start versus Lotte. | Beasley repeats his 7-IP/2-R KIA outing while Lotte's hot August lineup converts early traffic and/or KIA's bullpen gives away a late lead. | DG-P069-WINNER | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | C04 | **Combined Under 9.5 runs** | `LEAN` | MEDIUM | Both starters have already handled this opponent well; Shirakawa's recent 16⅓-IP/3-ER run supports a controlled early game, and team ERAs are mid-4s rather than extreme. | Lotte's .302 August hitting and KIA's .440 SLG create multiple early run clusters; bullpen exposure pushes the game to 10+. | DG-P069-TOTAL | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | C01 | **Lotte Giants ML** | `FORCED RANK` | MEDIUM-LOW | Lotte's August form is strong, Beasley has already pitched effectively against KIA, and the recent KIA bullpen collapse leaves a real late upset path. | Shirakawa suppresses Lotte again while KIA's superior power/on-base profile produces the decisive middle-inning separation. | DG-P069-WINNER | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | C03 | **Combined Over 9.5 runs** | `FORCED RANK` | MEDIUM-LOW | Both offences have credible 5+ run routes, and Lotte's August surge plus KIA's power keep 10+ live. | The named starters repeat their prior opponent-specific success and hand the game to the bullpens at a low base such as 2-2 or 3-2. | DG-P069-TOTAL | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

**Bottom-slot/swap test:** Over 9.5 is a credible branch rather than an automatic fade. It remains fourth only because the two named starters' current/opponent-specific evidence gives the lower-scoring path a modest edge at this exact threshold.

### Potential winner

**KIA Tigers — `LEAN`, MEDIUM evidence.** The winner call is driven by KIA's stronger season batting profile, home field, 60-50-2 record, 7-4-1 matchup edge and Shirakawa's recent form. **Strongest failure path:** Beasley suppresses KIA again, Lotte's hot August batting gets to Shirakawa, and the game reaches KIA's relief chain within one run.

### Validation and integrity boundary

No target-specific KBO numerical model has been fit, calibrated or validated. `H0` remains unbuilt. No internal probability was generated or published. The supplied lines were ranked by qualitative marginal win likelihood and robustness only. With no operator/odds snapshot, **value, expected return, staking, ROI and market edge are not determinable**.

**Sources used:**
- KBO official preview: `https://www.koreabaseball.com/MediaNews/News/Preview/View.aspx?bdSe=62140`
- KBO official team batting: `https://www.koreabaseball.com/Record/Team/Hitter/Basic2.aspx`
- KBO official team pitching: `https://www.koreabaseball.com/Record/Team/Pitcher/Basic1.aspx`
- KIA lineup/current starter report: `https://www.xportsnews.com/article/2187763`
- Lotte lineup/injury/current starter report: `https://www.xportsnews.com/article/2187802`
- Current pregame state cross-check: `https://www.yagoonara.com/schedule/list?team=3`

**Result at append:** `OPEN — PREGAME / PRE-FIRST-PITCH`.


---

## Settlement and retrospective append — P-067 through P-069

**Appended:** 2026-08-25T23:06:46+10:00 Australia/Melbourne.  
**Source owner for finals:** official KBO scoreboard, `https://eng.koreabaseball.com/Schedule/Scoreboard.aspx`.

### P-067 settlement — Doosan Bears at KT Wiz

**Official final:** Doosan **3**, KT **1**.

| Original rank | Frozen contract | Outcome | Settlement note |
|---:|---|---|---|
| 1 | Under 11.0 runs | **WIN** | 4 combined runs. |
| 2 | Doosan +1.5 | **WIN** | Doosan won outright by 2. |
| 3 | KT ML | **LOSS** | KT lost 1-3. |
| 4 | Over 8.5 runs | **LOSS** | Only 4 combined runs. |

**Potential winner:** KT Wiz — **LOSS**.

**Retrospective:** The low-total mechanism was strong and correctly ranked first. The side was misranked: Doosan starter Choi Min-seok delivered 6 innings of 1-run baseball, and Doosan's offence created the decisive separation via solo home runs, including Yang Eui-ji's go-ahead homer. The preissue card had explicitly identified Choi controlling KT traffic as the strongest KT-winner failure path; that ordinary branch occurred and deserved more side weight. **Process grade: COMPLIANT — winner/side weighting miss, no identity or settlement defect. Method change: none from one event.**

**Supporting recap:** `https://www.newspim.com/news/view/20260825001162`; `https://sports.news.nate.com/view/20260825n34624`.

### P-068 settlement — Hanwha Eagles at SSG Landers

**Official final:** Hanwha **1**, SSG **7**.

| Original rank | Frozen contract | Outcome | Settlement note |
|---:|---|---|---|
| 1 | Hanwha -1.5 | **LOSS** | Hanwha lost by 6. |
| 2 | Under 10.5 runs | **WIN** | 8 combined runs. |
| 3 | SSG +1.5 | **WIN** | SSG won outright. |
| 4 | Over 10.5 runs | **LOSS** | 8 combined runs. |

**Potential winner:** Hanwha Eagles — **LOSS**.

**Retrospective:** The total corridor held, but the favourite/separation read failed badly. SSG rookie Kim Min-jun worked 5 innings for 1 run, while Owen White allowed 4 runs in 5 innings and the game broke open with SSG's six-run sixth. The forecast correctly identified Kim's current quality-start form and SSG's close/upset route, but ranked Hanwha's season offence and historical series edge too aggressively. **Process grade: COMPLIANT — current-starter/late-inning separation branch underweighted. Method change: none from one event.**

**Supporting recap:** `https://sports.news.nate.com/view/20260825n34966`; `https://www.osen.co.kr/article/G1112863622`.

### P-069 settlement — Lotte Giants at KIA Tigers

**Official final:** Lotte **5**, KIA **8**.

| Original rank | Frozen contract | Outcome | Settlement note |
|---:|---|---|---|
| 1 | KIA Tigers ML | **WIN** | KIA won 8-5. |
| 2 | Under 9.5 runs | **LOSS** | 13 combined runs. |
| 3 | Lotte Giants ML | **LOSS** | Lotte lost. |
| 4 | Over 9.5 runs | **WIN** | 13 combined runs. |

**Potential winner:** KIA Tigers — **WIN**.

**Retrospective:** The outright KIA winner was correct, but the Under ranked too high. The game reached a 5-4 Lotte lead before KIA won on a ninth-inning pinch-hit walk-off grand slam by Lee Ho-yeon, exactly the kind of bullpen/HR-cluster structural tail that was named but not weighted heavily enough. This is a wrong total ranking, not evidence that all starter-based Under logic is defective. **Process grade: COMPLIANT — late-run cluster/tail weighting miss. Method change: none from one event.**

**Supporting recap:** `https://sports.news.nate.com/view/20260825n35084`; `https://m.news.nate.com/view/20260825n35050`.

**Disposition:** P-067, P-068 and P-069 are **CLOSED / SETTLED**. No older prediction log was modified.

---

## P-070 — Central Ballester Reserves vs El Porvenir Reserves — START PASSED / LIVE STATE NOT VERIFIED

**Record/view:** `P-070/V01`  
**Decision set:** `DS-P070-V01`  
**Selection origin:** `SYSTEMATIC_UNIVERSE`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / qualitative fallback  
**Request time:** 2026-08-25 approximately 23:03 Australia/Melbourne  
**Cutoff / final refresh:** 2026-08-25T23:06:46+10:00 Australia/Melbourne / 2026-08-25T10:06:46-03:00 Argentina  
**Competition:** provider labels vary between `Argentina Reserve League`, `Primera C Metropolitana Reserves`, and `Campeonato de Reserva de Primera Division C`; these are treated as the reserve fixture for the named clubs, not the senior Primera C match.  
**Scheduled start:** 2026-08-25 13:00 UTC / 10:00 Argentina / 23:00 Australia/Melbourne according to multiple current fixture/odds sources.  
**Venue:** `NOT VERIFIED`.

### GAME-STATE

`GAME-STATE: START PASSED / LIVE STATE NOT VERIFIED — NO PRETENCE OF PREGAME.`

At cutoff, current sources conflicted. A direct match-result page still stated **not started**, Sporty still displayed **Upcoming**, while another schedule page labelled the fixture **LIVE** based on the scheduled time. No authoritative reserve match centre with a verified score/clock was found. Therefore this card does **not** claim an exact live score or elapsed minute. All rows below are forced-research ranks, `NOT ACTIONABLE`, and `INELIGIBLE` for prospective performance because the exact live state was not verifiable.

### Frozen generated universe

The candidate universe was frozen from the currently observable market families before ranking:

- regulation 1X2;
- double chance;
- draw-no-bet;
- full-game goals O/U 2.5;
- first-half goals O/U 1.5;
- Asian handicap 0 / ±0.25 where shown;
- research-only total-corner thresholds 7.5 through 13.5 from the corner-stat provider family.

Verified market examples at cutoff included Central Ballester 2.30 / Draw 3.30 / El Porvenir 2.60, El Porvenir-or-Draw 1.55, El Porvenir DNB 1.95, full-game Under 2.5 at 1.90, and first-half Under 1.5 at 1.42 on Caliente. Odds are recorded as market context only; no value claim is made. The exact corner line/price was not verified at an operator.

### Current evidence

**Form / goal process:** El Porvenir's newest recoverable reserve sequence is materially stronger: wins over Claypole (2-1), Berazategui (3-1), General Lamadrid (1-0) and Yupanqui (2-1), plus a 2-2 draw with Cambaceres. Central Ballester's newest recoverable sequence is 0-2 vs Victoriano Arenas, 0-2 vs Yupanqui, 0-5 at Lugano, 1-0 vs Cañuelas and 0-2 at Estrella del Sur. This is not treated as a fitted probability, but it gives El Porvenir the clearer current attack/defence regime.

**H2H:** reserve H2H is sparse and mixed: El Porvenir lost 2-3 at home in July 2025 and won 2-1 away in September 2024. It is descriptive only. The senior clubs' 0-0 on 23 August 2026 is a different population and is not used as a reserve-team model input.

**Participants:** confirmed reserve starting XIs, goalkeeper, formation, set-piece takers and substitution plans were `NOT AVAILABLE` from a field-owning source at cutoff. This materially caps evidence quality.

**Goal corridor:** Central Ballester's recent lack of scoring and El Porvenir's stronger current form support an El Porvenir non-loss branch more than a Central win branch. First-half scoring evidence is mixed but still compatible with a 0-0/0-1 type opening half. Full-game Under 2.5 is less robust because El Porvenir's newest results include several 3-4 goal matches.

**Corner process:** direct current corner-causing evidence such as crosses, blocked crosses, end-line entries, defensive clearances and set-play volume was unavailable. Historical corner counts nevertheless show a relatively low central corner environment: Central Ballester's last-10 average total corners is 7.5 with only 10% over 10.5; its recent five listed totals were 8, 12, 1, 8 and 10. El Porvenir's recent listed corner totals were 9, 10, 7, 5 and 12, with roughly 4.2 corners for and 4.4 against per match in that sample. Because the direct target-event chain and operator definition are incomplete, the corner row is capped at `FORCED RANK / LOW` under the active soccer derivative gate.

### Scenario map

| Scenario | Mechanism | Main effect |
|---|---|---|
| Lower-scoring | Central remains low-output; El Porvenir controls field position without converting repeatedly; first half stays 0-0/0-1 | Helps 1H Under 1.5 and El Porvenir X2; can help full-game Under 2.5. |
| Central | El Porvenir creates the better chances and avoids defeat, with a 0-1, 1-1 or 0-2 type regulation path | Strongest support for El Porvenir X2; DNB remains viable. |
| Higher-scoring | El Porvenir's recent 2-3 goal attack persists and Central contributes, producing a 1-2/1-3/2-2 branch | Hurts full-game Under; may not hurt El Porvenir X2. |
| Corner tail | Early goal or persistent wide chasing creates repeated clearances/crosses | Main failure path for Under 10.5 corners. |
| State-risk tail | Match had already started and an unobserved goal/card/substitution occurred before cutoff | Invalidates any pretence that this is a clean pregame view; reason all rows are non-actionable/ineligible. |

### Frozen ranking — forced research only

| Rank | Candidate | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | C01 | **El Porvenir Reserves or Draw (X2)** | `FORCED RANK` | MEDIUM-LOW | El Porvenir's current reserve form is substantially stronger and Central has scored only once across the newest five recoverable matches. | Unverified live state already contains a Central goal/red-card advantage, or Central's home setup is materially different from recent losses. | DG-P070-SIDE | `INELIGIBLE` | `NOT ACTIONABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | C02 | **1st Half Under 1.5 goals** | `FORCED RANK` | MEDIUM-LOW | Central's attack has been extremely limited; a 0-0/0-1 first-half path is coherent with the current matchup. | El Porvenir continues its recent attacking surge and/or Central concedes another early multi-goal half. | DG-P070-GOALS | `INELIGIBLE` | `NOT ACTIONABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | C03 | **El Porvenir Reserves — Draw No Bet** | `FORCED RANK` | MEDIUM-LOW | Same stronger-form side thesis as C01, but draw becomes a push rather than a win. | Central rebounds at home, or an unverified live event already changed the game state. | DG-P070-SIDE | `INELIGIBLE` | `NOT ACTIONABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | C04 | **Under 10.5 total corners — research line, market availability not verified** | `FORCED RANK` | LOW | Recent total-corner samples for both teams cluster mostly below 11; Central's last-10 average is 7.5. | Missing width/cross/block/end-line evidence; an early goal creates chasing and repeated corners. | DG-P070-CORNERS | `INELIGIBLE` | `NOT ACTIONABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Potential winner

**El Porvenir Reserves — `FORCED WINNER — LOW CONFIDENCE`.** The call is based on the stronger recent reserve form and Central Ballester's very low recent scoring output. **Strongest failure path:** the live state had already changed before cutoff, or current reserve personnel differ materially from the historical form sample. Because the exact live score/clock and starting XIs were not verified, this winner call is informational only and not actionable.

### Integrity boundary

- No validated soccer probability model ran.
- No internal probability is published.
- Market prices are contextual only and were not captured under a complete value gate.
- The event state is materially uncertain after scheduled kickoff; therefore no row is treated as a clean pregame forecast.
- Corner evidence is incomplete under the active derivative-market gate; the row remains LOW evidence and research-only.

**Sources used:**
- Current match/result feed showing not started and market lines: `https://kqbd.mobi/argentina-reserve-league/ket-qua-tran-dau-central-ballester-reserve-vs-el-porvenir-reserves-252327032`
- Current fixture page showing Upcoming: `https://sporty.com/football/campeonato-de-reserva-de-primera-division-c/match/central-ballester-reserves-vs-club-el-porvenir-reserves/sr%3Amatch%3A111111114356776`
- Current schedule cross-check: `https://www.sportepoch.com/soccer/schedules`
- Caliente market page: `https://sports.caliente.mx/es_MX/e/32816027/Central-Ballester-%28R%29-vs-El-Porvenir-%28R%29`
- Current form summary: `https://leon.bet/de-de/blog/forecasts/soccer/central-ballester-2-club-el-porvenir-ii-reserve-25-08-2026-user`
- Corner/H2H data: `https://www.totalcorner.com/h2h/central-ballester-reserves-vs-el-porvenir-reserves`
- Central Ballester corner team page: `https://www.totalcorner.com/team/view/144850`

**Result at append:** `OPEN — START PASSED / LIVE STATE NOT VERIFIED; FORCED-RESEARCH RANKS ONLY`.

---

## P-071 — Alejandro Juan Mano vs Alejandro Turriziani Alvarez, ITF M25 Oviedo — DELAYED / NOT STARTED FORECAST

**Record/view:** `P-071/V01`  
**Decision set:** `DS-P071-V01`  
**Candidate policy/origin:** `SYSTEMATIC_UNIVERSE-CLOUDBET-MAIN-v1` / `SYSTEMATIC_UNIVERSE`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / qualitative fallback under RULES_GENERAL §10 tennis module  
**Request time:** 2026-08-25 approximately 23:14 Australia/Melbourne  
**Decision cutoff / final refresh:** 2026-08-25T23:16:00+10:00 Australia/Melbourne / 2026-08-25T15:16:00+02:00 Europe/Madrid  
**Competition:** ITF Men's World Tennis Tour, M25 Oviedo, singles main draw, Round of 32  
**Venue:** Real Club de Tenis de Oviedo, Oviedo, Spain  
**Surface:** outdoor clay  
**Scheduled start reported by current score/market sources:** 2026-08-25 11:00 UTC / 13:00 Europe/Madrid / 21:00 Australia/Melbourne  
**GAME-STATE at cutoff:** `DELAYED / POSTPONED — NOT STARTED`. Current order-of-play feeds showed the Oviedo program postponed/suspended and this match still without a played game; Robinhood displayed 0-0 while current bookmaker markets remained pre-match. No live score was used.

### Previous-log gate

`P-070` had only just crossed its scheduled soccer kickoff and remained without a trustworthy exact live state for settlement. It was therefore left OPEN and ungraded. No older prediction log was modified.

### Frozen candidate universe and market snapshot

Universe frozen from the current Cloudbet main markets visible before ranking: match winner; full-match game handicaps at -4, -4.5, -5, -5.5 and -6 for Juan Mano with corresponding opponent sides; and total games at 18.5, 19, 19.5, 20 and 20.5. Only exact lines visible in that frozen universe were eligible.

Cloudbet market context at access included: Juan Mano ML 1.25 / Turriziani Alvarez ML 3.65; Juan Mano -4 games 1.54; Juan Mano -4.5 games 1.67; Under 19.5 games 1.92; Under 20.5 games 1.68. These prices are contextual only. No calibrated internal probability exists, so no value/EV claim is permitted.

**Operator retirement/void terms:** not fully reconstructed for every derivative on this card; exact book settlement therefore remains a source limitation. The sporting forecast assumes a normally completed best-of-three ITF singles match. Any retirement/abandonment must later be settled under the operator's actual rules.

### Verified event and participant evidence

- ITF confirms M25 Oviedo runs 24-30 August 2026 at Real Club de Tenis de Oviedo on outdoor clay, $30,000 category M25.
- Alejandro Juan Mano: approximately ATP 657 live / official 656, age 21, 2026 overall 19-11 and clay 15-10. He reached the M25 Santander semifinal immediately before Oviedo, beating Alejandro Garcia 6-3 6-4, Pedro Rodenas 7-6 4-6 7-5 and Sergi Fita Juan 7-6 6-1 before losing to Carlos Sanchez Jover 1-6 6-2 6-2.
- Alejandro Turriziani Alvarez: approximately ATP 795/793, age 23, 2026 overall 17-17 but only 2-4 on clay. Recent clay results include a 6-3 6-1 win over Yuto Oki followed by a 6-0 6-4 loss to Andrea Paolini, plus earlier straight-set losses to Francesco Ferrari and Johan Nikles.
- H2H: Turriziani Alvarez leads 1-0, winning 6-3 7-5 at M25 Martos on hard court on 12 June 2025. This is retained as a real counter-signal, but its transfer is reduced because the current event is clay and Juan Mano's ranking/form regime has improved substantially since 2025.
- Workload/rest: Juan Mano played four matches from 18-22 August, including two three-set contests; Turriziani Alvarez's last listed ITF match was 13 August. That gives Turriziani the fresher-rest branch and is the main non-surface counterweight to the favourite.
- Direct current serve/return point statistics and a validated player-level clay hold/break model were not available in the research set. This caps confidence below HIGH and prevents a numerical probability claim.
- AEMET observations in Oviedo showed very high humidity and a small 0.2 mm precipitation reading at 09:00 local, but no precipitation at 10:00-12:00. The court delay is therefore recorded as observed from order-of-play sources; no weather cause is inferred.

### D0 / historical mechanism retrieval

No prior tennis event exists in the current Sports Research D0 retrospective set with a sufficiently comparable sport-native mechanism. `NO COMPARABLE CASE` is recorded. General process controls still apply: exact identity/settlement, current surface, participant workload, matchup continuity and retirement terms must be separated from raw H2H outcomes.

### Underlying tennis forecast

The central sporting branch favours **Juan Mano**. The biggest inputs are the surface-specific 2026 gap (15-10 clay versus 2-4), the ranking gap, and Juan Mano's much stronger immediate M25 clay run in Santander. Turriziani's 2025 straight-set H2H win and rest advantage keep the forecast from becoming a SUPPORTED blowout thesis.

The most coherent match-shape is a Juan Mano win in two sets, but not necessarily two extremely lopsided sets. A 6-3/6-4, 6-4/6-3 or 7-5/6-2 type result is more defensible than assuming repeated 6-1/6-2 scores. That makes the match winner the most robust row; moderate Unders and a modest favourite game handicap follow behind it.

### Scenario map

| Scenario | Mechanism | Contract effect |
|---|---|---|
| Lower / clean favourite | Juan Mano carries Santander clay level forward, wins return exchanges and avoids extended service games | Helps Mano ML, Mano -4 and both Unders. |
| Central | Mano wins in two competitive sets, with Turriziani holding enough to keep one set near 6-4/7-5 | Strongest for Mano ML and Under 20.5; -4 is more boundary-sensitive. |
| Competitive upset branch | Turriziani's extra rest and prior H2H pattern translate; he protects serve and forces a third set or wins a close two-set match | Hurts all four ranked rows, especially Unders/handicap. |
| Structural tail | Delayed court conditions, retirement, or interruption materially changes fitness/settlement | Book-specific treatment can dominate derivative outcomes; reason no value claim is made. |

### Frozen ranking

| Rank | Candidate | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | C01 | **Alejandro Juan Mano ML** | `LEAN` | MEDIUM-HIGH | Better current ranking, 15-10 clay record, and strong recent M25 Santander run give Mano the clearest route to two sets before Turriziani. | Turriziani's 2025 6-3 7-5 H2H win plus much greater rest transfers more strongly than expected. | DG-P071-MATCH | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | C02 | **Under 20.5 total games** | `LEAN` | MEDIUM | A straight-set Mano win can still clear this line with competitive score shapes such as 6-4 6-4 or 6-3 6-4; Turriziani's 2026 clay struggles reduce the three-set centre. | One tiebreak/7-5 set plus another competitive set, or any three-set match, pushes the total above 20.5. | DG-P071-TOTAL | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | C03 | **Alejandro Juan Mano -4.0 games** | `LEAN` | MEDIUM | Surface/form edge creates a credible 5+ game separation while the integer line preserves a push at exactly four. | Mano wins narrowly, e.g. 7-6 6-4 or 6-4 7-5, or Turriziani wins a set. | DG-P071-MARGIN | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | C04 | **Under 19.5 total games** | `FORCED RANK` | MEDIUM-LOW | The strongest straight-set favourite paths land at 18-19 games, e.g. 6-3 6-3 or 6-3 6-4. | A single 7-5/tiebreak set or a closer 6-4 6-4 type straight-set result is enough to beat the Under. | DG-P071-TOTAL | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Contract geometry and dependence

- C02 and C04 are nested Unders; C04 is strictly harder to win than C02.
- C03 is strongly positively dependent on the same Mano-dominance thesis but is not equivalent to either total: a 7-5 6-2 Mano win covers -4 while producing 20 total games, for example.
- C01 is the broadest favourite contract and remains valid across close two-set and three-set Mano wins.
- These are four thresholds on linked match/set/game processes, not four independent forecasts.

### Potential winner

**Alejandro Juan Mano — `LEAN`, MEDIUM-HIGH evidence.** Central mechanism: stronger current clay profile, higher ranking and better immediate ITF form. Strongest failure path: Turriziani's prior H2H success plus rest advantage produces a closer serving/return regime than the current clay records suggest.

### Integrity / model status

- No validated tennis probability model exists in the current Sports Research framework.
- No internal win probability, calibration or value edge is published.
- Current market odds are external context only and did not become an internal model output.
- Serve/return point data were incomplete, so confidence is capped.
- Match is delayed/not started rather than live; no elapsed-play information was used.

**Sources used:**
- ITF tournament fact sheet / official event identity and surface: `https://www.itftennis.com/en/tournament/m25-oviedo/esp/2026/m-itf-esp-2026-044/`
- ITF draws/order-of-play shell: `https://www.itftennis.com/en/tournament/m25-oviedo/esp/2026/m-itf-esp-2026-044/order-of-play/`
- TennisTemple current order of play / postponed-suspended state: `https://en.tennistemple.com/matches/2026-08-25`
- Cloudbet frozen market universe: `https://www.cloudbet.com/es/sports/tennis/international-tc367-itf-oviedo-men/36006356`
- TennisTonic player/H2H/surface records: `https://tennistonic.com/head-to-head-compare/Alejandro-Juan-Mano-Vs-Alejandro-Turriziani-Alvarez/`
- TennisExplorer / TennisTemple current player results and rankings
- AEMET Oviedo hourly observations: `https://www.aemet.es/es/eltiempo/observacion/ultimosdatos?datos=det&l=1249X&que=ast&w=0`

**Result at append:** `OPEN — DELAYED / NOT STARTED`.

---

## P-072 — Jelle Sels vs Stijn Paardekooper — DELAYED / NOT STARTED FORECAST

**Record/view:** `P-072/V01`  
**Decision set:** `DS-P072-V01`  
**Selection origin:** `SYSTEMATIC_UNIVERSE`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / qualitative tennis fallback under RULES_GENERAL §10  
**Request/cutoff:** 2026-08-25 approximately 23:18 Australia/Melbourne  
**Competition:** ITF Men's World Tennis Tour, M25 Oldenzaal, singles first round / Round of 32  
**Venue:** Oldenzaal, Netherlands; exact court shown by TennisTemple as Centre Court  
**Surface:** outdoor clay  
**Official event window:** ITF M25 Oldenzaal, 24-30 August 2026  
**GAME-STATE:** `DELAYED / NOT STARTED` — TennisTemple showed 0-0 with no game completed after the nominal 12:00 local listing; current bookmaker pages still exposed pre-match markets. No elapsed-play state was used.

### Previous-log gate

`P-070` remained inside its live window without a trustworthy exact state and was left OPEN/ungraded. `P-071` remained delayed/not started and was left OPEN/ungraded. No older prediction log was modified.

### Frozen candidate universe / market evidence

The current market universe was frozen from Betfair/1xBet/Scores24 observable pre-match families: match winner; set handicaps; total sets; total games; game handicaps; correct score. Exact externally visible contracts used here were Sels ML and both +1.5-set handicaps. `Over 2.5 sets` is retained as a research contract from the available total-sets family; its current exact price was not retrievable from the rendered page and therefore receives no value claim.

- Betfair current match-winner context: Sels 8/11, Paardekooper 1/1 on the crawled event page.
- 1xBet current event page displayed the same named match, clay/R32 identity and a broad 65-market pre-match universe including totals and handicaps; its displayed win-percentage graphic is external bookmaker context only and not an internal probability.
- Scores24 exposed both `Paardekooper +1.5 sets` and `Sels +1.5 sets` as current handicap contracts/trends.

### Verified participant / matchup evidence

- ITF confirms M25 Oldenzaal runs 24-30 August 2026 on outdoor clay, $30,000 category.
- Jelle Sels is the #5 seed and approximately ATP 538 (live around 544 on TennisTemple); Stijn Paardekooper is approximately ATP 888 (live around 874).
- No prior H2H was found by TennisTemple, SteveG Tennis or Scores24.
- Paardekooper's newest ITF sequence is high-quality for this level: beat Noah Thurner 6-3 6-1 and Noah Schlagenhauf 3-6 6-2 6-2 before losing a three-set quarterfinal to Jack Loge 7-6 3-6 3-6 on 21 August.
- Sels' most recent completed listed ITF results are older: loss to Abel Forger 2-6 6-3 3-6 on 9 July; retirement-aided win over Deney Wassermann on 7 July; loss to Kirill Kivattsev in three sets on 1 July; win over Yuichiro Inui 7-6 6-3 on 30 June.
- SteveG Tennis lists 2026 clay records of 8-12 for Sels and 6-5 for Paardekooper. Their broader career clay records favour Sels in experience/volume, but current-year clay form is not a clear Sels advantage.
- Recent serve/return comparison from Matchstat is close: Paardekooper has the better recent second-serve figure, while return numbers are nearly even; Sels has a modest recent break-point-conversion/deciding-set edge in that provider's comparison.
- Paardekooper is 196 cm and has produced a 77.3% service-hold rate in the SteveG sample, making a routine straight-set Sels separation less robust than ranking alone would imply.

### Underlying tennis forecast

This is a genuinely competitive first-round match. Sels has the ranking, seeding, career experience and a stronger long-run first-serve profile. Paardekooper has the more recent match rhythm, the better 2026 clay W/L in the recovered sample, and current serve/return indicators that are close enough to neutralise much of the ranking gap. External market sources also disagree on the favourite, reinforcing a broad two-sided match corridor rather than a clean mismatch.

The central branch is **both players winning at least one competitive set or Sels edging a close two-set/three-set match**. The outright winner lean is Sels, but only narrowly. A routine 6-2 6-2 Sels win is not the central thesis.

### Scenario map

| Scenario | Mechanism | Contract effect |
|---|---|---|
| Sels control | Experience/seeding and first-serve quality translate, Paardekooper's recent workload catches up | Sels ML wins; Sels +1.5 sets wins; Paardekooper +1.5 sets can fail if 2-0. |
| Central competitive | Paardekooper's recent clay rhythm/serve keeps him level while Sels' experience matters late | Strong for both +1.5-set contracts and Over 2.5 sets; slight Sels ML edge. |
| Paardekooper upset | Younger player sustains second-serve/hold form and Sels' month-plus lack of completed match sharpness matters | Paardekooper +1.5 wins; Sels ML loses; Sels +1.5 can still win in a 2-1 loss. |
| Structural tail | Delay/retirement/abandonment changes fitness or operator settlement | Derivative settlement becomes book-specific; no value claim. |

### Frozen ranking

| Rank | Candidate | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | C01 | **Stijn Paardekooper +1.5 sets** | `LEAN` | MEDIUM-HIGH | Recent clay rhythm, 6-5 2026 clay record and competitive serve profile make him more likely to take at least one set than to lose 0-2. | Sels' ranking/experience gap reasserts immediately and produces a clean straight-set win. | DG-P072-SETS | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | C02 | **Jelle Sels +1.5 sets** | `LEAN` | MEDIUM-HIGH | Higher ranking, #5 seed status and career experience make a 0-2 Sels loss less central than a match in which he wins at least one set. | Paardekooper's recent match sharpness overwhelms Sels' older form and produces a straight-set upset. | DG-P072-SETS | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | C03 | **Jelle Sels ML** | `LEAN` | MEDIUM | Seeding/ranking, long-run experience, first-serve profile and better deciding-set history give Sels a narrow late-match edge. | Paardekooper's current clay form and second-serve/hold profile are more predictive than ranking; Sels' lack of recent completed matches shows. | DG-P072-MATCH | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | C04 | **Over 2.5 total sets — research contract; exact current price not retrieved** | `FORCED RANK` | MEDIUM-LOW | External metrics/markets disagree on the favourite and both players have recent three-set evidence, supporting a competitive three-set branch. | Either player converts the small edge into a clean 2-0; especially Sels if ranking/experience dominates from the start. | DG-P072-SETS | `CORRELATED_SECONDARY` | `NOT ACTIONABLE / NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Contract geometry

- C01 and C02 can both win if the match finishes 2-1 either way; they are not independent confirmations.
- C04 (Over 2.5 sets) implies both C01 and C02 win in a normally completed best-of-three match, so all three share a strong dependence group.
- C03 is broader than any straight-set thesis and is the only outright-winner contract among the four.
- Retirement/abandonment settlement is operator-specific and was not reconstructed for every derivative; this prevents a value claim.

### Potential winner

**Jelle Sels — `LEAN`, MEDIUM evidence.** Central mechanism: higher ranking/seeding, substantially greater career experience and a modest late-match/first-serve edge. Strongest failure path: Paardekooper's much fresher competitive rhythm and current clay/second-serve profile prove more relevant than Sels' ranking history.

### Integrity / model status

- No dedicated validated tennis probability model exists in the current Sports Research framework.
- No internal win probability, calibration or EV/value claim is published.
- External bookmaker/model percentages were treated only as context and disagreement evidence.
- Exact live point-by-point state remained 0-0/no completed game at the retrieved match page; this is treated as delayed/not started rather than a live tennis forecast.

**Sources:** ITF M25 Oldenzaal official tournament page/calendar; TennisTemple Sels-Paardekooper match page; SteveG Tennis player/H2H pages; Scores24 match/trend pages; Betfair event page; 1xBet current event page; Matchstat comparison page.

**Result at append:** `OPEN — DELAYED / NOT STARTED`.  
**Next canonical ID:** `P-073`.

---

## P-073 — Tobol Kostanay vs Kaisar Kyzylorda — PREGAME FORECAST

**Record/view:** `P-073/V01`  
**Decision set:** `DS-P073-V01`  
**Selection origin:** `SYSTEMATIC_UNIVERSE`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / qualitative soccer champion  
**Request/cutoff:** 2026-08-25 approximately 23:47 Australia/Melbourne / 18:47 Asia/Almaty (UTC+5)  
**Competition:** Kazakhstan Premier League, postponed Round 21 fixture  
**Venue:** Central Stadium, Kostanay, Kazakhstan  
**Scheduled start:** 2026-08-25 19:00 Kazakhstan time / 14:00 UTC / 2026-08-26 00:00 Australia/Sydney-Melbourne  
**GAME-STATE:** `PREGAME` — Sports.kz official-style match page still displayed “match not started” at final refresh, with confirmed starting XIs published.

### Previous-log gate

`P-070` remained unresolved with no trustworthy final result; `P-071` and `P-072` remained delayed/not-started/open in the current research set. No prior open row was graded or rewritten. Only Prediction Log 2 was modified.

### Frozen candidate universe

Universe frozen before ranking from current pre-match market families visible at Betfred plus one corner research threshold identified in current corner-market research:

- Match result / double chance
- Full-match total goals: 1.5, 2.5, 3.5
- First-half total goals: 0.5, 1.5, 2.5
- Total corners: research threshold 7.5

Current Betfred lines at access included Tobol/Draw double chance 2/9, Under 3.5 goals 1/3, and 1H Under 1.5 goals 4/9. Current corner research exposed Over 7.5 total corners, but no trustworthy exact operator price was captured; the corner row is therefore research-grade only and not value-actionable.

### Verified identity, lineups and context

Sports.kz listed the fixture at Central Stadium in Kostanay, referee Sayat Karabayev, with the match still not started. Confirmed starters:

**Tobol:** Danil Ustimenko; Roman Asrankulov, Pape-Alioune Ndiaye, Aleksandr Marochkin, Amanzhol Bakitzhanov; Maksim Myakish, Askhat Tagybergen, Amine Talal, Luis Guerra; Uros Milovanovic, Vitaliy Lisakovich.

**Kaisar:** Nurymzhan Salaidin; Abylaikhan Tolegenov, Adilet Kenesbek, Niyaz Idrisov, Stefan Bukorac, Klaidher Macedo; Salamat Zhumabekov, Miqueias Cabral Evaristo, Bakdaulet Konlimkos; Agostinho, Aliyar Mukhamed.

Material lineup interpretation: Tobol retain the stronger senior attacking spine through Milovanovic + Lisakovich, while Islam Chesnokov is no longer in the current Tobol group. Kaisar do **not** start Victor Moses, Nikola Cuckic, Imoh Ezekiel or Nurali Zhaksylyk; Cuckic, Ezekiel and Zhaksylyk are bench options, while Moses is absent from the published match squad. This reduces the starting attacking ceiling relative to Kaisar's strongest recent configuration.

Table state: Tobol 9th with 25 points from 21; Kaisar 13th with 20 from 21. Kaisar's league profile is unusually draw-heavy (3W-11D-7L in the current table snapshot).

Recent results: Tobol beat Irtysh 2-0 after losses to Partizan and Ordabasy; Kaisar's latest sequence includes 2-3 vs Zhenis in the Cup, 1-2 vs Aktobe, 3-1 vs Zhenis, and league draws with Yelimay and Kaspiy. The postponed Round 23 fixtures mean no false assumption of a 23 August Tobol-Kaisar rematch was used.

Government weather source Kazhydromet forecast Kostanay dry/partly cloudy on 25 August, with no precipitation and moderate wind. Weather is therefore not used as a strong directional total modifier.

### Goal-process forecast

The central regulation branch is a controlled Tobol territorial edge against a compact Kaisar setup. Tobol have the more threatening starting front two and a home attacking baseline; Kaisar's starting XI is more conservative than its strongest available attacking unit. Kaisar's draw-heavy league profile and Tobol's recent low-output matches keep a large-score branch secondary.

Qualitative central score corridor: `Tobol 1-0 / 2-0 / 1-1`, with 2-1 a meaningful upper-central branch. A 3+ goal margin or open 2-2/3-1 game requires an early score, red-card state, unusually efficient finishing or substitute-driven late expansion.

### Corner-process evidence

Direct corner evidence is mixed but points to a mid-range total rather than an extreme. TotalCorner's recoverable H2H sample averages 9.1 total corners, with Over 9.5 in 40% of those meetings. Recent team samples show Tobol creating materially more corners than Kaisar in one provider; CornerEdge's current five-match sample puts both teams around 4.5 corners for and 4.5 conceded, with a 9.0 combined match baseline.

Mechanism interpretation: Tobol should have more possession/territory and Kaisar's deeper block can create clearances and corner pressure, supporting an 8+ corner branch. However, decisive direct-event inputs — current crosses, blocked crosses, end-line entries, clearance rates and exact bookmaker corner-provider definition — were not all available. Under RULES_SOCCER derivative completeness rules, the corner row cannot receive LEAN/SUPPORTED and is capped at `FORCED RANK` / LOW evidence.

### Scenario map

| Scenario | Mechanism | Main contract effect |
|---|---|---|
| Lower-output | Kaisar compact block, Tobol patient possession, low finishing efficiency | Strong for 1X, Under 3.5, 1H Under 1.5; corners can still reach 8 through pressure. |
| Central | Tobol territorial edge produces 1-0/2-0 or a 1-1 state | Strongest overall branch; supports top three ranks. |
| Kaisar upset | Counterattack/set piece converts first and Tobol's reshaped wide attack struggles without Chesnokov | Main kill path for Tobol 1X/ML; can increase second-half corners. |
| Open-game tail | Early goal/red card or substitute impact creates transitions and late scoring | Main kill path for both Under rows; can help Over 7.5 corners. |
| Early-Tobol-goal control | Tobol scores and lowers risk rather than continuing to force width | Helps Under goals but can hurt corner Over if pressure drops sharply. |

### Frozen ranking

| Rank | Candidate | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | C01 | **Tobol Kostanay or Draw (1X)** | `SUPPORTED` | MEDIUM-HIGH | Home field, stronger starting attacking spine, higher table position and Kaisar's conservative/draw-heavy setup make Tobol non-loss the most robust branch. | Kaisar again exploits Tobol on transition/set pieces and wins a low-margin match. | DG-P073-SIDE | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | C02 | **Under 3.5 total goals** | `LEAN` | MEDIUM-HIGH | Current lineups and central game state point to controlled scoring; four goals requires a more open tail than the base case. | Early goal, red card, defensive-error cluster or late substitute-driven expansion produces 3-1/2-2+. | DG-P073-GOALS | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | C03 | **1st Half Under 1.5 goals** | `LEAN` | MEDIUM | Kaisar's likely compact start, draw propensity and reduced starting attacking ceiling support a 0-0/1-0 half. | Early Tobol set-piece/pressing goal followed by a second before halftime, or Kaisar counter creates a fast two-goal half. | DG-P073-GOALS | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | C04 | **Over 7.5 total corners — research contract** | `FORCED RANK` | LOW | Mid-range corner baselines, Tobol territorial edge and Kaisar low-block clearance pressure make 8+ plausible. | Early lead suppresses Tobol width/pressure; missing cross/block/end-line evidence means the mechanism is incompletely observed. | DG-P073-CORNERS | `CORRELATED_SECONDARY` | `NOT ACTIONABLE / NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Potential winner

**Tobol Kostanay — `LEAN`, MEDIUM evidence.** Central mechanism: home field plus the stronger current starting attacking configuration and Kaisar's weakened starting forward unit. Strongest failure path: Kaisar's compact/counter approach repeats its successful prior-season matchup path, with Tobol's attack lacking enough wide penetration without Chesnokov.

### Integrity / model status

- No validated soccer probability model ran; no internal probabilities are published.
- Current bookmaker prices and external forecast percentages are contextual only and are not treated as internal model outputs or value evidence.
- Corner pick is explicitly capped by the derivative-market completeness gate.
- Potential winner and 1X are related but not duplicate contracts: the winner call is an outright result lean, while C01 is a non-loss contract.

**Primary sources / evidence lanes:** Sports.kz live match protocol and confirmed XIs; FotMob current fixture/form; Kazhydromet Kostanay forecast; Betfred current market contracts; TotalCorner historical/recent corner records; CornerEdge current corner sample; FootyStats current team xG/corner context.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-074`.

---

## P-074 — Maccabi Herzliya U19 vs Hapoel Rishon LeZion U19 — PREGAME FORECAST

**Record/view:** `P-074/V01`  
**Decision set:** `DS-P074-V01`  
**Selection origin:** `SYSTEMATIC_UNIVERSE`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / qualitative soccer champion  
**Request/cutoff:** 2026-08-25 approximately 23:56 Australia/Melbourne / 16:56 Asia/Jerusalem  
**Competition:** Israel U19 Elite Division 2026/27, Round 3  
**Scheduled start:** 2026-08-25 17:00 Israel / 14:00 UTC / 2026-08-26 00:00 Australia/Melbourne  
**GAME-STATE:** `PREGAME` — multiple current fixture/market sources still showed the event as not started before the 14:00 UTC kickoff.

### Previous-log gate

`P-070` remained inside its live/unverified window; `P-071` and `P-072` remained delayed/not-started/open; `P-073` remained pregame with kickoff later than this cutoff. No open row was settled or rewritten. Only Prediction Log 2 was modified.

### Frozen candidate universe

Universe frozen before ranking from current Paddy Power/SoccerPunter market families plus one predeclared research corner threshold:

- Full-time 1X2
- Full-match totals 2.5 / 3.5 / 4.5
- First-half totals 0.5 / 1.5 / 2.5
- First team to score
- Total corners research thresholds 7.5 / 8.5 / 9.5

Current verified market examples: Maccabi Herzliya U19 ML 4/5 at Paddy Power; Under 3.5 goals 4/11; 1H Under 1.5 goals 1/2. Current SoccerPunter snapshot also had Maccabi Herzliya -125, draw +260, Hapoel Rishon +250 and Over 2.5 -142 / Under 2.5 +110. Prices are market context only, not internal probabilities or value evidence.

### Verified event / form evidence

- Current season table is very early: 17/171 league matches played. Maccabi Herzliya U19 have played one league match and lost 0-1 to Hapoel Tel Aviv U19; Hapoel Rishon LeZion U19 have played two and lost both, scoring 0 and conceding 4.
- Rishon lost 0-2 to Hapoel Haifa U19 on 15 Aug and 0-2 to Beitar Jerusalem U19 on 22 Aug.
- Most recent H2H: Hapoel Rishon LeZion U19 0-3 Maccabi Herzliya U19 on 16 May 2026, 0-0 at half-time, corners 6-7 (13 total).
- Previous H2H on 20 Jan 2026: Maccabi Herzliya U19 3-4 Hapoel Rishon LeZion U19, 2-1 at half-time, corners 3-5 (8 total). The two current-era meetings therefore show a wide scoring range and corner totals of 8 and 13; H2H is descriptive only.
- 2025/26 Maccabi Herzliya U19 league profile: 2.93 total goals per match overall, 3.6 at home; 62% Over 2.5, 62% Under 3.5 overall; 1H total-goal average 1.2 and 44% 0-0 half-time scoreline overall. These are last-season baselines, not current-season rates.
- Historical 2025/26 corner lane: Hapoel Rishon LeZion U19 matches averaged 8.65 total corners in one provider; 65% cleared 7.5, 61% cleared 8.5, 48% cleared 9.5. Maccabi Herzliya's last five recoverable 2026 matches had total corners 6, 13, 8, 7 and 5 (mean 7.8).
- Confirmed U19 starting XIs were not available from a field-owning source at cutoff. Participant/role evidence is therefore `NOT_AVAILABLE`, reducing confidence.
- Herzliya weather around 17:00 local was forecast near 29°C, dry, with moderate wind; no strong weather direction was applied.

### Goal-process forecast

The strongest current evidence points to a lower-output central branch than the high-scoring January H2H. Both teams are scoreless to begin 2026/27, Rishon have conceded two in each of their first two games, and the most recent direct meeting finished 3-0 after a 0-0 half. Maccabi Herzliya have the stronger current side/winner case, but early-season youth volatility and missing confirmed lineups prevent a high-confidence favourite call.

Qualitative central score corridor: `Maccabi Herzliya 1-0 / 2-0 / 2-1`, with `1-1` a meaningful draw branch. The major upper tail is a recurrence of the January open-game regime (3-4 type), which is explicitly retained rather than averaged away.

### Corner-process evidence

The recoverable corner data support a mid-range total around 8-10 rather than an extreme. Two current-era H2Hs produced 8 and 13 corners; Rishon's historical match average was 8.65 and Maccabi's recent recoverable five-match sequence averaged 7.8. This makes 8+ corners plausible.

However, decisive direct-event inputs required by RULES_SOCCER — current cross volume, blocked crosses, end-line entries, defensive clearances, width/set-play plan and exact bookmaker corner-provider definition — were not all available. Therefore any corner row is capped at `FORCED RANK` / LOW evidence and is research-grade only.

### Scenario map

| Scenario | Mechanism | Main contract effect |
|---|---|---|
| Lower-output | Both attacks continue slow 2026/27 starts; Maccabi control without forcing tempo | Strong for Under 3.5 and 1H Under 1.5; Maccabi ML can win 1-0/2-0. |
| Central | Maccabi create more territory and eventually score; Rishon remain limited | Strongest for top three ranks; corners can build through Rishon defending. |
| Draw branch | Maccabi finishing remains weak and Rishon improve defensively | Hurts Maccabi ML while preserving both Under rows. |
| Open-game tail | Youth errors, early goal or transition game recreates January 3-4 regime | Main kill path for both Under rows; helps corner Over. |
| Corner-suppression tail | Early lead reduces attacking width and both sides attack centrally | Main kill path for Over 7.5 corners. |

### Frozen ranking

| Rank | Candidate | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | C01 | **Under 3.5 total goals** | `LEAN` | MEDIUM | Both teams are scoreless so far in 2026/27; Rishon's two losses were both 0-2, and the latest H2H was a controlled 0-3 rather than an open shootout. | Early goal/youth-error cluster recreates the January 3-4 tail. | DG-P074-GOALS | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | C02 | **1st Half Under 1.5 goals** | `LEAN` | MEDIUM | Maccabi's prior-season 1H profile was draw/low-output heavy and the latest direct meeting was 0-0 at HT; current attacks have opened slowly. | Two early defensive errors or an early goal that forces immediate response. | DG-P074-GOALS | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | C03 | **Maccabi Herzliya U19 ML** | `LEAN` | MEDIUM-LOW | Current market, latest 3-0 H2H and Rishon's 0-2, 0-2 start all point to a modest Maccabi side edge. | Maccabi's own scoreless start persists or Rishon recover enough attacking quality to exploit youth-game variance. | DG-P074-SIDE | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | C04 | **Over 7.5 total corners — research contract** | `FORCED RANK` | LOW | Current-era H2Hs landed at 8 and 13; Rishon's historical 7.5+ rate and Maccabi's recent corner sequence make 8+ plausible. | Missing current cross/block/end-line/clearance data; an early lead may suppress width and corner demand. | DG-P074-CORNERS | `CORRELATED_SECONDARY` | `NOT ACTIONABLE / NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Potential winner

**Maccabi Herzliya U19 — `LEAN`, MEDIUM-LOW evidence.** Central mechanism: Rishon's scoreless 0-2/0-2 start plus Maccabi's 3-0 win in the most recent meeting and current home-favourite market position. Strongest failure path: Maccabi's own weak opening attack and youth-level lineup uncertainty keep the draw/upset branch meaningful.

### Integrity / model status

- No validated soccer probability model ran; no internal probabilities are published.
- Youth/reserve population is treated separately from senior football; last-season and H2H data are descriptive and down-weighted.
- Confirmed starting XIs were not available from an authoritative source at cutoff.
- Corner pick is explicitly capped by the derivative completeness gate and is research-grade only.
- Current prices are external market context, not value evidence.

**Sources:** SoccerPunter current fixture/odds and H2H; Paddy Power current market page; FootyStats current 2026/27 table and 2025/26 Maccabi profile; 365Scores current round results; TotalCorner H2H/recent corners; OddAlerts historical U19 corner table; weather source cross-check.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-075`.

---

## P-075 — OKS vs Middelfart — PREGAME FORECAST

**Record/view:** `P-075/V01`  
**Decision set:** `DS-P075-V01`  
**Selection origin:** `SYSTEMATIC_UNIVERSE`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / qualitative soccer champion  
**Request/cutoff:** 2026-08-26 approximately 01:16 Australia/Melbourne / 2026-08-25 17:16 Europe/Copenhagen  
**Competition:** DBU Pokalen / Betano Pokalen 2026/27, Round 2 (1/32-final)  
**Venue:** OKSON-Park, Odense, Denmark  
**Scheduled start:** 2026-08-25 17:30 Europe/Copenhagen / 15:30 UTC / 2026-08-26 01:30 Australia/Melbourne  
**GAME-STATE:** `PREGAME` — Middelfart Boldklub's official fixture page listed the match for 17:30 local and current match/odds pages remained in pre-match state at cutoff.

### Previous-log gate

No earlier open Prediction Log 2 event had a newly verified authoritative final at this cutoff. P-070 remained unresolved; P-071/P-072 had no verified completed result; P-073/P-074 had crossed scheduled kickoff but no authoritative final was verified. They remain open and were not graded or rewritten. Only Prediction Log 2 was modified.

### Frozen candidate universe

Universe frozen before ranking from currently visible pre-match market families plus one predeclared corner research threshold:

- Full-time 1X2
- Double chance
- Full-match goal totals 1.5 / 2.5 / 3.5 / 4.5 / 5.5
- First team to score
- Draw no bet
- Both teams to score
- Total corners research threshold 9.5

SportyTrader's current odds comparison verified the existence of 1X2, double chance, goal totals, first-team-to-score, DNB and BTTS markets. Forebet exposed a 9.5 total-corners research threshold. No exact sportsbook/operator corner contract or settlement-provider definition was captured, so the corner row is research-grade only and not value-actionable.

### Identity, participants and current context

- Middelfart Boldklub's official site lists the cup fixture at OKSON-Park, 17:30 local.
- OKS play in the Danmarksserien; Middelfart play in the CampoBet 2. Division, creating a meaningful competition-level prior in Middelfart's favour.
- Middelfart's official 2026/27 sequence before this match: 4-1 Thisted, 2-0 Bredballe in the cup, 4-0 Brabrand, 1-1 at Roskilde, 2-3 vs Nykøbing. The club's coach had described the early-season offensive expression and chance creation as strong before the Nykøbing loss.
- Middelfart's first cup-round win at Bredballe came 2-0 despite a rotated XI, showing some depth but not proving rotation is harmless.
- New midfielder Hjalte Hemmingsen is officially eligible to make his first appearance in this match.
- OKS's current 2026 league/cup sequence includes 2-1 at Varde in the cup, 0-3 vs SfB-Oure, 1-6 at Odder and 4-1 vs Horsens FS. This implies both a meaningful scoring ceiling and a large defensive-collapse branch.
- Confirmed starting XIs were not found from a field-owning source before cutoff. Participant/rotation state is therefore `NOT_AVAILABLE`; this is the main evidence limitation.
- Match-window conditions in Odense were forecast around 22-23°C and dry/sunny with moderate wind. No strong weather total adjustment is applied.

### Goal-process forecast

The central regulation branch is sustained Middelfart territorial and shot-quality superiority. The competition-level gap, stronger recent attacking process and OKS's repeated multi-goal concessions support Middelfart control. Cup rotation is explicitly mixed into the scenario rather than ignored: Middelfart have a league match again on 29 August and may distribute minutes, but their previous cup rotation still produced a controlled 2-0 win.

Qualitative central score corridor: `OKS 0-2 / 0-3 / 1-3 Middelfart`, with `1-2` a meaningful tighter branch. The main structural upset path is heavy Middelfart rotation plus an early OKS goal/set-piece that converts the tie into a chaotic cup game.

### Corner-process evidence

The corner evidence is weaker than the goal/side evidence. Forebet's current page exposes an Under/Over 9.5 corner target and a low aggregate corner expectation in its current data panel, but it is an external analytical source and its coverage is not sufficient to own settlement or the full corner mechanism. Direct match-specific cross volume, blocked-cross rate, end-line entries, defensive clearances, set-play profile and exact bookmaker corner-provider definition were not all available.

Under RULES_SOCCER's derivative completeness gate, the corner row is capped at `FORCED RANK` / LOW evidence regardless of the directional lean.

### Scenario map

| Scenario | Mechanism | Main contract effect |
|---|---|---|
| Middelfart control | Class gap + stronger possession/chance creation; OKS defend deep | Strong for X2, Middelfart ML and Over 1.5; corners can remain moderate if goals arrive efficiently. |
| Central | Middelfart lead by 1-2 goals, OKS contribute little or one transition goal | Strongest overall branch: 0-2, 0-3, 1-2, 1-3. |
| Rotation-tight | Middelfart rotate heavily and play more conservatively | X2 still robust; ML weakens slightly; 1-0/2-0 reduces Over-2.5 but still supports Over 1.5 except 1-0. |
| Cup-upset tail | OKS score first, Middelfart finishing is poor, set-piece/transition variance spikes | Main kill path for Middelfart ML and X2. |
| Corner-expansion tail | Middelfart dominate without converting, generating repeated crosses/blocks/clearances | Main kill path for Under 9.5 corners. |

### Frozen ranking

| Rank | Candidate | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | C01 | **Middelfart or Draw — X2 (90 min)** | `SUPPORTED` | MEDIUM-HIGH | Clear competition-level and current-process edge; it survives a draw and most rotation scenarios. | Heavy rotation + early OKS goal + cup variance produces an outright OKS win. | DG-P075-SIDE | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | C02 | **Over 1.5 total goals (90 min)** | `SUPPORTED` | MEDIUM-HIGH | Every recent listed OKS league/cup match and Middelfart's recent scoring environment support at least two-goal exposure; central corridor is 2-4 goals. | A 0-1/1-0 type cup grind caused by rotation and inefficient finishing. | DG-P075-GOALS | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | C03 | **Middelfart ML — 90 min** | `SUPPORTED` | MEDIUM | Stronger division, stronger current attack, recent cup control and market consensus all point to the away side. | Cup rotation narrows the quality gap; OKS convert first and protect the lead or force a draw. | DG-P075-SIDE | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | C04 | **Under 9.5 total corners — research contract** | `FORCED RANK` | LOW | External current corner panel points to a moderate rather than extreme count; efficient Middelfart scoring can reduce sustained corner demand. | Middelfart dominate territory but finish poorly, creating repeated blocks/clearances and double-digit corners. Direct corner-causation evidence is incomplete. | DG-P075-CORNERS | `CORRELATED_SECONDARY` | `NOT ACTIONABLE / NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Contract geometry / dependence

- C01 and C03 are strongly dependent side expressions. Middelfart ML implies X2; X2 also wins on a draw.
- C02 is linked to the same Middelfart-attacking-strength thesis but is not identical: a 1-0 Middelfart win makes C01/C03 win and C02 lose.
- C04 uses a separate corner target process and is not inferred directly from possession/goals.
- Current external prices verify market availability only. Without a validated calibrated probability model, no +EV/value claim is permitted.

### Potential winner

**Middelfart — `SUPPORTED`, MEDIUM evidence (90-minute winner).** Central mechanism: materially stronger competition level and recent attacking process, plus demonstrated ability to control a lower-level cup opponent even with rotation. Strongest failure path: unverified starting XI/rotation substantially weakens the away side and an early OKS goal creates a high-variance cup state.

### Integrity / model status

- No validated soccer probability model ran; no internal probabilities are published.
- Confirmed starting XIs were not verified before cutoff and are explicitly treated as missing.
- Corner selection is capped by the derivative completeness gate and is research-grade only.
- External bookmaker prices and external forecast percentages are context/market verification, not internal model probabilities.
- Winner refers to the 90-minute result; qualification/extra-time is a distinct contract and was not substituted.

**Primary evidence lanes:** Middelfart Boldklub official fixture, match reports and squad news; FotMob current competition/team state; SportyTrader current market availability; Forebet current corner research panel; Scores24 current form/corner context; DMI/Met Office weather cross-check.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-076`.

---

## P-076 — FK Horní Ředice vs FK Dukla Praha — PREGAME FORECAST

**Record/view:** `P-076/V01`  
**Decision set:** `DS-P076-V01`  
**Selection origin:** `SYSTEMATIC_UNIVERSE`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / qualitative soccer champion  
**Request/cutoff:** 2026-08-26 approximately 01:20 Australia/Melbourne / 2026-08-25 approximately 17:20 Europe/Prague  
**Competition:** MOL Cup 2026/27, Round 2  
**Venue:** Fotbalový stadion FK Horní Ředice, Horní Ředice, Czechia  
**Scheduled start:** 2026-08-25 17:30 Europe/Prague / 15:30 UTC / 2026-08-26 01:30 Australia/Melbourne  
**GAME-STATE:** `PREGAME` — Onlajny.com and TN.cz both showed 0:0 / pre-match with the online feed not yet started at final refresh.

### Previous-log gate

- `P-070` was verified LIVE at 62' with El Porvenir Reserves leading Central Ballester Reserves 1-0; it remains open and was not graded.
- No other prior open Prediction Log 2 event had a newly verified authoritative final at this cutoff. Existing delayed/live/pregame entries remain open and immutable.
- Only Prediction Log 2 was modified.

### Frozen candidate universe

Universe frozen before ranking from the current Betfred market plus one predeclared corner research contract:

- Match result / double chance
- Full-match total goals: 2.5 / 3.5 / 4.5
- Both teams to score
- Draw no bet
- Three-way handicaps: Dukla -1 / -2
- Total corners research threshold: 9.5

Current Betfred market snapshot at access: Horní Ředice 10/1, draw 5/1, Dukla Praha 1/6; X2 1/28; Over 2.5 1/3; Under 4.5 1/3; Dukla -1 three-way 8/15; Dukla -2 three-way 13/10. An external current corner market panel exposed Under 9.5 corners around 1.80, but the exact operator/provider definition was not independently verified. Prices are market-context/contract-availability evidence only, not internal probabilities or value claims.

### Verified identity and current context

- Dukla's official club site confirms this as a MOL Cup Round 2 away fixture at Horní Ředice, 17:30 local.
- Horní Ředice are a newly promoted third-tier side. Their first two 3. liga matches produced 0-2 at Jablonec B and 0-6 at home to Mladá Boleslav B, with no league goal scored yet.
- Their cup form is materially stronger than their league start: 3-0 at Sparta Kolín and 3-0 at home to MFK Chrudim. Onlajny notes that they also eliminated second-tier Vlašim last season and pushed top-flight Slovácko before losing 1-2, so the underdog cup-upset branch is real and cannot be dismissed as class-gap noise.
- Dukla are a second-tier Chance Národní Liga club, currently seventh in the table snapshot. Their league start included 2-0 wins over Česká Lípa and Kroměříž plus a 2-2 draw at Táborsko, followed by consecutive 1-3 losses to Slavia Prague B and Ústí nad Labem.
- Dukla opened this cup run with a controlled 3-0 away win at fourth-tier Vykáň.
- Confirmed starting XIs were not available from an authoritative source at the cutoff; accessible lineup pages still stated that lineups would be added shortly before the match. Rotation is therefore the largest unresolved participant variable.
- FotMob listed the grass venue and about 24°C conditions. No verified severe weather mechanism was found; weather receives no strong directional weight.

### Goal-process forecast

The base regulation branch favours Dukla because of the one-tier class advantage, deeper professional squad and stronger underlying attacking ceiling. However, Horní Ředice have repeatedly raised their level in this competition and already defeated a recently second-tier Chrudim side 3-0, while Dukla arrive after two 1-3 league defeats. The side gap is therefore meaningful but not treated as deterministic.

Qualitative central score corridor: `Horní Ředice 0-2 / 1-2 / 0-3 / 1-3 Dukla Praha`.

This creates a strong 2-4 goal central band: Over 2.5 and Under 4.5 can both win on 3 or 4 total goals. The main high-total tail is an early Dukla goal followed by a widened cup game; the main low-total/upset tail is rotation plus Horní Ředice's compact cup state producing 0-1, 1-1 or 1-0 deep into the match.

### Corner-process evidence

Corner evidence is materially weaker than the side/goal evidence.

- A current historical panel reports Horní Ředice matches averaging about 9.69 total corners across 13 recent matches, with Over 9.5 occurring only 31% in that sample; their 2026-08-09 match at Jablonec B had 15 total corners (6-9) and their cup win at Sparta Kolín had 7 (5-2).
- Dukla's official 2026-08-21 match at Ústí produced 10 total corners (5-5); other official Dukla senior matches show a broad range around 4-11 total corners.
- Mechanistically, a Dukla territorial edge could raise Horní Ředice clearance/block exposure, but an efficient early Dukla lead could reduce later width and corner demand.
- Current direct cross volume, blocked-cross rate, end-line entries, defensive-clearance rate, set-play share and the exact bookmaker corner-provider definition were not all available.

Under RULES_SOCCER's derivative completeness gate, the corner row is capped at `FORCED RANK` / LOW evidence regardless of direction.

### Scenario map

| Scenario | Mechanism | Main contract effect |
|---|---|---|
| Dukla control | Professional depth + class edge, patient possession, stronger shot quality | Strong for X2 and Dukla ML; 0-2/0-3 supports goal corridor. |
| Central competitive cup tie | Horní Ředice compete physically and create one scoring phase, but Dukla retain quality edge | 1-2/1-3; supports X2, Dukla ML and Over 2.5. |
| Rotation-tight | Dukla rotate heavily and reduce attacking fluency | X2 remains robust; ML/Over 2.5 weaken; 0-1 or 1-1 becomes more plausible. |
| Horní Ředice cup-upset tail | Home set piece/counter converts first; Dukla's recent defensive instability persists | Main kill path for Dukla ML; X2 can still survive a draw. |
| Open-game/blowout tail | Early Dukla goal forces Horní Ředice forward and creates repeated transitions | Helps Over 2.5; threatens Under 4.5 and can expand corners. |
| Efficient-favourite state | Dukla score from a small number of high-quality attacks, then manage tempo | Supports side picks but can suppress corners below 9.5. |

### Frozen ranking

| Rank | Candidate | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | C01 | **Draw or FK Dukla Praha — X2 (90 min)** | `SUPPORTED` | MEDIUM-HIGH | One-tier class/depth edge while retaining draw protection; robust to moderate rotation and a competitive cup tie. | Horní Ředice repeat their strong cup upset pattern and win outright inside 90 minutes. | DG-P076-SIDE | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | C02 | **FK Dukla Praha ML — 90 min** | `LEAN` | MEDIUM | Stronger squad and professional-level attacking ceiling should create more high-quality scoring phases across 90 minutes. | Rotation plus Horní Ředice's proven cup resilience produces a draw or home upset. | DG-P076-SIDE | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | C03 | **Over 2.5 total goals — 90 min** | `LEAN` | MEDIUM | Central score corridor is mostly 3-4 goals; recent Horní league volatility and Dukla's last two 1-3 defeats preserve an open-game branch. | Rotated Dukla control without tempo plus Horní attacking suppression creates 0-1/0-2/1-1. | DG-P076-GOALS | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | C04 | **Under 9.5 total corners — research contract** | `FORCED RANK` | LOW | Horní recent corner sample sits near the boundary but has cleared 9.5 infrequently; efficient favourite scoring can reduce sustained crossing/corner pressure. | Dukla territorial dominance without early conversion creates repeated blocks/clearances and 10+ corners. Direct corner-causation inputs/provider definition are incomplete. | DG-P076-CORNERS | `CORRELATED_SECONDARY` | `NOT ACTIONABLE / NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Contract geometry / dependence

- C01 and C02 are strongly dependent side expressions: every Dukla 90-minute win makes both win, while a draw wins C01 and loses C02.
- C03 is related to the class-gap/open-game thesis but is not a duplicate; a controlled 0-2 Dukla win makes C01/C02 win and C03 lose.
- C04 is a separate corner target and is not inferred mechanically from goals or possession.
- Potential winner is an alias of the same 90-minute side thesis as C02 rather than an independent extra observation.

### Potential winner

**FK Dukla Praha — `LEAN`, MEDIUM evidence (90-minute winner).** Central mechanism: superior professional depth and class should produce the better shot-quality distribution over 90 minutes. Strongest failure path: Horní Ředice's demonstrably strong MOL Cup regime plus unverified Dukla rotation creates another upset or draw.

### Integrity / model status

- No validated soccer probability model ran; no internal probabilities are published.
- Confirmed XIs were unavailable at cutoff and are explicitly treated as missing rather than inferred.
- The corner selection is research-grade only and capped by the derivative-market completeness gate.
- Market prices verify contract availability/context only; no +EV/value claim is made.
- Winner means the 90-minute result. Qualification after extra time/penalties is a separate endpoint and was not substituted.

**Primary evidence lanes:** FK Dukla Praha official fixture/news/results; FK Horní Ředice official schedule/results; Onlajny.com pre-match live centre and historical cup context; Betfred current contract market; FotMob current venue/form; official Dukla match reports for recent corner counts; current historical corner panel for Horní Ředice.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-077`.

---

## P-077 — Vincent Weaver vs Aryan Jit Singh — PREGAME FORECAST

**Record/view:** `P-077/V01`  
**Decision set:** `DS-P077-V01`  
**Selection origin:** `SYSTEMATIC_UNIVERSE`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / qualitative tennis general-module champion  
**Request/cutoff:** 2026-08-26 approximately 01:26 Australia/Melbourne  
**Competition:** UTR PTT Clemson Men 02  
**Venue:** Duckworth Family Tennis Facility, Clemson, South Carolina, USA  
**Surface:** Outdoor hard  
**GAME-STATE:** `PREGAME` — current Betfair/AiScore/Betmaster pages still listed Weaver–Singh as an upcoming event with no live score. Displayed start times conflict across third-party/localised feeds, so no single timezone-normalised scheduled time is treated as authoritative.

### Previous-log gate

No new prior event was graded at this cutoff. P-075 and P-076 were still pre-kick at the user's 01:26 Melbourne request time; P-070 remained without a trustworthy verified final in the accessible sources checked. Existing open records remain immutable. Only Prediction Log 2 was appended.

### Frozen candidate universe

Frozen before ranking from the exact currently visible Betfair markets:

- Match winner: Vincent Weaver / Aryan Jit Singh
- Set 1 winner: Vincent Weaver / Aryan Jit Singh
- Set 2 winner: Vincent Weaver / Aryan Jit Singh

Betfair's current page listed both match-winner prices at 5/6, both Set 1 prices at 5/6, and Set 2 at Weaver 10/11 versus Singh 4/5. These prices verify contract availability only and are not internal probabilities or value evidence. No exact handicap or total-games threshold was recoverable reliably enough to freeze, so none was invented.

### Verified player/context evidence

- UTR PTT Clemson Men 02 is a hard-court event in Clemson; current fixtures and match pages list Weaver–Singh as upcoming.
- Aryan Jit Singh is 20/21, right-handed, with a broader recent adult UTR/ITF sample. Tennis Explorer lists a 2026 singles record of 5-8 overall; his recent UTR Bengaluru sequence includes wins over Kevin Titus Suresh and Deep Munim, a three-set loss to Neeraj Yashpaul, and a 2-0 loss to Dev Javia.
- In his first Clemson match Singh lost to Tarun Karra 4-6, 7-6, 3-6, showing he remained competitive enough to force a deciding set.
- Vincent Weaver is a high-level U.S. junior from Roswell, Georgia. TennisRecruiting listed him 45-19 overall and #74 on its current TennisRPI, with strong recent national-junior results.
- Weaver's first Clemson match ended in a 0-2 loss to Henrik Bladelius. Bladelius had been a very strong pre-match favourite, so the straight-set loss is negative current-tournament evidence but not proof Weaver is below Singh.
- No prior Weaver–Singh H2H was found in the accessible current sources.
- Both players competed the previous day. Singh's match went three sets, giving Weaver a small workload/rest edge; Singh has the larger recent adult-match experience advantage.

### Match-process assessment

This is close to a genuine 50/50 match. Singh's edge is adult competitive exposure and evidence that he can sustain a three-set UTR match against a credible opponent. Weaver's counter-edge is strong junior-level performance, local/home-country environment, and likely lower workload from a straight-set opener.

The central qualitative branch is a competitive two- or three-set match rather than a one-sided sweep. Singh receives only a narrow overall lean because his more transferable recent adult match sample slightly outweighs Weaver's junior record, but the market's even pricing is consistent with substantial uncertainty.

### Scenario map

| Scenario | Mechanism | Main contract effect |
|---|---|---|
| Singh experience edge | Better adult UTR/ITF rhythm, handles longer baseline exchanges and pressure points | Supports Singh ML and Singh set markets. |
| Weaver fast-start | Fresher legs, home-country environment, aggressive junior form | Main threat to Singh Set 1; can become full-match upset path. |
| Long match | Both hold level through one set each | Favors whichever player manages fatigue/second-serve pressure better; Singh's adult experience modestly helps. |
| Weaver ceiling | Junior ranking translates fully to this field and prior Bladelius result was opponent-strength driven | Main kill path for Singh ML. |
| Singh fatigue | Three-set Karra match carries over physically | Helps Weaver especially in Set 1/late second set. |

### Frozen ranking

| Rank | Candidate | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | C01 | **Aryan Jit Singh — Match Winner** | `LEAN` | MEDIUM | Older player with broader adult UTR/ITF experience and competitive three-set Clemson opener; slightly more transferable current evidence. | Weaver's strong junior level translates immediately and Singh carries fatigue from the Karra match. | DG-P077-SINGH | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | C02 | **Aryan Jit Singh — Set 2 Winner** | `LEAN` | MEDIUM-LOW | Singh showed recovery/adjustment by winning Set 2 against Karra after dropping Set 1; adult match experience may matter once patterns settle. | Weaver starts well and maintains serving/return pressure through the second set; one-match adjustment evidence is thin. | DG-P077-SINGH | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | C03 | **Aryan Jit Singh — Set 1 Winner** | `FORCED RANK` | LOW-MEDIUM | Same overall experience edge, but opening-set uncertainty is high and the current market prices this exactly even. | Weaver's fresher legs and faster start overwhelm Singh before he settles. | DG-P077-SET1 | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | C04 | **Vincent Weaver — Match Winner** | `FORCED RANK` | MEDIUM-LOW | Strong 45-19 junior record, #74 TennisRPI and home-country setting create a credible upset/win path in an evenly priced match. | Singh's adult match maturity and recent UTR competitiveness prove more transferable than Weaver's junior results. | DG-P077-MATCH-OPPOSITE | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Contract geometry / dependence

- C01 and C04 are exact opposite match-winner contracts; one wins if the match completes normally under matching retirement terms.
- C02 and C03 are strongly correlated with C01 but are separate set-level targets.
- Set 1 and match winner are not interchangeable: Weaver can win Set 1 and still lose the match, and vice versa.
- Because no operator/retirement rules were supplied, retirement/walkover settlement remains `UNKNOWN_DEFINITION` outside the exact Betfair snapshot used to verify availability.

### Potential winner

**Aryan Jit Singh — `LEAN`, MEDIUM evidence.** Central mechanism: more recent adult UTR/ITF exposure and a competitive three-set opener give him a small transferable-performance edge. Strongest failure path: Weaver's high junior level, fresher workload and home-country environment translate into better first-strike hard-court tennis than Singh's recent adult results suggest.

### Integrity / model status

- No validated tennis probability model ran; no internal probabilities are published.
- Tennis is handled under RULES_GENERAL's brief module: surface, format, retirement terms, serve/return quality, workload and matchup are required; no generic ranking-only forecast is used.
- Exact handicap/total-game lines were not sufficiently recoverable, so none was invented.
- Current bookmaker prices verify market existence/context only; no +EV/value claim is made.
- Confidence is intentionally capped because the matchup market is essentially even and Weaver's adult-level data sample is sparse.

**Primary evidence lanes:** Betfair current match/set markets; Betmaster current event listing; AiScore current schedule and prior Clemson results; Scores24 Clemson event/venue/surface pages; TennisRecruiting current Weaver activity/record; Tennis Explorer and ITF current Singh profile/results.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-078`.

---

## P-078 — SK Brann (W) vs FK Austria Wien (W) — PREGAME FORECAST

**Record/view:** `P-078/V01`  
**Decision set:** `DS-P078-V01`  
**Selection origin:** `USER_SUPPLIED + PREDECLARED RESEARCH ADDITIONS`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / qualitative soccer champion  
**Request/cutoff:** 2026-08-26 01:49 Australia/Melbourne / 2026-08-25 17:49 Europe/Oslo  
**Competition:** UEFA Women's Champions League 2026/27, Third Qualifying Round, first leg  
**Venue:** Brann Stadion, Bergen, Norway — natural grass  
**Scheduled start:** 2026-08-25 18:00 Europe/Oslo / 16:00 UTC / 2026-08-26 02:00 Australia/Melbourne  
**GAME-STATE:** `PREGAME` — Brann and Austria Wien official fixture pages still showed the first leg scheduled for 18:00 local; no verified goal/clock had begun at the final refresh.

### Previous-log gate

- `P-073` Tobol–Kaisar was found listed as postponed/suspended in current sources and remains open without grading.
- No authoritative final was verified for `P-074` at this cutoff; it remains open.
- `P-075` and `P-076` had kicked off recently and remain live/open rather than retrospectively graded.
- `P-077` remained an upcoming tennis event in the last verified state.
- No prior result was settled in this append. Only Prediction Log 2 was modified.

### Frozen target / contract manifest

**Tie state:** first leg of a two-leg UEFA Women's Champions League third qualifying round. This card ranks the **90-minute first-leg match only**. Qualification/advance after the second leg is a separate endpoint.

**User-supplied target families:**
- `P078-T01-1H-GOALS`: first-half combined goals, exact line 0.5.
- `P078-T02-FT-GOALS`: 90-minute combined goals, exact line 1.5.

**Predeclared research additions:**
- `P078-T03-RESULT`: 90-minute double chance, Brann or Draw (1X), verified in current market listings.
- `P078-T04-CORNERS`: 90-minute total corners, research threshold Over 7.5; current historical matchup market/stats pages expose the 7.5 threshold, but exact sportsbook/provider settlement definition was not supplied.

### Verified current evidence

- Brann are first in the 2026 Toppserien at 12-2-0 with a 45-4 goal difference after 14 matches. Their recent competitive sequence includes 5-0 Mitrovica, 3-2 PAOK, 3-0 Hønefoss and 5-1 Røa.
- Brann's UWCL Q2 matches both had first-half goals: 4-0 at halftime against Mitrovica and 1-1 at halftime against PAOK. The Hønefoss league win was 2-0 at halftime.
- Austria Wien are the reigning Austrian champions/double winners. Their current competitive sequence includes 3-2 Hajduk Split (3-1 HT), 5-0 Farul Constanța (2-0 HT), 2-0 LASK (0-0 HT), and 7-0 Red Bull Salzburg (5-0 HT).
- Austria's Farul win produced two corners inside the first two minutes, 32 shots, and an eventual 11-3 corner count; Modesta Uka repeatedly attacked from wide areas.
- Brann's current European attacking references include the wing pair Lauren Davidson and Diljá Zomers; Zomers scored four goals across the Q2 mini-tournament. Brann produced 13-0 corners vs Mitrovica but only 3-0 vs PAOK, showing large corner-state variance.
- UEFA's official squad list included Brann's Skoglund, Kvamme, Haugland, Eikeland, Zomers, Aahjem and Davidson and Austria's Pal, Kirchberger, Hanshaw, Schiechtl, Pfanner, Uka and others. A confirmed starting XI was not recoverable from an authoritative source before this cutoff, so exact starter/substitution exposure remains an uncertainty.
- Bergen match-window weather was forecast dry with very low precipitation probability and light winds; no meaningful weather suppression is applied.

### Goal-process assessment

This is a strong-team-versus-strong-team first leg rather than a class mismatch. Brann have the stronger domestic 2026 profile and home venue, while Austria are reigning Austrian champions and arrive with high current attacking output. Both Q2 campaigns showed that the teams can create early, but both also have strong defensive central branches.

**Qualitative central score corridor:** `Brann 2-1 / 2-0 / 1-1 Austria Wien`, with `3-1` as a higher-scoring Brann branch and `0-1` as the principal low-total away-upset branch.

The two supplied goal lines are nested across different horizons, not independent confirmations. An early goal supports both 1H Over 0.5 and FT Over 1.5, but a single first-half goal followed by a controlled second half can win the 1H contract while losing FT Over 1.5.

### Corner-process assessment

Corner direction is less reliable than the goal/side direction.

Available direct evidence supports attacking width and set-piece exposure: Austria won two corners inside two minutes against Farul and finished that match 11-3 on corners; Brann's Mitrovica match finished 13-0 on corners. But Brann–PAOK produced only three total corners despite five goals, demonstrating the danger of treating territorial dominance or scoring as a direct corner proxy.

Current cross frequency, blocked-cross rate, opponent-conceded corner rates in matched populations, end-line entries, defensive-clearance rates and exact sportsbook corner-provider definitions were not all verified. Under the soccer derivative completeness gate, C04 is therefore capped at `FORCED RANK` / LOW evidence.

### Scenario map

| Scenario | Mechanism | Main contract effect |
|---|---|---|
| Brann home control | Toppserien-leading attack, strong home territory, Davidson/Zomers width | Strong for 1X and supports O1.5; can raise corners if Austria defend deep. |
| Competitive first leg | Austria's champion-level structure and Uka/Pfanner threat keep game balanced | 1-1/2-1 supports O1.5 and 1X; early goal often supports 1H O0.5. |
| Cautious tie-state | Both teams respect second leg and avoid early transition exposure | Main kill path for 1H O0.5 and O1.5; 0-0/1-0 type branch. |
| Austria counter/upset | Brann overcommit at home; Austria convert first through transition/set play | Main kill path for Brann 1X. |
| High-corner pressure | Brann territorial pressure + Austria clear/block repeatedly | Supports O7.5 corners. |
| Efficient-finishing state | Goals arrive from few attacks/set pieces | Goal picks can win while corner O7.5 loses. |

### Frozen ranking

| Rank | Candidate | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | C01 | **SK Brann or Draw — 1X (90 min)** | `SUPPORTED` | MEDIUM-HIGH | Brann are unbeaten domestically, own the stronger current league profile and have home-field protection; a draw also wins. | Austria's current attacking form translates fully and they win the first leg outright. | DG-P078-SIDE | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | C02 | **Combined Total — Over 1.5 Goals (90 min)** | `SUPPORTED` | MEDIUM-HIGH | Both attacks enter in strong form; all four Q2 UWCL matches across the two teams cleared 1.5, and central branches cluster at 2-3+ goals. | First-leg caution plus strong goalkeeping/finishing regression produces 0-0, 1-0 or 0-1. | DG-P078-GOALS | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | C03 | **1st Half Goals — Over 0.5** | `LEAN` | MEDIUM | Both Brann Q2 UWCL matches had first-half scoring; Austria's Hajduk, Farul and Salzburg matches also had early goals, with only LASK 0-0 at HT in the recent four-match sequence. | Two-leg caution creates a probing first half and the game opens only after the break. | DG-P078-1H | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | C04 | **Total Corners — Over 7.5 (research contract)** | `FORCED RANK` | LOW | Both sides have direct recent high-corner examples and identifiable wide attacking mechanisms; 8+ is plausible in a territorial first leg. | Efficient finishing, narrow central attacks or early game control suppress repeated blocks/clearances; decisive direct corner inputs/provider definition are incomplete. | DG-P078-CORNERS | `CORRELATED_SECONDARY` | `NOT ACTIONABLE / NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Contract geometry / dependence

- User-supplied 1H Over 0.5 and 1H Under 0.5 are exact complements for the frozen first-half target; C03 selects the Over branch.
- User-supplied FT Over 1.5 and Under 1.5 are exact complements for the frozen 90-minute goal target; C02 selects the Over branch.
- C02 and C03 are positively dependent through the early-goal thesis but are not aliases.
- C01 is a side/result target and can win in low- or high-scoring states.
- C04 is a separate corner target; goals/possession are context only and are not substituted for corner-event labels.

### Potential winner

**SK Brann — `LEAN`, MEDIUM evidence (90-minute first-leg winner).** Central mechanism: stronger current domestic profile, Brann Stadion home effect and sustained attacking depth. Strongest failure path: Austria's reigning-champion structure and fast-start attacking form exploit Brann's aggressive home state. The draw remains materially live, which is why C01 (1X) ranks above the outright winner call.

### Integrity / model status

- No validated soccer probability model ran; no internal percentages are published.
- Starting XIs were not verified from an authoritative source at cutoff; official UEFA squad lists were available and used only for availability context.
- Exact corner provider/definition and complete target-event chain were unavailable, so the corner row is capped at `FORCED RANK` / LOW evidence.
- Market prices/league-average odds from external pages are contract-availability/context evidence only; no +EV/value claim is made.
- This is the first leg only. Qualification/advance is not treated as equivalent to the 90-minute winner.

**Primary evidence lanes:** Brann official fixture/results/coach preview; FK Austria Wien official fixtures/news; UEFA official squad lists; current FootyStats market/goal/corner threshold pages; SoccerZZ match statistics for recent UWCL corner examples; Met Office Bergen forecast.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-079`.

---

## P-079 — Abha vs Al Khaleej Saihat — PREGAME

**Append time / cutoff:** 2026-08-26 01:54 Australia/Melbourne / 2026-08-25 18:54 Asia/Riyadh  
**Method:** `MDS-2026.08.24-v2.1` qualitative soccer champion  
**Competition:** Roshn Saudi League 2026/27, Matchweek 3  
**Venue:** Prince Sultan Bin Abdul Aziz Sport City Stadium, Abha  
**Scheduled start:** 2026-08-25 19:05 Asia/Riyadh / 16:05 UTC / 2026-08-26 02:05 Australia/Melbourne  
**GAME-STATE:** `PREGAME` — SAFF and SPL both listed the match as the next Matchweek 3 fixture; no authoritative live score/clock was present at the final refresh.

### Previous-log gate

- P-070 through P-074 were rechecked. No new authoritative final suitable for settlement was verified from the current accessible sources, so no retrospective grade was appended.
- P-075 and P-076 had already crossed kickoff and remain live/open rather than being graded.
- P-077 and P-078 remained pregame/upcoming at their latest verified states.
- Only Prediction Log 2 was modified.

### Frozen target / contract manifest

**User-supplied exact targets:**
- `P079-T01-1H-GOALS`: first-half combined goals, line 0.5. Both Over and Under frozen; selected branch C03 = Over 0.5.
- `P079-T02-FT-GOALS`: 90-minute combined goals, line 1.5. Both Over and Under frozen; selected branch C01 = Over 1.5.

**Predeclared research additions:**
- `P079-T03-RESULT`: 90-minute double chance, Draw or Al Khaleej (X2), currently available in live sportsbook market pages.
- `P079-T04-CORNERS`: 90-minute total corners, Under 9.5. TotalCorner exposes a current 9.5 corner line; exact user operator/provider was not supplied.

### Verified identity / baseline

- SAFF lists Abha vs Al Khaleej for Tuesday 25 August 2026 at 19:05 local in Abha, Matchweek 3.
- Official SPL results: Abha lost 1-2 to Al Hazem in MW1 and 0-4 to Al Ahli in MW2, leaving them 0 points with 1 goal scored and 6 conceded after two league games.
- Al Khaleej drew 0-0 away to Al Taawoun in MW1 and 0-0 at home to Al Shabab in MW2, leaving them unbeaten with two points and no goals scored or conceded.
- Current external market pages show a close 1X2 with Al Khaleej marginally shorter on several operators; this is market context only, not internal probability evidence.
- The official SPL transfer register confirms Musa Barrow joined Al Khaleej and Michy Batshuayi joined Abha. Current probable-lineup feeds place Batshuayi in Abha's front line and Joshua King/Musa Barrow in Al Khaleej's attack, but **confirmed official starting XIs were not verified at cutoff**.

### Goal-process assessment

This is a collision of two very different early-season states. Abha's first two league matches both cleared 1.5 goals and both had first-half scoring: they trailed Al Hazem 0-2 at halftime and Al Ahli 0-2 at halftime. Al Khaleej, by contrast, have produced consecutive 0-0 league draws, both 0-0 at halftime.

The stronger mechanism for the low user thresholds is nevertheless **Over**, because Abha's defensive floor has been poor enough that Al Khaleej can clear the full-game line without needing Abha to contribute, while Abha now have more attacking quality than their one-goal league total alone suggests. Al Khaleej's King/Barrow attack has created shots without converting in the opening two rounds, so 0 goals is treated as an outcome, not a stable scoring rate.

**Qualitative central score corridor:** `1-1 / 1-2 Al Khaleej / 2-1 Abha`, with `0-1` and `0-0` as the main low-total branches and `1-3 / 2-2` as upper branches.

### Weather / context

Saudi Arabia's National Center for Meteorology daily report for 25 August keeps thunderstorm/hail/active-wind risk in parts of Asir, and an Asir light-rain warning was active during the day. This is treated as a variance modifier only: wet/windy conditions can disrupt clean finishing but also create defensive errors, set pieces and blocked deliveries. No automatic Under direction is applied.

### Corner process

Direct recent corner totals are mixed but generally moderate:
- Abha: 6 total corners vs Al Hazem, 6 vs Al Ahli; their 16 August cup draw with Al Orubah also had 6.
- Al Khaleej: 10 total corners vs Al Taawoun and 9 vs Al Shabab; their cup loss at Al Akhdoud had 10.
- The seven listed H2Hs average about 9 total corners, with only 43% over 9.5; the most recent 2024 meeting produced 9.

There is some direct target-event evidence from official SPL commentary for Al Khaleej: against Al Shabab, King/Barrow generated blocked shots and crosses around corner events, while the Taawoun game also produced 10 corners. However, a complete current cross/block/end-line/clearance/opponent-conceded rate chain and exact operator provider definition were not available. Under the soccer derivative completeness gate, the corner row is capped at `FORCED RANK` / LOW evidence.

### D0 mechanism retrieval

Applicable historical process controls from the development audit:
- draw-band discipline: prior soccer winner misses showed that a non-loss contract can be stronger than an outright winner when the draw branch is material;
- corners remain a separate event process and cannot be inferred mechanically from possession, shots or scoring.
No historical outcome is used as a fitted probability or mechanical vote.

### Scenario map

| Scenario | Mechanism | Main effect |
|---|---|---|
| Al Khaleej defensive control + improved conversion | Two clean sheets persist while King/Barrow finally convert against Abha's vulnerable defence | Strong for X2 and FT O1.5; supports Al Khaleej winner. |
| Abha home response | Batshuayi-led attack improves; home side exploits Al Khaleej fullback/transition space | O1.5 and 1H O0.5 can win even if X2 fails. |
| Al Khaleej finishing drought persists | Chances remain low quality or saved; Abha play more cautiously after 0-4 loss | Main kill path for O1.5 and 1H O0.5; 0-0/1-0 branch. |
| Early goal | Abha's recent first-half defensive vulnerability appears again | Strong for 1H O0.5 and increases FT O1.5. |
| Weather disruption | Rain/wind lowers clean combination play or increases errors/set pieces | Widens both goal and corner distributions; no fixed sign. |
| Low-corner match | Abha attack stays central and Al Khaleej protect territory without repeated blocks/clearances | Supports U9.5 corners. |

### Frozen ranking

| Rank | Candidate | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | C01 | **Combined Total — Over 1.5 Goals (90 min)** | `LEAN` | MEDIUM-HIGH | Abha have conceded 2+ in both league matches; one Al Khaleej conversion breakthrough can largely carry the line, while Abha have added higher-level attacking talent. | Al Khaleej's two-match 0-0 process persists and Abha respond conservatively, producing 0-0/1-0/0-1. | DG-P079-GOALS | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | C02 | **Draw or Al Khaleej — X2 (90 min)** | `LEAN` | MEDIUM | Al Khaleej are unbeaten with two clean sheets; Abha are 0-2 with six conceded, making the away non-loss branch more robust than an outright side. | Abha's home response plus Batshuayi/new attacking quality produces their first league win. | DG-P079-SIDE | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | C03 | **1st Half Goals — Over 0.5** | `LEAN` | MEDIUM | Both Abha league games had two first-half goals; their defensive vulnerability creates an early-goal route even against a cautious Al Khaleej. | Al Khaleej's consecutive 0-0 first halves control the pace and Abha avoid another fast collapse. | DG-P079-1H | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | C04 | **Total Corners — Under 9.5** | `FORCED RANK` | LOW | Abha's three most recent recoverable totals are all 6; H2H average is about 9 and only 43% of listed meetings cleared 9.5. | Al Khaleej's last three relevant totals were 9/10/10 and a chasing game can create repeated blocks/crosses; complete target-event chain/provider definition missing. | DG-P079-CORNERS | `CORRELATED_SECONDARY` | `NOT ACTIONABLE / NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Contract geometry / dependence

- 1H Over 0.5 and Under 0.5 are exact complements for first-half goals; C03 selects the Over branch.
- FT Over 1.5 and Under 1.5 are exact complements for 90-minute goals; C01 selects the Over branch.
- C01 and C03 are positively dependent through the early-goal thesis but are not aliases.
- C02 can win in both low- and high-scoring states and is a separate result target.
- C04 is a separate corner target and is not treated as confirmation of the goal thesis.

### Potential winner

**Al Khaleej — `LEAN`, MEDIUM-LOW evidence (90-minute winner).** The away side's two clean sheets, stronger early defensive process and King/Barrow attacking ceiling give them the narrow winner edge. The draw remains a large branch because Al Khaleej have not scored in either league match; Abha's home response is the other principal failure path. This is why X2 ranks above the outright winner call.

### Integrity / model status

- No validated soccer probability model ran; no internal percentages are published.
- Confirmed official starting XIs were not verified before cutoff; probable-lineup feeds are labelled source reports only.
- Current external odds are market-availability/context evidence only and do not support +EV claims.
- Exact sportsbook corner provider/definition and the complete direct corner-event chain were unavailable, so C04 is capped at `FORCED RANK` / LOW evidence.

**Primary evidence lanes:** SAFF official schedule/team page; Saudi Pro League official fixture/results, MW1/MW2 highlights and transfer register; NCM official weather report/warnings; SPL official match commentary for Al Khaleej process; TotalCorner recent corner records/H2H; current Betmaster/YesPlay/Ladbrokes market pages for contract availability only.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-080`.


---

## P-080 — Al Taawoun Buraidah vs Al Fayha — PREGAME

**Append time / cutoff:** 2026-08-26 02:00 Australia/Melbourne / 2026-08-25 19:00 Asia/Riyadh  
**Method:** `MDS-2026.08.24-v2.1` qualitative soccer champion  
**Competition:** Roshn Saudi League 2026/27, Matchweek 3  
**Venue:** Al Taawoun Club Stadium, Buraidah  
**Scheduled start:** 2026-08-25 19:10 Asia/Riyadh / 16:10 UTC / 2026-08-26 02:10 Australia/Melbourne  
**GAME-STATE:** `PREGAME` — official SAFF/SPL fixture lists still showed the match as upcoming with no score at cutoff.

### Previous-log gate

- P-079 remained pregame at this cutoff (scheduled 19:05 Asia/Riyadh / 02:05 Melbourne), so it was not settled or graded.
- Other recent open entries were preserved in their latest verified live/delayed/unresolved states; no hindsight settlement was inserted.
- Only Prediction Log 2 was modified.

### Frozen target / contract manifest

**User-supplied exact targets:**
- `P080-T01-1H-GOALS`: first-half combined goals, line 0.5. Selected branch C03 = **Over 0.5**.
- `P080-T02-FT-GOALS`: 90-minute combined goals, line 1.5. Selected branch C02 = **Over 1.5**.

**Predeclared research additions:**
- `P080-T03-RESULT`: 90-minute double chance, **Al Taawoun or Draw (1X)**, verified available in current bookmaker markets.
- `P080-T04-CORNERS`: 90-minute total corners, **Under 9.5**, with a current 9.5 market visible in aggregate sportsbook data. User operator/provider not supplied.

### Verified identity / baseline

- SAFF lists Al Taawoun vs Al Fayha for Tuesday 25 August 2026 at 19:10 local at Al Taawoun Club Stadium, Matchweek 3.
- SPL opening results: Al Taawoun drew 0-0 with Al Khaleej, then lost 3-2 at Al Kholood; Al Fayha lost 2-1 at NEOM and 3-0 at home to Al Hilal.
- Through two league matches, Al Taawoun have 1 point with a 2-3 goal balance; Al Fayha have 0 points with a 1-5 goal balance.
- Al Taawoun's summer rebuild added Abderrazak Hamdallah, Nedim Bajrami, Oscar Dorley and Zineddine Belaid. Al Fayha added Hugo Moura, Paulo Oliveira and Lazaro among others.
- Hamdallah scored both Al Taawoun goals in the 3-2 loss to Al Kholood and is the clearest current home attacking focal point.
- Confirmed official starting XIs were **not verified from an authoritative source** at cutoff. Current sportsbook/player-market pages list Hamdallah and other likely participants, but that is not treated as lineup confirmation.

### Goal-process assessment

Al Taawoun's first two league matches produced one 0-0 and one 3-2, while Al Fayha's produced 2-1 and 0-3. Three of the four team-games therefore cleared 1.5 goals, but the direction is not based on that count alone. The more important mechanisms are:

- Al Taawoun created a strong second-half response at Al Kholood, with Hamdallah scoring twice after a 0-3 halftime deficit.
- Al Fayha have conceded first-half goals in both league matches: 0-2 at halftime versus NEOM and 0-1 at halftime versus Al Hilal.
- Al Fayha's attack has still generated enough shot volume to avoid treating their one league goal as a stable low-scoring rate; Hugo Moura scored at NEOM and Fashion Sakala remains a transition threat.
- Al Taawoun's defence has already shown both a clean-sheet branch and a severe early-collapse branch, widening the score distribution rather than supporting a one-sided total narrative.

**Qualitative central score corridor:** `2-0 / 2-1 Al Taawoun / 1-1`, with `1-0` as the strongest low-total branch and `2-2 / 3-1` as upper branches.

### First-half assessment

- Al Taawoun: 0-0 HT vs Al Khaleej; 0-3 HT at Al Kholood.
- Al Fayha: 0-2 HT at NEOM; 0-1 HT vs Al Hilal.
- Thus three of the four opening league matches involving these teams had at least one first-half goal, and both Al Fayha league matches did.
- Mechanistically, Al Fayha's early defensive vulnerability plus Hamdallah-led Al Taawoun attacking pressure gives the Over 0.5 first-half branch a credible route. The strongest kill path is Al Fayha dropping into a compact block while Al Taawoun repeat the slow 0-0 opening seen against Al Khaleej.

### Weather / context

- NCM's Qassim page showed very hot, dry conditions and no active weather warning in the region. Heat is treated as a tempo/fatigue modifier, not an automatic Under: it can suppress sustained pressing but also increase late defensive fatigue.

### Corner process

Direct recent corner totals:
- Al Taawoun vs Al Khaleej: 10 total corners (6-4).
- Al Kholood vs Al Taawoun: 7 total corners (3-4), with Al Taawoun recorded at 15 crosses.
- NEOM vs Al Fayha: 7 total corners (3-4), with 5 combined blocked shots and 14 combined clearances in the available stat feed.
- Al Fayha vs Al Hilal: low single-digit total in current specialist feeds.

A current 9.5 corner market is available. Recent direct samples lean below 10, but the evidence is still incomplete: current opponent-adjusted cross/block/end-line/clearance rates and the user's exact settlement provider were not fully verified. Per the soccer derivative completeness gate, the corner row is capped at `FORCED RANK` / LOW evidence.

### D0 mechanism retrieval

Applicable historical controls:
- use draw-band discipline when the non-loss contract is materially more robust than the outright winner;
- do not infer corners from goal strength or possession alone;
- early-goal/score-state branches can alter later attacking and corner demand.
No historical result is used as a fitted probability or mechanical vote.

### Scenario map

| Scenario | Mechanism | Main effect |
|---|---|---|
| Al Taawoun territorial control | Hamdallah focal point plus home possession keeps Al Fayha pinned | Strong for 1X and FT O1.5; supports Al Taawoun winner. |
| Early Al Taawoun goal | Al Fayha repeat recent first-half defensive weakness | Strong for 1H O0.5 and increases FT O1.5. |
| Al Fayha compact block | Carille slows tempo, Sakala/Ganvoula threat stays transition-only | Main kill path for 1H O0.5; 1-0/0-0 branch. |
| Al Taawoun defensive relapse | Kholood-type transition/set-piece problems recur | O1.5 can still win while 1X/winner fail. |
| Heat/fatigue late | Dry heat lowers pressing intensity and can create late defensive errors | Widens second-half scoring; no automatic total sign. |
| Low-corner match | More central progression and efficient finishing reduce repeated blocks/clearances | Supports U9.5 corners. |

### Frozen ranking

| Rank | Candidate | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | C01 | **Al Taawoun or Draw — 1X (90 min)** | `SUPPORTED` | MEDIUM-HIGH | Home side have the stronger attacking ceiling, Al Fayha are 0-2 with five conceded, and the draw is protected. | Al Fayha exploit Al Taawoun's transition/set-piece weakness and convert one of few chances. | DG-P080-SIDE | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | C02 | **Combined Total — Over 1.5 Goals (90 min)** | `LEAN` | MEDIUM-HIGH | Al Fayha have conceded 2+ in both league games; Al Taawoun carry stronger home scoring upside through Hamdallah and support runners. | Compact Al Fayha block + slow Al Taawoun start produces 0-0/1-0/0-1. | DG-P080-GOALS | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | C03 | **1st Half Goals — Over 0.5** | `LEAN` | MEDIUM | Al Fayha conceded before halftime in both league games; Al Taawoun's last match had three first-half goals. | Repeat of Al Taawoun–Al Khaleej 0-0 opening and deliberate heat-managed tempo. | DG-P080-1H | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | C04 | **Total Corners — Under 9.5** | `FORCED RANK` | LOW | Three of four directly recoverable current league totals sit below 10; recent average is moderate rather than extreme. | Chasing score state creates repeated wing attacks, crosses, blocks and clearances; full direct-event chain/provider definition incomplete. | DG-P080-CORNERS | `CORRELATED_SECONDARY` | `NOT ACTIONABLE / NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Contract geometry / dependence

- 1H Over 0.5 and Under 0.5 are exact complements under matching 1H settlement terms; C03 selects the Over branch.
- FT Over 1.5 and Under 1.5 are exact complements under matching 90-minute terms; C02 selects the Over branch.
- C02 and C03 are positively dependent through an early-goal thesis but are not aliases.
- C01 can win in either low- or high-scoring states and is a separate result target.
- C04 is a separate corner process and is not treated as confirmation of the goal forecast.

### Potential winner

**Al Taawoun — `LEAN`, MEDIUM evidence (90-minute winner).** The home side's stronger current attacking personnel, Hamdallah's immediate scoring impact, Al Fayha's 0-2 league start and five conceded goals create the clearer winner route. The principal failure path is another Al Taawoun defensive breakdown or a low-possession Al Fayha counter/set-piece goal that turns the match into a draw or away upset. The 1X contract is therefore materially stronger than the outright winner call.

### Integrity / model status

- No validated soccer probability model ran; no internal percentages are published.
- Confirmed official starting XIs were not verified before cutoff.
- Current bookmaker prices are used only to verify market availability, not to claim value or internal probability.
- Exact corner provider/definition and complete target-event chain were unavailable, so C04 remains `FORCED RANK` / LOW evidence.

**Primary evidence lanes:** SAFF official calendar/championship page; Saudi Pro League official fixture/results, team pages, match commentary and summer transfer register; NCM Qassim/Buraydah weather; Sportingbet and current odds aggregators for contract availability only; recent official/specialist match-stat feeds for first-half and corner process.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-081`.


---

## 2026-08-26 comprehensive pending-queue cleanup — P-070 through P-080

**Cleanup time:** 2026-08-26T09:58:00+10:00 Australia/Melbourne  
**Method:** MDS-2026.08.24-v2.1  
**Scope:** every still-open new-log event from P-070 through P-080  
**Rule:** verify current state first; settle only verified finals; preserve live events open; append retrospectives without rewriting issued forecasts.  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`.

### Queue state sweep

| ID | Event | Verified state at cleanup | Action | Primary verification |
|---|---|---|---|---|
| P-070 | Central Ballester Reserves vs El Porvenir Reserves | **FINAL — 0-1 (HT 0-0)** | Close event; settle research-grade rows; corner row UNSETTLEABLE after retry | BongdaNet / current result feed |
| P-071 | Alejandro Juan Mano vs Alejandro Turriziani Alvarez | **FINAL — Juan Mano 6-4, 6-4** | Settle + retrospective | TennisTonic result page |
| P-072 | Jelle Sels vs Stijn Paardekooper | **FINAL — Sels 2-1** | Settle + retrospective | current ITF-result database / TennisStats247 |
| P-073 | Tobol Kostanay vs Kaisar Kyzylorda | **FINAL — Tobol 3-2 (HT 2-1)** | Settle goal/side rows; corner row UNSETTLEABLE after provider retry | current result feeds / Forebet score page |
| P-074 | Maccabi Herzliya U19 vs Hapoel Rishon LeZion U19 | **FINAL — Maccabi Herzliya 4-3 (HT 3-3), corners 7-6** | Settle + retrospective | AiScore / SoccerPunter / TotalCorner |
| P-075 | OKS vs Middelfart | **FINAL — OKS 0-1 Middelfart, corners 0-16** | Settle + retrospective | TotalCorner current result |
| P-076 | Horní Ředice vs Dukla Praha | **FINAL — 0-5 (HT 0-3), corners 1-6** | Settle + retrospective | Forebet current result |
| P-077 | Vincent Weaver vs Aryan Jit Singh | **LIVE — Weaver leads one set; exact in-set score CONFLICTING across current feeds** | **KEEP OPEN — NO SETTLEMENT / NO RETROSPECTIVE** | Betolimp live + Leon live conflict |
| P-078 | Brann W vs Austria Wien W | **FINAL — Brann 2-1 (HT 1-1), corners 5-3** | Settle + retrospective | Forebet current result |
| P-079 | Abha vs Al Khaleej | **FINAL — 1-1** | Settle + retrospective | Saudi Pro League / current detailed result feed |
| P-080 | Al Taawoun vs Al Fayha | **FINAL — 0-0, corners 12-3** | Settle + retrospective | Saudi Pro League + FotMob/APWin current stats |

### P-070 settlement — Central Ballester Reserves 0-1 El Porvenir Reserves

Issued state was `START PASSED / LIVE STATE NOT VERIFIED`, so every ranked row was already `INELIGIBLE` and `NOT ACTIONABLE`. The verified final was 0-1 with 0-0 at halftime. A fresh corner-stat retry did not recover an exact final corner count from a stable named provider; the issued corner row was itself a research threshold with provider/market availability unresolved.

| Rank | Candidate | Issued contract | Final state | Settlement | Performance treatment |
|---:|---|---|---|---|---|
| 1 | C01 | El Porvenir or Draw — X2 | El Porvenir won 1-0 | **WIN** | `INELIGIBLE` — state gate |
| 2 | C02 | 1H Under 1.5 goals | HT 0-0 | **WIN** | `INELIGIBLE` — state gate |
| 3 | C03 | El Porvenir DNB | El Porvenir won | **WIN** | `INELIGIBLE` — state gate |
| 4 | C04 | Under 10.5 corners — research threshold | exact final corners not verified after retry | **UNSETTLEABLE** | `INELIGIBLE`; provider/definition unresolved |
| — | Winner | El Porvenir | won 1-0 | **WIN** | informational only |

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| El Porvenir non-loss, low first half; no trustworthy live state | El Porvenir won 1-0 after 0-0 HT | Direction was right, but issued only after start without verified live state | State uncertainty was fully knowable and disclosed | **COMPLIANT** | None | State-control gate worked; research result must not become prospective performance | **No** |

### P-071 settlement — Juan Mano d. Turriziani Alvarez 6-4, 6-4

| Rank | Candidate | Issued contract | Final arithmetic | Settlement | Boundary note |
|---:|---|---|---|---|---|
| 1 | C01 | Alejandro Juan Mano ML | Juan Mano won 2-0 | **WIN** | — |
| 2 | C02 | Under 20.5 total games | 20 games | **WIN** | won by 0.5 game |
| 3 | C03 | Juan Mano -4.0 games | 12 games to 8 = +4 | **PUSH** | standard integer game-handicap assumption; operator not supplied |
| 4 | C04 | Under 19.5 total games | 20 games | **LOSS** | lost by 0.5 game |
| — | Winner | Juan Mano | won | **WIN** | — |

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Juan Mano straight-set central branch, with adjacent total/game-handicap boundaries | Exactly 6-4, 6-4 | Central branch correct; adjacent lines split WIN/PUSH/LOSS exactly at boundary | Boundary geometry was knowable and mapped | **COMPLIANT** | None | Tennis integer push mass and nested totals must remain explicit | **No** |

### P-072 settlement — Jelle Sels d. Stijn Paardekooper 2-1

| Rank | Candidate | Issued contract | Final state | Settlement | Dependence note |
|---:|---|---|---|---|---|
| 1 | C01 | Paardekooper +1.5 sets | Paardekooper won one set | **WIN** | same three-set thesis |
| 2 | C02 | Sels +1.5 sets | Sels won match | **WIN** | same three-set thesis |
| 3 | C03 | Sels ML | Sels won 2-1 | **WIN** | outright result |
| 4 | C04 | Over 2.5 total sets | three sets played | **WIN** | same three-set thesis |
| — | Winner | Sels | won | **WIN** | — |

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Competitive three-set branch with Sels narrow winner | Match went three sets and Sels won | Central competitive-match thesis materialized | Dependence was explicitly disclosed | **COMPLIANT** | None | Three winning set-related rows are one correlated mechanism observation, not three independent confirmations | **No** |

### P-073 settlement — Tobol 3-2 Kaisar

The verified score was 3-2 with Tobol leading 2-1 at halftime. The first three goals arrived very early in the match according to current result/timeline feeds, so the conservative first-half/low-total branch broke immediately. A fresh corner-stat search did not recover the exact final corner count from a stable result provider; the issued row was low-evidence and provider-unresolved, so it is not guessed.

| Rank | Candidate | Issued contract | Final state | Settlement | Performance treatment |
|---:|---|---|---|---|---|
| 1 | C01 | Tobol or Draw — 1X | Tobol won 3-2 | **WIN** | `PRIMARY_FORMAL` |
| 2 | C02 | Under 3.5 goals | 5 goals | **LOSS** | `PRIMARY_FORMAL` |
| 3 | C03 | 1H Under 1.5 goals | 3 first-half goals | **LOSS** | `CORRELATED_SECONDARY` |
| 4 | C04 | Over 7.5 corners — research-grade | exact final corner count not verified after retry | **UNSETTLEABLE** | low-evidence derivative; no invented settlement |
| — | Winner | Tobol | won | **WIN** | — |

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Tobol home protection + low-scoring/slow first-half central path | Early goals created a 2-1 HT state and expanded both teams' attacking demand | Side read survived; low-total branches failed decisively | Early-goal branch was identifiable prospectively but its realization was uncertain | **COMPLIANT** | None | Early score state can overwhelm a conservative pre-match total prior; explicitly branch it before ranking | **No** |

### P-074 settlement — Maccabi Herzliya U19 4-3 Hapoel Rishon LeZion U19

Verified final: 4-3, halftime 3-3, corners 7-6 (13 total).

| Rank | Candidate | Issued contract | Final state | Settlement | Note |
|---:|---|---|---|---|---|
| 1 | C01 | Under 3.5 goals | 7 goals | **LOSS** | youth high-tail realized |
| 2 | C02 | 1H Under 1.5 goals | 6 first-half goals | **LOSS** | failed immediately |
| 3 | C03 | Maccabi Herzliya U19 ML | Maccabi won 4-3 | **WIN** | side direction correct |
| 4 | C04 | Over 7.5 corners | 13 corners | **WIN** | low-evidence derivative win |
| — | Winner | Maccabi Herzliya U19 | won | **WIN** | — |

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Low-total centre with explicit U19 error/transition 4-3-style kill path | Six first-half goals and seven total; exactly the high-variance youth branch | Tail was identified but underweighted in verdict strength | Youth XI/role missingness and prior 4-3 tail were knowable | **COMPLIANT** | None | In youth/U19 with unverified XIs, cap low-total confidence and preserve wider error/transition tails | **No immediate weight change** |

### P-075 settlement — OKS 0-1 Middelfart

Verified final: 0-1; corners **0-16**.

| Rank | Candidate | Issued contract | Final state | Settlement | Note |
|---:|---|---|---|---|---|
| 1 | C01 | Middelfart or Draw — X2 | Middelfart won 1-0 | **WIN** | protected side robust |
| 2 | C02 | Over 1.5 goals | 1 goal | **LOSS** | class gap did not become goal volume |
| 3 | C03 | Middelfart ML | Middelfart won | **WIN** | side direction correct |
| 4 | C04 | Under 9.5 corners | 16 corners, all Middelfart | **LOSS** | extreme territorial/corner asymmetry |
| — | Winner | Middelfart | won | **WIN** | — |

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Middelfart class edge; Over if that control converted; corner Under unless inefficient pressure created repeats | Middelfart won only 1-0 but generated 16 corners | Issued corner kill path — territorial dominance without conversion — occurred exactly | This mechanism was explicitly knowable preissue | **COMPLIANT** | None | **Goals and corners must remain separate processes.** A dominant favourite can win a low-scoring match while producing massive corner pressure | **No** |

### P-076 settlement — Horní Ředice 0-5 Dukla Praha

Verified final: 0-5 (HT 0-3); corners 1-6 (7 total).

| Rank | Candidate | Issued contract | Final state | Settlement | Note |
|---:|---|---|---|---|---|
| 1 | C01 | Draw or Dukla — X2 | Dukla won 5-0 | **WIN** | — |
| 2 | C02 | Dukla ML | Dukla won | **WIN** | — |
| 3 | C03 | Over 2.5 goals | 5 goals | **WIN** | class/depth translated to scoring |
| 4 | C04 | Under 9.5 corners | 7 corners | **WIN** | low-evidence derivative win |
| — | Winner | Dukla Praha | won | **WIN** | — |

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Professional-depth/class advantage with a multi-goal Dukla branch | Dukla separated early and won 5-0 | Central upper-side branch materialized | Class/depth gap was verified | **COMPLIANT** | None | Cup class gap can be a useful side/scoring prior; it still does not mechanically determine corners | **No** |

### P-077 state hold — Vincent Weaver vs Aryan Jit Singh

**DO NOT SETTLE.** The event remains LIVE. Two current live feeds agree Weaver leads by one set but conflict on the exact score state: Betolimp showed **1-0 (6-1, 3-1)** at one crawl, while Leon showed **1-0 (6-2, second set not yet advanced)**. Because the live state is conflicting and no final exists, all issued rows remain `UNRESOLVED`.

| Candidate | Contract | Current status | Action |
|---|---|---|---|
| C01 | Aryan Jit Singh ML | LIVE / unresolved | no grade |
| C02 | Singh Set 2 winner | LIVE / unresolved | no grade |
| C03 | Singh Set 1 winner | first set appears lost, but conflicting feed/state means no final settlement append yet | no grade until trustworthy final/stat settlement |
| C04 | Vincent Weaver ML | LIVE / unresolved | no grade |
| Winner | Aryan Jit Singh | LIVE / unresolved | no grade |

**Process note:** current-state verification overrules any stale scheduled page or inferred result. Move on; do not retrospective-learn from an unfinished match.

### P-078 settlement — Brann W 2-1 Austria Wien W

Verified final: 2-1 (HT 1-1); corners 5-3 (8 total).

| Rank | Candidate | Issued contract | Final state | Settlement | Note |
|---:|---|---|---|---|---|
| 1 | C01 | Brann or Draw — 1X | Brann won | **WIN** | — |
| 2 | C02 | Over 1.5 goals | 3 goals | **WIN** | — |
| 3 | C03 | 1H Over 0.5 goals | HT 1-1 | **WIN** | — |
| 4 | C04 | Over 7.5 corners | 8 corners | **WIN** | won at the minimum winning integer |
| — | Winner | Brann | won | **WIN** | — |

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Brann home protection plus independent scoring routes on both sides | Brann won 2-1; first-half scoring and 8 corners | Central side/goal branch correct; corner was boundary-sensitive | Current form/competition context was available | **COMPLIANT** | None | Corner win at exactly 8 does **not** validate a low-evidence corner process; retain derivative gate | **No** |

### P-079 settlement — Abha 1-1 Al Khaleej

Verified final: 1-1. Current detailed result feeds report 7 total corners (5-2).

| Rank | Candidate | Issued contract | Final state | Settlement | Note |
|---:|---|---|---|---|---|
| 1 | C01 | Over 1.5 goals | 2 goals | **WIN** | exact threshold cleared |
| 2 | C02 | Al Khaleej or Draw — X2 | draw 1-1 | **WIN** | draw protection was decisive |
| 3 | C03 | 1H Over 0.5 goals | both goals occurred in first half | **WIN** | — |
| 4 | C04 | Under 9.5 corners | 7 corners | **WIN** | low-evidence derivative win |
| — | Winner | Al Khaleej | draw | **LOSS** | outright branch failed while X2 won |

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| X2 materially more robust than Al Khaleej ML because scoring remained uncertain | Match finished 1-1 | Draw-band reasoning worked exactly; outright winner failed | Draw risk was explicitly known | **COMPLIANT** | None | Preserve draw-band discipline: non-loss contracts can be strong while outright winner remains weak | **No** |

### P-080 settlement — Al Taawoun 0-0 Al Fayha

Verified final: 0-0. Current detailed stats report **Al Taawoun 26 shots, about 2.6 xG, 62% possession and 12 corners; Al Fayha 3 corners**, yet no goal was scored.

| Rank | Candidate | Issued contract | Final state | Settlement | Note |
|---:|---|---|---|---|---|
| 1 | C01 | Al Taawoun or Draw — 1X | 0-0 draw | **WIN** | protected side robust |
| 2 | C02 | Over 1.5 goals | 0 goals | **LOSS** | finishing/conversion failure |
| 3 | C03 | 1H Over 0.5 goals | HT 0-0 | **LOSS** | slow/inefficient first half branch |
| 4 | C04 | Under 9.5 corners | 15 corners | **LOSS** | territorial pressure converted to corners, not goals |
| — | Winner | Al Taawoun | draw | **LOSS** | outright branch failed |

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Taawoun territorial/scoring edge with compact-block 0-0 and high-corner chase branches named as kill paths | Taawoun dominated shots/xG/territory and corners but did not score | Process dominance did not become finishing; corner tail exploded | Conversion variance and separate corner process were knowable structurally | **COMPLIANT** | None | **Shots/xG/territory and corners are not goals.** Inefficient dominance can simultaneously kill a goal Over and a corner Under | **No** |

### Cleanup ledger — resolved eligible rows only

P-070 is excluded from performance because it was issued after kickoff without a verified live state. P-077 remains live. The following descriptive ledger therefore covers the nine eligible resolved events P-071–P-076 and P-078–P-080.

| Metric | Cleanup result | Interpretation |
|---|---:|---|
| Eligible settled events | 9 | one independent event unit each |
| Raw contract rows | **24 WIN / 10 LOSS / 1 PUSH / 1 UNSETTLEABLE** | descriptive only; includes correlated secondary rows |
| `PRIMARY_FORMAL` rows | **14 WIN / 4 LOSS** | dependence-normalized primary decisions under issued roles |
| Rank #1 rows | **8 WIN / 1 LOSS** | descriptive ordinal result; not calibration |
| Potential winners | **7 WIN / 2 LOSS** | losses were P-079 and P-080 draws |
| Proper-score eligible probabilities | 0 | no validated probabilities were issued |
| Profit/ROI/value eligible | 0 | no complete same-time value gate |

**Important:** these counts are not independent-model accuracy, calibration, ROI, or evidence of market edge. Multiple rows within one event can share the same thesis.

### Sport-reference learning candidates from this cleanup

These are **reference observations stored in Prediction Log 2 only**. They are not automatic edits to active sport-rule files and do not change forecast weights without the prospective governance gate.

| Reference ID | Sport | Evidence from cleanup | What went right/wrong | Reference treatment |
|---|---|---|---|---|
| `REF-SOC-2026-08-26-A` | Soccer | P-073, P-075, P-076, P-078, P-079, P-080 | Protected 1X/X2 branches were generally more robust than outright winners; P-079/P-080 drew while protection won | **Reinforces existing draw-band discipline; no new weight** |
| `REF-SOC-2026-08-26-B` | Soccer | P-075: 1 goal + 16 corners; P-080: 0 goals + 15 corners with heavy Taawoun pressure | Goal strength/territory did not map mechanically to corner or finishing outcomes | **Strong reinforcement of separate goal/corner processes** |
| `REF-SOC-2026-08-26-C` | Soccer | P-073 HT 2-1 and FT 3-2 | Early goals changed score-state demand and invalidated the pre-match low-total centre | **Keep explicit early-goal score-state branches in total analysis** |
| `REF-SOC-2026-08-26-D` | Soccer youth | P-074 4-3, HT 3-3 | Issued U19 error/transition tail occurred; low-total confidence was too strong with unverified youth XIs | **Candidate: cap low-total confidence when U19 lineup/role evidence is missing and high-tail evidence exists** |
| `REF-SOC-2026-08-26-E` | Soccer corners | P-076/P-078/P-079 corner rows won; P-075/P-080 lost badly | Mixed outcomes and boundary wins show why result-counting cannot validate low-evidence corner research | **Maintain derivative completeness gate; no promotion from hit count** |
| `REF-SOC-2026-08-26-F` | Soccer cups | P-075 and P-076 | Class gap supported side direction in both, but one game was 1-0/16 corners and the other 5-0/7 corners | **Class gap is a side prior, not an automatic total/corner sign** |
| `REF-TEN-2026-08-26-A` | Tennis | P-071 exact 20 games, +4 margin | U20.5 won, U19.5 lost, -4 pushed | **Preserve integer push mass and nested-line geometry** |
| `REF-TEN-2026-08-26-B` | Tennis | P-072 three-set result | Both +1.5-set rows and O2.5 sets won from one three-set path | **Dependence: one mechanism observation, not three confirmations** |
| `REF-STATE-2026-08-26-A` | Cross-sport | P-070 and P-077 | P-070 remained performance-ineligible because state was unverified; P-077 is held open because live feeds conflict | **State verification outranks schedule assumptions and retrospective convenience** |

### Source / settlement integrity notes

| Issue | Resolution |
|---|---|
| P-070 corners | one documented fresh retry across current result/corner feeds did not establish an exact final provider-defined corner total; `UNSETTLEABLE`, not guessed |
| P-071 -4.0 | graded `PUSH` under standard integer game-handicap treatment; operator was not supplied, so sportsbook-specific treatment remains unknown |
| P-073 corners | fresh score/result sources verify 3-2 and 2-1 HT, but exact final corners were not recovered from a stable result provider; `UNSETTLEABLE` |
| P-077 live score | current feeds conflict on exact set/game score but agree match is underway; no settlement until final source resolves it |
| Low-evidence corner wins | P-076/P-078/P-079 wins remain settlement facts only and do not upgrade the corner model/evidence gate |

**Cleanup result:** P-070–P-076 and P-078–P-080 are now CLOSED/SETTLED; **P-077 remains LIVE / UNRESOLVED**.  
**Next canonical ID remains:** `P-081`.


---

## P-081 — Independiente del Valle vs Deportes Tolima — PREGAME

**Append / issue preparation time:** 2026-08-26 10:07 Australia/Melbourne (2026-08-25 19:07 America/Guayaquil).  
**Method:** MDS-2026.08.24-v2.1 qualitative champion.  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`.  
**Selection origin / candidate policy:** predeclared four-family universe from the user request and analyst commentary before directional ranking: (1) protected full-time side, (2) supplied FT 1.5 total, (3) supplied 1H 0.5 total, (4) one verified/research-grade total-corners threshold.  
**Value state:** `NO VALUE DETERMINABLE` — no validated calibrated model and no complete same-time operator/terms snapshot for every row.

### Previous-log gate

`P-077` Vincent Weaver vs Aryan Jit Singh remains **LIVE / UNRESOLVED** at the latest current check. A live market feed still shows the match in progress and earlier live feeds conflicted on the exact set/game state. Per the state gate, it remains open and receives **no settlement or retrospective**. All other P-070–P-080 IDs are already closed/settled.

### Event identity / state freeze

| Field | Frozen value |
|---|---|
| Canonical ID | `P-081` |
| Official competition | CONMEBOL Libertadores 2026 — Round of 16, second leg |
| CONMEBOL match reference | Match 138 |
| Event | Independiente del Valle (ECU) vs Deportes Tolima (COL) |
| Venue | Estadio Banco Guayaquil, Quito metropolitan area / Sangolquí, Ecuador |
| Scheduled start | 2026-08-25 19:30 America/Guayaquil / 2026-08-26 10:30 Australia/Melbourne |
| GAME-STATE | **PREGAME** — current live/fixture feeds still show scheduled/not started at final research refresh |
| First-leg result | Deportes Tolima 0-1 Independiente del Valle |
| Aggregate start state | **IDV lead 1-0** |
| Advancement geometry | IDV advance with win or draw; Tolima one-goal win levels aggregate and sends tie to penalties; Tolima 2+ goal win advances in regulation |
| Regulation endpoint | 90 minutes + stoppage; potential extra resolution is penalties only after a one-goal Tolima regulation win under the current tie state |
| Operator | Not supplied by user; 1xBet/Bet365 snapshots used only to verify market availability, not value |
| Information cutoff | 2026-08-26 10:07 Australia/Melbourne |

### Target manifest

| Target ID | Definition | Start state | Endpoint / support | Termination / settlement |
|---|---|---|---|---|
| `SOC-P081-REG-SCORE-v1` | Regulation goals scored by IDV and Tolima | 0-0, aggregate IDV +1 | end of 90+ stoppage | regulation only; penalties excluded |
| `SOC-P081-1H-GOALS-v1` | Combined first-half goals | 0-0 | halftime | first-half stoppage included |
| `SOC-P081-CORNERS-v1` | Total regulation corners under research-grade provider convention | 0 | end of 90+ stoppage | bookmaker/provider definition remains `UNKNOWN_DEFINITION`; row capped accordingly |

### Current participant / lineup evidence

Current lineup feeds close to kickoff remain **probable rather than official field-owner confirmation**. 365Scores lists IDV with Aldair Quintana; Layan Loor, Richard Schunke, Mateo Carabajal, Daykol Romero; Jordy Alcívar, Junior Sornoza, Hugo Quintana; Emerson Pata, Arón Rodríguez and Carlos González. It lists Tolima with Neto Volpi and an attacking group including Adrián Parra, Jorge Hurtado and Sergio Aguayo, while Brayan Rovira is listed unavailable. Because the authoritative competition/club starting XI was not independently recovered at cutoff, these are treated as `SOURCE REPORT`, not `VERIFIED FACT`.

### Highest-priority process evidence

1. **Tie-state asymmetry:** IDV start 1-0 ahead on aggregate. A draw is sufficient for IDV, whereas Tolima must score. This creates a leading-state/control branch for IDV and a trailing/chasing branch for Tolima.
2. **First-leg process:** IDV won 1-0 with an 11th-minute Arón Rodríguez goal. Tolima then held far more possession but struggled for final-third efficiency. The first leg produced 8 corners (Tolima 5, IDV 3). A detailed provider recorded 12 IDV crosses vs 18 Tolima crosses, 5 vs 3 blocked shots and 19 vs 26 defensive clearances — direct corner-causing evidence rather than treating possession as a corner proxy.
3. **Current form:** IDV's recent run includes 3-2 vs Leones del Norte, 3-2 vs Delfín, 2-0 at LDU Quito, 1-0 vs Deportivo Cuenca and the 1-0 first-leg win. Tolima's recent run includes 0-0 vs Bucaramanga, 0-1 vs IDV, 2-1 vs Inter Bogotá, 2-3 vs Independiente Medellín and 2-1 at Alianza.
4. **Home / scoring profile:** current stat panels place IDV around 2+ goals scored per home match in recent samples and show a strong recent home win rate. Tolima's away scoring is materially weaker and its away loss rate higher in the same types of samples. These are supporting statistics, not independent votes.
5. **Weather:** INAMHI reporting for 25 August included possible rain in Quito/Sierra sectors. No automatic goal or corner sign is assigned; rain is treated as added passing/handling/surface variance only.

### D0 / mechanism retrieval

Relevant historical process references are qualitative only: D0 soccer events such as P-041 showed the danger of underweighting the draw branch, while the current Prediction Log 2 reference `REF-SOC-2026-08-26-A` reinforces that protected 1X/X2 contracts can be materially stronger than outright winner calls. `REF-SOC-2026-08-26-B/E` reinforces that goals and corners require separate event processes and that low-evidence corner hits do not validate the model. No historical outcome is used as a fitted probability or mechanical vote.

### Underlying qualitative forecast

**Central regulation branch:** IDV protect the aggregate lead, force Tolima to take more attacking risk as the match develops, and generate counterattacking opportunities. The most coherent central score paths are **1-1, IDV 1-0, IDV 2-0 and IDV 2-1**.  
**Lower-goal branch:** Tolima again fail to convert territory and IDV accept a controlled 0-0/1-0 game.  
**Upper-goal branch:** Tolima score first or equalize the aggregate early, which forces IDV to increase attacking demand and opens a 2-1/2-2/3-1 type game.  
**Structural tail:** red card, penalty, or rain-driven error changes both score-state and corner rates sharply.

### Corner-process card

| Layer | Current evidence |
|---|---|
| Expected exposure | Tolima must eventually chase if aggregate remains against them; IDV can counter into width |
| Team-for / opponent-conceded rates | IDV recent sample ~6.5 corners for and ~3.1 conceded; Tolima recent sample ~4.8 for and ~4.8 conceded |
| First-leg direct rate | 8 total corners: Tolima 5, IDV 3 |
| Width / cross evidence | first-leg detailed source: Tolima 18 crosses, IDV 12 |
| Block / clearance evidence | first-leg detailed source: 8 combined blocked shots; 45 combined defensive clearances |
| Score-state branch | Tolima chasing raises late attacking/corner exposure; an early Tolima goal can shift pressure back toward IDV |
| Exact settlement provider | **UNKNOWN_DEFINITION** because user did not name an operator; research-grade total-corner market used only for directional ranking |

Because the provider/definition layer is unresolved, the corner row is **not eligible for LEAN/SUPPORTED** under the soccer derivative completeness gate.

### Contract geometry

| Candidate | Win interval / condition | Relation |
|---|---|---|
| C01 — IDV or Draw (1X) | IDV regulation win or regulation draw | protected side; draw is a win |
| C02 — Over 1.5 goals | regulation total >= 2 | user-supplied FT threshold family |
| C03 — 1H Over 0.5 goals | first-half total >= 1 | user-supplied 1H threshold family |
| C04 — Over 7.5 corners | regulation corners >= 8 | separate derivative target; provider definition unresolved |

### Frozen ranked decision set

| Rank | Candidate ID | Exact contract | Verdict | Evidence | Central mechanism | Strongest ordinary kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | `P081-C01` | **Independiente del Valle or Draw — 1X** | **SUPPORTED** | **MEDIUM-HIGH** | IDV lead aggregate 1-0, are at home and do not need to chase; draw advances them | Tolima score first and then successfully defend/counter for an away regulation win | `SIDE/TIE-STATE` | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | `P081-C02` | **Combined Goals — Over 1.5** | **LEAN** | **MEDIUM-HIGH** | Tolima's need to score increases late risk; an IDV counter goal or Tolima equalizer can open the tie | repeat of first leg: Tolima sterile possession + IDV game-state control produces 0-0/1-0 | `GOAL-FULL` | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | `P081-C03` | **1st Half Goals — Over 0.5** | **LEAN** | **MEDIUM** | IDV have a strong recent first-half scoring profile; first leg had an 11' goal; Tolima cannot stay passive indefinitely | first-leg caution is replicated but finishing is worse, yielding 0-0 HT | `GOAL-1H/FULL-LINKED` | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | `P081-C04` | **Total Corners — Over 7.5** | **FORCED RANK** | **MEDIUM-LOW** | direct first-leg cross/block/clearance chain + Tolima chase state + both recent corner baselines centre around ~9-10 | early IDV goal kills Tolima's efficient buildup or goals arrive with few blocked/end-line events; exact provider unresolved | `CORNERS-SEPARATE` | `PRIMARY_FORMAL` | `NOT ACTIONABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Potential winner

**Independiente del Valle — LEAN, MEDIUM evidence.**  
The winner call is weaker than 1X because IDV do not need to win this second leg. Home form, current attacking quality and the 1-0 aggregate advantage support IDV, but a regulation draw is tactically acceptable and therefore materially lowers outright-win robustness.

### Market / validation boundary

Current 1xBet/Bet365 snapshots verify IDV as the regulation favourite, 1X as available, and Over 1.5 as available. Those prices are recorded only as contemporaneous market context. No target-specific validated soccer model has run, so no numerical probability, value, ROI or staking claim is authorised.

### Sources frozen for P-081

- CONMEBOL official rescheduling / tie details: `https://gol.conmebol.com/libertadores/es/news/fechas-definidas-para-la-serie-entre-deportes-tolima-e-independiente-del-valle`
- 365Scores current event / aggregate / probable lineup / Bet365 snapshot: `https://www.365scores.com/es/football/match/conmebol-libertadores-102/independiente-del-valle-deportes-tolima-7635-9142-102`
- 1xBet current market / recent results / venue: `https://1xbet.es/es/line/football/142091-copa-libertadores/745595030-independiente-del-valle-deportes-tolima`
- Primicias first-leg minute-by-minute and tie report: `https://www.primicias.ec/deportes/futbol/envivo-deportes-tolima-independiente-valle-octavos-final-copa-libertadores-resultado-ver-partido-tv-130467/`
- WinComparator first-leg detailed event stats including corners/crosses/blocks/clearances: `https://www.wincomparator.com/es-es/pronosticos/deportes-tolima-independiente-del-valle-8734930/`
- Independiente del Valle recent corner profile: `https://corneredge.bet/team/independiente-del-valle/corners/`
- Deportes Tolima recent corner profile: `https://corneredge.bet/team/deportes-tolima/corners/`
- INAMHI-derived Quito weather reporting: `https://www.ecuavisa.com/ecuador/clima-ecuador-25-agosto-inamhi-preve-lluvias-11-provincias-sierra-amazonia-20260825-0009.html`

**Logging status:** complete P-081 forecast appended before delivery.  
**Next canonical ID after this append:** `P-082`.


---

## 2026-08-26 settlement-integrity sweep and mandatory settlement-detail standard

**Sweep time:** 2026-08-26T10:11:00+10:00 Australia/Melbourne  
**Scope:** all currently open IDs in Prediction Log 2 plus settlement-quality standard for every future closed ID.  
**Rule:** a scheduled-time assumption is never enough to settle. Verify current event state first. If an event is `LIVE`, `UPCOMING`, delayed, suspended, or final verification is conflicting, preserve it open and move on. Only a trustworthy final/official statistical endpoint authorises settlement.

### Current open-queue verification

| ID | Event | Current verified state | Settlement action | Evidence status |
|---|---|---|---|---|
| `P-077` | Vincent Weaver vs Aryan Jit Singh | **LIVE / UNRESOLVED** — multiple current live feeds agree Weaver leads by one set, but exact score-state remains inconsistent across feeds; Betolimp showed `1-0 (6-1, 3-1)` in its current crawl while other live-market feeds expose a different first-set/state presentation | **NO SETTLEMENT. KEEP OPEN.** No contract, set winner, match winner, or retrospective is graded until a trustworthy final/stat source resolves the match. | Current live feeds; no final result source available |
| `P-081` | Independiente del Valle vs Deportes Tolima | **UPCOMING / PREGAME** — CONMEBOL lists the second leg for 25 Aug 2026 at 19:30 Ecuador; at this Melbourne sweep time the scheduled 10:30 Melbourne kickoff has not occurred | **NO SETTLEMENT. KEEP OPEN.** | CONMEBOL official fixture/tie page and current scheduled match feeds |

**All other issued IDs `P-067`–`P-080` are already CLOSED/SETTLED** except P-077. No previously issued settlement is rewritten here; this sweep only verifies queue status and strengthens the required settlement record.

### Mandatory detailed settlement schema — effective immediately

Every future completed event must receive a settlement append with **all** of the following fields. A shorter result-only note is insufficient.

| Required field | Settlement requirement |
|---|---|
| Event identity | Canonical ID/view, competition, participants, venue/date, and exact phase/endpoint |
| State verification | `FINAL` plus verification/access time; if final is not trustworthy, leave `UNRESOLVED` |
| Official final | Exact final score/result, period/set/innings detail where contract-relevant, and aggregate/advance result where applicable |
| Source hierarchy | Official governing-body/competition result first where available; named high-quality fallback only when official detail is unavailable |
| Contract-by-contract grading | Every issued canonical contract gets `WIN / LOSS / PUSH / VOID / UNRESOLVED / UNSETTLEABLE`, with the exact arithmetic or boundary explanation |
| Provider-sensitive stats | Corners, cards, player shots, tennis set/game handicaps, etc. require the frozen provider/definition where known; if exact stat cannot be verified after a documented retry, use `UNSETTLEABLE` rather than guessing |
| Potential winner | Grade the issued winner separately and respect regulation/OT/advance terms |
| Dependence | Identify aliases, exact complements, nested lines, overlaps, and correlated rows so several wins from one path are not counted as independent evidence |
| Preissue expectation | State the issued central mechanism and strongest ordinary kill path exactly as they existed before the result |
| Actual driver | Describe what actually decided the result using post-match process evidence, not only the final score |
| Difference / knowability | State whether the realised difference was predictable before issue, merely a known tail, or genuinely new/unavailable information |
| Process grade | `COMPLIANT / PROCESS_DEFECT / INCONCLUSIVE` |
| Defect class | Identity/contract, source transformation, arithmetic, temporal leakage, state, settlement, compliance, or `None` |
| Boundary sensitivity | Explicitly note one-run, half-point, integer-push, one-corner, tiebreak/set, or other threshold-sensitive outcomes |
| Learning disposition | Candidate observation / reinforces existing control / prospective test; **never** automatic weight changes from a single result |
| Method change | Normally `No`; any change requires the active prospective governance gate |
| Ledger treatment | Performance role and whether the row is proper-score/value eligible; no probability or ROI claims when none were issued |

### Honesty / settlement hard rules

1. **Live means live:** do not partially settle an event merely because one contract appears decided when the user requested a whole-log cleanup; preserve the event until a trustworthy final unless the original contract itself has an independently official final phase/stat and the log explicitly permits phase settlement.
2. **Upcoming means no retrospective:** scheduled games remain open even if a stale source says otherwise.
3. **Conflicting live feeds fail closed:** record the conflict and leave the event unresolved.
4. **No invented corners or niche stats:** a final score does not imply corner/card/player-stat settlement.
5. **No hindsight repair:** never rewrite an issued forecast, rank, confidence, cutoff, or source list after the result. Corrections and settlements are append-only.
6. **Outcome and process remain separate:** a losing compliant forecast is not automatically a method defect; a winning defective forecast is not validated.
7. **Detailed sources are mandatory:** every decisive final/stat claim must carry the source that actually owns or verifies that field.

### Current queue after sweep

| Status | IDs |
|---|---|
| `LIVE / UNRESOLVED` | `P-077` |
| `UPCOMING / PREGAME` | `P-081` |
| `CLOSED / SETTLED` | `P-067`–`P-076`, `P-078`–`P-080` |
| Next canonical ID | `P-085` |

**Current source checks:**
- P-077 live state: `https://betolimp.co.za/live`; `https://www.interwetten.com/en/sportsbook/live`; current Clemson match listing at `https://www.sofascore.com/tennis/match/v-weaver-a-singh/JvYdsPagk` (access restrictions may apply).
- P-081 official schedule/tie state: `https://gol.conmebol.com/libertadores/es/news/independiente-del-valle-y-deportes-tolima-definen-al-ultimo-clasificado-cuartos-de-final`; current scheduled listing cross-check: Eurosport match page.

**Result of this sweep:** no new settlement was appended because neither open event is complete. This is intentional and required for accuracy.

---

## P-082 — CF Monterrey vs Chicago Fire FC — PREGAME

**Append / issue preparation time:** 2026-08-26 10:17 Australia/Melbourne (2026-08-25 19:17 America/Chicago).  
**Method:** MDS-2026.08.24-v2.1 qualitative champion.  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`.  
**Selection origin / candidate policy:** user supplied 1H 0.5 and FT 1.5 goal families, plus predeclared protected-side and one verified total-corners family.  
**Value state:** `NO VALUE DETERMINABLE` — no validated calibrated model; market prices are used only for exact-contract verification/context.

### Previous-log gate

- `P-077` Vincent Weaver vs Aryan Jit Singh remains **LIVE / UNRESOLVED**. Current live feeds agree the match is in progress but continue to expose inconsistent exact score-state presentations. No settlement or retrospective is made.
- `P-081` Independiente del Valle vs Deportes Tolima remains **UPCOMING / PREGAME** at this cutoff; scheduled kickoff is 2026-08-26 10:30 Australia/Melbourne.
- No earlier closed result is rewritten.

### Event identity / state freeze

| Field | Frozen value |
|---|---|
| Canonical ID | `P-082` |
| Competition | Leagues Cup 2026 — Quarterfinal |
| Event | CF Monterrey vs Chicago Fire FC |
| Venue | SeatGeek Stadium, Bridgeview, Illinois, USA |
| Scheduled start | 2026-08-25 19:30 America/Chicago / 2026-08-26 10:30 Australia/Melbourne |
| GAME-STATE | **PREGAME** — ESPN/official tournament pages still show scheduled pre-kick state at final research refresh |
| Knockout rules | Single elimination; if tied after regulation, direct penalty shootout; no extra time |
| H2H | First competitive meeting between the clubs |
| Operator | Not supplied by user; Caliente/DraftKings-style snapshots used only to verify current contracts |
| Information cutoff | 2026-08-26 10:17 Australia/Melbourne |

### Target manifest

| Target ID | Definition | Start state | Endpoint / support | Settlement |
|---|---|---|---|---|
| `SOC-P082-REG-SCORE-v1` | Regulation goals scored by Monterrey and Chicago | 0-0 | 90 minutes + stoppage | penalties excluded |
| `SOC-P082-1H-GOALS-v1` | Combined first-half goals | 0-0 | halftime + stoppage | first-half only |
| `SOC-P082-CORNERS-v1` | Total regulation corners | 0 | 90 minutes + stoppage | provider-specific bookmaker definition unresolved; row evidence capped |

### Confirmed starting XIs

**Monterrey (4-2-3-1):** Esteban Andrada; Gerardo Arteaga, Víctor Guzmán, Carlos Salcedo, Ricardo Chávez; Óliver Torres, Orbelín Pineda; Lucas Ocampos, Jesús Corona, Diego Rossi; Hugo Cuypers.  
**Chicago Fire (4-3-3):** Chris Brady; Andrew Gutman, Jack Elliott, Joel Waterman, Jonathan Dean; Sergio Oregel, Dje Tah, Anton Salétros; Robert Lewandowski, Philip Zinckernagel, Puso Dithejane.

The confirmed XI materially strengthens the two-team attacking branch because Lewandowski starts rather than the earlier official-preview possibility of beginning on the bench. Monterrey also deploy their principal attacking group together.

### Highest-priority process evidence

1. **Chicago current state:** Chicago finished Leagues Cup Phase One 3-0-0, the only MLS side with a perfect nine points, beating Necaxa 2-0, Santos Laguna 3-1 and Cruz Azul 2-1. They enter on a seven-match unbeaten run across all competitions.
2. **Chicago attacking/early-goal mechanism:** Necaxa had a 31' opener by Chicago, Santos scored at 20', Orlando MLS had a Chicago goal at 4', Portland had Chicago goals at 9' and 14', and the Red Bulls match had Chicago score at 38'. The Cruz Azul Phase One match is the main recent 0-0-at-HT countercase under the official Leagues Cup recap.
3. **Monterrey attacking state:** the official Leagues Cup preview states Monterrey scored 10 goals across the four matches immediately preceding this quarterfinal preview. Cuypers scored three goals in Phase One; Ocampos, Rossi, Corona and Orbelín provide multiple creation/finishing channels.
4. **Monterrey variance:** Rayados lost 2-0 at León immediately before this game, but the prior results included 6-1 vs Juárez, 2-1 vs Nashville and 2-1 at Inter Miami. Their Phase One Leagues Cup team line was 1.67 goals scored and 1.33 conceded per match.
5. **Chicago defensive/finishing profile:** ESPN's tournament snapshot lists Chicago at 2.33 goals scored and 0.67 conceded per Leagues Cup match, with one clean sheet. The stronger recent form is balanced by Monterrey's higher-end individual attacking quality.
6. **Knockout state:** unlike a two-leg tie, neither side can bank an aggregate advantage. A regulation draw leads directly to penalties, supporting a late open-game branch if level.
7. **Corner mechanism:** recent recoverable totals include Chicago-Santos 9 corners, Chicago-RBNY 5, Monterrey-Nashville 14, Inter Miami-Monterrey 10 and Monterrey-Orlando 7. Monterrey-Nashville included 11 Monterrey corners. Current market sources verify a live 7.5-corner threshold. The sample is mixed but centred high enough for an 8+ branch.

### D0 / mechanism retrieval

Relevant qualitative references only:
- `REF-SOC-2026-08-26-A`: protected side markets can be more robust than outright winner calls where the draw band is material.
- `REF-SOC-2026-08-26-B/E`: goals and corners remain separate processes; low-evidence corner wins/losses do not validate a corner model.
- Historical soccer cards show the need to avoid converting general territorial dominance directly into corner direction.

No D0 result is used as a fitted probability or mechanical vote.

### Underlying qualitative forecast

**Central regulation branch:** both teams create enough high-quality attacking sequences for at least two total goals, with Chicago's current home/form edge offset by Monterrey's attacking ceiling. Central score paths are approximately **1-1, Chicago 2-1, Monterrey 2-1, Chicago 2-2 Monterrey** (draw then penalties).  
**Lower-goal branch:** both teams respect knockout risk, Chicago's defensive structure holds, and finishing regresses -> 0-0 or 1-0.  
**Upper-goal branch:** an early goal forces transition exchanges between Ocampos/Rossi/Cuypers and Lewandowski/Zinckernagel/Dithejane -> 2-2, 3-1 or 3-2.  
**Structural tail:** red card/penalty or a late tied-game push materially raises both goal and corner exposure.

### Contract geometry

- `Over 1.5` wins on 2+ regulation goals; `Under 1.5` wins on 0-1.
- `1H Over 0.5` wins on any first-half goal; `1H Under 0.5` requires 0-0 HT.
- `Chicago Fire or Draw (X2)` wins on Chicago regulation win or draw; it loses only on a Monterrey regulation win.
- `Over 7.5 corners` wins on 8+ regulation corners. It is a separate target process and is not evidence that goals must also be high.
- Regulation winner and qualification are different contracts because a draw goes directly to penalties.

### Frozen ranking

| Rank | Candidate ID | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | `P082-C01` | **Combined Goals — Over 1.5** | **SUPPORTED** | **MEDIUM-HIGH** | confirmed elite attacking lineups + Chicago 3-0 Phase One / seven-match unbeaten run + Monterrey multi-channel attack + knockout openness | disciplined 0-0/1-0 game with poor finishing despite talent | `GOAL-FULL` | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | `P082-C02` | **1st Half Goals — Over 0.5** | **LEAN** | **MEDIUM-HIGH** | 5 of Chicago's last 6 listed matches had a first-half goal; Monterrey's recent Leagues Cup games vs Miami/Nashville also had first-half goals | both sides open cautiously in a single-elimination quarterfinal, producing 0-0 HT | `GOAL-1H/FULL-LINKED` | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | `P082-C03` | **Chicago Fire or Draw — X2 (90 min)** | **LEAN** | **MEDIUM** | home venue, perfect Leagues Cup Phase One, seven unbeaten, Lewandowski starts; market also has Chicago as slight regulation favourite | Monterrey's first-choice attack converts quality early and controls transitions | `SIDE/DRAW-BAND` | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | `P082-C04` | **Total Corners — Over 7.5** | **FORCED RANK** | **MEDIUM-LOW** | current 7.5 market verified; recent combined-corner samples include 9, 14 and 10, with both teams using wide attackers/fullbacks | efficient finishing reduces blocked/end-line sequences; recent 5- and 7-corner games show the floor; exact operator/provider definition not supplied | `CORNERS-SEPARATE` | `PRIMARY_FORMAL` | `NOT ACTIONABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Potential winner

**Chicago Fire FC — LEAN, MEDIUM evidence (90-minute regulation winner).**  
Chicago has the stronger current form and the home setting, went 3-0 in Phase One, and starts Lewandowski. The call remains only a lean because Monterrey's confirmed XI is close to full attacking strength and has sufficient individual quality to win in regulation. A regulation draw is also a large branch and would send the quarterfinal directly to penalties.

### Market / validation boundary

Current Caliente/ESPN market snapshots verify:
- FT Over 1.5;
- 1H Over 0.5;
- Chicago/Draw X2;
- current total-corner markets around 7.5-9.5;
- Chicago as a slight regulation favourite and slight qualification favourite.

These prices are used to verify contract existence/context only. No target-specific validated soccer model has run, so no numerical probability, EV, ROI or staking claim is authorised.

### Sources frozen for P-082

- Leagues Cup official quarterfinal preview: `https://www.leaguescup.com/news/match-preview-chicago-fire-hosts-monterrey-in-seatgeek-stadium-as-they-look-to-remain-perfect-in-leagues-cup`
- Leagues Cup official knockout rules: `https://www.leaguescup.com/about/`
- Chicago Fire official quarterfinal schedule: `https://www.chicagofirefc.com/news/chicago-fire-fc-to-host-cf-monterrey-in-leagues-cup-2026-quarterfinals`
- Chicago Fire official latest result/injury context: `https://www.chicagofirefc.com/news/match-recap-chicago-fire-fc-extends-unbeaten-streak-to-seven-in-1-1-road-draw-at-red-bull-new-york`
- ESPN current event, confirmed lineups, tournament stats and form: `https://www.espn.com/soccer/match/_/gameId/401909652/chicago-fire-fc-monterrey`
- Monterrey official pre-quarterfinal / recent team context: `https://www.rayados.com/es/noticias/21558/rayados-enfrentara-al-chicago-fire-el-martes-25-de-agosto`
- Monterrey official latest Liga MX match: `https://www.rayados.com/es/noticias/21571/rayados-cae-ante-leon-en-la-jornada-5`
- Chicago-Santos official Leagues Cup recap: `https://www.leaguescup.com/news/match-recap-lewandowski-scores-first-leagues-cup-goal-as-chicago-rallies-past-santos-laguna`
- Chicago-Cruz Azul official Leagues Cup recap: `https://www.leaguescup.com/news/match-recap-dithejane-s-late-goal-keeps-chicago-fire-perfect-eliminates-cruz-azul`
- Inter Miami-Monterrey official recap/stat line: `https://www.intermiamicf.com/news/match-recap-inter-miami-cf-falls-against-cf-monterrey-in-second-leagues-cup-2026-phase-one-matchup`
- Current Caliente exact goals/half/corners market verification: `https://sports.caliente.mx/es_MX/Leagues-Cup/2026-08-25/Monterrey-vs-Chicago-Fire`

**Logging status:** complete P-082 forecast appended before delivery.  
**Next canonical ID after this append:** `P-083`.

---

## Administrative methodology note — top-two priority and mandatory rank-1 loss audit

**Effective:** 2026-08-26

This note is prospective and does not rewrite any issued forecast.

### Top-two priority objective

For every standard four-pick card, **ranks #1 and #2 are the priority outcomes**. Over a sufficiently large prospective sample, they should outperform ranks #3 and #4 on the frozen decision metrics. Track, at minimum:

| Metric | Purpose |
|---|---|
| Rank-1 win rate | Measures whether the highest-ranked contract is actually the strongest individual selection |
| Wins@2 | Counts how many of the top two settle as WIN |
| Hit@2 | Records whether at least one of the top two wins |
| NDCG@2 | Evaluates whether winning/relevant contracts are concentrated at the top of each four-row decision set |
| Exact-pair ordering | Checks whether higher-ranked exact complements/opposites are ordered correctly |

The priority is **not** to manufacture a high Hit@2 by selecting opposite sides, aliases, or redundant correlated branches. Ordinary ranks remain marginal-likelihood ranks, and dependence/contract geometry must remain explicit.

### Mandatory rank-1 loss audit

Whenever **rank #1 settles as LOSS**, perform a serious full-event retrospective covering **all four issued picks**, not only rank #1. The audit must include:

| Audit field | Required review |
|---|---|
| Settlement | Reverify final result/statistic and exact contract arithmetic for all four rows |
| Rank ordering | Determine whether #2/#3/#4 should have ranked above #1 based only on information knowable before issue |
| Event model | Compare the issued central/lower/upper/structural-tail scenarios with the actual match path |
| Kill paths | Identify whether the realised failure path was named, underweighted, missing, or unknowable |
| Participants/state | Recheck lineups, roles, starters, injuries, live-state timing and any late changes available before cutoff |
| Source quality | Audit decisive sources, freshness, provider definitions, conflicts and missingness |
| Contract geometry | Recheck complements, overlaps, pushes, aliases, draw bands, phase/full links and dependence |
| Sport-native mechanism | Reconstruct the relevant exposure → rate → outcome chain for every pick |
| Process grade | `COMPLIANT`, `PROCESS_DEFECT`, or `INCONCLUSIVE` |
| Knowability | State whether the miss was preventable with prediction-time information |
| Reference learning | Add any defensible sport-reference candidate observation |
| Method change | `NONE` after an ordinary single outcome unless a demonstrated process defect requires an immediate lock/correction |

A rank-1 loss is therefore a **mandatory research trigger**, not automatic proof that the framework is miscalibrated. Any forecast-weight change still requires prospective evidence under the existing champion–challenger and learning-register rules.

### Evaluation interpretation

Top-of-list evaluation is consistent with learning-to-rank practice, where metrics such as NDCG can explicitly emphasize the most highly ranked items. Proper forecast evaluation must still reward honest probability/distribution quality rather than outcome-only confidence. Therefore top-two accuracy is a decision objective and guardrail, not a substitute for calibration/proper scoring if validated probabilities are later introduced.

---

## Administrative clarification — settlement depth and rank-1 loss treatment

**Effective:** 2026-08-26  
**Status:** CONTROLLING CLARIFICATION for future settlements; append-only and prospective.

This clarification refines the prior top-two/rank-1 audit note without rewriting any issued forecast.

### Settlement standard — applies to every completed event

Every event that is verified FINAL receives a **detailed, accurate, source-backed settlement and retrospective**, regardless of whether rank #1 won or lost. The purpose is to record what actually happened and what the issued analysis got right or wrong, not to force a model change.

Every settlement must include, where applicable:

| Settlement field | Required record |
|---|---|
| Official final | Final score/result and authoritative/high-quality settlement source |
| Contract-by-contract grade | WIN / LOSS / PUSH / VOID / UNRESOLVED / UNSETTLEABLE for every issued row, with exact arithmetic/threshold reasoning |
| Potential winner | Separate settlement of the issued potential-winner contract |
| Match/process drivers | What actually drove the result in sport-native terms |
| Preissue expectation vs reality | Which expected mechanisms appeared, failed to appear, or were outweighed |
| Kill paths | Whether the realised adverse branch was identified before issue and how material it was |
| Dependence / geometry | Complements, overlap, pushes, aliases, phase/full links and correlated rows |
| Boundary sensitivity | Note results decided at or near an exact contract boundary |
| Source / state quality | Any lineup, starter, role, injury, provider-definition, live-state or timing issues |
| Knowability | Whether the relevant information was available before the forecast cutoff |
| Process grade | COMPLIANT / PROCESS_DEFECT / INCONCLUSIVE |
| Accurate observations | Specific sport/process observations worth preserving for future reference |
| Model/method change | **NONE REQUIRED FROM SETTLEMENT ALONE**; observations are recorded without automatically changing weights or the model |

### Extra audit when rank #1 loses

A rank-1 loss does **not** imply the model must change. It triggers **additional retrospective depth** on top of the normal detailed settlement.

When rank #1 settles as LOSS, additionally review:

1. **Why #1 was ranked first** using only information available before issue.
2. **All four picks together**, including whether #2, #3 or #4 had a stronger preissue case and should reasonably have ranked above #1.
3. **The full rank ordering**, not merely the losing contract.
4. **The realised match path versus every stored scenario branch**, including any underweighted tail.
5. **Sport-native exposure and rate mechanisms** for all four rows.
6. **Source freshness and missingness**, including lineups, participants, starters, injuries, weather, live state and provider definitions.
7. **Contract geometry/dependence**, to make sure correlation or an apparently safer alternate did not distort the ranking.
8. **Preventability/knowability**, distinguishing an avoidable process miss from ordinary outcome variance.
9. **Reference observations**, recording what the event teaches without converting one result into a new numerical weight or automatic rule.

### Interpretation

The standing principle is therefore:

> **Detailed settlement always. Extra introspection when the #1 “most likely” pick loses. Accurate observations are recorded; no model change is required merely because of the settlement outcome.**

Top-two performance remains a prospective ranking objective, but individual wins/losses are evidence to audit, not commands to refit or reweight the framework.


---

## P-083 — Cleveland Guardians at Los Angeles Angels, MLB regular season — PREGAME FORECAST

**Append / issue time:** 2026-08-26 11:29 Australia/Melbourne (2026-08-25 18:29 PDT).  
**GAME-STATE:** PREGAME / MLB official page in warmup state; scheduled first pitch 18:38 PDT at Angel Stadium.  
**Method:** MDS-2026.08.24-v2.1 qualitative champion.  
**Selection origin:** USER_SUPPLIED.  
**Operator / exact sportsbook settlement terms:** NOT SUPPLIED. Standard full-game MLB assumptions are used for research settlement; sportsbook-specific action/listed-pitcher rules remain unknown.  
**Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING.  
**Value state:** NO VALUE DETERMINABLE.

### Previous-log disposition at issue

- **P-077 Weaver vs Aryan Jit Singh:** still LIVE on current UTR feeds; not graded.
- **P-081 Independiente del Valle vs Deportes Tolima:** started and live; not graded.
- **P-082 Monterrey vs Chicago Fire:** started and live; not graded.
- No verified completed open event was available to settle before this forecast.

### Identity / official state / confirmed participants

MLB official probable-pitcher and lineup pages confirm:

- Cleveland: **Gavin Williams, RHP — 12-7, 3.72 ERA, 201 SO**.
- Los Angeles: **Walbert Ureña, RHP — 8-9, 2.80 ERA, 109 SO**.
- Cleveland confirmed order: Steven Kwan DH; Travis Bazzana 2B; José Ramírez 3B; Jo Adell RF; Nathaniel Lowe 1B; Angel Martínez LF; Patrick Bailey C; Petey Halpin CF; Brayan Rocchio SS.
- Angels confirmed order: Zach Neto SS; Mike Trout CF; Moisés Ballesteros C; Vaughn Grissom 1B; Josh Lowe RF; Christian Moore 2B; Gustavo Campero LF; Denzer Guzman 3B; Adam Frazier DH.
- Cleveland is 66-66; Los Angeles is 52-80 entering the game.

Current injury context relevant to the lineups: Cleveland OF Chase DeLauter was scratched Aug. 24 with recurring left-hamstring tightness and is absent from the confirmed order; Rhys Hoskins remains on the IL. For the Angels, Nolan Schanuel is on the IL with an intercostal strain and Wade Meckler is on the concussion IL.

### Environment

NWS Anaheim had an **Extreme Heat Warning**, with late-afternoon temperatures in the low-to-mid 90s °F and a mostly clear evening forecast with light southerly/southwesterly wind. Heat can marginally increase carry, but there is essentially no precipitation/delay threat. This is treated as a modest run/HR-variance modifier, not an automatic Over signal.

### Current process evidence

**Gavin Williams / Angels offence**

- MLB official preview: Williams has recorded **10+ strikeouts in 6 of his last 8 starts**, 78 K in 48 1/3 innings over that span.
- He enters at 201 strikeouts in 154 2/3 innings and a roughly 32% strikeout rate.
- Last start: 5 2/3 IP, 2 ER, 4 H, 11 K vs San Francisco.
- The Angels have been one of MLB's weakest recent offences and have been particularly strikeout-prone against right-handed pitching. Their confirmed order is top-heavy around Neto/Trout, with several lower-order bats carrying weak 2026 production.
- Williams does retain an ordinary HR/hard-contact kill path; his strikeout dominance does not eliminate isolated extra-base damage.

**Walbert Ureña / Cleveland offence**

- MLB official preview notes Ureña's **2.80 ERA ranks third among qualified rookies**.
- Supporting current metrics show a 1.24 WHIP, strong home run suppression and a notably better home ERA than road ERA.
- His ERA is better than his current estimators, so some regression risk exists; command/walks are a workload risk.
- Cleveland's confirmed lineup is functional but not a high-end run-scoring unit, and DeLauter's absence removes one of its strongest current bats.

**Team / bullpen state**

- Cleveland won the series opener **4-2**, its fifth straight win, and entered this game having won six consecutive meetings against the Angels.
- Cleveland used Colin Holderman, Hunter Gaddis and Cade Smith in the opener. That creates some back-to-back leverage exposure, but not enough by itself to overturn the starter-based suppression view.
- The Angels' poor overall record and offensive form support Cleveland's side, while Ureña's quality and the low expected scoring environment support the Angels +1.5 cushion.

### Development-set mechanism references applied

- Previous baseball retrospectives repeatedly showed that **low total does not automatically imply a close margin**, so the side and total are modelled separately.
- A strong/short starter outing does not mechanically force an Under/Over; starter exit and the relief chain remain explicit.
- HR/contact tails remain live even when ERA and recent run suppression are strong.

### Underlying qualitative event forecast

The central game shape is **pitching-led and relatively close**, with Cleveland holding the better outright-win path because Williams' strikeout profile matches well against the Angels' contact problems and Cleveland has the stronger current team form.

**Qualitative run corridor:** approximately **5-7 combined runs** as the central band, with 8 a meaningful boundary/tail and 9+ requiring either early command trouble, HR clustering, or bullpen damage.

**Central score branches:** Cleveland 3-2, Cleveland 4-2, Cleveland 4-3.  
**Lower-run branches:** 2-1, 3-1.  
**Upper tail:** 5-4 / 6-3 type game if heat-assisted carry, walks or bullpen exposure combine with clustered hard contact.

### Contract geometry

- **Angels +1.5** wins on any Angels win or a one-run Angels loss; loses if Cleveland wins by 2+.
- **Guardians ML** wins on any Cleveland win.
- Therefore **Angels +1.5 and Guardians ML can both win if Cleveland wins by exactly one run**.
- **Over 6.0** wins on 7+ runs, pushes on exactly 6, loses on 0-5.
- **Under 8.0** wins on 0-7 runs, pushes on exactly 8, loses on 9+.
- Therefore **Over 6.0 and Under 8.0 both win on exactly 7 combined runs**; they are overlapping alternate totals, not opposites.

### Frozen ranking

| Rank | Candidate ID | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | `P083-C01` | **Combined Total — Under 8.0 Runs** | **LEAN** | **MEDIUM-HIGH** | Williams strikeout dominance vs a weak/K-prone Angels order + Ureña's 2.80 ERA/home run suppression + DeLauter absent | heat-assisted carry, Ureña command/walks, Williams HR contact and bullpen clustering push game to 9+ | `TOTAL-ALT` | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | `P083-C02` | **Los Angeles Angels +1.5** | **LEAN** | **MEDIUM-HIGH** | low-scoring environment + Ureña quality makes a one-run Cleveland win or Angels upset a large branch | Williams overwhelms Angels and Cleveland creates a multi-run separation inning | `SIDE-MARGIN` | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | `P083-C03` | **Cleveland Guardians ML** | **LEAN** | **MEDIUM-HIGH** | Williams matchup edge + five-game CLE win streak + Angels offensive weakness + 6 straight CLE H2H wins | Ureña matches Williams, Trout/Neto supply decisive damage, Cleveland's leveraged bullpen is less fresh | `SIDE-MARGIN` | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | `P083-C04` | **Combined Total — Over 6.0 Runs** | **FORCED RANK** | **MEDIUM** | low threshold only needs 7; warm conditions and both pitchers retain walk/HR/bullpen tails | both starters work efficiently and the game settles in the 3-2 / 3-1 / 2-1 range; exactly 6 only pushes | `TOTAL-ALT` | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Top-two priority interpretation

The top two are not selected as a hedge. They are the two strongest marginal-likelihood contracts under the central low-scoring/close-game forecast. They are dependent: both can win in a one-run Angels loss, while the total and side arise from linked but distinct target dimensions.

### Potential winner

**Cleveland Guardians — LEAN, MEDIUM-HIGH evidence.**

The outright winner call is Cleveland because Williams has the stronger strikeout/matchup profile, the Guardians enter on materially better form, and the Angels' confirmed lineup remains weak beyond Neto/Trout. The biggest failure path is Ureña continuing to suppress contact while one or two Angels extra-base events against Williams create a low-scoring upset.

### What would change the view

- A late scratch of Williams, Ureña, Trout, Ramírez or another top-order bat.
- Unexpected bullpen unavailability.
- A material operator action/listed-pitcher rule that changes settlement eligibility.
- Start crossing/live state: the pregame target must be replaced by a distinct live target rather than reusing this card.

### Sources frozen for P-083

- MLB official starting lineups: `https://www.mlb.com/starting-lineups`
- MLB Guardians probable pitchers: `https://www.mlb.com/guardians/roster/probable-pitchers`
- MLB Angels probable pitchers: `https://www.mlb.com/angels/roster/probable-pitchers`
- MLB official game preview: `https://www.mlb.com/stories/game-preview/823989`
- MLB Guardians injury report: `https://www.mlb.com/news/guardians-injuries-and-roster-moves`
- MLB Angels injury report: `https://www.mlb.com/angels/news/angels-injuries-and-roster-moves`
- NWS Anaheim: `https://forecast.weather.gov/MapClick.php?lat=33.83&lon=-117.87`
- Reuters, Aug. 24 CLE 4-2 LAA recap: `https://www.reuters.com/sports/baseball/austin-hedges-parker-messick-steer-streaking-guardians-past-angels--flm-2026-08-25/`
- Reuters, Gavin Williams Aug. 20 start: `https://www.reuters.com/sports/baseball/gavin-williams-11-ks-guardians-take-rubber-match-vs-giants--flm-2026-08-20/`

**Logging status:** complete P-083 forecast appended before delivery.  
**Next canonical ID after this append:** `P-084`.


---

## P-084 — Washington Mystics at Phoenix Mercury, WNBA regular season — PREGAME FORECAST

**Record/view:** `P-084/V01`  
**Decision set:** `DS-P084-V01`  
**Candidate policy/origin:** `USER-SUPPLIED-ONLY-v1` / `USER_SUPPLIED`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / `E1-Q` qualitative  
**Issue window:** 2026-08-26 immediately before scheduled tip in Australia/Melbourne  
**Scheduled start:** 2026-08-25 22:00 ET / 19:00 Arizona local / 2026-08-26 12:00 Australia/Melbourne  
**Venue:** Mortgage Matchup Center, Phoenix, Arizona  
**GAME-STATE at cutoff:** **PREGAME** — current WNBA/market pages still listed the fixture as upcoming at the final refresh.  
**Operator/odds supplied by user:** none.  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`.

### Previous-log gate

- `P-077` Weaver vs Aryan Jit Singh remains open because a trustworthy final has not yet been frozen in the log; no retrospective grade was forced.
- `P-081` Independiente del Valle vs Deportes Tolima is live/unresolved at this issue window and is not graded.
- `P-082` Monterrey vs Chicago Fire is live/unresolved and is not graded.
- `P-083` Cleveland Guardians at Los Angeles Angels has started and is live; it is not graded.
- No verified final was newly available to settle before P-084.

### Identity, availability and current context

Washington enters **22-15**; Phoenix enters **13-24**. Current comparison pages list Washington **9-8 on the road** and Phoenix **5-12 at home**. Washington won the first 2026 meeting **95-75** on August 9.

**Availability:** Washington's official status report was reported as **no injuries to report**. Phoenix listed **Sami Whitcomb probable** with left-knee management and **Marta Suárez out** in concussion protocol. **Kelsey Plum is off the injury report and expected to return** after missing the previous three games with a calf issue. **DeWanna Bonner is no longer in the Phoenix rotation after a contract buyout.** Confirmed starting fives were not independently frozen from an authoritative pre-tip lineup feed, so no projected five is treated as confirmed fact.

### Sport-native process evidence

**Washington**

- Season profile: approximately **82.6 points scored / 83.1 allowed**, **77.2 pace**, **105.0 offensive rating**, **105.6 defensive rating**. That is a slow-possession team with one of the league's stronger defences but a below-average offence.
- Washington's frontcourt has a meaningful rebounding edge in current comparison data (roughly **37.8 rebounds per game** vs Phoenix around **31.7**).
- Shakira Austin enters off a career-high **31 points and 10 rebounds** against Portland; Kiki Iriafen had 18 and 10 in the same game.
- Washington has won **7 of its last 10** and beat Phoenix by 20 in the first meeting.

**Phoenix**

- Season profile: approximately **84.0 points scored / 87.8 allowed**, **79.0 pace**, **106.0 offensive rating**, **110.8 defensive rating**. Phoenix plays a little faster and has allowed substantially more efficient scoring than Washington.
- Phoenix enters on a two-game losing streak and has been eliminated from playoff contention.
- Kelsey Plum's return raises Phoenix's primary-ballhandler/shot-creation ceiling but also creates role reintegration uncertainty alongside Kahleah Copper and Alyssa Thomas.
- Bonner's exit removes a versatile defensive/lineup piece, which increases uncertainty around Phoenix's wing/forward defensive combinations.

### Recent game environment and direct matchup

- First 2026 meeting: Washington **95-75 Phoenix** (170 total).
- Washington's latest completed game: **105-100** at Portland, illustrating its upper scoring/foul/late-game tail despite the season-long slow pace.
- Phoenix's latest completed game: **89-99** vs Atlanta, another high-total environment.
- These recent scores raise the upper-total branch, but raw recent points do not replace possession, lineup and efficiency analysis.

### Current market benchmark — not a model input

Contemporaneous market pages around cutoff showed Washington roughly **-1.5 to -2.5** with a game total around **165.5-167.5**. This is retained only as an external same-time benchmark. It is not an internally trained probability and does not establish value.

### Underlying qualitative event forecast

The central game shape is **close, Washington-favoured, and mid-to-upper 160s in total scoring**. Washington has the more stable defence, rebounding base and healthier roster; Phoenix's Plum return raises its offensive ceiling enough to prevent treating the first 20-point meeting as the central margin.

**Central score corridor:** roughly **Washington 84-88 / Phoenix 80-85**, with the densest practical branches around **165-171 combined points** and Washington by **1-6**.

**Lower-total branch:** Washington controls half-court pace, Phoenix's returning ball-handlers remain inefficient, and the game falls into the **156-163** range.

**Upper-total branch:** Phoenix's defensive weakness, Plum/Copper creation, Washington's interior scoring and late fouling create **174+**.

**Margin tail:** Washington's defence/rebounding recreates a substantial part of the first meeting and wins by 7+; this is the main threat to Phoenix +6.5.

### Frozen contract geometry

| Candidate | Exact supplied contract | Win / push / loss geometry | Dependence |
|---|---|---|---|
| `P084-C01` | Washington Mystics +2.5 | WIN if WAS wins or loses by 1-2; LOSS if PHX wins by 3+ | `SIDE-ALT` |
| `P084-C02` | Phoenix Mercury +6.5 | WIN if PHX wins or loses by 1-6; LOSS if WAS wins by 7+ | `SIDE-ALT` |
| `P084-C03` | Over 163.5 points | WIN at 164+; LOSS at 163 or lower | `TOTAL-ALT` |
| `P084-C04` | Under 173.5 points | WIN at 173 or lower; LOSS at 174+ | `TOTAL-ALT` |

**Overlap:** Mystics +2.5 and Mercury +6.5 both win when Washington wins by 1-6. Over 163.5 and Under 173.5 both win from **164 through 173**. These are not independent confirmations.

### Frozen ranking

| Rank | Candidate ID | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | `P084-C01` | **Washington Mystics +2.5** | **SUPPORTED** | **MEDIUM-HIGH** | healthier roster + stronger defence/rebounding + 22-15 form base means Washington can win outright or survive a narrow Phoenix win | Plum return immediately lifts PHX creation and Washington's road defence gives up a 3+ point loss | `SIDE-ALT` | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | `P084-C02` | **Phoenix Mercury +6.5** | **LEAN** | **MEDIUM-HIGH** | current game projects much closer than the first H2H because Plum returns at home; +6.5 protects a broad Washington-by-1-to-6 central branch | Washington's defence/rebounding repeats the August 9 separation and wins by 7+ | `SIDE-ALT` | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | `P084-C04` | **Under 173.5 points** | **LEAN** | **MEDIUM** | Washington's slow pace/strong defence and a 173.5 ceiling leave room above the central 165-171 corridor | Phoenix defensive leakage + Plum/Copper pace/creation + late fouling produce 174+ | `TOTAL-ALT` | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | `P084-C03` | **Over 163.5 points** | **LEAN** | **MEDIUM** | Phoenix's weak defence, Plum return, recent 170+ environments and Washington's improving interior scoring make 164+ plausible | Washington successfully suppresses pace/transition and Phoenix's reintegrated offence stagnates into the low 160s or below | `TOTAL-ALT` | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Top-two priority interpretation

Ranks #1 and #2 are the two strongest marginal-likelihood contracts, not an intentionally diversified hedge. They are strongly dependent and can both win in the same close Washington victory. If rank #1 later loses, the settlement must receive the standing extra rank-order audit across all four rows; no automatic model change follows.

### Potential winner

**Washington Mystics — LEAN, MEDIUM-HIGH evidence.**

Washington is the preferred outright winner because of its healthier roster, better defence/rebounding, stronger record/current form and the direct 95-75 win earlier this month. Phoenix's home court and Plum's return keep the winner call below `SUPPORTED`; a narrow Phoenix win is an ordinary live branch rather than a remote tail.

### Material uncertainties

- Phoenix's exact first unit and minute distribution with Plum returning and Bonner gone.
- Whitcomb's probable status and any late restriction.
- Whether Phoenix's high-usage creators improve efficiency immediately or increase turnover/shot-selection volatility.
- Late starting-five changes after the information cutoff.

### Sources frozen for P-084

- WNBA official game page: `https://www.wnba.com/game/1022600286`
- WNBA official Aug. 9 recap: `https://www.wnba.com/watch/video/game-recap-washington-mystics-95-phoenix-mercury-75-08-09-2026`
- Phoenix Mercury 2026 schedule: `https://mercury.wnba.com/26season`
- Washington Mystics game notes: `https://mystics.wnba.com/game-notes`
- Washington current status report as surfaced from the team's official post; Phoenix availability as current pregame reporting
- Basketball-Reference 2026 Washington/Phoenix team and lineup pages for pace/rating/starting-lineup history
- Contemporaneous market benchmark pages around issue time for external spread/total context only

**Logging status:** P-084 appended before delivery.  
**Next canonical ID:** `P-085`.


---

## P-085 — Lobos Puebla vs Fuerza Regia, LNBP regular season — LIVE START-CROSSING FORECAST

**Record/view:** `P-085/V01`  
**Decision set:** `DS-P085-V01`  
**Candidate policy/origin:** `USER-SUPPLIED-ONLY-v1` / `USER_SUPPLIED`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / `E1-Q` qualitative  
**Issue state:** **LIVE — Lobos Puebla 25, Fuerza Regia 12; Q1 02:19 remaining** on the newest internally consistent live feed retrieved before issue.  
**Scheduled fixture:** LNBP regular season, Gimnasio Miguel Hidalgo, Puebla.  
**Start-crossing rule:** user requested an upcoming-game forecast, but scheduled start passed during research. The original four full-game contracts are preserved and re-ranked conditionally from the verified live state. The original pregame lines may no longer be available.  
**Operator/odds supplied by user:** none.  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`.

### Previous-log gate at issue

No earlier open item was newly verified FINAL in the status sweep immediately before P-085. P-077, P-081, P-082 and P-083 remained open/live/unresolved in current search results; P-084 had only just reached its scheduled tip window and was not settled. No result was forced.

### Current event state and baseline

Current live source: 365Scores showed **Lobos Plateados 25-12 Fuerza Regia with 2:19 remaining in Q1**. This is a 13-point Puebla lead with approximately 32:19 of regulation remaining.

Pregame/season context before the start crossing:

- Both clubs entered **8-5**.
- RealGM current LNBP table: Fuerza Regia **88.8 PPG / 88.2 OPPG**; Lobos Plateados **82.5 PPG / 81.4 OPPG**.
- Lobos entered on a **five-game winning streak** and were **5-2 at home**; Fuerza Regia were 3-2 away.
- The teams played the previous night in Puebla and Lobos won **98-88** (186 combined points).
- In that first game Lobos led 31-17 after Q1 and 59-41 at halftime. Fuerza Regia improved sharply after halftime, winning Q3 32-25 and Q4 15-14, but the early deficit was too large.
- Fuerza Regia's official recap reported 53.45% team shooting in that first game, 41.38% from three and 22 assists despite the loss, showing that comeback/offensive efficiency remains a real live branch rather than Puebla having an automatic runaway path.
- Lobos' reported top scorers in game one were Michael Myers 18, Shaquille Johnson 17 and Elias King 16; Fuerza Regia were led by Jimond Ivey 23 and Scott Bamforth 15.

### Live basketball process interpretation

The exact live state changes the side distribution materially:

- **Puebla +2.5** now has a 15.5-point effective cushion relative to Fuerza Regia -2.5 because Puebla already leads by 13.
- Fuerza Regia has demonstrated a strong second-half response against this opponent one night earlier, so the comeback branch is ordinary rather than remote; however, to cover -2.5 from the current state it must outscore Puebla by at least 16 over the remaining regulation time.
- The total state is also materially altered. There are already **37 points with 2:19 left in Q1**. The observed first-quarter scoring rate is high, but the model does **not** extrapolate that rate linearly. The stronger evidence is the combination of the current fast start, the 186-point first meeting and Fuerza Regia's season 88.8 PPG / 88.2 OPPG environment.
- A mid-game defensive slowdown remains plausible: Lobos' season games are lower scoring than Fuerza Regia's, and one hot quarter does not determine Q2/H2 efficiency.

### Exact supplied contract geometry from the live state

| Candidate ID | Original full-game contract | Settlement geometry | Live implication |
|---|---|---|---|
| `P085-C01` | Lobos Puebla +2.5 | Puebla wins if it wins outright or loses by 1-2; no push | Already +13 on scoreboard; Fuerza must swing at least 16 points from here to defeat this contract |
| `P085-C02` | Fuerza Regia -2.5 | Regia must win by 3+; no push | Requires a 16+ point net comeback from current state |
| `P085-C03` | Over 171.5 | Wins at 172+ | 37 already scored; needs 135+ over remaining ~32:19 |
| `P085-C04` | Under 171.5 | Wins at 171 or fewer | Requires remaining scoring of 134 or fewer |

The two side rows are exact opposites under matching full-game terms. The two total rows are exact complements. They are ranked from one conditional live score/margin view, not as four independent theses.

### Conditional live scenario map

**Central branch:** Puebla's early lead compresses somewhat as Fuerza Regia improves after Q1, but Lobos retain enough home/offensive control to avoid losing by 3+; the game remains in an elevated scoring environment.

**Lower-total branch:** Q2 and Q3 slow materially after the hot opening; Lobos use longer possessions protecting the lead; Fuerza Regia's perimeter efficiency regresses. This is the main Under 171.5 route.

**Upper-total branch:** Fuerza Regia's comeback requires faster pace and more three-point volume; Puebla continues converting inside/transition chances; late fouling extends the game. This supports Over 171.5.

**Margin reversal tail:** Fuerza Regia repeats and exceeds the previous night's second-half adjustment, wins the remaining three quarters decisively and turns the 13-point deficit into a 3+ point road win. This is the required kill path for Puebla +2.5 and the only route to Regia -2.5.

### Frozen live ranking

| Rank | Candidate ID | Exact original contract | Verdict | Evidence | Central mechanism | Strongest kill path | Dependence | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | `P085-C01` | **Lobos Puebla +2.5** | **SUPPORTED** | **HIGH for the conditional live state** | 13-point current lead + five-game winning streak + 98-88 win last night + home profile; Regia must create a 16-point net swing to cover -2.5 | Regia's previous second-half adjustment becomes a full comeback and Puebla collapses offensively/turns it over | `SIDE-EXACT` | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | `P085-C03` | **Over 171.5 points** | **LEAN** | **MEDIUM-HIGH** | 37 points already scored late Q1 + previous meeting totaled 186 + Regia season environment near 177 combined points + comeback script can raise pace/late fouling | sharp Q2/H2 regression, Puebla slows with lead, perimeter shooting cools and game lands in mid-160s | `TOTAL-EXACT` | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | `P085-C04` | **Under 171.5 points** | **FORCED RANK** | **MEDIUM-LOW** | one hot quarter need not persist; Puebla's season scoring environment is much lower than Regia's; lead-protection can suppress possessions | current pace persists, Regia comeback forces tempo and late fouling pushes total past 172 | `TOTAL-EXACT` | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | `P085-C02` | **Fuerza Regia -2.5** | **AVOID** | **LOW-MEDIUM** | Regia has enough offence and showed strong second-half adjustment the previous night | must overcome the current 13-point deficit and then win by 3+, a 16-point net swing against a team on a five-game streak | `SIDE-EXACT` | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

### Top-two priority interpretation

Ranks #1 and #2 are the two strongest conditional full-game contracts at issue. They are not selected to hedge: #1 comes from the current margin state, while #2 comes from the total/exposure state. If #1 later loses, the standing settlement rule requires the extra four-pick rank-order audit because it was the "most likely" row.

### Potential winner

**Lobos Puebla — LEAN / upgraded by live state.**

Pregame the market was close and in some snapshots Fuerza Regia was a slight favourite. The verified live state changes that materially: Puebla leads by 13, is at home, has won five straight and beat Fuerza Regia by 10 the previous night. The strongest failure path is the same one Fuerza Regia displayed in game one—superior second-half ball movement and perimeter efficiency—but it now needs to be large enough to erase the live deficit completely.

### Sources frozen for P-085

- 365Scores current live team page / score state: `https://www.365scores.com/es/basketball/team/fuerza-regia-6861`
- 365Scores current LNBP matchup/standings pages
- RealGM 2026-27 Mexican LNBP standings: `https://basketball.realgm.com/international/league/76/Mexican-LNBP/standings`
- Fuerza Regia official game-one recap / second-game preview: `https://www.fuerzaregia.com.mx/noticias/fuerza-regia-buscara-empatar-la-serie-en-el-segundo-duelo-ante-lobos`
- Puebla game-one recap: `https://puebla.quadratin.com.mx/deportes/vence-lobos-puebla-a-fuerza-regia-y-va-a-copa-value/`
- Caliente pregame market snapshot for exact alternate-line context: `https://sports.caliente.mx/es_MX/e/32786749/Lobos-de-Puebla-vs-Fuerza-Regia`

**Logging status:** P-085 LIVE start-crossing forecast appended before delivery.  
**Next canonical ID:** `P-086`.

## Operational source-hierarchy update — 2026-08-26

**Status:** ACTIVE PROSPECTIVE RESEARCH CONTROL  
**Scope:** All future Sports Research forecasts, live updates, settlements, retrospectives and sport-reference research.

### Betting-platform source restriction

Betting operators, sportsbook editorial networks, tipster pages and betting-analysis sites are **not primary sports-evidence sources**. They may be used mainly for:

- verifying that an exact contract/line is currently offered;
- capturing same-time odds, operator terms, push/void/OT/action rules and market availability;
- recording a market benchmark when the value/market-comparison lane explicitly requires it.

They should **not ordinarily control** claims about player/team quality, injuries, lineups, form, role, matchup strength, pace, xG, Statcast, shot quality, bullpen quality, weather or other sport-native process variables when a better non-betting source exists. Sportsbook editorial content (for example DraftKings Network-style analysis) is corroborative/discovery material only unless the underlying fact is independently verified.

### Preferred evidence hierarchy for sporting analysis

1. **Official governing body / league / competition / team / match centre** for identity, schedule, rules, lineups, injuries, live state, official statistics and final results.
2. **Official or league-operated statistical platforms** where available (for example MLB Baseball Savant/Statcast, WNBA/NBA official stats, KBO official statistics, UEFA/CONMEBOL official match statistics).
3. **StatMuse where its league/metric coverage is appropriate**, especially for current NBA/WNBA team/player statistical queries and compact recent/season comparisons; cross-check decisive volatile facts with official sources.
4. **Established non-betting statistical databases and specialist data providers** with defined methodology/coverage (for example Baseball Reference, FanGraphs, FotMob, FBref, Understat/Opta-derived sources where appropriate, RealGM, Tennis Abstract/ITF/ATP/WTA resources, official federation databases).
5. **Reputable named journalism** for verified current reporting not yet reflected in official releases.
6. **Betting platforms / market aggregators** for contract, price and settlement terms only, with sports-analysis claims independently verified wherever practicable.

### Comprehensive-source rule

Comprehensive research means using enough **independent, field-owning sources** to cover the decision-driving chain, not accumulating many sportsbook articles. For each forecast, prefer a diversified evidence set covering:

- identity/state/rules;
- participants/availability/roles;
- sport-native process statistics;
- opponent-adjusted recent and season context;
- venue/environment where relevant;
- direct matchup mechanisms;
- one strong contrary/kill-path branch;
- exact market/contract verification separately.

If an official or specialist non-betting source conflicts with sportsbook editorial analysis, the field-owning source controls the sporting fact. Betting-market information remains separate from the sports forecast unless the market-informed lane is explicitly being used.

---

## P-086 — Club León vs Real Salt Lake — Leagues Cup quarterfinal — START PASSED / LIVE STATE NOT VERIFIED

**Record/view:** `P-086/V01`  
**Decision set:** `DS-P086-V01`  
**Candidate origin:** `USER_SUPPLIED + RESEARCH-VERIFIED MARKET`  
**Method/cohort:** `MDS-2026.08.24-v2.1` / qualitative E1-Q process  
**Competition:** 2026 Leagues Cup, Quarterfinal  
**Venue:** Dick's Sporting Goods Park, Commerce City, Colorado — neutral-site competition fixture  
**Scheduled kickoff:** 2026-08-25 20:30 America/Denver = 2026-08-26 12:30 Australia/Melbourne  
**Issue-state classification:** `START PASSED / LIVE STATE NOT VERIFIED`  
**Operator supplied:** `NO`  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`  

### State-gate disposition

The scheduled kickoff passed during research. Multiple current pages still exposed pre-match/scheduled content and no sufficiently trustworthy source returned a consistent exact live score + minute at the final refresh. Under the start-crossing rule, this record **does not pretend to be pregame and does not publish an actionable live forecast**. The first-half 0.5 contract is especially state-sensitive because it could already be partially elapsed or settled. No fabricated live score, clock, card, substitution or corner state is inserted.

The pre-start research ordering below is preserved only as a **NON-ACTIONABLE / PERFORMANCE-INELIGIBLE research reference**. It is not counted as a prospective live forecast because the exact live state could not be frozen before issue.

### Verified pre-start event context

- Official/club competition material identifies León as the Liga MX #1 seed after a 3-0-0 Phase One and Real Salt Lake as the MLS #4 seed after a 2-0-1 Phase One with a +7 goal differential.
- León entered on a six-match winning streak across Leagues Cup and Liga MX, scoring 11 and conceding 4 during that run.
- León's Leagues Cup Phase One: 1-0 Nashville, 2-1 Orlando, 3-2 Inter Miami. Two of the three matches had at least one first-half goal; two of three cleared 1.5 full-match goals.
- Real Salt Lake's Phase One: 1-1 Tigres (lost shootout), 4-0 Atlante, 3-0 FC Juárez. All three had a first-half goal and all three cleared 1.5 goals.
- RSL's official pre-quarterfinal material notes the club's active MLS winless streak had reached seven after a 2-1 loss at Orlando, but key attackers Sergi Solans, Diego Luna, Morgan Guilavogui and other regulars were managed/rotated in league play around the cup window.
- The fixture is at Dick's Sporting Goods Park in Colorado rather than either club's normal home stadium; RSL has greater geographic/venue familiarity but the competition is neutral-site.
- NWS Commerce City forecast carried a chance of showers/thunderstorms around the evening window. Weather is treated as variance/delay risk, not an automatic total direction.

### Goal-process evidence

**First-half O0.5 pre-start research:** five of the six combined Leagues Cup Phase One matches across these teams contained a first-half goal (León 2/3, RSL 3/3). This is descriptive support only and not a generated probability.

**Full-match O1.5 pre-start research:** five of the six combined Phase One matches cleared 1.5 goals (León 2/3, RSL 3/3). León's six-match winning run and RSL's strong Phase One attacking output support a two-goal central branch, while knockout caution and the neutral venue remain ordinary Under kill paths.

### Corner-process evidence

Specialist recent-sample corner data placed León near 5.0 corners for / 5.2 against (about 10.2 combined) and RSL's small recent sample near 6.8 for / 8.4 against (high-variance, roughly 15.2 combined). Recent RSL total-corner examples included 9, 17, 13, 18 and 19. The exact `Over 7.5 total corners` threshold was available in current market listings.

However, the full current crosses → blocked-crosses/shots → end-line entries → clearances → corner chain and the user's operator-specific corner provider were not frozen. Therefore any corner direction remains capped at `FORCED RANK`, not `LEAN`/`SUPPORTED`.

### Pre-start research ordering — NON-ACTIONABLE / PERFORMANCE-INELIGIBLE

| Research rank | Exact contract | Research verdict | Evidence | Central mechanism | Strongest kill path | Status |
|---:|---|---|---|---|---|---|
| 1 | Combined goals **Over 1.5** | LEAN | MEDIUM-HIGH | Both clubs showed multiple independent scoring routes in Phase One; 5/6 combined Phase One matches cleared 1.5 | knockout caution + finishing suppression creates 0-0/1-0 | NON-ACTIONABLE — live state not verified |
| 2 | 1st-half goals **Over 0.5** | LEAN | MEDIUM | 5/6 combined Phase One matches had a first-half goal; both teams have recent early-score mechanisms | controlled opening / no early conversion; contract may already be partially elapsed or settled | NON-ACTIONABLE — live state not verified |
| 3 | **Real Salt Lake or Draw (X2)** | FORCED RANK | MEDIUM | strong Phase One (+7 GD), rested/managed attacking core, Colorado familiarity | León's six-match winning run and Arcila-led form carry through neutral venue | NON-ACTIONABLE — live state not verified |
| 4 | Total corners **Over 7.5** | FORCED RANK | MEDIUM-LOW | recent combined corner baselines sit above eight and both teams use wide/transition attacks | early efficient goals reduce repeated wide pressure; direct corner-causation/provider chain incomplete | NON-ACTIONABLE — live state not verified |

### Potential winner research view

**Real Salt Lake — FORCED WINNER / LOW-MEDIUM confidence (90-minute research view only).**

RSL's strong Phase One, better recent Leagues Cup goal differential, Colorado familiarity and managed cup attackers provide the narrow pre-start case. León's six straight wins and current finishing form make the opposite branch substantial. Because exact live state was not verified after kickoff, this winner view is **not an actionable or performance-eligible issued prediction**.

### Settlement/qualification terms note

Leagues Cup knockout matches tied after 90 minutes proceed directly to penalties under the 2026 knockout format. A 90-minute winner and the team to advance are therefore distinct contracts.

### Sources frozen for P-086 research reference

- Real Salt Lake official quarterfinal/storyline material: `https://www.rsl.com/news/real-salt-lake-faces-club-leon-in-2026-leagues-cup-quarterfinals`
- Real Salt Lake official current-form recap: `https://www.rsl.com/news/real-salt-lake-winless-streak-in-mls-extends-to-seven-with-2-1-loss-at-orlando`
- Real Salt Lake official Phase One recap vs FC Juárez: `https://www.rsl.com/news/real-salt-lake-keeps-leagues-cup-hopes-alive-in-3-0-victory-over-fc-juarez`
- Leagues Cup official match/preview and Phase One recaps
- ESPN current match page for event identity/live page
- NWS Commerce City weather forecast
- Specialist corner-rate pages for research-only derivative context
- Current market pages used only to confirm exact O1.5 / 1H O0.5 / X2 / O7.5-corner contract availability

**Logging status:** P-086 appended as `START PASSED / LIVE STATE NOT VERIFIED`; no false pregame/live forecast issued.  
**Next canonical ID:** `P-087`.

---

## Settlement append — P-081 — Independiente del Valle vs Deportes Tolima

**Settlement status:** CLOSED / FINAL  
**Verified final:** Independiente del Valle 3-1 Deportes Tolima (0-0 HT), aggregate 4-1.  
**Primary final source:** CONMEBOL Libertadores official match report, 25 Aug 2026.  
**Supporting derivative-stat source:** WinComparator match-stat page for total corners (IDV 3, Tolima 2 = 5).  
**Settlement note:** operator was not supplied; goal/side rows use regulation result, corner row is research-grade provider settlement and sportsbook-specific treatment remains unknown-definition.

### Contract-by-contract settlement

| Rank | Candidate | Issued contract | Final basis | Outcome | Settlement arithmetic |
|---:|---|---|---|---|---|
| 1 | `P081-C01` | IDV or Draw — 1X | IDV won 3-1 | **WIN** | IDV regulation win satisfies 1X |
| 2 | `P081-C02` | Over 1.5 goals | 4 regulation goals | **WIN** | 4 >= 2 |
| 3 | `P081-C03` | 1H Over 0.5 goals | HT 0-0; first goal 59' | **LOSS** | first-half goals = 0 |
| 4 | `P081-C04` | Over 7.5 corners | 5 total corners (3-2) | **LOSS** | 5 < 8 |

**Potential winner:** Independiente del Valle — **WIN**.

### Detailed retrospective

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Observation / reference value |
|---|---|---|---|---|---|
| IDV's aggregate lead and home state made 1X the strongest branch | IDV controlled the decisive moments and won outright 3-1 | Stronger than the minimum protected-side requirement | Knowable | **COMPLIANT** | Protected side correctly ranked #1; tie-state asymmetry mattered |
| Tolima's need to chase could create a 2+ goal game | All four goals came after halftime; IDV punished the opened second-half state | Total thesis right, timing later than expected | Partly knowable | **COMPLIANT** | Full-game chase-state mechanism was more robust than first-half timing |
| First-half goal was favored from prior early-score evidence | First half finished 0-0 with Tolima unable to register a shot on target | Early-goal extrapolation overstated | Knowable only probabilistically | **INCONCLUSIVE** | Do not let prior first-leg early goal dominate second-leg 1H timing |
| Chasing Tolima plus cross/block/clearance process could push corners above 7.5 | Only 5 corners despite Tolima's need to attack | Direct event rate did not translate into enough corner endpoints | Partly knowable | **COMPLIANT / DERIVATIVE LOW-EVIDENCE** | Reinforces separate corner-event process and low confidence without provider completeness |

**Rank-1 loss extra audit:** not triggered; rank #1 won.  
**Top-two priority result:** **2/2 WIN**.  
**Model change:** none; observations recorded only.

Sources retained:  
- CONMEBOL official final: https://gol.conmebol.com/libertadores/es/news/independiente-del-valle-avisa-elimino-tolima-y-va-por-el-campeon-defensor-en-cuartos  
- Research-grade match stats/corners: https://www.wincomparator.com/predictions/independiente-del-valle-deportes-tolima-8734931/

---

## Settlement append — P-082 — CF Monterrey vs Chicago Fire FC

**Settlement status:** CLOSED / FINAL  
**Verified final:** Monterrey 2-1 Chicago Fire (1-0 HT).  
**Primary final source:** MLS/Leagues Cup official match report.  
**Goal times:** Víctor Guzmán 45+4', Philip Zinckernagel 59', Orbelín Pineda 83'.  
**Supporting final-stat source:** match-stat report showing Monterrey 5 corners, Chicago 4 = 9 total.  
**Settlement note:** operator was not supplied; corner result is research-grade provider settlement.

### Contract-by-contract settlement

| Rank | Candidate | Issued contract | Final basis | Outcome | Settlement arithmetic |
|---:|---|---|---|---|---|
| 1 | `P082-C01` | Over 1.5 goals | 3 regulation goals | **WIN** | 3 >= 2 |
| 2 | `P082-C02` | 1H Over 0.5 goals | Monterrey scored 45+4' | **WIN** | first-half goals = 1 |
| 3 | `P082-C03` | Chicago Fire or Draw — X2 | Monterrey won 2-1 | **LOSS** | neither Chicago win nor draw occurred |
| 4 | `P082-C04` | Over 7.5 corners | 9 total corners (5-4) | **WIN** | 9 >= 8 |

**Potential winner:** Chicago Fire — **LOSS**.

### Detailed retrospective

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Observation / reference value |
|---|---|---|---|---|---|
| Two strong attacking XIs supported 2+ total goals | Three goals arrived, including a late Monterrey winner | Central goal branch realized | Knowable | **COMPLIANT** | Full-game goal exposure correctly ranked #1 |
| Recent early-goal profiles supported 1H O0.5 | Guzmán scored in first-half stoppage time | Correct but boundary-sensitive timing | Knowable only probabilistically | **COMPLIANT / BOUNDARY-SENSITIVE** | First-half line won late; do not overstate margin of correctness |
| Chicago's form/home setting supported X2 | Monterrey's individual quality converted the decisive late chance; Chicago equalized but could not hold | Monterrey ceiling was underweighted in side ranking | Knowable | **INCONCLUSIVE** | For cross-league knockout sides, confirmed top-end attacking quality can outweigh recent-form edge |
| 8+ corners plausible from both teams' wide attack | Final total 9 corners | Direction correct, only 1 above threshold | Partly knowable | **COMPLIANT / BOUNDARY-SENSITIVE** | Corner hit is not model validation; derivative remains low-confidence |
| Chicago narrow winner lean | Monterrey won 2-1 | Winner call wrong | Knowable | **INCONCLUSIVE** | Side/winner should remain below stronger goal contracts when matchup is balanced |

**Rank-1 loss extra audit:** not triggered; rank #1 won.  
**Top-two priority result:** **2/2 WIN**.  
**Model change:** none; observations recorded only.

Sources retained:  
- MLS official final: https://www.mlssoccer.com/competitions/leagues-cup/news/chicago-fire-exit-leagues-cup  
- Supporting final stats: reported Monterrey 5 corners / Chicago 4.

---

## P-087 — India vs Sri Lanka, 2nd Test, Day 4 — PRE-START DAY-4 LIVE-STATE RESEARCH CARD

**Record/view:** `P-087/V01`  
**Decision set:** `DS-P087-V01`  
**Sport/format:** Test cricket — India tour of Sri Lanka 2026, 2nd Test  
**Venue:** Sinhalese Sports Club, Colombo  
**Scheduled match:** 23–27 August 2026  
**Day-4 scheduled resumption:** 10:00 Sri Lanka local time  
**Request cutoff:** approximately 2026-08-26 14:10 Australia/Melbourne = 09:40 Sri Lanka local time  
**GAME-STATE:** **DAY 4 NOT YET STARTED AT CUTOFF — overnight state preserved**  
**Method:** MDS-2026.08.24-v2.1 qualitative champion  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Candidate origin:** USER_SUPPLIED  
**Requested output:** best 2 of 4 supplied contracts + potential winner.

### Previous-log gate

P-081 and P-082 were verified final and settled immediately before this append. P-077 remained unresolved in current feeds; P-083/P-084/P-085/P-086 were still live or not safely final at the research cutoff and were left open.

### Exact target/state freeze

**India 1st innings:** 503/9 declared.  
**Sri Lanka 1st innings:** 265/8 after 83.4 overs.  
**Sri Lanka trail:** 238 runs.  
**Overnight batters:** Sonal Dinusha 85* (137), Lahiru Kumara 8* (50).  
**Last batter:** Asitha Fernando.  
**Current ninth-wicket partnership:** 35 runs from 92 balls.  
**Sri Lanka need:** 22 additional runs to reach 287 and beat the 286.5 innings line; 39 additional runs to reach 304 and avoid the follow-on threshold.  
**India bowling:** Prasidh Krishna 3 wickets, Manav Suthar 3, Mohammed Siraj 1, Ravindra Jadeja 1; India had already taken the second new ball before stumps.

Targets are separate:
- `TEST-SL-1INN-TOTAL-v1`: Sri Lanka completed first-innings runs from state 265/8 to innings termination.
- `TEST-MATCH-RESULT-v1`: full Test result through scheduled completion under Test match rules.

### Strip / conditions hard gate

**STRIP STATUS:** OBSERVED / MATCH-EVIDENCE AVAILABLE. Pre-match Reuters reporting quoted Sri Lanka captain Dhananjaya de Silva describing the SSC pitch as dry, good for batting and expected to offer carry/bounce early; through three days the surface has supported both batting and wicket-taking rather than behaving as an extreme spin trap.  
**MATCH CONDITIONS STATUS:** OBSERVED / WEATHER RISK MATERIAL. Day 3 ended early because of rain and fading light. Current Colombo forecasts continue to show meaningful Day-4 shower/rain risk; this primarily increases the draw branch and can create stop-start new-ball conditions. No automatic Under is assigned from rain alone.

### Sport-native exposure / rate interpretation

**Sri Lanka first-innings total:** only two wickets remain, but Dinusha is set on 85 and the ninth-wicket pair has already survived 92 balls. The key regime change at the restart is the fresh morning plus a still-new second ball, allowing India to return to Krishna/Siraj rather than the late-day spin/light compromise. The 286.5 threshold is only 21 runs above the overnight score, so the line is genuinely close rather than a high-confidence tail fade.

**Match result:** India have already banked a 238-run first-innings lead with two Sri Lankan wickets remaining and two scheduled days left. If Sri Lanka are dismissed below 304, India retain the option to enforce the follow-on. Sri Lanka's top order is already depleted by the absences of Kusal Mendis, Dinesh Chandimal and Pathum Nissanka, and India have taken 8 wickets despite substantial lower-order resistance. The principal threat to an India win is lost playing time from rain/light plus another long Sri Lankan resistance phase, not a current Sri Lanka match-winning position.

### Scenario map

**Central:** India use the second new ball/fresh morning to take the last two wickets relatively early, retain a very large lead and have enough remaining overs across Days 4–5 to press for 12 more wickets.  
**Sri Lanka innings upper branch:** Dinusha farms strike effectively, Kumara/Asitha survive, and the tail adds 22+ before India finish the innings.  
**Draw branch:** repeated rain/light interruptions materially reduce available overs, Sri Lanka's tail extends the first innings and/or the second innings produces another long resistance phase.  
**India-win acceleration branch:** Sri Lanka are bowled out below 287/304 quickly, India enforce the follow-on, and the worn surface/new-ball spells produce another wicket cluster.

### Frozen ranking — BEST 2 ONLY

| Rank | Candidate ID | Exact supplied contract | Verdict | Evidence | Central mechanism | Strongest kill path | Performance role |
|---:|---|---|---|---|---|---|---|
| **1** | `P087-C03` | **India Win** | **LEAN** | **MEDIUM-HIGH** | 238-run lead, only two SL first-innings wickets remain, follow-on potentially available, two scheduled days left, depleted SL batting and multi-bowler wicket threat | rain/light removes a large block of overs and Sri Lanka repeat long lower-order/second-innings resistance | `PRIMARY_FORMAL` |
| **2** | `P087-C02` | **Sri Lanka 1st innings Under 286.5** | **LEAN** | **MEDIUM** | fresh Day-4 restart + second new ball + only Kumara/Asitha behind Dinusha; India need two wickets before 22 further runs | Dinusha remains set, farms strike and the tail extends the already 35-run ninth-wicket stand beyond another 21 runs | `PRIMARY_FORMAL` |

### Non-selected supplied rows

- `P087-C01` — Sri Lanka 1st innings Over 286.5: **credible but slightly weaker than Under 286.5** because the restart/new-ball regime increases immediate wicket hazard. This is a near-boundary call, not an AVOID.
- `P087-C04` — Draw: **material live branch**, primarily because of weather and lost-time risk, but still ranked below India Win because India's current lead/wicket state gives them several routes to force a result if enough overs are available.

### Potential winner

**India — LEAN.**  
The same match-state logic as rank #1 controls: India have the dominant scoreboard position and the larger number of remaining result pathways. The strongest failure path is weather-driven time loss rather than Sri Lanka presently taking control of the cricket.

### Sources retained for P-087

- Sri Lanka Cricket official series schedule: https://srilankacricket.lk/2026/07/india-national-mens-tour-of-sri-lanka-2026/  
- Cricbuzz live score/commentary for overnight state and Day-4 resumption timing: https://www.cricbuzz.com/live-cricket-scores/163017/2nd-test-india-tour-of-sri-lanka-2026  
- Indian Express live scorecard for overnight batting/bowling state: https://indianexpress.com/section/sports/cricket/live-score/sri-lanka-vs-india-2nd-test-live-score-full-scorecard-highlights-india-in-sri-lanka-2-test-series-2026-slin08232026272146/  
- Reuters pre-match pitch observation / Dhananjaya de Silva comments: Reuters Connect item `CRICKET-TEST-LKD-IND` dated 22 Aug 2026  
- Reuters on Sri Lanka batting absences: https://www.reuters.com/sports/cricket/sri-lankas-mendis-chandimal-out-second-test-against-india-says-coach-kirsten-2026-08-19/  
- Sri Lanka Department of Meteorology portal: https://meteo.gov.lk/en/  
- Current Colombo weather cross-checks used only for interruption risk, not as a deterministic direction.

**Logging status:** P-087 appended before delivery.  
**Next canonical ID:** `P-088`.

---

## P-084 settlement — Washington Mystics at Phoenix Mercury, WNBA

**Settlement appended:** 2026-08-26 before P-088 issue.  
**Verified final:** Washington Mystics **94**, Phoenix Mercury **84**; combined total **178**; Washington margin **+10**.  
**Primary settlement sources:** StatMuse final game page; CBS Sports/AP recap.  
**Source URLs:** `https://www.statmuse.com/wnba/game/8-25-2026-was-at-phx-8031`; `https://www.cbssports.com/wnba/gametracker/recap/WNBA_20260825_WAS%40PHO/`.

### Contract-by-contract settlement

| Original rank | Frozen contract | Outcome | Exact settlement arithmetic |
|---:|---|---|---|
| 1 | Mystics +2.5 | **WIN** | Washington won outright by 10. |
| 2 | Mercury +6.5 | **LOSS** | Phoenix lost by 10; needed to lose by 6 or fewer or win. |
| 3 | Under 173.5 points | **LOSS** | 94 + 84 = **178**, which is 4.5 above the line. |
| 4 | Over 163.5 points | **WIN** | 178 >= 164. |

**Potential winner:** Washington Mystics — **WIN**.

### Detailed retrospective

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Accurate observation for future reference |
|---|---|---|---|---|---|
| Washington +2.5 was the strongest protected side because of health, defence, rebounding and form | Washington controlled most of the game and won by 10; Citron scored 19, Iriafen 18/10, Austin 16 | Central side direction was correct and margin exceeded the protected threshold comfortably | Knowable | **COMPLIANT** | Washington's stable two-way profile was more durable than Phoenix's home/returning-player countercase |
| Phoenix +6.5 could survive a competitive game with Plum returning | Phoenix lost by 10; Plum returned but played only 17 minutes and scored 10 | The return improved available creation less than assumed, while Washington's depth/efficiency created separation | Partly knowable | **INCONCLUSIVE** | Returning-player status must be separated from expected workload and immediate impact; minutes uncertainty matters |
| Under 173.5 was supported by Washington's slower pace/defence | Washington shot efficiently enough to score 94; game reached 178 despite Phoenix scoring only 84 | Offensive efficiency, not simply pace, broke the upper total | Knowable as a shooting-efficiency tail | **COMPLIANT / TOTAL MISS** | A slow/defensive team can still drive an Over if its own offence converts at unusually high efficiency; possession and efficiency must remain separate |
| Over 163.5 retained a credible route through Phoenix defence and late scoring | 178 total | Lower alternate Over correctly captured a broad scoring band | Knowable | **COMPLIANT** | Alternate totals with a 10-point overlap are one score-distribution thesis, not independent confirmations |

**Rank-1 loss extra audit:** not triggered; rank #1 won.  
**Top-two priority result:** **1 WIN / 1 LOSS**.  
**Model change:** none; observations recorded only.

---

## P-088 — Howlers Sporting Singtam vs Sikkim Boys Football Club — SFA A Division S-League — PREGAME FORECAST

**Record/view:** `P-088/V01`  
**Decision set:** `DS-P088-V01`  
**Candidate origin:** user-supplied goal thresholds + analyst-selected side/corner rows  
**Competition:** SFA A Division S-League 2026, Sikkim, India  
**Venue:** Paljor Stadium, Gangtok — the competition schedule is being played at Paljor Stadium  
**Scheduled kickoff:** **2026-08-26 11:00 IST / 15:30 Australia/Melbourne**  
**Research cutoff:** approximately **2026-08-26 15:09 Australia/Melbourne**  
**GAME-STATE:** **PREGAME** — current schedule/stat feeds still listed the fixture without a live score.  
**Method:** MDS-2026.08.24-v2.1 qualitative champion  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

### Previous-log gate

- P-084 was verified final and settled immediately above.
- P-077, P-083, P-085 and P-086 did not have a trustworthy final available under the current source-quality gate and remain open/unsettled.
- P-087 India vs Sri Lanka Day 4 had already started by this cutoff and remains live/open.
- No unresolved event was graded from a stale or conflicting feed.

### Identity and current competition context

The Sikkim Football Association lists Howlers Sporting Singtam and Sikkim Boys among the 10 clubs in the 2026 A Division S-League. The Away End's current competition schedule lists this exact fixture for **26 August at 11:00 AM**, with the league's matches at Paljor Stadium.

Howlers' 2026 league record before this match is **1 win, 2 draws, 4 losses**, with **10 goals scored and 16 conceded** from seven listed matches. Sikkim Boys are **0 wins, 1 draw, 6 losses**, with **8 scored and 24 conceded** from seven listed matches. The recent Sikkim Boys sequence is especially weak defensively: **1-6 vs Brotherhood, 2-4 vs Dzongri, 0-6 vs Red Panda**. Howlers' latest three are **0-0 vs Red Panda, 1-2 vs Sikkim Police, 0-5 vs Sikkim Aakraman**.

### Lineup / availability state

**Confirmed starting XIs:** `NOT AVAILABLE` from an authoritative source at cutoff.  
No player injury/selection claim is used directionally without a reliable current release. This lowers side confidence and prevents player-prop recommendations.

### Weather / surface context

IMD's Gangtok forecast for 26 August is generally cloudy with moderate rain and high humidity, and the Sikkim sub-division warning includes heavy-rain risk. This is treated as **variance**, not an automatic Under: a wet surface can reduce clean combination play but also increase errors, set pieces, loose clearances and defensive mistakes.

### Goal-process evidence

Howlers' seven current-league results: **2-3, 3-4, 1-1, 3-1, 0-0, 1-2, 0-5**. Six of seven contained at least three total goals except the 0-0 and 1-1? More precisely, four of seven cleared 2.5, while six of seven had a first-half goal based on the available goal times. Their volatility is driven as much by defensive concessions as by their own attack.

Sikkim Boys' current-league results include **3-4, 0-1, 1-2, 1-1, 1-6, 2-4, 0-6**. Five of seven clearly cleared 2.5 goals, and at least five of the six matches with recoverable goal times contained a first-half goal. Their last three alone produced **7, 6 and 6 total goals**.

The central mechanism is therefore not simply "both teams score freely". It is: **Sikkim Boys' defensive concession rate + Howlers' own defensive instability + a league environment with frequent early goals and multi-goal separation**.

### Corner-process evidence

Direct recent corner records are available but the full causal chain is incomplete.

- Howlers recent recoverable totals: **7 vs Aakraman, 19 vs Sikkim Police, 8 vs Dzongri, 10 vs Brotherhood**.
- Sikkim Boys recent recoverable totals: **8 vs Red Panda, 12 vs Dzongri, 11 vs Brotherhood, 9 vs Gangtok Himalayan**.

Every one of the four listed Sikkim Boys samples reached at least 8 corners; three of four Howlers samples reached at least 8. However, current crosses, blocked crosses, end-line entries and clearance data are not available, and the user's sportsbook/provider definition is unknown. The corner row is therefore capped below `LEAN` under the soccer derivative gate.

### Scenario map

**Central:** Howlers create the better territorial/scoring opportunities against the league's weakest current defence; Sikkim Boys remain dangerous enough in transition to contribute to an open match. Score branches: **2-1, 3-1, 3-2 Howlers**.  
**Lower-goal branch:** rain + poor finishing + conservative first phase yields **1-0, 1-1 or 2-0**.  
**Upper-goal branch:** another Sikkim Boys defensive collapse plus Howlers transition concessions creates **4-1, 4-2 or 3-3**.  
**Side failure branch:** Howlers' own recent attacking drought persists and Sikkim Boys exploit the same defensive instability that has hurt Howlers all season.  
**Corner upper branch:** repeated low-quality attacks, wet-surface clearances and blocked deliveries inflate corners without corresponding goals.

### Ranked picks

| Rank | Candidate ID | Exact contract | Verdict | Evidence | Central mechanism | Strongest kill path | Performance role |
|---:|---|---|---|---|---|---|---|
| **1** | `P088-C03` | **Howlers Sporting Singtam or Draw — 1X** | **SUPPORTED** | **MEDIUM-HIGH** | Howlers have the better current record, home designation and substantially less severe defensive collapse than winless Sikkim Boys | Howlers' recent attacking drought continues and Sikkim Boys score first / exploit transition errors | `PRIMARY_FORMAL` |
| **2** | `P088-C02` | **Total Combined Goals Over 2.5** | **LEAN** | **MEDIUM-HIGH** | Sikkim Boys have conceded 16 in their last three; both teams' season profiles contain repeated 3+ goal states | rain/poor finishing produces 1-0, 1-1 or 2-0 | `PRIMARY_FORMAL` |
| **3** | `P088-C01` | **1st Half Goals Over 0.5** | **LEAN** | **MEDIUM** | available goal-time data shows frequent first-half scoring for both teams, including 6/7 Howlers league matches with a first-half goal | cautious wet opening or wasteful finishing leaves 0-0 HT | `CORRELATED_SECONDARY` |
| **4** | `P088-C04` | **Total Corners Over 7.5** — research threshold | **FORCED RANK** | **MEDIUM-LOW** | recent direct corner samples for both teams cluster at 8+ | quick goal reduces sustained attack/corner demand; direct cross/block/clearance data and exact provider definition are missing | `CORRELATED_SECONDARY` |

### Contract notes

- The user's 1H goal threshold is mapped directionally to **Over 0.5**.
- The user's full-match total threshold is mapped directionally to **Over 2.5**.
- `Over 7.5 corners` is a research-grade analyst-selected threshold. Exact availability at the user's operator was **not verified**, so it is not a value recommendation.
- No prices/operator terms were supplied; all rows are `NO VALUE DETERMINABLE`.

### Potential winner

**Howlers Sporting Singtam — LEAN.**  
Howlers are preferred because they have at least demonstrated a win/draw path in this league and face a Sikkim Boys side that is winless with severe recent defensive leakage. The strongest failure path is Howlers' own current attacking weakness: they have scored only once in their last three, so the favourite can fail if Sikkim Boys survive the opening phase or score first.

### Sources retained for P-088

- Sikkim Football Association competition page: `https://sikkimfootball.in/club-competitions`
- SFA 2026 competition calendar / participating clubs: Sikkim Express, `https://www.sikkimexpress.com/news-details/sfa-unveils-2026-27-competition-calendar-a-division-s-league-to-kick-off-on-july-16`
- Current fixture/results and goal times: The Away End, `https://theawayend.co/sikkim-premier-division-league/`
- Recent match/standings cross-check: Sofascore SFA A Division pages
- Goal/corner event records: TotalCorner team/league pages for Howlers and Sikkim Boys
- Official weather: India Meteorological Department Gangtok city forecast / Sikkim warning pages
- Market source used only for contract existence/context, not sporting analysis: Fonbet current Howlers–Boys Club page

**Logging status:** P-088 appended before delivery.  
**Next canonical ID:** `P-089`.

---

# Prediction Log 2 closeout settlement sweep — 2026-08-26

**Closeout timestamp:** 2026-08-26 17:58 Australia/Melbourne.  
**Method:** MDS-2026.08.24-v2.1.  
**Integrity boundary:** this append settles only verified completed targets. It does not rewrite any issued forecast, rank, cutoff, scenario or confidence. P-087 and P-088 remain live. No numerical probability, EV, staking claim or calibration inference is created retrospectively.

## P-077 settlement — Vincent Weaver vs Aryan Jit Singh, UTR PTT Clemson Men

**Settlement status:** CLOSED / FINAL.  
**Verified result:** Vincent Weaver defeated Aryan Jit Singh **2 sets to 0**.  
**Result evidence:** current tennis result listings record `Vincent Weaver 2-0 Aryan Jit Singh`; the pre-match market had both players priced evenly at 5/6, reinforcing that the issued card itself correctly described this as close rather than a strong favourite situation.

### Contract-by-contract settlement

| Original rank | Candidate | Frozen contract | Outcome | Settlement basis |
|---:|---|---|---|---|
| 1 | `P077-C01` | Aryan Jit Singh — Match Winner | **LOSS** | Weaver won the match 2-0. |
| 2 | `P077-C02` | Aryan Jit Singh — Set 2 Winner | **LOSS** | A 2-0 Weaver match win means Weaver won Set 2. |
| 3 | `P077-C03` | Aryan Jit Singh — Set 1 Winner | **LOSS** | A 2-0 Weaver match win means Weaver won Set 1. |
| 4 | `P077-C04` | Vincent Weaver — Match Winner | **WIN** | Weaver won outright. |

**Potential winner:** Aryan Jit Singh — **LOSS**.  
**Top-two priority result:** **0/2**.  
**Rank-1 loss audit:** **TRIGGERED**.

### Comprehensive rank-1 loss audit

**Why rank #1 was first preissue:** Singh had the broader adult UTR/ITF evidence, had just pushed his Clemson opener to three sets, and the analyst treated adult-match transferability as the narrow edge over Weaver's stronger junior résumé. The card itself correctly noted that the market was essentially even and capped confidence.

**What actually happened:** Weaver won in straight sets. Accessible result sources reliably establish the 2-0 outcome, but a trustworthy point-by-point serve/return data set was not recovered in this audit. Therefore the record does **not** invent first-serve percentage, break-point conversion, winner/error counts or a false tactical explanation.

**Knowable preissue information that was underweighted:** Weaver's 45-19 junior record, #74 TennisRPI, local/home-country setting and fresher workload were all already on the card. Those facts were not hidden surprises. The result is evidence that the uncertainty in translating Weaver's junior level to this adult UTR setting was at least as important as Singh's adult-experience edge.

**Four-pick ordering re-audit:**
- `P077-C04 Weaver ML` had a stronger preissue case than its #4 slot suggests because the market was even and it represented the full opposite match thesis.
- `P077-C02 Singh Set 2` was supported partly by a one-match "adjustment" observation from Singh's previous three-set match. That is thin phase-specific evidence and should not have been treated as stronger than the opposing full-match moneyline without better serve/return evidence.
- `P077-C03 Singh Set 1` was already labelled forced/low-medium and its #3 placement was appropriately cautious, but the first three ranks still concentrated heavily on one Singh thesis.
- A defensible preissue alternative ordering would have moved Weaver ML materially higher and treated both Singh set rows as lower-confidence derivatives. This is a ranking-quality observation, not a hindsight claim that Weaver was "obvious".

**Process grade:** `INCONCLUSIVE` — no identity, settlement, arithmetic or temporal-leakage defect is demonstrated, but the evidence base was too thin to justify concentrating ranks 1-3 on Singh-related outcomes.  
**Defect class:** none proven; evidence-thickness / rank-concentration concern only.  
**Method change:** none from the result alone.  
**Reference observation:** in sparse UTR/junior crossover matches, opposite match-winner evidence should be compared directly with derivative set rows; a single prior-set recovery pattern is not sufficient independent evidence for a high set-winner rank.

**Sources:**
- Result listing: https://www.sportfogadas.org/ajanlatok/tenisz?start=2026-08-25
- Pre-match even market / set markets: https://www.betfair.com/betting/tennis/utr-men-clemson-usa/vincent-weaver-v-aryan-jit-singh/e-35968075
- Pre-match current market cross-check: https://sports.caliente.mx/es_MX/e/32874970/Vincent-Weaver-vs-Aryan-Jit-Singh

---

## P-083 settlement — Cleveland Guardians at Los Angeles Angels, MLB

**Settlement status:** CLOSED / FINAL.  
**Official final:** Cleveland Guardians **8**, Los Angeles Angels **6**, **10 innings**; combined runs **14**; Cleveland margin **+2**.

### Contract-by-contract settlement

| Original rank | Candidate | Frozen contract | Outcome | Settlement arithmetic |
|---:|---|---|---|---|
| 1 | `P083-C01` | Combined Total — Under 8.0 Runs | **LOSS** | 14 total runs; Under 8 loses at 9+. |
| 2 | `P083-C02` | Los Angeles Angels +1.5 | **LOSS** | Angels lost by 2; +1.5 required a win or loss by exactly 1. |
| 3 | `P083-C03` | Cleveland Guardians ML | **WIN** | Cleveland won 8-6. |
| 4 | `P083-C04` | Combined Total — Over 6.0 Runs | **WIN** | 14 total runs; no push. |

**Potential winner:** Cleveland Guardians — **WIN**.  
**Top-two priority result:** **0/2**.  
**Rank-1 loss audit:** **TRIGGERED**.

### Comprehensive rank-1 loss audit

**Preissue expectation:** a 5-7 run central band led by Gavin Williams' strikeout profile, Walbert Ureña's run suppression and a weak Angels order; the card explicitly named Williams home-run contact, Ureña command/walks and bullpen clustering as the Under's strongest ordinary kill paths.

**Actual game driver:** the Under failed immediately through the precise tail that had been identified. MLB reports that Williams recorded only four outs, his shortest start of the season, and allowed **5 runs on 6 hits including two home runs**, plus a walk. Cleveland then erased a 5-0 deficit; José Ramírez delivered both a game-tying double in the eighth and the two-run go-ahead double in the tenth. The extra-inning branch converted a regulation-tied 6-6 game into an 8-6 final.

**Knowability:** the exact 1 1/3-inning collapse was not forecastable as a deterministic event, but Williams' HR/contact tail was explicitly knowable and documented before issue. The process miss is therefore weighting, not missing identity or hindsight information.

**Four-pick ordering re-audit:**
- `Under 8.0` was too dependent on both starters staying near their central run-prevention regimes. It was a reasonable lean, but `MEDIUM-HIGH` evidence understated the ordinary HR/early-hook tail.
- `Angels +1.5` actually matched the regulation close-game thesis: the game was 6-6 after nine. It lost only when Cleveland won by two in the tenth. That makes the contract highly extra-inning/boundary sensitive, not evidence that the close-game read was wholly wrong.
- `Guardians ML` had direct, event-specific preissue support from Williams' matchup profile and Cleveland's form, independent of the Under threshold. There is a reasonable preissue case that it should have ranked above Angels +1.5 rather than below it.
- `Over 6.0` required only seven runs and possessed multiple explicitly named tail routes. It was not properly treated as impossible; its #4 forced-rank position reflected the low-score centre, but the realised game demonstrates the size of the overlap between "low central expectation" and "low alternate Over" in a volatile baseball run distribution.

**Process grade:** `COMPLIANT` — forecast/ranking miss with a known-underweighted kill path; no identity/source/settlement defect.  
**Defect class:** none.  
**Method change:** none from one event.  
**Reference observation:** starter K/ERA form cannot suppress an explicitly live HR/early-exit branch; extra innings can convert a close-game side thesis into a +1.5 loss even when regulation finishes tied.

**Primary source:** https://www.mlb.com/news/jose-ramirez-has-5-rbis-as-guardians-beat-angels  
**Official game story:** https://www.mlb.com/stories/game/823989/

---

## P-085 settlement — Lobos Puebla vs Fuerza Regia, LNBP

**Settlement status:** CLOSED / FINAL.  
**Official-team final:** Fuerza Regia **91**, Lobos Puebla **90**; combined total **181**; Fuerza Regia margin **+1**.  
**Critical integrity finding:** the official Fuerza Regia recap says Fuerza Regia won **Q1 24-20**. That is mathematically incompatible with the issued P-085 live snapshot of **Lobos 25-12 with 2:19 left in Q1**: scores cannot later decrease to a 24-20 quarter final. The issued live-state feed was therefore wrong, mismatched, stale, or otherwise unusable for this event.

### Contract-by-contract settlement

| Original rank | Candidate | Frozen full-game contract | Outcome | Settlement arithmetic |
|---:|---|---|---|---|
| 1 | `P085-C01` | Lobos Puebla +2.5 | **WIN** | Lobos lost by 1; +2.5 covers. |
| 2 | `P085-C03` | Over 171.5 points | **WIN** | 181 total >= 172. |
| 3 | `P085-C04` | Under 171.5 points | **LOSS** | 181 total > 171.5. |
| 4 | `P085-C02` | Fuerza Regia -2.5 | **LOSS** | Fuerza won by only 1; needed 3+. |

**Potential winner:** Lobos Puebla — **LOSS**.  
**Top-two result:** **2/2 WIN**, but this result is **NOT evidence that the live process was valid**.  
**Rank-1 loss audit:** not triggered because rank #1 settled WIN.

### Process-defect audit

**Issued mechanism:** P-085's #1 case was dominated by the claimed 13-point Lobos lead, and the card explicitly stated Fuerza Regia needed a 16-point net swing to cover -2.5. The total analysis likewise used 37 points allegedly already scored late in Q1.

**Official reality:** Fuerza Regia's official recap reports the opposite first-quarter leader and a 24-20 Q1 score. The conditional inputs used to upgrade Lobos and the Over were therefore not a trustworthy representation of the event state.

**Why the final wins do not validate the forecast:** Lobos +2.5 and Over 171.5 happened to win, but they were ranked using a materially false live state. A winning defective process remains defective under the framework.

**Process grade:** `PROCESS_DEFECT`.  
**Defect class:** `LIVE_STATE / SOURCE_TRANSFORMATION / STATE-VERIFICATION`.  
**Immediate process lock:** **ACTIVE** — for niche competitions where an official live match centre is unavailable, a live score used directionally must be corroborated by a second independent current source that matches participant orientation, score and period/clock. If this cannot be done, classify `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`. This is a source-state control, **not** a forecast-weight or probability-model change.

**Method-weight change:** none.  
**Reference observation:** third-party live feeds can be internally plausible yet wrong enough to reverse the conditional game state; source corroboration must precede any live-state upgrade.

**Official team source:** https://www.fuerzaregia.com.mx/  
(News item: “FUERZA REGIA SE IMPONE EN PUEBLA Y REGRESA A MONTERREY CON EL TRIUNFO”)

---

## P-086 closeout — Club León vs Real Salt Lake, Leagues Cup quarterfinal

**Settlement status:** CLOSED / FINAL — **RESEARCH REFERENCE ONLY / PERFORMANCE-INELIGIBLE**, exactly as declared at issue.  
**Official final:** Club León **3**, Real Salt Lake **0**.  
**Halftime:** León 1-0 RSL after Diber Cambindo's 21st-minute goal.  
**Official RSL stats:** León 19-11 shots, 8-5 shots on goal, **8-3 corners** (11 total).

### Research-row outcome audit

| Research rank | Frozen research contract | Outcome | Final basis |
|---:|---|---|---|
| 1 | Combined goals Over 1.5 | **WIN** | 3 goals. |
| 2 | 1st-half goals Over 0.5 | **WIN** | Cambindo scored 21'. |
| 3 | Real Salt Lake or Draw (X2) | **LOSS** | León won 3-0. |
| 4 | Total corners Over 7.5 | **WIN** | 11 total corners. |

**Research potential winner:** Real Salt Lake — **LOSS**.

### Retrospective

The goal and corner research directions were broadly correct: León scored in the first half, the match reached three goals, and the clubs produced 11 corners. The side/winner view was wrong. León created the stronger shot volume (19-11), led from 21 minutes, and added goals from a 66th-minute corner and a 72nd-minute breakaway.

The most important process result is **not** 3/4 research-row accuracy. It is that P-086 correctly refused to manufacture a live forecast after kickoff when no consistent score/clock could be verified. That state-gate decision remains correct and keeps P-086 outside prospective performance metrics.

**Process grade:** `COMPLIANT — STATE GATE SUCCESS / PERFORMANCE-INELIGIBLE`.  
**Method change:** none.

**Official/club sources:**
- https://www.rsl.com/news/real-salt-lake-2026-leagues-cup-run-ends-in-3-0-loss-to-club-leon
- https://www.leaguescup.com/competitions/leagues-cup/2026/matches/leovsrsl-08-25-2026/

---

## P-087 live partial-settlement update — India vs Sri Lanka, 2nd Test, Day 4

**Event status:** **LIVE — DO NOT FULLY SETTLE**.  
**Verified completed subtarget:** Sri Lanka's first innings ended at **290** after resuming Day 4 on 265/8. Sonal Dinusha made **103**. India enforced the follow-on; Reuters' lunch snapshot had Sri Lanka 83/2 in the second innings, still 130 runs behind.

### Completed contract only

| Rank | Candidate | Frozen target | Status |
|---:|---|---|---|
| 1 | `P087-C03` | India Win | **UNRESOLVED — MATCH LIVE** |
| 2 | `P087-C02` | Sri Lanka 1st innings Under 286.5 | **LOSS — COMPLETED TARGET** |

**Settlement arithmetic for C02:** Sri Lanka 290 > 286.5.

**Preissue expectation vs reality for C02:** the issued card said the strongest Under kill path was Dinusha remaining set, farming strike and extending the ninth-wicket stand by another 22+ runs. That precise branch occurred: Sri Lanka added 25 from the overnight 265/8 and crossed the 286.5 boundary before being dismissed.

**No match-level retrospective yet.** Rank #1 is India Win and remains unresolved; therefore the rank-1 loss audit is not triggered.

**High-quality current source:** https://www.reuters.com/sports/cricket/sri-lanka-83-2-after-india-enforce-follow-on-2026-08-26/

---

## P-088 live-state hold — Howlers Sporting Singtam vs Sikkim Boys Football Club

**Event status:** **LIVE — NO SETTLEMENT**.  
**Latest verified specialist state at closeout:** **72' — Howlers SC 3, Sikkim Boys Club 5; corners 2-3**.  
The match is therefore explicitly skipped under the live-event rule. None of P-088's four rows or potential winner is graded yet.

**Current live/stat source:** https://www.totalcorner.com/league/view/8157  
**Competition schedule/reference:** https://theawayend.co/sikkim-premier-division-league/

---

## Closeout disposition

| Status | IDs / notes |
|---|---|
| CLOSED / SETTLED | P-067–P-086, with P-086 performance-ineligible and P-085 carrying a documented process defect |
| LIVE / PARTIALLY SETTLED | P-087 — only Sri Lanka 1st innings Under 286.5 is settled LOSS; India Win remains unresolved |
| LIVE / UNSETTLED | P-088 — 72' state 3-5 at closeout |
| Next canonical forecast | `P-089` |
| New forecast destination | `PREDICTION_LOG_3.md` |

**Prediction Log 2 is now closed for new forecast issuance. New games continue sequentially in Prediction Log 3.**

