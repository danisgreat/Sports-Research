# Soccer — sport and competition rules reference

Status: **ACTIVE — reference**
Created: **2026-09-04**
Companion to: **[RULES_SOCCER.md](RULES_SOCCER.md) §9**. Reference only; it does not change `SFA-SOCCER` or any gate. It documents the IFAB Laws of the Game, the competition variables that decide settlement, and the specific rules of every soccer competition in the prediction logs.

Rules-era caveat: formats below are those in force for the **2025–2026 / 2026 / 2026-27** seasons the current log covers. Domestic formats (split systems, playoff qualifier counts, foreign-player quotas, relegation on/off) change frequently — **verify the season** for any event, especially for the Belgian, Danish, Egyptian, Argentine, Mexican, Chinese and Kazakh competitions, which have all changed format recently.

**Maintenance (RULES_GENERAL.md §3, `G2`).** Last reviewed **2026-09-04**. Before the first card of a new season / new edition of any competition here — or the first appearance of a competition after a break of ~6 weeks or more (most European leagues run Aug–May, so the August restart is a hard checkpoint; Brazil, China, Argentina, the Nordic and MLS-adjacent competitions run on other calendars) — re-verify against the field owner: the IFAB Laws currently in force (a new edition applies from 1 July each year), the competition's format (team count, split-system adoption, playoff/liguilla qualifier count, promotion/relegation on or off, points/tiebreak order), substitution and VAR adoption, foreign-player quotas, and any points deductions — then update the section below **before** issuing the card. The first time a new soccer competition is forecast, document its full rules here first. Recent examples of why this matters: the away-goals rule was abolished (2021); the 5-substitutions and goalkeeper-8-second rules were added; the UEFA competitions moved to the 36/18-team "league phase"; Liga MX abolished its play-in round from Apertura 2026; the Belgian, Danish and Egyptian leagues changed their split formats; China revised its foreign-player rule for 2026.

---

## 1. The IFAB Laws of the Game (universal)

**Objective.** Two teams of **11** (including a goalkeeper). Score by putting the whole ball over the opponent's goal line between the posts and under the bar. Most goals wins; many competitions allow a draw, others force a winner (§2).

**Duration.** Two **45-minute** halves + **"additional time"** (stoppage time) added by the referee for stoppages. Since 2022–2026 referees add time far more generously (often 5–10+ minutes) — this materially raises late-goal and total exposure versus pre-2022 data. Half-time ≤15 minutes. A "cooling break" (~3 min) may be taken mid-half in hot conditions.

**Restarts.** Kick-off (start of each half and after a goal), throw-in (ball out on the touchline), goal kick, corner kick, free kick (direct — can score directly; or indirect), penalty kick (a foul by the defending team inside its own penalty area, or a deliberate handball there), drop ball.

**Offside.** An attacker is offside if, when a team-mate plays the ball, they are nearer the opponents' goal line than both the ball and the second-last opponent, **and** become involved in active play. Not offside direct from a throw-in, corner or goal kick.

**Fouls and misconduct.** Direct free kick / penalty for kicking, tripping, pushing, holding, handball, dangerous play, etc. **Yellow card** (caution) for reckless fouls, dissent, time-wasting, persistent infringement; **two yellows = red**. Straight **red card** (dismissal) for serious foul play, violent conduct, denying an obvious goal-scoring opportunity (DOGSO), spitting, offensive language. A sent-off player is **not replaced** — the team plays a man short for the rest of the match. A red card carries a suspension into subsequent matches (length varies by competition).

**Substitutions.** Since 2022 the Laws permit up to **5 substitutions** per team (made in a maximum of **3 stoppages**, plus half-time), where the competition adopts it — almost all professional competitions now do. **Concussion substitutes** (an additional 1 or 2, permanent, not counting against the 5) are used in many competitions. Friendlies and some youth competitions allow more.

**VAR (Video Assistant Referee).** Where adopted, on-field review of four categories only: **goals** (and build-up infringements), **penalty decisions**, **direct red cards**, **mistaken identity**. "Clear and obvious error" / "serious missed incident" threshold. **Semi-automated offside** (SAOT) is now used in the top UEFA competitions and several leagues. Many lower divisions, reserve leagues, youth leagues and some cup rounds have **no VAR** — this raises officiating variance and is an identity fact worth recording.

**Goalkeeper 8-second rule (Law 12, from 1 July 2025).** A goalkeeper controlling the ball with the hands must release it within **8 seconds** (the referee shows a visible 5-second countdown). Penalty for a breach: a **corner kick** to the opponents (replacing the old, almost-never-called indirect free kick for 6 seconds). This modestly increases corner counts and reduces goalkeeper time-wasting.

**"Captain only" (from 1 July 2025).** When the referee signals it, only the **captain** may approach to query a decision; other players who surround the referee are cautioned.

**Coin toss.** Decides which team kicks off and which way each team attacks in the first half; teams switch ends at half-time.

---

## 2. Shared competition variables (these decide settlement)

Resolve **all** of these per competition and per fixture before setting any market (RULES_SOCCER.md §1, controls 1, 18):

### 2.1 Regulation vs extra time vs penalties

