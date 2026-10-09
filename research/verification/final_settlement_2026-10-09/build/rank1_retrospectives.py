"""Deep Rank-1 retrospections required by the 2026-10-09 top-two rule.

Each entry is a dated post-event review. Nothing here changes an original
forecast, probability, rank or model; corrective actions are proposals only.
Shared quantitative checks are reproduced in tennis_overdispersion_check.py.
"""

R = {}

R['P-148'] = """**Claim.** Rank 1 was 1st Half Over 0.5 goals in Toluca Femenil v León Femenil, a FORCED RANK at MEDIUM-LOW evidence. The central first-half family listed 1-0, 0-1 and 1-1, with 0-0 named only as "the principal contrary branch".
**What happened.** HT 0-0; one goal (77'). Toluca won 1-0. Rank 2 (Toluca team corners Over 4.5) also lost on the best available reading, so the card scored 0/2.
**Distribution check.** No score matrix was produced. A league-typical first-half goal rate near 0.70 makes a 0-0 half a 30% event, so this was not a tail outcome. The card named the failure path and then ranked against it without a number.
**Knowable at cutoff?** Partly. Both clubs' first-half creation (shots and xG by half) was never retrieved. The ranking leaned on historical goal occurrence instead.
**Verdict.** RANKING_SELECTION error, not variance alone. A roughly 65-70% proposition was placed at Rank 1 without a measured edge over the alternatives.
**Own-top-2 counterfactual.** The same goal model would have ranked Toluca double chance (home favourite; it won) or Under 2.5 (won) above a first-half proposition. Both rank higher in mass for a low-event women's league fixture.
**Failure class.** FIRST_HALF_GOAL_OVERSELECTION (recurs in P-234, P-250, P-342 and P-377: five Rank-1 failures in this cohort).
**Proposed correction (not implemented).** Require a fitted half-time score matrix (first-half λ from half-split xG) before any 1H row can be Rank 1, and require its probability to exceed the next-best coherent row by at least 5 points."""

R['P-176'] = """**Claim.** Rank 1 was Amiens team total Under 1.5 goals. The card also called Versailles as the regulation winner (Rank 3 ML), so the whole slate leaned on Versailles containing Amiens.
**What happened.** Amiens 3-0 (HT 0-0). Ranks 1-4 all lost; only the corners Under won (secondary 8). Winner call incorrect.
**Distribution check.** No joint goal matrix. Ranks 1 (Amiens Under 1.5), 2 (Under 2.5) and 3 (Versailles ML) are positively dependent: one "Amiens are weak at home" thesis supplied all three. Their joint failure mass was never printed. Correlated rows behaved as one bet.
**Knowable at cutoff?** The early-season Ligue 3 sample (three rounds) was too small to support a directional team-strength claim. The card rated it MEDIUM instead of capping it.
**Verdict.** MODEL/THESIS error amplified by DEPENDENCE. One wrong strength estimate sank the top three rows.
**Own-top-2 counterfactual.** A coherent matrix with home advantage and three-round shrinkage toward the league mean would have centred near 1.3-1.1 Amiens. It would not have produced Amiens Under 1.5 and Versailles ML together. The top two would likely have been Under 3.5 and 1H Under 1.5 type rows, or a corners row with an exposure model.
**Failure class.** SMALL_SAMPLE_STRENGTH_OVERREACH plus TOP_ROW_DEPENDENCE.
**Proposed correction.** Shrink team ratings by an explicit early-season prior weight (games played / (games played + k)). Print the joint top-two failure mass. Forbid Rank 1 and Rank 2 from sharing the same directional thesis when that mass exceeds 0.35."""

R['P-200'] = """**Claim.** Rank 1 was Herning Blue Fox -2.5 (LEAN, MEDIUM). Herning was the potential winner.
**What happened.** Regulation 3-3; Herning won 4-3 in overtime. Herning won, but by one goal. Rank 2 (Over 6.5) won on the card's own full-match assumption.
**Distribution check.** In hockey a -2.5 needs a three-goal margin. The framework's own H-R2 reference puts two-goal-plus margins at 0.568 of all NHL games. Three-goal-plus margins are roughly half that (an estimate, not a registered statistic), and only a share of those go to the favourite, so even a clear favourite rarely clears 50% on -2.5.
**Knowable at cutoff?** Yes. The puck-line geometry is structural, and the card recorded unresolved goalie and preseason state.
**Verdict.** CONTRACT_GEOMETRY error. A three-goal handicap was ranked above the Over and the +2.5 counter-branch, both of which won.
**Own-top-2 counterfactual.** With a hockey goal model (regulation Poisson plus an OT bridge), Rungsted +2.5 (about 0.75-0.80) and Over 6.5 rank first and second. Both won, giving 2/2.
**Failure class.** HANDICAP_TAIL_OVERREACH.
**Proposed correction.** Rank-1 eligibility for any ±2.5 or wider hockey handicap requires a fitted margin distribution, including empty-net mass, with p ≥ 0.60."""

