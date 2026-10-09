
<!-- BEGIN FINAL SETTLEMENT 2026-10-09 -->
## Final settlement of all pending records — 2026-10-09

**Scope.** All 72 records still carrying a sporting settlement obligation: the 65 records of `research/verification/carryover_review_2026-10-08/carryover.json` and P-550–P-556 from the 2026-10-09 import. This is settled under the user directive of 2026-10-09: settle everything; where details cannot be found, settle anyway; only Rank 1 and Rank 2 can count as wins; every Rank-1 failure gets a deep retrospection. Original forecasts, probabilities and ranks are unchanged. No canonical ID is consumed; the next canonical ID stays **P-557**. No pending record carried an unassigned temporary ID: every `TMP-`/`LOCAL-` alias already maps to a canonical P-ID.

**Settle-anyway hierarchy.** (A) owner/official field; (B) structured provider or multi-source agreement; (C) best-available single, secondary or provisional evidence adopted as final; (E) estimate from a partial measurement that bounds the field, with confidence stated; (OP) sporting endpoint known but operator rule absent, so the card's own frozen working assumption or the framework default applies (CURRENT_RULES: a missing operator definition does not block sporting settlement; RULES_TENNIS: a retirement voids games rows; RULES_CRICKET: runs scored before a stop count); (X) no admissible data, so the row is VOID.

**Cohort result under the top-two rule** (71 forecast cards; P-532 was a no-forecast intake): **79 counted wins from 134 live top-two rows (59.0%)**; Rank 1 40 W / 28 L / 3 VOID (58.8% of live); Rank 2 39 W / 27 L / 5 VOID; cards with both top rows won 27, split 26, both lost 15, void 3; Hit@2 53/68. Winner calls 37 correct / 11 incorrect (23 not recoverable). Ranks 3+ are recorded as informational only.

**Rank-1 failures with deep retrospection (28):** P-148, P-176, P-200, P-217, P-234, P-250, P-274, P-342, P-369, P-377, P-430, P-492, P-519, P-520, P-521, P-522, P-524, P-527, P-531, P-534, P-541, P-544, P-547, P-548, P-549, P-551, P-553, P-555. Recurring failure classes (a record can carry more than one): first-half-goal over-selection (P-148, P-234, P-250, P-342, P-377); baseball +1.5 cushion ceiling (P-274, P-524, P-544, P-547); basketball totals without a pace model (P-527, P-548, P-553); tennis score-tree under-dispersion or dependence (P-541, P-551, P-555); rank by q instead of p (P-519, P-521, P-522); dependent top two sharing one driver (P-176, P-492, P-541, P-549, P-555). Full analysis: `research/verification/final_settlement_2026-10-09/REPORT.md` and `FRAMEWORK_RETROSPECTIVE_2026-10-09.md`.

**Records settled in this block (50).** P-126–P-522 have no research-ledger parent. P-538–P-549 are canonical ledger cards, but `verify_rollover` pins exactly twelve addenda for that import, so their final settlements are recorded here by canonical ID instead of as second ledger addenda. P-523–P-537 and P-550–P-556 are settled by individual dated ledger addenda that follow.

### Final settlement · P-126 · Sikkim Aakraman FC vs Sikkim Boys Club

**Final settlement (2026-10-09) — Sikkim Aakraman FC vs Sikkim Boys Club (SFA A Division S-League).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Aakraman win; secondary records conflict 1-0 vs 3-0 and 28 vs 29 August; halftime and corners not recovered.

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Sikkim Aakraman FC match winner | **WIN** | YES | C best-available | Both conflicting secondary finals (1-0 and 3-0) are Aakraman wins, so the winner is invariant to the conflict |
| 2 | 1st Half Over 0.5 goals | **VOID** | NO (void/push) | X no data | No halftime score in any recovered source |
| 3 | Combined total Over 2.5 goals | **WIN** | NO (rank 3+ informational) | C best-available | Adopts the later multi-listing secondary 3-0 over the older single 1-0 claim |
| 4 | Total corners Over 7.5 (research threshold) | **VOID** | NO (rank 3+ informational) | X no data | No corner aggregate exists in any recovered source |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **1 counted win(s) of 1 live top-two row(s)**. Rank 1: WIN; Rank 2: VOID.
**Winner call.** Sikkim Aakraman FC: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-136 · James Duckworth vs Arthur Fery

**Final settlement (2026-10-09) — James Duckworth vs Arthur Fery (ATP Winston-Salem Open SF).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Fery advanced; Duckworth retired injured at 4-6, 1-2 (alternative report 4-6, 2-1) after 59 minutes.

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Total games Over 22.5 | **VOID** | NO (void/push) | OP default rule | RULES_TENNIS: a retirement voids the games rows; 13 games played, threshold not reached or excluded |
| 2 | James Duckworth +1.5 games | **VOID** | NO (void/push) | OP default rule | Retirement convention; handicap not mathematically decided at the stop |
| 3 | Arthur Fery -1.5 games | **VOID** | NO (rank 3+ informational) | OP default rule | Retirement convention |
| 4 | Total games Under 22.5 | **VOID** | NO (rank 3+ informational) | OP default rule | Retirement convention; Under could not be decided before 23 games became impossible |

**Top-two result.** VOID: no live top-two row (VOID card) — **0 counted win(s) of 0 live top-two row(s)**. Rank 1: VOID; Rank 2: VOID.
**Winner call.** Arthur Fery: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 was VOID**, so there is no performance result and no mandatory deep retrospection.

### Final settlement · P-148 · Toluca Femenil vs Leon Femenil

