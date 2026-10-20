<!-- BEGIN CANONICAL RESEARCH P-613 -->
## P-613 — CRICKET / ODI Tri-Series · Pakistan vs Sri Lanka · 2026-10-18
Import: 2026-10-21T01:07:13+11:00; prompt 4 NEW_CANONICAL_EVENT. Local event key `LOCAL-20261018MELILL01-G0002` → canonical **P-613**; native identity ESPNcricinfo 1550713 (ODI no. 5037). Source mini `20261018MELILL01`, frozen source SHA-256 `f5163079058a28a8c9a900009f112838b0ca50c3f6985c8a363248d290b6e245` (142,555 bytes). Card core SHA-256 `9be9acad2d18763ef81c1702d84d71a36a4be6481483b0322d60aeaf6ddda314` (38,220 bytes) = the exact bytes between the local BEGIN/END CARD marker lines (source offsets 43006–81226); markers and headings outside them remain in the preserved source. Original method, probabilities, ranks, statuses, timing and gaps are literal; any NOT_ASSIGNED / PENDING wording inside the core is historical. Import is not a forecast timestamp and confers no certification.

## Card · LOCAL-20261018MELILL01-G0002 · CRICKET / Pakistan ODI Tri-Series · Pakistan vs Sri Lanka · 2026-10-18

### Owner-entered upcoming-game request (exact supplied contracts retained)

> Upcoming Cricket Game: Pakistan vs Sri Lanka, Tri-Nations ODI  
> Estimated Game Time Start: 18 October 2026, 7:00 PM AEDT (can be delayed so continue the process as normal)  
> Pakistan 1st Innings Runs at end of 50 overs Total: Over/Under 311.5 Runs  
> Pakistan 1st Innings Runs at the end of 5 overs: Over/Under 26.5 Runs  
> Research comprehensively using the latest GitHub main and verified official/public sources, including confirmed playing XI and injuries, four ranked contracts, winner, reasons and sources. No retrospective, score exposure, canonical import or settlement.

### Record metadata and authority

| Field | Status / evidence |
|---|---|
| Local event key | `LOCAL-20261018MELILL01-G0002` **PROVISIONAL COPY ONLY**; only use after duplicate/custody checks; native event surrogate `PCB-TRIODI-20261018-PAK-SL-M1`, official PCB tournament match number 1; ICC match page `/matches/274142/pakistan-vs-sri-lanka` |
| Canonical identifier | `NOT_ASSIGNED`; assigned only at verified PROMPT_4_IMPORT; no P-ID reserved |
| Authority | `PUBLISHED_MAIN_PINNED`, `danisgreat/Sports-Research`, commit `3e29a58693e2ed02ff862e9bf0f751af2feadee1`; `MDS/P v22.2` / `CR-2026.10.17-R6` / `SEL-2026.10.12-v3` / `SCV-v11` |
| References read | `research/prompts/1_GAME_CARD.md` shared steps; `research/prompts/1_sports/CRICKET.md` all seven steps; `RULES_CRICKET.md` §0; `PROBABILITY_TOOLKIT.md` §§1,7,9,11; `SELECTION_RULES.md` §§1–4; `BASE_RATES_REGISTER.md` cricket availability; preceding turn: `CURRENT_STATE`, `METHOD`, `CURRENT_RULES`, `CARD_AND_LOG_TEMPLATES`, `MINI_LOG_IDENTITY_PROTOCOL`, `HISTORICAL_SOURCE_PROTOCOL`, `ROSTER_AVAILABILITY_PROTOCOL`, `RESEARCH_COMPLETION_PROTOCOL`, `GAME_LOG_STATUS_CURRENT`; some entire long references not fully reread |
| Intended format | Men's one-day international, each side up to 50 overs, two white balls, 10-over initial powerplay, bowlers max 10 overs absent reduction; 5-over phase = after 30 legal balls, subject to early all-out/abandonment |
| Match/venue | PCB Pakistan–England–Sri Lanka men's ODI tri-series, match 1; Rawalpindi Cricket Stadium, Rawalpindi, Pakistan; 2026-10-18 13:00 PKT (+05:00) / 08:00 UTC / 19:00 AEDT (+11:00) |
| Toss | **Sri Lanka won and chose to bowl; Pakistan bats first**; current pre-start report https://www.thenews.pk/story/1443659-sri-lanka-win-toss-elect-to-bowl-first-against-pakistan-in-tri-nation-series-opener (18 October 2026). Not independently corroborated from a timestamped official scorecard; `SECONDARY_CONFIRMED/PRIMARY_UNVERIFIED` |
| Research/issue timing | Completed after scheduled start (19:00 AEDT); research session check after 19:06 AEDT. `POST_START_ISSUE` / `NOT_PROSPECTIVE_PRESTART`. Actual ball-one time not independently verified. No in-play or final score read for inference; sourced pre-start lineups/toss evaluated only when publication timing is explicit. Any source unverified before first ball is `KNOWN_AT_UNVERIFIED` |
| Model scope | `ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY`, hand-derived normal-mixture approximation, not trained/calibrated ML. No code/model/RL, no external prediction, odds, tips, implied market probabilities or bookmaker sources |
| Contract endpoint | Pakistan's **first innings** (it bats first). Innings ends at 50 overs or dismissal; a total beyond 311.5 can be reached before 50 overs. Five-over endpoint = runs after exactly five completed overs, when reached. No score substituted from a chase. Provider-specific reduced-overs/void rules UNVERIFIED |
| Weather | Pre-start Rawalpindi hazy sun forecast, roughly 1% rain probability from available daily forecast, but no live meteorological guarantee; exact surface `STRIP_UNCONFIRMED` |
| Performance | Research-only; NOT_PERFORMANCE_ELIGIBLE; INFORMATION_INCOMPLETE because official XI/phase inputs, operator settlement and full independent history corroboration not closed |
| Source state | Scores from previous dates only; match's live score/result/outcome NOT_USED; no retrospective or settlement |

