# Base-rates register

**Opened 2026-09-17(b).** Single home for **published base rates used as identity inputs** to a card's arithmetic.

## What belongs here, and what does not

Historical field-owner frequencies belong here with numerator/denominator, exact population, endpoint, retrieval date, query, missingness and uncertainty. They are empirical estimates, even when calculated without a fitted regression. They can inform an explicitly weighted prior or baseline; they are not mathematical identity inputs that every matchup must share. Numbers below are preserved from the prior retrieval and were not independently re-fetched in this correction. No universal run-line ceiling, push cap, variance floor or automatic rank bar follows from them. See SCORING_AND_VALIDATION and RULES_GENERAL G-L24.

## Why it exists

Before this register, base rates lived inside whichever sport file happened to derive one. The `P-438`–`P-451` audit derived eight new MLB figures at once and immediately exposed the problem: the same number was needed by `RULES_BASEBALL.md` controls 34, 35 and 37, by `RULES_GENERAL.md` `G-L24`, and by the scorecard's push-mass coherence rule in `METHOD.md` §5. Three copies of a number with three refresh dates is how a stale base rate becomes an invisible error. There is one copy, here.

It also makes the honest gaps visible. Most sports in this repository have **no derived margin band at all**, and the table below says so in the same place it publishes the one that exists, rather than leaving the absence implicit.

---

## 1. Handicap / margin bands — consumed by `G-L24` (`RULES_GENERAL.md` §16.13(e))

G-L24 queries the specified team’s signed-margin distribution, not the realised winner’s pooled margin. See RULES_GENERAL section 16.13(e) for exact integer, half-line and draw treatment.

| Sport / competition | Line | `b_L` | Conditioning | `n` | Source and query | Derived | Refresh |
|---|---|---|---|---:|---|---|---|
| **MLB** | 1.5 | **0.278** overall | by winner-minus-loser season W%: −0.2 **0.284** · −0.1 **0.301** · 0.0 **0.282** · +0.1 **0.268** · **+0.2 0.229** | 2,286 | `statsapi.mlb.com/api/v1/schedule?sportId=1&startDate=2026-03-25&endDate=2026-09-16&gameType=R&hydrate=linescore`; margin = \|away−home\| on `Final`/`Completed Early` games | 2026-09-17(b) | each season, and mid-season if cited after 1 Aug |
| MLB (9-inning games only) | 1.5 | 0.239 | excludes extras | 2,086 | same | 2026-09-17(b) | with the row above |
| NFL | 3 / 7 | key-number masses **`NOT_YET_DERIVED`** | — | — | `G-L12` already fixes a historical residual SD benchmark of about 13.9 points (Stern 1991), not a conditional width floor in `RULES_AMERICAN_FOOTBALL.md`; the key-number *masses* at 3 and 7 have never been computed here | — | derive before the next NFL handicap card |
| Soccer — **EPL 2025-26** | 1.5 | pooled P(\|margin\| ≥ 2) **0.350**; draw **0.274**; one-goal **0.376** | pooled, both sides; the conditional (favourite) band is still to be derived per card | 380 | §7.3 | 2026-09-25 | each season. Other competitions: `NOT_YET_DERIVED` |
| Basketball — **NBA 2025-26 / WNBA 2026 / NBL 2025-26** | varies | pooled P(\|margin\| ≤ k) for k = 3, 5, 7, 10, 15 | pooled; margin is integer-valued, so `b_L` is read per line from §7.1 | 1,235 / 327 / 165 | §7.1 | 2026-09-25 | each season. Other leagues: `NOT_YET_DERIVED` |
| NHL 2025-26 | 1.5 | P(margin ≥ 2) **0.568** of all games; **0.756** of regulation-decided games | empty-net goals are in **73.0%** of two-goal regulation wins (§7.2) | 1,312 | §7.2 | 2026-09-25 | each season |
| AFL, NRL, rugby union, cricket, tennis | varies | `NOT_YET_DERIVED` | — | — | — | — | derive per competition before use |

**Missing band:** mark the reference NOT_YET_DERIVED. A complete conditional model may still supply a transparent subjective or fitted margin distribution. Missing pooled data does not automatically demote a row; missing conditional evidence is disclosed. The previous 0.53/0.54 ceiling and fixed extras contribution are withdrawn. For example w=.85 and r=.23 imply P(−1.5)=.6545 without violating probability laws. No historical card is re-ranked.

## 2. Endpoint / overtime mixtures — consumed by `RULES_BASEBALL.md` control 37 and `G-L19`

