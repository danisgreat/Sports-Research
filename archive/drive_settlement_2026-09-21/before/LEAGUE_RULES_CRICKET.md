# Cricket — sport and competition rules reference

Status: **ACTIVE — reference**
Created: **2026-09-04**
Companion to: **[RULES_CRICKET.md](RULES_CRICKET.md) §11**. Reference only; it does not change `SFA-CRICKET` or any gate. It documents the laws of cricket, the format-level playing conditions, and the competition-specific rules for every cricket competition that appears in the prediction logs.

Rules-era caveat: the playing conditions below are those in force for the **2025–2026** seasons the current log covers (ICC men's playing conditions effective July 2025; ICC Women's Championship 2025–2029; The Hundred 2026; CPL 2026; ETPL 2026 inaugural). Cricket changes its playing conditions almost every year — verify the era for any event outside this window.

**Maintenance (RULES_GENERAL.md §3, `G2`).** Last reviewed **2026-09-04**. Before the first card of a new season / edition of any competition here — or the first appearance of a cricket competition after a break of ~6 weeks or more — re-verify the ICC playing conditions and the competition's own playing regulations against the field owner (ICC, the league operator) for changes to powerplay/bowler limits, DRS, DLS minima, the Super Over rule, the points/NRR system, squad rules, or the knockout format, and update the relevant section below **before** issuing the card. The first time a new cricket competition is forecast, add its full playing conditions and format here first. Watch especially for: a franchise-league deviation from ICC conditions (e.g. the IPL's two-bouncers-per-over and Impact Player rules, which are IPL-only and not guaranteed to persist), a format switch (The Hundred's investors have floated a move to franchise T20), and expansion/contraction of a league's team count.

---

## 1. The laws of cricket (all formats)

**Objective.** Two teams of eleven. One team bats (tries to score **runs**) while the other bowls and fields (tries to take **wickets** and restrict runs). The team that scores more runs, under the match's format rules, wins.

**The field.** An oval grass ground. In the centre is the **pitch**: 22 yards (20.12 m) between the two sets of **stumps** (three wooden stumps + two bails per end). A **30-yard (27.4 m) circle** is marked around the pitch for fielding-restriction purposes. The **boundary** is the edge of the field — ball over it on the full = **6 runs**, along the ground or bouncing = **4 runs**.

**An over.** Six legal deliveries bowled from one end by one bowler (five in The Hundred — see §4). After an over the bowling switches to the other end and a different bowler; a bowler may not bowl two overs in succession. Ends alternate; the batters do not swap ends between overs (they swap by running odd numbers of runs, or at the end of an over the striker/non-striker roles swap because the bowling end changed).

**Scoring runs.** The two batters at the crease run between the wickets — each completed length = 1 run. Plus boundaries (4/6). Plus **extras**: **wide** (1 run + re-bowled, ball passes out of the batter's reach), **no-ball** (1 run + re-bowled + **free hit** next ball in white-ball cricket, for overstepping / illegal delivery / dangerous ball), **bye** (ball passes the batter and keeper), **leg-bye** (ball hits the batter's body, not bat, and they run).

**Getting out (dismissals).** **Bowled** (ball hits stumps), **caught** (fielder catches it on the full), **leg before wicket / LBW** (ball would have hit the stumps but for the batter's pad, subject to the LBW law — pitching line, impact line, wickets-in-line), **run out** (stumps broken while a batter is out of the crease during a run), **stumped** (keeper breaks the stumps with the batter out of the crease and not attempting a run), **hit wicket**, **handled the ball / obstructing the field / hit the ball twice / timed out** (rare). When 10 of the 11 batters are out, the innings is **all out** (the 11th has no partner).

**The toss.** Before the match a coin is tossed; the winning captain chooses to **bat** or **bowl** first. In conditions terms this is one of the largest single levers in the sport (RULES_CRICKET.md §2).

**DRS (Decision Review System).** Where available, each side may **review** an on-field umpire's out/not-out decision to the third umpire (ball-tracking, UltraEdge/Snicko, replays). **Umpire's call** on marginal LBW ball-tracking keeps the on-field decision and the reviewing side keeps its review. Review allowance: **two unsuccessful reviews per team per innings** in T20Is and ODIs (Tests also two, topped back up after 80 overs in some eras); franchise leagues set their own (usually one or two).

**Powerplay / fielding restrictions (base concept).** For a defined early portion of each innings only **two** fielders are allowed outside the 30-yard circle; outside the powerplay the limit is **five** outside the circle (and never more than five on the leg side, and at delivery no more than two behind square on the leg side). The exact powerplay length is format-specific (§2–§4).

**Weather and DLS.** Rain/bad light stops play. If overs are lost, the target is recalculated by the **Duckworth–Lewis–Stern (DLS)** method, which accounts for overs and wickets remaining as "resources." A minimum number of overs must be bowled to the side batting second for a result (T20: **5 overs** each side unless further reduced by playing conditions; ODI: **20 overs**). Below that minimum the match is **no result** / abandoned. The team batting second chases a **par score + 1**; being level with the par score at a stoppage is a **tie**.

**Super Over (tie-breaker).** Where a match must produce a winner and the scores are level, each side bats **one over** (six balls, maximum **two wickets**). Higher score wins. If the Super Over is also tied, **further Super Overs are played until there is a winner** (the old boundary-count tie-break was abolished in 2019). Bowlers and batters used in one Super Over have restrictions on reuse in the next.

**Over-rate / stop clock (white-ball, in force 2024–2026).**
- **Stop clock:** the fielding side must be ready to bowl the first ball of the next over within **60 seconds** of the previous over ending. Two warnings per innings; the **third and each subsequent breach = 5 penalty runs** to the batting side.
- **In-match over-rate penalty:** if the fielding side is not in position to bowl the first ball of the **final over** by the scheduled cutoff time, **one fewer fielder is allowed outside the 30-yard circle** for the rest of the innings.

**Other current playing-condition points (ICC, effective July 2025).**
- **Wide judgement** now references the batter's leg position **at the moment of delivery**, so a batter who moves across cannot manufacture a wide by the movement alone (leg-side wides are still strict in white-ball cricket).
- **One bouncer (above shoulder height) per over** in ICC T20Is; **two per over** in ODIs. (The IPL uses two per over — a franchise-league deviation; do not assume it elsewhere.)
- **Serious-injury replacement:** from October 2025, on trial, a player who suffers a serious on-field injury after the match starts may be replaced by a **like-for-like fully participating** substitute (a widening of the older concussion-substitute rule).
- **Boundary catches:** a fielder must be **entirely within the boundary** (or their last contact with the ground was inside) when they touch the ball; airborne fielders taking a ball beyond the boundary get one touch and must land inside.

---

## 2. Format playing conditions — Test and ODI (base reference; not directly forecast in the log so far)

### 2.1 Test cricket
- **Two innings per side**, up to **5 days**, minimum **90 overs per day**. No fixed innings length — an innings ends when the side is all out, declares, or (rarely) time runs out.
- **New ball** available after 80 overs. **Follow-on:** the side batting first, if 200+ runs ahead after the first innings, may ask the opponent to bat again immediately.
- **Result:** win (opponent's second innings dismissed/target chased), **draw** (time expires with the match unfinished), or **tie** (extremely rare — scores level with the last team all out). **No DLS** in Tests — lost time simply makes a draw more likely.
- **World Test Championship (2025–2027):** a points percentage table (12 points per win, 4 per draw, of a possible 12 per match), with in-match over-rate and slow-over penalties; top two contest a one-off final.
- Settlement: the **draw is a first-class outcome** and must be an explicit branch for any Test winner market.

### 2.2 One Day International (ODI) / List A
- **50 overs per side**, one innings each. Bowler maximum **10 overs**.
- **Powerplays:** overs 1–10 = two fielders out (P1); overs 11–40 = four out (P2); overs 41–50 = five out (P3).
- **Two new balls** (one from each end) in ODIs for the first ~34 overs, then one chosen ball for the death — the exact rule has changed repeatedly; the 2025 update moved to one ball from over 35.
- **DRS:** two unsuccessful reviews per team per innings.
- **DLS** applies; minimum **20 overs** to the side batting second for a result.
- **Result:** win or tie; no draw. **Super Over** in knockouts, bilateral series usually record a tie.

---

## 3. Format playing conditions — Twenty20 (T20 / T20I)

This is the base format for the CPL, the ETPL, and the bilateral / tri-series T20Is in the log (Namibia T20I Tri-Series; Pakistan Women's T20Is).

- **20 overs per side**, one innings each. **Bowler maximum 4 overs** (in a full match; pro-rated down in a reduced match, normally to no more than 1/5 of the innings + rounding).
- **Powerplay:** overs **1–6** — only **two** fielders outside the 30-yard circle. Overs 7–20 — **five** outside the circle.
- **Free hit** for any no-ball (front-foot, back-foot, height, more-than-permitted-bouncer): the next ball, the striker can only be out run-out / handled / obstructing, and the field may not change unless the batters cross.
- **DRS** (where deployed): **two** unsuccessful reviews per team per innings.
- **DLS:** minimum **5 overs** each side for a result (unless playing conditions reduce further, e.g. some leagues use a 10-over minimum in knockouts). Par score at every ball is published.
- **Interval / strategic timeout:** ICC T20Is have an optional drinks break; most **franchise leagues have a compulsory 2½-minute strategic timeout in each innings** (see per-league notes).
- **Stop clock + over-rate fielder penalty** as in §1.
- **Result:** win, tie (→ Super Over in almost all T20 leagues and knockouts), or no result. **A tied league match is usually one point each; a tied knockout goes to a Super Over.**
- **Points (standard T20 league):** win **2**, tie/no-result **1**, loss **0**. Standings ordered by points, then **net run rate (NRR)** = (runs scored ÷ overs faced) − (runs conceded ÷ overs bowled) across the tournament; a side bowled out is treated as having faced its full quota of overs for NRR.

---

## 4. The Hundred (Men's and Women's Competition)

**Governing body:** ECB. **Teams:** 8 city franchises (7 England, 1 Wales), each fielding a men's and a women's side; matches are played as **men's + women's double-headers at the same venue**. **2026:** the 100-ball format is **retained**; franchise part-ownership stakes were sold to private investors in 2025 and several teams were rebranded (e.g. Oval Invincibles → **MI London**, Northern Superchargers → **Sunrisers Leeds**). New investors have floated converting the event to franchise T20, but not before 2028.

### 4.1 Playing conditions (the 100-ball format)
- **100 balls per innings.** Whoever scores more runs wins. Target match length ~2h30, two 65-minute innings + 15-minute interval.
- **"Overs" are 5 balls.** The bowling captain may have a bowler deliver **5 or 10 consecutive balls** (i.e. one or two 5-ball sets back-to-back).
- **Change of ends every 10 balls** (not every 5).
- **Bowler maximum: 20 balls per match** (four 5-ball sets), of which no more than **10 in a row**.
- **Powerplay: 25 balls** at the start of each innings — only **two** fielders outside the 30-yard circle. After ball 25, **five** outside the circle.
- **No-ball: 2-run penalty** (not 1) + **free hit**.
- **One strategic timeout** per bowling side, up to 90 seconds, not during the powerplay.
- **New-batter rule:** the incoming batter must be ready to face within 60 seconds; a warning, then **5 penalty runs** for repeat delays.
- **DRS** is used in televised matches (limited reviews per side).
- **DLS** applies for weather; a minimum number of balls (the equivalent of 5 five-ball overs, i.e. 25 balls) must be bowled to the chasing side for a result.

### 4.2 Competition format
- **Group stage:** each team plays 8 matches (4 home, 4 away) — a partial round-robin. Points: **win 4, tie 2, no-result/weather-abandoned 2 each, loss 0**. Ranking by points, then **net run rate** (computed per ball for the 100-ball format).
- **Knockout:** top **3** teams advance. **Eliminator:** 2nd v 3rd. **Final:** Eliminator winner v 1st. (Historically played across two "Finals Day" fixtures / Lord's finals — confirm the year's exact structure.)
- Men's and women's competitions run in parallel with the same format.

### 4.3 Settlement notes
- Innings are measured in **balls**, not overs — "first-innings total", "team X runs", "over/under" lines are set against a **100-ball** innings, and any recency comparison to T20 data must adjust for the ~20-ball shorter innings and 5-ball powerplay-overs difference (RULES_CRICKET.md §10.8).
- A weather-abandoned match is **2 points each** and settles most match markets as **no result / void**, not as a loss for the higher-ranked side.

---

## 5. Caribbean Premier League (CPL) — "Republic Bank CPL"

**Governing body:** Cricket West Indies / CPL. **Format:** Twenty20. **2026 season:** 7 August – 20 September, **7 teams**, **39 matches**, final in Barbados. The Jamaica franchise returned for 2026, expanding the league from 6 to 7.

**2026 teams:** Antigua & Barbuda Falcons, Barbados Tridents, Guyana Amazon Warriors, a returning Jamaica franchise, Saint Lucia Kings, St Kitts & Nevis Patriots, Trinbago Knight Riders. **Venues:** Sir Vivian Richards Stadium (Antigua), Kensington Oval (Barbados), Providence Stadium (Guyana), Sabina Park (Jamaica), Warner Park (St Kitts), Daren Sammy Cricket Ground (St Lucia), Arnos Vale (St Vincent), Queen's Park Oval (Trinidad).

**Squad and selection rules (2026):** 17-player squads = **9 West Indian + 5 overseas + 3 "breakout" (developmental West Indian) players**. In the XI: **maximum 4 overseas players**, and **at least 1 breakout player is mandatory** in every match XI.

**Scheduling quirk:** teams play their home fixtures in a concentrated **"home week"**, often with two venues hosting on the same day. This compresses travel and rest patterns unusually — the venue/travel block in a CPL card behaves differently from other T20 leagues (RULES_CRICKET.md §10.9).

**Playing conditions:** standard ICC-derived T20 conditions — 6-over powerplay, 4-over bowler cap, free hit for no-balls, compulsory strategic timeout each innings, DRS, DLS (5-over minimum for a result), **Super Over** for a tie in any match. Caribbean pitches are typically **slow, low and spin-friendly**, and dew can be a major second-innings factor at day-night venues — this is a heavy toss/chasing consideration.

**Points and playoffs:** win 2 / tie or no-result 1 / loss 0, ranked by points then NRR. **Top 4** qualify. Playoff bracket: **Qualifier 1** (1st v 2nd — winner to the Final), **Eliminator** (3rd v 4th — loser out), **Qualifier 2** (Qualifier 1 loser v Eliminator winner — winner to the Final), **Final**. All playoff games at a single host venue.

---

## 6. European T20 Premier League (ETPL) — inaugural 2026

**Governing body:** a private venture (ICC-sanctioned), run across the European Cricket pathway. **2026 is the inaugural edition** — 26 August – 20 September, played in Ireland, Northern Ireland, the Netherlands and Scotland.

**Teams:** **6 franchises** — two each from **Ireland, Scotland and the Netherlands**. (Log example: Belfast Wolves, Edinburgh Castle Rockers.)

**Squad and selection rules:** 17-player squads with **at least 8 local players**, **5–7 overseas players**, and **at least one European Associate** and **one Global Associate** player per squad. In the XI: **at least 5 local players** and a **maximum of 4 overseas players**.

**Format:** **double round-robin** — each franchise plays every other twice (10 group games each) — then a knockout: the **table-topper goes straight to the Final**, and **2nd v 3rd** play a **Qualifier** for the other Final place.

**Playing conditions:** standard ICC T20 playing conditions (6-over powerplay, 4-over bowler cap, free hit, DRS where broadcast, DLS 5-over minimum, Super Over for ties). Points: win 2 / tie or no-result 1 / loss 0, then NRR.

**Analytical caution (inaugural league):** there is **no venue-and-format history and no team history** for this competition (RULES_CRICKET.md control 17, sparse-competition hierarchical shrinkage). Player form must be imported from other competitions with heavy shrinkage; Irish, Scottish and Dutch late-August weather makes **reduced-over and no-result outcomes materially more likely** than in a Caribbean or subcontinental T20 league.

---

## 7. Bilateral and tri-series T20Is and ODIs

Covers: **Namibia T20I Tri-Series 2026** (men's T20Is), **Pakistan Women tour of Sri Lanka** (women's T20Is), **Ireland Women tour of England** (women's ODIs, part of the ICC Women's Championship).

### 7.1 T20Is (bilateral / tri-series)
- Full ICC **T20I playing conditions** as in §3 (6-over powerplay, 4-over cap, one bouncer/over, free hit, stop clock, DRS where deployed, DLS 5-over minimum, Super Over in a final).
- **Tri-series:** a short round-robin (each team plays the others once or twice) then a **final** between the top two. League ties → 1 point each; the **final** goes to a Super Over.
- **Associate / lower-profile fixtures** (Namibia and its opponents) may have **no DRS**, less reliable ball-tracking, uncovered-pitch or drop-in-pitch variability, and thin venue history — widen conditions and participant uncertainty accordingly.

### 7.2 Women's ODIs and the ICC Women's Championship (2025–2029)
- **50-over ODI** playing conditions (§2.2): 10-over P1 (2 out), overs 11–40 (4 out), 41–50 (5 out); bowler max 10 overs; two new balls; DRS two reviews/team/innings; DLS 20-over minimum.
- **ICC Women's Championship 2025–2029:** **11 teams** (India, South Africa, Australia, England, Sri Lanka, New Zealand, Bangladesh, Pakistan, West Indies, Ireland, Zimbabwe). Each team plays **8 three-match series** (4 home, 4 away) — **132 ODIs** total over the cycle. **2 points per ODI win, 1 for a tie/no-result.** The table decides direct qualification for the **2029 Women's World Cup** (the rest go to a qualifier).
- Settlement: each match is a standalone ODI (win/tie/no-result); the **series** and the **Championship table** are separate propositions. A women's ODI between a top side and Ireland/Zimbabwe has a **wide expected-margin distribution** and a real mismatch/rain-shortened tail.

---

## 8. Cross-competition quick reference

| Competition | Format | Innings unit | Powerplay | Bowler cap | Tie rule | Knockout |
|---|---|---|---|---|---|---|
| Test / WTC | 2 inns/side, 5 days | overs (no cap) | new ball @80 | none | draw or tie | WTC final (1 match) |
| ODI / Women's Championship | 50 overs | 50 overs | 10 / 11–40 / 41–50 | 10 overs | tie (SO in knockouts) | World Cup qualification table |
| T20I bilateral/tri-series | 20 overs | 20 overs | overs 1–6 | 4 overs | SO in finals, 1 pt each in league | tri-series final |
| The Hundred | 100 balls | 100 balls | 25 balls | **20 balls** | 2 pts each; SO in knockouts | top 3 → Eliminator → Final |
| CPL | 20 overs | 20 overs | overs 1–6 | 4 overs | Super Over | top 4 → Q1/Elim/Q2/Final |
| ETPL (2026) | 20 overs | 20 overs | overs 1–6 | 4 overs | Super Over | 1st → Final; 2nd v 3rd → Qualifier |

**Always resolve, per RULES_CRICKET.md §1:** the exact competition and season, the innings unit (overs vs balls), the powerplay and bowler limits, the DRS availability, the DLS minimum and current par, the Super Over / tie rule, the points and NRR rules, and the knockout bracket — before any rate or contract work. For weather-exposed fixtures also resolve the **minimum-overs-for-a-result** and the operator's **no-result / void** settlement.

## September 5 ETPL observed-match rules clarification

The official ETPL-linked NV Play record for [Match 13](https://www.etplofficial.com/nvplay-embed?customerId=1A9E0000-8D41-7CED-D487-08DEF280CD56&innings=2&matchId=ac4fe6d2-e979-49db-9803-83495a8a047f&theme=light&widget=match-centre) records a match reduced **before play to 12 overs**, a **four-over regulatory powerplay**, Belfast 40/1 at that boundary, 54/2 at six and 146/3 at twelve. The user's six-over contract is therefore distinct from this match’s powerplay. Glasgow won the toss and bowled. The scorer labels the ground Sportpark Westvliet, Den Haag; preserve that owner label alongside the original card’s Voorburg/Duivesteijn label rather than assuming aliases from name alone.

This is an exact-match observation, not a reconstructed universal ETPL reduced-over table. Verify the current competition conditions when another innings length is encountered. By Match 13 some inaugural-season match history exists; “no history” must mean no prior-season history, not zero current observations. Keep unique current-match denominators and condition on format/innings order rather than fabricating long windows or transferring 20-over averages unchanged to shortened innings.

## ETPL powerplay definition and settlement hazards — confirmed 2026-09-06

Added because ETPL phase contracts are now settleable and therefore need an exact, sourced definition rather than an assumed one.

**Standard mandatory powerplay:** `Overs 0.1 – 6.0`, recorded on the official scorecard as `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - N runs, W wickets)`. Confirmed for ETPL 2026 matches 9 through 15 from the structured scorecard note (`SRC-ESPN-SITE-API-CRICKET`).

**Settlement hazard — the powerplay shortens with the innings.** In a rain-reduced ETPL match the mandatory powerplay is scaled down with the overs, and the scorecard note records the *actual* range. Two observed cases in this competition:

| Match | Powerplay range recorded | Innings length |
|---|---|---|
| Amsterdam Flames v Belfast Wolves (M8) | `Overs 0.1 - 1.3` | 5 overs per side |
| Glasgow Cosmic v Belfast Wolves (M13) | `Overs 0.1 - 3.4` | 12 overs per side |

A "powerplay Over/Under" contract frozen against an assumed six-over phase and settled against a 1.3-over or 3.4-over phase is a `GATE-CONTRACT` failure, not a close call. **Always read the actual powerplay range from the scorecard note before settling**, and where the toss is unpublished at freeze, state the phase length assumption alongside the batting-order condition.

**Observed ETPL 2026 full six-over powerplay population** (the descriptive `REFERENCE_BASE_RATE` for phase contracts in this competition, ESPN's official 8th–12th Matches): 28, 39, 49, 50, 51, 55, 56, 61, 68, 72 — median 53, mean 52.9. **Corrected 2026-09-06(d):** the population was originally mislabelled "matches 9-13"; the fixtures are officially the 8th through 12th Matches (verified against ESPN's `description` field). The actual 13th Match (Glasgow Cosmic v Belfast Wolves, reduced to 12 overs) is a different fixture from the one previously labelled M13 here, and is correctly excluded from a full-six-over population since its own powerplay was reduced. This population also does not yet reconcile three earlier same-competition cards (`P-099`, `P-115`, `P-171`) that ESPN's series ID does not appear to carry — treat this table as the confirmed 8th-12th-Match population only, not the tournament's complete history, until that gap is closed.

## 2026-09-06(f) — settlement and retrospective addendum

P-217 settlement clarification: the actual officially completed revised innings was 16 overs, GAW 185/5. The fixed 20-over target is preserved; research Over/Under grades use that revised completed-innings convention explicitly, with no extrapolated 20-over score and OPERATOR_ACTION UNKNOWN_DEFINITION. ESPN reports the mandatory PP ending at 4.5 (24/2), which must not replace the frozen six-completed-over target. P-305/P-311 batting-first conditions were met by the actual toss. [Details](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). No competition playing law or operator rule has been invented/changed.


## Exact exposure and retrospective correction - 2026-09-12

Keep P-364's completed innings/45-over targets separate from its still-live Test winner. P-366's fixed-20-over targets remain terminal censored after the actual 19-over match; P-217's inherited revised-16-over research convention does not automatically govern a different frozen contract. P-262's official CPL phase record is Falcons 43/1 at six and 183/4 at 20, illustrating resources and phase dependence, not a new competition law. No new ICC/league playing-condition change was established in this pass. See RULES_CRICKET and the recovered historical retrospective.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — source firewall precedence

All league-specific source instructions are subordinate to `SOURCES.md` PF-1/PF-2. Official board/competition sources and admitted ball-level historical sources outrank derivative previews. Sportsbook/betting/fantasy/DFS material and market-derived projections are never predictive evidence; if an older league note suggests otherwise, this section controls.