- **League matches:** end after 90' + stoppage. A **draw is a live result**. No extra time.
- **Single-leg knockouts:** if level after 90', normally **two 15-minute halves of extra time** (played in full — a goal does not end them), then a **penalty shoot-out** if still level. Some cups (notably the **Carabao Cup** before the semis, **Leagues Cup**, **Chinese FA Cup** before round 5) **skip extra time and go straight to penalties**.
- **Two-leg ties:** the team with the higher **aggregate** score over both legs advances. If aggregate is level after the second leg's 90', **extra time then penalties** in the second leg. The **away-goals rule was abolished by UEFA in 2021** and by CONMEBOL earlier; some competitions (Liga MX Liguilla) instead advance the **higher-seeded/better-placed team** when aggregate is level, with no extra time except in the final. **Always check the tie-break rule for the specific competition.**
- **A "regulation winner" bet, an "advance/qualify" bet, and an "eventual match winner" bet are three different propositions** (RULES_SOCCER.md control 18). The standard 90-minute market **excludes** extra time and penalties unless the operator says "including ET/pens." A shoot-out win is never a regulation win.

### 2.2 Penalty shoot-out

Five kicks each, alternating, then **sudden death** if level. Only players on the pitch at the end of extra time may take kicks. Since 2017 the standard order is ABAB; the "ABBA" order was trialled and dropped. In the log's terms, a shoot-out result settles "advance/win the tie" markets and any explicit "including penalties" market — nothing else.

### 2.3 Points, tiebreakers and league tables

- **Points:** win **3**, draw **1**, loss **0** — universal in the modern era.
- **Ordering when level on points** varies and matters for relegation/title/European-place markets:
  - **Goal difference first**, then goals scored, then head-to-head: England (Premier League), Germany (Bundesliga), Netherlands, Brazil (with a different chain — see §6.1), most leagues.
  - **Head-to-head first**, then goal difference: **Spain (LaLiga)**, **Italy (Serie A)**, Argentina and several others.
  - **A playoff match ("spareggio"/"desempate")** if two teams are level for the title, a Champions-League place or relegation: **Serie A**, and historically Spain.
- **Points deductions** for insolvency, financial-fair-play or licensing breaches are applied by several federations mid-season — check the current table, not a pre-season projection.

### 2.4 Season structure types

- **Balanced double round-robin** (everyone plays everyone home and away): Premier League, LaLiga, Serie A, Bundesliga, Ligue 1, Eredivisie, Brasileirão, Roshn Saudi League, Chinese Super League, Championnat National.
- **Split system** (a full or partial round-robin, then the table splits into a championship group and a relegation group, with points carried): **Scotland, Belgium, Denmark, Israel, Egypt (2025-26)** and others. In a split league, the fixture list and even the number of remaining games differ by group — never assume a full home-and-away season.
- **Apertura / Clausura** (two separate short championships per calendar year, each with its own champion, plus an annual/aggregate table for continental qualification and relegation): **Argentina, Mexico** and much of Latin America. Frequently followed by a knockout **playoff / "Liguilla" / "fase final"** among the top teams of the short tournament.
- **Group + knockout** (a tournament, not a league): the cups, Leagues Cup, and the continental competitions.

### 2.5 Promotion, relegation and playoffs

The number of clubs relegated, whether the process includes a **relegation/promotion playoff**, and whether **relegation is currently suspended** (Mexico; Egypt for 2025-26) are all competition- and season-specific and are given per competition below. In some countries relegation is decided by a **multi-season average** ("promedios" in Argentina, "coeficiente" in Mexico) rather than the current season alone.

### 2.6 Squad and foreign-player rules

Registered-squad size (often 25 with homegrown-player quotas in Europe), and **foreign / non-domestic player limits** — how many may be **registered** and how many may be **on the pitch at once** — vary widely (see Saudi Arabia, China, Argentina below). A change of one or two available imports is a large effective-strength swing in leagues with tight quotas.

### 2.7 Populations that must not be pooled

Friendlies, youth, reserve/second-team, and senior competitive matches are **different populations** (RULES_SOCCER.md §1). Within senior football, a two-leg European tie is a different population from the same clubs' league matches (controls 12, 15, 28). Knockout stakes suppress the pregame scoring baseline before any goal (control 28).

---

## 3. Continental and international club competitions

### 3.1 UEFA Europa Conference League ("UEFA Conference League")

UEFA's third-tier club competition. In the log: **2026-27 qualifying, second qualifying round, 2nd leg** (July–August 2026).

- **Qualifying (July–August):** two-legged ties (Champions Path and Main Path), aggregate score, **extra time + penalties** in the second leg if level (no away goals). Winners of the play-off round reach the league phase.
- **League phase (since 2024-25):** **36 clubs in one table** ("Swiss model"); each club plays **6 matches** against 6 different opponents (3 home, 3 away). Win 3 / draw 1 / loss 0. **Top 8 → round of 16 directly; 9th–24th → a two-legged knockout play-off; 25th–36th eliminated** (no drop to another competition).
- **Knockout (R16 onward):** two legs, aggregate, ET + penalties, **no away goals**. **Final:** single match at a neutral venue, ET + penalties.
- Settlement: qualifying and knockout ties need the "regulation / 90'" vs "advance" endpoint frozen. League-phase matches are ordinary 90-minute fixtures where a draw is live.

