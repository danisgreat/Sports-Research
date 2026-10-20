<!-- BEGIN CANONICAL RESEARCH P-602 -->
## P-602 — SOCCER / UAE Pro League · Al Dhafra SCC vs Dubai United · 2026-10-16
Import: 2026-10-21T01:07:13+11:00; prompt 4 NEW_CANONICAL_EVENT. Local event key `LOCAL-2026101679B3FBCC8D-G0002` → canonical **P-602**; native identity UAEPL fixture 22e17f5f-7604-11f1-b32b-0289588efdb9. Source mini `2026101679B3FBCC8D`, frozen source SHA-256 `b7478342e7ecba6861d9d79e4fc98b1dcd686356260f8b21911989847115ad7e` (313,155 bytes). Card core SHA-256 `5fbba3e57274fd2f7247e633940f1b375b5ea11efc900ac62c80986c136424fb` (25,794 bytes) = the exact bytes between the local BEGIN/END CARD marker lines (source offsets 70773–96567); markers and headings outside them remain in the preserved source. Original method, probabilities, ranks, statuses, timing and gaps are literal; any NOT_ASSIGNED / PENDING wording inside the core is historical. Import is not a forecast timestamp and confers no certification.

## Card · LOCAL-2026101679B3FBCC8D-G0002 · SOCCER / UAE ADNOC Pro League · Al Dhafra SCC vs Dubai United · 2026-10-16 UAE

- **Local event key:** `LOCAL-2026101679B3FBCC8D-G0002` — LOCAL_UNIMPORTED; G0002 only in this cumulative local working copy.
- **Canonical ID:** `NOT_ASSIGNED / PROMPT_4_IMPORT`. GitHub READ_ONLY; no remote publication.
- **Native identity:** `UAEPL:2026-27:MW6:ALDHAFRA:DUBAIUNITED:2026-10-16` stable surrogate; official fixture URL `SRC-UAE001`; provider-native UUID `22e17f5f-7604-11f1-b32b-0289588efdb9` is a public fixture route, provider ID semantics not separately inspected.
- **Authority:** `PUBLISHED_MAIN_PINNED ca03fdf844b3c29c723b1d6244024b195604fff8`. MDS-2026.10.16-v20.0 / CR-R7 / SCV-v11 / SEL-v3 / MINI-v1 / EXH-v1 / RETAIN-v2 / PRIMARY-v3.3 / CYCLE-v1.
- **Start:** scheduled `2026-10-16T17:05:00+04:00` UAE = `2026-10-16T13:05:00Z` = `2026-10-17T00:05:00+11:00` AEDT. Hamdan Bin Zayed Stadium, Al Dhafra/Madinat Zayed. Actual first play NOT_VERIFIED. Research/card preparation `2026-10-16T23:52:10+11:00`; issue state measured against actual current time, NOT retroactively assigned.
- **Forecast disposition:** `RESEARCH_ONLY_NO_MODEL` / `UNCALIBRATED_ANALYST_SCENARIO / NOT_PRIMARY`. Genuine primary model `p_card=NOT_ESTIMATED`, model grid/η/warm-start/feedback `NOT_COMPUTED`. The six analyst probabilities below are **not** executed GitHub model probabilities, RL policy outputs, certified calibration or forward-settled results.
- **Capability attempt:** `python -m ml capability` in local container => `/opt/pyvenv/bin/python: No module named ml`; `git ls-remote https://github.com/danisgreat/Sports-Research.git HEAD` => `Could not resolve host: github.com`; connector GitHub source reads do not install or execute the primary runtime. No fabricated receipts/hashes, baseline, contextual-cycle release or feedback.
- **Model execution manifests:** one G0002 row with blank execution and feedback paths, reason `NOT_RUN_CAPABILITY_BLOCKED`; historical 2025/26 Division One games are not admitted as top-flight same-competition training observations without a validated competition adjustment.
- **Sport endpoints:** first half 45 minutes plus stoppage; full time 90 minutes plus stoppage, no extra time/penalty kicks; corners recorded in 90 minutes plus stoppage. Original operator terms, abandoned/postponed/void grading and corner provider definition UNKNOWN_DEFINITION; no theoretical integer push at 0.5/2.5/10.5 given the assumed units.
- **Roster:** official exact-match starting XI and bench NOT_VERIFIED; prior-game XI listings are not confirmed selections. Official pregame interview states some injured Dubai United players returned but names not provided; manager change for Al Dhafra confirmed by club source. Availability uncertainty NOT fitted.
- **Information closure:** INFORMATION_INCOMPLETE (XI/bench, specific absences, event-time final recheck, first-half full 20-game rows, independently reconciled game-level corners, provider terms and executable ML remain open). Retained analysis is usable as an audit-labelled analyst comparison only.

