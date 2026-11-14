# DRAFT-006 — Creighton Bluejays at Kansas State Wildcats · NCAA Division I Men's Basketball · 10–11 November 2026

**STATUS:** `READ_ONLY_DRAFT / NOT_ISSUED / NOT_FROZEN / UNCALIBRATED_QUALITATIVE`  
**Mini context:** `research/active_minis/20261109R3NEXT.md`; cumulative local draft only; proposed `LOCAL-20261109R3NEXT-G0006` is **NOT ALLOCATED OR RESERVED**.  
**Repository:** `danisgreat/Sports-Research`, read-only `main` at `f79559b45183ca63a2ce5fc2611321975bae744f`; MDS-2026.11.10-v24.12 / CR-2026.11.10-R2 / P-2026.11.10-v24.10 / SEL-2026.10.22-v4.  
**Research observation:** 11 November 2026, Australia/Melbourne, before the official 13:10 AEDT tip-off, from dated pregame sources. This is **not** a frozen pre-start issue. **No result, in-game, or post-start statistics used.**

## A1. Event, exact contracts and timeline

- **Fixture:** Creighton Bluejays (away, Big East, 2–0) at Kansas State Wildcats (home, Big 12, 1–1); men's NCAA Division I nonconference regular season.
- **Official preview start:** Tuesday 10 November 2026, 20:10 CST, `2026-11-11T02:10Z`, Wednesday 11 November 2026, **13:10 AEDT**. Other schedule pages report 20:00 CST, so the ten-minute discrepancy is a published schedule-versus-tipoff distinction. User estimated 13:00 AEDT.
- **Venue:** Bramlage Coliseum, Manhattan, Kansas, US. Kansas State official game centre: https://www.kstatesports.com/game-center/19321 . Kansas State official game notes: https://www.kstatesports.com/news/2026/11/9/mens-basketball-k-state-hosts-creighton-in-nationally-ranked-matchup-on-fs1 .
- **Contracts:** (1) Creighton **−3.5 points**; (2) Kansas State **+3.5 points**; (3) full-game **Over 159.5** points; (4) full-game **Under 159.5** points. Full contest **including overtime** is assumed per framework BK-OT-1; regulation is 2 × 20 minutes, extra periods 5 minutes. No half-point pushes. Winner informational: Creighton vs Kansas State including OT.
- **State at research:** scheduled in official university sources. Actual jump ball and confirmed lineup were not established. Source pages marked FINAL by an unrelated score provider were **not used** for inference because they conflict with prestart wall-clock timing and the goal here is independent pregame research.

## A2. Directional assessments by supplied contract

| Exact row | Pre-event qualitative assessment | Confidence / action |
|---|---|---|
| Creighton −3.5 | Marginal lean; better early defence and rebound/turnover creation could establish a multibasket advantage | LOW; not ranked as a calibrated selection |
| Kansas State +3.5 | Real alternative; first Creighton road game, K-State home venue, prolific perimeter shooting and an experienced new coach | LOW; close-spread uncertainty |
| Over 159.5 | Needs higher-than-early-season combined efficiency or repeat of K-State's CSUN three-point conversion; viable shooting/late-foul tail | LOW |
| **Under 159.5** | **Strongest qualitative direction** from early scoring totals and lower scoring cross-match diagnostic; no confidence threshold proven | LOW-to-MODERATE qualitative only |
| Creighton game winner (informational) | Marginal Creighton lean; independent ML probability NOT_COMPUTED | LOW |
| Kansas State game winner (informational) | Plausible home upset; independent ML probability NOT_COMPUTED | LOW |

**Single directional recommendation if one must be selected:** Under 159.5 total points. **Formal selection:** `NO_STRONG_PICK / ABSTAIN` (no completed competition-specific reference distribution or independently validated p_card). The spread and total may co-win in a scenario such as Creighton 79–73 (152 total), but that score is purely illustrative, **not** a model projection.

## A3. Dated online form and true window sizes

