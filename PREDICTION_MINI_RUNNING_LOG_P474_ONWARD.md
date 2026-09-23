# Prediction Mini Running Log — P-474 Onward

Created: Sep 20, 2026
Last full settlement / retrospective / audit pass: **Sep 21, 2026 (Australia/Melbourne)**
Location/time basis: Australia/Melbourne
Governing method: MDS-2026.09.19-v4.3 / CR-2026.09.19-4
Control hashes recorded at issue: METHOD `da544d4c47efdf33bdbcc130a5ef0adc23055f77f80fd25284c1dc55f3d1b1b6`; RULES_BASEBALL `1e0b5a0e9636469f7b75fcc21d19f9fe3c557c691724e67bba821b145889a411`; RULES_BASKETBALL `f5ad8787a08fe6b1533c0f273058f26ab3ff3f731bc5307ebe40423993c14421`
Operating mode: SPORTS_ONLY / MARKET_BLIND
Performance status: **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**
Next intended ID after this card: P-482, subject to fresh reconciliation against `PREDICTION_LOG_COMBINED_4.md`.
Retrospective policy: settle completed events only after the CR-4 three-source terminal-state gate passes; live/unresolved events remain pending.

### What the 2026-09-21 pass did

Every one of P-474 through P-481 was already marked settled on 2026-09-20. This pass did **not** take that on trust. Each event's terminal state was re-verified against at least one source lineage that the original settlement did not use, and every pre-game claim that could be checked against a post-game record — confirmed lineups, benches, substitutions, participation, phase fields, corner fields — was checked.

Outcome of the re-audit:

- **All eight finals confirmed.** No settled row changed. No win became a loss or vice versa.
- **Three material new findings** that the 2026-09-20 pass did not record: the P-480 Anyembe availability error, the P-478 lineup-projection result (22 of 22 exact), and the P-478 corner-evidence downgrade (betting-branded pages used where a registered structured source publishes the field).
- **Two settlement-evidence upgrades:** P-478/P-480/P-481 corner fields now rest on the ESPN soccer `wonCorners` structured route, and P-479's phase field now rests on the ESPNcricinfo scorecard match note rather than a source that has since gone behind a bot wall.
- **One resolved pre-game uncertainty:** Natasha Cloud (P-475) is confirmed DNP.
- **A structural measurement correction:** the supplied-slate "record" across this mini log is almost entirely mechanical, because 28 of its 32 rows are strict complementary pairs. This is set out in §4.
- Document structure was rebuilt to the required order, and the mandatory validation questions are now answered explicitly and individually for every event.

Verification sources used in this pass are listed inside each event's `2026-09-21 independent re-audit` block.

## 1. Incomplete / Unsettled Logs

**None.** All eight events (P-474 through P-481) are completed, settled and retrospectively reviewed. Each passes the CR-4 three-source terminal-state gate, and after this pass each rests on at least four distinct lineages.

No event in this mini log is Upcoming, Live, Delayed, Suspended, Postponed, Abandoned or Cancelled.

| ID | Event | Event status | Settlement status |
|---|---|---|---|
| P-474 | Athletics @ Cleveland Guardians (MLB) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |
| P-475 | Chicago Sky @ Atlanta Dream (WNBA) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |
| P-476 | Minnesota Twins @ Los Angeles Angels (MLB) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |
| P-477 | Sydney Kings vs Cairns Taipans (NBL) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |
| P-478 | Djurgårdens IF vs IF Elfsborg (Allsvenskan) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |
| P-479 | Edinburgh Castle Rockers vs Belfast Wolves (ETPL Final) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |
| P-480 | Viborg FF vs FC Nordsjælland (Superligaen) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |
| P-481 | Villarreal vs Levante (La Liga) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |

## 2. Temporary-ID / Canonical-ID Conflict Logs

**No conflict, and no temporary ID is required for any entry in this mini log.**

Reconciliation performed on 2026-09-21:

- `PREDICTION_MINI_RUNNING_LOG_P452_ONWARD.md` covers **P-452 through P-473** and states next ID **P-474**. All 22 of its entries are settled with retrospectives complete and none awaiting settlement.
- This mini log covers **P-474 through P-481**, contiguous with the above, with no overlap and no reuse.
- `GAME_LOG_STATUS_CURRENT.md` enumerates canonical records through **P-451**.
- `PREDICTION_LOG_COMBINED_4.md` is the single active canonical log and remains the queue/next-ID authority.

**Outstanding integrity observations (not conflicts, but they should be cleared before the next issue).**

1. **The canonical register has not yet absorbed P-452 through P-481.** `GAME_LOG_STATUS_CURRENT.md` still ends at P-451, and one paragraph inside it still says "next ID `P-438`" alongside a later correction saying P-452. Thirty mini-log entries (P-452–P-481) exist only in the two mini logs. `METHOD.md` §3 step 7 requires an external log to be reconciled into the canonical log within 24 hours of availability, and states that an overdue unregistered log blocks the next forecast. **On a strict reading of that rule, P-482 is blocked until P-452–P-481 are imported into `PREDICTION_LOG_COMBINED_4.md` and the status register is extended.** That is a documentation-integrity matter, not a settlement defect — every entry is settled and evidenced.
2. **Temporary handles held elsewhere remain open and are unaffected by this pass.** 23 primary handles plus documentary/period audits sit in Parts 2–4. They are listed in §4.9 below with the 2026-09-21 re-probe result. None belongs to this mini log and none blocks it.

## 3. Fully Settled Logs


### P-474 — MLB — Athletics @ Cleveland Guardians

- Canonical / staging ID: P-474

- Venue: Progressive Field, Cleveland, Ohio, United States

- Venue timezone: America/New_York

- Official venue-local start: Sep 19, 2026 at 6:10 PM EDT

- Australia/Melbourne conversion: Sep 20, 2026 at 8:10 AM AEST; calendar-date rollover = YES

- Research cutoff / distribution freeze: Sep 20, 2026 at approximately 8:14 AM AEST

- Issuance state: START_CROSSED_UNVERIFIED. The official scheduled start had passed before delivery. Per the user's explicit instruction, research continued, but no live score, pitches, baserunners, or other in-game observations were admitted into the predictive model.

- Normal pregame preflight: FAIL with exactly one blocking finding, PF-EVENT-STATE. Source-count, lineage, field-owner, timezone, line-quarantine and freeze-order checks passed. This is therefore a late-issued research forecast, not a normal pregame PASS.

#### Identity / contracts

Supplied contracts were quarantined until after the sporting distribution was frozen:

- Cleveland Guardians moneyline

- Athletics +1.5 runs

- Full-game Over 7.5 runs

- Full-game Under 7.5 runs

Research endpoint treats a completed MLB regular-season game as including extra innings. Exact sportsbook suspension/action rules were not supplied, so operator action is not asserted.

#### Starters / lineups / availability

Official probable-starter handshake:

- Athletics: Jacob Lopez, LHP — 6-4, 5.02 ERA, 107 K in 114.2 IP.

- Guardians: Tanner Bibee, RHP — 6-15, 4.16 ERA, 140 K in 177.1 IP.

Latest pregame lineup cross-check recovered from CBS/STATS-Field Level and an MLB-derived automated game feed:

- Athletics: Henry Bolte CF; Jeff McNeil 1B; Shea Langeliers DH; Lawrence Butler RF; Zack Gelof 3B; Donovan Walton 2B; Carlos Cortes LF; Brian Serven C; Alika Williams SS.

- Guardians: Steven Kwan CF; José Ramírez 3B; Chase DeLauter DH; Jo Adell RF; Angel Martínez LF; David Fry 1B; Travis Bazzana 2B; Austin Hedges C; Brayan Rocchio SS.

Lineup integrity note: the MLB starting-lineups index retrieved during the research window still rendered the matchup as TBD, so a field-owner posted-order capture was not recovered to gate standard. The secondary lineup cross-check is used with an evidence cap; no player prop is ranked.

Major Athletics absences materially reduce their offensive depth: Brent Rooker, Nick Kurtz and Jacob Wilson are on the 60-day IL with 2027 expected returns; Tyler Soderstrom underwent season-ending hip surgery. Shea Langeliers is available and is a key surviving power bat.

Guardians availability: Rhys Hoskins remains out; Colin Holderman's wrist rehab suffered a setback; Shawn Armstrong was still on rehab progression. Chase DeLauter and Angel Martínez had recent day-to-day issues but were listed in the latest pregame lineup cross-check, so they are treated as available with residual uncertainty.

#### Pitching / team process evidence

Tanner Bibee:

- Latest completed start: 6 2/3 IP, 2 ER, 7 K.

- Baseball Savant 2026 line: 28 HR allowed, .307 wOBA, .318 xwOBA, 39.2% hard-hit and 8.3% barrel rate. This supports a credible Athletics home-run/cluster tail even though Cleveland is preferred overall.

Jacob Lopez:

- Season line remains volatile at 5.02 ERA / 1.48 WHIP.

- One recent quality-start branch is real: 6 IP, 2 ER, 7 K in the official MLB record against Texas.

- But the immediate recent window also contains material contact/home-run damage; CBS/Field Level reported nine runs on 13 hits in 9 2/3 innings over his prior two starts and five homers allowed across his prior three outings.

Current-regime team context since early August, used descriptively rather than as a fitted coefficient:

- Athletics: 91 wRC+, -15 defensive runs in the cited metric, 6.17 starter ERA, 4.53 bullpen ERA.

- Guardians: 101 wRC+, approximately neutral/positive defense, 3.11 bullpen ERA.

Bullpen workload note: Cleveland used Joey Cantillo for six relief innings in the preceding game; Hunter Gaddis and Cade Smith each handled late innings. Cantillo's immediate availability is therefore reduced, while the strongest one-inning leverage arms were used but not multi-inning exhausted. Workload informs availability only, not quality.

#### Weather / park

National Weather Service Cleveland forecast around the game window was roughly low-70s °F, mostly cloudy with a chance of showers and modest winds. No reliable park-orientation transformation justified a signed wind adjustment, so weather widens interruption/environment uncertainty but does not force an Over or Under direction.

#### Frozen independent joint run distribution

Model: explicit UNVALIDATED_SUBJECTIVE scenario mixture; independent Poisson team-run kernels within each scenario, then a separate MLB extra-inning branch. This is not a fitted, calibrated or prospectively validated model.

Scenario 1 — Cleveland control: weight 0.33; CLE 5.0, ATH 2.7.

Scenario 2 — competitive central: weight 0.34; CLE 4.2, ATH 3.4.

Scenario 3 — Athletics power / Bibee HR tail: weight 0.15; CLE 3.8, ATH 5.0.

Scenario 4 — high-run starter-to-bullpen cluster: weight 0.18; CLE 6.2, ATH 4.3.

Frozen centre:

- Cleveland runs: 4.76

- Athletics runs: 3.57

- PROJECTED TOTAL: 8.34 runs

- Projected Cleveland margin: +1.19 runs

- Regulation total SD: approximately 3.09 runs

- Regulation margin SD: approximately 3.12 runs

- Representative score family: Cleveland 5-3 Athletics

- Distribution ID: P-474-dist-v1

- Distribution SHA-256: 80ed1ee27b0e8c1958bbe2ce07fbca5d9ce2a8ffb06c4dd974e4eb9f2ca6467d

##### Mandatory total projection / ceiling audit

PROJECTED TOTAL: 8.34

SUPPLIED TOTAL: 7.5

RAW GAP: +0.84 runs

DISTRIBUTION WIDTH: \~3.09 runs SD

NORMALIZED GAP: \~+0.27 SD

ASSESSMENT: MODEST SEPARATION, not a strong total edge.

PREFERRED SUPPLIED SIDE: Over 7.5.

MODEL ALTERNATE TARGET: Over 6.5, roughly 71-72% from the same frozen distribution before minor extras uplift. Operator availability is not asserted.

Component / failure-state budget:

- Cleveland centre 4.8 + Athletics centre 3.6 = about 8.4 -\> Over.

- Cleveland ordinary high 6 + Athletics centre 3-4 -\> 9-10 -\> Over.

- Cleveland centre 4-5 + Athletics ordinary high 5 -\> 9-10 -\> Over.

- Bibee-control + depleted Oakland branch can still produce 4-2 / 5-2 -\> Under 7.5.

- A strong Lopez outing plus Cleveland home-last-bat suppression can produce 3-2 / 4-2 -\> Under.

- A tie after nine activates MLB's automatic runner at second, increasing the scoring rate of the extra-inning branch and modestly helping the Over relative to a regulation-only calculation.

#### Ranked supplied contracts

1\. GUARDIANS ML — \~65.5% UNVALIDATED_SUBJECTIVE — Rank #1.

   Why: Cleveland owns the stronger current bullpen/process profile; Oakland's lineup is missing several of its highest-impact bats; Bibee's central branch is more stable than Lopez's; Cleveland also has home-last-bat and extra-inning home advantage.

   Main failure: Bibee's 28-HR season tail is hit by Langeliers/Butler/Gelof, while Lopez reaches his quality-start branch and Cleveland's depleted relief depth is exposed.

2\. OVER 7.5 RUNS — \~60.6% — Rank #2.

   Why: independent centre is 8.34; Lopez's contact/HR volatility plus Bibee's own HR tail produces several ordinary 5-3, 5-4 and 6-3 states; MLB extras add upper-tail scoring when regulation ends tied.

   Main failure: Bibee suppresses the depleted Oakland lineup and Lopez lands his good-start branch, producing a 4-2 / 5-2 or lower state; a Cleveland lead can also remove the bottom of the ninth.

3\. ATHLETICS +1.5 — \~52.8% — Rank #3.

   Why: the +1.5 wins in every Athletics victory and every Cleveland one-run win. The regulation model puts about 13.1% mass specifically on a Cleveland one-run win, which creates meaningful overlap with Guardians ML.

   Main failure: Cleveland separates by 2+ through the Lopez-to-middle-relief transition, a multi-run homer/sequence cluster, or late bullpen separation.

4\. UNDER 7.5 RUNS — \~39.4% — Rank #4.

   Why it remains live: Cleveland has a legitimate run-prevention path against a heavily depleted Athletics lineup, and Bibee just delivered a strong start.

   Why it ranks last: 7.5 is below the 8.34 centre, both starters retain home-run/contact tails, and several ordinary rather than extreme score combinations clear eight runs.

Forced-pair integrity: Over 7.5 + Under 7.5 = 100% conditional on action; there is no push at a half-run line. Guardians ML and Athletics +1.5 are not complements because both win when Cleveland wins by exactly one run.

#### Potential game winner

CLEVELAND GUARDIANS — approximately 65.5% eventual-win estimate.

Regulation decomposition before the extra-inning branch:

- Cleveland win \~59.1%

- Tie after nine \~12.1%

- Athletics win \~28.8%

The MLB automatic-runner branch is assigned a small home-side edge, lifting Cleveland's eventual research endpoint to about 65.5%. This is an unvalidated scenario assumption, not a calibrated MLB win model.

#### Dependence / kill-path audit

Top two: Guardians ML + Over 7.5.

- Approximate joint success: \~40%.

- Approximate both-fail state: \~14%.

- Approximate probability at least one of top two wins: \~86%.

- Main both-fail family: Athletics win a low-scoring game because Lopez reaches his strong branch while Bibee allows one decisive power cluster, e.g. 4-3 / 3-2 Athletics.

Guardians ML and Athletics +1.5 positively overlap in Cleveland one-run wins; they should not be treated as independent confirmation.

#### Self-selected model targets outside the supplied slate

These are model thresholds, not claims that an operator offers them:

- Over 6.5 runs: \~71-72%, safer than the supplied Over 7.5.

- Athletics team total Under 4.5: \~70% regulation-model target; slightly lower after accounting for extra-inning exposure.

- Cleveland team total Over 3.5: \~68% regulation-model target.

These are not promoted above the supplied four in the official ranked slate because the user explicitly supplied those four contracts and the Drive baseball rule requires every supplied row to be ranked.

#### Integrity flags

- START_CROSSED_USER_OVERRIDE / PF-EVENT-STATE BLOCK

- NO_LIVE_GAME_STATE_USED_IN_MODEL

- MLB_FIELD_OWNER_POSTED_LINEUPS_NOT_RECOVERED_TO_GATE_STANDARD

- EXACT_OPERATOR_SUSPENSION/ACTION_RULES_UNKNOWN

- UNVALIDATED_SUBJECTIVE_DISTRIBUTION

- MARKET_ODDS / LINE_MOVEMENT / TIPSTERS / FANTASY-DFS EXCLUDED

- Original issue status: UNSETTLED — LATE-ISSUED RESEARCH FORECAST / NO RETROSPECTIVE

#### Sources / provenance

1\. MLB Probable Pitchers — exact event, venue, scheduled time, official probable starters and season starter lines — PRIMARY FIELD OWNER — https://www.mlb.com/probable-pitchers

2\. MLB Scores / schedule — exact event/date/state route — PRIMARY FIELD OWNER — https://www.mlb.com/scores/2026-09-19

3\. MLB Athletics injuries and roster moves — Rooker/Kurtz/Wilson and other current IL status — PRIMARY FIELD OWNER — https://www.mlb.com/athletics/news/athletics-injuries-and-roster-moves

4\. MLB Athletics report on Wilson/Kurtz/Soderstrom — season-ending availability context — PRIMARY TEAM/FIELD OWNER — https://www.mlb.com/news/jacob-wilson-nick-kurtz-expected-to-miss-rest-of-2026-season

5\. MLB Guardians injuries and roster moves — Hoskins/Holderman/Armstrong and recent day-to-day availability — PRIMARY FIELD OWNER — https://www.mlb.com/guardians/news/guardians-injuries-and-roster-moves

6\. MLB Guardians transactions — Holderman rehab status and bullpen roster context — PRIMARY FIELD OWNER — https://www.mlb.com/guardians/roster/transactions

7\. Baseball Savant / MLB — Bibee Statcast contact, xwOBA, hard-hit, barrel and HR data — PRIMARY MLB TRACKING SOURCE — https://baseballsavant.mlb.com/team/114_4

8\. MLB game video, Athletics at Rangers — official Lopez 6 IP / 2 ER / 7 K quality-start branch — PRIMARY FIELD OWNER — https://www.mlb.com/video/game/822851

9\. Reuters — Bibee latest 6 2/3 IP / 2 ER / 7 K and Cleveland recent offense — HIGH-QUALITY INDEPENDENT — https://www.reuters.com/sports/baseball/guardians-creep-closer-al-central-lead-by-hammering-twins--flm-2026-09-13/

10\. Covering the Corner series preview — current-regime wRC+, defense, starter ERA and bullpen ERA diagnostics — INDEPENDENT SECONDARY — https://www.coveringthecorner.com/cleveland-guardians-analysis/74254/series-preview-athletics-at-guardians

11\. Covering the Corner game discussion — pregame matchup / lineup corroboration — INDEPENDENT SECONDARY — https://www.coveringthecorner.com/cleveland-guardians-discussion/74401/athletics-at-guardians-bibee-vs-lopez-discussion

12\. CBS Sports / STATS LLC / Field Level Media exact-game preview — posted lineup cross-check, Lopez recent-contact/HR window, WHIP and starter context — INDEPENDENT SECONDARY — exact Athletics-at-Guardians game preview.

13\. National Weather Service Cleveland — venue-area game-window temperature/cloud/showers/wind context — GOVERNMENT FIELD OWNER — https://forecast.weather.gov/MapClick.php?FcstType=digital\&lat=41.4797\&lon=-81.6785

14\. MLB Automatic Runner glossary — extra-inning runner-on-second rule — RULES FIELD OWNER — https://www.mlb.com/glossary/rules/designated-runner

15\. MLB Regulation Game glossary — nine-inning/home-last-bat/extra-inning endpoint definition — RULES FIELD OWNER — https://www.mlb.com/glossary/rules/regulation-game

16\. Sports Research Drive — METHOD.md, RULES_BASEBALL.md, RULES_GENERAL.md, CONTROL_MANIFEST_2026-09-19.md, DATA_SOURCE_REGISTER.md and FORECAST_PREFLIGHT_MANIFEST.md — governing methodology.

Source firewall: no sportsbook odds, betting picks, tipster predictions, line movement, fantasy/DFS projections, or market consensus were used as predictive inputs. The user-supplied 7.5/+1.5/ML contracts were queried only after distribution freeze.

#### Document mapping / candidate learnings

- Starter HR/contact tail plus depleted opponent lineup should remain a two-sided mixture rather than a one-sign Under adjustment -\> existing RULES_BASEBALL starter/current-regime and cluster controls; no new fixed coefficient.

- Exact posted-lineup field-owner retrieval remained incomplete at the issuance gate -\> DATA_SOURCE_REGISTER source-latency/retrieval observation.

- Start crossing with explicit user direction demonstrates that normal preflight can fail while a clearly labelled research-only late forecast is still recorded without live-state contamination -\> EXTERNAL_LOGGING_WORKFLOW process note candidate; do not weaken normal pregame gate.

---

#### Settlement and retrospective — P-474

Settlement status: SETTLED / RETROSPECTIVE COMPLETE.

Verified final: Cleveland Guardians 12, Athletics 6.

Actual full-game total: 18 runs.

Actual margin: Cleveland +6.

Three-source final-state gate: PASS.

- MLB official scoreboard/game story: FINAL, Cleveland 12-6.

- Associated Press / CBS reporting: Cleveland 12-6 final.

- Athletics Nation / Field Level Media independent recap: Cleveland 12-6 final.

Settlement sources:

- MLB official scoreboard: https://www.mlb.com/scores/2026-09-19

- MLB official game story: https://www.mlb.com/stories/game/824380

- AP/CBS final recap: CBS Sports exact-game recap, Sep 19, 2026.

- Athletics Nation final recap: https://www.athleticsnation.com/athletics-scores-and-standings/109853/as-fall-to-guardians-12-6

- Field Level Media final recap: https://fieldlevelmedia.com/mlb/angel-martinez-homers-twice-guardians-dominate-athletics/

##### Pick-by-pick settlement — supplied slate

1\. Guardians ML — WIN. Cleveland won 12-6.

2\. Over 7.5 — WIN. Final total was 18.

3\. Athletics +1.5 — LOSS. Oakland lost by six.

4\. Under 7.5 — LOSS.

Potential game winner: Cleveland Guardians — WIN.

Self-selected model targets:

- Over 6.5 — WIN.

- Athletics team total Under 4.5 — LOSS; Athletics scored 6.

- Cleveland team total Over 3.5 — WIN; Cleveland scored 12.

##### Ranking / top-two / totals review

Rank #1 Guardians ML succeeded, so no Rank-1 failure trigger applies.

Highest-ranked full-game O/U, Over 7.5, succeeded; no mandatory top-O/U failure trigger applies.

Top two supplied selections both succeeded: Guardians ML WIN + Over 7.5 WIN. Hit@2 = YES; both-win = YES.

The ordering of Guardians ML above Over 7.5 was defensible on pre-game evidence because Cleveland had the stronger side profile, while the total was only \~0.27 SD above the supplied line and retained a genuine low-scoring branch.

##### What the outcome turned on

Cleveland's upper-tail offensive cluster arrived immediately. The Athletics led 2-0 in the top of the first, but Cleveland scored five before Jacob Lopez recorded an out, including Chase DeLauter's three-run homer and Angel Martínez's two-run homer. Cleveland added five more in the third. Lopez was charged with 10 runs and 10 hits in 2 2/3 innings.

The important second mechanism was that Tanner Bibee also failed to suppress Oakland. Bibee allowed six runs on 12 hits in 4 2/3 innings. The final therefore came from a two-sided starter-failure / sequencing / home-run state rather than a simple Cleveland-control state.

##### Expected script vs reality

What went right:

- Cleveland was correctly preferred to win.

- Lopez's contact/home-run and early-hook risk was explicitly identified before issue.

- The Over was correctly preferred to the Under.

- Cleveland team total Over 3.5 and Over 6.5 both captured the favourite's offensive upside.

What went wrong:

- The 8.34-run centre badly understated the realized 18-run upper tail.

- The model's Athletics team-total Under 4.5 depended too much on Bibee/depleted-lineup suppression; Bibee instead allowed six runs himself.

- The high-run branch existed, but its two-sided form — Lopez collapse plus Bibee collapse in the same game — was not given enough prominence.

This does not justify adding a fixed Over coefficient. One realised extreme game is not evidence that the centre itself should be shifted by an arbitrary amount.

##### Availability / lineup / source audit

The issue-time card explicitly recorded that field-owner posted orders were not recovered to gate standard and therefore did not rank player props. That limitation was handled correctly. The final was settled from multiple explicit terminal-state sources rather than search snippets.

Source-quality result:

- MLB official final/game story: retained as field owner.

- AP/CBS and Field Level Media: retained as high-quality independent final/result sources.

- Athletics Nation: useful secondary game-script corroboration, not a substitute for MLB field ownership.

##### Blind spots and mitigation

Blind spot: simultaneous failure of both starters was under-emphasized even though each had a documented contact/HR tail.

Pre-game knowability: PARTLY KNOWABLE — the component risks were known; the exact joint realization was not.

Materiality: HIGH for the total and Athletics team total; LOW for the Cleveland winner.

Mitigation: when both starters carry credible upper-tail contact/HR risk, explicitly show a joint two-starter-failure branch before ranking a total or team-total Under.

Existing control check: RULES_BASEBALL already requires BB-B2 joint early-hook, BB-B3 cluster and BB-B5 relief-transition states. This is principally an execution/emphasis observation, not evidence for a new permanent rule.

##### Document mapping

- RULES_BASEBALL.md — existing BB-B2/BB-B3/BB-B5 controls; reinforce execution only, no new coefficient.

- DATA_SOURCE_REGISTER.md — retain the issue-time official-lineup retrieval-latency observation.

- Prediction log — record the two-sided starter-collapse learning with P-474.

---

#### 2026-09-21 independent re-audit — P-474

**Re-verification of the settled final.** The 2026-09-20 settlement was re-checked against a source lineage that was not used in the original settlement pass, so the terminal state now rests on four distinct lineages rather than three.

- MLB Stats API official schedule record, `statsapi.mlb.com/api/v1/schedule?sportId=1&date=2026-09-19`, gamePk **824380**: status `Final`, Athletics 6 @ Cleveland Guardians 12.
- MLB Stats API official linescore for gamePk 824380: 9 innings; away line 2-0-1-1-2-0-0-0-0 (6 runs, 12 hits, 1 error); home line 5-0-5-1-0-1-0-0-X (12 runs, 15 hits, 1 error). The bottom of the ninth was not played, which is consistent with the home side leading.
- MLB Stats API official boxscore for gamePk 824380: Jacob Lopez 2.2 IP, 10 R / 10 ER, 10 H, 2 HR; Tanner Bibee 4.2 IP, 6 R / 6 ER, 12 H, 1 HR.

Every settled row is unchanged. **Final total 18; margin Cleveland +6.** The inning-by-inning record independently confirms the game-script claims in the 2026-09-20 retrospective (Athletics 2-0 in the top of the first, Cleveland 5 in the bottom of the first and 5 more in the third).

**Settlement-evidence upgrade.** The original settlement leaned on narrative recaps (AP/CBS, Athletics Nation, Field Level Media). Those remain valid corroboration, but the MLB Stats API linescore/boxscore is a structured field-owner record that settles run totals, margins, innings played and individual pitching lines without narrative interpretation. It should be the first settlement route for every MLB card, ahead of any recap.

**Ranking metrics — supplied slate (the only ranked slate on this card).**

| Metric | Value | Basis |
|---|---|---|
| Rank-1 | **WIN** | Guardians ML |
| Hit@2 | **YES** | Guardians ML + Over 7.5 |
| Wins@2 | **2 / 2** | both top-two rows won |
| NDCG@2 (binary relevance, ideal drawn from the whole ranked slate) | **1.000** | DCG@2 = 1 + 1/log₂3 = 1.6309; IDCG@2 = 1.6309 |
| Ranked-row record | 2 W / 2 L | forced-pair structure; see the note below |
| Winner call | **WIN** | Cleveland, p ≈ 0.655 |

**Forced-pair caveat (new, and it matters).** Over 7.5 / Under 7.5 is a strict complementary pair on a half-line: exactly one of those two rows wins by construction, whatever the model says. Only the preferred side carries information. Counting the preferred sides once, this card's informative decision rows are Guardians ML (0.655, **W**), Athletics +1.5 (0.528, **L**) and Over 7.5 (0.606, **W**) — 2 W / 1 L, not "2 W / 2 L out of four". The self-selected targets add Over 6.5 (**W**), Athletics team total Under 4.5 (**L**) and Cleveland team total Over 3.5 (**W**).

**Mandatory validation questions.**

