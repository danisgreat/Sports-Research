<!-- MINI-LOG-FORMAT: mini-log-6 -->
# FORMAT EXAMPLE — synthetic active mini

NOT_ISSUED / NOT_IMPORTABLE. EXAMPLE IDs are documentation identifiers, never P-IDs. Every team, event, time and probability below is a stipulated toy fixture, not observed sports evidence. Do not copy these values into a real card.

## A. Authority snapshot
| Field | Value |
|---|---|
| Repository / branch / read HEAD | FORMAT_EXAMPLE / N/A / N/A |
| Relevant working differences | N/A synthetic fixture |
| Method / control / scoring / selection | MDS-2026.10.11-v10.0 / CR-2026.10.11-R1 / SCV-2026.10.11-v6 / SEL-2026.10.11-v2 |
| Active Combined Log | N/A — never imported |
| Highest committed / next canonical ID | N/A / N/A |
| Outstanding local minis and IDs | NONE |
| First working ID | EXAMPLE-001 (not allocatable) |
| Reading receipt / opened at | Template fixture reviewed with v10 documents; no live repository or event receipt asserted |
| Mode | FORMAT_EXAMPLE |

SPORTS_ONLY / MARKET_BLIND · RESEARCH_ONLY_NOT_CERTIFIED · CANONICAL_IMPORT_STATUS: NOT_IMPORTABLE

## B. Local ID rules
Examples consume no P-ID. Production rules are in CARD_AND_LOG_TEMPLATES §2.

## C. Carryover and evidence queue
NONE.

# NEW LOCAL EVENT CARDS

<!-- BEGIN CARD EXAMPLE-001 -->
## Card · EXAMPLE-001 · Synthetic points · A vs B · fixture day

- **Working ID:** EXAMPLE-001 — NOT_ISSUED — NOT_IMPORTABLE
- **Event key / native ID / aliases:** SYNTHETIC:TOY:001 / N/A / NONE
- **Authority:** v10 versions above; P_ORDER_V2; synthetic fixture
- **Analysis status:** UNCALIBRATED_ANALYST_SCENARIO (toy calculation only)
- **Timing:** hypothetical PREGAME; cutoff 2000-01-01T10:00:00Z; completion 10:01Z; hypothetical issue/recheck 10:02Z; source times/actual start N/A, no real issue claimed
- **Scheduled start:** hypothetical 2000-01-01T10:10:00Z; venue UTC; Sydney 2000-01-01T21:10:00+11:00
- **Scheduled lead / band:** 8 minutes / BUFFERED (hypothetical)
- **Endpoint / definition:** toy regulation points; draw allowed; no push/void on half lines; operator N/A; retirement/listed pitcher/abandonment N/A for this stipulated fixture
- **Distribution object:** TOY_JOINT_V1 — (A,B) masses (2,0):0.45; (1,0):0.25; (0,1):0.20; (1,1):0.10
- **Expected score:** points — A 1.25 (SD 0.7665); B 0.30 (SD 0.4583); total 1.55 (SD 0.4975); margin A−B +0.95 (SD 1.1608)
- **Baseline:** BASELINE_LEAGUE_V1_TOY — stipulated independent fixture masses .30/.30/.25/.15 on the same four states; no real league fit or archive sample claimed
- **Regime flags / context:** NONE / synthetic arithmetic
- **Settlement fields / capture plan:** toy final A/B points; fixture-only source; no live capture, scheduled job NO
- **Rules read / archive check:** CURRENT_RULES §§2–8; SELECTION_RULES §§2–3/9; SCORING_AND_VALIDATION §§1–3; archive N/A synthetic
- **Evidence receipt:** all inputs stipulated in A3; no external sporting source

### Decision block
Toy primary choice A +0.5; both primary propositions share the same loss state, so the pair gives no diversification benefit.

| Rank | Role | Tag | Contract key / exact proposition | p_card | BASELINE_P | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED | a_margin: A +0.5 points, regulation | 80.0% | 75.0% | TOY_JOINT_V1 | B wins |
| 2 | PICK | ANALYST_DERIVED | b_home: A Over 0.5 points, regulation | 80.0% | 75.0% | TOY_JOINT_V1 | A scores zero |
| 3 | INFORMATIONAL | SUPPLIED | c_away: B Under 0.5 points, regulation | 70.0% | 60.0% | TOY_JOINT_V1 | B scores |
| 4 | INFORMATIONAL | SUPPLIED | d_winner: A to win in regulation (draw loses) | 70.0% | 60.0% | TOY_JOINT_V1 | B win or draw |

