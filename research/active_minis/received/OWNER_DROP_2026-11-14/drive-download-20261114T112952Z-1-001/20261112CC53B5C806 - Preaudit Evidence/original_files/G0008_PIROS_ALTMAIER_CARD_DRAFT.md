<!-- BEGIN CARD LOCAL-20261112CC53B5C806-G0008 -->
## Card · LOCAL-20261112CC53B5C806-G0008 · Tennis / Orléans Challenger 125 · Zsombor Piros vs Daniel Altmaier · 2026-11-13 CET

- **Local event key:** `LOCAL-20261112CC53B5C806-G0008` — `LOCAL_UNIMPORTED_EVENT`; canonical ID `NOT_ASSIGNED / PROMPT_4_IMPORT`.
- **Competition / format:** 2026 ATP Challenger Orléans (Co'met Orléans Open), men's singles quarterfinal; indoor hard court, best-of-three, ordinary 6–6 tiebreak assumed; final-set tiebreak detail not independently reverified.
- **Identity:** [7] Zsombor Piros (HUN) versus [2] Daniel Altmaier (GER), no verified historical H2H. Tournament official timetable confirms quarterfinals Friday 13 Nov; Tennis-France and contemporaneous order-of-play reporting list 13:00 CET; other providers list conflicting 10:00/11:00 UTC provisional times.
- **Scheduled time:** owner estimate `2026-11-13T23:00:00+11:00` = 2026-11-13 13:00 CET = 12:00 UTC, corroborated by published Court 1 order-of-play reporting; actual first service `NOT_VERIFIED`.
- **Research completion / record capture:** `2026-11-13T22:58:23+11:00` AEDT; time and phase are independent of actual first serve; do not certify prospective issue without a verified pre-start cutoff and immutable published freeze. The prior official listed time is the relevant cutoff; known-at of dynamic stats is partly unverified.
- **Authority:** GitHub `danisgreat/Sports-Research`, read-only pinned `008cedc4ff469e7a808292aa3667a7bffe22e273`; MDS/P v24.16 / CR-2026.11.11-R4 and 2026-11-12 records R1 / prompt P-2026.11.11-v24.14 / SCV-v13 / SEL-v4; user overrides publication in favor of chat-local drafts.
- **Research / primary status:** `INFORMATION_INCOMPLETE / UNCALIBRATED_QUALITATIVE / PRIMARY_P_NOT_ESTIMATED / READ_ONLY_DRAFT / NOT_REPOSITORY_ISSUED`.
- **Independent diagnostic:** exact completed-match scoring-tree enumeration, **not** Monte Carlo, with scenario source script `tennis_shadow_piros_altmaier_20261113.py` and JSON `TENNIS_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0008.json`; all displayed numbers are **shadow-only** and not framework p_card, official published odds or certification.
- **End points / action:** completed best-of-three total games and net games margin including tiebreak sets as 7–6; Piros +2.5 wins if Piros games minus Altmaier games ≥−2; Altmaier −2.5 wins if margin ≤−3; Over 22.5 wins when total ≥23, Under wins when ≤22. No push for half-lines if completed; withdrawal/retirement/void handling unknown without operator terms.
- **Learning:** `LEARN_RECORD_INCOMPLETE`; five dated recent matches for each player verified to descriptive level, but full L15/L20 match-score archive, publication timestamps, and point-level source-event provenance not independently reconstructed. `PENDING_SETTLEMENT`; no league learning write.
- **Lineup and health:** Individual tennis starters are the participants if play begins; both named participants confirmed in tournament draw; no confirmed fitness clearance, medical reports, or retirement status. Prior reported MTOs found in nonofficial preview, NOT independently admitted as a health fact.
- **Sources, known-at:** see A3/A8. Retrieval during current chat before/scheduled near start, original publication timestamps missing for some dynamic pages; do not designate CLEAN_PRE_START_INPUTS for an unverifiable original availability claim.
- **Model availability:** `ML_NOT_RUN` for repository formal reference, kit, card lint, freeze and learning log; chat-local exact-scoring diagnostic `EXECUTED_NOT_PRIMARY`; not a trained or calibrated Challenger model.

### Decision block

**Qualitative leading direction: Over 22.5 games (LOW confidence).** It survives all four exploratory score-strength scenarios, unlike either games-handicap side. A close straight-set match or dominant Altmaier service game is the principal failure mechanism. No safe/high-confidence certified selection.

| Rank | Role | Tag | Contract key and exact proposition | p_card | p_base | BASELINE_P | Line distance | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|---|---|
| 1 | QUALITATIVE_LEAN | SUPPLIED | T-OVER22.5: completed match total ≥23 | NOT_ESTIMATED | NOT_ESTIMATED | BASELINE_UNAVAILABLE: Challenger peer cohort not frozen | Not estimated for primary | QUALITATIVE; separate exact-chain shadow below | Quick two-set match without enough tiebreaks |
| 2 | SECONDARY_QUALITATIVE | SUPPLIED | P-PLUS2.5: Piros games margin ≥−2 | NOT_ESTIMATED | NOT_ESTIMATED | BASELINE_UNAVAILABLE | Not estimated for primary | QUALITATIVE; high opponent-sensitivity in shadow | Altmaier serves at current two-match rate and dominates breaks |

**All supplied propositions, independent exact-chain sensitivity (NOT p_card):**

| Contract | All-surface 52wk | Indoor shrink-20 match | Indoor 52wk alone | Two-match high-variance stress | Direction / action |
|---|---:|---:|---:|---:|---|
| **Piros +2.5 games** | 72.574% | 71.777% | 67.005% | 35.368% | Not stable across all samples; no certified p |
| **Altmaier −2.5 games** | 27.426% | 28.223% | 32.995% | 64.632% | Opposite to Piros +2.5; not independent evidence |
| **Over 22.5 games** | 59.644% | 61.151% | 64.288% | 52.886% | First qualitative direction; low confidence |
| **Under 22.5 games** | 40.356% | 38.849% | 35.712% | 47.114% | Complement of Over; quick straight-set win route |

**Baseline coverage:** 0 numeric primary rows; no trustworthy Challenger league-only comparator. **Rank-1 gate:** NOT_ASSESSABLE, no calibrated p_card or precision test. **Rank-2 floor:** NOT_ASSESSABLE. **Winner:** official winner probability NOT_ESTIMATED; shadow Piros matchwin 58.1% indoor-shrunk, across tested sources 21.8%–59.7%; not decision-ready. **Joint failure:** within indoor-shrink scenario, P(Piros +2.5 loses AND Over 22.5 loses) = 0.1480, computed as P(Under 22.5) − P(Piros +2.5 AND Under 22.5) = 0.3885 − 0.2405; this is not independent-leg probability. **No push** for completed half-lines; void terms unresolved. **Abstain** is reasonable, since no primary numeric contract meets qualification.

### Appendix

#### A1. Identity, scheduling, state

Exact participants/round/venue: [7] Piros vs [2] Altmaier; Orleans France, indoor hard, Challenger 125 quarterfinal, best of three. Tournament organizer programme lists QF Friday 13-Nov; independent scheduling lists 13:00 Paris and user estimates 23:00 Melbourne. Other schedule vendors conflict at UTC 10:00 or 11:00; do not silently discard conflicts. Original start/progression/withdrawal not verified at issue. No other mini key or prior card for this target. `TIMING_UNVERIFIED` until exact first ball; prior score/result not viewed and no outcome exposure claimed.

#### A2. Frozen supplied contracts and full universe

Only four user-supplied full-match propositions ranked qualitatively; no derived lines/market prices considered:
- `Piros handicap +2.5`: unconditional full completed match W if Piros net games margin ≥−2, L otherwise; P=0, V only if retirement/WO under missing operator contract.
- `Altmaier handicap −2.5`: W if Altmaier net games margin ≥3, L otherwise; complementary to first on fully completed matches.
- `Total Over 22.5`: W if ≥23 games played in completed match; L if ≤22; half-line, no push.
- `Total Under 22.5`: W if ≤22; L if ≥23, complementary to Over.
- Matchwinner for both sides is informational only, not an owner's additional line and has no primary p.

#### A3. Evidence, recent history and roster/medical

Sources with precise URLs and retrieved or examined in current chat around `2026-11-13T22:58:23+11:00` AEDT:
1. Tournament fixture and schedule: `https://opendorleans.com/programmation/` (organizer tournament stage, no exact match clock); `https://www.tennis-france.com/tournois/orleans-2026` (13:00 Paris); `https://tennistonic.com/tennis-news/1081224/prediction-preview-h2h-altmaier-piros-martinez-portero-and-basavareddy-to-play-on-court-1-on-friday-orleans-challenger/` (scheduling and factual match scores only, **none of its odds or predictions used**); `https://www.sofascore.com/tennis/match/zsombor-piros-daniel-altmaier/iUabsVpHb` (conflicting 10:00 UTC provisional schedule). Date of page publication often unknown; field-level original known-at remains unverified.
2. Tournament draw: `https://en.sportsand.me/tennis/challenger-orleans?tab=draw` (result dates, draw; page also contains odds, intentionally not used); `https://en.sportsand.me/tennis/team/zsombor-piros?tab=calendar` (Piros dated results).
3. Historical and opponent service facts: `https://www.tennisexplorer.com/match-detail/?id=3377369` (2026 indoors Piros 13–3, Altmaier 6–4, overall season scope Piros 55–25 and Altmaier 27–34, rank around 99/73); `https://www.stevegtennis.com/head-to-head/men/Daniel_Altmaier/Zsombor_Piros/` (two-round score and service game numerators); 52-week serve/return statistics table at `https://pythiatennis.com/daniel-altmaier-vs-zsombor-piros-prediction-and-stats/?d=2026-11-13` (**raw historical stat columns only; no output or market/pricing used**). These are not federation-certified underlying row snapshots; named profile definitions differ.
4. Head-to-head: first recorded tour meeting (`0–0`); no previous verified match record. Height/handedness from TennisExplorer; not entered as a numeric effect.

**Five most recent played matches (the overlapping L5 form window):**

| Player | Date | Event | Opponent | Match outcome, sets | Pre-cutoff evidence and caveat |
|---|---|---|---|---|---|
| Piros | 2026-11-11 | Orléans CH R16 | Clément Tabur | W 2–6, 7–6(6), 6–3 | Draw and matches; qualifying service stats not full raw point feed |
| Piros | 2026-11-10 | Orléans CH R32 | Luca Nardi | W 7–6(2), 1–6, 6–4 | Draw and matches |
| Piros | 2026-11-06 | Bratislava 2 CH QF | Dalibor Svrčina | L 6–4, 0–6, 4–6 | Piros scores from opponent-side display |
| Piros | 2026-11-04 | Bratislava 2 CH R16 | Sascha Gueymard Wayenburg | W 6–3, 6–7, 6–3 | Tiebreak points unavailable in one feed |
| Piros | 2026-11-02 | Bratislava 2 CH R32 | Matthew William Donald | W 6–3, 6–3 | No retirement reported, not proof of medical fitness |
| Altmaier | 2026-11-11 | Orléans CH R16 | Buvaysar Gadamauri | W 3–6, 7–5, 6–1 | Match results from draw; opponent qualified |
| Altmaier | 2026-11-10 | Orléans CH R32 | Adrien Gobat | W 6–2, 3–6, 6–3 | Qualifying opponent; two-set service split in stat provider |
| Altmaier | 2026-10-31 | Paris Masters qualifying | Alex Molčan | L 4–6, 6–7 | Official match date/time provider comparison needed |
| Altmaier | 2026-10-29 | Basel ATP R16 | Jiří Lehečka | L 5–7, 4–6 | ATP vs Challenger competition-level difference |
| Altmaier | 2026-10-26 | Basel ATP R32 | Juan Manuel Cerúndolo | W 6–7, 7–6, 6–4 | Tiebreak details in secondary provider |

**L5:** Piros 4–1, Altmaier 3–2. **L10:** Piros 7–3, Altmaier 6–4 based on secondary statistical digest, not independently reconstructable complete dated game rows here. **L15/L20:** `NOT_VERIFIED`, cannot print true n and opponent-adjusted rate. **2026 indoor:** Piros 13–3, Altmaier 6–4 in TennisExplorer view; other publishers show Piros 14–3/Altmaier 6–5 because of source scope/timing; do not merge as independent facts. **2026 season:** sources vary e.g. Piros 51–23 vs 55–25 and Altmaier 27–34, depending event/retirement/snapshot inclusion. `SEASON_SCOPE_CONFLICT` flagged rather than fabricated resolution. Specific level-adjusted opponent strength unavailable.

**Exact-match two-round serving evidence** (unfitted and very small): Altmaier 27 aces, 24/27 service games held (89%) and 109/155 service points (70.3%); Piros 15 aces, 23/30 holds (77%) and 135/224 service points (60.3%); their return-points-won ratio 38.2% vs 35.7%, respectively. Source SteveG, two matches. First opponent-quality problem: both Altmaier opponents were qualifiers; stronger numbers may not translate unchanged against Piros's return. Piros faced stronger prior opponents in mixed indoor Challenger fields. These last-two matches already sit inside 52-week indoor samples, no double-counted adjustment.

**Health/participants:** both listed in quarterfinal draw. No independently confirmed new injury, MTO, withdrawal, limited serving, medication, physiotherapy or coaching change; `INJURY_STATUS_UNVERIFIED`, not healthy confirmed. Bench/replacements `N/A` for individual tennis singles; travel is back-to-back European indoor weeks for Piros, Altmaier Paris/Basel to Orleans, but workload and recovery remain conditional.

#### A4. Distribution and sensitivity, arithmetic

**Model shadow (not primary):** exact recursion over point service probability → service hold → alternating server game states → 6–6 tiebreak → best-of-three set states and completed match total/margin. Each scenario sums all terminal match-score state masses to 1. P(game hold) = p⁴(1+4q+10q²) + 20p³q³ × p²/(p²+q²), q=1−p. Initial server 50:50. Tie-break server order is 1–2–2–2. No point-by-point actual model was run on the official repository. Shadow code under `/mnt/data/tennis_shadow_piros_altmaier_20261113.py` and JSON separately retained.

52-week sourced point win rates: Piros SPW 62.3% all / 63.7% indoor, RPW 39.0% all / 37.0% indoor, 72 all / 16 indoor matches; Altmaier SPW 62.9% all / 69.1% indoor, RPW 34.5% all / 31.1% indoor, 60 all / 10 indoor. Opponent match-up approximation **Piros serve p=½[Piros SPW+(1−Altmaier RPW)]**, vice versa for Altmaier; indoor shrink setting n₀=20 equivalent matches, explicitly *unfitted sensitivity* rather than optimized/validated coefficient.

| Scenario | Piros matchup SPW | Altmaier matchup SPW | Expected games | P(deciding set), shadow | Piros matchwinner, shadow |
|---|---:|---:|---:|---:|---:|
| All surface | 0.639 | 0.619 | 25.32 | 49.2% | 59.7% |
| Indoor shrink20 | 0.650 | 0.633 | 25.62 | 49.4% | 58.1% |
| Indoor only | 0.663 | 0.660 | 26.21 | 50.0% | 51.2% |
| Two-round stress | 0.611 | 0.673 | 24.50 | 42.1% | 21.8% |

All scenario numbers are **uncalibrated conditional forecasts, not confidence intervals**, likely overstate precision and do not have an independent skill certificate. Point-service independence, unweighted opponents, score-state/pressure, return/serve covariance, retirement terms and break-point volatility all cause error. The most adverse recent-two stress has a much larger Altmaier serving advantage; long-run indoor-only outcomes favor Piros's return enough to preserve the cushion. Because that short-run scenario already overlaps the long-run 52-week sample, it is a **stress test, not a fourth independent piece of evidence or mixture weight**. Formal reference stage, frozen baseline/adjustments, simulation release and ledger verification were not run; shadow does not fill them.

**Expected score:** formal primary NOT_COMPUTED. Indoor-shrink shadow only: approximate expected total and Piros minus Altmaier total-games margin in table above; shadow approximate player games (T+M)/2 and (T−M)/2. These are means across different set counts, not an achievable match score or prediction of a particular final. A 7–6, 6–4 straight-set match totals 23 and meets the Over; 6–4, 6–4 totals 20 and stays Under. Three full sets generally cross 22.5, but early retirement/short decider conventions differ and must be verified.

**League-only baseline:** `NOT_RUN / BASELINE_UNAVAILABLE`, no time-stamped Challenger cohort over identical best-of-three indoor 22.5 and handicap 2.5 was accessed. No retrospective 0.5 substitution. **Adjusted reference:** `NONE`, no official released model or coherent frozen input verified; independent shadow is not a replacement for the formal stage. **Sensitivity:** numeric four-case table above. **Calibration:** no validated scope, NO_DEMONSTRATED_SKILL by tennis rule. **Primary confidence:** low.

#### A5. All propositions and W/P/L/V

Propositions are complements within each line family, but not between families. All completed games half-lines have W+L=1, P=0, V=0 under assumptions. The uncalibrated shadow gives p(W) by scenario as in Decision table; p(L)=1−p(W). For unknown retirement and operator void, unconditioned V cannot be estimated. Cross-family joint at indoor-shrink: Piros cushion AND Under is printed in Decision block; P(Over AND Piros cushion) can be derived from shared match score object, never multiplication of marginals. No modeled edge over a user-supplied price, as none was used.

#### A6. Adjustments and playing context

| Mechanism | Factual basis | Numerical adjustment? | Uncertainty / direction |
|---|---|---|---|
| Indoor surface and form | Piros 13–3 2026 indoor; Altmaier 6–4, shorter Altmaier schedule | No primary; indoor vs all-surface scenarios only | Piros return can shorten Alt holds; indoor speed increases tiebreak frequency |
| Current serve | Altmaier 24/27 holds in first two vs Piros 23/30 | No primary; recent-two stress only | Can reverse handicap, while total retains modest Over in model |
| Return and opponent level | Piros returns a higher share of points all-surface; Altmaier faced two qualifiers | No scalar | Overweighting one-week service runs is a known failure route |
| Workload/rest | Both last played 11 November, two three-set Orléans wins each | Scenario width only | Fatigue may widen break-rate tails both directions |
| Venue/conditions | Indoor hard court, both right-handed; ball speed not verified | No scalar | No outdoor weather effect; court speed unquantified |
| Medical | No current injury clearance or MTO cross-verified | No scalar | Late withdrawal could void, constrain or shift service |

#### A7. Family, branch and coherence checks

- Both players can win 2–0 or 2–1; every terminal match state is derived from same joint score grid. Piros +2.5 and Altmaier −2.5 sum to 1 for fully completed event, as do Over/Under 22.5. No push. Winner and games handicap are **not** constrained to move together in tennis (a deciding-set loser may win more games overall), unlike standard points sports.
- Piros recent three-set matches support long-match branches, but Altmaier two matches also three-set; these are overlapping endpoint observations rather than independent model certifiers. The three-set branch in indoor shrink is roughly half of completed matches, unfitted and perhaps too high.
- `RANK1_UNSTABLE` numerically not assessable: no formal p_card/ε/league comparator; shadow direction for Over stable across scenario set but fails high-confidence qualification.
- No scenario demonstrated prospectively calibrated advantage over league reference; avoid assertions of a safe or near-certain bet.

#### A8. Source register, failures, timing and capture plan

| Source / URL | Decisive fields checked | Status / gaps |
|---|---|---|
| Tournament organizer https://opendorleans.com/programmation/ | Competition quarterfinal date, stage, publishing process | Organizer page may have old cached editions; Friday stage reverified by contemporaneous draw |
| Tennis-France https://www.tennis-france.com/tournois/orleans-2026 | Court 13:00 CET listing | Independent schedule, actual match start not confirmed |
| Tennis Tonic https://tennistonic.com/tennis-news/1081224/prediction-preview-h2h-altmaier-piros-martinez-portero-and-basavareddy-to-play-on-court-1-on-friday-orleans-challenger/ | First 2 results and Court 1 time; no odds or predictions admitted | Publication 13-Nov; timestamp to minute missing |
| TennisExplorer https://www.tennisexplorer.com/match-detail/?id=3377369 | Ranking, indoor records, player dimensions | Dynamic stats cache conflicts in exact season match n |
| SportsAnd https://en.sportsand.me/tennis/challenger-orleans?tab=draw | Progression and score lines | Betting content intentionally ignored; no official point-level match feeds |
| SteveGTennis https://www.stevegtennis.com/head-to-head/men/Daniel_Altmaier/Zsombor_Piros/ | Set/serve/return numerators at event | Two-match sample; competition/opponent confounding |
| PythiaTennis https://pythiatennis.com/daniel-altmaier-vs-zsombor-piros-prediction-and-stats/?d=2026-11-13 | Raw 52wk SPW/RPW counts only | Fitted predictions, odds, rankings, returns **NOT used**; underlying original match-level feed not audited |
| Sofascore https://www.sofascore.com/tennis/match/zsombor-piros-daniel-altmaier/iUabsVpHb | Competing 10:00 UTC schedule | Conflicts with 13:00 CET / 12:00 UTC order-of-play, source likely stale |

**Next evidence requirements:** verify first-serve and full official match result from ATP Challenger score centre; find original 13-Nov organizer order-of-play PDF and exact source release time; confirm official player fitness, any MTO/withdrawal, match rule (retirement treatment per operator) and full dated surface L15/L20 stats; only then consider a new dated source refresh. All due dates are triage targets, no automation scheduled, no future result-check promise. Avoid original outcome exposure in a pregame card.

#### A9. Completion and readback audit

| Procedure | Actual work / result | Remaining gap | State |
|---|---|---|---|
| Authority, native identity, duplicate | Read pinned GitHub rule-set and existing G0001–G0007, exact participants/draw | No repository lease or working tree issue | CHAT_LOCAL_ONLY |
| Event start/venue/state | Orléans QF, indoor; 13:00 CET order of play cross-checked | Actual first ball and competing provisional provider times | DONE_WITH_GAPS |
| Players, roster, injury and availability | Names/draw verified, no substitutes in singles | New injury clearance / medical release not found | INCOMPLETE_EVIDENCE |
| Online historical form and sources | Dated 5 matches each; 2026 indoor records and conflicting season totals | Complete sourced L15/L20 and per-point opponent-adjusted source archive | INCOMPLETE_EVIDENCE |
| Sport mechanisms | Serve/return, tiebreaks, best of three, rest, opponent level, retirement | Quantified court speed/fitness and tiebreak game rule confirmation | DONE_WITH_GAPS |
| Reference, model execution, calibration | Exact scoring diagnostic script executed; output file with scenarios | Formal primary reference/baseline, ledger, kit, model freeze not executed | SHADOW_ONLY |
| Contract and sensitivity | Four owner lines including W/P/L/V, four scenario comparisons | Operator retirement terms; no calibrated p_card | DONE_QUALITATIVE |
| Expected score/dependence | Shadow total/game margin, common-state probability, scenario ranges | No primary expected score or exact baseline | SHADOW_ONLY |
| A1–A9, mini append, custody | Whole card, prior-block identity check, intake/footer/queue update, SHA-256 receipt | No repository commit, pregame freeze or GitHub published issue | CHAT_LOCAL_DRAFT |

**Overall information status:** `INFORMATION_INCOMPLETE`; **forecast status:** `UNCALIBRATED_QUALITATIVE / PRIMARY_P_NOT_ESTIMATED / EXPLORATORY_EXACT_ENUMERATION_SHADOW`; **issue status:** `TIMING_UNVERIFIED / CHAT_LOCAL_NOT_ISSUED_IN_REPOSITORY`; **settlement:** NOT_PERFORMED; **canonical import:** NOT_PERFORMED. Any numeric scenario results are **not** validated primary probabilities.

**SPORTS_ONLY_MARKET_BLIND:** YES (no source odds/picks used) · **OUTCOME_EXPOSURE:** NO_MATCH_RESULT_USED · **GITHUB_WRITE:** NO
<!-- END CARD LOCAL-20261112CC53B5C806-G0008 -->