### 3.2 UEFA Women's Champions League (new format, 2025-26)

- **League phase:** **18 clubs in one table**; each plays **6 matches** vs 6 different opponents (3 home, 3 away). Nine clubs enter directly; nine via the third qualifying round.
- **Knockout:** **top 4 get a bye to the quarter-finals; 5th–12th play a two-legged knockout play-off**; then QF and SF two legs (aggregate, ET + penalties, no away goals); **Final** single match at a neutral venue.
- Qualifying rounds (in the log: **third qualifying round, league path, first/second leg**) are two-legged ties, aggregate, ET + penalties in the second leg.

### 3.3 UEFA Women's Europa Cup (new for 2025-26)

UEFA's **second women's club competition**, launched 2025-26 to sit below the Women's Champions League. Two-legged qualifying rounds → a group/league stage → two-legged knockouts → final. Aggregate scoring, ET + penalties, no away goals. Because it is brand-new, there is **no competition history** — treat as a sparse population and shrink hard (RULES_SOCCER.md control 13).

### 3.4 CONMEBOL Copa Libertadores

South America's premier club competition. In the log: **Round of 16, second leg** (2026).

- **Group stage:** 8 groups of 4, double round-robin, top 2 advance (3rd drops to the Copa Sudamericana).
- **Knockout (R16 → QF → SF):** **two legs, aggregate, NO away goals** (removed in 2005), **penalties directly if aggregate is level after the second leg's 90'** — CONMEBOL knockouts before the final go **straight to penalties, with no extra time** (a key difference from UEFA). Confirm per edition, as CONMEBOL has toggled this.
- **Final:** a **single match at a pre-selected neutral venue** (since 2019), with extra time + penalties.
- Settlement: the "advance" market for a R16/QF/SF tie can be decided by a shoot-out with no extra time — freeze the endpoint.

### 3.5 FIFA Intercontinental Cup

A FIFA competition launched in 2024, contested annually by the reigning continental club champions. A **single-match knockout ladder**: the AFC/CAF/CONCACAF/OFC champions play off (the "playoff" and "FIFA Challenger Cup" stages), the survivor plays the CONMEBOL champion (the "Derby of the Americas"), and that winner plays the **UEFA Champions League holder** in the **final** (the FIFA Intercontinental Cup itself). All ties are single matches with **extra time + penalties**. It is distinct from the expanded 32-team **FIFA Club World Cup** (played in 2025, next in 2029).

---

## 4. Domestic leagues — Europe

### 4.1 England — Premier League

20 clubs, **38-match** balanced season (Aug–May). Win 3 / draw 1 / loss 0. **Tiebreak: goal difference, then goals scored, then head-to-head; a playoff match only if the title, relegation or a European place is otherwise unresolved.** **Bottom 3 relegated** to the Championship (which sends up 2 automatically + 1 playoff winner). **5 substitutions** (3 stoppages) + concussion subs. Full **VAR + semi-automated offside**. 25-player squad with **homegrown** quotas; no in-season transfer of the mid-season break rule beyond a short winter pause. No promotion/relegation playoffs at the top level. European qualification: top 5 (currently) to the Champions League + Europa/Conference places, plus domestic cup winners.

### 4.2 England — Carabao Cup (EFL Cup)

Single-elimination knockout of all 92 Premier League + EFL clubs (Premier League clubs in European competition enter in round 3). **No replays.** **No extra time until the semi-finals** — a drawn match in rounds 1–4 and the quarter-finals goes **straight to a penalty shoot-out**. **Semi-finals are two legs** (aggregate, ET + penalties if level after the second leg, **no away goals**). **Final:** single match at Wembley, ET + penalties. Winner qualifies for the Europa/Conference League. Heavy rotation is normal in the early rounds — treat as a partial-strength population.

### 4.3 Germany — Bundesliga

18 clubs, **34-match** balanced season with a **winter break** (~mid-Dec to mid-Jan). Win 3 / draw 1 / loss 0. **Tiebreak: goal difference, then goals scored, then head-to-head.** **16th place plays a two-legged relegation/promotion playoff** against the 3rd-placed club of the 2. Bundesliga; **17th–18th relegated automatically**. **5 subs.** VAR. The **"50+1" ownership rule** shapes the league's economics but not match rules.

### 4.4 Germany — 2. Bundesliga

18 clubs, 34 matches, same points/tiebreak/subs/VAR as the Bundesliga. **Top 2 promoted; 3rd plays the Bundesliga's 16th** in a two-legged playoff. **Bottom 2 relegated to the 3. Liga; 16th plays the 3. Liga's 3rd** in a playoff. In the log: **2026-27, Matchday 3**.

### 4.5 Spain — LaLiga (LaLiga EA Sports)

20 clubs, **38-match** balanced season. Win 3 / draw 1 / loss 0. **Tiebreak: head-to-head first (points, then goal difference between the tied clubs), then overall goal difference, then goals scored, then Fair Play.** **Bottom 3 relegated.** **5 subs.** VAR + SAOT. Non-EU player registration limits apply (typically 3 in the squad). Note the head-to-head-first tiebreak makes late-season "who finishes above whom" markets behave differently from England/Germany.

### 4.6 Italy — Serie A