| Sport | Quantity | Value | `n` | Source | Derived | Refresh |
|---|---|---:|---:|---|---|---|
| **MLB** | P(tie after 9 → extras) | **0.0875** | 2,286 | `statsapi`, `currentInning > scheduledInnings` | 2026-09-17(b) | each season |
| MLB | P(final margin = 1 \| extras) | **0.685** | 200 | same (2-run 0.205; 3+ 0.110) | 2026-09-17(b) | each season |
| MLB | runs added by extras | mean **2.88**; P(≥2) **0.605**; P(≥4) ≈ 0.24 | 200 | same; final total minus 9-inning total | 2026-09-17(b) | each season |
| MLB | regulation total in games that reach extras | mean **6.81**, median 6 | 200 | same | 2026-09-17(b) | each season |
| MLB | innings played in extras games | 10: 149 · 11: 34 · 12: 13 · 13: 4 | 200 | same | 2026-09-17(b) | each season |
| KBO / NPB | terminal-tie rate after the innings cap | `NOT_YET_DERIVED` | — | `G-L19` requires the cap itself as a `G0`/`G2` identity field (baseball control 32, origin `P-432`) | — | derive before the next KBO/NPB winner label |
| Soccer (knockout) | extra-time / shoot-out reach rate | `NOT_YET_DERIVED` | — | — | — | derive before the next knockout winner label |

**Correct endpoint identity:** if regulation ends tied with total exactly L and an action-valid full game completes, at least one run is added, so the total exceeds L with probability 1 conditional on that state and completion. The historical 0.605 is P(at least two added), a different event. Compute tie probability from joint team scores; do not add extras to an already final-score model.

---

## 3. Total-runs / total-points geometry — consumed by `RULES_BASEBALL.md` control 35 and `METHOD.md` §5

| Quantity | 2026 value | `n` | Note |
|---|---:|---:|---|
| MLB mean / median total runs | **8.98 / 8** | 2,286 | sd **4.53**, variance 20.49 |
| MLB push mass by integer line | 6 → 7.0% · **7 → 11.5%** · 8 → 8.1% · 9 → 9.1% · 10 → 6.7% · 11 → 7.3% · 12 → 4.2% | 2,286 | **11.5% is the maximum at any integer** |
| Share of MLB total-runs variance explained by park identity | **4.3%** | 30 parks, n ≥ 60 each | between-park variance of means 0.885 against a total variance of 20.49 |

**Push cap withdrawn:** Var(T)=E[Var(T|X)]+Var(E[T|X]). The park-only 4.3% figure does not constrain every conditional variance or PMF cell. The 11.5% maximum is a realised cohort frequency, not a universal matchup ceiling. Derive push mass from a coherent conditional model and check it on held-out games. No independent row cap or automatic ranking correction follows.

### Venue reference distributions (2026, through 16 Sep)

Consumed by control 35's "print the venue base rate beside the line" requirement. `n` ≈ 74–78 per park, so the standard error on each proportion is ≈ 5.7 points — **these anchor a disclosure, they do not settle a close call.**

| Venue | mean | median | P(≥12) | modal total |
|---|---:|---:|---:|---|
| Coors Field | 11.38 | 11 | **47.3%** | 10 (12.2%) |
| Wrigley Field | 9.85 | 9 | 41.0% | 3 (11.5%) |
| Target Field | 9.18 | 9 | 27.3% | 5 (10.4%) |
| Daikin Park | 8.94 | 9 | 27.3% | 9 (10.4%) |
| Chase Field | 8.76 | 8 | 22.4% | 9 (13.2%) |
| Progressive Field | 8.45 | 8 | 24.4% | 5 (12.8%) |
| Busch Stadium | 8.36 | 8 | 21.8% | 5 (14.1%) |
| Globe Life Field | 8.18 | 8 | 20.3% | 6 (17.6%) |

~~Remaining 22 parks: `NOT_YET_DERIVED`~~ **All 30 parks are derived through 24 Sep in §7.5 (2026-09-25). That table supersedes the eight rows above**, which are kept as the 16 Sep snapshot.

---

## 4. Round / competition reference rates — evidence only, not identity inputs

These are too small to be identities. They are recorded because a card that departs far from its own round's realised rate should say why.

| Competition | Quantity | Value | `n` | Derived |
|---|---|---:|---:|---|
| ACL2 + UEL matchday 1, 16 Sep 2026 | first-half goals 0/1/2/3/4 | 8 / 3 / 4 / 1 / 1 | 17 | 2026-09-17(b) |
| same | P(1H ≥ 2) → a 1H Under 1.5 wins | **35.3%** → 64.7% | 17 | SE ≈ 12 points |
| same | P(1H ≥ 3) → a 1H Under 2.5 wins | **11.8%** → 88.2% | 17 | SE ≈ 8 points |
| same | P(FT ≥ 3) / P(FT ≥ 5) | 35.3% / 17.6% | 17 | — |

**How this was used, and the limit.** The three cards that priced a 1H Under 2.5 at 87–92% sat on the round's own 88.2% and went 3/0. `P-438` priced a 1H Under **1.5** at 84% against a round rate of 64.7% and lost. At `n = 17` that gap is ~1.6 SE — suggestive, not conclusive — so it supports **soccer control 40's disclosure requirement** (derive sibling phase lines from one printed distribution) and supports **no coefficient at all**.


