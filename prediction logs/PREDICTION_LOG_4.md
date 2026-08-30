# Prediction Log 2

Status: **ACTIVE — NEW GAME LOGS APPEND HERE BY CURRENT USER DIRECTIVE**
Opened: **2026-08-26**
Current method: **MDS-2026.08.26-v2.2 — qualitative champion**
Numerical state: **NTS-2026.08.25-v0.2 — Stage 0 design/pre-fit; no validated numerical model**
Predecessor record: `PREDICTION_LOG_COMBINED.md` — preserved as historical/canonical predecessor evidence.

## Current controlling snapshot

| Field | Current value |
|---|---|
| As of | **2026-08-27 02:42 Australia/Melbourne — comprehensive settlement/research sweep through P-102** |
| Next canonical ID | `P-103` |
| OPEN — live | `P-087` India vs Sri Lanka match-result target; `P-100` Apollon Women vs FH Women; `P-102` Wolfsburg Women vs Inter Women |
| OPEN — pregame/future | `P-101` Germany Women vs Türkiye Women |
| Newly closed in this sweep | `P-088`, `P-089`–`P-099` |
| Niche-stat final disposition | `P-088-C04` corners = `UNSETTLEABLE` after post-final retry; event itself is CLOSED |
| Process-defect flag | `P-095` = `PROCESS_DEFECT — PARTICIPANT/SOURCE IDENTITY` (forecast named the wrong starting pitchers) |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` unless the framework's future validation and same-time market-price gates are satisfied |


## General learnings and integrity controls — 2026-08-27 cleanup

These are **prediction-log observations/process controls**, not retrospective coefficient changes. Forecast weights remain unchanged unless the prospective learning register later promotes a forecast rule.

| Learning ID | Scope | Observation / control | Status in this log | Why |
|---|---|---|---|---|
| `PL2-GL-001` | Baseball / all sports identity | **Final participant identity gate:** a named starting pitcher/goalie/QB/XI role may control the forecast only when verified from the field-owning official source at the final volatile refresh. If official confirmation is unavailable, record `NOT_RELEASED`/`CONFLICTING` and lower evidence rather than naming a secondary-preview participant as confirmed. | **IMMEDIATE PROCESS LOCK — INTEGRITY** | P-095's result was forecast using the wrong starter identities; contract results therefore cannot validate its mechanism. |
| `PL2-GL-002` | Baseball | A low central total does **not** imply a close margin. One dominant starter plus clustered HR/contact/error damage can create 4-0, 8-0 or similar low/moderate-total separation. | Reinforcement of existing baseball margin control | P-089 and P-093 both showed this. |
| `PL2-GL-003` | Baseball | +1.5 handicaps need an explicit **2+ separation tail** driven by starter contact/HR shape, hook point and relief quality; one prior good start is not protection from a blowout. | Candidate / existing tail-stress test reinforced | P-090's 9-1 result came through the exact contact/separation branch. |
| `PL2-GL-004` | Baseball | A short/uncertain starter is an **exposure mixture**, not an automatic Over. Relief performance must be modeled independently. | Reinforcement | P-091: Orix starter exited after 2 IP/5 runs, but Orix relief then threw seven scoreless innings; the 12-run total required multiple mechanisms. |
| `PL2-GL-005` | Cricket | Powerplay/phase pace and completed innings total remain distinct targets. After a fast start, wickets/resources can still collapse the full innings. | Strong reinforcement of existing cricket phase rule | P-094: Yorkshire were 34/0 after five but all out for 171. P-099: Amsterdam reached 56/2 after six but finished 157/8. |
| `PL2-GL-006` | Soccer two-leg ties | Aggregate-state models need an explicit **early trailing-team goal regime switch**. A goal that makes the tie live can rapidly widen the full-match goal distribution. | Candidate / existing score-state control reinforced | P-098's rank-1 Under failed after Thailand scored at 12'. |
| `PL2-GL-007` | Soccer corners | Corner race and corner total must remain separate from goals and from each other; width/cross volume can produce a corner edge without a high total. | Reinforcement | P-098: Thailand won the corner count 4-3 despite only seven total corners. |
| `PL2-GL-008` | Low-information leagues | In local/youth/sparse-data football, unverified XIs plus extreme two-sided defensive volatility should cap side/double-chance confidence unless participant/role evidence is available. | Candidate only — no weight change | P-088 rank #1 1X lost 3-8 after the known early-concession/transition kill path occurred. |
| `PL2-GL-009` | Evaluation | Overlapping alternate lines and opposite-team positive handicaps can produce several winning rows in one event; do not count them as independent confirmation. | Existing dependence control reinforced | P-092 had all four rows win; P-093 had both Over 7.5 and Under 9.5 win. |

## Logging rule

1. Every **new game forecast/log** from this cutover is appended to this file.
2. Continue the canonical `P-###` sequence; **do not restart numbering**.
3. Before a new forecast, reverify and settle any predecessor event that is now final; leave genuinely live events open and continue according to the active rules.
4. Preserve issued forecast views. Settlements, corrections, retrospectives, and administrative snapshot updates are appended rather than used to rewrite historical reasoning.
5. Apply `RULES_GENERAL`, the relevant sport-specific rules, the numerical-training honesty boundary, and the current research/settlement workflow for every entry.

## Current game index — after 2026-08-27 cleanup

| ID | Event | Current disposition | Settlement note |
|---|---|---|---|
| P-087 | India vs Sri Lanka, 2nd Test | **LIVE / PARTIALLY SETTLED** | SL 1st-innings U286.5 already LOSS at 290; match-result target still open. Day 4 ended SL 229/6, lead 16. |
| P-088 | Howlers SC vs Sikkim Boys FC | **CLOSED** | Final 3-8. Rows: L / W / W / UNSETTLEABLE; winner LOSS. |
| P-089 | Hanshin Tigers @ Chunichi Dragons | **CLOSED** | Final Chunichi 4-0. Rows: W / L / W / L; winner LOSS. |
| P-090 | Nippon-Ham Fighters @ Seibu Lions | **CLOSED** | Final Nippon-Ham 9-1. Rows: L / L / W / W; winner LOSS. |
| P-091 | Rakuten Eagles @ Orix Buffaloes | **CLOSED** | Final Orix 7-5. Rows: W / L / W / L; winner WIN. |
| P-092 | Doosan Bears @ KT Wiz | **CLOSED** | Final KT 5-4. **All four supplied rows won** because of overlap geometry; winner WIN. |
| P-093 | NC Dinos @ LG Twins | **CLOSED** | Final LG 8-0. Rows: W / L / W / W; winner WIN. |
| P-094 | Yorkshire Women vs Surrey Women | **CLOSED** | Yorkshire 171; Surrey 172/8. Rows: W / L / W / L; winner WIN. |
| P-095 | TSG Hawks @ Fubon Guardians | **CLOSED — PROCESS DEFECT** | Final Fubon 5-4. Rows: W / L / W / L; winner LOSS. Wrong starting-pitcher identities in issued mechanism. |
| P-096 | Rakuten Monkeys @ CTBC Brothers | **CLOSED** | Final CTBC 2-0. Rows: L / W / L / W; winner LOSS. |
| P-097 | Wei-Chuan Dragons @ Uni-Lions | **CLOSED** | Final Uni 1-0. Rows: W / W / L / L; winner WIN. |
| P-098 | Vietnam vs Thailand | **CLOSED** | Final 2-2; Vietnam advance 4-2 agg. Rows: L / W / W / W; match-winner lean LOSS. |
| P-099 | Rotterdam Dockers vs Amsterdam Flames | **CLOSED** | Amsterdam 157/8 (PP 56/2); Rotterdam 158/5. Rows: W / L / W / L; winner WIN. |
| P-100 | Apollon Women vs FH Women | **LIVE — DO NOT SETTLE** | Latest verified retrievable state: FH lead 2-0 at 69:21. |
| P-101 | Germany Women vs Türkiye Women | **PREGAME / FUTURE** | Scheduled 27 Aug 17:00 CEST / 28 Aug 01:00 Melbourne. |
| P-102 | Wolfsburg Women vs Inter Women | **LIVE — DO NOT SETTLE** | Latest verified retrievable state: 0-0 at 29:49. |


---

## Next entry

The next new game is **P-093**. P-087 remains live on its match-result target and P-088 remains unresolved because a trustworthy full-time state has not been recovered.

---

## Queue re-verification before P-089 — 2026-08-26 18:51 Australia/Melbourne

The carried predecessor queue was rechecked before issuing the new event.

| ID | Event | Current state at recheck | Action |
|---|---|---|---|
| P-087 | India vs Sri Lanka, 2nd Test | **LIVE** — Reuters reported Sri Lanka 83/2 in the follow-on, still 130 runs behind; the previously completed Sri Lanka first-innings Under 286.5 remains a settled LOSS at 290, but the match-result target remains unresolved | Leave open; no premature match-result settlement |
| P-088 | Howlers Sporting Singtam vs Sikkim Boys Club | **CURRENT FULL-TIME STATE NOT TRUSTWORTHILY VERIFIED** — current web sources conflicted/staled: TotalCorner reverted to a 0-0 listing while a separate live feed still showed Howlers 3-5 Sikkim Boys around 68'; no reliable final was recovered | Leave open; do not guess settlement |

**Queue conclusion:** neither carried item can be fully closed honestly at this cutoff. Proceed to P-089 under the live/unverified-state rule.

Sources checked: Reuters, 2026-08-26, `https://www.reuters.com/sports/cricket/sri-lanka-83-2-after-india-enforce-follow-on-2026-08-26/`; TotalCorner team/league current pages; secondary live-state cross-check.

---

## P-089 — Hanshin Tigers @ Chunichi Dragons — PREGAME

**Recorded / evidence cutoff:** 2026-08-26 18:51:55 Australia/Melbourne / 17:51:55 JST  
**Scheduled start:** 2026-08-26 18:00 JST / 19:00 Australia/Melbourne  
**Sport / competition:** Nippon Professional Baseball (NPB), JERA Central League regular season  
**Official event:** Chunichi Dragons vs Hanshin Tigers, 21st meeting of 2026  
**Venue:** Vantelin Dome, Nagoya  
**GAME-STATE:** **PREGAME** — NPB official match page still displayed `試合開始前` (before start) at the final refresh.  
**Method:** MDS-2026.08.26-v2.2 qualitative champion  
**Numerical state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE` — no usable same-time prices were supplied; this is a likelihood/robustness ranking, not an EV or staking recommendation.

### Frozen supplied contract slate

Standard full-game official-result treatment is assumed because no operator rules were supplied. NPB can record draws; operator-specific handling remains an explicit unknown.

| Candidate | Supplied contract | Research settlement geometry |
|---|---|---|
| P089-C01 | Dragons +1.5 | WIN if Chunichi wins/draws or loses by exactly 1; LOSS if Hanshin wins by 2+ |
| P089-C02 | Tigers +0.5 | Under standard full-game handicap treatment: WIN if Hanshin wins or official result is tied; LOSS if Chunichi wins |
| P089-C03 | Combined Over 6.0 runs | WIN at 7+; PUSH at exactly 6; LOSS at 0-5 |
| P089-C04 | Combined Under 8.0 runs | WIN at 0-7; PUSH at exactly 8; LOSS at 9+ |

**Dependence geometry:** C03 and C04 overlap — both win at exactly 7 runs; C03 pushes/C04 wins at 6; C03 wins/C04 pushes at 8. C01 and C02 also overlap — both can win if Hanshin wins by exactly one, and under the standard official-result assumption both can win on a draw. These are four contract queries on one event, not four independent opportunities.

### Official participants and current state

NPB's final pregame page confirmed:

- **Hanshin battery:** Masashi Ito (LHP) / Seishiro Sakamoto.
- **Chunichi battery:** Hideaki Wakui (RHP) / Yudai Ishii.
- **Hanshin order:** Koji Chikamoto, Takumu Nakano, Shota Morishita, Teruaki Sato, Yusuke Oyama, Yuta Maegawa, Seishiro Sakamoto, Hiyu Motoyama, Masashi Ito.
- **Chunichi order:** Hiroki Fukunaga, Seiji Uebayashi, Seiya Hosokawa, Miguel Sanó, Takaya Ishikawa, Hanada, Yudai Ishii, Ryuku Tsuchida, Hideaki Wakui.
- **Venue/weather:** indoor dome environment, so outdoor weather is not a decision driver. However, Vantelin's 2026 home-run wing changes the long-ball environment relative to older park history and is retained as an upper-tail factor rather than assuming the historical park suppresses all power.

Primary current source: NPB official live page, `https://npb.jp/scores/2026/0826/d-t-21/`.

### Starter process

**Masashi Ito, Hanshin** — NPB season line through 25 August: 7 appearances, 35.2 IP, 32 H, 2 HR, 10 BB, 30 K, 10 ER, **2.52 ERA**. On 19 August versus Yakult he threw **6.0 scoreless innings, 4 H, 2 BB, 7 K**. On 9 August against this Chunichi lineup family he worked **5.0 scoreless innings**; Chunichi collected six hits against him but did not score, and Hanshin ultimately won 1-0. Ito has explicitly identified the new Vantelin home-run wing as the main risk and said he wants to keep the ball down.

**Hideaki Wakui, Chunichi** — NPB season line through 25 August: 8 appearances, 45.2 IP, 51 H, 7 HR, only 3 BB, 32 K, 16 ER, **3.15 ERA**. His command profile is strong, but the seven home runs in 45.2 innings create a real damage-cluster tail against Hanshin's power-heavy middle order. His latest official start, 12 August against DeNA at Vantelin, was **5.0 IP, 6 H, 0 BB, 2 K, 3 ER**, with two solo home runs allowed.

**Starter conclusion:** Ito has the better current run-prevention case and the more relevant recent opponent-specific result. Wakui's elite walk suppression keeps his floor respectable, but his home-run exposure is the clearest route to Hanshin separating by multiple runs or pushing the total upward.

### Team and matchup baseline

- Through 25 August, NPB lists Hanshin at **63-48-1 (.568), first in the Central League**, and Chunichi at **50-65-1 (.435)**. Hanshin therefore owns the much stronger season-level team baseline.
- Team batting totals through 25 August: **Hanshin 419 runs in 112 games**; **Chunichi 390 in 116**. That produces a raw combined scoring environment around seven runs before current-starter, venue and matchup adjustments.
- Hanshin's lineup contains two of the league's most dangerous qualified hitters: through 25 August, Teruaki Sato was batting **.320 with 30 HR**, and Shota Morishita **.297 with 31 HR**. That is the main reason the upper Under is not treated as a certainty against Wakui.
- Chunichi entered this game on **four straight wins**, including yesterday's 4-2 victory over Hanshin. Recent momentum is therefore a genuine counterweight to the season table.
- The August 7-9 Hanshin-Chunichi series ended 3-2 Chunichi, 7-1 Chunichi, and 1-0 Hanshin; yesterday was 4-2 Chunichi. Those four recent meetings all finished at **8 runs or fewer**, but they are treated as matchup diagnostics rather than a deterministic H2H rule.
- Hanshin's last 10 completed games before today produced combined totals of 5, 7, 7, 9, 5, 3, 5, 5, 8 and 6. Eight finished below 8, one landed exactly 8 and one exceeded it. This supports a compressed central corridor, but the statistic is diagnostic only and is not converted to a probability.
- Chunichi's last four home games at Vantelin before today were 3-0, 5-4, 3-2 and 4-2. Three were clearly low-scoring and one reached nine; that 5-4 game is retained as a direct warning against treating the dome as an automatic Under.

### Bullpen / late-game availability

There was no obvious severe bullpen exhaustion regime entering today because 24 August was an off day. Yesterday Chunichi received seven innings from Ohno and used Yoshida and closer Matsuyama for one inning each; Hanshin used Jingu, Severino and Tsuda for one inning each after Yuki Nishi. Hanshin's Iwazaki/Doris high-leverage options were not used in yesterday's final, while Chunichi did use Matsuyama. This is a small late-game lean toward Hanshin rather than a controlling factor. Hanshin also had Yuasa deregistered on 24 August, so the relief advantage is not treated as one-sided certainty.

### Qualitative joint-run corridor

The research-only central branch is a **roughly 5-7 run game**, with the modal side shape leaning **Hanshin by about one run** rather than a wide separation. This is not a fitted mean or calibrated probability.

- **Lower branch (2-4 runs):** Ito suppresses Chunichi again; Wakui limits free passes and keeps Hanshin's power in the park; both teams lean on fresh relief.
- **Central branch (5-7):** each starter allows modest traffic, Hanshin's stronger middle order creates slightly more damage, and the game remains within one run or a narrow two-run window.
- **Upper branch (8-10+):** Wakui's home-run tail is hit by Sato/Morishita/Oyama, or Chunichi's right-handed power takes advantage of the shortened Vantelin dimensions against Ito; bullpen leverage then expands the scoring tail.

### Required unique contract ranking

| Rank | Candidate | Contract | Verdict | Evidence quality | Performance role | Central reason | Strongest ordinary kill path |
|---:|---|---|---|---|---|---|---|
| **1** | P089-C04 | **Combined Under 8.0** | **SUPPORTED** | MEDIUM-HIGH | PRIMARY_FORMAL | 8.0 is a high upper boundary relative to the 5-7 central corridor; Ito's current run prevention, Wakui's command, recent Hanshin totals and recent matchup scores all point toward 0-7 more often than the 9+ tail | Hanshin's elite middle-order power reaches Wakui's 7-HR-in-45.2-IP tail and Chunichi contributes enough against the new Vantelin dimensions to create 5-4, 6-3 or worse |
| **2** | P089-C02 | **Tigers +0.5** | **LEAN** | MEDIUM | PRIMARY_FORMAL | Hanshin own the stronger season baseline, better current starter case, and stronger top-of-order power; +0.5 also protects an official tie under the stated standard assumption | Chunichi's four-game winning run continues at home; Hosokawa/Sanó/Uebayashi generate the key extra-base hit and Wakui avoids the damaging homer, producing another 3-2 or 4-2 Chunichi result |
| **3** | P089-C01 | **Dragons +1.5** | **LEAN** | MEDIUM | CORRELATED_SECONDARY | The low-run corridor gives +1.5 meaningful cushion, and a one-run Hanshin win allows C01 and C02 to win together; recent H2H has repeatedly stayed inside this margin structure | Hanshin's starter and lineup edge expresses as separation rather than merely a win — e.g. 4-2, 5-2 or 5-1 — with Wakui's home-run tail driving the margin past +1.5 |
| **4** | P089-C03 | **Combined Over 6.0** | **FORCED RANK** | MEDIUM-LOW | CORRELATED_SECONDARY | The Over has a live path because 7 runs wins and overlaps with the Under-8 thesis, but it needs the upper part of the central corridor; exactly 6 only pushes | Ito repeats his recent suppression of Chunichi and Wakui's command limits extended innings, producing 3-2, 4-1 or another 4-2-type game |

**Near-tie note:** ranks #2 and #3 are close. The ordering is not a hedge/diversification choice: C02 is placed narrowly higher because the season-strength + starter + lineup edge points to Hanshin avoiding defeat slightly more strongly than the margin-cushion case points to Chunichi avoiding a 2+ loss. A 3-2 Hanshin result is the important overlap path where both win.

### Potential game winner

**Hanshin Tigers — `LEAN`, not `SUPPORTED`.**

The winner case is independent of the handicap ranking: Hanshin are the stronger season team, Ito has the better current starter profile and already threw five scoreless innings against Chunichi on 9 August, and Hanshin's 3-5 hitters have materially more established power production. The reason this stays only a `LEAN` is equally concrete: Chunichi are at home, have won four straight, beat Hanshin 4-2 yesterday, and have won three of the last four recent meetings listed above. This is a real contest, not a high-confidence moneyline spot.

### Final controls / honesty boundary

- No prices were supplied, so **no value/edge/ROI/staking claim** is made.
- No numerical model is fit or validated for NPB under the active NTS Stage-0 program; **no win probabilities are published or back-filled**.
- The four rows are dependent contract queries, not independent betting opportunities.
- The exact sportsbook's NPB extra-inning/draw/action rules were not supplied. Research geometry uses standard full official-result assumptions; actual book settlement must be checked against that operator.
- Old Vantelin park reputation is not treated as immutable because the 2026 home-run wing changed the dimensions.
- The final NPB pregame refresh still showed **game not started** and confirmed the lineups/batteries before this card was appended.

### Primary web evidence retained

- NPB official current game page / lineup: `https://npb.jp/scores/2026/0826/d-t-21/`
- NPB Central League standings: `https://npb.jp/cl/?id=top`
- NPB 2026 team batting: `https://npb.jp/bis/2026/stats/tmb_c.html`
- NPB Masashi Ito season record: `https://npb.jp/bis/players/71375153.html`
- NPB Hideaki Wakui season record: `https://npb.jp/bis/players/31635110.html`
- NPB 2026-08-19 Hanshin-Yakult box score (Ito 6 scoreless): `https://npb.jp/bis/eng/2026/games/s2026081901373.html`
- NPB 2026-08-12 Chunichi-DeNA box score (Wakui latest start): `https://npb.jp/bis/eng/2026/games/s2026081201356.html`
- NPB 2026-08-09 Hanshin-Chunichi box score (Ito 5 scoreless): `https://npb.jp/bis/eng/2026/games/s2026080901350.html`
- NPB 2026-08-25 Chunichi-Hanshin box score: `https://npb.jp/bis/eng/2026/games/s2026082501388.html`
- Hanshin official August schedule/results: `https://www.hanshintigers.jp/game/schedule/2026/08.html`
- Chunichi official August schedule/results: `https://dragons.jp/game/schedule/?month=202608`
- Nikkan Sports Ito/Vantelin report, 2026-08-25: `https://www.nikkansports.com/baseball/news/202608250000776.html`

**Result:** `OPEN — PREGAME` at issue.  
**Next canonical ID after this append:** `P-090`.


---

## Queue re-verification before P-090 — 2026-08-26 18:58 Australia/Melbourne

