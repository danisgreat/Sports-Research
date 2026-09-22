# Prediction Mini Running Log — P-318 Continuation

**Status:** SETTLEMENT-UPDATED LOCAL APPEND-ONLY MIRROR — P-318–P-332 SETTLED/ADMIN-CLOSED 2026-09-07  
**Started:** 2026-09-06 21:13 Australia/Melbourne  
**Source continuation:** `PREDICTION_MINI_RUNNING_LOG_P317(2).md`  
**Google Drive:** READ ONLY  
**Canonical Drive authority:** `PREDICTION_LOG_COMBINED_2.md`  
**Historical archive:** `PREDICTION_LOG_COMBINED.md` (`P-001`–`P-271`, closed)  
**Local next forecast slot:** **`P-333`**  
**Numerical state:** `NTS-2026.09.02-v0.3 — Stage 0 / pre-fit`  
**Probability state:** `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`  
**Market state:** `SPORTS_ONLY / MARKET_BLIND`

> This file is a new local continuation. Google Drive remains read-only.  
> No Drive file was edited in creating this continuation.  
> P-306–P-317 are preserved as already-issued local records and are **not renumbered** merely because the Drive canonical log has not yet imported them.  
> Before every new forecast, refresh the Drive controlling snapshot and reconcile event identity / canonical numbering without rewriting issued IDs.

---

# 2026-09-07 CONTROLLING SETTLEMENT / RETROSPECTIVE OVERLAY — P-318 TO P-332

**Settlement authority:** `MDS-2026.09.06-v4.0`, read fresh from Google Drive on 2026-09-07.  
**Drive status:** **READ ONLY — no Google Drive file was edited.**  
**Frozen-evidence rule:** every issued rank, probability, candidate, target, issue horizon and pre-game evidence block below remains immutable. This overlay changes only current queue/settlement state and appends retrospective evidence.  
**Canonical-ID reconciliation:** Drive's `PREDICTION_LOG_COMBINED_2.md` still says **next canonical ID = P-318**. The only Drive artifact already containing `P-318` onward is this same local continuation. Therefore **no genuine ID collision exists and no temporary settlement ID is allocated.** The local sequence `P-318`–`P-332` is retained for later canonical import.  
**Next local forecast slot:** `P-333`.

## Current queue state

| ID | Event | Current disposition |
|---|---|---|
| P-318 | Henan vs Chengdu Rongcheng | **FINAL / SETTLED** |
| P-319 | Yunnan Yukun vs Liaoning Tieren | **FINAL / SETTLED — start-crossed original-line view retained** |
| P-320 | Tianjin Jinmen Tigers vs Zhejiang | **FINAL / SETTLED** |
| P-321 | Sønderjyske vs AC Horsens | **FINAL / SETTLED** |
| P-322 | South Africa vs Zimbabwe | **FINAL / SETTLED — batting-first condition met** |
| P-323 | Everton vs Manchester United | **FINAL / SETTLED — EPL PRIMARY_SCORED** |
| P-324 | Valencia vs Barcelona | **ADMINISTRATIVE CLOSED / NO ACTIONABLE FORECAST ISSUED** |
| P-325 | Bangladesh Women vs Sri Lanka Women | **FINAL / SETTLED — Bangladesh batted first, condition met** |
| P-326 | Western Carolina @ Campbell | **ADMINISTRATIVE CLOSED / NO ACTIONABLE FORECAST ISSUED** |
| P-327 | Angers SCO vs Rennes | **FINAL / SETTLED** |
| P-328 | Arsenal vs Chelsea | **FINAL / SETTLED — EPL PRIMARY_SCORED** |
| P-329 | Bologna vs Sassuolo | **FINAL / SETTLED** |
| P-330 | Puerto Rico Women vs Belgium Women | **ADMINISTRATIVE CLOSED / NO ACTIONABLE FORECAST ISSUED** |
| P-331 | Milwaukee Brewers @ Cincinnati Reds | **FINAL / SETTLED — MLB PRIMARY_SCORED** |
| P-332 | Deportivo Alavés vs CA Osasuna | **FINAL / SETTLED** |

No P-318–P-332 sporting result remains open. Older inherited evidence/definition follow-ups remain governed by `PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md` and are not silently closed here.

---

## P-318 — Henan vs Chengdu Rongcheng

### Settlement
**Final:** Henan 0–0 Chengdu Rongcheng. **HT:** 0–0.  
Fresh secondary structured displays report **Henan 9 corners, Chengdu 0**, with Henan 16–9 in total shots and 4–0 in shots on target.

| Rank | Frozen contract | Grade |
|---:|---|---|
| 1 | 1H Over 0.5 goals | **LOSS** |
| 2 | Chengdu Over 4.5 team corners | **LOSS** |
| 3 | FT Over 2.5 goals | **LOSS** |
| 4 | FT Under 2.5 goals | **WIN** |
| 5 | 1H Under 0.5 goals | **WIN** |

**Potential winner:** Chengdu Rongcheng — **LOSS**; regulation match was drawn.

### Retrospective
1. **What did the result turn on?** Chengdu produced possession without effective terminal threat. The most important sporting fact is not merely the 0–0 score: the recovered stat line has Chengdu at **zero shots on target and zero corners**, while Henan generated the stronger shot/corner volume. The pre-game “Felipe absence → pressure without enough finishing” low-output branch occurred much more strongly than the central Chengdu attacking branch.
2. **Was it knowable before issue, and was it in the card?** **Partly.** Felipe's suspension, Henan's recent low-scoring home states, unresolved Chengdu XI/bench depth, and an explicit “territory, low finishing” / 0–0-to-0–1 branch were in the frozen card. What was not knowable was the extreme endpoint of **zero Chengdu corners and zero shots on target**. The card nevertheless over-weighted H2H first-half-goal frequency and historical Chengdu corner averages relative to the current striker/lineup uncertainty.
3. **Smallest routine change:** when a major central finisher is absent and the current attacking XI is incomplete, require one current **route-to-corner / route-to-shot-on-target** check (width, crosses, box entries, blocked attempts or current-role evidence) before letting historical team-corner averages outrank the low-conversion branch. This is a research-routine note, **not a new fitted coefficient or automatic corner downgrade**.

**Source checks:**  
- Offside Scores, final/stat line: https://offsidescores.com/br/futebol/jogo/henan-chengdu-rongcheng-20260906/db16d476-6821-4752-ac77-fcdd75ad1141/detalhe  
- HooFoot match-stat recap: https://hoofoot.net/pt/full-matches/chinese-super-league/henan-vs-chengdu-rongcheng-highlights-september-06-2026/

---

## P-319 — Yunnan Yukun vs Liaoning Tieren

### Settlement
**Final:** Yunnan Yukun 5–0 Liaoning Tieren. **HT:** 2–0.  
Recovered final stats: **Yunnan 3 corners, Liaoning 6; total 9**.

| Rank | Frozen contract | Grade |
|---:|---|---|
| 1 | 1H Over 0.5 goals | **WIN** |
| 2 | Total Corners Over 8.5 | **WIN** — 9 corners |
| 3 | FT Over 2.5 goals | **WIN** |
| 4 | FT Under 2.5 goals | **LOSS** |
| 5 | 1H Under 0.5 goals | **LOSS** |

**Potential winner:** Yunnan Yukun — **WIN**.

### Retrospective
1. **Driver:** Yunnan converted its home attacking edge early (32' and 40') and then separated decisively after halftime. The match became a one-sided five-goal result despite Liaoning having slightly more possession and six corners.
2. **Knowability:** **Yes, directionally.** The frozen card already had Yunnan's 7-2-3 home record, Liaoning's 1-3-7 away record, Liaoning's weak away scoring/defence, Kunimoto's suspension, and a Yunnan territorial/high-goal branch. Yunnan's congested week and recent 1–0 home games were valid counters, but they did not erase the much wider season scoring environment. The precise 5–0 and Cléber hat-trick were not knowable.
3. **Smallest routine change:** when short recent low-score samples conflict sharply with a season/home scoring environment, keep an explicit **high-conversion favourite tail** in the component budget instead of letting the two most recent 1–0s act as an implicit ceiling.

**Observation:** the corner Over won only by the minimum possible margin while Yunnan itself had just three corners. This is another reminder that **goal dominance, possession and total corners are separate targets**.

**Sources:**  
- Sofascore final/timeline: https://www.sofascore.com/football/match/yunnan-yukun-liaoning-tieren-fc/PzNbsQZOd  
- HooFoot final statistics (3–6 corners): https://hoofoot.net/es/full-matches/chinese-super-league/yunnan-yukun-vs-liaoning-tieren-highlights-september-06-2026/  
- FotMob final/timeline: https://www.fotmob.com/matches/liaoning-tieren-vs-yunnan-yukun/va1fhk9b

---

## P-320 — Tianjin Jinmen Tigers vs Zhejiang

### Settlement
**Final:** Tianjin Jinmen Tigers 2–1 Zhejiang. **HT:** 1–1.  
TotalCorner reports **Tianjin 10 corners, Zhejiang 4**.

| Rank | Frozen contract | Grade |
|---:|---|---|
| 1 | 1H Over 0.5 goals | **WIN** |
| 2 | Zhejiang Over 4.5 team corners | **LOSS** — 4 |
| 3 | FT Over 2.5 goals | **WIN** — exactly 3 goals |
| 4 | FT Under 2.5 goals | **LOSS** |
| 5 | 1H Under 0.5 goals | **LOSS** |

**Potential winner:** Zhejiang — **LOSS**.

### Retrospective
1. **Driver:** the early-event/three-goal branch occurred, but the allocation was wrong. Tianjin, not Zhejiang, converted the match into the stronger territory/corner result. Zhejiang's pre-game attacking reputation and corner baseline did not translate to five corners or the win.
2. **Knowability:** **Partly.** The card explicitly contained the Tianjin home/relegation-pressure upset path, Zhejiang's poor away record, Cardoso's absence and Tianjin's Schettine absence. It also stated the exact corner kill path: efficient attacks can terminate as shots/goals rather than blocks/clearances. The current exact XIs/benches were unresolved, so the winner and team-corner conclusions were already evidence-capped.
3. **Smallest routine change:** for team-corner rows, supplement season corner averages with a current **opponent-conditioned route profile** and keep an explicit efficiency-vs-corner tradeoff; do not treat general attacking strength or possession as sufficient evidence for a team-corner threshold.

**Source:** TotalCorner Tianjin current results, including 2–1 and 10–4 corners: https://www.totalcorner.com/team/view/82046

---

## P-321 — Sønderjyske vs AC Horsens

### Settlement
**Final:** Sønderjyske 2–5 AC Horsens. **HT:** 1–2.  
TotalCorner and WinDrawWin independently display **1–1 corners (2 total)**. Sønderjyske's official recap supports the 5–2 final and the match's reversal after a bright home start.

| Rank | Frozen contract | Grade |
|---:|---|---|
| 1 | 1H Over 0.5 goals | **WIN** |
| 2 | Total Match Corners Over 9.5 | **LOSS** — 2 total |
| 3 | FT Over 2.5 goals | **WIN** |
| 4 | FT Under 2.5 goals | **LOSS** |
| 5 | 1H Under 0.5 goals | **LOSS** |

**Potential winner:** AC Horsens — **WIN**.

### Retrospective
1. **Driver:** early scoring became a seven-goal game, but that scoring did **not** generate a high-corner environment. The available event records also show a major first-half disciplinary disruption to Sønderjyske, which materially changed the match state; the exact downstream score sequence was post-issue information.
2. **Knowability:** the strong first-half-goal and Horsens-winner paths were in the frozen card. A red-card/man-down event was not knowable as a specific occurrence. More importantly, the corner forecast was built from ~11-corner historical match environments and did not survive the actual goal-rich/low-corner path.
3. **Smallest routine change:** preserve a **goal-rich / corner-poor branch** in soccer derivative analysis and flag red-card matches as disrupted when later using them for baseline learning. Do not use the red card as retrospective proof that the pre-game total should have been Over; settle the issued contracts but isolate the disruption in later model comparisons.

**Sources:**  
- Sønderjyske official recap: https://soenderjyskefodbold.dk/droemmestart-endte-i-nedtur-mod-ac-horsens/  
- TotalCorner final/corners: https://www.totalcorner.com/team/view/710  
- WinDrawWin result/stat cross-check: https://www.windrawwin.com/us/results/sonderjyske/

---

## P-322 — South Africa vs Zimbabwe — Namibia T20I Tri-Series Final

### Settlement
South Africa won the toss and **batted first**, so all four conditional rows activated. **South Africa 205/5; Zimbabwe 157 all out; South Africa won by 48 runs.** Official ICC reporting records **South Africa 67/0 after the first six-over powerplay**.

| Rank | Frozen contract | Grade |
|---:|---|---|
| 1 | SA 6-over PP Over 54.5 | **WIN** — 67/0 |
| 2 | SA 20-over Over 186.5 | **WIN** — 205 |
| 3 | SA 20-over Under 186.5 | **LOSS** |
| 4 | SA 6-over PP Under 54.5 | **LOSS** |

**Potential winner:** South Africa — **WIN**.

### Retrospective
1. **Driver:** the opening pair immediately validated the high-phase branch, reaching 67/0, and South Africa sustained enough middle/death output to reach 205. Zimbabwe then failed to chase.
2. **Knowability:** **Yes, directionally and unusually clearly.** The frozen card had South Africa powerplays of 61 and 59 against Zimbabwe plus 70 in the latest relevant game, which is why the PP Over was Rank 1. It also had the 228-run ceiling and a current batting-process argument for the innings Over. The exact 67/0 and 205 were not knowable.
3. **Smallest routine change:** none beyond retaining the existing phase-specific evidence chain. This event is useful **positive process evidence**: PP and full-innings targets were assessed separately and happened to align; the result does not justify inferring full-innings Over from every strong powerplay.

**Official source:** ICC, “Relentless South Africa secure tri-series title in Windhoek”: https://www.icc-cricket.com/news/relentless-south-africa-secure-tri-series-title-in-windhoek

---

## P-323 — Everton vs Manchester United — EPL

### Settlement
**Final:** Everton 2–2 Manchester United. **HT:** 0–0.  
Goals came at 46', 83', 88' and 90+6'. Manchester United took **3 corners**.

| Rank | Frozen contract | p (`UNVALIDATED_SUBJECTIVE`) | Grade | Brier |
|---:|---|---:|---|---:|
| 1 | 1H Over 0.5 | 0.74 | **LOSS** | 0.5476 |
| 2 | Man United Over 4.5 team corners | 0.64 | **LOSS** — 3 | 0.4096 |
| 3 | FT Over 2.5 | 0.57 | **WIN** | 0.1849 |
| 4 | FT Under 2.5 | 0.43 | **LOSS** | 0.1849 |
| 5 | 1H Under 0.5 | 0.26 | **WIN** | 0.5476 |

**Ranked-row mean Brier:** **0.3749**, versus 0.2500 trivial 0.5 baseline.  
**Potential winner:** Manchester United — **LOSS**; draw. The 1X2 allocation is retained but not folded into the binary-row Brier denominator.

### Retrospective
1. **Driver:** the game was entirely a **second-half event**. United scored immediately after halftime, then a late 83'/88'/96' exchange produced the Over and draw. United had enough attacking quality to score twice but only three corners.
2. **Knowability:** **Partly.** United's deeper attacking bench and both teams' defensive vulnerability were in the card, so a second-half high-event state was available. But the 74% Rank-1 1H Over was too aggressive relative to the card's own low-event H2H evidence and early-season uncertainty. The exact 46' breakthrough and stoppage-time equaliser were unknowable.
3. **Smallest routine change:** when a first-half probability is high but the evidence set also contains multiple recent low-event H2Hs, show the **phase split explicitly**: first-half creation versus second-half substitution/score-state creation. Do not let full-match attacking quality silently inflate a first-half probability.

**Sources:**  
- Reuters match report: https://www.reuters.com/sports/soccer/maitland-niles-screamer-earns-everton-2-2-draw-with-man-utd-2026-09-06/  
- Guardian live report: https://www.theguardian.com/football/live/2026/sep/06/everton-v-manchester-united-premier-league-live  
- StatMuse Manchester United corners: https://www.statmuse.com/fc/ask/manchester-united-corner-game-logs  
- OFStats final stat display: https://ofstats.com/matches/view/everton-manchester-united-2026-09-06

---

## P-324 — Valencia vs Barcelona

**Administrative disposition:** **CLOSED / NO FORECAST ISSUED.**  
Official LaLiga final: **Valencia 0–5 Barcelona**, with Barcelona scoring at 6', 22', 50', 79' and 84'. The frozen record explicitly failed the exact live-state gate after kickoff, so no rank, probability or winner call was issued. **No W/L, Brier score or retrospective prediction is created after the fact.**

**Process note:** this is a correct fail-closed example. The smallest improvement is operational only: obtain an exact clock/period source faster if a live request is to be actionable. The result itself must not be used to invent a historical forecast.

**Official source:** https://www.laliga.com/en-NL/match/temporada-2026-2027-laliga-ea-sports-valencia-cf-fc-barcelona-4

---

## P-325 — Bangladesh Women vs Sri Lanka Women — Women's Asia Cup T20

### Settlement
Sri Lanka won the toss and elected to field, so **Bangladesh batted first** and the conditional rows activated. Bangladesh made **114/8**, with **37/1 after six overs**. Sri Lanka reached 115/6 and won by four wickets.

| Rank | Frozen contract | p | Grade | Brier |
|---:|---|---:|---|---:|
| 1 | BAN PP Under 42.5 | 0.73 | **WIN** — 37/1 | 0.0729 |
| 2 | BAN innings Under 116.5 | 0.56 | **WIN** — 114 | 0.1936 |
| 3 | BAN innings Over 116.5 | 0.44 | **LOSS** | 0.1936 |
| 4 | BAN PP Over 42.5 | 0.27 | **LOSS** | 0.0729 |

**Mean Brier:** **0.1332**.  
**Potential winner:** Sri Lanka Women — **WIN**.

### Retrospective
1. **Driver:** Bangladesh's powerplay stayed below the line and the full innings finished only 2.5 runs below 116.5. Sri Lanka then survived a difficult chase to win.
2. **Knowability:** **Yes, directionally.** The frozen card explicitly preferred Bangladesh's slower powerplay and lower innings ceiling, with current personnel/injury context and phase-specific evidence. The exact 37/1 and 114/8 were not knowable, and the innings result was **boundary-sensitive**, not a dominant Under.
3. **Smallest routine change:** preserve the existing phase/innings separation and label a 114 result against 116.5 as a **narrow boundary validation**, not proof of a broad low-scoring regime.

**Sources:**  
- Hindustan Times match stats, including Bangladesh PP 37/1 and innings 114/8: https://www.hindustantimes.com/cricket/match-stats-sl-w-vs-ban-w-women%E2%80%99s-asia-cup-t20-2026-match-10-sri-lanka-women-vs-bangladesh-women-t20-slwbw09062026273829  
- Wisden match report/scorecard search result was used as a score/toss cross-check in the research pass.

---

## P-326 — Western Carolina @ Campbell

**Administrative disposition:** **CLOSED / NO ACTIONABLE FORECAST ISSUED.**  
Official Campbell final: **Campbell 28–19 Western Carolina**. The frozen record crossed the start while exact live-state ownership remained unresolved, and explicitly issued **no rank and no winner call**. No historical prediction is inferred.

**Process note:** the fail-closed state gate is retained. The post-match result is useful only for event-state closure, not performance accounting.

**Official source:** Campbell University: https://gocamels.com/news/2026/9/6/football-worth-the-wait-camels-down-no-24-wcu-28-19-in-home-opener.aspx

---

## P-327 — Angers SCO vs Rennes

### Settlement
**Final:** Angers 1–2 Rennes. **HT:** 1–2.  
Recovered stat displays: **Angers 12 corners, Rennes 6; total 18**.

| Rank | Frozen contract | p | Grade | Brier |
|---:|---|---:|---|---:|
| 1 | 1H Over 0.5 | 0.75 | **WIN** | 0.0625 |
| 2 | Total corners Over 8.5 | 0.64 | **WIN** — 18 | 0.1296 |
| 3 | FT Over 2.5 | 0.60 | **WIN** — exactly 3 | 0.1600 |
| 4 | FT Under 2.5 | 0.40 | **LOSS** | 0.1600 |
| 5 | 1H Under 0.5 | 0.25 | **LOSS** | 0.0625 |

**Mean Brier:** **0.1149**.  
**Potential winner:** Rennes — **WIN**.

### Retrospective
1. **Driver:** Rennes scored at 9' and benefited from a 17' own goal; Angers replied at 35'. All three goals came before halftime, while Angers' sustained chase later generated a very large corner count.
2. **Knowability:** the frozen card's early-goal, Rennes-attacking and high-corner branches were all present. The exact own goal was not knowable. The result supports the **mechanism direction**, but the total Over was only one goal beyond the threshold and should not be treated as an extreme scoring success.
3. **Smallest routine change:** none beyond explicitly preserving **trailing-team corner accumulation** as a separate mechanism from goal conversion; this match is a clean example of that distinction.

**Sources:**  
- OFStats final/timeline and 12–6 corners: https://ofstats.com/matches/view/angers-sco-rennes-2026-09-06  
- Football.fr match report: https://www.football.fr/direct-foot/337762/338173/angers-rennes.shtml

---

## P-328 — Arsenal vs Chelsea — EPL

### Settlement
**Final:** Arsenal 2–1 Chelsea. **HT:** 1–1.  
Chelsea scored after 77 seconds; Arsenal equalised at 25' and won at 50'. Guardian match stats: **Arsenal 5 corners, Chelsea 3**.

| Rank | Frozen contract | p | Grade | Brier |
|---:|---|---:|---|---:|
| 1 | 1H Over 0.5 | 0.68 | **WIN** | 0.1024 |
| 2 | Arsenal Over 4.5 team corners | 0.62 | **WIN** — 5 | 0.1444 |
| 3 | FT Over 2.5 | 0.53 | **WIN** — exactly 3 | 0.2209 |
| 4 | FT Under 2.5 | 0.47 | **LOSS** | 0.2209 |
| 5 | 1H Under 0.5 | 0.32 | **LOSS** | 0.1024 |

**Mean Brier:** **0.1582**.  
**Potential winner:** Arsenal — **WIN**.

### Retrospective
1. **Driver:** Chelsea's 77-second opener immediately created the high-tempo chase state. Arsenal produced heavy first-half pressure, equalised, then completed the comeback early in the second half. The corner line cleared by one.
2. **Knowability:** **Yes, directionally.** Both current attacks, Chelsea's midfield absence, Arsenal's home edge, and an early-goal route were all in the card. The exact first-77-seconds goal was unknowable. The Arsenal corner result was boundary-sensitive rather than dominant.
3. **Smallest routine change:** no structural change. Retain the current rule that an early goal changes the subsequent exposure state; when evaluating the corner row later, record that it cleared **5 vs 4.5**, not as evidence of a large corner edge.

**Sources:**  
- Guardian match page with score/corners: https://www.theguardian.com/football/match/2026/sep/06/arsenal-v-chelsea  
- Guardian match report/live coverage: https://www.theguardian.com/football/live/2026/sep/06/arsenal-v-chelsea-premier-league-live

---

## P-329 — Bologna vs Sassuolo

### Settlement
**Final:** Bologna 2–2 Sassuolo. **HT:** 0–1.  
Final corner count **Bologna 10, Sassuolo 7; total 17**. Bologna substitute Artem Dovbyk equalised at 90+1'.

| Rank | Frozen contract | p | Grade | Brier |
|---:|---|---:|---|---:|
| 1 | Total corners Over 6.5 | 0.61 | **WIN** | 0.1521 |
| 2 | FT Under 2.5 | 0.58 | **LOSS** | 0.3364 |
| 3 | 1H Over 0.5 | 0.55 | **WIN** | 0.2025 |
| 4 | 1H Under 0.5 | 0.45 | **LOSS** | 0.2025 |
| 5 | FT Over 2.5 | 0.42 | **WIN** | 0.3364 |

**Mean Brier:** **0.2460**.  
**Potential winner:** Bologna — **LOSS**; draw.

### Retrospective
1. **Driver:** the match had high attempt/corner volume and two Sassuolo leads, then Bologna's bench supplied the 90+1 equaliser. Bologna's underlying attacking volume finally converted enough to break the preferred Under.
2. **Knowability:** **Partly.** The frozen card explicitly knew Bologna's strong xG despite zero league goals and listed a credible high-event branch. It also knew Dovbyk was on the bench and Sassuolo's defence/rotation was incomplete. The precise stoppage-time substitute goal was unknowable. The main process weakness was giving the Under 58% while the same evidence acknowledged substantial Bologna shot creation and capable attacking reserves.
3. **Smallest routine change:** whenever a high-impact striker/creator is **available from the bench**, include that role explicitly in the second-half scoring component rather than treating “not starting” as equivalent to unavailable.

**Sources:**  
- ZeroZero final stats, 10–7 corners and Dovbyk 90+1: https://www.zerozero.pt/jogo/2026-09-06-bologna-sassuolo/12240729  
- StatMuse Bologna/Sassuolo corner cross-checks: https://www.statmuse.com/fc/ask/bologna-corner-stats-in-each-match?l=seriea and https://www.statmuse.com/fc/ask/sassuolo-last-10-matches-corner-stats

---

## P-330 — Puerto Rico Women vs Belgium Women

**Administrative disposition:** **CLOSED / NO ACTIONABLE FORECAST ISSUED.**  
Official FIBA final: **Puerto Rico 64–76 Belgium**. The frozen log issued no rank and no winner because the live-state gate could not be verified at the time. No retrospective prediction or Brier score is fabricated.

**Official source:** FIBA: https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128130-PUR-BEL

---

## P-331 — Milwaukee Brewers @ Cincinnati Reds — MLB

### Settlement
**Final:** Cincinnati Reds 12–8 Milwaukee Brewers.

| Rank | Frozen contract | p | Grade | Brier |
|---:|---|---:|---|---:|
| 1 | Combined Total Over 8.5 | 0.57 | **WIN** | 0.1849 |
| 2 | Cincinnati +1.5 | 0.56 | **WIN** | 0.1936 |
| 3 | Milwaukee -1.5 | 0.44 | **LOSS** | 0.1936 |
| 4 | Combined Total Under 8.5 | 0.43 | **LOSS** | 0.1849 |

**Mean Brier:** **0.1893**.  
**Potential winner:** Milwaukee — **LOSS**.

### Retrospective
1. **Driver:** Cincinnati's offence overwhelmed the Brewers in the middle innings. Elly De La Cruz drove in four, Cincinnati stacked multiple-hit performances, and Milwaukee defensive errors compounded the run environment. Singer allowed six runs but was supported by 12 Cincinnati runs, showing why the winner call and starter comparison were separable from the total.
2. **Knowability:** **Partly.** The frozen card already had GABP homer volatility, Cincinnati's right-handed matchup path, Harrison's severe prior-start HR failure and a 10-run-ish upper state. It nevertheless leaned Milwaukee 64% on the stronger season/starter profile. The exact De La Cruz production, error sequence and 20-run final were unknowable.
3. **Smallest routine change:** in hitter-friendly parks, keep **defence/error and multi-inning bullpen exposure** as separate run components rather than allowing the starting-pitcher comparison to dominate the winner allocation. This is not a blanket Over rule.

**Source:** Reuters, “Elly De La Cruz (4 RBIs) powers Reds to series win over Brewers”: https://www.reuters.com/sports/baseball/elly-de-la-cruz-4-rbis-powers-reds-series-win-over-brewers--flm-2026-09-06/

---

## P-332 — Deportivo Alavés vs CA Osasuna

### Settlement
**Final:** Alavés 5–2 Osasuna. **HT:** Alavés 2–0.  
Final corner displays: **Alavés 4, Osasuna 1; total 5**.

| Rank | Frozen contract | p | Grade | Brier |
|---:|---|---:|---|---:|
| 1 | FT Under 2.5 | 0.60 | **LOSS** | 0.3600 |
| 2 | Total corners Over 8.5 | 0.59 | **LOSS** — 5 | 0.3481 |
| 3 | 1H Over 0.5 | 0.57 | **WIN** | 0.1849 |
| 4 | 1H Under 0.5 | 0.43 | **LOSS** | 0.1849 |
| 5 | FT Over 2.5 | 0.40 | **WIN** | 0.3600 |

**Mean Brier:** **0.2876**.  
**Potential winner:** Alavés — **WIN**.

### Retrospective
1. **Driver:** Alavés converted an even-looking opening into a 2–0 halftime lead, Osasuna immediately responded after halftime, and the match expanded to seven goals. Lucas Boyé scored a hat-trick. Despite the goal explosion, the match produced only five corners.
2. **Knowability:** **Partly.** The frozen card had Alavés' strong current xG profile, Osasuna's Budimir threat, and a 2–1/1–2 upper-tail branch. But it made low-event 0–0/1–0/1–1 score families central and put Under 2.5 at 60%. Alavés lineup evidence was also conflicted, which should have widened the tails rather than supporting a narrow low-event centre. The exact hat-trick and seven-goal output were unknowable.
3. **Smallest routine change:** when both teams have credible attacking xG/finishing routes and the participant state is conflicted, widen the **score-distribution tail** explicitly before assigning a 60% Under. Separately, do not infer corners from goal volume: seven goals occurred with only five corners.

**Sources:**  
- Official LaLiga final/timeline: https://www.laliga.com/es-CO/partido/temporada-2026-2027-laliga-ea-sports-deportivo-alaves-ca-osasuna-4  
- Official Osasuna match report: https://www.osasuna.es/en/match-recap-alavesosasuna-2026/27  
- OFStats final/corners cross-check: https://ofstats.com/matches/view/deportivo-alaves-osasuna-2026-09-06

---

# P-318–P-332 DESCRIPTIVE SETTLEMENT SUMMARY

Issued sporting cards: **12** (`P-318, P-319, P-320, P-321, P-322, P-323, P-325, P-327, P-328, P-329, P-331, P-332`).  
Administrative no-forecast closures: **3** (`P-324, P-326, P-330`).  
Ranked rows issued and now settled: **57 = 28 W / 29 L**.  
Potential-winner calls on issued cards: **7 W / 5 L**.

These are mixed sports, mixed horizons and mixed target families. The raw 28/57 is **descriptive only** and is not a model accuracy claim, ROI, edge or calibration estimate.

## v4.0 subjective-probability scorecard

Cards with issued `UNVALIDATED_SUBJECTIVE` ranked-row probabilities: **P-323, P-325, P-327, P-328, P-329, P-331, P-332**.  
Total scored binary ranked rows: **33**, with **17 W / 16 L**.  
Mean Brier across those mixed populations: **0.2181** versus **0.2500** for a 0.5 baseline. This mixed-population figure is **not** the primary performance claim.

`PRIMARY_SCORED` populations represented here:
- **EPL (P-323 + P-328):** 10 rows, 5 W / 5 L, mean Brier **0.2666** vs 0.2500 baseline.
- **MLB (P-331):** 4 rows, 2 W / 2 L, mean Brier **0.1893** vs 0.2500 baseline.
- **Combined primary rows in this small continuation only:** 14 rows, 7 W / 7 L, mean Brier **0.2445** vs 0.2500 baseline.

The samples are far too small for calibration or superiority claims. Complementary rows also create dependence, so row counts are not independent event trials.

---

# GENERAL LEARNINGS, RULE CHANGES, OBSERVATIONS AND NEW SOURCE USE — 2026-09-07

## General learnings / observations
1. **Goals, possession and corners remain separate processes.** P-318 had 0–0 with Henan 9–0 corners; P-320 had Zhejiang lose while taking only four corners; P-329 had four goals and 17 corners; P-332 had seven goals and only five corners. There is no reliable goals↔corners shortcut.
2. **First-half and full-match creation must be phase-separated.** P-323's 74% first-half Over lost while four second-half goals produced the full-match Over. Conversely P-327/P-328 had early goals and full-match Overs. Full-match attacking quality cannot be allowed to silently inflate a first-half probability.
3. **Cricket phase and innings remain independent targets.** P-322's strong PP and innings Over aligned; P-325's PP Under and innings Under also aligned, but neither event justifies a deterministic phase→innings rule. Settle and model each field separately.
4. **Bench availability is not the same as absence.** P-329's Dovbyk bench role mattered directly when he scored the 90+1 equaliser. A named high-impact reserve belongs in the second-half scoring state.
5. **Disrupted matches need a retrospective flag, not hindsight reranking.** P-321's major disciplinary event changed the match state. The result still settles contracts, but later baseline learning should mark the match as disrupted rather than attributing every downstream outcome to pre-game process.
6. **MLB starter comparisons do not own the entire run/winner distribution.** P-331 demonstrates how park, offence, errors and later innings can dominate even when the preferred team has the stronger season/starter profile.
7. **Boundary wins are not broad validation.** P-319 corners Over 8.5 won at 9; P-325 innings Under 116.5 won at 114; P-328 Arsenal corners Over 4.5 won at 5. Store the distance-to-line when judging mechanism strength.
8. **The first v4 probability sample is mixed.** EPL P-323 was poorly scored; EPL P-328 was materially better; MLB P-331 beat the 0.5 baseline on only four rows. Nothing here is sufficient to call probabilities calibrated.

## Rule changes
**No new predictive rule, numerical weight, automatic rank change or fitted coefficient is promoted from this pass.** Under METHOD v4.0, a sporting pattern normally needs recurrence review at the 25-settled-card cadence within a `PRIMARY_SCORED` population. The items above are retained as observations/routine improvements. Existing controls on field ownership, phase separation, bench depth, derivative settlement, no-hindsight rewriting and score-state paths remain sufficient.

### Candidate watch items, not promoted rules
- current route-to-corner evidence when a major central attacker is absent;
- explicit second-half bench-attacker contribution;
- distance-to-line in derivative retrospective evaluation;
- disrupted-match flag for later population baselines.

## New / newly demonstrated settlement-source uses
| Source | Demonstrated field | Disposition |
|---|---|---|
| ICC official match report | P-322 toss, 67/0 powerplay, 205 innings, result | **High-authority official settlement use** |
| LaLiga official match pages | P-324 and P-332 final, scoring timeline, lineups | **High-authority official event owner** |
| FIBA official game page | P-330 final and quarter-by-quarter score | **High-authority official event owner** |
| Campbell University official report | P-326 final / game recap | **Official team source, suitable for event closure** |
| TotalCorner current result rows | P-320/P-321 exact corner fields | **Specialist derivative field; useful, not automatically independent of other displays** |
| StatMuse football corner logs | P-323/P-329 team-corner corroboration | **Structured specialist corroboration; field-specific only** |
| Guardian match stats | P-328 exact 5–3 corners and final | **High-quality secondary/specialist settlement aid** |
| OFStats | P-318/P-327/P-332 detailed stat/timeline cross-checks | **Secondary structured evidence; do not elevate above an available field owner** |
| Reuters match reports | P-323/P-331 result drivers | **High-quality narrative driver evidence; not a replacement for derivative field owners** |