### Decision block
Analyst probabilities across the six supplied opposite-direction contracts indicate a high chance of under 10.5 corners and a moderately high chance of at least one first-half goal / 3+ full-time goals. This is **not a trained primary forecast**; sample-size/lineup/competition uncertainty is material. Expected score ≈ **Al Dhafra 1.25 – Dubai United 2.08** goals, expected total 3.33 and expected combined corners 7.80 (not an exact final-score prediction).

#### A1. Identity, timing, event state
- Official `SRC-UAE001` and club/league pregame news `SRC-UAE002`, `SRC-UAE003` confirm the named clubs, home venue, local kickoff and league matchweek 6. Not to be confused with UAE U23 reserve fixture on 17 October (different venue/participants).
- Soccer full-match goal and corner endpoints are 90+stoppage. Pre-match web captures in these searches show schedules, not actual final; exact kickoff and event state at post-card readback NOT_VERIFIED. Sources have page published dates; exact per-page retrieval seconds not supplied by service. This card's document write time is recorded truthfully.
- No same-identity local G0001 duplicate: it is the unrelated CSL Henan/Tianjin original. Other unpublished user-desktop minis, writer leases and canonical body duplicate inventory remain incompletely accessible. New canonical IDs deliberately not assigned.

#### A2. Frozen owner request and candidate universe
```text
**Upcoming game — SOCCER**

- Game details: <Al Dhufra SCC vs Dubai United>
- Scheduled start: <12:05 AM AEDT, 17 October 2026 (Can be delayed)>
- Supplied contracts: <Combined 1st half goals: Over/Under 0.5 Goals>, <Combined total goals: Over/Under 2.5 Goals>, <Combined Total Corners: Over/Under 10.5 Corners>
- Research constraints: <continue pre game analysis/research/process even if it goes past start time>
```
Exactly six requested contracts, period/endpoint qualified, no substitutions:

| Supplied contract | Quantity/period | Analyst p (NOT_PRIMARY) | Mechanical W/P/L/V interpretation |
|---|---|---:|---|
| Under 10.5 corners | Combined awarded corners, FT 90+ | **0.7919** | W if total ≤10; L if ≥11; P=0; V conditional on terms |
| Over 10.5 corners | Same | **0.2081** | W if ≥11; L if ≤10; P=0 |
| 1H Over 0.5 goals | Combined goals first half, stoppage | **0.6747** | W if at least 1 by HT; L at 0 |
| 1H Under 0.5 goals | Same | **0.3253** | W at 0 by HT; L if ≥1 |
| FT Over 2.5 goals | Combined full-time regulation goals | **0.6461** | W if ≥3; L if ≤2 |
| FT Under 2.5 goals | Same | **0.3539** | W if ≤2; L if ≥3 |

These are complementary only for fully played/recorded fixtures with matching settlement conventions. CYCLE/PRIMARY model p_card for all six = NOT_ESTIMATED. Supplied rows are descriptive rank-only; no model-certified PICK designations. Original payout/odds not provided, monetary EV NOT_COMPUTABLE.

#### A3. Audited online history, league context, roster and research sources
**Recent league form (GF goals scored/GA conceded; sorted newest first, UAE venue date):**

| Al Dhafra window | n | GF | GA | GF/game | GA/game | Note |
|---|---:|---:|---:|---:|---:|---|
| L5 | 5 | 3 | 9 | 0.600 | 1.800 |
| L10 | 10 | 6 | 18 | 0.600 | 1.800 |
| L15 | 15 | 8 | 30 | 0.533 | 2.000 |
| L20 | 20 | 13 | 39 | 0.650 | 1.950 |

| Dubai United window | n | GF | GA | GF/game | GA/game | Note |
|---|---:|---:|---:|---:|---:|---|
| L5 | 5 | 12 | 13 | 2.400 | 2.600 |
| L10 | 10 | 17 | 16 | 1.700 | 1.600 |
| L15 | 15 | 24 | 22 | 1.600 | 1.467 |
| L20 | 20 | 34 | 25 | 1.700 | 1.250 |