---

<!-- AUDIT-2026-09-24F -->
## 5. MLB 2026 doubleheader and one-run rates — derived 2026-09-24(f)

**Query.** `statsapi.mlb.com/api/v1/schedule?sportId=1&gameType=R&startDate=2026-03-01&endDate=2026-09-24&fields=dates,date,games,gamePk,doubleHeader,gameNumber,status,codedGameState,detailedState,teams,away,home,score,dayNight,scheduledInnings`. The query was run on 2026-09-24 at about 23:30 AEST.

**Filter.** Final (`codedGameState = F`), with `scheduledInnings = 9`.

**Status and use.**
- These are reference estimates with their `n`.
- The doubleheader rows are **§4-class evidence**: n = 23, and they are confounded with makeup-game timing. They are not identity inputs.
- The one-run row is a §1-class reference rate. `RULES_GENERAL.md` §"2026-09-24(f)"(d) (`COVERING_PAIR`) consumes it.

| Population | n | Mean total runs | SD | P(total ≤ 7) (95% CI) | P(total ≤ 8) |
|---|---:|---:|---:|---|---:|
| All 9-inning regular-season finals | 2,374 | 8.95 | 4.51 | 0.428 (0.408–0.448) | 0.510 |
| Non-doubleheader | 2,328 | 8.98 | 4.52 | 0.427 (0.407–0.448) | 0.508 |
| Doubleheader G1 (all types) | 23 | 7.78 | 3.44 | 0.435 (0.232–0.637) | 0.609 |
| Doubleheader G2 (all types) | 23 | 7.91 | 4.14 | 0.478 (0.274–0.682) | 0.565 |
| Doubleheader G1, split admission (`S`) | 20 | 8.05 | 3.02 | 0.400 (0.185–0.615) | 0.600 |
| Doubleheader G1, traditional (`Y`) | 3 | 6.00 | 5.10 | — (n too small) | — |
| Day games, non-doubleheader | 846 | 8.89 | 4.55 | 0.431 (0.398–0.465) | 0.515 |

| Population | n (decided games) | One-run games | P(one-run) |
|---|---:|---:|---:|
| 2026 MLB regular-season finals | 2,374 | 655 | **0.276** |

**Reading.**
- G1 and G2 have similar means, both below the league. That points to a doubleheader-context confound (makeup games, weather and timing), **not** a G1-specific effect.
- The P(≤ 7) for G1 is indistinguishable from non-doubleheader games.
- The rejected rule `MLB-DOUBLEHEADER-G1-TOTAL-DEFLATION` claimed "57.3%". That figure has no source and is contradicted here.
- P(one-run) is the probability that both opposite +1.5 rows win. That is a structural rate, not skill.

---

<!-- AUDIT-CLOSURE-2026-09-25 -->
## 6. Cricket and tennis records carried from the 2026-09-22 cohort audit (added 2026-09-25)

**Status: §4-class context, not an identity input.** One venue over one fortnight is not a base rate, and the 2026-09-22 audit ruled that the chase result pattern is context only (`RULES_CRICKET.md` control 5, §2.8).

**Kensington Oval, CPL 2026, 12–18 Sep: powerplay (0.1–6.0 overs) by innings order.** Source: ESPN cricket API summaries for events 1534212–1534216, via the CPL league-ID route (Part 5 §"2026-09-22", P-482 retrospective).

| Innings order | Powerplays (runs/wickets) | n | Mean runs | Over 47.5 |
|---|---|---:|---:|---:|
| All teams batting first | 50/1, 30/3, 24/4, 34/1, 37/2 | 5 | 35.0 | 1 of 5 |
| All teams chasing | 36/3, 33/2, 79/0, 77/1\*, 75/1 | 5 | 60.0 | 3 of 5 |

\* Target-censored: the Falcons needed 77 in Qualifier 1.

- **Toss context** (not a rule): toss winners chose to field in 6 of 6 Kensington matches from 12 to 20 Sep, and the chasing side won all six.
- **Use:** it shows why phase totals must be split by innings order (control 21, extended 2026-09-25). It is not a prior for any future Kensington phase total.

**WTA best-of-three total games: gap record — CLOSED 2026-09-25.** As of 2026-09-22 no admitted source for a WTA total-games base rate existed; the Sackmann `tennis_wta` repository returned HTTP 404. The ESPN tennis scoreboard is now admitted for this purpose. It covers the Slams, WTA/ATP tour events and WTA 125 events, but not ITF. The 2026 rates are in §7.4. ITF totals remain `NOT_YET_DERIVED`.

---

<!-- RESEARCH-2026-09-25 -->
## 7. Cross-sport reference rates — derived 2026-09-25

**Status: §1-class reference rates** (historical field-owner frequencies with n and query). They are not identities, not coefficients and not caps, and none automatically moves a centre, width or rank.