R['P-217'] = """**Claim.** Rank 1 was Guyana Amazon Warriors 20-over innings Under 174.5. Rank 2 was GAW after 6 overs Over 46.5.
**What happened.** The match was reduced to 16 overs. GAW still made 185/5, so the line was crossed with four overs fewer than planned. After six completed overs GAW were only 31/2. Both top rows lost: a slow start followed by an extreme back end.
**Distribution check.** The two top rows were opposing phase theses: a slow innings overall, but a fast powerplay. A ball-by-ball resource model ties powerplay scoring to final totals positively. Ranking Under-total with Over-powerplay hedges internally and guarantees neither. Reaching 185 in 16 overs (11.6 runs per over) is a far tail of any reasonable CPL innings distribution. The 31/2 start then 154 from ten overs is a death-overs explosion.
**Knowable at cutoff?** The rain-reduction risk was knowable (weather). The scale of the explosion was not.
**Verdict.** VARIANCE in the outcome, plus a COHERENCE error in slate construction.
**Own-top-2 counterfactual.** A single innings model would have paired Under-total with Under-powerplay (the powerplay Under won), or skipped totals given rain-reduction risk.
**Failure class.** PHASE_INCOHERENCE plus REDUCED_OVERS_RISK_UNMODELLED.
**Proposed correction.** Phase rows must come from one ball-state model, with the reduced-overs/DLS branch printed. Ban opposing-direction phase/total pairs in the top two unless the joint mass of both winning is at least 0.30."""

R['P-234'] = """**Claim.** Rank 1 was 1st Half Over 0.5 goals at a stated 0.50 (a coin flip at Rank 1).
**What happened.** HT 0-0; Dalian won 1-0 after a goalkeeper red-card disruption. Rank 2 (Dalian team goals Over 0.5) won.
**Distribution check.** A 0.50 probability is disqualifying for Rank 1 by itself. Rank 2 carried the same stated 0.50, so the ordering was arbitrary.
**Knowable at cutoff?** Yes. The stated probability exposed it.
**Verdict.** RANKING_SELECTION error. A no-edge row was given the top slot.
**Own-top-2 counterfactual.** Cup quarterfinals between a lower-tier home side and Shenhua carry heavy Under and draw mass. Under 2.5 (won) and Dalian team Over 0.5 (won) would have been the coherent top two.
**Failure class.** FIRST_HALF_GOAL_OVERSELECTION; NO_EDGE_RANK1.
**Proposed correction.** Hard gate: Rank 1 needs p_card ≥ 0.55 and at least 3 points of separation from Rank 3. Otherwise print RANK1_UNSTABLE and choose by distribution mass."""

R['P-250'] = """**Claim.** Rank 1 was 1st Half Over 0.5 (LEAN, MEDIUM), citing Yunnan's early-event rate and Chongqing's cup first-half goals. The card's own counter-path cited the May head-to-head 0-0.
**What happened.** HT 0-0; Yunnan won 1-0 and advanced. Rank 2 (corners Over 8.5) was settled VOID for want of any provider. The card counted 0/1.
**Distribution check.** The original deep review already found it: matchup-specific low-event evidence (a 0-0 continuity head-to-head and Chongqing's low-event regime) was named as the main kill path and then underweighted against broad first-half frequencies.
**Knowable at cutoff?** Yes. The kill path was printed before kick-off.
**Verdict.** EVIDENCE_WEIGHTING error.
**Own-top-2 counterfactual.** Full Under 2.5 and Yunnan to advance (both correct) would lead a distribution fitted with head-to-head and opponent shrinkage.
**Failure class.** FIRST_HALF_GOAL_OVERSELECTION; NAMED_KILL_PATH_UNDERWEIGHTED.
**Proposed correction.** When a card names a "main kill path", it must assign that path explicit probability mass in the matrix. If the mass exceeds 0.30, the row cannot be Rank 1."""