Al Dhafra L20 includes 5 games from 2026/27 and 15 from 2025/26, all first division **top tier**; Dubai United L20 includes 5 UAEPL games from 2026/27 plus **15 second-tier Division One** games. These windows overlap and are not independent samples. Dubai United's lower-division history must not be assumed equally strong as UAEPL performance; RSSSF confirms promotion (2025/26 second place, 45 GF/28 GA in 28 games). Explicit previous competition flag retained; raw L20 rates are diagnostic, not silently fed into a fitted UAEPL model.

| # | Al Dhafra game date | GF | GA | Competition |
|---:|---|---:|---:|---|
| 1 | 2026-09-11 | 2 | 1 | UAEPL |
| 2 | 2026-09-06 | 0 | 1 | UAEPL |
| 3 | 2026-08-29 | 0 | 2 | UAEPL |
| 4 | 2026-08-22 | 0 | 2 | UAEPL |
| 5 | 2026-08-15 | 1 | 3 | UAEPL |
| 6 | 2026-05-16 | 1 | 0 | UAEPL |
| 7 | 2026-05-10 | 0 | 5 | UAEPL |
| 8 | 2026-05-05 | 2 | 2 | UAEPL |
| 9 | 2026-04-24 | 0 | 1 | UAEPL |
| 10 | 2026-04-11 | 0 | 1 | UAEPL |
| 11 | 2026-04-05 | 0 | 1 | UAEPL |
| 12 | 2026-03-18 | 0 | 3 | UAEPL |
| 13 | 2026-03-10 | 1 | 2 | UAEPL |
| 14 | 2026-02-26 | 1 | 1 | UAEPL |
| 15 | 2026-02-20 | 0 | 5 | UAEPL |
| 16 | 2026-02-13 | 1 | 1 | UAEPL |
| 17 | 2026-02-06 | 2 | 3 | UAEPL |
| 18 | 2026-01-28 | 0 | 2 | UAEPL |
| 19 | 2026-01-19 | 1 | 1 | UAEPL |
| 20 | 2026-01-08 | 1 | 2 | UAEPL |

| # | Dubai United game date | GF | GA | Competition |
|---:|---|---:|---:|---|
| 1 | 2026-09-10 | 1 | 1 | UAEPL |
| 2 | 2026-09-05 | 3 | 4 | UAEPL |
| 3 | 2026-08-28 | 4 | 1 | UAEPL |
| 4 | 2026-08-23 | 3 | 2 | UAEPL |
| 5 | 2026-08-15 | 1 | 5 | UAEPL |
| 6 | 2026-05-29 | 0 | 2 | Division One |
| 7 | 2026-05-23 | 1 | 1 | Division One |
| 8 | 2026-05-15 | 0 | 0 | Division One |
| 9 | 2026-05-10 | 2 | 0 | Division One |
| 10 | 2026-05-03 | 2 | 0 | Division One |
| 11 | 2026-04-24 | 2 | 1 | Division One |
| 12 | 2026-04-15 | 1 | 3 | Division One |
| 13 | 2026-04-11 | 2 | 1 | Division One |
| 14 | 2026-04-04 | 0 | 0 | Division One |
| 15 | 2026-03-15 | 2 | 1 | Division One |
| 16 | 2026-03-07 | 3 | 1 | Division One |
| 17 | 2026-02-26 | 3 | 0 | Division One |
| 18 | 2026-02-21 | 2 | 1 | Division One |
| 19 | 2026-02-16 | 1 | 1 | Division One |
| 20 | 2026-02-06 | 1 | 0 | Division One |

**Independent current-season confirmation:** League owner confirms Al Dhafra 1W/4L and Dubai United 2W/1D/2L, the latest dated matches and venue. Season reports across 35 UAEPL games show 117 total goals, 56 home and 61 away: average 3.343 goals/match, 1.600 home and 1.743 away. League scoring time buckets 1–15,16–30,31–45 minute goals: 13+14+15=42 (45th-minute timing group; added-half-time caveat). <https://www.besoccer.com/competition/info/arabian_gulf_league/2027>.