- **Where they are used:** a card prints the relevant row beside its own number (`REFERENCE_BASE_RATE`). When a card departs far from the row, it says why.
- **Queries, scripts and result JSON:** [`research/base_rates_2026-09-25/`](research/base_rates_2026-09-25/README.md).
- **Retrieval:** 2026-09-25, 00:10–01:00 AEST.
- **ESPN lane change, verified this pass:** scoreboard date *ranges* now return HTTP 400. Query one date per call.

### 7.1 Basketball — regular season

**(a) Level, shape and bands**

| Quantity | NBA 2025-26 | WNBA 2026 | NBL 2025-26 |
|---|---:|---:|---:|
| Games (n) | 1,235 | 327 | 165 |
| Total points: mean / SD / median | 230.7 / 21.7 / 231 | 174.4 / 20.7 / 173 | 182.5 / 19.1 / 182 |
| Home margin, mean (95% CI) | +1.72 (0.81, 2.64) | +1.70 (0.11, 3.28) | +0.65 (−2.10, 3.41) |
| Home win | 0.555 | 0.538 | 0.503 |
| Margin SD (raw) | 16.4 | 14.6 | 18.1 |
| Overtime rate | 0.044 | 0.037 | 0.055 |
| Points added by overtime (mean) | 25.2 | 26.5 | 24.4 |
| P(\|margin\| ≤ 3 / 5 / 7) | 0.146 / 0.246 / 0.341 | 0.150 / 0.269 / 0.382 | 0.176 / 0.279 / 0.364 |
| P(\|margin\| ≤ 10 / 15) | 0.479 / 0.656 | 0.554 / 0.719 | 0.455 / 0.624 |
| First half: mean / SD / share of regulation | 116.3 / 12.6 / 0.506 | 86.3 / 12.6 / 0.497 | 92.4 / 11.3 / 0.510 |
| Quarter means Q1 / Q2 / Q3 / Q4 | 58.7 / 57.6 / 58.5 / **55.3** | 43.7 / 42.6 / 44.0 / 43.2 | 46.1 / 46.3 / **44.5 / 44.2** |

**(b) Width benchmark.** This is the residual SD around a crude, leak-free season-to-date predictor (see the research README). It is the reference for `C-WIDTH-BENCHMARK` (`RULES_GENERAL.md` §"2026-09-25(b)").

| Competition | Total: raw SD → residual SD | Margin: raw SD → residual SD | n scored |
|---|---|---|---:|
| NBA 2025-26 | 21.7 → **19.4** | 16.4 → **15.1** | 1,076 |
| WNBA 2026 | 20.7 → **19.5** | 14.6 → **13.3** | 248 |
| WNBA 2025 / 2024 | 18.4 → 16.9 / 17.6 → 16.0 | 15.2 → 13.7 / 12.9 → 11.1 | — |
| NBL 2025-26 | 19.1 → **18.7** | 18.1 → **15.2** | 111 |
| NBL 2024-25 / 2023-24 | 20.7 → 18.8 / 17.7 → 17.2 | 15.9 → 15.0 / 14.6 → 16.1 | — |

**(c) Early season and regime shifts.** Three seasons each; within-season difference, inverse-variance pooled.

| Quantity | NBL (2023-24, 2024-25, 2025-26) | WNBA (2024, 2025, 2026) |
|---|---|---|
| Games where both teams have played fewer than 3 games: total minus the rest of that season | −11.7, −5.0, −8.6 → pooled **−8.5 (−14.3, −2.7)**, n = 38 early games | +8.5, +6.0, +3.4 → pooled **+6.5 (+0.4, +12.6)**, n = 57 |
| Both teams fewer than 5 games | pooled −6.2 (−10.8, −1.6), n = 69 | pooled +4.1 (−0.4, +8.6), n = 95 |
| Season-to-date predictor residual bias (actual − predicted) | +4.0, +9.3, +4.2 (scoring rises through the season) | +1.1, +0.6, +2.3 |
| League mean total by season | 181.2 → 185.7 → 182.5 | 163.7 → 163.7 → **174.4** |

**Reading.**
- The early-season effect has the **same sign in 3 of 3 seasons in each league and opposite signs between the two leagues**. That is why no cross-league rule follows. Each is a league-specific reference rate for that league's opening games.
- **WNBA 2026 scored 10.7 points per game more than 2024 and 2025.** Any multi-season WNBA average or head-to-head that includes 2024 or 2025 is contaminated by that regime (M24) unless it is adjusted or excluded, and the card says which.
- NBL cards issued in the first rounds of 2026-27 (P-508, P-509 and later) sit inside the early-season window.

**(d) Back-to-backs** (named-mechanism reference; `RECENCY_AND_REBOUND.md` §7.3). NBA team on a back-to-back against a rested opponent: margin residual **−1.84 (−3.78, +0.11)**, n = 261. Totals show no reliable fatigue effect.

