<!-- BEGIN CANONICAL RESEARCH P-606 -->
## P-606 — BASKETBALL / NBA preseason · Charlotte Hornets @ Memphis Grizzlies · 2026-10-16 (US)
Import: 2026-10-21T01:07:13+11:00; prompt 4 NEW_CANONICAL_EVENT. Local event key `LOCAL-2026101679B3FBCC8D-G0006` → canonical **P-606**; native identity NBA 0012600059. Source mini `2026101679B3FBCC8D`, frozen source SHA-256 `b7478342e7ecba6861d9d79e4fc98b1dcd686356260f8b21911989847115ad7e` (313,155 bytes). Card core SHA-256 `163b69ceb9fc4eeaee2ffe4bb070f42857e8023a1eba228d841d88e5e744c794` (18,716 bytes) = the exact bytes between the local BEGIN/END CARD marker lines (source offsets 171916–190632); markers and headings outside them remain in the preserved source. Original method, probabilities, ranks, statuses, timing and gaps are literal; any NOT_ASSIGNED / PENDING wording inside the core is historical. Import is not a forecast timestamp and confers no certification.

## Card · LOCAL-2026101679B3FBCC8D-G0006 · BASKETBALL / NBA Preseason · Charlotte Hornets @ Memphis Grizzlies · 2026-10-17

- **Stable local event key:** `LOCAL-2026101679B3FBCC8D-G0006`; canonical ID `NOT_ASSIGNED`, assignment only at `PROMPT_4_IMPORT`. Native NBA ID `0012600059` (from NBA game URL). This key is a **candidate research draft**, not asserted as a valid original issued card because owner desktop/lease and source custody are not independently controlled.
- **Pinned repository/main:** `27e013c35477dbffb7b7699b269a0b978fb69b7f`; `PUBLISHED_MAIN_PINNED`; MDS/P v20.0, CR-R7, SEL v3, CYCLE-v1, PRIMARY-v3.3. Repository read-only. No market/odds inputs and no workshop model. The known original five card bodies are retained exactly in this separate file.
- **User-supplied intake, transcribed (UI escaping and exact bytes not independently verifiable):**
```text
[$github](app://connector_76869538009648d5b282a4bb21c3d157) Upcoming game — BASKETBALL

- Competition details: <CHA Hornets @ MEM Grizzlies, NBA Pre-Season>
- Scheduled start: <11:00 AM AEDT, 17 October 2026 (can be delayed, so continue research and processes as normal)>
- Supplied contracts: <Hornets +2.5>, <Grizzlies -2.5>, <Combined Total Points: Over/Under 229.5 Points>,
- Research constraints: <continue pre game research even if game starts, continue until research is properly done>

i need the probability issue and expected value as well based on research and/or processes in the github/ML/RL.
```

### A1. Event identity / timing / authority
- NBA.com event `0012600059`, 2026-10-16 20:00 US Eastern Daylight Time (UTC−04) = 2026-10-17 00:00 UTC = 2026-10-17 11:00 Australia/Melbourne AEDT (UTC+11); FedExForum, Memphis, TN; NBA preseason 2026–27. Official Hornets announcement 2026-07-27 and NBA game page agree. Actual tipoff delay, clock, game phase, and first-play start NOT_VERIFIED. Research/file issue **2026-10-17T11:17:59+11:00**, AFTER scheduled tip. Classification `POST_SCHEDULED_START_ISSUE / KNOWN_AT_UNVERIFIED / NOT_CERTIFIED_PRE_START` (no live/final exposure intentionally used; cannot affirm CLEAN_PRE_START_INPUTS without archive times).
- Duplicate/custody check: all five locally visible older card markers inspected; no CHA/MEM target in those five. Global desktop/canonical bodies and other minis not exhaustively accessible. Existing mini logical writer token was not externally verified and previous copies were marked NOT_ISSUED. New cumulative copy must be **READ_ONLY_DRAFT / NOT_ISSUED**, not an assertion of appended original.
- Settlement `NOT_PERFORMED`; owner-provided handicap/scores are points. Primary endpoint assumed full-game incl overtime as ordinary NBA game scoring; provider-specific action, OT settlement and void terms UNKNOWN_DEFINITION; regulation-only interpretation unpriced separately because no regulator/period-qualified rows were supplied; both interpretations remain a definition question. 229.5 cannot push on integral scores; ±2.5 cannot push. Event is exhibition/preseason and personnel/minutes are not equivalent to regular-season.