R['P-274'] = """**Claim.** Rank 1 was Giants +1.5 runs.
**What happened.** Pirates 5-2. The listed starter (Jared Jones) did not start; Bachar did. Rank 2 (Pirates ML) won.
**Distribution check.** An away underdog +1.5 has a structural ceiling: P(win) plus P(lose by exactly 1). About 27-30% of MLB games are decided by one run. A typical road underdog sits near 0.58-0.62 on +1.5, and that bound leaves no large edge.
**Knowable at cutoff?** The starter change was knowable only near first pitch. The ceiling was always knowable.
**Verdict.** CONTRACT_GEOMETRY plus LATE_STARTER_CHANGE. The ranking assumed an edge the geometry does not normally provide.
**Own-top-2 counterfactual.** Pirates ML (won) and Under 9.0 (won) ranked first and second would have given 2/2. Under the own-picks rule, a starter change also triggers a re-run of the run distribution.
**Failure class.** RUNLINE_CUSHION_CEILING (recurs in P-524, P-544 and P-547).
**Proposed correction.** For baseball +1.5 rows, print the decomposition P(win) + P(lose by 1) from a fitted run-difference distribution (Skellam or negative binomial). Rank 1 needs p ≥ 0.65. A confirmed starter change after cutoff must void the card or force a dated re-forecast."""

R['P-342'] = """**Claim.** Rank 1 was 1st Half Over 0.5 at p 0.68; Rank 2 was Over 2.5 at p 0.56. This was a Slovak cup mismatch with a heavily rotated favourite (Komárno).
**What happened.** HT 0-0; Komárno 2-0 with goals at 74' and 90'. Corners 1-15. Total territorial control, late conversion. Both top rows lost (0/2).
**Distribution check.** The card itself printed "2-0 control, 0-0 at half" as a kill path. The territorial evidence (a corner edge of 15-1) was right; the conversion-timing model was missing.
**Knowable at cutoff?** Yes. The rotation of the favourite was documented.
**Verdict.** MECHANISM error: territory was confused with conversion timing. This was the original cohort's worst-graded card.
**Own-top-2 counterfactual.** Komárno to win (correct) and Over 8.5 corners (won), or Under 2.5 (won). Each follows directly from a dominance-without-finishing model.
**Failure class.** FIRST_HALF_GOAL_OVERSELECTION; ROTATION_CONVERSION_DISCOUNT_MISSING.
**Proposed correction.** For a rotated favourite, apply a conversion discount to the favourite's first-half λ, backed by evidence. Re-rank territorial props (corners, shots) above timing props."""

R['P-369'] = """**Claim.** Rank 1 was total corners Under 10.5 at p 0.68, with no frozen corner provider.
**What happened.** FotMob corners 5-6 = 11, so the Under lost by one corner. Rank 2 (1H Over 0.5) also lost (HT 0-0). The card scored 0/2.
**Distribution check.** Corner counts are overdispersed (variance about 1.3-1.6 times the mean). With a mean near 9.5 and negative-binomial width, P(≤10) is about 0.62-0.66. The 0.68 was mildly optimistic, and the outcome sat one integer past the line: close to ordinary variance.
**Knowable at cutoff?** The provider gap was known. Score-state effects (a 1-1 game with late chasing) add corners and were not modelled.
**Verdict.** VARIANCE with a provider-governance defect. The miss was by the minimum possible margin.
**Own-top-2 counterfactual.** Under 2.5 (won, at 1-1) and 1H Under 0.5 (won) both carry more mass for a low-shot, low-xG fixture.
**Failure class.** CORNER_ROW_WITHOUT_PROVIDER_OR_NB_MODEL.
**Proposed correction.** Corner rows require a registered provider and a negative-binomial count model with score-state adjustment. Without both, cap p at 0.60, which removes them from Rank 1."""

R['P-377'] = """**Claim.** Rank 1 was 1st Half Over 0.5 at a stated 68% (UNVALIDATED_SUBJECTIVE).
**What happened.** Xelajú 0-0 Cobán; corners 7, so Rank 2 (Over 8.5 corners) also lost. The card scored 0/2.
**Distribution check.** Guatemala's Liga Nacional has a goals-per-game environment lower than the European priors implicitly used, so the first-half goal base rate falls toward 0.60-0.65. Xelajú's home at altitude also slows tempo.
**Knowable at cutoff?** Yes. League-specific base rates were not printed.
**Verdict.** BASE_RATE_TRANSFER error (European first-half priors applied to a lower-scoring league) plus FIRST_HALF_GOAL_OVERSELECTION.
**Own-top-2 counterfactual.** Under 2.5 (won) and 1H Under 0.5 (won) under a league-calibrated matrix gives 2/2.
**Failure class.** FIRST_HALF_GOAL_OVERSELECTION; LEAGUE_BASE_RATE_MISSING.
**Proposed correction.** BASE_RATES_REGISTER must hold per-league first-half and full-time goal rates estimated from the Previous Sports Results archive. A card without its league's base rate cannot use goal-timing rows at Rank 1."""