### 7.2 NHL 2025-26 — regular season, `api-web.nhle.com/v1/score/{date}` (n = 1,312)

| Quantity | Value |
|---|---|
| Total goals: mean / SD | 6.25 / 2.30 |
| P(total ≤ 3 / 4 / 5 / 6 / 7 / 8) | 0.127 / 0.194 / **0.427** / **0.531** / 0.749 / 0.821 |
| Decided in regulation / overtime / shoot-out | 0.752 / 0.158 / 0.091 (reached overtime 0.248) |
| Games with an empty-net goal; empty-net goals per game | **0.346**; 0.382 |
| Regulation-decided margin 1 / 2 / 3 / 4 / 5+ | 0.244 / 0.233 / 0.307 / 0.142 / 0.073 |
| P(margin ≥ 2): all games; regulation-decided | **0.568** (0.541, 0.595); 0.756 |
| Two-goal regulation wins containing an empty-net goal | **0.730** (0.673, 0.788), n = 230 |
| Home win; home margin | 0.522; +0.13 goals |
| **Preseason 2025** (n = 104): total mean; P(total ≤ 5); overtime or shoot-out | **5.68**; **0.567**; 0.212 |
| **Preseason 2026 to 24 Sep** (n = 36): total mean; P(total ≤ 5) | **5.33**; 0.556 |
| Playoffs 2026 (n = 82): total mean; overtime | 5.93; 0.268 |

**Structural notes.**
1. A game decided after regulation adds exactly one goal to the regulation tie, so full-game totals of overtime and shoot-out games are **odd**. That is why P(total = 5) is 0.233 but P(total = 6) is 0.104. A 2–2 regulation tie lands Under 5.5; a 3–3 tie lands Over 6.5.
2. Most two-goal margins are created by an empty-net goal. A −1.5 row is largely a bet on the trailing side pulling its goalie and conceding.
3. **Preseason games score about half a goal to a goal fewer than the regular season.** A preseason card uses the preseason row, not the regular-season one.

### 7.3 EPL 2025-26 (n = 380; scoreboard plus match summaries)

| Quantity | Value |
|---|---|
| Total goals: mean / SD; distribution 0 / 1 / 2 / 3 / 4 / 5 / 6+ | 2.75 / 1.57; 0.071 / 0.139 / 0.239 / 0.266 / 0.155 / 0.087 / 0.042 |
| Over 1.5 / 2.5 / 3.5; both teams score | 0.789 / 0.550 / 0.284; 0.561 |
| Home / draw / away | 0.426 / **0.274** / 0.300 |
| \|margin\| 0 / 1 / 2 / 3+ | 0.274 / 0.376 / 0.203 / 0.147 |
| First half: mean goals; distribution 0 / 1 / 2 / 3 / 4+ | **1.19** (second half 1.56); 0.284 / 0.382 / 0.224 / 0.084 / 0.026 |
| P(first half ≥ 1 / ≥ 2 / ≥ 3) | 0.716 / **0.334** / 0.111 |
| Corners: mean / SD / median; per team | 10.0 / 3.27 / 10; 5.0 (SD 2.77) |
| P(corners ≥ 8 / 9 / 10 / 11 / 12) | 0.755 / 0.661 / 0.563 / 0.437 / 0.316 |
| Width benchmark: total residual SD; margin residual SD | 1.61 (no better than raw 1.57); 1.51 |

The first-half P(≥ 2) of 0.334 agrees with §4's ACL2/UEL round (0.353, n = 17). A first-half Under 1.5 above about 0.75 needs a named reason.

### 7.4 Tennis 2026 — ESPN tennis scoreboard, completed singles, 1 Jan – 24 Sep

Retirements (208) and walkovers (51) are excluded, because their totals are censored. ITF is not covered.

| Quantity | Women, best of 3 (n = 5,146; 94 events incl. WTA 125 and qualifying) | Men, best of 3 (n = 2,698) | Men, Slam main draw, best of 5 (n = 485) |
|---|---|---|---|
| Total games: mean / SD / median; 10th–90th percentile | 21.75 / 5.79 / 20; 15–30 | 23.41 / 6.00 / 22; 17–32 | 37.25 / 9.34 / 36; 26–51 |
| P(deciding set) | **0.340** (±0.013) | 0.358 | 0.217 (five sets) |
| Mean total: straight sets / deciding set | **18.2 / 28.6** | 19.6 / 30.3 | 33.6 (3–4 sets) / 50.5 |
| P(total ≥ 19 / 20 / 21 / 22 / 23) | 0.624 / 0.542 / 0.472 / 0.425 / 0.376 | 0.763 / 0.671 / 0.586 / 0.530 / 0.453 | — |
| Winner's game margin: mean / SD | 5.35 / 2.65 | 4.43 / 2.38 | 6.49 / 3.26 |
| P(winner margin ≥ 4 / 5 / 6 / 7) | 0.767 / 0.637 / **0.495** / 0.344 | 0.659 / 0.486 / 0.321 / 0.185 | 0.827 / 0.749 / 0.652 / 0.509 |
| … given a straight-sets win: ≥ 5 / ≥ 6 / ≥ 7 | 0.818 / **0.663** / 0.479 | 0.654 / 0.447 / 0.270 | — |
| … given a deciding-set win: ≥ 5 / ≥ 6 / ≥ 7 | 0.286 / **0.168** / 0.081 | 0.186 / 0.094 / 0.032 | — |
| Any tiebreak | 0.216 | 0.384 | 0.538 |