**Corners, current UAEPL five-match descriptive rates (`SRC-UAE010`):** Al Dhafra 3.40 for + 3.20 conceded, Dubai United 3.80 for + 5.20 conceded. Independent home excerpts (`SRC-UAE011`): Al Dhafra last home league corners 6+1=7 versus Al Wahda and 2+3=5 versus Sharjah; these are only partial cross-checks, not proof of complete five-game corner totals.

**Availability and mechanisms:** exact-competition pregame Al Dhafra manager Patrice Carteron replaces prior manager Alen Horvat, confirmed `SRC-UAE003`; organizer coach interview `SRC-UAE002` reports Dubai United manager Andrea Pirlo says several injured players have returned, identities/positions not named. `SRC-UAE012` labels XI as *last starting XIs* from Sep 11/Sep 10, so those are NOT today’s confirmed eleven/bench. No injury list can be treated as a verified clean squad or all available.

**Source-discovery/reuse observations:**
| Source ID | Source scope | URL opened/search result | Collector | Closure/limitations |
|---|---|---|---|---|
| SRC-UAE001 | UAE Pro League official fixture | https://uaeproleague.ae/en/fixtures/22e17f5f-7604-11f1-b32b-0289588efdb9 | Official/owner | Observed source coverage only; provider lineage and complete independent corroboration NOT_VERIFIED |
| SRC-UAE002 | UAE Pro League official pre-match news | https://uaepl.ae/en/news-and-gallery/adnoc-pro-league-989 | Official/owner | Observed source coverage only; provider lineage and complete independent corroboration NOT_VERIFIED |
| SRC-UAE003 | Al Dhafra club 2026-10-16 report | https://dfsc.ae/%D8%A7%D9%84%D8%B8%D9%81%D8%B1%D8%A9-%D9%8A%D8%B3%D8%AA%D9%82%D8%A8%D9%84-%D9%8A%D9%88%D9%86%D8%A7%D9%8A%D8%AA%D8%AF-%D9%81%D9%8A-%D8%A7%D9%84%D8%B8%D9%87%D9%88%D8%B1-%D8%A7%D9%84%D8%A3%D9%88%D9%84/ | Official/owner | Observed source coverage only; provider lineage and complete independent corroboration NOT_VERIFIED |
| SRC-UAE004 | UAE season first 35 league fixture goals | https://www.besoccer.com/competition/info/arabian_gulf_league/2027 | Independent/secondary | Observed source coverage only; provider lineage and complete independent corroboration NOT_VERIFIED |
| SRC-UAE005 | Al Dhafra 2025/26 and current results | https://www.besoccer.com/team/matches/al-dhafra/2026 | Independent/secondary | Observed source coverage only; provider lineage and complete independent corroboration NOT_VERIFIED |
| SRC-UAE006 | Al Dhafra cross-check last 20 results | https://globalsportsarchive.com/en/soccer/team/al-dhafra-scc/1752/matches | Independent/secondary | Observed source coverage only; provider lineage and complete independent corroboration NOT_VERIFIED |
| SRC-UAE007 | Dubai United 2026/27 and Division One results | https://www.footballfixtures.org/team/dubai-united | Independent/secondary | Observed source coverage only; provider lineage and complete independent corroboration NOT_VERIFIED |
| SRC-UAE008 | Dubai United prior league corroboration | https://www.besoccer.com/team/matches/united-football-club | Independent/secondary | Observed source coverage only; provider lineage and complete independent corroboration NOT_VERIFIED |
| SRC-UAE009 | Dubai United prior results cross-check | https://www.footballfirst.com/football-live-centre/team/dubai-united-fc/7907/results | Independent/secondary | Observed source coverage only; provider lineage and complete independent corroboration NOT_VERIFIED |
| SRC-UAE010 | Season five-game corners per side | https://betting-insider.com/en/football/matches/al-dhafra-vs-dubai-united/stats/ | Independent/secondary | Observed source coverage only; provider lineage and complete independent corroboration NOT_VERIFIED |
| SRC-UAE011 | Al Dhafra recent home-corners examples | https://footybets.io/statistics/al-dhafra/ | Independent/secondary | Observed source coverage only; provider lineage and complete independent corroboration NOT_VERIFIED |
| SRC-UAE012 | Previous XI clearly historical, not confirmed | https://www.playmakerstats.com/match/2026-10-16-al-dhafra-dubai-united/12676790 | Independent/secondary | Observed source coverage only; provider lineage and complete independent corroboration NOT_VERIFIED |
| SRC-UAE013 | 2025/26 division strength/United promotion | https://rsssf.org/tablesu/uae2026.html | Independent/secondary | Observed source coverage only; provider lineage and complete independent corroboration NOT_VERIFIED |
| SRC-UAE014 | League goals first-half drought review | https://uaecuesports.com/coverage/al-dhafra-s-first-half-drought-meets-united-s-late-leak-107983/ | Independent/secondary | Observed source coverage only; provider lineage and complete independent corroboration NOT_VERIFIED |

