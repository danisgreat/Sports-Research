# READ_ONLY_DRAFT / NOT_ISSUED — Perth Lynx vs Bendigo Spirit

**Fixture:** WNBL 2026–27 Round 4, Perth Lynx (home) v Bendigo Spirit (away). 10 November 2026, 18:00 AWST = 21:00 AEDT = 10:00 UTC. Perth High Performance Centre. **Status at research:** scheduled; actual first play NOT_VERIFIED. The game may be delayed.

**Requested complete-match contracts including any overtime (BK-OT-1):** Perth −10.5 points, Bendigo +10.5 points, Over 167.5 points, Under 167.5 points. Moneyline probabilities for both sides requested under REQ-v4 even when no ML line appears.

**Authority check:** GitHub repository `danisgreat/Sports-Research`, published `main` HEAD `f79559b45183ca63a2ce5fc2611321975bae744f`. Read-only connector verification, not a working-tree checkout. MDS-2026.11.10-v24.12; CR-2026.11.10-R2; P-2026.11.10-v24.10; SCV-2026.10.22-v12; SEL-2026.10.22-v4. Relevant controls: `CORE.md` §§1–7, `CURRENT_STATE.md` generated state, `research/prompts/1_GAME_CARD.md`, `research/prompts/1_sports/BASKETBALL.md`, `RULES_BASKETBALL.md` §§0–8, `PARAMETERS.md` Part A, `GAME_REQUEST_TEMPLATE.md` §1b, `RESEARCH_PROTOCOL.md` Part A, `CARD_AND_LOG_TEMPLATES.md` §§2–3 and existing `research/active_minis/20261109R3NEXT.md`. The repository reports next local key `LOCAL-20261109R3NEXT-G0001` and next canonical number P639, but **neither was allocated or reserved in this read-only draft**. Existing writer lease prevents an unauthorized append; existing mini was not modified. Model registry `research/model_registry/ML_PROMOTIONS.csv` has header only, no promoted competition.

**Disposition:** independent web research performed; analyst model **not executed** in repository; no reference tier command, source-audit command, ledger append, freeze, Monte Carlo, simulation, commit, push, canonical import, or settlement. Quantities below are independently calculated **unqualified illustrative shadow diagnostics** from an explicitly defined simplified approximation, **not** an issued `p_card` or a calibrated probability. Overall `INFORMATION_INCOMPLETE` and `READ_ONLY_DRAFT / NOT_ISSUED`.

## Decision summary

- **Likely winner:** Perth Lynx, direction supported by stronger W–L record and home court, but exact official model probability `NOT_ESTIMATED`.
- **Highest indicative contract:** Bendigo Spirit **+10.5**, *tentative, low-to-medium confidence*. The unqualified shrunk-scores diagnostic gives ~61.6% cover versus Perth −10.5 ~38.4%. This is **not a certified success probability**; it is highly sensitive to Bendigo's final active roster.
- **Total 167.5:** **no reliable side**. The simple current-season diagnostic gives Over ~55.2% / Under ~44.8%, while six prior H2Hs all finished Under and a plausible Bendigo availability reduction reverses the Over lean. **Abstain** for a strong total selection.
- **Formal Rank-1 status:** `NOT_ASSESSABLE / NO_STRONG_PICK`; no issued ranks, no pre-event frozen card.

## A1. Identity, timing, event state

The official club fixture confirms Tuesday 10 November at 18:00 Perth time: https://perthlynx.wnbl.com.au/news/wnbl27-fixture-drop-perth-lynx-set-to-ignite-perth-hpc. The league Round 4 preview confirms 21:00 AEDT: https://www.wnbl.com.au/news/crunch-time-the-key-storylines-leading-into-round-4. A same-day preview contains an apparently erroneous date in its matchup header (17 October), conflicting with its 10 November title; do not use that header over the actual fixture. https://www.wnbl.com.au/news/how-to-watch-talking-points-perth-v-bendigo.

Actual confirmed starters, active bench, coach rotations, verified first play, and operator-specific markets are NOT_VERIFIED. Indoor FIBA-style 40-minute game; include five-minute overtime periods under the user's BK-OT-1 contract convention, but exact overtime transition probability is not estimated here.

## A2. Frozen exact supplied propositions