| ID | Event | State at recheck | Action |
|---|---|---|---|
| P-087 | India vs Sri Lanka, 2nd Test | **LIVE / match-result unresolved** — current Day-4 reporting still had Sri Lanka batting in the follow-on; no final existed at this gate | Leave open; do not settle match-result target |
| P-088 | Howlers Sporting Singtam vs Sikkim Boys Club | **FULL-TIME STATE STILL NOT TRUSTWORTHILY VERIFIED** — exact-match search did not recover an authoritative final | Leave unresolved; do not guess |
| P-089 | Hanshin Tigers @ Chunichi Dragons | NPB page still showed **pre-start** during the same final-refresh window | Leave open |

**Queue conclusion:** no predecessor item could be honestly closed before P-090. Proceed under the active live/unverified-state rule.

---

## P-090 — Hokkaido Nippon-Ham Fighters @ Saitama Seibu Lions — PREGAME

**Recorded / final evidence cutoff:** 2026-08-26 18:58:26 Australia/Melbourne / 17:58:26 JST  
**Scheduled start:** 2026-08-26 18:00 JST / 19:00 Australia/Melbourne  
**Competition:** NPB Pacific League regular season, 22nd meeting  
**Venue:** Belluna Dome  
**Official state at final refresh:** `試合開始前` / **PREGAME**, NPB official page.  
**Method:** MDS-2026.08.26-v2.2 qualitative champion.  
**Numerical state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`; NTS Stage 0 remains pre-fit.  
**Prices:** none supplied; `NO VALUE DETERMINABLE`.

### Frozen supplied candidate slate

| Candidate | User-supplied contract | Research settlement geometry under standard full-official-game assumption | Eligibility |
|---|---|---|---|
| P090-C01 | **Seibu Lions +1.5** | WIN if Seibu wins/ties or loses by exactly 1; LOSS if Nippon-Ham wins by 2+ | ELIGIBLE |
| P090-C02 | **Nippon-Ham Fighters +0.5** | WIN if Nippon-Ham wins or official result is tied; LOSS if Seibu wins | ELIGIBLE |
| P090-C03 | **Combined Over 5.5** | WIN at 6+ total runs; LOSS at 0-5 | ELIGIBLE |
| P090-C04 | **Combined Under 7.5** | WIN at 0-7 total runs; LOSS at 8+ | ELIGIBLE |

**Operator caveat:** operator/action, extra-inning and tie settlement terms were not supplied. The research intervals above use the standard full official result as the target. Actual sportsbook grading must follow the named operator if later provided.

### Contract dependence / interval map

- C01 and C02 are **not complements**. If Nippon-Ham wins by exactly one, **both win**; if Seibu wins, C01 wins and C02 loses; if Nippon-Ham wins by 2+, C02 wins and C01 loses.
- C03 and C04 are **overlapping alternates**, not opposites. At **6 or 7 total runs, both win**. At 0-5 only C04 wins; at 8+ only C03 wins.
- The four rows therefore represent dependent queries on one game/margin/total process, not four independent opportunities.

### Event identity, starters and confirmed lineups

NPB's final pre-start page confirmed **Kota Tatsu — Yuya Gunji** as the Nippon-Ham battery and **Yutaro Watanabe — Taiga Kojima** as Seibu's battery.

**Nippon-Ham lineup:** Mizutani RF; Kiyomiya 1B; Reyes DH; Nomura CF; Arizono 3B; Otsuka SS; Gunji C; Yoshida LF; Hosokawa 2B; Tatsu P.  
**Seibu lineup:** Canario RF; Kojima C; Nevin DH; Lin An-Ko LF; Hirasawa 3B; Hiruma CF; Kishi 1B; Genda SS; Nakata 2B; Watanabe P.

Notable lineup context: Nippon-Ham's season offense is stronger in aggregate, but **Chusei Mannami and Minami Mizuno are not in the starting nine**. Seibu likewise use a reshuffled lower half, with regular contributors including Seiya Watabe and Aito/Nishikawa available off the bench rather than all starting. This is treated as an exposure change, not as an automatic Under.

### Starting-pitcher process

**Yutaro Watanabe, Seibu:** through 25 August, 18 appearances / **117.1 IP, 3.14 ERA, 97 H, 8 HR, 35 BB, 88 K**. His current matchup evidence is useful rather than merely reputational: the Pacific League preview listed him at **2-1 with a 2.89 ERA in four 2026 appearances against Nippon-Ham**, and on 12 August he held the Fighters to **2 runs over 7 innings**. His most recent start on 19 August was **5 scoreless innings** against Orix. The ordinary failure branch is clear: Nippon-Ham lead the Pacific League power comparison here and Kiyomiya/Reyes can turn Watanabe's otherwise solid contact suppression into a multi-HR inning.

**Kota Tatsu, Nippon-Ham:** through 25 August, 22 appearances / **89.2 IP, 3.11 ERA, 72 H, 8 HR, 21 BB, 88 K**. His last actual start on 14 August was **7 IP, 2 R, 8 K, 0 BB/HBP**, following another **7 IP, 2 R** outing on 7 August. His planned 22 August start was rained out, and he was moved into this 26 August slot after Takayuki Kato became unavailable through illness. That creates an unusual rest/schedule branch: the extra competitive rest may help freshness, but the altered preparation means workload/command cannot simply be assumed identical to a normal rotation turn.

### Team-level baseline and bullpen state

Through 25 August, NPB official team batting had Nippon-Ham at **478 runs / 117 games, .251/.314/.414 with 142 HR**, versus Seibu at **418 runs / 117 games, .246/.305/.364 with 85 HR**. That is a meaningful Nippon-Ham offensive advantage, especially in home-run ceiling.

The counterweight is pitching: NPB official team pitching had **Seibu 2.84 ERA** versus **Nippon-Ham 3.31 ERA** through 25 August. Seibu also carried the better current W-L record in that table (**66-48 vs 63-53**) and the Pacific League preview had Seibu leading this season series **12-9** entering the game.

Yesterday's same-venue game was **Seibu 3, Nippon-Ham 1**. Seibu used Taira as starter and Wingenter/Kaino late; Nippon-Ham used Ito, Miyanishi and Rao. For today's final bench, Seibu still list Kaino plus Matsumoto, Sato Hayate, Moriwaki, Shinohara, Kuroki, Mameta and Sato So; Nippon-Ham list Uehara, Kanemura, Rao, Hori, Fukushima, Yanagawa, Kiyomiya Tora and Sun. Bullpen availability therefore does not force a one-sided total call; it mainly reinforces Seibu's season-long run-prevention advantage while preserving late-inning variance.

### Qualitative target corridor

The active framework does **not** authorise a fitted NPB probability or numeric score forecast. The qualitative central branch is a **close game with roughly 5-7 combined runs**, built from:

1. two starters carrying ERAs near 3.1 with current quality-start evidence;
2. Watanabe's specific success against this opponent;
3. Seibu's league-leading/near-leading team run prevention;
4. Nippon-Ham's materially stronger season offense and home-run ceiling, preventing an aggressive low-total call;
5. the confirmed batting orders, which remove some Nippon-Ham season-level depth/power from the starting nine.

The strongest upper-tail branch is Nippon-Ham's power getting to Watanabe early, forcing Seibu into middle relief while Tatsu's altered rest/preparation produces a short start. The strongest lower-tail branch is both starters working six-plus efficient innings and Seibu's bullpen closing a 3-1/3-2 type game.

### Required unique ranking

| Rank | Candidate | Pick | Verdict | Evidence quality | Performance role | Central mechanism | Strongest ordinary kill path |
|---:|---|---|---|---|---|---|---|
| **1** | P090-C01 | **Seibu Lions +1.5** | **SUPPORTED** | MEDIUM-HIGH | PRIMARY_FORMAL | Seibu own the stronger current record, much better team ERA, home field, 12-9 season-series edge and a starter with 2.89 ERA vs Nippon-Ham; +1.5 survives every Seibu win/tie and a one-run Fighters win | Nippon-Ham's superior power shows up cleanly and Tatsu matches Watanabe, creating a 4-2/5-2 Fighters win that clears the cushion |
| **2** | P090-C04 | **Combined Under 7.5** | **LEAN** | MEDIUM-HIGH | PRIMARY_FORMAL | Both starters are around 3.1 ERA with strong current starts, Watanabe has matchup-specific suppression, Seibu's team ERA is 2.84, and the confirmed lineups reduce some offensive exposure | Fighters' 142-HR season power produces early damage or Tatsu's irregular turn ends early, opening a 5-3/6-3 bullpen branch |
| **3** | P090-C03 | **Combined Over 5.5** | **LEAN** | MEDIUM | CORRELATED_SECONDARY | A six- or seven-run game sits inside the same central corridor and lets C03 and C04 both win; Nippon-Ham's season offense is strong enough that 6+ remains very live | Both starters repeat their recent suppression and Seibu controls late innings, producing 3-1, 3-2 or 2-1 |
| **4** | P090-C02 | **Nippon-Ham Fighters +0.5** | **FORCED RANK** | MEDIUM | CORRELATED_SECONDARY | Fighters have the stronger season offense and Tatsu is capable of matching Watanabe, so this remains a genuine live branch | Seibu's stronger pitching/record/home/H2H profile converts to any outright Seibu win, which is enough to lose +0.5 |

### Ranking checks

**Top-slot check:** C01 has event-specific support beyond generic form: Watanabe's current opponent record, confirmed lineup, Seibu's 2.84 team ERA and home/season-series position all align with a cushion that also survives a one-run Nippon-Ham win. It is therefore the only row upgraded to `SUPPORTED`.

**#2 vs #3 total check:** Under 7.5 is higher because the lower-tail starter/Seibu-bullpen mechanism is stronger than the 8+ scoring tail. Over 5.5 remains close because the two totals overlap at 6-7; it is not treated as a fade.

**Bottom-slot swap test:** best case for Fighters +0.5 is real: Nippon-Ham have 478 runs and 142 HR to Seibu's 418/85, and Tatsu has two straight seven-inning two-run starts. That prevents `AVOID`. It stays fourth because the exact condition it needs — Seibu not winning — conflicts with the stronger home/pitching/current-record evidence supporting C01 and the winner lean.

### Potential game winner

**Saitama Seibu Lions — `LEAN`.**

The winner case is narrower than the +1.5 case and is therefore not upgraded to `SUPPORTED`. Seibu enter with the better record and team ERA, lead the 2026 season series, won yesterday 3-1, and have the more matchup-proven starter in Watanabe. Against that, Nippon-Ham possess the stronger offense by a large margin and Tatsu's recent form is good enough to make this a genuinely close game. The likely-winner call is therefore **Seibu, but only as a lean**.

### Honesty / publication boundary

- No prices supplied: **NO VALUE DETERMINABLE**; no EV/ROI/staking claim.
- NTS-2026.08.25-v0.2 remains Stage 0/pre-fit: **no calibrated probabilities are generated or published**.
- One target corridor controls the total lines; no independent line-by-line pseudo-probabilities are invented.
- Operator-specific NPB tie/extra-inning/action rules remain unknown and must control actual settlement if supplied later.
- Final official NPB refresh at the recorded cutoff still showed **game not started**.

### Primary evidence retained

- NPB official live/event page and confirmed lineups: `https://npb.jp/scores/2026/0826/l-f-22/index.html`
- NPB Yutaro Watanabe 2026 stats: `https://npb.jp/bis/players/53155138.html`
- NPB Kota Tatsu 2026 stats: `https://npb.jp/bis/players/01205155.html`
- NPB Pacific League team batting: `https://npb.jp/bis/2026/stats/tmb_p.html`
- NPB Pacific League team pitching: `https://npb.jp/bis/2026/stats/tmp_p.html`
- Pacific League official game preview/current roster page: `https://pacificleague.com/game/36345`
- NPB 25 August Seibu-Fighters official play-by-play/final: `https://npb.jp/scores/2026/0825/l-f-21/playbyplay.html`

**Result:** `OPEN — PREGAME` at issue.  
**Next canonical ID after this append:** `P-091`.


---

## Queue re-verification before P-091 — 2026-08-26 19:02 Australia/Melbourne

| ID | Event | Current state at recheck | Action |
|---|---|---|---|
| P-087 | India vs Sri Lanka, 2nd Test | **LIVE** — current reporting still showed Sri Lanka batting in the follow-on on Day 4; match-result target unresolved | Leave open; no premature settlement |
| P-088 | Howlers Sporting Singtam vs Sikkim Boys Club | **CURRENT FULL-TIME STATE NOT TRUSTWORTHILY VERIFIED** — targeted current searches still did not produce a reliable official/full-time result | Leave open; do not guess settlement |
| P-089 | Hanshin Tigers @ Chunichi Dragons | **PREGAME** — NPB official page still displayed `試合開始前` after 18:00 JST | Leave open |
| P-090 | Nippon-Ham Fighters @ Seibu Lions | **PREGAME** — NPB official page still displayed `試合開始前` after 18:00 JST | Leave open |

**Queue conclusion:** no earlier item was honestly settleable at this gate. Proceed to P-091.

---

## P-091 — Tohoku Rakuten Golden Eagles @ Orix Buffaloes — PREGAME

**Recorded / evidence cutoff:** 2026-08-26 19:02:31 Australia/Melbourne / 18:02:31 JST  
**Scheduled start:** 2026-08-26 18:00 JST / 19:00 Australia/Melbourne  
**Sport / competition:** Nippon Professional Baseball (NPB), Pacific League regular season  
**Official event:** Orix Buffaloes vs Tohoku Rakuten Golden Eagles, 20th meeting of 2026  
**Venue:** Kyocera Dome Osaka  
**GAME-STATE:** **PREGAME** — NPB's official match page still displayed `試合開始前` at the final refresh, despite the scheduled start time having just passed.  
**Method:** MDS-2026.08.26-v2.2 qualitative champion  
**Numerical state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE` — no same-time prices supplied; likelihood/robustness ranking only.

### Frozen supplied contract slate

Operator/action rules were not supplied. Research settlement geometry uses the standard full official NPB game result, including the possibility of an official tie; actual sportsbook grading must follow the named operator if later provided.

| Candidate | User-supplied contract | Research settlement geometry | Eligibility |
|---|---|---|---|
| P091-C01 | **Rakuten Eagles +0.5** | WIN if Rakuten wins or the official result is tied; LOSS if Orix wins | ELIGIBLE |
| P091-C02 | **Orix Buffaloes +1.5** | WIN if Orix wins/ties or loses by exactly 1; LOSS if Rakuten wins by 2+ | ELIGIBLE |
| P091-C03 | **Combined Over 6.5 runs** | WIN at 7+ total runs; LOSS at 0-6 | ELIGIBLE |
| P091-C04 | **Combined Under 8.5 runs** | WIN at 0-8 total runs; LOSS at 9+ | ELIGIBLE |

**Dependence geometry:** C01 and C02 are not complements; both win on an official tie and both also win if Rakuten wins by exactly one. C03 and C04 overlap: **both win at 7 or 8 total runs**. These are four contract queries on one joint game process, not four independent opportunities.

### Official participants and confirmed starting lineups

NPB's official pre-start page confirmed the following batteries and batting orders.

**Rakuten battery:** Kosei Shoji (RHP) / Hikaru Ohta.  
**Rakuten order:** Daisuke Nakashima LF; Ryosuke Tatsumi CF; Rui Muneyama SS; Luke McCusker DH; Hiroto Murabayashi 3B; YG Yasuda 1B; Yosuke Yoshino RF; Hikaru Ohta C; Yo Yang 2B.

**Orix battery:** Kyosuke Saito (RHP) / Kenya Wakatsuki.  
**Orix order:** Yuma Mune 3B; Ryoma Nishikawa DH; Ryoto Kita RF; Ryo Ohta 1B; Kotaro Kurebayashi SS; Tomoya Noguchi 2B; Ryoma Yamanaka LF; Kenya Wakatsuki C; Shun Mugitani CF.

Kyocera Dome removes outdoor weather from the decision chain.

Primary current source: NPB official live page, `https://npb.jp/scores/2026/0826/b-e-20/box.html`.

### Starter process

**Kosei Shoji, Rakuten:** through 25 August, NPB lists **19 appearances, 117.0 IP, 109 H, 19 HR, 31 BB, 121 K, 53 ER, 4.08 ERA**. The strikeout/walk shape is respectable, but the **19 home runs** are an important upper-tail variable. He has seen Orix repeatedly this month: on 3 August at Tokyo Dome he allowed **4 ER in 6 innings**; on 11 August at Rakuten Mobile he gave Orix only **2 ER over 7 innings** before the Rakuten bullpen allowed seven late runs. That leaves a credible central six-to-seven-inning branch, but no basis for calling him a dominant suppressor against this lineup.

**Kyosuke Saito, Orix:** his top-level 2026 line is a misleadingly tiny sample: one July 22 relief appearance, **0.1 IP, 8 H, 7 ER**, producing a nominal 189.00 ERA. That outing is retained as a volatility warning but is not treated as his talent level. His relevant current body of work is in the Western farm league: **14 appearances, 64.1 IP, 56 H, 6 HR, 19 BB, 47 K, 23 ER, 3.22 ERA, 5-2**. Most importantly, on **18 August** he started against SoftBank's farm side and threw **7.0 IP, 4 H, 0 BB, 8 K, 2 ER**, his final tune-up before this first-team start. Orix reporting also noted that he had been working on fastball quality after the July blow-up.

**Starter conclusion:** Shoji supplies a stable but homer-prone major-league baseline; Saito supplies materially more uncertainty but also genuine evidence of a successful farm reset. This is a wider distribution than a normal two-established-starter game — especially on the upper total tail — but Saito's July outlier does not justify automatically making the Over the top pick.

### Team-level baseline

Through 23 August, official NPB team batting showed:

- **Orix:** 403 runs in 114 games, .245 AVG, .306 OBP, .360 SLG, 79 HR.
- **Rakuten:** 359 runs in 111 games, .240 AVG, .305 OBP, .355 SLG, 82 HR.

That is approximately **3.54 Orix runs/game vs 3.23 Rakuten**, before today's starter/lineup adjustments. Orix therefore owns the somewhat stronger season offense, but not by a massive gap.

Official standings through 23 August had **Orix 55-57-2 (.491)** and **Rakuten 43-67-1 (.391)**, a substantial season-level team-strength edge to Orix. Official Pacific League pitching data had **Orix 3.81 team ERA** and **Rakuten 3.76**, so the overall team edge is not a simple pitching superiority story; Orix's better record has come with the better offense/overall run balance rather than an elite staff.

### Current matchup evidence and yesterday's game

Rakuten won yesterday's same-venue opener **5-1**. Orix starter Kuri was charged with 4 ER over 5.1 innings; Rakuten starter Tatsuki Ito allowed 1 ER over 5 innings. Rakuten used Suzuki, Kutani, Kajiya and Nishiguchi for one inning each. Orix used Tomiyama, Higashiyama, Yamaoka and Iwasaki behind Kuri. Both clubs therefore used four relievers, but neither burned every premium option: **Orix closer Andres Machado was not used**, and Rakuten closer **Shoma Fujihira was not used**. Bullpen availability does not create a forced Over.

Recent 2026 Orix–Rakuten finals show genuine scoring variance rather than a one-direction H2H trend: **9-6 Orix (Aug 3), 3-1 Orix (Aug 5), 3-1 Rakuten (Aug 6), 9-1 Orix (Aug 11), 7-2 Rakuten (Aug 12), 8-2 Orix (Aug 13), 5-1 Rakuten (Aug 25)**. The last seven therefore contain both four-run games and multiple 9+ run games. This evidence is used to widen the corridor, not to mechanically vote Over or Under.

Season-series context is also mixed with the broader standings: after yesterday's result, Rakuten held an **11-8** edge in the 2026 head-to-head despite being far worse in the overall Pacific League table. That is a material reason not to make an Orix outright winner look stronger than it is.

### Qualitative joint-run corridor

The active framework does not authorise a fitted NPB probability. The research-only central branch is approximately **6-8 combined runs**, with a wider-than-normal **4-10+** tail because Saito's first-team workload is uncertain.

Mechanistically:

1. Orix's season offense is modestly better and faces a starter who has allowed 19 HR in 117 innings.
2. Rakuten faces a starter whose current farm form is credible, but whose transition back to first-team hitters is uncertain after a disastrous July cameo.
3. Both clubs retain usable late-inning relief, including fresh high-leverage options.
4. The exact alternate totals deliberately overlap: **7-8 runs cashes both Over 6.5 and Under 8.5**, which sits directly inside the central corridor.

The upper tail is Saito failing to carry his farm reset into the first team and Shoji's homer vulnerability simultaneously showing up. The lower tail is Saito giving Orix five-to-six competent innings while Shoji limits damage and both bullpens handle the final third.

### Required unique ranking

| Rank | Candidate | Pick | Verdict | Evidence quality | Performance role | Central mechanism | Strongest ordinary kill path |
|---:|---|---|---|---|---|---|---|
| **1** | P091-C02 | **Orix Buffaloes +1.5** | **SUPPORTED** | MEDIUM-HIGH | PRIMARY_FORMAL | Orix are the materially stronger season team, have the slightly stronger offense and home venue, while +1.5 still wins on every Orix win/tie and even a one-run Rakuten win; Saito's farm reset prevents treating the starter matchup as an automatic Orix disadvantage | Rakuten's 11-8 season-series edge and yesterday's 5-1 win prove a live upset branch; if Saito's first-team command collapses again, Rakuten can win by 2+ and clear the cushion |
| **2** | P091-C04 | **Combined Under 8.5** | **LEAN** | MEDIUM | PRIMARY_FORMAL | The central corridor is 6-8, both bullpens retain high-leverage options, and Saito's 3.22 farm ERA/strong Aug 18 start is more relevant than the 189.00 one-out outlier | Saito's return fails quickly and Shoji's 19-HR profile also leaks damage, creating the 5-4/6-4/7-3 branch that defeats 8.5 |
| **3** | P091-C03 | **Combined Over 6.5** | **LEAN** | MEDIUM | CORRELATED_SECONDARY | Seven or eight runs sits in the central corridor, so C03 and C04 can both win; Saito uncertainty plus Shoji's home-run exposure keeps 7+ highly plausible | Both starters reach six efficient innings and the fresh back-end relievers convert the game into 3-2, 4-2 or another six-or-fewer total |
| **4** | P091-C01 | **Rakuten Eagles +0.5** | **FORCED RANK** | MEDIUM | CORRELATED_SECONDARY | Rakuten's season-series lead and yesterday's 5-1 win make the upset/no-loss branch genuine, and Shoji is the more established first-team starter | Orix's stronger season record, home venue and slightly better offense convert to any outright Orix win; +0.5 has no one-run-loss cushion |