R['P-430'] = """**Claim.** Rank 1 was Al Nassr team total Over 0.5 at p 0.85; Al Nassr was the potential winner.
**What happened.** Al Ain 4-0. Al Nassr had 15 shots and 10 corners but did not score. Rank 2 (Match Over 1.5) won.
**Distribution check.** At p 0.85, P(0 goals) = 0.15 implies λ ≈ 1.9 for Al Nassr away at Al Ain in the ACLE. That is a top-team home rate, not an away rate against a strong host. A realistic λ of 1.3-1.5 gives P(score) ≈ 0.73-0.78.
**Knowable at cutoff?** Yes. No official XI or bench had been retrieved, and the original review called the 85% "too assertive".
**Verdict.** PROBABILITY_EXTREMITY under unresolved participant state.
**Own-top-2 counterfactual.** Match Over 1.5 (won) and 1H Over 0.5 (won) both rank higher once Al Nassr's λ is shrunk.
**Failure class.** OVERCONFIDENT_TEAM_TOTAL.
**Proposed correction.** Cap any single-team "to score" row at 0.80 unless both XIs are confirmed and the λ is fitted. Display the implied λ next to every team-total probability."""

R['P-492'] = """**Claim.** Rank 1 was Michael King Over 14.5 pitching outs; Rank 2 was Padres +1.5.
**What happened.** Dodgers 7-0. King got 12 outs (4.0 IP, 81 pitches, five runs). Both top rows lost (0/2).
**Distribution check.** A starter-outs prop and a team cushion share one driver: the starter's early run prevention. When King was hit, both failed together. The original review already noted the shared removal pathway.
**Knowable at cutoff?** The dependence was knowable. Its realisation was variance.
**Verdict.** TOP_ROW_DEPENDENCE. The top two were one bet on King.
**Own-top-2 counterfactual.** Dodgers ML (won) and Under 8.5 (won at 7) are less correlated with the King thesis.
**Failure class.** SHARED_DRIVER_TOP_TWO.
**Proposed correction.** Compute the joint top-two failure probability by simulation. If it exceeds 0.30, replace Rank 2 with the best row whose correlation with Rank 1 is below 0.3."""

R['P-519'] = """**Claim.** Rank 1 was AFLW total Under 89.5 at p 0.719 (q 0.780). Rank 2 was Suns -27.5 at p 0.449 (q 0.731).
**What happened.** Gold Coast 69-39 St Kilda (total 108, margin +30). Rank 1 lost; Rank 2 won. The original card's claimed 50-22 settlement was fabricated and later rejected against the AFLW match centre.
**Distribution check.** Rank 2's p (0.449) was below Rank 3's p (0.551), its complement on the same margin. The slate was ordered by q, a ranking score, not by probability: an inversion. On the totals side, 0.719 for Under 89.5 was too extreme for a 2026 AFLW total, given the variance of quarter scoring.
**Knowable at cutoff?** Yes. Ordering by q is a process defect visible in the card.
**Verdict.** RANK_BY_Q_NOT_P plus OVERCONFIDENT_TOTAL, plus a fabricated settlement in the original record.
**Own-top-2 counterfactual.** Ordering by p gives St Kilda +27.5 (0.551, lost) then Under (0.719, lost). The issue here is the total's distribution. A fitted AFLW scoring-shot model with a 2026 era mean would have centred higher.
**Failure class.** RANK_BY_Q_NOT_P; FABRICATED_SETTLEMENT_RECORD.
**Proposed correction.** The validator must reject any card where rank order is not non-increasing in p_card. Settlement text must cite an owner match ID whose score fields are machine-checked."""

R['P-520'] = """**Claim.** Rank 1 was Lotte Giants ML at p 0.577; Rank 2 was Hanwha +1.5 at 0.520.
**What happened.** Hanwha 6-2 (three first-inning runs). Rank 2 won.
**Distribution check.** A 0.577 moneyline is roughly a 58/42 game: Lotte loses about 42% of the time. A 0.52 Rank 2 is a coin flip. This slate had no strong row.
**Knowable at cutoff?** The weakness of the slate was visible.
**Verdict.** VARIANCE on a weak slate; RANK1_INSTABILITY.
**Own-top-2 counterfactual.** The four supplied rows were near-even, so a coherent run model would print RANK1_UNSTABLE. Its strongest-mass row would likely be Under 10.5 (won at 8 runs) with Hanwha +1.5.
**Failure class.** WEAK_SLATE_FORCED_RANK.
**Proposed correction.** When no row exceeds 0.58, label the card LOW_EDGE_SLATE, and score its Rank 1 separately so these do not dilute evaluation of strong-slate cards."""