### Decision block — four supplied propositions

| Rank | Role | Supplied exact contract | p_card | p_base | BASELINE_P | P(win)/P(loss)/P(push)/P(void)* | Signed line distance / z | Main failure mechanism |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | PICK | **Pakistan first innings Under 311.5 runs, up to 50 overs** | **0.732** | 0.740 | `BASELINE_UNAVAILABLE: exact ODI first-innings cohort/window not verified` | .732/.268/0/0 | 311.5−277.75=+33.75; z_base=.644 | Pakistan's top order remains intact; unusually fast scoring, favourable pitch, SL attack absence |
| 2 | PICK | **Pakistan first innings Over 26.5 runs after 5 completed overs** | **0.606** | 0.608 | `BASELINE_UNAVAILABLE: verified 5-over field-owner history lacking` | .606/.394/0/0 | 26.5−29.5=−3.0; z_base=−.273 | Early wicket(s), powerplay swing/seam, opener dot-ball cluster |
| 3 | INFORMATIONAL | Pakistan first innings Under 26.5 runs after 5 completed overs | 0.394 | 0.392 | BASELINE_UNAVAILABLE | .394/.606/0/0 | +3.0 runs from 5-over mean | Fast first five overs, boundaries/extras |
| 4 | INFORMATIONAL | Pakistan first innings Over 311.5 runs, up to 50 overs | 0.268 | 0.260 | BASELINE_UNAVAILABLE | .268/.732/0/0 | +33.75 runs above projected full mean | Middle-order slowdown, wickets, 300-level ceiling |

\* `W/L/P/V` are conditional on two decisive, normally completed innings/phase endpoints and operator rules treating each half-run line as a two-way contract. These are **not unconditional no-result/void-inclusive masses**, because the user's operator was not provided. No in-play status or outcome has been used to grade them.

**Rank-1 gate:** p≈0.732 ≥ 0.62; next eligible non-complementary p≈0.606; lead≈0.126 ≥ 0.04; `PASS_BASE_SCENARIO`, ε≥0.002 for Φ-table precision and materially greater structural uncertainty. High-scoring sensitivity changes the order; `SCENARIO_UNSTABLE`, not a robust performance claim. **Rank-2 floor:** p≈0.606 ≥ 0.58 (`PASS_BASE`, yet not calibrated). Only two picks; the remaining two are complement rows. All four supplied rows printed without threshold shopping or invented replacement lines.

**Potential outright winner:** **Pakistan, conditional estimate approximately 0.60** (Sri Lanka approximately 0.40, excluding tie/no-result/DLS ambiguity). This is a separate, low-confidence analyst judgement from home venue, 2025 home ODI head-to-head and squads, **NOT** output from the quantified first-innings distribution, and not a calibrated win probability. Winner endpoint/tie/no-result shares NOT_COMPUTED; therefore the full three-/four-way winning state is INCOMPLETE. Confidence is lower than a 60% label may suggest.

**Decision rationale:** Pakistan's historical last-20 ODI innings averaged 237.5, but this includes shortened successful chases; this does not imply a 237.5 batting-first expectation. Sri Lanka conceded 282.2 per game across its last ten ODIs, while Pakistan posted 299/5 batting first against Sri Lanka in Rawalpindi in Nov 2025. The 311.5 total is above the conditional first-innings centre of 277.75 by 33.75. In contrast, Pakistan clearing 26.5 in five overs is a small cushion above the expected first-five run centre 29.5 and is sensitive to the unconfirmed opening batters/new-ball attack and actual strip. Both selected rows can lose together: a very slow opening followed by a later high score or a very fast opening coupled with below-312 finish has different consequences; their precise joint dependence is NOT estimated.

### A1. Fixture, temporal identity, format, toss and existing-record checks

- PCB official tournament fixture https://www.pcb.com.pk/tournament-reports.php?action=tournament_matches&sort_by=date_start&sort_order=desc&tournament_id=1465 lists 18 Oct match 1 at Rawalpindi. ECB corroboration https://www.ecb.co.uk/news/4562387/pakistan-to-host-sri-lanka-and-england-in-odi-triseries . PCB pregame announcement https://www.pcb.com.pk/press-release-detail/pakistan-england-sri-lanka-set-to-begin-preparations-for-odi-world-cup-with-tri-series-from-18-to-31.html confirms 13:00 PKT start / 12:30 PKT toss.
- Exact user contracts are Pakistan batting-first full 50-over total and first 5 overs, not Pakistan's second innings, not Sri Lanka's innings, not the match total, and not a T20 powerplay.
- Reported toss Sri Lanka field first as linked in metadata. Official match sheet, XI/bench and precise first ball time were not independently verified at research issue. Do not backdate a pre-start release because user submitted earlier.
- Existing combined canonical register latest pinned: P-600 highest, P-601 next; read-only contextual information; no claimed direct GitHub append. An extant active mini and exclusive writer lease are unverified. The prior MEL–ILL full MD is an **unissued draft**, not a verified active mini; this card's key is a **provisional continuation for the supplied cumulative draft copy**, not a reservation against other minis. Duplicates must be reconciled by the repository owner.
- No separate ODI match of these opponents on this date confused with Pakistan's preceding Oct 9–13 Sri Lanka T20Is or Nov 2025 three-ODI series.