1. **Confirmed starting lineups for both sides?** **NO — partial.** The card recorded `MLB_FIELD_OWNER_POSTED_LINEUPS_NOT_RECOVERED_TO_GATE_STANDARD`: the MLB starting-lineups index still rendered the matchup as TBD inside the research window, and a CBS/STATS-Field Level secondary cross-check was used with an explicit evidence cap. That was handled correctly — no player prop was ranked. The post-hoc boxscore shows the secondary cross-check was materially right, but that is hindsight and does not retroactively upgrade the pre-game evidence grade.
2. **Bench / bullpen / rotation state obtained?** **YES, partially and with the right framing.** Cleveland's preceding-game bullpen usage (Cantillo six relief innings; Gaddis and Smith in late innings) was recovered and used as an availability constraint only, not as a quality penalty. The Athletics bullpen was characterised by current-regime ERA rather than by named availability, which is weaker.
3. **Coaching / manager information?** **NOT OBTAINED, and not material.** MLB managerial decisions that mattered here (Lopez's hook at 2⅔ innings) are downstream of performance, not a pre-game identity fact.
4. **Injuries, suspensions, rest, late withdrawals checked?** **YES.** Rooker, Kurtz, Wilson (60-day IL) and Soderstrom (season-ending surgery) for the Athletics; Hoskins, Holderman and Armstrong for Cleveland, with DeLauter and Martínez flagged as day-to-day with residual uncertainty. DeLauter and Martínez both played and both homered, so the decision to treat them as available was correct.
5. **Were the original sources accurate and current?** **YES for availability and starters; INCOMPLETE for posted lineups.** No source used in the card was contradicted by the final record.
6. **Better sources available for future use?** **YES.** `statsapi.mlb.com` `game/{pk}/boxscore` exposes `battingOrder`, `bench` and `bullpen` by name, and `schedule?hydrate=lineups` returns 9+9 once orders are posted. The 2026-09-19 implementation ledger already recorded this lane as demonstrated. This card fell back to a CBS/STATS secondary instead of using it. That is an execution gap, not a missing capability.
7. **Blind spots in the pre-game analysis?** **YES.** The joint two-starter-failure branch. Both starters carried a documented contact/home-run tail, and the card said so about each of them separately, but the state in which *both* tails fire in the same game was never given explicit mass. The realised 18-run total sat far above the 8.34 centre precisely because both fired.
8. **How should this be handled in future?** When both starters carry a credible upper-tail contact/HR profile, print an explicit joint-collapse branch with its own weight *before* ranking any total or team-total Under. `RULES_BASEBALL` controls BB-B2 (joint early hook), BB-B3 (cluster) and BB-B5 (relief transition) already require these states; the defect is that they were listed and not executed as weighted branches. That is recurring-mistake **M15 (control listed, not executed)**, which turns out to be the dominant defect across this mini log — see §4.7.

**Verdict on this event.** Rank #1 and the top over/under both won, the winner call was right, and the one genuine analytical miss — the magnitude of the upper tail — did not change any ranked outcome. No rule change is warranted. The realised 18-run game is a single upper-tail realisation and, per `SCORING_AND_VALIDATION.md` §5, one named failure does not prove its mass was too low.

---


### P-475 — WNBA — Chicago Sky @ Atlanta Dream

- Canonical / staging ID: P-475

- Competition: WNBA 2026 regular season

- Official event ID: WNBA game 1022600310

- Venue: State Farm Arena, Atlanta, Georgia, United States

- Venue timezone: America/New_York

- Official venue-local start: Sep 19, 2026 at 7:00 PM EDT

- Australia/Melbourne conversion: Sep 20, 2026 at 9:00 AM AEST; calendar-date rollover = YES

- Research cutoff / independent distribution freeze: Sep 20, 2026 at approximately 9:04:40 AM AEST

- Issuance state: START_CROSSED_UNVERIFIED. Research crossed scheduled tip while completing the required source and methodology checks. No live score, possession, lineup-on-court, shot, foul, injury-in-game or other post-tip performance information was admitted into the predictive model.

- Method / controls: MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-BASKETBALL

- Operating mode: SPORTS_ONLY / MARKET_BLIND

- Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE

- Preflight: FAIL with exactly one blocking finding, PF-EVENT-STATE. Source count/lineage, field-owner mix, timezone conversion, source firewall, line quarantine and freeze order otherwise passed.

- No retrospective performed.

#### Identity / supplied contracts

The supplied thresholds were quarantined until after the independent basketball distribution was frozen:

- Atlanta Dream -15.5

- Chicago Sky +15.5

- Full-game Over 176.5

- Full-game Under 176.5

Exact operator overtime/action/void terms were not independently supplied. The research endpoint is a normal completed WNBA game including the explicit overtime tail; operator settlement remains a separate field if later required.

#### Participant / availability state

Official WNBA injury-report process was checked, but the dynamically rendered league page did not expose the exact current team rows through the accessible research route. Current pre-tip reporting was therefore reconciled across team/league records and independent current sources and is evidence-capped rather than relabelled field-owner-confirmed.

Chicago:

- Natasha Cloud — QUESTIONABLE, left knee, after leaving the Sep. 17 Washington game in the first half and not returning.

- Azurá Stevens — OUT, right knee.

- DiJonai Carrington — OUT, left foot.

- Skylar Diggins — OUT for the remainder of the season, right knee.

- Rickea Jackson — OUT for the remainder of the season after a torn left ACL.

- Current available core includes Kamilla Cardoso, Courtney Vandersloot, Sydney Taylor, Rachel Banham, Gabriela Jaquez, Aicha Coulibaly, Jacy Sheldon and Elizabeth Williams.

- Cloud's unresolved availability is represented as a minutes/role mixture; no binary full-workload assumption is made.

Atlanta:

- Brionna Jones — OUT for the remainder of the season, left leg.

- Current core available in pre-tip records: Jordin Canada, Allisha Gray, Rhyne Howard, Angel Reese, Naz Hillmon, DeWanna Bonner, Madina Okot and the supporting guard/wing rotation.

- Atlanta's long-running most-used starting unit has been Canada / Gray / Howard / Hillmon / Reese, but a confirmed five for this exact game was not recovered to gate standard before the research cutoff and is not relabelled as confirmed.

Because both confirmed starting fives were not recovered to the governing gate standard, lineup-sensitive player props are not promoted. Full-game side/total rows carry a participant-evidence cap.

#### Current regime / recent form

Current records immediately before the event:

- Atlanta: 27-14, 8-2 over the latest league-recorded ten-game form window.

- Chicago: 15-26, four straight losses; the current standings snapshot shows Chicago materially behind Atlanta.

Descriptive score windows calculated from the latest completed game sequence:

- Atlanta L5: 4-1; 90.4 scored / 80.2 allowed.

- Atlanta L10: 8-2; 97.5 scored / 83.0 allowed.

- Atlanta L15: 11-4; 94.1 scored / 84.7 allowed.

- Atlanta L20: 15-5; 94.9 scored / 86.3 allowed.

- Chicago L5: 1-4; 78.0 scored / 93.0 allowed.

- Chicago L10: 3-7; 81.0 scored / 90.9 allowed.

- Chicago L15: 6-9; 85.2 scored / 91.3 allowed.

- Chicago L20: 8-12; 86.9 scored / 91.6 allowed.

These result windows are diagnostic only. They are not converted into a mechanical points adjustment.

Latest completed games:

- Atlanta beat Connecticut 103-59. Angel Reese scored 30 with 10 rebounds in under 25 minutes; Atlanta's blowout reduced her exposure rather than requiring full star minutes.

- Chicago lost 110-80 to Washington. Chicago was heavily outrebounded and Washington converted Chicago turnovers into transition/early-offense scoring. Cloud left with the knee issue.

- Those two blowouts widen today's mismatch branches but do not by themselves justify a 15.5-point central margin.

Current-season head-to-head:

- Atlanta 82-75 Chicago on June 9.

- Atlanta 93-91 Chicago on July 19.

Atlanta is 2-0, but the margins were only 7 and 2. Those games are retained as direct matchup context; today's much more depleted Chicago roster means they do not control the current margin distribution.

#### Possession / efficiency mechanism

Historical structured current-season baselines before the last game placed Atlanta around:

- 90.8 points per game;

- 80.6 pace;

- 112.3 offensive rating;

- 106.0 defensive rating;

- +6.3 net rating.

Chicago's comparable baseline before the last game was around:

- 86.7 points per game;

- 81.7 pace;

- 105.5 offensive rating;

- 109.1 defensive rating;

- -3.6 net rating.

The current model does not add arbitrary points for injuries or recent results. Instead, it uses an explicit scenario mixture spanning Cloud active/functional, Cloud limited/out, Atlanta favourite sustain, Atlanta blowout slowdown/bench compression, Chicago shooting resistance and a higher-pace late-scoring branch.

Expected possession environment: approximately 80-82 regulation possessions, with material variance from Chicago transition defence/turnovers and Atlanta's ability to control the game state.

Decision-driving mechanisms:

1\. Atlanta's Gray/Howard/Canada perimeter creation against a depleted Chicago guard/wing rotation.

2\. Reese/Hillmon/Okot/Bonner frontcourt rebounding and second-chance pressure against a Chicago group missing Stevens.

3\. Chicago's Cardoso interior scoring/rebounding as its clearest stable half-court floor.

4\. Cloud's uncertain creation/defence and replacement minutes for Vandersloot/Taylor/Banham/Jaquez/Coulibaly/Sheldon.

5\. Atlanta's blowout rotation: starter minutes can fall while bench pace/offence persists.

6\. Chicago's garbage-time response: reduced Atlanta defensive intensity can compress the margin and lift the total simultaneously.

7\. Late-foul and overtime branches remain explicit but low-mass.

#### Frozen independent joint score distribution

Model: explicit UNVALIDATED_SUBJECTIVE scenario mixture. Within each scenario, team-score uncertainty is represented with approximately 10-point team SD and modest positive game-level correlation (\~0.15). This is an uncertainty representation, not a calibrated WNBA model.

Scenario 1 — Cloud active / competitive central: weight 0.22; ATL 95, CHI 80.

Scenario 2 — Cloud limited/out / Atlanta central: weight 0.22; ATL 97, CHI 76.

Scenario 3 — favourite sustain / shooting-rebound separation: weight 0.22; ATL 104, CHI 74.

Scenario 4 — blowout slowdown / bench compression: weight 0.18; ATL 91, CHI 82.

Scenario 5 — Chicago resistance / shooting-high: weight 0.10; ATL 92, CHI 87.

Scenario 6 — higher-pace bench / late-scoring branch: weight 0.06; ATL 101, CHI 85.

Frozen distribution:

- Atlanta centre: 96.76

- Chicago centre: 79.16

- PROJECTED TOTAL: 175.92

- PROJECTED ATLANTA MARGIN: +17.60

- Approx total SD including scenario uncertainty: 15.54

- Approx margin SD including scenario uncertainty: 15.40

- Representative score family: Atlanta 97-79

- Distribution ID: P-475-dist-v1

- Distribution SHA-256: 0392fe62912bad317ee0ffae5adb0d08ce9bd73b6c044eb9543ae1889d443968

##### Mandatory total projection / team-score budget

PROJECTED TOTAL: 175.92

SUPPLIED TOTAL: 176.5

RAW GAP: -0.58 points

DISTRIBUTION WIDTH: \~15.54 points SD

NORMALIZED GAP: \~-0.04 SD

ASSESSMENT: CLOSE TO PROJECTION / WEAK MAIN-TOTAL EDGE.

Preferred supplied side: Under 176.5, but only marginally.

Team-score threshold budget:

- Chicago floor 70-74 requires Atlanta roughly 103-107 to cross 176.5; the favourite-sustain branch can do it, while many suppression/blowout states remain Under.

- Chicago centre 78-81 requires Atlanta about 96-99; this is almost exactly Atlanta's central score range, so ordinary states land on both sides.

- Chicago ordinary high 86-88 requires only Atlanta 89-91; that underdog-response branch tends to push the game Over even when the final margin compresses.

- Atlanta ordinary high 101-104 can push the game Over even with Chicago in the mid-70s.

- Therefore Chicago's depleted offence is not an automatic Under: Atlanta's own ceiling can consume the total budget.

Model alternate-total targets from the same frozen distribution:

- Under 184.5 \~71.0%.

- Under 188.5 \~80%+.

These are model thresholds only; operator availability is not asserted.

##### Mandatory large-spread separation audit

Projected margin: Atlanta +17.60

Supplied spread: Atlanta -15.5

Raw separation beyond line: +2.10 points

Margin width: \~15.40 points SD

Normalized separation: \~0.14 SD

ASSESSMENT: LINE INSIDE THE CENTRAL MARGIN CORRIDOR / weak-to-modest supplied spread edge.

Mismatch states:

- Favourite sustain: Atlanta keeps pressure, rebounding and transition efficiency high -\> 25-30+ margin possible.

- Favourite slowdown: starter minutes fall; Atlanta bench scores enough to win but Chicago response compresses the closing margin -\> 7-12 point final possible.

- Underdog response: Cardoso plus secondary guards score against reduced defensive intensity -\> margin can fall inside 15.5 while total rises.

- Underdog suppression: Chicago's missing creators/wings reduce half-court quality and defensive resistance -\> wide Atlanta margin with a lower total.

The two 2026 H2H margins (7 and 2) are a warning against treating -15.5 as automatic; today's roster state is worse for Chicago, but the current model still keeps substantial compression mass.

#### Best four model-selected picks

These are model target thresholds, not claims that a sportsbook currently offers each exact line.

1\. ATLANTA DREAM ML — \~87.3% UNVALIDATED_SUBJECTIVE.

   Rationale: stronger current roster continuity, superior current team process, home venue, Chicago's depleted creation/wing defence and Atlanta's multiple scoring/rebounding pathways.

   Main failure: Chicago shoots above its ordinary range, Cardoso controls the paint and Atlanta's post-World-Cup/rotation efficiency underperforms.

2\. ATLANTA TEAM TOTAL OVER 88.5 — \~77.2%.

   Rationale: Atlanta's independent team centre is \~96.8, every central scenario keeps the favourite above 90 before within-scenario shooting variance, and Chicago just allowed 110 while losing transition/rebounding control.

   Main failure: Atlanta builds an early lead, sharply cuts primary creators and the bench shoots poorly enough to stall in the mid-80s.

3\. CHICAGO TEAM TOTAL UNDER 86.5 — \~75.1%.

   Rationale: independent Chicago centre \~79.2; Diggins/Jackson/Carrington/Stevens unavailable and Cloud uncertain; Atlanta owns a strong current defensive/rebounding structure.

   Main failure: garbage-time response, Cardoso paint efficiency, secondary shooting variance or Atlanta defensive-intensity reduction lifts Chicago into the high 80s.

4\. ATLANTA -8.5 — \~71.9%.

   Rationale: materially safer than -15.5 while preserving the same current-regime mismatch mechanism; survives more blowout-compression states.

   Main failure: Cloud plays effectively, Chicago's secondary guards shoot well and Atlanta wins only narrowly, as in the two prior 2026 meetings.

#### Supplied slate ranking

1\. DREAM -15.5 — \~55.1% — preferred supplied side / LOW evidence because line sits close to margin centre.

2\. UNDER 176.5 — \~51.6% — preferred supplied total / CLOSE TO PROJECTION / very weak directional separation.

3\. OVER 176.5 — \~48.4% — live ordinary-high/garbage-time branch but slightly below the frozen centre query.

4\. SKY +15.5 — \~44.9% — substantial compression path remains, but current roster depletion makes Atlanta 16+ more likely than Chicago +15.5 in the model.

Forced-pair integrity:

- Dream -15.5 + Sky +15.5 = 100% conditional on action.

- Over 176.5 + Under 176.5 = 100% conditional on action.

- No push exists at either half-point threshold.

#### Potential game winner

ATLANTA DREAM — \~87.3% eventual-win estimate.

This winner view is materially stronger than Atlanta -15.5. The model is confident Atlanta wins much more often than not but only modestly prefers a 16+ point final margin.

#### Dependence / kill-path audit

Top two model picks: Atlanta ML + Atlanta team total Over 88.5.

- Approx joint win: \~73.3%.

- Approx both-fail: \~8.9%.

- Approx at least one wins: \~91.1%.

- Main both-fail state: Atlanta's shooting/turnover process collapses enough to keep the Dream at 88 or below while Chicago's remaining creators/Cardoso produce the upset.

Across all four model-selected targets, approximate all-four-win mass is \~55.6%; approximate all-four-fail mass is \~5.4%. These are derived from the same unvalidated joint scenario object and are not independence calculations.

Top two supplied sides: Atlanta -15.5 + Under 176.5.

- Approx joint win: \~28%.

- Approx both-fail: \~21.5%.

- Main both-fail family: Atlanta wins narrowly or Chicago stays within 15.5 while garbage-time/late-foul scoring pushes the total Over 176.5.

#### Information not confirmed / integrity flags

- START_CROSSED_USER_OVERRIDE / PF-EVENT-STATE BLOCK

- NO_LIVE_GAME_STATE_USED_IN_MODEL

- CONFIRMED_STARTING_FIVES_NOT_RECOVERED_TO_GATE_STANDARD

- CLOUD_FINAL_ACTIVE/INACTIVE_STATUS_NOT_RECOVERED_PRETIP_TO_FIELD_OWNER_STANDARD

- WNBA_OFFICIAL_INJURY_PAGE_DYNAMIC_ROWS_NOT_EXPOSED_IN_RESEARCH_ROUTE

- EXACT_OPERATOR_OVERTIME/ACTION_TERMS_UNKNOWN

- UNVALIDATED_SUBJECTIVE_DISTRIBUTION

- NO SPORTSBOOK ODDS / MARKET MOVEMENT / TIPSTER / FANTASY-DFS PREDICTIVE INPUT

- Original issue status: UNSETTLED — LATE-ISSUED RESEARCH FORECAST / NO RETROSPECTIVE

#### Sources / provenance

1\. WNBA exact game page, game 1022600310 — exact event, 7:00 PM ET start, State Farm Arena, prior 2026 H2H — PRIMARY FIELD OWNER — https://www.wnba.com/game/1022600310/chi-vs-atl

2\. WNBA official injury-report page — reporting rules and current-update process; exact dynamic rows were not exposed through the accessible text route — PRIMARY FIELD OWNER — https://www.wnba.com/wnba-injury-report

3\. WNBA official current standings/homepage — current Atlanta record and league context — PRIMARY FIELD OWNER — https://www.wnba.com/

4\. Atlanta Dream official Sep. 17 recap — 103-59 win, Reese 30/10 in under 25 minutes, current player/rotation context — PRIMARY TEAM — https://dream.wnba.com/news/dream-returns-with-a-decisive-win

5\. Atlanta Dream official current roster — Canada/Gray/Howard/Reese/Hillmon and current rotation — PRIMARY TEAM — https://dream.wnba.com/roster

6\. Chicago Sky official WNBA team page — current 15-26 record and roster — PRIMARY FIELD OWNER / TEAM — https://www.wnba.com/team/1611661329/chicago-sky

7\. WNBA official Sep. 17 Chicago recap — Washington 110, Chicago 80 — PRIMARY FIELD OWNER — WNBA game recap archive.

8\. Reuters, Sep. 1 — Skylar Diggins shut down for the 2026 season with knee injury — HIGH-QUALITY INDEPENDENT.

9\. Reuters / NBC Chicago / WNBA player archive — Rickea Jackson torn ACL, out for season — HIGH-QUALITY INDEPENDENT + LEAGUE ARCHIVE.

10\. Athlon final pre-tip injury report, published 2:00 PM EDT — Cloud questionable; Stevens/Carrington/Diggins out; Jones out — CURRENT INDEPENDENT SECONDARY; source lineage is not treated as a field owner.

11\. Field Level Media current Chicago recap — Cloud left Sep. 17 with left-knee injury; Chicago lost 110-80 — INDEPENDENT SECONDARY.

12\. Basketball-Reference 2026 Atlanta / Chicago schedules and team pages — pace, ORtg/DRtg, season process and disaggregated game sequence — HISTORICAL STRUCTURED CANDIDATE / diagnostic only.

13\. Basketball-Reference Atlanta starting-lineup history — long-running Canada/Gray/Hillmon/Howard/Reese lineup continuity — HISTORICAL STRUCTURED CANDIDATE; not a confirmed exact-game five.

14\. Sports Research Drive — METHOD.md, RULES_BASKETBALL.md, RULES_GENERAL.md, CONTROL_MANIFEST_2026-09-19.md, DATA_SOURCE_REGISTER.md and FORECAST_PREFLIGHT_MANIFEST.md — governing methodology.

Source firewall: sportsbook odds, consensus, betting picks, line movement, fantasy/DFS projections and betting-derived analysis were not admitted as predictive inputs. User-supplied -15.5/+15.5/176.5 contracts were queried only after the independent distribution freeze.

#### Document mapping / candidate learnings

- Large-spread Chicago depletion does not eliminate blowout-compression/garbage-time response -\> existing RULES_BASKETBALL mismatch-state controls; no new coefficient.

- Main 176.5 total sits almost exactly on independent centre despite strong Atlanta-side mismatch -\> reinforces team-score-budget requirement rather than a one-sign depleted-underdog Under.

- Exact official injury-row/confirmed-five retrieval remained incomplete near tip -\> DATA_SOURCE_REGISTER source-access/latency observation.

- Start-crossing late-research handling remains a process exception only; do not weaken the normal pregame issuance gate in METHOD/FORECAST_PREFLIGHT.

---

#### Settlement and retrospective — P-475

Settlement status: SETTLED / RETROSPECTIVE COMPLETE.

Verified final: Atlanta Dream 106, Chicago Sky 81.

Actual full-game total: 187 points.

Actual margin: Atlanta +25.

Three-source final-state gate: PASS.

- WNBA official recap: Atlanta 106-81 Chicago, explicit completed game recap.

- Atlanta Dream official team recap: 106-81 final.

- CBS/AP / independent box-score reporting: 106-81 final.

Settlement sources:

- WNBA official recap: https://www.wnba.com/watch/video/game-recap-atlanta-dream-106-chicago-sky-81-09-19-2026

- Atlanta Dream official recap: https://dream.wnba.com/news/dream-dominate-in-final-regular-season-home-game

- CBS Sports exact-game recap / box score, Sep 19, 2026.

- StatMuse exact-game team-stat record, Sep 19, 2026.

##### Pick-by-pick settlement — model-selected slate

1\. Atlanta Dream ML — WIN.

2\. Atlanta team total Over 88.5 — WIN; Atlanta scored 106.

3\. Chicago team total Under 86.5 — WIN; Chicago scored 81.

4\. Atlanta -8.5 — WIN; Atlanta won by 25.

##### Pick-by-pick settlement — supplied slate

1\. Dream -15.5 — WIN.

2\. Under 176.5 — LOSS; final total 187.

3\. Over 176.5 — WIN.

4\. Sky +15.5 — LOSS.

Potential game winner: Atlanta Dream — WIN.

##### Ranking / top-two review

Model-selected Rank #1 Atlanta ML succeeded.

The model-selected top two both succeeded: Atlanta ML WIN + Atlanta team total Over 88.5 WIN.

All four model-selected targets won.

Supplied Rank #1 Dream -15.5 succeeded. The second supplied row, Under 176.5, lost, so at least one of the supplied top two hit but both did not.

The spread read was materially better than the full-game-total read: projected Atlanta +17.6 versus actual +25 correctly identified the wide-margin family, while the projected total 175.92 sat almost exactly on the supplied 176.5 line.

##### Enhanced full-game O/U review

Under 176.5 was the preferred supplied full-game total and lost. It receives the enhanced totals review even though the higher-ranked model-selected Atlanta team-total Over 88.5 won.

Why Under was preferred:

- Independent centre 175.92 was 0.58 below the line.

- Chicago's depleted creation supported an underdog-suppression branch.

- Favourite blowout states could reduce starter minutes.

Why it failed:

- Atlanta scored 106, materially above the central Atlanta score.

- Atlanta shot 52.9% from the field and 50.0% from three (13-of-26), while producing 29 assists and 13 steals.

- The decisive separation occurred in a 32-point Atlanta third quarter, and Isobel Borlase supplied 18 points as depth scoring remained productive.

- Chicago scored 81, close to the model's ordinary Chicago centre. The Under miss was driven primarily by Atlanta's favourite-offensive-ceiling branch, not by an unexpected Chicago offensive explosion.

Could another supplied total side have ranked above it ex ante?

The pre-game gap was only \~0.04 SD, so the Under/Over ordering was inherently fragile. The outcome alone does not prove Over should have been preferred. However, the card itself simultaneously gave Atlanta team total Over 88.5 a much stronger \~77% model probability. That should have made the full-game Under's vulnerability to an Atlanta 100+ state even more explicit in the ranking narrative.

Smallest justified improvement:

Before ranking a full-game Under in a mismatch, reconcile the favourite team-total upper tail and bench-offence branch directly with the game-total budget. If the favourite's high-confidence team-total Over can consume most of the total by itself, the full-game Under must remain low evidence unless the underdog floor is sufficiently low in the same joint states.

This is already substantially covered by RULES_BASKETBALL controls 11, 17 and 18 plus PF-10 distribution-first. No new fixed adjustment is justified from one game.

##### What went right

- Atlanta winner and separation were correctly identified.

- The safer Atlanta -8.5 alternate won comfortably.

- Atlanta TT Over 88.5 correctly captured the favourite's scoring ceiling.

- Chicago TT Under 86.5 correctly captured Chicago's limited scoring output.

- The model explicitly warned that a depleted underdog does not automatically make the full game Under; Atlanta's own ceiling could consume the budget. That warning described the realised mechanism.

##### What went wrong

- The preferred supplied Under 176.5 was too close to the centre to deserve much directional confidence.

- Atlanta's shooting/ball-movement ceiling was realized at an extreme level: 50% from three and 29 assists.

- The full-game total ranking did not fully reflect how strongly the model already liked Atlanta's own team-total Over.

##### Availability / lineup audit

Pre-game, confirmed starting fives were not recovered to gate standard and the card correctly capped participant-sensitive confidence. Post-game reporting shows the available Atlanta core delivered across multiple roles, including Reese, Gray, Howard, Canada and Borlase. No retrospective assumption is used to pretend the exact final five was known pre-tip.

The unresolved pre-game Natasha Cloud status remains a source-process limitation; no prohibited fantasy source is used to backfill it.

##### Source audit

- WNBA official recap and Dream official recap: retained as primary result/game-script sources.

- CBS/AP: retained as high-quality independent box-score/final corroboration.

- StatMuse: useful structured diagnostic for team-stat cross-check, not the sole terminal-state source.

##### Blind spots and mitigation

Blind spot: favourite bench/depth scoring staying efficient after separation.

Pre-game knowability: PARTLY KNOWABLE — roster depth and blowout states were known, exact 50% three-point shooting was not.

Materiality: HIGH for the full-game total; LOW for winner.

Mitigation: explicitly couple favourite team-total ceiling, starter-minute reduction and bench offensive quality in the game-total state tree.

##### Document mapping

- RULES_BASKETBALL.md — controls 11/17/18 already govern mismatch total, team-score budget and late-blowout multi-axis states; reinforce execution, no new fixed rule.

- DATA_SOURCE_REGISTER.md — WNBA exact-injury/starting-five retrieval latency remains a source-access observation.

- Prediction log — record the full-game Under miss alongside the successful favourite team-total Over.

---

#### 2026-09-21 independent re-audit — P-475

**Re-verification of the settled final.** Re-checked at the ESPN WNBA site API, a lineage not used in the original settlement pass.

- `site.api.espn.com/apis/site/v2/sports/basketball/wnba/scoreboard?dates=20260919`, event **401857199**: status `Final`, Atlanta Dream 106, Chicago Sky 81.
- Quarter lines — Atlanta 26 / 25 / **32** / 23; Chicago 25 / 22 / 19 / 15. The third-quarter separation described in the 2026-09-20 retrospective is confirmed exactly.
- ESPN summary team statistics — Atlanta FG 36-68 (52.9%), 3PT **13-26 (50.0%)**, 29 assists, 13 steals, 35 rebounds, 15 turnovers; Chicago FG 31-67 (46.3%), 3PT **4-20 (20.0%)**, 21 assists, 8 steals, 30 rebounds, 17 turnovers.

Every settled row is unchanged. **Final total 187; margin Atlanta +25.**

**Two pre-game uncertainties are now resolved — this is new information the 2026-09-20 pass did not record.**

- **Natasha Cloud did not play.** The ESPN player box lists Cloud as a **DNP**, alongside Azurá Stevens, Skylar Diggins and DiJonai Carrington. The card's pre-tip status for her was QUESTIONABLE and was represented as a minutes/role mixture rather than a binary. The mixture was the right handling, and the "limited/out" leg of it is what actually occurred. The card should not be credited with knowing this, but the method of representing an unresolved availability as a weighted branch rather than as an assumed state is validated here.
- **Atlanta's starting five was exactly Canada / Gray / Howard / Hillmon / Reese** — the "long-running most-used starting unit" the card identified from Basketball-Reference lineup history but explicitly refused to relabel as confirmed. Chicago started Cardoso / Vandersloot / Coulibaly / Taylor / Jaquez. The Basketball-Reference lineup-continuity proxy was exactly right on the favourite, and the card was right not to overclaim it. Continuity history is a good prior on a starting five and a bad substitute for a confirmed team sheet.

**Chicago's scoring shape, newly visible.** Chicago's 81 came from breadth rather than from its nominal core: Jaquez 14, Cardoso 11, Coulibaly 11, Vandersloot 10, Maly 10, Sheldon 9, with 4-of-20 from three. The Chicago team-total Under 86.5 therefore won through the mechanism the card named — limited creation and no perimeter efficiency — not by accident.

**Ranking metrics.**

| Metric | Model-selected slate | Supplied slate |
|---|---|---|
| Rank-1 | **WIN** (Atlanta ML) | **WIN** (Dream -15.5) |
| Hit@2 | **YES** | **YES** |
| Wins@2 | **2 / 2** | **1 / 2** |
| NDCG@2 | **1.000** | **0.613** (DCG 1.000 / IDCG 1.6309) |
| Row record | 4 W / 0 L | 2 W / 2 L (one forced pair each way) |
| Top over/under | Atlanta TT Over 88.5 (Rank #2) — **WIN** | Under 176.5 (Rank #2) — **LOSS**, `TOP_OU_REVIEW` fired and the enhanced review is above |
| Winner call | **WIN** — Atlanta, p ≈ 0.873 | — |

**Forced-pair caveat.** Both supplied pairs (-15.5 / +15.5 and Over / Under 176.5) are strict complements, so the supplied "2 W / 2 L" is mechanically fixed and carries no information. The informative content of the supplied slate is exactly two decisions: prefer Atlanta -15.5 (0.551, **W**) and prefer Under 176.5 (0.516, **L**) — 1 W / 1 L at probabilities barely above a coin flip. The model-selected slate is where the signal is: four free targets at 0.719–0.873, all four won.

**Mandatory validation questions.**

1. **Confirmed starting fives?** **NO.** The card carried `CONFIRMED_STARTING_FIVES_NOT_RECOVERED_TO_GATE_STANDARD` and capped participant-sensitive confidence accordingly. Correct handling. Post-hoc, the projected Atlanta five was exact.
2. **Bench / rotation information?** **PARTIALLY.** The available-core lists for both teams were recovered and were accurate. Depth quality was not modelled — and Atlanta's bench produced Borlase 18 and Paopao 5 in 36 combined minutes, which is precisely what beat the full-game Under.
3. **Coaching information?** **NOT OBTAINED.** The material coaching variable here was starter-minute management in a blowout (Reese 28 min, Gray 28, Canada 27 — never fully rested). That is knowable only as a tendency, not as a fact, and the card did carry a "blowout slowdown / bench compression" scenario at weight 0.18.
4. **Injuries / availability changes checked?** **YES, but the decisive row was left unresolved.** Season-ending absences (Diggins, Jackson, Brionna Jones) and the Stevens / Carrington absences were all correct. Natasha Cloud's final status was not recovered pre-tip — `CLOUD_FINAL_ACTIVE/INACTIVE_STATUS_NOT_RECOVERED_PRETIP_TO_FIELD_OWNER_STANDARD`. She was out.
5. **Were the original sources accurate and current?** **MOSTLY YES.** The WNBA official injury page did not expose its dynamic rows through the accessible route, which is the root cause of question 4. An Athlon 2:00 PM EDT injury report was used as a current independent secondary, was correct on every row it covered, and was correctly not promoted to field-owner status.
6. **Better sources available?** **YES, and concrete.** The ESPN WNBA `summary?event=` endpoint returns a per-player `starter` boolean and a `didNotPlay` flag. Post-game it settles the participation question definitively; pre-game the same endpoint exposes a `rosters` block once inactives are posted. It should be added to the WNBA settlement route and tested as a pre-tip availability route, because the official WNBA injury page is JS-rendered and has now failed this lane twice.
7. **Blind spots?** **YES — one, and the card half-saw it.** The favourite's bench offensive efficiency after separation. The card explicitly warned that "a depleted underdog does not automatically make the full game Under; Atlanta's own ceiling could consume the budget" — that warning describes exactly what happened — but the ranking then still preferred Under 176.5 while simultaneously assigning Atlanta team-total Over 88.5 a 77% probability. Those two statements are in tension and the tension was never reconciled numerically.
8. **How should this be handled in future?** Before a full-game Under can be ranked as the preferred total in a mismatch, print the implied joint budget: P(favourite team total ≥ x) against P(underdog team total ≤ total − x) in the same frozen states. If the favourite's own team-total Over is already high-confidence, the full-game Under must be labelled LOW evidence unless the underdog floor is demonstrably low in those same states. `RULES_BASKETBALL` controls 11, 17 and 18 and `PF-10` (distribution-first) already require this; the failure is execution, not absence — recurring-mistake **M15** (control listed, not executed) and **M14** (total probability not reconciled with the card's own centre and width in the ranking narrative).

**Verdict on this event.** The strongest call on the card — Atlanta to win, and to win comfortably — was right, all four free targets won, and the single loss was a 0.516 near-coin-flip the card had already labelled `CLOSE TO PROJECTION / WEAK MAIN-TOTAL EDGE`. The honest reading is that the labelling was right and the ordering was fragile, not that the total model is broken. No new rule; execution reinforcement only.

---


### P-476 — MLB — Minnesota Twins @ Los Angeles Angels

- Canonical / staging ID: P-476

- Competition: MLB 2026 regular season

- Venue: Angel Stadium, Anaheim, California, United States

- Venue timezone: America/Los_Angeles

- Official venue-local start: Sep 19, 2026 at 6:38 PM PDT

- Australia/Melbourne conversion: Sep 20, 2026 at 11:38 AM AEST; calendar-date rollover = YES

- Research cutoff / independent distribution freeze: Sep 20, 2026 at 11:29:34 AM AEST

- Issuance state: PREGAME / SCHEDULED at freeze.

- Method / controls: MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-BASEBALL

- Operating mode: SPORTS_ONLY / MARKET_BLIND

- Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE

- Preflight: PASS, zero blocking findings. Source count/lineage, field-owner mix, timezone conversion, current event state, source firewall, line quarantine and freeze order all passed.

- Distribution ID: P-476-dist-v1

- Distribution SHA-256: 780302c06f545698c2e893258d8e928cc4ed9a601d0876cf2cb749c654e23d57

- No retrospective performed.

#### Identity / supplied contracts

The user-supplied contracts were parsed for identity and quarantined from predictive construction until after the independent joint run distribution was frozen:

- Los Angeles Angels ML

- Minnesota Twins +1.5 runs

- Full-game Over 7.0 runs

- Full-game Under 7.0 runs

Research endpoint assumes a normally completed MLB regular-season game including extra innings. Exact operator-specific listed-pitcher, suspension, shortening, action and void terms were not supplied, so operator action is not asserted.

The integer 7.0 total is push-capable. Over / Push / Under are therefore reported as a three-state probability set; Over and Under are not falsely forced to sum to 100%.

#### Official starters / posted lineups

Official starter handshake:

- Minnesota: Joe Ryan, RHP — 6-10, 3.84 ERA, 146 SO.

- Los Angeles: Reid Detmers, LHP — 6-8, 3.36 ERA, 199 SO.

The current MLB all-club starting-lineup index recovered complete posted orders:

Minnesota — Luke Keaschall RF; Austin Martin LF; Ryan Jeffers C; Josh Bell DH; Brooks Lee 3B; Royce Lewis 2B; Victor Caratini 1B; Walker Jenkins CF; Ryan Kreidler SS.

Los Angeles — Zach Neto SS; Mike Trout DH; Wade Meckler LF; Vaughn Grissom 2B; Moisés Ballesteros 1B; Denzer Guzman 3B; Josh Lowe RF; Jose Siri CF; Tyler Heineman C.

Retrieval note: team-specific MLB lineup subpages still rendered this matchup as TBD while MLB's current all-club lineup index exposed the full orders. The full orders are retained as the newest field-owner index view, while the intra-MLB cache inconsistency is recorded rather than hidden.

#### Availability / roster state

Minnesota:

- Byron Buxton — OUT, right hip; underwent hip labrum repair on Sep. 18 and expected back in 2027.

- Trevor Larnach — 10-day IL, left wrist sprain.

- Kaelen Culpepper — 10-day IL, left hamstring strain.

- Joe Ryan was activated Sep. 7 after a left glute strain.

- Royce Lewis is in the posted lineup after the recent shoulder-soreness episode, so he is treated as available rather than carrying forward an obsolete absence flag.

Los Angeles:

- Kyren Paris — 10-day IL, right index-finger fracture; expected 2027.

- Nolan Schanuel — right intercostal strain, expected 2027 after rehab irritation.

- Samy Natera Jr. — 15-day IL, left forearm inflammation.

- Sam Bachman was activated Sep. 16.

- Mike Trout, Zach Neto, Josh Lowe and the currently posted starting position-player group are treated as available.

Both offences are therefore below ideal full-season roster strength. Minnesota is missing Buxton/Larnach/Culpepper; Los Angeles is missing Schanuel/Paris. No one-sided injury multiplier was applied.

#### Starter process

Joe Ryan:

- Underlying 2026 Statcast snapshot: 27.1% K, 5.0% BB, .289 xwOBA, 3.46 xERA.

- Contact-tail warning: 11.1% barrel rate and 42.6% hard-hit rate in that snapshot.

- Returned from the glute IL on Sep. 7.

- Latest start versus Cleveland: 4.0 IP, 4 ER, 84 pitches; his first MLB start back was also only four innings.

- Current modelling therefore separates Ryan's per-batter skill from his length/hook distribution. A central Ryan branch does not assume six-plus innings simply from his season reputation.

- Career matchup context: official MLB preview states Ryan is 2-0 with a 3.10 ERA and 41 K in five career starts versus the Angels. This remains weak contextual evidence and does not override current workload state.

Reid Detmers:

- Current official line: 3.36 ERA, 199 K.

- Latest start: 6.0 IP, 3 ER, 8 K versus Seattle.

- That was his seventh consecutive quality start, supporting a materially longer central exposure than Ryan's current post-IL branch.

- 2026 Statcast snapshot: 28.3% K, 7.4% BB, .290 xwOBA, 3.48 xERA, 8.7% barrel rate.

- Pitch mix snapshot: roughly 45% four-seam and 32% slider, with curve/change secondary usage.

Starter comparison: Detmers has the stronger current length/form branch; Ryan retains strong underlying strikeout/control indicators but has a meaningful short-start and hard-contact tail. This produces only a modest Angels winner lean, not a large separation.

#### Bullpen transition / workload

Minnesota's preceding Sep. 18 game:

- Connor Prielipp worked seven innings.

- Tommy Nance handled the eighth and escaped a bases-loaded, no-out jam.

- Travis Adams worked a clean ninth for the save.

- Nance had also worked the 13th inning on Sep. 16; Adams had appeared in that extra-inning game as well. Their recent use is treated as a modest availability/workload consideration, not a quality penalty.

- Jeff Hoffman was not required in the Sep. 18 shutout and remains part of the late-leverage path.

Los Angeles's preceding Sep. 18 game:

- Grayson Rodriguez worked 6 2/3 innings.

- Sammy Peralta covered the transition and Luke Murphy pitched the ninth.

- Ben Joyce, Tayler Saucedo and Blake Weiman were not all forced back into the Sep. 18 game after the Sep. 17 ten-inning contest; the late bullpen therefore has a better-rested branch than if the prior game had been a short-start bullpen game.

- Ben Joyce had allowed the tying two-run Walker Jenkins homer on Sep. 17, which is retained as a realised tail, not converted into an automatic negative performance adjustment.

#### Current offensive diagnostics

Recent results are descriptive only; they do not mechanically shift the model without a current mechanism.

- Minnesota last 30 days: 4.12 R/G, .231/.299/.388.

- Minnesota Sep. 5-19 window: 3.08 R/G, lowest in the cited current MLB-team comparison; the roster has also lost Buxton and Larnach.

- Los Angeles last 30 days: 3.96 R/G, .227/.303/.350.

- Los Angeles latest 15-day window: 3.43 R/G.

- Current series: Angels won 5-4 in 10 innings on Sep. 17; Twins won 3-0 on Sep. 18. These outcomes widen the plausible branches but do not become predictive coefficients.

#### Environment

National Weather Service Anaheim hourly forecast around first pitch:

- about 78°F at 6 PM PDT, falling toward 74°F at 7 PM;

- dewpoint around 64°F;

- southwest wind roughly 7 mph;

- 0% precipitation in the relevant evening window.

No audited park-orientation transform was recovered that justifies assigning the wind a signed run effect, so weather is treated as benign/low-disruption rather than as an Over or Under coefficient.

#### Frozen independent joint run distribution

Model: explicit UNVALIDATED_SUBJECTIVE scenario mixture. Regulation team runs use independent Poisson kernels within each scenario; ties then enter a separately declared MLB automatic-runner extra-inning branch. This is not a fitted, calibrated or prospectively validated model.

1\. Central starter control — weight 0.34 — MIN 3.2, LAA 3.6.

2\. Detmers suppression / Ryan stable — weight 0.22 — MIN 2.4, LAA 3.3.

3\. Ryan short / Angels relief-transition attack — weight 0.18 — MIN 3.2, LAA 4.8.

4\. Twins power/contact cluster — weight 0.14 — MIN 5.0, LAA 3.4.

5\. Bullpen / HR cluster — weight 0.12 — MIN 4.7, LAA 5.0.

Frozen centre:

- Minnesota runs: 3.456

- Los Angeles runs: 3.890

- PROJECTED TOTAL: 7.346

- PROJECTED ANGELS MARGIN: +0.434

- Regulation total SD: about 2.99 runs

- Regulation margin SD: about 2.87 runs

- Representative score family: Angels 4-3 / Twins 4-3

- Regulation state: MIN win \~36.3%; tie \~14.25%; LAA win \~49.45%.

- Eventual Angels winner branch after explicit extras assumption: \~56.9%.

Extra-inning assumptions are scenario parameters, not empirical calibration:

- Angels win 52% of regulation-tie states.

- Twins +1.5 covers 90% of regulation-tie extra-inning branches.

- Exact total-7 treatment explicitly reallocates low tied scores into eventual Over/Push/Under states rather than pretending extra innings do not exist.

#### Mandatory total projection / 7.0 push audit

PROJECTED TOTAL: 7.346

SUPPLIED TOTAL: 7.0

RAW GAP: +0.346 runs

REGULATION TOTAL SD: \~2.99

NORMALIZED GAP: \~+0.12 SD

ASSESSMENT: CLOSE TO PROJECTION / WEAK MAIN-TOTAL EDGE.

Full-game research probabilities after the explicit extra-inning branch:

- OVER 7.0: \~46.6% WIN

- EXACTLY 7: \~15.9% PUSH

- UNDER 7.0: \~37.5% WIN

Conditional on a non-push:

- Over q ≈ 55.4%

- Under q ≈ 44.6%

The preferred supplied total side is therefore Over 7.0, but it is not a strong total call. The large push mass is why neither total direction belongs near the top of the overall supplied ranking by unconditional win probability.

Team-score budget:

- MIN 2-3 + LAA 3-4 produces 5-7 and is Under/Push territory.

- MIN 3-4 + LAA 4 produces 7-8 and straddles the target.

- Ryan-short states with LAA 5 plus ordinary MIN 3-4 clear the total.

- Detmers suppression plus weak Angels conversion can produce 2-3 / 3-3 regulation states.

- A 3-3 regulation tie is especially important: the automatic runner can convert what was an Under through nine into a final Push or Over.

#### Supplied-slate ranking

1\. MINNESOTA TWINS +1.5 — \~63.4% UNVALIDATED_SUBJECTIVE.

   Decomposition: every Minnesota win covers, every Angels one-run win covers, and most tied-regulation extra-inning decisions still finish within one run.

   Main failure: Ryan's short-start/contact tail plus a multi-run Angels sequence produces a 2+ Los Angeles win.

2\. LOS ANGELES ANGELS ML — \~56.9%.

   Why: Detmers owns the stronger current length/form branch; Minnesota's offence is missing Buxton/Larnach and has been weak in the latest current-regime window; Ryan's post-IL outings have both been short.

   Main failure: Ryan's underlying K/BB skill reasserts, Walker Jenkins/Keaschall/Jeffers generate enough damage against Detmers, and the stronger Minnesota overall season profile wins a close game.

3\. OVER 7.0 — \~46.6% win / \~15.9% push / \~37.5% loss; q(non-push) \~55.4%.

   Why preferred to Under: independent centre is 7.35 and Ryan's length/contact tail plus the MLB extra-inning branch supply plausible 5-3 / 4-4-to-extras states.

   Why not high-ranked: the target is only 0.12 SD below the centre and both offences have current suppression mechanisms.

4\. UNDER 7.0 — \~37.5% win / \~15.9% push / \~46.6% loss; q(non-push) \~44.6%.

   Why live: Detmers' seven-QS run, Ryan's underlying skill and both offences' current scoring weakness create genuine 3-2 / 4-2 / 3-3 regulation states.

   Why last: a push is not a win under the ranking objective, and the frozen centre sits slightly above seven.

Supplied-line dependence:

- Angels ML and Twins +1.5 are not independent and can both win when Los Angeles wins by exactly one run.

- They cannot both lose in a normally actioned completed game: a Twins win cashes +1.5, while an Angels 2+ win cashes Angels ML.

- Approximate overlap is the Angels one-run-win state, including extra-inning one-run decisions; the model places material mass there.

- Over 7.0 and Under 7.0 are push-capable opposites, not binary complements.

#### Best four model-selected targets

Candidate-slate discipline: to avoid trivially inflating hit probability by choosing arbitrarily wide alternates, self-selected lines are limited to nearby/common thresholds around the user's requested markets plus one exposure-linked pitcher threshold. Operator availability is not asserted.

1\. REID DETMERS 5+ STRIKEOUTS — \~82% UNVALIDATED_SUBJECTIVE.

   Exposure chain: seven consecutive quality starts support roughly 21-27 batter central exposure; 2026 Statcast K% snapshot is 28.3%; latest start produced eight strikeouts in six innings.

   Main failure: early contact/traffic forces a short outing or Minnesota suppresses two-strike conversion.

2\. MINNESOTA TWINS +2.5 — \~76-77%.

   Why: the joint margin distribution is centred near Angels +0.43; this survives Minnesota wins plus one- and two-run Angels wins and is much more robust to the Ryan-short branch than +1.5.

   Main failure: Angels separation through Ryan's early exit followed by middle-relief damage.

3\. MINNESOTA TEAM TOTAL UNDER 4.5 — \~70%.

   Why: independent MIN centre is 3.46; Detmers' current length plus strikeout profile and Minnesota's depleted/low-scoring current regime support a four-or-fewer central outcome.

   Main failure: Detmers' home-run/contact variance or late Angels bullpen leakage after a competitive start.

4\. FULL-GAME UNDER 8.5 — \~63-64%.

   Why: 8.5 sits materially above the 7.35 independent centre and protects against the exact-7 push issue.

   Main failure: Ryan exits early and both middle-relief groups encounter an HR/sequence cluster; extra innings also erode Under protection in tied high-regulation states.

The model-selected slate is not independent: Detmers 5+ K, Minnesota TT Under 4.5 and Under 8.5 share a Detmers-control / Minnesota-suppression driver.

Top-two model dependence cannot be honestly assigned a single joint probability from the current joint score object because the Detmers strikeout module is exposure-linked but not fully coupled to the team-score simulator. Valid Fréchet bounds for Detmers 5+ K (\~82%) and Twins +2.5 (\~76-77%) put joint success roughly between 59% and 77%; JOINT_UNQUANTIFIED beyond those bounds.

#### Potential game winner

LOS ANGELES ANGELS — \~56.9% eventual-win estimate.

This is a modest lean, not a strong winner call. Twins +1.5 ranks above Angels ML because a low-scoring close game creates a broad overlap region in which Los Angeles wins by one and both contracts succeed.

#### Integrity flags

- PREGAME / SCHEDULED AT FREEZE

- PREFLIGHT PASS / ZERO BLOCKS

- MLB_ALL_CLUB_LINEUP_INDEX_POSTED_ORDERS; TEAM_SPECIFIC_LINEUP_CACHE_TBD

- EXACT_OPERATOR_LISTED_PITCHER/ACTION/VOID TERMS UNKNOWN

- UNVALIDATED_SUBJECTIVE_DISTRIBUTION

- INTEGER_TOTAL_PUSH_EXPLICIT

- MARKET ODDS / IMPLIED PROBABILITY / LINE MOVEMENT / SPORTSBOOK PREVIEWS / TIPSTERS / FANTASY-DFS EXCLUDED

- Original issue status: UNSETTLED — PREGAME FORECAST / NO RETROSPECTIVE

#### Sources / provenance

1\. MLB Probable Pitchers — exact event, venue, scheduled time, Ryan/Detmers identities and current headline stats — PRIMARY FIELD OWNER — https://www.mlb.com/probable-pitchers

2\. MLB Starting Lineups — current all-club posted batting orders — PRIMARY FIELD OWNER — https://www.mlb.com/starting-lineups

3\. MLB Twins/Angels probable-pitcher pages — team-side exact-event corroboration — PRIMARY TEAM/FIELD OWNER.

4\. MLB Twins injury/transaction records — Buxton, Larnach, Culpepper and Ryan availability — PRIMARY TEAM/FIELD OWNER.

5\. MLB Angels injury/transaction records — Paris, Schanuel, Natera and Bachman availability — PRIMARY TEAM/FIELD OWNER.

6\. MLB Joe Ryan Sep. 13 report / film record — 4.0 IP, 4 ER, 84 pitches and current post-IL workload context — PRIMARY FIELD OWNER.

7\. MLB Reid Detmers Sep. 14 film record — 6.0 IP, 3 ER, 8 K and seventh straight quality start — PRIMARY FIELD OWNER.

8\. Baseball Savant / MLB — Ryan and Detmers Statcast xwOBA/xERA/K/BB/contact and arsenal snapshots — PRIMARY MLB TRACKING SOURCE.

9\. Reuters / Field Level Media — Detmers latest start and current series/game context — HIGH-QUALITY INDEPENDENT.

10\. AP / StatMuse exact Sep. 18 game record — bullpen transition and preceding-game usage cross-check — INDEPENDENT SECONDARY / structured diagnostic.

11\. StatMuse / Retrosheet — current L14/L15/L30 scoring diagnostics — INDEPENDENT STRUCTURED DIAGNOSTIC.

12\. National Weather Service — venue-area hourly temperature, dewpoint, wind and precipitation — GOVERNMENT FIELD OWNER.

13\. Sports Research Drive — METHOD.md, RULES_BASEBALL.md, RULES_GENERAL.md, UPCOMING_GAME_RESEARCH_GUIDE.md, DATA_SOURCE_REGISTER.md, CONTROL_MANIFEST_2026-09-19.md and forecast preflight validator — GOVERNING METHODOLOGY.

Source firewall: no sportsbook odds, market consensus, implied probabilities, line movement, betting previews/picks, tipsters, fantasy/DFS projections or ownership data were admitted as predictive inputs. User-supplied contracts were queried only after the independent distribution was frozen and hashed.

#### Document mapping / candidate learnings

- Ryan's post-IL skill and current starter length must remain separate exposure dimensions -\> existing RULES_BASEBALL starter-BF/pitch-count/hook control.

- Exact 7.0 produces material push mass -\> current SCORING_AND_VALIDATION push-capable W/P/L requirement; no new rule needed.

- Full MLB lineup index versus lagging team-specific TBD cache -\> DATA_SOURCE_REGISTER retrieval/latency observation only.

- Detmers current length plus Twins roster depletion supports a suppression branch, but Ryan hard-contact/short-start and MLB extras preserve an upper tail -\> existing cluster, relief-transition and extras controls; no fixed coefficient added.

---

#### Settlement and retrospective — P-476

Settlement status: SETTLED / RETROSPECTIVE COMPLETE.

Verified final: Los Angeles Angels 6, Minnesota Twins 5 in 11 innings.

Actual full-game total: 11 runs.

Actual margin: Angels +1.

Three-source final-state gate: PASS.

- Reuters / Field Level Media: explicit Angels 6-5 final in 11 innings.

- CBS/AP exact-game recap/box score: explicit 6-5 final and 11-inning pitching/stat record.

- Independent local/secondary game recap corroboration plus MLB event video/stat records for pitcher-specific settlement.

Settlement sources:

- Reuters final recap: https://www.reuters.com/sports/baseball/angels-rally-ninth-take-down-twins-11th--flm-2026-09-20/

- CBS Sports exact-game recap / box score, Sep 19, 2026.

- MLB Joe Ryan game video: https://www.mlb.com/video/joe-ryan-strikes-out-five-x4706

- MLB scores/event record, Sep 19, 2026.

##### Pick-by-pick settlement — supplied slate

1\. Twins +1.5 — WIN; Minnesota lost by one.

2\. Angels ML — WIN.

3\. Over 7.0 — WIN; final total 11.

4\. Under 7.0 — LOSS.

Potential game winner: Los Angeles Angels — WIN.

##### Pick-by-pick settlement — model-selected slate

1\. Reid Detmers 5+ strikeouts — WIN, exactly 5 strikeouts in 5.0 innings.

2\. Twins +2.5 — WIN.

3\. Minnesota team total Under 4.5 — LOSS; Minnesota scored 5.

4\. Full-game Under 8.5 — LOSS; final total 11.

##### Ranking / top-two review

Supplied Rank #1 Twins +1.5 and Rank #2 Angels ML both won. This is the precise overlap state described pre-game: Los Angeles won by exactly one run, so both contracts succeeded. Hit@2 = YES; both-win = YES; the dependence logic was correct and important.

Model-selected Rank #1 Detmers 5+ K won exactly at the threshold, and Rank #2 Twins +2.5 also won.

No Rank-1 failure trigger applies.

##### Enhanced totals review

The supplied Over 7.0 won, but the self-selected Under 8.5 lost. Because the card contained competing total targets across separate slates, the Under 8.5 miss is reviewed to the enhanced standard rather than ignored.

Why Under 8.5 was selected:

- Independent centre was 7.346.

- Detmers' current length/strikeout form plus Minnesota roster depletion supported suppression.

- 8.5 appeared to provide a meaningful cushion above the centre.

Why it failed:

- Minnesota had already built a 5-2 lead entering the bottom of the eighth.

- Adam Frazier's two-run pinch-hit double cut it to 5-4.

- Vaughn Grissom's ninth-inning solo homer tied the game 5-5.

- The game then entered MLB automatic-runner extra innings and Christian Moore drove in the winning run in the 11th, producing the 6-5 final.

- Thus the late relief-transition + tie + extra-inning branch added four runs after the game stood at seven through seven innings.

The supplied Over 7.0 benefited from exactly the extra-inning/late-cluster mechanism that the pre-game card explicitly preserved. The self-selected Under 8.5 did not leave enough room for that same tail.

Pitcher reality:

- Joe Ryan: 5 innings, 2 runs, 5 strikeouts.

- Reid Detmers: 5 innings, 4 runs, 5 strikeouts.

Ryan did not realize the forecast's most damaging short-start branch. Detmers also failed to produce the central six-plus-inning quality-start suppression branch, though his 5+ K prop still landed exactly.

Could Under 8.5 have been ranked lower ex ante?

Yes, relative to the supplied Over 7.0, because the same joint object carried \~14% regulation-tie mass and explicitly acknowledged automatic-runner scoring. An Under above the centre can still be reasonable, but the card should not let the central 7.35 estimate dominate the tie/late-bullpen tail when selecting a nearby 8.5 threshold.

Smallest justified improvement:

For MLB self-selected Unders, explicitly report the probability mass of tie-after-nine and late relief-transition states that can cross the alternate threshold, not merely the distance from the central total. This is already required conceptually by BB-B5 and BB-B7; the issue is execution, not a new fixed penalty.

##### What went right

- Angels winner was correct.

- Twins +1.5 correctly captured the close-game distribution.

- The exact one-run Angels win validated the non-independence explanation for the top two supplied picks.

- Over 7.0 was correctly preferred to Under 7.0.

- Detmers 5+ strikeouts won exactly.

- The pre-game analysis explicitly warned that a 3-3 or other tied regulation state could turn an Under/Push into an Over through automatic-runner extras; the realised game followed that general late/extras mechanism.

##### What went wrong

- Minnesota scored 5, defeating the Minnesota TT Under 4.5.

- Detmers allowed four runs in five innings, so the Detmers-suppression branch was too strong relative to his realised run prevention.

- Under 8.5 understated late bullpen/extras scoring despite the model already identifying those states.

- The game did not require Ryan's early-collapse branch to reach 11 runs; late-game scoring was enough.

##### Availability / lineup / source audit

The pre-game card recovered MLB's all-club posted orders but recorded an intra-MLB cache inconsistency on team-specific lineup pages. That uncertainty was transparently logged rather than hidden. No material postgame evidence shows that an unmodelled late scratch was the central cause of the miss; the dominant mechanism was late relief/extras.

For Detmers 5+ K, CBS box-score data records 5.0 IP and 5 strikeouts, so the prop settles as a WIN.

##### Source audit

- Reuters: retained as high-quality independent game-script/final source.

- CBS/AP: retained for final and detailed box score.

- MLB official event/player video: retained as field-owner pitcher-event corroboration.

- Search snippets or stale live feeds are not used to override the explicit final sources.

##### Blind spots and mitigation

Blind spot: underweighting late relief + automatic-runner extras when selecting Under 8.5.

Pre-game knowability: YES as a structural tail, but not its exact realization.

Materiality: HIGH for Under 8.5 and MIN TT Under 4.5; LOW for winner/+run-line selections.

Mitigation: display the tie-after-nine and late-relief threshold-crossing mass before ranking a nearby alternate Under.

##### Document mapping

- RULES_BASEBALL.md — BB-B5 relief transition and BB-B7 extras already cover the failure mechanism; execution reminder only.

- SCORING_AND_VALIDATION.md — preserve push-aware 7.0 handling; the supplied Over correctly won outright rather than pushing.

- DATA_SOURCE_REGISTER.md — retain MLB all-club versus team-page lineup-cache latency observation.

- Prediction log — record the exact one-run top-two overlap success and Under 8.5 extras-tail miss.

---

#### 2026-09-21 independent re-audit — P-476

**Re-verification of the settled final.** Re-checked at the MLB Stats API, a structured field-owner lineage not used in the original settlement pass (which relied on Reuters / Field Level Media, CBS/AP and MLB video).

- `statsapi.mlb.com/api/v1/schedule?sportId=1&date=2026-09-19`, gamePk **823976**: status `Final`, Minnesota Twins 5 @ Los Angeles Angels 6.
- Official linescore: **11 innings played** (scheduled 9). Minnesota by inning 0-0-2-1-1-0-0-1-0-0-0 = 5 (11 hits, 1 error); Los Angeles 0-0-0-2-0-0-0-2-1-0-1 = 6 (11 hits, 0 errors, 15 left on base).
- Official boxscore: **Joe Ryan 5.0 IP, 2 R / 2 ER, 5 K**; **Reid Detmers 5.0 IP, 4 R / 4 ER, 5 K**.

Every settled row is unchanged. **Final total 11; margin Angels +1 in 11 innings.**

The linescore independently confirms the retrospective's game script to the inning: Minnesota led **5-2** entering the bottom of the eighth, the Angels scored 2 in the eighth (5-4), 1 in the ninth (5-5) and 1 in the eleventh (6-5). The claim that the game stood at seven runs through seven innings is exact — 4 + 3 = 7 after seven.

**Detmers 5+ strikeouts settles WIN at exactly the threshold**, now confirmed at the field owner rather than at a box-score aggregator. One strikeout fewer would have flipped it; that fragility belongs beside the win rather than being read as a validated exposure model.

**Ranking metrics.**

| Metric | Supplied slate | Model-selected slate |
|---|---|---|
| Rank-1 | **WIN** (Twins +1.5) | **WIN** (Detmers 5+ K) |
| Hit@2 | **YES** | **YES** |
| Wins@2 | **2 / 2** | **2 / 2** |
| NDCG@2 | **1.000** | **1.000** |
| Row record | 3 W / 1 L | 2 W / 2 L |
| Top over/under | Over 7.0 (Rank #3) — **WIN** | Full-game Under 8.5 (Rank #4) — **LOSS** |
| Winner call | **WIN** — Angels, p ≈ 0.569 | — |

**Push-capable scoring, done properly.** Over 7.0 was frozen as a three-state target, W/P/L = 0.466 / 0.159 / 0.375, and the realised outcome was a WIN. Complete W/P/L Brier = **0.2255**; decisive q = 0.466 / (1 − 0.159) = **0.5541**, decisive binary Brier = **0.1988**. Reporting only the decisive score would overstate the card, because the 15.9% push mass was real and was correctly disclosed. This is the best-executed piece of contract geometry in the mini log.

**The top-two overlap logic is the standout result.** The card ranked Twins +1.5 (0.634) above Angels ML (0.569) and said why: both rows win when Los Angeles wins by exactly one run, and the joint model put material mass on that state. Los Angeles won by exactly one run. The mechanism was named before the event and then occurred — that is a validated piece of reasoning, not a favourable-looking coincidence.

**Mandatory validation questions.**

1. **Confirmed starting lineups?** **YES — both, in full.** The MLB all-club starting-lineups index returned complete nine-man posted orders for both teams. This is the only card in the mini log that cleared the lineup gate outright, and it is also the only card that passed preflight with zero blocking findings. That co-occurrence is worth noting: the card issued earliest relative to first pitch was also the card with the best evidence.
2. **Bench / bullpen state?** **YES.** Both bullpens were reconstructed from the preceding Sep 18 game with named-arm workload (Prielipp 7 IP, Nance, Adams for Minnesota; Rodriguez 6⅔, Peralta, Murphy for Los Angeles), and the extra-inning Sep 16/17 usage was carried forward as an availability constraint. Correct treatment — workload informed availability, not quality.
3. **Coaching information?** **NOT OBTAINED, not material.**
4. **Injuries / availability?** **YES, and correctly current.** Buxton (hip labrum repair, Sep 18), Larnach and Culpepper for Minnesota; Paris, Schanuel and Natera for Los Angeles; Bachman activated Sep 16; Ryan activated Sep 7. Critically, the card **removed an obsolete absence flag** on Royce Lewis because he appeared in the posted order. That is the correct direction of error-correction, and the exact opposite of the P-480 failure below.
5. **Were the original sources accurate and current?** **YES**, with one disclosed inconsistency: MLB's team-specific lineup subpages still rendered TBD while the all-club index exposed full orders. The card recorded the inconsistency instead of hiding it.
6. **Better sources available?** **Marginally.** `game/{pk}/linescore` and `game/{pk}/boxscore` should be the first settlement route rather than Reuters/CBS recaps — they settle innings played, team totals, margins and pitcher lines in two calls with no narrative interpretation. Same upgrade as recommended for P-474.
7. **Blind spots?** **YES — one, and it is the card's own stated tail.** Under 8.5 was selected as a self-chosen alternate sitting 1.15 runs above the 7.346 centre, while the same frozen object carried about 14.25% tie-after-nine mass plus an explicit automatic-runner branch. The card described the mechanism that beat it and then chose a threshold that could not survive it.
8. **How should this be handled in future?** For any MLB alternate Under, print P(tie after nine) + P(late relief-transition crossing) against the chosen threshold, not merely the distance from the central total. `RULES_BASEBALL` BB-B5 and BB-B7 already require both states; the card had them as prose rather than as a threshold-crossing calculation. **M14 / M15 again.**

**Verdict on this event.** Process-best card of the mini log: preflight PASS, both lineups confirmed, push mass handled honestly, dependence between the top two stated in advance and then realised. The only defect is the self-selected Under 8.5, beaten by a tail the card itself had documented.

---


### P-477 — Australia NBL — Sydney Kings vs Cairns Taipans

- Canonical / staging ID: P-477

- Competition: Australia NBL27, Round 1

- Venue: Afterpay Arena, Sydney Olympic Park, New South Wales, Australia

- Official scheduled start: Sep 20, 2026 at 5:00 PM AEST

- Original research state: PREGAME / SCHEDULED at final pre-issue refresh

- Method / controls: MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-BASKETBALL

- Operating mode: SPORTS_ONLY / MARKET_BLIND

- Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE

- No retrospective performed.

#### Original pre-game prediction

Independent frozen centre:

- Sydney Kings: approximately 97 points

- Cairns Taipans: approximately 90 points

- PROJECTED TOTAL: approximately 186.7

- PROJECTED SYDNEY MARGIN: approximately +7.2

- Representative score: Sydney 97-90 Cairns

Best four model-selected targets:

1\. SYDNEY KINGS ML — \~70% UNVALIDATED_SUBJECTIVE.

2\. OVER 179.5 TOTAL POINTS — \~69%.

3\. UNDER 191.5 TOTAL POINTS — \~63%.

4\. CAIRNS TAIPANS +11.5 — \~61%.

Supplied-slate ranking:

1\. OVER 185.5 — \~53.3%.

2\. CAIRNS +8.5 — \~52.9%.

3\. SYDNEY -8.5 — \~47.1%.

4\. UNDER 185.5 — \~46.7%.

Potential game winner:

SYDNEY KINGS — \~70%.

#### Original research reasoning / availability

- Sydney retained a championship-level core led by Kendric Davis, Matthew Dellavedova, Torrey Craig and Xavier Cooks, with Andrew Carr added to the frontcourt.

- Davis had a shortened preparation because passport issues delayed his return to Australia; availability was not treated as equivalent to perfect opening-night rhythm.

- Cairns' current roster was treated as materially stronger offensively than the prior-season team, with Jack McVeigh, Keanu Pinder, Jaylon Brown, Reyne Smith and Malique Lewis providing multiple scoring paths.

- Confirmed absences at issue: Sydney — Keli Leaupepe; Cairns — Jaylin Galloway and Luke Paul.

- Expected/projected starting fives were retrieved, but a formal final confirmed starting five for both clubs was not recovered to gate standard before issue. Rotation-sensitive player props were therefore not promoted.

- The supplied -8.5 and 185.5 thresholds were close to the independent centre, so the winner and nearby alternate thresholds were considered more robust.

#### Material pre-game sources

1\. NBL exact-game preview / talking points — event identity, expected depth charts and current team context — PRIMARY LEAGUE — https://league.nbl.com.au/news/how-to-watch-talking-points-sydney-v-cairns-fnm29

2\. NBL / Cairns club schedule — exact event/date/time — PRIMARY LEAGUE — https://www.nbl.com.au/club-schedule/cairns

3\. Sydney Kings club schedule / team material — schedule and roster context — PRIMARY TEAM — https://www.nbl.com.au/club-schedule/syd

4\. Cairns Taipans injury report — Jaylin Galloway and Luke Paul availability — PRIMARY TEAM — https://www.taipans.com/news/injury-report-round-1-nbl27

5\. NBL team/statistical and preseason reports — current roster/process context and Cairns final preseason scoring — PRIMARY LEAGUE.

6\. Sydney Kings official preseason reporting — current rotation/process context — PRIMARY TEAM.

7\. Sports Research Drive — METHOD.md, RULES_BASKETBALL.md, RULES_GENERAL.md, CONTROLS.md, DATA_SOURCE_REGISTER.md and current control manifest — GOVERNING METHODOLOGY.

Source firewall: sportsbook odds, betting picks, prediction markets, line movement, fantasy/DFS projections and betting-derived analysis were excluded from predictive inputs.

#### Settlement and retrospective — P-477

Settlement status: SETTLED / RETROSPECTIVE COMPLETE.

Verified final: Sydney Kings 111, Cairns Taipans 90.

Actual full-game total: 201 points.

Actual margin: Sydney +21.

Three-source terminal-state gate: PASS.

1\. NBL / AAP postgame report — explicit Sydney 111-90 Cairns final, quarter-by-quarter scoring and player statistics — PRIMARY LEAGUE / INDEPENDENT AAP REPORTING — https://league.nbl.com.au/news/kings-open-title-defence-in-style

2\. Cairns Taipans official postgame report — explicit 111-90 defeat plus game script and player statistics — PRIMARY TEAM — https://www.taipans.com/news/pinder-stars-but-taipans-fall-to-kings

3\. Austadiums exact-event record — explicit 111-90 Final, Sep 20 2026, 5:00 PM at Afterpay Arena — INDEPENDENT EVENT RECORD — https://www.austadiums.com/sport/event/34482

##### Pick-by-pick settlement — model-selected slate

1\. Sydney Kings ML — WIN.

2\. Over 179.5 total points — WIN; actual total 201.

3\. Under 191.5 total points — LOSS; actual total 201.

4\. Cairns Taipans +11.5 — LOSS; Cairns lost by 21.

##### Pick-by-pick settlement — supplied slate

1\. Over 185.5 — WIN; actual total 201.

2\. Cairns +8.5 — LOSS; Cairns lost by 21.

3\. Sydney -8.5 — WIN; Sydney won by 21.

4\. Under 185.5 — LOSS.

Potential game winner: Sydney Kings — WIN.

##### Rank-1 / top-two review

Model-selected Rank #1 Sydney ML won and Rank #2 Over 179.5 also won.

Rank-1 success = YES.

Hit@2 = YES.

Both top-two win = YES.

No Rank-1 failure trigger applies.

The ordering was defensible: Sydney's deeper championship core and the independent +7.2 margin centre supported the winner, while Over 179.5 sat materially below the 186.7 total centre. The realised 21-point margin was substantially wider than projected, but that does not invalidate Sydney ML being ranked first.

##### Enhanced totals review

The highest-ranked model-selected over/under, Over 179.5, WON. The highest-ranked supplied over/under, Over 185.5, also WON. No TOP_OU_REVIEW failure trigger applies.

The nearby upper Under 191.5 lost because the game reached 201. Sydney scored 32 in Q1, 59 by halftime and 31 more in Q3, including 6/9 from three in that third period. The pre-game centre of 186.7 therefore underweighted the upper scoring tail. The correct lesson is not to reverse every nearby Under; it is to make the high-variance perimeter/transition branch explicit before ranking an upper Under close to the centre.

##### Expected game script vs actual

Expected: Sydney as the more likely winner, Cairns materially improved offensively, central score around 97-90, and a competitive game with enough scoring to prefer a lower Over.

Actual: Cairns led 14-8 early and remained within six at halftime, 59-53, so the competitive early branch was real. Sydney then separated decisively in the third quarter, leading 90-73 after three and finishing 111-90.

The largest forecast miss was separation/upper-tail magnitude, not winner direction. Projected Sydney margin was +7.2 versus +21 actual; projected total was 186.7 versus 201 actual.

##### What went right

- Sydney winner call was correct.

- Model Rank #1 and Rank #2 both won.

- The lower alternate Over 179.5 correctly captured a game with significant offensive upside.

- Supplied Over 185.5 was correctly preferred to Under 185.5.

- The pre-game absence check correctly had Luke Paul and Jaylin Galloway unavailable for Cairns; the NBL postgame report says Cairns still had both to come into the team.

- Pinder was correctly treated as a major Cairns offensive path; he delivered 27 points.

##### What went wrong

- Under 191.5 was too aggressive relative to the model's own uncertainty and lost by 9.5 points.

- Cairns +11.5 and +8.5 underestimated Sydney's separation tail.

- The central forecast did not place enough weight on a Sydney perimeter burst: six Kings finished in double figures and the third quarter was driven by hot outside shooting.

- Cairns' 13/44 three-point shooting created a high-volume, low-efficiency possession profile that widened the margin while still allowing the combined total to reach 201.

- Jack McVeigh scored only seven, while Cairns' foul trouble also reduced their ability to sustain the halftime response.

##### Starting-lineup / availability audit

Confirmed pre-game absences that were modelled: Sydney — Keli Leaupepe; Cairns — Jaylin Galloway and Luke Paul.

Exact field-owner starting fives were not recovered before issue and this remains an evidence limitation. No postgame source recovered in this settlement pass indicates that an unmodelled late withdrawal was the primary cause of the result.

##### Blind spots and mitigation

Blind spot: insufficient mass on a high-scoring Sydney separation branch in an opening-round game with strong shooting depth.

Pre-game knowability: PARTLY. Sydney's depth was known, but the exact 6/9 third-quarter three-point burst was not predictable.

Materiality: HIGH for Under 191.5 and Cairns spreads; LOW for Sydney ML and the lower Over.

Mitigation: when the centre supports an Over but an upper Under is also selected, explicitly quantify the branch in which favourite shooting efficiency plus opponent high-volume perimeter attempts create both a larger margin and a higher total. This is an execution reinforcement of existing distribution/tail controls, not a new fixed coefficient.

##### Source-quality audit

- NBL/AAP: retained as a high-quality league-hosted final/game-script source.

- Cairns Taipans official: retained as a primary team result and availability source.

- Austadiums: useful independent explicit-final corroboration for exact event/date/venue.

- NBL public schedule shell: do not use its generic LIVE NOW label as proof of event state; it displayed that label on future fixtures during the earlier check.

##### Document mapping / learnings

- DATA_SOURCE_REGISTER.md: candidate source-state observation — NBL public schedule LIVE NOW labels can be shell-level and must not control event state without an exact-event terminal source.

- RULES_BASKETBALL.md / SCORING_AND_VALIDATION.md: execution note only — nearby upper Unders require explicit upper-tail/separation mass when the same card already recognizes strong favourite shooting depth.

- No permanent sport-specific or cross-sport rule promoted from this single event.

- Dataset status remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

---

#### 2026-09-21 independent re-audit — P-477

**Re-verification of the settled final.** The NBL/AAP postgame report was re-opened in full this pass and returns the complete quarter sequence, which the 2026-09-20 settlement summarised but did not enumerate.

- NBL / AAP postgame report: **Sydney Kings 111, Cairns Taipans 90**. Q1 32-26; halftime **59-53**; three-quarter time **90-73**; final 111-90.
- Leading scorers: Kendric Davis 26 (6 ast, 5 reb), Xavier Cooks 18 (7 reb, 2 blk), Torrey Craig 13 for Sydney; **Keanu Pinder 27** (5 reb, 4 ast), Shaun Bruce 13, Malique Lewis 13 for Cairns.
- Shooting: Sydney 65% from the field in the first half and **6-of-9 from three in the third quarter**; Cairns **13-of-44 from beyond the arc (29.5%)**.
- Corroborating lineages already recorded: Cairns Taipans official postgame report (111-90) and the Austadiums exact-event record (111-90 Final, Sep 20 2026, 5:00 PM, Afterpay Arena).

Every settled row is unchanged. **Final total 201; margin Sydney +21.**

**A source-state warning recorded on 2026-09-20 is confirmed and should be promoted.** The NBL public schedule shell displayed a generic `LIVE NOW` label on fixtures that had not started. This pass re-confirms that the NBL schedule shell is not an event-state authority. Event state for NBL must come from an exact-event record (league match centre, club postgame report or an independent exact-event record such as Austadiums), never from a schedule-page badge.

**Ranking metrics.**

| Metric | Model-selected slate | Supplied slate |
|---|---|---|
| Rank-1 | **WIN** (Sydney ML) | **WIN** (Over 185.5) |
| Hit@2 | **YES** | **YES** |
| Wins@2 | **2 / 2** | **1 / 2** |
| NDCG@2 | **1.000** | **0.613** |
| Row record | 2 W / 2 L | 2 W / 2 L (both forced pairs) |
| Top over/under | Over 179.5 (Rank #2) — **WIN** | Over 185.5 (Rank #1) — **WIN** |
| Winner call | **WIN** — Sydney, p ≈ 0.70 | — |

**Forced-pair caveat.** Both supplied pairs (Over/Under 185.5 and Cairns +8.5 / Sydney -8.5) are strict complements, so the supplied 2 W / 2 L is again mechanically fixed. Informative decisions: prefer Over 185.5 (0.533, **W**) and prefer Cairns +8.5 (0.529, **L**) — two near-coin-flips, one each way.

**The internal contradiction on this card is worth naming.** The model-selected slate simultaneously held **Over 179.5 (0.69)** and **Under 191.5 (0.63)**, which is a corridor bet of 180–191 with a stated width of about 12 points around a 186.7 centre. The realised 201 cleared the corridor. Selecting both ends of a narrow corridor as two of the four "best" targets inflates the apparent slate size without adding independent information: the two rows share one driver and can only both win inside a band the card itself described as uncertain. Under `SCORING_AND_VALIDATION.md` §3 these are not two independent trials.

**Mandatory validation questions.**

1. **Confirmed starting fives?** **NO.** Expected/projected fives were retrieved; a formal confirmed five for either club was not recovered before issue. Rotation-sensitive props were correctly not promoted.
2. **Bench / rotation information?** **PARTIALLY.** Squad composition was known; rotation depth was treated qualitatively. Six Kings finished in double figures, which is a depth outcome the card did not quantify.
3. **Coaching information?** **NOT OBTAINED.** For an opening-round game with a new Sydney signing (Andrew Carr) and a substantially rebuilt Cairns roster, rotation policy is genuinely uncertain and arguably deserved an explicit uncertainty widening rather than a narrower corridor.
4. **Injuries / availability?** **YES and correct.** Sydney: Keli Leaupepe out. Cairns: Jaylin Galloway and Luke Paul out. All three were correctly modelled as absent, and the NBL postgame report confirms Cairns still had Galloway and Paul to come into the team. Kendric Davis's shortened preparation (passport-delayed return) was flagged and correctly not converted into a performance penalty — he scored 26.
5. **Were the original sources accurate and current?** **YES on availability and identity.** The one defective source was the NBL schedule shell's `LIVE NOW` badge, which was correctly refused.
6. **Better sources available?** **YES.** Austadiums proved to be a clean independent exact-event terminal record for Australian fixtures and should be registered as a third lineage for NBL/AFL/NRL settlement. Separately, the ESPN site API does **not** cover NBL, so the standard keyless lane is unavailable for this competition and the league/club/independent-event triad is the correct substitute.
7. **Blind spots?** **YES — two.** (a) An opening-round game after a long off-season has wider outcome dispersion than the card's ~12-point corridor allowed; roster turnover on both sides was known pre-game and should have widened, not narrowed, the distribution. (b) The joint state in which the favourite's perimeter efficiency spikes *and* the underdog shoots high-volume/low-efficiency threes produces a larger margin **and** a higher total at the same time. Cairns went 13-of-44 from three; that is 44 possessions ending in a low-percentage shot, which sustains pace while losing the game.
8. **How should this be handled in future?** Two specific changes. First, treat **round-one / post-off-season / heavy-roster-turnover** games as an explicit variance-widening state, and record it as a candidate test rather than a fixed coefficient until there is a sample. Second, never rank an upper Under and a lower Over from the same corridor as two independent "best" targets — state the corridor once, with its probability, and count it as one decision.

**Verdict on this event.** Direction was right on every axis that mattered (winner, the lower Over, the supplied Over) and the two losses were the two corridor-closing rows. The correct lesson is about corridor width and slate independence, not about the winner model.

---


### P-478 — Soccer / Sweden Allsvenskan — Djurgårdens IF vs IF Elfsborg

- Canonical / staging ID: P-478

- Competition: Sweden Allsvenskan 2026, Round 22

- Venue: 3Arena, Stockholm, Sweden; artificial surface

- Official venue-local start: Sep 20, 2026 at 14:00 CEST (Europe/Stockholm, UTC+2)

- Australia/Melbourne conversion: Sep 20, 2026 at 22:00 AEST (UTC+10); calendar-date rollover = NO

- Independent distribution freeze: approximately Sep 20, 2026 at 22:01 AEST

- Issuance state: START_CROSSED_UNVERIFIED / LATE-ISSUED RESEARCH FORECAST. The scheduled kickoff crossed while the required research was being completed; the structured event feed still showed Scheduled. No live score, shot, corner, card, substitution, possession or other in-game observation is admitted into the forecast.

- Method / controls: MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-SOCCER

- Operating mode: SPORTS_ONLY / MARKET_BLIND

- Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE

- Distribution ID: P-478-dist-v1

- Distribution SHA-256: 605b2c4ca216a77088c4df63f4f8224373c70b9370fd59e7b90d4e481d78b8ea

- No retrospective performed.

#### Identity / supplied contracts

User-supplied contracts were parsed only for identity and quarantined until after the independent goal distribution was frozen:

- First-half Over 0.5 goals

- First-half Under 0.5 goals

- Full-game Over 2.5 goals

- Full-game Under 2.5 goals

Research endpoint is regulation 90 minutes plus stoppage time. No extra-time/penalty endpoint applies to this Allsvenskan league fixture. Exact operator-specific action/void rules were not supplied.

#### Event/time/source gate

Official Djurgården and Elfsborg pages both identify Sunday Sep 20 at 14:00 local at 3Arena. The Allsvenskan round schedule independently lists the same fixture in Round 22. Melbourne conversion is 22:00 AEST.

At the final state refresh after the scheduled time crossed, the structured soccer event route still returned Scheduled and a zero-filled shell rather than a verified live sequence. Because scheduled-start crossing itself blocks a normal pregame issuance under the active controls, this is recorded as a late-issued research forecast rather than retroactively called a normal pregame PASS.

#### Participants / availability

Exact field-owner starting XIs were not recoverable through the accessible official Djurgården page: its preview still stated that the squad would be published one hour before kickoff. High-quality/current lineup feeds and recent official club selections converge on the following role-continuity XI shapes, but they are not relabelled official-confirmed:

Djurgården 4-2-3-1:

Jacob Rinne; Adam Ståhl, Miro Tenho, Jacob Une Larsson, Piotr Johansson; Daniel Stensson, Matias Siltanen; Patric Åslund, Bo Hegland, Jeppe Okkels; Kristian Lien.

Elfsborg 4-2-3-1:

Isak Pettersson; Alexander Jensen, Rasmus Wikström, Thomas Isherwood, Niklas Hult; Julius Magnússon, Simon Olsson; Momoh Kamara, Julius Beck, Arbër Zeneli; Leo Östman.

Role continuity is strong: Djurgården's official Sep 14 2-0 win over GAIS used the same XI; Elfsborg's official Sep 13 1-0 win over Kalmar used the same XI.

Material availability:

- Djurgården: Christos Almyras suspended after the red card versus GAIS. He was not part of the above recent starting XI, so this is primarily a bench/rotation loss rather than a starting-XI removal.

- Elfsborg: Per Frick is unavailable with a broken hand in current independent availability feeds. He was used as a late substitute in the Sep 13 official match record, so his loss affects late attacking depth more than the projected starting structure.

- No unsupported late-scratch claim is added.

Participant limitation: exact official matchday benches/final XIs were not recovered to field-owner standard before issue. Player props are therefore not ranked, and lineup-sensitive rows retain an evidence cap.

#### Current team/process evidence

Season through 21 Allsvenskan matches:

- Djurgården: 2nd, 41 points, 46 goals for / 19 against; xG 40.3 / xGA 26.0.

- Elfsborg: 34 points, 29 goals for / 21 against; xG 29.1 / xGA 25.7.

Djurgården have five straight Allsvenskan wins entering this fixture. The latest official home result was 2-0 over GAIS, with Lien scoring before halftime and Hegland after halftime. The streak is treated as descriptive; the signed view comes from current creation/defence/roster mechanisms rather than a momentum coefficient.

Elfsborg's latest official league result was 1-0 over Kalmar, with a 0-0 first half and Momoh Kamara scoring in the 51st minute. Their recent league sequence includes 1-1 at Göteborg, 2-0 over Degerfors, 1-2 at Brommapojkarna and 1-0 over Kalmar.

First-half evidence:

- Djurgården have scored in the first half in 67% of league matches overall and approximately 82% of home matches in the current sample.

- Elfsborg have scored in the first half in 43% overall / 40% away, while conceding about 0.40 first-half goals per away match.

- Recent Djurgården first-half xG examples include 0.80 vs GAIS, 2.10 vs Mjällby at home, 0.72 away to Mjällby and 0.44 at Malmö.

- Elfsborg's recent first-half creation has varied rather than consistently spiked.

This creates an early-goal lean driven mainly by Djurgården home creation, while Elfsborg's first-half defensive record prevents treating Over 0.5 as a high-certainty row.

#### Corner process

Corners are modelled separately from goals.

- Djurgården: 6.4 corners taken per Allsvenskan match, third-highest league rate in the cited current table.

- Elfsborg: 4.1 taken per match.

- Allsvenskan baseline: approximately 5.1 corners per team per match; home teams about 5.5, away teams about 4.8.

- Djurgården's recent individual corner counts: 2, 6, 3, 4, 7, 5, 7, 5, 6, 13 across the cited ten-match sequence.

- Score-state mechanism: a Djurgården lead can reduce their later attacking/corner demand, while an Elfsborg chasing state can add width/cross/end-line exposure. This prevents treating Djurgården territorial superiority as a one-sign team-corner guarantee.

Explicit corner-total scenario mixture produces an expected total around 9.4 corners. Over 7.5 is approximately 71% under the unvalidated subjective model. Exact operator/provider availability is not asserted.

#### Environment

SMHI's Stockholm-area forecast for Sep 20 shows roughly 12-16 C, south-westerly wind around 6 m/s with gusts around 14 m/s and some precipitation risk. 3Arena uses an artificial surface. Weather is retained as a mechanism/variance factor for long balls, crossing and set plays; no automatic Over/Under coefficient is applied.

#### Frozen independent goal distribution

Model: UNVALIDATED_SUBJECTIVE scenario mixture with independent Poisson goal kernels inside each state. It is not fitted, calibrated or prospectively validated.

1\. Central Djurgården territorial/home-control state — weight 0.36 — DJU 1.9, ELF 0.9.

2\. Djurgården pressure + Elfsborg compact/suppressed attack — 0.24 — DJU 2.2, ELF 0.7.

3\. Elfsborg counter/resistance branch — 0.18 — DJU 1.6, ELF 1.2.

4\. Closed top-table/keeper branch — 0.14 — DJU 1.4, ELF 0.6.

5\. Open transition/set-piece/weather-variance branch — 0.08 — DJU 2.5, ELF 1.5.

Frozen centre:

- Djurgården goals: \~1.90

- Elfsborg goals: \~0.91

- PROJECTED TOTAL: \~2.81

- Representative score family: Djurgården 2-1 / 2-0 / 1-1

- Djurgården regulation win: \~60.2%

- Draw: \~21.9%

- Elfsborg regulation win: \~17.9%

- Djurgården-or-draw: \~82.1%

Full-game total:

- Over 2.5: \~52.6%

- Under 2.5: \~47.4%

The supplied 2.5 line is therefore close to the independent centre and is not a strong full-game-total call.

First-half model:

- first-half centre \~1.11 goals

- Over 0.5 first-half goals: \~66.5%

- Under 0.5: \~33.5%

#### Best five model-selected targets

Candidate-slate discipline: thresholds are common/nearby soccer contracts, not arbitrarily wide alternates, and operator availability is not asserted.

1\. DJURGÅRDEN TEAM TOTAL OVER 0.5 GOALS — \~84.2% UNVALIDATED_SUBJECTIVE.

   Main mechanism: \~1.90 home scoring centre, 46 season goals, 40.3 xG, and a current XI retaining Lien/Hegland/Åslund/Okkels.

   Main failure: Elfsborg's defensive/keeper branch plus finishing variance produces 0-0 or a narrow away result.

2\. DJURGÅRDEN OR DRAW (1X) — \~82.1%.

   Main mechanism: stronger current season attack/defence profile and home control.

   Main failure: Elfsborg absorbs territory and wins a low-event transition/set-piece game.

3\. ELFSBORG TEAM TOTAL UNDER 1.5 GOALS — \~76.8%.

   Main mechanism: Elfsborg centre \~0.91, Djurgården 19 goals conceded in 21 matches and recent defensive suppression.

   Main failure: Djurgården turnover/set-piece errors or an early Elfsborg goal forcing an open score-state.

4\. TOTAL CORNERS OVER 7.5 — \~71.2%.

   Main mechanism: Djurgården 6.4 corners taken/game, Elfsborg 4.1, plus trailing-state width/cross exposure.

   Main failure: early efficient finishing reduces shot-block/end-line sequences or both sides attack centrally with low corner conversion.

5\. FULL-GAME UNDER 3.5 GOALS — \~68.9%.

   Main mechanism: the central total is 2.81; Elfsborg's attack is materially below Djurgården's and both clubs have credible low-event/keeper branches.

   Main failure: an early goal creates transition space and the match enters the open 2-2 / 3-1 family.

The user-supplied first-half Over 0.5 (\~66.5%) is narrowly outside the model top five but remains the preferred supplied first-half side.

#### Supplied-market ranking

1\. FIRST-HALF OVER 0.5 GOALS — \~66.5% — preferred.

2\. FULL-GAME OVER 2.5 GOALS — \~52.6% — very weak lean / close to projection.

3\. FULL-GAME UNDER 2.5 GOALS — \~47.4%.

4\. FIRST-HALF UNDER 0.5 GOALS — \~33.5%.

Forced-pair integrity:

- 1H Over 0.5 + 1H Under 0.5 = 100% conditional on action.

- FT Over 2.5 + FT Under 2.5 = 100% conditional on action.

No push exists at either half-goal threshold.

#### Potential game winner

DJURGÅRDEN — \~60.2% regulation-win estimate.

This is a clear but not overwhelming winner lean. Draw mass remains approximately 21.9%, which is why 1X ranks materially above the outright win.

#### Dependence / kill-path audit

The top selections are not independent:

- Djurgården TT Over 0.5 and 1X share the home attack/control driver.

- Elfsborg TT Under 1.5 also positively overlaps with a Djurgården-control state.

- Under 3.5 can win with 1X in 1-0, 2-0, 1-1 and 2-1 outcomes, but loses in high-separation/open states.

- Corner Over 7.5 is only partially linked to goals because trailing-state width can raise corners even when finishing is poor.

Top-two exact joint probability is not honestly identified by the current marginal goal model beyond the same score grid; the pair is highly dependent and is not presented as a parlay probability.

#### Integrity flags

- START_CROSSED_USER_OVERRIDE / PF-EVENT-STATE BLOCK

- NO_LIVE_GAME_STATE_USED_IN_MODEL

- EXACT_OFFICIAL_MATCHDAY_XIS/BENCHES_NOT_RECOVERED_TO FIELD-OWNER STANDARD

- CURRENT ROLE-CONTINUITY XIS RECOVERED FROM OFFICIAL PRIOR MATCHES + INDEPENDENT CURRENT LINEUP FEEDS

- MARKET ODDS / IMPLIED PROBABILITY / LINE MOVEMENT / SPORTSBOOK PREVIEWS / TIPSTERS / FANTASY-DFS EXCLUDED

- UNVALIDATED_SUBJECTIVE_DISTRIBUTION

- Current status: UNSETTLED — LATE-ISSUED RESEARCH FORECAST / NO RETROSPECTIVE

#### Sources / provenance

1\. Djurgården official preview — exact event, 3Arena, 14:00 local, suspension/warning state — PRIMARY TEAM — https://www.dif.se/nyheter/2026/infor-djurgarden-elfsborg

2\. Djurgården official schedule / date announcement — exact fixture time — PRIMARY TEAM — https://www.dif.se/nyheter/2026/speldatum-satta-for-omgang-18-23-i-allsvenskan

3\. IF Elfsborg official supporter/schedule information — exact event/date/time — PRIMARY TEAM — https://elfsborg.se/2026/09/15/supporterinfo-djurgardens-if-borta-1/

4\. Allsvenskan official round schedule — competition/round identity — PRIMARY COMPETITION — https://allsvenskan.se/nyheter/sa-spelas-omgang-18-23-av-allsvenskan/

5\. Djurgården official Sep 14 GAIS report — recent official starting XI, availability and 2-0 game script — PRIMARY TEAM — https://www.dif.se/nyheter/2026/norsk-briljans-visade-vagen-mot-gais

6\. Elfsborg official Sep 13 Kalmar report — recent official starting XI, bench usage and 1-0 game script — PRIMARY TEAM — https://elfsborg.se/2026/09/13/kamaras-mal-avgjorde-mot-kalmar/

7\. xGstats — current Allsvenskan record, goals and xG/xGA for both clubs — INDEPENDENT STRUCTURED STATISTICAL SOURCE — https://xgstats.com/teams/djurgardens-if and https://xgstats.com/teams/if-elfsborg

8\. FootyStats / SoccerStats — current first-half scoring/conceding splits and home/away scoring rates — INDEPENDENT STRUCTURED DIAGNOSTIC.

9\. FootyMetrics / Statz — current Allsvenskan corner-for rates and league home/away corner baselines — INDEPENDENT STRUCTURED DIAGNOSTIC.

10\. OFStats — Djurgården current shot/possession/corner diagnostics and match-by-match corners — INDEPENDENT STRUCTURED DIAGNOSTIC.

11\. FotMob/GioScore current match pages — lineup-role continuity and current availability cross-check; not promoted above official club records — INDEPENDENT CURRENT SECONDARY.

12\. SMHI — Stockholm-area current weather forecast — GOVERNMENT WEATHER FIELD OWNER.

13\. Structured soccer event feed — exact event ID 67126774 and final pre-issue scheduled-state check — CURRENT EVENT-STATE SOURCE.

14\. Sports Research Drive — METHOD.md, RULES_SOCCER.md, RULES_GENERAL.md, CONTROLS.md and current control manifest — GOVERNING METHODOLOGY.

Source firewall: betting-academy, bookmaker, odds, tipster, prediction-market and fantasy/DFS sources surfaced during discovery but were excluded from predictive evidence.

#### Document mapping / candidate learnings

- Official club preview can remain cache-lagged past its promised one-hour-before squad publication -\> DATA_SOURCE_REGISTER source-latency observation candidate.

- Early-goal lean was reconciled against Elfsborg's strong first-half defensive numbers rather than driven by Djurgården's recent scoring streak -\> existing RULES_SOCCER early-goal control executed; no new rule.

- Corners were derived independently from corner exposure/rates and score-state width rather than from possession/xG dominance -\> existing RULES_SOCCER corner-process control executed; no new rule.

- Scheduled-start crossing while the structured event route still shows Scheduled remains a process exception only; do not weaken the normal pregame gate.

#### Completed-event settlement check — derivative still unresolved

Factual event state: COMPLETED.

Verified regulation result: Djurgårdens IF 1, IF Elfsborg 2.

Verified halftime state: Djurgården 0, Elfsborg 1.

Three independent result lineages agree on the completed 1-2 result: the structured exact-event feed (event 67126774, COMPLETE), Aftonbladet/TT's explicit postgame report, and current independent match reporting. The final corner count required to settle Rank #4 Total Corners Over 7.5 was not recovered from a trustworthy final field after attempts through the exact Sofascore match page and additional indexed/stat-provider routes. Pre-match/market-derived corner pages and stale in-game snapshots are not used to manufacture the endpoint.

Resolved-row grading:

1\. Djurgården team total Over 0.5 — WIN; Djurgården scored once.

2\. Djurgården or Draw (1X) — LOSS; Elfsborg won 2-1.

3\. Elfsborg team total Under 1.5 — LOSS; Elfsborg scored twice.

4\. Total Corners Over 7.5 — UNRESOLVED_DERIVATIVE / FINAL CORNER FIELD NOT VERIFIED.

5\. Full-game Under 3.5 — WIN; three goals.

Supplied slate:

1\. First-half Over 0.5 — WIN; Elfsborg led 1-0 at halftime.

2\. Full-game Over 2.5 — WIN; final total three.

3\. Full-game Under 2.5 — LOSS.

4\. First-half Under 0.5 — LOSS.

Potential game winner: Djurgården — LOSS.

##### Partial retrospective on resolved rows

Rank #1 Djurgården TT Over 0.5 won. Rank #2 Djurgården-or-draw lost, so Hit@2 = YES but both-win = NO. No Rank-1 failure trigger applies.

The biggest modelling miss was team/winner separation: the forecast assigned only \~17.9% to an Elfsborg regulation win and \~76.8% to Elfsborg Under 1.5, yet Elfsborg scored twice and won. Aftonbladet/TT reports that Rasmus Wikström's 0-1 just before halftime came through a weak Jacob Rinne intervention. Djurgården improved after halftime and equalised, but Fotbollskanalen's postgame analysis identifies a second structural failure: offensive substitutions increased the home threat but two substitutes failed their defensive assignments, allowing Alexander Jensen to run free and set up Simon Olsson for the decisive 2-1.

What went right:

- Djurgården did score, landing Rank #1.

- First-half Over 0.5 landed.

- Full-game Over 2.5 landed while Under 3.5 also landed, correctly illustrating the 3-goal overlap band.

- The pre-game analysis explicitly preserved an Elfsborg counter/resistance branch rather than treating Djurgården home control as certain.

What went wrong:

- The Elfsborg counter/resistance branch was materially underweighted relative to the realised 2-1 away win.

- Djurgården-or-draw and Elfsborg Under 1.5 both failed.

- The pre-game model did not quantify goalkeeper-error and substitution-driven defensive-transition tails strongly enough for the side/away-team-total distribution.

- Exact matchday XI/bench confirmation was missing at issue; that mattered because the decisive second goal involved substitute defensive responsibilities.

Source audit:

- Aftonbladet/TT postgame — explicit 1-2 final and goal sequence — https://www.aftonbladet.se/senastenytt/ttsport/sport/a/JOdbOX/mardrom-for-djurgarden-jattetavla-och-forlust

- Fotbollskanalen postgame — detailed tactical/substitution explanation of the decisive 1-2 goal — https://www.fotbollskanalen.se/artiklar/allsvenskan/fem-spaningar-slarvigt-och-svagt-av-djurgarden

- Sofascore exact-event route — confirms the correct event and exposes detailed-stat capability, but the accessible indexed response did not expose the final corner count — https://www.sofascore.com/football/match/if-elfsborg-djurgardens-if/jKsmK

- Market/betting pages that surfaced while searching for corners were rejected as settlement evidence.

Document mapping:

- RULES_SOCCER.md: existing bench/substitution and score-state transition controls are relevant; execution reinforcement only.

- DATA_SOURCE_REGISTER.md: exact-event derivative-source latency/coverage note for Allsvenskan corners.

- No final retrospective closeout or permanent rule promotion until the corner derivative is settled.

Formal status: COMPLETED / GOAL+SIDE ROWS GRADED / CORNER DERIVATIVE PENDING / NOT FULLY SETTLED.

#### Final settlement and retrospective — P-478

Settlement status: SETTLED / RETROSPECTIVE COMPLETE.

Verified final: Djurgårdens IF 1, IF Elfsborg 2.

Halftime: Djurgården 0, Elfsborg 1.

Verified final corners: Djurgården 4, Elfsborg 7; total 11.

Three-source terminal-state gate: PASS.

- Structured exact-event soccer feed, event 67126774 — COMPLETE at 1-2.

- IF Elfsborg official postgame report — explicit 1-2 away win and goal sequence — https://ipv6.elfsborg.se/2026/09/20/stark-trepoangare-borta-mot-djurgarden/

- Aftonbladet/TT postgame report — explicit 1-2 final and game narrative — https://www.aftonbladet.se/senastenytt/ttsport/sport/a/JOdbOX/mardrom-for-djurgarden-jattetavla-och-forlust

Corner endpoint cross-check:

- WinDrawWin exact result page: 4-7 corners.

- BetStudy exact result page: 4-7 corners.

- TotalCorner exact H2H/result row: 4-7 corners, total 11.

These are used only for the final derivative field; sportsbook odds/tips are not used as predictive evidence.

##### Pick-by-pick settlement — model-selected slate

1\. Djurgården team total Over 0.5 — WIN; Djurgården scored once.

2\. Djurgården or Draw (1X) — LOSS; Elfsborg won 2-1.

3\. Elfsborg team total Under 1.5 — LOSS; Elfsborg scored twice.

4\. Total Corners Over 7.5 — WIN; 11 corners.

5\. Full-game Under 3.5 goals — WIN; total three.

Model-selected slate: 3 W / 2 L.

##### Supplied-market settlement

1\. First-half Over 0.5 — WIN; Elfsborg led 1-0 at halftime.

2\. Full-game Over 2.5 — WIN; total three.

3\. Full-game Under 2.5 — LOSS.

4\. First-half Under 0.5 — LOSS.

Potential game winner: Djurgården — LOSS.

##### Rank-1 / top-two review

Rank #1 Djurgården TT Over 0.5 — WIN.

Rank #2 Djurgården or Draw — LOSS.

Hit@2 = YES.

Both top-two win = NO.

No Rank-1 failure trigger applies.

The highest-ranked over/under in the model-selected slate was Total Corners Over 7.5 at Rank #4, and it WON with 11 corners. The highest-ranked goal-total row, Under 3.5 at Rank #5, also WON. No TOP_OU_REVIEW failure trigger applies.

##### Expected vs actual game script

The forecast correctly retained an Elfsborg counter/resistance branch, but assigned it too little mass: Elfsborg's regulation-win estimate was only \~17.9%. Rasmus Wikström put Elfsborg ahead at 44', Djurgården equalised through Jacob Une Larsson at 66', and Simon Olsson restored the away lead at 76'.

The side/winner miss was driven by two concrete mechanisms. First, the 0-1 involved a major Jacob Rinne error. Second, after Djurgården made more attacking substitutions, the decisive 1-2 exposed defensive-transition assignments; postgame tactical reporting identified the space that allowed Alexander Jensen to create the winner.

##### What went right

- Rank #1 landed.

- The first-half Over 0.5 direction landed.

- The model's 3-goal overlap band was coherent: Over 2.5 and Under 3.5 both won.

- The corner model was directionally correct; 11 actual corners cleared 7.5.

- The forecast did preserve an Elfsborg counter/resistance scenario instead of treating home control as deterministic.

##### What went wrong

- Djurgården-or-draw was materially overestimated at \~82.1%.

- Elfsborg Under 1.5 was too strong at \~76.8%; Elfsborg scored twice.

- Goalkeeper-error and substitution/transition tails were present conceptually but underweighted in the side and away-team-total distribution.

- The potential winner call was wrong.

- Exact field-owner matchday XI/bench confirmation was unavailable before issue, and the decisive second-half mechanism involved substitution-linked defensive responsibilities.

##### Source/lineup audit

The projected starting XIs were broadly close to the eventual starting structures, but the issue-time card correctly did not label them field-owner confirmed. This limitation mattered more for the bench/substitution state than for the opening XI. The final should therefore not be used to claim that the pregame lineup retrieval was complete.

##### Blind spots and mitigation

Blind spot: insufficient weight on goalkeeper-error plus transition exposure after attacking substitutions.

Pre-game knowability: PARTLY. The exact Rinne error was irreducible event variance; the possibility that aggressive substitutions widen transition risk was knowable structurally.

Materiality: HIGH for 1X and Elfsborg Under 1.5; LOW for Rank #1, corners and Under 3.5.

Mitigation: execute the existing bench/substitution score-state branch explicitly inside winner/team-total scenario weights rather than leaving it only as prose.

Rule status: execution reinforcement only; no new permanent rule from one event.

##### Document mapping

- RULES_SOCCER.md: existing bench/substitution and score-state transition controls; execution reinforcement.

- DATA_SOURCE_REGISTER.md: Allsvenskan derivative final-field routes (WinDrawWin / BetStudy / TotalCorner) as research-only fallback observations, not predictive sources.

- No permanent algorithm change promoted.

- Dataset remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

---

#### 2026-09-21 independent re-audit — P-478

**Re-verification of the settled final, and a material upgrade to the corner evidence.**

- ESPN soccer site API, `swe.1` scoreboard for 2026-09-20, event **401842828**: status `Full Time`, **Djurgården 1 — IF Elfsborg 2**.
- ESPN `swe.1` summary for event 401842828 — key events: Stensson yellow 39'; **Rasmus Wikström goal 44' (Elfsborg)**; Djurgården substitutions Fallenius 45', Abdulmalik 60', Max Larsson 60'; **Jacob Une goal 66' (Djurgården)**; **Simon Olsson goal 76' (Elfsborg)**; Langhoff 75', Rosenquist 78'.
- ESPN team statistics for the same event: **corners Djurgården 4, Elfsborg 7 — total 11**; possession 55.6 / 44.4; shots 9 / 15; shots on target 2 / 3.

**This resolves a genuine evidence-quality defect in the 2026-09-20 settlement.** That pass settled Total Corners Over 7.5 from three betting-branded derivative pages (WinDrawWin, BetStudy, TotalCorner) because it could not reach a trustworthy final corner field, and it recorded that limitation honestly. The corner count is in fact published by the ESPN soccer summary endpoint as `wonCorners`, a keyless structured route that is already in the project source register as the verified owner of soccer corner fields. **The settlement outcome is unchanged — 11 corners, Over 7.5 WIN — but the evidence now rests on a registered non-market structured source instead of three betting-branded pages.** The betting-branded citations should be demoted to "not required" for this row.

This is the most transferable finding in the whole audit: a known-good source in the register was not used, and a weaker substitute was accepted in its place. That is recurring-mistake **M15** in its source-selection form.

**A strong, and genuinely surprising, positive finding on lineups.** The card published role-continuity XIs for both clubs while explicitly refusing to label them confirmed. Against the ESPN confirmed team sheets:

- **Djurgården — 11 of 11 exact.** Rinne; Ståhl, Tenho, Une (Larsson), Johansson; Stensson, Siltanen; Åslund, Hegland, Okkels; Lien.
- **Elfsborg — 11 of 11 exact.** Pettersson; Jensen, Wikström, Isherwood, Hult; Magnússon, Olsson; Kamara, Beck, Zeneli; Östman.

The method that produced this was: take the starting XI from each club's **own official report of its most recent league match**, then cross-check against a current independent lineup feed, and publish it as projected. That produced 22 of 22 correct names here. Contrast P-481 below, where a same-day third-party lineup page was treated as fresher and got three of the four named attackers wrong. **Role continuity from the club's own last official team sheet is the stronger projection route; same-day third-party lineup pages are not.** This is a concrete, testable source-quality conclusion and the single most useful thing recovered in this pass.

**Ranking metrics.**

| Metric | Model-selected slate | Supplied slate |
|---|---|---|
| Rank-1 | **WIN** (Djurgården TT Over 0.5) | **WIN** (1H Over 0.5) |
| Hit@2 | **YES** | **YES** |
| Wins@2 | **1 / 2** | **2 / 2** |
| NDCG@2 | **0.613** | **1.000** |
| Row record | 3 W / 2 L | 2 W / 2 L (both forced pairs) |
| Top over/under | Total Corners Over 7.5 (Rank #4) — **WIN**; Under 3.5 (Rank #5) — **WIN** | 1H Over 0.5 (Rank #1) — **WIN** |
| Winner call | **LOSS** — Djurgården, p ≈ 0.602 | — |

**Mandatory validation questions.**

1. **Confirmed starting XIs?** **NO — projected only, and correctly labelled.** The official Djurgården preview still said the squad would be published one hour before kick-off, and the accessible route never refreshed. Post-hoc the projections were exact, which validates the method but does not retroactively confer a confirmed evidence grade.
2. **Bench / substitute information?** **NO — and this is where it mattered.** The card had no matchday bench. The decisive 1-2 came at 76', after Djurgården had made three attacking substitutions (45', 60', 60'), and postgame tactical reporting attributes the goal to two substitutes failing defensive assignments, which let Alexander Jensen run free to create for Simon Olsson. A missing bench is not a missing detail on this card; it is a missing input to the decisive mechanism.
3. **Coaching / tactical information?** **PARTIALLY.** Formation shape (4-2-3-1 both sides) was modelled. In-game substitution policy was not, and it is what the postgame analysis identifies as causal.
4. **Injuries / suspensions / withdrawals?** **YES and correct.** Djurgården: Christos Almyras suspended after a red card v GAIS, correctly characterised as a bench/rotation loss because he was not in the recent XI. Elfsborg: Per Frick unavailable with a broken hand, correctly characterised as a loss of late attacking depth. Neither was contradicted by the team sheets.
5. **Were the original sources accurate and current?** **MIXED.** Club official reports, the Allsvenskan round schedule and the xG/corner statistical sources were accurate. The structured event feed still returned `Scheduled` after kick-off had passed, which is a staleness defect and is the reason the card was correctly labelled a late-issued research forecast rather than a normal pregame PASS. For settlement, the betting-branded corner routes were adequate but unnecessary — see above.
6. **Better sources available?** **YES, decisively.** ESPN `swe.1` `summary?event=` supplies the final, halftime-implied goal times, both confirmed XIs, both benches, substitution times and `wonCorners` in a single keyless call. It should be the primary settlement and lineup-audit route for every ESPN-covered soccer competition, ahead of both the structured event feed and any derivative statistics page.
7. **Blind spots?** **YES — three, in order of materiality.** (a) The away side's win branch was assigned only 17.9% while Elfsborg were a 34-point top-half side with 29.1 xG and 25.7 xGA; that is too thin for a competent visiting team even against a five-win home streak. (b) Goalkeeper error was not represented at all, and the 0-1 came through a weak Jacob Rinne intervention. (c) Substitution-driven defensive-transition risk existed in prose but carried no weight in the side or away-team-total distributions.
8. **How should this be handled in future?** Three specific, small changes. First, **floor the away-win branch** in a two-competent-sides league fixture at the competition's own away-win base rate unless there is a named suppression mechanism — Djurgården's home record is a reason to sit above the base rate, not a reason to sit at half of it. Second, require the **bench/substitution branch to carry explicit weight** in the winner and team-total distributions whenever the favourite is expected to chase or extend a lead, rather than appearing only as narrative. Third, record **goalkeeper-error mass** as part of ordinary low-event variance rather than treating a single defensive mistake as unmodellable; the point is not to predict the error but to stop the away-win branch being compressed below its base rate.

**Verdict on this event.** Rank #1, both corner and goal totals and the first-half direction all landed; the side/winner view was materially wrong and the away-team-total Under was too confident. The corner model deserves specific credit: it was built independently of the goal model from corner-exposure rates and score-state width, it predicted about 9.4, the realised count was 11, and it won even though the goal-side view was wrong. That independence is the right design and should be preserved.

---


### P-479 — Cricket / European T20 Premier League Final — Edinburgh Castle Rockers vs Belfast Wolves

- Canonical / staging ID: P-479

- Competition: European T20 Premier League 2026 Final

- Venue: The Village, Malahide, Ireland

- Official venue-local start: Sep 20, 2026 at 14:15 IST (Europe/Dublin, UTC+1)

- Australia/Melbourne conversion: Sep 20, 2026 at 23:15 AEST (UTC+10); date rollover = NO

- Original issue state: PREGAME; final pre-issue refresh did not recover toss/confirmed XI.

- Method / controls: MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-CRICKET

- Operating mode: SPORTS_ONLY / MARKET_BLIND

- Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE

#### Original pre-game prediction

Frozen Belfast batting-first centre:

- Powerplay / first six overs: \~45 runs.

- Full first innings: \~160 runs.

- Working first-innings central corridor: \~145-175.

Best four model-selected targets:

1\. Belfast Wolves first six overs UNDER 55.5 — \~73% UNVALIDATED_SUBJECTIVE.

2\. Belfast Wolves first innings OVER 144.5 — \~66%.

3\. Belfast Wolves first innings UNDER 174.5 — \~64%.

4\. Edinburgh Castle Rockers to win — \~56%.

Supplied-line ranking:

1\. Belfast first six UNDER 46.5 — \~56%.

2\. Belfast first innings OVER 158.5 — \~53%.

3\. Belfast first innings UNDER 158.5 — \~47%.

4\. Belfast first six OVER 46.5 — \~44%.

Potential game winner: Edinburgh Castle Rockers — \~56%.

#### Original research reasoning / availability

- Belfast's four prior Malahide first-innings powerplays in the retrieved sample were 43/3, 49/1, 54/1 and 36/2, producing a 45.5-run mean and supporting the powerplay-Under direction.

- The full-innings sample was 107, 161, 187 and 190, showing that a subdued powerplay could still recover into a high final score; the Sep 17 meeting was 36/2 after six but 190/4 after 20.

- Edinburgh's attack carried multiple wicket paths through Boult, Curran, Jarvis, Santner and Watt.

- Charlie Tear was officially ruled out for Edinburgh. Mark Chapman had retired hurt in the prior meeting, but no reliable current source confirmed a continuing injury; Chapman and David Miller were treated as selection uncertainties rather than invented absences.

- Strip status: NOT FOUND AFTER SEARCH after the required pitch-report ladder. Venue/format historical scoring and the preceding Malahide match were used only as historical context.

- Match-window conditions were low-disruption with no material rain signal.

#### Material sources

1\. ETPL exact final page — event identity / official competition route — https://www.etplofficial.com/matches/6a688c61b30844b0969df8c2

2\. Tixr official event listing — exact local date/time and Malahide venue — https://www.tixr.com/groups/etplofficial/events/etpl-2026-final-edinburgh-castle-rockers-v-belfast-wolves-198572

3\. CricketWorld Sep 17 exact scorecard — Belfast 190/4 and 36/2 powerplay against Edinburgh — https://www.cricketworld.com/cricket/edinburgh-castle-rockers-vs-belfast-wolves/match/scorecard/98352

4\. CricketEurope tournament results — current ETPL result/scoring context — https://www.cricketeurope.com/FINALSCORE/RESULTS/TOURNAMENTS/EuropeanT20PremierLeague.shtml

5\. ETPL qualifier page — Belfast's immediate prior qualifier result and workload — https://www.etplofficial.com/matches/6a688c61b30844b0969df8c1

6\. CricketArchive / Cricket Ireland scorecard — prior exact Edinburgh-Belfast match context — https://www.cricketarchive.com/CricketIreland/Scorecards/1458/1458982.html

7\. Pitchcare Malahide groundskeeping profile — historical venue tendency only, not current strip — https://www.pitchcare.com/blogs/news/the-craic-of-leather-on-willow-at-malahide

8\. Weather forecast — match-window temperature/rain context.

9\. Sports Research Drive — governing method and cricket rules.

Source firewall: betting picks, fantasy/DFS projections, market odds and prediction-site recommendations were excluded from predictive inputs.

#### Current state check

CURRENT STATUS: LIVE / NO SETTLEMENT.

A current CricTracker exact-event page reports Play Ongoing, Edinburgh elected to bowl, with Belfast 69/1 after 9.1 overs at the observed refresh. This is a moving live state and is recorded separately from the immutable pre-game prediction. No row is graded and no retrospective is performed while the match remains live.

Live-state source: https://www.crictracker.com/live-scores/ecr-vs-tba-final-t20-european-t20-premier-league-20-sep-2026/

Document mapping: no new lesson promoted while live. Any post-match learning waits for terminal-state verification.

#### Settlement and retrospective — P-479

Settlement status: SETTLED / RETROSPECTIVE COMPLETE.

Verified final: Belfast Wolves 150/5 (20 overs); Edinburgh Castle Rockers 151/3 (18.4 overs).

Result: Edinburgh Castle Rockers won by 7 wickets.

Belfast powerplay: 41/1 after six overs.

Three-source terminal-state gate: PASS.

- CricketWorld exact scorecard — Completed; Belfast 150/5, Edinburgh 151/3, Edinburgh won by 7 wickets; exact powerplay 41/1 — https://www.cricketworld.com/cricket/edinburgh-castle-rockers-vs-belfast-wolves/match/scorecard/98355

- BBC report syndicated by Yahoo Sports — explicit Edinburgh seven-wicket final and full innings totals — https://ca.sports.yahoo.com/news/edinburgh-castle-rockers-beat-belfast-174958677.html

- MyKhel exact scorecard — Result; Edinburgh 151/3 beat Belfast 150/5 by 7 wickets — https://www.mykhel.com/cricket/edinburgh-castle-rockers-vs-belfast-wolves-2026-final-scorecard-m273640/

##### Pick-by-pick settlement — model-selected slate

1\. Belfast first six Under 55.5 — WIN; powerplay 41/1.

2\. Belfast first innings Over 144.5 — WIN; 150/5.

3\. Belfast first innings Under 174.5 — WIN; 150/5.

4\. Edinburgh Castle Rockers to win — WIN.

Model-selected slate: 4 W / 0 L.

##### Supplied-line settlement

1\. Belfast first six Under 46.5 — WIN; 41 runs.

2\. Belfast first innings Over 158.5 — LOSS; 150.

3\. Belfast first innings Under 158.5 — WIN.

4\. Belfast first six Over 46.5 — LOSS.

Potential game winner: Edinburgh Castle Rockers — WIN.

##### Rank-1 / top-two / total review

Rank #1 Under 55.5 powerplay — WIN.

Rank #2 Over 144.5 innings — WIN.

Hit@2 = YES.

Both top-two win = YES.

The highest-ranked over/under selection was Rank #1 and won, so no enhanced failure trigger applies.

##### Expected vs actual game script

The pregame powerplay centre was \~45 and the realised powerplay was 41/1, strongly validating the early-phase direction. Belfast then recovered through Tim Tector's 84 and Devon Conway's 29 but lost middle/death acceleration when Glenn Maxwell made 3 and Lorcan Tucker 6, finishing at 150/5. That landed inside the forecast's 145-175 central corridor and simultaneously won Over 144.5 and Under 174.5.

Edinburgh chased efficiently to 151/3 in 18.4 overs, driven by Andries Gous' unbeaten 90. The winner call therefore landed through both bowling control and chase quality.

##### What went right

- All four model-selected targets won.

- Both top-two selections won.

- The powerplay model correctly separated early scoring from the full-innings ceiling.

- The 145-175 innings corridor was well centred around the actual 150.

- The explicit possibility that a subdued powerplay could still recover into a respectable final total was correct.

- Edinburgh winner was correct.

##### What went wrong / limitations

- The exact supplied 158.5 full-innings line was on the wrong side: Over 158.5 lost while Under won.

- The pregame analysis could not confirm the final XI or exact current strip before issue.

- Mark Chapman and David Miller did not appear in the final Belfast batting XI; the pregame card appropriately treated them as selection uncertainties rather than asserting availability.

- Postgame CricketWorld metadata describes the surface as spinning/average with swing favourable, but this is retrospective information and is not retroactively inserted as known pregame strip evidence.

##### Availability / participant audit

Belfast's realised batting group included Stirling, Tector, Conway, Maxwell, Tucker and Manenti. The uncertainty around Chapman/Miller was material to the ceiling branch, but because it was disclosed rather than fabricated, this is an evidence-quality limitation rather than a hindsight error.

##### Blind spots and mitigation

Blind spot: exact 158.5 threshold sensitivity around a central innings corridor.

Pre-game knowability: YES. A centre around 160 with meaningful uncertainty means 158.5 should remain a low-separation call.

Materiality: HIGH only for the supplied 158.5 pair; LOW for the broader model-selected corridor and winner.

Mitigation: retain corridor-first modelling and avoid overstating confidence when a supplied line lies within a few runs of the independent centre.

Rule status: existing threshold-separation and phase-to-innings controls worked; no new rule.

##### Document mapping

- RULES_CRICKET.md: powerplay-to-innings separation worked as intended.

- DATA_SOURCE_REGISTER.md: CricketWorld exact match notes successfully exposed the final powerplay field for settlement.

- No permanent rule change promoted.

- Dataset remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

---

#### 2026-09-21 independent re-audit — P-479

**Re-verification of the settled final at a stronger source than the original settlement used.** The 2026-09-20 pass settled at CricketWorld, BBC-via-Yahoo and MyKhel. CricketWorld is now behind a bot-verification wall and returns nothing through either the direct route or the text proxy, so that lineage is no longer reproducible. The ESPNcricinfo full scorecard, reached through the `r.jina.ai` text proxy, reproduces every settled field and adds the exact phase record:

- **Belfast Wolves 150/5 (20 overs)**; Edinburgh Castle Rockers **151/3 (18.4 overs)**; **Edinburgh won by 7 wickets with 8 balls remaining**.
- **Toss: Edinburgh Castle Rockers, elected to field first.** Belfast therefore batted first, which is what activated every supplied "Belfast first innings" and "Belfast first six" contract.
- **`Powerplay 1: Overs 0.1 - 6.0 (Mandatory - 41 runs, 1 wicket)`** — the exact field that settles both powerplay rows, published as a structured match note rather than inferred from a ball-by-ball reconstruction.
- Belfast batting: Stirling 8 (10), **Tim Tector 84 (62)**, **Devon Conway 29 (24)**, Maxwell 3 (5), Tucker 6 (5), Manenti 16* (14); extras 4. Fall of wickets 1-18 (2.6), 2-81 (11.3), 3-95 (12.6), 4-105 (14.4), **5-150 (19.6)**.
- Belfast did not bat: Chris Jordan, Mark Adair, Gavin Hoey, Fred Klaassen, Matthew Humphreys. **Neither Mark Chapman nor David Miller appears in the XI at all** — confirming the card's decision to treat them as selection uncertainties rather than asserting availability.
- Edinburgh chase: Ross Adair 23 (14), Smuts 15 (23), **Andries Gous 90* (61)**, McMullen 17 (12), Santner 2* (2).

Every settled row is unchanged. **Belfast powerplay 41/1; Belfast innings 150; Edinburgh won by 7 wickets.**

One correction to a secondary source used in the settlement chain: the Yahoo-syndicated BBC summary names the No. 3 batter as "Paul Conway". The scorecard shows **Devon Conway**. The mini log's original text said Devon Conway and was right; the syndicated summary was wrong. This is a small but useful illustration of why a scorecard and not a recap owns player-level fields.

**Ranking metrics.**

| Metric | Model-selected slate | Supplied slate |
|---|---|---|
| Rank-1 | **WIN** (Belfast first six Under 55.5) | **WIN** (Belfast first six Under 46.5) |
| Hit@2 | **YES** | **YES** |
| Wins@2 | **2 / 2** | **1 / 2** |
| NDCG@2 | **1.000** | **0.613** |
| Row record | **4 W / 0 L** | 2 W / 2 L (both forced pairs) |
| Top over/under | Under 55.5 (Rank #1) — **WIN** | Under 46.5 (Rank #1) — **WIN** |
| Winner call | **WIN** — Edinburgh, p ≈ 0.56 | — |

**Why this card worked, mechanically.** The powerplay was modelled *separately* from the full innings rather than as a fraction of it. The card's powerplay centre was ~45 against a realised 41, and its full-innings corridor was 145–175 against a realised 150. Both were right at the same time precisely because they were built as two linked but distinct quantities. The card also explicitly wrote down the state in which a subdued powerplay still recovers into a large total — it had a 36/2-to-190/4 precedent from the same two teams three days earlier — and then declined to let that precedent drag the innings centre upward. That is correct use of a small sample: as a width argument, not as a centre shift.

**Mandatory validation questions.**

1. **Confirmed XIs / toss?** **NO — neither, before issue.** The final pre-issue refresh recovered neither the toss nor a confirmed XI. The card issued anyway and labelled the gap. In a T20 final where every supplied contract was conditioned on "Belfast first innings", **the toss is an activation condition, not a detail** — if Belfast had bowled first, all four supplied rows would have needed activation review rather than settlement. The card was one coin-flip away from a `CONDITION NOT MET` outcome of the kind recorded at P-445.
2. **Bench / squad information?** **PARTIALLY.** Squad availability was known at competition level; the final XI was not.
3. **Coaching / captaincy information?** **NOT MATERIAL** beyond the toss decision, which is covered above.
4. **Injuries / withdrawals?** **YES, and handled to the right standard.** Charlie Tear was officially ruled out for Edinburgh. Mark Chapman had retired hurt in the previous meeting, but no reliable current source confirmed an ongoing injury, so the card treated Chapman and David Miller as **selection uncertainties rather than inventing absences**. Both were in fact absent from the XI. Declining to assert an unverified absence and then being right is exactly the behaviour `METHOD.md` §6 requires.
5. **Were the original sources accurate and current?** **YES at the time; one has since degraded.** CricketWorld supplied the powerplay field on 2026-09-20 and is now bot-walled. That is a live source-availability change and should be recorded.
6. **Better sources available?** **YES.** ESPNcricinfo's full scorecard via the text proxy exposes `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - N runs, W wickets)` as an explicit structured match note, plus toss, fall of wickets and the did-not-bat list. It is strictly better than CricketWorld for phase settlement and is the same route that settled P-406's six-over rows on 2026-09-16. It should be the registered first route for T20 phase fields.
7. **Blind spots?** **TWO, both about conditions rather than modelling.** (a) **Strip status was `NOT FOUND AFTER SEARCH`** after the full pitch-report ladder, so the innings centre rested on venue/format history plus the preceding same-venue match, which the rules correctly treat as a different strip. Postgame metadata describes the surface as spinning/average with swing — useful, but retrospective, and correctly not backfilled. (b) The supplied 158.5 line sat within ~8.5 runs of a ~160 centre with substantial innings variance, so neither side of it ever deserved confidence; the card said 53/47 and that was honest.
8. **How should this be handled in future?** Keep the corridor-first construction, which worked. Add one hard requirement: **when every supplied contract is conditioned on a specific team batting first, the toss must be treated as a blocking activation gate** — either recover it, or state the activation probability explicitly and rank conditional on activation. The existing cricket rules cover innings-phase separation well; they do not currently force the toss to be treated as an activation condition on the supplied slate.

**Verdict on this event.** The best-forecast card in the mini log: four of four model-selected targets won, the powerplay and the innings corridor were both centred correctly, the winner was right, and the two supplied losses were the dead side of a near-coin-flip line. The only real exposure was procedural — issuing four toss-conditional contracts without the toss.

---


### P-480 — Soccer / Denmark Superligaen — Viborg FF vs FC Nordsjælland

- Canonical / staging ID: P-480

- Competition: Denmark Superligaen

- Venue: Energi Viborg Arena, Viborg, Denmark

- Official venue-local start: Sep 20, 2026 at 18:00 CEST (Europe/Copenhagen, UTC+2)

- Australia/Melbourne conversion: Sep 21, 2026 at 02:00 AEST; date rollover = YES

- Original issue state: PREGAME / NOT STARTED

- Method / controls: MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-SOCCER

- Operating mode: SPORTS_ONLY / MARKET_BLIND

- Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE

#### Original pre-game prediction

Frozen goal centre:

- Viborg \~1.26

- FC Nordsjælland \~1.42

- Projected total \~2.68

Best five:

1\. First-half UNDER 1.5 goals — \~75% UNVALIDATED_SUBJECTIVE.

2\. FC Nordsjælland team total OVER 0.5 — \~75%.

3\. Full-game UNDER 3.5 goals — \~72%.

4\. Total corners OVER 7.5 — \~70%.

5\. FC Nordsjælland or Draw (X2) — \~66%.

Supplied lines:

- First-half Over 0.5 \~60.9%; Under 0.5 \~39.1%.

- Full-game Under 2.5 \~50.2%; Over 2.5 \~49.8%.

Potential game winner: FC Nordsjælland \~41.1%; Draw \~25.4%; Viborg \~33.5%.

#### Original research reasoning / availability

- Viborg entered with 11 goals scored / 7 conceded; FCN 13 / 6, while current xG data indicated FCN's attack was stronger than the raw 13 goals.

- Viborg's official Opta preview noted all five of FCN's most recent league goals had arrived after the 60th minute, supporting a distinction between a quieter first half and later FCN scoring.

- Corners were modelled separately: Viborg home match-corner environment around 12.25 and FCN away around 9.00 in the retrieved small samples, then shrunk for uncertainty.

- Official/current lineup sources converged on likely XI shapes but the accessible final feed still labelled them predicted rather than field-owner confirmed, so no player prop was promoted.

- Viborg: Riahi long-term knee injury officially confirmed; current feeds also listed Anyembe, Freriks and Njoh unavailable.

- FCN: current feed listed Salquist, Araphat Mohammed and Souleymane Alio unavailable; no suspensions were reported by Viborg's official preview.

- Weather near kickoff included showers and wind; treated as variance, not an automatic total direction.

#### Material sources

1\. Viborg official schedule — exact event/time — https://vff.dk/ligaen/kampprogram

2\. Viborg official Opta/Superstats preview — H2H, goal timing, passing/tackling and suspension context — https://www.vff.dk/nyhedsarkiv/8-sport/15936-info-og-stats-for-vff-fcn-4

3\. FC Nordsjælland official material — recent team/result context — https://fcn.dk/nyheder/2026/september/highlights-fc-nordsjaelland-agf-1

4\. MatchPulse — current-season xG/xGA — https://matchpulsestats.com/en/league/119/xg

5\. SoccerStats — current home/away goal and corner splits — https://www.soccerstats.com/pmatch.asp?league=denmark\&stats=50-1-10-2027

6\. FotMob exact-event page — projected XI/current availability; not promoted above official sources — https://www.fotmob.com/en-GB/matches/viborg-vs-nordsjaelland/3crs0u?player=1382135

7\. Viborg official Riahi medical update — https://vff.dk/nyhed/sport/15790-mohamed-riahi-alvorligt-knaeskadet

8\. FCN official squad/availability material — https://fcn.dk/nyheder/2026/september/truppen-til-aftenens-kamp-i-herning

9\. Weather forecast and Sports Research Drive methodology.

#### Current state check

CURRENT STATUS: LIVE / NO SETTLEMENT.

The structured soccer event feed (event 71925034) showed Viborg vs FC Nordsjælland live at the state refresh. No row is graded and no retrospective is performed while live.

Document mapping: none while live; retain for terminal-state settlement.

#### Settlement and retrospective — P-480

Settlement status: SETTLED / RETROSPECTIVE COMPLETE.

Verified final: Viborg FF 4, FC Nordsjælland 1.

Halftime: Viborg 3, FC Nordsjælland 1.

Final corners: Viborg 4, FC Nordsjælland 5; total 9.

Three-source terminal-state gate: PASS.

- Structured exact-event soccer feed, event 71925034 — COMPLETE at 4-1.

- Eurosport exact match page — completed 4-1 with final stats including 4-5 corners — https://www.eurosport.nl/voetbal/3f-superliga/2026-2027/live-viborg-ff-fc-nordsjaelland_mtc21873592/live.shtml

- Sky Sports exact fixture/result page — full-time Viborg 4-1 FC Nordsjælland — https://www.skysports.com/football/viborg-ff-vs-fc-nordsjaelland/6482622979768878232

Derivative cross-check:

- Abseits exact match page: HT 3-1, corners 4-5.

- Campo/Ritzau report: four first-half goals and 3-1 halftime, final 4-1.

- Eurosport: corners 4-5.

##### Pick-by-pick settlement — model-selected slate

1\. First-half Under 1.5 goals — LOSS; halftime total was four.

2\. FC Nordsjælland team total Over 0.5 — WIN; FCN scored once.

3\. Full-game Under 3.5 goals — LOSS; final total five.

4\. Total Corners Over 7.5 — WIN; total nine.

5\. FC Nordsjælland or Draw (X2) — LOSS; Viborg won 4-1.

Model-selected slate: 2 W / 3 L.

##### Supplied-line settlement

- First-half Over 0.5 — WIN.

- First-half Under 0.5 — LOSS.

- Full-game Under 2.5 — LOSS.

- Full-game Over 2.5 — WIN.

Potential game winner: FC Nordsjælland — LOSS.

##### Mandatory enhanced Rank-1 / TOP_OU failure review

Rank #1 First-half Under 1.5 — LOSS.

This row was also the highest-ranked over/under selection, so one enhanced review covers both the Rank-1 and TOP_OU triggers.

Rank #2 FCN team total Over 0.5 — WIN.

Hit@2 = YES.

Both top-two win = NO.

Why Rank #1 was placed first:

- the first-half centre was \~0.95 goals;

- FCN's previous five league goals had all arrived after the 60th minute;

- FCN's two immediately preceding league matches had reached halftime 0-0;

- the forecast expected a patient opening and separated late FCN scoring from early scoring.

Why that ranking failed:

- Viborg scored at 16', 33' and 41'; FCN scored at 26'. The match had four first-half goals before the model's preferred slow-opening branch could establish itself.

- The pregame reasoning overweighted FCN's recent late-goal timing and underweighted Viborg's own home first-half attacking capacity and the possibility of early conversion from both sides.

- The 75% estimate was too confident for a phase total built from small, overlapping timing samples and without field-owner confirmed lineups/bench state.

- The supplied 1H Over 0.5 at \~60.9% actually won and was the structurally safer early-goal target because it needed only one event, whereas Under 1.5 required the entire first half to avoid a second goal.

Should another row have ranked above it?

YES. On the frozen information, FC Nordsjælland team total Over 0.5 was also estimated around 75% and was less sensitive to exact first-half timing. Given the unresolved XI/bench state and the small timing sample, FCN TT Over 0.5 should have been Rank #1 or at minimum tied ahead of the first-half Under after an uncertainty penalty.

Failure classification:

- Small/overlapping sample timing inference: YES.

- Poor uncertainty handling: YES.

- Missing confirmed lineup/bench information: CONTRIBUTORY.

- Existing rule not fully executed: YES — the phase-total path geometry and evidence-grade cap should have prevented a 75% phase Under from being treated as clearly strongest without stronger first-half suppression evidence.

- Genuine variance: PARTLY, but not sufficient to excuse the ranking.

##### Full-match total review

Under 3.5 also lost, with five total goals. The same underlying miss carried forward: the distribution underweighted the high-conversion/open branch. Viborg's 3-1 halftime score meant the Under 3.5 was already dead by the break.

The preferred supplied full-game side had been Under 2.5 at only \~50.2%, essentially no separation. It lost, while Over 2.5 won. This was not a strong pregame opinion and should remain classified as near-coin-flip rather than a major directional failure.

##### Actual game script

Viborg led through Mads Søndergaard at 16'. Alexander Lind equalised for FCN at 26'. Dorian Hanza restored Viborg's lead at 33', and Charly Horneman made it 3-1 at 41'. Adam Kleis-Kristoffersen completed the 4-1 at 81'.

The decisive feature was not late FCN scoring. It was Viborg's first-half attacking efficiency and FCN's inability to suppress repeated home chances. FCN still scored once, preserving Rank #2.

##### What went right

- FCN team total Over 0.5 won.

- Total corners Over 7.5 won with nine.

- Supplied first-half Over 0.5 won.

- Supplied full-game Over 2.5 won.

- The corner model remained independent of the incorrect goal-total direction and still landed.

##### What went wrong

- Rank #1 failed badly: four first-half goals versus an Under 1.5 call.

- Under 3.5 failed by 1.5 goals.

- FCN X2 and the potential winner call failed.

- The model over-weighted FCN's recent late-goal pattern and under-weighted Viborg's home attacking ceiling.

- The 2.68 full-game centre was materially too low for the realised high-conversion game.

##### Lineup / availability audit

The pregame card explicitly said the accessible lineup feeds were projected rather than field-owner confirmed. The realised scorers included Dorian Hanza and Alexander Lind, both consistent with the expected attacking structures. No postgame evidence indicates a late withdrawal was the central cause. The main failure was distribution/ranking, not an undisclosed injury.

##### Blind spots and mitigation

1\. First-half phase Under built from small timing samples.

   - Pre-game knowability: YES.

   - Materiality: VERY HIGH.

   - Mitigation: shrink recent goal-timing streaks more aggressively toward competition/home-away first-half base rates and require stronger bilateral suppression evidence before assigning \~75% to U1.5.

2\. Viborg home attacking ceiling.

   - Pre-game knowability: YES.

   - Materiality: HIGH.

   - Mitigation: give the home side's multi-window chance/goal production an explicit branch independent of opponent recent scoring timing.

3\. No confirmed XI/bench.

   - Pre-game knowability: known missingness.

   - Materiality: MODERATE.

   - Mitigation: preserve a wider phase-total distribution when final participant state is unresolved.

Rule status: these are execution corrections to existing phase-total, recency and uncertainty controls. Do not promote a new fixed coefficient from one match.

##### Source audit / document mapping

- Campo/Ritzau: strong same-day game-script source.

- Eurosport and Abseits: useful exact-event final/halftime/corner fields.

- Structured soccer feed: reliable terminal-state confirmation.

- RULES_SOCCER.md: execution reinforcement for phase-total geometry, recency shrinkage and XI uncertainty.

- DATA_SOURCE_REGISTER.md: Danish Superliga exact-event derivative field routes as research-only settlement candidates.

- Dataset remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

---

#### 2026-09-21 independent re-audit — P-480

**Re-verification of the settled final at the keyless structured lane.**

- ESPN soccer site API, `den.1` scoreboard for 2026-09-20, event **401874495**: status `Full Time`, **Viborg FF 4 — FC Nordsjælland 1**.
- ESPN `den.1` summary key events: Nelsson yellow 8'; **Mads Søndergaard 16' (Viborg)**; **Alexander Lind 26' (FCN)**; **Dorian Hanza 33' (Viborg)**; **Charly Horneman 41' (Viborg)**; FCN double substitution at 45'; Viborg triple substitution at 70'; **Adam Kleis-Kristoffersen 81' (Viborg)**.
- ESPN team statistics: **corners Viborg 4, FC Nordsjælland 5 — total 9**; possession 47.7 / 52.3; shots **20 / 14**; shots on target **6 / 2**.

Every settled row is unchanged. **Final 4-1; halftime 3-1; corners 9.** The four first-half goals (16', 26', 33', 41') are confirmed to the minute, so the Rank #1 first-half Under 1.5 was dead by the 33rd minute.

**A pre-game availability error that the 2026-09-20 pass did not catch — this is the most important new finding on this card.**

The card recorded: *"Viborg: Riahi long-term knee injury officially confirmed; current feeds also listed **Anyembe**, Freriks and Njoh unavailable."*

The ESPN confirmed team sheet for this match lists Viborg's starting XI as **Kasper Kiilerich; Daniel Anyembe, Lukas Kirkegaard, Oliver Kristensen, Hjalte Bidstrup, Jeppe Grønning, Mads Søndergaard, Asker Bech, Dorian Hanza, Charly Horneman, Sami Jalal**.

**Daniel Anyembe started.** A player the card carried as unavailable, on the authority of a third-party "current feed", was in the starting eleven. The Riahi absence was sourced to Viborg's own official medical update and was correct; the three additional names came from a non-official feed and at least one of them was wrong.

Materiality: **CONTRIBUTORY, not decisive.** The distribution failure at P-480 was a phase-total and recency-shrinkage failure, and a full-back's presence does not by itself explain four first-half goals. But the direction of the error is exactly wrong for this card — the model was already under-rating Viborg's home attacking capacity, and it was simultaneously subtracting an available starter from Viborg's XI. An availability feed that removes real starters systematically depresses the home side's modelled ceiling. That is a compounding error, not an isolated one.

Classification: this is the **mirror image of the P-481 defect** (a projected XI treated as more confirmed than it was) and the **mirror image of the P-476 success** (an obsolete absence flag correctly removed because the player appeared in the posted order). Three cards in the same mini log, one rule: **an unavailability claim from a non-official aggregator is a hypothesis, and it must be dropped the moment a team sheet contradicts it — and flagged as unverified until then.**

**Ranking metrics.**

| Metric | Model-selected slate | Supplied slate (derived from stated probabilities) |
|---|---|---|
| Rank-1 | **LOSS** (First-half Under 1.5) | **WIN** (1H Over 0.5, 0.609) |
| Hit@2 | **YES** (FCN TT Over 0.5) | **YES** |
| Wins@2 | **1 / 2** | **1 / 2** |
| NDCG@2 | **0.387** (DCG 0.6309 / IDCG 1.6309) | **0.613** |
| Row record | 2 W / 3 L | 2 W / 2 L (both forced pairs) |
| Top over/under | First-half Under 1.5 (Rank #1) — **LOSS**, `TOP_OU_REVIEW` fired and the enhanced review is above | FT Under 2.5 (0.502) — **LOSS** |
| Winner call | **LOSS** — FC Nordsjælland, p ≈ 0.411 | — |

This is the mini log's only Rank #1 failure, and the only event where Rank #1 and the top over/under are the same row, so one enhanced review covers both triggers. NDCG@2 of 0.387 is the worst on the card set and correctly reflects that the winning row was the second-ranked one.

**Mandatory validation questions.**

1. **Confirmed starting XIs?** **NO.** The accessible feed labelled both XIs projected, and the card said so. No player prop was promoted, which was correct.
2. **Bench / substitute information?** **NO.** Viborg's triple substitution at 70' produced the 81' fifth goal through Adam Kleis-Kristoffersen, who came on at 70'. A card with no bench cannot represent that path.
3. **Coaching information?** **NOT OBTAINED.**
4. **Injuries / suspensions / withdrawals?** **PARTIALLY, AND ONE ROW WAS WRONG.** Riahi (official, correct) and the FCN absences (Salquist, Araphat Mohammed, Souleymane Alio — none appear in the XI or on the bench, so those were correct). **Anyembe was listed unavailable and started.** Viborg's official preview reported no suspensions, which was consistent.
5. **Were the original sources accurate and current?** **NO — not fully.** The official Viborg and FCN material was accurate. The third-party availability feed was not, and it was used without a label distinguishing official-confirmed absences from feed-asserted ones. `METHOD.md` §1.1 requires `source_class` and `field_owner` on every material input; that was not carried through to the availability rows.
6. **Better sources available?** **YES.** ESPN `den.1` `summary?event=` returns both confirmed XIs, both benches, all substitutions with minutes, goal times and `wonCorners` in one keyless call, and it settles goal *timing*, which is what a first-half phase contract actually needs. Viborg's own matchday squad announcement is the correct pre-game authority for Viborg absences; the third-party feed should be demoted to corroboration only.
7. **Blind spots?** **YES — four, and they compound.** (a) A first-half phase Under built on a small, overlapping goal-timing sample ("FCN's last five league goals all after the 60th minute", "FCN's last two league matches were 0-0 at half") — five goals and two matches is not a basis for 75%. (b) Viborg's own home first-half attacking capacity was never given an independent branch; the phase model was constructed almost entirely from the *opponent's* recent timing. (c) No confirmed XI or bench. (d) The Anyembe availability error, which pushed in the same direction as (b).
8. **How should this be handled in future?** Four specific changes, none of which is a new coefficient. First, **a phase total may not exceed the competition/home-away phase base rate by more than a stated shrinkage allowance when the only supporting evidence is a goal-timing streak of fewer than ~10 events** — shrink hard toward the base rate and say by how much. Second, **model both sides' phase production independently**; a first-half Under requires bilateral suppression evidence, and this card had unilateral evidence. Third, prefer the **structurally shorter path**: 1H Over 0.5 needs one event, 1H Under 1.5 needs the whole half to avoid a second event; when two rows have similar stated probability, the one with fewer failure paths should outrank. Fourth, **label every availability row with its source class** and never let an aggregator-asserted absence into the XI without an official corroboration or an explicit `UNVERIFIED_ABSENCE` tag.

**Verdict on this event.** The enhanced Rank-1 / `TOP_OU_REVIEW` conducted on 2026-09-20 reached the right conclusion — FCN team total Over 0.5 should have outranked the first-half Under on frozen information — and this pass confirms it and adds a fourth contributing cause that the earlier pass missed. The corner model again held up independently of the wrong goal-total direction, landing at 9 against a 7.5 line. Classification: **not variance.** This was a knowable over-confidence built on a small timing sample, compounded by an unverified availability subtraction.

---


### P-481 — Soccer / Spain La Liga — Villarreal vs Levante

- Canonical / staging ID: P-481

- Competition: Spain La Liga, Matchday 7

- Venue: Estadio de la Cerámica, Vila-real, Spain

- Official venue-local start: Sep 20, 2026 at 18:30 CEST (Europe/Madrid, UTC+2)

- Australia/Melbourne conversion: Sep 21, 2026 at 02:30 AEST; date rollover = YES

- Original issue state: PREGAME / SCHEDULED

- Method / controls: MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-SOCCER

- Operating mode: SPORTS_ONLY / MARKET_BLIND

- Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE

#### Original pre-game prediction

Frozen goal centre:

- Villarreal \~1.85

- Levante \~1.13

- Projected total \~2.98

- Villarreal win \~54.0%; Draw \~22.6%; Levante win \~23.4%.

Best five:

1\. Villarreal team total OVER 0.5 — \~83% UNVALIDATED_SUBJECTIVE.

2\. Full-game UNDER 4.5 — \~81%.

3\. Villarreal or Draw (1X) — \~77%.

4\. First-half OVER 0.5 — \~72%.

5\. Villarreal OVER 4.5 corners — \~68%.

Supplied lines:

- First-half Over 0.5 \~72%; Under 0.5 \~28%.

- Full-game Over 2.5 \~56%; Under 2.5 \~44%.

Potential game winner: Villarreal \~54%.

#### Original research reasoning / availability

- Villarreal's underlying attack was materially stronger than its early results: current sources placed them around 12.3-12.5 xG from six league matches, with 91 shots and 39 on target.

- Levante had conceded nine in five league matches and carried an away scoring weakness in the small current sample.

- The Villarreal attack included Pépé, Moleiro, Gerard Moreno and Mikautadze in the freshest accessible lineup feed.

- A source conflict was resolved in favour of the fresher same-day team news: Juan Foyth was back available, while Santi Comesaña was out with a right-ankle problem; an older page still listing Comesaña starting was treated as stale.

- Levante's official call-up ruled out Álex Primo, Karl Etta Eyong and Hugo Sotelo.

- Villarreal had shorter rest after the Sep 17 Málaga match; Levante's scheduled midweek Athletic fixture had been postponed.

- Weather was dry and low-disruption around kickoff.

#### Material sources

1\. LaLiga official exact fixture page — event/stadium/kickoff and current competition records — https://www.laliga.com/es-GB/partido/temporada-2026-2027-laliga-ea-sports-villarreal-cf-levante-ud-7

2\. Villarreal official calendar — independent kickoff confirmation — https://villarrealcf.es/en/calendario-primer-equipo/

3\. Levante official match call-up — confirmed Álex Primo, Karl Etta Eyong and Hugo Sotelo absences — https://www.levanteud.com/en/news/convocatoria-or-villarreal-cf-levante-ud-2627

4\. AS exact-match lineup page — freshest lineup state — https://as.com/resultados/futbol/primera/2026_2027/directo/regular_a_7_6a4496c62a77870/alineaciones/amp/

5\. EFE / Mundo Deportivo — same-day Foyth return and Comesaña unavailability corroboration — https://www.mundodeportivo.com/futbol/laliga/20260920/1004229059/villarreal-mide-mejoria-pujante-levante.html

6\. StatMuse — xG/xGA/shots/SOT/possession diagnostics — https://www.statmuse.com/fc/ask/villarreal-levante-xg-xga-xgot?l=laliga

7\. MatchPulse — current-season xG cross-check — https://matchpulsestats.com/es/league/140/xg

8\. SoccerStats / PrematchStats — home/away, first-half and corner splits.

9\. Weather forecast and Sports Research Drive methodology.

Source firewall: sportsbook odds, line movement, betting previews/tips and fantasy/DFS projections were excluded.

#### Current state check

CURRENT STATUS: LIVE / NO SETTLEMENT.

The structured soccer event feed (event 72478604) showed Villarreal vs Levante live at the state refresh. No row is graded and no retrospective is performed while live.

Document mapping: none while live; retain for terminal-state settlement.

#### Settlement and retrospective — P-481

Settlement status: SETTLED / RETROSPECTIVE COMPLETE.

Verified final: Villarreal 3, Levante 1.

Halftime: 1-1.

Final corners: Villarreal 7, Levante 1.

Three-source terminal-state gate: PASS.

- Structured exact-event soccer feed, event 72478604 — COMPLETE at 3-1.

- Cadena SER / EFE exact postgame report — explicit 3-1 final and goal sequence — https://cadenaser.com/nacional/2026/09/20/villarreal-levante-resumen-resultado-y-goles-del-partido-de-la-jornada-7-de-laliga-ea-sports-cadena-ser/

- Europa Press exact match report — explicit 3-1 final, goals and final statistics — https://www.europapress.es/deportes/estadisticas-deportivas/noticia-villareal-levante-resumen-goles-resultado-partido-hoy-20260920202832.html

Corner endpoint cross-check:

- Europa Press: corners 7-1.

- Soccerzz exact match page: corners 7-1.

- Sofascore postgame analysis explicitly states the 7-1 corner count.

The corner settlement is therefore verified independently of market pages.

##### Pick-by-pick settlement — model-selected slate

1\. Villarreal team total Over 0.5 — WIN; Villarreal scored three.

2\. Full-game Under 4.5 goals — WIN; total four.

3\. Villarreal or Draw (1X) — WIN.

4\. First-half Over 0.5 goals — WIN; halftime 1-1.

5\. Villarreal Over 4.5 corners — WIN; Villarreal had seven.

Model-selected slate: 5 W / 0 L.

##### Supplied-line settlement

- First-half Over 0.5 — WIN.

- First-half Under 0.5 — LOSS.

- Full-game Over 2.5 — WIN.

- Full-game Under 2.5 — LOSS.

Potential game winner: Villarreal — WIN.

##### Rank-1 / top-two / total review

Rank #1 Villarreal TT Over 0.5 — WIN.

Rank #2 Under 4.5 — WIN.

Hit@2 = YES.

Both top-two win = YES.

The highest-ranked over/under selection, Under 4.5, WON. No enhanced failure trigger applies.

##### Expected vs actual game script

The independent centre was Villarreal 1.85, Levante 1.13, total 2.98. The actual 3-1 sat in the forecast's open Villarreal-control family. Ayoze Pérez scored at 41', Iván Romero equalised at 42', Alberto Moleiro restored the lead at 54', and substitute Georges Mikautadze completed the scoring at 86'.

The territorial mechanism was strongly supported postgame: Soccerzz records approximately 2.90 xG to 0.94, 21-6 shots, 7-1 shots on target and 7-1 corners. Villarreal's stronger attacking process therefore translated into both goals and corners.

##### What went right

- All five model-selected picks won.

- Both top-two selections won.

- Villarreal winner call won.

- The supplied 1H Over 0.5 and FT Over 2.5 directions both won.

- Villarreal TT Over 0.5 was robust to lineup changes and landed comfortably.

- Under 4.5 correctly protected against a 3-1 open game.

- Villarreal Over 4.5 corners was supported by actual territorial pressure and landed at seven.

##### Important pre-game mistake despite the wins — lineup audit

The pregame card described the freshest accessible lineup feed as showing Pépé, Moleiro, Gerard Moreno and Mikautadze in the attacking structure. The verified final lineup did NOT match that description:

- Starters included Tajon Buchanan, Alberto Moleiro, Ilias Akhomach and Ayoze Pérez.

- Nicolas Pépé, Gerard Moreno and Georges Mikautadze started on the bench.

- Mikautadze later came on and scored the 86' goal.

This is a genuine pre-game source-latency/lineup-classification defect. The fact that every team-level pick won does not erase it. The selections were robust because they were team-level, but a player prop based on the stated projected attack could have been badly wrong.

##### What went wrong / limitations

- The lineup source was treated as fresher/more definitive than it actually was.

- The final total centre of \~2.98 was somewhat low versus the realised four goals, although the distribution retained sufficient upper-tail mass for Under 4.5 and Over 2.5 to coexist.

- Levante's scoring branch was not negligible; Iván Romero's 42' equaliser confirmed that the away side could punish Villarreal despite the territorial mismatch.

##### Source-quality audit

- Europa Press / EFE-style match reporting: strong for final, scorers and team stats.

- Soccerzz: useful detailed exact-event lineup/xG/corner record.

- Sofascore postgame article: useful independent derivative corroboration.

- The pregame AS lineup page was not reliable enough to be treated as a confirmed team sheet at the issue timestamp. Future cards must preserve the label PROJECTED until a field-owner or exact-event provider explicitly marks the XI confirmed.

##### Blind spots and mitigation

Blind spot: near-kickoff lineup freshness/confirmation.

Pre-game knowability: YES — the missing official confirmation was itself observable.

Materiality: LOW for the team-level selections that were issued; potentially HIGH for any player prop.

Mitigation: do not upgrade a lineup from projected to confirmed solely because a page is same-day or recently refreshed. Require an explicit confirmation marker or field-owner team sheet.

Rule status: this is enforcement of an existing lineup-verification rule, not a new rule.

##### Document mapping

- RULES_SOCCER.md / RULES_GENERAL.md: existing projected-vs-confirmed XI distinction was not executed strictly enough; record as an execution failure.

- DATA_SOURCE_REGISTER.md: AS same-day lineup route should remain secondary unless explicit confirmation state is exposed.

- No new permanent rule required.

- Dataset remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

---

#### 2026-09-21 independent re-audit — P-481

**Re-verification of the settled final at the keyless structured lane.**

- ESPN soccer site API, `esp.1` scoreboard for 2026-09-20, event **401882857**: status `Full Time`, **Villarreal 3 — Levante 1**.
- ESPN `esp.1` summary key events: Mandi yellow 13'; **Ayoze Pérez 41'** (assisted by Alberto Moleiro); **Iván Romero 42'** (assisted by Jeremy Toljan); **halftime 1-1**; **Alberto Moleiro 54'** (assisted by Ilias Akhomach); **Georges Mikautadze 86'** (assisted by Moleiro); substitutions Gerard Moreno and Mikautadze **on at 67'**, Nicolas Pépé **on at 79'**.
- ESPN team statistics: **corners Villarreal 7, Levante 1**; possession 62.2 / 37.8; shots **21 / 6**; shots on target **7 / 1**.

Every settled row is unchanged. **Final 3-1; halftime 1-1; Villarreal 7 corners.** The corner field is now confirmed at a registered structured source rather than only at Europa Press / Soccerzz / a Sofascore article.

**The lineup defect identified on 2026-09-20 is confirmed in full, and it is worse than described.** ESPN's confirmed team sheet:

- **Villarreal XI:** Péter Gulácsi; Renato Veiga, Pau Navarro, Sergi Cardona, Alex Freeman; Alberto Moleiro, Nathan Saliba, Pape Gueye; Ayoze Pérez, Tajon Buchanan, Ilias Akhomach.
- **Villarreal bench:** Gerard Moreno, Carlos Maciá, **Georges Mikautadze**, Tani Oluwaseyi, **Juan Foyth**, **Nicolas Pépé**, Luiz Júnior, Rubén Gómez, Logan Costa, Santiago Mouriño, Alassane Diatta, Carlos Romero.

The pregame card described the Villarreal attack as "Pépé, Moleiro, Gerard Moreno and Mikautadze". **Three of those four started on the bench.** Only Moleiro started. Juan Foyth, whose return to availability the card specifically resolved in favour of the fresher same-day source, also did not start. Santi Comesaña, correctly recorded as out, appears in neither the XI nor the bench — so the availability call was right and the **starting-XI call was wrong**.

Set against P-478 in the same mini log, the contrast is exact and instructive:

| Card | Lineup projection method | Result vs confirmed team sheet |
|---|---|---|
| P-478 | Starting XI from each club's **own official report of its last league match**, cross-checked against a current independent feed, published as **projected** | **22 of 22 names correct** |
| P-481 | A **same-day third-party lineup page** (AS), treated as "the freshest accessible lineup state" | **3 of 4 named attackers wrong**; also wrong on Foyth |

"Same-day" is a recency property, not a confirmation property. A same-day page that has not yet ingested the official team sheet is simply a stale projection with a fresh timestamp, and treating it as more authoritative than the club's own last official XI is a source-hierarchy inversion.

**Ranking metrics.**

| Metric | Model-selected slate | Supplied slate (derived from stated probabilities) |
|---|---|---|
| Rank-1 | **WIN** (Villarreal TT Over 0.5) | **WIN** (1H Over 0.5, 0.72) |
| Hit@2 | **YES** | **YES** |
| Wins@2 | **2 / 2** | **2 / 2** |
| NDCG@2 | **1.000** | **1.000** |
| Row record | **5 W / 0 L** | 2 W / 2 L (both forced pairs) |
| Top over/under | Full-game Under 4.5 (Rank #2) — **WIN** | FT Over 2.5 (0.56) — **WIN** |
| Winner call | **WIN** — Villarreal, p ≈ 0.54 | — |

**Why the picks survived a wrong lineup, and why that is not reassurance.** Every model-selected row was a **team-level** target: Villarreal to score at least once, the match to stay under 4.5, Villarreal-or-draw, a first-half goal, Villarreal over 4.5 corners. None of those depends on which individual starts. The territorial thesis — Villarreal's underlying attack being far stronger than its early results — was confirmed emphatically postgame (about 2.90 xG to 0.94, 21-6 shots, 7-1 shots on target, 7-1 corners). **The forecast was right for the right reason and the lineup was wrong at the same time.** Five wins from five is not evidence that the lineup retrieval worked; it is evidence that the targets chosen were robust to it. A single player prop on Pépé, Moreno or Mikautadze would have been built on a false premise.

**Mandatory validation questions.**

1. **Confirmed starting XIs?** **NO — and, unlike every other card in this mini log, this one did not say so clearly enough.** The card described the AS page as "the freshest accessible lineup feed" and used its player list as if it were the attacking structure. The `PROJECTED` label must survive until a field owner or exact-event provider explicitly marks the XI confirmed.
2. **Bench / substitute information?** **NO.** The 86' third goal came from Mikautadze, an unmodelled 67' substitute; the 79' introduction of Pépé is likewise a bench event. Two of Villarreal's three goals involved players the card had placed in the starting XI and who were in fact substitutes.
3. **Coaching information?** **NOT OBTAINED.** Villarreal had short rest after a Sep 17 Málaga fixture and Levante's midweek Athletic game had been postponed — a rotation-relevant asymmetry the card did identify. Villarreal did in fact rotate. The card had the *reason* to expect rotation and still published a non-rotated XI.
4. **Injuries / suspensions / withdrawals?** **YES and correct.** Levante's official call-up ruled out Álex Primo, Karl Etta Eyong and Hugo Sotelo — none appear. Comesaña out and Foyth available were both correct as **availability** statements. The card conflated availability with selection.
5. **Were the original sources accurate and current?** **MIXED.** LaLiga official, the Villarreal calendar, the Levante official call-up, StatMuse and MatchPulse were all accurate. The AS lineup page was not accurate as a team sheet and was over-weighted.
6. **Better sources available?** **YES.** ESPN `esp.1` `summary?event=` provides both confirmed XIs, both benches, every substitution with its minute, goal times with assists and `wonCorners` — one keyless call that would have settled every field this card had to assemble from four separate providers. For pre-game use, the confirmed XI appears in the same `rosters` block once the team sheet is published (typically one hour before kick-off), which is a cleaner confirmation gate than reading a newspaper lineup page.
7. **Blind spots?** **YES — two.** (a) Lineup confirmation state, as above. (b) The total centre of ~2.98 was slightly low against a realised four goals, but the distribution retained enough upper-tail mass for Under 4.5 and Over 2.5 to coexist, so this is a minor calibration observation rather than a failure.
8. **How should this be handled in future?** One hard rule, which already exists and was not executed: **a lineup may only be labelled confirmed when the source explicitly exposes a confirmation marker or is the club/league team sheet itself.** Add one operational test that makes the rule self-enforcing: before publishing a projected XI, check it against the club's own most recent official match report; where the two disagree, publish the union with both labelled, and never name a specific attacking quartet as "the" structure. Also: when the card has already identified a **short-rest rotation risk**, that is a positive reason to widen the XI uncertainty, not to publish a single XI with more confidence.

**Verdict on this event.** Best raw result in the mini log — 5 W / 0 L on the model-selected slate, correct winner, correct on both supplied directions, and a territorial thesis confirmed by the postgame data. It also contains the mini log's clearest process failure. Both statements are true at once and the record should keep both. Recurring-mistake **M19 (published lineup not retrieved / projected treated as confirmed)** applies squarely.

---


## 4. General Learnings, Rule Changes, Observations, and New Sources

All figures below are **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE** descriptive diagnostics on eight events across five sports. Eight events is not a sample from which calibration, edge or model quality can be inferred, and nothing here is a prospective validation. Every probability referenced is `UNVALIDATED_SUBJECTIVE`.

### 4.0 What the eight events actually show

#### Ranking metrics, by slate

| ID | Slate | Rank-1 | Hit@2 | Wins@2 | NDCG@2 | Rows | Winner call |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|
| P-474 | supplied (only ranked slate) | W | YES | 2/2 | 1.000 | 2 W / 2 L | **W** |
| P-475 | model-selected | W | YES | 2/2 | 1.000 | 4 W / 0 L | **W** |
| P-475 | supplied | W | YES | 1/2 | 0.613 | 2 W / 2 L | — |
| P-476 | model-selected | W | YES | 2/2 | 1.000 | 2 W / 2 L | **W** |
| P-476 | supplied | W | YES | 2/2 | 1.000 | 3 W / 1 L | — |
| P-477 | model-selected | W | YES | 2/2 | 1.000 | 2 W / 2 L | **W** |
| P-477 | supplied | W | YES | 1/2 | 0.613 | 2 W / 2 L | — |
| P-478 | model-selected | W | YES | 1/2 | 0.613 | 3 W / 2 L | **L** |
| P-478 | supplied | W | YES | 2/2 | 1.000 | 2 W / 2 L | — |
| P-479 | model-selected | W | YES | 2/2 | 1.000 | 4 W / 0 L | **W** |
| P-479 | supplied | W | YES | 1/2 | 0.613 | 2 W / 2 L | — |
| P-480 | model-selected | **L** | YES | 1/2 | **0.387** | 2 W / 3 L | **L** |
| P-480 | supplied | W | YES | 1/2 | 0.613 | 2 W / 2 L | — |
| P-481 | model-selected | W | YES | 2/2 | 1.000 | 5 W / 0 L | **W** |
| P-481 | supplied | W | YES | 2/2 | 1.000 | 2 W / 2 L | — |

**Model-selected slates (the free, information-bearing slates), 7 cards:** Rank-1 **6 / 7**; Hit@2 **7 / 7**; both-of-top-two **5 / 7**; rows **22 W / 9 L** across 31 rows; mean binary Brier **0.1965**.

**Winner calls, 8 cards:** **6 W / 2 L**; mean Brier **0.1684**. Both losses were soccer: P-478 Djurgården (p ≈ 0.602) and P-480 FC Nordsjælland (p ≈ 0.411 — a call the card itself did not rate above even money).

**NDCG@2 definition used here.** Binary relevance; DCG@2 = rel₁ + rel₂ / log₂3; IDCG@2 is drawn from the whole ranked slate's realised relevances (1.6309 when the slate contains two or more winners, 1.0 when it contains exactly one, undefined when it contains none). No slate in this mini log was a total blank, so NDCG@2 is defined everywhere.

#### The supplied-slate "record" is almost entirely mechanical — treat it accordingly

This is the most important measurement finding of the pass, and it applies to every future card that ranks a user-supplied four-contract slate.

Across the eight cards, the supplied slates contain **32 rows**. Of those:

- **28 rows form 14 strict complementary pairs** (Over/Under on a half-line, or spread/counter-spread). Exactly one row of each pair wins by construction. These pairs generated **14 guaranteed wins** regardless of forecast quality.
- **4 rows are genuinely informative** — the two moneyline/run-line pairs at P-474 (Guardians ML, Athletics +1.5) and P-476 (Angels ML, Twins +1.5), which are *not* complements because both can win when the favourite wins by exactly one run. These produced **3 W / 1 L**.

Total: 17 W / 15 L — of which **14 wins were arithmetic**. The honest decision-level reading is:

| Supplied-slate view | Result | Brier |
|---|---|---|
| Forced-pair preferred sides, counted once each (13 half-line/spread decisions) | 9 W / 4 L | 0.2007 |
| Non-complementary rows (4) | 3 W / 1 L | 0.1794 |
| P-476 Over 7.0 (push-capable, scored separately) | WIN | complete W/P/L 0.2255; decisive q = 0.5541 → 0.1988 |

`SCORING_AND_VALIDATION.md` §3 already requires the preferred side of a forced pair to be counted once in a decision score. The practical consequence for reporting is blunt: **never state a supplied-slate row record as if it were a performance figure.** A card that ranks four supplied contracts made of two complementary pairs will report "2 W / 2 L" whatever it forecasts. This mini log's honest supplied-slate signal is 13 near-coin-flip decisions at a 0.2007 Brier, which is worse than the free-slate 0.1965 — as expected, because the supplied lines sat close to the model's own centres on almost every card.

#### Where the forecasts were strong, and where they were not

**Strong, repeatedly and for stated reasons:**

- **Winner/side direction** — 6 of 8, including both cricket and NBL underdocumented competitions.
- **"Team X scores at least once" / team-total floors** — Rank #1 on three soccer cards, won on all three (P-478, P-481; P-480's equivalent row was Rank #2 and won).
- **Corners, modelled independently of goals** — 3 for 3 (P-478 11 v 7.5; P-480 9 v 7.5; P-481 Villarreal 7 v 4.5), and two of those three landed on cards where the goal-side view was wrong. Independence of the corner model from the goal model is doing real work and must be preserved.
- **Phase-to-innings separation in T20** — P-479's powerplay centre (~45 v realised 41) and innings corridor (145–175 v realised 150) were both right simultaneously.
- **Dependence reasoning on the top two** — P-476 named the exact one-run overlap state in advance and it occurred.

**Weak, repeatedly:**

- **Full-game and phase Unders.** Losses at P-475 (U176.5), P-476 (U8.5), P-477 (U191.5), P-480 (1H U1.5 and FT U3.5). Every one of these lost because the card's own documented upper-tail mechanism fired — late relief and extras, favourite bench offence, favourite perimeter burst, home first-half conversion. **Not one of these was an unforeseeable event.** In each case the mechanism was written down in prose and given no weight in the threshold calculation.
- **Central totals under-estimated the realised total on 6 of 8 cards** (P-474 8.34 v 18; P-475 175.9 v 187; P-476 7.35 v 11; P-477 186.7 v 201; P-480 2.68 v 5; P-481 2.98 v 4). Only P-478 (2.81 v 3) and P-479 (~160 v 150) were close or high. **This is a signal worth logging and is explicitly not yet a rule** — see §4.8. Eight events cannot establish a centre bias, `C-RUN-CENTRE-BIAS` is already development-only under `SCORING_AND_VALIDATION.md` §5, and a generic Over tilt is exactly what that section prohibits. But six of eight in the same direction, with a consistent stated mechanism (documented upper tails not carried into the threshold arithmetic), is a hypothesis with a mechanism attached rather than a bare streak.

### 4.1 Cross-sport learnings

1. **A documented tail that is not given weight is not modelled.** This is the single recurring cause of loss in this mini log. P-474's two-starter collapse, P-475's favourite bench ceiling, P-476's extras tail, P-477's perimeter burst and P-480's home first-half conversion were all *named in the card* and none was carried into the threshold arithmetic. The fix is mechanical: any mechanism named in the failure-mode prose must appear as a weighted branch in the frozen distribution, or be explicitly declared as excluded with a reason. This is recurring-mistake **M15** (control listed, not executed) and it appears on five of eight cards.
2. **Prefer the shorter failure path when two rows have similar probability.** P-480 ranked 1H Under 1.5 (needs the entire half to avoid a second goal) above rows that needed one event. P-475 ranked a full-game Under (needs both teams' totals to stay jointly low) above a favourite team-total Over already priced at 77%. Where stated probabilities are close, path geometry should break the tie toward the row with fewer ways to lose.
3. **An unavailability claim from a non-official aggregator is a hypothesis.** P-480 removed a player from the XI who started; P-476 correctly restored a player an obsolete flag had removed; P-481 treated a same-day third-party page as a team sheet. All three are the same failure class in different directions: availability source class was not carried through to the row.
4. **Team-level targets are robust to lineup error; player-level targets are not.** P-481 went 5 W / 0 L on a materially wrong XI because every row was team-level. That is a reason to be **more** disciplined about player props, not a reason to relax lineup verification.
5. **Independence between derivative models and the main outcome model is valuable and should be protected.** The corner models won twice on cards whose goal models were wrong. Deriving corners from possession/xG dominance would have destroyed that independence.
6. **Do not rank both ends of a narrow corridor as two of the "best" targets.** P-477 held Over 179.5 and Under 191.5 simultaneously around a 186.7 centre. They share one driver, cannot both win outside a ~12-point band, and are not two independent trials.
7. **Start-crossing handling held up.** Four of the eight cards (P-474, P-475, P-478, and P-479 in substance) were issued at or after the scheduled start. In every case the card failed preflight on `PF-EVENT-STATE`, labelled itself a late-issued research forecast, and admitted no live-state information. No settled row shows contamination. The exception process is working and should not be used as an argument for weakening the normal pregame gate — but note that the one card that issued cleanly pregame (P-476) was also the only card with both confirmed lineups. **Late issuance and thin participant evidence travel together.**

### 4.2 Sport-specific learnings

**Baseball (MLB).**

- When both starters carry a documented contact/HR tail, the joint two-starter-failure state needs explicit mass before any total or team-total Under is ranked (P-474). `RULES_BASEBALL` BB-B2/BB-B3/BB-B5 already require it.
- Any alternate Under must be tested against `P(tie after nine) + P(late relief-transition crossing)`, not just the distance from the central total (P-476). BB-B5/BB-B7 already require it.
- Integer totals were handled correctly at P-476: three-state W/P/L, no forced complement, push explicitly not counted as a win. Preserve this.
- The MLB Stats API (`schedule`, `game/{pk}/linescore`, `game/{pk}/boxscore`) settles every MLB field used in this mini log with no narrative interpretation. It should be the first settlement route.

**Basketball (WNBA / NBL).**

- A depleted underdog does not make the full game Under. Twice in this mini log the *favourite's* ceiling consumed the total budget (P-475 Atlanta 106; P-477 Sydney 111). The favourite's team-total Over and the full-game Under must be reconciled in the same joint states before the Under is ranked.
- Blowout states do not reliably suppress scoring: reduced defensive intensity plus productive bench minutes can raise the total while widening the margin (P-475 Borlase 18 in 19 minutes; P-477 six Kings in double figures).
- High-volume low-efficiency perimeter shooting by the losing side sustains pace while losing the game (P-477 Cairns 13-of-44). Margin and total can both go up together; this is a joint state, not two separate ones.
- Round-one / post-off-season / high-roster-turnover games deserve wider dispersion, not a narrower corridor (P-477). Candidate test only — see §4.8.

**Soccer.**

- Corners: keep them independent of the goal model. Build from corner-exposure rates plus score-state width. 3 for 3 here.
- Phase (first-half) totals built on small goal-timing samples are the weakest construct in the set (P-480). Shrink hard toward the competition/home-away phase base rate.
- Away-win branches for competent visiting sides are being compressed too far (P-478: 17.9% for a 34-point side away at a strong home team). Floor against the competition away-win base rate unless a named suppression mechanism justifies going below it.
- Substitution-driven defensive transition decided P-478 and contributed to P-480's fifth goal. A bench is not optional context in soccer; it is an input to the second-half distribution.
- Team-total "over 0.5" rows on the stronger side were the most reliable soccer row type in this mini log (3 for 3 at 0.75–0.84).

**Cricket (T20).**

- Powerplay and full-innings must be modelled as linked but distinct quantities. Modelling the innings as a multiple of the powerplay would have failed at P-479; modelling them separately got both right.
- A subdued powerplay followed by recovery is a real and common state, and a recent same-fixture example of it (36/2 → 190/4) is a width argument, not a centre shift. The card got this right.
- **New:** when every supplied contract is conditioned on a named team batting first, the toss is an activation gate. P-479 issued four toss-conditional rows without the toss and was one coin-flip from a `CONDITION NOT MET` outcome like P-445.

### 4.3 Potential rule changes

Ordered by strength of evidence. Nothing here is asserted as validated; each is a proposal with its evidence and its status.

| # | Proposal | Evidence in this mini log | Status | Target document |
|---|---|---|---|---|
| R-A | **Named-mechanism closure.** Any mechanism named in a card's failure-mode prose must appear as a weighted branch in the frozen distribution or be explicitly declared excluded with a reason. | 5 of 8 cards (P-474, P-475, P-476, P-477, P-480) | **Strong — execution rule, adds no coefficient.** Recommend adoption. | `METHOD.md` §4 field 3; `CONTROLS.md` |
| R-B | **Availability source-class tagging.** Every availability row carries `source_class` and `field_owner`; a non-official aggregator absence is tagged `UNVERIFIED_ABSENCE` and may not remove a player from a modelled XI on its own. | P-480 (Anyembe started while listed unavailable); P-476 (correct removal of a stale flag); P-481 | **Strong — enforces an existing `METHOD.md` §1.1 requirement that was not carried through.** Recommend adoption. | `METHOD.md` §1.1; `RULES_GENERAL.md` §16; `DATA_SOURCE_REGISTER.md` |
| R-C | **Lineup-projection hierarchy.** The club's own official report of its most recent match, cross-checked against a current independent feed, outranks a same-day third-party lineup page. Recency is not confirmation. | P-478 22/22 exact by the first method; P-481 3-of-4 attackers wrong by the second | **Strong, but n = 2.** Recommend adoption as a source-hierarchy rule; record as a standing test. | `RULES_SOCCER.md`; `SOURCES.md`; `DATA_SOURCE_REGISTER.md` |
| R-D | **Toss as an activation gate in cricket** when the supplied slate is conditioned on a named team batting first: recover it, or rank explicitly conditional on activation and state the activation probability. | P-479; precedent P-445 (`CONDITION NOT MET`, all four rows NO ACTION) | **Strong — closes a known failure mode already realised once.** Recommend adoption. | `RULES_CRICKET.md`; `LEAGUE_RULES_CRICKET.md` |
| R-E | **Phase-total shrinkage floor.** A phase total supported only by a goal-timing streak of fewer than ~10 events may not depart from the competition/home-away phase base rate by more than a stated shrinkage allowance, and the allowance must be printed. | P-480 (75% on five goals and two matches) | **Moderate — mechanism clear, magnitude not derived.** Adopt the *disclosure* requirement now; the magnitude stays `NOT_YET_DERIVED`. | `RULES_SOCCER.md`; `RECENCY_AND_REBOUND.md` (`R-1` family) |
| R-F | **Corridor rows count once.** An upper Under and a lower Over drawn from the same frozen centre are one corridor decision, not two targets. | P-477 | **Moderate.** Consistent with `SCORING_AND_VALIDATION.md` §3. | `SCORING_AND_VALIDATION.md` §3; `METHOD.md` §4 field 4 |
| R-G | **Forced-pair reporting discipline.** A supplied-slate row record may not be presented as a performance figure; the preferred side of each complementary pair is counted once and the mechanical component is stated. | All 8 cards; 14 of 17 supplied wins were arithmetic | **Strong — a reporting-honesty rule, no forecasting effect.** Recommend adoption. | `SCORING_AND_VALIDATION.md` §3; `EXTERNAL_LOGGING_WORKFLOW.md` |
| R-H | **Away-win base-rate floor** in soccer for a competent visiting side, absent a named suppression mechanism. | P-478 (17.9%) | **Weak — n = 1.** Log as a candidate test; do not adopt. | `RULES_SOCCER.md` (candidate) |

**Explicitly rejected as rule candidates:**

- **Any generic Over tilt or fixed centre adjustment.** Six of eight centres were low, but `SCORING_AND_VALIDATION.md` §5 prohibits an unexplained signed lean, and one mini log cannot establish a centre bias. The mechanism (unweighted tails) is addressed by R-A, which is a process fix, not a coefficient.
- **Any rule designed to make one side of every total win.** The user's own brief prohibits it and it would be unjustifiable: the Under losses here were caused by specific, identifiable, fixable mechanism omissions, not by the Under side being structurally wrong.
- **Down-ranking Rank-#1 candidates generally after P-480.** One Rank-1 loss in eight events, with an identified cause, is not evidence that the ranking objective is wrong.

### 4.4 Algorithm improvements

1. **Threshold-crossing budget as a required output for every ranked total.** Instead of "centre 7.35, line 7.0, gap +0.35", print the mass of each named state that crosses the threshold: `P(tie after nine) = 0.1425`, `P(late relief transition adds ≥2) = …`, and so on. The centre-and-gap display (already mandated by the 19 Sep display directive) tells you where the distribution sits; it does not tell you which states move it across the line. The four Under losses in this mini log are all threshold-crossing failures, not centre failures.
2. **Joint budget reconciliation before ranking a mismatch total.** `P(favourite TT ≥ x)` against `P(underdog TT ≤ total − x)` in the same frozen states, printed. P-475 would have shown the contradiction immediately.
3. **Path-geometry tiebreak.** Where two ranked rows are within a stated tolerance of each other, rank the one with fewer failure paths first, and record that the tiebreak was applied.
4. **Bench/substitution branch with explicit weight** in soccer winner and team-total distributions whenever the favourite is expected to chase or protect a lead.
5. **Keep derivative models structurally independent** of the primary outcome model. Corners earned their place here precisely because they were not derived from the goal model.

### 4.5 Source improvements

**Newly demonstrated in this pass, with what each is good for.**

| Source / route | Best used for | Evidence from this pass |
|---|---|---|
| `site.api.espn.com/apis/site/v2/sports/soccer/{league}/summary?event={id}` | **Confirmed starting XIs, full benches, substitutions with minutes, goal times and assists, and `wonCorners`** — the complete settlement and lineup-audit package for an ESPN-covered soccer competition, in one keyless call | Settled P-478, P-480 and P-481 finals, halftimes, goal minutes, corner counts (4-7, 4-5, 7-1) and both team sheets for each |
| `site.api.espn.com/.../soccer/{league}/scoreboard?dates=YYYYMMDD` | Terminal-state confirmation (`Full Time`) with explicit status, not just a score | Confirmed all three soccer finals |
| `statsapi.mlb.com/api/v1/game/{pk}/linescore` and `/boxscore` | Innings played, per-inning runs, team totals, margins, individual pitcher lines — settles MLB totals, run lines and pitcher props without narrative | Settled P-474 and P-476 including the 11-inning endpoint and both `5 K` lines |
| `site.api.espn.com/.../basketball/wnba/summary?event={id}` | **Per-player `starter` boolean and `didNotPlay` flag**, plus full team shooting splits | Resolved Natasha Cloud DNP and confirmed Atlanta's exact starting five at P-475 |
| ESPNcricinfo full scorecard via `r.jina.ai` | **Explicit `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - N runs, W wickets)` match note**, toss, fall of wickets, did-not-bat list | Settled P-479's 41/1 powerplay and confirmed Chapman/Miller absent from the XI |
| Austadiums exact-event records | Independent third lineage for Australian fixtures where ESPN has no coverage | Corroborated P-477 111-90 with venue, date and start time |

**Sources demoted or flagged by this pass.**

- **CricketWorld** — supplied P-479's powerplay field on 2026-09-20; on 2026-09-21 it returns a bot-verification wall through both the direct route and the text proxy. Reclassify as *intermittently available*; do not rely on it as a required lineage for a phase field when ESPNcricinfo carries the same match note.
- **WinDrawWin / BetStudy / TotalCorner** — used to settle the P-478 corner row. They gave the right number, but a registered structured source publishes the same field and was not used. Keep them as a last-resort research-only fallback, explicitly below the ESPN `wonCorners` route, and never as predictive evidence.
- **AS same-day lineup page (`as.com/.../alineaciones/`)** — must remain `PROJECTED` unless it exposes an explicit confirmation marker. It was materially wrong at P-481.
- **Third-party availability feeds (generic)** — wrong on Anyembe at P-480. Demote to corroboration; official club matchday squad announcements own the field.
- **NBL public schedule shell** — displays `LIVE NOW` on fixtures that have not started. Confirmed again this pass. Never an event-state authority.
- **Syndicated recaps** — the BBC-via-Yahoo P-479 summary misnamed Devon Conway as "Paul Conway". Recaps do not own player-level fields; scorecards do.
- **The structured soccer event feed used at issue time** — still returned `Scheduled` after kick-off had passed at P-478. Adequate as one lineage; not sufficient alone for event state.

### 4.6 Data-quality observations

1. **Confirmed lineups were obtained for both sides on exactly one of eight cards** (P-476). That is the headline data-quality number of this mini log. On P-478 the projection happened to be exact; on P-481 it was materially wrong; on the remaining five it was uncapturable or capped.
2. **A bench was obtained on zero of the five cards where a bench mattered.** Benches decided or contributed to the outcome at P-478 (both Elfsborg's and Djurgården's), P-480 (Kleis-Kristoffersen's 81' goal after a 70' introduction), P-475 (Borlase 18 from the bench), P-481 (Mikautadze's 86' goal after a 67' introduction) and P-477 (six Kings in double figures).
3. **Intra-provider cache inconsistency is normal, not exceptional.** MLB's all-club lineup index had full orders while its own team pages showed TBD (P-476); a club's official preview promised a squad one hour before kick-off and never refreshed through the accessible route (P-478); the structured soccer feed showed `Scheduled` after kick-off (P-478). Each was correctly logged rather than hidden. This is a retrieval-latency pattern that should be expected and planned around, not treated as an anomaly each time.
4. **Every settlement in this mini log now rests on at least four distinct lineages**, and every derivative field (corners, powerplay) is settled from a source that publishes the field directly rather than from an inference.
5. **Coaching/manager information was obtained on zero of eight cards.** On most it was genuinely immaterial. On P-481 it was not: the card identified a short-rest rotation risk and then published a single non-rotated XI.

### 4.7 Recurring blind spots

Mapped to the existing recurring-mistake registry so repeat offences are countable rather than re-described.

| Registry item | Where it appears in this mini log | Repeat? |
|---|---|---|
| **M14** — total probability not derived from the card's own centre/width | P-475 (Under ranked against the card's own 77% favourite TT Over), P-476 (U8.5 against the card's own tie mass) | Yes — previously logged 2026-09-09 |
| **M15** — control listed but not executed | P-474, P-475, P-476, P-477, P-480, and the P-478 source-selection variant | **Yes, and dominant — 6 of 8 cards.** This is the highest-frequency defect in the set |
| **M17** — small-sample rate used as direction | P-480 (five goals, two matches → 75%) | Yes |
| **M19** — published lineup not retrieved / projected treated as confirmed | P-481 squarely; P-480's availability variant; P-474/P-475/P-477/P-478/P-479 as known missingness correctly labelled | Yes |
| **M11** — unit-performance uncertainty converted into an Over lean | Not observed. Uncertainty was represented as width on every card | No — this control is holding |
| **M10** — kill path stated as prose rather than a weighted branch | This is the mechanism behind M15 here; the kill paths were written and not weighted | Yes |

**New blind spot not previously in the registry — candidate M20: "complementary-pair record reported as performance."** A supplied slate built from complementary pairs produces a fixed row record independent of forecast quality, and reporting it alongside free-slate results invites a false read. Proposed as an addition to the registry with the R-G reporting rule.

### 4.8 Items requiring more evidence before becoming formal rules

1. **Central-total under-estimation.** Six of eight centres sat below the realised total. Mechanism (unweighted documented tails) is plausible and is addressed by R-A as a *process* fix. **Do not convert into a coefficient.** Required before any promotion: per-sport separation, actual means versus medians, a chronological out-of-sample block, and a comparison against the frozen empirical baseline per `SCORING_AND_VALIDATION.md` §4. Status: **development observation, continues `C-RUN-CENTRE-BIAS`.**
2. **Round-one / post-off-season variance widening (basketball).** n = 1 (P-477). Needs a systematic sample of opening-round games across NBL/NBA/WNBA seasons with a pre-specified dispersion metric. Status: **candidate test.**
3. **Away-win base-rate floor (soccer).** n = 1 (P-478). Needs the actual competition away-win base rates and a check of how often recent cards have gone below them. Status: **candidate test (R-H).**
4. **Lineup-projection hierarchy (R-C).** n = 2, but with a clear mechanism and an unusually clean contrast (22/22 versus 3-of-4 wrong). Recommend adopting as a source-hierarchy rule now — it costs nothing and removes a known failure — while continuing to record hit rates for both methods.
5. **Whether team-level target selection should be formalised as a hedge against lineup uncertainty.** P-481 suggests it, but "choose robust targets" can degenerate into choosing uninformative ones. Needs a definition that distinguishes robustness from triviality before it can be a rule. Status: **not ready.**

### 4.9 Open handles outside this mini log — 2026-09-21 re-probe

Recorded here because Phase 8 requires checking whether other entries still require settlement. **None of these belongs to this mini log, and none blocks it.**

The 23 primary handles (Part-2 custody 9, Part-3 custody 13, Part-4 custody 1) plus the documentary/period audits remain open. The Part-3 soccer corner handles are **not open because the value is unknown** — ESPN values are already recorded against them (P-399 17, P-401 17 / IFK 8, P-407 Brugge 9, P-409 Troyes 5, P-410 Leipzig 8, P-419 2+2, P-430 Al Ain 2). They are open because each card **pre-registered a specific field owner** (Lega Serie A, Allsvenskan/SEF, Pro League, LFP, DFL, AFC) and §16.10(j) forbids booking at a provider that was not pre-registered. Refusing to book them is the correct, outcome-independent application of the rule — at P-430 the unbooked evidence points to a *loss*, which is the clearest possible demonstration that the rule is not being applied opportunistically.

Re-probe results, 2026-09-21:

| Pre-registered field owner | Route attempted | Result |
|---|---|---|
| Allsvenskan (P-401, P-419) | `allsvenskan.se/match/6529990` | **HTTP 404** — still unreachable |
| SEF / Everysport API (P-401, P-419) | `api.everysport.com/v1/events/{id}` | **HTTP 401** — requires an API key |
| DFL / Bundesliga (P-410) | `bundesliga.com` match facts | **HTTP 403** — still unreachable |
| Pro League (P-407) | `proleague.be` | Site reachable, no exact-event corner field exposed on the accessible route |

**Structural observation worth escalating.** Pre-registering a settlement provider that does not publish the target field creates a permanently unsettleable row. Seven derivative rows have now been open for a week or more with the correct value already in hand from a registered structured source, purely because the pre-registration named the wrong owner. The rule protects against outcome-driven provider shopping and should be kept. But the pre-registration step should require a check that the named provider actually publishes the field — otherwise the control converts a solvable settlement into a permanent gap. Proposed as a `RULES_GENERAL.md` §16.10 clarification: **a settlement provider may only be pre-registered for a derivative field if that provider is known to publish that field**; where it does not, pre-register the structured route that does (for soccer corners, ESPN `wonCorners`).

### 4.10 Audits reviewed and archived in this pass

Reviewed against their own closure statements and against the current authority chain (`METHOD.md` MDS-2026.09.19-v4.3 / CR-2026.09.19-4, `AUDIT_IMPLEMENTATION_2026-09-19.md`). Archived where closed, superseded or redundant **and** not cited by a currently governing operational document. Files cited only by `LEARNING_REGISTER.md` were treated as archivable, because that register is itself an evidence archive and `METHOD.md` §9 classifies dated retrospectives and audit snapshots as evidence, not active instructions.

| Document | Disposition | Reason |
|---|---|---|
| `PREDICTION_MINI_RUNNING_LOG_P452_ONWARD.md` (folder) | **ARCHIVED** | All 22 entries settled with retrospectives complete; superseded by this mini log; next ID P-474 confirmed contiguous |
| `AUDIT_CHANGELOG_2026-09-06.md` | **ARCHIVED** | Its one outstanding item (retro-tagging ~86 pre-`L-095` lessons) was formally closed as not-to-be-done in `AUDIT_IMPLEMENTATION_2026-09-19.md` §4 |
| `AUDIT_CHANGELOG_2026-09-06_OVERHAUL.md` | **ARCHIVED** | Historical record of a pass implemented in full the same day; no active citation |
| `AUDIT_CHANGELOG_2026-09-07.md` | **ARCHIVED** | Closed settlement/ledger pass; cited only by the learning register |
| `AUDIT_CHANGELOG_2026-09-09.md` | **ARCHIVED** | Closed; no active citation |
| `AUDIT_CHANGELOG_2026-09-11.md` | **ARCHIVED** | Its one outstanding item (`statsapi battingOrder` lineup route "not yet demonstrated pre-game") was closed as demonstrated in `AUDIT_IMPLEMENTATION_2026-09-19.md` §3 |
| `AUDIT_CHANGELOG_2026-09-12.md` | **ARCHIVED** | Closed; no active citation |
| `COMPREHENSIVE_RETROSPECTIVE_2026-08-22.md` | **ARCHIVED** | P-001–P-060 retrospective under MDS-2026.08.22-v1.1; superseded twice over |
| `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-02.md` | **ARCHIVED** | Superseded by the 2026-09-05 and 2026-09-12 audits |
| `GAME_LOG_LEDGER_2026-09-06.md` | **ARCHIVED** | Superseded by `GAME_LOG_STATUS_CURRENT.md`; no active citation |

**Retained in place despite being historical**, because a currently governing document links to them and moving them would break an active reference: `AUDIT_CHANGELOG_2026-09-05.md` (cited by `AGENT_ROLE_AND_TASK.md`, `EXTERNAL_LOGGING_WORKFLOW.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`), `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md` (`RULES_GENERAL.md`, `DATA_SOURCE_REGISTER.md`), `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-12.md` (`GAME_LOG_STATUS_CURRENT.md`, `SOURCES.md`, `PERFORMANCE_ELIGIBILITY_POLICY.md`), `FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md`, `GAME_LOG_BLINDSPOT_REVIEW_2026-09-06.md`, `GAME_LOG_STATUS_INDEX_2026-09-05.md`, `IMPROVEMENT_PLAN_2026-09-06.md`, `PREGAME_ELIGIBILITY_REGISTER_2026-09-05.md`.

**Retained as current authority, not archivable:** `METHOD.md`, `SCORING_AND_VALIDATION.md`, `CONTROLS.md`, `CONTROL_MANIFEST_2026-09-19.md`, `FORECAST_PREFLIGHT_MANIFEST.md`, `MODEL_REVIEW_2026-09-17.md` (linked from `METHOD.md` and `README.md`), `AUDIT_IMPLEMENTATION_2026-09-17.md` (linked from `METHOD.md` §10), `AUDIT_IMPLEMENTATION_2026-09-19.md` (the current control revision ledger), `GAME_LOG_STATUS_CURRENT.md`, all `RULES_*.md`.

**Findings judged outdated or redundant during this review:**

- `AUDIT_CHANGELOG_2026-09-11.md`'s claim that the `statsapi battingOrder` lineup route was "proposed, not yet demonstrated pre-game" is **outdated** — it was demonstrated on 2026-09-19. Ironically, P-474 still fell back to a CBS/STATS secondary rather than using it, which is why this is listed under §4.5 as an execution gap.
- The `L-095` / `L-096` backlog item ("retro-tag ~86 pre-`L-095` lessons") is **closed as not-to-be-done** and should not be reopened; the correct unit was active controls, which are now classified in `CONTROLS.md`.
- `GAME_LOG_STATUS_INDEX_2026-09-05.md`'s "6/25 top-two and 13/13 main-line O/U" summaries are **superseded** by explicitly enumerated denominators, and — in light of §4.0 — any such headline O/U rate computed over complementary pairs should be treated as structurally inflated regardless of which audit produced it.
- `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md`'s settlement-only performance-eligibility framing is **superseded** by the 2026-09-12 LEARNING_ONLY directive and by `PERFORMANCE_ELIGIBILITY_POLICY.md`.

## 5. Document Update Mapping

Where each learning should eventually be incorporated. **No governing document was modified by this pass.** The mini log is the only file rewritten; archiving moved closed audit files without editing their contents.

| # | Learning / change | Target document | Section | Type |
|---|---|---|---|---|
| 1 | R-A named-mechanism closure — a named failure mechanism must be a weighted branch or an explicit exclusion | `METHOD.md` | §4 compact object, field 3 (Joint distribution) | Execution rule |
| 2 | R-A operational check | `CONTROLS.md` | per-card gate list | New gate |
| 3 | R-B availability source-class tagging; `UNVERIFIED_ABSENCE` label | `METHOD.md` §1.1; `RULES_GENERAL.md` §16 | provenance fields / participant freeze | Enforcement of existing requirement |
| 4 | R-B register entry for third-party availability feeds | `DATA_SOURCE_REGISTER.md` | availability field ownership | Source demotion |
| 5 | R-C lineup-projection hierarchy (club's own last official XI > same-day third-party page) | `RULES_SOCCER.md`; `SOURCES.md`; `DATA_SOURCE_REGISTER.md` | lineup retrieval | Source hierarchy |
| 6 | R-D toss as activation gate for batting-first-conditional slates | `RULES_CRICKET.md`; `LEAGUE_RULES_CRICKET.md` | activation / contract identity | New blocking gate |
| 7 | R-E phase-total shrinkage disclosure (magnitude `NOT_YET_DERIVED`) | `RULES_SOCCER.md`; `RECENCY_AND_REBOUND.md` | phase totals / `R-1` family | Disclosure requirement |
| 8 | R-F corridor rows count once | `SCORING_AND_VALIDATION.md` §3; `METHOD.md` §4 field 4 | decision counting | Scoring clarification |
| 9 | R-G forced-pair reporting discipline; no supplied-slate row record presented as performance | `SCORING_AND_VALIDATION.md` §3; `EXTERNAL_LOGGING_WORKFLOW.md` | decision metrics / log presentation | Reporting-honesty rule |
| 10 | Candidate **M20** "complementary-pair record reported as performance" | `LEARNING_REGISTER.md` recurring-mistake registry | M-series | New registry entry |
| 11 | M15 repeat count (6 of 8 cards) | `LEARNING_REGISTER.md` | M15 evidence rows | Evidence update |
| 12 | Threshold-crossing budget as required output for every ranked total | `METHOD.md` §4 field 4; `RULES_BASEBALL.md`; `RULES_BASKETBALL.md`; `RULES_SOCCER.md` | totals presentation | Algorithm/output change |
| 13 | Joint budget reconciliation (favourite TT Over vs full-game Under) | `RULES_BASKETBALL.md` controls 11/17/18 | mismatch totals | Execution reinforcement |
| 14 | Path-geometry tiebreak between close-probability rows | `METHOD.md` §4 field 4 | ranking | Ranking clarification |
| 15 | Bench/substitution branch carries explicit weight in soccer winner and team-total distributions | `RULES_SOCCER.md` | score-state transitions | Execution reinforcement |
| 16 | Preserve independence of the corner model from the goal model | `RULES_SOCCER.md` | corner process | Preserve-as-is note |
| 17 | MLB two-starter joint-collapse branch | `RULES_BASEBALL.md` BB-B2/BB-B3/BB-B5 | starter states | Execution reinforcement |
| 18 | MLB alternate-Under tie/extras crossing mass | `RULES_BASEBALL.md` BB-B5/BB-B7 | relief transition, extras | Execution reinforcement |
| 19 | ESPN soccer `summary?event=` as primary settlement + lineup route (`wonCorners`, XIs, benches, subs, goal times) | `DATA_SOURCE_REGISTER.md`; `SOURCES.md`; `RULES_SOCCER.md` | settlement routes | New/promoted source |
| 20 | MLB Stats API `linescore`/`boxscore` as first MLB settlement route | `DATA_SOURCE_REGISTER.md`; `RULES_BASEBALL.md` | settlement routes | New/promoted source |
| 21 | ESPN WNBA `summary?event=` `starter`/`didNotPlay` for participation settlement and pre-tip availability testing | `DATA_SOURCE_REGISTER.md`; `RULES_BASKETBALL.md` | availability/settlement | New/promoted source |
| 22 | ESPNcricinfo `Powerplay 1` match note as registered T20 phase-field route; CricketWorld reclassified intermittent | `DATA_SOURCE_REGISTER.md`; `RULES_CRICKET.md` | phase settlement | Source promotion + demotion |
| 23 | Austadiums as independent third lineage for Australian fixtures; NBL schedule shell is never an event-state authority | `DATA_SOURCE_REGISTER.md`; `RULES_BASKETBALL.md` | event state | New source + source warning |
| 24 | WinDrawWin / BetStudy / TotalCorner demoted below the ESPN `wonCorners` route; research-only fallback, never predictive | `DATA_SOURCE_REGISTER.md`; `SOURCES.md` | corner fields | Source demotion |
| 25 | Pre-registered settlement provider must be known to publish the target field | `RULES_GENERAL.md` §16.10 | derivative settlement | Rule clarification — unblocks 7 stalled rows |
| 26 | P-452–P-481 canonical import and register extension; the `next ID P-438` line in the status register is stale | `PREDICTION_LOG_COMBINED_4.md`; `GAME_LOG_STATUS_CURRENT.md` | queue / canonical index | Ledger integrity — **do this before issuing P-482** |
| 27 | Late issuance and thin participant evidence co-occur; keep the start-crossing exception but do not weaken the pregame gate | `EXTERNAL_LOGGING_WORKFLOW.md`; `METHOD.md` §3 | issuance | Process observation |
| 28 | Candidate tests: round-one variance widening; away-win base-rate floor; central-total under-estimation | `LEARNING_REGISTER.md` | prospective-test archive | Candidate tests, not rules |

**Proposed new document — not created.** `TOTALS_THRESHOLD_BUDGET.md`. Purpose: a single cross-sport specification for the threshold-crossing budget (item 12) — which states must be enumerated per sport, how their mass is printed, and how the budget is reconciled against team-total rows before a total is ranked. Justification: items 12, 13, 17 and 18 are the same requirement re-expressed in four sport files, and the four Under losses in this mini log are all instances of it. A single specification referenced from each `RULES_<SPORT>.md` would stop it being restated inconsistently. **This is a proposal only; no document was created.**

## 6. Settlement Lists

### Settled logs — first to most recent

1. **P-474** — Athletics @ Cleveland Guardians, MLB — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Cleveland 12-6; total 18. Supplied slate 2 W / 2 L; Rank-1 WIN; winner WIN.
2. **P-475** — Chicago Sky @ Atlanta Dream, WNBA — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Atlanta 106-81; total 187. Model slate 4 W / 0 L; supplied 2 W / 2 L; Rank-1 WIN both slates; `TOP_OU_REVIEW` fired on supplied Under 176.5; winner WIN.
3. **P-476** — Minnesota Twins @ Los Angeles Angels, MLB — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Angels 6-5 in 11 innings; total 11. Supplied 3 W / 1 L; model slate 2 W / 2 L; Rank-1 WIN both slates; winner WIN.
4. **P-477** — Sydney Kings vs Cairns Taipans, NBL — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Sydney 111-90; total 201. Model slate 2 W / 2 L; supplied 2 W / 2 L; Rank-1 WIN both slates; winner WIN.
5. **P-478** — Djurgårdens IF vs IF Elfsborg, Allsvenskan — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Elfsborg 2-1; HT 0-1; corners 4-7 (11). Model slate 3 W / 2 L; supplied 2 W / 2 L; Rank-1 WIN; winner LOSS.
6. **P-479** — Edinburgh Castle Rockers vs Belfast Wolves, ETPL Final — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Belfast 150/5 (PP 41/1); Edinburgh 151/3 in 18.4, won by 7 wickets. Model slate 4 W / 0 L; supplied 2 W / 2 L; Rank-1 WIN both slates; winner WIN.
7. **P-480** — Viborg FF vs FC Nordsjælland, Superligaen — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Viborg 4-1; HT 3-1; corners 4-5 (9). Model slate 2 W / 3 L; supplied 2 W / 2 L; **Rank-1 LOSS — enhanced Rank-1 + `TOP_OU_REVIEW` completed**; winner LOSS.
8. **P-481** — Villarreal vs Levante, La Liga — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Villarreal 3-1; HT 1-1; corners 7-1. Model slate 5 W / 0 L; supplied 2 W / 2 L; Rank-1 WIN both slates; winner WIN. Records a confirmed pre-game lineup defect despite the clean result.

### Logs still awaiting settlement — first to most recent

**None.** No entry in this mini log is unsettled, unresolved, live, delayed, suspended, postponed, abandoned or cancelled.

For completeness, the open items that exist **elsewhere** in the ledger and are not part of this mini log are listed in §4.9: 23 primary handles (Part-2 custody 9, Part-3 custody 13, Part-4 custody 1 — `P-430-C05`) plus the documentary/period audits, including `P-255-C05` and `P-256-C05` as `UNRESOLVED_PERIOD` and `P-418` as `RESULT_NOT_RECOVERED`. Re-probed 2026-09-21; all pre-registered field owners remain unreachable; no handle changed state.

## 7. Running Integrity Notes

- Governing methodology remains **MDS-2026.09.19-v4.3 / CR-2026.09.19-4**. Historical cards keep the method/control version under which they were issued; nothing was retrofitted.
- The dataset remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. Settlement does not confer performance eligibility (`METHOD.md` §7). No EV, ROI, edge or calibration claim follows from anything in this document.
- **No issued forecast, probability, rank, selection, reasoning or canonical ID was altered by the 2026-09-21 pass.** Every original pre-game card is preserved verbatim. All additions are dated, appended settlement and audit material, per `METHOD.md` §6.
- **No settled row changed.** The re-audit confirmed all eight finals and every graded row.
- **Three new findings were added** that the 2026-09-20 pass did not have: the P-480 Anyembe pre-game availability error; the P-478 lineup-projection result (22 of 22 names correct) and the source-hierarchy conclusion that follows from contrasting it with P-481; and the P-478 corner-evidence downgrade, where betting-branded pages were used to settle a field that a registered structured source publishes.
- **Two settlement-evidence upgrades were applied** without changing any outcome: soccer corner fields now rest on ESPN `wonCorners`, and the P-479 powerplay field now rests on the ESPNcricinfo match note (CricketWorld has since gone behind a bot wall and is no longer reproducible).
- **One pre-game uncertainty was resolved:** Natasha Cloud (P-475) did not play.
- Market odds, line movement, betting tips, tipsters and fantasy/DFS material were **not** admitted as predictive evidence on any card. Betting-branded pages appear only as historical settlement cross-checks at P-478, and this pass replaces them with a structured non-market route.
- **No governing methodology file, rules file, canonical prediction log or register was edited.** Nine closed or superseded audit documents and the fully settled P-452 mini-log folder were moved to the Drive archive with their contents unchanged; every proposed rule change is recorded in §5 as a mapping, not applied.
- **Ledger action required before the next issue:** import P-452–P-481 into `PREDICTION_LOG_COMBINED_4.md`, extend `GAME_LOG_STATUS_CURRENT.md` past P-451, and remove the stale "next ID `P-438`" line. Under `METHOD.md` §3 step 7 an overdue unregistered external log blocks the next forecast.
- Next intended prediction ID: **P-482**, subject to that reconciliation.