**Main draw v qualifying (women):** main draw n = 3,547, mean 21.95, P(deciding) 0.352; qualifying n = 1,599, mean 21.28, P(deciding) 0.313.

**Structural notes.**
1. Total games is a **two-component mixture**: straight sets centre about 18, deciding sets about 29. Lines from 19.5 to 25.5 sit in the trough between them, so a total row there is mostly a bet on P(deciding set). A card prints that probability beside the 0.34–0.35 reference.
2. **Games-handicap coherence** (for `C-HCP-COHERENCE`, `RULES_TENNIS.md` §"2026-09-25(b)"). P(player −k.5) = P(win in straight sets) × P(margin ≥ k+1 | straight-sets win) + P(win in a deciding set) × P(margin ≥ k+1 | deciding-set win). The conditional rows above are the population reference. `P-495` stated P(win) 0.843 and P(−5.5) 0.591, which implies P(margin ≥ 6 | win) = 0.70. That is **above even the straight-sets conditional (0.663)**, and the card named no hold/break evidence for it. The row lost.

### 7.5 MLB 2026 — all parks, first five innings, width (statsapi; 9-inning Finals, n = 2,373 through 24 Sep)

**League.** Total runs mean 8.95, SD 4.51.

**Width benchmark.** Residual SD around the crude team predictor is **4.50** (n = 2,146). That is essentially the raw SD: team season rates explain almost none of the game-total variance (`RECENCY_AND_REBOUND.md` §2). The margin residual SD is 4.57.

**First five innings:**
- mean 5.00, SD 3.29;
- P(F5 ≤ 3 / 4 / 5 / 6) = 0.376 / 0.499 / 0.612 / 0.708;
- P(tied after five) **0.154**;
- the first five innings carry 55.9% of all runs.

**One-run asymmetry (added 2026-09-25(c)).** Home teams win **52.9%** of games. They win by exactly one run **16.7%** of the time and lose by exactly one run **10.9%**: walk-offs end home wins at a one-run margin. So P(home +1.5) = 0.638 and P(away +1.5) = 0.638 are nearly equal, although the moneyline split is 52.9 / 47.1. A card's +1.5 row is judged against that 0.638 baseline, not against its moneyline probability (`SKILL_BASELINE_LEDGER.md`).

**Venues:** every park with n ≥ 30. SE of a mean is about 0.4–0.6 runs, so these anchor a disclosure and do not settle a close call.

| Venue | n | Mean | Median | P(≤ 7) | P(≥ 10) | P(≥ 12) |
|---|---:|---:|---:|---:|---:|---:|
| Sutter Health Park | 71 | 11.41 | 11 | 0.225 | 0.634 | 0.380 |
| Coors Field | 80 | 11.12 | 10.5 | 0.225 | 0.613 | 0.438 |
| Nationals Park | 78 | 10.83 | 10 | 0.231 | 0.564 | 0.410 |
| PNC Park | 80 | 10.00 | 9.5 | 0.375 | 0.500 | 0.362 |
| Kauffman Stadium | 77 | 9.82 | 9 | 0.416 | 0.416 | 0.299 |
| Wrigley Field | 80 | 9.79 | 9 | 0.400 | 0.487 | 0.400 |
| Citizens Bank Park | 77 | 9.43 | 9 | 0.377 | 0.468 | 0.299 |
| Target Field | 77 | 9.18 | 9 | 0.403 | 0.429 | 0.273 |
| American Family Field | 77 | 9.03 | 7 | 0.519 | 0.364 | 0.260 |
| Rate Field | 78 | 8.96 | 9 | 0.372 | 0.410 | 0.231 |
| Daikin Park | 81 | 8.88 | 8 | 0.432 | 0.383 | 0.259 |
| Chase Field | 79 | 8.82 | 8 | 0.430 | 0.354 | 0.228 |
| Great American Ball Park | 81 | 8.75 | 9 | 0.395 | 0.481 | 0.222 |
| Yankee Stadium | 77 | 8.74 | 8 | 0.442 | 0.416 | 0.299 |
| Citi Field | 81 | 8.67 | 8 | 0.444 | 0.284 | 0.222 |
| Truist Park | 81 | 8.63 | 8 | 0.420 | 0.346 | 0.235 |
| UNIQLO Field at Dodger Stadium | 80 | 8.61 | 8 | 0.463 | 0.338 | 0.212 |
| Oracle Park | 78 | 8.60 | 7.5 | 0.500 | 0.346 | 0.256 |
| Tropicana Field | 81 | 8.58 | 7 | 0.506 | 0.321 | 0.235 |
| Oriole Park at Camden Yards | 80 | 8.54 | 8 | 0.450 | 0.388 | 0.225 |
| Progressive Field | 81 | 8.47 | 8 | 0.457 | 0.395 | 0.247 |
| loanDepot park | 78 | 8.45 | 8 | 0.474 | 0.372 | 0.218 |
| Busch Stadium | 81 | 8.43 | 8 | 0.457 | 0.370 | 0.222 |
| Fenway Park | 77 | 8.42 | 8 | 0.481 | 0.364 | 0.221 |
| Rogers Centre | 78 | 8.32 | 8 | 0.487 | 0.372 | 0.192 |
| Globe Life Field | 80 | 8.19 | 8 | 0.438 | 0.350 | 0.188 |
| Comerica Park | 78 | 8.10 | 7.5 | 0.500 | 0.295 | 0.192 |
| Angel Stadium | 81 | 7.88 | 7 | 0.543 | 0.309 | 0.136 |
| Petco Park | 78 | 7.78 | 7.5 | 0.500 | 0.282 | 0.154 |
| T-Mobile Park | 77 | 7.78 | 8 | 0.494 | 0.286 | 0.104 |