The entire **current 2026–27 regular season** prior to this matchup contains **two completed games per team**; therefore L5, L10, L15 and L20 each have **true n=2**, not imputed n=5–20. Exhibitions and prior-season games are *not* blended into current-team windows given both coaching and roster turnover. Older-season windows need a separately reconstructed regime-conditioned appendix if the protocol's full historical coverage is to be satisfied.

| Date (venue local) | Team | Opponent | H/A | Score, first-listed team first | Combined | Provenance |
|---|---|---|---|---|---:|---|
| 2026-11-02 | Creighton | Kansas City | Home | Creighton 76–61 Kansas City | 137 | https://gocreighton.com/sports/mens-basketball/schedule/2026-27 |
| 2026-11-05 | Creighton | Le Moyne | Home | Creighton 83–55 Le Moyne | 138 | https://gocreighton.com/news/2026/11/5/hot-start-carries-mens-basketball-past-le-moyne |
| 2026-11-03 | Kansas State | South Dakota State | Home | Kansas State 66–68 South Dakota State | 134 | https://www.kstatesports.com/sports/mbball/schedule |
| 2026-11-06 | Kansas State | CSUN | Home | Kansas State 95–78 CSUN | 173 | https://www.kstatesports.com/game-center/19320 |

**Per-team overlapping current-season windows:**
- Creighton L5/L10/L15/L20 each W2–L0, n=2; points for `(76+83)/2=79.5`, against `(61+55)/2=58.0`, total `(137+138)/2=137.5`. Over 159.5: 0/2; Under: 2/2.
- Kansas State L5/L10/L15/L20 each W1–L1, n=2; points for `(66+95)/2=80.5`, against `(68+78)/2=73.0`, total `(134+173)/2=153.5`. Over 159.5: 1/2; Under: 1/2.
- Combined *four nonindependent team-games* Under 159.5 count 3/4 and Over count 1/4, descriptive only; not a binomial probability estimate and not opponent adjusted.
- **Historical H2H:** 2025-12-13 Kansas State 83–76 at Creighton; 159 total. Kansas State holds all-time series 9–8 and won previous four, but coach and personnel continuity poor; downweight. https://www.kstatesports.com/game-center/19321 .

## A4. Distribution, reference and numerical diagnostics

**Reference stage:** `NOT_EXECUTED`; no local authorised working tree with executable ML reference receipt, no `python -m ml reference tier`, no competition baseline receipt, no official card; hence no published `ANALYST_PRIMARY_V1 p_card`, no Poisson/normal/Monte Carlo run, no uncertainty interval masquerading as statistical confidence. KBL/WNBL/NBL/other basketball competition models are not transported to NCAAB. The repository `research/model_registry/ML_PROMOTIONS.csv` has only its header; no competition-specific fitted model is promoted.

**Raw scoring versus opposing allowance calculation (transparent, not a calibrated forecast):**
- Creighton descriptive scoring centre: `(79.5 scored + 73.0 Kansas State conceded)/2 = 76.25`.
- Kansas State descriptive scoring centre: `(80.5 scored + 58.0 Creighton conceded)/2 = 69.25`.
- Descriptive sum: **145.50**, margin Creighton **+7.00**. The distance from 159.5 is **14.0 points**.
- **Major limitation:** Creighton defence is based on Kansas City and Le Moyne only; Kansas State scored 95 against CSUN with a high-variance 17/41 3PT performance, while Creighton is playing on the road for the first time. Neither an established opponent-adjusted efficiency baseline nor home uplift has been estimated. This centre is a *diagnostic*, not a rankable forecast.
- An Under and Creighton cover can coexist (e.g. 79–73, total 152, margin 6); a Kansas State hot shooting/fast-paced branch can produce Over and Kansas State +3.5. They are dependent alternatives. Overtime is an explicit unresolved upside total tail, not silently excluded.
- **Baseline_P, p_card, score distribution widths, overtime frequency, covariance, possession count:** `NOT_COMPUTED / NOT_VERIFIED` for this exact league/regime. No simulation performed.

