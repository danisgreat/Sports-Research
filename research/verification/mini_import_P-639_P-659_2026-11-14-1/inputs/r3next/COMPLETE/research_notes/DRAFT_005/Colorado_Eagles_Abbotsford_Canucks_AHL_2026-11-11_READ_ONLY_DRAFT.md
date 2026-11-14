# READ_ONLY_DRAFT / NOT_ISSUED — Colorado Eagles @ Abbotsford Canucks, AHL 2026-11-11 AEDT

**Research receipt:** 2026-11-11T12:42:40+11:00. Pre-game web research for the first fixture in a **two-game Abbotsford home set**. Not a frozen official card; no model release/reference, source-audit CLI, card lint, Monte Carlo, pregame freeze or repo write has been run. All goal and score data below predate the fixture. This note is **UNCALIBRATED_QUALITATIVE / NO_STRONG_PICK** for official scoring.

**Repository context:** `danisgreat/Sports-Research` pinned published main `f79559b45183ca63a2ce5fc2611321975bae744f`, MDS-2026.11.10-v24.12 / CR-2026.11.10-R2 / P-2026.11.10-v24.10 / SCV-2026.10.22-v12 / SEL-2026.10.22-v4; published active `research/active_minis/20261109R3NEXT.md` is ACTIVE / EMPTY. This document is being inserted into a **local working copy with 4 earlier research drafts**. Proposed slot `DRAFT-005` / `LOCAL-20261109R3NEXT-G0005`, **NOT ALLOCATED**. No canonical P-ID used.

## Decision block — uncalibrated research only

| Requested contract | Directional assessment | Confidence / status |
|---|---|---|
| Colorado Eagles ML | Opposing direction; competitive goalie and defense case | LOW / UNCALIBRATED_QUALITATIVE |
| Abbotsford Canucks ML | **Preferred ML side**, home form + territorial-play advantage | LOW–MODERATE / UNCALIBRATED_QUALITATIVE |
| Over 5.5 goals | H2H 7 goals in both; Abbotsford season 6.17 combined / real scoring upside | LOW / UNCALIBRATED_QUALITATIVE |
| Under 5.5 goals | **Very slight total lean**, goalie strength and Colorado low recent totals | VERY LOW / UNCALIBRATED_QUALITATIVE |

**Single directional selection:** Abbotsford Canucks ML, **not** a certified or ≥0.65 confidence selection. **Framework disposition:** `NO_STRONG_PICK / ABSTAIN` pending verified goalies, full dressed rosters, operator settlement terms and the baseline-reference execution. No claimed `p_card`, simulation, profitable edge or release probability.

## A1 — Event identity, schedule, timing and source custody

- League: American Hockey League (AHL), 2026–27 regular season, game 1 of Abbotsford–Colorado home doubleheader; official league fixture native ID **1029282** (next-day rematch `1029289` is a separate event; do not merge).
- Teams: Colorado Eagles (away) at Abbotsford Canucks (home), Rogers Forum, Abbotsford, BC, Canada.
- **Authoritative venue-local scheduled start:** 2026-11-10 19:00 America/Vancouver, **PST UTC−08**, which is **2026-11-11 03:00 UTC = 2026-11-11 14:00 Australia/Melbourne (AEDT UTC+11)**. The owner's `11 Nov 12:00 AEDT` is two hours too early. Some structured providers render `02:00 UTC` or `PDT` in November; these are inconsistent with the venue's 7 pm clock after DST ended and are not chosen as authoritative.
- Official club schedule (7 pm): https://abbotsford.canucks.com/tickets/singlegame?month=All ; Colorado club schedule lists `Nov 10 8:00PM` in its Mountain-zone schedule: https://www.coloradoeagles.com/games . Official AHL matchup: https://theahl.com/stats/game-center/1029282 . Independent preview: https://insidetherink.com/ahl-game-preview-colorado-eagles-at-abbotsford-canucks-with-projected-lines-11-10-2026/ .
- Estimated start remains estimated; actual first puck-drop **NOT_VERIFIED**. Snapshot excludes in-play and final results. No post-start data are used to adjust the direction. If actual issue occurs after verified first play, label `POST_START_ISSUE` rather than pregame regardless of the evidence cutoff.