### A2. Freeze the four user supplied lines and rules

| Contract key | Team | Period | Exact line | Action definition | Uncertainty |
|---|---|---|---|---|---|
| PAK_RUNS_INN1_50_O3115 / U3115 | Pakistan batting first | Innings 1, maximum 50 overs | 311.5 | Over ≥312; Under ≤311 in a completed, 50-over-scheduled innings | No specific operator void/reduction convention provided; team may be all out earlier |
| PAK_RUNS_INN1_05_O265 / U265 | Pakistan batting first | Total at 5.0 overs (30 legal balls) | 26.5 | Over ≥27; Under ≤26 | Can cease before 5 overs if all out/abandoned; operator's action not verified |

These two pairs are `FORCED_PAIR` complement relationships under a fully decisive endpoint; they cannot be four independent suggestions or combined for an artificial Hit@2. No price/odds supplied and no financial expected value computed. ODI powerplay lasts 10 overs; this five-over line is **not** the full powerplay.

### A3. Squad/selection, injury, bowlers and prior game history

**Pakistan (PCB announced 16-player ODI squad):** Shaheen Shah Afridi (captain), Abrar Ahmed, Salman Ali Agha, Arafat Minhas, Babar Azam, Faheem Ashraf, Fakhar Zaman, Muhammad Ghazi Ghori (wk), Haris Rauf, Hasan Nawaz, Naseem Shah, Razaullah, Saad Baig (wk), Saim Ayub, Shadab Khan, Sufiyan Moqim. Official source (5 Oct) https://www.pcb.com.pk/press-release-detail/pakistan-squads-announced-for-sri-lanka-t20is-and-odi-tri-series.html ; squad training confirmed PCB 15 Oct https://www.pcb.com.pk/press-release-detail/pakistan-odi-squad-begins-preparations-for-tri-series.html . Mohammad Rizwan is **not** in this ODI squad. Sahibzada Farhan and Maaz Sadaqat were on T20 duty, not the named ODI squad; do not transfer their T20 5-over scores to this ODI XI. **Confirmed openers, Nos. 3–4, wicketkeeper selection, actual bat-first batting order: NOT_VERIFIED**. Expected opener candidates Saim Ayub and Fakhar Zaman are projections, not an exact XI.

**Sri Lanka (ICC 4 Oct original conditional squad):** Kusal Mendis (capt/wk), Sahan Arachchige, Dushmantha Chameera, Sachindu Colombage, Avishka Fernando, Asitha Fernando, Janith Liyanage, Dilshan Madushanka, Eshan Malinga, Kamindu Mendis, Kamil Mishara, Pathum Nissanka (subject to medical clearance), Pavan Rathnayake, Dasun Shanaka, Maheesh Theekshana, Dunith Wellalage: https://www.icc-cricket.com/news/sri-lanka-unveil-odi-squad-for-tri-series-in-pakistan . **Revision (16 Oct)**: Pathum Nissanka ruled out by hamstring injury after no medical clearance; Lahiru Udara called in, reported by https://www.thenews.pk/print/1443109-nissanka-ruled-out-of-tri-series-as-pakistan-sl-step-up-preparations . **Wanindu Hasaranga injured/unavailable**; Sahan Arachchige is named among the replacement squad, reported https://www.wisden.com/series/pakistan-odi-tri-series-2026/cricket-news/pakistan-tri-series-2026-all-you-need-to-know-full-schedule-squads-venues-and-match-timings-for-the-odi-tri-series . Do not assume Nissanka played or Wasaranga bowled, and do not confuse a named squad with a final selected XI. **Confirmed Sri Lanka new-ball bowling pair, XI and bench: NOT_VERIFIED**.

**Conditional roster effects:** A missing Sri Lankan attacking spin option (Hasaranga) can affect middle-overs wickets/ceiling; size NOT_QUANTIFIED without opponent-adjusted role data. Nissanka's absence affects Sri Lanka's chase-strength/possible winner, **not Pakistan's first five overs batting directly**. Pakistan keeper/top-order selections could change batting depth; no fake run adjustments were applied. Player-specific current ODI balls faced, first-five strike rates and bowler five-over economy not verified, so not used as numerical evidence. No official exact-match medical clearances or final late XI announcement confirmed; `LINEUP_UNCONFIRMED` / `INFORMATION_INCOMPLETE`.

**Pakistan men's ODI results, most recent 20 eligible completed games (scores from Pakistan perspective; batting first / chase and reduced innings distinguished).** Series results cross-referenced through historical PCB/ICC/ESPN scorecards and Wisden series records (see A8), but NOT every row independently opened and double-verified; `ROW_CORROBORATION_OPEN`.