### A2. Contract table, sports expected values, formulas
Declared candidate universe EXACT four supplied directional contracts: CHA +2.5 points, MEM −2.5 points, combined OVER 229.5 points, combined UNDER 229.5 points; do not add or silently change thresholds. Sports-only, no bookmaker odds or monetary payout used. All numbers below are `UNCALIBRATED_ANALYST_SCENARIO / NOT_PRIMARY`, **not p_card** and not trained ML/RL.

| Analyst order | Contract | Analyst win probability | Expected sporting centre | Expected margin to line | Mechanism / limitation |
|---:|---|---:|---:|---:|---|
| 1 | Combined **Under 229.5** (full incl OT) | **64.09%** | combined **222.46** | 229.5 − E[total] = **+7.04 points** | Normal-approx total 19.5 SD; possible OT/rotation-driven tails |
| 2 | **Grizzlies −2.5** (full incl OT) | **53.66%** | MEM margin **+4.20** | E[MEM−CHA−2.5] = **+1.70 points** | High uncertainty: large last-season/preseason reversal |
| 3 | **Hornets +2.5** (full incl OT) | **46.34%** | CHA margin **−4.20** | E[CHA−MEM+2.5] = **-1.70 points** | Exact complement to MEM −2.5 under same convention |
| 4 | Combined **Over 229.5** (full incl OT) | **35.91%** | combined **222.46** | E[total−229.5] = **-7.04 points** | Exact complement to Under 229.5 |

- **Expected full-time score:** CHA 109.13 – MEM 113.33; expected full-game total **222.46**; expected MEM margin **+4.20**. These are NOT money-profits; no financial ROI/EV can be computed without payout and terms. No value claim.
- Model inputs were fixed BEFORE computing contract tails, with no opportunity to choose the line. Same point-count object produces the four opposite probabilities; `P(CHA+2.5) + P(MEM−2.5) = 1` and `P(Over229.5) + P(Under229.5)=1`; integer scoring means no push at half-point lines in the chosen full-game endpoint.
- Uncalibrated joint object: *approximate* bivariate-normal on full-game total T and MEM minus CHA margin D. Marginal means 222.46324, 4.19853; assumed `σ_T=19.5`, `σ_D=18.5` points, zero T/D correlation for illustration only. Under wins when T≤229; MEM −2.5 wins when D≥3. `Phi((229.5−E[T])/σ_T)` and `Phi((E[D]−2.5)/σ_D)` approximate the probabilities using continuity at the half-point threshold. Assumed SDs not fitted/calibrated; team/pace, injuries and pregame lineup uncertainty explicitly not fully learned.
- Raw recent-preseason pairing: expected CHA =(96.0 + 115.0)/2 = 105.5000; expected MEM =(118.0 + 109.3333)/2 = 113.6667; prior 17-game comparative pairing CHA =123.0294, MEM =109.3235. Central means = `0.75 * preseason + 0.25 * prior17` ±0.75 points per team for home advantage (declared heuristic, not measured here). Each previous-season row is a diagnostic of a DIFFERENT rotation and season; 75/25 is discretionary sensitivity, not fitted optimal weight.
- Probabilities are scenario estimates. **Primary model p_card: NOT_ESTIMATED** for every supplied row. ML model receipt, fitted family, fitted mixture experts, η, feedback warm start, BASELINE_P, qualification: NONE / NOT_RUN. Analyst probabilities must never be substituted into primary p_card / frozen expert weights.