20 clubs, **38-match** balanced season. Win 3 / draw 1 / loss 0. **Tiebreak: head-to-head (points, then GD in those matches), then overall goal difference, then goals scored; a single playoff match ("spareggio") if two clubs finish level and the position decides the title, a Champions League place, or relegation.** **Bottom 3 relegated** (Serie B promotes 2 + a playoff winner). **5 subs.** VAR. Winter break. In the log: **2026-27, Matchday 2**.

### 4.7 Italy — Coppa Italia

Single-elimination knockout, **seeded** so that Serie A clubs (especially the top 8) enter in later rounds and **host** lower-seeded opponents (home advantage by ranking, not draw). **Extra time + penalties** if level (all rounds). **Semi-finals are two legs** (the only two-legged round; aggregate, ET + penalties, no away goals). **Final:** single match in Rome, ET + penalties. Winner qualifies for the Europa League. In the log: **2026-27, Round of 32**.

### 4.8 Netherlands — Eredivisie

18 clubs, **34-match** balanced season. Win 3 / draw 1 / loss 0. **Tiebreak: goal difference, then goals scored.** The champion and cup winner take European places; a **European play-off** among clubs finishing roughly 5th–8th decides a Conference League qualifying spot. **Bottom club relegated automatically; 16th–17th enter the "Nacompetitie"** — a multi-club playoff with second-tier (Eerste Divisie) clubs for the remaining top-flight places. **5 subs.** VAR.

### 4.9 Belgium — Jupiler Pro League (Belgian Pro League)

**2025-26: 16 clubs** (expanding to 18 in 2026-27). **Regular season:** full double round-robin (30 matches). **Then the table splits:**
- **Champions' play-offs (top 6):** a further double round-robin; **regular-season points are halved** (and rounded) before it starts. Decides the title and top European places.
- **Europe play-offs (7th–12th):** a mini-tournament for the last European ticket; **points halved**.
- **Relegation play-offs (13th–16th):** a further round-robin; **regular-season points carried in full**. **No automatic relegation in 2025-26** — the bottom club after the relegation play-offs meets the Challenger Pro League promotion-playoff winner in a promotion/relegation playoff.
- Settlement: the point-halving means mid-table "points" markets and title/relegation projections must use the **post-split** points, not the regular-season table.

### 4.10 Denmark — Superliga (3F Superliga)

**12 clubs.** **Regular season:** double round-robin (**22 matches**). **Then the table splits, with all points carried in full:**
- **Championship play-off (top 6):** a double round-robin (**10 more matches**) for the title and European places.
- **Qualification/relegation play-off (bottom 6):** a double round-robin; a further **European play-off** for a Conference League qualifying spot; **the bottom 2 are relegated** to the 1st Division.
- Win 3 / draw 1 / loss 0; GD-based tiebreak. In the log: **2026-27, Round 6** (regular season).

### 4.11 Denmark — DBU Pokalen (Danish Cup, "Betano Pokalen")

Single-elimination knockout across all tiers. Early rounds single-leg (lower-ranked club hosts); **quarter-finals and semi-finals are two legs** (aggregate, ET + penalties, no away goals); **final** single match. Extra time + penalties whenever a single match or an aggregate is level. Winner qualifies for the Europa League. In the log: **2026-27, Round 2 (1/32-final)**.

### 4.12 France — Championnat National (National 1)

France's **third tier** (below Ligue 1 and Ligue 2), 18 clubs, **34-match** balanced season, a mix of professional and semi-professional clubs. Win 3 / draw 1 / loss 0; GD tiebreak. **Top 2 (sometimes 3) promoted to Ligue 2; bottom 4 relegated to National 2.** **No end-of-season playoffs. No VAR.** Reserve teams of Ligue 1 clubs may compete but cannot be promoted. Lower budgets, higher variance, thin public data — a sparse population (RULES_SOCCER.md controls 13, 21). In the log: **Round 4** (referred to as "Ligue 3 / National").

---

## 5. Domestic leagues and cups — rest of the world

### 5.1 Brazil — Campeonato Brasileiro Série A

20 clubs, **38-match** balanced season (roughly April–December — a **calendar-year** season, unlike Europe). Win 3 / draw 1 / loss 0. **Tiebreak chain: most wins, then goal difference, then goals scored, then head-to-head, then fewest red cards, then fewest yellow cards, then a draw.** **Bottom 4 relegated** to Série B. Top clubs qualify for the Copa Libertadores and Copa Sudamericana. **5 subs** (6 in some domestic competitions), VAR. Heavy fixture congestion (state championships, two national cups, continental play) means rotation is constant. In the log: **Round 25**.

### 5.2 Argentina — Liga Profesional de Fútbol (Torneo Apertura / Torneo Clausura)

**2026 format:** two tournaments per year (**Apertura**, first half; **Clausura**, second half). **2 zones of ~15 clubs**; each club plays its zone home-and-away plus **1 interzonal "clásico"** (≈15–16 matches). **Top 8 of each zone** enter a **single-match knockout** (Octavos → Cuartos → Semifinales → Final; higher seed hosts; extra time + penalties if level). Each tournament has its own champion.
- **Annual table ("Tabla anual"):** regular-phase points from both tournaments combined — decides most **Copa Libertadores / Sudamericana** berths and **one relegation**.
- **Relegation by "promedios":** a **three-season points-per-match average**; the club(s) with the worst average go down (plus the annual-table bottom club). This means a club can be safe on current form but doomed on its average, or vice versa — check the promedios table, not just the current standings.
- VAR in the top flight. In the log: **Torneo Clausura 2026** (and earlier "Fecha 7, Zona A").