## A5. Contract-specific failure branches and sensitivity

1. **Creighton −3.5:** wins if Creighton wins by 4+ after any OT. Drivers: two early clean home wins, Enis production, more steals/defensive pressure. Failure: K-State's home perimeter conversion, Creighton first away appearance and new rotation.
2. **Kansas State +3.5:** wins on K-State win or defeat by 1–3; loses on Creighton margin 4+. Drivers: home court and Rechsteiner shooting; failure: K-State's shot-selection volatility and an early deficit from turnovers.
3. **Over 159.5:** 160+ combined. Needs fast conversion, elevated second-half pace/fouls, high 3PT or overtime. This is a plausible but not established state.
4. **Under 159.5:** ≤159 points. Supported by 137, 138 and 134 totals in three pregame matches, Creighton half-court defending and a raw 145.5 diagnostic. Main failure: K-State's 17-of-41 3-point form against CSUN, late fouling, overtime, or Creighton's early defence regressing against better competition.
5. **Winner:** slight Creighton lean; do not confuse projected winner with a successful −3.5 point cover.
6. Any correlation between the preferred Under and preferred Creighton handicap is unmeasured; don't treat as independent legs.

## A6. Expected rotations, health, coaching, conditions

**Official *probable*, not confirmed, starting five** (Kansas State game notes 9 Nov):

| Creighton | Kansas State |
|---|---|
| Austin Swartz | Brandon Rechsteiner |
| Wes Enis | Jaden Schutt |
| BJ Davis | Dez Lindsay |
| Jackson McAndrew | Isaiah Abraham |
| Oswin Erhunmwunse | Pape N'Diaye |

- **Kansas State injury:** Timo Malovec missed its first two games and is day-to-day; coach Casey Alexander's 9 November statement confirms improvement but **not game availability**. Source: https://www.kstatesports.com/news/2026/11/9/mens-basketball-alexander-players-preview-home-game-vs-creighton . An independent pre-tip active-roster check is outstanding.
- **Creighton health:** no injury confirmed from the opened official school preview. This is *not* proof of a completely healthy active roster. Game-specific bench and scratches NOT_VERIFIED.
- **Leading scorers:** Wes Enis 20.5 PPG (Creighton); Brandon Rechsteiner 21.0 PPG (Kansas State). Kansas State 17/41 from three vs CSUN, with Rechsteiner contributing 26 points. https://www.kstatesports.com/game-center/19320 .
- **Coaches:** Alan Huss first year Creighton, Casey Alexander first year Kansas State. Creighton lost long-time coach Greg McDermott and added nine players; continuity from the 2025 matchup is poor. Sources: two schools' 2026-11-07/09 previews.
- **Rest:** Creighton last played Nov 5 (four full days off); Kansas State Nov 6 (three full days off). No immediate back-to-back; no fatigue coefficient justified.
- **Venue:** Kansas State home at Bramlage Coliseum; Creighton making first 2026–27 road appearance. Location and atmosphere are plausible scenario variables but no measured numerical home modifier inserted.
- **Tempo:** season points insufficient to identify stable possessions and opponent-adjusted pace. K-State three-point volume raises variance. Do not pool NBA/WNBA or extrapolate K-State 95-point single game as stable attack.

## A7. Selection and model execution gates

| Check | Status |
|---|---|
| Competitor identity & venue | VERIFIED in official team game previews |
| Official schedule time | VERIFIED (8:10 p.m. CT), estimated time discrepancy noted |
| Full-game rules/OT convention | NCAA men's 40-minute regulation, overtime-inclusive BK-OT-1; exact operator-specific terms not supplied |
| Current-season scores | VERIFIED 2 of 2 each team; four dated rows |
| Last 5/10/15/20 of same current roster | Only n=2 available; historical regime windows not reconstructed |
| Probable starters | Official pregame preview, not game-confirmed |
| Active bench, scratches, Malovec final status | UNRESOLVED |
| Exact team possessions, efficiency, opponent adjustment | NOT_COMPUTED |
| Official league-only reference run and reference receipt | NOT_EXECUTED |
| Analyst p_card, covariance, OT branches, Monte Carlo | NOT_COMPUTED |
| PICKS_V2 lint, freeze, learning log | NOT_EXECUTED |
| Issuing-writer lease and authorized repository append | NOT_HELD / NOT_EXECUTED |
| GitHub mutation | NONE; standing READ-ONLY mode |

