# Cricket analysis rules — dated history to 2026-09-28

**Archived 2026-09-28 (md-only restructure).** These are the dated sections that followed the competition-rules section of `RULES_CRICKET.md`, moved verbatim. They are the evidence record. The live rules are §0 of `RULES_CRICKET.md`, and nothing here reinstates a rule that §0 or `CURRENT_RULES.md` §I withdraws.

## September 5 settlement learning — prospective SFA amendment


At phase-to-innings transitions, record `phase_runs`, `legal_balls_used`, `wickets`, `batters_remaining`, `set_batters`, `bowler_overs_remaining`, `field_restriction_phase` and `termination/target_state`. For every representative phase state calculate the runs allowed/required to each full-innings threshold. Test both early Under/full Over and early Over/full Under; neither is an anomaly requiring an early phase forecast to be discarded. This makes L-039/L-050/L-057 operational without assigning weights.


P-283's batting-first refresh correctly removed chase censoring. A sparse five-match first-innings average could not alone justify the remaining innings Under. P-286 finished the first six at 54/2 then added 92 in six; a normal 20-over venue centre is not a rate-preserving forecast of a 12-over innings. Use reduced-over intent, remaining hitters and actual available bowling allocation; missing final XI triggers the existing LOW cap throughout the final ranking.


Separate the user’s exact **six-over cumulative runs** contract from the regulatory powerplay. The official ETPL-linked Match 13 scorer records a four-over powerplay (40/1), six-over checkpoint 54/2 and 12-over final 146/3. The official toss was Glasgow electing to bowl. NV Play may label delivery ordinals 4.7/9.8 including wides; obtain legal-over boundaries from the scorecard/completed-over grouping, not decimal interpretation. Current Match 13 evidence is not a universal reduced-powerplay table for every league.


Preserve P-286's already-issued 12-over contract versus P-217's interrupted 20-over contract: the former completed its stated exposure; the latter still needs the unnamed operator's action/void rule. C-P293-CR-RESOURCES has zero prospective completions, and T20I/ETPL populations remain separate.




Full evidence and frozen-card comparisons: [September 5 audit](archive/audit_documents_implemented_2026-09-25/COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md).


## September 5(b) settlement learning — P-294–P-305 second continuation


**`P-300` (Rotterdam Dockers vs Edinburgh Castle Rockers, ETPL Match 14) — L-074, verbatim-fetch requirement.** An AI-summarised fetch of `etplofficial.com/matches` for this match produced an internally self-contradictory result: it claimed Edinburgh Castle Rockers "batted second" while simultaneously reporting they "won by 55 runs" — a win-margin type (runs) that is only meaningful for a team defending a total batting first. A second, literal/verbatim-quote fetch of the identical URL resolved cleanly: ECR batted first, scored 148 all out in 19.3 overs; Rotterdam were bowled out for 93 in 18 overs; ECR won by 55 runs. **New rule:** any scoreline read from `etplofficial.com`'s match-list page (or a comparably sparse/low-traffic competition site) must be obtained via a literal/verbatim quote request, never accepted from a first summarised read, because summarisation of this page's compact card layout has now been shown to misattribute which team's figure belongs to which stat.


Separately, ECR's confirmed 148 all out is itself informative: it is below their own recent 156-189 range against a credible opposing attack (Nortje/Wiese-class), and the card's own #2-ranked `20-over Under 168.5` correctly captured that direction. But the six-over powerplay figure for either innings could not be independently sourced post-match despite the same search effort that recovered the full-innings total — the ETPL powerplay-level split remains the weakest-sourced cricket market type in this framework, now with a second consecutive unresolved case (`P-300` following the pattern already logged for `C-PL5-CR-SPARSE-COMP`). Both `P-300`'s and `P-305`'s (still-live, deferred) powerplay rows should be treated as a standing `LOW`-or-below evidence cap for ETPL powerplay contracts specifically until a reproducible source is found, distinct from the full-innings total which has settled cleanly in every ETPL case checked this session.


**Kill-path library addition (§10.5):**


| Kill path | Defeats | Evidence origin |
|---|---|---|
| A summarised fetch of `etplofficial.com`'s compact match-card layout misattributing a stat between the two teams | Any scoreline accepted from a first AI-summarised read of that specific page | `P-300`; L-074 |
| A strong recent top-order still being bowled out below its own recent range against a credible attack | A full-innings Over ranked ahead of the Under purely from a strong recent top-order narrative | `P-300` |