### 5.3 Argentina — Primera C and reserve-league fixtures

The log also contains **Argentine reserve-team fixtures** (labelled variously "Argentina Reserve League", "Primera C Metropolitana Reserves", "Campeonato de Reserva"). These are **reserve (second-string) matches** that mirror the senior club fixture list, usually played at training grounds or small stadia, **with no VAR, minimal public data, heavy squad rotation, and frequent trialists/youth players**. **Primera C** itself is a lower senior division (4th–5th tier of the AFA pyramid) with its own promotion playoffs. Treat both as sparse, low-information populations and cap participant-dependent rows hard (RULES_SOCCER.md control 13).

### 5.4 Saudi Arabia — Roshn Saudi League (Saudi Pro League)

**18 clubs**, **34-match** balanced season (Aug–May). Win 3 / draw 1 / loss 0; GD tiebreak. **Bottom 3 relegated** to the First Division League. **Squad limited to 25**, of which **up to 10 may be foreign**, with **a maximum of 8 foreign players on the pitch at once** (quota expanded in recent seasons). VAR. Top clubs qualify for the AFC Champions League Elite. The heavy foreign allowance means the league's effective quality is highly roster-dependent and top-heavy.

### 5.5 China — Chinese Super League (CFA Super League)

**16 clubs**, **30-match** balanced season (a **calendar-year** season, roughly March–November). Win 3 / draw 1 / loss 0; GD tiebreak. **Bottom 2 relegated** to China League One (which promotes 2). **2026 foreign-player rule ("6655"):** roughly **5 foreign players registered per match and 4 on the pitch simultaneously**, with salary controls — confirm the exact numbers for the season. VAR. In the log: **Round 25**.

### 5.6 China — Chinese FA Cup

Single-elimination knockout, ~80 clubs across all tiers, **8 rounds** (March–December). Lower-division clubs enter first and host. **From the fifth round onward, a level match goes to 30 minutes of extra time then penalties**; in the earlier rounds a level match goes **straight to penalties**. **Quarter-finals and semi-finals** are (in recent editions) single matches; confirm per year. Winner qualifies for the AFC Champions League Two. In the log: **quarter-final** ties (2026).

### 5.7 Egypt — Egyptian Premier League

**2025-26: 21 clubs**, new **split format** — a single round-robin first half, then the table splits into **Group A (top 7)** contesting the title and continental places and **Group B (bottom 14)** contesting survival, with **4 relegated** (relegation had been cancelled the previous season). Win 3 / draw 1 / loss 0. VAR at major venues only. A long, hot-weather, congested calendar (clubs also play CAF competitions and the Egypt Cup). In the log: **Round 3**.

### 5.8 Israel — Israeli Premier League and State Cup