Sources linked above are web-search/open outputs for this task. Browsing/open behavior differs by route and some owner pages are crawled snapshots; retrieval timestamp precision, raw capture hashes and full provider independence remain NOT_VERIFIED. No prediction website's odds/prices/tips were used as numerical inputs.

#### A4. Explicit analyst distribution, expected-score arithmetic, baseline and sensitivities
**Research-supported but uncalibrated full-time construction:** current UAEPL first five GF/GA home = 3/5,9/5; away =12/5,13/5. Geometric opposing strength pairing for team goals:

- `lambda_home=sqrt((Al Dhafra GF/5)*(Dubai United GA/5))=sqrt(0.6*2.6)=1.2490 goals`.
- `lambda_away=sqrt((Dubai United GF/5)*(Al Dhafra GA/5))=sqrt(2.4*1.8)=2.0785 goals`.
- `lambda_total=3.3275` goals, `expected signed Al Dhafra margin = -0.8295`. This is a *scenario* and is not the repository's fitted Dixon–Coles goal grid; goal covariance/low-score corrections are omitted. `Pois(3.32746)` total: `P(FT≥3) = 1 - exp(-lambda)*(1+lambda+lambda²/2)=0.6461`; complement `0.3539`.
- Scenario goal winner diagnostics from independent team Poissons (Skellam): Al Dhafra win ≈ 22.5%, draw ≈ 21.0%, United win ≈ 56.5%. Again NOT_PRIMARY and not a trained match-winner forecast.

**First-half totals, unsupported primary phase:** UAE league has 42 recorded 1–45 minute goals among 117 total; observed timing share `42/117 ≈ 0.3590`. Naive proportional expected 1H goals `lambda_total*(42/117)=1.1944`; choose a declared **6% analyst downward adjustment** to 1.123 (Al Dhafra no first-half goals in their 5 UAEPL matches, club-focused report `SRC-UAE014`; adjustment size deliberately heuristic and not learned). `Pois(1.123)` gives `P(1H≥1)=1-e^-1.123=0.6747`. The numerator may miss goals grouped under first-half stoppage in one provider; denominator/time bucketing and source lineage therefore remain open. This half probability is an UNCALIBRATED_ANALYST_SCENARIO only.

**Corners, unsupported primary family:** projected home awarded `0.5*(home-for3.4+opponent-against5.2)=4.3`; projected away awarded `0.5*(away-for3.8+opponent-against3.2)=3.5`. Hence `mu_corners=7.8`. Corners are overdispersed: assumed **negative-binomial variance-to-mean ratio=1.6** (not empirically fitted), so shape `r=mu/(1.6-1)=13`, success `p=r/(r+mu)=0.625`. `P(C≤10)=NB_CDF(10;r=13,p=0.625)=0.7919`, `P(C≥11)=0.2081`. As a comparison the Poisson at the same centre yields under10.5≈0.8352, demonstrating distribution sensitivity. No independent 20-game corner ledger/variance fit exists here.

**Baseline:** `BASELINE_LEAGUE_V1` identical-contract executable artifact/receipt NOT_COMPUTED; 2026/27 league 3.343 gpm is a descriptive reference, NOT falsely frozen as exact-scope baseline probabilities. Expected total corners does NOT use a proved league-wide corner mean. Adjustments: managerial change, recovered injured players, home/away samples and weather remain UNFITTED, and no unverified input decides Rank1 of a PRIMARY numerical card.

| Scenario | Expected FT goals | 1H goals | Corners | P(1H Over0.5) | P(FT Over2.5) | P(Under10.5 corners) |
|---|---:|---:|---:|---:|---:|---:|
| Low-scoring/fewer corners | 2.85 | 0.98 | 6.80 | 62.5% | 54.2% | 86.8% |
| Base (published analyst diagnostic) | 3.3275 | 1.123 | 7.80 | 67.5% | 64.6% | 79.2% |
| High-scoring/higher corners | 3.75 | 1.40 | 9.20 | 75.3% | 72.3% | 66.4% |

