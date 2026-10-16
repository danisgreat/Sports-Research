<!-- MINI-LOG-FORMAT: mini-log-7 -->
# FORMAT EXAMPLE — synthetic active mini

NOT_ISSUED / NOT_IMPORTABLE. EXAMPLE IDs are documentation identifiers, never P-IDs. Every team, event, time and probability below is a stipulated toy fixture, not observed sports evidence. Do not copy these values into a real card. The previous mini-log-6 pair is kept unchanged in [legacy_mini_log_6/](legacy_mini_log_6/EXAMPLE_ACTIVE_MINI.md).

## A. Authority snapshot
| Field | Value |
|---|---|
| Authority mode | FORMAT_EXAMPLE (a real mini prints PUBLISHED_MAIN_PINNED <full SHA> or LOCAL_WORKING_TREE <branch/HEAD>) |
| Repository / branch / read HEAD | FORMAT_EXAMPLE / N/A / N/A |
| Relevant working differences | N/A synthetic fixture |
| Method / control / scoring / selection | MDS-2026.10.12-v11.0 / CR-2026.10.12-R1 / SCV-2026.10.12-v7 / SEL-2026.10.12-v3 |
| Active Combined Log | N/A — never imported |
| Highest committed / next canonical ID | N/A / N/A |
| Outstanding local minis and IDs | NONE |
| First working ID | EXAMPLE-001 (not allocatable) |
| Issuing writer / lease start / lease expiry | FORMAT_EXAMPLE writer / 2000-01-01T09:00:00Z / 2000-01-02T09:00:00Z (toy) |
| Lease hand-overs | NONE |
| Frozen for settlement | NO |
| Reading receipt / opened at | Template fixture reviewed with v11 documents; no live repository or event receipt asserted |
| Mode | FORMAT_EXAMPLE |

SPORTS_ONLY / MARKET_BLIND · RESEARCH_ONLY_NOT_CERTIFIED · CANONICAL_IMPORT_STATUS: NOT_IMPORTABLE

## B. Local ID rules
Examples consume no P-ID. Production rules are in CARD_AND_LOG_TEMPLATES §2.

## C. Carryover and evidence queue
| ID | Event key | Queue | Original card / frozen pick table | Latest revision | Open field | Responsible actor | Next source + exact field | Due (ISO, tz) | Final-time basis | Last attempt | Scheduled automation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NONE | | | | | | | | | | | |

## D. Request intake
| Request key | Received (ISO, tz) | Event / alias as requested | Disposition | Card or addendum pointer, or no-card reason |
|---|---|---|---|---|
| REQ-EXAMPLE-1 | 2000-01-01T09:30:00Z | "A vs B, toy points" | CARD | EXAMPLE-001 |

# NEW LOCAL EVENT CARDS

<!-- BEGIN CARD EXAMPLE-001 -->
## Card · EXAMPLE-001 · Synthetic points · A vs B · fixture day