## A2 — Exact contract definitions and action gates

| Raw user contract | Unit | Intended scope | Official-status gate |
|---|---|---|---|
| Eagles ML | Match winner | Entire match including AHL regular-season OT/SO, conditional on operator | Operator's exact match-winning and void terms NOT_VERIFIED |
| Canucks ML | Match winner | Complementary entire-match endpoint | Same unknown operator terms |
| Over 5.5 | Total goals ≥ 6 | Full match, OT included; shootout goal counting varies by operator | UNKNOWN_DEFINITION until exact operator rule frozen |
| Under 5.5 | Total goals ≤ 5 | Complementary total | Same unknown operator terms |

There is no drawn outcome in an AHL regular-season **eventual winner**, but a 60-minute score can be tied; the eventual winner must be reconciled with the permitted OT/SO and any shootout-final-score rule. Empty-net and overtime branches are not ignored. No official operator was supplied and there is no derived numeric `W/P/L/V` mass.

## A3 — Complete current-season prior games, pre-event only; online L5/L10/L15/L20

**Abbotsford Canucks: 12 completed league games (through Nov 7)**. Dates are local team schedule dates; official source and independent scoreboard records: https://www.ahldashboard.com/teams/1168?tab=schedule ; https://omnihockey.com/teams/ahl-440/schedule ; https://www.hockey.com/ahl/teams/abbotsford-canucks/schedule .

| Date | Opponent | Goals for | Against | Listed final total | Decision |
|---|---|---:|---:|---:|---|
| 2026-10-02 | @ CGY | 2 | 4 | 6 | L |
| 2026-10-03 | @ CGY | 2 | 4 | 6 | L |
| 2026-10-09 | @ COL | 3 | 4 | 7 | OTL/SO |
| 2026-10-10 | @ COL | 4 | 3 | 7 | W |
| 2026-10-17 | vs CV | 7 | 3 | 10 | W |
| 2026-10-18 | vs CV | 5 | 4 | 9 | W/SO |
| 2026-10-24 | vs CGY | 3 | 1 | 4 | W |
| 2026-10-25 | vs CGY | 4 | 2 | 6 | W |
| 2026-10-28 | @ SJ | 5 | 2 | 7 | W |
| 2026-10-30 | @ BAK | 5 | 1 | 6 | W |
| 2026-11-06 | vs ONT | 2 | 1 | 3 | W |
| 2026-11-07 | vs ONT | 0 | 3 | 3 | L |

**Colorado Eagles: 14 completed league games (through Nov 7)**. Source: https://www.ahldashboard.com/teams/1176?tab=schedule ; official https://www.coloradoeagles.com/games ; https://www.hockey.com/ahl/teams/colorado-eagles/schedule .

| Date | Opponent | Goals for | Against | Listed final total | Decision |
|---|---|---:|---:|---:|---|
| 2026-10-03 | @ TUC | 2 | 0 | 2 | W |
| 2026-10-04 | @ TUC | 5 | 3 | 8 | W |
| 2026-10-09 | vs ABB | 4 | 3 | 7 | W/SO |
| 2026-10-10 | vs ABB | 3 | 4 | 7 | L |
| 2026-10-16 | @ MIL | 4 | 1 | 5 | W |
| 2026-10-17 | @ MIL | 1 | 2 | 3 | OTL |
| 2026-10-23 | vs BAK | 4 | 1 | 5 | W |
| 2026-10-24 | vs BAK | 1 | 4 | 5 | L |
| 2026-10-27 | vs CLT | 3 | 6 | 9 | L |
| 2026-10-28 | vs CLT | 3 | 0 | 3 | W |
| 2026-11-01 | @ SD | 2 | 3 | 5 | OTL/SO |
| 2026-11-04 | @ CV | 1 | 2 | 3 | L |
| 2026-11-06 | vs CGY | 1 | 2 | 3 | L |
| 2026-11-07 | vs CGY | 6 | 4 | 10 | W |