| Contract | Win condition (including overtime) | Diagnostic assessment | Primary `p_card` |
|---|---|---|---|
| Perth −10.5 | Perth final margin >=11 | Outsized line relative to shrunk mean | NOT_ESTIMATED |
| Bendigo +10.5 | Perth final margin <=10 | Tentative lean; fragile to absences | NOT_ESTIMATED |
| Over 167.5 | Final points >=168 | Slight conditional Over in base diagnostic; no strong edge | NOT_ESTIMATED |
| Under 167.5 | Final points <=167 | Six recent prior H2Hs support; current season total rates oppose | NOT_ESTIMATED |
| Perth ML (informational) | Perth wins | Qualitative favourite | NOT_ESTIMATED |
| Bendigo ML (informational) | Bendigo wins | Plausible upset path if game remains close | NOT_ESTIMATED |

All half-point spread and total contracts have no integer push under completed-score settlement. Opposing handicap outcomes are complements; Over/Under are complements. Void/abandonment/operator-specific provisions remain UNKNOWN; a postponed fixture is not automatically VOID.

## A3. Evidence, availability and dated historical inputs

### Pre-event 2026–27 results (exclude preseason and future fixtures)

| Side | Date | Opponent | Team | Opponent | Combined | Result |
|---|---|---|---:|---:|---:|---|
| Perth | 2026-10-17 | Townsville | 86 | 83 | 169 | W |
| Perth | 2026-10-24 | Adelaide | 90 | 82 | 172 | W |
| Perth | 2026-11-03 | Townsville | 86 | 99 | 185 | L |
| Bendigo | 2026-10-17 | UC Capitals | 92 | 94 | 186 | L |
| Bendigo | 2026-10-27 | Townsville | 68 | 91 | 159 | L |
| Bendigo | 2026-11-02 | Geelong | 70 | 77 | 147 | L |
| Bendigo | 2026-11-07 | UC Capitals | 83 | 97 | 180 | L |

Main source: https://schedule.nbl.com.au/schedule-v2/wnbl and https://api.thesportsdb.com/season/5113-australian-wnbl/2026-2027. Specific supporting club match story: https://perthlynx.wnbl.com.au/news/lynx-pounce-to-hand-lightning-third-straight-defeat; and for Nov 7 https://www.wnbl.com.au/news/puoch-celebrates-100th-game-in-capitals-victory-over-spirit.

### Computed scoring form windows

**Current season**, Perth n=3: 87.33 scored, 88.00 conceded, 175.33 total, 2–1. Bendigo n=4: 78.25 scored, 89.75 conceded, 168.00 total, 0–4. Small samples and opponent imbalance preclude stable pace/efficiency inference.

The following rolling windows bridge the end of 2025–26 and the beginning of 2026–27, so they are **historical only**, not interchangeable rosters or inputs to the current score centre. Completed finals included; September preseason excluded. Source for 2025–26 regular scores: https://fixturedownload.com/results/wnbl-2025/perth-lynx and https://fixturedownload.com/results/wnbl-2025/bendigo-spirit; postseason: https://www.thesportsdb.com/season/5113-australian-wnbl/2025-2026 and https://www.nbl.com.au/news/townsville-edge-perth-to-claim-wnbl26-championship.

| Side | Window | True n | Scored PG | Allowed PG | Wins |
|---|---|---:|---:|---:|---:|
| Perth | L5 | 5 | 89.20 | 92.00 | 2 |
| Perth | L10 | 10 | 92.00 | 84.70 | 7 |
| Perth | L15 | 15 | 87.40 | 80.60 | 10 |
| Perth | L20 | 20 | 89.55 | 78.70 | 15 |
| Bendigo | L5 | 5 | 77.60 | 88.00 | 0 |
| Bendigo | L10 | 10 | 74.40 | 85.10 | 1 |
| Bendigo | L15 | 15 | 77.53 | 83.07 | 4 |
| Bendigo | L20 | 20 | 77.65 | 78.45 | 9 |

H2H, Nov 2025–Feb 2026, chronological: Perth 79–64 Bendigo; Bendigo 87–58 Perth; Perth 85–81 Bendigo; Bendigo 64–88 Perth; Perth 86–76 Bendigo; Bendigo 75–81 Perth. Perth 5–1, mean Perth margin +5.0, six totals 143,145,166,152,162,156 (mean 154; Under 167.5 6/6). These are roster-incompatible historical observations, not six new independent predictive features. Historical cross-checks: https://www.wnbl.com.au/news/perth-lynx-dampen-bendigo-spirit and https://bendigospirit.wnbl.com.au/news/semi-final-game-two-preview.