Neutral or one-off sites (n < 30: Estadio Alfredo Harp Helu 2, Las Vegas Ballpark 6, Field of Dreams 1, Journey Bank Ballpark 1) are not tabled.

### 7.6 Width calibration of issued cards — descriptive, hindsight (2026-09-24 cohort, P-495–P-509)

z = (actual − card centre) / card width, from each card's Field 3 line and the settled final. Calibrated widths give a mean z² of about 1.

| Target | Cards | Mean z | Mean z² | Basketball only |
|---|---:|---:|---:|---|
| Total | 15 | −0.11 | **1.29** | **1.93** (n = 7; largest misses P-499 +2.33, P-508 −2.21) |
| Margin | 13 | 0.00 | 0.57 | 0.96 (n = 7) |

**Reading.**
- Centres are unbiased.
- Basketball **total** widths ran about 39% too narrow (√1.93). The LKL cards' widths (12.1–12.9) sat 19–38% below every total benchmark in §7.1(b) (15.9–19.5). No LKL benchmark has been derived; LKL is `NOT_YET_DERIVED`.
- Margin widths were adequate.
- n = 7 is far too small to calibrate on. This opens the prospective measurement `C-WIDTH-Z` (`LEARNING_REGISTER.md` §"2026-09-25(b)"), and it is **not** a width multiplier.

### 7.7 NFL, AFL and NRL references, TB-1 widths and underdog-cushion cover rates (derived 2026-09-25(e))

**Source.** ESPN site API scoreboards (`football/nfl`, `australian-football/afl`, `rugby-league/3`), one date per call. There were 1,704 completed games and 0 failed days. The NRL regular season is ESPN season type 1. Query: `research/team_baseline_2026-09-25e/oval_base_rates.py` → `oval_base_rates.json`. No odds are read. These rows replace `NOT_YET_DERIVED` for the NFL, AFL and NRL.

#### (a) Population rows

| | NFL 2024 | NFL 2025 | AFL 2025 | AFL 2026 | NRL 2025 | NRL 2026 |
|---|---:|---:|---:|---:|---:|---:|
| n | 272 | 272 | 207 | 207 | 216 | 213 |
| Home win (non-neutral) | 0.524 | 0.536 | 0.565 | 0.585 | 0.551 | 0.545 |
| Draw | 0.000 | 0.004 | 0.005 | 0.015 | 0.005 | 0.000 |
| Total mean (SD) | 45.8 (13.1) | 46.0 (13.8) | 168.6 (29.8) | 178.2 (29.1) | 46.1 (14.0) | 47.8 (13.9) |
| Total 10 / 50 / 90% | 30 / 46 / 62 | 29 / 45 / 65 | 132 / 168 / 208 | 142 / 181 / 216 | 29 / 44 / 64 | 30 / 48 / 66 |
| Home margin mean | +1.7 | +2.2 | +6.0 | +7.1 | +3.8 | +0.0 |
| Margin SD | 14.5 | 14.2 | 42.5 | 40.8 | 18.7 | 20.7 |

**NFL key numbers** (the G-L12 residual benchmark; previously `NOT_YET_DERIVED`):

| Margin | 2024 | 2025 |
|---|---:|---:|
| P(\|margin\| = 3) | 0.136 | 0.151 |
| P(\|margin\| = 7) | 0.074 | 0.096 |
| P(\|margin\| ≤ 3) | 0.239 | 0.268 |
| P(\|margin\| ≤ 7) | 0.518 | 0.496 |