### Ranking checks

**Top-slot test:** Orix +1.5 receives the most robust geometry of the four supplied rows. It does not require trusting Saito to win the game; it only requires avoiding a Rakuten win by 2+. Orix's much better season record and offense support that cushion, while the Saito farm evidence removes the strongest reason to dismiss it outright.

**Total pair check:** Under 8.5 is ranked above Over 6.5 because 9+ requires the more extreme upper-tail branch, whereas 7-8 allows both total contracts to win. The Over is still a `LEAN`, not a fade, because the Saito transition risk and Shoji's home-run profile keep 7+ fully live.

**Bottom-slot swap test:** the best case for Rakuten +0.5 is legitimate — Rakuten lead this season series 11-8 and won yesterday 5-1, while Shoji is far more established than Saito at first-team level. It stays fourth because the exact contract loses on **any** Orix win, whereas the strongest season-wide evidence still points Orix and the +1.5 line already captures the close-Rakuten-win scenario more robustly.

### Potential game winner

**Orix Buffaloes — `LEAN`.**

Orix have the stronger season record, stronger aggregate offense, home venue and a starting lineup with Ryoma Nishikawa/Kita/Ohta/Kurebayashi through the heart of the order. The winner call is held below `SUPPORTED` because Rakuten lead the season series, won yesterday, and Shoji is the more proven first-team starter. Saito's farm form is good enough to make an Orix lean defensible, but his first-team re-entry remains the largest single uncertainty in the game.

### Honesty / publication boundary

- No prices supplied: **NO VALUE DETERMINABLE**; no EV/ROI/staking claim.
- NTS-2026.08.25-v0.2 remains Stage 0/pre-fit: **no calibrated probabilities generated or published**.
- One joint qualitative corridor controls both totals; no independent threshold pseudo-probabilities are invented.
- Operator-specific tie/extra-inning/action treatment remains unknown.
- Final NPB refresh at the recorded cutoff still showed **game not started**.

### Primary evidence retained

- NPB official event/live page: `https://npb.jp/scores/2026/0826/b-e-20/box.html`
- NPB Kosei Shoji player record: `https://npb.jp/bis/players/21925157.html`
- NPB Kyosuke Saito player record: `https://npb.jp/bis/players/41745157.html`
- NPB Orix farm pitching: `https://npb.jp/bis/eng/2026/stats/idp2_b.html`
- NPB Saito Aug 18 farm start: `https://npb.jp/bis/eng/2026/games/fs2026081800886.html`
- NPB Pacific League team batting: `https://npb.jp/bis/2026/stats/tmb_p.html`
- Pacific League official team pitching statistics: `https://pacificleague.com/en/stats/team/pitcher`
- NPB 25 August Orix-Rakuten final: `https://npb.jp/bis/eng/2026/games/s2026082501750.html`
- NPB recent H2H finals: 3 Aug, 5 Aug, 6 Aug, 11 Aug, 12 Aug, 13 Aug 2026 official scorecards.

**Result:** `OPEN — PREGAME` at issue.  
**Next canonical ID after this append:** `P-092`.


---

## Queue re-verification before P-092 — 2026-08-26 19:20 Australia/Melbourne

| ID | Event | Current state at recheck | Action |
|---|---|---|---|
| P-087 | India vs Sri Lanka, 2nd Test | **LIVE / unresolved** — same-day current coverage still identified the Colombo Test as live on Day 4; no authoritative final was available at this gate | Leave open; no premature settlement |
| P-088 | Howlers Sporting Singtam vs Sikkim Boys Club | **FULL-TIME STATE NOT TRUSTWORTHILY VERIFIED** — targeted current search still did not recover a reliable official/full-time result | Leave open; do not guess settlement |
| P-089 | Hanshin Tigers @ Chunichi Dragons | **Official NPB page still displayed `試合開始前`** at the current refresh | Leave open |
| P-090 | Nippon-Ham Fighters @ Seibu Lions | **Official NPB page still displayed `試合開始前`** at the current refresh | Leave open |
| P-091 | Rakuten Eagles @ Orix Buffaloes | **Official NPB page still displayed `試合開始前`** at the current refresh | Leave open |

**Queue conclusion:** no existing item was honestly settleable before P-092. Proceed with the new KBO pregame card.

---

## P-092 — Doosan Bears @ KT Wiz — PREGAME

**Recorded / evidence cutoff:** 2026-08-26 19:20 Australia/Melbourne / 18:20 KST  
**Scheduled start:** 2026-08-26 18:30 KST / 19:30 Australia/Melbourne  
**Sport / competition:** KBO League regular season  
**Official fixture:** Doosan Bears at KT Wiz, season meeting 12  
**Venue:** Suwon KT Wiz Park, Suwon, South Korea  
**GAME-STATE:** **PREGAME** — official KBO daily schedule listed `DOOSAN : KT` at Suwon for 18:30 KST with no score at the forecast cutoff.  
**Method:** MDS-2026.08.26-v2.2 qualitative champion  
**Numerical state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE` — no same-time prices or operator terms supplied.

### Frozen target and supplied decision set

**Target IDs**
- `TGT-P092-MARGIN`: official full-game Doosan/KT final run margin through the KBO game endpoint, including any permitted extra-inning/tie state.
- `TGT-P092-RUNS`: combined official full-game runs through the same endpoint.
- `TGT-P092-WINNER`: official full-game match winner state.

Operator-specific tie/refund, listed-pitcher/action, suspension and shortened-game settlement rules were not supplied and remain `UNKNOWN_DEFINITION`. Research geometry uses the official KBO final sporting outcome; sportsbook settlement must follow the actual operator if later provided.

| Candidate | User-supplied contract | Research settlement geometry | Dependence / eligibility |
|---|---|---|---|
| P092-C01 | **Doosan Bears +1.5** | WIN if Doosan wins/ties or loses by exactly 1; LOSS if KT wins by 2+ | `DG-P092-MARGIN`; ELIGIBLE |
| P092-C02 | **KT Wiz +1.5** | WIN if KT wins/ties or loses by exactly 1; LOSS if Doosan wins by 2+ | `DG-P092-MARGIN`; ELIGIBLE |
| P092-C03 | **Combined Over 8.5 runs** | WIN at 9+ total runs; LOSS at 0-8 | `DG-P092-TOTAL`; ELIGIBLE |
| P092-C04 | **Combined Under 10.5 runs** | WIN at 0-10 total runs; LOSS at 11+ | `DG-P092-TOTAL`; ELIGIBLE |

**Geometry:** C01 and C02 overlap: both win on a tie or any one-run result. C03 and C04 also overlap: **both win at exactly 9 or 10 combined runs**. The four rows are deterministic queries of one joint game process, not four independent opportunities.

### D0 mechanism retrieval

**Predeclared query:** baseball → pregame → full-game side/positive-handicap and alternate-total markets → named starters → starter-length / HR-contact / bullpen-chain mechanism.

Retrieved mechanism cases: **P-034, P-036, P-053, P-054, P-060**. Transferable checks only, not outcome votes:

- starter run quality and starter length must be scored separately;
- bullpen workload indicates likely availability, not guaranteed performance;
- a +1.5 cushion needs outright / one-run / 2+-run separation branches;
- short expected starter length is not automatically an Over;
- HR/contact, early-hook and late-relief clustering must be kept as explicit upper/separation tails.

The immediate same-team predecessor **P-067 (25 August Doosan @ KT)** is current-series context rather than D0: Doosan won 3-1. Its retrospective specifically noted that the Doosan starter-control branch was knowable and underweighted in the prior KT winner call. That result is not mechanically carried forward because today's starters and lineup differ.

### Confirmed starters and current lineup state

**KBO official preview starters:**
- **Doosan: Jack Logue, LHP** — 22 G, 6-6, 4.06 ERA. His latest start (20 Aug at NC) was 6.1 IP, 4 ER. In his one 2026 start against KT (11 Apr at Suwon) he allowed 9 hits and 5 runs, 3 earned, over 6 innings.
- **KT: Davis Daniel, RHP** — 2 KBO starts, 10.0 IP, 9 H, 1 HR, 3 BB, 8 K, 3 ER, 2.70 ERA. He went exactly 5 innings in both starts: 5 IP/2 ER at NC on 13 Aug and 5 IP/1 ER at LG on 19 Aug. This is a promising but still small first-team sample; it is not treated as proven 2.70-ERA talent.

**Same-day lineup reporting:**
- Doosan's order was reported as Park Chan-ho, Jung Soo-bin, Ahn Jae-seok, Yang Eui-ji, Kim Min-seok, Unio Severino, Oh Myung-jin, Kim Dae-han and Jo Soo-haeng, with Logue–Yang as the battery.
- **Park Jun-soon is out of the starting nine** after an 0-for-11 stretch over his previous three games. His season production (.307, 16 HR, .888 OPS in the same-day report) makes that a material reduction to Doosan's normal offensive ceiling even though the rest of the order retains Yang Eui-ji and Jung Soo-bin.
- KT's reported order: Choi Won-jun, Kim Hyun-soo, Ahn Hyun-min, Sam Hilliard, Jang Sung-woo, Kim Sang-soo, Heo Kyung-min, Han Seung-taek and Kwon Dong-jin.

### Team baseline and matchup process

Official KBO team batting through the current table:
- **KT:** .279 AVG, 599 runs in 109 games, 82 HR.
- **Doosan:** .270 AVG, 525 runs in 113 games, 86 HR.

This gives KT the clearly stronger season run-production baseline despite a similar home-run count.

Official KBO team pitching through the current table:
- **Doosan:** **3.69 ERA**, 51 quality starts, 85 HR allowed — league-leading run prevention.
- **KT:** **4.37 ERA**, 46 quality starts, 94 HR allowed.

Standings at the same cutoff: **KT 64-42-3 (.604), first; Doosan 59-50-4 (.541), fifth**. The season series entering today is **KT 6-1-4** after Doosan's 3-1 win yesterday.

The direct starter comparison is mixed rather than one-sided: Daniel has the better current run line but only 10 KBO innings and no six-inning start; Logue has the proven 6+ inning workload but has been more hittable and struggled in his one 2026 KT start.

### Bullpen / late-inning branch

Doosan used **Kim Taek-yeon, Takada Takuto and Lee Young-ha for one scoreless inning each yesterday** after Choi Min-seok completed six. They may still be available on consecutive days, but their back-to-back branch is explicitly different from a fully rested pen.

KT's starter So Hyeong-jun also completed six innings yesterday. The exact KT relief-chain usage was not fully reconstructed from the official scoreboard in this pass, so no unsupported claim of a fully fresh or exhausted KT pen is made.

Daniel's two KBO starts ending after exactly five innings means KT's middle/late relief exposure is a real structural branch today. Per the active rule, this raises uncertainty; it does **not** mechanically make Over 8.5 the preferred total.

### Environment

Suwon KT Wiz Park is outdoors. Korea Meteorological Administration's 26 August short-term forecast carried possible rain/showers across the Seoul metropolitan/Gyeonggi area into the **18:00-21:00 KST** window. No stadium-local delay/postponement had been verified at the cutoff and KBO still listed the 18:30 game normally. Weather therefore widens delay/ball-grip uncertainty but receives **no automatic Over or Under sign**.

### Qualitative joint-game corridor

No validated KBO numerical model exists. The qualitative central branch is approximately **8-10 combined runs with a narrow KT side edge**, not a calibrated mean or probability.

- **Lower branch:** Daniel's early KBO run suppression persists, Logue reaches 6+ efficiently, Doosan's elite season staff contains KT and the game lands around 5-7 runs.
- **Central branch:** KT's stronger offense gets 4-6 runs while Doosan gets 3-5; the game stays close and lands around 8-10.
- **Upper branch:** Daniel exits after five or earlier, Doosan's worked late trio is stressed, Logue's prior KT contact/HR risk resurfaces, and 11+ becomes live.
- **Separation tail:** either Daniel turns his small-sample start into six strong innings and KT breaks open Doosan's relief chain, or Logue reproduces yesterday's Doosan starter-control script and Doosan wins by 2+.

### Required unique ranking

| Rank | Candidate | Pick | Verdict | Evidence quality | Performance role | Actionability | Central mechanism | Strongest ordinary kill path | Probability state |
|---:|---|---|---|---|---|---|---|---|---|
| **1** | P092-C02 | **KT Wiz +1.5** | **LEAN** | MEDIUM-HIGH | PRIMARY_FORMAL | LIKELIHOOD RANK ONLY | KT has the stronger season record/offense, home field and the more favorable current starter run line; +1.5 also survives every KT win/tie and a one-run Doosan loss | Doosan just demonstrated the exact failure branch yesterday: starter suppression + two solo HR + late relief. Logue's length and Doosan's 3.69 staff ERA can recreate a 4-2/5-2 Doosan win | NOT_GENERATED / NOT PUBLISHED |
| **2** | P092-C04 | **Combined Under 10.5** | **LEAN** | MEDIUM | PRIMARY_FORMAL | LIKELIHOOD RANK ONLY | 10.5 sits above the central 8-10 corridor; Daniel has allowed only 3 ER in 10 KBO innings and Doosan owns the league's best staff ERA | KT's 599-run offense attacks Logue, Daniel again stops at five, and the Doosan high-leverage trio faces back-to-back stress, producing 6-5/7-4 or another 11+ game | NOT_GENERATED / NOT PUBLISHED |
| **3** | P092-C01 | **Doosan Bears +1.5** | **LEAN** | MEDIUM | CORRELATED_SECONDARY | LIKELIHOOD RANK ONLY | Doosan's run prevention is materially better, Logue usually supplies more starter length than Daniel, and the +1.5 survives a one-run KT win | KT's superior offense, home venue, season-series edge and Daniel's current suppression convert into a multi-run KT win; Park Jun-soon's absence lowers the Doosan response ceiling | NOT_GENERATED / NOT PUBLISHED |
| **4** | P092-C03 | **Combined Over 8.5** | **FORCED RANK** | MEDIUM-LOW | CORRELATED_SECONDARY | LIKELIHOOD RANK ONLY | 9-10 sits inside the central corridor and cashes alongside Under 10.5; Daniel's five-inning exposure and Logue's prior KT contact allow a live 9+ route | Both starters work efficiently enough to hand leads to usable pens and the Doosan staff baseline wins out, leaving 3-2/4-3/5-3 or another 8-or-fewer final | NOT_GENERATED / NOT PUBLISHED |

### Ranking checks

**Top-slot test:** KT +1.5 is the strongest marginal contract, but **not upgraded to `SUPPORTED`**. The strongest contrary path is ordinary and fresh: Doosan won this exact matchup by two yesterday and still owns the league's best run-prevention baseline. The starter and lineup changes favor KT enough to rank the cushion first, not enough to call it a strong-certainty branch.

**Side-overlap check:** both +1.5 lines can win on a one-run game or tie. The rank is therefore about which 2+-run-loss tail is less likely, not about choosing opposite sides as a hedge. KT's broader team/offensive edge makes the Doosan-by-2+ tail the smaller of the two, but the gap is not large.

**Total-overlap check:** Over 8.5 and Under 10.5 both win at **9-10**. Under ranks higher because it additionally wins every lower-scoring branch, while Over needs at least nine and is more exposed to the strong Doosan run-prevention baseline.

**Bottom swap test:** the best case for Over 8.5 is legitimate — the raw team scoring environment is close to this band, Daniel has not worked past five innings in KBO, Doosan's leverage trio worked yesterday, and Logue allowed KT nine hits in their earlier meeting. It remains fourth because those are upper-exposure/tail mechanisms rather than enough evidence to override Daniel's current run suppression plus Doosan's season staff quality.

### Potential winner

**KT Wiz — `LEAN` (thin).**

KT is first in the league, has the stronger offense, home field, a 6-1-4 season-series edge and a starter who has allowed only three earned runs in his first two KBO outings. The winner call is intentionally weaker than KT +1.5 because Doosan's 3.69 staff ERA, Logue's ability to work six-plus, yesterday's 3-1 result and Doosan's current two-game winning run all make an outright KT loss a normal branch rather than a tail.

### Honesty / publication boundary

- No odds or operator supplied: **NO VALUE DETERMINABLE**; no EV, ROI, staking or market-edge claim.
- NTS-2026.08.25-v0.2 remains Stage 0/pre-fit: **no numerical KBO probability was generated or published**.
- The 8-10 corridor is a qualitative scenario band, not a fitted score distribution.
- Park Jun-soon's lineup omission is verified by same-day reporting; the exact effect size is an inference, not a model coefficient.
- Weather is a possible game-window uncertainty, not a directional total rule.
- Final pre-issue state was still **PREGAME** before the official 18:30 KST start.

### Sources retained

- KBO official daily schedule: `https://eng.koreabaseball.com/Schedule/DailySchedule.aspx`
- KBO official 26 Aug preview: `https://web1.koreabaseball.com/MediaNews/News/Preview/View.aspx?bdSe=62150`
- KBO official Davis Daniel daily pitching record: `https://www.koreabaseball.com/Record/Player/PitcherDetail/Daily.aspx?playerId=56002`
- KBO official team batting: `https://www.koreabaseball.com/Record/Team/Hitter/Basic1.aspx`
- KBO official team pitching: `https://www.koreabaseball.com/Record/Team/Pitcher/BasicOld.aspx`
- KBO official 25 Aug scoreboard: `https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-08-25`
- Same-day lineup report: Chosun/OSEN, 26 Aug 2026, Park Jun-soon omitted / Oh Myung-jin starts at 2B.
- Korea Meteorological Administration short-term forecast, 26 Aug 2026.

**Result:** `OPEN — PREGAME` at issue.  
**Next canonical ID after this append:** `P-093`.

### P-092/V02 — final delivery-state confirmation (2026-08-26 19:22:46 Australia/Melbourne)

The final delivery clock check remained **before the scheduled 19:30 Australia/Melbourne / 18:30 KST first pitch**. No later lineup/starter contradiction was found after the P-092/V01 cutoff. The controlling delivery order therefore remains **#1 KT Wiz +1.5 `LEAN`; #2 Under 10.5 `LEAN`; #3 Doosan Bears +1.5 `LEAN`; #4 Over 8.5 `FORCED RANK`**, with **KT Wiz `LEAN`** as the potential winner.

---

## P-093 — NC Dinos @ LG Twins, KBO regular season — PREGAME FORECAST

**View ID:** P-093/V01  
**Recorded / evidence cutoff:** 2026-08-26T19:27:57+10:00 Australia/Melbourne / 2026-08-26T18:27:57+09:00 Asia/Seoul  
**Scheduled start:** 2026-08-26 18:30 KST / 19:30 Australia/Melbourne  
**Venue:** Jamsil Baseball Stadium, Seoul  
**GAME-STATE:** `PREGAME — OFFICIAL KBO SCOREBOARD STILL 경기전, NO GAME ACTION`. Final official scoreboard refresh immediately before append continued to show NC @ LG as pregame with 18:30 start and blank inning lines.

**Method:** MDS-2026.08.26-v2.2 qualitative champion. Numerical state `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`; NTS-2026.08.25-v0.2 remains Stage 0/pre-fit. No calibrated KBO probability exists.  
**Candidate origin:** `USER_SUPPLIED`; complete four-row slate frozen before directional ranking.  
**Operator/odds:** NOT SUPPLIED. Full-game research interpretation assumed; exact sportsbook extra-inning/tie/suspension/action rules are `UNKNOWN_DEFINITION`. No value/EV/ROI/staking claim is permitted.

### Queue / retrospective gate

P-087 remains live/open; P-088 still lacks a trustworthy verified final. P-089/P-090/P-091 were still exposed as pregame by their official NPB pages at the latest queue check, and P-092 remained pregame before its 19:30 Melbourne start. No preceding record had a newly verified final that could honestly be settled before P-093.

**D0 mechanism retrieval:** nearest comparable KBO/baseball controls include P-049 (long starter exposure drove the Under; separate score-centre width from direction), P-053/P-054 (direct starter matchup + confirmed batting order + eighth/ninth chain outrank generic season/H2H; bullpen workload describes availability, not performance), and P-067 (Doosan@KT: a low-total read succeeded while the favored winner missed when the opposing starter-control branch materialised). These are process checks only, not analogue voting or probabilities.

### Target and contract freeze

**Target IDs:**
- `P093-KBO-MARGIN-FULL-v1`: official full-game LG-minus-NC run margin under the supplied operator's action/extra-inning/tie rules; start state pregame; endpoint official graded full game.
- `P093-KBO-RUNS-FULL-v1`: combined NC + LG official full-game runs; same start/endpoint assumptions.
- `P093-KBO-WINNER-FULL-v1`: full-game winner direction; operator draw/tie treatment unknown.

**Contract geometry:**
- C01 NC Dinos +1.5: wins on any NC win, official tie, or exactly one-run LG win under the research-grade margin interpretation; loses on LG by 2+.
- C02 LG Twins +1.5: wins on any LG win, official tie, or exactly one-run NC win; loses on NC by 2+.
- C03 Over 7.5: wins at 8+ combined runs.
- C04 Under 9.5: wins at 0–9 combined runs.
- C03 and C04 **overlap at exactly 8 or 9 runs**. C01 and C02 can both win in a one-run game or an official tie. These are dependent contract queries, not four independent events.

### Confirmed event and participant evidence

**Official KBO preview:** season meeting 12 at Jamsil. LG starts **Im Chan-kyu**, NC starts **Koo Chang-mo**. Im: 22 G, 11-4, 4.14 ERA, three consecutive quality starts; latest was 6 IP/1 ER vs KT. Koo: 21 G, 9-4, 3.89 ERA; recent form includes 7 scoreless innings vs KT on Aug 12 and 6 IP/2 ER vs Doosan on Aug 20. The same official preview identifies NC's bullpen slump/comeback-loss problem as continuing.