| Date | Opponent | Pakistan runs (overs) | Opponent runs (overs) | Pakistan innings role / context |
|---|---|---|---|---|
| 2026-06-04 | Australia | 161/6 (41.5) | 157 all out (42.0) | Chase ended early |
| 2026-06-02 | Australia | 190 all out (44.0) | 231/9 (50.0) | Chase, all out |
| 2026-05-30 | Australia | 202/5 (42.3) | 200 all out (44.1) | Chase ended early, Rawalpindi |
| 2026-03-15 | Bangladesh | 279 all out (50.0) | 290/5 (50.0) | Chase |
| 2026-03-13 | Bangladesh | 274 all out (47.3) | 114 all out (23.3) | Bat first; DLS-result context |
| 2026-03-11 | Bangladesh | 114 all out (30.4) | 115/2 (15.1) | Bat first |
| 2025-11-16 | Sri Lanka | 215/4 (44.4) | 211 all out (45.2) | Chase ended early, Rawalpindi |
| 2025-11-14 | Sri Lanka | 289/2 (48.2) | 288/8 (50.0) | Chase ended early, Rawalpindi |
| 2025-11-11 | Sri Lanka | 299/5 (50.0) | 293/9 (50.0) | Bat first, Rawalpindi |
| 2025-11-08 | South Africa | 144/3 (25.1) | 143 all out (37.5) | Chase ended early |
| 2025-11-06 | South Africa | 269/9 (50.0) | 270/2 (40.1) | Bat first |
| 2025-11-04 | South Africa | 264/8 (49.4) | 263 all out (49.1) | Chase ended early |
| 2025-04-05 | New Zealand | 221 all out (40.0) | 264/8 (42.0) | Bat in rain-shortened 42-over ODI; not full 50 |
| 2025-04-02 | New Zealand | 208 all out (41.2) | 292/8 (50.0) | Chase |
| 2025-03-29 | New Zealand | 271 all out (44.1) | 344/9 (50.0) | Chase |
| 2025-02-23 | India | 241 all out (49.4) | 244/4 | Bat first |
| 2025-02-19 | New Zealand | 260 all out (47.2) | 320/5 | Chase |
| 2025-02-14 | New Zealand | 242 all out (49.3) | 243/5 | Bat first |
| 2025-02-12 | South Africa | 355/4 (49.0) | 352/5 (50.0) | Chase ended at victory, overshoot allowed |
| 2025-02-08 | New Zealand | 252 all out (47.5) | 330/6 | Chase |

**Sri Lanka men's ODI results, most recent 20 eligible completed games (scores from Sri Lanka perspective):**

| Date | Opponent | Sri Lanka runs (overs) | Opponent runs (overs) | Context |
|---|---|---|---|---|
| 2026-09-27 | England | 132 all out (29.1) | 355/7 (50.0) | Chase |
| 2026-09-24 | England | 321/6 (50.0) | 305/9 (50.0) | Bat first |
| 2026-09-22 | England | 176 all out (37.0) | 265 (48.1) | Chase |
| 2026-06-03 | West Indies | 303/7 (50.0) | 262 (49.2) | Bat first |
| 2026-01-27 | England | 304 (46.4) | 357/3 (50.0) | Chase |
| 2026-01-24 | England | 219 (49.3) | 223/5 (46.2) | Bat first |
| 2026-01-22 | England | 271/6 (50.0) | 252 (49.2) | Bat first |
| 2025-11-16 | Pakistan | 211 (45.2) | 215/4 (44.4) | Bat first, Rawalpindi |
| 2025-11-14 | Pakistan | 288/8 (50.0) | 289/2 (48.2) | Bat first, Rawalpindi |
| 2025-11-11 | Pakistan | 293/9 (50.0) | 299/5 (50.0) | Chase, Rawalpindi |
| 2025-08-31 | Zimbabwe | 278/5 (49.3) | 277/7 (50.0) | Chase ended at victory |
| 2025-08-29 | Zimbabwe | 298/6 (50.0) | 291/8 (50.0) | Bat first |
| 2025-07-08 | Bangladesh | 285/7 (50.0) | 186 (39.4) | Bat first |
| 2025-07-05 | Bangladesh | 232 (48.5) | 248 (50.0) | Chase |
| 2025-07-02 | Bangladesh | 244 all out | 167 all out | Bat first; exact overs not confirmed |
| 2025-02-14 | Australia | 281/4 (50.0) | 107 (24.2) | Bat first |
| 2025-02-12 | Australia | 214 all out (46.0) | 165 (33.5) | Bat first |
| 2025-01-11 | New Zealand | 290/8 (50.0) | 150 (29.4) | Bat first |
| 2025-01-08 | New Zealand | 142 all out (30.2) | 255/9 (37.0) | Chase in reduced-overs ODI |
| 2025-01-05 | New Zealand | 178 all out (43.4) | 180/1 (26.2) | Bat first |

**Compiled form aggregates; individual underlying score rows still require independent corroboration** (overlapping windows count once; simple completed-score mean is NOT a full-50-over mean):

| Side | Window | true n | Scored / match | Conceded / match | Mean signed run difference | Coverage and limitation |
|---|---|---:|---:|---:|---:|---|
| Pakistan | L5 | 5 | 221.2 | 198.4 | +22.8 | 2026-03-13 to 2026-06-04; multiple completed chases |
| Pakistan | L10 | 10 | 216.7 | 204.2 | +12.5 | 2025-11-08 to 2026-06-04 |
| Pakistan | L15 | 15 | 226.7 | 231.7 | −5.0 | 2025-03-29 to 2026-06-04 |
| Pakistan | L20 | 20 | 237.5 | 248.2 | −10.7 | 2025-02-08 to 2026-06-04; includes reduced-overs game |
| Sri Lanka | L5 | 5 | 247.2 | 308.8 | −61.6 | 2026-01-27 to 2026-09-27 |
| Sri Lanka | L10 | 10 | 251.8 | 282.2 | −30.4 | 2025-11-11 to 2026-09-27 |
| Sri Lanka | L15 | 15 | 257.0 | 266.1 | −9.1 | 2025-07-02 to 2026-09-27 |
| Sri Lanka | L20 | 20 | 248.0 | 242.4 | +5.6 | 2025-01-05 to 2026-09-27; includes reduced-overs game |