These scenario bounds are **parameter sensitivity, not calibrated confidence intervals**; they are not reconstructed ML ensemble weights and do not demonstrate predictive skill.

#### A5. All six original directions, ranks, distribution families and expected quantities
| Analyst rank | Supplied direction | analyst_p NOT_PRIMARY | Expected relevant count | Why / distance to line |
|---:|---|---:|---:|---|
| 1 | FT combined corners UNDER 10.5 | **79.2%** | 7.80 corners | difference centre − line = −2.70 corners; overdispersion scenario; not primary |
| 2 | 1H combined goals OVER 0.5 | **67.5%** | 1.123 goals | difference +0.623 first-half goals; league-time proxy, heuristic |
| 3 | FT combined goals OVER 2.5 | **64.6%** | 3.327 goals | difference +0.827 goals; five-game cross-rate Poisson |
| 4 | FT combined goals UNDER 2.5 | **35.4%** | 3.327 goals | same unconditional goal grid complement |
| 5 | 1H combined goals UNDER 0.5 | **32.5%** | 1.123 goals | same 1H grid complement |
| 6 | FT combined corners OVER 10.5 | **20.8%** | 7.80 corners | same corner grid complement |

For these half-unit lines `PUSH=0` **conditional on normal action**, `VOID=UNKNOWN` outside final normal completion; W/L complement is calculated as if no void. No arbitrarily capped probability, betting-market source or forced 90% contract. Under repository selection rank1 0.62/0.04 provisional gate, the analyst best alternative is 1H Over0.5 (0.6747); margin ≈0.1172; however **this is NOT a model-eligible numeric gate**, since fitted primary corner/half adapters and same-line baseline are absent. Family dependence unknown (goals/corners joint not modelled); do not assert both decisive can be forecast jointly with Poisson independence.

#### A6. Specific risks and unadjusted comparisons
- Dubai United L20 contains 15 lower-tier fixtures; promotion/competition-strength regime prevents naive L20 blending. UAEPL current five show high-scoring games; early-season tail volatility large.
- Al Dhafra coach replacement is confirmed but managerial uplift is not estimated; returning Dubai United injured players are unnamed and may alter the odds materially.
- Exact XI, bench, late absences, field conditions and first play not confirmed. No game action should be retrospectively priced as if those were known.
- Corners source exposes only aggregate own/opponent averages for five games, not joint fixture-level covariance/variance; NB overdispersion is a transparent assumption.
- First-half source timing bins do not prove complete 1H stoppage inclusion; half-time lineup selection may matter disproportionately at a 0.5 line.
- 2025/26 head-to-head has different rosters and divisions, is not admitted as a predictive adjustment. Operator rules still open.

#### A7. Selection, correlated families and ML/RL shadow controls
- The fitted `PRIMARY_HEDGE_MIX_V3` and connected CYCLE worker were not executed: no supported `PREDICTIONS.csv`, `EXECUTION.csv`, release, weights, candidate/comparator receipt, learned expert losses or RL policy. Historical/source-verified feature rows are retainable as **future candidates only**, not learned online Hedge feedback.
- Uncalibrated analyst ranking for the exact six supplied directions given A5; first two only descriptive, never named PRIMARY_PICK. Corners vs 1H goal jointly dependent/unknown; numeric RET04/XCARD6/T2/Brier/baseline-delta/frozen shadow requires valid fitted joint/paired evidence, therefore NOT_COMPUTED.
- The framework's RL component is online expert weighting, not a trained action-selection environment agent. No unsupported RL performance gain is asserted. Correct evidence horizon is earliest of actual issue, verified kickoff and source-known-at; original statistical snapshot timestamps remain observed, not backdated.