## ID / temporary-holding conclusion
**No conflicting canonical ID was found. No `TMP-SETTLED-*` identifier is required.** Drive still reports P-318 as the next canonical slot, and P-318–P-332 exist only in this local continuation pending future canonical import. If Drive later assigns any of those IDs to a different event, preserve both records and move the conflicting local settlement into the existing `TMP-SETTLED-<date>-<sequence>` holding procedure before any aggregate calculation.

---

# 0. FRESH GOVERNANCE INITIALISATION — 2026-09-06

## 0.1 Effective method state

The September 6 Drive audit produced `MDS-2026.09.06-v3.7` and then a same-day external-blindspot addendum states that `L-087`–`L-101` were adopted and the method advanced to **`MDS-2026.09.06-v3.8`**.

There is a **metadata consistency defect** in the current Drive snapshot:

- `AUDIT_CHANGELOG_2026-09-06.md` addendum and the README status paragraph state that the external-blindspot amendments advance the method to **v3.8**.
- `PREDICTION_LOG_COMBINED_2.md` top snapshot still prints **v3.7**.
- the fetched top metadata of `RULES_GENERAL.md` still prints **v3.6**, even though the file contains September 6 amendment sections including the later controls.

**Operational rule for this mini-log:** apply the latest explicit September 6 control amendments, including `L-087`–`L-101`, while recording the metadata conflict rather than silently pretending the headers are synchronised. Re-check this conflict before each issued card. No calibrated probability, edge, ROI or staking claim is permitted.

## 0.2 September 6 controls carried forward

The following current controls are mandatory in addition to the prior sport-specific `SFA-<SPORT>` rules:

1. **Structured-endpoint-first acquisition (`G10.1`, `L-080`).** Query field-owning structured/statistical endpoints before relying on narrative match reports where available.
2. **Settlement-source pre-registration (`G10.2`, `L-081`).** Derivative markets are allowed when the competition/provider coverage can actually settle the field; do not apply blanket market-type bans.
3. **Synthetic-content exclusion (`L-079`).** Simulated, AI-generated, preview, fantasy or tip content cannot establish event facts or settle contracts.
4. **Bench / coaching / rotation record (`G14.2`, `L-082`).** Record full bench/substitute depth, coach state and material rotation/rest signals. `BENCH_NOT_RETRIEVED` blocks a margin or full-game total row from Rank #1.
5. **Bimodal phase-total treatment (`L-083`).** In phase markets with meaningful early possession/wicket-loss risk, model high-output and collapse branches separately rather than averaging them away.
6. **Aggregate tail budget (`G20.2`, `L-084`).** Mandatory disclosure only unless and until its prospective validation promotes an ordinal effect.
7. **Total-row path geometry (`G21.1`, `L-085`).** State the concrete mechanism/path by which each Over/Under wins and loses; disclosure is mandatory, weighting remains prospective where specified.
8. **Top-slot separation floor (`G26.1`).** Rank #1 must have a defensible mechanism separation from Rank #2; administrative tie-breaking must not masquerade as predictive separation.
9. **Archival completeness (`G34.1`, `L-086`).** Every issued row, rank, target definition and source set must be preserved before delivery so ranks cannot become permanently ungradable.
10. **Standard-rules settlement (`G36.1`).** Where operator terms are absent, use the documented standard competition/rules endpoint only when the gate permits it, and label the assumption explicitly.
11. **Governance split (`L-087`).** A disclosure/process safeguard may be promoted while any claimed magnitude/weighting effect remains `CANDIDATE`; do not turn a retrospective lesson into an unvalidated coefficient.
12. **Rank-gap field (`L-088`).** Record the qualitative separation between adjacent ranks, especially Rank #1 vs Rank #2.
13. **Two-pass retrospective discipline (`G37.1`, `L-089`).** When retrospective work is explicitly requested, grade the frozen issue-time process before seeing/using outcome-driven explanations, then separately grade outcome drivers/current-rule gaps.
14. **Settlement-only performance eligibility (`EP-2026.09.06-v2`, `L-078` / `L-090` stratification requirement).** Settled rows enter descriptive performance accounting; headline accuracy must be stratified by method version, horizon, sport, target family and event/decision-set weighting before being interpreted.
15. **Control taxonomy / evidence density / market terminology (`L-095`, `L-099`, `L-100`).** Distinguish integrity blockers from disclosure controls and candidate predictive hypotheses; respect sport evidence-density labels; `MARKET_BLIND` means price/market-analysis blind for issuance, not ignorance of the user-supplied contract definition.
16. **No hindsight rewriting.** Issued ranks and frozen evidence remain immutable. Later corrections, settlements and learnings are append-only.

## 0.3 Wolfram tool status

The user explicitly invoked Wolfram for this continuation. Two Wolfram MCP calls were attempted during initialisation (`WolframContext` and `WolframLanguageEvaluator`) and both returned an upstream MCP/SSE **404**. Therefore:

- Wolfram contributed **no event evidence or computation** to this initialisation;
- no Wolfram-derived value is cited as if it succeeded;
- future queries may retry Wolfram when it is materially useful, but public/official sports evidence still requires the normal field-owner research workflow.

---

# 1. HISTORICAL FROZEN UNSETTLED / INCOMPLETE QUEUE — SUPERSEDED BY 2026-09-07 CONTROLLING OVERLAY ABOVE

> The table below is preserved as issue-time/history evidence. Its `UNSETTLED` labels are no longer the current queue state. Use the controlling settlement snapshot at the top of this file.

These records remain **separate at the top** until an explicit settlement/retrospective pass closes them. This initialisation does not retrospectively regrade them.

## 1.1 Local issued / incomplete records after the Drive-settled P-294–P-305 cohort

| ID | Sport | Event | Frozen/issued state | Rank #1 | Potential winner | Current local status |
|---|---|---|---|---|---|---|
| **P-332** | Soccer — Spain La Liga | Deportivo Alavés vs CA Osasuna | **PREGAME; verified kickoff 2026-09-06 18:30 CEST / 2026-09-07 02:30 AEST; final structured refresh 2026-09-07 02:27:58 AEST remained Scheduled; LaLiga field-owner page had not exposed final XI in retrieved record; Osasuna current XI/full bench aligned across same-day secondary sources, but Alavés secondary lineup sources conflicted, so SO-P2 = CONFLICTING/SECONDARY_ONLY; Osasuna official injuries: Aimar Oroz (left biceps femoris), Jorge Herrando (left adductor), Valentin Rosier (muscle) unavailable/recovering; Alavés current reporting: Mikel Rodríguez ACL out long-term, Toni Martínez doubtful with soleus issue; Mendizorroza ~29C at match window with AEMET yellow high-temperature warning, light-rain current observation but forecast drying/mostly sunny** | **FT Under 2.5 — 60% UNVALIDATED_SUBJECTIVE** | **Deportivo Alavés — slight regulation-time lean, 41% UNVALIDATED_SUBJECTIVE** | **UNSETTLED — EXPLORATORY / NOT SCORED; retrospective deferred** |
| **P-331** | Baseball — MLB | Milwaukee Brewers (Kyle Harrison) @ Cincinnati Reds (Brady Singer) | **PREGAME freeze 2026-09-07 02:06:21 AEST / 2026-09-06 12:06:21 EDT; verified 12:10 EDT first pitch; MLB official probable-pitcher page confirms Harrison/Singer; current secondary lineup service has both orders confirmed but MLB lineup page crawl still showed TBD, so BB-P2 PARTIAL; MIL: Frelick-Yelich-Chourio-Bauers-Mitchell-Turang-Pratt-Bo Naylor-Hamilton; CIN: Myers-De La Cruz-Stewart-Stephenson-Suarez-Bleday-McLain-Brito-Rodriguez; Reds activated Graham Ashcraft for fresh bullpen depth, while Pagan/Santillan worked Saturday; Brewers Ashby worked Friday/Saturday, Megill Friday, Uribe/Romero available in current roster; GABP weather ~25C, dry, 9-10 mph L-to-R** | **Over 8.5 — 57% UNVALIDATED_SUBJECTIVE** | **Milwaukee Brewers — eventual winner lean, 64% UNVALIDATED_SUBJECTIVE** | **UNSETTLED — MLB PRIMARY_SCORED; retrospective deferred** |
| **P-330** | Basketball — FIBA Women's World Cup | Puerto Rico Women vs Belgium Women | **LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST; verified scheduled tip 2026-09-06 15:45 UTC / 2026-09-07 01:45 AEST; final pre-tip time handshake reached 01:44:58 AEST, but the next verified clock was 01:45:02 AEST; FIBA exact-match page still had no live score/quarter/clock and current secondary live-score pages had not exposed a trustworthy exact basketball state; under BK-P3/RULES_GENERAL timing gate the pre-tip four-row snapshot was NOT ISSUED** | **NO RANK #1 — state gate failed** | **NO WINNER CALL ISSUED** | **OPEN / NO-ACTION — retrospective deferred** |
| **P-329** | Soccer — Italy Serie A | Bologna vs Sassuolo | **PREGAME; verified kickoff 2026-09-06 18:00 CEST / 2026-09-07 02:00 AEST; G31 refresh 2026-09-07 01:35:59 AEST remained Scheduled; Bologna official squad confirms Orsolini out ~3 weeks and El Azzouzi unavailable; Sky current matchday page lists full XI/benches for both sides, Sassuolo unavailable: Walukiewicz, Koné, Boloca, Pieragnolo, Candé; Berardi bench, Bologna Dovbyk bench; Sassuolo played Coppa Italia 1-1 + penalties on Sep 2; Dall'Ara weather ~34C at kickoff, dry, falling to ~31C by 20:00** | **Total Match Corners Over 6.5 — 61% UNVALIDATED_SUBJECTIVE** | **Bologna — slight regulation-time lean, 42% UNVALIDATED_SUBJECTIVE** | **UNSETTLED — EXPLORATORY / NOT SCORED; retrospective deferred** |
| **P-328** | Soccer — English Premier League | Arsenal vs Chelsea | **PREGAME; verified kickoff 2026-09-06 16:30 BST / 2026-09-07 01:30 AEST; G31 structured refresh 2026-09-07 01:27:48 AEST remained Scheduled; current XIs/full benches consistently reported by multiple current live sources but not both recovered from field-owner lineup pages, therefore `SECONDARY_ONLY`; Arsenal Saliba/Mosquera absent, Bruno Guimaraes bench; Chelsea Caicedo unavailable, Colwill bench; Emirates weather ~26C, mostly cloudy/partly sunny, no material rain signal** | **1H Over 0.5 — 68% UNVALIDATED_SUBJECTIVE** | **Arsenal — slight regulation-time lean, 51% UNVALIDATED_SUBJECTIVE** | **UNSETTLED — EPL PRIMARY_SCORED; retrospective deferred** |
| **P-327** | Soccer — France Ligue 1 | Angers SCO vs Stade Rennais FC | **PREGAME; verified kickoff 2026-09-06 17:15 CEST / 2026-09-07 01:15 AEST; final structured refresh 2026-09-07 01:09:21 AEST remained Scheduled; official Rennes 21-man squad retrieved, Abdelhamid Aït Boudlal unavailable for family reason, Brice Samba included after prior muscle issue; exact current starting XIs/full benches not independently retrieved before freeze; Angers secondary injury reports list Haris Belkebla (thigh) and Louis Mouton (knee), final official matchday status unresolved; venue-level structured weather ~32C/mMostly sunny, Météo-France Angers government forecast hot/dry/weak wind** | **1H Over 0.5 — 75% UNVALIDATED_SUBJECTIVE** | **Rennes — slight regulation-time lean, 55% UNVALIDATED_SUBJECTIVE** | **UNSETTLED — EXPLORATORY / NOT SCORED; retrospective deferred** |
| **P-326** | American Football — NCAA FCS | #24 Western Carolina @ Campbell | **START-CROSSED / LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST; official rescheduled kickoff 2026-09-06 11:00 EDT / 2026-09-07 01:00 AEST; final pre-start research refresh 00:57:17 AEST was pregame, but delivery crossed 01:00:00 AEST; immediate post-start structured feed showed DELAYED with 0 plays/0 yards/0:00 possession, while Campbell official schedule had not published a field-owner zero-play delay confirmation; under RULES_GENERAL start-crossing gate the pregame 4-row snapshot was NOT ISSUED and no live probabilities/winner were published** | **NO RANK #1 — state gate unresolved** | **NO WINNER CALL ISSUED** | **OPEN / NO-ACTION — retrospective deferred** |
| **P-325** | Cricket — Women's Asia Cup T20 | Bangladesh Women vs Sri Lanka Women | **PREGAME freeze 2026-09-07 00:28:36 AEST; verified kickoff 2026-09-06 18:30 GST / 2026-09-07 00:30 AEST (user estimate '12:30 PM' corrected by 12h); exact-match centre still showed toss/playing XIs unannounced; Bangladesh first-innings rows CONDITIONALLY ACTIONABLE ONLY IF Bangladesh bat first; Fariha Islam Trisna ruled out (Grade II right-thigh tear), Farjana Easmin replacement; Dewmi Vihanga ruled out (right knee), Nimasha Meepage replacement; exact current strip report not recovered after six-rung search** | **BAN 1st-innings PP Under 42.5 — 73% UNVALIDATED_SUBJECTIVE (conditional on BAN batting first)** | **Sri Lanka Women — match-winner lean, 66% UNVALIDATED_SUBJECTIVE** | **UNSETTLED — EXPLORATORY / NOT SCORED; retrospective deferred** |
| **P-324** | Soccer — Spain La Liga | Valencia vs Barcelona | **LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST; scheduled 2026-09-06 16:15 CEST / 2026-09-07 00:15 AEST; structured soccer source switched to Live 0-0 by 2026-09-07 00:18:49 AEST, but no exact match clock/period was exposed by the field-owning/structured source set; LaLiga official page still showed Scheduled, creating a source-state conflict; no pregame ranking or live probability issued** | **NO RANK #1 — state gate failed** | **NO WINNER CALL ISSUED** | **OPEN / NO-ACTION — retrospective deferred** |
| **P-323** | Soccer — English Premier League | Everton vs Manchester United | **PREGAME; verified kickoff 2026-09-06 14:00 BST / 23:00 AEST; final structured refresh 2026-09-06 22:56:02 AEST remained Scheduled; both current XIs and full benches retrieved; Everton Christian Nørgaard unavailable, Iliman Ndiaye transferred out; Manchester United Carlos Baleba, Matthijs de Ligt, Manuel Ugarte and Amad Diallo unavailable, Mason Mount returns to bench; formal v4 bench-depth integers not reliably reconstructed** | **1H Over 0.5 goals — 74% UNVALIDATED_SUBJECTIVE** | **Manchester United — slight regulation-time lean (45% / draw 29% / Everton 26%)** | **UNSETTLED — MDS-2026.09.06-v4.0 PRIMARY_SCORED EPL; retrospective deferred** |
| **P-322** | Cricket — Namibia T20I Tri-Series Final | South Africa vs Zimbabwe | **START-CROSSED / NO PUBLIC TOSS OR SCORECARD FOUND AT FREEZE; scheduled 2026-09-06 14:00 CAT / 22:00 AEST; final refresh 2026-09-06 22:06:38 AEST; Cricket Australia still showed Upcoming / team to be announced / scorecard unavailable; contracts CONDITIONALLY ACTIONABLE ONLY IF SOUTH AFRICA BAT FIRST; Lutho Sipamla ruled out (left hamstring), Jason Smith ruled out of tri-series (right adductor), Andile Simelane replacement available; final XI not published in controlling sources** | **South Africa 1st-innings PP Over 54.5 — conditional on SA batting first** | **South Africa — match-winner lean** | **UNSETTLED — START-CROSSED ORIGINAL-LINE / TOSS-CONDITIONAL; retrospective deferred** |
| **P-321** | Soccer — Denmark Superliga | Sønderjyske vs AC Horsens | **PREGAME; official/structured kickoff 2026-09-06 14:00 CEST / 22:00 AEST; final structured refresh 2026-09-06 21:57:49 AEST remained Scheduled; AC Horsens official 20-man squad retrieved; Sønderjyske exact current XI/bench not independently retrieved; Brynjar Ingi Bjarnason suspended, Mathias Olesen injury/day-to-day, Christian Vestergaard knee injury** | **1H Over 0.5 goals** | **AC Horsens — slight regulation-time lean** | **UNSETTLED — retrospective deferred; participant/bench and derivative-provider caps applied** |
| **P-320** | Soccer — China Super League | Tianjin Jinmen Tigers vs Zhejiang | **PREGAME; official Tianjin fixture + structured schedule both resolve kickoff to 2026-09-06 20:00 CST / 22:00 AEST, correcting user's 21:35 estimate; final structured refresh 2026-09-06 21:41:50 AEST remained Scheduled; current official XI/bench not independently retrievable before issue; Tianjin Schettine confirmed injured/out; Zhejiang Cardoso confirmed injured/out ~2 weeks** | **1H Over 0.5 goals** | **Zhejiang — slight regulation-time lean** | **UNSETTLED — retrospective deferred; participant/bench and derivative-provider caps applied** |
| **P-319** | Soccer — China Super League | Yunnan Yukun vs Liaoning Ironman | **START-CROSSED / VERIFIED LIVE 0-0; research began pre-kickoff; final structured refresh at 2026-09-06 21:35:37 AEST / 19:35:37 CST switched to Live at 0-0; exact match clock not exposed; no scoring/corner/live-event data used beyond the 0-0 state; current XIs/benches not independently retrievable before issue; Liaoning's Takahiro Kunimoto suspended and Guy Mbenza confirmed available** | **1H Over 0.5 goals** | **Yunnan Yukun — regulation-time lean** | **UNSETTLED — START-CROSSED ORIGINAL-LINE VIEW; retrospective deferred; participant/bench/provider-definition caps apply** |
| **P-318** | Soccer — China Super League | Henan vs Chengdu Rongcheng | **PREGAME; freeze 2026-09-06 21:30:10 AEST / 19:30:10 CST; scheduled 21:35 AEST / 19:35 CST; structured state Scheduled; current Henan XI recovered; Chengdu current XI only partially retrievable; Felipe suspended; no live data used** | **1H Over 0.5 goals** | **Chengdu Rongcheng — slight 90-minute lean** | **UNSETTLED — retrospective deferred; full-bench/complete-Chengdu-XI evidence cap applies** |
| **P-317** | Baseball — KBO | Doosan Bears @ SSG Landers | Same-event pregame revision of P-316; freeze 2026-09-06 17:59:15 AEST / 16:59:15 KST; Yang Eui-ji late out resolved; Doosan order verified; no live data used | **Under 10.5 runs** | **Doosan Bears — narrow lean** | **UNSETTLED; same event as P-316; do not double-count event-level performance** |
| **P-316** | Baseball — KBO | Doosan Bears @ SSG Landers | Pregame; freeze 2026-09-06 17:52:22 AEST / 16:52:22 KST; starters official; final indexed batting orders unresolved | **Under 10.5 runs** | **Doosan Bears — narrow lean** | **UNSETTLED; superseded for same-event latest-view purposes by P-317, but issued record remains immutable** |
| **P-315** | AFLW | Waalitj Marawar (West Coast) vs Narrm (Melbourne) | Start-crossed original-line view; no live score/stat data used | **West Coast +33.5** | **Melbourne** | **UNSETTLED** |
| **P-314** | Baseball — MLB | LA Angels @ Pittsburgh Pirates | Pregame; starters and posted lineups verified | **Under 8.5 runs** | **Pittsburgh Pirates** | **UNSETTLED** |
| **P-313** | Baseball — MLB | Milwaukee Brewers @ Cincinnati Reds | Pregame; starters official; MIL official order unresolved at freeze | **Brewers -1.5** | **Milwaukee Brewers** | **UNSETTLED** |
| **P-312** | Baseball — MLB | Detroit Tigers @ Cleveland Guardians | Start-crossed original-line view; no live pitch/event data used | **Detroit Tigers +1.5** | **Cleveland Guardians** | **UNSETTLED** |
| **P-311** | Cricket — WCPL Women | Barbados Tridents Women vs Trinbago Knight Riders Women | Pregame pre-toss; TKR phase rows conditional on TKR batting first | **TKR PP Under 41.5** | **Barbados Tridents Women** | **UNSETTLED** |
| **P-310** | Tennis — US Open | Luciano Darderi vs Dane Sweeny | Pregame | **Dane Sweeny +5.5 games** | **Luciano Darderi** | **UNSETTLED** |
| **P-309** | American Football — NCAA FCS | Gardner-Webb @ Wofford | Pregame; college availability incomplete | **Under 50.5 points** | **Wofford** | **UNSETTLED** |
| **P-308** | Tennis — US Open | Taylor Fritz vs Francisco Cerundolo | Pregame | **Francisco Cerundolo +6.5 games** | **Taylor Fritz** | **UNSETTLED** |
| **P-307** | Cricket — Women's Asia Cup T20 | India (W) vs Pakistan (W) | Research initiated; Pakistan won toss and elected to bat; user moved on before full card was issued | **NOT ISSUED** | **NOT ISSUED** | **INCOMPLETE / NO FINAL FORECAST ISSUED** |
| **P-306** | Soccer — EPL | Manchester City vs Coventry City | Start-crossed/original-line research view; post-start play excluded | **1H Over 0.5 goals** | **Manchester City** | **UNSETTLED / prospective evaluation quarantined** |

### Duplicate-event accounting rule

`P-316` and `P-317` are two issued views of the **same KBO event**. Preserve both cards, but do not count them as two distinct event units in event-level performance summaries. Any row-level comparison must explicitly state the view/version being graded.

## 1.2 Inherited evidence / contract-definition follow-ups from the September 6 Drive audit

The latest audit changelog says **13 follow-ups remain open**. They are administrative/evidence/definition items, not new forecasts and not events awaiting a score:

`P-126, P-148, P-149, P-166, P-176, P-178, P-179, P-200, P-217, P-233, P-234, P-235, P-274`

Primary categories:

- event identity/state conflict: `P-126`;
- derivative/corners evidence coverage gaps: `P-148, P-149, P-176, P-178, P-179, P-233, P-234, P-235`;
- contract/action-term closure candidates under `G36.1`: `P-166, P-200, P-217, P-274`.

**Drive inconsistency note:** the current `PREDICTION_LOG_COMBINED_2.md` snapshot text says “11 event records” while its own listed remaining items plus the September 6 audit changelog resolve to **13 follow-up items**. This mini-log preserves the explicit 13-item audit list and does not silently alter Drive.

---

# 2. SETTLED BASELINE / DO NOT RE-OPEN AUTOMATICALLY

The September 6 Drive audit closed the older P-294–P-305 continuation work and evidence gaps that were previously present in the P-317 local file. In particular:

- `P-304` Rank #1 (`1H Over 0.5`) settled **WIN**; Slavia potential winner correct.
- `P-305` Rank #1 (`Amsterdam Flames PP Over 51.5`, condition met) settled **WIN**; Amsterdam Flames potential winner correct.
- `P-300` ECR powerplay recovered as **28 runs / 3 wickets**; PP Over 50.5 lost, PP Under 50.5 won.
- `P-302-C01` Bournemouth corners recovered as **3**; Over 2.5 won.
- `P-273` Palermo corners recovered as **3**; Over 4.5 lost.
- `P-151` Boca corners recovered as **11**; Over 4.5 won.

These settled facts are inherited learning/evidence and must not be duplicated as fresh forecasts in this continuation.

---

# 3. RUNNING-LOG RULE FOR EVERY NEW QUERY

For every new sports query from `P-318` onward:

1. **Refresh Drive first:** current canonical snapshot, `RULES_GENERAL.md`, `AGENT_ROLE_AND_TASK.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `LEARNING_REGISTER.md`, `DATA_SOURCE_REGISTER.md`, and the relevant sport/competition rules.
2. **Reconcile IDs without rewriting history:** preserve local issued P-306–P-317; if Drive has since imported them, use the canonical mapping it records. Otherwise continue the local non-reuse sequence.
3. **Keep incomplete/unsettled records at the top.** Do not move a card into its chronological settled section until the requested settlement protocol has produced a complete result/contract disposition.
4. **Do not automatically perform a retrospective unless requested.** A status check may identify that an event is final, but retrospective analysis remains a deliberate settlement task unless the current user instruction explicitly asks for it.
5. **Freeze the exact target before directional research:** event, participant, phase, interval, line, endpoint, rules era, operator/standard settlement assumptions and state.
6. **Use field owners for volatile facts:** official league/team/tournament sources for schedule, state, lineups/XIs/starters, rules and finals; specialist/structured endpoints only for fields they actually own.
7. **Pre-register settlement evidence for derivative rows** wherever practical so the chosen row will later be gradable.
8. **Retrieve bench/coaching/rotation state** where relevant; enforce the Rank #1 block when the current rules require it.
9. **Build one coherent event corridor/distributional state** for winner, side, margin, total and phase rows; state overlap/push/nesting geometry.
10. **Record tail budget, total-row path geometry and rank gap** as required disclosures. Do not promote candidate weights without their prospective test passing.
11. **Rank supplied/valid rows uniquely from most likely to least likely.** No fabricated probabilities or confidence percentages.
12. **Record every decision-driving source** with URL/record, timing, role/field owned, missingness/conflict state and whether it was actually used.
13. **Archive the complete issued card before delivery** so no ranks are later lost.
14. **Append the full new card and update the top queue in this file after every query.**

---

# 4. BASELINE SOURCE REGISTER — NEW CONTINUATION INITIALISATION

## Local source

| Source | Role |
|---|---|
| `PREDICTION_MINI_RUNNING_LOG_P317(2).md` | Immediate local predecessor; establishes issued P-306–P-317 records and next local slot P-318 |

## Google Drive sources read in this initialisation

| Source | Role / finding |
|---|---|
| `PREDICTION_LOG_COMBINED_2.md` | Canonical Drive queue/ID authority; September 6 v3.7 settlement snapshot; confirms older P-294–P-305 cohort settlement state |
| `PREDICTION_MINI_RUNNING_LOG_P317.md` | Drive copy of the prior local continuation; cross-checks P-306–P-317 queue and source state |
| `AUDIT_CHANGELOG_2026-09-06.md` | September 6 settlement/source audit; v3.7 patch plus same-day external blindspot addendum; records files changed, L-079–L-101 controls and 13 remaining follow-ups |
| `README.md` | Active-document map and same-day statement that the external blindspot amendments are dispositioned and method is now v3.8 in that addendum context |
| `RULES_GENERAL.md` | General hard gates / GFA-2; contains September 6 amendment content, while its fetched header remains stale at v3.6 |
| `LEARNING_REGISTER.md` | Current promoted/candidate control registry; confirms L-087–L-101 external-blindspot amendment section and control-taxonomy additions |

## Tool-source note

| Tool | Initialisation result |
|---|---|
| Wolfram `WolframContext` | Failed upstream MCP/SSE probe with HTTP 404; no evidence/computation used |
| Wolfram `WolframLanguageEvaluator` | Failed upstream MCP/SSE probe with HTTP 404; no evidence/computation used |

---

# 5. NEXT FORECAST SLOT

**Next local continuation ID after this issued card: `P-319`.**

P-318 is issued below and remains in the unsettled queue until a later explicit settlement/retrospective pass.

---

# P-318 — Henan vs Chengdu Rongcheng — 2026 China Super League Round 26

## Frozen identity / state

- **Venue:** Zhengzhou Hanghai Stadium, Zhengzhou, China.
- **Scheduled kickoff:** 2026-09-06 **19:35 CST / 21:35 AEST**.
- **Information cutoff:** **19:30:10 CST / 21:30:10 AEST**.
- **State at freeze:** **PREGAME / SCHEDULED** from structured event `68995376`.
- **Method:** latest September 6 control set (`v3.8` amendments with Drive metadata conflict disclosed) + `GFA-2` + `SFA-SOCCER`.
- **Numerical state:** Stage 0 / no fitted model.
- **Probability/value:** not generated; no calibrated probability, edge, ROI or stake.
- **Retrospective:** **deferred by user**.
- **Market-blind:** bookmaker prices, implied probabilities, line movement and consensus excluded.

### Frozen five-row slate

1. 1H **Over 0.5 goals**
2. 1H **Under 0.5 goals**
3. Full match **Over 2.5 goals**
4. Full match **Under 2.5 goals**
5. **Chengdu Rongcheng Over 4.5 team corners** — research-selected fifth row.

The fifth row is a derivative contract. The user's exact operator/provider corner definition was not supplied, so under `SO-P3` it is capped at `FORCED RANK / MEDIUM-LOW` even though the sporting evidence is usable. Post-match settlement source pre-registered: official/Opta-style final corner count, with FotMob/Opta as the intended structured cross-check.

## Precondition audit

| Gate | State | Effect |
|---|---|---|
| Competition / 90-minute endpoint | PASS | Regular-season CSL match; potential winner explicitly means regulation-time winner |
| Current XI / goalkeeper | PARTIAL-PASS | Current Henan XI recovered; current release confirms Wei Shihao and Rômulo start for Chengdu, but full Chengdu XI not independently exposed in retrievable pre-kickoff source |
| Bench / coaching / rotation | PARTIAL | Coaches Daniel Ramos and John Aloisi verified; both complete benches not recovered |
| Full-game Rank #1 gate | BLOCKED | `G14.2/L-082`: incomplete bench record means a full-match total cannot be Rank #1 |
| Corner provider definition | PARTIAL | Current corner evidence available; exact user operator definition unknown, so fifth row cannot receive LEAN/SUPPORTED |
| Schedule/state | PASS | Official club notice and structured source agree; state still Scheduled before cutoff |
| Weather | PARTIAL-PASS | Warm ~28–30°C, no strong immediate rain signal; no directional weather coefficient applied |

## Latest starting / availability evidence

### Henan current XI
Current lineup release:
- GK **Shi Chenglong**
- **Maidana**
- **Yeljan Shinar**
- **Lucas Maia**
- **Wang Shangyuan**
- **Bruno Nazario**
- **He Chao**
- **Huang Ruifeng**
- **Maranhao**
- **Gustavo**
- **Zheng Dalun**

This preserves the main Henan attacking chain: **Gustavo + Nazario + Maranhao**.

### Chengdu current state
- Current lineup release explicitly confirms **Wei Shihao** and **Rômulo** start.
- **Felipe is suspended** for accumulated yellow cards.
- Felipe is Chengdu's leading scorer: **17 league goals in 19 appearances** in current season records.
- A predicted Chengdu XI existed in preview material, but because it was not an actual release it is **not promoted to confirmed fact**.
- The remaining current Chengdu XI and complete bench were not independently recovered before the freeze and are left unresolved rather than invented.

### Personnel mechanism
Felipe's absence materially reduces Chengdu's direct penalty-box finishing and central target play. It does **not** remove their full creation structure because Wei Shihao and Rômulo start. Henan retain Gustavo and Nazario at home. This combination lowers confidence in a Chengdu blowout or automatic Over while leaving an early goal and sustained Chengdu territory live.

## Descriptive scoring baseline

### Henan
FBref entering this match:
- **8-7-9**
- goals **32 for / 34 against**
- **1.33 scored / 1.42 conceded**
- home **4-4-4**
- latest: **1-1 vs Chongqing Tonglianglong**

Recent five listed league scores:
- 1-1 Dalian Yingbo
- 0-0 Qingdao West Coast
- 1-4 Shanghai Shenhua
- 4-4 Liaoning Tieren
- 1-1 Chongqing Tonglianglong

### Chengdu
FBref entering this match:
- **15-6-4**, league leaders
- goals **51 for / 30 against**
- **2.04 scored / 1.20 conceded**
- away **7-3-2**
- latest: **2-1 vs Liaoning Tieren**

Last five:
- 1-1 Wuhan Three Towns
- 0-1 Yunnan Yukun
- 3-2 Zhejiang
- 4-5 Shanghai Shenhua
- 2-1 Liaoning Tieren

### Qualitative corridor
A non-fitted cross-regime sanity check puts the unadjusted combined centre around the high-2s. Felipe's suspension pulls the Chengdu finishing centre downward; Wei/Rômulo starting offsets part of that reduction.

Working corridor:
- Henan **1–2**
- Chengdu **1–2**
- total **2–4**
- ordinary score families: **1-1, 1-2, 2-1, 1-3**

Therefore the **2.5 total lies inside central support** and is not the strongest contract on the card.

## First-half goal audit

Recent listed H2H half-time states:
- 2026-05-09: Chengdu **1-0** Henan
- 2025-10-31: Chengdu **1-0** Henan
- 2025 FA Cup: **0-0**
- 2025-06-14: Henan **2-2** Chengdu
- 2024-09-21: Henan **1-0** Chengdu
- 2024-05-10: Chengdu **3-2** Henan

**5 of 6** contained at least one first-half goal. This is descriptive only, but it aligns with today's current participants.

Henan's latest home league match also had **Gustavo score at 17'**, making the half-time score 1-0 before the match finished 1-1.

### 1H Over mechanism
- Henan's current Gustavo/Nazario attack can create the first goal.
- Wei Shihao and Rômulo keep Chengdu's early chance creation intact despite Felipe's suspension.
- Chengdu have a championship-clinching incentive with a win, so a passive draw-protection opening is not the central tactical state.
- The first-half row is less dependent on unresolved bench depth than the full-match totals.

### 1H Over kill path
Chengdu can dominate territory but lack central conversion without Felipe, while Henan defend compactly and try to reach half-time level. That gives a real 0-0 branch, but it is not the central branch.

## Full-match 2.5 path geometry

### Over 2.5 paths
- Henan scores once and Chengdu still converts twice: **1-2 / 1-3**.
- Early goal opens score-state chasing and transition exposure.
- Chengdu have conceded **10 across their last five league games**, preserving an opponent-contribution path.
- Henan's recent 4-4 is an upper-tail example, not a centre.

### Under 2.5 paths
- Felipe absence turns Chengdu pressure into shots/corners without enough finishing.
- Henan's three latest listed home league scores are **1-1, 0-0, 1-1**, all Under 2.5.
- If Chengdu lead 1-0, title-security control can reduce late risk.
- Unresolved bench quality adds uncertainty to both directions.

**Conclusion:** Over 2.5 narrowly leads Under 2.5, but the rank gap is very small.

## Corner process — Chengdu Over 4.5 team corners

Current specialist samples:
- TotalCorner: Chengdu **6.29 corners for**, 4.29 against, total-match environment 10.58; first-half Chengdu corners 3.25.
- AccaPlanner: Chengdu **6.64 corners for**, 4.16 against, total 10.80.
- Henan recent corner profile: about **5.3 for / 4.8 against**, home for about 5.7.
- May 9 H2H: Chengdu **9 corners**, Henan 4; half-time corners **5-2 Chengdu**.

### Corner mechanism
Without Felipe, Chengdu can shift a greater share of attacks toward width, crosses, blocked deliveries and defensive clearances rather than direct central finishing. If level, the need to win preserves attacking exposure.

### Corner kill paths
- early Chengdu lead reduces later attacking demand;
- Henan dominate possession and force Chengdu into low-volume counterattacks;
- direct attacks end in clean shots/goals instead of blocked/cleared corner events.

Because the exact operator definition is unknown, the row stays `FORCED RANK` despite a strong sporting case.

## Conditions / incentive / coaching
- **Ramos (Henan)** explicitly said the side prepared specifically for Chengdu and acknowledged Felipe's absence.
- **Aloisi (Chengdu)** leads a side with a current championship-clinching opportunity if they win.
- Warm match conditions (~28–30°C) and no strong immediate rain signal do not provide a material suppression mechanism.
- Motivation is treated as tactical exposure context, not as an automatic scoring coefficient.

## Scenario / tail map

| Branch | Representative state | Favours |
|---|---|---|
| Early Chengdu breakthrough | HT 0-1 → FT 1-2 | 1H Over, FT Over, Chengdu |
| Henan early goal | HT 1-0 → FT 1-1 / 1-2 | 1H Over; total mixed |
| Felipe-driven conversion suppression | HT 0-0 → FT 0-1 / 1-1 | 1H Under, FT Under |
| Open two-sided game | HT 1-1 → FT 2-2 / 1-3 | both Overs |
| Chengdu territory, low finishing | 0-0/0-1 HT → 0-1/1-1 FT; 5–8 CHR corners | corner Over + FT Under |
| Early Chengdu lead/control | 0-1 HT → 0-1/0-2 FT | 1H Over + FT Under possible; corner risk |
| High-event tail | 1-3 / 2-3 | FT Over |
| Low-event tail | 0-0 / 1-0 | both Unders |

Aggregate-tail disclosure: the strongest high tail is an early goal propagating into chasing/transition exposure; the strongest low tail is Felipe's absence converting Chengdu pressure into non-goal events. The corner Over can therefore coexist coherently with an Under 2.5 state.

## Frozen ranking

| Rank | Contract | Verdict | Evidence | Reason |
|---:|---|---|---|---|
| **1** | **1H Over 0.5 goals** | **LEAN** | **MEDIUM** | Best definition integrity and least bench dependence; 5/6 recent listed H2H HT states had a goal; current attackers support the mechanism |
| **2** | **Chengdu Over 4.5 team corners** | **FORCED RANK** | **MEDIUM-LOW** | Current Chengdu corner-for rates ~6.3–6.6; 9 corners in May H2H; strong width/pressure mechanism, but exact operator definition missing |
| **3** | **Full Match Over 2.5 goals** | **FORCED RANK / slight direction** | **MEDIUM-LOW** | Season/recent scoring keeps 3+ live, but 2.5 is inside the central corridor and Felipe is out |
| **4** | **Full Match Under 2.5 goals** | **FORCED RANK** | **MEDIUM-LOW** | Felipe absence plus Henan's recent low-scoring home states; ranks just below Over because Wei/Rômulo start and both defensive tails are real |
| **5** | **1H Under 0.5 goals** | **FORCED RANK** | **LOW** | Genuine 0-0 HT branch, but weaker than current early-goal evidence |

### Rank gaps
- #1 → #2: **modest / real**
- #2 → #3: **small**
- #3 → #4: **very small**
- #4 → #5: **moderate**

## Potential winner

**Chengdu Rongcheng — slight 90-minute regulation lean.**

Why:
- 15-6-4 vs Henan 8-7-9;
- away 7-3-2;
- +21 season goal difference;
- win carries title-clinching incentive;
- Wei Shihao and Rômulo start.

Why only slight:
- Felipe (17 league goals) is suspended;
- Henan retain Gustavo/Nazario at home;
- Henan's recent home state is draw-heavy;
- Chengdu's recent defensive results are volatile.

No calibrated win probability is published.

## Source register — P-318

### Drive governing documents
- `RULES_SOCCER.md` — SFA-SOCCER, XI/bench/goal/corner/provider/score-state gates.
- `RULES_GENERAL.md` — GFA-2, timing, source hierarchy, G14.2, tail/path disclosures, no hindsight.
- `LEARNING_REGISTER.md` — current September 6 promoted/candidate controls.
- `PREDICTION_LOG_COMBINED_2.md` and this local mini-log — canonical/local queue authority.

### Current fixture / personnel
- Henan official Weibo fixture notice: https://weibo.com/2/detail/5339892545492301
- Henan official pre-match conference: https://weibo.com/2/detail/5339892779582856
- Structured soccer game record `68995376` — scheduled state / exact kickoff.
- Hupu current lineup release via hupu.com — current Henan XI and explicit Wei Shihao/Rômulo starting confirmation; full Chengdu XI/benches truncated in retrievable source.
- Qiumiwu Chengdu roster/injury page: https://www.qiumiwu.com/team/chengdurongcheng/roster — Felipe suspension.
- Current Chengdu title-context reporting from CSL/Sina feeds — win can clinch the title.

### Season / form / H2H
- FBref Henan 2026 schedule: https://fbref.com/en/squads/b037fc40/2026/matchlogs/c62/schedule/Henan-Scores-and-Fixtures-Chinese-Super-League
- FBref Chengdu 2026 schedule: https://fbref.com/en/squads/abbeb68a/2026/matchlogs/c62/schedule/Chengdu-Rongcheng-Scores-and-Fixtures-Chinese-Super-League
- FBref H2H: https://fbref.com/en/stathead/matchup/teams/b037fc40/abbeb68a/Henan-vs-Chengdu-Rongcheng-History
- AiScore H2H: https://www.aiscore.com/head-to-head/soccer-chengdu-rongcheng-vs-henan-fc
- GioScore Henan 1-1 Chongqing (Aug 29): https://gioscore.com/football/match/chongqing-tonglianglong-fc-henan-songshan-longmen/19674618

### Corners / settlement lane
- TotalCorner CSL table: https://www.totalcorner.com/league/corner_stats/116
- AccaPlanner CSL corners: https://www.accaplanner.com/league/china-super-league/corners/corners/
- TotalCorner May 9 H2H: https://www.totalcorner.com/stats/chengdu-rongcheng-vs-henan/193328008
- CornerEdge Henan profile: https://corneredge.bet/team/henan-jianye/corners/
- FotMob/Opta match lane: https://www.fotmob.com/ — intended later structured corner cross-check; user operator definition remains unknown.

### Weather
- Timeanddate Zhengzhou current conditions: https://www.timeanddate.com/worldclock/china/zhengzhou
- FotMob current match page — ~28°C / grass venue.

### Exclusions
Bookmaker odds, implied probabilities, line movement, prediction markets, tipsters, editorial picks, AI/simulated predictions and unconfirmed predicted lineups were excluded from the rank.

### Wolfram status
User explicitly invoked Wolfram. `WolframContext` was attempted for P-318 but returned an upstream MCP/SSE **HTTP 404**. **No Wolfram-derived fact, computation or probability was used.**

## Bottom line

1. **1H Over 0.5 goals**
2. **Chengdu Rongcheng Over 4.5 team corners**
3. **Full Match Over 2.5 goals**
4. **Full Match Under 2.5 goals**
5. **1H Under 0.5 goals**

**Potential winner:** Chengdu Rongcheng — slight regulation-time lean.

**P-318 status:** `PREGAME FORECAST ISSUED — UNSETTLED`  
**Retrospective:** deferred.  
**Next local slot:** `P-319`.


---

# P-319 — Yunnan Yukun vs Liaoning Ironman — 2026 China Super League Round 26

## 1. Frozen identity / state

| Field | Frozen value |
|---|---|
| Local continuation ID | `P-319` |
| Sport | Soccer |
| Competition | 2026 Chinese Super League — Round 26 |
| Event | Yunnan Yukun vs Liaoning Ironman / Liaoning Tieren |
| Venue | Yuxi Plateau Sports Center Stadium, Yuxi, Yunnan |
| Scheduled kickoff | 2026-09-06 19:35 CST / 21:35 AEST |
| Research initiation | Pre-kickoff |
| Final state refresh | **2026-09-06 21:35:37 AEST / 19:35:37 CST** |
| Verified state at final refresh | **LIVE, 0-0** |
| Exact match clock | **NOT EXPOSED by the returned structured record** |
| View type | **START-CROSSED / VERIFIED-LIVE 0-0 ORIGINAL-LINE VIEW** |
| Method | latest September 6 controls including `GFA-2 + SFA-SOCCER`, `L-079`–`L-101`; Drive metadata version conflict preserved |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Retrospective | **NOT PERFORMED — explicitly deferred** |

### Temporal-integrity note

The request arrived before the scheduled 21:35 AEST kickoff, but the scheduled start was crossed during research. The final structured soccer refresh at 21:35:37 AEST had switched the game to **Live, 0-0**. No goal, corner, shot, card or other live event was used to change the sporting thesis. Because the exact match clock was not exposed, this is **not labelled PREGAME** and is evidence-capped as a start-crossed original-line view.

## 2. Frozen decision set

The user supplied two paired goal targets and requested one additional corner market. The frozen five-row slate is:

1. **1st Half Over 0.5 goals**
2. **Total corners Over 8.5** — research-selected line; regulation + stoppage only
3. **Full Match Over 2.5 goals**
4. **Full Match Under 2.5 goals**
5. **1st Half Under 0.5 goals**

### Corner definition caveat

The user's exact sportsbook/stat-provider definition was not supplied. The sporting target is interpreted as **corners taken during 90 minutes plus stoppage time, excluding extra time**. Because the operator/provider is unknown, the corner row cannot exceed `FORCED RANK / MEDIUM-LOW` under `SO-P3`, even if the sporting direction is otherwise strong.

## 3. Current participant / availability / rotation audit

### Yunnan Yukun

No current injury was listed in the accessible same-day injury summary before issue.

The **latest fully confirmed XI/bench retrievable before this card** was Yunnan's 1-0 China FA Cup win over Chongqing Tonglianglong on 2 September:

**XI:** Wang Zhifeng; Tsui Wang-Kit, Yi Teng, Burcă; Xu Xin, Ionita, Hou Yongyong, Kayque; Oscar Taty Maritu, Huang Zichang, Bunyamin Abdusalam.

**Bench:** Bao Yaxiong, Yu Jianxian, Hu Ruibao, Shi Ke, Zhang Xiangshuo, Deng Hanwen, Zhang Chenliang, Zhao Yuhao, Duan Liuyu, Cleber, Han Zilong, Fernando.

Important workload context:
- Yunnan played the full cup quarter-final only four days earlier.
- Coach Jodi's pre-match camp explicitly described the week as **three matches in one week** and said recovery/adjustment had been the main training priority.
- Oscar, Ionita, Xu Xin, Hou Yongyong and other core players all started the cup match, so rotation/fatigue uncertainty is real.

The exact Sep 6 starting XI and bench were actively sought but not independently recoverable from a sufficiently authoritative indexed source before issue. Therefore no unverified predicted XI is promoted to fact.

### Liaoning Ironman

**Takahiro Kunimoto (邦本宜裕)** was listed as **suspended for accumulated yellow cards** for this fixture.

A current pre-match press conference supplied an important positive change: head coach Seo Jung-won stated that **Guy Mbenza is available again**, describing his return as a major attacking boost and saying it expands the team's tactical options.

The most recent fully confirmed league XI available in the source set was the Aug 29 match at Chengdu:
Zhang Yan; Dilmurat, Yuan Mincheng, Zhang Hongfu, Li Haoran; Yan Dinghao, Kunimoto, Felipe, Li Tixiang; An Yien, Jeffinho.

Bench: Xie Jintian, Pan Ximing, Chen Binbin, Zang Yifeng, Tian Yuda, Liu Guobo, Gao Jiarun, Xu Dong, Pang Shenghan, Tian Yinong, Tian De'ao.

That XI is **not** asserted as today's XI. It is a role/availability reference only. Today's key regime change is:
- Kunimoto out suspended;
- Mbenza back available.

### Participant gate result

`SO-P2 = PARTIAL`.

The exact current XIs, goalkeepers and full benches were not independently re-handshaken before issue. Under the Drive rules this:
- blocks a margin or full-match total from Rank #1;
- caps participant-sensitive rows;
- requires wider substitution/rotation tails.

## 4. Season goal environment

### Yunnan Yukun

Current league record before this match:
- 25 matches
- 49 scored
- 51 conceded
- 10-5-10
- home: 7-2-3, 26 scored / 19 conceded in 12

Descriptive scoring environment:
- overall combined goals in Yunnan league matches: **100 / 25 = 4.00**
- home combined environment: **45 / 12 = 3.75**

### Liaoning Ironman

Current league record:
- 24 matches
- 34 scored
- 41 conceded
- 7-4-13
- away: 1-3-7, 11 scored / 19 conceded in 11

Descriptive scoring environment:
- overall combined goals: **75 / 24 = 3.13**
- away combined environment: **30 / 11 = 2.73**

A simple home/away rate blend places the unadjusted joint scoring centre a little above three goals. This is diagnostic only, not a fitted probability model.

## 5. First-half scoring process

The same-day team data split goals by 15-minute blocks.

Yunnan:
- goals scored in first 45: **7 + 7 + 7 = 21**
- goals conceded in first 45: **5 + 7 + 9 = 21**
- total first-half goal events involving Yunnan: **42 across 25 league matches**

Liaoning:
- first-half goals scored: **4 + 4 + 3 = 11**
- first-half goals conceded: **9 + 8 + 5 = 22**
- total first-half goal events involving Liaoning: **33 across 24 league matches**

Recent half-time states support the same direction.

Yunnan latest five listed competitive matches:
- 1-0 Chongqing (FA Cup), HT **0-0**
- 0-6 Zhejiang, HT **0-5**
- 3-3 Beijing Guoan, HT **0-1**
- 3-1 Dalian, HT **0-1**
- 1-0 Chengdu, HT **0-0**

Liaoning latest five league matches:
- 1-2 at Chengdu, HT **0-1**
- 4-4 vs Henan, HT **0-2**
- 1-2 vs Shenzhen, HT **1-1**
- 0-1 at Dalian, HT **0-1**
- 3-1 vs Shanghai Shenhua, HT **2-0**

Thus Liaoning's last five all contained a first-half goal, while Yunnan's latest five contain both 0-0 and high-event first-half branches. The current mechanism is more important than the streak: Yunnan's home attack plus Liaoning's weak away defence, offset by Yunnan congestion and Kunimoto's absence.

## 6. Full-match scoring mechanism

### Over path

The clearest Over 2.5 mechanisms are:
- Yunnan's home attack against a Liaoning side conceding 19 in 11 away games;
- Liaoning's Mbenza return adding a central finishing/hold-up option;
- both teams' recent defensive volatility;
- an early goal forcing the trailing team into higher attacking exposure;
- Yunnan fatigue/rotation creating late defensive transition errors.

Recent league totals:
- Yunnan: 6, 6, 4, 1, 5, 7, 4, 7, 3, 6 across the listed last ten league games.
- Liaoning: 3, 8, 3, 1, 4, 1, 2, 4, 6, 5 across the listed last ten.

### Under path

The Under remains live because:
- Yunnan's last two home competitive games were 1-0 Chengdu and 1-0 Chongqing;
- Yunnan may show fatigue-driven attacking suppression rather than only defensive fatigue;
- Kunimoto's suspension removes a creative midfield piece for Liaoning;
- Liaoning away scoring is only 11 goals in 11 league matches;
- the first May meeting ended 2-1, exactly one goal above the line, so the threshold remains boundary-sensitive.

## 7. Corner process

### Season / recent corner environment

Current league corner data:
- Yunnan team corners: about **5.1 per match**
- Liaoning team corners: about **4.4 per match**
- Liaoning corners conceded: about **5.3 per match**
- Liaoning away total-corner environment: about **9.36**
- broader Yunnan match-corner environment: around **10.3–10.8**

Recent Yunnan match corner totals:
- vs Chongqing Cup: 4
- at Zhejiang: 10
- at Beijing: 14
- vs Dalian: 12
- vs Chengdu: 13

Recent Liaoning league corner totals:
- at Chengdu: 13
- vs Henan: 16
- vs Shenzhen: 11
- at Dalian: 9
- vs Shanghai Shenhua: 6

Recent four-league-match team corner counts:
- Yunnan: 3, 5, 9, 7
- Liaoning: 6, 8, 6, 3

Head-to-head:
- May 2026: 8 total corners
- Nov 2024: 11
- Jun 2024 at Yunnan: 18

### Corner mechanism

Over 8.5 is supported by:
- both teams currently averaging roughly 4–5+ corners;
- Liaoning conceding ~5 corners per match;
- Yunnan's home territorial edge;
- trailing-state width/crossing if Liaoning fall behind;
- Mbenza's return increasing box-target value for Liaoning wide delivery;
- recent league samples clustering around 9–16 total corners.

### Corner kill path

The main failure state is a low-event game where:
- Yunnan score early and manage territory without repeated end-line attacks;
- Liaoning lack sustained possession/width without Kunimoto;
- attacks terminate in clean shots/goals rather than blocks/clearances;
- the match resembles Yunnan's 1-0 cup win with only four total corners.

## 8. Weather / venue / incentive

Yuxi match-day sources indicated cloudy conditions, temperatures roughly in the high teens/low 20s around the evening and light winds, with no strong weather mechanism requiring a one-way goal/corner adjustment.

Yunnan's coach called the match important for league position before the break and for carrying momentum into the cup programme. Motivation is treated only as a tactical exposure context, not a coefficient.

## 9. Scenario / tail map

| Branch | Representative state | Favours |
|---|---|---|
| Yunnan territorial start | HT 1-0 → FT 2-1 / 3-1 | 1H Over, FT Over, Yunnan |
| Liaoning counter/Mbenza impact | HT 0-1 / 1-1 → FT 1-2 / 2-2 | both Overs; Liaoning upset tail |
| Low-conversion Yunnan control | HT 0-0 → FT 1-0 / 2-0 | both Unders; Yunnan |
| Early goal + open chase | HT 1-1 → FT 3-1 / 2-2 | both Overs + corner Over |
| Corner-heavy, low conversion | 0-0/1-0 HT → 1-1/2-0 FT with 9–13 corners | corner Over + FT Under possible |
| Congestion decay | close at 60' → late transition goals | FT Over |
| Kunimoto absence hurts Liaoning creation | Yunnan 1-0 / 2-0 | FT Under/Yunnan |
| Yunnan fatigue hurts press/defence | 1-1 → 2-2 / 2-3 | FT Over |

Aggregate-tail disclosure:
- high-goal tail: early goal + Yunnan congestion + Mbenza-enabled transition/box threat;
- low-goal tail: Yunnan controls at home while Liaoning's away attack suffers without Kunimoto;
- high-corner tail can coexist with either goal direction.

## 10. Frozen ranking — most likely to least likely

| Rank | Contract | Verdict | Evidence | Core reason |
|---:|---|---|---|---|
| **1** | **1st Half Over 0.5 goals** | **LEAN / START-CROSSED** | **MEDIUM-LOW** | Liaoning's last five all had a first-half goal; season first-half event rates are high enough to support the mechanism; least dependent on full-bench uncertainty |
| **2** | **Total Corners Over 8.5** | **FORCED RANK** | **MEDIUM-LOW** | Yunnan/Liaoning match environments centre near ~10 corners and recent league totals are frequently 9–16; exact operator/provider definition is missing |
| **3** | **Full Match Over 2.5 goals** | **FORCED RANK / LEAN DIRECTION** | **MEDIUM-LOW** | Yunnan home scoring plus Liaoning defensive/away weakness and recent high totals support 3+; bench/rotation uncertainty and current 0-0 live start-cross cap the row |
| **4** | **Full Match Under 2.5 goals** | **FORCED RANK** | **LOW–MEDIUM-LOW** | Liaoning away attack is modest, Kunimoto is suspended and Yunnan have two recent 1-0 home competitive wins; broader scoring environment still points above it |
| **5** | **1st Half Under 0.5 goals** | **FORCED RANK** | **LOW** | Real 0-0 HT branch exists, especially with Yunnan fatigue, but it conflicts with Liaoning's recent first-half pattern and season first-half event environment |

### Rank gaps
- #1 → #2: **small-to-moderate**
- #2 → #3: **small**
- #3 → #4: **moderate**
- #4 → #5: **small-to-moderate**

## 11. Potential winner

### **Yunnan Yukun — regulation-time lean**

Primary reasons:
- home record **7-2-3** versus Liaoning away **1-3-7**;
- Yunnan have 49 league goals versus Liaoning's 34;
- Yunnan won the first 2026 meeting **2-1 away**;
- Liaoning's Kunimoto suspension removes an important creator;
- Yunnan were reported with no current injury in the accessible same-day injury summary.

Why this is not strong:
- Yunnan are in a congested three-match week and used many core players in the Sep 2 cup tie;
- Mbenza is back for Liaoning;
- Yunnan conceded 6 at Zhejiang in the prior league match;
- exact current XIs/benches were not independently recovered.

No calibrated win probability is published.

## 12. Source register — P-319

### Drive governing documents
- `RULES_SOCCER.md` — SFA-SOCCER; participant, bench, goal, corner and provider-definition gates.
- `LEAGUE_RULES_SOCCER.md` — China Super League competition reference; 2026 China foreign-player-rule change noted in current reference.
- `RULES_GENERAL.md` — timing/state/source hierarchy, G14.2 bench/coaching, G20.2/G21.1/G26.1, no hindsight.
- `LEARNING_REGISTER.md` — September 6 promoted/candidate controls.
- local `PREDICTION_MINI_RUNNING_LOG_P318_UPDATED.md` — immediate continuation / P-319 handoff.

### Event identity / state
- Structured soccer schedule/game ID `68995374` — Yunnan Yukun vs Liaoning Tieren, scheduled 21:35 AEST.
- Final structured refresh at **21:35:37 AEST** — state switched to **Live, 0-0**.
- Chinese Super League official Weibo fixture notice surfaced through the CSL official feed.
- Sina CSL database: https://match.sports.sina.com.cn/football/csl/
- China schedule cross-checks from current CSL fixture sources.

### Personnel / injuries / coaching
- Qiumiwu same-day match/injury page: https://www.qiumiwu.com/game/112072522080
  - Kunimoto suspended;
  - season player/stat context.
- Qiumiwu injury article: https://www.qiumiwu.com/news/1999354624498
- PP Sports / current pre-match conference:
  https://www.ppsport.com/360news/news/2609368.html
  - Seo Jung-won says Mbenza is available again and materially helps the attack.
- Yunnan official-club pre-match conference republished by Sohu:
  https://m.sohu.com/a/1072295873_120815119
  - three-match week / recovery emphasis / match importance.
- Yunnan Sep 2 confirmed Cup XI/bench:
  https://news.zhibo8.com/zuqiu/2026-09-02/6a97cdc039f17native.htm
  https://news.zhibo8.com/zuqiu/2026-09-02/match2111562date2026vnative.htm
- Liaoning Aug 29 confirmed XI/bench:
  https://m.zhibo8.cc/news/web/zuqiu/2026-08-29/6a9295c8dac30native.htm

### Goal / form / H2H
- Qiumiwu same-day team season and 15-minute goal-distribution data:
  https://www.qiumiwu.com/game/112072522080
- Nowscore current standings/home-away record cross-check:
  https://m.nowscore.com/Analy/Analysis/2944812.htm
- TotalCorner H2H / latest five:
  https://www.totalcorner.com/h2h/liaoning-ironman-vs-yunnan-yukun
- 17500 Yunnan full 2026 result/HT sequence:
  https://m.17500.cn/zq/data-team/course-70422-0-0
- CFL official May H2H report:
  https://www.cfl-china.cn/zh/content/news/CLkv.html

### Corners
- TotalCorner current H2H / recent:
  https://www.totalcorner.com/h2h/liaoning-ironman-vs-yunnan-yukun
- TotalCorner Yunnan profile:
  https://www.totalcorner.com/team/view/120597
- FootyMetrics Liaoning:
  https://www.footymetrics.com/teams/327074-liaoning-tieren-fc
- ScanGoal CSL corner table:
  https://scangoal.com/stats/china-super-league-corner-stats-2026
- Research provider definition remains unknown from the user's operator; row capped accordingly.

### Weather
- China weather / Yuxi:
  https://yn.weather.com.cn/yuxi/index.shtml
- Yuxi local forecast mirrors used only as corroboration; no strong one-way weather sign assigned.

### Explicit exclusions
Bookmaker odds, implied probabilities, line movement, betting consensus, tipsters, AI/simulated forecasts and predicted lineups were excluded from the sporting rank.

### Wolfram status
The user explicitly invoked Wolfram. Both:
- `WolframContext`, and
- `WolframLanguageEvaluator`

were attempted for P-319 and returned upstream MCP/SSE **HTTP 404** errors. No Wolfram-derived statistic, probability or calculation is presented as successful.

## 13. Bottom line

1. **1st Half Over 0.5 goals**
2. **Total Corners Over 8.5**
3. **Full Match Over 2.5 goals**
4. **Full Match Under 2.5 goals**
5. **1st Half Under 0.5 goals**

**Potential winner:** **Yunnan Yukun — regulation-time lean.**

**P-319 status:** `START-CROSSED / VERIFIED LIVE 0-0 ORIGINAL-LINE VIEW — UNSETTLED`  
**Retrospective:** deferred.  
**Next local slot:** `P-333`.


---

# P-320 — Tianjin Jinmen Tigers vs Zhejiang — 2026 Chinese Super League Round 26

## 1. Frozen identity / state

| Field | Frozen value |
|---|---|
| Local continuation ID | `P-320` |
| Sport | Soccer |
| Competition | 2026 Chinese Super League — Round 26 |
| Event | Tianjin Jinmen Tigers vs Zhejiang Professional / Zhejiang FC |
| Venue | TEDA Football Stadium, Tianjin |
| User-estimated kickoff | 2026-09-06 21:35 AEST |
| Verified official kickoff | **2026-09-06 20:00 CST / 22:00 AEST** |
| Final structured state refresh | **2026-09-06 21:41:50 AEST** |
| Verified state | **PREGAME / Scheduled** |
| Game ID | `68995378` |
| Method | **MDS-2026.09.06-v3.8 process controls; GFA-2 + SFA-SOCCER; SPORTS_ONLY / MARKET_BLIND** |
| Numerical state | `NTS-2026.09.02-v0.3 — Stage 0 / no fitted soccer model` |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED` |
| Value state | `NO VALUE DETERMINABLE` |
| Retrospective | **NOT PERFORMED — explicitly deferred** |

### Timing correction

The user's estimated 21:35 AEST start was not used as the field-owner clock. Tianjin's official fixture page and multiple current CSL schedules list **20:00 China Standard Time**, which is **22:00 AEST**. The structured soccer schedule independently returned the same 12:00 UTC / 22:00 AEST start, so this card remained genuinely pregame at the final state refresh.

## 2. Competition/rules gate

The current Drive competition reference classifies the Chinese Super League as:
- 16 clubs;
- 30-match balanced calendar-year season;
- 3 points win / 1 draw / 0 loss;
- bottom two relegated;
- regulation league matches end after 90' + stoppage with a draw live;
- VAR in use;
- 2026 foreign-player rule recorded in the Drive reference as the changed "6655" regime, with exact match-registration/on-field application requiring seasonal verification.

No extra time or penalties apply to the regulation winner / goal / corner rows on this league card.

## 3. Frozen five-row decision set

1. **1st Half Over 0.5 goals**
2. **Zhejiang Over 4.5 team corners**
3. **Full Match Over 2.5 goals**
4. **Full Match Under 2.5 goals**
5. **1st Half Under 0.5 goals**

### Corner definition caveat

The user did not supply the sportsbook/stat-provider definition for corners. The target is interpreted as **Zhejiang regulation-time team corners, 90 minutes plus stoppage time, excluding any abandoned/void branches under operator terms**. Because the exact operator/provider is unknown, this derivative row is capped under `SO-P3` and cannot be labelled `SUPPORTED`.

## 4. Current personnel / injury / bench audit

### Tianjin Jinmen Tigers

**Confirmed unavailable:** Guilherme Schettine.

Source hierarchy resolution:
- one aggregator labelled Schettine as "suspended";
- higher-quality current Tianjin reporting, including the pre-match training report and coach context, states he is **injured**, did not take part in the final stadium session, and is expected to target the next Liaoning fixture.
- Therefore the card records **INJURED / OUT**, not suspended.

Why it matters:
- Tianjin had previously built a 5-3-2 attacking plan around **Schettine + Alberto Quiles**;
- Tianjin media report that his sudden injury disrupted attacking organisation;
- Tianjin have scored only **one goal in their last two league matches** since the disruption.

Latest fully confirmed prior XI, vs Qingdao West Coast on 29 Aug:
**Yan Bingliang; Yang Fan, Aitor Córdoba, Sun Ming Him; Xadas, Cristian Salvador, Huang Jiahui, Ba Dun, Wang Qiuming; Alberto Quiles, Xie Weijun.**

Prior bench:
Qi Yuxi, Wang Xianjun, Liu Shuai, Wu Xinghan, Liu Junxian, Ji Shengpan, Li Yongjia, Chen Zhexuan, Guo Hao, Shi Yan.

The exact Sep 6 XI and bench were repeatedly sought, including club/CSL, live match, indexed lineup and current news searches, but were **not independently retrievable as confirmed** before issue.

### Zhejiang

**Confirmed unavailable:** Cardoso.

Direct current coach statement:
- Ross Aloisi said Cardoso **cannot play** against Tianjin;
- Cardoso is expected to miss about **two weeks**.

This overrides the lower-quality same-day aggregator page that listed Zhejiang as having no injuries.

Latest fully confirmed prior XI, 6-0 vs Yunnan Yukun on 29 Aug:
**Zhao Bo; Liu Haofan, Xu Junchi, Sun Guowen, Lucas; Park Jin-seob; Marko Tolić, Cheng Jin, Alexandru Mitriță; Tao Qianglong, Wang Yudong.**

Prior bench:
Dong Chunyu, Huo Shenping, Wang Yang, Bao Shengxin, Wang Shiqin, Zhang Aihui, Qian Jiegei, Wu Wei, Zhang Jiaqi, Gao Di, Fang Hao, Ning Fangze.

That XI is used only as a latest role/system reference, **not claimed as today's starting XI**.

### Participant gate result

`SO-P2 = PARTIAL`.

Current XI/goalkeeper/full-bench handshake was not completed from a sufficiently authoritative indexed source before issue. Under the Drive controls:
- no side, handicap or full-game total can receive the strongest participant-backed label;
- full-game total and winner tails remain widened;
- the starting-XI regime may not be projected unchanged over 90 minutes.

## 5. Season / form scoring environment

### Tianjin
- league record: **7-8-9**
- goals: **33 for / 31 against** in 24
- home record: **3-4-5**
- season scoring: ~**1.38 per match**
- season conceding: ~**1.29 per match**
- last five league scores: **1-1, 0-0, 2-4, 1-2, 3-2**
- corresponding HT states: **0-1, 0-0, 0-2, 0-0, 0-1**

### Zhejiang
- league record: **9-6-9**
- goals: **40 for / 40 against** in 24
- away record: **3-3-6**
- season scoring/conceding: ~**1.67 / 1.67**
- last five league scores: **6-0, 1-1, 2-3, 1-2, 3-2**
- corresponding HT states: **5-0, 0-0, 2-1, 1-1, 1-0**

### First-half reconciliation

Across those latest five:
- Tianjin had a first-half goal in **3/5**;
- Zhejiang had a first-half goal in **4/5**;
- the first 2026 H2H finished **0-0 at half-time**, despite Zhejiang producing the stronger first-half chances.

Mechanism balance:
- Zhejiang's Mitriță/Tolić/Wang Yudong creation gives a credible early-goal path;
- Tianjin were explicitly criticised internally for starting slowly in the prior home match;
- but Schettine's absence can reduce Tianjin contribution, and the May H2H demonstrates a real low-conversion first-half branch.

## 6. Full-match goal process

### Over 2.5 path
- Zhejiang's last five league matches produced **6, 2, 5, 3, 5 total goals**;
- Tianjin's last five produced **2, 0, 6, 3, 5**;
- Zhejiang just scored six against Yunnan, with Mitriță and Tolić driving an extremely productive attacking game;
- Tianjin are under major relegation pressure and cannot simply treat a home draw as ideal;
- an early goal forces a more open chase state.

### Under 2.5 path
- Schettine is unavailable and Tianjin have scored once in their last two league games;
- Cardoso is unavailable for Zhejiang;
- Tianjin's coach explicitly prioritised defensive preparation against Zhejiang's stronger attack;
- the May meeting was 0-0 until the 81st minute and finished 1-1;
- Zhejiang's away record is only **3-3-6**, materially weaker than their overall attacking reputation.

### Path geometry
The 2.5 line sits close to the current qualitative centre. Over is preferred, but the Under branch is too substantial for a strong gap.

## 7. Corner process

Current 2026 league corner rates:
- **Zhejiang:** 5.50 corners for, 4.75 against, **10.25 combined**
- **Tianjin:** 4.33 for, 5.79 against, **10.12 combined**

Opponent-conditioned Zhejiang corner corridor:
- own baseline: **5.50**
- Tianjin opponent-conceded baseline: **5.79**
- simple descriptive midpoint: ~**5.65 Zhejiang corners**

Recent Zhejiang team-corner counts:
- 7 vs Yunnan
- 7 at Shenzhen
- 6 vs Chengdu
- 8 at Beijing
- 3 vs Dalian

Recent Tianjin corners conceded:
- 6 vs Qingdao West Coast
- 12 at Wuhan
- 1 vs Beijing Guoan
- 5 at Shandong
- 5 vs Yunnan

The first 2026 H2H produced **6 Zhejiang corners**, despite ending only 1-1.

### Why Zhejiang Over 4.5 team corners
- direct corner exposure is stronger than using goal dominance as a proxy;
- Zhejiang average above the threshold;
- Tianjin concede one of the higher corner rates in the league;
- Zhejiang have cleared 4.5 in four of their latest five;
- if Tianjin score first or protect a draw, Zhejiang width/territory should increase corner-causing events.

### Corner kill paths
- Zhejiang score early and reduce width/end-line demand;
- Tianjin allow central progression rather than forcing wide recycle;
- efficient finishing terminates attacks as goals/shots rather than blocks/clearances;
- exact operator/provider definition differs from the assumed team-corner settlement.

## 8. Weather / venue

Tianjin's official match-day post stated an expected **25°C feels-like temperature** at the stadium.

Independent forecasts were broadly consistent on ~25°C around 20:00 local, light-to-moderate breeze and some chance of evening showers/cloud. No weather sign was strong enough to reverse the ranking.

Potential weather mechanism:
- light rain could marginally increase slick-surface transition variance and defensive handling errors;
- there is no evidence of extreme wind, heat or heavy precipitation sufficient for a one-way goal/corner adjustment.

## 9. Incentive / tactical state

Tianjin:
- are in a relegation fight after a points deduction;
- coach Yu Genwei described the match as requiring concentration, unity and improved defensive execution;
- Tianjin media described the remaining home fixtures as critical.

Zhejiang:
- are mid-table but remain the stronger attacking roster by Tianjin's own coach's assessment;
- Ross Aloisi wants the side to carry the intensity/confidence from the 6-0 win;
- Cardoso's absence removes one attacking option but does not remove the Mitriță/Tolić/Wang Yudong creation core.

Motivation is treated as an exposure/state input only, not as a directional coefficient.

## 10. Scenario / tail map