**Over 5.5 and scored-form windows** (over = 6 or more in listed final score; shootout game-final accounting noted below). Four windows are overlapping, not independent observations.

| Window | ABB true n | ABB wins | ABB GF/g | ABB GA/g | ABB total/g | ABB O5.5 | COL true n | COL wins | COL GF/g | COL GA/g | COL total/g | COL O5.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| L5 | 5 | 4 | 3.20 | 1.80 | 5.00 | 3/5 | 5 | 2 | 2.60 | 2.20 | 4.80 | 1/5 |
| L10 | 10 | 8 | 3.80 | 2.40 | 6.20 | 7/10 | 10 | 4 | 2.60 | 2.50 | 5.10 | 2/10 |
| L15 | 12 | 8 | 3.50 | 2.67 | 6.17 | 9/12 | 14 | 7 | 2.86 | 2.50 | 5.36 | 5/14 |
| L20 | 12 | 8 | 3.50 | 2.67 | 6.17 | 9/12 | 14 | 7 | 2.86 | 2.50 | 5.36 | 5/14 |

Season facts: ABB 42 goals for/32 against in 12, total 74/12=6.1667, home 5–1; COL 40/35 in 14, total 75/14=5.3571, away 3–3. The ABB 10/9 shootout loss is displayed 3–4 and COL win 4–3: awarded shootout final score contributes a goal on the structured scoreboards. Operator markets may count shootout separately, so their exact total settlement must be verified. L15 and L20 have *true n* only 12 ABB, 14 COL; these windows **are not fabricated up to n=15/20**. Names/dates and first-period/second-period splits remain out of scope of these summaries.

## A4 — Roster, goalie, eligibility, availability and travel

**Projections, NOT confirmed dressed lineup:**
- COL forwards: Beckman–Brindley–Nielsen; Makar–Wise–DiMarsico; Jedlička–Prishchepov–Gay; Turcotte–Connors–Chiasson. Defence: Gagne–Middleton, Fensore–Behrens, Aamodt–Stjernberg. Preview goaltenders: **Ilya Nabokov; Trent Miner**.
- ABB forwards: Lind–Cootes–Fix-Wolansky; Berard–Mueller–Patterson; Alriksson–Wouters–Stienburg; Ravinskis–Safonov–Brimmer. Defence: Mynio–Clayton, Schuldt–White, Kudryavtsev–Thompson. Preview goaltenders **Nikita Tolopilo; Ty Young**.
- Projections: https://insidetherink.com/ahl-game-preview-colorado-eagles-at-abbotsford-canucks-with-projected-lines-11-10-2026/ ; official exact match sheet not yet available for pregame verification, so **STARTERS_PROJECTED / SCRATCHES_NOT_VERIFIED**.
- Goalie Nabokov: 2026–27 pregame snapshot **8 games / 2.11 GAA / .929 SV%**. Independent 8GP record: https://insidetherink.com/stats/ahl/players/ilya-nabokov-11118/ and https://www.eliteprospects.com/team/894/colorado-eagles/stats/2026-2027?league=ahl&tab=goalies .
- Goalie Tolopilo: current 8-game snapshot **2.12 GAA / .915 SV%** from club roster and secondary game log: https://abbotsford.canucks.com/team/roster/9983?view=Stats and https://insidetherink.com/stats/ahl/players/nikita-tolopilo-9983/ . The AHL individual player page and an AHL Dashboard player cache still showed **6GP, 2.48/.905**; report the timestamped mismatch without treating the stale data as zero or definitive. Official team roster/other stats corroborate 8GP but game-day start remains unconfirmed.
- ABB backup Ty Young: 4 games, 2.72 GAA / .908 SV%, via https://www.eliteprospects.com/team/3375/abbotsford-canucks/stats/2026-2027?tab=goalies . COL backup Trent Miner: secondary roster flags him injured, but current official medical eligibility status **NOT_VERIFIED**. Do not assert healthy or out solely from this flag.
- Recent transactions: Gavin Brindley returned on loan from NHL Colorado **1 Nov**, Taylor Makar returned **26 Oct**, per official AHL transactions https://theahl.com/stats/transactions/419/94 . Do not confuse Colorado Eagles with NHL Colorado Avalanche; do not attribute NHL absences to this AHL roster without assignment evidence.
- Workload: COL last played home vs Calgary on Sat 7 Nov, ABB last home vs Ontario on Sat 7 Nov. Neither on a back-to-back; COL travels from Colorado to British Columbia, ABB remains home. Flight specifics and acclimation **NOT_VERIFIED**. ABB is slated for another home game vs COL Nov 11; today's game is not the second leg.
- Injury/illness/suspension and actual bench status for all players **NOT_VERIFIED**; no reliable verified full medical report found. **Not** equivalent to healthy.