- Cricket format: international men's ODIs only, completed official matches; abandoned/washout games excluded. Date of latest eligible historical fixture 27 Sep (SL), 4 Jun (PAK). Recent ODI sample small and time-stale for PAK; roster changes mean past teams not identical.
- Season-to-date: no natural common ODI league season; tournament has no prior games (`n=0`); cricket ODI rolling form windows used instead. League/venue level: Cricbuzz Rawalpindi all-time first-innings ODI mean reported **242 across 31 matches**, mixture of eras/teams; `STALE_VENUE_REGIME`, not a current-season fitted baseline. No `BASELINE_LEAGUE_V1` with verified matching 2026 batting-first first-five cohort available. Do not present 242 as 2026-specific.
- **R2 window blend for comparison:** `WEIGHTS/RECIPE_NOT_FULLY_REPRODUCED` because overlapping windows cannot be independent fitted sample rates and the current true global ODI baseline/strength-adjusted opposition schedule is missing. No invented k or derived adjusted team strengths; manual scenario-centres below are exposed judgement rather than falsely labelled R2 output. Pakistan raw L20 237.5 is not automatically an expected 50-over innings, because many innings stopped when targets were reached. Season league means, strengths and exact 5-over distributions remain MISSING.
- Historical sources and independent verification attempts are in A8. Abandoned matches, 2026 recent T20s and game-day ODI outcomes are excluded from scoring windows. Rows with exact innings overs unclear are labelled rather than manufactured. **Windows overlap; counted once.**

### A4. Conditional distribution, arithmetic, expected score and sensitivity

**Why no exact ball-by-ball model:** No verified pre-first-ball live official XI, top-four ordering, new-ball pairing, recent five-over scores with legal-ball deliveries, or pitch strip data. No historical verified venue/phase residual variance estimate. Therefore the below is a transparent, **subjective analyst approximation** with uncertain inputs, not a calibrated fit, bootstrap or true derived innings/wicket transition grid. Model widths are assumptions; the missing inputs prevent objective accuracy assessment.

**Full first-innings runs:** one conditional three-component **normal approximation** for completed 50-over-scheduled innings including all-out termination in the historical dispersion; scenario weights low/base/high = 0.25 / 0.50 / 0.25, centres μ = 255 / 278 / 300 runs, common assumed SD = 52.0 runs. Rationale: blended manually from Pakistan's recent completed innings including a 299/5 first-innings ODI versus this opponent at the venue, Sri Lanka's recent L10 conceded 282.2, historical venue mean 242; scenario range for pitch/XI uncertainty. Does **not** assert a measured 52-run residual or mathematically explicit 10-wicket state: this remains the main structural limitation. Mean = .25×255 + .50×278 + .25×300 = **277.75 runs**; width ~54.4 after between-scenario spread, not a calibrated confidence interval.

\[
P(U311.5)=\sum_{j\in\{L,B,H\}}w_j\,\Phi((311.5-\mu_j)/52)
\]

- LOW z=(311.5−255)/52=1.087; Φ≈0.861; contribution .25×.861=.2153.
- BASE z=(311.5−278)/52=0.644; Φ≈0.740; contribution .50×.740=.3700.
- HIGH z=(311.5−300)/52=0.221; Φ≈0.588; contribution .25×.588=.1470.
- **Under 311.5** ≈ .2153+.3700+.1470=**0.7323**; **Over 311.5** ≈ 1−.7323=**0.2677**. Φ interpolation ε≈.002; additional model/parameter uncertainty much larger. Half-line yields no push if the innings contract is decisive.

**Pakistan first 5 completed overs:** separate conditional three-component normal **marginal approximation**, scenario weights 0.25/0.50/0.25, centres μ_5 = 27 / 29.5 / 32 runs, common **assumed** SD=11 runs; arbitrary judgement informed by plausible early ODI scoring, **not** derived from a verified opening-30-ball sample. This quantity is intrinsically integer and nonnegative; Gaussian tail below zero is a small unnormalised approximation (base Φ(−29.5/11) about 0.004), disclosed as such. No direct link to wickets modelled. Mean=29.5 runs.

- LOW z=(27−26.5)/11=.045; P(Over26.5)=Φ(.045)≈.518; weighted .25×.518=.1295.
- BASE z=(29.5−26.5)/11=.273; P(Over26.5)=Φ(.273)≈.608; weighted .50×.608=.3040.
- HIGH z=(32−26.5)/11=.500; P(Over26.5)=Φ(.5)≈.6915; weighted .25×.6915=.1729.
- **Over 26.5** ≈ .1295+.3040+.1729=**0.6064**; **Under 26.5** ≈ **0.3936**. Rounding to three decimals: .606 and .394.

**Scenario probabilities (not 95% confidence bounds):**