| Branch | Representative path | Favours |
|---|---|---|
| Zhejiang fast start | HT 0-1 / 1-1 → FT 1-2 / 1-3 | 1H Over, FT Over, Zhejiang |
| Tianjin defensive discipline | HT 0-0 → FT 0-1 / 1-1 | 1H Under, FT Under |
| Relegation-pressure home response | HT 1-0 → FT 1-1 / 2-1 | 1H Over, Tianjin upset tail |
| Open transition game | HT 1-1 → FT 2-2 / 2-3 | both Overs |
| Zhejiang territorial control, low conversion | HT 0-0 → FT 0-1 / 1-1 with 5–8 Zhejiang corners | Zhejiang corners + goal Under |
| Zhejiang chasing state | Tianjin score first → Zhejiang 6–9 team corners | Zhejiang corner Over |
| Efficient early Zhejiang finishing | Zhejiang lead without many blocked attacks | goals Over possible, corner Over kill path |

Aggregate tails are explicitly disclosed rather than used as fitted weights.

## 11. Frozen rank order

| Rank | Contract | Verdict | Evidence | Core rationale |
|---:|---|---|---|---|
| **1** | **1st Half Over 0.5 goals** | **LEAN** | **MEDIUM** | Zhejiang first-half event rate is strong in recent form; Tianjin have conceded a first-half goal in 3/5 recent league matches; less dependent on unverified full benches than the full-game rows |
| **2** | **Zhejiang Over 4.5 team corners** | **FORCED RANK** | **MEDIUM-LOW** | 5.50 own corners + Tianjin 5.79 conceded, 4/5 recent clearance, May H2H Zhejiang 6 corners; exact provider definition missing |
| **3** | **Full Match Over 2.5 goals** | **FORCED RANK / preferred direction** | **MEDIUM-LOW** | recent combined scoring environments are elevated and Zhejiang retain major creators; both current striker absences and unresolved benches prevent stronger status |
| **4** | **Full Match Under 2.5 goals** | **FORCED RANK** | **MEDIUM-LOW** | Schettine/Cardoso absences, Tianjin defensive emphasis, previous H2H 1-1; broader current scoring environment still puts it below the Over |
| **5** | **1st Half Under 0.5 goals** | **FORCED RANK** | **LOW–MEDIUM-LOW** | May H2H and two of Tianjin's last five produced 0-0 HT, but recent Zhejiang first-half creation makes this the weaker side |

### Rank gaps
- #1 → #2: **small**
- #2 → #3: **small**
- #3 → #4: **small-to-moderate**
- #4 → #5: **small**

## 12. Potential winner

### **Zhejiang — slight regulation-time lean**

Why Zhejiang:
- stronger current chance-creation/attacking profile;
- 40 league goals versus Tianjin's 33;
- Tianjin coach publicly described Zhejiang's overall roster strength as higher;
- Mitriță, Tolić and Wang Yudong remain the key current attacking references;
- Tianjin's Schettine absence has already disrupted the preferred front-two structure.

Why the lean is only slight:
- Zhejiang are **3-3-6 away**;
- Tianjin are at home in a high-stakes relegation match;
- Zhejiang also lose Cardoso;
- exact current XI/bench confirmation remains unresolved;
- the first 2026 meeting was a 1-1 draw.

Most coherent score families:
1. **Tianjin 1-2 Zhejiang**
2. **1-1**
3. **2-2**
4. Tianjin upset tail **2-1**

No calibrated win probability is published.

## 13. Source register — P-320

### Google Drive governing sources
- `RULES_SOCCER.md` — current SFA-SOCCER participant, goal, corner and settlement gates.
- `LEAGUE_RULES_SOCCER.md` — Chinese Super League competition reference; regulation-league endpoint, format, VAR and 2026 foreign-player-rule note.
- `RULES_GENERAL.md` — timing, participant/bench, source hierarchy, tail/path/rank-gap and no-hindsight controls.
- `LEARNING_REGISTER.md` — September 6 `L-087`–`L-101` governance amendments; README/search evidence identifies method as v3.8.
- local `PREDICTION_MINI_RUNNING_LOG_P319_UPDATED.md` — immediate append-only handoff.

### Identity / schedule / official state
- Tianjin official fixture page:
  https://www.tianjinfc.com/fixtures.html
- Tianjin official/club match preview republished by Zhibo8:
  https://news.zhibo8.com/zuqiu/2026-09-05/6a9c1bb23689cnative.htm
- CSL/Sina fixture database:
  https://match.sports.sina.com.cn/football/csl/
- structured soccer game ID `68995378`, final refresh remained Scheduled for 12:00 UTC / 22:00 AEST.

### Personnel / injuries / coaching
- Tianjin Daily / current pre-match report:
  https://k.sina.com.cn/article_5953190046_162d6789e06703r8ry.html
- Tianjin coach pre-match comments:
  https://www.ppsports.com/article/news/2609430.html
- Zhejiang coach Ross Aloisi confirms Cardoso out ~2 weeks:
  https://news.zhibo8.com/zuqiu/2026-09-05/6a9bf77581843native.htm
- Lower-quality injury aggregator retained as conflict evidence:
  https://www.qiumiwu.com/news/1999357412168
- Tianjin prior confirmed XI/bench vs Qingdao West Coast:
  https://news.zhibo8.com/zuqiu/2026-08-29/6a928b7482256native.htm
- Zhejiang prior confirmed XI/bench vs Yunnan:
  https://news.zhibo8.com/zuqiu/2026-08-29/6a9287de64faanative.htm

### Goals / standings / form / H2H
- FBref Tianjin:
  https://fbref.com/en/squads/42dff5fb/Tianjin-TEDA-Stats
- FBref Zhejiang:
  https://fbref.com/en/squads/8d9bcfa3/2026/c62/Zhejiang-Professional-Stats-Chinese-Super-League
- Qiumiwu same-day season data:
  https://www.qiumiwu.com/game/112074276149
- Zhejiang official/CFL May 1-1 report:
  https://www.cfl-china.cn/zh/content/news/CLkv.html
- Zhejiang club May report:
  https://www.zhejiangfc.com/2026/05/55915.html
- TotalCorner May H2H field:
  https://www.totalcorner.com/stats/zhejiang-vs-tianjin-jinmen-tigers/193328038

### Corners
- 2026 CSL corner table:
  https://www.totalcorner.com/league/corner_stats/116
- Zhejiang profile:
  https://www.totalcorner.com/team/view/13579
- Tianjin profile:
  https://www.totalcorner.com/team/view/82046
- Current H2H/recent corner record:
  https://www.totalcorner.com/h2h/tianjin-jinmen-tigers-vs-zhejiang
- Exact operator/provider definition: **NOT SUPPLIED / UNKNOWN**, therefore row capped.

### Weather
- Tianjin official match-day post: 25°C feels-like at match time.
- Met Office Tianjin hourly forecast:
  https://weather.metoffice.gov.uk/forecast/wwgqderhu
- FotMob venue/weather corroboration:
  https://www.fotmob.com/zh-Hans/matches/tianjin-jinmen-tiger-vs-zhejiang-professional/pld4pn

### Explicit exclusions
Bookmaker prices, implied probabilities, line movement, tipsters, betting-consensus pages, AI/synthetic predictions and predicted lineups were excluded from the sporting ranking.

## 14. Bottom line

1. **1st Half Over 0.5 goals**
2. **Zhejiang Over 4.5 team corners**
3. **Full Match Over 2.5 goals**
4. **Full Match Under 2.5 goals**
5. **1st Half Under 0.5 goals**

**Potential winner:** **Zhejiang — slight regulation-time lean.**

**P-320 status:** `PREGAME — UNSETTLED`  
**Retrospective:** deferred.  
**Next local slot:** `P-321`.


---

# P-321 — Sønderjyske vs AC Horsens — 2026-27 Danish Superliga Round 7

## 1. Frozen identity / state