## A5 — Offence, defence, xG, special teams, baseline arithmetic and total logic

Season actual rates (team A at Abbotsford, team B Colorado):
- ABB goals scored=42/12=**3.5000**; conceded=32/12=**2.6667**. COL scored=40/14=**2.8571**; conceded=35/14=**2.5000**.
- **Plain opponent cross-matched actual-goal diagnostic:** projected ABB = (3.5000 + 2.5000)/2=**3.0000**; COL=(2.8571+2.6667)/2=**2.7619**; combined=**5.7619**, unadjusted. This is not an approved competition reference, and ignores opponent mix, goalies and outliers.
- **Expected-goals-strength diagnostic:** ABB xGF/60=2.85, COL xGA/60=2.90 -> mean ABB 2.875; COL xGF/60=2.65, ABB xGA/60=2.60 -> mean COL 2.625; combined **5.500**. This is an unadjusted average of reported xG inputs, **not** a score-grid, qualified model, or a forecast probability. Source: https://www.ahldashboard.com/teams/1168?tab=stats ; https://www.ahldashboard.com/teams/1176?tab=stats .
- Expected-goals-share: ABB **52.27%**, COL **47.74%**. Scoring-chance share ABB **53.14%**, COL **45.45%** (different share definitions/sources, so not constrained to sum to exactly 100%).
- Special teams: ABB PP **7/45=15.56%**, PK **33/39=84.62%**; COL PP **9/64=14.06%**, PK **53/61=86.89%**. Both PP rates modest; COL PK more effective, limiting ABB special-team upside. Special-team opportunity volume for this exact game NOT_VERIFIED; do not apply a fictional fixed goal shift.
- League-wide current AHL summary gives **5.83 goals/game in regulation**; the specific league/period cohort, full-game shootout-awarded goals and data lineage must be reconciled before a model prior. https://pitchlabstats.com/hockey-league/ahl .
- The 5.5 total sits between several close diagnostics (5.50 xG, 5.76 cross-match, 5.83 league). The near-horizon combined totals (COL L5 4.8, ABB L5 5.0) lean below the line but are a small, overlapping sample. ***Neither a robust Over nor a robust Under***. OT/SO and empty-net tails alter total 5.5 behaviour.
- **Numerical reference stage:** `python -m ml reference tier --competition AHL` and `reference run` NOT_EXECUTED; league-only baseline parameters NOT_FROZEN; no `ANALYST_PRIMARY_V1` p_card, code score grid, adjustment ledger, simulation seed/N, Monte Carlo error, game-level posterior or adjusted expected margin calculated. Do not claim them.

## A6 — H2H, score-state dependence and rules