R['P-521'] = """**Claim.** Rank 1 was Joventut -5.5 at **p 0.408** (q 0.677). Rank 4 was its near-complement, Breogán +5.5, at p 0.592.
**What happened.** Breogán 110-104. Rank 1 lost; Rank 2 (Over 179.5) won with 214 points.
**Distribution check.** The card's own probability said Rank 1 would lose 59% of the time. This is the clearest q-versus-p inversion in the cohort: the forecast was internally correct (Breogán +5.5 more likely) and the ranking contradicted it.
**Knowable at cutoff?** Yes. It was printed on the card.
**Verdict.** RANK_BY_Q_NOT_P. A pure process failure; the probability layer was right.
**Own-top-2 counterfactual.** Ordering by p: Breogán +5.5 (0.592, won) and Over 179.5 (0.538, won) gives 2/2.
**Failure class.** RANK_BY_Q_NOT_P.
**Proposed correction.** Same validator as P-519. Add a regression test that loads every historical card with p and q and flags inversions."""

R['P-522'] = """**Claim.** Rank 1 was Over 169.5 at p 0.667; Rank 2 was Tenerife -3.5 at 0.553. Rank 4 (Zaragoza +9.5) had p 0.605, above Rank 2.
**What happened.** Tenerife 80-81 Zaragoza (total 161). Ranks 1-3 lost; only Zaragoza +9.5 won. The card scored 0/2.
**Distribution check.** The Over 169.5 (0.667) and the Over 179.5 (0.457) imply P(170-179) ≈ 0.21. Under a normal total that means SD ≈ 18.6 around a centre near 177.5. The actual 161 is about -0.9 SD, ordinary variance. Rank 4's higher p than Rank 2 is another inversion.
**Knowable at cutoff?** The inversion was. The low total was variance plus missing early-season pace shrinkage.
**Verdict.** RANK_BY_Q_NOT_P plus VARIANCE.
**Own-top-2 counterfactual.** By p: Over 169.5 (lost), then Zaragoza +9.5 (won), giving 1/2.
**Failure class.** RANK_BY_Q_NOT_P.
**Proposed correction.** Same validator. Also derive totals rows from a possessions × efficiency model with early-season shrinkage to the prior-season league pace."""

R['P-524'] = """**Claim.** Rank 1 was KIA +1.5 at p 0.592 (q 0.638). Rank 2 was KT ML at 0.530.
**What happened.** KT 7-5. KIA lost by 2 after briefly tying. Late home runs (a seventh-inning three-run shot and an eighth-inning two-run shot) set the margin.
**Distribution check.** For a home underdog, +1.5 covers on a win, a 12-inning KBO tie, or a one-run loss. The card cited a 27.7% one-run share. With P(KIA win) ≈ 0.47, the ceiling is about 0.47 + 0.53×0.28 + tie ≈ 0.63. The stated 0.592 was consistent, but it was not an edge. The card's total mean of 8.80 above 8.5 contradicted its own Under probability of 0.527, a coherence fault on Rank 3.
**Knowable at cutoff?** The geometry was. The late bullpen clusters were variance.
**Verdict.** RUNLINE_CUSHION_CEILING; COHERENCE fault on the totals rows.
**Own-top-2 counterfactual.** KT ML (won) and Over 8.5 (won, implied by the card's own 8.80 mean) gives 2/2.
**Failure class.** RUNLINE_CUSHION_CEILING; MEAN_VS_TAIL_INCOHERENCE.
**Proposed correction.** Derive every row from one run-distribution object, and assert that the sign of (mean − line) matches the side of the favoured total."""

R['P-527'] = """**Claim.** Rank 1 was Under 174.5 (qualitative, not certified) in Hapoel Tel Aviv v Real Madrid, with Madrid as the potential winner. A later consolidated version reversed the priority and was NO_FORECAST.
**What happened.** Hapoel 102-98 (total 200, 25.5 above the line). Hapoel built a big lead, Madrid ran 19-0 in the third quarter, and Hapoel held on. Rank 2 (Hapoel +4.5) won.
**Distribution check.** A EuroLeague total of 174.5 is low for the competition's modern scoring environment, and a 200-point game is about +1.8 SD on a typical 13-14 SD. The Under thesis needed slow pace, but the game shape (a lead, a comeback run, late fouling) inflates possessions.
**Knowable at cutoff?** The base rate was knowable from the archived EuroLeague data. No possessions model was run.
**Verdict.** MODEL error (no pace/efficiency model) plus BASE_RATE neglect.
**Own-top-2 counterfactual.** A possessions × efficiency model centred on the competition mean would not rate Under 174.5 above 50%. Hapoel +4.5 (won) and the Over (won) would lead, giving 2/2.
**Failure class.** BASKETBALL_TOTAL_WITHOUT_PACE_MODEL (recurs in P-548 and P-553).
**Proposed correction.** Basketball totals at Rank 1 require the runtime basketball engine (possessions × efficiency, bivariate). Without it, cap p at 0.58."""