### A3. Historical and current team process — last 5/10/15/20 (true n)
- Fully reconstructed diagnostic ledger of **20 dated played games for each team** in `GAME_OBSERVATIONS_AUDIT.csv`. This is 17 late-2025–26 games (CHA: 15 regular-season + 2 play-in; MEM: 17 regular-season) followed by **only 3 current-2026 preseason** games. Every window below includes the three preseason games; windows L5/10/15/20 cross distinct competition phases and rosters. They are NOT 20 homogeneous 2026–27 preseason games. All windows overlap and must not be counted as independent evidence.
| Team | L5 GF–GA / n | L10 GF–GA / n | L15 GF–GA / n | L20 GF–GA / n |
|---|---:|---:|---:|---:|
| CHA | 505–575 / 5 | 1068–1118 / 10 | 1639–1646 / 15 | 2265–2169 / 20 |
| MEM | 556–624 / 5 | 1131–1291 / 10 | 1675–1934 / 15 | 2230–2551 / 20 |

- Current preseason (true n=3/side): Charlotte BKN **90–124** (Oct 6), MIL **105–90** (Oct 11), @BOS **93–114** (Oct 14); totals 214, 195, 207. Memphis @ATL **132–123** (Oct 5), ORL **118–122** (Oct 8), @CHI **104–100** (Oct 10); totals 255, 240, 204. Charlotte offense 96.0, defense 109.33, 69 turnovers/3 (~23.0); Memphis offense 118, defense 115 in respective three played games. NBA official Charlotte recap corroborates 114–93 loss to Boston. <Post-2026-10-17-11:00 results intentionally NOT USED>.
- Prior last17 diagnostics: CHA 116.29 for/108.29 allowed; MEM 110.35 for/129.76 allowed. Team strength and minutes distribution were radically different in those April regular/play-in games. No strength-matched roster shrink learned, so large signal disagreement widens sensitivity, not a certified pregame lean.
- Source routes: NBA.com game, NBA official Hornets schedule and Oct 14 team recap, RealGM 2026–27 preseason matchup and 2025–26 team histories. Alternate cache for CHA 2025–26 returned March31-Apr12 fixtures as PREVIEW while search indexed a later results snapshot; marked DATA_PROVENANCE_CONFLICT. Native game IDs for historical rows not resolved (stable diagnostic surrogate only). Date-only games with UTC-local-time unknown. Independent row-by-row official box-score corroboration and source capture SHA/known-at remain **OPEN**, so structured history is quarantined; not admissible training history or baselines.

### A4. Team/roster/conditions, context, numerical process
- Official Hornets 25 Sep medical announcement: **Kon Knueppel**, **Grant Williams** will miss preseason for hamstrings. Official NBA/MEM 10 Oct: **Isaiah Stewart** moderate ankle sprain, to be reevaluated after 2 weeks; no healthy roster assumed. Additional statuses including Grayson Allen right knee soreness, Coby White calf, Kylan Boswell knee and other fitness: sources conflict and exact team health release/activation unverified. Do not infer participation.
- Rookie Wire 2026-10-16 projected CHAR Dennis Schröder, Grayson Allen, Brandon Miller, Naz Reid, Moussa Diabaté; projected MEM Ty Jerome, Cedric Coward, Jaylen Wells, Cameron Boozer, Zach Edey. **PROJECTED only**, not confirmed starters/bench/roles; reporting Grayson Allen a knee problem requires reconciliation, so projected lineup not used to assert availability. Official NBA game lineup/live gamebook and bench/confirmed absences not source-frozen before initial tip. League-endpoint expected 48 minutes plus overtime if tied; pace, substitution distribution, coach experimentation, injury risk, late changes and venue not parameter-fitted.
- Model execution attempted from sandbox: `python -m ml capability --out NBA_CAPABILITY.csv` **exit 1** with `/opt/pyvenv/bin/python: No module named ml`; `git clone --depth 1 --no-checkout https://github.com/danisgreat/Sports-Research.git ...` **exit 128**, DNS error `Could not resolve host: github.com`. Python scientific libraries suffice for standalone normal arithmetic but do **not** constitute repository execution. Required frozen competition release, `ml.workflow research`, `ml.workflow verify`, feedback/hedge expert weights never generated. Per CYCLE-v1 retain true failure, not an invented EXECUTION.csv, and continue source research. Previous league profiles retired; never use them as fallback.
- The input cut from official/historical source snapshots is pre-2026-10-17T11:00 in sporting dates. Publication/availability **before tip is not proven for every retrieved source**, and the local issue is after scheduled tip, so `POST_START_ISSUE / KNOWN_AT_UNVERIFIED` not a prospective frozen forecast. Live/current match score/box score NOT used in modeling. Existing contextual repository adapter would require 30 admitted league-specific events and previously observed participants; that admission was not demonstrated here. No claimed RL agent/control or learned policy.