**Confirmed LG order:** Shin Min-jae 2B; Park Hae-min CF; Austin Dean DH; Moon Bo-kyung 3B; Song Chan-ui LF; Moon Jeong-bin 1B; Koo Bon-hyuk SS; Park Dong-won C; Hong Chang-ki RF. Oh Ji-hwan is out of the starting nine. Moon Bo-kyung returns to cleanup after 10 hits in his previous 20 at-bats; Park Dong-won starts after three straight games out of the starting lineup. Austin produced a cycle in yesterday's 5-4 extra-inning win.

**Confirmed NC order:** Kim Joo-won SS; Kwon Hee-dong RF; Park Min-woo 2B; Blaine Crim 1B; Park Geon-woo DH; Lee Woo-sung LF; Kim Hwi-jip 3B; Kim Hyung-jun C; Cheon Jae-hwan CF. Seo Ho-cheol is deliberately benched despite a strong historical line vs Im because the manager cited his current confidence/form; old direct batter-v-pitcher history is therefore not promoted over the actual current lineup decision.

### Baseline and current process

**Team offense:** official KBO team batting table through the current completed schedule shows NC **.272, 540 runs in 107 games, 100 HR** and LG **.269, 584 runs in 113 games, 106 HR**. That is roughly 5.05 NC runs/game and 5.17 LG runs/game as descriptive season baselines, not forecasts. League-wide scoring is 5697 runs across 560 games, roughly 10.17 combined runs/game; the requested 7.5/9.5 corridor therefore straddles a normal KBO scoring environment rather than an extreme market.

**Team/venue strength:** the latest official standings/team-v-team table before today's game had LG materially ahead overall and with the better home profile; the season series was approximately balanced with LG holding a narrow edge after yesterday's win. This is contextual strength only; it does not override Koo's stronger current starter run-prevention line.

**Yesterday's 5-4 LG win:** the game was 0-2 entering the bottom of the eighth, LG moved ahead on Austin's three-run HR, NC tied in the ninth, NC retook the lead in the tenth, then LG walked it off. This is useful mechanism evidence: both starters suppressed scoring into the late game, while bullpens/late state created the upper run tail. It is not treated as a trend vote for another 9-run game.

**Bullpen exposure:** yesterday required 10 innings. LG's late group included a blown ninth-inning lead and further tenth-inning work; NC also surrendered late separation. Exact availability/performance branches remain uncertain. Per the active baseball rule, workload is used to estimate likely availability only and receives no automatic negative performance coefficient.

**Weather:** KMA's late-afternoon forecast allowed only very light/drizzle-type precipitation around much of Seoul/Gyeonggi rather than a verified material Jamsil delay. No directional total adjustment is made from weather.

### Qualitative joint run / margin corridor

**Lower branch:** Koo continues his August command/run suppression and Im extends his three-QS run; both reach six-plus; late relief is competent -> roughly 5–7 total runs, close game.  
**Central branch:** each starter allows a manageable 2–3 runs, LG's deeper/currently hotter middle order creates a slight home edge, and one bullpen adds late scoring -> roughly **8–10 total runs**, narrow LG lean.  
**Upper branch:** early starter traffic or an HR cluster plus the previous night's bullpen workload/NC late-relief weakness -> 11+ runs.  
**LG-separation tail:** Austin/Moon Bo-kyung attack Koo before his normal exit and NC's relief chain leaks -> LG by 2+; kills C01.  
**NC-separation tail:** Koo dominates, NC converts Im's weaker historical matchup shape/current traffic into a lead, and LG's worked late arms fail -> NC by 2+; kills C02.

### Frozen ranking

| Rank | Candidate / contract | Exact win interval | Verdict | Evidence quality | Dependence group | Performance role | Actionability | Central mechanism | Strongest kill path | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | **C02 — LG Twins +1.5** | LG win/tie or lose by exactly 1 | `LEAN` | MEDIUM-HIGH | P093-MARGIN | PRIMARY_FORMAL | Likelihood rank only | Better overall/home baseline, stronger current lineup shape, +1.5 cushion, NC bullpen instability | Koo controls LG and NC wins by 2+ | NOT_GENERATED / NOT PUBLISHED |
| **2** | **C01 — NC Dinos +1.5** | NC win/tie or lose by exactly 1 | `LEAN` | MEDIUM | P093-MARGIN | CORRELATED_SECONDARY | Likelihood rank only | Koo's 3.89 ERA/current August suppression plus broad one-run cushion keeps NC live in a close-game corridor | LG's middle order reaches Koo and NC relief creates 2+ separation | NOT_GENERATED / NOT PUBLISHED |
| **3** | **C03 — Over 7.5 runs** | 8+ | `LEAN` | MEDIUM | P093-TOTAL | PRIMARY_FORMAL | Likelihood rank only | Season scoring environment + both competent offenses + late-bullpen/HR tail; 8–9 is inside central corridor | Both starters reach 6–7 quality innings and game stays 3-2/4-2 | NOT_GENERATED / NOT PUBLISHED |
| **4** | **C04 — Under 9.5 runs** | 0–9 | `FORCED RANK` | MEDIUM-LOW | P093-TOTAL | CORRELATED_SECONDARY | Likelihood rank only | Two in-form starters make 6–9 highly live and 8–9 wins both total rows | 10+ arrives through normal late bullpen scoring or HR clustering; 10 already defeats this row while Over still wins | NOT_GENERATED / NOT PUBLISHED |

**Top-slot check:** LG +1.5 has fresh event-specific support, but Koo is too credible a starter to upgrade the row to `SUPPORTED`; rank #1 remains `LEAN`.  
**Bottom swap test:** Under 9.5 has a genuine case because Koo/Im are both in good current form. It remains fourth because the line loses at 10 while Over 7.5 already wins at 8, and the official team-scoring environment plus late-relief uncertainty leave 10+ as an ordinary—not exotic—failure route.

### Potential winner

**LG Twins — `LEAN` (thin).** LG have the better overall/home team baseline, the more convincing current middle-order form, and NC's bullpen is the more persistent late-game concern. Koo's current starter form is strong enough that the winner call is materially weaker than LG +1.5 and is not upgraded beyond a thin lean.

### Integrity / limitations

- No operator, odds, both-side prices, tie rules, extra-inning/action or suspension terms were supplied. Book settlement may differ from the research-grade full-game geometry.
- No fitted/calibrated KBO model ran. No numerical probability was generated or published.
- Recent scoring and yesterday's 5-4 are diagnostic only; starter exposure, confirmed orders and relief-chain uncertainty control the card.
- The view was frozen and appended before the scheduled first pitch while the official KBO scoreboard still showed `경기전`.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-094`.


---

## P-094 — Yorkshire Women vs Surrey Women, Metro Bank One Day Cup Women — TOSS COMPLETE / PRE-FIRST-BALL FORECAST

**View ID:** `P-094/V01`  
**Recorded / evidence cutoff:** 2026-08-26T19:36:26+10:00 Australia/Melbourne / 2026-08-26T10:36:26+01:00 BST  
**Scheduled start:** 2026-08-26 10:30 BST / 19:30 Australia/Melbourne  
**Venue:** Ampleforth College, Ampleforth, North Yorkshire  
**Competition / rules population:** Metro Bank One Day Cup Women / ECB Women's One-Day Cup, 50-over List A  
**GAME-STATE:** `TOSS COMPLETE — PRE-FIRST-BALL / NO SCORED DELIVERY EXPOSED AT CUTOFF`. A current specialist scorecard reported **Surrey Women elected to bowl**, so Yorkshire bat first. Separate current live feeds still exposed no batter/bowler line and/or 0 overs at the final research refresh. No elapsed-run-rate information enters this view.

**Method:** MDS-2026.08.26-v2.2 qualitative champion.  
**Numerical state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`; NTS-2026.08.25-v0.2 remains Stage 0/pre-fit.  
**Candidate origin:** `USER_SUPPLIED`; all four supplied rows frozen before ranking.  
**Operator / odds:** NOT SUPPLIED. Exact operator shortened-match, void, settlement and statistic-provider terms remain `UNKNOWN_DEFINITION`; no value, EV, ROI or staking claim is permitted.

### Queue / retrospective gate

The carried predecessor records P-087 and P-088 were not newly settleable from a controlling authoritative final in this pass. P-089 through P-093 were recently issued/open records in the current working log and no trustworthy completed final was established before P-094. No live/open record was graded from a stale source.

### Target and contract freeze

**Target A — `P094-YOR-1INN-RUNS-v1`:** Yorkshire Women's completed first-innings total from the pre-first-ball state. Unit = runs including extras under official scorecard convention. Endpoint = 50 completed overs or earlier all-out/competition-recognised innings termination; shortened/abandoned operator treatment unknown.

- `P094-C01`: Yorkshire 1st innings **Over 225.5** — WIN at 226+.
- `P094-C02`: Yorkshire 1st innings **Under 225.5** — WIN at 225 or fewer.
- These are exact complements if the innings receives a normal settled result under the operator's terms.

**Target B — `P094-YOR-FIRST5-RUNS-v1`:** Yorkshire runs after the first **5 completed overs / 30 legal deliveries**, including extras under official scorecard convention. Endpoint = end of 5.0 overs; shortened/abandoned operator treatment unknown.

- `P094-C03`: Yorkshire first 5 overs **Over 19.5** — WIN at 20+.
- `P094-C04`: Yorkshire first 5 overs **Under 19.5** — WIN at 19 or fewer.
- These are exact complements if the 5-over phase is completed and settled.

The first-five target and full-innings target are related but **not interchangeable**. Early pace/wickets inform later resources only through a new state; the 5-over result is not extrapolated mechanically to 50 overs.

### Identity, toss, conditions and availability

- Yorkshire's official fixture and live page identify this exact 26 August match at Ampleforth College, 10:30 BST.
- Yorkshire's official live report described the ground pre-match as **dry and bright** and stated this is a **new venue for Yorkshire Women / first professional first-team fixture there**, so no trustworthy same-competition venue scoring prior is available.
- **STRIP STATUS:** `NOT FOUND AFTER SEARCH`. No official/curator match-specific grass, hardness, seam, turn or pace description was found. A generic secondary score-site pitch label is excluded from directional evidence.
- **MATCH CONDITIONS STATUS:** `OBSERVED — dry/bright pre-start`; no verified material weather interruption at cutoff.
- Current specialist scorecard reported **Surrey elected to bowl**. The authoritative Yorkshire page had not yet exposed the toss/XIs at the retrieval snapshot.
- **Confirmed XI status:** `NOT AVAILABLE FROM CONTROLLING OFFICIAL SOURCE AT CUTOFF`. Secondary squad/playing-XI pages were inconsistent/stale enough that no unverified player was treated as definitely selected. This caps evidence strength.

### Competition / team baseline

Before this match, the official/established standings sources had Surrey Women **5 wins from 11, 22 points, NRR around -0.12** and Yorkshire Women **3 wins from 11, 16 points, NRR around -0.29**.

Yorkshire's 2026 One-Day Cup innings show a wide distribution rather than a stable low/high regime. Relevant completed team scores include **178, 185 (44-over rain-reduced first innings), 280/9, 241, 290, 257, 196/8 in a shortened chase, 238, 194/4 in a chase, 150 and 202**. The spread demonstrates both 250+ ceilings and genuine collapse floors; raw mean/median is diagnostic only.

More relevant to today's **bat-first** state:
- 178 all out vs Somerset;
- 185 all out in a rain-reduced 44-over innings vs Surrey;
- 280/9 vs The Blaze;
- 241 vs Lancashire;
- 238 all out vs Warwickshire;
- 150 all out vs The Blaze after Yorkshire elected to bat.
This is a near-balanced threshold history around 225.5 rather than a strong one-sided trend.

Surrey's 2026 field-first/bowling-first evidence is comparatively supportive of a 225+ opponent ceiling: opponents batting first against Surrey have included Yorkshire 185 in a rain-reduced game, Durham 256, Somerset 337, Hampshire 272, Essex 227 and Lancashire 246. This does **not** become an automatic Over; opposition quality, venue and current XI differ. It does prevent the earlier 185 against Surrey from being treated as the only matchup baseline.

### Current batting / matchup process

Yorkshire's official preview highlights **Sterre Kalis** as an in-form batting anchor: she made 52 in the previous One-Day Cup game at Warwickshire and had passed 1,000 runs across Yorkshire/Netherlands cricket since April. That supports a higher middle-innings stability branch if she receives normal exposure.

The strongest Yorkshire failure mechanism is also well established: wicket clusters. In the April Surrey game Yorkshire were well placed at **131/2** before collapsing to **185 all out**; against The Blaze on 23 June they slipped to **60/5 inside 16 overs** and were dismissed for 150. Current batting-first upside therefore depends on preserving wickets through the first 15–25 overs, not merely clearing 20 in the opening five.

### First-five-over process

The cleanest exact same-opponent phase comparator is the 15 April game at The Oval. Surrey also won the toss and bowled; Yorkshire were **28/1 after exactly five overs**, clearing today's 19.5 threshold despite an early wicket. At 3.1 overs they were already 20/0 before losing Georgie Boyce at 21.

One comparator cannot establish a probability. It is used only to demonstrate that the threshold can be cleared through ordinary boundary/running output even with one new-ball wicket. Other Yorkshire starts show substantial variance, and today's opening pair was not authoritatively confirmed at cutoff.

### Qualitative scenario map

**Lower / collapse branch:** Surrey's new-ball attack creates 1–2 early wickets, Yorkshire are <=19 after five and lose another cluster in overs 10–25 -> roughly 170–215; helps C04 and C02.

**Central branch:** Yorkshire clear roughly 20–30 in the first five with 0–1 wickets down, top-order resources establish a middle-overs base, Surrey take wickets often enough to cap the finish -> roughly **225–245**; helps C03, with C01/C02 close around their boundary.

**Upper branch:** wickets are preserved through 25–30 overs and Yorkshire reach the late phase with 6+ wickets in hand -> 250–280+; helps C03 and C01.

**Slow-start recovery branch:** first five finish <=19 but wickets remain intact, Yorkshire recover through middle/late overs -> C04 and C01 can both win. This explicitly prevents first-five Under from being treated as a full-innings Under.

**Fast-start collapse branch:** Yorkshire clear 20 in five but lose a middle-order cluster similar to April vs Surrey / June vs Blaze -> C03 and C02 can both win. This explicitly prevents first-five Over from being treated as a full-innings Over.

### Frozen unique ranking

| Rank | Candidate | Exact contract | Verdict | Evidence quality | Dependence group | Performance role | Actionability | Central mechanism | Strongest ordinary kill path | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | `P094-C03` | **Yorkshire first 5 overs Over 19.5** | `LEAN` | MEDIUM | P094-FIRST5 | PRIMARY_FORMAL | LIKELIHOOD RANK ONLY | Modest 4-rpo threshold; same Surrey field-first matchup produced 28/1 after five; dry pre-start conditions; no chase cap because Yorkshire bat first | Unconfirmed opening combination plus Surrey new-ball wickets leaves Yorkshire 15–19 after five | NOT_GENERATED / NOT PUBLISHED |
| **2** | `P094-C01` | **Yorkshire 1st innings Over 225.5** | `LEAN` | MEDIUM | P094-FULL | PRIMARY_FORMAL | LIKELIHOOD RANK ONLY | Full bat-first exposure, current Kalis form, multiple Yorkshire 238–290 first-innings ceilings, and Surrey has conceded 227–337 in several field-first 2026 games | Repeat of Yorkshire's known collapse branch: 1–2 early wickets become 5 down by the middle overs and total stops near 180–215 | NOT_GENERATED / NOT PUBLISHED |
| **3** | `P094-C02` | **Yorkshire 1st innings Under 225.5** | `FORCED RANK` | MEDIUM-LOW | P094-FULL | CORRELATED_SECONDARY | LIKELIHOOD RANK ONLY | Yorkshire's batting-first record contains 178, rain-reduced 185 and 150; Surrey previously triggered a 131/2 -> 185 collapse | Wickets are preserved through the middle overs and the unfamiliar venue proves benign enough for 240+ | NOT_GENERATED / NOT PUBLISHED |
| **4** | `P094-C04` | **Yorkshire first 5 overs Under 19.5** | `FORCED RANK` | MEDIUM-LOW | P094-FIRST5 | CORRELATED_SECONDARY | LIKELIHOOD RANK ONLY | New-ball uncertainty and unconfirmed XI make a cautious/one-wicket start live | 20 runs requires only 4.0 rpo; the exact April Surrey comparator reached 20 by 3.1 overs and 28/1 after five | NOT_GENERATED / NOT PUBLISHED |

### Ranking checks

**Top-slot test:** C03 is only a `LEAN`, not `SUPPORTED`. The threshold is modest and the same-opponent phase example supports it, but one historical phase plus an unconfirmed current opening combination is insufficient for stronger language.

**Full-innings swap test:** C01 and C02 are close. C01 gets the edge because today's Yorkshire innings is uncapped by a chase target, Kalis carries current form, and Surrey's broader field-first 2026 concession profile has repeatedly crossed 225.5. C02 remains a live branch because Yorkshire's collapse floor is unusually clear and has occurred against Surrey itself.

**Phase/full dependence audit:** C03 is not evidence that C01 must win. The historical record contains both fast starts followed by collapse and slow starts followed by recovery; the two target IDs remain separate.

### Potential winner

**Surrey Women — `LEAN` (medium-low confidence).**