### Player status / projected roles (not confirmed starters)

**Perth:** Georgia Amoore (primary guard), Anneli Maley (frontcourt/rebounding), Haley Peters, Alex Ciabattoni, Steph Gorman, Teonni Key and Teige Morrell in the projected rotation. Sami Whitcomb **season-out with knee injury** according to club-statement tracker, although the WNBL's current-game preview says "no injuries listed" (the latter evidently does not catalogue all longer-term squad absences). Against Townsville on Nov 3, Amoore 20 points/8 assists in 37:14; Maley 19 points/11 rebounds in 32:45; Key 16 points in 25:24. https://www.basketball.com.au/games/townsville-fire-v-perth-lynx-women-03-11-2026; https://www.basketball.com.au/news/wnbl-injury-report.

**Bendigo:** Expected contributors Jade Melbourne (creator), Kelsey Griffin, Marianna Tolo (reported minutes management following Achilles recovery), Casey Samuels, Georgia Booth, Olivia Pollerd and Mia Harvey. The WNBL November 10 preview lists **Isobel Borlase (WNBA commitments), Catherine MacGregor (knee), Kelsey Rees (ankle), Kelly Wilson (personal reasons), Abbey Wehrung (pregnant policy)** as out. Earlier injury-tracker statuses for Wilson and Wehrung disagree. Particularly, the WNBL's Nov 7 match report explicitly records Wehrung's three fourth-quarter three-pointers only three days before this game; status change or data error **unresolved**, and no inference from her previous appearance to tonight's participation is authorized. Olivia Olechnowicz's back issue shows a Round 4 return target but not a verified active designation. Melbourne posted 24 points/6 rebounds/6 assists in 35:50 in Nov 7 box-score evidence, and Pollerd 16/7 in 26:11. https://www.wnbl.com.au/news/how-to-watch-talking-points-perth-v-bendigo; https://www.wnbl.com.au/news/puoch-celebrates-100th-game-in-capitals-victory-over-spirit; https://www.basketball.com.au/news/wnbl-injury-report; https://www.basketball.com.au/games/bendigo-spirit-v-uc-capitals-women-07-11-2026.

**Starting five / reserve bench:** NO_CONFIRMED_GAME_SPECIFIC_RELEASE. Two projected Perth lineups disagree about Gorman/Ciabattoni and Morrell/Key. No trustworthy minutes distribution or closing-five probability available for the exact game. Source timestamps are page publication dates where present; actual original issue/retrieval/roster timestamps for all fields are not proven. Roster uncertainty **must not be collapsed into confirmed out/available minutes**.

## A4. Arithmetic — independent illustrative diagnostic, not repository model execution

Current team points from first four/three results and available nine-team 2026–27 league standings were independently reconciled. The complete indexed standings snapshot indicated cumulative WNBL points-for 3,434 across 42 team-games = 21 fixtures, league mean total 163.52, average team score 81.7619. This league mean is **provisional** because the provider's direct page sometimes renders an earlier snapshot; recompute from the official full 21-game ledger before any formal reference freeze. Standings snapshot: https://www.fanziz.com/basketball/series/wnbl-2627/points-table. Match-result corroboration: https://api.thesportsdb.com/season/5113-australian-wnbl/2026-2027.

Direct two-sided offence/defence mean diagnostic: Perth=(87.33+89.75)/2=88.54; Bendigo=(78.25+88.00)/2=83.13; total=171.67; Perth margin=5.42. This treats only three/four games as fully trustworthy and therefore is not the selected estimator.

**Shrinkage demonstrator:** fixed prior equivalent to `k=5` league games, not fitted or validated. Perth weight `wP=3/(3+5)=0.375`, Bendigo weight `wB=4/(4+5)=0.4444`. Let `L=163.5238/2=81.7619` team points. For each score, add its own shrunk offence departure and opponent shrunk defence departure. Split an **assumed** home advantage of +1.5 points in margin into +0.75/-0.75, taken for scenario illustration from the repository's FIBA40 family home-prior +1.49 (not WNBL-validated):

- `E(Perth)=L+wP×(87.333−L)+wB×(89.75−L)+0.75 = 88.1515`.
- `E(Bendigo)=L+wB×(78.25−L)+wP×(88−L)−0.75 = 81.7903`.
- `E(total)=169.9418`; `E(Perth margin)=+6.3611`.