Full evidence: [PREDICTION_LOG_COMBINED_2.md, 2026-09-05(b) section](PREDICTION_LOG_COMBINED_2.md#component-import--p-294p-305-second-continuation--2026-09-05b).


## September 6 settlement learning — `P-300` / `P-305` powerplay settlement (bimodal-language corrected 2026-09-06(d))


**The evidence gap is closed, and the Sept 5(b) evidence cap is lifted.** The September 5(b) addendum recorded that no independently reproducible powerplay figure could be found for `P-300` or `P-305`, and imposed a standing evidence cap on ETPL powerplay-level contracts as a result. That cap is **withdrawn**. A structured, keyless, reproducible phase field exists and was verified on 2026-09-06:


```
https://site.api.espn.com/apis/site/v2/sports/cricket/<seriesId>/summary?event=<eventId>
```


Its `notes[]` array carries, per innings, the literal string `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - N runs, W wickets)`, alongside a `toss` note in the form `"<Team> , elected to <bat|field> first"`. The `<seriesId>` path segment is the ESPNcricinfo series ID (for example `1547871` for ETPL 2026), **not** a slug; `cricket/scoreboard` without a series ID returns 404. Registered in `DATA_SOURCE_REGISTER.md` §September 6 as `SRC-ESPN-SITE-API-CRICKET`, status `CANDIDATE / RESEARCH ONLY`. Where the host board or competition publishes a conflicting figure, the board controls — this is a data partner, not the field owner.


Settlements produced by this lane: `P-305` Amsterdam Flames powerplay **60/1** → Rank #1 `Flames PP Over 51.5` **WIN**; `P-300` Edinburgh Castle Rockers powerplay **28/3** → Rank #1 `ECR PP Over 50.5` **LOSS**, complement `PP Under 50.5` **WIN**. Both toss preconditions were verified from the same `notes` array rather than assumed.


### The substantive algorithm change: phase totals are bimodal, and runs alone hide it


`P-300`'s Rank #1 loss is not explained by a bad line or a bad venue read. The venue supported 60 and 69 powerplay scores in the very next match on the same ground. It is explained by a retrieval omission.


Edinburgh Castle Rockers' two prior full powerplays were **68 for 3** and **55 for 1**. The card carried the run figures and dropped the wicket figures. Both prior observations cleared 50.5, so on runs alone the row looked well supported. A top order of high-strike-rate openers (Smuts, Gous, Adair) that loses wickets while scoring fast is exposed to a wide-variance, resource-sensitive powerplay outcome rather than a single central tendency, and in Match 14 that variance produced a low outcome: three wickets inside 2.6 overs, powerplay 28.


**Correction, 2026-09-06(d) (second independent review, findings F16 and F19).** Two prior observations (68/3, 55/1) do not establish a validated **bimodal** distribution — that is a statistical-shape claim the sample is too thin to support, and it is corrected below to a wide-variance/resource-branch disclosure instead. Separately, later matches at the same venue producing higher powerplay scores (60, 69) are **consistent with** wickets being a contributing factor in `P-300`'s low score; they do not **prove** it, and do not exclude other causes (strip, attack, specific conditions on that day) that a different match's outcome cannot establish either way. Both corrections narrow the causal and statistical claims here without withdrawing the actionable requirement below: retrieve wickets alongside runs, and name the collapse branch explicitly.


**Required from now on, `SFA-CRICKET`:**


1. **Retrieve runs *and* wickets for every phase observation in the window.** A phase table showing only runs is an incomplete retrieval, not a complete one, and the card must say so.
2. **Compute the phase wicket rate** across the retrieved window. Where it is **≥1.5 wickets per innings** (a disclosure threshold, not a validated statistical cutoff), the phase total is modelled with an explicit **wide-variance, resource-sensitive** treatment rather than a single central estimate, and the supplied line is located against the observed **range/extremes** in the window, not asserted as "modes" of a bimodal distribution unless the sample is actually large enough to support that specific statistical claim (rarely true at n≤3–4 observations, as corrected 2026-09-06(d)).
3. **Write the collapse branch as a named kill path** in the frozen kill-path table for any powerplay/phase Over row. It is not a risk-paragraph mention; it is a branch with its own settled phase score.
4. **Print the competition-level phase population**, not only the two teams' own figures — for `P-300`/`P-305` the ten completed six-over powerplays in ETPL 2026 were 28, 39, 49, 50, 51, 55, 56, 61, 68, 72, median 53. This is the `REFERENCE_BASE_RATE` for the phase and feeds `G26.1` directly.


### Kill-path library addition (§10.5)


| Kill path | Defeats | Evidence origin |
|---|---|---|
| **Powerplay top-order collapse** — an attacking top three loses 2–3 wickets inside the first 3 overs, converting a high-mean phase into a bottom-decile phase score | Any powerplay/phase **Over** row justified by a high phase *mean* without the phase *wicket* rate | `P-300`, ECR 28/3 after prior powerplays of 68/3 and 55/1 (`L-083`, narrowed 2026-09-06(d) — wide-variance disclosure, not a validated bimodal shape) |
| **Chasing-side powerplay inflation** — the second innings' powerplay runs faster than the first because a target is known | A first-innings-anchored phase read applied to the chase | ETPL 2026 M15: Dublin 69/1 chasing versus Amsterdam 60/1 setting |


### Sport ordering override addition (§10.6)


- **Disclosure only, per `RULES_GENERAL.md` §15:** a powerplay/phase **Over** row whose retrieved window shows a phase wicket rate ≥1.5 per innings is flagged as `TAIL_EXPOSED` and the card names the mechanism that suppresses the collapse branch **today** (a defensive-intent opener, a slow strip, a named absent new-ball bowler) or states that it cannot. "Their mean is high" is not that mechanism. This no longer imposes a hard ordinal bar — see the firewall correction in `RULES_GENERAL.md` §15.
- **Endorsed pattern, keep it:** where the toss is unpublished at cutoff, a phase row that names the batting-order condition explicitly (`conditional on X batting first`) rather than assuming it is the correct construction. Both `P-300` and `P-305` used it, both conditions resolved cleanly, and neither settlement was contested. Assuming a batting order that has not been drawn is a `GATE-CONTRACT` defect; declaring it as a condition is not.




### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | ETPL/associate and franchise T20 phase fields are sourceable through `SRC-ESPN-SITE-API-CRICKET`; name the exact series ID and event ID at freeze. Where the competition has no ESPNcricinfo series ID, phase rows are `SETTLEMENT_UNSOURCED`. |
| `G14.2` coaching / bench / rotation record | Cricket has no bench in the substitution sense; record instead the named XI, the confirmed impact-player/substitute provision from `LEAGUE_RULES_CRICKET.md` where the competition has one, and the head coach. Pitch-side toss reports, broadcast team-sheet reveals, or accredited cricket beat reporting verified under Control `S-1 Rev 2` qualify as `PROJECTED_BEAT_VERIFIED`, satisfy `G14.2`, and do not block Rank #1. |
| `G20.2` distributional tail audit | Derive phase and innings tail mass from the **same frozen cricket resource distribution** used for ranking: legal balls, wickets/resources, role/XI continuity, phase scoring, toss/strip/conditions as separate evidence, and DLS/reduced-overs branches where applicable. Historical second-highest/median or second-lowest/median constructions are superseded and are not active forecast inputs. |
| `G21.1` exact target geometry | Map every supplied total/phase-total to its exact settlement event and derive WIN/PUSH/LOSS (plus void/censoring where applicable) from the same frozen sport-native PMF/CDF or coherent branch mixture. Genuine unions may be described as unions, but historical `TRUE_UNION` / `LOW_BAR_CUMULATIVE` / `CENTRAL_BAND` path-count labels have **no mandatory ordinal effect** and are not a substitute for the distribution. |
| `G26.1` no universal separation floor | Print any relevant reference base rate and `rank_gap` descriptively. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank by the row's exact marginal likelihood from the frozen joint distribution plus robustness/evidence uncertainty; precise probabilities require the validated-model gate. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md`](archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Before ranking phase and full-innings totals, calculate the remaining run requirement in legal balls with wickets/batters/bowlers/field restrictions. Evaluate early-Over/full-Under and early-Under/full-Over paths. Carry final XI uncertainty into the final evidence grade rather than raising the rank’s confidence after a failed gate.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-217 slow six-over scoring and P-305 strong PP scoring led to the opposite full-innings direction; evaluate remaining balls/wickets/roles independently. P-311 new openers weaken use of four old-roster PP observations as a ceiling, without prescribing a numerical uplift. Preserve fixed six-over targets separately from a shortened mandatory PP (P-217: mandatory phase 4.5 overs). Revised-innings research grades require the convention beside the grade; operator action remains unknown. P-305 has four frozen ranks and the batting-first condition was met.


## 2026-09-09 settlement learning — P-333, P-343 (both no-forecast; process worked)


`P-333` (Pakistan Women 143/8 beat Hong Kong Women 71) and `P-343` (Bangladesh Women 103/7 beat UAE Women 69/9) were both **administrative no-forecast closures**. Each had an innings-order-dependent supplied target (a "team batting first" first-innings runs / powerplay line), the toss was not verified before the scheduled start crossed, and the target could not be frozen because it does not survive both the bat-first and bat-second states. `CR-P3` (toss/innings-order blocking precondition) and §10.6.2 (no innings-total row above `LOW` before the toss unless it survives both branches) **worked exactly as designed** — no rank, probability or winner was issued, and the later results (Pakistan/Bangladesh did bat first) cannot be used to manufacture a grade.


**Operational note (no algorithm change):** when an innings-order-dependent cricket target is requested, begin the toss / live-state / XI handshake **earlier** in the research window so it is resolved before the scheduled start crosses. The failure here was not the gate — it was losing the `PREGAME` window to a late toss check. If the toss genuinely cannot be verified before start, the fail-closed `NO ACTIONABLE LIVE FORECAST` output is correct and must not be softened. Cross-sport: this is the same "acquire the volatile state faster on a time-boxed request" operational lesson as `P-324`/`P-326`/`P-334` (`RULES_GENERAL.md` §"2026-09-09").


### Cross-sport controls instantiated here (`G-L1`, `G-L2`, `G-L7`, `G-L8`)


The four cross-sport requirements adopted from the `P-333`–`P-344` cohort (`RULES_GENERAL.md` §§16.5(a)–(d)) apply to cricket from the next card. All four are **disclosure/retrieval requirements — no fitted weight, no ordinal bar** (`L-087`).


| Cross-sport control | Cricket instantiation |
|---|---|
| **`G-L1` §16.5(a)** — enumerate outcome-state families with explicit mass | §10.3's `CR-B1`–`CR-B8` branch set already names the required states; `16.5(a)` requires each to carry an **explicit probability mass summing to 1**, and the innings/phase corridor to be located against the **modal family**, not only the centre. The bimodality already recognised by `L-083` (a phase window losing ≥1.5 wickets is modelled against the modes, not the mean) is exactly this requirement — now generalised to every innings and phase target. Print a **representative Rank-#1 innings/phase score** and check it against every other supplied line on the same innings. |
| **`G-L2` — declared uncertainty model** | State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls. |
| **`G-L7` §16.5(c)** — aggregate-to-disaggregate retrieval | Do not let a batting average, a "last five innings" mean or an economy rate carry directional weight while the **innings-by-innings record** is available. Print the per-innings log for the decision-relevant window — runs, balls faced, dismissal mode, and for bowlers the **per-spell figures by phase** — and state whether a run of low or high scores is front-loaded, back-loaded or uniform. `P-333`'s own pre-cutoff research is a positive example: it printed all five L5 innings (55, 119/9, 115/6, 175/5, 176/7) and correctly observed that a 128.0 mean over a 55–176 range "is not a sufficient distribution by itself" — that is `16.5(c)` already being applied well, and it is the standard for every card. Quantify **every top-six batter and every frontline bowler**; a bare name in a squad list is `AGGREGATE_ONLY` and caps the dependent innings/phase rows. |
| **`G-L8` — distribution coherence** | Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability. |


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-11 settlement learning — `P-352`, `P-357`, `P-364`, `P-366`, `P-370`


Four issued cricket cards and one fail-closed administrative closure ([`PREDICTION_LOG_COMBINED_3.md` §"2026-09-11"](PREDICTION_LOG_COMBINED_3.md)). Rank #1 **1 W / 3 L** (`P-352`, `P-357`, `P-364` lost). **Limited-overs new-ball phase Unders 3 / 3** (`P-352` first five overs 18/0; `P-357` powerplay 43/3; `P-366` ≤49 at six overs); the Test restart phase (`P-364`) lost. Innings totals 1 W / 3 L. `P-364`'s match is still live; its winner label is open. Learning-only; no fitted weight or ordinal bar (`L-087`).


### What went right (keep it)


- **New-ball phase reads** (3 / 3 in limited overs) — the phase is where the evidence was cleanest.
- **`P-370`: `CR-P3` failed closed** on an innings-order-dependent contract whose toss was unverified at the start — the third correct fail-closed after `P-333` and `P-343`.
- **`P-366`: target-by-target settlement.** A rain-reduced 19-over innings of 172/4 was not remapped onto a 20-over line; the reached six-over target was graded and the 20-over rows were closed as censored (control 15, "incomplete is not zero").
- **`P-352` retrieved both XIs after the toss** and an observed exact-match pitch report — the handshake to copy.


### What went wrong, linked to earlier lessons


1. **Same-venue, same-week surface evidence set aside (`P-352`).** Windhoek produced T20I innings of **228/4, 217/3 and 205/5** between 4 and 6 September (ESPNcricinfo). The ODI card declined to "transfer T20 scoring", anchored on five April ODIs (highest 268/7), set 278 ±48 and lost Under 305.5 to 348/6. → **control 25**.
2. **A slow phase read as low-scoring regardless of wickets (`P-352`), and a collapse branch without mass (`P-357`).** 18/0 kept every resource; 43/3 → 62/6 destroyed them. Controls 3, 16 and 19 already require the phase-end *wicket* state; they were not executed.
3. **Post-toss XIs not retrieved (`P-357`).** The toss was complete at the freeze, so both XIs had been nominated. Dublin's attack held five international-level bowlers; Young took 5-21. → **control 26**.
4. **A generic restart slowdown against the batting side's own tempo (`P-364`).** 24 needed in six overs from 156/4 with a set batter and a 39-over-old ball; England's Stokes–McCullum-era rate is ~4.1–4.5 an over; the card assumed ~2.8–3.8; England made 54. → **control 27**; `G-L2`.


### Structural control additions


25. **Same-venue, same-week scoring in another format is current-surface evidence.** Where the same ground has hosted matches in another format within the last few days, convert their totals against that format's typical total at a comparable level and apply the result to this match's centre as a **named, signed adjustment with a stated weight**. An older same-format venue sample does not outrank it. Origin `P-352`.


26. **After the toss, the XIs exist — retrieve them.** Players are nominated before the toss (MCC Law 1.2 and every competition's playing conditions); once the toss is recorded, "XI unresolved" is a `RETRIEVAL_MISS`. Fetch both XIs from the toss commentary or scorecard page — ESPNcricinfo (via `r.jina.ai` if the direct route is blocked), Cricbuzz, or the competition's scoring provider — before freezing. If genuinely unreachable, record `RETRIEVAL_MISS` and cap every XI-dependent row. Origin `P-357`; contrast `P-352`.


27. **Test-session phase priors start from the batting side's current-era tempo; an overnight restart is width.** For a Test phase target (runs by over N, session runs), the prior is the batting side's own recent Test run rate in comparable conditions. An overnight restart widens the next-hour distribution; it takes a **signed** slowdown only with direct evidence — a new ball due, a change in overhead conditions, a named fresh spell. Origin `P-364`.


### Kill-path library additions (§10.5)


| Kill path | Defeats | Origin |
|---|---|---|
| A surface that has just produced 200+ T20 totals producing a big ODI total | An innings Under anchored on an older same-format venue sample | `P-352`; control 25 |
| A slow but wicket-light phase converting into a big innings | An innings Under that reads the phase runs without the phase wickets | `P-352`; controls 16, 19 |
| A three-wicket cluster at one score (62/3 → 62/6) | A team-total Over or winner resting on team record rather than the selected attack | `P-357`; control 3 |
| An aggressive batting side scoring at its era rate straight after an overnight restart | A Test phase Under built on a restart slowdown | `P-364`; control 27 |


### Pre-issue checklist additions (§10.7)


- Same-venue, same-week cross-format totals listed and converted, or recorded as none (control 25).
- Both XIs retrieved after the toss, or `RETRIEVAL_MISS` (control 26).
- For a Test phase: the batting side's era run rate printed as the prior; any restart slowdown justified by a named mechanism (control 27).
- Phase-end state printed as runs **and** wickets before any innings row is derived from a phase view (controls 16, 19).
- `P(R1 ∧ R2)` for phase + innings pairs — a slow phase *with* wickets is anti-coupled with an innings Over (`G-L10`, `P-357`).


### Source notes (this pass)


- ESPNcricinfo returns HTTP 403 to direct fetches; `r.jina.ai/https://www.cricinfo.com/...` worked for live state and full scorecards (verify the date on the returned page — the proxy can be cached).
- **ETPL's first-party match page stayed a stale "Yet to bat" shell for more than 24 hours** after Match 19 finished; it read COMPLETED by ~23:30 AEST on 2026-09-11 but still carried no scores. Settle ETPL from the Cricket Ireland-branded CricketArchive scorecards and CricketEurope; use the first-party page for status only.




## 2026-09-12 algorithm corrections and retrospective integration


Keep Test restart targets conditional on the observed innings state, ball age, wickets and batter/bowler resources. P-364 remains a live Test with settled innings/45-over rows; no winner is awarded early. The 39-to-45-over target added 54 runs, not six overs from a fresh innings. A nominated XI before toss is not proof of a publicly accessible team sheet. For P-357/P-366, missing public availability times remain unknown. Preserve P-366's unreached fixed 20-over target as censored. Remove the Sporting Life betting-tips preview used in P-364 from prospective sporting inputs and retrieve original market-blind reporting. Strike rate/run rate are not binomial proportions.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. Shared correction and methodology sources (`audit_2026-09-12/rule_corrections.md`, not present in this repository). All current log observations remain learning-only and not performance-eligible.




## Recovered mini-log reinforcement - 2026-09-12


P-262's official CPL report verifies Falcons 43/1 at six overs and 183/4 at twenty. Model retained wickets, innings order, set batters and remaining attack; a slow powerplay is not a full-innings ceiling. P-252's recovered mini already identified the need to remove chase-censoring once batting first is confirmed. P-352/P-364 repeat the phase/resources concern. Record dropped catches as post-issue events, not pregame evidence. Any changed resource/acceleration weights remain CANDIDATE for prospective comparison. Evidence: audit_2026-09-12/recovered_historical_retrospectives.md.




## 2026-09-15 settlement learning — `P-364` final (England won by 8 wickets)


`P-364`'s Test finished on Day 4 (12 Sep): Pakistan 133 & 449 (96.4 ov); England 453 & 130/2 (24.2 ov). Potential winner **England — WIN**; the four ranked rows were already settled (R1 L, R2 L, R3 W, R4 W). Learning-only; no fitted weight or ordinal bar (`L-087`). Evidence: ESPNcricinfo full scorecards via `r.jina.ai`; [combined log §"2026-09-15"](PREDICTION_LOG_COMBINED_3.md).


### What went right (keep it)


- The winner label's **state reasoning** — first-innings lead with wickets in hand, the stronger attack, playable venue weather — was correct.
- Both XIs were confirmed from Day-1 records published before the Day-2 cutoff; the Over kill paths that decided R1/R2 were all written on the card.


### What went wrong, linked to earlier lessons


1. **Control 27's prior was available on the card and not used (`G-L7`).** England's 2026-series innings before the freeze: Leeds 409/89.5 (4.55), Lord's 290/66.4 (4.35) and 208/54.2 (3.83) — **907 runs / 210.8 overs = 4.30 an over**. The 45-over row required 4.00. The card cited the PCB scorecards of both Tests but priced a restart slowdown instead. This current-series table replaces the 2022-era averages previously quoted as control 27's evidence (per the 2026-09-12 correction).
2. **The winner label used a series aggregate for the draw branch (`G-L1`, `G-L7`).** "Pakistan have failed to reach 200 in any innings" (171, 135, 110, 194, 133 — true when written) stood in for a time budget. Pakistan then batted 96.4 overs for 449 after roughly 27 overs were lost on Day 2. England still won with a day to spare, but the draw branch carried no number.


### Structural control changes


27. *(Evidence refresh — rule text unchanged.)* **Print the batting side's current-series innings table (runs, overs, run rate, conditions) as the phase prior before any adjustment.** Era or calendar-year averages are context, not the prior. Worked example `P-364`: 4.30 series rate v 4.00 required.


28. **A Test potential-winner label is a three-way time budget, printed as masses.** Print win / draw / loss masses with the arithmetic behind them: overs remaining in the match (scheduled overs less a stated weather-loss allowance from the venue-coordinate forecast), the current lead/deficit and wickets in hand, and the overs the trailing side must survive. Include a **resistance branch** (the trailing side bats 90+ overs) sized from its batting resources, not from its series innings aggregate. A series aggregate of either side may not substitute for this table (`G-L7`). Origin `P-364` (label correct; reasoning under-specified). Disclosure only — no coefficient.


### Kill-path library additions (§10.5)


| Kill path | Defeats | Origin |
|---|---|---|
| A trailing side that failed to reach 200 all series batting 90+ overs in its second innings, with lost overs to weather | A Test winner label or draw-branch mass built on the trailing side's series innings aggregate | `P-364`; control 28 |
| A small chase losing two wickets in the first over (England 2/2 chasing 130) | A winner/margin row treating a small-target chase as certain | `P-364` (did not decide the match; recorded as a live branch) |


### Pre-issue checklist additions (§10.7)


- Test phase or innings total: the batting side's current-series innings table printed first (control 27).
- Test winner label: win/draw/loss masses with overs-remaining and weather-loss arithmetic, and a resistance branch (control 28).


### Source notes (this pass)


- **ESPNcricinfo series results page via `r.jina.ai`** (`/series/<slug>/match-schedule-fixtures-and-results`) lists every match result and links every full scorecard in one fetch — the fastest route to a current-series innings table.
- The web-search engine summary reported England's chase as "132 for 2"; the opened scorecard reads **130/2**. Never settle or build a prior from a search summary.
- Cricbuzz and NDTV Sports were unreachable to WebFetch from this environment on 2026-09-15 (route-specific); Wikipedia's series article agreed on the result but is corroboration only (likely the same upstream lineage).




## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


**Cards:** P-379 (2nd ODI), P-389 (withheld), P-395, P-400, P-406 (ETPL / WCPL).


- **Positive — phase and innings are separate targets:** P-379 South Africa 24/0 after 5 (Under 25.5 WIN) then 335/9 (Over 315.5 WIN); P-395 Belfast 49 after 6 then 161/6. Keep the joint phase → innings tree (controls 16, 19).
- **Winner independence:** P-400 — both Guyana innings Unders won (33 powerplay, 119 all out) but TKR still failed to chase; innings totals and winner are distinct targets.
- **Exact phase settlement:** P-406's six-over rows stay unresolved — a final score and fall-of-wicket markers do not give the exact 6.0-over score (`TMP-OPEN-20260914-06`; control 15).
- **Anti-hindsight:** P-389's withheld conditional research later looked good but was never issued; it is not retro-scored (cf. P-333, P-343, P-370).
- **`G-L12` instantiation:** a limited-overs or Test winner label prints the margin/result masses (control 28) — do not centre a mismatch toward a close finish because the weaker side's recent innings are sparse.


## 2026-09-16 settlement learning — `P-406` six-over rows settled


Learning-only; disclosure and process only (`L-087`). Evidence: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-16"](PREDICTION_LOG_COMBINED_3.md).


- **Settled.** ESPN cricket API `cricket/1547871/summary?event=1547895`, Edinburgh innings (section 1), matchnote *Powerplay 1: Overs 0.1 – 6.0 (Mandatory – 68 runs, 2 wickets)*. Edinburgh reached 50 in 4.1 overs, then were bowled out for 118 in 18.3.
  - **Rank #1, ECR first 6 overs Over 50.5 (64%): WIN.**
  - **Rank #4, Under 50.5: LOSS.**


  The card's phase thesis was right. Its innings Over 172.5 and its Edinburgh winner label lost to the middle-overs collapse (Bracewell 5/12).
- **What went right.** Phase and innings were ranked as separate targets, phase first. Cricket phase rows in the import are now 4 of 4 when preferred (P-379, P-395, P-400, P-406) — see `C-PHASE-VS-FULL-TOTAL`.
- **What went wrong — the settlement process, not the forecast.** Two passes tried Statz and fall-of-wicket markers and left the row "exact checkpoint not recovered", while `DATA_SOURCE_REGISTER.md` had documented this exact ESPN field since 2026-09-06.


### Structural control addition
29. **Phase-checkpoint settlement route.**
    - **Where it applies:** ETPL (verified) and any other ESPNcricinfo series after a coverage probe.
    - **The settling record:** the ESPN cricket API matchnote `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - N runs, W wickets)` in that innings' `section`. The series ID goes in the path; find the event with `cricket/<seriesId>/scoreboard?dates=`.
    - **Limit:** valid only when the powerplay is the full 6.0 overs. A reduced-innings powerplay (P-217) does not settle a six-over row.
    - **On the card:** print this route (`G-L14`).


**Disruption facts (§16.11(o)):** record rain or wet-ground stoppages and overs lost with the score at the interruption (P-406's match notes include a wet-ground entry at 0/0).


## 2026-09-17 settlement learning — `P-424`, `P-428`, `P-429`, `P-431`


Learning-only; disclosure and process changes only (`L-087`). Cross-sport rules: `RULES_GENERAL.md` §16.12. Evidence: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md). Both ETPL scorecards were independently verified at the ESPN cricket API (series 1547871), including the powerplay matchnotes.


### What went right (keep it)
- **`P-429` is the model card of the batch** (Brier 0.1635, top two both won). It ranked *same-opponent, same-venue, unchanged-top-order* wicket evidence — Afghanistan 41/4 against this attack two days earlier — above generic batting-first totals. Afghanistan were 41/1 in the powerplay and Arshdeep took two.
- **Two correct fail-closes.** `P-424` and `P-428` both crossed their scheduled start without a verified toss or live state and issued nothing. Both research-only directions (Under 170.5, Under 168.5) would have **lost**, so the gate also avoided two losing bookings.
- **Phase and innings remain separate targets.** `P-424` realised **48/2 after six → 214/5**; `P-428` realised 54/2 → 181/6. Confirms controls 16 and 19 and `L-009`/`L-039`.


### What went wrong, linked to earlier lessons
1. **`P-431`: both Unders lost to a ceiling the card had already recorded.** England's **257/3 at the same venue** in July was on the card, yet Under 193.5 was given 55% and the powerplay Under 62%. England made 254/4 with a 90/1 powerplay (Brook 114*, Buttler 80). → control 30 and `G-L20`.
2. **`P-429` R4:** Varun Chakaravarthy's absence was treated as a simple scoring-ceiling positive. India's replacement ensemble squeezed overs 7–15 for 64 runs and five wickets. → control 31.


### Structural control additions
30. **Direct same-venue, current-regime ceiling.** Before ranking an **upper Under** (or a lower Over) on an innings or phase total, search the current regime for the same team at the same venue. If a comparable innings has already cleared the line, print it beside the line with its own mass, and give a named current mechanism — personnel, strip, role — for why it will not repeat. "It was an outlier" is not a mechanism. Origin `P-431`; cross-sport form `G-L20`.
31. **Bowling replacement chain.** An absent bowler is never a one-sign adjustment to the opposition's scoring. Print the chain: **outgoing role and its phase exposure → incoming bowler's role and rate → residual attack's combined phase resources**. Evaluate the ensemble, not the absence. Origin `P-429` (Varun out, Bishnoi in, Nitish Kumar Reddy 3/24 in the middle overs); reinforces `L-006`.


## 2026-09-17(b) settlement learning — `P-445` (CPL 2026 Eliminator) — **the conditional-activation gate, validated**


Learning-only (`L-087`). Cross-sport rules: `RULES_GENERAL.md` §16.13. Evidence: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md). **Independently verified this pass** at ESPN `cricket/1534175/summary?event=1534214`: matchnote `section 1` is the **Barbados** innings, Barbados powerplay **24/4**, Barbados **144/6 (20)**, Jamaica chase powerplay **79/0**, Maaz Sadaqat **100 off 44** (112 off 49), Jamaica **145/1 in 14.1**, won by 9 wickets. Saim Ayub, unresolved at the freeze, played.


### What went right — this is the whole lesson


The card supplied two Jamaica contracts — first-innings 20-over runs and first-six-overs runs — under a user definition of "first innings" as *the team batting first*. A pre-ball toss was **not** retrieved before the frozen cutoff. Rather than guessing the innings order or quietly re-pointing the contracts, the card **froze the activation condition as a first-class field** and wrote the failure branch out in advance: *"If Barbados bats first, these exact targets are not silently transferred to Jamaica's second innings."*


Jamaica won the toss and bowled. All four ranked rows settled **`NO ACTION / CONDITION NOT MET`**, with no Brier, no Rank-#1 score and no top-two score. The card is excluded from every cohort rate.


Had those rows been reassigned to Jamaica's chase, the powerplay row would have been graded against a **79/0** target-censored chase powerplay and the innings rows against a target-capped **145/1** — different contracts in a different tactical state, exactly the failure the chase-total cap rule exists to prevent. The gate cost the batch one scored card and prevented a target-identity error that would have contaminated four rows and every aggregate built on them.


Also right: the pitch-report ladder was run to exhaustion and returned `STRIP STATUS: NOT FOUND AFTER SEARCH` rather than a fabricated read; the same-day WCPL playoff's rain reduction to eight overs was carried as an environment fact; and the DLS/shortening branch was flagged as `UNKNOWN_DEFINITION` because the operator's action terms were not supplied.


### What went wrong


1. **The winner label over-rated Barbados at 62%.** The card's own text said Jamaica's batting ceiling was "higher than the venue sample implies" and then under-weighted it. Jamaica's new ball took Barbados to **24/4** inside the powerplay and Sadaqat's century ended the chase with 35 balls to spare. The evidence for the caveat was on the card; the distribution did not reflect it. → `G-L21`(3).
2. **The toss was the decisive unretrieved field — not the XI.** The line-up gap is real and recurring, but on this card the field that determined whether any contract existed at all was the toss, roughly 30 minutes before the first ball and after the freeze. This is a **timing** problem, not a retrieval-effort problem, and the conditional gate is the correct answer to it.


### Structural control addition


32. **Conditional activation is a first-class contract field — validated, keep verbatim.** Where a supplied contract is defined relative to an innings role ("first innings", "the team batting first", "the chase") and the toss has not been retrieved before the freeze, the card:


    1. stores the **activation condition** as an explicit field beside the contract, in the same place as the target and the settlement route;
    2. states, in advance, what happens if the condition fails — by name, with the specific alternative target that is **not** to be substituted;
    3. at settlement, evaluates the **activation condition before any outcome lookup**, and grades `NO ACTION / CONDITION NOT MET` without consulting the score;
    4. excludes non-activated rows from every W/L, Brier, Rank-#1, top-two and winner statistic, and records the card as a process event rather than a scored trial.


    A chase innings is **target-censored and tactically different** and can never settle a batting-first contract, however similar the phase looks: `P-445`'s Jamaica chase powerplay was 79/0 against a batting-first sample whose mean was 43.5. Origin `P-445`; this is the positive counterpart to the batting-first/chase confusions in the earlier log. **Where the toss is retrievable before the freeze it must be retrieved** (`G-L14`); the gate is for when it is not.


### Source note


The mini log settled this card from a `cricketworld.com` scorecard URL that is **not reproducible by this repository's retrieval ladder** — the page returns a Cloudflare interstitial through `r.jina.ai`. The reproducible route is the ESPN cricket lane, and **the CPL 2026 series ID `1534175` was already recorded in `DATA_SOURCE_REGISTER.md`** from `P-217`. Searching for a settlement route that the register already held is a `G-L14` execution miss; consult the register first. See `SOURCES.md` §"2026-09-17(b)".


### `G-L24` in cricket (added 2026-09-17(b))


Cricket run and wicket margins are different targets; successful chases terminate at the target. Derive each contract from its batting-first/chasing state and exact endpoint, never from a pooled winner-margin band. A missing pooled reference does not create an automatic rank bar. Unknown conditional exposure remains an evidence limitation. Preserve P-445 activation and NO ACTION handling.


### `G-L22`–`G-L23` in cricket (added 2026-09-17(b))


**`G-L22` — and cricket is the sport where this cuts the other way.** Most supplied cricket contracts are **`FREE`, not forced pairs**: an innings total, a powerplay total, a wicket row and a team total are separate targets, and a card can be right or wrong on each independently. That is a real structural advantage over the `{side, ¬side, over, under}` slate that MLB cards are handed, and it is most of why cricket and soccer card Briers in this log look better than MLB's — **contract geometry, not skill.** Label the rows anyway: where an operator does supply an exact complementary pair, mark it `FORCED_PAIR`, name the preferred side, and do not count it as two results. Never compare a free-row Brier with a forced-pair Brier without saying which is which.


**`G-L23`:** the process record is **phase runs and wickets** (powerplay, middle, death), the toss and innings order, and the ball-by-ball resource state; the disruption facts are **rain interruptions, DLS revisions, injuries and substitutions with the over and score**. A DLS revision is an **endpoint** event: a card whose target was revised mid-innings failed on the endpoint, not on its read of the surface, and no control may be amended from it as though the pitch assessment was wrong.


## Current model implementation — 2026-09-17


Use METHOD v4.2's six-field object and SCORING_AND_VALIDATION for exact outcome/push scoring, event-level comparison, descriptive recency and declared hierarchical uncertainty. MODEL_IMPLEMENTATION_RECIPES supplies this sport's retained model scope and endpoint design. Forecast probabilities come from the joint model; pooled base rates are uncertain context, not universal limits. Numeric row caps disconnected from that model, absolute-distance probability ordering and retrospective tail reweighting are withdrawn. No fitted coefficient or predictive improvement is claimed. New cards freeze the method/control hash; existing cards keep their issued versions.


## 2026-09-19 — recency/rebound evidence, debutant gate and the top-O/U review


Cross-sport: [`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md) control `R-1`; source controls `S-1` (social identity) and `S-2` (press conferences) in `SOURCES.md` §"2026-09-19"; enhanced-failure trigger in `METHOD.md` §7.


**`R-1` applies qualitatively; the magnitudes are `NOT_YET_DERIVED` for cricket and must not be imported from baseball.** Cricket has a stronger reason than most sports to distrust a single prior-innings comparator: the strip changes between matches, so a prior innings is a comparable drawn from a *different conditions* population. `P-457` moved a five-over centre to 37 on **one** observation (42/1 in the previous ODI, on a strip its own sources called "unusually grassy") and the realised figure was 29/0.


**Pitch/conditions ladder history — superseded prospectively by CR-2026.09.21-1.** The valid substance of the earlier Rung 7/8 amendment is retained but the numbering was internally duplicative: the old ladder already used the toss broadcast, while the amendment added it again. For forecasts under CR-2026.09.21-1, use §2's separate **TOSS FACT** and **STRIP/PITCH EVIDENCE** ladders. The preceding same-venue match remains `DIFFERENT_STRIP_CONTEXT` unless same-strip reuse is explicitly confirmed; the toss broadcast is a toss source and may also be an exact-strip source only when it contains a named current-match pitch assessment.


**Debutant gate.** ESPN's cricket `summary` carries an explicit **`debuts[]`** array naming each debutant and team — verified on `P-452`, which flagged Noor ul Rahman for Afghanistan. Query it for every XI once teams are named. A debutant is `NO_PRIOR_FORMAT_RECORD`: he contributes width, and no phase or innings row may rest on an assumed contribution from him.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** ICC/national-board/competition official scorecards, toss/team sheets/rules and verified pitch/weather; Cricsheet may support historical ball-level research subject to coverage/revision checks. Betting/fantasy/DFS sources are prohibited.


Model innings and phase totals from resource state: batting order, wickets/resources, bowling availability, venue/pitch, toss, weather and format/target censoring. Six-over/Powerplay and full-innings outputs must come from linked state dynamics rather than separately invented probabilities. The supplied line is queried only after the innings distribution is frozen.




## 2026-09-21 — cricket toss/strip source audit implementation — CR-2026.09.21-1


This is an **integrity/retrieval change only**. No forecast weight, run adjustment, probability boost or claimed accuracy gain is created.


New verified research lanes:
- official board/competition/rightsholder video as a first-class toss/pitch source;
- sanctioned NV Play/board-branded Match Centre for toss and live scoring where the competition officially uses it;
- specialist live-commentary transcript of a named broadcast pitch report, lineage-tagged to that broadcast;
- official toss-report pages that combine toss, XIs and captain comments on the wicket.


New controls:
- separate TOSS and STRIP statuses/ladders;
- `AUTOMATED_PITCH_METADATA` classification for unattributed feed-generated surface labels;
- shared-lineage fingerprinting for identical/near-identical unusual pitch blocks across front ends;
- `INSUFFICIENT_VENUE_HISTORY` as a legitimate venue-history state;
- field-specific `STALE` handling for official dynamic pages;
- mandatory toss-window plus final pre-issue refresh.


Required cricket output block:


```text
TOSS STATUS:
- Status:
- Winner:
- Decision:
- XI status:
- Source:
- Upstream lineage:
- Retrieved at:
- Pre/post toss:


STRIP STATUS:
- Status: OBSERVED / NOT_FOUND_AFTER_SEARCH / CONFLICTING / STALE_ONLY
- Exact-match source(s):
- Speaker/author:
- Observation/report:
- Strip number if known:
- Same-strip reuse confirmed?:
- Automated metadata present?:
- Context-only evidence:
- Search ladder attempted:
- Missingness/conflicts:


MATCH CONDITIONS STATUS:
- Weather source:
- Match-window weather:
- Interruption/DLS risk:
- Dew/light only if evidenced:
- Conditions signals and independence:


SOURCE-LINEAGE CHECK:
- Qualifying event lineages:
- Pitch lineages:
- Suspected duplicate feeds:
- Search snippets used as evidence? NO
```






<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


This section is the current prospective override for audit-derived ranking logic in this sport. Earlier dated examples remain historical evidence, but any incompatible active instruction is superseded.


- **Retained sport package:** legal-ball/resource phase mapping; XI and role continuity; toss, exact strip and match conditions kept separate; exact current-strip evidence; venue-format baseline with honest missingness; DLS/reduced-overs branches.
- **Withdrawn here:** second-highest/median or second-lowest/median pseudo-tail construction; path-count/category shortcuts as ranking rules; universal 40–60% top-slot bands; normalized-distance ordering; any one-result rebound/hangover/“due” rule; and any implication that a cushion determines the outright winner.
- **Current construction:** build one coherent sport-native joint outcome distribution/branch mixture, freeze it before supplied lines are queried, then derive exact target marginals and dependencies from that object. When a fitted/calibrated numerical distribution does not exist, a probability may be printed only as an `UNVALIDATED_SUBJECTIVE` output of the card's own complete, reproducible, declared distribution (METHOD §5). A number that cannot be reproduced from the printed distribution is invented precision and is not permitted. No subjective number carries a performance, calibration or value claim. *(Wording corrected 2026-09-25: the earlier "keep probabilities unquantified" contradicted METHOD §5; 2026-09-23 read-only audit item 5.)*

<!-- SETTLED-ROW-REVIEW-2026-09-25D -->
## 2026-09-25(d) — track record from the full settled-row review

**Track record (`C-TRACK-RECORD`).** 34 decisions from 14 cards: won 64.7% at a mean stated 0.630. Brier 0.227. Resolution is 0.039 but **reliability is 0.022**, the worst calibration of any sport with n ≥ 30: some skill, but mis-stated.

- **Unders won 9/12 at a stated 0.589; Overs 7/12 at 0.631** (`T-TOTAL-DIRECTION-LEAGUE`).
- This agrees with the earlier observation that buried powerplay-overs Unders keep winning. It also agrees with control 21: chase totals are capped by the target, and batting-first phase windows run lower.
- No direction coefficient follows. The response is the innings-order mixture (control 21) and `BASELINE_P` from the venue window where one exists.

Source: `research/settled_rows_2026-09-25/README.md`. The figures are hindsight on the framework's own cards, descriptive, and use card-cluster intervals. None is a coefficient (`L-087`). Controls: `RULES_GENERAL.md` §"2026-09-25(d)".


<!-- RANK-MODEL-2026-09-25E -->
## 2026-09-25(e) — Rank 1 and Rank 2 in cricket

Controls: `RULES_GENERAL.md` §"2026-09-25(e)".

**Record at Rank 1/2 (probability era): 17 W / 10 L.** Cricket has resolution but is mis-stated (reliability 0.022).

- **RM-1 applies its global recalibration only.** Cricket has no cushion-class rows, and RM-1 did not re-order any held-out cricket card. Rows stated at 0.55–0.60 read as coin flips (q about 0.53–0.61).
- **Settlement tables must print the contract text.**
  - Several cricket rows in the logs carry a result with a blank contract cell (P-352, P-356, P-357, P-364), so the dataset cannot classify them.
  - The canonical settlement table (`| Rank | Contract | Family | p | q | BASELINE_P | Result | Brier |`) is mandatory from 2026-09-25(e).
- **No TB-1 lane.** `TEAM_BASELINE_P: NOT_COVERED`. The anchors remain the chase cap and the venue window by innings order.
- **Unchanged:** the toss, strip and conditions ladders, and scorecard-only settlement. The Unders/Overs asymmetry stays TESTING.