| Scenario / assumption | Under 311.5 | Over 26.5 | Consequence |
|---|---:|---:|---|
| Low: 255-run innings / 27 after five | 0.861 | 0.518 | Under stronger, first-five Over no longer rank-2-floor eligible |
| Base: 278-run innings / 29.5 after five | 0.740 | 0.608 | Both directions favoured |
| High: 300-run innings / 32 after five | 0.588 | 0.692 | Over five becomes Rank 1, total Under falls below Rank-1 threshold |
| Weighted primary | **0.732** | **0.606** | Scenario-dependent rankings; don't claim robust gate |

**Score/wickets expected object:** Pakistan first-innings runs 277.75, conditional full-overs-scheduled; projected five-over runs 29.5, SD 11 assumed. Wickets lost at five overs, total wickets/expected overs remaining, Sri Lanka response, run covariance, win margin and no-result probability **NOT_COMPUTED**; no falsely precise 50-over team v team score projected. The two marginal approximations don't constitute a physical monotone ball-by-ball shared grid; P(5-over result, 50-over result) joint is **unquantified**.

**Joint failure bounds, selected Rank 1 Under311.5 and Rank 2 Over26.5:** losses are innings Over311.5 p≈.268 and first-five Under26.5 p≈.394. Without a verified joint phase→innings model, Fréchet: `max(0,.268+.394−1)=0 ≤ P(both lose) ≤ min(.268,.394)=.268`. Historical diagnostic threshold 0.30/0.35 is not crossed at upper bound under these assumed marginals, but the true joint not estimated, and parameter uncertainty is omitted. Do **not** multiply as if independent.

**Baseline and EV:** Venue first-innings historical mean 242 with n=31 is contextual only, unverified source-date cutoff and mismatched competition-era; a valid matching league-only BASELINE_P is not reproducible. Five-over baseline unavailable. No market odds or stake conditions supplied; monetary EV cannot be computed and market odds are excluded under SPORTS_ONLY. Probabilities above are *not* price edges or validated advantages. `TEAM_BASELINE_P: NOT_COVERED_FOR_CRICKET`.

### A5. Full supplied candidate universe and exact complements

| Distinct quantity | Line | Side | Approximate p_card | p(loss) | Decision |
|---|---:|---|---:|---:|---|
| Pakistan bat-first innings runs | 311.5 | Under | .732 | .268 | Rank 1; selected |
| Pakistan after 5.0 overs runs | 26.5 | Over | .606 | .394 | Rank 2; selected |
| Pakistan after 5.0 overs runs | 26.5 | Under | .394 | .606 | Informational direct opposite |
| Pakistan bat-first innings runs | 311.5 | Over | .268 | .732 | Informational direct opposite |

No additional analyst-derived thresholds manufactured. Complement arithmetic `.732+.268=1.000`, `.606+.394=1.000`. No exact conditional pair correlation computed. A no-result or five-over-shortened match may trigger operator-specific void, not modelled as zero in unconditional probability.

### A6. Pitch, availability, toss, weather, conditions and alternatives

| Material input | Observed pre-start evidence | Applied effect / honest limit |
|---|---|---|
| Pakistan innings role | Sri Lanka chose to field, current 18 Oct source | Bat-first scenario only; no chase-target censoring for Pakistan's first innings |
| Current pitch strip | No independent official strip report verified | Three centres 255/278/300; cannot assert hard/flat/green pitch or seam swing |
| Historical venue | Previous Pakistan 299/5 vs Sri Lanka Nov 2025; venue compiled ODI mean ~242/31 | Old-game context, not first-five-phase rate nor current strip |
| Sri Lanka Hasaranga absence | Injured, squad change reported before match | Could weaken spin wicket containment in overs 11–40; *no numerical adjustment fitted* |
| Sri Lanka Nissanka absence | Hamstring injury, replacement Lahiru Udara (16 Oct) | Lowers/changes potential Sri Lanka batting side, not directly Pakistan first-innings run total |
| Pakistan top-order selection | ODI squad Babar, Fakhar, Saim, Salman; XI unverified | Unconfirmed opener composition; principal early-5-overs sensitivity |
| Sri Lanka new-ball pair | Chameera/Asitha Fernando/Madushanka/Malinga in squad; XI and allocations unverified | Critical uncertainty for Over26.5, no invented bowler economy |
| Weather/DLS | Pre-match forecast low rain risk; official rain/wet outfield not checked | Full 50-overs assumed; reduced innings case and void conventions unresolved |
| Recent T20Is at venue | 9–13 Oct 2026 Pakistan v Sri Lanka T20 series; separate teams/squads | Not pooled with ODI phase/innings distributions |
| Rest | ODI squads prepared at venue 15–17 Oct; SL some players had T20 series | No unverified fatigue-based expected-run adjustment |

Base figures are centre assumptions, not inferred numerical causal effects. Unadjusted counterfactual absent a fully fitted dataset is `NOT_COMPUTED`; label sensitivity `SCENARIO_UNSTABLE`. Any player-specific confirmed absence effect cannot be isolated with present data.

### A7. Statistical controls, comparisons and gates