R['P-531'] = """**Claim.** Rank 1 was Fever +4.5 and Rank 2 was Over 181.5. These were qualitative ranks with no probabilities, from late research (cutoff about 11:01 AEST, already after the scheduled start) with a reported starter change. Las Vegas was the potential winner (correct).
**What happened.** Aces 94-83 (total 177). Both top rows lost (0/2); Aces -4.5 and Under 181.5 won.
**Distribution check.** No distribution was produced. With a modest Aces edge (win about 0.58, margin SD about 12, mean margin about +2.4), Fever +4.5 is about 0.57: coherent with the winner call, but well short of Rank-1 strength. The +11 margin is about +0.7 SD on that assumption, ordinary variance. The Over 181.5 also had no pace basis, and the 177 total sat inside a normal band.
**Knowable at cutoff?** The research was already late and the medical effect of the starter change was censored. Neither top row had quantitative support.
**Verdict.** VARIANCE on unquantified, low-edge rows, plus a LATE_INFORMATION process defect.
**Own-top-2 counterfactual.** A margin/total model would probably still favour the Fever cushion (about 0.57) but would not have placed a pace-free Over at Rank 2. The likely partner is Under 181.5 or a smaller-cushion side row, so 1/2 is the plausible own-picks result.
**Failure class.** QUALITATIVE_RANKS_WITHOUT_DISTRIBUTION; LATE_RESEARCH.
**Proposed correction.** For playoff basketball, run the runtime basketball engine (possessions × efficiency) even for late cards. When a starter change is confirmed after cutoff, publish a dated re-forecast rather than keeping stale ranks."""

R['P-534'] = """**Claim.** Rank 1 was Roosters -4.5 in the NRL Grand Final; Rank 2 was Over 38.5.
**What happened.** Roosters 19-18 (total 37). The Roosters won the premiership by a field goal. Both top rows lost: -4.5 by 3.5 points and Over 38.5 by 1.5. The card scored 0/2. Winner call correct.
**Distribution check.** Grand Finals are tighter and lower-scoring than regular-season games: defensive intensity, conservative kicking, field goals. A -4.5 needs a margin of 5 or more, which in a near-even final is about 40-45%. Knights +12.5 and Under 48.5 both won easily.
**Knowable at cutoff?** Yes. `Previous Sports Results/Rugby League/NRL` holds seasonal results back to the early 1900s, including Grand Finals, from which a finals-specific margin and total compression could be estimated.
**Verdict.** BASE_RATE_NEGLECT (finals compression) plus CONTRACT_GEOMETRY.
**Own-top-2 counterfactual.** A finals-adjusted model would rank Knights +12.5 (won) and Under 48.5 (won) at the top, giving 2/2.
**Failure class.** FINALS_REGIME_IGNORED.
**Proposed correction.** Add a finals/knockout regime flag to the NRL and AFL engines, with margin and total compression factors estimated from the archive."""

R['P-541'] = """**Claim.** Rank 1 was Bellucci -3.5 games at 62.0% and Rank 2 was Under 21.5 games at 54.0%. Bellucci was the potential winner at 77.0% (hard-court Elo benchmark about 81.6%).
**What happened.** Yi Zhou won 6-4, 3-6, 7-6(4); games were level 16-16 over 32 games. The card scored 0/2 and the winner call was incorrect.
**Distribution check.** Both top rows needed the same branch: Bellucci winning comfortably in straight sets. The card's 23% upset branch and its "close Bellucci win" branch each defeat both rows. Roughly, P(both lose) ≈ P(Zhou wins) + P(Bellucci wins in three sets) ≈ 0.23 + 0.20 ≈ 0.4. The pair was close to a single bet. The upset itself was a 23% event: real, but not a tail.
**Knowable at cutoff?** The dependence was knowable. The upset was variance. The card also recorded Bellucci workload concerns and Zhou's freshness, the stated upset mechanisms, without widening the distribution.
**Verdict.** VARIANCE on Rank 1, plus TOP_ROW_DEPENDENCE that turned one miss into 0/2.
**Own-top-2 counterfactual.** The max-mass row on this distribution is Bellucci ML (77%), which also lost. A diversified own top two of Bellucci -3.5 and Over 21.5 (46%, won) would have scored 1/2. The lesson is diversification, not a better single pick.
**Failure class.** TOP_ROW_DEPENDENCE; TENNIS_WORKLOAD_UNMODELLED.
**Proposed correction.** Run the joint top-two failure check (simulate both rows on one tree). Model workload as a negative shift in the match-level serve-probability random effect, not as narrative only."""