- **Working ID:** EXAMPLE-001 — NOT_ISSUED — NOT_IMPORTABLE
- **Event key / native ID / aliases:** SYNTHETIC:TOY:001 / N/A / NONE
- **Authority:** v11 versions above; P_ORDER_V2 priced from the declared mixture; synthetic fixture
- **Analysis status:** UNCALIBRATED_ANALYST_SCENARIO (toy calculation only)
- **Timing:** hypothetical PREGAME; cutoff 2000-01-01T10:00:00Z; research completion 09:10Z; lineup check 10:01Z; hypothetical issue/recheck 10:02Z; source times/actual start N/A, no real issue claimed
- **Scheduled start:** hypothetical 2000-01-01T10:10:00Z; venue UTC; Sydney 2000-01-01T21:10:00+11:00
- **Scheduled lead / band:** 8 minutes / BUFFERED (hypothetical)
- **Endpoint / definition:** toy regulation points; draw allowed; no push/void on half lines; operator N/A; retirement/listed pitcher/abandonment N/A for this stipulated fixture
- **Distribution object:** TOY_JOINT_V2 — mixture of three stipulated cases (A,B) masses (2,0)/(1,0)/(0,1)/(1,1): low .40/.25/.25/.10, base .45/.25/.20/.10, high .50/.25/.15/.10; mixture .45/.25/.20/.10
- **Expected score:** points — A 1.25 (SD 0.7665); B 0.30 (SD 0.4583); total 1.55 (SD 0.4975); margin A−B +0.95 (SD 1.1608); the mixture's masses equal the base case, so the moments are unchanged
- **Baseline:** BASELINE_LEAGUE_V1_TOY — stipulated independent fixture masses .30/.30/.25/.15 on the same four states; no real league fit or archive sample claimed
- **Regime flags / context:** NONE / synthetic arithmetic
- **Settlement fields / capture plan:** toy final A/B points; fixture-only source; no live capture, scheduled job NO
- **Rules read / archive check:** CURRENT_RULES §§2–8; SELECTION_RULES §§2–3/5/9; SCORING_AND_VALIDATION §§1–3; ARCHIVE_USE_GUIDE recipe R2 (toy rows in A3); archive N/A synthetic
- **Evidence receipt:** all inputs stipulated in A3; no external sporting source
- **Known-at:** N/A synthetic; no archive capture; no KNOWN_AT_UNVERIFIED input
- **Lineup state / issue step:** N/A (toy sport has no lineup); hypothetical research completion 10:01Z, issue freeze 10:02Z when complete; no countdown requirement
- **Pricing basis:** MIXTURE low/base/high = .25/.50/.25 on TOY_ENVIRONMENT (labelled unfitted)
- **Form windows:** A scored L5/L10/L15/L20/season 1.40/1.30/1.27/1.25/1.25 (n 5/10/15/20/20); B scored .20/.30/.33/.30/.30; league .80; primary rates A 1.209, B .345; recency blend A 1.240, B .349; printed only, not applied (A3)

### Decision block
Toy primary choice A +0.5; both primary propositions share the same loss state, so the pair gives no diversification benefit.

| Rank | Role | Tag | Contract key / exact proposition | p_card | p_base | BASELINE_P | Line distance (units / z) | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED | a_margin: A +0.5 points, regulation | 80.0% | 80.0% | 75.0% | −1.45 / −1.249 | TOY_JOINT_V2 | B wins |
| 2 | PICK | ANALYST_DERIVED | b_home: A Over 0.5 points, regulation | 80.0% | 80.0% | 75.0% | −0.75 / −0.978 | TOY_JOINT_V2 | A scores zero |
| 3 | INFORMATIONAL | SUPPLIED | c_away: B Under 0.5 points, regulation | 70.0% | 70.0% | 60.0% | +0.20 / +0.436 | TOY_JOINT_V2 | B scores |
| 4 | INFORMATIONAL | SUPPLIED | d_winner: A to win in regulation (draw loses) | 70.0% | 70.0% | 60.0% | −0.45 / −0.388 | TOY_JOINT_V2 | B win or draw |

**Baseline coverage:** 4/4.
**Rank-1 gate:** RANK1_UNSTABLE; .80; best alternative b_home .80; gap 0.00; ε 0 (exact fixture arithmetic); floor passes, margin fails; full four-row fixture universe.
**Rank-2 floor:** PASS (.80 ≥ .58).
**Joint failure:** exact unconditional .20, common losing state (0,1); both decisive mass 1.00; not mechanically protected.
**Shadow gate / Rank 2:** RET03 uses b_home .80, gap zero, RANK1_UNSTABLE; RET04=b_home (.80, baseline .75, joint .20); XCARD6=b_home (minimum joint .20, tie-break p then key); NOT_PRIMARY shadow records.
**Shadow RANK_DELTA / BASE_ONLY:** RANK_DELTA top two c_away (Δ .10) and d_winner (Δ .10; tie broken by p_card, then key), joint loss .30 (states (0,1),(1,1)); BASE_ONLY ranks and gate identical to primary (p_base = p_card); NOT_PRIMARY.
**Adjustment dependence:** NONE; no large adjustment; form rates printed only.
**Potential winner:** A .70, B .20, draw .10; sum 1.00.
**Supplied rows not selected:** NONE; both supplied rows are informational, not primary picks.