| Field | Frozen value |
|---|---|
| Local continuation ID | `P-321` |
| Sport | Soccer |
| Competition | Denmark 3F Superliga — 2026-27 regular season, Round 7 |
| Event | Sønderjyske Fodbold vs AC Horsens |
| Venue | AL Sydbank Park, Haderslev |
| Verified kickoff | **2026-09-06 14:00 CEST / 22:00 AEST** |
| Final structured state refresh | **2026-09-06 21:57:49 AEST** |
| Verified state | **PREGAME / Scheduled** |
| Structured game ID | `71925004` |
| Method | **MDS-2026.09.06-v3.8 process controls; GFA-2 + SFA-SOCCER; SPORTS_ONLY / MARKET_BLIND** |
| Numerical state | `NTS-2026.09.02-v0.3 — Stage 0 / no fitted soccer model` |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED` |
| Value state | `NO VALUE DETERMINABLE` |
| Retrospective | **NOT PERFORMED — explicitly deferred** |

## 2. Competition / contract gate

Drive competition reference for Denmark Superliga:
- 12 clubs.
- Regular season is a 22-match double round robin.
- Table then splits into top-six championship and bottom-six qualification/relegation groups, with points carried in full.
- Regulation league match ends after 90 minutes plus stoppage; a draw is a live result.
- Standard 1X2/winner, goal and corner contracts refer to regulation time unless the user's operator says otherwise.

This fixture is Round 7 of the regular season, not a cup tie.

## 3. Frozen five-row slate

1. **1st Half Over 0.5 goals**
2. **Total Match Corners Over 9.5**
3. **Full Match Over 2.5 goals**
4. **Full Match Under 2.5 goals**
5. **1st Half Under 0.5 goals**

### Corner settlement definition

User did not provide the sportsbook/stat-provider definition. The sporting target is interpreted as **total corners taken by both teams in 90 minutes plus stoppage time**. Exact provider/operator settlement remains unknown, so the corner row is capped at `FORCED RANK / MEDIUM-LOW` under `SO-P3`.

## 4. Current participant / injury / rotation audit

### AC Horsens — current official squad retrieved

AC Horsens published a 20-player matchday squad on 6 Sep 2026:

1 Matej Delac  
6 Jakob Bonde  
7 Ivan Milicevic  
11 Kelvin Ehibhatiomhan  
14 Julius Madsen  
15 Adrian Justinussen  
16 Abdul Moro  
17 Adam Herdonsson  
18 Julius Körkkö  
19 Jimi Tauriainen  
20 Karlo Lusavec  
22 John Batigi  
24 Ole Martin Kolskogen  
26 Victor Palsson  
27 Yamirou Ouorou  
28 Alagie Saine  
30 Seniko Doua  
31 Anders Hoff  
35 Mikkel Kupijbida  
40 Ismaila Ceesay

Important current changes:
- **Jakob Bonde** is in the squad and can debut after joining from OB.
- **Ismaila Ceesay** from the U19 squad can debut.
- **Kristian Kirkegaard is no longer an AC Horsens player**, having been sold to Silkeborg on 1 Sep; predicted-lineup pages still listing him are therefore stale and were not promoted.
- **Christian Vestergaard** is listed with a knee injury and is unavailable in current injury coverage.

Latest tactical reference before today:
- Horsens have generally used **4-2-3-1**.
- Kelvin Ehibhatiomhan is the key current scorer, with **3 league goals in 5 appearances** in the current pre-match dataset.
- Jimi Tauriainen has been an important creator.

### Sønderjyske — current availability only partially resolved

Current injury/suspension coverage:
- **Brynjar Ingi Bjarnason — suspended**.
- **Mathias Olesen — injured / day-to-day**.
- FotMob also lists **Christian Vestergaard** on the AC Horsens side with a long-term knee injury.

Latest official Sønderjyske league squad recovered was the 20-player squad for FC København on 31 Aug:
Nicolai Flø, Alexander Munksgaard, Daniel Grétarsson, Rasmus Vinderslev, Sefer Emini,
Mohamed Cherif, Matthew Hoppe, Maxime Soulas, Dalton Wilkins, Lirim Qamili, Anders Hoeg,
Pachanga Kristensen, Andreas Oggesen, Ebube Duru, Brynjar Ingi Bjarnason, Bubacarr Tambedou,
Berkant Bayrak, Ismail Seydi, David Frimpong, Jacob Christensen.

Cup-load context:
- Sønderjyske played at Thisted on **3 Sep**, only three days before this league game.
- Club coach Fatah Abdirahman explicitly said the team had **three matches in the week** and would manage form/physical niggles.
- The cup trip was roughly **500 km round trip**.
- Sønderjyske used a strong squad and won 2-0, with Sefer Emini and Bubacarr Tambedou scoring.
- AC Horsens played its cup game earlier, on **1 Sep**, winning 4-0 at IF Lyseng, giving Horsens the better rest window.

### Participant gate

`SO-P2 = PARTIAL`.

The exact current Sønderjyske starting XI, goalkeeper and full bench were not independently retrieved from a field-owning source before freeze. AC Horsens' official matchday squad was retrieved, but its final starting XI was not.

Therefore:
- side/full-match-total confidence remains capped;
- prior predicted lineups are not treated as confirmed;
- substitution and second-half uncertainty is widened.

## 5. Current table / goal environment

### Sønderjyske
- **12th / 12**
- 1 point from 6
- **0-1-5**
- goals **5 for / 13 against**
- current league match goal environment: **18 / 6 = 3.00 total goals per match**

League results:
- 2-3 vs Midtjylland
- 0-1 at OB
- 0-0 vs Viborg
- 2-3 at Brøndby
- 0-3 vs Nordsjælland
- 1-3 at FC København

### AC Horsens
- **6th / 12**
- 7 points from 6
- **2-1-3**
- goals **8 for / 10 against**
- current league match goal environment: **18 / 6 = 3.00 total goals per match**

League results:
- 1-1 vs Nordsjælland
- 1-2 at Midtjylland
- 0-2 vs Brøndby
- 2-1 at OB
- 2-1 vs Lyngby
- 2-3 vs Viborg

Sønderjyske are winless and bottom; Horsens' current top-flight results are materially stronger, but both six-match samples remain early-season and must be shrunk.

## 6. First-half goal process

Sønderjyske half-time states:
- vs Midtjylland: **2-2**
- at OB: **0-0**
- vs Viborg: **0-0**
- at Brøndby: **0-3**
- vs Nordsjælland: **0-1**
- at FC København: **1-2**

Thus **4/6** Sønderjyske league matches contained at least one first-half goal.

AC Horsens current data show a **first-half opener in all 6 league matches**. Recent explicit HT examples:
- vs Viborg: **0-2**
- vs Lyngby: **1-0**
- at OB: match was already **1-1 before half-time**

Mechanisms supporting 1H Over 0.5:
- Sønderjyske have conceded 13 goals in six and have repeatedly allowed opponents to control the first half.
- Horsens have opened every current league match into a non-zero first-half state.
- Sønderjyske are under table pressure at home and cannot comfortably play a low-risk long-duration draw.
- Ehibhatiomhan gives Horsens a current central scoring outlet.

Kill paths:
- Sønderjyske's 0-0 HT against both OB and Viborg.
- Thursday cup load may suppress Sønderjyske early intensity.
- Horsens are an away promoted side and may choose to manage the first 20-30 minutes.
- Exact current XIs are not fully resolved.

## 7. Full-match total process

### Over 2.5 paths

Current league Overs:
- Sønderjyske: 4/6 matches finished with 3+ goals.
- Horsens: 4/6 finished with 3+ goals.

Mechanisms:
- Sønderjyske are conceding **2.17 goals per match** through six.
- Horsens have scored 2 in each of their last three league games.
- If Horsens lead, Sønderjyske must increase exposure at home, opening transition space.
- If Sønderjyske score first, Horsens' recent 4-2-3-1 attacking structure has enough threat to force a chase state.

### Under 2.5 paths

- Sønderjyske produced 0-1 and 0-0 in Rounds 2-3.
- Horsens had 1-1 and 0-2 in two of six.
- Sønderjyske's shorter rest may lower attacking output rather than only increase defensive errors.
- Current injury/suspension and current-XI incompleteness create uncertainty in the attacking allocation.
- Early-season scoring outcomes remain noisy under the Drive shrinkage rule.

The 2.5 line sits near the current qualitative centre; the Over is preferred but not by a large margin.

## 8. Corner process

Current Superliga corner data:

### Sønderjyske
- **4.67 corners for**
- **6.50 conceded**
- **11.17 total corners per match**
- home: about **5.0 for / 5.0 against**
- current match totals: 9, 16, 11, 11, 10, 10
- **5/6** league matches have reached 10+ corners

### AC Horsens
- **3.00 corners for**
- **8.33 conceded**
- **11.33 total corners per match**
- away match average around **11.0**
- current match totals: 17, 10, 10, 12, 11, 9
- **5/6** league matches have reached 10+ corners

### Why match Over 9.5 rather than an AC team-corner Over

The direct target-event evidence says the strongest repeatable feature is **both teams conceding many corners**, especially AC Horsens' 8.33 conceded per match. Horsens themselves win only 3.0 per match, so a team-corner Over for AC would wrongly transfer opponent defensive pressure into Horsens attacking-corner production.

Match total Over 9.5 better matches the mechanism:
- Sønderjyske home team-corner rate around 5;
- Horsens extremely high corners conceded;
- Sønderjyske also concede 6.5;
- both current match environments are above 11 corners.

Kill paths:
- early clean finishing reduces blocked/cross/end-line events;
- Horsens score first and drop into compact protection;
- Sønderjyske's fatigue suppresses territorial volume;
- the exact operator/provider settlement definition remains unknown.

## 9. Rest / congestion

This is a meaningful asymmetry.

### Sønderjyske
- league match at FCK: Aug 31
- cup at Thisted: Sep 3
- Horsens league match: Sep 6
- coach explicitly described **three matches in one week**
- roughly **500 km round-trip** for the Thisted cup tie

### AC Horsens
- league vs Viborg: Aug 28
- cup at IF Lyseng: Sep 1
- Sønderjyske league: Sep 6

Horsens have approximately two extra days since their cup fixture and did not have the same Thursday-to-Sunday turnaround.

This supports Horsens later-game freshness, but it is not converted into a numerical coefficient.

## 10. Weather / surface context

Haderslev forecast around 14:00 local:
- roughly **18°C / 65°F**
- mostly sunny / sunny intervals
- precipitation risk around **10% or lower**
- moderate westerly wind, with other current services around 20-25 km/h

No heavy rain or extreme heat mechanism was found. The wind is worth noting for high balls/crosses, but not strong enough to impose a one-way goal or corner adjustment.

## 11. H2H treatment

Sønderjyske have won the last four direct meetings, including a 4-1 win in March 2024.

This is **descriptive only**:
- the latest meeting was in a different season and lower-division context;
- Horsens have since been promoted and materially changed the squad;
- old H2H does not outweigh current participant/form/rest evidence under the Drive rules.

## 12. Frozen ranking — most likely to least likely

| Rank | Contract | Verdict | Evidence | Core reason |
|---:|---|---|---|---|
| **1** | **1st Half Over 0.5 goals** | **LEAN** | **MEDIUM** | Horsens have had a first-half opener in all six current league matches; Sønderjyske are 4/6; current defensive and table-state mechanisms support an early event |
| **2** | **Total Match Corners Over 9.5** | **FORCED RANK** | **MEDIUM-LOW** | both current match environments are ~11 corners; 5/6 for each side reached 10+; exact provider definition missing |
| **3** | **Full Match Over 2.5 goals** | **FORCED RANK / preferred direction** | **MEDIUM-LOW** | 4/6 Overs for each; Sønderjyske defensive leakage and Horsens recent scoring support 3+; XI/rest uncertainty caps it |
| **4** | **Full Match Under 2.5 goals** | **FORCED RANK** | **LOW–MEDIUM-LOW** | low-event branches exist through Sønderjyske fatigue and early-season variance, but current combined scoring environment points above |
| **5** | **1st Half Under 0.5 goals** | **FORCED RANK** | **LOW** | supported by two Sønderjyske 0-0 HTs, but conflicts with Horsens' 6/6 first-half opener sequence |

### Rank gaps
- #1 → #2: **small-to-moderate**
- #2 → #3: **small**
- #3 → #4: **small-to-moderate**
- #4 → #5: **moderate**

## 13. Potential winner

### **AC Horsens — slight regulation-time lean**

Why Horsens:
- 7 points versus Sønderjyske's 1.
- 8-10 goal difference versus 5-13.
- Horsens have won two of the last three league matches.
- Sønderjyske are 0-1-5 and have conceded 13.
- Horsens have the superior rest window after the cup round.
- Horsens' official current matchday squad is known and includes fresh options Bonde/Ceesay.

Why only slight:
- Sønderjyske are at home.
- Old H2H strongly favours Sønderjyske, even though it is downweighted.
- Exact current starting XIs/benches were not fully confirmed.
- Horsens have conceded 10 in six and lost 2-3 to Viborg last league outing.
- Early-season sample sizes remain small.

Most coherent score families:
- **Sønderjyske 1-2 AC Horsens**
- **1-1**
- **1-3**
- lower-event branch **0-1**

No calibrated win probability is published.

## 14. Source register — P-321

### Google Drive governing documents
- `RULES_SOCCER.md` — current SFA-SOCCER participant, goal, corner and provider-definition gates.
- `LEAGUE_RULES_SOCCER.md` — Denmark Superliga split format / regulation endpoint.
- `RULES_GENERAL.md` — current source/timing/bench/path/tail/rank controls.
- `LEARNING_REGISTER.md` — latest Sep 6 governance controls; operational method v3.8.
- local `PREDICTION_MINI_RUNNING_LOG_P320_UPDATED.md` — immediate append-only handoff.

### Event identity / state
- Sønderjyske official fixture schedule:
  https://soenderjyskefodbold.dk/de-syv-foerste-3f-superliga-kampe-i-2026-2027-saesonen-er-fastlagt/
- Sønderjyske official AC Horsens event page:
  https://soenderjyskefodbold.dk/alle-samarbejdsklubber-inviteres-gratis-til-ac-horsens-kampen/
- AC Horsens official squad page:
  https://achorsens.dk/nyheder/2026/8-august/truppen-mod-sonderjyske
- Structured soccer schedule/game ID `71925004`, final pregame refresh 21:57:49 AEST remained Scheduled.

### Personnel / injuries / squad changes
- AC Horsens official current squad:
  https://achorsens.dk/nyheder/2026/8-august/truppen-mod-sonderjyske
- AC Horsens official news index, current transfers:
  https://achorsens.dk/
- FotMob current injury/suspension listing:
  https://www.fotmob.com/matches/sonderjyske-vs-ac-horsens/2rpq55
- Sønderjyske official Aug 31 squad:
  https://soenderjyskefodbold.dk/truppen-mod-fc-koebenhavn-3/
- Sønderjyske official Sep 3 cup squad:
  https://soenderjyskefodbold.dk/pokaltruppen-mod-thisted-fc/

### Rest / recent match context
- Sønderjyske official training schedule:
  https://soenderjyskefodbold.dk/traeningstider/
- Sønderjyske official cup preview:
  https://soenderjyskefodbold.dk/optakt-thisted-fc-er-foerste-stop-i-betano-pokalen/
- Sønderjyske official 2-0 cup report:
  https://soenderjyskefodbold.dk/avancement-trods-boevlet-forestilling-mod-nord/
- AC Horsens official Sep 6 squad article records both teams' cup wins and dates.

### Table / goals / form
- Sky Sports current Superliga table:
  https://www.skysports.com/football/sonderjyske-vs-ac-horsens/table/556152
- FBref Horsens current season:
  https://fbref.com/en/squads/60e145ad/2026-2027/matchlogs/all_comps/schedule/Horsens-Scores-and-Fixtures-All-Competitions
- BetExplorer Sønderjyske score/HT sequence:
  https://www.betexplorer.com/football/team/sonderjyske/42ectuVa/results/
- WinDrawWin current team result/stat pages:
  https://www.windrawwin.com/results/sonderjyske/
  https://www.windrawwin.com/results/ac-horsens/
- Football Charts Horsens first-goal timing:
  https://www.football-charts.com/leagues/denmark/superliga/teams/horsens

### Corners
- CornerValue Sønderjyske:
  https://www.cornervalue.com/team/sonderjyske
- CornerValue AC Horsens:
  https://www.cornervalue.com/team/ac-horsens
- WinDrawWin Denmark Superliga corner table:
  https://www.windrawwin.com/us/soccer-stats/corners/denmark-superliga/
- CornerEdge Sønderjyske rolling context:
  https://corneredge.bet/team/sonderjyske/corners/
- exact operator/provider definition: **NOT SUPPLIED / UNKNOWN**

### Weather
- Met Office Haderslev:
  https://weather.metoffice.gov.uk/forecast/u1yf21vww
- Weather Underground Haderslev hourly cross-check:
  https://www.wunderground.com/hourly/dk/haderslev/IHADER5/date/2026-9-6

### Explicit exclusions
Bookmaker prices/odds, implied probabilities, market movement, tipster picks, AI/synthetic predictions and predicted lineups were excluded from the sporting rank. Predicted-lineup pages were used only to identify discrepancies requiring current-source reconciliation and were not treated as confirmed participants.

## 15. Bottom line

1. **1st Half Over 0.5 goals**
2. **Total Match Corners Over 9.5**
3. **Full Match Over 2.5 goals**
4. **Full Match Under 2.5 goals**
5. **1st Half Under 0.5 goals**

**Potential winner:** **AC Horsens — slight regulation-time lean.**

**P-321 status:** `PREGAME — UNSETTLED`  
**Retrospective:** deferred.  
**Next local slot:** `P-322`.


---

# P-322 — South Africa vs Zimbabwe — Namibia T20I Tri-Series 2026 Final

## 1. Frozen identity / state

| Field | Frozen value |
|---|---|
| Local continuation ID | `P-322` |
| Sport | Cricket |
| Competition | Namibia T20I Tri-Series 2026 — Final |
| Event | South Africa vs Zimbabwe |
| Venue | FNB / Namibia Cricket Ground, Windhoek |
| Scheduled start | **2026-09-06 14:00 CAT / 12:00 GMT / 22:00 AEST** |
| Final state refresh | **2026-09-06 22:06:38 AEST / 14:06:38 CAT** |
| Public state at freeze | **START-CROSSED; Cricket Australia still displayed Upcoming, both teams "to be announced", scorecard unavailable; Cricbuzz still had no live score/toss publication** |
| Toss | **NOT RECOVERED / NOT PUBLISHED in controlling source set at freeze** |
| Exact XI | **NOT RECOVERED at freeze** |
| Contract action gate | **South Africa 20-over and 6-over first-innings lines are ACTIONABLE ONLY IF SOUTH AFRICA BAT FIRST** |
| Method | latest Sep 6 process controls; `GFA-2 + SFA-CRICKET`; sports-only / market-blind |
| Numerical state | `NTS-2026.09.02-v0.3 — Stage 0; no fitted cricket model` |
| Probability/value | **NOT GENERATED / NO VALUE CLAIM** |
| Retrospective | **NOT PERFORMED — explicitly deferred** |

### Temporal-integrity classification

The scheduled start was crossed during research. At the final refresh, the best current match-centre source available (Cricket Australia) still labelled the final **Upcoming**, with no announced teams and no scorecard. Cricbuzz also had not populated toss/scorecard information. Because the timestamp had crossed but a zero-play/toss state was not field-owner confirmed, this is **not labelled PREGAME**. It is a `START-CROSSED / ORIGINAL-LINE / TOSS-CONDITIONAL` card.

No live runs, wickets or in-play information were used.

## 2. Governing cricket contract

Drive `RULES_CRICKET.md` requires the card to freeze:
- exact competition/format;
- innings and batting team;
- scheduled overs/balls;
- powerplay/field-restriction phase;
- shortening/DLS conditions;
- winner/tie/Super Over endpoint.

For this standard international T20:
- scheduled innings = **20 overs / 120 legal balls** unless shortened;
- mandatory powerplay = **overs 1–6**;
- the user's "South Africa 1st innings" wording is interpreted literally as the innings of the team batting first;
- therefore if Zimbabwe bat first, both supplied South Africa first-innings contracts are **NO ACTION in this research card**, rather than being silently converted to South Africa's chase.

Operator-specific shortened-match settlement terms were not supplied.

## 3. Frozen four selections — conditional on South Africa batting first

1. **South Africa 1st Innings, 6 overs: OVER 54.5**
2. **South Africa 1st Innings, 20 overs: OVER 186.5**
3. **South Africa 1st Innings, 20 overs: UNDER 186.5**
4. **South Africa 1st Innings, 6 overs: UNDER 54.5**

If South Africa do **not** bat first, do not transfer these forecasts to the second innings.

## 4. Current squad / injury / workload audit

### South Africa

Original Namibia-tour group was a deliberately developmental Proteas squad led by Bjorn Fortuin.

Confirmed unavailable:
- **Jason Smith — ruled out before the tri-series with a right adductor muscle strain.**
- **Lutho Sipamla — ruled out for the remainder of the tri-series with a left hamstring injury sustained in the opener.**
- **Andile Simelane replaced Sipamla in the squad.**

Current active squad pool before the final:
Bjorn Fortuin, Eathan Bosch, Dewald Brevis, Tony de Zorzi, Connor Esterhuizen, Jordan Hermann, Rubin Hermann, Duan Jansen, Kwena Maphaka, Nqobani Mokoena, Nqabayomzi Peter, Lhuan-dre Pretorius, Prenelan Subrayen, Andile Simelane.

Important recent workload/selection note:
- Duan Jansen, the series-leading wicket-taker entering the final, was **rested** against Namibia on Sep 4.
- His Sep 6 status was not yet confirmed at freeze.
- The batting core of Pretorius, Esterhuizen and Brevis remains the decisive run-production unit.

### Zimbabwe

Current tournament squad:
Sikandar Raza (c), Brian Bennett, Ryan Burl, Graeme Cremer, Ben Curran, Brad Evans, Innocent Kaia, Wessly Madhevere, Tadiwanashe Marumani, Wellington Masakadza, Kundai Matigimu, Blessing Muzarabani, Dion Myers, Newman Nyamhuri, Tafadzwa Tsiga.

Availability:
- **Graeme Cremer returned to the national squad after recovering from a left-arm injury** before this tournament.
- No new confirmed Zimbabwe injury exclusion was recovered for the final before freeze.

Selection uncertainty is meaningful because Zimbabwe rotated:
- **Muzarabani and Cremer both played** the Aug 29 meeting;
- both were **outside the XI** for the Sep 1 meeting, when Zimbabwe instead used Wellington Masakadza and Kundai Matigimu.

The final XI was not published in the controlling source set at freeze, so the 186.5 full-innings line carries a broader bowling-composition tail.

## 5. Current South Africa batting process

### Tournament results

South Africa:
- lost to Namibia: 145/9 chasing 164;
- beat Zimbabwe: 146/3 in 13.4 overs chasing 145;
- beat Zimbabwe: **185/7 batting first**;
- beat Namibia: **228/4 batting first**.

Their batting has accelerated materially through the tournament.

### Key current batters

**Lhuan-dre Pretorius**
- tournament: **226 runs in 4 innings**, average 56.50 entering final;
- sequence includes 22 vs Zimbabwe, **94 vs Zimbabwe**, **101 vs Namibia**;
- has moved from two low early scores into consecutive dominant innings.

**Dewald Brevis**
- tournament leader-tier production: **194 runs through 4 matches** in current series table;
- 75* from 32 in the first Zimbabwe meeting;
- 41 from 27 in the Sep 1 first innings.

**Connor Esterhuizen**
- promoted to open against Namibia on Sep 4;
- made **88 from 40**;
- with Pretorius put on **156** for the first wicket.

The key uncertainty is whether South Africa retain Esterhuizen as opener or return Jordan Hermann to the opening role. This matters to PP explosiveness, but both configurations cleared 54.5 against Zimbabwe in this series.

## 6. South Africa 6-over powerplay process

### Direct same-opponent evidence

Against Zimbabwe, South Africa's first six overs have been:

- **61** on Aug 29 while chasing;
- **59/0** on Sep 1 while batting first.

Both clear **54.5**.

Against Namibia on Sep 4:
- South Africa reached **70/0 after six**.

Therefore South Africa's latest three tournament powerplays available in the relevant current top-order regime are all above 54.5.

### Why Over 54.5 is Rank #1

Mechanisms:
- Pretorius is attacking without needing reckless first-ball exposure;
- Esterhuizen's promotion added another high-boundary-rate opener;
- Brevis supplies immediate acceleration if an opener falls;
- Zimbabwe's strongest bowling XI did not prevent a 61-run PP on Aug 29: Muzarabani and Cremer both played that match;
- when those two were absent Sep 1, South Africa made 59/0;
- current dry, warm conditions do not introduce a rain/surface suppression signal.

Kill paths:
- Muzarabani new-ball wicket(s);
- final pressure produces a more conservative first 2–3 overs;
- Zimbabwe use a spin matchup earlier;
- an opener change back to Jordan Hermann reduces boundary rate;
- a worn strip produces slower initial timing.

The line requires 55, so a normal 8.5–9.0 RPO powerplay is not enough; South Africa need roughly 9.17 RPO. Their current evidence supports that, but it is not a trivial line.

## 7. South Africa 20-over 186.5 process

### Direct opponent meeting

South Africa batted first against Zimbabwe Sep 1:
- **59/0 after 6**
- **100/1 after 11.0**
- **154/1 after 15.1**
- finished **185/7**

This is critical path evidence. The Under landed by only **1.5 runs**, but the process was not a stable 185 pace. South Africa were on a 200+ trajectory before a late seven-wicket cluster.

Zimbabwe death/middle response:
- Wesley Madhevere: **3/20**
- Brad Evans: **2/33**
- South Africa lost wickets at 15.2, 16.1, 17.2, 18.0, 19.0 and 20.0 after being 154/1.

### Latest batting-first ceiling

On Sep 4 versus Namibia:
- **70/0 powerplay**
- 156-run opening stand;
- Pretorius 101, Esterhuizen 88;
- South Africa **228/4**.

This is an upper-tail performance and must not simply be copied into the final, but it demonstrates the current batting ceiling.

### Current-series venue first innings

Six league-stage first innings at this ground:
**163, 144, 195, 185, 156, 228**

- series average = **178.5**
- last four average = **191.0**
- South Africa's two completed batting-first totals = **185 and 228**, average **206.5**

The line 186.5 is therefore:
- above the full series average;
- essentially on top of the direct Zimbabwe result;
- below South Africa's recent batting-first centre, which is inflated by the 228 upper tail.

### Over 186.5 path

- 55–65+ PP;
- Pretorius survives into overs 8–12;
- Brevis/Esterhuizen preserve boundary rate through spin;
- wickets in hand at over 15;
- death phase avoids Sep 1's collapse;
- Zimbabwe's seam/spin composition fails to create a wicket cluster.

Representative corridor:
- PP 58–66
- 10 overs 92–105
- 15 overs 145–160
- finish 188–210

### Under 186.5 path

- one or two PP wickets;
- Zimbabwe bring Raza/Cremer/Madhevere into a middle-overs squeeze;
- Muzarabani returns to the final XI and improves death control;
- South Africa repeat the Sep 1 conversion failure from 154/1 to 185/7;
- final pressure plus worn-surface grip suppresses risk-taking.

Representative corridor:
- PP 45–55
- 10 overs 80–92
- 15 overs 125–142
- finish 165–185

The 186.5 total is consequently much closer to the boundary than the PP direction.

## 8. Zimbabwe bowling context

### Aug 29 vs South Africa
Zimbabwe XI included:
- Blessing Muzarabani
- Graeme Cremer
- Brad Evans
- Newman Nyamhuri
- Raza/Madhevere

South Africa still chased at **10.68 RPO**, scoring 61 in the PP.

Bowling:
- Muzarabani 3 overs, 30 runs, 1 wicket
- Cremer 2 overs, 32
- Nyamhuri 2 overs, 31
- Evans 2.4 overs, 19

### Sep 1 vs South Africa
Zimbabwe used:
- Brad Evans 4/33, 2 wickets
- Madhevere 3/20, 3 wickets
- Nyamhuri 4/30
- Raza 4/36
- Masakadza 3/31
- Matigimu 2/29

The key containment came through wicket clustering, not sustained low run rate through the first 15 overs.

## 9. Pitch / venue report

### Long-run venue record

Cricbuzz venue data:
- 32 recorded T20s
- historical average first innings: **141**
- historical average second innings: **127**
- highest recorded total: **230/6**
- chasing teams have historically won more often than teams batting first.

This is **not** used as the controlling run environment because it blends different competitions, teams and eras.

### Current tournament strip/environment

The current six-match tri-series first-innings average is **178.5**, and the last four first innings average **191.0**. The most recent first innings was South Africa's 228/4.

Observed current characteristics:
- enough pace/carry and boundary value for aggressive top orders;
- new ball can still provide seam/swing if hit-the-deck bowlers execute;
- spin has been effective as a middle-over wicket/control mechanism;
- innings can be bimodal: rapid starts followed by significant wicket clusters.

**Pitch verdict:** current-tournament evidence is **materially more batting-friendly than the historical venue average**, but 186.5 is high enough that middle/death wicket risk remains decisive.

## 10. Weather / playing conditions

At the live research refresh, Windhoek was around **23°C with hazy sunshine**. Forecast through the match window is dry/hazy and roughly mid-20s Celsius, with no meaningful rain signal.

Independent weather sources also show:
- essentially zero / <5% precipitation risk;
- low humidity;
- moderate afternoon wind but no extreme wind condition.

**Weather effect:** no DLS/rain suppression is built into the central branch. Dry conditions support a normal full 20-over innings if the match begins normally.

## 11. Final / toss state

At the final research refresh:
- scheduled start had passed by about six minutes;
- Cricket Australia still labelled the match **Upcoming**;
- both teams were still "Team to be announced";
- scorecard was unavailable;
- no controlling toss publication was recovered.

Accordingly:
- card is **START-CROSSED**, not pregame;
- no live data were used;
- the two South Africa first-innings markets are **conditional on SA batting first**;
- toss alone does not create an Over/Under directional adjustment; it determines whether the supplied contracts exist.

## 12. Frozen ranking

| Rank | Contract | Verdict | Evidence | Core reason |
|---:|---|---|---|---|
| **1** | **SA 1st innings 6-over PP OVER 54.5** | **LEAN — conditional on SA batting first** | **MEDIUM** | 61 and 59 in both Zimbabwe meetings; 70 last game; strongest direct phase-specific mechanism |
| **2** | **SA 1st innings 20-over OVER 186.5** | **LEAN DIRECTION / CONDITIONAL** | **MEDIUM-LOW** | 185 direct H2H was boundary loss after 154/1; latest 228; top-order form and current pitch environment support 187+ |
| **3** | **SA 1st innings 20-over UNDER 186.5** | **FORCED RANK / CONDITIONAL** | **MEDIUM-LOW** | direct H2H landed 185; final/worn-strip and Zimbabwe wicket-cluster paths are credible; broader current batting process sits slightly above |
| **4** | **SA 1st innings 6-over PP UNDER 54.5** | **FORCED RANK / CONDITIONAL** | **LOW** | requires new-ball wickets or material tempo suppression against a current phase that has cleared 54.5 in three straight relevant tournament PPs |

### Rank gaps
- #1 → #2: **moderate**
- #2 → #3: **small**
- #3 → #4: **moderate**

## 13. Potential winner

### **South Africa — match-winner lean**

Why:
- finished league stage **3-1**, top with 6 points and +1.232 NRR;
- Zimbabwe finished **2-2**, both losses coming against South Africa;
- South Africa beat Zimbabwe by **7 wickets** and **43 runs** in the two league meetings;
- South Africa's top-order ceiling has risen during the tournament;
- Fortuin/Jansen/Subrayen have given South Africa multiple bowling control/wicket routes.

Why not stronger:
- this is a developmental South Africa squad, not their first-choice national XI;
- Sipamla and Jason Smith are unavailable;
- final XI/toss unresolved at freeze;
- Zimbabwe retain experienced match-winners Raza, Muzarabani, Evans, Burl and Cremer;
- a one-game final increases outcome variance.

No calibrated probability is published.

## 14. Source register — P-322

### Google Drive
- `RULES_CRICKET.md` — SFA-CRICKET identity, innings, phase, toss, pitch/conditions, DLS and settlement controls.
- `LEAGUE_RULES_CRICKET.md` — current ICC-derived T20 playing-condition reference.
- `RULES_GENERAL.md` — state/timing/source hierarchy, path/tail/rank controls.
- `LEARNING_REGISTER.md` — latest Sep 6 process controls / method v3.8 operational addendum.
- local `PREDICTION_MINI_RUNNING_LOG_P321_UPDATED.md` — immediate append-only handoff.

### Official / governing / high-quality event sources
- ICC series details:
  https://www.icc-cricket.com/news/all-the-details-about-namibia-south-africa-and-zimbabwe-tri-series
- ICC South Africa injury update:
  https://www.icc-cricket.com/news/south-africa-suffer-another-injury-setback-in-namibia
- ICC South Africa Namibia-tour squad:
  https://www.icc-cricket.com/news/new-south-africa-skipper-set-to-lead-side-on-namibia-tour
- ICC Zimbabwe squad:
  https://www.icc-cricket.com/news/experienced-spinner-in-zimbabwe-squad-for-namibia-tri-series
- ICC Sep 1 South Africa-Zimbabwe report:
  https://www.icc-cricket.com/news/splendid-win-boosts-south-africa-s-tri-series-final-chances
- ICC Sep 4 South Africa-Namibia report:
  https://www.icc-cricket.com/news/proteas-edge-namibia-to-secure-final-clash-against-zimbabwe
- Cricket Australia final match centre:
  https://www.cricket.com.au/matches/CA%3A40951/south-africa-men-zimbabwe-men-namibia-t20i-tri-series-2026-men
- Cricket Australia series page:
  https://www.cricket.com.au/matches/series/CA%3A4709/namibia-t20i-tri-series-2026
- CSA Namibia squad announcement:
  https://links.cricket.co.za/fortuin-set-to-lead-proteas-men-in-namibia-sa-a-squads-announced-for-bangladesh-a-tour/

### Scorecards / phase evidence
- Cricbuzz Aug 29 SA-ZIM:
  https://www.cricbuzz.com/live-cricket-scorecard/169913/zim-vs-rsa-2nd-match-namibia-t20i-tri-series-2026
- Cricbuzz Sep 1 SA-ZIM:
  https://www.cricbuzz.com/live-cricket-scorecard/170000/rsa-vs-zim-4th-match-namibia-t20i-tri-series-2026
- Cricbuzz Sep 4 SA-NAM:
  https://m.cricbuzz.com/live-cricket-scorecard/170011/rsa-vs-nam-6th-match-namibia-t20i-tri-series-2026
- NDTV Sep 1 match notes:
  https://sports.ndtv.com/cricket/live-coverage/zim-vs-sa-match-4-windhoek-zmsa09012026273843
- CricketWorld Sep 4 scorecard/powerplay:
  https://www.cricketworld.com/cricket/namibia-vs-south-africa/match/scorecard/98366
- Cricbuzz series stats:
  https://www.cricbuzz.com/cricket-series/12933/namibia-t20i-tri-series-2026

### Pitch / venue
- Cricbuzz venue guide:
  https://www.cricbuzz.com/cricket-series/12933/namibia-t20i-tri-series-2026/venues/1438021/namibia-cricket-ground
- Current six-match series scorecards listed above.

### Weather
- structured Windhoek forecast retrieved at local ~14:04: 23°C, hazy sunshine; dry match window.
- Met Office Windhoek:
  https://weather.metoffice.gov.uk/forecast/k7upt5gg6
- Timeanddate Windhoek:
  https://www.timeanddate.com/weather/namibia/windhoek/hourly

### Explicit exclusions
Bookmaker odds, implied probabilities, betting tips/prediction models, fantasy/Dream11 predicted XIs, toss predictions and synthetic/AI forecasts were excluded from the sporting rank. Prediction pages were used only as discovery leads when necessary and did not control any selection.

## 15. Bottom line

**Conditional on South Africa batting first:**
1. **SA PP OVER 54.5**
2. **SA 20 overs OVER 186.5**
3. **SA 20 overs UNDER 186.5**
4. **SA PP UNDER 54.5**

**Potential winner:** **South Africa — match-winner lean.**

If Zimbabwe bat first, the two supplied South Africa "first innings" contracts are **not action in this card**.

**P-322 status:** `START-CROSSED / TOSS-CONDITIONAL — UNSETTLED`  
**Retrospective:** deferred.  
**Next local slot:** `P-323`.


---

# P-323 — Everton vs Manchester United — 2026-27 English Premier League

## 1. Frozen identity / state

| Field | Frozen value |
|---|---|
| Local continuation ID | `P-323` |
| Population | **EPL — PRIMARY_SCORED under MDS-2026.09.06-v4.0** |
| Competition | English Premier League, 2026-27 |
| Event | Everton vs Manchester United |
| Venue | Hill Dickinson Stadium, Bramley-Moore Dock, Liverpool |
| Verified kickoff | **2026-09-06 14:00 BST / 23:00 AEST** |
| Structured event ID | `72221238` |
| Final G31 refresh | **2026-09-06 22:56:02 AEST** |
| State at freeze | **PREGAME / Scheduled** |
| Method | **MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND** |
| Numerical state | **Stage S0 — design only; no fitted soccer model** |
| Probability tier | **UNVALIDATED_SUBJECTIVE — mandatory v4.0 analyst probabilities, not calibrated/model probabilities** |
| Retrospective | **NOT PERFORMED — explicitly deferred** |

No bookmaker odds, implied probabilities, line movement, consensus, tipster analysis or synthetic prediction content entered the football ranking.

## 2. Frozen five-row slate

1. **1st Half Over 0.5 Goals**
2. **Manchester United Over 4.5 Team Corners**
3. **Full Match Over 2.5 Goals**
4. **Full Match Under 2.5 Goals**
5. **1st Half Under 0.5 Goals**

### Corner contract assumption

The user's sportsbook/stat-provider definition was not supplied. The research target is **Manchester United regulation-time corners over 4.5, 90 minutes plus stoppage time**. The intended research settlement lane is the structured EPL `wonCorners` field, but the user's operator definition remains `UNKNOWN_DEFINITION`; the corner row is therefore capped at `FORCED RANK / MEDIUM-LOW`.

## 3. Current confirmed participants

### Everton — 4-2-3-1

**Starting XI**
- Jordan Pickford
- Merlin Röhl
- James Tarkowski
- Jarrad Branthwaite
- Vitalii Mykolenko
- Harrison Armstrong
- James Garner
- Brennan Johnson
- Kiernan Dewsbury-Hall
- Tyrique George
- Thierno Barry

**Bench**
- Hayden Hackney
- Braiden Graham
- Jake O'Brien
- Charly Alcaraz
- Tyler Dibling
- Mark Travers
- Ainsley Maitland-Niles
- Jack Grealish
- Michael Keane

**Manager:** David Moyes.

Current personnel notes:
- Brennan Johnson replaces the departed **Iliman Ndiaye**, who transferred to Manchester City.
- Jack Grealish starts on the bench.
- **Christian Nørgaard is unavailable through injury.**
- Current reporting describes a thin Everton attacking group; Barry is the only recognised central striker in the available senior group.

### Manchester United — 4-2-3-1

**Starting XI**
- Senne Lammens
- Diogo Dalot
- Harry Maguire
- Lisandro Martínez
- Luke Shaw
- Kobbie Mainoo
- Youri Tielemans
- Bryan Mbeumo
- Bruno Fernandes
- Marcus Rashford
- Matheus Cunha

**Bench**
- Karl Darlow
- Ayden Heaven
- Noussair Mazraoui
- Leny Yoro
- Andrey Santos
- Patrick Dorgu
- Mason Mount
- Benjamin Šeško
- Joshua Zirkzee

**Manager:** Michael Carrick.

Current participant notes:
- United are unchanged from the 5-2 win over Ipswich.
- Mason Mount is back on the bench.
- Current absences include Carlos Baleba, Matthijs de Ligt, Manuel Ugarte and Amad Diallo.

### Bench/coaching gate

Full benches and named managers were retrieved for both clubs.

`BENCH_DEPTH_COUNT` under the exact v4 definition — named bench players who started at least 40% of the side's last ten fixtures — was **NOT RELIABLY RECONSTRUCTED** before freeze. This is recorded rather than guessed.

Qualitatively, United have the deeper attacking second-half bench (Mount, Šeško, Zirkzee, Dorgu plus defensive options Yoro/Mazraoui). Everton have Grealish, Dibling and Alcaraz as attacking change options but materially less centre-forward depth.

## 4. L5 / L10 / L15 / L20 trend audit

### Everton

Current league:
- Everton 2-0 Crystal Palace
- Bournemouth 1-1 Everton
- GF 3 / GA 1
- xG approximately 2.89 / xGA approximately 4.18
- corners won 11 / conceded 10

Reconstructed current competitive/league windows from the published result sequence:

| Window | Everton goals for | goals against | Per-match total environment |
|---|---:|---:|---:|
| L5 | 6 | 7 | 2.60 |
| L10 | 16 | 16 | 3.20 |
| L15 | 22 | 23 | 3.00 |
| L20 | 28 | 27 | 2.75 |

Trend interpretation:
- Everton's scoreboard defence (1 conceded in two league matches) has materially outperformed its current chance-quality conceded (~4.18 xGA).
- That does **not** force a regression claim; it creates a branch between sustained Pickford/shot-stopping/blocks and greater future conversion by opponents.
- Everton's broader windows are not structurally ultra-low scoring.

### Manchester United

Current league:
- Hull 2-0 Manchester United: United xG ~1.83, 21 shots, 6 corners.
- Manchester United 5-2 Ipswich: United xG ~5.02, 33 shots, 8 corners.
- current United xG ~6.85 in two matches.

Current reconstructed windows:

| Window | United goals for | goals against | Per-match total environment |
|---|---:|---:|---:|
| L5 | 11 | 6 | 3.40 |
| L10 | 20 | 13 | 3.30 |
| L15 | 28 | 18 | 3.07 |
| L20 | 40 | 24 | 3.20 |

Trend interpretation:
- United's attack is operating in a materially higher-scoring environment than Everton's prior-season baseline.
- The current two-game shot/xG sample is too small to extrapolate literally, but it supports a positive attack adjustment rather than merely citing the 5-2 score.

## 5. First-half process

2025-26 EPL baseline:
- **272 of 380 matches (72%)** contained at least one first-half goal.

2025-26 team phase rates:
- Everton: approximately **74%** 1H Over 0.5.
- Manchester United: approximately **76%**.

Current 2026-27:
- Everton's two league matches both had a first-half goal.
- United's two league matches both had a first-half goal.

Recent 2025-26 H2H:
- Manchester United 0-1 Everton: HT 0-1.
- Everton 0-1 Manchester United: HT 0-0.
- H2H first-half O0.5: 1/2.

H2H receives low weight because the first meeting was distorted by an early Everton red card and both squads have materially changed.

### Explicit first-half probability arithmetic

Descriptive prior:
- 60% × EPL 72% = 43.20 pp
- 25% × mean team prior 75% = 18.75 pp
- 10% × current 4/4 event sample 100% = 10.00 pp
- 5% × recent H2H 50% = 2.50 pp

**Baseline = 74.45%**

Signed current adjustments:
- Everton attacking attrition / Barry-only recognised central-forward depth: **-1 pp**
- United unchanged high-creation XI: **+1 pp**
- dry/moderate-breeze venue conditions: **0 pp**

**Resulting subjective centre = ~74%**
**Uncertainty width = ±8 percentage points**

Therefore:
- `P(1H Over 0.5) = 74% UNVALIDATED_SUBJECTIVE`
- `P(1H Under 0.5) = 26% UNVALIDATED_SUBJECTIVE`

This is analyst probability bookkeeping under v4.0, not a fitted or calibrated probability.

## 6. Full-match joint goal object

### Prior arithmetic

Inputs:
- 2025-26 EPL mean: **2.75 goals/match**
- prior-season team match environments: Everton ~2.56; United ~3.14; midpoint **2.85**
- current two-match environments: Everton 2.0; United 4.5; midpoint **3.25**

Weighted baseline:
- 50% × 2.75 = 1.375
- 35% × 2.85 = 0.998
- 15% × 3.25 = 0.488

**Baseline centre = 2.86 goals**

Signed adjustments:
- current chance-creation / conversion-deficit signal (United 6.85 xG in two; Everton 4.18 xGA vs 1 conceded), heavily shrunk: **+0.20**
- Everton attacking attrition, Ndiaye gone, Grealish bench, Barry only recognised CF: **-0.15**
- two most recent H2Hs both one-goal totals, low continuity weight: **-0.10**
- United unchanged attacking XI plus materially deeper attacking bench: **+0.10**
- weather/surface: **0.00**

**Resulting centre = 2.91 goals**
**Explicit width = ±1.25 goals**

The 2.5 line is **0.41 goals below** the subjective centre.

### Component budget

Prior scoring share from 2025-26 rates:
- Everton 1.24 / (1.24 + 1.82) = **40.5%**
- United = **59.5%**

Current allocation adjustments:
- Everton home effect: +2 percentage points Everton share
- Everton current attacking personnel loss/depth: -4 pp Everton share

Resulting allocation:
- Everton **38.5%**
- United **61.5%**

Apply to 2.91:
- Everton goal component = 2.91 × 0.385 = **1.12**
- United goal component = 2.91 × 0.615 = **1.79**
- sum = **2.91**

Derived subjective exact-contract probabilities:
- **Over 2.5: 57% UNVALIDATED_SUBJECTIVE**
- **Under 2.5: 43% UNVALIDATED_SUBJECTIVE**

These are intentionally close because 2.5 sits inside the central width.

## 7. Corner process — Manchester United Over 4.5

Current United corner evidence:
- at Hull: **6**
- vs Ipswich: **8**
- latest five: **8, 6, 3, 7, 7 = 6.2 average**

Current Everton conceded:
- vs Crystal Palace: **0**
- at Bournemouth: **10**
- current average conceded: **5.0**

Recent H2H United corners:
- **9** at Old Trafford
- **1** at Everton
- mean **5.0**

Role continuity:
- Bruno Fernandes, United's primary high-volume set-piece/corner taker last season, starts.
- Bryan Mbeumo also carries recent corner/set-play delivery volume and starts.
- United's current shot/territory numbers (21 and 33 shots) create repeatable block/clearance/end-line exposure.

### Explicit corner arithmetic

- 45% × United L5 6.2 = 2.79
- 25% × current United 7.0 = 1.75
- 20% × Everton current conceded 5.0 = 1.00
- 10% × recent H2H 5.0 = 0.50

**Baseline = 6.04 United corners**

Signed adjustments:
- current high shot/cross/territory pressure: **+0.25**
- Everton thinner late bench / defensive-pressure branch: **+0.10**
- early United lead can reduce late attacking corner demand: **-0.15**

**Corner centre = 6.24**
**Width = ±2.8 corners**

The 4.5 line is **1.74 corners below** the centre.

**P(United Over 4.5 team corners) = 64% UNVALIDATED_SUBJECTIVE**

Because the user's operator/stat provider was not supplied:
- verdict remains **FORCED RANK / MEDIUM-LOW**
- research settlement lane: structured EPL `wonCorners`
- operator action: `UNKNOWN_DEFINITION` until operator terms are supplied.

## 8. Rest / congestion

- Everton last league match: Aug 29.
- Manchester United last league match: Aug 30.
- approximate rest: Everton 8 days, United 7 days.
- neither side carries material European midweek congestion into this Sunday match.

**Signed adjustment: 0.00 goals**; no meaningful rest asymmetry.

## 9. Environment / current-surface gate

Venue:
**Hill Dickinson Stadium, Bramley-Moore Dock, Liverpool**
Approximate venue coordinates: **53.4251, -3.0028**.

Nearest public Met Office hourly grid used is approximately 1.8 km from the stadium coordinate and covers the full match window.

Match-window weather:
- around kickoff: roughly **23°C**
- afternoon peak around **24–25°C**
- precipitation probability **<5%**
- moderate southerly/westerly waterfront breeze, roughly low-to-mid teens mph
- no heavy rain, extreme wind or heat mechanism.

Surface: outdoor football pitch; no roof/weather closure mechanism.

**Environment adjustment to goal centre = 0.00.**

Bidirectional weather audit:
- breeze may reduce cross accuracy;
- the same breeze can increase defensive miscontrols, deflections and clearances;
- no evidence supports a net signed adjustment.

## 10. Bidirectional-sign audit

1. **Everton attacking thinness**
   - helps Under / United side by reducing Everton finishing depth;
   - can hurt Under if a thin bench also reduces Everton's late defensive control.
2. **United territory and cross volume**
   - increases shot/corner generation;
   - if United convert early, later corner demand can fall.
3. **Everton xGA vs GA gap**
   - supports a greater future-conversion branch;
   - Pickford/blocks may persist and convert opposition pressure into corners rather than goals.
4. **Recent low-scoring H2H**
   - supports Under;
   - continuity is weak because of the red-card distortion and roster changes.
5. **Dry waterfront breeze**
   - can suppress clean crossing;
   - can increase deflections/clearances.
   - net signed effect = 0.

No two-way mechanism was applied only in the direction convenient to the selected row.

## 11. Frozen ranking

| Rank | Contract | UNVALIDATED_SUBJECTIVE probability | Verdict | Evidence |
|---:|---|---:|---|---|
| **1** | **1st Half Over 0.5 goals** | **74%** | **LEAN** | **MEDIUM** |
| **2** | **Manchester United Over 4.5 team corners** | **64%** | **FORCED RANK** | **MEDIUM-LOW** |
| **3** | **Full Match Over 2.5 goals** | **57%** | **LEAN direction** | **MEDIUM-LOW** |
| **4** | **Full Match Under 2.5 goals** | **43%** | **FORCED RANK** | **MEDIUM-LOW** |
| **5** | **1st Half Under 0.5 goals** | **26%** | **FORCED RANK** | **LOW** |

Complementary-pair coherence:
- 1H O0.5 74% + U0.5 26% = 100%.
- FT O2.5 57% + U2.5 43% = 100%.

No push is possible at either half-goal line.

## 12. Potential winner

### **Manchester United — slight 90-minute regulation lean**

`UNVALIDATED_SUBJECTIVE` 1X2 allocation:
- **Manchester United 45%**
- **Draw 29%**
- **Everton 26%**

Why United:
- current goal component in the joint object: **1.79 vs Everton 1.12**
- stronger L5/L10/L15/L20 scoring trend
- unchanged current XI after the 5-2 Ipswich performance
- Mbeumo / Bruno / Rashford / Cunha creation structure
- deeper second-half attacking bench
- Everton's current defensive result has materially outperformed chance quality conceded.

Why only slight:
- Everton are at home
- Pickford/Branthwaite/Tarkowski can keep a low-event branch alive
- current EPL sample is only two matches per side
- both recent league H2Hs finished with only one goal
- United themselves conceded twice to Ipswich and lost 2-0 at Hull.

Representative score families:
- **Everton 1-2 Manchester United**
- **1-1**
- **1-3 Manchester United**
- low-event tails: **0-1**, **1-0**

## 13. Settlement sources preregistered

- Match score / first-half score / winner: official Premier League / structured EPL match record.
- Corners: structured EPL `wonCorners` research field, with `OPERATOR_ACTION = UNKNOWN_DEFINITION` unless the user's sportsbook terms are later supplied.

Synthetic/simulated prediction content is prohibited for settlement.

## 14. Source register — P-323

### Drive authority
- `README.md` — v4.0 active framework and EPL `PRIMARY_SCORED`.
- `METHOD.md` — mandatory v4 lifecycle, probability mandate and scoring.
- `CONTROLS.md` — current quick-reference gates.
- `SOURCES.md` — structured EPL lane and source ownership.
- `RULES_GENERAL.md` §16 — controlling mandatory gate classification and explicit-arithmetic requirement.
- `RULES_SOCCER.md` — soccer participant, goal, corner, bench and score-state process.
- `LEAGUE_RULES_SOCCER.md` — EPL regulation/competition rules.
- local `PREDICTION_MINI_RUNNING_LOG_P322_UPDATED.md` — append-only handoff.

### Identity / state
- Structured soccer event ID `72221238`; kickoff 13:00 UTC / 14:00 BST / 23:00 AEST.
- Final structured refresh **22:56:02 AEST** — still Scheduled.

### Current lineups / bench / availability
- Manchester United official team announcement:
  https://www.manutd.com/en/news/detail/ruben-amorim-names-team-for-everton-encounter-06-september-2026
- Guardian live lineup/report:
  https://www.theguardian.com/football/live/2026/sep/06/everton-v-manchester-united-premier-league-live-score-updates
- Current Everton/United confirmed lineup listing used only for factual participant fields:
  https://www.oddschecker.com/tips/football/20260906-everton-vs-manchester-united-lineups
- Reuters transfer/current Everton squad context:
  https://www.reuters.com/sports/soccer/
- Current Times Everton squad-depth reporting:
  https://www.thetimes.com/sport/football/

### Current form / xG / corners
- StatMuse Everton vs Crystal Palace:
  https://www.statmuse.com/fc/match/8-22-2026-eve-vs-cry-124953
- StatMuse Hull vs Manchester United:
  https://www.statmuse.com/fc/match/8-23-2026-hul-vs-mun-124957
- StatMuse Manchester United vs Ipswich:
  https://www.statmuse.com/fc/match/8-30-2026-mun-vs-ips-124967
- Current Bournemouth vs Everton match/stat pages and current team result windows retrieved during research.
- 2025-26 EPL first-half scoring baseline and team phase tables retrieved from current historical stat source set.

### H2H
- Premier League / current match-stat records:
  - Manchester United 0-1 Everton, 24 Nov 2025
  - Everton 0-1 Manchester United, 23 Feb 2026

### Weather / venue
- Everton official Hill Dickinson Stadium location/venue page.
- Stadium coordinates cross-check: approximately 53.4251, -3.0028.
- Met Office nearest venue-hourly grid, full 13:00–17:00 local window.
- No generic city forecast was used as the sole environment evidence.

### Explicit exclusions
Odds, implied probabilities, line movement, bookmaker previews, tipsters, betting consensus, synthetic/AI simulations and predicted lineups were excluded from the sporting probability/ranking process.

## 15. Bottom line

1. **1H Over 0.5 — 74% UNVALIDATED_SUBJECTIVE**
2. **Manchester United Over 4.5 team corners — 64%**
3. **Full-match Over 2.5 — 57%**
4. **Full-match Under 2.5 — 43%**
5. **1H Under 0.5 — 26%**

**Potential winner:** **Manchester United — slight regulation-time lean (45%; draw 29%; Everton 26%).**

**P-323 status:** `PREGAME — UNSETTLED`  
**Population:** `EPL — PRIMARY_SCORED`  
**Retrospective:** deferred.  
**Next local slot:** `P-324`.


---

# P-324 — Valencia vs Barcelona — 2026-27 La Liga

## State / admission decision

| Field | Frozen value |
|---|---|
| Local continuation ID | `P-324` |
| Competition | Spain La Liga — 2026-27, Matchday 4 |
| Venue | Camp de Mestalla, Valencia |
| Scheduled kickoff | **2026-09-06 16:15 CEST / 2026-09-07 00:15 AEST** |
| Method | **MDS-2026.09.06-v4.0** |
| User-requested contracts | 1H O/U 0.5; FT O/U 2.5; plus one research-selected corner row |
| Structured state observation | **Live, 0-0** at 2026-09-07 00:18:49 AEST |
| Exact match clock / period | **NOT VERIFIED** |
| Official LaLiga page at same research window | **Still displayed Scheduled** |
| Output state | **LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST** |
| Retrospective | **NOT PERFORMED** |

## Why no five-pick card was issued

`RULES_GENERAL.md` §2 under the active v4.0 framework requires, once scheduled start has passed, a live card to freeze the **exact score, clock, period and observation time**. A 0-0 live shell without an exact clock does not satisfy the state gate. The permitted outputs are a verified live target/view, `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`, or a verified final/no-forecast disposition.

The user requested a pregame ranking, but research began after the official 00:15 AEST kickoff. Freezing a pre-start ranking after kickoff would violate the no-hindsight/timestamp invariant. Therefore:
- no 1H Over/Under probability was issued;
- no FT Over/Under probability was issued;
- no corner row was ranked;
- no winner call was issued;
- no `UNVALIDATED_SUBJECTIVE` probability was created.

## Verified identity / current public facts

- FC Barcelona official schedule: Valencia vs Barcelona, Sep 6, 16:15 CEST at Mestalla.
- LaLiga official schedule: same fixture and local kickoff.
- Structured soccer game ID: `72478542`.
- At 00:18:49 AEST, structured soccer state: **Live, 0-0**.
- LaLiga official match page still showed the fixture as **Scheduled**, producing a live-state conflict.
- LaLiga pre-match comparison showed Barcelona 3-0-0, 12 goals scored / 2 conceded; Valencia 0-1-2, 1 scored / 4 conceded entering the match.

Those facts are retained as research context only and were **not converted into a post-kickoff pregame forecast**.

## Source register — P-324

### Google Drive governing sources
- `METHOD.md` — MDS-2026.09.06-v4.0 active lifecycle and no-hindsight boundary.
- `RULES_GENERAL.md` — §2 start-crossing / timestamp invariant / exact live state requirement.
- `RULES_SOCCER.md` — live soccer state requires score, clock/period and recomputation from remaining exposure.
- local `PREDICTION_MINI_RUNNING_LOG_P323_UPDATED.md` — immediate append-only handoff.

### Identity / schedule
- FC Barcelona official schedule:
  https://www.fcbarcelona.com/en/futbol/primer-equipo/calendario
- FC Barcelona viewing guide:
  https://www.fcbarcelona.com/en/football/first-team/news/4571041/when-and-where-to-watch-valencia-v-fc-barcelona
- Valencia official fixture/ticket record:
  https://entradas.valenciacf.com/valenciacf_webservices/select/2964323?hl=en-US&viewCode=V_blockmap_view
- LaLiga official fixture page:
  https://www.laliga.com/partido/temporada-2026-2027-laliga-ea-sports-valencia-cf-fc-barcelona-4

### Live state
- Structured soccer game ID `72478542`: **Live, 0-0** at 00:18:49 AEST.
- Repeated structured refreshes did not expose an exact clock in the available game summary.
- Sky Sports and Flashscore corroborated 0-0/live state but did not provide a sufficiently reliable exact match clock in the retrieved record.
- LaLiga page remained `Scheduled`, so the state conflict was preserved rather than silently resolved.

### Explicit exclusions
No bookmaker odds, implied probabilities, tipster content, synthetic predictions, or stale pregame ranking were used.

## Bottom line

**No actionable P-324 forecast issued.**

Reason: **scheduled start crossed + exact live clock/period not verified**.

**P-324 status:** `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`  
**Retrospective:** deferred.  
**Next local slot:** `P-325`.


---

# P-325 — Bangladesh Women vs Sri Lanka Women — Women's Asia Cup T20 2026

## 1. Frozen identity / state

| Field | Frozen value |
|---|---|
| Local continuation ID | `P-325` |
| Population | Cricket / Women's Asia Cup — **EXPLORATORY, NOT PRIMARY-SCORED** |
| Event | Bangladesh Women vs Sri Lanka Women |
| Competition | Women's Asia Cup T20 2026, Group B, Match 10 |
| Venue | Dubai International Cricket Stadium, Dubai |
| Verified kickoff | **2026-09-06 18:30 GST / 14:30 UTC / 2026-09-07 00:30 AEST** |
| User-estimated kickoff | 2026-09-07 **12:30 PM AEST — corrected by 12 hours** |
| Final volatile freeze | **2026-09-07 00:28:36 AEST** |
| State | **PREGAME** |
| Toss | **NOT YET PUBLISHED in the controlling exact-match source at freeze** |
| Playing XIs | **NOT YET PUBLISHED at freeze** |
| Method | **MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND** |
| Numerical state | **Stage S0 — no fitted/validated cricket model** |
| Probability tier | **UNVALIDATED_SUBJECTIVE** |
| Retrospective | **NOT PERFORMED — explicitly deferred** |

## 2. Exact contract / activation rule

User defines "first innings" as the team batting first.

Therefore the following four Bangladesh contracts are **actionable only if Bangladesh bat first**:
- Bangladesh 20-over total O/U 116.5
- Bangladesh 6-over powerplay O/U 42.5

If Sri Lanka bat first, **do not transfer these forecasts to Bangladesh's chase**.

Standard T20 structure used:
- 20 overs / 120 legal balls per full innings
- powerplay overs 1–6
- DLS/shortening can alter operator action; user's sportsbook-specific shortened-match terms were not supplied.

## 3. Frozen ranking — conditional on Bangladesh batting first

| Rank | Contract | UNVALIDATED_SUBJECTIVE probability | Verdict | Evidence |
|---:|---|---:|---|---|
| **1** | **Bangladesh 1st innings, 6-over PP UNDER 42.5** | **73%** | **LEAN** | **MEDIUM** |
| **2** | **Bangladesh 1st innings, 20-over UNDER 116.5** | **56%** | **LEAN direction / FORCED RANK** | **MEDIUM-LOW** |
| **3** | **Bangladesh 1st innings, 20-over OVER 116.5** | **44%** | **FORCED RANK** | **MEDIUM-LOW** |
| **4** | **Bangladesh 1st innings, 6-over PP OVER 42.5** | **27%** | **FORCED RANK** | **LOW–MEDIUM-LOW** |

Complementary coherence:
- PP U42.5 73% + O42.5 27% = 100%
- innings U116.5 56% + O116.5 44% = 100%

No push exists on half-run lines.

## 4. Bangladesh current availability

Confirmed unavailable:
- **Fariha Islam Trisna — OUT**, Grade II right-thigh tear, estimated 4–6 weeks.
- **Farjana Easmin**, 17-year-old uncapped right-arm seamer, named as replacement.

Current squad:
Nigar Sultana (c), Nahida Akter, Dilara Akter, Juairiya Ferdous, Sharmin Akter Supta, Sarmin Sultana, Sobhana Mostary, Shorna Akter, Ritu Moni, Fahima Khatun, Rabeya Khan, Marufa Akter, Sultana Khatun, Shanjida Akter Meghla, Farjana Easmin.

Latest tournament XI vs Indonesia:
Juairiya Ferdous, Dilara Akter, Sobhana Mostary, Nigar Sultana, Shorna Akter, Ritu Moni, Fahima Khatun, Rabeya Khan, Nahida Akter, Marufa Akter, Shanjida Akter Meghla.

Exact Match 10 XI remained unannounced at freeze.

## 5. Sri Lanka current availability

Confirmed unavailable:
- **Dewmi Vihanga — OUT**, right-knee injury sustained in a practice match.
- **Nimasha Meepage**, left-arm spinner, named as replacement.

Current squad:
Chamari Athapaththu (c), Imesha Dulani, Sanjana Kavindi, Vishmi Gunaratne, Harshitha Samarawickrama, Kavisha Dilhari, Nilakshika Silva, Hasini Perera, Kaushini Nuthyangana, Sugandika Kumari, Chamudi Praboda, Chethana Vimukthi, Kawya Kavindi, Mithali Ayodhya, Nimasha Meepage.

Sri Lanka's current bowling group has shown substantial spin/slow-ball control in Dubai, including:
- UAE 79 all out; UAE PP 22/2
- Indonesia 49 all out; Indonesia PP 22/4
- Chamari Athapaththu 7/5 against Indonesia.

Exact Match 10 XI remained unannounced at freeze.

## 6. Bangladesh batting-first evidence

Latest five completed Bangladesh **batting-first** T20 innings:

| Opponent | Total | PP |
|---|---:|---:|
| Indonesia | 129/8 | 32/1 |
| South Africa | 117 | 23/2 |
| India | 136/8 | 40/1 |
| Pakistan | 123/6 | 23/3 |
| Australia | 77/8 | 22/3 |

Arithmetic:
- innings mean = (129 + 117 + 136 + 123 + 77) / 5 = **116.4**
- PP mean = (32 + 23 + 40 + 23 + 22) / 5 = **28.0**
- PP U42.5 = **5/5** in this window.

This streak is not used alone. The mechanism is slow/conservative first-phase scoring plus wicket exposure, reinforced by Sri Lanka's current new-ball/spin suppression and Dubai's current low/mid-scoring women's tournament environment.

## 7. Current tournament scoring environment

Completed first innings through the first nine matches:
**120, 79, 159, 129, 119, 124, 193, 71, 55**

Arithmetic:
- sum = 1,049
- 1,049 / 9 = **116.56**

The user's 116.5 line is therefore essentially on the current tournament first-innings mean.

Important distribution point:
- this is not a tight 116-run environment;
- the range is broad (55 to 193), indicating innings outcomes are strongly resource/wicket-state dependent.

Bangladesh's only current-tournament first innings:
- **129/8 vs Indonesia**
- **32/1 PP**

Sri Lanka's two opponent powerplays:
- UAE **22/2**
- Indonesia **22/4**

## 8. Direct Bangladesh–Sri Lanka 2026 continuity

Full-length T20Is in Bangladesh earlier in 2026:
- Apr 28: Sri Lanka 161/4; Bangladesh 136/7; Bangladesh PP **44/4**
- Apr 30: Sri Lanka 154/4; Bangladesh 133/5; Bangladesh PP **46/0**
- May 2: shortened 9-over match; Sri Lanka 87/6 beat Bangladesh 84/6 by 3 runs

These H2Hs are useful because much of the batting/bowling core remains, but they are downweighted because:
- first two Bangladesh innings were **chases**, not batting-first targets;
- venue was Sylhet, not Dubai;
- May 2 was shortened to nine overs;
- current UAE surface/tournament regime is materially different.

The 44 and 46 powerplays are the strongest contrary evidence to PP Under 42.5 and prevent an excessively high subjective probability.

## 9. Pitch / conditions ladder

### Six-rung disclosure

| Rung | Attempt | Result |
|---:|---|---|
| **1** | Exact-match toss/broadcast pitch report searched | **NOT FOUND before freeze; toss not populated** |
| **2** | `"Dubai International Cricket Stadium" curator pitch`, groundstaff/venue profile | **Curator Tony Hemming identified; no current Match-10 strip statement recovered** |
| **3** | Exact-match specialist match centre / facts | **Match 10 page found; venue/start confirmed, toss/XI blank at freeze; no exact strip description** |
| **4** | Exact-match specialist preview / pitch-and-conditions search | **Attempted; no sufficiently attributable exact-strip report recovered before freeze** |
| **5** | Named current reporting quoting curator/team management | **No Match-10 current strip quote recovered** |
| **6** | Venue/format historical baseline + current competition baseline | **COMPLETED** |

**STRIP STATUS: NOT FOUND AFTER SEARCH**

No grass, hardness, pace, seam or turn claim is presented as today's observed strip.

### Rung 6 historical/current baseline

Long-run mixed T20 venue record:
- 135 T20s
- average first innings **140**
- average second innings **120**

This long-run sample mixes men's/women's teams, eras and competition strengths, so it is background only.

Current Women's Asia Cup first-innings mean:
- **116.56 from 9 completed matches**

Current competition evidence is much more relevant to the 116.5 target than the mixed historical 140.

Recent exact-venue mechanisms:
- Sri Lanka restricted UAE to 79 and Indonesia to 49.
- Bangladesh made 129/8 against Indonesia.
- recent India–Pakistan match produced a Pakistan batting collapse.
- current women’s games have repeatedly shown spin/wicket-cluster pathways.

## 10. Match-window weather

Venue-local conditions are forecast dry/hot:
- around match start: high-30s °C
- clear / very low precipitation probability
- moderate breeze
- humidity increasing into the evening/night.

**MATCH CONDITIONS STATUS: OBSERVED / DRY-HOT**

No rain/DLS suppression is in the central branch.

Bidirectional condition effects:
- heat can reduce fielding intensity / help boundary value;
- evening humidity/dew can aid skid and batting later;
- the same dry/used surface can support spin and slower-ball grip.
No one-way weather coefficient is used.

## 11. PP joint event object

Inputs:
- 45% × Bangladesh L5 first-bat PP mean 28.0 = **12.60**
- 25% × current Bangladesh Dubai PP 32 = **8.00**
- 20% × Sri Lanka current opponent PP conceded mean 22 = **4.40**
- 10% × 2026 full-length H2H Bangladesh PP mean 45 = **4.50**

Baseline = **29.50 runs**

Signed qualitative-bookkeeping adjustments:
- current Dubai low-dot-ball / spin-wicket environment: **-1.5**
- Sri Lanka current bowling suppression: **-1.0**
- unresolved final XI: **0 signed**, widen uncertainty

**PP centre ≈ 27.0**
**Width ≈ ±15 runs**

42.5 lies **15.5 runs above** the centre.

Result:
- PP Under 42.5 = **73% UNVALIDATED_SUBJECTIVE**
- PP Over 42.5 = **27%**

## 12. Full-innings joint event object

Inputs:
- 40% × Bangladesh L5 batting-first mean 116.4 = **46.56**
- 30% × current tournament first-innings mean 116.56 = **34.97**
- 20% × comparable recent Bangladesh totals vs Sri Lanka (136,133,111 mean 126.7; downweighted for chase/venue mismatch) = **25.34**
- 10% × Bangladesh current Dubai innings 129 = **12.90**

Baseline = **119.77**

Signed adjustments:
- Sri Lanka current bowling suppression / wicket-taking depth: **-5**
- current Dubai women's wicket-cluster/spin signal: **-2**
- Bangladesh Shorna/Nigar/Ritu late-order recovery capacity: **+1**
- Fariha injury: **0 batting adjustment**

**Full-innings centre ≈ 113.8**
**Width ≈ ±22 runs**

116.5 lies only **2.7 runs above** the centre, well inside the width.

Result:
- Under 116.5 = **56%**
- Over 116.5 = **44%**

This is a boundary market, not a high-confidence Under.

### Component budget
Central innings allocation:
- powerplay: **27**
- overs 7–15: **51**
- overs 16–20: **36**
- total = **114**

Important phase linkage:
- a PP Under with 0–1 wickets can still lead to a 120–130 finish;
- a PP Under with 2–3 wickets materially lowers the death-overs ceiling.
Powerplay result alone does not determine the full innings.

## 13. Potential winner

### **Sri Lanka Women — match-winner lean**

`UNVALIDATED_SUBJECTIVE`:
- **Sri Lanka 66%**
- **Bangladesh 34%**

Reasons:
- Sri Lanka are defending champions and 2-0 in Group B.
- They have restricted UAE to 79 and Indonesia to 49 in Dubai.
- They beat Bangladesh in all three T20Is of the April/May 2026 series.
- Athapaththu, Dilhari, Sugandika and the current bowling group provide more demonstrated wicket-taking/containment routes.
- Bangladesh's Fariha absence reduces a left-arm pace option.

Why not stronger:
- Bangladesh's spin attack is highly credible in current Dubai conditions.
- Bangladesh won their tournament opener comfortably.
- final XI and toss were not yet published at freeze.
- one-match T20 variance is substantial.

Winner call is for the match under the tournament's official tie/Super Over rules, not a regulation-only football-style endpoint.

## 14. Bidirectional-sign audit

1. **Slow Bangladesh PP**
   - supports PP Under;
   - if achieved with wickets intact, can support later acceleration and FT Over.
2. **Sri Lanka spin strength**
   - suppresses rate;
   - attacking spin can also produce boundaries if Bangladesh target it successfully.
3. **Dew/evening humidity**
   - can improve batting skid later;
   - first-innings Bangladesh would experience less late-night dew than the chase.
4. **Bangladesh 129 vs Indonesia**
   - shows ceiling above 116.5;
   - Indonesia is materially weaker than Sri Lanka's bowling attack.
5. **Bangladesh 133/136 vs Sri Lanka earlier in 2026**
   - contrary evidence to FT Under;
   - those were chases in Sylhet and not the same venue/innings regime.

## 15. Settlement preregistration

- Match winner / innings total: exact official/competition scorecard if available post-match, otherwise official board/ICC report with scorecard cross-check.
- Powerplay: exact official phase field or legality-reconciled scorecard/delivery source.
- Operator action on shortened/abandoned innings: **UNKNOWN unless user's sportsbook terms are supplied**.

## 16. Source register

### Google Drive
- `METHOD.md` — MDS-2026.09.06-v4.0.
- `RULES_CRICKET.md` — innings identity, toss/participant, PP/phase, pitch ladder and joint-process controls.
- `LEAGUE_RULES_CRICKET.md` — T20/T20I base playing conditions.
- `DATA_SOURCE_REGISTER.md` §6/6A — cricket source lanes and six-rung pitch/conditions ladder.
- local `PREDICTION_MINI_RUNNING_LOG_P324_UPDATED.md` — immediate append-only handoff.

### Current event / schedule
- current exact-match scorecard/search centre: Match 10, Dubai International Stadium, Sep 6, 20:00 IST / 14:30 UTC.
- Cricbuzz Women’s Asia Cup venue/event listing: Dubai International Cricket Stadium; curator Tony Hemming.

### Injury / squads
- Bangladesh: BCB-attributed Fariha Islam Trisna injury/replacement reporting.
- Sri Lanka: Dewmi Vihanga injury; Nimasha Meepage replacement reporting.
- ICC / Sri Lanka Cricket tournament squad releases.

### Current tournament / phase evidence
- Bangladesh vs Indonesia scorecard: 129/8; PP 32/1.
- Sri Lanka vs UAE scorecard: UAE 79; PP 22/2.
- Sri Lanka vs Indonesia scorecard: SL 124/7; Indonesia 49; PP suppression / Athapaththu 7/5.
- completed Women’s Asia Cup first-innings score set through Match 9.

### H2H / recent Bangladesh
- Apr 28 2026: Sri Lanka 161/4, Bangladesh 136/7.
- Apr 30 2026: Sri Lanka 154/4, Bangladesh 133/5.
- May 2 2026: 9-over match, Sri Lanka 87/6, Bangladesh 84/6.
- Bangladesh recent batting-first scorecards vs South Africa, India, Pakistan, Australia and Indonesia.

### Weather / venue
- venue-specific Dubai International Stadium weather forecast.
- Dubai match-window hourly cross-check.
- Cricbuzz venue long-run T20 baseline.

### Exclusions
Bookmaker odds, implied probabilities, market movement, fantasy/Dream11 pages, synthetic/AI predictions and generic unattributed “pitch report” pages were excluded.

## 17. Bottom line

**ONLY IF BANGLADESH BAT FIRST:**
1. **BAN PP UNDER 42.5 — 73% UNVALIDATED_SUBJECTIVE**
2. **BAN 20-over UNDER 116.5 — 56%**
3. **BAN 20-over OVER 116.5 — 44%**
4. **BAN PP OVER 42.5 — 27%**

**Potential winner: Sri Lanka Women — 66% UNVALIDATED_SUBJECTIVE**

**P-325 status:** `PREGAME — TOSS/XI CONDITIONAL — UNSETTLED`  
**Population:** `EXPLORATORY — NOT SCORED`  
**Retrospective:** deferred.  
**Next local slot:** `P-326`.


---

# P-326 — #24 Western Carolina @ Campbell — NCAA FCS

## Final issue disposition

| Field | Final value |
|---|---|
| Local continuation ID | `P-326` |
| Event | #24 Western Carolina at Campbell |
| Venue | Barker-Lane Stadium / Ed Gore Field, Buies Creek, North Carolina |
| Rescheduled kickoff | **2026-09-06 11:00 EDT / 2026-09-07 01:00 AEST** |
| Last pre-start research refresh | **2026-09-07 00:57:17 AEST** |
| Delivery-time crossing | **01:00:00 AEST passed before issue** |
| Immediate post-start structured state | **DELAYED; 0 plays, 0 total yards, 0:00 possession** |
| Field-owner delay + zero-play confirmation | **NOT RECOVERED** |
| Final state | **LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST** |
| Four ranked picks | **NOT ISSUED** |
| Potential winner | **NOT ISSUED** |
| Probability state | **NOT ISSUED** |
| Retrospective | **NOT PERFORMED — explicitly deferred** |

## Why the researched pregame ranking was not issued

The user requested a pregame four-row forecast. Research was substantially complete before the verified rescheduled 11:00 AM EDT / 1:00 AM AEST kickoff, but the final user-facing issue occurred after the scheduled start.

Under `RULES_GENERAL.md` §2, once scheduled start has passed:
- a stale pregame freeze may not be delivered merely because research began before kickoff;
- a live view requires exact verified live state;
- `LIVE — DELAYED ZERO-PLAY` requires the field owner to establish both the delay and that no sport-native unit has begun;
- if that cannot be established, the permitted output is `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`.

The immediate post-start structured feed marked the event **DELAYED** and showed zero plays/yards/possession, but Campbell's official schedule had not yet published a delay/zero-play state. Because the two required field-owner facts were not jointly verified, the pregame four-row snapshot was withheld.

No market result, live score, play, possession or post-start performance was used to create a replacement ranking.

## Pregame research retained for audit, not issued as picks

The following evidence was gathered before the start crossing and is retained only to document the research process:

### Current quarterback / participant picture

**Western Carolina**
- Lex Thomas was the current starting-QB regime entering the game.
- Week 0 vs Eastern Kentucky: 27/35, 320 passing yards, 3 passing TD; 69 rushing yards and 1 rushing TD.
- Backup branch included Isaac Lee and other roster QBs.
- Current offensive skill contributors included AJ Colombo, Michael Rossin and Josh Perry.

**Campbell**
- Kamden Sixkiller was the current starting-QB regime entering the game.
- Week 0 vs ETSU: 29/42, 343 passing yards, 2 passing TD; 95 rushing yards and 2 rushing TD.
- Campbell returned four of five offensive-line starters and had substantial QB/receiver continuity.
- Campbell allowed 528 total yards to ETSU in the opener.

A uniform school-issued game-day injury/inactive report was not recovered for either FCS program. Under `AM-P5`, absence of an NFL-style report was not interpreted as full health.

### Current form and historical context

- Western Carolina beat Eastern Kentucky **45-21** in Week 0.
- Campbell beat ETSU **49-37** in Week 0.
- 2025 H2H at Barker-Lane: Western Carolina won **42-35**.
- 2024 H2H: Campbell won **24-16**.
- Current-regime continuity was stronger for Campbell at QB because Sixkiller remained the starter; Western Carolina's 2025 H2H quarterback was not the current starter.

### Weather

Pregame conditions around Barker-Lane Stadium:
- about **79°F / 26°C**
- mostly cloudy
- roughly **49% precipitation probability around 11 AM/noon**
- thunderstorm risk increasing later in the game window.

The weather created meaningful wet-ball/lightning uncertainty but was not converted into a post-start directional forecast.

## Source register — P-326

### Google Drive
- `METHOD.md` — MDS-2026.09.06-v4.0 lifecycle.
- `RULES_GENERAL.md` — start-crossing and zero-play-delay state requirements.
- `RULES_AMERICAN_FOOTBALL.md` — NCAA/FCS QB, unit-exposure, college-availability and weather controls.
- local `PREDICTION_MINI_RUNNING_LOG_P325_UPDATED.md` — immediate append-only handoff.

### Event / state
- Campbell official schedule:
  https://gocamels.com/sports/football/schedule/2026
- Current structured post-start feed:
  FOX Sports Western Carolina vs Campbell game feed, showing DELAYED with zero plays/yards/possession.
- CBS current schedule cross-check showing Sunday 11:00 AM ET.

### Pregame team research
- Western Carolina Week 0 official recap:
  https://catamountsports.com/news/2026/8/29/football-thomas-defense-fuel-second-half-surge-in-45-21-opening-win-over-eku.aspx
- Western Carolina current stats / roster / Lex Thomas award pages.
- Campbell Week 0 official recap:
  https://gocamels.com/news/2026/8/30/football-camels-down-etsu-in-season-opener-49-37.aspx
- Campbell current preview / Sixkiller feature / current roster.
- 2025 official H2H Campbell recap and Western Carolina box score.

### Weather
- Venue-local structured Buies Creek hourly forecast.
- National Weather Service point forecast for Buies Creek/Harnett County.

### Explicit exclusions
Sportsbook prices, implied probabilities, market movement, public betting percentages, tipster picks and synthetic/AI predictions were excluded. Search results that surfaced betting prices were not used as sporting evidence.

## Bottom line

**No actionable P-326 forecast was issued.**

Reason: **scheduled start crossed before delivery, and the immediate delayed/zero-play state could not be jointly confirmed by the field owner.**

**P-326 status:** `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`  
**Retrospective:** deferred.  
**Next local slot:** `P-327`.



---

# P-327 — Angers SCO vs Stade Rennais FC — 2026-27 Ligue 1

## 1. Frozen identity / state

| Field | Frozen value |
|---|---|
| Local continuation ID | `P-327` |
| Population | Soccer — France Ligue 1 — **EXPLORATORY / NOT PRIMARY-SCORED** |
| Competition | Ligue 1 McDonald's 2026-27, Matchday 3 |
| Event | Angers SCO vs Stade Rennais FC |
| Venue | Stade Raymond-Kopa, Angers |
| Verified kickoff | **2026-09-06 17:15 CEST / 2026-09-07 01:15 AEST** |
| Structured game ID | `72036146` |
| Final state refresh | **2026-09-07 01:09:21 AEST** |
| State | **PREGAME / Scheduled** |
| Method | **MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND** |
| Probability tier | **UNVALIDATED_SUBJECTIVE** |
| Numerical state | Stage S0 — no fitted/validated soccer model |
| Retrospective | **NOT PERFORMED — explicitly deferred** |

## 2. Frozen five-row slate

1. **1st Half Over 0.5 Goals**
2. **Total Match Corners Over 8.5**
3. **Full Match Over 2.5 Goals**
4. **Full Match Under 2.5 Goals**
5. **1st Half Under 0.5 Goals**

### Corner definition

User did not supply the sportsbook/stat-provider definition. Research target:
**combined regulation-time corners, 90 minutes plus stoppage time, Over 8.5**.

Because provider/settlement terms are unresolved, the corner row remains `FORCED RANK / MEDIUM-LOW` even though the sporting direction is favourable.

## 3. Participant / availability audit

### Rennes

Official current 21-man travelling/match group:
Kilian Belazzoug, Nicolas Lemaître, Brice Samba,
Przemysław Frankowski, Bryan Reynolds, Charlie Cresswell, Anthony Rouault, Gonçalo Oliveira, Quentin Merlin, Mahamadou Nagida,
Valentin Rongier, Adrien Thomasson, Mahdi Camara, Ludovic Blas, Sebastian Szymański,
Mousa Al-Tamari, Issa Soumaré, Eliezer Mayenda, Boulaye Dia, Estéban Lepaul, Arnaud Nordin.

Confirmed current absence:
- **Abdelhamid Aït Boudlal — not in squad for family/personal reason (expecting a child).**

Brice Samba:
- missed Le Mans because of a muscle issue;
- returned to training;
- **is included in today's official squad**.
Therefore he is **not labelled OUT**, but the starting goalkeeper was not confirmed before freeze.

Latest official Rennes league XI vs Le Mans:
Nicolas Lemaître; Frankowski, Cresswell, Aït Boudlal, Merlin; Szymański, Rongier, Thomasson; Al-Tamari, Lepaul, Soumaré.

Current team-sheet status:
- exact starting XI: **NOT RETRIEVED / not field-owner confirmed at freeze**
- exact bench: **NOT RETRIEVED**
- manager: **Franck Haise**

### Angers

Exact current official Matchday-3 squad/starting XI was not recovered before freeze.

Latest confirmed opening-round XI vs Lille:
Anthony Lopes; Raolisoa, Camara, Lefort, Ekomié; Belkhdim, van den Boomen; Allevinah, Bermont, Sbaï; El Ouazzani.

Against Auxerre, Angers won 3-1 with the same broad 4-2-3-1/attacking structure and van den Boomen, Harouna Djibirin and El Ouazzani scoring.

Current secondary injury reports:
- **Haris Belkebla — thigh injury / expected mid-September**
- **Louis Mouton — knee injury / about 1–2 weeks**
These are recorded as secondary-only because a final official Angers matchday release was not recovered.

Manager: **Stéphane Gilli**.

### Participant gate

`SO-P2 = PARTIAL`.
Exact current XIs/full benches were unresolved, so side and full-match total confidence is capped. Full-game total cannot occupy Rank #1 under the current bench rule.

## 4. Current first-half process

Current Ligue 1 matches:

### Angers
- vs Lille: **HT 0-2**, goals conceded 11' and 31'
- at Auxerre: **HT 1-1**, Angers scored 5', Auxerre 35'

### Rennes
- vs PSG: **HT 2-0**, Rennes goals 9' and 38'
- vs Le Mans: **HT 2-1**, goals at 5', 26', 30'

Thus every one of the four current league matches involving these clubs has contained at least one first-half goal.

Historical league baselines:
- 2025-26 Ligue 1 1H Over 0.5: ~70%
- broader 2024-26 pooled Ligue 1: ~72.9%
- Rennes 2025-26: ~76.5% 1H Over 0.5

Mechanisms:
- Rennes are currently creating early through Lepaul/Szymański/Rongier and transition attacks.
- Angers have both scored and conceded inside the first 11 minutes this season.
- Angers' opening Lille match showed defensive exposure before halftime.
- Rennes' first two league matches both became multi-goal first halves.

Kill paths:
- unresolved starting goalkeeper/defensive personnel;
- Angers may lower their block at home against Rennes;
- hot conditions may reduce sustained pressing intensity;
- current 4/4 is a tiny sample and is not used as a standalone rule.

### First-half probability bookkeeping

- 50% × 2025-26 league prior 70% = 35.0 pp
- 20% × broader two-season Ligue 1 72.9% = 14.58 pp
- 15% × Rennes prior 76.5% = 11.48 pp
- 15% × current four-match sample 100% = 15.0 pp

Baseline = **76.06%**

Signed adjustments:
- exact current XIs/GK unresolved: **-1 pp**
- heat / possible pacing reduction: **0 to -1 pp**, treated mainly as width
- direct early-goal mechanisms current: already represented in current sample; no double-count

Final:
- **1H Over 0.5 = 75% UNVALIDATED_SUBJECTIVE**
- **1H Under 0.5 = 25%**

Subjective width: roughly ±9 pp.

## 5. Full-match goal process

### Current season
Angers:
- 0-2 Lille
- 3-1 Auxerre
=> 3 GF / 3 GA, **3.0 total goals per match**

Rennes:
- 2-2 PSG
- 3-2 Le Mans
=> 5 GF / 4 GA, **4.5 total goals per match**

Combined current midpoint = **3.75 goals**

### Recent L5
Angers recent five league scores:
1-3, 1-1, 1-1, 0-2, 3-1
=> GF 6 / GA 8, total environment **2.8**

Rennes recent five:
2-4, 2-1, 1-3, 2-2, 3-2
=> GF 10 / GA 12, total environment **4.4**

Combined L5 midpoint = **3.6**

### L10
Current-reconstructed Angers L10:
GF ~9 / GA ~19 => **2.8 total/match**

Current-reconstructed Rennes L10:
GF ~21 / GA ~17 => **3.8 total/match**

Combined midpoint ≈ **3.3**

### L15 / L20 note
Source indexing around the season boundary is not perfectly synchronized. The available long-window provider records still show:
- Angers last-20 historical profile approximately **15–17 GF / 25–26 GA**
- Rennes long-window profile approximately **35–37 GF / 27–29 GA**

These windows support Rennes as the stronger scoring side but are treated with lower weight because of current-season roster changes and source-lag ambiguity.

### H2H
Recent official sequence:
- Rennes 2-1 Angers (Apr 2026)
- Angers 1-1 Rennes (Aug 2025)
- Angers 0-3 Rennes (Mar 2025)
- Rennes 2-0 Angers (Dec 2024)
- Rennes 4-2 Angers (Apr 2023)

3 of those 5 finished Over 2.5.

### Full-total arithmetic

Inputs:
- 40% × 2025-26 Ligue 1 mean 2.82 = **1.128**
- 20% × current-season midpoint 3.75 = **0.750**
- 20% × L5 midpoint 3.60 = **0.720**
- 10% × L10 midpoint 3.30 = **0.330**
- 10% × recent H2H mean 3.20 = **0.320**

Baseline = **3.248 goals**

Signed adjustments:
- current Rennes attacking personnel / Lepaul form: **+0.10**
- current Angers defensive/personnel uncertainty: **+0.05**
- exact XIs/full benches unresolved: **-0.15 signed centre, wider tail**
- hot conditions: **-0.10**

Resulting centre ≈ **3.15 goals**
Width ≈ **±1.35 goals**

2.5 is ~0.65 below the centre.

Final:
- **Over 2.5 = 60% UNVALIDATED_SUBJECTIVE**
- **Under 2.5 = 40%**

### Component budget
Working allocation:
- Rennes scoring component ≈ **1.85**
- Angers scoring component ≈ **1.30**
- sum ≈ **3.15**

The Rennes share is supported by stronger current and long-window scoring, but Angers' 3-1 at Auxerre preserves a meaningful home scoring branch.

## 6. Corner process

Current exact corner results:
- Angers vs Lille: **8-3**, total 11
- Auxerre vs Angers: **7-10**, total 17
- Rennes vs PSG: **0-10**, total 10
- Rennes vs Le Mans: **8-6**, total 14

All four current league matches reached at least **10 total corners**.

Broader context:
- 2025-26 Ligue 1 average about **9.4 corners/match** in the retrieved historical table.
- 2025-26 Over 8.5 corners rate around **56%** in that dataset.
- Rennes have taken **127 corners over their last 20 league matches = 6.35 per match**.
- Rennes' rolling total-corner match environment is approximately **10.9** over the last 12 months.
- Recent Angers–Rennes H2H average is about **8.8** total corners.

Mechanism:
- Angers have generated high current corner volume themselves (8 and 10).
- Rennes can create sustained width/cross/block sequences, especially through Frankowski/Merlin and attacking changes.
- When Rennes sit deeper, the opponent can take over corner volume, as PSG's 10 corners showed.
- This makes a **combined** corner total more robust than simply assuming Rennes domination equals Rennes corners.

### Corner bookkeeping

Qualitative centre:
- league prior ≈ 9.4
- current four-match mean = (11+17+10+14)/4 = **13.0**
- Rennes rolling environment ≈ 10.9
- H2H ≈ 8.8

Heavy shrinkage to league/H2H because current sample is four matches.

Working centre ≈ **10.4 corners**
Width ≈ **±3.4 corners**

At 8.5:
- **Over 8.5 = 64% UNVALIDATED_SUBJECTIVE**

Provider caveat:
`UNKNOWN_DEFINITION`, so verdict remains `FORCED RANK / MEDIUM-LOW`.

## 7. Weather / surface

Venue-specific structured forecast for **Stade Raymond-Kopa** at research time:
- current around **32°C**
- mostly sunny / intermittent clouds
- no meaningful rain signal in the immediate match window.

Météo-France Angers government forecast:
- hot/sunny Sunday afternoon
- weak wind
- no material precipitation mechanism around the match.

There is some temperature granularity difference between the exact-stadium structured point and the municipality-level government page, but both agree on the important football mechanism: **hot, dry, low-rain conditions with no strong wind**.

Effects:
- heat can reduce prolonged pressing and late tempo;
- dry conditions preserve normal surface speed and footing;
- no rain/wind mechanism supports a strong Under.

Net total adjustment: **-0.10 goals**, mainly via heat.
No corner-direction adjustment beyond wider late-game tempo uncertainty.

## 8. Rest / schedule

- Angers last played Aug 29 at Auxerre: about 8 days rest.
- Rennes last played Aug 30 vs Le Mans: about 7 days rest.
- No meaningful congestion asymmetry.
- Rennes next play Marseille on Sep 11, but no verified pre-match rotation statement justified downgrading today's XI.

Rest adjustment: **0.00**.

## 9. Bidirectional-sign audit

1. **Rennes early attack**
   - supports 1H Over and FT Over;
   - an early lead can reduce second-half attacking need.
2. **Angers current high corner production**
   - supports total-corner Over;
   - if Angers convert pressure early, corner demand can fall.
3. **Hot weather**
   - can suppress press/tempo;
   - can also create fatigue-driven defensive errors late.
4. **Samba availability uncertainty**
   - a returning first-choice keeper can help Rennes defence;
   - incomplete match sharpness can widen keeper outcomes.
5. **Angers 3-1 win at Auxerre**
   - supports Angers scoring and FT Over;
   - two late goals came after 70', so it does not backfill first-half evidence.
6. **Rennes' PSG match**
   - Rennes scored twice despite only 30.5% possession and zero corners;
   - transition scoring and corner production are therefore explicitly separated.

## 10. Frozen ranking

| Rank | Contract | UNVALIDATED_SUBJECTIVE probability | Verdict | Evidence |
|---:|---|---:|---|---|
| **1** | **1st Half Over 0.5 Goals** | **75%** | **LEAN** | **MEDIUM** |
| **2** | **Total Match Corners Over 8.5** | **64%** | **FORCED RANK** | **MEDIUM-LOW** |
| **3** | **Full Match Over 2.5 Goals** | **60%** | **LEAN direction / capped** | **MEDIUM-LOW** |
| **4** | **Full Match Under 2.5 Goals** | **40%** | **FORCED RANK** | **LOW–MEDIUM-LOW** |
| **5** | **1st Half Under 0.5 Goals** | **25%** | **FORCED RANK** | **LOW** |

Complementary coherence:
- 1H O0.5 75% + U0.5 25% = 100%
- FT O2.5 60% + U2.5 40% = 100%

## 11. Potential winner

### **Rennes — slight regulation-time lean**

`UNVALIDATED_SUBJECTIVE` 1X2:
- **Rennes 55%**
- **Draw 25%**
- **Angers 20%**

Why Rennes:
- stronger current scoring output (5 goals in two vs Angers 3).
- Rennes' recent L5/L10 attack is materially stronger.
- Lepaul has scored three league goals already.
- Rennes have won 11 of the last 15 H2Hs in the retrieved long H2H set.
- deeper officially named current attacking squad: Lepaul, Dia, Mayenda, Nordin, Al-Tamari, Blas, Szymański.

Why only slight:
- exact XI and goalkeeper are not confirmed.
- Angers are at home and just won 3-1 at Auxerre.
- Rennes conceded four in their first two matches.
- Aït Boudlal is unavailable.
- Samba's return-to-squad status does not guarantee he starts or is at full match sharpness.

Representative score families:
- **Angers 1-2 Rennes**
- **1-1**
- **Angers 1-3 Rennes**
- upset tail **2-1 Angers**

## 12. Settlement preregistration

- score / first-half score / winner: official Ligue 1 / club match centre.
- corners: named official/structured provider field when available; `OPERATOR_ACTION = UNKNOWN_DEFINITION` unless user's sportsbook terms are supplied.

## 13. Source register — P-327

### Google Drive
- `METHOD.md` — MDS-2026.09.06-v4.0 active.
- `RULES_SOCCER.md` — participant, goal, corner, provider and substitution controls.
- `LEAGUE_RULES_SOCCER.md` — Ligue 1 regulation rules.
- `RULES_GENERAL.md` — v4 state, participant, environment, arithmetic and final-refresh gates.
- local `PREDICTION_MINI_RUNNING_LOG_P326_UPDATED.md` — append-only handoff.

### Official identity / current squad
- Angers official schedule:
  https://angers-sco.fr/equipe-pro/calendrier-resultat/
- Angers official programming:
  https://angers-sco.fr/programmation-decouvrez-la-programmation-des-4-premieres-journees-de-ligue-1/
- Rennes official current squad:
  https://www.staderennais.com/actualites/ligue-1-mcdonalds/le-groupe-face-au-sco-0
- Rennes current pre-match conference:
  https://www.staderennais.com/actualites/ligue-1-mcdonalds/la-conference-de-presse-davant-match
- Structured game ID `72036146`, final refresh 01:09:21 AEST: Scheduled.

### Current match/process
- Lille official Angers 0-2 report:
  https://www.losc.fr/actualites/2026-08-23/angers-losc-le-compte-rendu
- Auxerre–Angers current match stats/report:
  Maxifoot / TNT Sports exact match records.
- PSG official Rennes 2-2 record:
  https://www.psg.fr/en/matches/mens-football/20262027/paris-vs-rennes-2026-08-23
- Rennes official Le Mans 3-2 report:
  https://www.staderennais.com/actualites/equipe-pro/trois-buts-et-trois-points-a-la-maison
- Rennes official match stats page for Le Mans.

### Historical/statistical research
- StatMuse transient current/historical match logs for Angers and Rennes.
- Ligue 1 official 2025-26 season goal average: 2.82.
- PerformanceOdds 2025-26 first-half/Over trends.
- historical Ligue 1 corner table / current Rennes corner rolling data.
- TotalCorner H2H descriptive corner history.

### Weather
- exact Stade Raymond-Kopa structured weather forecast.
- Météo-France Angers government forecast:
  https://meteofrance.com/previsions-meteo-france/angers/49000

### Explicit exclusions
Bookmaker prices, implied probabilities, betting consensus, market movement, tipster picks, prediction models and synthetic/AI simulations were excluded from ranking. Any bookmaker odds encountered in search were ignored.

## 14. Bottom line

1. **1H Over 0.5 — 75% UNVALIDATED_SUBJECTIVE**
2. **Total Match Corners Over 8.5 — 64%**
3. **FT Over 2.5 — 60%**
4. **FT Under 2.5 — 40%**
5. **1H Under 0.5 — 25%**

**Potential winner: Rennes — 55% regulation-time UNVALIDATED_SUBJECTIVE**

**P-327 status:** `PREGAME — UNSETTLED`
**Population:** `EXPLORATORY — NOT SCORED`
**Retrospective:** deferred.
**Next local slot:** `P-328`.


---

# P-328 — Arsenal vs Chelsea — 2026-27 English Premier League

## Frozen identity / state
- Competition: English Premier League 2026-27, Matchweek 3.
- Venue: Emirates Stadium, London.
- Verified kickoff: **2026-09-06 16:30 BST / 2026-09-07 01:30 AEST**.
- Structured game ID: `72221232`.
- G31 refresh: **2026-09-07 01:27:48 AEST — Scheduled**.
- Method: **MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND**.
- Population: **EPL — PRIMARY_SCORED**.
- Probability tier: **UNVALIDATED_SUBJECTIVE**.
- Retrospective: deferred.

## Current participant picture

### Arsenal — current matchday XI reported across multiple current live sources
Raya; White, Konsa, Gabriel, Calafiori; Rice, Lewis-Skelly; Saka, Ødegaard, Tzolis; Havertz.

Bench:
Arrizabalaga, Hincapié, Eze, Merino, Zubimendi, Bruno Guimarães, Dowman, Gyökeres, Madueke.

Availability:
- William Saliba — absent/injured.
- Cristhian Mosquera — absent after knock.
- Jurrien Timber — not in current matchday group.
- Bruno Guimarães — fit enough for bench after knock.
- Arsenal attacking bench retains Eze, Gyökeres and Madueke.

### Chelsea — current matchday XI reported across multiple current live sources
Emiliano Martínez; Acheampong, Lacroix, Fofana; Pedro Neto, Reece James, Romeo Lavia, Jorrel Hato; Cole Palmer, Morgan Rogers; João Pedro.

Bench:
Penders, Colwill, Gusto, Chavarría, Barco, Quenda, Gittens, Welbeck, Estêvão.

Availability:
- Moisés Caicedo — unavailable due to fitness issue.
- Levi Colwill — bench, therefore not labelled out.
- Reece James starts.
- Chelsea retain attacking bench options Estêvão, Quenda, Gittens and Welbeck.

Participant status:
`SO-P2 = PARTIAL / SECONDARY_ONLY`.
The exact current XIs and full benches are strongly corroborated by multiple same-day current sources, but both were not recovered from field-owner lineup pages before freeze. Side and full-total rows therefore remain capped.

## Current 2026-27 process

Arsenal:
- 3-0 Coventry; HT 2-0.
- 1-0 Aston Villa; HT 0-0.
- GF 4 / GA 0.
- xG **2.84**, xGA **0.62**.
- corners won **12** in two matches: 8 vs Coventry, 4 at Villa.
- Arsenal have allowed only one shot on target across their opening two league matches according to current reporting.

Chelsea:
- 3-2 Fulham; HT 2-1.
- 4-3 Brighton; HT 3-1.
- GF 7 / GA 5.
- xG **5.32**, xGA **2.95**.
- corners won **8** in two matches: 4 and 4.
- corners conceded: Fulham 6, Brighton 7 => **13 / 6.5 per match**.
- Chelsea's two league matches have both been high-event, transition-heavy games.

## Recent H2H
- 2025-11-30: Chelsea 1-1 Arsenal; HT 0-0; corners 3-3.
- 2026-03-01: Arsenal 2-1 Chelsea; HT 1-1; corners Arsenal 5, Chelsea 10.
Arsenal are unbeaten in the last five league H2Hs in the retrieved current record and won the most recent.

## 1H goal object

Inputs:
- 55% × EPL 2025-26 1H O0.5 prior ~72% = 39.6 pp
- 20% × Arsenal current 1/2 = 10.0 pp
- 20% × Chelsea current 2/2 = 20.0 pp
- 5% × recent H2H 1/2 = 2.5 pp

Baseline = **72.1%**

Signed adjustments:
- Arsenal elite current defensive suppression / 0.62 xGA: **-4 pp**
- Chelsea current fast-start attack (goals at 1', 4', 14', 32' across first two): **+2 pp**
- lineups secondary-only rather than field-owner confirmed: **-2 pp width/caution**

Final:
- **1H Over 0.5 = 68%**
- **1H Under 0.5 = 32%**
- subjective width ~±9 pp.

## Corner object — Arsenal team corners O4.5

Direct current evidence:
- Arsenal own corners: 8, 4 => mean **6.0**
- Chelsea corners conceded: 6, 7 => mean **6.5**
- Arsenal home last-five corner sample available: 8, 3, 3, 7, 10 => mean **6.2**
- recent H2H Arsenal corners: 3 and 5 => mean **4.0**

Arithmetic:
- 35% × 6.0 = 2.10
- 30% × 6.5 = 1.95
- 20% × 6.2 = 1.24
- 15% × 4.0 = 0.60

Baseline = **5.89 Arsenal corners**

Adjustments:
- Chelsea 3-4-2-1 wing-back structure can concede end-line/cross volume: **+0.15**
- early Arsenal lead can reduce later corner need: **-0.15**

Centre = **5.9**, width ~±2.7.

Final:
- **Arsenal Over 4.5 team corners = 62% UNVALIDATED_SUBJECTIVE**.

Provider/definition not supplied:
`UNKNOWN_DEFINITION`; row remains `FORCED RANK / MEDIUM-LOW`.

## Full-match goal object

Current midpoint total environment:
- Arsenal: 2.0 goals/match
- Chelsea: 6.0 goals/match
=> midpoint **4.0**, but this is only two matches each and is heavily shrunk.

Prior / current arithmetic:
- 45% × 2025-26 EPL mean 2.75 = **1.238**
- 25% × recent Arsenal/Chelsea H2H mean 2.5 = **0.625**
- 20% × current environment midpoint 4.0 = **0.800**
- 10% × current xG+xGA blended environment ≈2.9 = **0.290**

Baseline ≈ **2.95 goals**

Signed adjustments:
- Arsenal current defensive suppression: **-0.25**
- Chelsea current attack / Palmer-Rogers-João Pedro transition quality: **+0.20**
- Arsenal centre-back disruption (Saliba/Mosquera out, Konsa debut): **+0.10**
- Caicedo absence weakens Chelsea midfield control: **+0.10**
- secondary-only lineup status / derby control branch: **-0.10**
- weather: **0.00**

Resulting centre ≈ **3.00 goals**
Width ≈ **±1.30**.

2.5 is 0.50 below centre.

Final:
- **Over 2.5 = 53%**
- **Under 2.5 = 47%**

The line sits inside the central width, so neither total side is strong.

Component budget:
- Arsenal scoring component ≈ **1.70**
- Chelsea scoring component ≈ **1.30**
- combined ≈ **3.00**.

## Weather / rest
Emirates Stadium match-window structured forecast:
- around **26°C**
- mostly cloudy / partly sunny
- no material precipitation or strong-wind mechanism.

Rest:
- Arsenal last played Aug 31: ~6 days.
- Chelsea last played Aug 30: ~7 days.
No meaningful congestion asymmetry.

## Bidirectional-sign audit
1. Arsenal defensive form supports Under and Arsenal side, but Saliba/Mosquera absences widen Chelsea scoring tail.
2. Chelsea's fast starts support 1H Over, but Arsenal have allowed almost no current shot quality.
3. Caicedo absence can increase Chelsea defensive exposure, but may also push Chelsea toward a more conservative midfield.
4. Arsenal territory supports corners, but an early lead can reduce later corner demand.
5. Chelsea's transition threat can create goals without possession and does not imply Chelsea corner dominance.
6. Recent H2H has been controlled, but both current attacking structures have changed.

## Frozen ranking
| Rank | Contract | UNVALIDATED_SUBJECTIVE | Verdict |
|---:|---|---:|---|
| **1** | **1H Over 0.5 goals** | **68%** | LEAN / MEDIUM |
| **2** | **Arsenal team corners Over 4.5** | **62%** | FORCED RANK / MEDIUM-LOW |
| **3** | **FT Over 2.5 goals** | **53%** | LEAN direction / MEDIUM-LOW |
| **4** | **FT Under 2.5 goals** | **47%** | FORCED RANK / MEDIUM-LOW |
| **5** | **1H Under 0.5 goals** | **32%** | FORCED RANK / LOW |

## Potential winner
**Arsenal — slight regulation-time lean**

UNVALIDATED_SUBJECTIVE 1X2:
- Arsenal **51%**
- Draw **27%**
- Chelsea **22%**

Reasons:
- home field;
- reigning champions and 2-0-0 start with 4-0 goal difference;
- current defensive process is materially stronger;
- Arsenal are unbeaten in the recent league H2H set and won the latest meeting;
- Chelsea's Caicedo absence matters to midfield control.

Why only slight:
- Arsenal have Saliba and Mosquera absent;
- Chelsea's Palmer/Rogers/João Pedro attack has produced seven goals in two league matches;
- Chelsea are also 2-0-0;
- current lineups were not recovered from both clubs' field-owner pages.

Representative scores:
- Arsenal 2-1 Chelsea
- 1-1
- Arsenal 2-0 Chelsea
- Chelsea upset tail 1-2

## Settlement preregistration
- score / first-half score / winner: official Premier League structured match record.
- corners: official structured EPL `wonCorners` field where available; operator-specific action remains `UNKNOWN_DEFINITION` unless user's sportsbook terms are supplied.

## Source register
Google Drive:
- METHOD.md — MDS-2026.09.06-v4.0.
- RULES_SOCCER.md — SO-P2/SO-P3, goal/corner separation, early-goal and bench controls.
- LEAGUE_RULES_SOCCER.md — EPL regulation rules.
- local PREDICTION_MINI_RUNNING_LOG_P327_UPDATED.md — append-only handoff.

Current identity/state:
- structured EPL schedule/game ID `72221232`.
- final G31 refresh 01:27:48 AEST: Scheduled.
- Chelsea official preview confirms Sep 6, 16:30 BST, Emirates Stadium.

Current lineups:
- Guardian current live Arsenal-Chelsea coverage.
- current confirmed-lineup reporting from Yahoo/Roundtable Sports, SBNation and ArsenalStation.
- field-owner lineup pages for both clubs were not independently recovered before freeze; status therefore `SECONDARY_ONLY`.

Current team stats:
- StatMuse Arsenal 2026-27 aggregate: GF4 GA0, xG2.84 xGA0.62, 12 corners.
- StatMuse Chelsea 2026-27 aggregate: GF7 GA5, xG5.32 xGA2.95, 8 corners.
- StatMuse exact Arsenal-Coventry, Villa-Arsenal, Fulham-Chelsea and Chelsea-Brighton match records.
- Chelsea official Brighton match report.

H2H:
- StatMuse Chelsea 1-1 Arsenal, Nov 30 2025.
- StatMuse Arsenal 2-1 Chelsea, Mar 1 2026.

Weather:
- venue-specific structured Emirates Stadium forecast.

Explicit exclusions:
bookmaker odds, implied probabilities, market movement, betting consensus, tipster picks and synthetic/AI predictions.

## Bottom line
1. **1H Over 0.5 — 68%**
2. **Arsenal team corners O4.5 — 62%**
3. **FT Over 2.5 — 53%**
4. **FT Under 2.5 — 47%**
5. **1H Under 0.5 — 32%**

Potential winner: **Arsenal — 51% regulation-time lean**.

**P-328 status:** `PREGAME — UNSETTLED`
**Population:** `EPL — PRIMARY_SCORED`
**Retrospective:** deferred.
**Next local slot:** `P-329`.


---

# P-329 — Bologna vs Sassuolo — 2026-27 Serie A

## 1. Frozen identity / state

| Field | Frozen value |
|---|---|
| Local continuation ID | `P-329` |
| Population | Soccer — Italy Serie A — **EXPLORATORY / NOT PRIMARY_SCORED** |
| Competition | Serie A 2026-27, Matchday 3 |
| Event | Bologna vs Sassuolo |
| Venue | Stadio Renato Dall'Ara, Bologna |
| Verified kickoff | **2026-09-06 18:00 CEST / 2026-09-07 02:00 AEST** |
| Structured game ID | `71945226` |
| Final G31 refresh | **2026-09-07 01:35:59 AEST** |
| State | **PREGAME / Scheduled** |
| Method | **MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND** |
| Numerical state | Stage S0 — no fitted/validated soccer model |
| Probability tier | **UNVALIDATED_SUBJECTIVE** |
| Retrospective | **NOT PERFORMED — explicitly deferred** |

## 2. Frozen five-row slate

1. **Total Match Corners Over 6.5**
2. **Full Match Under 2.5 Goals**
3. **1st Half Over 0.5 Goals**
4. **1st Half Under 0.5 Goals**
5. **Full Match Over 2.5 Goals**

Corner definition:
- target is combined regulation-time corners, 90 minutes plus stoppage time;
- exact sportsbook/provider definition not supplied;
- `UNKNOWN_DEFINITION`, therefore corner row remains `FORCED RANK / MEDIUM-LOW`.

## 3. Current participant / availability picture

### Bologna — current matchday XI listed by Sky
Skorupski;
Zortea, Heggem, Theate, Miranda;
Ferguson, Moro;
Bernardeschi, Odgaard, Cambiaghi;
Piccoli.

Bench:
Pessina, Happonen, Holm, Vitik, De Silvestri, Alhassane, Helland, Pobega, Mbangula, Amondarain, Dovbyk, Enem.

Confirmed / current unavailable:
- **Riccardo Orsolini — OUT**, left-hamstring injury, Bologna official recovery estimate about 3 weeks.
- **Oussama El Azzouzi — unavailable**, thigh issue / separate training earlier in week.

Current selection implications:
- Bernardeschi replaces Orsolini on the right attacking line.
- Dovbyk is an attacking second-half option from the bench.
- Theate starts after recent arrival/competition for the centre-back place.
- Bologna retain attacking bench depth through Dovbyk and Mbangula.

### Sassuolo — current matchday XI listed by Sky
Murić;
Cinquegrano, Leysen, Idzes, Doig;
Adžić, Matić, Bakola;
Volpato, Bowie, Laurienté.

Bench:
Turati, Satalino, Obrador, Odenthal, Ćaleta-Car, Van der Brempt, Thorstvedt, Dominguez, Sulemana, Lipani, Berardi, Esposito, Kulla.

Unavailable / injury list:
- **Sebastian Walukiewicz — muscle injury**
- **Ismaël Koné — broken ankle**
- **Daniel Boloca — knee/muscle injury**
- **Edoardo Pieragnolo — cruciate-knee injury**
- **Fali Candé — cruciate-knee injury**

Selection implications:
- **Domenico Berardi starts on the bench**, despite scoring the winner vs Torino.
- Sassuolo still have late attacking escalation through Berardi, Esposito and Dominguez.
- current midfield has Matić as the senior control point with Adžić/Bakola.

### Participant gate
The current XI/bench set is strongly current and same-day on Sky, while Bologna's squad/injury record is club-official. A field-owner lineup page for both clubs was not independently recovered before freeze, so participant status is treated as **current secondary-confirmed / not dual field-owner confirmed**.

Side/full-total confidence is therefore capped at `MEDIUM-LOW`.

## 4. Current scoring / chance process

### Bologna
2026-27:
- Bologna 0-1 Lazio
- Atalanta 1-0 Bologna

Current score environment:
- GF 0 / GA 2
- 1.0 total goals per match

But the chance process is better than the scoreline:
- vs Lazio: Bologna **1.85 xG**, Lazio 0.73
- at Atalanta: Bologna **1.18 xG**, Atalanta 0.22
- total Bologna xG ≈ **3.03**, goals scored = 0

This is a severe early finishing shortfall, but the v4 early-season rule forbids assuming automatic regression. Orsolini's injury removes one of Bologna's highest-quality finishing/set-piece threats, which weakens the simple “xG must convert” argument.

Defensively:
- only ≈0.95 opponent xG across the two league games;
- both concessions were second-half goals;
- Bologna were 0-0 at halftime in both league matches.

### Sassuolo
2026-27:
- Atalanta 2-1 Sassuolo
- Sassuolo 2-1 Torino

Current score environment:
- GF 3 / GA 3
- 3.0 total goals per match

Chance process:
- at Atalanta: Sassuolo ≈2.70 xG, 22 shots, 8 on target
- vs Torino: Sassuolo ≈1.73 xG, 19 shots, 7 on target
- current attacking xG ≈ **4.43 / 2 = 2.22 per match**

Sassuolo have therefore created materially more attack than the raw 3 goals indicate.

Contrary path:
- current XI leaves Berardi on the bench;
- Sassuolo played a Coppa Italia tie four days earlier;
- Bologna's defence has suppressed opponent xG very well.

## 5. L5 / L10 / L15 / L20 trend audit

### Bologna
Current last 10 Serie A record from the retrieved match log:
- GF **11**
- GA **12**
- total environment **2.30 / match**

Latest five:
- 0-1 Atalanta
- 0-1 Lazio
- 3-3 Inter
- 1-0 Atalanta
- 3-2 Napoli
=> GF 7 / GA 7, total environment **2.80**

Longer-window current StatMuse fields:
- last 20 GF around **20**
- last 20 GA around **26**
=> roughly **2.30 total / match**

L15 provider snapshots around the season boundary are not perfectly synchronized; the available sequence supports the same broad pattern: Bologna have often been low-to-mid total, with sporadic high-scoring outliers rather than a persistent high-total regime.

### Sassuolo
Last 10:
- GF **13**
- GA **13**
- total environment **2.60**

Latest five:
- 2-1 Torino
- 1-2 Atalanta
- 0-1 Parma
- 2-3 Lecce
- 1-2 Torino
=> GF 6 / GA 9, total environment **3.00**

Last 15 retrieved provider snapshot:
- GF **19**
- goal differential **-2**, implying GA ≈21
=> total environment ≈ **2.67**

Last 20:
- GF ≈ **26**
- GA ≈ **26**
=> **2.60**

Trend conclusion:
- Bologna's long environment is materially lower.
- Sassuolo are structurally closer to 2.6–3.0.
- current Sassuolo attack is hotter than its long-window baseline, but current personnel/rest reduce confidence in transferring that ceiling unchanged.

## 6. First-half goal process

Current league:
- Bologna-Lazio: **HT 0-0**
- Atalanta-Bologna: **HT 0-0**
- Atalanta-Sassuolo: first goal 6' => 1H O0.5
- Sassuolo-Torino: **HT 1-1** => 1H O0.5

Current combined sample: **2/4** with a first-half goal.

Recent H2H:
- Bologna 1-1 Sassuolo, Dec 2025: **HT 0-0**
- Sassuolo 0-1 Bologna, Mar 2026: Bologna scored at **6'**, HT 0-1

Recent H2H: **1/2** 1H O0.5.

League prior:
- 2025-26 Serie A 1H O0.5 ≈ **65.7–66%**
- two-season 2024-26 pooled baseline ≈ **66.8%**

### 1H arithmetic
- 60% × league prior 65.7% = **39.42 pp**
- 20% × current four-match sample 50% = **10.00 pp**
- 10% × recent H2H 50% = **5.00 pp**
- 10% × current first-half chance environment ≈55% = **5.50 pp**

Baseline ≈ **59.9%**

Signed adjustments:
- Bologna two consecutive 0-0 HT + current strong defensive suppression: **-2 pp**
- Orsolini out / Berardi bench: **-1.5 pp**
- 34°C kickoff heat / lower early press intensity: **-1.5 pp**

Final:
- **1H Over 0.5 = 55%**
- **1H Under 0.5 = 45%**

Width: roughly ±10 pp.

This is not a strong early-goal game. The Over remains only slightly ahead because the league prior and Sassuolo's current early-event profile outweigh Bologna's low-event first halves by a small margin.

## 7. Full-match goal object

### Prior arithmetic

Inputs:
- 35% × 2025-26 Serie A mean ≈2.43 = **0.851**
- 30% × current xG-environment midpoint:
  - Bologna total xG environment ≈1.99
  - Sassuolo total xG environment ≈3.23
  - midpoint ≈2.61
  => **0.783**
- 15% × L10 midpoint (2.30 and 2.60 → 2.45) = **0.368**
- 10% × current score-environment midpoint (1.0 and 3.0 → 2.0) = **0.200**
- 10% × recent H2H average (2 and 1 → 1.5) = **0.150**

Baseline ≈ **2.35 goals**

Signed adjustments:
- Bologna current xG underconversion creates upside branch: **+0.12**
- Sassuolo current attacking process strong: **+0.10**
- Orsolini out: **-0.10**
- Berardi bench at kickoff: **-0.06**
- Sassuolo shorter recovery after Sep 2 cup tie: **-0.04**
- hot/dry 34°C kickoff conditions: **-0.08**
- Sassuolo defensive absences widen Bologna scoring branch: **+0.05**

Resulting centre ≈ **2.34 goals**
Width ≈ **±1.20**

2.5 lies about **0.16 goals above** the centre.

Final:
- **Under 2.5 = 58%**
- **Over 2.5 = 42%**

### Component budget
Working allocation:
- Bologna ≈ **1.25**
- Sassuolo ≈ **1.09**
- total ≈ **2.34**

The Bologna component is higher despite zero goals so far because:
- home field;
- 3.03 xG created in two;
- Sassuolo defensive absences.
It is capped by Orsolini's absence and continued finishing uncertainty.

## 8. Corner process — Total Match Corners Over 6.5

Current exact league corner totals:
- Bologna-Lazio: **8-6 = 14**
- Atalanta-Bologna: **1-2 = 3**
- Atalanta-Sassuolo: **4-4 = 8**
- Sassuolo-Torino: **4-3 = 7**

Current mean = **8.0 total corners**
Over 6.5 = **3/4**.

Longer team corner rates:
- Bologna last 20: **83 corners / 20 = 4.15**
- Sassuolo last 20: **80 corners / 20 = 4.00**
- combined own-corner baseline ≈ **8.15**

Recent H2H:
- Dec 2025: **2-3 = 5**
- Mar 2026: **11 total corners**
- mean = **8.0**

Mechanism:
- Bologna still create crosses/end-line pressure despite low goals; they completed nine crosses in the league opener and produced eight corners.
- Sassuolo have taken four corners in each current league match.
- trailing-state pressure can raise the corner count even in a low-goal game.
- combined total is preferred to a team-only corner line because current share is unstable across score states.

Kill path:
- Bologna-Atalanta produced only three total corners;
- heat can reduce sustained pressing and crossing volume;
- early efficient finishing can lower later corner demand.

Working corner centre ≈ **8.1**
Width ≈ **±3.0 corners**

Final:
- **Total Match Corners Over 6.5 = 61% UNVALIDATED_SUBJECTIVE**

Provider caveat:
`UNKNOWN_DEFINITION`; row remains `FORCED RANK / MEDIUM-LOW`.
Do not transfer this probability to Over 7.5/8.5.

## 9. Rest / rotation

Bologna:
- last league match Aug 31 at Atalanta
- roughly 6 days rest

Sassuolo:
- Sep 2 Coppa Italia vs Frosinone
- 1-1 after 90 minutes, then penalty shootout
- roughly 4 days before this match

Sassuolo's current XI is not identical to the cup XI, but the shorter turnaround matters to late-game pressing/defensive recovery.

Net:
- slight negative to Sassuolo late physical ceiling;
- no large direct winner coefficient because they could rotate from the bench.

## 10. Weather / surface gate

Venue-specific structured forecast:
- kickoff ~**34°C**
- ~32°C around 19:00
- ~31°C around 20:00
- mostly sunny/clear
- no meaningful rain signal
- no strong wind mechanism.

Met Office Bologna/Borgo Panigale:
- precipitation chance <5% through the relevant hours.

Mechanisms:
- hot conditions can lower sustained pressing and repeated high-intensity transitions;
- heat also increases fatigue-related defensive errors late;
- dry footing avoids rain-induced randomness.

Net full-goal adjustment:
**-0.08 goals**, with wider late fatigue tail.

## 11. Bidirectional-sign audit

1. **Bologna 0 goals from 3.03 xG**
   - supports scoring upside;
   - does not guarantee regression, especially with Orsolini absent.
2. **Sassuolo 4.43 current xG**
   - supports Sassuolo goal/Over branch;
   - Berardi bench and compressed rest cap direct extrapolation.
3. **Hot weather**
   - suppresses early press and tempo;
   - can increase late fatigue mistakes.
4. **Bologna defensive xGA**
   - supports Under and Bologna winner branch;
   - tiny two-match sample requires shrinkage.
5. **Sassuolo defensive absences**
   - supports Bologna scoring;
   - Sassuolo retain enough back-line depth to avoid treating absences as collapse.
6. **Low recent H2H**
   - supports Under;
   - coaching and striker personnel have changed, so it is low-weight context.

## 12. Frozen ranking

| Rank | Contract | UNVALIDATED_SUBJECTIVE probability | Verdict | Evidence |
|---:|---|---:|---|---|
| **1** | **Total Match Corners Over 6.5** | **61%** | **FORCED RANK** | **MEDIUM-LOW** |
| **2** | **Full Match Under 2.5 Goals** | **58%** | **LEAN direction** | **MEDIUM-LOW** |
| **3** | **1st Half Over 0.5 Goals** | **55%** | **LEAN direction** | **MEDIUM-LOW** |
| **4** | **1st Half Under 0.5 Goals** | **45%** | **FORCED RANK** | **LOW–MEDIUM-LOW** |
| **5** | **Full Match Over 2.5 Goals** | **42%** | **FORCED RANK** | **LOW–MEDIUM-LOW** |

Complementary coherence:
- 1H O0.5 55% + U0.5 45% = 100%
- FT U2.5 58% + O2.5 42% = 100%

## 13. Potential winner

### **Bologna — slight regulation-time lean**

UNVALIDATED_SUBJECTIVE 1X2:
- **Bologna 42%**
- **Draw 31%**
- **Sassuolo 27%**

Why Bologna:
- home field;
- despite 0 goals, created ≈3.03 xG in two league matches;
- conceded only ≈0.95 xG in those two;
- Sassuolo shorter turnaround;
- Sassuolo have several defensive/midfield absences;
- Bologna won the most recent H2H 1-0.

Why only slight:
- Bologna are 0-0-2 and remain without Orsolini;
- Sassuolo's current attack has created ≈4.43 xG through two;
- Berardi can materially alter the second half from the bench;
- current lineup evidence is not dual field-owner confirmed.

Representative scores:
- **Bologna 1-0 Sassuolo**
- **1-1**
- **Bologna 2-1 Sassuolo**
- Sassuolo upset branch: **0-1 / 1-2**

## 14. Settlement preregistration

- score / first-half score / 90-minute winner: official Serie A / club match record.
- corners: structured official/defined corner field where available; operator-specific action remains `UNKNOWN_DEFINITION` unless sportsbook terms are supplied.

## 15. Source register — P-329

### Google Drive
- `METHOD.md` — MDS-2026.09.06-v4.0.
- `RULES_SOCCER.md` — participant, early-goal, corner, bench and current-regime controls.
- `LEAGUE_RULES_SOCCER.md` — Serie A rules: 20 clubs, 38 matches, 5 subs, VAR, regulation draw live.
- local `PREDICTION_MINI_RUNNING_LOG_P328_UPDATED.md` — append-only handoff.

### Official / current identity and availability
- Bologna official schedule:
  https://www.bolognafc.it/en/kick-off-times-and-fixtures-up-to-matchday-5/
- Bologna official squad:
  https://www.bolognafc.it/en/squad-list-for-bologna-vs-sassuolo/
- Bologna official Orsolini condition:
  https://www.bolognafc.it/il-notiziario-di-giornata-33/
- Bologna current match centre:
  https://www.bolognafc.it/match/bologna-sassuolo-9/
- Sassuolo official current training:
  https://www.sassuolocalcio.it/prima-squadra/allenamento-mattutino-al-mfc-sabato-la-conferenza-di-fine-mercato-di-palmieri/
- Sassuolo official Torino report:
  https://www.sassuolocalcio.it/prima-squadra/serie-a-enilive-segui-il-live-di-sassuolo-torino/

### Current lineups / injuries
- Sky Sport current Bologna-Sassuolo lineup page and matchday formation page.
- FotMob current injury list cross-check.
- Oddschecker current confirmed-XI corroboration was used only for lineup cross-check, not betting content.

### Current stats / xG / corners
- xGscore Bologna-Lazio and Atalanta-Bologna exact match xG/stat records.
- xGscore Sassuolo-Torino.
- Maxifoot / current match record Atalanta-Sassuolo.
- StatMuse current Bologna and Sassuolo match logs and corner windows.
- Sky exact Sassuolo-Torino stats.

### H2H
- Bologna official Sassuolo 0-1 Bologna, Mar 15 2026.
- Bologna official Bologna 1-1 Sassuolo, Dec 28 2025.
- Sky / FBref exact Dec 2025 H2H stats.
- PlayerStats / TotalCorner used for exact historical corner sequence/count, not predictive betting content.

### Rest
- FBref / ANSA Sassuolo 1-1 Frosinone, Sep 2 2026, Coppa Italia, Sassuolo advanced on penalties.

### Weather
- exact Stadio Renato Dall'Ara structured hourly forecast.
- Met Office Bologna/Borgo Panigale.
- current independent hourly Bologna cross-check.

### Explicit exclusions
Bookmaker odds, implied probabilities, public betting percentages, market movement, tipster predictions and synthetic/AI forecasts were excluded from ranking. Any betting-oriented content accidentally present on statistical pages was ignored.

## 16. Bottom line

1. **Total Match Corners Over 6.5 — 61% UNVALIDATED_SUBJECTIVE**
2. **FT Under 2.5 Goals — 58%**
3. **1H Over 0.5 Goals — 55%**
4. **1H Under 0.5 Goals — 45%**
5. **FT Over 2.5 Goals — 42%**

Potential winner:
**Bologna — 42% regulation-time lean**.

**P-329 status:** `PREGAME — UNSETTLED`
**Population:** `EXPLORATORY — NOT SCORED`
**Retrospective:** deferred.
**Next local slot:** `P-330`.


---

# P-330 — Puerto Rico Women vs Belgium Women — FIBA Women's Basketball World Cup 2026

## Final issue disposition

| Field | Final value |
|---|---|
| Local continuation ID | `P-330` |
| Competition | FIBA Women's Basketball World Cup 2026 — Group C |
| Event | Puerto Rico Women vs Belgium Women |
| Venue | Berlin Arena / Uber Arena, Berlin, Germany |
| Verified scheduled tip | **2026-09-06 15:45 UTC / 2026-09-07 01:45 AEST** |
| Last pre-tip time handshake | **2026-09-07 01:44:58 AEST** |
| First post-tip clock | **2026-09-07 01:45:02 AEST** |
| FIBA exact-match state after tip | **No live score / quarter / game clock exposed in retrieved page** |
| Secondary live state after tip | **No trustworthy exact score + quarter + clock recovered** |
| Final state | **LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST** |
| Four ranked picks | **NOT ISSUED** |
| Potential winner | **NOT ISSUED** |
| Probability state | **NOT ISSUED** |
| Retrospective | **NOT PERFORMED — explicitly deferred** |

## Why no four-pick card was issued

The user requested a pregame card at:
- Puerto Rico +24.5
- Belgium -24.5
- Total Over 147.5
- Total Under 147.5

The current Drive method, `MDS-2026.09.06-v4.0`, requires `PREGAME` cutoff and final volatile refresh before scheduled start. `RULES_BASKETBALL.md` further requires exact phase identity and, for live work, score, quarter/clock, possession/lineup/foul state and remaining-possession recomputation.

Research was nearly complete immediately before 01:45 AEST, but the final issue boundary crossed:
- 01:44:58 AEST: still pre-tip
- 01:45:02 AEST: scheduled start crossed

The FIBA field-owner page still did not expose a current score, quarter or clock. Sofascore, Flashscore, AiScore and Scorecenter pages likewise did not provide a sufficiently trustworthy exact live state in the retrieved records.

Therefore the pre-tip ranking was withheld rather than backdated, and no live original-line probability was manufactured.

## Pregame research retained for audit only

The following was researched before/around the start and is retained only as context. It is **not an issued forecast**.

### FIBA current tournament context

Official FIBA opening-round results:
- **Australia 70-54 Puerto Rico**
- **Belgium 89-75 Türkiye**

Current official team-comparison snapshot entering this game:
- Puerto Rico: 54.0 points per game
- Belgium: 89.0 points per game
- Puerto Rico: 43 rebounds, 6 assists
- Belgium: 42 rebounds, 26 assists
- Puerto Rico shooting: 30.8% 2PT, 27.8% 3PT
- Belgium shooting: 59.1% 2PT, 34.5% 3PT

These are one-game tournament samples and were not allowed to control a large-spread forecast.

### Puerto Rico current key exposures

Official FIBA team/player pages from the Australia game:
- Arella Guirantes: 34 minutes, 14 points, 10 rebounds, 8 turnovers, 5/18 FG
- Trinity San Antonio: 11 points, primary ball-handling/creation involvement
- Imani McGee-Stafford: 11 points, 12 rebounds, 3 blocks
- Tayra Melendez: 17 efficiency and major rebounding/defensive contribution

Puerto Rico scored:
- Q1 11
- Q2 13
- Q3 14
- Q4 16
for 54 total against Australia.

### Belgium current key exposures

Official FIBA team/player pages from the Türkiye game:
- Emma Meesseman: **27 points, 9 rebounds, 5 assists, 2 blocks**
- Julie Vanloo: **22 points**
- Kyara Linskens: **11 points, 8 rebounds**
- Julie Allemand: **9 assists**, 30 minutes
- Belgium scored 89 and shot 59.1% on two-point attempts against Türkiye.

Belgium quarter scores:
- Q1 26
- Q2 18
- Q3 27
- Q4 18

### Head-to-head history

Official FIBA:
- 2022 World Cup: Puerto Rico 65-68 Belgium
- 2021 Olympics: Belgium 87-52 Puerto Rico
- 2018 World Cup: Puerto Rico 36-86 Belgium

The historical margins are extremely dispersed:
- Belgium +3
- Belgium +35
- Belgium +50

That dispersion itself is important under the large-spread controls: old blowouts cannot be copied into a current -24.5 centre without current possession/efficiency/bench separation.

### Recent broader form

Current result records around March 2026:
Puerto Rico:
- 77-61 New Zealand
- 56-47 Senegal
- 52-91 Spain
- 48-91 USA

Belgium:
- 93-50 Czechia
- 102-64 South Sudan
- 81-50 Mali
- 80-65 China
- 89-75 Türkiye at the World Cup

This shows Belgium's genuine high-margin ceiling, but the Drive large-spread rule requires factorisation of:
- possessions
- shooting-efficiency gap
- turnover/rebound conversion
- bench quality
- opening separation
- maximum lead
- closing-margin compression

Those were being built before the timing boundary crossed, but no final probability was issued.

### Total-line structure retained for audit

The user supplied **147.5**.

Current tournament opening scores:
- Puerto Rico game total: **124**
- Belgium game total: **164**

Simple midpoint = **144**, but this is not a forecast because:
- each is only one game;
- opponent quality differs;
- Belgium's favourite-dominance branch can raise both margin and total;
- Puerto Rico suppression can widen the margin while lowering the total;
- garbage time can either sustain Belgium scoring or create Puerto Rico response points.

The Drive `RULES_BASKETBALL.md` explicitly requires the total and margin to share one mismatch state tree rather than being treated as independent "safe" selections.

## Current roster / availability status

FIBA's World Cup roster tracker labels **both Belgium and Puerto Rico final rosters confirmed** for the event.

Official Puerto Rico tournament player pool includes key current names such as:
Arella Guirantes, Trinity San Antonio, Imani McGee-Stafford, Tayra Melendez, Pamela Rosado, Brianna Jones, India Pagan, Zaida Gonzalez, Jackie Benitez and Sofia Roma.

Official Belgium current tournament profile confirms active current exposure for:
Emma Meesseman, Julie Vanloo, Julie Allemand, Kyara Linskens, Antonia Delaere, Elise Ramette and Bethy Mununga among the current group.

No current official pre-tip injury release establishing a newly unavailable decision-driving player was recovered in the cutoff window.

Exact starting fives were not recovered from the FIBA field-owner page before tip. Under `BK-P2`, availability/starting-five state therefore remained incomplete for a normal pregame issue.

## Competition / rules

FIBA women's senior rules:
- four 10-minute quarters
- standard FIBA foul/bonus rules
- overtime if tied after regulation
- user did not provide sportsbook-specific regulation-vs-OT terms for spread/total

Therefore `BK-P4 = UNKNOWN_DEFINITION` would have required the overtime branch to remain explicit even if a valid card had issued.

## Source register — P-330

### Google Drive
- `METHOD.md` — MDS-2026.09.06-v4.0.
- `RULES_BASKETBALL.md` — BK-P1 through BK-P4, mismatch spread factorisation, team-score budget and live-state requirements.
- `RULES_GENERAL.md` — start-crossing / final refresh / no-hindsight boundary.
- local `PREDICTION_MINI_RUNNING_LOG_P329_UPDATED.md` — append-only handoff.

### Official FIBA identity / state / roster
- Puerto Rico vs Belgium exact-match page:
  https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128130-PUR-BEL
- World Cup roster tracker:
  https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/news/roster-tracker-fiba-womens-basketball-world-cup-2026
- Puerto Rico team profile:
  https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/puerto-rico
- Belgium team profile:
  https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/belgium
- Australia vs Puerto Rico:
  https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128129-AUS-PUR
- Belgium vs Türkiye:
  https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128128-BEL-TUR
- FIBA qualification-state article confirming Belgium advance with a win:
  current Sep 6 FIBA qualification tracker.

### Live-state reconciliation
- FIBA exact-match page remained without exact live score/quarter/clock in the retrieved state after 01:45 AEST.
- Sofascore current event page.
- Flashscore current Puerto Rico / Women's World Cup pages.
- AiScore current match page.
- Scorecenter current match page.
None supplied a sufficiently reliable exact score + quarter + clock at the issue checkpoint.

### Explicit exclusions
Bookmaker prices, implied probabilities, line movement, betting-site picks, public betting percentages, prediction markets and synthetic/AI forecasts were excluded. The user-supplied +24.5/-24.5/147.5 thresholds were used only as contract definitions.

## Bottom line

**NO ACTIONABLE P-330 FORECAST ISSUED.**

Reason:
**scheduled tip crossed before delivery + exact live score/quarter/clock could not be verified.**

**P-330 status:** `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`
**Retrospective:** deferred.
**Next local slot:** `P-331`.


---

# P-331 — Milwaukee Brewers @ Cincinnati Reds — MLB

## 1. Frozen identity / state

| Field | Frozen value |
|---|---|
| Event | Milwaukee Brewers at Cincinnati Reds |
| Venue | Great American Ball Park, Cincinnati |
| Scheduled first pitch | **2026-09-06 12:10 EDT / 2026-09-07 02:10 AEST** |
| Final research freeze used for issuance | **2026-09-07 02:06:21 AEST** |
| State | **PREGAME / WARMUP** |
| Method | **MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND** |
| Population | **MLB — PRIMARY_SCORED** |
| Probability tier | **UNVALIDATED_SUBJECTIVE** |
| Retrospective | **DEFERRED by user request** |

Supplied contracts:
- Brewers -1.5
- Reds +1.5
- Game Over 8.5
- Game Under 8.5

Standard MLB full-game interpretation:
- scheduled nine innings;
- Cincinnati has home last-bat entitlement;
- MLB extra-inning automatic runner applies if tied after nine;
- operator-specific listed-pitcher / suspension / shortened-game action terms were not supplied, so `BB-P4 = UNKNOWN_DEFINITION`.

## 2. Starter identity handshake

Official MLB probable-pitcher pages:
- **MIL LHP Kyle Harrison — PROBABLE_OFFICIAL**, 10-4, 3.45 ERA, 130 SO.
- **CIN RHP Brady Singer — PROBABLE_OFFICIAL**, 5-13, 4.83 ERA, 117 SO.

No starter-identity ambiguity at freeze.

### Harrison current regime
Last five:
- 23.1 IP
- 13 ER
- 5.01 ERA
- 29 K
- 9 HR

But the sequence is highly bimodal:
- first four of those starts: 19.2 IP, only 4 ER;
- most recent at Wrigley: 3.2 IP, 9 ER, 5 HR.

Milwaukee's own report said Harrison believed the Cubs had identified pitch tipping and planned mechanical/signalling cleanup. This is retained as an upper-tail warning, not treated as proof the issue is fixed.

### Singer current regime
Last five:
- 28.0 IP
- 17 ER
- 5.46 ERA
- 37 H
- 5 HR
- 6 BB.

Singer allowed 3+ ER in all five starts, including 4 ER/10 H in 4.1 IP last time out.

Contrary evidence:
- Singer threw **7 scoreless innings with 7 strikeouts against Milwaukee on June 22**.
This prevents treating the Brewers scoring branch as automatic.

## 3. Current batting orders

Current same-day secondary lineup service marked both orders confirmed.

### Milwaukee
1. Sal Frelick — RF — L
2. Christian Yelich — DH — L
3. Jackson Chourio — LF — R
4. Jake Bauers — 1B — L
5. Garrett Mitchell — CF — L
6. Brice Turang — 2B — L
7. Cooper Pratt — SS — R
8. Bo Naylor — C — L
9. David Hamilton — 3B — L

### Cincinnati
1. Dane Myers — CF — R
2. Elly De La Cruz — DH — S
3. Sal Stewart — 1B — R
4. Tyler Stephenson — C — R
5. Eugenio Suárez — 3B — R
6. JJ Bleday — LF — L
7. Matt McLain — SS — R
8. Juan Brito — 2B — S
9. Héctor Rodríguez — RF — L

Participant evidence caveat:
- MLB's official same-day starting-lineup web crawl still showed TBD.
- Therefore `BB-P2 = PARTIAL`, even though two current secondary sources agreed and Milwaukee's own same-day post corroborated Bo Naylor catching and Yelich batting second.
- Run-line and total evidence capped at `MEDIUM-LOW`.

Important platoon geometry:
- Milwaukee has **seven left-handed hitters** against Singer RHP.
- Cincinnati can present **six right-handed bats including switch hitters turning right-handed** against Harrison LHP.
Both starters therefore face meaningful opposite-hand exposure, increasing contact/HR-tail uncertainty.

## 4. Current offences / team regime

Milwaukee:
- **5.02 runs/game** through 143 games.
- 718 runs, third in MLB in the retrieved current table.
- recent 10-game run total: **58 runs = 5.8/game**.
- current record: **88-55**.

Cincinnati:
- approximately **4.17 runs/game** in current season snapshot.
- last 10 before/through the series roughly **4.7 runs/game** in the retrieved current window.
- current record: **68-74**.

Current series:
- Sep 4: Milwaukee **10-7** Cincinnati.
- Sep 5: Cincinnati **5-3** Milwaukee after a long weather delay.
Series is 1-1 entering the finale.

The prior two results are context only. Their useful mechanism is bullpen workload, not a "bounce back" narrative.

## 5. Bullpen / workload tree

### Milwaukee
Friday:
- Chad Patrick, Antonio Senzatela, Aaron Ashby, Trevor Megill covered relief work after Shane Drohan.

Saturday:
- Dustin May exited after 3.2 innings because of the long delay.
- DL Hall entered after the delay.
- Aaron Ashby also worked and took the loss.

Implications:
- **Ashby has worked on back-to-back days** and is downgraded for availability.
- Megill worked Friday but not Saturday in the retrieved record, so he is more plausible today.
- Abner Uribe is back from the IL.
- JoJo Romero was activated Sep 2.
- Milwaukee retains a deeper set of plausible leverage alternatives than Cincinnati.

### Cincinnati
Saturday:
- Andrew Abbott only completed 4 innings.
- Tony Santillan worked in relief and earned the win.
- Emilio Pagán worked the ninth and earned the save.

Current transaction:
- **Graham Ashcraft activated from the 60-day IL on Sep 6; Sam Moll DFA'd.**
Ashcraft supplies a fresh higher-leverage arm, but his first MLB appearance after a long UCL-sprain layoff carries role/command uncertainty.

Implication:
Cincinnati is not simply "bullpen exhausted," but its normal late-game chain is less clean because Pagán/Santillan worked late Saturday and Ashcraft is returning from a long absence.

## 6. Park / weather

Great American Ball Park:
- compact dimensions and a persistent home-run-enhancing reputation;
- current game-window weather approximately **25°C / 77°F at first pitch**, rising to 27–28°C;
- precipitation approximately **0%**;
- wind roughly **9–10 mph left-to-right**.

No rain-delay branch is central today, unlike Saturday.

Weather sign:
- warm dry air supports normal carry;
- cross-field wind is not treated as a strong one-way run adjustment;
- park geometry preserves multi-HR/cluster tails for both starters.

## 7. Joint team-run object

### Milwaukee run centre

Prior:
- Milwaukee scoring rate: **5.02**
- Cincinnati season pitching ERA context: **4.68**
- simple midpoint = **(5.02 + 4.68)/2 = 4.85**

Signed adjustments:
- Singer 4.83 season ERA / 5.46 L5 regime: **+0.20**
- seven-left-handed-batter lineup vs RHP: **+0.15**
- GABP / warm-dry environment: **+0.15**
- Bo Naylor replacing Contreras at catcher lowers batting depth somewhat: **-0.10**

**Milwaukee centre ≈ 5.25 runs**

### Cincinnati run centre

Prior:
- Cincinnati scoring rate: **4.17**
- Milwaukee season pitching ERA context: **3.50**
- midpoint = **(4.17 + 3.50)/2 = 3.84**

Signed adjustments:
- right-handed/switch-heavy order vs Harrison LHP: **+0.15**
- Harrison recent five-HR/tipping upper-tail branch: **+0.15**
- GABP / warm-dry environment: **+0.10**
- Milwaukee leverage-relief depth: **-0.15**

**Cincinnati centre ≈ 4.09 runs**

### Joint centre

**5.25 + 4.09 = 9.34 runs**

Subjective total width:
**approximately ±4.0 runs**, reflecting baseball overdispersion, HR clusters, starter hook states and extra innings.

The 8.5 threshold sits **0.84 runs below** the centre.

Final subjective:
- **Over 8.5 = 57%**
- **Under 8.5 = 43%**

## 8. Margin / run-line object

Central run separation:
**Milwaukee 5.25 - Cincinnati 4.09 = +1.16 Milwaukee**

But baseball run lines require explicit cushion decomposition.

Working eventual winner:
- Milwaukee **64%**
- Cincinnati **36%**

Within the Milwaukee-win tree:
- multi-run Milwaukee win: **44% of all game outcomes**
- exactly-one-run Milwaukee win: approximately **20%**
- Cincinnati win: approximately **36%**

Therefore:
- **Brewers -1.5 = 44%**
- **Reds +1.5 = 56%**

This is coherent with Milwaukee being the more likely winner while Cincinnati +1.5 remains the more likely run-line outcome.

Why the one-run branch is material:
- Cincinnati owns home last-bat;
- MLB extras create a high one-run-final frequency branch;
- Singer has previously held Milwaukee scoreless in this matchup;
- the Brewers have already won several close meetings in the season series.

Why Milwaukee's 2+ branch remains large:
- season-wide team-quality gap;
- Singer's current contact/run prevention;
- Milwaukee's left-handed order;
- Cincinnati's bullpen leverage uncertainty;
- Milwaukee can create a clustered middle inning, as shown Friday, though Friday's result itself is not predictive.

## 9. Mandatory upper-tail / kill-path reconciliation

### Over 8.5 routes
- Singer early hook after sustained left-handed traffic.
- Harrison's pitch-identification/HR issue is not fully resolved.
- GABP turns ordinary fly balls into HR opportunities.
- Reds right-handed cluster vs LHP.
- one starter exits before 5 innings and exposes middle relief.
- extra innings with automatic runner.

### Under 8.5 routes
- Harrison's Sep 1 collapse was mostly an isolated pitch-tipping event and the Brewers corrected it.
- Singer repeats his June pitch-shape/location success vs Milwaukee.
- Milwaukee's low-HR offensive identity fails to exploit GABP.
- fresh leverage arms such as Uribe/Romero/Megill and newly activated Ashcraft suppress the last three innings.
- 4-3 / 5-3 / 4-2 style finish without extra innings.

### Brewers -1.5 routes
- Singer allows 3–4 runs before/through the fifth.
- Harrison returns near season centre.
- Milwaukee bullpen preserves separation.
- Cincinnati's leverage chain is compromised by Saturday workload.

### Reds +1.5 routes
- Singer keeps Milwaukee below 5.
- Harrison's HR tail repeats against De La Cruz/Stewart/Stephenson/Suárez/McLain.
- home ninth/extras produce a one-run finish.
- Cincinnati wins outright.

## 10. Frozen ranking

| Rank | Contract | UNVALIDATED_SUBJECTIVE | Verdict |
|---:|---|---:|---|
| **1** | **Combined Total OVER 8.5** | **57%** | **LEAN / MEDIUM-LOW** |
| **2** | **Cincinnati Reds +1.5** | **56%** | **LEAN / MEDIUM-LOW** |
| **3** | **Milwaukee Brewers -1.5** | **44%** | **FORCED RANK / MEDIUM-LOW** |
| **4** | **Combined Total UNDER 8.5** | **43%** | **FORCED RANK / MEDIUM-LOW** |

Complement checks:
- O8.5 57% + U8.5 43% = 100%.
- MIL -1.5 44% + CIN +1.5 56% = 100%.

Rank #1 and #2 are effectively a small-gap pair, not a large confidence separation.

## 11. Potential winner

### **Milwaukee Brewers — eventual winner lean**

`UNVALIDATED_SUBJECTIVE`:
- **Milwaukee 64%**
- **Cincinnati 36%**

Reasons:
- 88-55 vs 68-74 current record.
- Milwaukee ~5.02 R/G versus Cincinnati ~4.17.
- Harrison season line (3.45 ERA/1.20 WHIP) is stronger than Singer's (4.83/1.45).
- Milwaukee's team pitching is near the top of MLB in the current table.
- Milwaukee has more credible late-game relief alternatives even with Ashby taxed.

Why not stronger:
- Harrison's latest start was a severe five-HR failure and his pitch-tipping fix is unverified in competition.
- Cincinnati's order is right-handed enough to stress a lefty.
- GABP increases homer volatility.
- Singer has already thrown seven scoreless innings against Milwaukee this season.
- Cincinnati has home last-bat.

Representative score families:
- **Milwaukee 6-4**
- **Milwaukee 5-4**
- **Milwaukee 6-3**
- Cincinnati upset tail: **5-4 / 6-4**

## 12. Settlement preregistration

- official MLB Gameday / StatsAPI controls final score and innings.
- run line and total use full-game result including extra innings unless the user's operator terms later establish otherwise.
- `OPERATOR_ACTION = UNKNOWN_DEFINITION` for listed-pitcher, suspension/shortening and other operator-specific action terms.

## 13. Source register

### Google Drive
- `METHOD.md` — active MDS-2026.09.06-v4.0; MLB `PRIMARY_SCORED`.
- `RULES_BASEBALL.md` — BB-P1 through BB-P5, starter/lineup/bullpen/park/cluster/run-line controls.
- `RULES_GENERAL.md` / active framework controls.
- local `PREDICTION_MINI_RUNNING_LOG_P330_UPDATED.md` — append-only handoff.

### Official MLB
- probable pitchers:
  https://www.mlb.com/probable-pitchers/2026-09-06
- MLB Brewers probable pitchers:
  https://www.mlb.com/brewers/roster/probable-pitchers
- Reds injuries:
  https://www.mlb.com/reds/news/reds-injuries-and-roster-moves
- Brewers injuries:
  https://www.mlb.com/amp/news/brewers-injuries-and-roster-moves.html
- Harrison Cubs/tipping report:
  https://www.mlb.com/news/kyle-harrison-allows-five-home-runs-against-cubs
- official prior-game Gameday:
  https://www.mlb.com/gameday/brewers-vs-reds/2026/09/05/824468/final

### Current lineups / performance
- RotoWire current same-day confirmed batting orders.
- Brewers same-day game discussion carrying club social post / Bo Naylor and Yelich role notes.
- StatMuse Brewers current R/G and last-10 scoring.
- StatMuse Reds current R/G and last-10 scoring.
- StatMuse Kyle Harrison last five.
- StatMuse Brady Singer last five.
- Baseball-Reference current matchup / season-series context.
- Reuters Sep 4 and Sep 5 game reports for bullpen usage and game chronology.

### Weather
- venue-specific structured Great American Ball Park hourly forecast.
- current Great American Ball Park weather cross-check.

### Explicit exclusions
Sportsbook odds, implied probabilities, market movement, consensus, tipster picks, DFS projections, synthetic/AI predictions and externally generated model picks were excluded from the sporting ranking. User-supplied -1.5/+1.5/8.5 thresholds were treated only as contract definitions.

## 14. Bottom line

1. **Over 8.5 — 57% UNVALIDATED_SUBJECTIVE**
2. **Reds +1.5 — 56%**
3. **Brewers -1.5 — 44%**
4. **Under 8.5 — 43%**

**Potential winner: Milwaukee Brewers — 64% eventual-winner lean.**

**P-331 status:** `PREGAME — UNSETTLED`
**Population:** `MLB — PRIMARY_SCORED`
**Retrospective:** deferred.
**Next local slot:** `P-332`.


---

# P-332 — Deportivo Alavés vs CA Osasuna — 2026-27 La Liga

## 1. Frozen identity / state

| Field | Frozen value |
|---|---|
| Local continuation ID | `P-332` |
| Competition | LaLiga EA Sports 2026-27, Matchday 4 |
| Event | Deportivo Alavés vs CA Osasuna |
| Venue | Mendizorroza, Vitoria-Gasteiz |
| Verified kickoff | **2026-09-06 18:30 CEST / 2026-09-07 02:30 AEST** |
| Structured game ID | `72478526` |
| Final state refresh | **2026-09-07 02:27:58 AEST** |
| State | **PREGAME / Scheduled** |
| Method | **MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND** |
| Population | **La Liga — EXPLORATORY / NOT PRIMARY_SCORED** |
| Probability tier | **UNVALIDATED_SUBJECTIVE** |
| Retrospective | **NOT PERFORMED — explicitly deferred** |

## 2. Frozen five-row slate

1. **Full Match Under 2.5 Goals**
2. **Total Match Corners Over 8.5**
3. **1st Half Over 0.5 Goals**
4. **1st Half Under 0.5 Goals**
5. **Full Match Over 2.5 Goals**

Corner target assumption:
- combined regulation-time corners, 90 minutes plus stoppage time;
- sportsbook/provider definition not supplied;
- `UNKNOWN_DEFINITION`, so the corner row is capped at `FORCED RANK / MEDIUM-LOW`.

## 3. Current participants / availability

### Osasuna

Same-day current secondary sources align on:
**Sergio Herrera; Iñigo Arguibide, Enzo Boyomo, Catena, Abel Bretones; Iker Muñoz, Jon Moncayola, Rubén García, Moi Gómez; Jonathan Dubasin, Ante Budimir.**

Current bench reported:
Aitor Fernández, Lucas Torró, Romain Del Castillo, Raúl Moro, Mauro Echegoyen, Raúl García de Haro, Kike Barja, Asier Osambela, Asier Bonel, Diego Rico, Rockson Yeboah.

Manager: **Luis Miguel Ramis**.

Official Osasuna injury/training record:
- **Aimar Oroz — left biceps femoris injury**.
- **Jorge Herrando — left adductor injury**.
- **Valentin Rosier — ongoing muscular recovery**.
All three missed the Sep 4 group session and are treated unavailable for the central branch.

New signing **Romain Del Castillo** trained with the squad and appears on the current bench list.

### Alavés

The LaLiga field-owner page did not expose the final XI in the retrieved record before freeze.
Same-day secondary sources conflict:
- AS/Cadena SER list a 5-3-2/variant with Sivera; Ángel Pérez, Tenaglia, Koski, Jonny; Antonio Blanco, Pablo Ibáñez, Denis Suárez; Abde/Aitor Mañas/Lucas Boyé in the attacking set.
- another same-day source lists Aleñá and Mariano among the starters instead.

Therefore **Alavés XI = CONFLICTING / SECONDARY_ONLY**. No player is called `CONFIRMED_OFFICIAL` from those sources.

Current same-day reporting identifies:
- **Mikel Rodríguez — ACL rupture, long-term out (6–8 months reported)**.
- **Toni Martínez — doubtful with a small soleus tear**.

Manager: **Quique Sánchez Flores**.

### Participant gate

`SO-P2 = CONFLICTING / SECONDARY_ONLY` for Alavés and `SECONDARY_ONLY` for Osasuna.
Consequences:
- side/winner confidence capped;
- full-total confidence kept at MEDIUM-LOW;
- no named-player prop issued;
- secondary lineup facts are not upgraded to official confirmation.

## 4. Current 2026-27 goal/chance process

### Alavés
Current league record:
- **3 matches: 2W-1D-0L**
- **5 GF / 1 GA**
- **4.60 xG / 2.36 xGA**
- 42 shots, 13 on target
- 17 corners, **5.67 per match**.

Results:
- Alavés 3-0 Getafe
- Rayo 1-1 Alavés
- Alavés 1-0 Villarreal

Current score environment = **2.00 total goals/match**.

### Osasuna
Current league record:
- **3 matches: 2W-1D-0L**
- **3 GF / 1 GA**
- **5.04 xG / 2.99 xGA**
- 35 shots, 14 on target
- 13 corners, **4.33 per match**.

Results:
- Osasuna 0-0 Levante
- Celta 1-2 Osasuna
- Osasuna 1-0 Getafe

Current score environment = **1.33 total goals/match**.

Both teams are tied for the fewest goals conceded in LaLiga through this snapshot: **1 each**.

## 5. L5 / L10 / long-window trend audit

### Alavés
Latest five league results by chronology:
- 1-0 Villarreal
- 1-1 Rayo
- 3-0 Getafe
- 1-2 Rayo (end 2025-26)
- 1-0 Oviedo

Approximate L5 environment:
- GF **7**, GA **3**, total **2.0/match**.

Current L10 retrieved sequence:
- GF **14**, GA **11**, total environment **2.5/match**.

### Osasuna
Latest five:
- 1-0 Getafe
- 2-1 Celta
- 0-0 Levante
- 0-1 Getafe
- 1-2 Espanyol

L5:
- GF **4**, GA **4**, total environment **1.6/match**.

Current L10 retrieved sequence:
- GF **10**, GA **13**, total environment **2.3/match**.

### L15/L20 missingness
A clean synchronized L15/L20 output for both clubs was **not recovered before cutoff**. This is recorded as `PARTIAL_WINDOW_RETRIEVAL`, rather than reconstructed from stale/non-equivalent provider snapshots. Under v4.0, that missing required-analysis layer caps the affected goal/corner rows at no higher than `MEDIUM-LOW` evidence.

Trend conclusion:
- both current and recent windows lean below the broader LaLiga scoring baseline;
- current defensive outcomes are supported by xGA, not only clean-sheet luck;
- the current samples remain only three matches and are aggressively shrunk.

## 6. Full-match goal object

Reference baselines:
- 2025-26 LaLiga: **2.69 goals/match**, 50% Over 2.5 / 50% Under 2.5.
- current Alavés match environment: **2.00**.
- current Osasuna match environment: **1.33**.
- current combined environment midpoint: **1.67**.
- current xG+xGA match-environment midpoint:
  - Alavés: (4.60 + 2.36) / 3 = **2.32**
  - Osasuna: (5.04 + 2.99) / 3 = **2.68**
  - midpoint = **2.50**.
- latest 2026 H2H: Alavés 2-2 Osasuna, but one match is low-weight context.

Explicit arithmetic:
- 40% × 2.69 = **1.076**
- 30% × 1.67 = **0.501**
- 20% × 2.50 = **0.500**
- 10% × 4.00 H2H = **0.400**

Baseline centre = **2.48 goals**.

Signed adjustments:
- both current defences have only 1 GA and sub-1.0 xGA/game: **-0.12**
- Osasuna Aimar Oroz attacking absence: **-0.07**
- Osasuna Herrando absence weakens defensive continuity: **+0.04**
- Alavés attacking availability uncertainty / Toni Martínez doubt: **-0.05**
- extreme heat/high-temperature warning: **-0.08**
- lineup conflict: **0 signed**, widen distribution

**Resulting centre ≈ 2.20 goals**
**Width ≈ ±1.20 goals**

Line location:
- 2.5 is **0.30 goals above** centre.

Final subjective:
- **Under 2.5 = 60%**
- **Over 2.5 = 40%**

Component budget:
- Alavés ≈ **1.20**
- Osasuna ≈ **1.00**
- total ≈ **2.20**.

Main Under paths:
- 1-0 / 0-0 / 1-1 / 0-1
- early tactical control under heat
- both defences preserve current chance suppression
- Osasuna create but fail to convert their xG edge efficiently.

Main Over paths:
- Budimir converts a high-value set-piece/cross chance and Alavés must chase
- Herrando absence disrupts Osasuna's back line
- Alavés' current 4.60 xG turns into multi-goal home output
- red card / penalty / early goal creates a regime switch.

## 7. First-half goal object

Baselines:
- 2025-26 LaLiga 1H Over 0.5: **70%**.
- current 2026-27 league overall snapshot: approximately **65.7–66%**.
- current team rates: Alavés approximately **1/3**, Osasuna **2/3**, combined midpoint **50%**.

Arithmetic:
- 50% × 70% = **35.0 pp**
- 25% × 65.7% = **16.4 pp**
- 25% × current team midpoint 50% = **12.5 pp**

Baseline = **63.9%**.

Signed adjustments:
- both current defences strong: **-4 pp**
- Aimar Oroz absent: **-2 pp**
- heat / possible lower early press intensity: **-2 pp**
- Budimir/Alavés direct-striker threat preserves early-goal tail: **+1 pp**

Final:
- **1H Over 0.5 = 57%**
- **1H Under 0.5 = 43%**

Width ≈ ±10 pp.

The Over stays slightly ahead because the league prior remains high, but it is much weaker than a generic LaLiga early-goal pick after reconciling the teams' current defensive regimes.

## 8. Corner process — Total Over 8.5

Current own-corner rates:
- Alavés: **5.67/match**
- Osasuna: **4.33/match**
- combined expected own production = **10.00**.

2025-26 LaLiga:
- approximately **9.7 corners/match**.
- Over 9.5 approximately 48.2%, implying 8.5 sits below the historical median-ish environment.

Current exact team corner sequences:
- Alavés: **5, 7, 5**
- Osasuna: **9, 3, 1**

Latest 2026 H2H:
- Alavés **7** corners, Osasuna **1** = **8 total**.

Corner centre arithmetic:
- 45% × league prior 9.7 = **4.37**
- 40% × current combined own rate 10.0 = **4.00**
- 15% × H2H 8.0 = **1.20**

Baseline = **9.57 corners**.

Adjustments:
- high heat may reduce repeated press/cross volume: **-0.20**
- score-state chasing branch can restore late corners: **+0.10**

**Centre ≈ 9.47 corners**
**Width ≈ ±3.2 corners**

Final:
- **Total Corners Over 8.5 = 59% UNVALIDATED_SUBJECTIVE**.

Mechanism:
- Alavés are producing corners even with low possession (24.1% vs Villarreal yet 5 corners), so the process is not a simple possession proxy.
- Osasuna's current corner allocation is volatile (9,3,1), so combined total is preferred over an Osasuna team-corner line.
- if either side trails, width/direct-cross volume can lift late corner exposure.

Provider caveat:
`UNKNOWN_DEFINITION`; therefore this row remains `FORCED RANK / MEDIUM-LOW` despite ranking #2.

## 9. Weather / environment gate

Venue-specific structured forecast for Mendizorroza:
- around **29°C** during the match window, falling toward 27°C later;
- current structured condition briefly showed light rain around the pre-match observation;
- hourly forecast then trends mostly sunny/dry;
- **AEMET yellow warning for extreme high temperature** in Llanada Alavesa, with maximum temperature warning up to ~36°C.

Mechanisms:
- heat can suppress repeated pressing and early tempo;
- heat also creates late fatigue/error tails;
- light pre-match rain can slightly change surface speed but there is no central persistent-rain branch.

Net goal adjustment: **-0.08 goals**.
No automatic corner sign beyond slightly lower early pressing.

## 10. Rest / congestion

Alavés last league match: Aug 28 vs Villarreal — about 9 days rest.
Osasuna last league match: Aug 31 vs Getafe — about 6 days rest.

This is a modest Alavés recovery advantage.
No European midweek congestion applies.

Net side effect: small Alavés positive branch; no large coefficient.

## 11. Bidirectional-sign audit

1. **Both teams' one-goal-conceded start**
   - supports Under;
   - early-season clean sheets are unstable, so xGA is used to check mechanism.
2. **Osasuna xG > goals**
   - supports future scoring upside;
   - finishing shortfall is not guaranteed to regress in one match.
3. **Aimar Oroz absence**
   - suppresses Osasuna creativity;
   - Del Castillo/Raúl provide replacement attacking pathways.
4. **Herrando absence**
   - weakens Osasuna defensive continuity;
   - Boyomo/Catena remain a credible central pairing.
5. **Heat**
   - can lower tempo;
   - can create late defensive fatigue and mistakes.
6. **Alavés low possession vs Villarreal**
   - does not imply low corner exposure: they still won 5 corners.
7. **Latest H2H was 2-2**
   - supports the Over tail;
   - it is one prior match and current managers/participants differ, so it does not own the present total.

## 12. Frozen ranking

| Rank | Contract | UNVALIDATED_SUBJECTIVE | Verdict | Evidence |
|---:|---|---:|---|---|
| **1** | **Full Match Under 2.5 Goals** | **60%** | **LEAN** | **MEDIUM-LOW** |
| **2** | **Total Match Corners Over 8.5** | **59%** | **FORCED RANK** | **MEDIUM-LOW** |
| **3** | **1st Half Over 0.5 Goals** | **57%** | **LEAN direction** | **MEDIUM-LOW** |
| **4** | **1st Half Under 0.5 Goals** | **43%** | **FORCED RANK** | **LOW–MEDIUM-LOW** |
| **5** | **Full Match Over 2.5 Goals** | **40%** | **FORCED RANK** | **LOW–MEDIUM-LOW** |

Complement coherence:
- FT U2.5 60% + O2.5 40% = 100%
- 1H O0.5 57% + U0.5 43% = 100%

Rank gaps:
- #1 → #2: **tiny**
- #2 → #3: **small**
- #3 → #4: **moderate**
- #4 → #5: **small**

## 13. Potential winner

### **Deportivo Alavés — slight regulation-time lean**

`UNVALIDATED_SUBJECTIVE` 1X2:
- **Alavés 41%**
- **Draw 34%**
- **Osasuna 25%**

Why Alavés:
- home field;
- 5 GF / 1 GA vs Osasuna 3 / 1;
- 4.60 xG / 2.36 xGA is a strong current two-way profile;
- longer rest;
- Osasuna missing Aimar Oroz, Herrando and Rosier.

Why only slight:
- both teams have 7 points and are unbeaten;
- Osasuna's current xG (5.04) is actually slightly higher;
- Budimir remains a high-value finishing/set-piece threat;
- Alavés exact XI is source-conflicted;
- Alavés have their own injuries/uncertainties.

Representative score families:
- **Alavés 1-0**
- **1-1**
- **0-0**
- **Osasuna 0-1**
- upper-tail branch: **2-1 / 1-2**.

## 14. Settlement preregistration

- score / half-time score / regulation winner: official LaLiga match record.
- corners: official/structured defined field where available; `OPERATOR_ACTION = UNKNOWN_DEFINITION` unless sportsbook terms are later supplied.

## 15. Source register

### Google Drive
- `METHOD.md` — active MDS-2026.09.06-v4.0.
- `RULES_GENERAL.md` — start-crossing, participant identity, bench, environment, arithmetic and source hierarchy.
- `RULES_SOCCER.md` — SO-P1/SO-P2/SO-P3, goal/corner separation, early-goal reconciliation and participant controls.
- `LEAGUE_RULES_SOCCER.md` — LaLiga 20-club/38-match format, 5 subs, VAR/SAOT, 90-minute regulation draw live.
- local `PREDICTION_MINI_RUNNING_LOG_P331_UPDATED.md` — immediate append-only handoff.

### Identity / state
- LaLiga official match page and team schedules.
- structured soccer event `72478526`, final refresh 02:27:58 AEST: Scheduled.

### Participants / injuries
- Osasuna official Sep 1, Sep 3 and Sep 4 training releases.
- AS/Cadena SER same-day lineup records.
- same-day Alavés preview reporting for Mikel Rodríguez / Toni Martínez.
- current secondary-source Alavés lineup conflict preserved explicitly.

### Current process / stats
- StatMuse 2026-27 Alavés aggregate: 5 GF, 1 GA, 4.60 xG, 2.36 xGA, 17 corners.
- StatMuse 2026-27 Osasuna aggregate: 3 GF, 1 GA, 5.04 xG, 2.99 xGA, 13 corners.
- StatMuse current exact-match corner/xG sequences.
- StatMuse current L5/L10 match records.
- 2025-26 LaLiga baseline: 2.69 goals/match, 50% O2.5, ~9.7 corners/match, ~70% 1H O0.5.
- 2026-27 league first-half O0.5 snapshot ~65.7–66%.

### Weather
- venue-specific structured Mendizorroza hourly forecast.
- AEMET severe-weather feed carried in structured forecast: yellow high-temperature warning for Llanada Alavesa.

### Explicit exclusions
Bookmaker odds, market-implied probabilities, line movement, public betting, tipster picks and synthetic/AI prediction pages were excluded. Betting-site content was not used for ranking; one same-day lineup page was used only to identify and preserve a participant-source conflict.

## 16. Bottom line

1. **FT Under 2.5 — 60% UNVALIDATED_SUBJECTIVE**
2. **Total Corners Over 8.5 — 59%**
3. **1H Over 0.5 — 57%**
4. **1H Under 0.5 — 43%**
5. **FT Over 2.5 — 40%**

**Potential winner: Deportivo Alavés — 41% regulation-time lean.**

**P-332 status:** `PREGAME — UNSETTLED`
**Population:** `EXPLORATORY — NOT SCORED`
**Retrospective:** deferred.
**Next local slot:** `P-333`.