Width floor proxy: `sigma_margin=12.76×1.10=14.036` and `sigma_total=16.82×1.10=18.502` from `PARAMETERS.md` FIBA40 family residual widths. WNBL-specific residuals, covariance, possessions and efficiency are NOT_ESTIMATED. For an illustrative normal marginal only: `P(Perth ML)≈Phi(6.3611/14.036)=0.6748`, `P(Perth -10.5)≈Phi((6.3611-10.5)/14.036)=0.3840`, `P(Bendigo +10.5)≈0.6160`, `P(Over 167.5)≈Phi((169.9418-167.5)/18.502)=0.5525`, `P(Under 167.5)≈0.4475`.

**Limitations:** these normal probabilities are hand-calculated (no MC or fitted engine), and are **not** published p_card or qualified probabilities. A fully coherent joint team-score distribution, actual WNBL possession-based ORtg/DRtg, covariance, overtime branch, confirmed lineup-specific effects and precision audit have not been computed. An approximation to completed-game averages is not an explicitly simulated overtime process. Under the repository, numerical gate, pair rank and joint-failure results are NOT_ASSESSABLE.

## A5. Complete supplied-contract assessment and sensitivity

| Scenario | Expected Perth | Expected Bendigo | Mean total | Mean home margin | Indicative P(Bendigo +10.5) | Indicative P(Over 167.5) |
|---|---:|---:|---:|---:|---:|---:|
| More current-season weight (`k=3`) | 89.86 | 82.12 | 171.99 | +7.74 | 57.8% | 59.6% |
| Base illustrative (`k=5`) | 88.15 | 81.79 | 169.94 | +6.36 | 61.6% | 55.2% |
| More league shrinkage (`k=7`) | 87.09 | 81.61 | 168.69 | +5.48 | 64.0% | 52.6% |
| More shrinkage (`k=10`) | 86.08 | 81.45 | 167.53 | +4.63 | 66.2% | 50.1% |

**Availability conditional sensitivity, NOT empirical effects:** shifting Bendigo's base centre down 3 points (e.g., less creator/bench availability) changes its indicative +10.5 cover to 53.2% and Over to 48.8%. A −5-point Bendigo change yields about 47.6% and 44.5%, reversing the cover preference. A +3 change raises them to 69.4% and 61.6%. These are thought experiments, not estimates that an individual absence is worth 3 or 5 points.

**Interpretation:** Lynx winner is the broad directional call. Bendigo +10.5 is the leading conditional spread lean if the last-game rotation is retained; it is not a strong unconditional play because the exact-day absences are disputed. At 167.5, competing current-season rates and six older H2Hs do not support a stable total lean.

## A6. Adjustments, venue, fatigue, coaching and overlapping evidence

- **Home:** Perth's venue is confirmed; illustrative +1.5 final margin from FIBA40-family **scenario assumption**, not a measured WNBL adjustment ledger entry. Perth has only one current-season home game, so a stable home split is unavailable.
- **Rest/travel:** Perth last played Nov 3 (seven days), Bendigo Nov 7 (three days) and travels interstate. This may help Perth late; **no sourced WNBL effect size or quantified direction**; scenario only, not secretly added to the centre.
- **Availability:** projected absences already largely represented in current-season scores. Do not deduct missing Borlase/Rees again; avoid double counting. Late changes in Wehrung/Olechnowicz, Tolo's restriction and Perth's actual rotation require exact minutes to alter numbers defensibly.
- **Coaching:** Perth Ryan Petrik; Bendigo Kennedy Kereama. Sources: https://www.basketball.com.au/news/wnbl-rosters and https://bendigospirit.wnbl.com.au/news/kennedy-kereama-re-signs-as-head-coach-of-the-bendigo-spirit. Coaching effect NOT_ESTIMATED.
- **Weather:** indoor venue — not an operative scoring variable.
- **H2H:** six prior meetings offer caution for the total but have materially different scorers/usage; numerical weight ZERO here. Rivalry/history not a license for an extra point adjustment.

## A7. Dependence, baseline and model-shadow controls

The +10.5 cushion and Under share a negative-tail risk: poor Bendigo offense increases the chance of an Under but also increases the chance Perth wins by >10.5; they must not be described as two independent safe legs. In the absence of a supported joint team-score model, `P(both fail)` = **NOT_COMPUTED**. Illustrative margin and total normal marginals alone cannot certify that joint.