R['P-544'] = """**Claim.** Rank 1 was Doosan +1.5 at 62.7%, on Choi's start and the league-best Doosan staff. Rank 2 was LG win (+0.5).
**What happened.** LG 7-5 (12 runs). Doosan lost by 2. Rank 2 won.
**Distribution check.** Away underdog +1.5 ceiling as for P-274 and P-524: about 0.45 + 0.55×0.28 ≈ 0.60. The stated 62.7% sat at the ceiling. The 12-run game, against a starter-quality thesis, reached the bullpen-transition tail the card named.
**Knowable at cutoff?** The geometry was.
**Verdict.** RUNLINE_CUSHION_CEILING.
**Own-top-2 counterfactual.** LG win (won) and Over 7.5 (won; the card's 51.6% plus the transition tail) gives 2/2.
**Failure class.** RUNLINE_CUSHION_CEILING.
**Proposed correction.** As P-274: print the decomposition and require p ≥ 0.65 for a +1.5 at Rank 1."""

R['P-547'] = """**Claim.** Rank 1 was NC +1.5 at 61.8%. Rank 2 was SSG ML at 56.0%, the potential winner.
**What happened.** SSG 6-3 (9 runs). NC lost by 3. Rank 2 won and the winner call was correct.
**Distribution check.** The card favoured SSG to win (56%) and also ranked NC +1.5 first. That is coherent (0.44 + 0.56×0.31 ≈ 0.61), but it puts a ceiling-level cushion ahead of the side the card actually believed in. The Munhak run environment (10.45 runs per game) widens the margin distribution and lowers one-run mass: high-scoring parks produce fewer one-run games.
**Knowable at cutoff?** Yes. The park run environment was printed on the card.
**Verdict.** RUNLINE_CUSHION_CEILING worsened by a HIGH_RUN_ENVIRONMENT_MARGIN_WIDENING the card did not apply.
**Own-top-2 counterfactual.** SSG ML (won) and Under 9.5 (won at 9) gives 2/2.
**Failure class.** RUNLINE_CUSHION_CEILING.
**Proposed correction.** Make the one-run share a function of the expected total, estimated from the KBO archive, instead of a flat 27.7%."""

R['P-548'] = """**Claim.** Rank 1 was Under 178.5 at 64.5%, on a 172-point centre. KCC was the potential winner (correct).
**What happened.** KCC 103-98 (total 201, 22.5 over the line). Rank 2 (KOGAS +8.5) won.
**Distribution check.** A 64.5% Under 178.5 on a 172 centre implies SD ≈ 17. The result is +1.7 SD, about a 5% tail. The card recorded KCC's "extreme game-to-game variance" and the KBL's 2026-27 foreign-player rule change, both reasons to widen the distribution further, which would have pulled the Under toward 0.60.
**Knowable at cutoff?** Partly. Uncertainty about the scoring regime was documented, but the centre was not shifted.
**Verdict.** VARIANCE on a mis-centred, under-wide distribution. The regime change should have moved the mean, not just the width.
**Own-top-2 counterfactual.** KOGAS +8.5 (won) and KCC -2.5 (won) carry more mass than a regime-uncertain total, giving 2/2.
**Failure class.** BASKETBALL_TOTAL_WITHOUT_PACE_MODEL; RULE_CHANGE_REGIME_SHIFT.
**Proposed correction.** When a league changes a rule mid-season or pre-season, hold totals out of Rank 1 until 5+ games of the new regime have been observed, or use a change-point prior."""

R['P-549'] = """**Claim.** Rank 1 was Guangxi double chance (X2) at 81.85%; Rank 2 was Guangxi team Over 0.5 at 79.81%. Both came from a Poisson matrix with Guangxi λ 1.60.
**What happened.** Foshan 1-0 (HT 0-0). Both top rows lost (0/2); winner call incorrect.
**Distribution check.** The two rows are very strongly dependent: Guangxi failing to score drives both. Under the card's own matrix, P(both lose) = P(Foshan win with Guangxi 0) ≈ 0.10-0.12. The ranked pair offered almost no diversification. A λ of 1.60 away for a second-placed side is plausible. The card noted Guangxi's two latest away wins were 1-0 with 0-0 halves, evidence of a lower away λ (about 1.2-1.3) that was not used.
**Knowable at cutoff?** The dependence and the low away λ were both printed.
**Verdict.** TOP_ROW_DEPENDENCE plus EVIDENCE_WEIGHTING.
**Own-top-2 counterfactual.** Under 3.5 (won) and Under 2.5 (won), both positively related to a low-λ reality, would rank first and second with an away-specific λ. That gives 2/2.
**Failure class.** SHARED_DRIVER_TOP_TWO.
**Proposed correction.** Fit home and away attack/defence separately (Dixon-Coles with venue split) and require a diversification check on the top two."""