**Disposition:** `NO_STRONG_PICK / ABSTAIN`. Single research-only direction: **Under 159.5**, with meaningful three-point/OT/first-road-game risk. **Selection certification:** NONE.

## A8. Source receipt and atomic provenance

Official and timely *pregame* sources; no odds or market predictor reports used as anchors:

1. Kansas State game notes, **published 9 November 2026**, start, venue, probable fives, 2026–27 averages, H2H, coaching: https://www.kstatesports.com/news/2026/11/9/mens-basketball-k-state-hosts-creighton-in-nationally-ranked-matchup-on-fs1 .
2. Kansas State coach press conference summary, **published 9 November**, Malovec day-to-day and opponent assessment: https://www.kstatesports.com/news/2026/11/9/mens-basketball-alexander-players-preview-home-game-vs-creighton .
3. Kansas State game centre, fixture and 2025 H2H: https://www.kstatesports.com/game-center/19321 .
4. Kansas State completed CSUN game centre, Nov 6, box and team shot counts: https://www.kstatesports.com/game-center/19320 .
5. Creighton official schedule, Kansas City 76–61 and Le Moyne 83–55: https://gocreighton.com/sports/mens-basketball/schedule/2026-27 .
6. Creighton Le Moyne recap published Nov 5, box and period scores: https://gocreighton.com/news/2026/11/5/hot-start-carries-mens-basketball-past-le-moyne .
7. Creighton pregame notes published Nov 7, coaches and first away game: https://d2560u4h06m0te.cloudfront.net/news/2026/11/7/mens-basketball-visits-kansas-state-on-tuesday .

**Source access:** no `python -m ml source-audit` tool execution and no archived downloaded source packet. Public web reads completed through web search for this analysis. Publication dates are explicitly given where available; exact underlying press release edit times and source known-at receipts have not been archived. No postgame source used to infer the result. Retrieval around 11 November 2026 12:51–12:55 AEDT; exact per-item retrieval timestamps not persisted. Parent repos/issuer remain read-only.

## A9. Research completion matrix, delivery and custody

| Coverage field | Status / exact missingness |
|---|---|
| A1 fixture/time/venue/contracts | DONE, pregame verified |
| A2 all supplied contract directions | DONE, qualitative; paired probabilities not available |
| A3 true current-season rolling windows | DONE at actual n=2; prior-season L5/L10/L15/L20 NOT_RECONSTRUCTED |
| A4 model/reference/expected distribution | PARTIAL: transparent 145.5 diagnostic; no executable reference or scores SD |
| A5 coherent contract-specific mechanisms | DONE qualitative; no normalized joint probability model |
| A6 health/starter/pace/rest | PARTIAL: probable fives and Malovec press report, no confirmed game five/bench/efficiency |
| A7 lint/freeze/scoring gates | NOT_EXECUTED |
| A8 provenance | PARTIAL: 7 official source URLs, unarchived exact source times/source-audit |
| A9 readback, writer custody, commitment | WORKING_COPY_ONLY; local file readback feasible, GitHub untouched |

**Classification:** `PARTIAL_RESEARCH / UNCALIBRATED_QUALITATIVE / NOT_ISSUED`, not performance eligible. The proposed draft key is for local organization **only**. For any later authorized import, confirm live state, duplicate identity, the published mini's writer lease and no outcome exposure, then run competition reference, source audits and all required freeze/linter and learning-log processes before any eligible issuance. This draft cannot be converted retrospectively into a frozen pre-tip forecast.