Two prior **2026–27 head-to-head** matches (Colorado home): **9 October COL 4–3 ABB (shootout)**, **10 October ABB 4–3 COL (regulation)**. Both ended with seven in listed final score. Independent corroboration: https://www.coloradoeagles.com/news/detail/eagles-roar-back-to-defeat-abbotsford-4-3-in-shootout and https://www.coloradoeagles.com/news/detail/eagles-come-up-short-in-4-3-loss-to-abbotsford , plus schedules above.

Winner has mutually exclusive home and away control / regulation-draw-to-OT branches; either team can win quickly or via OT. Total plausible paths include 3–2 ABB (ABB ML, Under 5.5), 4–2 ABB (ABB ML, Over 5.5), 3–2 COL (COL ML, Under 5.5), and 4–3 either team (Over 5.5). The moneyline and total are **not statistically independent**: trailing-team goalie pulls, empty-net goals, score state and OT/SO create correlated tails. Goals from shootout settlement depend on actual operator convention.

## A7 — Candidate comparison and recommendation gates

| Contract | Supporting facts | Principal kill paths | Assessment |
|---|---|---|---|
| ABB ML | 8–3–1 season, 5–1 home, L5 4 wins, 52.27% xGF share, relative rest and territory advantage | COL Nabokov .929, Colorado 3–3 away, H2H tied, ABB last game shutout, roster uncertainty | **Single directional selection, LOW–MODERATE** |
| COL ML | Nabokov season goalie edge, strong 86.9% PK, offense led by Beckman/Brindley/Nielsen, Oct 9 H2H victory | ABB 5–1 home, 3.5 GF/game, defensive xG edge, recent dominance | Credible opposing ML, no strong pick |
| Over 5.5 | Both H2H 7, ABB L10 total 6.2, league total >5.5 | COL L10 5.1, projected good goalies, ABB last 2 totals 3 | Low |
| Under 5.5 | COL 8 of last 10 listed finals ≤5; both projected goalies strong, PP conversion modest, xG diagnostic ≈5.5 | ABB 7/10 L10 over, ABB season 6.17, empty net / OT, H2H 7 twice | **Very slight lean, very low confidence** |

**Rank and abstain:** NO_STRONG_PICK / ABSTAIN (no valid numerical reference, operator definition or frozen confirmed goalies; no claimed probability ≥0.65). Most defensible *directional* side = **Abbotsford Canucks ML**, preferred total = **Under 5.5** but **not recommended as a strong second pick**. Distinguish this from a high-confidence or executed-model forecast. No odds, bets or price-based information used.

## A8 — Source and evidence register / uncertainty

| Field | URL / evidence | Limitations |
|---|---|---|
| Official fixture / native ID | https://theahl.com/stats/game-center/1029282 ; https://theahl.com/stats/game-center | Page shows identifier/schedule but no finalized pregame starting-goalie sheet on checked view |
| Venue clock / timezone | https://abbotsford.canucks.com/tickets/singlegame?month=All ; https://www.coloradoeagles.com/games ; https://www.ticketmaster.ca/abbotsford-canucks-vs-colorado-eagles-abbotsford-british-columbia-11-10-2026/event/11006518E8530EF3 | Some third parties render Nov UTC hour wrongly, especially PDT vs PST |
| L5/L10/L15/L20 true-n histories | https://www.ahldashboard.com/teams/1168?tab=schedule ; https://www.ahldashboard.com/teams/1176?tab=schedule ; independent official Colorado club scores | Rolling windows fully enumerated; local dates from first schedule; opponent adjustment absent |
| Team strength & special teams | https://www.ahldashboard.com/teams/1168?tab=stats ; https://www.ahldashboard.com/teams/1176?tab=stats ; https://pitchlabstats.com/hockey-league/ahl | xG model lineage not independently validated; team game counts small |
| Projected players / goalies | https://insidetherink.com/ahl-game-preview-colorado-eagles-at-abbotsford-canucks-with-projected-lines-11-10-2026/ | **Projected**, not league-confirmed active/dressed lists |
| 8-GP goalie statistics | https://abbotsford.canucks.com/team/roster/9983?view=Stats ; https://www.eliteprospects.com/team/3375/abbotsford-canucks/stats/2026-2027?tab=goalies ; https://www.eliteprospects.com/team/894/colorado-eagles/stats/2026-2027?league=ahl&tab=goalies | AHL Tolopilo direct player page stale at 6 GP; no certified exact-match starts |
| October H2H | https://www.coloradoeagles.com/news/detail/eagles-roar-back-to-defeat-abbotsford-4-3-in-shootout ; https://www.coloradoeagles.com/news/detail/eagles-come-up-short-in-4-3-loss-to-abbotsford | Prior games same season but home sides reversed; weak n2 |
| Recent player transactions | https://theahl.com/stats/transactions/419/94 | Official Colorado transactions through 1 Nov; further pregame movements not verified |
| Source access / rule screening | Repo `SOURCES.md` and `PREGAME_SOURCES.csv` entry marks theahl.com/stats/standings ALLOWED from 8 Nov. Individual opened URLs not given a fresh `python -m ml source-audit` | **SOURCE_AUDIT_NOT_EXECUTED**, so no newly claimed URL verdict; do not retry any refused source through a workaround |