### A5. Scenario/sensitivity and contract mechanism audit
| Scenario | Preseason component weight | Expected total | Expected MEM margin | P(CHA+2.5) | P(MEM−2.5) | P(Over229.5) | P(Under229.5) |
|---|---:|---:|---:|---:|---:|---:|---:|
| central | 0.75 | 222.46 | +4.20 | 46.3% | 53.7% | 35.9% | 64.1% |
| prior_strength_40pct | 0.60 | 224.44 | +0.92 | 53.4% | 46.6% | 39.8% | 60.2% |
| preseason_strength_90pct | 0.90 | 220.49 | +7.48 | 39.4% | 60.6% | 32.2% | 67.8% |
| higher_variance | 0.75 | 222.46 | +4.20 | 46.9% | 53.1% | 38.0% | 62.0% |
| lower_variance | 0.75 | 222.46 | +4.20 | 45.8% | 54.2% | 33.0% | 67.0% |
| mem_home_bigger | 0.75 | 222.46 | +6.70 | 41.0% | 59.0% | 35.9% | 64.1% |
| home_neutral | 0.75 | 222.46 | +2.70 | 49.6% | 50.4% | 35.9% | 64.1% |

- History/season mixture weight is a consequential unresolved analyst assumption: reducing preseason weight to 0.60 reverses the spread centre to MEM +0.92, so CHA +2.5 becomes slightly likelier; 0.90 weight increases MEM projected margin to +7.48. This is **ADJUSTMENT_DEPENDENT** for spread selection. Over/Under remains center-dependent; preseason turnover shrink effects, unknown starters/bench and double-team preseason volatility not directly measured.
- For all four supplied rows action conditions require 48min+explicit OT, no 2.5/229.5 pushes, only genuine cancellations/abandonments possible void contingent operator terms. No team-specific winner ML contract supplied; expected result from this scenario is MEM more points (not an ML probability). `ε` from floating-point normal CDF negligible (<0.01 percentage points), but total systematic/model uncertainty dominates; quoted hundredths reflect calculation arithmetic, not predictive precision.
- **Unfitted rotation/lineup tail:** an illustrative ±8-point shift in expected combined scoring (holding assumed σT=19.5) changes P(Under 229.5) from **77.97%** at total centre 214.46 to **48.03%** at 230.46. These are *unweighted stress tests*, not probabilities of lineup outcomes.
- Parameter stress: expected total changes 220.49 to 224.44 as mixing weight changes; assumed σT 16–23 / σD 16–22, home court zero to two each side. Alternative scenario rows retained in calculation JSON. Material missing team-rotation data stops confident primary rank, not independent research.

### A6. Candidate selection/dependence / baseline
- Exact researched directions are four; analyst descending order Under229.5 (64.09%), MEM−2.5 (53.66%), CHA+2.5 (46.34%), Over229.5 (35.91%). This is **analyst order only**, not PRIMARY ranking because no model p_card.
- Hypothetical numerical gate check on *uncalibrated* numbers only: top 0.64090 exceeds 0.62, best non-complement is MEM−2.5 0.53658, gap ~0.10432>0.04. `PRIMARY_GATE=NOT_ASSESSABLE_NO_MODEL`, not PASS. Analytic rank2 p=0.53658 falls below 0.58 provisional Rank-2 floor. No published/fitted same-line league baseline (`BASELINE_P=NOT_ESTIMATED`) or RET03/RET04/XCARD6 frozen shadows; cannot claim verified performance.
- Dependence: exact opposite contracts are mutually exclusive complements. Under and MEM−2.5 lose together when total≥230 AND MEM margin≤2, probability not identified without a fitted joint; under zero-correlation illustrative assumption gives (1−0.64090)×(1−0.53658)=0.1664; rigorous marginal Fréchet bounds 0 to 0.3591. It is not a measured joint. No forced rule-derived top two beyond supported exact rows.