- `P_ORDER_V2`: only four exact supplied directions priced; ranked by p_card; rank 1 and 2 are primary picks, 3 and 4 informational; no q tiers.
- **Rank-1 numerical gate:** PASS on chosen manual mixture at p .732, best independent alternative p .606, lead .126; in high-run scenario it fails for Under 311.5 and row order changes; `ADJUSTMENT_DEPENDENT/SCENARIO_UNSTABLE`.
- **Rank-2 floor:** PASS base at .606 but LOW scenario .518 fails. No extra confidence attributed to provider line or toss alone.
- `RET03` shadow gate (exclude same innings quantity as Rank 1): Over26.5, .606, lead .126, PASS_BASE. `RET04` alternate different quantity: same Over26.5; NOT_PRIMARY. `XCARD6` exact-joint failure optimization: NOT_COMPUTED, Fréchet interval only. `RANK_DELTA`: NONE because no frozen league-only comparator. `BASE_ONLY`: Under311.5 .740, Over26.5 .608; same rank1/2.
- `PRECISION ε`: .002 per Φ reading from official repo normal table, but true epistemic error from unvalidated μ, σ and missing innings/phase physical transition parameters is far larger; ε is not an accuracy uncertainty bound.
- `SAME-QUANTITY`: Over/Under at each threshold forced complements; no dummy Hit@2 credit, no pushes for half-run lines under a decisive endpoint.
- `PERFORMANCE_ELIGIBLE`: NO. Previous ODI examples are sourcing and contextual form, not an out-of-sample evaluation of this method.

### A8. Source registry, exact fields, attempts, unfinished corroboration

The following are the specific research routes that informed this card. Publication/retrieval precise ISO timestamps were not exposed for every item; source-known-before-first-ball remains unverified when not date-stamped. Every game row needs point-in-time official box-score and independently collected second lineage before this evidence set can be marked complete.

| Source / original URL | Relevance; field and limitations |
|---|---|
| https://www.pcb.com.pk/press-release-detail/pakistan-england-sri-lanka-set-to-begin-preparations-for-odi-world-cup-with-tri-series-from-18-to-31.html | PCB 17 Oct match time (13:00 PKT), scheduled toss (12:30 PKT), tri-series |
| https://www.pcb.com.pk/tournament-reports.php?action=tournament_matches&sort_by=date_start&sort_order=desc&tournament_id=1465 | PCB organizer tournament match 1, date, venue |
| https://www.ecb.co.uk/news/4562387/pakistan-to-host-sri-lanka-and-england-in-odi-triseries | ECB independently corroborates teams/fixture/venue/date |
| https://www.thenews.pk/story/1443659-sri-lanka-win-toss-elect-to-bowl-first-against-pakistan-in-tri-nation-series-opener | 18 Oct toss Sri Lanka bowl first; one reporting lineage, official feed corroboration pending |
| https://www.pcb.com.pk/press-release-detail/pakistan-squads-announced-for-sri-lanka-t20is-and-odi-tri-series.html | PCB 5 Oct exact Pakistan 16-player ODI squad vs separately named T20 squad |
| https://www.pcb.com.pk/press-release-detail/pakistan-odi-squad-begins-preparations-for-tri-series.html | PCB 15 Oct training participants and role groups |
| https://www.icc-cricket.com/news/sri-lanka-unveil-odi-squad-for-tri-series-in-pakistan | ICC SLC 4 Oct 16-player list; Nissanka only conditional upon clearance |
| https://www.thenews.pk/print/1443109-nissanka-ruled-out-of-tri-series-as-pakistan-sl-step-up-preparations | 16 Oct dated Nissanka medically ruled out and Lahiru Udara called up; Sri Lanka match XI still unverified |
| https://www.wisden.com/series/pakistan-odi-tri-series-2026/cricket-news/pakistan-tri-series-2026-all-you-need-to-know-full-schedule-squads-venues-and-match-timings-for-the-odi-tri-series | 16 Oct squad comparison; Hasaranga injury and Arachchige role |
| https://www.pcb.com.pk/match/36405.html | **11 Nov 2025** PAK 299/5 and SL 293/9 ODI, Rawalpindi; historical, NOT today |
| https://www.cricbuzz.com/live-cricket-scorecard/170720/pak-vs-sl-1st-odi-match-pakistan-odi-tri-series-2026 | 18 Oct fixture/scorecard route, pre-match indexed; no score/playing XI used from live section |
| https://www.icc-cricket.com/matches/274142/pakistan-vs-sri-lanka | ICC exact 18 Oct match centre route; direct opening returned cache-miss, no XI claim |
| https://www.cricbuzz.com/cricket-series/ (search cricket ground records for Rawalpindi ODI) | Rawalpindi historical 31 ODI/242 first-innings mean from structured ground-stat discovery; current-regime count/time not certified |
| https://www.pcb.com.pk/ | Official Pakistan cricket match scorecards and team announcements as field-owner, match by date, Nov 2025/2026 home fixtures |
| https://www.icc-cricket.com/ | Independent international governing-body current ODI fixture and prior-series scorecards |
| https://www.espncricinfo.com/ | Cricket match scorecards/schedules for PAK AUS May–June 2026, Bangladesh March, NZ March–April 2025, SL England September 2026 and Jan 2026, WI June 2026, 2025 bilateral ODI games; individual exact paths not fully retained |
| https://www.wisden.com/ | Prior-series scorecard index and dated historical aggregates; does not by itself independently collect every official ball count |
| https://www.accuweather.com/ | Rawalpindi 18 Oct dated pre-match forecast: hazy sun, low precipitation probability; location/product exact route and issued time not retained |
| GitHub at SHA `3e29a58693e2ed02ff862e9bf0f751af2feadee1`: `PROBABILITY_TOOLKIT.md`, `BASE_RATES_REGISTER.md`, `SELECTION_RULES.md`, `RULES_CRICKET.md`, `research/prompts/1_sports/CRICKET.md` and shared core | Manual normal-mixture rule, historical cricket baseline not derived, selection thresholds, game-log statuses |