`BASELINE_LEAGUE_V1` exact-row receipt: NOT_RUN / NOT_FROZEN. WNBL-specific mean total 163.52 from the indexed 21 games is provisional, and the repository has no validated WNBL row; `FAMILY_PRIOR:BASKETBALL_FIBA40` is unqualified for this competition. An actual baseline and its endpoint/width must be frozen before the card, which was not possible in read-only connector mode. `model_p NONE`; NO promoted WNBL release. No `pregame run`, no shadow execution, no reference receipt, no ML grid, no `PICKS_V2` block and no model ranking or rank delta should be treated as issued.

## A8. Source register, conflicts and next verifications

1. Official WNBL fixture, result and game status: https://schedule.nbl.com.au/schedule-v2/wnbl (game specific box/lineups before tip).
2. Club and WNBL preview / projected rotation and game-day absences: https://www.wnbl.com.au/news/how-to-watch-talking-points-perth-v-bendigo. Header appears copied from another date; fixture source supersedes it.
3. Independent tracked roster and injury list: https://www.basketball.com.au/news/wnbl-injury-report. Source says latest league injury list 4 Nov; inconsistent with 10 Nov preview for Wehrung/Wilson.
4. WNBL Nov 7 report explicitly describes Abbey Wehrung playing and hitting fourth-quarter threes: https://www.wnbl.com.au/news/puoch-celebrates-100th-game-in-capitals-victory-over-spirit. Must resolve whether her status changed in the following three days.
5. Latest two player-score detail sources: https://www.basketball.com.au/games/townsville-fire-v-perth-lynx-women-03-11-2026 and https://www.basketball.com.au/games/bendigo-spirit-v-uc-capitals-women-07-11-2026. Extracting full box from a dynamic page returned partial data; full pace/rotation ledger was not compiled.
6. Exact archived results: https://www.thesportsdb.com/season/5113-australian-wnbl/2025-2026 and https://api.thesportsdb.com/season/5113-australian-wnbl/2026-2027.
7. Official match game-centre starting five, active reserves, game ID, first play, updated injury releases, Tolo actual minutes, Olechnowicz final status and operator settlement terms: all **NOT_VERIFIED**. A fresh official release is required to settle the contradictions; no automatic task has been scheduled.

The repository's `python -m ml source-audit` cannot be claimed executed without a local project checkout; the connected GitHub route was read-only. Official/structured search evidence was used for this draft but is **not** equivalent to the repository's approved-source receipt. No odds, market prices or betting forecasts were used as inputs.

## A9. Integrity, scope and completion matrix

| Protocol item | Work/result | Gap/status |
|---|---|---|
| Identity/timing/competition/endpoint | WNBL27 R4; Tue 10 Nov 18:00 AWST, club/league fixture verified | Actual tip and operator terms NOT_VERIFIED |
| Starting fives, bench, fitness | Projected players and WNBL 10 Nov / 4 Nov reports compared | Live exact active bench/starter and Wehrung discrepancy unresolved |
| Prior results and 2025–26 H2H | Current 3+4 games and six H2H extracted | Source availability timestamps and full box-score feature rows incomplete |
| L5/L10/L15/L20/season | Cross-season rows counted; explicit n; current season n3/n4 | Cross-season roster incompatibility; limited league-specific context |
| Venue, scheduling, rest, style | Home Perth, seven days vs three days, interstate travel, key creators | No measured WNBL rest/pace/shot-profile adjustment |
| Reference and model execution | Read published controls and registry; unpromoted | No local code, reference freeze, full score grid or post-card shadow execution |
| All supplied rows / arithmetic | Four exact game lines + both ML direction; transparent illustrative normal formula | No issued p_card / validated pair ranking or OT transition |
| Baseline, sensitivity, dependence | Provisional league mean; k3–k10 and ±3/5 Bendigo score sensitivity | League baseline freeze, joint failure, roster effects unverified |
| Append/retention/commit/settlement | Standalone Markdown read-only research artifact | Mini unchanged; no local ID; NOT_ISSUED; no commit/push; no settlement |

**Outcome exposure:** NONE knowingly used in research preceding 21:00 AEDT; no guarantee of formal pre-start issue. **Overall research closure:** INFORMATION_INCOMPLETE (required confirmed starters/bench, source audit, possession model, WNBL baseline and numerical gating not completed). **Prediction classification:** research-only diagnostic with a conditional lean, no primary issued forecast. **Next action:** check official starters and Wehrung/Olechnowicz/Tolo minutes before any future independently authorized and reproducible card freeze.