### Appendix
#### A1. Identity, timing and state
Fixture identity/times only; production C2/C11 event verification N/A. No real pregame source/custody assertion.
#### A2. Frozen supplied contracts and candidate recipe
The declared toy universe is exactly a_margin, b_home, c_away, d_winner; no search/ladder optimality claim beyond this fixed fixture set. Quantity keys: signed margin, A team total, B team total, signed margin. Deterministic equal-p ties sort by contract key.
#### A3. Evidence and archive inputs
Availability procedure: N/A for this stipulated toy sport (no real participants, starters, bench or injury list). This exemption never applies merely because a real competition is obscure. Real-game examples and negative cases are in [availability fixtures](../../verification/framework_change_2026-10-14-4/FIXTURES.md).
Candidate case masses and separate baseline masses .30,.30,.25,.15 are stipulated before the outcome fixture; every case sums to 1. No external sources, sample size or fitted model invented.

Form windows (toy rows, template §3b). Side A:

| Window | n | Dates | Scored per game | Conceded per game | Margin per game | Opponents | Previous season | Flags |
|---|---:|---|---:|---:|---:|---|---:|---|
| L5 | 5 | toy | 1.40 | N/A | N/A | N/A | 0 | — |
| L10 | 10 | toy | 1.30 | N/A | N/A | N/A | 0 | — |
| L15 | 15 | toy | 1.27 | N/A | N/A | N/A | 0 | — |
| L20 | 20 | toy | 1.25 | N/A | N/A | N/A | 0 | — |
| Season to date | 20 | toy | 1.25 | N/A | N/A | N/A | 0 | — |
| League level (toy) | — | — | 0.80 | — | — | — | — | — |

Primary rate (k = 2): (20 × 1.25 + 2 × 0.80) ÷ 22 = 1.209. Recency blend: (1.40 + 1.30 + 1.27 + 1.25) ÷ 4 = 1.305; shrunk with n = 13.5: (13.5 × 1.305 + 1.6) ÷ 15.5 = 1.240. Side B: L5/L10/L15/L20/season .20/.30/.33/.30/.30; primary (20 × .30 + 1.6) ÷ 22 = .345; blend .2825, shrunk .349. Windows overlap; counted once. The toy distribution is stipulated, so these rates are printed and not applied.
#### A4. Distribution, baseline, expected-score arithmetic and sensitivity
Mixture: .25 × low + .50 × base + .25 × high = (.10 + .225 + .125, .0625 + .125 + .0625, .0625 + .10 + .0375, .025 + .05 + .025) = .45/.25/.20/.10. W/P/L/V: ranks 1–2 .80/0/.20/0; ranks 3–4 .70/0/.30/0. Baseline ranks 1–2 .75/0/.25/0; ranks 3–4 .60/0/.40/0.

E(A)=2×.45+.25+.10=1.25; E(B)=.20+.10=.30. E(A²)=2.15; Var(A)=2.15−1.25²=.5875. Var(B)=.30−.30²=.21. E(AB)=.10; covariance=.10−1.25×.30=−.275. Total variance=.5875+.21−.55=.2475. Margin variance=.5875+.21+.55=1.3475. SDs are square roots, rounded to four decimals.

Line distances: a_margin needs margin > −0.5: −0.5 − 0.95 = −1.45, z = −1.45/1.1608 = −1.249. b_home: 0.5 − 1.25 = −0.75, z −0.978. c_away: 0.5 − 0.30 = +0.20, z +0.436. d_winner: 0.5 − 0.95 = −0.45, z −0.388.

Sensitivity cases low/base/high give primary p .75/.80/.85 and lower-row p .65/.70/.75; pair/order unchanged, gate margin zero throughout. Because the cases are symmetric, the mixture equals the base case. These are toy cases, not confidence intervals.
#### A5. Full priced universe or labelled subset; W/P/L/V by row
The four-row declared universe and all masses are above. Complements have p .20/.20/.30/.30. No omitted allowed draws; no push/void. No probability clipping.
#### A6. Adjustments, regimes and unadjusted comparison
Adjustments NONE (form rates printed, not applied); unadjusted pair equals primary. Regimes NONE.
#### A7. Family checks and shadow records
Synthetic points only; real sport-family checks N/A. Both primary loss sets are {(0,1)}. Different quantity does not imply independence. RANK_DELTA: Δ = .05/.05/.10/.10; c_away and d_winner tie on Δ and on p_card, so the contract key orders them. Shadows frozen above before the settlement fixture.
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