**Final settlement (2026-10-09) — Toluca Femenil vs Leon Femenil (Liga MX Femenil Apertura 2026 J5).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Toluca 1-0 Leon (HT 0-0; F. Robert 77').

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | 1st Half Over 0.5 goals | **LOSS** | NO (loss) | B structured | HT 0-0 from official club report and match timeline |
| 2 | Toluca team corners Over 4.5 | **LOSS** | NO (loss) | C best-available | Specialist display read Toluca 2 (2-6 ordering never resolved); inherited provisional LOSS adopted |
| 3 | Full match Over 2.5 goals | **LOSS** | NO (rank 3+ informational) | B structured | One goal |
| 4 | Full match Under 2.5 goals | **WIN** | NO (rank 3+ informational) | B structured | One goal |
| 5 | 1st Half Under 0.5 goals | **WIN** | NO (rank 3+ informational) | B structured | HT 0-0 |

**Top-two result.** TOP2_ALL_LOST: every live top-two row LOST — **0 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: LOSS.
**Winner call.** Toluca Femenil: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was 1st Half Over 0.5 goals in Toluca Femenil v León Femenil, a FORCED RANK at MEDIUM-LOW evidence. The central first-half family listed 1-0, 0-1 and 1-1, with 0-0 named only as "the principal contrary branch".
**What happened.** HT 0-0; one goal (77'). Toluca won 1-0. Rank 2 (Toluca team corners Over 4.5) also lost on the best available reading, so the card scored 0/2.
**Distribution check.** No score matrix was produced. A league-typical first-half goal rate near 0.70 makes a 0-0 half a 30% event, so this was not a tail outcome. The card named the failure path and then ranked against it without a number.
**Knowable at cutoff?** Partly. Both clubs' first-half creation (shots and xG by half) was never retrieved. The ranking leaned on historical goal occurrence instead.
**Verdict.** RANKING_SELECTION error, not variance alone. A roughly 65-70% proposition was placed at Rank 1 without a measured edge over the alternatives.
**Own-top-2 counterfactual.** The same goal model would have ranked Toluca double chance (home favourite; it won) or Under 2.5 (won) above a first-half proposition. Both rank higher in mass for a low-event women's league fixture.
**Failure class.** FIRST_HALF_GOAL_OVERSELECTION (recurs in P-234, P-250, P-342 and P-377: five Rank-1 failures in this cohort).
**Proposed correction (not implemented).** Require a fitted half-time score matrix (first-half λ from half-split xG) before any 1H row can be Rank 1, and require its probability to exceed the next-best coherent row by at least 5 points.

### Final settlement · P-149 · Colorado Rapids 2 vs Ventura County FC

**Final settlement (2026-10-09) — Colorado Rapids 2 vs Ventura County FC (MLS NEXT Pro).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Colorado Rapids 2 2-3 Ventura County (HT 1-1).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | 1st Half Over 0.5 goals | **WIN** | YES | A owner | HT 1-1 club-origin report |
| 2 | Ventura County team corners Over 3.5 | **WIN** | YES | C best-available | Inherited research WIN from secondary corner display; no owner aggregate |
| 3 | Full match Over 2.5 goals | **WIN** | NO (rank 3+ informational) | A owner | Five goals |
| 4 | Full match Under 2.5 goals | **LOSS** | NO (rank 3+ informational) | A owner | Five goals |
| 5 | 1st Half Under 0.5 goals | **LOSS** | NO (rank 3+ informational) | A owner | HT 1-1 |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** Ventura County FC: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-166 · Melbourne Mustangs vs Canberra Brave

**Final settlement (2026-10-09) — Melbourne Mustangs vs Canberra Brave (AIHL Goodall Cup SF).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Mustangs 5-4 Canberra after overtime (regulation 4-4).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Melbourne +1.5 | **WIN** | YES | B structured | Endpoint-invariant: draw in regulation and win after OT both cover |
| 2 | Over 7.5 goals | **WIN** | YES | B structured | Endpoint-invariant: 8 regulation goals and 9 full-game goals both exceed 7.5 |
| 3 | Under 7.5 goals | **LOSS** | NO (rank 3+ informational) | B structured | Endpoint-invariant |
| 4 | Canberra -1.5 | **LOSS** | NO (rank 3+ informational) | B structured | Endpoint-invariant |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** Melbourne Mustangs: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-176 · Amiens SC vs FC Versailles

**Final settlement (2026-10-09) — Amiens SC vs FC Versailles (France Ligue 3).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Amiens 3-0 Versailles (HT 0-0); corners 5+3=8 (secondary timeline).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Amiens team total Under 1.5 | **LOSS** | NO (loss) | B structured | Amiens scored 3 |
| 2 | Under 2.5 goals | **LOSS** | NO (loss) | B structured | Three goals |
| 3 | Versailles moneyline | **LOSS** | NO (rank 3+ informational) | B structured | Amiens won |
| 4 | 1st Half Over 0.5 goals | **LOSS** | NO (rank 3+ informational) | B structured | HT 0-0 |
| 5 | Total match corners Under 10.5 | **WIN** | NO (rank 3+ informational) | C best-available | Secondary timeline 5+3=8; FFF match sheet unavailable |

**Top-two result.** TOP2_ALL_LOST: every live top-two row LOST — **0 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: LOSS.
**Winner call.** FC Versailles: INCORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was Amiens team total Under 1.5 goals. The card also called Versailles as the regulation winner (Rank 3 ML), so the whole slate leaned on Versailles containing Amiens.
**What happened.** Amiens 3-0 (HT 0-0). Ranks 1-4 all lost; only the corners Under won (secondary 8). Winner call incorrect.
**Distribution check.** No joint goal matrix. Ranks 1 (Amiens Under 1.5), 2 (Under 2.5) and 3 (Versailles ML) are positively dependent: one "Amiens are weak at home" thesis supplied all three. Their joint failure mass was never printed. Correlated rows behaved as one bet.
**Knowable at cutoff?** The early-season Ligue 3 sample (three rounds) was too small to support a directional team-strength claim. The card rated it MEDIUM instead of capping it.
**Verdict.** MODEL/THESIS error amplified by DEPENDENCE. One wrong strength estimate sank the top three rows.
**Own-top-2 counterfactual.** A coherent matrix with home advantage and three-round shrinkage toward the league mean would have centred near 1.3-1.1 Amiens. It would not have produced Amiens Under 1.5 and Versailles ML together. The top two would likely have been Under 3.5 and 1H Under 1.5 type rows, or a corners row with an exposure model.
**Failure class.** SMALL_SAMPLE_STRENGTH_OVERREACH plus TOP_ROW_DEPENDENCE.
**Proposed correction.** Shrink team ratings by an explicit early-season prior weight (games played / (games played + k)). Print the joint top-two failure mass. Forbid Rank 1 and Rank 2 from sharing the same directional thesis when that mass exceeds 0.35.

### Final settlement · P-178 · AS Cannes vs Le Puy-en-Velay

**Final settlement (2026-10-09) — AS Cannes vs Le Puy-en-Velay (France Ligue 3).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Cannes 2-0 Le Puy; corners 8+8=16 (secondary).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Under 2.5 goals | **WIN** | YES | B structured | Two goals |
| 2 | Cannes team total Under 1.5 | **LOSS** | NO (loss) | B structured | Cannes scored 2 |
| 3 | 1st Half Over 0.5 goals | **WIN** | NO (rank 3+ informational) | B structured | First-half goal |
| 4 | Both teams to score - No | **WIN** | NO (rank 3+ informational) | B structured | Le Puy did not score |
| 5 | Total corners Under 10.5 | **LOSS** | NO (rank 3+ informational) | C best-available | Secondary aggregate 16; inherited research LOSS adopted |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: LOSS.
**Winner call.** AS Cannes: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-179 · Thionville Lusitanos vs Paris 13 Atletico

**Final settlement (2026-10-09) — Thionville Lusitanos vs Paris 13 Atletico (France Ligue 3).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Thionville 1-1 Paris 13 (two penalty goals in play; HT 0-0); corners 8+1=9 (secondary).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Thionville team total Over 0.5 | **WIN** | YES | B structured | Thionville scored |
| 2 | 1st Half Over 0.5 goals | **LOSS** | NO (loss) | B structured | HT 0-0 |
| 3 | Paris 13 team total Under 1.5 | **WIN** | NO (rank 3+ informational) | B structured | One goal |
| 4 | Under 2.5 goals | **WIN** | NO (rank 3+ informational) | B structured | Two goals |
| 5 | Under 10.5 corners | **WIN** | NO (rank 3+ informational) | C best-available | Secondary aggregate 9 |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: LOSS.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-200 · Herning Blue Fox vs Rungsted Seier Capital

**Final settlement (2026-10-09) — Herning Blue Fox vs Rungsted Seier Capital (Danish Metal Ligaen).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Herning 4-3 Rungsted after overtime (regulation 3-3).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Herning Blue Fox -2.5 | **LOSS** | NO (loss) | B structured | One-goal win; endpoint-invariant LOSS |
| 2 | Over 6.5 goals | **WIN** | YES | OP default rule | Card's frozen working assumption was full match incl. OT/SO: 7 goals. Regulation-only reading (6) would be LOSS |
| 3 | Rungsted Seier Capital +2.5 | **WIN** | NO (rank 3+ informational) | B structured | Endpoint-invariant |
| 4 | Under 6.5 goals | **LOSS** | NO (rank 3+ informational) | OP default rule | Full match incl. OT/SO per card assumption |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: WIN.
**Winner call.** Herning Blue Fox: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was Herning Blue Fox -2.5 (LEAN, MEDIUM). Herning was the potential winner.
**What happened.** Regulation 3-3; Herning won 4-3 in overtime. Herning won, but by one goal. Rank 2 (Over 6.5) won on the card's own full-match assumption.
**Distribution check.** In hockey a -2.5 needs a three-goal margin. The framework's own H-R2 reference puts two-goal-plus margins at 0.568 of all NHL games. Three-goal-plus margins are roughly half that (an estimate, not a registered statistic), and only a share of those go to the favourite, so even a clear favourite rarely clears 50% on -2.5.
**Knowable at cutoff?** Yes. The puck-line geometry is structural, and the card recorded unresolved goalie and preseason state.
**Verdict.** CONTRACT_GEOMETRY error. A three-goal handicap was ranked above the Over and the +2.5 counter-branch, both of which won.
**Own-top-2 counterfactual.** With a hockey goal model (regulation Poisson plus an OT bridge), Rungsted +2.5 (about 0.75-0.80) and Over 6.5 rank first and second. Both won, giving 2/2.
**Failure class.** HANDICAP_TAIL_OVERREACH.
**Proposed correction.** Rank-1 eligibility for any ±2.5 or wider hockey handicap requires a fitted margin distribution, including empty-net mass, with p ≥ 0.60.

### Final settlement · P-217 · Trinbago Knight Riders vs Guyana Amazon Warriors

**Final settlement (2026-10-09) — Trinbago Knight Riders vs Guyana Amazon Warriors (CPL).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Reduced to 16 overs: GAW 185/5, TKR 172/7; GAW won by 9 runs (DLS); GAW after 6 completed overs 31/2.

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | GAW innings Under 174.5 | **LOSS** | NO (loss) | OP default rule | Runs scored before any stop count (RULES_CRICKET); 185 crossed the line, so the Under was lost irrespective of the reduction |
| 2 | GAW after 6 overs Over 46.5 | **LOSS** | NO (loss) | B structured | Six completed overs 31/2 (not the 4.5-over powerplay 24/2) |
| 3 | GAW after 6 overs Under 46.5 | **WIN** | NO (rank 3+ informational) | B structured | 31/2 |
| 4 | GAW innings Over 174.5 | **WIN** | NO (rank 3+ informational) | OP default rule | 185 crossed 174.5 |

**Top-two result.** TOP2_ALL_LOST: every live top-two row LOST — **0 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: LOSS.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was Guyana Amazon Warriors 20-over innings Under 174.5. Rank 2 was GAW after 6 overs Over 46.5.
**What happened.** The match was reduced to 16 overs. GAW still made 185/5, so the line was crossed with four overs fewer than planned. After six completed overs GAW were only 31/2. Both top rows lost: a slow start followed by an extreme back end.
**Distribution check.** The two top rows were opposing phase theses: a slow innings overall, but a fast powerplay. A ball-by-ball resource model ties powerplay scoring to final totals positively. Ranking Under-total with Over-powerplay hedges internally and guarantees neither. Reaching 185 in 16 overs (11.6 runs per over) is a far tail of any reasonable CPL innings distribution. The 31/2 start then 154 from ten overs is a death-overs explosion.
**Knowable at cutoff?** The rain-reduction risk was knowable (weather). The scale of the explosion was not.
**Verdict.** VARIANCE in the outcome, plus a COHERENCE error in slate construction.
**Own-top-2 counterfactual.** A single innings model would have paired Under-total with Under-powerplay (the powerplay Under won), or skipped totals given rain-reduction risk.
**Failure class.** PHASE_INCOHERENCE plus REDUCED_OVERS_RISK_UNMODELLED.
**Proposed correction.** Phase rows must come from one ball-state model, with the reduced-overs/DLS branch printed. Ban opposing-direction phase/total pairs in the top two unless the joint mass of both winning is at least 0.30.

### Final settlement · P-233 · Beijing Guoan vs Lanzhou Longyuan Athletic

**Final settlement (2026-10-09) — Beijing Guoan vs Lanzhou Longyuan Athletic (China FA Cup QF).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Beijing 3-1 Lanzhou (HT 1-0); corners 13 (specialist).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Beijing team goals Over 1.5 | **WIN** | YES | B structured | Beijing 3 |
| 2 | 1st Half Over 0.5 goals | **WIN** | YES | B structured | HT 1-0 |
| 3 | Total goals Over 2.5 | **WIN** | NO (rank 3+ informational) | B structured | Four goals |
| 4 | Both teams to score - No | **LOSS** | NO (rank 3+ informational) | B structured | Both scored |
| 5 | Corners Over 8.5 | **WIN** | NO (rank 3+ informational) | C best-available | Specialist 13; Xinhua terminal corroboration |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-234 · Dalian Yingbo vs Shanghai Shenhua

**Final settlement (2026-10-09) — Dalian Yingbo vs Shanghai Shenhua (China FA Cup QF).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Dalian 1-0 Shenhua (HT 0-0; goalkeeper red card); corners 10 (specialist).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | 1st Half Over 0.5 goals | **LOSS** | NO (loss) | B structured | HT 0-0 |
| 2 | Dalian team goals Over 0.5 | **WIN** | YES | B structured | Dalian 1 |
| 3 | Corners Over 8.5 | **WIN** | NO (rank 3+ informational) | C best-available | Specialist 10 |
| 4 | Both teams to score - Yes | **LOSS** | NO (rank 3+ informational) | B structured | Shenhua 0 |
| 5 | Total goals Over 2.5 | **LOSS** | NO (rank 3+ informational) | B structured | One goal |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: WIN.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was 1st Half Over 0.5 goals at a stated 0.50 (a coin flip at Rank 1).
**What happened.** HT 0-0; Dalian won 1-0 after a goalkeeper red-card disruption. Rank 2 (Dalian team goals Over 0.5) won.
**Distribution check.** A 0.50 probability is disqualifying for Rank 1 by itself. Rank 2 carried the same stated 0.50, so the ordering was arbitrary.
**Knowable at cutoff?** Yes. The stated probability exposed it.
**Verdict.** RANKING_SELECTION error. A no-edge row was given the top slot.
**Own-top-2 counterfactual.** Cup quarterfinals between a lower-tier home side and Shenhua carry heavy Under and draw mass. Under 2.5 (won) and Dalian team Over 0.5 (won) would have been the coherent top two.
**Failure class.** FIRST_HALF_GOAL_OVERSELECTION; NO_EDGE_RANK1.
**Proposed correction.** Hard gate: Rank 1 needs p_card ≥ 0.55 and at least 3 points of separation from Rank 3. Otherwise print RANK1_UNSTABLE and choose by distribution mass.

### Final settlement · P-235 · Shandong Taishan vs Shanghai Port

**Final settlement (2026-10-09) — Shandong Taishan vs Shanghai Port (China FA Cup QF).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Shanghai Port 3-0 at Shandong; corners 14 (specialist).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | 1st Half Over 0.5 goals | **WIN** | YES | B structured | First-half goal |
| 2 | Shanghai Port team goals Over 0.5 | **WIN** | YES | B structured | Port 3 |
| 3 | Both teams to score - Yes | **LOSS** | NO (rank 3+ informational) | B structured | Shandong 0 |
| 4 | Total goals Over 2.5 | **WIN** | NO (rank 3+ informational) | B structured | Three goals |
| 5 | Corners Over 8.5 | **WIN** | NO (rank 3+ informational) | C best-available | Specialist 14 |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-250 · Yunnan Yukun vs Chongqing Tonglianglong

**Final settlement (2026-10-09) — Yunnan Yukun vs Chongqing Tonglianglong (China FA Cup QF).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Yunnan 1-0 Chongqing (HT 0-0); Yunnan advanced; corners not recovered.

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | 1st Half Over 0.5 goals | **LOSS** | NO (loss) | B structured | HT 0-0 |
| 2 | Total corners Over 8.5 | **VOID** | NO (void/push) | X no data | No provider aggregate in any source |
| 3 | Full match Over 2.5 goals | **LOSS** | NO (rank 3+ informational) | B structured | One goal |
| 4 | Full match Under 2.5 goals | **WIN** | NO (rank 3+ informational) | B structured | One goal |
| 5 | 1st Half Under 0.5 goals | **WIN** | NO (rank 3+ informational) | B structured | HT 0-0 |

**Top-two result.** TOP2_ALL_LOST: every live top-two row LOST — **0 counted win(s) of 1 live top-two row(s)**. Rank 1: LOSS; Rank 2: VOID.
**Winner call.** Yunnan Yukun (advance): CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was 1st Half Over 0.5 (LEAN, MEDIUM), citing Yunnan's early-event rate and Chongqing's cup first-half goals. The card's own counter-path cited the May head-to-head 0-0.
**What happened.** HT 0-0; Yunnan won 1-0 and advanced. Rank 2 (corners Over 8.5) was settled VOID for want of any provider. The card counted 0/1.
**Distribution check.** The original deep review already found it: matchup-specific low-event evidence (a 0-0 continuity head-to-head and Chongqing's low-event regime) was named as the main kill path and then underweighted against broad first-half frequencies.
**Knowable at cutoff?** Yes. The kill path was printed before kick-off.
**Verdict.** EVIDENCE_WEIGHTING error.
**Own-top-2 counterfactual.** Full Under 2.5 and Yunnan to advance (both correct) would lead a distribution fitted with head-to-head and opponent shrinkage.
**Failure class.** FIRST_HALF_GOAL_OVERSELECTION; NAMED_KILL_PATH_UNDERWEIGHTED.
**Proposed correction.** When a card names a "main kill path", it must assign that path explicit probability mass in the matrix. If the mass exceeds 0.30, the row cannot be Rank 1.

### Final settlement · P-251 · Sassuolo vs Frosinone

**Final settlement (2026-10-09) — Sassuolo vs Frosinone (Coppa Italia R32).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Sassuolo 1-1 Frosinone after 90 minutes, decided on penalties; corners 6+5=11 (ESPN 401911806).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | 1st Half Over 0.5 goals | **WIN** | YES | B structured | First-half goal |
| 2 | Full match Over 2.5 goals | **LOSS** | NO (loss) | B structured | Two goals in 90 minutes |
| 3 | Corners Over 8.5 | **WIN** | NO (rank 3+ informational) | B structured | ESPN 11 |
| 4 | Full match Under 2.5 goals | **WIN** | NO (rank 3+ informational) | B structured | Two goals |
| 5 | 1st Half Under 0.5 goals | **LOSS** | NO (rank 3+ informational) | B structured | First-half goal |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: LOSS.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-255 · Inter Women vs VfL Wolfsburg Women

**Final settlement (2026-10-09) — Inter Women vs VfL Wolfsburg Women (UWCL third qualifying round, 2nd leg).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Regulation 2-0 Inter; 3-1 after extra time; Wolfsburg through 5-4 on penalties; whole-match corners 12+12=24 incl. ET (UEFA 2049369).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | 1st Half Over 0.5 goals | **WIN** | YES | A owner | UEFA first-half goal |
| 2 | Total corners Over 8.5 (90 minutes) | **WIN** | YES | E estimated bound | 24 corners over 120 minutes; failure needs 16+ corners in 30 minutes of ET (>99% the 90-minute count exceeded 8.5) |
| 3 | Full match Over 2.5 goals | **LOSS** | NO (rank 3+ informational) | A owner | Two goals in regulation |
| 4 | Full match Under 2.5 goals | **WIN** | NO (rank 3+ informational) | A owner | Two goals in regulation |
| 5 | 1st Half Under 0.5 goals | **LOSS** | NO (rank 3+ informational) | A owner | First-half goal |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-256 · Paris Saint-Germain Women vs Eintracht Frankfurt Women

**Final settlement (2026-10-09) — Paris Saint-Germain Women vs Eintracht Frankfurt Women (UWCL third qualifying round, 2nd leg).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Regulation 1-1; PSG 5-1 after extra time (Frankfurt 10 players from 66'); whole-match corners 11+4=15 incl. ET (UEFA 2049367).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Total corners Over 8.5 (90 minutes) | **WIN** | YES | E estimated bound | 15 over 120 minutes; failure needs 7+ in ET. Pro-rata 90-minute expectation 11.3; with PSG ET dominance weighting the estimate stays about 10. Estimated confidence about 75% |
| 2 | 1st Half Over 0.5 goals | **WIN** | YES | A owner | First-half goal |
| 3 | Full match Under 2.5 goals | **WIN** | NO (rank 3+ informational) | A owner | Two goals in regulation |
| 4 | Full match Over 2.5 goals | **LOSS** | NO (rank 3+ informational) | A owner | Two goals in regulation |
| 5 | 1st Half Under 0.5 goals | **LOSS** | NO (rank 3+ informational) | A owner | First-half goal |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-265 · Toluca vs Club Leon

**Final settlement (2026-10-09) — Toluca vs Club Leon (Leagues Cup SF).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Toluca 2-0 Leon (HT 1-0); corners 4+5=9 (ESPN 401914297).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Corners Over 8.5 | **WIN** | YES | B structured | ESPN 9 (first winning integer) |
| 2 | Full match Over 2.5 goals | **LOSS** | NO (loss) | B structured | Two goals |
| 3 | 1st Half Over 0.5 goals | **WIN** | NO (rank 3+ informational) | B structured | HT 1-0 |
| 4 | Full match Under 2.5 goals | **WIN** | NO (rank 3+ informational) | B structured | Two goals |
| 5 | 1st Half Under 0.5 goals | **LOSS** | NO (rank 3+ informational) | B structured | HT 1-0 |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: LOSS.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-274 · San Francisco Giants @ Pittsburgh Pirates

**Final settlement (2026-10-09) — San Francisco Giants @ Pittsburgh Pirates (MLB).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Pirates 5-2 Giants (actual starter Bachar, listed Jared Jones).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Giants +1.5 | **LOSS** | NO (loss) | OP default rule | Sporting proposition settled as action (CURRENT_RULES: missing operator definition does not block sporting settlement); lost by 3 |
| 2 | Pirates moneyline | **WIN** | YES | OP default rule | Pittsburgh won |
| 3 | Over 9.0 runs | **LOSS** | NO (rank 3+ informational) | OP default rule | Seven runs |
| 4 | Under 9.0 runs | **WIN** | NO (rank 3+ informational) | OP default rule | Seven runs |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: WIN.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was Giants +1.5 runs.
**What happened.** Pirates 5-2. The listed starter (Jared Jones) did not start; Bachar did. Rank 2 (Pirates ML) won.
**Distribution check.** An away underdog +1.5 has a structural ceiling: P(win) plus P(lose by exactly 1). About 27-30% of MLB games are decided by one run. A typical road underdog sits near 0.58-0.62 on +1.5, and that bound leaves no large edge.
**Knowable at cutoff?** The starter change was knowable only near first pitch. The ceiling was always knowable.
**Verdict.** CONTRACT_GEOMETRY plus LATE_STARTER_CHANGE. The ranking assumed an edge the geometry does not normally provide.
**Own-top-2 counterfactual.** Pirates ML (won) and Under 9.0 (won) ranked first and second would have given 2/2. Under the own-picks rule, a starter change also triggers a re-run of the run distribution.
**Failure class.** RUNLINE_CUSHION_CEILING (recurs in P-524, P-544 and P-547).
**Proposed correction.** For baseball +1.5 rows, print the decomposition P(win) + P(lose by 1) from a fitted run-difference distribution (Skellam or negative binomial). Rank 1 needs p ≥ 0.65. A confirmed starter change after cutoff must void the card or force a dated re-forecast.

### Final settlement · P-341 · BUL FC vs Ntugasaze FC

**Final settlement (2026-10-09) — BUL FC vs Ntugasaze FC (Uganda Premier League R3).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** BUL 4-1 Ntugasaze (HT 2-1); corners not recovered.

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | 1st Half Over 0.5 goals | **WIN** | YES | B structured | HT 2-1 |
| 2 | Under 2.5 goals | **LOSS** | NO (loss) | B structured | Five goals |
| 3 | Total corners Over 7.5 | **VOID** | NO (rank 3+ informational) | X no data | No provider carries this match |
| 4 | Over 2.5 goals | **WIN** | NO (rank 3+ informational) | B structured | Five goals |
| 5 | 1st Half Under 0.5 goals | **LOSS** | NO (rank 3+ informational) | B structured | HT 2-1 |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: LOSS.
**Winner call.** BUL FC: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-342 · MSK Novohrad Lucenec vs KFC Komarno

**Final settlement (2026-10-09) — MSK Novohrad Lucenec vs KFC Komarno (Slovnaft Cup R3).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Komarno 2-0 Lucenec (HT 0-0; 74', 90'); corners 1-15 (secondary aggregators).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | 1st Half Over 0.5 goals | **LOSS** | NO (loss) | B structured | HT 0-0 |
| 2 | Over 2.5 goals | **LOSS** | NO (loss) | B structured | Two goals |
| 3 | Total corners Over 8.5 | **WIN** | NO (rank 3+ informational) | C best-available | Secondary aggregate 16 |
| 4 | Under 2.5 goals | **WIN** | NO (rank 3+ informational) | B structured | Two goals |
| 5 | 1st Half Under 0.5 goals | **WIN** | NO (rank 3+ informational) | B structured | HT 0-0 |

**Top-two result.** TOP2_ALL_LOST: every live top-two row LOST — **0 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: LOSS.
**Winner call.** KFC Komarno: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was 1st Half Over 0.5 at p 0.68; Rank 2 was Over 2.5 at p 0.56. This was a Slovak cup mismatch with a heavily rotated favourite (Komárno).
**What happened.** HT 0-0; Komárno 2-0 with goals at 74' and 90'. Corners 1-15. Total territorial control, late conversion. Both top rows lost (0/2).
**Distribution check.** The card itself printed "2-0 control, 0-0 at half" as a kill path. The territorial evidence (a corner edge of 15-1) was right; the conversion-timing model was missing.
**Knowable at cutoff?** Yes. The rotation of the favourite was documented.
**Verdict.** MECHANISM error: territory was confused with conversion timing. This was the original cohort's worst-graded card.
**Own-top-2 counterfactual.** Komárno to win (correct) and Over 8.5 corners (won), or Under 2.5 (won). Each follows directly from a dominance-without-finishing model.
**Failure class.** FIRST_HALF_GOAL_OVERSELECTION; ROTATION_CONVERSION_DISCOUNT_MISSING.
**Proposed correction.** For a rotated favourite, apply a conversion discount to the favourite's first-half λ, backed by evidence. Re-rank territorial props (corners, shots) above timing props.

### Final settlement · P-368 · Al Jazira vs Al Nasr

**Final settlement (2026-10-09) — Al Jazira vs Al Nasr (UAE Pro League MW5).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Al Jazira 1-1 Al Nasr (HT 1-0); corners 6-3=9 (FotMob).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | 1st Half Over 0.5 goals | **WIN** | YES | B structured | HT 1-0 |
| 2 | Total corners Over 7.5 | **WIN** | YES | B structured | FotMob 9 |
| 3 | Over 2.5 goals | **LOSS** | NO (rank 3+ informational) | B structured | Two goals |
| 4 | Under 2.5 goals | **WIN** | NO (rank 3+ informational) | B structured | Two goals |
| 5 | 1st Half Under 0.5 goals | **LOSS** | NO (rank 3+ informational) | B structured | HT 1-0 |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-369 · Dubai United vs Shabab Al Ahli

**Final settlement (2026-10-09) — Dubai United vs Shabab Al Ahli (UAE Pro League MW5).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Dubai United 1-1 Shabab Al Ahli (HT 0-0); corners 5-6=11 (FotMob).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Total corners Under 10.5 | **LOSS** | NO (loss) | B structured | FotMob 11 |
| 2 | 1st Half Over 0.5 goals | **LOSS** | NO (loss) | B structured | HT 0-0 |
| 3 | Over 2.5 goals | **LOSS** | NO (rank 3+ informational) | B structured | Two goals |
| 4 | Under 2.5 goals | **WIN** | NO (rank 3+ informational) | B structured | Two goals |
| 5 | 1st Half Under 0.5 goals | **WIN** | NO (rank 3+ informational) | B structured | HT 0-0 |

**Top-two result.** TOP2_ALL_LOST: every live top-two row LOST — **0 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: LOSS.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was total corners Under 10.5 at p 0.68, with no frozen corner provider.
**What happened.** FotMob corners 5-6 = 11, so the Under lost by one corner. Rank 2 (1H Over 0.5) also lost (HT 0-0). The card scored 0/2.
**Distribution check.** Corner counts are overdispersed (variance about 1.3-1.6 times the mean). With a mean near 9.5 and negative-binomial width, P(≤10) is about 0.62-0.66. The 0.68 was mildly optimistic, and the outcome sat one integer past the line: close to ordinary variance.
**Knowable at cutoff?** The provider gap was known. Score-state effects (a 1-1 game with late chasing) add corners and were not modelled.
**Verdict.** VARIANCE with a provider-governance defect. The miss was by the minimum possible margin.
**Own-top-2 counterfactual.** Under 2.5 (won, at 1-1) and 1H Under 0.5 (won) both carry more mass for a low-shot, low-xG fixture.
**Failure class.** CORNER_ROW_WITHOUT_PROVIDER_OR_NB_MODEL.
**Proposed correction.** Corner rows require a registered provider and a negative-binomial count model with score-state adjustment. Without both, cap p at 0.60, which removes them from Rank 1.

### Final settlement · P-377 · Xelaju MC vs Coban Imperial

**Final settlement (2026-10-09) — Xelaju MC vs Coban Imperial (Guatemala Liga Nacional Apertura).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Xelaju 0-0 Coban; corners 7 (secondary).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | 1st Half Over 0.5 goals | **LOSS** | NO (loss) | B structured | HT 0-0 |
| 2 | Over 8.5 total corners | **LOSS** | NO (loss) | C best-available | Secondary 7; inherited research LOSS adopted |
| 3 | Over 2.5 goals | **LOSS** | NO (rank 3+ informational) | B structured | No goals |
| 4 | Under 2.5 goals | **WIN** | NO (rank 3+ informational) | B structured | No goals |
| 5 | 1st Half Under 0.5 goals | **WIN** | NO (rank 3+ informational) | B structured | HT 0-0 |

**Top-two result.** TOP2_ALL_LOST: every live top-two row LOST — **0 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: LOSS.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was 1st Half Over 0.5 at a stated 68% (UNVALIDATED_SUBJECTIVE).
**What happened.** Xelajú 0-0 Cobán; corners 7, so Rank 2 (Over 8.5 corners) also lost. The card scored 0/2.
**Distribution check.** Guatemala's Liga Nacional has a goals-per-game environment lower than the European priors implicitly used, so the first-half goal base rate falls toward 0.60-0.65. Xelajú's home at altitude also slows tempo.
**Knowable at cutoff?** Yes. League-specific base rates were not printed.
**Verdict.** BASE_RATE_TRANSFER error (European first-half priors applied to a lower-scoring league) plus FIRST_HALF_GOAL_OVERSELECTION.
**Own-top-2 counterfactual.** Under 2.5 (won) and 1H Under 0.5 (won) under a league-calibrated matrix gives 2/2.
**Failure class.** FIRST_HALF_GOAL_OVERSELECTION; LEAGUE_BASE_RATE_MISSING.
**Proposed correction.** BASE_RATES_REGISTER must hold per-league first-half and full-time goal rates estimated from the Previous Sports Results archive. A card without its league's base rate cannot use goal-timing rows at Rank 1.

### Final settlement · P-399 · Genoa vs Frosinone

**Final settlement (2026-10-09) — Genoa vs Frosinone (Serie A).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Genoa 1-1 Frosinone; corners 8+9=17 (ESPN 401874991).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | 1st Half Over 0.5 goals | **WIN** | YES | B structured | First-half goal |
| 2 | Combined corners Over 8.5 | **WIN** | YES | B structured | ESPN 17 |
| 3 | Full time Under 2.5 | **WIN** | NO (rank 3+ informational) | B structured | Two goals |
| 4 | Full time Over 2.5 | **LOSS** | NO (rank 3+ informational) | B structured | Two goals |
| 5 | 1st Half Under 0.5 goals | **LOSS** | NO (rank 3+ informational) | B structured | First-half goal |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-401 · IFK Goteborg vs Halmstads BK

**Final settlement (2026-10-09) — IFK Goteborg vs Halmstads BK (Allsvenskan).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** IFK 2-1 Halmstad (12 Sep, not 13 Sep); corners 8+9=17, IFK 8 (ESPN 401874088).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Combined corners Over 8.5 | **WIN** | YES | B structured | ESPN 17 |
| 2 | Halmstad team total Under 1.5 | **WIN** | YES | B structured | Halmstad 1 |
| 3 | IFK team corners Over 4.5 | **WIN** | NO (rank 3+ informational) | B structured | ESPN IFK 8 |
| 4 | 1st Half Under 0.5 goals | **LOSS** | NO (rank 3+ informational) | B structured | First-half goal |
| 5 | Full time Over 2.5 | **WIN** | NO (rank 3+ informational) | B structured | Three goals |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-407 · Club Brugge vs Royal Antwerp

**Final settlement (2026-10-09) — Club Brugge vs Royal Antwerp (Belgian Pro League).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Club Brugge 3-1 Antwerp (HT 1-1); corners Brugge 9, Antwerp 4 (league/Opta).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Club Brugge team corners Over 4.5 | **WIN** | YES | A owner | Owner 9 (the rank index's blank-contract 'P' literal is a mapping defect, not a push) |
| 2 | Royal Antwerp team goals Under 1.5 | **WIN** | YES | A owner | Antwerp 1 |
| 3 | 1st Half Over 0.5 goals | **WIN** | NO (rank 3+ informational) | A owner | HT 1-1 |
| 4 | Full match Under 3.5 goals | **LOSS** | NO (rank 3+ informational) | A owner | Four goals |
| 5 | Full match Over 2.5 goals | **WIN** | NO (rank 3+ informational) | A owner | Four goals |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-409 · Lille OSC vs ESTAC Troyes

**Final settlement (2026-10-09) — Lille OSC vs ESTAC Troyes (Ligue 1 MW4).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Lille 2-0 Troyes (18', 90+3'); corners Lille 2, Troyes 5 (ESPN 401876462).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Lille team goals Over 0.5 | **WIN** | YES | B structured | Lille 2 |
| 2 | Troyes team corners Over 2.5 | **WIN** | YES | B structured | ESPN 5 (index 'P' literal is a mapping defect) |
| 3 | Lille or Draw (90 min) | **WIN** | NO (rank 3+ informational) | B structured | Lille won |
| 4 | 1st Half Over 0.5 goals | **WIN** | NO (rank 3+ informational) | B structured | 18' goal |
| 5 | Full match Under 3.5 goals | **WIN** | NO (rank 3+ informational) | B structured | Two goals |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** Lille: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-410 · RB Leipzig vs Hamburger SV

**Final settlement (2026-10-09) — RB Leipzig vs Hamburger SV (Bundesliga MD3).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Leipzig 5-0 Hamburg (HT 2-0); DFL corners 7-7.

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | RB Leipzig team goals Over 0.5 | **WIN** | YES | A owner | Leipzig 5 |
| 2 | RB Leipzig or Draw (90 min) | **WIN** | YES | A owner | Leipzig won |
| 3 | Hamburger SV team goals Under 1.5 | **WIN** | NO (rank 3+ informational) | A owner | Hamburg 0 |
| 4 | 1st Half Over 0.5 goals | **WIN** | NO (rank 3+ informational) | A owner | HT 2-0 |
| 5 | RB Leipzig team corners Over 4.5 | **WIN** | NO (rank 3+ informational) | A owner | DFL 7 (index 'P' literal is a mapping defect) |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-418 · Drukpa FC vs Royal Thimphu College FC

**Final settlement (2026-10-09) — Drukpa FC vs Royal Thimphu College FC (Bhutan Premier League).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** RSSSF (single secondary, updated 25 Sep) lists 14 Sep Drukpa 1-3 RTC; federation page stale; original ranked contracts not preserved anywhere in the repository or its history.

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| — | Original ranked contracts not preserved | **VOID** | NO (contract not preserved) | X no data | No contract text survives; a sporting final cannot be mapped onto an unknown proposition |

**Top-two result.** VOID: no live top-two row (VOID card) — **0 counted win(s) of 0 live top-two row(s)**. Rank 1: VOID; Rank 2: VOID.
**Winner call.** NOT_PRESERVED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 was VOID**, so there is no performance result and no mandatory deep retrospection.

### Final settlement · P-419 · Djurgardens IF vs GAIS

**Final settlement (2026-10-09) — Djurgardens IF vs GAIS (Allsvenskan MW21).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Djurgarden 2-0 GAIS (35', 63'; three red cards); corners 2-2=4 (ESPN 401873992).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Djurgarden team goals Over 0.5 | **WIN** | YES | B structured | Djurgarden 2 |
| 2 | Djurgarden or Draw (1X) | **WIN** | YES | B structured | Djurgarden won |
| 3 | GAIS team goals Under 1.5 | **WIN** | NO (rank 3+ informational) | B structured | GAIS 0 |
| 4 | Under 3.5 total goals | **WIN** | NO (rank 3+ informational) | B structured | Two goals |
| 5 | Total corners Over 7.5 (self-generated alternate) | **LOSS** | NO (rank 3+ informational) | B structured | ESPN 4 (index 'P' literal is a mapping defect) |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** Djurgarden: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-430 · Al Ain vs Al Nassr

**Final settlement (2026-10-09) — Al Ain vs Al Nassr (AFC Champions League Elite MD1).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Al Ain 4-0 Al Nassr (HT 1-0); corners Al Ain 2, Al Nassr 10 (ESPN 401912656).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Al Nassr team total Over 0.5 | **LOSS** | NO (loss) | A owner | Al Nassr 0 |
| 2 | Match Over 1.5 goals | **WIN** | YES | A owner | Four goals |
| 3 | 1st Half Over 0.5 goals | **WIN** | NO (rank 3+ informational) | A owner | HT 1-0 |
| 4 | Al Nassr +0.5 / X2 | **LOSS** | NO (rank 3+ informational) | A owner | Al Ain won |
| 5 | Al Ain team corners Over 3.5 | **LOSS** | NO (rank 3+ informational) | B structured | ESPN Al Ain 2 (index 'P' literal is a mapping defect) |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: WIN.
**Winner call.** Al Nassr: INCORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was Al Nassr team total Over 0.5 at p 0.85; Al Nassr was the potential winner.
**What happened.** Al Ain 4-0. Al Nassr had 15 shots and 10 corners but did not score. Rank 2 (Match Over 1.5) won.
**Distribution check.** At p 0.85, P(0 goals) = 0.15 implies λ ≈ 1.9 for Al Nassr away at Al Ain in the ACLE. That is a top-team home rate, not an away rate against a strong host. A realistic λ of 1.3-1.5 gives P(score) ≈ 0.73-0.78.
**Knowable at cutoff?** Yes. No official XI or bench had been retrieved, and the original review called the 85% "too assertive".
**Verdict.** PROBABILITY_EXTREMITY under unresolved participant state.
**Own-top-2 counterfactual.** Match Over 1.5 (won) and 1H Over 0.5 (won) both rank higher once Al Nassr's λ is shrunk.
**Failure class.** OVERCONFIDENT_TEAM_TOTAL.
**Proposed correction.** Cap any single-team "to score" row at 0.80 unless both XIs are confirmed and the λ is fitted. Display the implied λ next to every team-total probability.

### Final settlement · P-492 · San Diego Padres @ Los Angeles Dodgers

**Final settlement (2026-10-09) — San Diego Padres @ Los Angeles Dodgers (MLB).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Dodgers 7-0 Padres.

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Michael King Over 14.5 pitching outs | **LOSS** | NO (loss) | A owner | MLB owner player 650633: 12 outs (4.0 IP) |
| 2 | San Diego +1.5 | **LOSS** | NO (loss) | B structured | Lost by 7 |
| 3 | Los Angeles moneyline | **WIN** | NO (rank 3+ informational) | B structured | Dodgers won |
| 4 | Over 8.5 runs | **LOSS** | NO (rank 3+ informational) | B structured | Seven runs |

**Top-two result.** TOP2_ALL_LOST: every live top-two row LOST — **0 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: LOSS.
**Winner call.** Los Angeles Dodgers: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was Michael King Over 14.5 pitching outs; Rank 2 was Padres +1.5.
**What happened.** Dodgers 7-0. King got 12 outs (4.0 IP, 81 pitches, five runs). Both top rows lost (0/2).
**Distribution check.** A starter-outs prop and a team cushion share one driver: the starter's early run prevention. When King was hit, both failed together. The original review already noted the shared removal pathway.
**Knowable at cutoff?** The dependence was knowable. Its realisation was variance.
**Verdict.** TOP_ROW_DEPENDENCE. The top two were one bet on King.
**Own-top-2 counterfactual.** Dodgers ML (won) and Under 8.5 (won at 7) are less correlated with the King thesis.
**Failure class.** SHARED_DRIVER_TOP_TWO.
**Proposed correction.** Compute the joint top-two failure probability by simulation. If it exceeds 0.30, replace Rank 2 with the best row whose correlation with Rank 1 is below 0.3.

### Final settlement · P-518 · New York Mets @ Washington Nationals

**Final settlement (2026-10-09) — New York Mets @ Washington Nationals (MLB).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Mets 7-1 Nationals (gamePk 822678).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Mets +1.5 | **WIN** | YES | A owner | Mets won by 6 |
| 2 | Nationals +1.5 | **LOSS** | NO (loss) | A owner | Nationals lost by 6 |
| 3 | Over 8.5 runs | **LOSS** | NO (rank 3+ informational) | A owner | Eight runs |
| 4 | Under 8.5 runs | **WIN** | NO (rank 3+ informational) | A owner | Eight runs |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: LOSS.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-519 · Gold Coast Suns vs St Kilda (AFLW)

**Final settlement (2026-10-09) — Gold Coast Suns vs St Kilda (AFLW) (AFLW).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Gold Coast 69-39 St Kilda (AFLW match 8942; total 108, margin +30). The original card's claimed 50-22 final is a rejected fabrication.

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Total Under 89.5 | **LOSS** | NO (loss) | A owner | Total 108 |
| 2 | Gold Coast -27.5 | **WIN** | YES | A owner | Margin +30 |
| 3 | St Kilda +27.5 | **LOSS** | NO (rank 3+ informational) | A owner | Margin -30 |
| 4 | Total Over 89.5 | **WIN** | NO (rank 3+ informational) | A owner | Total 108 |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: WIN.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was AFLW total Under 89.5 at p 0.719 (q 0.780). Rank 2 was Suns -27.5 at p 0.449 (q 0.731).
**What happened.** Gold Coast 69-39 St Kilda (total 108, margin +30). Rank 1 lost; Rank 2 won. The original card's claimed 50-22 settlement was fabricated and later rejected against the AFLW match centre.
**Distribution check.** Rank 2's p (0.449) was below Rank 3's p (0.551), its complement on the same margin. The slate was ordered by q, a ranking score, not by probability: an inversion. On the totals side, 0.719 for Under 89.5 was too extreme for a 2026 AFLW total, given the variance of quarter scoring.
**Knowable at cutoff?** Yes. Ordering by q is a process defect visible in the card.
**Verdict.** RANK_BY_Q_NOT_P plus OVERCONFIDENT_TOTAL, plus a fabricated settlement in the original record.
**Own-top-2 counterfactual.** Ordering by p gives St Kilda +27.5 (0.551, lost) then Under (0.719, lost). The issue here is the total's distribution. A fitted AFLW scoring-shot model with a 2026 era mean would have centred higher.
**Failure class.** RANK_BY_Q_NOT_P; FABRICATED_SETTLEMENT_RECORD.
**Proposed correction.** The validator must reject any card where rank order is not non-increasing in p_card. Settlement text must cite an owner match ID whose score fields are machine-checked.

### Final settlement · P-520 · Hanwha Eagles @ Lotte Giants

**Final settlement (2026-10-09) — Hanwha Eagles @ Lotte Giants (KBO).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Hanwha 6-2 Lotte (owner game 20260927HHLT0).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Lotte Giants moneyline | **LOSS** | NO (loss) | A owner | Hanwha won |
| 2 | Hanwha Eagles +1.5 | **WIN** | YES | A owner | Hanwha won |
| 3 | Over 10.5 runs | **LOSS** | NO (rank 3+ informational) | A owner | Eight runs |
| 4 | Under 10.5 runs | **WIN** | NO (rank 3+ informational) | A owner | Eight runs |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: WIN.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was Lotte Giants ML at p 0.577; Rank 2 was Hanwha +1.5 at 0.520.
**What happened.** Hanwha 6-2 (three first-inning runs). Rank 2 won.
**Distribution check.** A 0.577 moneyline is roughly a 58/42 game: Lotte loses about 42% of the time. A 0.52 Rank 2 is a coin flip. This slate had no strong row.
**Knowable at cutoff?** The weakness of the slate was visible.
**Verdict.** VARIANCE on a weak slate; RANK1_INSTABILITY.
**Own-top-2 counterfactual.** The four supplied rows were near-even, so a coherent run model would print RANK1_UNSTABLE. Its strongest-mass row would likely be Under 10.5 (won at 8 runs) with Hanwha +1.5.
**Failure class.** WEAK_SLATE_FORCED_RANK.
**Proposed correction.** When no row exceeds 0.58, label the card LOW_EDGE_SLATE, and score its Rank 1 separately so these do not dilute evaluation of strong-slate cards.

### Final settlement · P-521 · Rio Breogan vs Joventut

**Final settlement (2026-10-09) — Rio Breogan vs Joventut (Liga ACB).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Breogan 110-104 Joventut (ACB 105378; total 214, Breogan +6).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Joventut -5.5 | **LOSS** | NO (loss) | A owner | Joventut lost by 6 |
| 2 | Over 179.5 | **WIN** | YES | A owner | Total 214 |
| 3 | Under 179.5 | **LOSS** | NO (rank 3+ informational) | A owner | Total 214 |
| 4 | Breogan +5.5 | **WIN** | NO (rank 3+ informational) | A owner | Breogan won |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: WIN.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was Joventut -5.5 at **p 0.408** (q 0.677). Rank 4 was its near-complement, Breogán +5.5, at p 0.592.
**What happened.** Breogán 110-104. Rank 1 lost; Rank 2 (Over 179.5) won with 214 points.
**Distribution check.** The card's own probability said Rank 1 would lose 59% of the time. This is the clearest q-versus-p inversion in the cohort: the forecast was internally correct (Breogán +5.5 more likely) and the ranking contradicted it.
**Knowable at cutoff?** Yes. It was printed on the card.
**Verdict.** RANK_BY_Q_NOT_P. A pure process failure; the probability layer was right.
**Own-top-2 counterfactual.** Ordering by p: Breogán +5.5 (0.592, won) and Over 179.5 (0.538, won) gives 2/2.
**Failure class.** RANK_BY_Q_NOT_P.
**Proposed correction.** Same validator as P-519. Add a regression test that loads every historical card with p and q and flags inversions.

### Final settlement · P-522 · La Laguna Tenerife vs Casademont Zaragoza

**Final settlement (2026-10-09) — La Laguna Tenerife vs Casademont Zaragoza (Liga ACB).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Tenerife 80-81 Zaragoza (ACB 105380; total 161).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Combined total Over 169.5 | **LOSS** | NO (loss) | A owner | Total 161 |
| 2 | Tenerife -3.5 | **LOSS** | NO (loss) | A owner | Tenerife lost by 1 |
| 3 | Combined total Over 179.5 | **LOSS** | NO (rank 3+ informational) | A owner | Total 161 |
| 4 | Zaragoza +9.5 | **WIN** | NO (rank 3+ informational) | A owner | Zaragoza won |

**Top-two result.** TOP2_ALL_LOST: every live top-two row LOST — **0 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: LOSS.
**Winner call.** NOT_RECOVERED: NOT_AUDITED.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was Over 169.5 at p 0.667; Rank 2 was Tenerife -3.5 at 0.553. Rank 4 (Zaragoza +9.5) had p 0.605, above Rank 2.
**What happened.** Tenerife 80-81 Zaragoza (total 161). Ranks 1-3 lost; only Zaragoza +9.5 won. The card scored 0/2.
**Distribution check.** The Over 169.5 (0.667) and the Over 179.5 (0.457) imply P(170-179) ≈ 0.21. Under a normal total that means SD ≈ 18.6 around a centre near 177.5. The actual 161 is about -0.9 SD, ordinary variance. Rank 4's higher p than Rank 2 is another inversion.
**Knowable at cutoff?** The inversion was. The low total was variance plus missing early-season pace shrinkage.
**Verdict.** RANK_BY_Q_NOT_P plus VARIANCE.
**Own-top-2 counterfactual.** By p: Over 169.5 (lost), then Zaragoza +9.5 (won), giving 1/2.
**Failure class.** RANK_BY_Q_NOT_P.
**Proposed correction.** Same validator. Also derive totals rows from a possessions × efficiency model with early-season shrinkage to the prior-season league pace.

### Final settlement · P-538 · Florida Panthers @ Los Angeles Kings

**Final settlement (2026-10-09) — Florida Panthers @ Los Angeles Kings (NHL).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Florida 2-1 Los Angeles (regulation).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Panthers moneyline | **WIN** | YES | A owner | Florida won |
| 2 | Full-game Under 5.5 | **WIN** | YES | A owner | Three goals |
| 3 | Kings moneyline | **LOSS** | NO (rank 3+ informational) | A owner | Kings lost |
| 4 | Full-game Over 5.5 | **LOSS** | NO (rank 3+ informational) | A owner | Three goals |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** Florida Panthers: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-539 · Aleksandar Kovacevic vs Matteo Berrettini

**Final settlement (2026-10-09) — Aleksandar Kovacevic vs Matteo Berrettini (ATP Shanghai R128).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Berrettini 6-7(3), 6-1, 6-4 (games 18-12, total 30).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Berrettini -2.5 games | **WIN** | YES | A owner | +6 games |
| 2 | Under 24.5 games | **LOSS** | NO (loss) | A owner | 30 games |
| 3 | Kovacevic +2.5 games | **LOSS** | NO (rank 3+ informational) | A owner | -6 games |
| 4 | Over 24.5 games | **WIN** | NO (rank 3+ informational) | A owner | 30 games |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: LOSS.
**Winner call.** Matteo Berrettini: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-540 · Adrian Mannarino vs Nikoloz Basilashvili

**Final settlement (2026-10-09) — Adrian Mannarino vs Nikoloz Basilashvili (ATP Shanghai R128).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Mannarino advanced 6-3, 2-2 ret. (13 games).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Mannarino -0.5 games | **VOID** | NO (void/push) | OP default rule | RULES_TENNIS retirement convention voids games rows; +3 at the stop is not a completed-match margin |
| 2 | Over 22.5 games | **VOID** | NO (void/push) | OP default rule | Retirement convention; 13 games |
| 3 | Basilashvili +0.5 games | **VOID** | NO (rank 3+ informational) | OP default rule | Retirement convention |
| 4 | Under 22.5 games | **VOID** | NO (rank 3+ informational) | OP default rule | Retirement convention |

**Top-two result.** VOID: no live top-two row (VOID card) — **0 counted win(s) of 0 live top-two row(s)**. Rank 1: VOID; Rank 2: VOID.
**Winner call.** Adrian Mannarino: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 was VOID**, so there is no performance result and no mandatory deep retrospection.

### Final settlement · P-541 · Mattia Bellucci vs Yi Zhou

**Final settlement (2026-10-09) — Mattia Bellucci vs Yi Zhou (ATP Shanghai R128).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Yi Zhou 6-4, 3-6, 7-6(4) (games 16-16, total 32).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Bellucci -3.5 games | **LOSS** | NO (loss) | A owner | Games level 16-16 |
| 2 | Under 21.5 games | **LOSS** | NO (loss) | A owner | 32 games |
| 3 | Over 21.5 games | **WIN** | NO (rank 3+ informational) | A owner | 32 games |
| 4 | Yi Zhou match winner | **WIN** | NO (rank 3+ informational) | A owner | Zhou won |

**Top-two result.** TOP2_ALL_LOST: every live top-two row LOST — **0 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: LOSS.
**Winner call.** Mattia Bellucci: INCORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was Bellucci -3.5 games at 62.0% and Rank 2 was Under 21.5 games at 54.0%. Bellucci was the potential winner at 77.0% (hard-court Elo benchmark about 81.6%).
**What happened.** Yi Zhou won 6-4, 3-6, 7-6(4); games were level 16-16 over 32 games. The card scored 0/2 and the winner call was incorrect.
**Distribution check.** Both top rows needed the same branch: Bellucci winning comfortably in straight sets. The card's 23% upset branch and its "close Bellucci win" branch each defeat both rows. Roughly, P(both lose) ≈ P(Zhou wins) + P(Bellucci wins in three sets) ≈ 0.23 + 0.20 ≈ 0.4. The pair was close to a single bet. The upset itself was a 23% event: real, but not a tail.
**Knowable at cutoff?** The dependence was knowable. The upset was variance. The card also recorded Bellucci workload concerns and Zhou's freshness, the stated upset mechanisms, without widening the distribution.
**Verdict.** VARIANCE on Rank 1, plus TOP_ROW_DEPENDENCE that turned one miss into 0/2.
**Own-top-2 counterfactual.** The max-mass row on this distribution is Bellucci ML (77%), which also lost. A diversified own top two of Bellucci -3.5 and Over 21.5 (46%, won) would have scored 1/2. The lesson is diversification, not a better single pick.
**Failure class.** TOP_ROW_DEPENDENCE; TENNIS_WORKLOAD_UNMODELLED.
**Proposed correction.** Run the joint top-two failure check (simulate both rows on one tree). Model workload as a negative shift in the match-level serve-probability random effect, not as narrative only.

### Final settlement · P-542 · Adelaide 36ers vs Melbourne United

**Final settlement (2026-10-09) — Adelaide 36ers vs Melbourne United (NBL27 R4).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Melbourne 96-91 Adelaide (total 187).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Under 187.5 | **WIN** | YES | A owner | Total 187 |
| 2 | Adelaide +9.0 | **WIN** | YES | A owner | Lost by 5 |
| 3 | Over 175.5 | **WIN** | NO (rank 3+ informational) | A owner | Total 187 |
| 4 | Melbourne -1.5 | **WIN** | NO (rank 3+ informational) | A owner | Won by 5 |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** Melbourne United: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-543 · Hiroshima Toyo Carp @ Hanshin Tigers

**Final settlement (2026-10-09) — Hiroshima Toyo Carp @ Hanshin Tigers (NPB).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Hanshin 2-1 Hiroshima in 11 innings (1-1 after nine).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Carp +1.5 | **WIN** | YES | A owner | Lost by 1 |
| 2 | Hanshin win | **WIN** | YES | A owner | Hanshin won |
| 3 | Under 5.5 runs | **WIN** | NO (rank 3+ informational) | A owner | Three runs |
| 4 | Over 5.5 runs | **LOSS** | NO (rank 3+ informational) | A owner | Three runs |

**Top-two result.** TOP2_ALL_WON: every live top-two row WON — **2 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: WIN.
**Winner call.** Hanshin Tigers: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-544 · Doosan Bears @ LG Twins

**Final settlement (2026-10-09) — Doosan Bears @ LG Twins (KBO).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** LG 7-5 Doosan (nine innings, total 12).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Doosan +1.5 | **LOSS** | NO (loss) | A owner | Lost by 2 |
| 2 | LG +0.5 (LG win) | **WIN** | YES | A owner | LG won |
| 3 | Over 7.5 runs | **WIN** | NO (rank 3+ informational) | A owner | Twelve runs |
| 4 | Under 7.5 runs | **LOSS** | NO (rank 3+ informational) | A owner | Twelve runs |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: WIN.
**Winner call.** LG Twins: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was Doosan +1.5 at 62.7%, on Choi's start and the league-best Doosan staff. Rank 2 was LG win (+0.5).
**What happened.** LG 7-5 (12 runs). Doosan lost by 2. Rank 2 won.
**Distribution check.** Away underdog +1.5 ceiling as for P-274 and P-524: about 0.45 + 0.55×0.28 ≈ 0.60. The stated 62.7% sat at the ceiling. The 12-run game, against a starter-quality thesis, reached the bullpen-transition tail the card named.
**Knowable at cutoff?** The geometry was.
**Verdict.** RUNLINE_CUSHION_CEILING.
**Own-top-2 counterfactual.** LG win (won) and Over 7.5 (won; the card's 51.6% plus the transition tail) gives 2/2.
**Failure class.** RUNLINE_CUSHION_CEILING.
**Proposed correction.** As P-274: print the decomposition and require p ≥ 0.65 for a +1.5 at Rank 1.

### Final settlement · P-545 · Hanwha Eagles @ Kiwoom Heroes

**Final settlement (2026-10-09) — Hanwha Eagles @ Kiwoom Heroes (KBO).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Kiwoom 5-3 Hanwha (total 8).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Kiwoom +2.5 | **WIN** | YES | A owner | Kiwoom won |
| 2 | Over 9.5 runs | **LOSS** | NO (loss) | A owner | Eight runs |
| 3 | Hanwha moneyline | **LOSS** | NO (rank 3+ informational) | A owner | Hanwha lost |
| 4 | Under 9.5 runs | **WIN** | NO (rank 3+ informational) | A owner | Eight runs |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: LOSS.
**Winner call.** Hanwha Eagles: INCORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-546 · Samsung Lions @ KT Wiz

**Final settlement (2026-10-09) — Samsung Lions @ KT Wiz (KBO).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** KT 9-3 Samsung (total 12).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | KT +1.5 | **WIN** | YES | A owner | KT won by 6 |
| 2 | Samsung +1.5 | **LOSS** | NO (loss) | A owner | Samsung lost by 6 |
| 3 | Over 9.5 runs | **WIN** | NO (rank 3+ informational) | A owner | Twelve runs |
| 4 | Under 9.5 runs | **LOSS** | NO (rank 3+ informational) | A owner | Twelve runs |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: WIN; Rank 2: LOSS.
**Winner call.** KT Wiz: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Rank 1 won**, so no mandatory deep retrospection is triggered.

### Final settlement · P-547 · NC Dinos @ SSG Landers

**Final settlement (2026-10-09) — NC Dinos @ SSG Landers (KBO).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** SSG 6-3 NC (total 9).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | NC +1.5 | **LOSS** | NO (loss) | A owner | Lost by 3 |
| 2 | SSG moneyline | **WIN** | YES | A owner | SSG won |
| 3 | Over 9.5 runs | **LOSS** | NO (rank 3+ informational) | A owner | Nine runs |
| 4 | Under 9.5 runs | **WIN** | NO (rank 3+ informational) | A owner | Nine runs |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: WIN.
**Winner call.** SSG Landers: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was NC +1.5 at 61.8%. Rank 2 was SSG ML at 56.0%, the potential winner.
**What happened.** SSG 6-3 (9 runs). NC lost by 3. Rank 2 won and the winner call was correct.
**Distribution check.** The card favoured SSG to win (56%) and also ranked NC +1.5 first. That is coherent (0.44 + 0.56×0.31 ≈ 0.61), but it puts a ceiling-level cushion ahead of the side the card actually believed in. The Munhak run environment (10.45 runs per game) widens the margin distribution and lowers one-run mass: high-scoring parks produce fewer one-run games.
**Knowable at cutoff?** Yes. The park run environment was printed on the card.
**Verdict.** RUNLINE_CUSHION_CEILING worsened by a HIGH_RUN_ENVIRONMENT_MARGIN_WIDENING the card did not apply.
**Own-top-2 counterfactual.** SSG ML (won) and Under 9.5 (won at 9) gives 2/2.
**Failure class.** RUNLINE_CUSHION_CEILING.
**Proposed correction.** Make the one-run share a function of the expected total, estimated from the KBO archive, instead of a flat 27.7%.

### Final settlement · P-548 · Busan KCC Egis vs Daegu KOGAS Pegasus

**Final settlement (2026-10-09) — Busan KCC Egis vs Daegu KOGAS Pegasus (Korea KBL).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** KCC 103-98 KOGAS (regulation total 201, KCC +5).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Under 178.5 | **LOSS** | NO (loss) | A owner | Total 201 |
| 2 | Korea Gas +8.5 | **WIN** | YES | A owner | Lost by 5 |
| 3 | Over 168.5 | **WIN** | NO (rank 3+ informational) | A owner | Total 201 |
| 4 | KCC -2.5 | **WIN** | NO (rank 3+ informational) | A owner | Won by 5 |

**Top-two result.** TOP2_SPLIT: one of the two live top-two rows WON — **1 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: WIN.
**Winner call.** Busan KCC Egis: CORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was Under 178.5 at 64.5%, on a 172-point centre. KCC was the potential winner (correct).
**What happened.** KCC 103-98 (total 201, 22.5 over the line). Rank 2 (KOGAS +8.5) won.
**Distribution check.** A 64.5% Under 178.5 on a 172 centre implies SD ≈ 17. The result is +1.7 SD, about a 5% tail. The card recorded KCC's "extreme game-to-game variance" and the KBL's 2026-27 foreign-player rule change, both reasons to widen the distribution further, which would have pulled the Under toward 0.60.
**Knowable at cutoff?** Partly. Uncertainty about the scoring regime was documented, but the centre was not shifted.
**Verdict.** VARIANCE on a mis-centred, under-wide distribution. The regime change should have moved the mean, not just the width.
**Own-top-2 counterfactual.** KOGAS +8.5 (won) and KCC -2.5 (won) carry more mass than a regime-uncertain total, giving 2/2.
**Failure class.** BASKETBALL_TOTAL_WITHOUT_PACE_MODEL; RULE_CHANGE_REGIME_SHIFT.
**Proposed correction.** When a league changes a rule mid-season or pre-season, hold totals out of Rank 1 until 5+ games of the new regime have been observed, or use a change-point prior.

### Final settlement · P-549 · Foshan Nanshi vs Guangxi Hengchen

**Final settlement (2026-10-09) — Foshan Nanshi vs Guangxi Hengchen (China League One).** Settled under the user's 2026-10-09 directive: every pending record is settled, with missing details settled on the best available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.

**Final event.** Foshan 1-0 Guangxi (HT 0-0).

| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |
|---:|---|---|---|---|---|
| 1 | Guangxi double chance X2 | **LOSS** | NO (loss) | A owner | Foshan won |
| 2 | Guangxi team Over 0.5 goals | **LOSS** | NO (loss) | A owner | Guangxi 0 |
| 3 | Under 3.5 goals | **WIN** | NO (rank 3+ informational) | A owner | One goal |
| 4 | 1st Half Over 0.5 goals | **LOSS** | NO (rank 3+ informational) | A owner | HT 0-0 |
| 5 | Under 2.5 goals | **WIN** | NO (rank 3+ informational) | A owner | One goal |

**Top-two result.** TOP2_ALL_LOST: every live top-two row LOST — **0 counted win(s) of 2 live top-two row(s)**. Rank 1: LOSS; Rank 2: LOSS.
**Winner call.** Guangxi Hengchen: INCORRECT.
**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is a research-ledger closure, not operator certification.

**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** Rank 1 was Guangxi double chance (X2) at 81.85%; Rank 2 was Guangxi team Over 0.5 at 79.81%. Both came from a Poisson matrix with Guangxi λ 1.60.
**What happened.** Foshan 1-0 (HT 0-0). Both top rows lost (0/2); winner call incorrect.
**Distribution check.** The two rows are very strongly dependent: Guangxi failing to score drives both. Under the card's own matrix, P(both lose) = P(Foshan win with Guangxi 0) ≈ 0.10-0.12. The ranked pair offered almost no diversification. A λ of 1.60 away for a second-placed side is plausible. The card noted Guangxi's two latest away wins were 1-0 with 0-0 halves, evidence of a lower away λ (about 1.2-1.3) that was not used.
**Knowable at cutoff?** The dependence and the low away λ were both printed.
**Verdict.** TOP_ROW_DEPENDENCE plus EVIDENCE_WEIGHTING.
**Own-top-2 counterfactual.** Under 3.5 (won) and Under 2.5 (won), both positively related to a low-λ reality, would rank first and second with an away-specific λ. That gives 2/2.
**Failure class.** SHARED_DRIVER_TOP_TWO.
**Proposed correction.** Fit home and away attack/defence separately (Dixon-Coles with venue split) and require a diversification check on the top two.

<!-- END FINAL SETTLEMENT 2026-10-09 -->