**Rank-1 gate:** RANK1_UNSTABLE; .80; best alternative b_home .80; gap 0.00; floor passes, margin fails; full four-row fixture universe.
**Rank-2 floor:** PASS (.80 ≥ .58).
**Joint failure:** exact unconditional .20, common losing state (0,1); both decisive mass 1.00; not mechanically protected.
**Shadow gate / Rank 2:** RET03 uses b_home .80, gap zero, RANK1_UNSTABLE; RET04=b_home (.80, baseline .75, joint .20); XCARD6=b_home (minimum joint .20, tie-break p then key); NOT_PRIMARY shadow records.
**Adjustment dependence:** NONE; no large adjustment.
**Potential winner:** A .70, B .20, draw .10; sum 1.00.
**Supplied rows not selected:** NONE; both supplied rows are informational, not primary picks.

### Appendix
#### A1. Identity, timing and state
Fixture identity/times only; production C2/C11 event verification N/A. No real pregame source/custody assertion.
#### A2. Frozen supplied contracts and candidate recipe
The declared toy universe is exactly a_margin, b_home, c_away, d_winner; no search/ladder optimality claim beyond this fixed fixture set. Quantity keys: signed margin, A team total, B team total, signed margin. Deterministic equal-p ties sort by contract key.
#### A3. Evidence and archive inputs
Candidate masses .45,.25,.20,.10 and separate baseline masses .30,.30,.25,.15 are stipulated before the outcome fixture. Both sum to 1. No external sources, sample size or fitted model invented.
#### A4. Distribution, baseline, expected-score arithmetic and sensitivity
W/P/L/V: ranks 1–2 .80/0/.20/0; ranks 3–4 .70/0/.30/0. Baseline ranks 1–2 .75/0/.25/0; ranks 3–4 .60/0/.40/0.

E(A)=2×.45+.25+.10=1.25; E(B)=.20+.10=.30. E(A²)=2.15; Var(A)=2.15−1.25²=.5875. Var(B)=.30−.30²=.21. E(AB)=.10; covariance=.10−1.25×.30=−.275. Total variance=.5875+.21−.55=.2475. Margin variance=.5875+.21+.55=1.3475. SDs are square roots, rounded to four decimals.

Sensitivity transfers .05 mass between (2,0) and (0,1). Low/base/high A-winning environment: masses .40/.25/.25/.10; .45/.25/.20/.10; .50/.25/.15/.10. Primary p .75/.80/.85, lower-row p .65/.70/.75; pair/order unchanged, gate margin zero throughout. These are toy sensitivity cases, not confidence intervals.
#### A5. Full priced universe or labelled subset; W/P/L/V by row
The four-row declared universe and all masses are above. Complements have p .20/.20/.30/.30. No omitted allowed draws; no push/void. No probability clipping.
#### A6. Adjustments, regimes and unadjusted comparison
Adjustments NONE; unadjusted pair equals primary. Regimes NONE.
#### A7. Family checks and shadow records
Synthetic points only; real sport-family checks N/A. Both primary loss sets are {(0,1)}. Different quantity does not imply independence. Shadows frozen above before the settlement fixture.
#### A8. Sources, failures, capture/refresh plan
Synthetic input only; no live route, capture or refresh performed/claimed.
#### A9. Integrity receipt and readback
SPORTS_ONLY_MARKET_BLIND: PASS for fixture inputs · OUTCOME_EXPOSURE: synthetic example, no prospective evidence · SETTLEMENT: NOT_PERFORMED in this original example · CANONICAL_IMPORT: NOT_IMPORTABLE
<!-- END CARD EXAMPLE-001 -->

# RUNNING FOOTER
<!-- BEGIN FOOTER -->
| Field | Value |
|---|---|
| Highest new working ID used / next working ID | EXAMPLE-001 / EXAMPLE-002 (not allocatable) |
| Repository next-ID snapshot | N/A |
| New cards / numeric / qualitative / NO_FORECAST | 1 / 1 / 0 / 0 (synthetic) |
| Pending events / unresolved evidence records | 0 / 0 |
| Local mini status / import status | FORMAT_EXAMPLE / NOT_IMPORTABLE |
| GitHub writes performed | NO live log write |
<!-- END FOOTER -->

# SETTLEMENT AND RETROSPECTIVES
<!-- SETTLEMENT-FORMAT: mini-settlement-5 -->

FORMAT EXAMPLE ONLY. Authority: v10; no real source, time of issue or sporting result asserted. Frozen original is research/prompts/examples/EXAMPLE_ACTIVE_MINI.md; the settled example must begin with those exact bytes. One card, zero carryovers/addenda. No P-ID allocated.