- **Israeli Premier League (Ligat ha'Al):** **14 clubs**, a double round-robin (**26 matches**), then a **split** into a **top playoff (1st–6th)** for the title/Europe and a **bottom playoff (7th–14th)** with **relegation** (bottom 2, sometimes + a playoff). Points carried. Win 3 / draw 1 / loss 0.
- **Israel State Cup (Gvia ha'Medina):** single-elimination knockout of all tiers; **extra time + penalties** if level; final at a national stadium; winner qualifies for the Europa/Conference League. In the log: **2026/27, Round 1**.
- **Israel U19 "Elite" (Noar Premier) division:** the **under-19 youth league** — a development competition. No VAR, volatile lineups, results driven by individual age-group talent; a sparse, low-information population.

### 5.9 Kazakhstan — Premier League (Qazaqstan Prem'er Ligasy)

**2026: expanded to 16 clubs** (from 14). Calendar-year season (March–November). Win 3 / draw 1 / loss 0. **2 clubs relegated** to the First League (which promotes 3). The champion enters the UEFA Champions League qualifying path. VAR at selected matches. In the log: a **postponed Round 21 fixture**.

### 5.10 Armenia — Premier League and Cup

- **Armenian Premier League:** a small league (**10–11 clubs**) playing a **quadruple round-robin** (~36 matches) to fill a full season. Win 3 / draw 1 / loss 0. Bottom club relegated (sometimes + a playoff) with the First League. Champion to the UEFA Champions League qualifying path. Thin squads, small crowds, wide performance variance.
- **Armenian Cup:** knockout; **quarter-finals and semi-finals two legs** (aggregate, ET + penalties, no away goals), **final** a single match; winner to the Europa/Conference League. In the log: a **preliminary / Round of 16** listing.

### 5.11 Uzbekistan — Pro League (second tier)

The **Uzbekistan Pro League is the second tier** of Uzbek football (the top flight is the **Uzbekistan Super League**, 16 clubs). The Pro League runs a calendar-year season (April–November); **top 2 promoted** to the Super League, bottom club(s) relegated to the First League. No VAR; minimal public data. In the log: **Round 17**. Do not confuse it with the Super League.

### 5.12 India — SFA A Division S-League (Sikkim)

A **state-level competition in Sikkim** run under the local sports-federation structure ("SFA" = Sports For All / Sikkim Football Association A Division). Effectively a **regional semi-amateur league** — small squads, part-time players, single grounds, no VAR, near-zero reliable public data, and frequent schedule uncertainty (the log carries an *unresolved* fixture, P-126, precisely because the field-owner schedule could not be confirmed). Standard 90-minute league matches, draws live, points 3-1-0. This is the sparsest population in the entire soccer register — participant/identity uncertainty caps essentially every market (RULES_SOCCER.md control 13, and the general evidence ceiling).

---

## 6. North and Central America

### 6.1 United States — NWSL (National Women's Soccer League)

**2026: 16 clubs** (Boston Legacy and Denver Summit added). **30-match** balanced regular season, single table. Win 3 / draw 1 / loss 0; **draws are live** in the regular season. **No promotion/relegation** (closed league); a **salary cap and roster limits** (~26 senior roster, allocation/international slots). VAR (added 2024). The regular-season leader wins the **NWSL Shield**.
- **Playoffs:** **8 clubs**, single-elimination, seeded by regular-season points. If level after 90', **two full 15-minute extra-time periods** (played out completely), then a **penalty shoot-out**. The final is the **NWSL Championship**.

### 6.2 United States — MLS NEXT Pro

MLS's **third-division development league** (mostly MLS reserve teams + a few independents). **No draws:** a match level after 90' goes **straight to a penalty shoot-out** — **both teams get 1 point for the 90-minute draw, and the shoot-out winner gets a 2nd point** (so a "regulation winner" is a real, distinct outcome from a "match/shoot-out winner"). **3 points for a 90-minute win.** Rosters ~20 for a matchday; up to 5 subs. Heavy developmental rotation — effective team strength swings match to match. **Playoffs:** conference-based single-elimination. In the log: **Colorado Rapids 2 vs Ventura County FC** — the card's "potential winner" is explicitly the **regulation winner**, not the shoot-out winner.

### 6.3 Mexico — Liga MX

**18 clubs.** Two tournaments per year (**Apertura**, Jul–Dec; **Clausura**, Jan–May), each a **17-match** single round-robin, each with its own champion.
- **Liguilla (playoff):** **from Apertura 2026 the "Play-In"/reclasificación round is abolished — the top 8 of the Tabla General go straight to two-legged quarter-finals**, then two-legged semi-finals, then a two-legged final. Higher aggregate advances; **if aggregate is level in the QF or SF, the higher-seeded team advances (no extra time); the final has extra time + penalties.**
- **Tiebreakers:** points, GD, goals scored, head-to-head, away goals, relegation coefficient, Fair Play.
- **Relegation is suspended** — the club with the worst multi-season **coefficient** pays a fine instead of going down. Continental berths (CONCACAF Champions Cup) go to tournament champions and the top of the aggregate table.
- **5 subs**, VAR. In the log: cards reference **Apertura 2026** and earlier **Apertura 2026** fixtures.

### 6.4 Mexico — Liga MX Femenil

The women's competition, **same Apertura/Clausura + Liguilla structure** as the men's Liga MX (17-match tournaments, top-8 two-legged playoff, higher seed advances on level aggregate outside the final). No relegation. In the log: **Apertura 2026**.

### 6.5 CONCACAF — Leagues Cup

An annual **MLS vs Liga MX** tournament (co-sanctioned). **2026: 36 clubs — all 18 Liga MX + 18 qualified MLS clubs.**
- **Phase One (group stage):** clubs split into an **Eastern** and **Western** region of 18, each seeded into 3 tiers; each club plays **3 or 4 cross-league matches** in a mini-round-robin. **"No draws" format — a group match level after 90' goes straight to a penalty shoot-out** (3 points for a 90-minute win, and points for a shoot-out result).
- **Knockout:** the **top 4 clubs from each league** enter a fixed **MLS-vs-Liga-MX bracket** — quarter-finals, semi-finals, third-place match, final — all **single matches, straight to penalties if level (no extra time except, in most editions, the final)**.
- The **finalists and the third-place-match winner qualify for the 2027 CONCACAF Champions Cup.**
- Settlement: the "no draws / straight to penalties" rule means a "regulation (90') result" market and a "match winner (incl. penalties)" market diverge frequently — freeze which one the card uses. In the log: **2026 Quarterfinal** cards.

---

## 7. Friendlies and exhibition tournaments

In the log: **Coupang Play Series** (a promoter-run friendly series in South Korea, e.g. Manchester City vs Atlético Madrid), **KCC Pre-Season Cup** (a club pre-season tournament in Cambodia — *not* the Cambodian Premier League), and various senior "pre-season friendly" / "Telekom Cup" matches.

- **Friendly rules are loose:** often **6+ substitutions** (sometimes unlimited or "rolling"), sometimes **shorter halves**, and a drawn match in a friendly *tournament* frequently goes **straight to a penalty shoot-out** for the bracket / trophy (no extra time).
- **The starting XI cannot be projected for 90 minutes** (RULES_SOCCER.md controls 7, 16): teams make wholesale changes at half-time or on the hour. Separate the **starting-XI phase** from the **mass-substitution phase**; if the substitution plan is unknown, widen second-half scoring and side tails and cap any participant-dependent thesis.
- Motivation is low and asymmetric (fitness work vs a team treating it as a trophy). Treat every friendly as its own one-off population — no transfer to or from competitive form.

### 7.1 ASEAN Club Championship ("ASEAN Hyundai Cup")

Unlike the above, the **ASEAN Club Championship** is a **competitive regional club competition** (Southeast Asian federation), with a group stage and a **two-legged final** (aggregate, ET + penalties). In the log: **senior men's final, second leg**. Treat it as competitive, not a friendly, but with a sparse-competition evidence ceiling.

---

## 8. Cross-competition settlement quick reference

| Competition | Type | Draw in regulation? | Level knockout → | 5 subs / VAR |
|---|---|---|---|---|
| Premier League | balanced league | yes | n/a | yes / yes |
| Carabao Cup | knockout | — | **straight to pens** (ET+pens in 2-leg SF and final) | yes / yes |
| Bundesliga / 2. Bundesliga | balanced league (+ relegation playoff) | yes | n/a | yes / yes |
| LaLiga | balanced league (H2H tiebreak) | yes | n/a | yes / yes |
| Serie A | balanced league (H2H tiebreak; spareggio) | yes | n/a | yes / yes |
| Coppa Italia | seeded knockout | — | ET + pens (2-leg SF) | yes / yes |
| Eredivisie | balanced league (+ Nacompetitie) | yes | n/a | yes / yes |
| Jupiler Pro League | split (points halved in title/Europe playoffs) | yes | n/a | yes / yes |
| Danish Superliga | split (points carried) | yes | n/a | yes / yes |
| DBU Pokalen | knockout | — | ET + pens | yes / partial |
| Championnat National (FRA 3) | balanced league | yes | n/a | yes / **no VAR** |
| Brasileirão Série A | balanced league (calendar year) | yes | n/a | yes / yes |
| Argentine Liga Profesional | Apertura/Clausura + zonal top-8 knockout | yes (league) | ET + pens (final phase) | yes / yes |
| Argentine reserve / Primera C | reserve / lower senior | yes | varies | no / **no VAR** |
| Roshn Saudi League | balanced league (10 foreign / 8 on pitch) | yes | n/a | yes / yes |
| Chinese Super League | balanced league (calendar year; "6655") | yes | n/a | yes / yes |
| Chinese FA Cup | knockout | — | pens (early), ET + pens (R5+) | yes / partial |
| Egyptian Premier League | split (21 clubs, 2025-26) | yes | n/a | yes / partial |
| Israeli Premier League | split | yes | n/a | yes / partial |
| Israel State Cup | knockout | — | ET + pens | yes / partial |
| Israel U19 Elite | youth league | yes | n/a | — / no |
| Kazakhstan Premier League | balanced league (16 clubs, 2026) | yes | n/a | yes / partial |
| Armenian Premier League | quadruple round-robin | yes | n/a | yes / partial |
| Armenian Cup | knockout (2-leg QF/SF) | — | ET + pens | yes / partial |
| Uzbekistan Pro League | 2nd-tier league | yes | n/a | yes / no |
| Sikkim SFA A Division S-League | regional semi-amateur league | yes | n/a | — / no |
| NWSL | balanced league + 8-team playoff | yes (league) | **full ET + pens** | yes / yes |
| MLS NEXT Pro | 3rd-tier league, **no draws** | **no** — 90' draw → shoot-out for bonus point | shoot-out | ~5 / no |
| Liga MX / Femenil | Apertura/Clausura + top-8 Liguilla | yes (league) | higher seed advances (QF/SF); ET+pens (final) | yes / yes |
| Leagues Cup | group + knockout, **no draws** | **no** — 90' draw → shoot-out | shoot-out (ET+pens usually in final only) | yes / yes |
| UEFA Conference League | qualifying/league phase/knockout | yes (league phase) | ET + pens; no away goals | yes / yes |
| UEFA Women's Champions League | qualifying + 18-team league phase + knockout | yes (league phase) | ET + pens; no away goals | yes / yes |
| UEFA Women's Europa Cup | qualifying + group + knockout (new) | yes (group) | ET + pens; no away goals | yes / partial |
| CONMEBOL Libertadores | group + knockout | yes (group) | **pens directly** (R16–SF); ET+pens (final) | yes / yes |
| FIFA Intercontinental Cup | single-match knockout ladder | — | ET + pens | yes / yes |
| Club friendlies / pre-season cups | exhibition | yes (or shoot-out for a trophy) | usually straight to pens | 6+ / usually no |
| ASEAN Club Championship | group + 2-leg final | yes (group) | ET + pens | — / partial |

## 9. Identity checklist (soccer)

Resolve before any rate or contract work, per RULES_SOCCER.md §1:

1. **Exact competition and season**, and therefore the **format type** (balanced league / split / Apertura-Clausura / group-knockout / cup) and the **rule package** in force (subs, VAR, foreign-player quota, points deductions).
2. **Population:** senior competitive vs friendly vs reserve/second-team vs youth — never pooled.
3. **Fixture type:** league match (draw live), single-leg knockout, two-leg tie (which leg, aggregate state), or a "no-draws" competition (MLS NEXT Pro, Leagues Cup, Libertadores knockouts before the final).
4. **Winner-decision rule** for this exact fixture: does it have **extra time**? does a level knockout go **straight to penalties**? if a two-leg aggregate is level, does the **higher seed advance** (Liga MX) or is there ET + penalties (UEFA)? **No away goals** anywhere current.
5. **Market endpoint:** is the contract "regulation / 90'+ stoppage" (the default), "advance/qualify", or "eventual winner incl. ET/penalties"? A shoot-out win is never a regulation win; an ET winner is never a regulation-winner call (RULES_SOCCER.md control 18).
6. **Table stakes** if the card touches a title/relegation/European place: the **tiebreak order** (GD-first vs head-to-head-first), whether a **playoff match** can occur, whether **relegation is suspended**, and whether it is decided by a **multi-season average**.
7. **Data environment:** VAR present or not; public data depth; sparse-competition evidence ceiling (RULES_SOCCER.md control 13) for the lower and exotic competitions above.


## Verified competition-metadata corrections - 2026-09-12

P-176/P-178/P-179 are Ligue 3 2026-27 round-four fixtures. P-179 was a 1-1 league draw, not a National 2 cup tie decided by shootout; in-play penalty goals must not become shootout settlement. P-233/P-234/P-235 were Chinese FA Cup quarterfinals on 1 September, not R16. These corrections are backed by exact L'Equipe and Xinhua/Titan records in audit_2026-09-12/historical_queue_evidence.md. They do not establish any corner total or require a general cup scoring coefficient. P-265's separate Leagues Cup semifinal ended Toluca 2-0 Leon, with first goal at 41 minutes, verified from club/competition reports; its later corner adjudication remains a documentary gap.


## 2026-09-15 — competition sections found missing by `P-374` and `P-377`

Reference only; changes no algorithm. Each fact below was read on an opened page on 2026-09-15; anything not confirmed is marked.

### UEFA Champions League (men's), 2026-27 — league phase and knockouts

- **League phase:** 36 clubs; each plays **eight matches, four home and four away, against eight different opponents** — two from each of four coefficient pots, one home and one away — in a single 36-team table. Win 3 / draw 1 / loss 0.
- **Progression:** places **1–8** go straight to the round of 16; **9–24** play two-legged knockout phase play-offs (9–16 seeded); **25–36** are eliminated from European competition.
- **Tiebreak order when level on points:** goal difference; goals scored; away goals scored; wins; away wins; higher points collected by league-phase opponents; superior goal difference of opponents; higher goals scored by opponents; lower disciplinary points; UEFA club coefficient. *(Source: Wikipedia "2026–27 UEFA Champions League league phase", which summarises the UEFA regulations; open the regulations before settling anything that turns on a tiebreak.)*
- **Calendar:** Matchday 1 8–10 September 2026 to Matchday 8 27 January 2027; play-offs February 2027; round of 16 March; quarter-finals April; semi-finals late April–early May; **final Saturday 5 June 2027, Estadio Metropolitano, Madrid** (UEFA.com).
- **Not confirmed on an opened page this pass:** knockout-tie procedure (aggregate, extra time, penalties, away goals). Verify against the UEFA regulations before any advance/qualify contract; 90-minute contracts are unaffected.
- **Settlement lane:** UEFA `matchstats` FAME feed (field owner for corners, attempts and possession — `SOURCES.md` §"2026-09-11"); ESPN `soccer/uefa.champions` corroborates.

### Guatemala — Liga Nacional (Liga Bantrab), Apertura 2026

- **Final phase (new for Apertura 2026):** **six** clubs qualify, down from eight, so the quarter-finals are removed. **1st and 2nd go straight to the semi-finals**; **3rd v 6th** and **4th v 5th** play the preliminary round (Prensa Libre; ClaroSports).
- **Level series:** in every series **except the final**, the tiebreak favours the club that finished higher in the regular phase (ClaroSports, quoted: "en todas las series, excepto en la final, el criterio de desempate favorecerá al club que haya terminado en mejor posición"). The final's procedure was not stated in the opened articles.
- **Calendar:** season opened on the weekend of 25–26 July 2026; regular phase ends 23 November; second leg of the final scheduled 20 December (could move to 27 December if a Guatemalan club reaches the Copa Centroamericana final).
- **Clubs:** San Pedro and Deportivo Suchitepéquez were promoted (Prensa Libre). **Club count and number of regular-phase rounds are not confirmed:** Prensa Libre gives 22 rounds; a second summary gave 10 clubs / 17 rounds, which is inconsistent. Confirm from the league's own table (`ligagt.com`) before using either number.
- **Settlement lane:** Liga Bantrab official feed owns the score; ESPN `soccer/gua.1` carries scores but **no match statistics**, so no corner or shot contract can be settled there (`P-377-C02`).

<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — source firewall precedence

All league-specific source instructions are subordinate to `SOURCES.md` PF-1/PF-2. Official competition/federation/club sources outrank derivative score sites. Sportsbook/betting/fantasy/DFS material and market-derived projections are never predictive evidence; if an older league note suggests otherwise, this section controls.