**Required open-field attempts/closure status:**

| Field | Actual search or comparison performed | Status / next field-owner route |
|---|---|---|
| Match ID/date, tournament | PCB + ECB organizer releases and ICC listed match | CLOSED at fixture level; native event IDs beyond ICC URL not independently reconciled |
| Toss and bat-first activation | Current 18 Oct independently dated local report | PARTIAL; open PCB exact match official toss and publication timestamp |
| Pakistan XI, openers, batting order, bench | PCB 5 Oct squad, PCB training, current match centre search | NOT_VERIFIED; PCB match 1 XI / scorecard selection, pre-first-ball timestamp |
| Sri Lanka XI, new-ball pair, bench | ICC 4 Oct squad, 16 Oct Udara report; official match centre discovery | NOT_VERIFIED; SLC/PCB XI and exact new-ball roles publication/time |
| Pakistan and Sri Lanka injury/selection | PCB official roster; ICC original SLC roster; latest Nissanka replacement; Hasaranga replacement coverage | PARTIAL; exact-match last-minute scratch/injury updates require checking |
| Form L5/L10/L15/L20 | Schedules/scorecards compiled into true-n, with reduced-overs and chase annotations | PARTIAL; row-by-row independent official+provider corroboration and correction/overs of some fixtures needed |
| Five-over phase sample | Scorecard/feed routes for 2025 and 2026; no systematic five-over legal-ball data recovered | MISSING; derive actual five-over runs/wickets by official ball-by-ball for each bat-first ODI before cutoff |
| Current venue pitch strip | Venue history and pre-match preview routes | NOT_VERIFIED; field-owner strip/pitch report and ground staff/official toss statements |
| Weather and DLS | Pre-match daily forecast | PARTIAL; official ground match conditions, precipitation radar/forecast time, interruption risk |
| Same-line venue baseline | Historical reported first-innings mean 242/31; not exact-era matched | MISSING; filter all ODI 50-over first-innings scorecards in chosen date interval and map historic full overs |
| Physical innings-wickets/phase joint | No verified bowling allocation or 5-over probabilities | NOT_COMPUTED; cannot claim exact joint or physically constrained grid |
| Operator action | User provided lines without bookmaker/operator | UNKNOWN_DEFINITION; obtain specific 50-over and phase rain/wicket rules if settling |
| Writer lease and verified cumulative active source | Checked GitHub active_minis inventory and previous local standalone draft; no verified active original | BLOCKED_APPEND; reconcile issuing writer before any official mini update |

### A9. Verification matrix, safety and file readback

| Requirement | Result |
|---|---|
| Step 1 GitHub pinned main and relevant controls | PASS for named controls; some lengthy ancillary sections not exhaustively reread |
| Step 2 official fixture/format/venue/toss | Fixture confirmed, toss single second-lineage report; exact first-ball and operator rules not independently verified |
| Step 3 exact XI, starters, bench, absences | Injury/squad updates covered; both XIs and new-ball pair OPEN; C20 INFORMATION_INCOMPLETE |
| Step 3 both teams' last 5/10/15/20 | True n=5/10/15/20 printed, pre-date rows, chases and reduced games annotated; independent row-by-row verification OPEN |
| Step 4 innings and phase conditional math | Four supplied numeric directions priced, formulas/weights/centres/widths shown; no predictive calibration or physically exact joint |
| Step 4 baseline/expected score/uncertainty | Expected innings 277.75 and 5-over 29.5 conditional estimates; league-only baselines missing; team wickets and all-match joint not modelled |
| Step 5 candidates/top-2/dependence | Four ranked directions; only 2 primary; complements checked; Fréchet joint interval only |
| Step 6 ODI phase, toss, weather, DLS rules | ODI vs T20 distinguished; limited DLS/operator detail; first innings confirmed via secondary toss source |
| Step 7 retain original, no retrospective/import | Proposed local draft only; event result excluded; no settlement, no canonical P-ID, no Github/Drive writes |
| Historical pregame performance eligibility | **FAIL**: issue completed after scheduled 19:00 AEDT; do not count prospective pre-start predictions |
| C21 probabilities | APPROXIMATE, UNCALIBRATED; primary analyst assumptions explicit; five-over parameter provenance weak |
| C16/C22 complete actual active-mini update | **BLOCKED**: real active original and writer lease not established. Companion cumulative DRAFT copy may include unchanged previous draft; no assertion of issued official mini |
| Overall | `RESEARCH_RETAINED_AS_DRAFT` / `INFORMATION_INCOMPLETE` / `POST_START_ISSUE` / `DRAFT_NOT_APPLIED` |

**SPORTS_ONLY_MARKET_BLIND: PASS** — user lines are thresholds, not odds. **OUTCOME_EXPOSURE:** match live/result intentionally not consulted; source publication-known-at may remain uncertain. **SETTLEMENT/RETROSPECTIVE: NOT_PERFORMED.** **CANONICAL_IMPORT: NOT_PERFORMED.** **ML/RL: NOT_RUN (per current methodology).**
<!-- END CANONICAL RESEARCH P-613 -->