#### A8. Actual source attempts, failures, corroboration, next fields
| Field / exact source route attempted | Observed result | Closure and next route |
|---|---|---|
| Official fixture `SRC-UAE001` plus organizer `SRC-UAE002` and club `SRC-UAE003` | Matchweek 6/venue/kickoff identified | ID/time source confirmed; native provider semantics/actual first play OPEN |
| Team L5/L10/L15/L20 via `SRC-UAE005`/`SRC-UAE006` & `SRC-UAE007`/`SRC-UAE008`/`SRC-UAE009` | 20 dated goals pairs each; true window n 5/10/15/20, previous-division scope flagged | Further official prior-match row-by-row corroboration needed; incomplete provider lineage OPEN |
| League current form and 35-game stats `SRC-UAE001` / `SRC-UAE004` / `SRC-UAE013` | 3-9 and 12-13 first five; league total 117/35; 2025/26 Dubai United promoted | Cross-source values match at aggregate level, independence of statistics collectors not comprehensively established |
| Current 5-game corner rates `SRC-UAE010` versus home samples `SRC-UAE011` | 3.4,3.2 vs 3.8,5.2; two older home scorelines | Complete match-by-match corn totals, corner definitions, 2nd collector, variance NOT_VERIFIED; next official UAEPL match-stat detail |
| Coach/news `SRC-UAE002`,`SRC-UAE003` | Carteron new coach; Pirlo says several return from injury | Named exact XI, bench, full injured/suspended list OPEN; next owner match sheet and both teams' official channels |
| Last XI `SRC-UAE012` | Explicit *last starting XIs* | Never exact-game confirmation; original exact sheet still OPEN |
| `python -m ml capability` in sandbox | `/opt/pyvenv/bin/python: No module named ml` | Code bootstrap `git ls-remote` failed DNS; pinned offline worker/approved checkout, install deps/release/history then execute/verify primary |
| 1H 42/117 minute buckets `SRC-UAE004` + drought `SRC-UAE014` | Defined season aggregate and named trend | Direct match-level both-side first-half L20, official half-time definition/stoppage/source lineage OPEN |
| Operator contract terms | NO user terms, no URL captured | Need owner original acceptance/action/abandonment settlement definitions; UNKNOWN_DEFINITION |
| Pre-start final time state | No verified official first-play snapshot | Mark `KNOWN_AT_UNVERIFIED`, do not claim clean first-play availability; actual automation NOT_SCHEDULED |

No fake source-closure CSV entries or unrun retry promises. SOURCE_DISCOVERY_REGISTER/SOURCE_SEARCH_ATTEMPTS/REQUIREMENT_CLOSURE not fabricated from an unperformed secondary workflow. Open fields remain INFORMATION_INCOMPLETE and can be revisited by a later authorized owner review.

#### A9. Honest research/execution/custody integrity receipt and completion matrix
| Check | Result | Explanation |
|---|---|---|
| A1 identity and kickoff | PARTIAL_PASS | Owner/league/club sources agree, actual first play not verified |
| A2 all supplied contracts assessed | PASS | 6/6 analyst direction scenarios, endpoint and action caveats |
| A3 dated form | PARTIAL_PASS | 20 each recovered and counted; source independence and lower-tier change unresolved |
| A3 exact lineup/absences | OPEN | Prior-game starters ≠ confirmed today; injury-return names not disclosed |
| A4 distribution and expected quantities | PASS_ANALYST_ONLY | True arithmetic; no fitted primary calibration / model grid |
| A4 baseline and CYCLE/primary | NOT_EXECUTED | `No module named ml`, clone DNS inaccessible; no invented files/fit/receipts |
| A5 candidate/probability coverage | PASS_ANALYST_ONLY | Exact supplied 6 directional percentages, NOT_PRIMARY |
| A6 sensitivity | PASS_ANALYST_ONLY | Three parameter/dispersion cases, unfit effects marked |
| A7 learning/shadow selection | NOT_COMPUTED | No official bundle, frozen baseline, joint effects or audited model feedback |
| A8 corroboration/availability | INFORMATION_INCOMPLETE | Exact next routes and scope limitations logged |
| A9 retention/readback/canonical | TO_VERIFY_LOCALLY | Local cumulative Markdown and companion CSV delivered separately; no GitHub write; canonical NOT_ASSIGNED |

- **Overall:** INFORMATION_INCOMPLETE / RESEARCH_ONLY_NO_MODEL; the three numerical forecasts are analyst sensitivity calculations, **not** trained ML/RL output. Operator endpoints unverified. No settled outcomes, scoring outcomes or historical model-performance claims.
- **Time:** actual draft file creation/readback recorded by local filesystem; all original earlier G0001 issued bytes remain intact, cumulative copy includes G0002, no previous original prediction rewritten.
<!-- END CANONICAL RESEARCH P-602 -->