<!-- BEGIN SETTLEMENT EXAMPLE-001 revision-1 -->
### Settlement · EXAMPLE-001 · Synthetic A vs B · hypothetical post-final review

**Card state:** SETTLED (synthetic only)
**Original card / prior revision:** EXAMPLE_ACTIVE_MINI.md / NONE
**Final event / verified final time:** stipulated A=0, B=1; not a real observed result; time N/A
**Definition status:** frozen toy regulation convention; operator N/A
**Expected vs final:** A expected 1.25/final 0/error −1.25/z −1.631; B .30/1/+.70/z +1.528; total 1.55/1/−.55/z −1.106; margin +.95/−1/−1.95/z −1.680. SDs from original fixture, not re-estimated.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis / definition / time |
|---|---|---|---|---|---|---|---|
| 1 | a_margin: A +0.5 points, regulation | 80.0% | 75.0% | LOSS | N/A synthetic | NO (loss) | −1+.5<0; frozen toy endpoint; no real retrieval |
| 2 | b_home: A Over 0.5 points, regulation | 80.0% | 75.0% | LOSS | N/A synthetic | NO (loss) | 0<.5 |
| 3 | c_away: B Under 0.5 points, regulation | 70.0% | 60.0% | LOSS | N/A synthetic | NO (informational) | 1>.5 |
| 4 | d_winner: A to win in regulation (draw loses) | 70.0% | 60.0% | LOSS | N/A synthetic | NO (informational) | 0<1 |

**Top-two result:** ALL_LOST; W0/L2/PUSH0/VOID0/UNRESOLVED0; 0/2 decisive wins; Hit@2 0/1; two-decisive both-loss outcome 1.
**Proper scores:** each primary Brier=.8²=.64; baseline=.75²=.5625; delta +.0775; event primary mean delta +.0775. Primary log loss −ln(.2)=1.6094; baseline −ln(.25)=1.3863; delta +.2231. Informational rows Brier .49 versus .36, separately recorded. One event and no real weeks: no skill inference.
**Shadow results:** RET03 unstable; RET04/XCARD6 both select original b_home, LOSS; NOT_PRIMARY. They do not add scored trials.
**Winner call:** original A call incorrect in this toy outcome.
**R1. Original prediction:** Rank 1 a_margin: A +0.5 points, regulation, p_card 80.0%; Rank 2 b_home: A Over 0.5 points, regulation, p_card 80.0%.
**R2. Final event:** stipulated A0–B1, no unresolved fixture fields.
**R3. Contract settlement:** the literal four propositions all lose by the arithmetic above.
**R4. Rank diagnostics:** 0/2 primary; NDCG N/A because all four rows lose; original gate unstable.
**R5. Winner call:** A .70/B .20/draw .10, observed toy state B win.
**R6. Line assessment:** margin plus .5 is −.5; A total is .5 below .5; B total is .5 above .5; no line changed.
**R7. Expected versus realised mechanism:** state (0,1) had original mass .20; both primary losses share that state.
**R8. Missed mechanism:** none identifiable from a single stipulated outcome.
**R9. Source/timing review:** N/A synthetic; no actual pregame custody or source-quality claim.
**R10. Classification:** arithmetic process SOUND within fixture; real-world process NOT_ASSESSABLE; model uncalibrated; suspected shared-driver exposure, not proven miscalibration.
**R11. Hypothesis:** test frozen alternate pairs on future paired events and exact joint masses; PROPOSED_NOT_TESTED.
**R12. Disposition:** NO_CHANGE to frozen toy forecast; no live recommendation promotion.

**Deep Rank-1 retrospection.**

**Claim:** A +0.5, p .80, tied with Rank 2; original gate unstable.
**What happened:** toy A lost by one; +.5 does not cover.
**Distribution check:** exact losing-state mass .20; signed-margin z about −1.680 using original SD. No claim this one draw validates the distribution.
**Knowability:** only the stipulated input distribution existed for this fixture; no real pre-cutoff catalyst or hindsight alternative invented.
**Verdict:** arithmetic/coherence passed; predictive adequacy and causal variance/model shares NOT_ASSESSABLE from one toy outcome.
**Own-top-two counterfactual:** unchanged under the fixed recipe; no post-result swap.
**Failure class:** SHARED_DRIVER_TOP_TWO as a descriptive losing-set property; empirical model failure not established.
**Proposed correction:** frozen paired alternative experiment with proper-score/coverage controls; PROPOSED_NOT_TESTED.
<!-- END SETTLEMENT EXAMPLE-001 revision-1 -->