**Close games:**
- AFL: P(\|m\| ≤ 6) 0.145 / 0.169; ≤ 12 0.300 / 0.280; ≤ 24 0.478 / 0.473.
- NRL: P(\|m\| ≤ 2) 0.125 / 0.150; ≤ 6 0.343 / 0.291; ≤ 12 0.509 / 0.455.

#### (b) Reference widths (TB-1 residual SD, leak-free)

| | Total | Margin |
|---|---:|---:|
| NFL | 13.4 | 13.6 |
| AFL | 29.1 | 36.8 |
| NRL | 13.9 | 19.9 |

The `C-WIDTH-BENCHMARK` row for these leagues. A card below 0.85 × the reference names what it knows.

#### (c) Underdog cushion cover rates

The underdog is the side with the lower leak-free TB-1 margin, never the market. Each entry is the share of games in which the underdog covered +k.5.

| League (season) | Dog won | +1.5 | +2.5 | +3.5 | +4.5 / +5.5 / +6.5 | +7.5 / +8.5 | larger |
|---|---:|---:|---:|---:|---:|---:|---|
| NBA 2025-26 | 0.297 | 0.321 | 0.348 | 0.383 | +5.5 0.439 | +7.5 0.501 | +9.5 0.562 |
| WNBA 2026 | 0.321 | 0.339 | 0.365 | 0.390 | +5.5 0.459 | +7.5 0.531 | +9.5 0.610 |
| WNBA 2025 | 0.353 | 0.365 | 0.385 | 0.409 | +5.5 0.480 | +7.5 0.540 | +9.5 0.631 |
| NBL 2025-26 | 0.368 | 0.397 | 0.427 | 0.449 | +5.5 0.507 | +7.5 0.559 | +9.5 0.566 |
| NBL 2024-25 | 0.383 | 0.392 | 0.408 | 0.442 | +5.5 0.500 | +7.5 0.583 | +9.5 0.683 |
| NFL 2024 | 0.320 | 0.345 | 0.379 | 0.453 | +6.5 0.567 | +7.5 0.606 | +10.5 0.690; +13.5 0.704 |
| NFL 2025 | 0.395 | 0.422 | 0.457 | 0.543 | +6.5 0.596 | +7.5 0.655 | +10.5 0.695; +13.5 0.762 |
| NRL 2025 | 0.385 | 0.412 | 0.440 | — | +4.5 0.511; +6.5 0.566 | +8.5 0.615 | +12.5 0.670 |
| NRL 2026 | 0.417 | 0.429 | 0.491 | — | +4.5 0.509; +6.5 0.549 | +8.5 0.617 | +12.5 0.651 |
| AFL 2025 | 0.294 | — | — | — | +6.5 0.383 | +12.5 0.483 | +18.5 0.556; +24.5 0.600; +30.5 0.628 |
| AFL 2026 | 0.328 | — | — | — | +6.5 0.430 | +12.5 0.505 | +18.5 0.586; +24.5 0.618; +30.5 0.688 |

**Use.** This table is the `BASELINE_P` of a +k.5 row on the TB-1 underdog (`C-PLUS-CUSHION` as amended in `RULES_GENERAL.md` §"2026-09-25(e)"(e)). Read the nearest k and the most recent season. Where the side is not the TB-1 underdog, use `TEAM_BASELINE_P`.

**Reading.** A small cushion on the weaker team covers well under half the time in every one of these leagues. That is the population mechanism behind M32.

#### (d) TB-1 resolution map (out of sample, latest season)

Details are in `research/team_baseline_2026-09-25e/README.md`.

| Target | TB-1 beats the base rate | No resolution |
|---|---|---|
| Sides and margins | NBA, WNBA, NBL, NFL, AFL, NRL, EPL (by 5–19% in Brier) | MLB, NHL |
| Totals | NBA, WNBA, NFL (marginal) | NBL, AFL, NRL, EPL, MLB, NHL |

---

## Maintenance

- **Cite, never copy.** A sport file, `METHOD.md` or a card points at the row here. If a figure must be restated in place for readability, restate it with its `n` and derivation date attached so a stale copy is self-evident.
- **Staleness.** A season-cadence figure cited more than one completed season after its derivation date is `STALE` and must be recomputed before it is used as a reference prior.
- **Provenance.** Every row carries the query that produced it. A row whose query cannot be re-run is downgraded to §4 (evidence only) and loses its reference-use status.
- **`n` travels with the number, always** — in the sport file, on the card, and in any report (`METHOD.md` §5).

**Related:** `RULES_GENERAL.md` §16.13(e) (`G-L24`) · `RULES_BASEBALL.md` controls 34–37 · `RULES_AMERICAN_FOOTBALL.md` (G-L12 residual benchmark) · `DATA_SOURCE_REGISTER.md` §"2026-09-17(b)" (`SRC-MLB-STATSAPI-SEASON`) · `CONTROLS.md`.