Surrey enter with the better One-Day Cup record (5 wins from 11 versus Yorkshire's 3 from 11), already defeated Yorkshire earlier in this competition, and won the toss/elected to field today, allowing them to chase with knowledge of the target. Against that, Yorkshire are at home, Kalis is in form, the venue is new/low-information, and the confirmed XIs were not available from a controlling official source at cutoff. The winner is therefore a lean only, not a strong selection.

### Integrity / limitations

- **No calibrated probability exists.** H0 is not built; NTS remains Stage 0/pre-fit.
- **No odds/operator were supplied:** `NO VALUE DETERMINABLE`.
- `STRIP STATUS = NOT FOUND AFTER SEARCH`; no generic pitch label is promoted as observed surface evidence.
- Official Yorkshire reporting supplied venue, schedule and dry/bright conditions but had not yet published toss/XIs in the retrieved snapshot; toss is supported by current specialist live reporting.
- This view is frozen at a **pre-first-ball / no-scored-delivery** state. If a later live score exists after this append, it requires a new live view rather than rewriting P-094/V01.

### Sources retained

- Yorkshire official fixture/match centre: `https://yorkshireccc.com/match/yorkshire-women-v-surrey-women-metro-bank-one-day-cup-women-26-aug-2026/`
- Yorkshire official live report: `https://yorkshireccc.com/news/live-yorkshire-women-v-surrey-metro-bank-odc/`
- Yorkshire official preview / Sterre Kalis: Yorkshire CCC, 25 Aug 2026.
- Current specialist live/toss page: Cricket World, Yorkshire Women vs Surrey Women, Match 54 — Surrey elected to bowl.
- Current zero-over/no-ball-data corroboration: WYN Cricket current match page.
- Same-opponent phase evidence: Yorkshire CCC live report, Surrey v Yorkshire Women, 15 Apr 2026 — Yorkshire 28/1 after five.
- Yorkshire first-innings/collapse evidence: Yorkshire CCC match reports and scorecards, 2026 One-Day Cup.
- Competition result cross-check: established scorecard listings; official club pages control Yorkshire-specific facts where available.

**Result at append:** `OPEN — TOSS COMPLETE / PRE-FIRST-BALL`.  
**Next canonical ID:** `P-095`.


---

## P-095 — TSG Hawks @ Fubon Guardians, CPBL regular season — PREGAME FORECAST

**View ID:** `P-095/V01`  
**Recorded / evidence cutoff:** 2026-08-26, final pre-issue refresh before the scheduled 18:35 CST / 20:35 Australia/Melbourne first pitch  
**Official event:** CPBL 2026 regular season GAME 290  
**Venue:** Xinzhuang Baseball Stadium, New Taipei City  
**GAME-STATE:** `PREGAME — OFFICIAL CPBL PAGE: 比賽準備中 / 未開始` at the final refresh.  
**Method:** MDS-2026.08.26-v2.2 qualitative champion.  
**Numerical state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`; NTS-2026.08.25-v0.2 remains Stage 0/pre-fit.  
**Candidate origin:** `USER_SUPPLIED`.  
**Operator / odds:** NOT SUPPLIED. Row 2 “Guardians” is resolved as **Fubon Guardians moneyline**, matching Row 1’s opposing Hawks moneyline. Operator tie/action, shortened-game and void terms remain `UNKNOWN_DEFINITION`; no value/EV/ROI/staking claim is permitted.

### Queue / retrospective gate

Previously issued same-evening NPB, KBO and Yorkshire–Surrey records were not demonstrated final during this pregame pass and are retained open/live as applicable. No open event was settled from a stale or incomplete source.

D0 mechanism retrieval transferred the following process checks only, not outcome votes: baseball starter length must be separated from run quality (`T-004`); bullpen workload predicts availability rather than performance (`T-005` / L-006); the direct starter/lineup/late-relief chain must outrank generic season/H2H reputation in winner calls; and the current baseball tail-stress candidate requires explicit contact/early-hook/relief/extra-inning branches.

### Target / contract freeze

**Target A — `P095-MATCH-RESULT-v1`:** official CPBL full-game result state from pregame start through regulation and competition-authorised extra innings/tie endpoint. CPBL regular-season games are scheduled for nine innings; if tied, the competition rule allows tiebreak extra innings through the 12th. Sportsbook tie treatment is unknown because the operator was not supplied.

- `P095-C01`: **TSG Hawks ML** — research interpretation: Hawks outright win; sportsbook tie/refund treatment unknown.
- `P095-C02`: **Fubon Guardians ML** — research interpretation: Guardians outright win; sportsbook tie/refund treatment unknown.

**Target B — `P095-GAME-RUNS-v1`:** combined official runs by both teams through the contract’s full-game endpoint. Standard full-game including competition extra innings is assumed for research; operator shortened-game/action terms remain unknown.

- `P095-C03`: **Over 6.5** — WIN at 7+ combined runs.
- `P095-C04`: **Under 6.5** — WIN at 0–6 combined runs.
- These total rows are exact complements under matching normal settlement terms; no push exists at 6.5.

### Volatile facts / participants

- Official CPBL GAME 290 page: TSG Hawks @ Fubon Guardians, Xinzhuang, 2026-08-26, still `未開始 / 比賽準備中` at the final refresh.
- Same-day preview identifies the probable starters as **David Buchanan (TSG)** versus **Quinton Martinez (Fubon)**.
- Buchanan: 6-5, **2.48 ERA** entering the game; his only 2026 start against Fubon was 0-1 with 4.76 matchup ERA. Recent official CPBL game evidence includes **6 IP, 5 H, 0 BB, 5 K, 1 ER** on Aug 15.
- Martinez: 1-0, **3.18 ERA** in an extremely small first-team sample; his Aug 12 CPBL start was **5.2 IP, 3 H, 2 BB, 5 K, 2 ER, 86 pitches**, followed by four scoreless relief appearances from the named Fubon chain.
- **Posted batting-order status:** `NOT_AVAILABLE FROM CONTROLLING OFFICIAL SOURCE AT CUTOFF`. This prevents a SUPPORTED verdict and blocks a full T-010 top-six pitch-shape/platoon audit.
- Xinzhuang weather in the same-day preview: roughly **29–30°C, ~10% rain chance**. No automatic weather total direction is applied.

### Current team baseline

Same-day standings before first pitch:
- **Full season:** Fubon 46-42 (.523), TSG 43-45-1 (.489).
- **Second half:** TSG 13-16 (.448), Fubon 12-16 (.429).

Current second-half process snapshot from the CPBL advanced-stat environment:
- TSG offense: roughly **121 runs in 29 games** (~4.17/game), AVG around .271, OBP .340, SLG .355.
- Fubon offense: roughly **94 runs in 28 games** (~3.36/game), AVG around .246, OBP .304, SLG .312.
- TSG second-half staff ERA around **3.95**; Fubon around **4.16**.

The raw current offensive sum is therefore around the mid-7s before starter/context adjustment. It is a baseline only, not a fitted total forecast.

### Starter / bullpen / contact branches

**TSG starter branch:** Buchanan is the more established current starter: season 2.48 ERA, strong walk suppression, and recent six-inning/one-run work. His failure branch is not dismissed: on Aug 9 he allowed 11 hits and 6 runs (4 earned) over five innings, demonstrating a real contact-cluster tail, and Fubon scored three earned runs against him in their earlier meeting.

**Fubon starter branch:** Martinez’s first CPBL start was good, but 5.2 innings / one first-team start is too small to treat his 3.18 ERA as a stable full-season rate. His plausible branch is another 5–6 competent innings; his uncertainty branch is earlier exposure to the Fubon middle relief.

**Bullpen availability:** recent postponements/rest reduce obvious workload pressure for both clubs. This is used only to inform likely availability. It is not converted into a blanket “fresh bullpen = good bullpen” assumption.

**Home-last-bat / extras:** Fubon own the home ninth when trailing/tied; if already leading after the top of the ninth, they may lose a half-inning of offensive exposure. A tie can create extra-inning/tiebreak run clustering through the CPBL maximum-12th-inning structure.

### Relevant matchup history — diagnostic only

Recent 2026 TSG–Fubon finals at Xinzhuang include totals of **4, 13, 15, 6, 7 and 8** across sampled meetings. This is a wide distribution, not a stable Over/Under law. It supports keeping both the starter-suppression floor and the contact/bullpen/extra-inning upper branch active.

### Qualitative scenario map

**Lower scoring:** Buchanan works 6–7 quality innings, Martinez repeats his 5–6 inning debut shape, rested relief avoids traffic -> roughly **4–6 combined runs**; favors Under 6.5.

**Central:** Buchanan suppresses Fubon but not completely; TSG’s stronger current offense gets into the Fubon starter/middle innings; both pens contribute ordinary scoring -> roughly **6–8 combined runs**.

**Upper/contact branch:** Buchanan’s known hit-cluster tail returns and/or Martinez exits around five with traffic; a relief inning or extra-inning tiebreak adds runs -> **9+**; favors Over 6.5.

**TSG winner branch:** Buchanan gives the clear starter edge, TSG’s second-half offensive gap persists, and the Hawks score first into a rested late chain.

**Fubon winner branch:** home field plus the stronger full-season record matters, Martinez repeats his good debut, and Fubon’s core attacks Buchanan’s contact rather than his walk rate; Fubon’s late relief protects a narrow lead.

### Frozen unique ranking

| Rank | Candidate | Contract | Verdict | Evidence quality | Dependence group | Performance role | Actionability | Main mechanism | Strongest ordinary kill path | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | `P095-C03` | **Combined Over 6.5 runs** | `LEAN` | MEDIUM | P095-TOTAL | PRIMARY_FORMAL | LIKELIHOOD RANK ONLY | Low 7-run threshold relative to current scoring baseline; Martinez sample/length uncertainty; both teams possess ordinary relief/contact paths and extras can add tail mass | Buchanan dominates Fubon, Martinez repeats 5–6 quality innings, and rested bullpens preserve a 3-2/4-2 game | NOT_GENERATED / NOT PUBLISHED |
| **2** | `P095-C01` | **TSG Hawks ML** | `LEAN` | MEDIUM | P095-SIDE | PRIMARY_FORMAL | LIKELIHOOD RANK ONLY | Established starter advantage with Buchanan, better second-half offense and slightly better second-half pitching baseline | Fubon home/full-season edge plus Martinez’s competent start; Buchanan’s prior Fubon/contact-cluster branch produces a narrow home win | NOT_GENERATED / NOT PUBLISHED |
| **3** | `P095-C02` | **Fubon Guardians ML** | `FORCED RANK` | MEDIUM-LOW | P095-SIDE | CORRELATED_SECONDARY | LIKELIHOOD RANK ONLY | Home field, better full-season record, recent second-half H2H edge and a viable Martinez/late-relief path | Buchanan suppresses the weaker current Fubon offense while TSG reaches Martinez after five innings | NOT_GENERATED / NOT PUBLISHED |
| **4** | `P095-C04` | **Combined Under 6.5 runs** | `FORCED RANK` | MEDIUM-LOW | P095-TOTAL | CORRELATED_SECONDARY | LIKELIHOOD RANK ONLY | Buchanan’s 2.48 ERA, Martinez’s good first start, rest/freshness and Fubon’s weak current offense make 2-1/3-2/4-2 credible | Only seven runs beat the line; TSG’s current offense, Martinez’s limited sample, Buchanan’s hit-cluster tail or one relief/extra-inning event can push the game over | NOT_GENERATED / NOT PUBLISHED |

### Ranking audit

- **#1 remains LEAN, not SUPPORTED** because the current official batting orders were not verified and the total sits near the centre rather than in a protected alternate corridor.
- **Over/Under 6.5 are exact complements** under normal matching terms; there is no overlap and no push. The Over receives the narrow edge because seven runs is below the raw second-half combined scoring baseline and the upper branches are ordinary, while starter/rest evidence keeps the gap small.
- **Side pair is near-tied:** Hawks ML is preferred because Buchanan’s current established quality and TSG’s second-half offense are more event-specific than Fubon’s broader full-season edge. Fubon remains a real home-win branch.
- No historical D0 outcome is used as a vote or fitted probability.

### Potential winner

**TSG Hawks — `LEAN` (thin).**

The winner lean is driven primarily by Buchanan’s established starter quality and TSG’s better current second-half offensive output. Fubon’s home field, better full-season record, Martinez’s solid first CPBL start, and Buchanan’s one earlier loss to Fubon prevent stronger language.

### Integrity / limitations

- Current official batting orders were not verified at cutoff.
- Operator was not supplied; moneyline tie/refund/action and shortened-game treatment are `UNKNOWN_DEFINITION`.
- No calibrated CPBL probability exists; no numerical model has run.
- No odds were supplied: `NO VALUE DETERMINABLE`.
- Weather is contextual only; 10% rain does not create a total direction.
- Bullpen rest is availability evidence, not performance evidence.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-096`.


---

## P-096 — Rakuten Monkeys @ CTBC Brothers, CPBL regular season — PREGAME FORECAST

**View ID:** `P-096/V01`  
**Recorded / evidence cutoff:** 2026-08-26, final pre-issue refresh before the scheduled 18:35 CST / 20:35 Australia/Melbourne first pitch  
**Official event:** CPBL 2026 regular season GAME 288  
**Venue:** Taipei Dome, Taipei  
**GAME-STATE:** `PREGAME — OFFICIAL CPBL ADVANCED-STATS PAGE: 比賽準備中 / 未開始` at the final refresh.  
**Method:** MDS-2026.08.26-v2.2 qualitative champion.  
**Numerical state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`; NTS-2026.08.25-v0.2 remains Stage 0/pre-fit.  
**Candidate origin:** `USER_SUPPLIED`.  
**Operator / odds:** NOT SUPPLIED. Exact moneyline tie/refund/action, shortened-game and void terms remain `UNKNOWN_DEFINITION`; no value/EV/ROI/staking claim is permitted.

### Queue / retrospective gate

Previously issued same-evening NPB/KBO/cricket/CPBL records had not been demonstrated final during this pass and remain open/live as applicable. No open event was graded from a stale or incomplete source.

D0 / promoted-process controls transferred here only as process checks: starter length must be separated from run quality; bullpen workload predicts availability rather than performance; low totals do not imply close margins; recent scoring results are diagnostic only; and the full starter/lineup/contact/bullpen chain must control over generic H2H or streak language.

### Target / contract freeze

**Target A — `P096-MATCH-RESULT-v1`:** official CPBL full-game result from pregame start through the competition-authorised endpoint. Research interpretation uses outright win for moneyline; sportsbook tie/refund treatment is unknown because the operator was not supplied.

- `P096-C01`: **Rakuten Monkeys ML** — research outcome = Rakuten outright win.
- `P096-C02`: **CTBC Brothers +1.5 runs** — WIN if CTBC wins/ties or loses by exactly one under standard research run-line geometry; operator-specific tie/action terms unknown.

These two contracts are **not exact opposites**. A one-run Rakuten win can make both C01 and C02 winners.

**Target B — `P096-GAME-RUNS-v1`:** combined official runs by both teams through the full-game endpoint under standard research treatment.

- `P096-C03`: **Over 7.5** — WIN at 8+ combined runs.
- `P096-C04`: **Under 7.5** — WIN at 0–7 combined runs.
- These are exact complements under matching normal settlement terms; no push exists at 7.5.

### Volatile facts / participants

- Official CPBL advanced-stats GAME 288 page: Rakuten Monkeys @ CTBC Brothers, Taipei Dome, 2026-08-26, still `比賽準備中 / 未開始` at the final refresh.
- Same-day reporting identifies the starters as **Tseng Chia-hui (Rakuten)** versus **Wu Li-chen (CTBC)**.
- Tseng: **5-1, 2.90 ERA** in 16 appearances; versus CTBC in 2026: **2-0, 0.96 ERA** across four appearances.
- Wu: **3-4, 5.61 ERA** in 15 appearances; versus Rakuten in 2026: **1-0, 4.82 ERA** across four appearances.
- **Official posted batting order:** `NOT AVAILABLE / NOT VERIFIED FROM CONTROLLING OFFICIAL SOURCE AT CUTOFF`. This prevents any row from receiving `SUPPORTED`.

### Team / standings context

Same-day pregame table:
- **Second half:** Rakuten 16-12 (.571), CTBC 17-16 (.515).
- **Full season:** Rakuten 40-46-2 (.465), CTBC 37-53-2 (.411).

The second-half records are relatively close; the event-specific starter matchup is therefore more decisive than standings alone.

The CPBL standings page also shows Rakuten ahead 3-2 in the current second-half head-to-head split entering the game. This is contextual only and is not used as a raw probability.

### Previous-night process and bullpen usage

Official CPBL game data from 25 August: **Rakuten 11, CTBC 1**.
- Rakuten starter Aposhian(?) / official listed starter worked **7.0 IP, 93 pitches, 1 ER**; Rakuten then used only two relievers for 19 and 13 pitches.
- CTBC starter Lo? / official listed starter worked **5.0 IP, 101 pitches, 5 ER**; CTBC then used four relief arms. **Wei Shuo-cheng threw 45 pitches**, **Wu Chun-wei 22**, and another position-player/low-leverage inning was required.
- The previous result is not treated as a trend vote. Its transferable mechanism is that Rakuten's ordinary relief availability is cleaner, while CTBC's middle-relief alternatives are more constrained tonight.

### Starter / run-process branches

**Rakuten starter branch:** Tseng has the clearly superior current run-prevention line and the best specific matchup evidence on the card (0.96 ERA vs CTBC). His central branch is 5–7 effective innings with CTBC held to a low-to-moderate run contribution. The ordinary kill path is that CTBC's offense has shown high-scoring capability elsewhere and a single contact/HR cluster can defeat an ERA-led centre.

**CTBC starter branch:** Wu's 5.61 season ERA and 4.82 matchup ERA create a materially wider early-run and early-hook branch. His best case is that his prior win over Rakuten reflects a workable matchup and he gets through five or six with ordinary damage. His kill path is early traffic that forces CTBC into the more-worked middle relief.

**Bullpen branch:** Rakuten's late chain is relatively cleaner from the previous night; CTBC's middle relief has more workload uncertainty. This is availability evidence only, not a deterministic performance downgrade.

**Venue/environment:** Taipei Dome removes ordinary outdoor rain/wind effects from the run model; no generic outdoor weather direction is applied.

### Relevant 2026 matchup evidence — diagnostic only

Recent sampled Rakuten–CTBC finals include:
- 9-6 Rakuten (15 total)
- 5-3 Rakuten (8)
- 1-2 CTBC (3)
- 4-2 Rakuten (6)
- 11-1 Rakuten on 25 Aug (12)

This wide spread is used to preserve both low- and high-scoring branches, not to form a raw Over hit rate.

### Qualitative scenario map

**Lower scoring:** Tseng reproduces his strong CTBC matchup, Wu limits traffic better than his season ERA, and CTBC's rested leverage arms avoid the stressed middle-relief branch -> approximately **5–7 combined runs**; favors Under 7.5 and CTBC +1.5 if close.

**Central:** Tseng keeps CTBC around 2–3 runs while Rakuten scores 4–6 across Wu plus relief -> approximately **7–9 combined runs**, with Rakuten holding the side edge.

**Upper/contact branch:** Wu is hooked early and CTBC's middle relief inherits traffic; Rakuten reaches 6+, while CTBC contributes enough against Tseng/late relief -> **10+**; favors Over.

**Rakuten winner / separation branch:** Tseng gives the clear starter edge and Rakuten's offense again reaches CTBC's starter/bullpen chain -> Rakuten by 2+; defeats CTBC +1.5.

**Narrow Rakuten branch:** Tseng wins the run-prevention battle but CTBC's bullpen limits damage -> Rakuten by exactly one; **both Rakuten ML and CTBC +1.5 win**.

**CTBC upset branch:** Wu provides his good tail, CTBC creates a starter contact cluster against Tseng and the home side's later innings decide a close game.

### Frozen unique ranking

| Rank | Candidate | Contract | Verdict | Evidence quality | Dependence group | Performance role | Actionability | Main mechanism | Strongest ordinary kill path | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | `P096-C01` | **Rakuten Monkeys ML** | `LEAN` | MEDIUM-HIGH | P096-SIDE | PRIMARY_FORMAL | LIKELIHOOD RANK ONLY | Large starter-quality/matchup edge for Tseng, cleaner recent bullpen availability, modestly better current/full-season baseline | CTBC creates an early contact cluster against Tseng while Wu lands in his better tail and home relief protects the lead | NOT_GENERATED / NOT PUBLISHED |
| **2** | `P096-C02` | **CTBC Brothers +1.5** | `LEAN` | MEDIUM | P096-SIDE | CORRELATED_SECONDARY | LIKELIHOOD RANK ONLY | Positive run cushion survives any CTBC win and a one-run Rakuten win; CTBC remain competitive in second-half record and own home batting entitlement | Tseng suppresses CTBC and Wu/strained middle relief allow Rakuten to separate by 2+ | NOT_GENERATED / NOT PUBLISHED |
| **3** | `P096-C03` | **Combined Over 7.5** | `LEAN` | MEDIUM | P096-TOTAL | PRIMARY_FORMAL | LIKELIHOOD RANK ONLY | Wu's 5.61 ERA, 4.82 matchup ERA, early-hook risk and CTBC middle-relief workload create an ordinary 8+ branch even if Tseng pitches well | Tseng dominates and Wu gives a competent five-plus innings, producing 4-2/5-2/4-3 | NOT_GENERATED / NOT PUBLISHED |
| **4** | `P096-C04` | **Combined Under 7.5** | `FORCED RANK` | MEDIUM-LOW | P096-TOTAL | CORRELATED_SECONDARY | LIKELIHOOD RANK ONLY | Tseng's 2.90 season ERA and 0.96 matchup ERA can suppress CTBC enough for a 4-2/5-2 type game; dome removes weather volatility | Eight runs are enough to lose; Wu plus more-constrained CTBC middle relief can produce the required upper run contribution without CTBC scoring heavily | NOT_GENERATED / NOT PUBLISHED |

### Ranking audit

- **#1 is LEAN, not SUPPORTED:** current official batting orders were not verified and the game still contains a normal CTBC upset branch.
- **Side geometry:** Rakuten ML and CTBC +1.5 overlap on a one-run Rakuten win. This overlap is explicitly disclosed and the rows are not treated as independent evidence.
- **Total geometry:** Over 7.5 and Under 7.5 are exact complements under matching normal terms. Over receives only a narrow edge because the Wu/CTBC-relief upper branch offsets Tseng's strong run-suppression centre.
- **No result from yesterday is treated as proof of persistence.** Yesterday's 11-1 score informs participant/workload and failure-path structure only.

### Potential winner

**Rakuten Monkeys — `LEAN`.**

The winner lean is driven by the event-specific starter mismatch: Tseng's 2.90 ERA and 0.96 mark against CTBC versus Wu's 5.61/4.82 profile. Rakuten also enter with the better full-season winning percentage and a cleaner previous-night bullpen workload. CTBC's home setting, relatively competitive second-half record, and the unverified current batting orders keep the winner below `SUPPORTED`.

### Integrity / limitations

- Current official batting orders were not verified before cutoff.
- Operator was not supplied; moneyline tie/refund/action and shortened-game treatment are `UNKNOWN_DEFINITION`.
- No calibrated CPBL probability exists; no numerical model ran.
- No odds were supplied: `NO VALUE DETERMINABLE`.
- H2H and yesterday's blowout are diagnostic/process evidence only.
- Bullpen workload informs availability, not guaranteed performance.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-097`.


---

## P-097 — Wei-Chuan Dragons @ Uni-President 7-ELEVEn Lions, CPBL regular season — PREGAME FORECAST

**View ID:** `P-097/V01`  
**Recorded / evidence cutoff:** 2026-08-26 approximately 20:26 Australia/Melbourne / 18:26 CST, final pre-issue refresh before the scheduled 18:35 CST / 20:35 Australia/Melbourne first pitch  
**Official event:** CPBL 2026 regular season GAME 289  
**Venue:** Tainan Asia-Pacific International Baseball Stadium ("亞太主"), Tainan  
**GAME-STATE:** `PREGAME — OFFICIAL CPBL ADVANCED-STATS PAGE: 比賽準備中 / 未開始` at the final refresh.  
**Method:** MDS-2026.08.26-v2.2 qualitative champion.  
**Numerical state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`; NTS-2026.08.25-v0.2 remains Stage 0/pre-fit.  
**Candidate origin:** `USER_SUPPLIED`.  
**Operator / odds:** NOT SUPPLIED. Exact moneyline tie/refund/action, shortened-game and void terms remain `UNKNOWN_DEFINITION`; no value/EV/ROI/staking claim is permitted.

### Queue / retrospective gate

Previously issued same-evening NPB, KBO, cricket and CPBL records were not demonstrated final in this pass and remain open/live as applicable. No open event was graded from stale or incomplete information.

D0/promoted-process controls transferred only as process checks: starter run quality and expected length are distinct; bullpen workload predicts availability rather than performance; current participants/process outrank raw recent scores; recent suppression must retain contact/HR/early-hook tails; and full-game side/total contracts derive from one coherent qualitative run/margin corridor.

### Target / contract freeze

**Target A — `P097-MATCH-RESULT-v1`:** official CPBL full-game result state from pregame through the competition-authorised endpoint. CPBL regular-season ties remain possible after the permitted extra-inning/tiebreak endpoint; because no operator was supplied, sportsbook tie/refund treatment is `UNKNOWN_DEFINITION`.

- `P097-C01`: **Wei-Chuan Dragons ML** — research outcome = Dragons outright win.
- `P097-C02`: **Uni-President Lions ML** — research outcome = Lions outright win.
- These moneyline win events are mutually exclusive, but a league tie can leave neither research outcome as a win; operator refund/settlement treatment is unknown.

**Target B — `P097-GAME-RUNS-v1`:** combined official runs by both teams through the full-game endpoint under standard research treatment.

- `P097-C03`: **Over 7.5** — WIN at 8+ combined runs.
- `P097-C04`: **Under 7.5** — WIN at 0–7 combined runs.
- These totals are exact complements under matching normal settlement terms; no push exists at 7.5.

### Volatile facts / starters / lineups

- Official CPBL GAME 289 page: Wei-Chuan Dragons @ Uni-President 7-ELEVEn Lions, 2026-08-26 at Asia-Pacific Stadium, still `比賽準備中 / 未開始` at final refresh.
- Same-day pregame reporting identifies the starters as **Bryan Woodall (伍鐸), Wei-Chuan** vs **Lin Chao-en (林詔恩), Uni-Lions**.
- Woodall enters **2-5, 4.02 ERA** in 14 appearances; against Uni in 2026, **0-1 with a 4.41 ERA** across three appearances.
- Lin enters **3-3, 3.30 ERA** in 11 appearances; against Wei-Chuan, no decision with a **3.38 ERA** across two appearances.
- Woodall's latest indexed start on Aug 16: **5.1 IP, 9 H, 2 ER, 4 K, 101 pitches** against Rakuten. On Aug 2 he allowed **5 ER in 5.2 IP** against CTBC, showing a real contact-cluster/early-damage tail.
- **Official posted batting order:** `NOT AVAILABLE / NOT VERIFIED FROM CONTROLLING OFFICIAL SOURCE AT CUTOFF`. This caps every row below `SUPPORTED`.

### Current competition/team baseline

Official CPBL second-half table entering Aug 26:
- **Wei-Chuan:** 17-13 (.567), second place; **road 8-5**.
- **Uni-Lions:** 15-17 (.469), fourth; **home 8-11**.
- Full-season standings from same-day reporting: Wei-Chuan **56-34 (.622)**; Uni **44-46-1 (.489)**.

Official second-half team process:
- **Wei-Chuan pitching:** 30 G, 103 runs allowed, **2.80 ERA**, 1.27 WHIP, only 6 HR allowed.
- **Uni pitching:** 32 G, 111 runs allowed, **3.13 ERA**, 1.26 WHIP, 12 HR allowed.
- **Wei-Chuan offense:** 30 G, **105 runs**, .307 OBP, .315 SLG, .234 AVG.
- **Uni offense:** 32 G, **115 runs**, .334 OBP, .342 SLG, .271 AVG.

Those translate to a descriptive scoring baseline of roughly **3.50 Wei-Chuan runs/game and 3.59 Uni runs/game** in the current half, while both pitching staffs have allowed roughly 3.4–3.5 actual runs/game. This is a baseline only, not a fitted forecast.

### Recent state / bullpen availability

- The scheduled Aug 25 Wei-Chuan–Uni game at the same venue was **postponed by rain**, so neither club carried a normal previous-night pitching workload into this contest.
- Wei-Chuan's most recent completed game was a **3-2, 10-inning win over Fubon on Aug 23**. That game required late relief, but the subsequent rest/postponement materially improves current availability.
- Uni's most recent completed game was an **11-1 loss to CTBC on Aug 23** in which starter Hu Chih-wei allowed five earned runs in 0.2 IP. That result is not transferred as a current run-rate prior because today's starter is Lin Chao-en and the club has had rest.
- Bullpen freshness is therefore treated mainly as **availability**, not proof either bullpen will perform well.

### Matchup history — diagnostic only

Recent 2026 Wei-Chuan–Uni finals span both tails, including:
- Uni 11-6 Wei-Chuan (17 total)
- Wei-Chuan 3-0 Uni
- Uni 4-1 Wei-Chuan
- Uni 2-1 Wei-Chuan
- Wei-Chuan 5-3 Uni
- Uni 7-5 Wei-Chuan
- Wei-Chuan 2-0 Uni
- Wei-Chuan 1-0 Uni
- Wei-Chuan 8-7 Uni
- Uni 6-1 Wei-Chuan

The current second-half table shows Uni **3-1** against Wei-Chuan in the half to date. This is context only; it does not override the large full-season team-strength gap or current starter/bullpen evidence.

### Environment

Same-day reporting listed the outdoor Asia-Pacific venue around **28–29°C with ~30% rain probability**. Yesterday's same matchup was postponed by rain. No automatic Over/Under adjustment is made: potential delay/wet-ball effects are bidirectional and no current official delay was posted at cutoff.

### Qualitative run/margin scenario map

**Lower scoring:** Lin works 6+ effective innings, Woodall avoids the contact cluster, and both rested bullpens perform to the stronger current-half staff profiles -> approximately **4–6 combined runs**; favors Under 7.5.

**Central:** Lin gives Uni a modest starter edge, Woodall allows 2–4, and Wei-Chuan's bullpen limits late damage while the Dragons score 2–4 against Lin/relief -> approximately **6–8 combined runs**, with a very narrow Uni side edge.

**Upper/contact branch:** Woodall's hit/contact tail appears early, Uni creates a multi-run inning, and Wei-Chuan's stronger overall club answers against Lin/late relief -> **9+ combined runs**; favors Over.

**Wei-Chuan winner branch:** the league-leading overall club converts its superior full-season depth and stronger current-half pitching into a close road win after surviving Woodall's innings.

**Uni winner branch:** Lin outperforms Woodall, Uni's better current-half OBP/AVG creates more traffic, and the home club protects a narrow lead with its rested relief chain.

**Tie branch:** a close low-scoring game remains level through regulation/extra-inning process; neither research moneyline outcome becomes an outright win, with sportsbook treatment unknown.

### Frozen unique ranking

| Rank | Candidate | Contract | Verdict | Evidence quality | Dependence group | Performance role | Actionability | Main mechanism | Strongest ordinary kill path | Probability state |
|---:|---|---|---|---|---|---|---|---|---|---|
| **1** | `P097-C04` | **Combined Under 7.5 runs** | `LEAN` | MEDIUM-HIGH | P097-TOTAL | PRIMARY_FORMAL | LIKELIHOOD RANK ONLY | Both clubs' second-half staff ERAs are 3.13 or better; bullpens are rested after the postponement; current-half combined scoring baseline sits around 7.1 before matchup adjustment | Woodall's contact tail or one clustered relief inning creates 5+ Uni runs and forces the Dragons to answer, taking the game to 8+ | NOT_GENERATED / NOT PUBLISHED |
| **2** | `P097-C02` | **Uni-President Lions ML** | `LEAN` | MEDIUM | P097-SIDE | PRIMARY_FORMAL | LIKELIHOOD RANK ONLY | Lin has the better starter ERA/matchup line; Uni has the stronger current-half AVG/OBP/SLG and has gone 3-1 vs Wei-Chuan in the current half | Wei-Chuan's much stronger full-season record, 8-5 current-half road mark and superior 2.80 staff ERA overcome Woodall's weaker start | NOT_GENERATED / NOT PUBLISHED |
| **3** | `P097-C01` | **Wei-Chuan Dragons ML** | `FORCED RANK` | MEDIUM | P097-SIDE | CORRELATED_SECONDARY | LIKELIHOOD RANK ONLY | Wei-Chuan are 56-34 overall, 17-13 in the half, 8-5 on the road and own the better current-half pitching staff | Lin wins the starter matchup and Uni's stronger current-half on-base/contact profile creates enough early lead for the rested home bullpen | NOT_GENERATED / NOT PUBLISHED |
| **4** | `P097-C03` | **Combined Over 7.5 runs** | `FORCED RANK` | MEDIUM-LOW | P097-TOTAL | CORRELATED_SECONDARY | LIKELIHOOD RANK ONLY | Woodall's 4.02 ERA / 4.41 matchup ERA and demonstrated hit-cluster tail create an ordinary 8+ branch; recent H2H includes several 8+ games | Lin and both rested bullpens keep scoring around 3-2, 4-2 or 4-3; only seven or fewer is required to beat the Over | NOT_GENERATED / NOT PUBLISHED |

### Ranking audit

- **#1 is LEAN, not SUPPORTED:** 7.5 is not a high alternate line, Woodall carries meaningful contact risk, and the current official batting orders were not verified.
- **Total geometry:** Over/Under 7.5 are exact complements under matching normal terms. The Under edge comes from the two current-half pitching profiles plus rest, not from a raw H2H Under streak.
- **Side pair is close:** Uni gets the narrow pregame edge because today's starter and current-half offense are more event-specific than the broad full-season record. Wei-Chuan's season strength and bullpen prevent the Lions from reaching SUPPORTED.
- **No H2H or last-game result is used as a mechanical vote.**
- **Weather remains conditional:** yesterday's postponement justifies vigilance, not a directional total assumption.

### Potential winner

**Uni-President 7-ELEVEn Lions — `LEAN` (thin).**

The winner lean is driven by Lin Chao-en's better current starter line, Uni's stronger current-half contact/on-base production and the current-half 3-1 matchup record. Against that, Wei-Chuan are clearly the stronger full-season club and own the superior current-half pitching staff, so this remains a narrow winner call rather than a high-confidence view.

### Integrity / limitations

- Current official batting orders were not verified before cutoff.
- Operator was not supplied; CPBL moneyline tie/refund/action and shortened-game treatment are `UNKNOWN_DEFINITION`.
- No calibrated CPBL probability exists; no numerical model ran.
- No odds were supplied: `NO VALUE DETERMINABLE`.
- The Aug 23 Uni 11-1 loss is not treated as current pitcher evidence because today's starter is different and the club has since rested.
- Bullpen rest informs availability, not guaranteed performance.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-098`.


---

## P-098 — Vietnam vs Thailand, ASEAN Hyundai Cup 2026 Final Leg 2 — PRE-KICKOFF-DATA VIEW

**View ID:** `P-098/V01`  
**Recorded / evidence cutoff:** 2026-08-26 approximately 23:01 Australia/Melbourne / 20:01 Hanoi  
**Competition:** ASEAN Hyundai Cup 2026, senior men's final, second leg  
**Venue:** Mỹ Đình National Stadium, Hanoi  
**Aggregate entering leg:** Vietnam lead **2-0** after winning the first leg 2-0 in Bangkok on 22 Aug 2026.  
**Scheduled start:** 20:00 Hanoi / 23:00 Australia/Melbourne.  
**GAME-STATE:** `SCHEDULED START CROSSED — KICKOFF NOT YET OBSERVED IN FINAL CURRENT FEEDS`. Current match pages still showed the fixture, confirmed lineups and no live score/minute/stat line at the freeze. No elapsed-match information enters this view. If later evidence shows kickoff occurred before this timestamp due feed lag, settlement must review prospective eligibility and any later analysis requires a distinct live view.

**Method:** MDS-2026.08.26-v2.2 qualitative champion.  
**Numerical state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`.  
**Operator / odds:** NOT SUPPLIED. Research market reference showed full-match goals 2.5 and total corners around 9.5; operator settlement/tie/provider terms unknown. `NO VALUE DETERMINABLE`.

### Identity, tie state and lineups

Official ASEAN competition sources confirm the senior men's two-legged final and Vietnam's 2-0 aggregate lead.

Current starting lineups at cutoff:

**Vietnam:** Patrik Lê Giang; Trương Tiến Anh, Phạm Xuân Mạnh, Nguyễn Thành Chung, Đoàn Văn Hậu, Nguyễn Văn Vĩ; Đỗ Hoàng Hên, Lê Phạm Thành Long, Nguyễn Hoàng Đức; Nguyễn Đình Bắc, Nguyễn Xuân Son.

**Thailand:** Kampon Pathomakkakul; Waris Choolthong, Nattapong Sayriya, Manuel Bihr, Oussama Thiangkham; Sarach Yooyen, Kakana Khamyok, Chaiyaphon Otton; Yotsakon Burapha, Teerasak Poeiphimai, Seksan Ratree.

Vietnam therefore retain an aggressive front structure but do not need to chase the leg. Thailand begin two goals behind on aggregate and must increase attacking exposure.

### Goal-process evidence

First leg: Thailand 0-2 Vietnam. Official ASEAN reporting states Thailand controlled significant stretches and created chances, but halftime remained **0-0**; Vietnam scored both goals in the second half.

Vietnam enter on a strong defensive run: their recent sequence includes 0-0 Singapore, 3-0 Indonesia, 3-1 Cambodia, 2-0 Malaysia, 2-0 Malaysia and 2-0 Thailand, with multiple clean sheets and several controlled first halves.

Thailand's recent tournament sequence includes 2-0 Malaysia, 1-0 Philippines, 2-0 Myanmar, 3-1 Singapore, 1-2 Singapore and 0-2 Vietnam.

Thailand have publicly emphasised the importance of an early goal. This raises first-half attack exposure, but Vietnam's 2-0 aggregate cushion reduces their own need to force tempo.

### Corner-process evidence

**Research line:** total corners approximately **9.5**.

Direct target-event evidence:
- First leg: Thailand won corners **6-3**; first-half corners **2-0 Thailand**.
- Vietnam vs Malaysia second leg: Vietnam won corners **11-7**, showing Vietnam can still generate corners while managing an aggregate lead.
- Thailand's sampled tournament corner counts: 2, 7, 7, 2, 2, 6.
- Vietnam's sampled tournament corner counts: 6, 7, 2, 4, 3, 11, 3.
- First-leg combined corners = **9**.

Today's strongest corner-specific state modifier is Thailand trailing 0-2 on aggregate, which should increase width, crosses, blocked crosses, defensive clearances and end-line events. Vietnam's transition attack remains the main counter-path to a Thailand corner edge.

### Frozen four-pick ranking

| Rank | Candidate | Exact contract | Verdict | Evidence quality | Dependence group | Main mechanism | Strongest ordinary kill path | Probability state |
|---:|---|---|---|---|---|---|---|---|
| **1** | `P098-C01` | **Full match Under 2.5 goals (90 + stoppage)** | `LEAN` | MEDIUM-HIGH | P098-GOALS | Vietnam can manage a 2-0 aggregate lead, have a strong clean-sheet run, and already held Thailand scoreless in Bangkok | An early Thailand goal makes the tie live; Vietnam then counterattack into space and the leg opens toward 2-1/2-2 | NOT_GENERATED / NOT PUBLISHED |
| **2** | `P098-C02` | **Thailand to record more regulation corners than Vietnam** | `LEAN` | MEDIUM | P098-CORNERS | Thailand must chase two aggregate goals; first leg produced a 6-3 Thai corner edge; direct width/cross/block/clearance pathway is present | Vietnam's home transition game produces repeated byline attacks/set pieces, as in their 11-corner second leg vs Malaysia | NOT_GENERATED / NOT PUBLISHED |
| **3** | `P098-C03` | **1st half Over 0.5 goals** | `LEAN` | MEDIUM-LOW | P098-GOALS | Thailand need an early goal and cannot afford another passive 0-0 half; Vietnam's front line can exploit transition space | First leg was 0-0 HT despite Thai pressure, and Vietnam can again absorb without forcing the match | NOT_GENERATED / NOT PUBLISHED |
| **4** | `P098-C04` | **Total corners Under 9.5 (90 + stoppage)** | `FORCED RANK` | MEDIUM-LOW | P098-CORNERS | First leg stopped at 9 and many sampled tournament matches stayed in high-single-digit corner totals | Thailand's desperation attack plus Vietnam counters create repeated corner-causing sequences; an early goal increases tempo | NOT_GENERATED / NOT PUBLISHED |

### User-supplied market directions

- **1st-half 0.5 goals:** preferred side = **Over 0.5**, narrowly.
- **Full-match 2.5 goals:** preferred side = **Under 2.5**, more strongly.

The first-half and full-match goal targets are linked but not interchangeable. A first-half goal can widen the later total distribution; a scoreless first half does not guarantee the full Under.

### Scenario map

**Controlled leg:** Vietnam defend compactly, Thailand hold territory without clinical finishing -> 0-0, 1-0, 0-1 or 1-1; helps Under 2.5 and can still support Thailand most corners.

**Early Thailand goal:** aggregate pressure rises sharply -> helps 1H Over, raises full-game Over risk and increases corner tempo.

**Early Vietnam goal:** Thailand would need three unanswered goals to force extra time -> strongest branch for Thailand corner volume and a more open goal tail.

**Scoreless halftime:** 1H Over loses, but Thailand's second-half pressure/corners can spike while Under 2.5 remains live.

### Potential winner

**Vietnam — `LEAN`.**

Vietnam are home, lead 2-0 on aggregate, enter on a strong winning/clean-sheet run and won the first leg away. The outright leg winner call is intentionally only a lean because Vietnam do not need to win this leg; a draw or narrow defeat still serves the tournament objective.

### Integrity / limitations

- Scheduled kickoff had just crossed, but no current feed at freeze displayed a scored live state or match clock. No live pace/possession/shot/corner state is inferred.
- If later evidence proves feed lag and kickoff had already occurred before this timestamp, provenance/performance eligibility must be reviewed at settlement.
- Corner provider/operator was not supplied; “more corners” and total-corner settlement use research-grade regulation definitions, with tie/void terms unknown.
- No calibrated soccer/corner probability model exists.
- No odds were supplied: `NO VALUE DETERMINABLE`.

**Result at append:** `OPEN — START CROSSED / KICKOFF NOT OBSERVED`.  
**Next canonical ID:** `P-099`.


---

## P-099 — Rotterdam Dockers vs Amsterdam Flames, European T20 Premier League 2026 — TOSS COMPLETE / PRE-FIRST-BALL VIEW

**View ID:** `P-099/V01`  
**Recorded / evidence cutoff:** 2026-08-26 approximately 23:15–23:2x Australia/Melbourne / 15:15–15:2x CEST  
**Competition:** European T20 Premier League 2026, Match 1, inaugural season  
**Venue:** Sportpark Duivesteijn / Voorburg Cricket Club, Voorburg, Netherlands  
**Scheduled start:** 15:15 CEST / 23:15 Australia/Melbourne  
**GAME-STATE:** `TOSS COMPLETE — SCHEDULED START CROSSED — NO SCORED DELIVERY VERIFIED`. Cricbuzz reported Rotterdam Dockers won the toss and elected to field. Multiple current score pages still showed 0/0 at 0.0 or “match yet to begin”; therefore Amsterdam are confirmed to bat first, but no live ball/score is used in this view.

**Method:** MDS-2026.08.26-v2.2 qualitative champion.  
**Numerical state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`; NTS-2026.08.25-v0.2 remains Stage 0/pre-fit.  
**Candidate origin:** `USER_SUPPLIED`; all four rows frozen.  
**Operator / odds:** NOT SUPPLIED. Shortened-match, abandonment, DLS/void and exact phase-settlement terms remain `UNKNOWN_DEFINITION`; `NO VALUE DETERMINABLE`.

### Queue / retrospective gate

Previously issued P-089 through P-098 were not demonstrated final in this pass and remain open/live as applicable. No settlement was manufactured from an incomplete source.

### Target / contract freeze

**Target A — `P099-AF-1INN-TOTAL-v1`:** Amsterdam Flames' first-innings runs from pre-first-ball until completion of their scheduled 20-over innings or earlier all-out/official innings termination.

- `P099-C01`: Amsterdam Flames 1st innings **Over 164.5** — WIN at 165+ runs.
- `P099-C02`: Amsterdam Flames 1st innings **Under 164.5** — WIN at 164 or fewer.
- Exact complements under normal full-innings settlement. If rain shortens the innings, operator treatment is unknown.

**Target B — `P099-AF-PP6-v1`:** Amsterdam Flames runs after the first **6 completed overs / 36 legal deliveries**, including extras under the official scorecard convention.

- `P099-C03`: first 6 overs **Over 40.5** — WIN at 41+.
- `P099-C04`: first 6 overs **Under 40.5** — WIN at 40 or fewer.
- Exact complements if the six-over phase is completed and settled.

The 6-over target and 20-over target are related but are not interchangeable. A slow powerplay can be followed by acceleration; a fast powerplay can still be followed by a middle-over collapse.

### Identity, toss, squads and availability

- Official ETPL/Amsterdam fixture sources confirm the opening Dutch derby on 26 Aug at Voorburg.
- Cricbuzz live page: **Rotterdam Dockers won the toss and opted to field**.
- Amsterdam official squad includes Mitchell Marsh, Steve Smith, Tim David, Michael Bracewell, Scott Edwards, Bas de Leede, Curtis Campher, Max O'Dowd, Ajinkya Rahane and others.
- Rotterdam's squad includes Faf du Plessis, Heinrich Klaasen, Anrich Nortje, Sandeep Lamichhane, Logan van Beek, David Wiese, Roelof van der Merwe, Michael Levitt and others.
- **Confirmed playing XIs:** `NOT AVAILABLE / NOT VERIFIED FROM A CONTROLLING SOURCE AT CUTOFF`. Current live pages still exposed squads rather than a settled XI. This caps all verdicts below `SUPPORTED`.

### Strip / venue / weather gate

**STRIP STATUS:** `NOT FOUND AFTER SEARCH / SECONDARY REPORTS ONLY`.

Current match-specific secondary previews describe good pace/carry or a batting-friendly surface, generally placing first-innings expectations in the mid-150s to 160s. These are source reports, not an observed curator/official strip description, and are not treated as internally generated forecasts.

Historical venue evidence:
- Netherlands vs New Zealand, Voorburg, 4 Aug 2022: New Zealand **148/7**, powerplay **33/2**; contemporary reporting described a tricky, two-paced/uneven-bounce surface.
- Netherlands vs New Zealand, same venue, 5 Aug 2022: Netherlands **147/4** before New Zealand chased 149/2 in 14 overs.

This is four-year-old international evidence and is therefore down-weighted, not transferred mechanically to the inaugural 2026 ETPL strip. It does, however, prevent an unsupported assumption that 165+ is automatically a low target at Voorburg.

**MATCH CONDITIONS STATUS:** `CONFLICTING / MODERATE WEATHER UNCERTAINTY`. KNMI's day forecast carried material precipitation risk in parts of the Netherlands, while match-specific preview sites quoted much lower rain chances. No official match delay was posted at the freeze. Weather uncertainty widens shortened-match/void scenarios but is not assigned an automatic Over/Under direction.

### Batting and bowling process

Amsterdam have unusually high batting pedigree on the squad sheet: Marsh, Smith, Tim David, O'Dowd, Rahane, Edwards, de Leede, Bracewell and Campher provide multiple top/middle/death combinations.

Rotterdam counter with a high-quality, multi-phase bowling pool:
- Nortje / van Beek / Wiese or equivalent pace/new-ball options;
- Lamichhane / van der Merwe for middle-over spin;
- additional seam/all-round options.

Because the actual XI and bowling allocation are not confirmed, the forecast uses scenario branches rather than assuming every marquee player starts.

**Powerplay mechanism:** 40.5 requires 6.83 runs/over. Amsterdam's batting ceiling makes 41+ very ordinary if wickets are preserved, but Rotterdam can deploy high-end pace immediately and historical venue powerplays were not especially fast. This makes the first-six pair close, with a narrow Under edge.

**Full-innings mechanism:** 164.5 requires 8.25 runs/over. Amsterdam's middle/death firepower creates a real 175–190 ceiling, but the deeper Rotterdam attack and the venue's limited historical scoring evidence support a central range below that upper branch.

### Scenario map

**Lower/new-ball branch:** Rotterdam's quicks remove 1–2 top-order wickets, Amsterdam are ~32–39 after six and rebuild through overs 7–14 -> roughly **140–158**; helps C04 and C02.

**Central branch:** Amsterdam reach ~38–45 after six with 1 wicket down, middle overs are controlled by spin/pace changes, late hitting lifts them -> roughly **155–168**; full-innings threshold is near the top of this band.

**Upper batting branch:** Amsterdam preserve 8–9 wickets through 10–12 overs and Tim David/Marsh/Bracewell-type finishers receive clean exposure -> **175–195+**; helps C03/C01.

**Fast-start collapse:** Amsterdam clear 41 in the powerplay but lose 3–4 wickets across overs 7–13 -> C03 and C02 can both win.

**Slow-start recovery:** Amsterdam remain ≤40 after six but preserve wickets and dominate the death -> C04 and C01 can both win.

### Frozen unique ranking

| Rank | Candidate | Contract | Verdict | Evidence quality | Dependence group | Performance role | Main mechanism | Strongest ordinary kill path | Probability state |
|---:|---|---|---|---|---|---|---|---|---|
| **1** | `P099-C02` | **Amsterdam Flames 1st innings Under 164.5** | `LEAN` | MEDIUM | P099-FULL | PRIMARY_FORMAL | Strong Rotterdam multi-phase attack; older Voorburg T20 evidence around 147–148; 165 requires sustained 8.25 rpo across a first-ever league match | Amsterdam's marquee batting depth preserves wickets and overwhelms the death overs, reaching 175–190+ | NOT_GENERATED / NOT PUBLISHED |
| **2** | `P099-C04` | **Amsterdam Flames first 6 overs Under 40.5** | `LEAN` | MEDIUM-LOW | P099-PP | PRIMARY_FORMAL | Rotterdam can attack immediately with elite pace; 2022 venue powerplay evidence was restrained; possible cautious inaugural-match start | Amsterdam's top order attacks fielding restrictions cleanly and reaches 41 with no more than one wicket lost | NOT_GENERATED / NOT PUBLISHED |
| **3** | `P099-C03` | **Amsterdam Flames first 6 overs Over 40.5** | `FORCED RANK` | MEDIUM-LOW | P099-PP | CORRELATED_SECONDARY | 41 is only 6.83 rpo and Amsterdam's squad contains several high-class T20 top-order options | Nortje/van Beek/Wiese-type new-ball pressure plus one early wicket leaves the phase in the mid-30s | NOT_GENERATED / NOT PUBLISHED |
| **4** | `P099-C01` | **Amsterdam Flames 1st innings Over 164.5** | `FORCED RANK` | MEDIUM-LOW | P099-FULL | CORRELATED_SECONDARY | Amsterdam's batting ceiling is high enough for 175+ if wickets are preserved and secondary current pitch reports are correct | Rotterdam's deep attack prevents a clean acceleration path; even a 40+ powerplay can still finish 155–164 after middle-over wickets | NOT_GENERATED / NOT PUBLISHED |

### Ranking audit

- **No SUPPORTED row:** inaugural league, unverified XI, no observed exact strip and conflicting weather evidence materially limit confidence.
- The full-innings Under is preferred over the Over, but the 164.5 boundary remains close to the qualitative centre; this is not a strong low-scoring call.
- The first-six Under narrowly outranks its complement because the new-ball attack is the most reliable phase-specific mechanism available. It is weaker than the full-innings Under.
- Powerplay and full-innings targets remain separate; no phase outcome is treated as deterministic evidence for the full innings.

### Potential winner

**Rotterdam Dockers — `FORCED WINNER — LOW CONFIDENCE`.**

Rotterdam gain the toss/chase configuration and possess a deep bowling attack capable of keeping Amsterdam below a premium first-innings total, while their batting squad includes Faf du Plessis, Heinrich Klaasen, Michael Levitt, Mitchell Owen, Donovan Ferreira and David Wiese. Amsterdam's batting/all-round depth is at least as formidable, and confirmed XIs are missing, so the winner is intentionally not elevated to a normal LEAN.

### Integrity / limitations

- Toss verified; Amsterdam bat first.
- No scored delivery verified at the final state refresh.
- Confirmed playing XIs unavailable at cutoff.
- Exact strip not observed; current surface descriptions are secondary reports.
- Weather sources conflict; no directional weather adjustment.
- Operator/odds absent; shortened-match and phase settlement unknown.
- No calibrated numerical model exists and no probabilities are published.

**Result at append:** `OPEN — TOSS COMPLETE / PRE-FIRST-BALL`.  
**Next canonical ID:** `P-100`.


---

## P-100 — Apollon Limassol Women vs FH Hafnarfjordur Women, UEFA Women's Europa Cup 2026/27 — PREGAME FORECAST

**View ID:** `P-100/V01`  
**Recorded / evidence cutoff:** 2026-08-27 approximately 00:4x Australia/Melbourne / 2026-08-26 approximately 17:4x Cyprus local  
**Competition:** UEFA Women's Europa Cup 2026/27, first qualifying round, first leg  
**Venue:** Stelios Kyriakides Stadium, Paphos, Cyprus  
**Scheduled kickoff:** 2026-08-26 18:00 Cyprus local / 2026-08-27 01:00 Australia/Melbourne  
**GAME-STATE:** `PREGAME`. Official CFA/UEFA fixture sources and current score pages still showed the match before kickoff at the final refresh.

**Method:** MDS-2026.08.26-v2.2 qualitative champion.  
**Numerical state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`.  
**Candidate origin:** user requested goal directions and analyst-selected side/corner additions.  
**Operator / odds:** user did not supply an operator or prices. Same-day market pages were used only to verify that Apollon +0.5/double chance and the 2.5-goal family were offered; `NO VALUE DETERMINABLE`.

### Identity / competition / lineups

Official UEFA and Cyprus FA sources confirm:
- first qualifying round, first leg;
- return leg in Iceland on 2 Sep 2026;
- kickoff 18:00 local at Stelios Kyriakides Stadium.

Confirmed starting XIs from current match data:
- **Apollon 3-4-3:** Hara; Ficzay, Giannou, Georgiou; Mooney, Savva, Prvulovic, Pearse; Freda, Higgins, Hudson.
- **FH 4-5-1:** Gudlaugsdóttir; Linnet, Smith, Sandoval, Björnsdóttir; Magnúsdóttir, Haraldsdóttir, Hauksdóttir, Errington, Snorradóttir; Halldórsdóttir.

Apollon's attacking core is materially strong:
- Krystyna Freda and Natasha Hudson each scored 17 domestic league goals in 2025/26.
- Freda has 3 goals across Apollon's two 2026/27 UEFA Women's Champions League matches.

FH's 2026 Icelandic league profile is also strong overall, but current attacking personnel are less complete:
- FootyStats lists Ída Marín Hermannsdóttir as FH's current league top scorer with 7.
- She does not appear in the current UEFA squad list.
- Nia Christopher, another leading FH scorer, is on the bench rather than starting.

### Goal-process evidence

Apollon's two recent 2026/27 UEFA matches:
- Apollon 3-3 Czarni Sosnowiec after 90 minutes; halftime 2-2.
- Vllaznia 1-1 Apollon after 90 minutes; Vllaznia scored in the 6th minute, with Apollon eventually winning 2-1 after extra time.

So both recent European matches had at least one first-half goal; one of two cleared 2.5 in regulation.

FH's recent Icelandic league results:
- 0-1 vs Vikingur — HT 0-1
- 0-3 vs Breidablik — HT 0-2
- 6-4 at Fram — HT 2-1 to FH
- 2-2 at IBV — HT 2-0 to FH
- 7-3 vs Stjarnan — HT 4-1

All five had a first-half goal. Three of five cleared 2.5 full-match goals. Across the 16-match league season, FH had scored 52 and conceded 29, confirming a high-event domestic scoring environment, though competition strength/regime differ from UEFA qualifying.

### Corner-process evidence

Corner analysis is kept separate from goals.

Verified / source-backed corner evidence:
- UEFA records **17 Apollon corners across two 2026/27 UWCL matches**.
- APWin reports those matches averaged **14.5 total corners**, with Apollon averaging **8.5 for** and **6.0 against**.
- FH-specific recent corner data are less clean and provider-consistent; some secondary team pages conflict on opponent/date mapping.
- Direct cross, blocked-cross, end-line-entry and clearance data for this exact matchup were not available.

Because the direct corner-causing chain is incomplete, the corner selection is capped at **FORCED RANK / MEDIUM-LOW evidence** under the active soccer derivative-market rule.

### Frozen four-pick ranking

| Rank | Candidate | Contract | Verdict | Evidence quality | Dependence group | Main mechanism | Strongest ordinary kill path | Probability state |
|---:|---|---|---|---|---|---|---|---|
| **1** | `P100-C01` | **Apollon +0.5 / Apollon or Draw (90 + stoppage)** | `LEAN` | MEDIUM-HIGH | P100-SIDE | Home first leg, strong confirmed front three, Freda/Hudson scoring pedigree, FH current scoring personnel less complete | FH's strong Icelandic season translates cleanly to Europe and their midfield controls Apollon's wingback space | NOT_GENERATED / NOT PUBLISHED |
| **2** | `P100-C02` | **1st Half Over 0.5 Goals** | `LEAN` | MEDIUM-HIGH | P100-GOALS | Both recent Apollon European matches had a 1H goal; FH's last five league matches all had a 1H goal; both lineups contain direct attacking threats | First-leg caution produces a slow opening, FH's 4-5-1 blocks central access and Apollon avoid early risk | NOT_GENERATED / NOT PUBLISHED |
| **3** | `P100-C03` | **Full Match Over 2.5 Goals (90 + stoppage)** | `LEAN` | MEDIUM | P100-GOALS | Apollon's current European matches have produced 6 and 2 regulation goals; FH's domestic attack/defence profile is high-event; early-goal branches widen the match | The tie remains tactically conservative, FH's recent 0-1/0-3 scoring slump persists and Apollon win/manage 1-0 or 2-0 | NOT_GENERATED / NOT PUBLISHED |
| **4** | `P100-C04` | **Total Corners Over 9.5 (research-grade line, 90 + stoppage)** | `FORCED RANK` | MEDIUM-LOW | P100-CORNERS | Apollon's two recent UEFA matches averaged 14.5 total corners and Apollon themselves averaged 8.5; 3-4-3 wingback structure can generate width/set-piece pressure | Small two-match sample fails to transfer; FH sit deep without producing many own corners; direct cross/block/end-line evidence is incomplete | NOT_GENERATED / NOT PUBLISHED |

### User-supplied goal-market directions

- **1st Half O/U 0.5:** preferred side = **Over 0.5**.
- **Full Match O/U 2.5:** preferred side = **Over 2.5**.

These are separate targets. A first-half goal increases the chance of later game-state expansion but does not mechanically imply Over 2.5.

### Scenario map

**Low-event branch:** FH's 4-5-1 stays compact, Apollon control without forcing central entries -> 0-0 HT and 1-0/1-1/2-0 FT. Hurts both goal Overs.

**Central branch:** one first-half goal forces the trailing side to open, with both teams generating transition/set-piece opportunities -> approximately 2-3 total goals.

**High-event branch:** early Apollon breakthrough plus FH response, or FH score first and Apollon chase at home -> 3-5 total goals and elevated corners.

**Apollon control branch:** Freda/Higgins/Hudson exploit FH's defensive line, Apollon avoid defeat and can win narrowly.

**FH upset branch:** Icelandic match fitness and physical transition carry over, Apollon's wingbacks leave space and FH score first.

### Potential winner

**Apollon Limassol Women — `LEAN` (thin-to-moderate).**

Apollon are the potential winner because of:
- home first leg;
- confirmed high-output front line;
- strong recent European attacking evidence;
- FH's recent consecutive league losses;
- incomplete current FH scoring personnel relative to their domestic-season peak.

The winner remains only a lean because FH have had a strong 2026 Icelandic league season and this is the first head-to-head meeting.

### Integrity / limitations

- No calibrated soccer or corner probability model exists.
- No user-supplied prices: `NO VALUE DETERMINABLE`.
- Corner row is deliberately capped at FORCED RANK because direct cross/block/end-line/clearance evidence is incomplete.
- FH domestic stats are adjusted qualitatively for the different UEFA competition level.
- All supplied and selected contracts are regulation/90+stoppage unless otherwise stated.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-101`.


---

## P-101 — Germany Women vs Türkiye Women, international friendly — PREGAME FORECAST

**View ID:** `P-101/V01`  
**Recorded / evidence cutoff:** 2026-08-27 approximately 01:4x Australia/Melbourne  
**Competition:** Senior women's international preparation game for FIBA Women's Basketball World Cup 2026  
**Venue:** LANXESS Arena, Cologne, Germany  
**Scheduled tip:** 2026-08-27 17:00 CEST / 2026-08-28 01:00 Australia/Melbourne  
**GAME-STATE:** `PREGAME`.

**Method:** MDS-2026.08.26-v2.2 qualitative champion.  
**Numerical state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`.  
**Candidate origin:** `USER_SUPPLIED`.  
**Operator / odds:** NOT SUPPLIED; operator-specific regulation/OT and void terms remain `UNKNOWN_DEFINITION`. `NO VALUE DETERMINABLE`.

### Frozen contracts

- `P101-C01`: Germany -2.5 — Germany wins by 3+.
- `P101-C02`: Türkiye +2.5 — Türkiye wins outright or loses by 1–2.
- `P101-C03`: Combined Over 131.5 — 132+.
- `P101-C04`: Combined Under 131.5 — 131 or fewer.

### Availability / roster context

Germany's current preparation group includes Alexis Peterson, Luisa Geiselsöder, Emily Bessoir, Marie Gülich, Alexandra Wilke, Lina Sontag and others. Frieda Bühner, Leonie Fiebich, Satou Sabally and Nyara Sabally cannot join until the WNBA pause from 31 August.

Türkiye are without Alperi Onar (left-hand avulsion fracture) and Manolya Kurtulmuş. Kennedy/Beren Burke is not due to join in Germany until 28 August, after this game.

Germany's two official August tests: 60-65 Spain and 62-68 Hungary.
Türkiye's four published August preparation games: 63-51 Portugal, 56-44 Portugal, 76-77 Czechia, 62-52 Czechia.

### Scenario / ranking

| Rank | Contract | Verdict | Evidence | Central mechanism |
|---:|---|---|---|---|
| 1 | **Under 131.5** | LEAN | MEDIUM-HIGH | Current preparation scoring is mostly low; both teams lack major creators/scorers relative to full-strength World Cup rosters |
| 2 | **Germany -2.5** | LEAN | MEDIUM | Home court, FIBA rank 11 vs 16, deeper current structure, Türkiye missing Burke/Onar |
| 3 | **Türkiye +2.5** | FORCED RANK | MEDIUM | Türkiye are 3-1 in published prep and need only a one-possession loss |
| 4 | **Over 131.5** | FORCED RANK | MEDIUM-LOW | Friendly rotation/transition can widen scoring, but most current prep totals sit below the line |

### Potential winner

**Germany Women — LEAN.**

### Integrity

No calibrated basketball model ran. No user-supplied odds were provided. Friendly rotation/minutes uncertainty remains material.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-102`.


---

## P-102 — VfL Wolfsburg Women vs Inter Women, UEFA Women's Champions League 2026/27 — PREGAME FORECAST

**View ID:** `P-102/V01`  
**Recorded / evidence cutoff:** 2026-08-27 approximately 01:56 Australia/Melbourne / 2026-08-26 approximately 17:56 CEST  
**Competition:** UEFA Women's Champions League 2026/27, third qualifying round, league path, first leg  
**Venue:** AOK Stadion, Wolfsburg, Germany  
**Scheduled kickoff:** 2026-08-26 18:00 CEST / 2026-08-27 02:00 Australia/Melbourne  
**GAME-STATE:** `PREGAME`. Official Wolfsburg/UEFA pages still displayed the fixture pre-kickoff at the final refresh; official lineups were already published.

**Method:** MDS-2026.08.26-v2.2 qualitative champion.  
**Numerical state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`.  
**Candidate origin:** user supplied the two goal-market families; analyst added side and corner-race contracts.  
**Operator / odds:** user did not supply an operator or prices. Same-day market pages were used only to verify that the 1H 0.5, full-match 2.5, and match-result families were currently offered. `NO VALUE DETERMINABLE`.

### Identity / lineups / tie state

UEFA and club sources confirm this is the first leg of a two-legged third-round qualifying tie; the second leg is in Milan on 2 September.

**Wolfsburg 4-3-3:** Johannes; Bjelde, Carleer, Küver, Linder; Vallotto, Minge, Peddemors; Huth, Prašnikar, Zicai.

**Inter 4-4-2:** Rúnarsdóttir; Schough, Van Diemen, Andrés, Robustellini; Glionna, Tomašević, Vilhjálmsdóttir, Le Bihan; Raphino, Polli.

Wolfsburg are at home and retain an aggressive front three with Huth/Prašnikar/Zicai. Inter use two forwards but also a flat four-man midfield capable of protecting central space.

### Current competitive / process evidence

Wolfsburg:
- 2025/26 Bundesliga runners-up, **72 goals in 26 matches**, second-best attack in Germany.
- 2026 Supercup: lost **0-3 to Bayern**, with two first-half goals conceded (HT 0-2).
- 2026/27 Bundesliga opener: won **8-2 at Nürnberg** after trailing 0-2 at halftime; Nürnberg were reduced to ten in the 51st minute, so the eight-goal second-half explosion is not treated as an ordinary baseline.
- The current first XI closely resembles the group used in the Nürnberg/Bayern competitive matches.

Inter:
- 2025/26 Serie A runners-up, finishing 11 points behind Roma.
- Current 2026 sequence: **3-2 Grasshopper**, **1-0 Union Berlin**, **2-0 Newcastle**, **1-0 Parma**.
- First-half scoring in those four: Grasshopper 1-1 HT, Union 0-1 HT, Newcastle 0-1 HT, Parma 0-0 HT.
- Inter therefore arrive with a strong recent defensive sequence, but the opponent quality and competition context are materially different from Wolfsburg away in UWCL qualifying.

### Goal-process interpretation

**First-half 0.5:** both of Wolfsburg's current competitive matches contained at least one first-half goal; three of Inter's last four current matches also contained a first-half goal. Wolfsburg's high home attacking ceiling plus Inter's willingness to use two forwards supports an early-event branch. The kill path is first-leg caution and Inter's compact 4-4-2 producing a 0-0 half.

**Full-match 2.5:** Wolfsburg's 2025/26 attack produced 72 goals, and their two current competitive matches finished on 3 and 10 total goals. Inter's latest four matches finished on 5, 1, 2 and 1 total goals, so the away side brings a real suppression branch. Current market lines also strongly shade Over 2.5, but market prices are benchmark/context only and not internal probabilities. The central qualitative corridor is approximately 3-4 goals, with 2-0/2-1 and 3-0/3-1 branches prominent.

### Corner-process evidence

Corner target is modeled separately from goals.

Available direct/near-direct evidence:
- Wolfsburg's current structure uses Huth and Zicai as wide forwards, supported by full-backs Bjelde/Linder; home-favorite pressure can create crosses, blocked shots and defensive clearances.
- Inter's 4-4-2 can defend in two compact banks and funnel Wolfsburg attacks wide, which can increase Wolfsburg's corner share.
- Public current-season aggregate sources show both teams capable of meaningful shot volume, but provider-consistent current cross/block/end-line/clearance data are incomplete.
- Public corner aggregators disagree on recent totals and do not provide a sufficiently clean field-owned exact-match chain.

Therefore the selected corner row is **Wolfsburg to record more regulation corners than Inter**, but it is capped at `FORCED RANK / MEDIUM-LOW evidence`; tie/provider settlement is unknown.

### Frozen four-pick ranking

| Rank | Candidate | Contract | Verdict | Evidence quality | Dependence group | Main mechanism | Strongest ordinary kill path | Probability state |
|---:|---|---|---|---|---|---|---|---|
| **1** | `P102-C01` | **Wolfsburg ML (90 + stoppage)** | `LEAN` | MEDIUM-HIGH | P102-SIDE | Home first leg, stronger long-run club level, 72-goal 2025/26 attack, current aggressive XI, deeper European pedigree | Inter's recent clean-sheet/low-concession form transfers well; Rúnarsdóttir and compact 4-4-2 hold Wolfsburg to a draw or Inter counter into a win | NOT_GENERATED / NOT PUBLISHED |
| **2** | `P102-C02` | **1st Half Over 0.5 Goals** | `LEAN` | MEDIUM-HIGH | P102-GOALS | Both current Wolfsburg competitive games and 3/4 current Inter matches had a 1H goal; both lineups carry direct attacking threat | First-leg caution and Inter's defensive block slow the opening to 0-0 | NOT_GENERATED / NOT PUBLISHED |
| **3** | `P102-C03` | **Full Match Over 2.5 Goals (90 + stoppage)** | `LEAN` | MEDIUM | P102-GOALS | Wolfsburg's high scoring baseline and home pressure can produce 2-3 themselves; an early goal widens the tie | Inter's recent defensive form persists and the first leg settles 1-0/2-0/1-1 | NOT_GENERATED / NOT PUBLISHED |
| **4** | `P102-C04` | **Wolfsburg to record more regulation corners than Inter** | `FORCED RANK` | MEDIUM-LOW | P102-CORNERS | Home territorial edge, 4-3-3 width, Huth/Zicai/Bjelde/Linder cross and block pathways | Wolfsburg score early and reduce pressure; Inter's own wide counters/Glionna-Schough side generate enough corners, or corner count ties | NOT_GENERATED / NOT PUBLISHED |

### User-supplied goal-market directions

- **1st Half O/U 0.5:** preferred side = **Over 0.5**.
- **Full Match O/U 2.5:** preferred side = **Over 2.5**.

These are linked but not identical targets. A first-half goal raises the later open-game branch but does not guarantee three full-match goals.

### Scenario map

**Low-event branch:** Inter's compact block frustrates Wolfsburg, first half is 0-0, and the game ends 1-0/1-1/2-0 -> both goal Overs vulnerable.

**Central branch:** Wolfsburg score in the first half or early second half, Inter must leave more space, and the game reaches roughly 2-1/3-0/3-1 -> supports Wolfsburg ML and Over 2.5.

**Inter-resistance branch:** Rúnarsdóttir plus Van Diemen/Andrés absorb pressure and Inter counter through Raphino/Polli -> draw/upset branch; Wolfsburg ML vulnerable.

**Wolfsburg pressure branch:** sustained width creates repeated box entries, blocks and corners, with Huth/Zicai driving the territorial edge -> supports Wolfsburg corner race.

### Potential winner

**VfL Wolfsburg Women — `LEAN`.**

The winner lean is driven by home advantage, stronger established European level, a high-scoring domestic baseline and the current attacking XI. Inter's recent defensive sequence and first-leg tactical incentives prevent an upgrade to SUPPORTED.

### Integrity / limitations

- Official starting XIs were verified.
- User did not supply operator/odds; `NO VALUE DETERMINABLE`.
- No calibrated soccer/corner model exists.
- Corner row is deliberately capped at FORCED RANK because the direct cross/block/end-line/clearance evidence is incomplete.
- The 8-2 Nürnberg result is not treated as a normal scoring baseline because Nürnberg played with ten from the 51st minute.
- Market prices were used only as contract-availability/benchmark context, not as internal probability outputs.

**Result at append:** `OPEN — PREGAME`.  
**Next canonical ID:** `P-103`.

---

# Comprehensive pending-log settlement and retrospective sweep — 2026-08-27

**Sweep timestamp:** 2026-08-27 02:42 Australia/Melbourne.  
**Method:** MDS-2026.08.26-v2.2 qualitative champion.  
**Integrity boundary:** only verified completed events/targets are graded. LIVE events remain open. Issued ranks/reasoning are not rewritten. Contract outcome and process grade are separate. One result does not automatically change forecast weights.

## Sweep status

| ID | Verified state | Action |
|---|---|---|
| P-087 | **LIVE / Day 4 stumps** — Sri Lanka 229/6 in follow-on, lead 16 | Keep match-result target open; retain prior partial settlement only |
| P-088 | **FINAL** — Sikkim Boys 8-3 Howlers | Settle result/goal rows; corners UNSETTLEABLE after retry |
| P-089 | **FINAL** — Chunichi 4-0 Hanshin | Settle + retrospective |
| P-090 | **FINAL** — Nippon-Ham 9-1 Seibu | Settle + rank-1 audit |
| P-091 | **FINAL** — Orix 7-5 Rakuten | Settle + retrospective |
| P-092 | **FINAL** — KT 5-4 Doosan | Settle + dependence audit |
| P-093 | **FINAL** — LG 8-0 NC | Settle + retrospective |
| P-094 | **FINAL** — Surrey chased Yorkshire 171 | Settle + cricket phase audit |
| P-095 | **FINAL** — Fubon 5-4 TSG | Settle + **process-defect audit** |
| P-096 | **FINAL** — CTBC 2-0 Rakuten | Settle + rank-1 audit |
| P-097 | **FINAL** — Uni 1-0 Wei-Chuan | Settle + retrospective |
| P-098 | **FINAL** — Vietnam 2-2 Thailand | Settle + rank-1/tie-state audit |
| P-099 | **FINAL** — Rotterdam 158/5 chased Amsterdam 157/8 | Settle + cricket phase audit |
| P-100 | **LIVE** — latest retrievable 69:21, FH 2-0 | Skip settlement |
| P-101 | **PREGAME / FUTURE** | Keep open |
| P-102 | **LIVE** — latest retrievable 29:49, 0-0 | Skip settlement |

### Descriptive cleanup counts — not independent performance metrics

Across **P-088 through P-099**, the contract ledger is **28 WIN / 19 LOSS / 1 UNSETTLEABLE**. These rows are heavily dependent and include exact complements, nested totals and overlapping handicaps, so this is **not** model accuracy, calibration, edge, EV or ROI. Rank #1 was **8-4** descriptively; P-095 is process-defective and should not be used to validate its mechanism. No probability backfill is permitted.

---

## P-087 — India vs Sri Lanka, 2nd Test — live hold

**Current verified state:** Day 4 ended with Sri Lanka **229/6** in the follow-on, leading by **16 runs** after India 503/9d and Sri Lanka 290. The match-result target is still live and therefore remains unresolved.

| Rank | Candidate | Status |
|---:|---|---|
| 1 | India match win | **OPEN — MATCH LIVE** |
| 2 | Sri Lanka 1st innings Under 286.5 | **LOSS — previously completed at 290** |

**Action:** no full-match retrospective yet. The first-innings loss remains correctly recorded; it was caused by the explicitly identified Dinusha/tail-end extension branch.

**Source quality:** current Day-4 reports from Indian Express/Times of India plus live score reconciliation.

---

## P-088 — Howlers Sporting Singtam 3-8 Sikkim Boys FC

**Verified final:** Sikkim Boys won **8-3**. The Away End lists Howlers goals at 9', 57', 63' and Sikkim Boys goals at 7', 37', 45', 46', 58', 75', 78', 83'.

### Contract settlement

| Rank | Candidate | Frozen contract | Final | Outcome |
|---:|---|---|---|---|
| 1 | P088-C03 | Howlers or Draw — 1X | Sikkim Boys 8-3 | **LOSS** |
| 2 | P088-C02 | Over 2.5 goals | 11 goals | **WIN** |
| 3 | P088-C01 | 1H Over 0.5 | 5 first-half goals | **WIN** |
| 4 | P088-C04 | Over 7.5 corners | trustworthy final corner count not recovered | **UNSETTLEABLE** |

**Potential winner:** Howlers — **LOSS**.

### Rank-1 loss audit

The issued #1 thesis leaned on Howlers' better pregame record and Sikkim Boys' severe defensive leakage. Its own strongest kill path was that **Howlers' attacking weakness persisted and Sikkim Boys scored first / exploited transition errors**. Sikkim Boys scored first in the 7th minute and ultimately produced eight goals. The direction of Sikkim Boys' defensive weakness was real—Howlers still scored three—but it did not imply Howlers were the safer non-loss side in a high-volatility, low-information game.

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Howlers' relatively better record would make 1X most robust; 3+ goals likely | Sikkim Boys scored first and repeatedly exploited an open/unstable defensive game; total exploded to 11 | Side confidence was too strong relative to two-sided volatility; goal direction was sound | Unverified XI and extreme recent defensive variance were known limitations | **INCONCLUSIVE** | Sparse-participant / confidence calibration candidate | `PL2-GL-008` | **No forecast-weight change**; future low-info side rows require stronger participant/role evidence for SUPPORTED |

**Corner settlement note:** post-final retry found the fixture result but no trustworthy provider-consistent corner final. A stale TotalCorner row could not be reconciled to the verified 3-8 final. Per niche-stat policy, close P088-C04 as `UNSETTLEABLE`; do not keep the whole event open.

**Source:** The Away End SFA A Division results; TotalCorner post-final retry for niche stat.

---

## P-089 — Chunichi Dragons 4-0 Hanshin Tigers

### Contract settlement

| Rank | Contract | Outcome |
|---:|---|---|
| 1 | Under 8.0 | **WIN** — total 4 |
| 2 | Hanshin +0.5 | **LOSS** |
| 3 | Chunichi +1.5 | **WIN** |
| 4 | Over 6.0 | **LOSS** |
| — | Potential winner: Hanshin | **LOSS** |

### What happened

Hideaki Wakui produced the decisive suppression branch, working six scoreless innings. Hanshin starter Masashi Ito allowed the decisive Chunichi damage, including home-run/contact events, and Chunichi won without allowing a run. The top Under thesis was correct, but the side/winner inference was not.

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| 5-7-run central game, slight Hanshin side edge | Wakui shut down Hanshin; Chunichi separated 4-0 while staying well Under | Total centre was good; close-margin/winner branch was wrong | Chunichi home form and Hanshin separation failure path were known | **COMPLIANT** | None | `PL2-GL-002` | None; reinforce margin distribution independence |

---

## P-090 — Nippon-Ham Fighters 9-1 Seibu Lions

### Contract settlement

| Rank | Contract | Outcome |
|---:|---|---|
| 1 | Seibu +1.5 | **LOSS** |
| 2 | Under 7.5 | **LOSS** |
| 3 | Over 5.5 | **WIN** |
| 4 | Nippon-Ham +0.5 | **WIN** |
| — | Potential winner: Seibu | **LOSS** |

### Rank-1 loss audit

Kota Tatsu threw a complete game, allowing one run with ten strikeouts. Yutaro Watanabe was hit hard: 6 IP, 10 hits, 9 runs (8 earned), including two home runs. The preissue card correctly named a Nippon-Ham power/HR separation path, but it did not weight that tail enough against Seibu +1.5.

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Close, lower-scoring Seibu-leaning game | Tatsu dominated; Watanabe's contact/HR tail produced 9-run separation | The exact separation tail existed but was underweighted | HR/contact risk was knowable; magnitude was tail realization | **COMPLIANT** | None | Existing `C-PL2-BB-TAIL-STRESS`; `PL2-GL-003` | No immediate weight change |

---

## P-091 — Orix Buffaloes 7-5 Rakuten Eagles

### Contract settlement

| Rank | Contract | Outcome |
|---:|---|---|
| 1 | Orix +1.5 | **WIN** |
| 2 | Under 8.5 | **LOSS** |
| 3 | Over 6.5 | **WIN** |
| 4 | Rakuten +0.5 | **LOSS** |
| — | Potential winner: Orix | **WIN** |

### What happened

Orix starter Kyosuke Saito lasted only two innings and allowed five runs (three earned), validating the uncertainty branch. Crucially, Orix's bullpen then shut Rakuten out for the remainder while Orix erased the five-run deficit and won 7-5. The 12-run total was not simply “short starter = Over”; it required both early starter failure and a later Rakuten relief/defensive collapse.

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Orix +1.5 robust; 6-8 central with wide upper tail | Saito imploded early, Orix relief stabilized, Orix staged large comeback | Upper tail wider than central read; side cushion survived | Saito uncertainty was explicitly known | **COMPLIANT** | None | `PL2-GL-004` | None |

---

## P-092 — KT Wiz 5-4 Doosan Bears

### Contract settlement

| Rank | Contract | Outcome |
|---:|---|---|
| 1 | KT +1.5 | **WIN** |
| 2 | Under 10.5 | **WIN** |
| 3 | Doosan +1.5 | **WIN** |
| 4 | Over 8.5 | **WIN** |
| — | Potential winner: KT | **WIN** |

KT won **5-4 on a walk-off**. This landed exactly in the overlap geometry: KT by one makes **both +1.5 side contracts winners**, while a nine-run total makes **Over 8.5 and Under 10.5 both winners**.

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Close KT-leaning game around 8-10 total | One-run walk-off, nine total | Very close to central corridor | Overlap was explicitly mapped preissue | **COMPLIANT** | None | `PL2-GL-009` | None; preserve dependence-normalized reporting |

**Evaluation warning:** 4/4 is not four independent confirmations.

---

## P-093 — LG Twins 8-0 NC Dinos

### Contract settlement

| Rank | Contract | Outcome |
|---:|---|---|
| 1 | LG +1.5 | **WIN** |
| 2 | NC +1.5 | **LOSS** |
| 3 | Over 7.5 | **WIN** |
| 4 | Under 9.5 | **WIN** |
| — | Potential winner: LG | **WIN** |

LG starter Im Chan-kyu threw six scoreless innings. Austin Dean hit two home runs, Song Chan-ui also homered, and NC starter Koo Chang-mo allowed five runs. The event produced a large margin while still finishing inside the 8-9 overlapping-total band.

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Narrow LG edge, 8-10-run centre | LG shutout plus clustered HR damage created 8-0 | Margin tail was much wider than side centre; total corridor remained accurate | HR/separation branch was knowable | **COMPLIANT** | None | `PL2-GL-002`, `PL2-GL-009` | None |

---

## P-094 — Yorkshire Women 171; Surrey Women 172/8

**Verified innings/match:** Yorkshire **171 all out in 33 overs**; Surrey chased **172/8** to win by two wickets. Yorkshire were **34/0 after five overs**.

### Contract settlement

| Rank | Contract | Outcome |
|---:|---|---|
| 1 | Yorkshire first 5 overs Over 19.5 | **WIN** — 34/0 |
| 2 | Yorkshire 1st innings Over 225.5 | **LOSS** — 171 |
| 3 | Yorkshire 1st innings Under 225.5 | **WIN** |
| 4 | Yorkshire first 5 overs Under 19.5 | **LOSS** |
| — | Potential winner: Surrey | **WIN** |

The preissue scenario map explicitly contained **“fast start, middle collapse”**. That is almost exactly what occurred: the powerplay cleared comfortably, but wicket/resource loss terminated the innings far below 225.5.

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| First-five Over slight edge; full innings around 225 boundary | 34/0 after five, then all out 171 by 33 overs | Full-innings ceiling was too high, but phase separation was correctly represented | Collapse branch was explicitly known | **COMPLIANT** | None | `PL2-GL-005` | None; reinforce phase-specific wicket/resource modelling |

---

## P-095 — Fubon Guardians 5-4 TSG Hawks — **PROCESS DEFECT**

### Contract settlement

| Rank | Contract | Outcome |
|---:|---|---|
| 1 | Over 6.5 | **WIN** — total 9 |
| 2 | TSG ML | **LOSS** |
| 3 | Fubon ML | **WIN** |
| 4 | Under 6.5 | **LOSS** |
| — | Potential winner: TSG | **LOSS** |

### Critical identity correction

The official CPBL final record shows the actual starters were:

- **TSG: Cannan (坎南)** — 6 IP, 7 H, 4 ER.
- **Fubon: Matisse (瑪帝斯)** — 6 IP, 4 H, 1 ER.

The issued P-095 card instead built its starter analysis around **David Buchanan vs Quinton Martinez**. That is not ordinary forecast variance; it is a participant/source identity failure.

The official final also shows Fubon won 5-4, with Chang Yu-cheng homering and the game decided through the actual starter/bullpen chain.

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Over lean + TSG side lean based heavily on Buchanan/Martinez matchup | Actual starters were Cannan/Matisse; Fubon won 5-4 | Forecast mechanism was attached to the wrong participants | **Knowable and preventable** with final official starter verification | **PROCESS_DEFECT** | **PARTICIPANT/SOURCE IDENTITY** | `PL2-GL-001` | **Immediate integrity process lock only**; no forecast-weight change |

**Important:** the Over 6.5 **won**, but it is a *right contract outcome for a defective issued mechanism*. It cannot validate the starter reasoning or be used as evidence that the analysis was calibrated.

**Official source:** CPBL advanced game record `2026-A-290`.

---

## P-096 — CTBC Brothers 2-0 Rakuten Monkeys

### Contract settlement

| Rank | Contract | Outcome |
|---:|---|---|
| 1 | Rakuten ML | **LOSS** |
| 2 | CTBC +1.5 | **WIN** |
| 3 | Over 7.5 | **LOSS** |
| 4 | Under 7.5 | **WIN** |
| — | Potential winner: Rakuten | **LOSS** |

Tseng Chia-hui was excellent: **7 IP, 2 H, 0 R**. But Wu Li-chen matched/surpassed the suppression, throwing **7 scoreless innings with 7 strikeouts**. CTBC scored both runs in the eighth against Rakuten relief. The starter edge did not convert to the match winner because the game stayed 0-0 into the bullpen phase.

### Rank-1 loss audit

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Tseng edge + better current offense would give Rakuten ML the narrow advantage | Both starters scoreless; CTBC won the late bullpen phase 2-0 | Wu's small-sample “good tail” and tied-game relief leverage were underweighted | Uncertainty around Wu was known; exact 7-scoreless realization was not | **COMPLIANT** | None | Young/small-sample starter scenario + tied-game relief branch candidate | None |

**Official source:** CPBL game `2026-A-288`.

---

## P-097 — Uni-Lions 1-0 Wei-Chuan Dragons

### Contract settlement

| Rank | Contract | Outcome |
|---:|---|---|
| 1 | Under 7.5 | **WIN** |
| 2 | Uni-Lions ML | **WIN** |
| 3 | Dragons ML | **LOSS** |
| 4 | Over 7.5 | **LOSS** |
| — | Potential winner: Uni-Lions | **WIN** |

Lin Chao-en threw **6.1 scoreless innings**; Bryan Woodall allowed only one run in six. Both bullpens preserved the low-scoring state. This was close to the issued mechanism: Lin starter edge + rested bullpens + suppressed current-half scoring.

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| 6-8-run central, narrow Uni side edge | Uni won 1-0 through starter/bullpen suppression | Lower tail realized more strongly than centre | Fully within named lower branch | **COMPLIANT** | None | No new lesson | None |

**Official source:** CPBL game `2026-A-289`.

---

## P-098 — Vietnam 2-2 Thailand — Vietnam advance 4-2 aggregate

### Contract settlement

| Rank | Contract | Outcome |
|---:|---|---|
| 1 | Full-match Under 2.5 goals | **LOSS** — 4 goals |
| 2 | Thailand more corners than Vietnam | **WIN** — Thailand 4, Vietnam 3 |
| 3 | 1H Over 0.5 goals | **WIN** — Thailand led 1-0 at HT |
| 4 | Total corners Under 9.5 | **WIN** — 7 total |
| — | Potential match winner: Vietnam | **LOSS** — regulation draw 2-2 |

Vietnam still won the **tie/championship** 4-2 on aggregate, but the issued potential winner was a **match-winner** call, so it grades LOSS rather than being retrospectively relabelled “advance”.

Thailand scored in the **12th minute**, exactly activating the preissue Under's strongest kill path: the aggregate became live, forcing a more open score-state. Thailand later reached 2-0 before Vietnam recovered to 2-2.

### Rank-1 loss audit

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Vietnam could manage 2-0 aggregate lead; Under 2.5 strongest | Thailand scored early, reopening the tie; match expanded to 2-2 | Central aggregate-control branch was superseded by named early-goal regime switch | **Explicitly identified preissue** | **COMPLIANT** | None | `PL2-GL-006`, `PL2-GL-007` | None |

**Corner note:** Thailand's 4-3 corner edge supports the separate chasing-width mechanism, while only seven total corners shows why “Thailand must attack” cannot be mechanically converted into a high corner total.

---

## P-099 — Rotterdam Dockers 158/5 beat Amsterdam Flames 157/8

**Verified result:** Amsterdam **157/8**; Rotterdam **158/5 in 18.1 overs**, winning by five wickets. Cricbuzz records Amsterdam's mandatory powerplay as **56 runs**, with Amsterdam **56/2 after six overs**.

### Contract settlement

| Rank | Contract | Outcome |
|---:|---|---|
| 1 | Amsterdam 1st innings Under 164.5 | **WIN** — 157 |
| 2 | Amsterdam first 6 Under 40.5 | **LOSS** — 56 |
| 3 | Amsterdam first 6 Over 40.5 | **WIN** |
| 4 | Amsterdam 1st innings Over 164.5 | **LOSS** |
| — | Potential winner: Rotterdam | **WIN** |

Amsterdam reached **41/2 after four overs and 56/2 after six**, then finished only 157/8. This is another clean demonstration that powerplay scoring and full-innings output are separate targets. Bas de Leede's 75 anchored the innings, but Amsterdam did not receive enough finishing contribution to clear 164.5.

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Full-innings Under strongest; PP Under narrowly preferred | PP was much faster (56), but Rotterdam pulled scoring back to 157; chase completed in 18.1 | Full-innings process right; PP phase read wrong | Final XI/new-ball matchup uncertainty was known | **COMPLIANT** | None | `PL2-GL-005`; final-XI importance reinforced | None |

**Source:** ESPN/Cricbuzz official-style scorecards and over-by-over data.

---

## P-100 — Apollon Women vs FH Women — LIVE HOLD

**Latest verified retrievable state:** **69:21 — FH lead 2-0**, goals Helena Errington 37' and Andrea Hauksdóttir 43'.  
Per the user's live-event rule, **do not settle the event yet**. Move to the next pending record.

---

## P-101 — Germany Women vs Türkiye Women — PREGAME HOLD

Scheduled for **27 Aug 17:00 CEST / 28 Aug 01:00 Australia/Melbourne**. No settlement.

---

## P-102 — Wolfsburg Women vs Inter Women — LIVE HOLD

**Latest verified retrievable state:** **29:49 — 0-0**.  
Per the user's live-event rule, **do not settle the event yet**.

---

## Cleanup closeout

| Category | IDs |
|---|---|
| **Closed in this sweep** | P-088 through P-099 |
| **Still live/open** | P-087, P-100, P-102 |
| **Pregame/future** | P-101 |
| **Process-defective settled event** | P-095 |
| **Final unsettleable niche row** | P-088-C04 corners |
| **Next canonical ID** | `P-103` |

### Sport-reference additions from this sweep

**Baseball**
- Preserve an official final-starter identity gate (`PL2-GL-001`).
- Strengthen explicit 2+ separation stress branches for +1.5 contracts (`P-090`).
- Keep short-start exposure distinct from bullpen performance (`P-091`).
- Keep low-total and close-margin hypotheses separate (`P-089`, `P-093`).

**Cricket**
- Powerplay and innings totals must remain independent target objects. Wicket-resource transitions can completely reverse the apparent direction after six overs (`P-094`, `P-099`).

**Soccer**
- Two-leg aggregate models must branch immediately on an early trailing-team goal (`P-098`).
- Corners remain a separate target process: attacking necessity can alter corner share without necessarily creating a high total (`P-098`).
- Sparse local leagues with unverified XIs require confidence caps on side/double-chance claims (`P-088`).

**Model/training**
- No coefficients, calibrated probabilities, EV assumptions or staking rules are changed from these results. NTS remains Stage 0/pre-fit.