R['P-551'] = """**Claim.** Rank 1 was Over 22.5 total games at 60.9%, from an i.i.d. point model with near-equal serve points (0.637 v 0.630) and a deciding-set probability of 49.9%. The card itself flagged that this was "above historical men best-of-three reference 35.8%".
**What happened.** Vallejo 6-3, 6-1 (16 games). Rank 2 (Royer +1.5) also lost (0/2); winner call correct.
**Distribution check (reproduced).** Reimplementing the card's exact tree gives P(Over 22.5) = 0.609 and P(3 sets) = 0.499. Adding a match-level form shock (SD 0.05 on serve points, enough to bring P(3 sets) to 0.384, near the 35.8% reference) gives **P(Over 22.5) = 0.474**. On a calibrated deciding-set rate the Rank-1 row was a sub-50% proposition. P(|margin| ≥ 6) rises from 0.18 to 0.31.
**Knowable at cutoff?** Yes. The card printed the 49.9% versus 35.8% discrepancy and did not act on it.
**Verdict.** DISTRIBUTION_MISSPECIFICATION: the i.i.d. points assumption understates between-player variance.
**Own-top-2 counterfactual.** Under the overdispersed tree: Royer +1.5 (0.55, lost) and Under 22.5 (0.53, won) gives 1/2, with the pair no longer sharing the long-match driver.
**Failure class.** TENNIS_IID_UNDERDISPERSION (also P-555).
**Proposed correction.** Add a per-match random effect to the tennis engine. Calibrate its SD so the deciding-set rate and the game-margin distribution match the ATP archive. Reject any card whose P(3 sets) deviates from the reference by more than 8 points without a documented reason."""

R['P-553'] = """**Claim.** Rank 1 was Under 171.5 at 57.63%, from a Gaussian total with mean 167 and SD 19.5. Chiba was the potential winner.
**What happened.** Kobe 94-86 (total 180). Rank 2 (Kobe +6.5) won; winner call incorrect.
**Distribution check.** Φ(4.5/19.5) ≈ 0.59 before overtime, so the card was internally consistent. A total of 180 is +0.67 SD, an ordinary outcome. The card's own regulation anchors (Kobe's 74.5 and Chiba's 86.0 scored, with their conceded figures) average to about 170. The analyst then moved Kobe down 3.75 and Chiba up 1.0 by judgment (net -2.75 to 167), which made the Under the top row. On the unadjusted 169.75 mean, P(Under 171.5) ≈ 0.54.
**Knowable at cutoff?** The judgment adjustment is the decisive step and it was unsupported ("not a fitted coefficient").
**Verdict.** JUDGMENT_ADJUSTMENT error on a near-coin-flip row placed at Rank 1.
**Own-top-2 counterfactual.** Without the judgment shift, the total is near 50/50 and drops out. Kobe +6.5 (won) and a side row lead.
**Failure class.** UNFITTED_ANALYST_ADJUSTMENT; NEAR_COIN_FLIP_RANK1.
**Proposed correction.** Analyst adjustments must be logged as named parameters with a prior size. A row whose ranking depends on an unfitted adjustment larger than 0.25 SD cannot be Rank 1."""

R['P-555'] = """**Claim.** Rank 1 was Kopřiva +3.5 games at 61.5%; Rank 2 was Over 22.5 at 58.6%. Both came from an i.i.d. tree with Bergs holding 81.4% and Kopřiva 76.4%, and a three-set branch of 48.4%.
**What happened.** Bergs 6-3, 6-1 (12-4, 16 games). Both top rows lost (0/2).
**Distribution check (reproduced).** Reimplementing the tree gives P(Kopřiva +3.5) = 0.615, P(Over) = 0.586 and P(3 sets) = 0.484, matching the card. With the same match-level form shock (SD 0.05), P(Over 22.5) falls to **0.464**, while P(+3.5) stays about 0.61 and P(|margin| ≥ 6) rises from 0.21 to 0.33. Rank 1 was robust to the misspecification; Rank 2 was not. The pair was strongly dependent, since both need a long competitive match. The blowout branch defeated both.
**Knowable at cutoff?** The dependence and the inflated three-set mass were both knowable.
**Verdict.** DISTRIBUTION_MISSPECIFICATION (Rank 2) plus TOP_ROW_DEPENDENCE. Rank 1 alone was variance.
**Own-top-2 counterfactual.** Kopřiva +3.5 (0.61, lost) and Under 22.5 (0.54 under overdispersion, won) gives 1/2, with the pair now hedged against the blowout branch.
**Failure class.** TENNIS_IID_UNDERDISPERSION; SHARED_DRIVER_TOP_TWO.
**Proposed correction.** As P-551. Also require the top two in tennis to include at most one row that needs a deciding set."""