### A7. Sports quantity EV versus monetary expected value
- E[Hornets points] **109.13**; E[Grizzlies points] **113.33**; E[total] **222.46**; E[MEM−CHA] **+4.20**. Hornets +2.5 expected adjusted margin **-1.70 points**; Grizzlies −2.5 **+1.70 points**. Under 229.5 has **+7.04 point** expected line distance, not profit or guarantee.
- No financial EV, ROI, bookmaker implied break-even or model edge asserted. The supplied lines contain no return multipliers; repo SPORTS_ONLY firewalls bookmaker-derived data. Do not treat a positive point buffer as monetary expected value.

### A8. Source, provenance, known-at and field-level gaps
- Read back `SOURCE_EVIDENCE.md`, `GAME_OBSERVATIONS_AUDIT.csv`, `RESEARCH_EXPORT/LOCAL-2026101679B3FBCC8D-G0006/` and `CALCULATION_RECEIPT.json`. All source IDs S01–S11 in evidence ledger are publicly addressable exact links. Historic 40 rows acquired from two RealGM team schedules and additional indexed snapshots; NOT all rows independently corroborated with official match box scores. Published time for many team game rows unknown. Raw webpage capture hash unavailable; export `capture_sha256`/`known_at` remain blank and `review_status=QUARANTINED_UNVERIFIED_CAPTURE_KNOWN_AT` (never a reviewed ML dataset).
- Open evidence needed: official confirmed starters, bench and named scratches each side with pre-tip timestamp; Grayson Allen/Coby White/Kylan Boswell current status; match start/delay and score exposure; operator overtime/void definition for spread/total; full league preseason comparator cohort and baseline sample; independent source per historical dated game row; source-known-at/published-at and genuine webpage capture bytes; fitted competition release/history training/feedback and actual model execution; desktop writer lease/canonical duplicate reconciliation.
- Unresolved lineup/release/custody and model failures do not waive contract assessments above; all four supplied directional cases assessed and mathematically complementary. No claim that research completeness is achieved while source lineage/availability remains open. No automated retry asserted.

### A9. Execution and C1–C22 research-completion matrix
| Domain | Actual status / evidence |
|---|---|
| C1–C4 authority identity/time | Repo pinned `27e013c35477dbffb7b7699b269a0b978fb69b7f`; event NBA `0012600059` verified, fixed schedule and full-game scope; exact tip/clock and model cutoff known-at uncertified; issued after scheduled start. |
| C5–C8 both-team L5/L10/L15/L20 | 40 dated rows with true n and cross-phase flags in historical CSV; official independent box-score corroboration and capture SHA incomplete. |
| C9–C11 roster/availability C20 | Official Hornets Knueppel/Williams OUT and Memphis Stewart OUT; projected starting fives not confirmed, benches/scratches and additional medical unresolved. |
| C12–C15 arithmetic/sensitivity | Four complete analyst numerical tails, sport expected score, line distances, explicit independent marginal normal assumptions, sensitivity executed; ML p_card NOT_ESTIMATED. |
| C16–C19 selection/dependence | Four directions analyst ranked, complementary and marginal joint bounds reported, eligibility and precision labels NO_PRIMARY; same-line primary BASELINE_P and shadows not run. |
| C21 actual ML capability | `python -m ml capability` EXIT1 No module named ml; Git clone EXIT128 DNS. No executable pinned checkout, release, attempt or bundle; `ml.workflow research` and `ml.workflow verify` NOT_RUN; no fabricated learning ledger/feedback. |
| Learning pipeline | 40 historical diagnostic rows; machine-ingest export schema generated with unknown known_at/capture fields; **QUARANTINED**, no dry-run ingest (module absent), no shared learning-store write. |
| C22 custody/delivery | Original five card bodies preserved byte-identically; one candidate new G0006 card inserted in verified separate cumulative file, intake/footer/manifest updated in that separate copy; original desktop/owner issuing-writer access UNVERIFIED. |
| Scope and completion | Independent history, assumptions, numerical estimates and field-level gaps retained; `INFORMATION_INCOMPLETE / RESEARCH_ONLY_NO_MODEL / READ_ONLY_DRAFT / NOT_ISSUED`. No settlement. No GitHub writes. |

<!-- END CANONICAL RESEARCH P-606 -->