Evidence retrieved for this session on **11 November 2026**, before the 14:00 AEDT official schedule start as reported by the tool context; exact source publication/update times are often unavailable, hence `KNOWN_AT_UNVERIFIED` for decisive facts lacking a dated original. No claimed full two-source independence for each field. No future retry task or ongoing monitor scheduled.

## A9 — Research completion and issuance gates

| Gate | Status |
|---|---|
| Fixture teams/league/home/away, official native ID | VERIFIED from AHL and both clubs |
| Precise venue-local time and AEDT | VERIFIED from 19:00 PST conversion; conflicting 02:00 UTC structured pages excluded |
| Actual first puck drop | NOT_VERIFIED |
| L5/L10/L15/L20 true n, all available games | COMPUTED from dated histories (n12 ABB/n14 COL ceilings) |
| H2H two earlier same-season games | VERIFIED |
| Full selected skaters / scratches for this game | PROJECTED_ONLY / NOT_VERIFIED |
| Actual starting goalies | PROJECTED_ONLY / NOT_VERIFIED |
| Medical absences and replacement validity | NOT_VERIFIED; no inference of healthy |
| Special teams, xG, simple scoring diagnostics | COMPUTED/DISCLOSED from sources, not a model |
| Expected-score grid, OT/SO, pull-empty-net branches | NOT_COMPUTED |
| League reference model tier / baseline / promotion | NOT_EXECUTED |
| Adjustment ledger and independent calibration | NOT_EXECUTED / NOT_QUALIFIED |
| Operator exact ML and 5.5 SO/OT action rules | UNKNOWN_DEFINITION |
| Numerical W/P/L probabilities on each contract | NOT_COMPUTED |
| Approved CLI source-audit per opened URL | NOT_EXECUTED |
| PICKS_V2 / card lint / learning-log / game freeze | NOT_EXECUTED |
| Official mini writer authorization / issued local event key | NOT_HELD / NOT_ALLOCATED |
| GitHub commit and push | NOT_EXECUTED; STRICT READ_ONLY |
| Research completion | PARTIAL_RESEARCH / READ_ONLY_DRAFT / NOT_ISSUED |

**Custody and future reconciliation:** This note belongs in the user's already-existing local **draft working copy** as `DRAFT-005`, with a proposed G0005 *only*. The original published `mini-log-10` footer remains unchanged and records 0 officially issued cards. On any future authorized reconciliation, the issuing repository agent must re-read latest active mini, check live identity/lease and time status, inspect both selected goalies and the complete dressed lists, run required reference/source checks, and allocate or remap a local key on that authorized path. Never use this draft as an immutable published prediction or input to certified scoring.
