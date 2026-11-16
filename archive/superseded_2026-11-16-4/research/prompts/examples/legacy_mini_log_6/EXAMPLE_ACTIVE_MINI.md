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
