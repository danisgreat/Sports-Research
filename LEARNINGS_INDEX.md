# Learnings index — every lesson, test and recurring mistake, one line each

**Opened 2026-09-26.** This is the navigable index of `LEARNING_REGISTER.md`, which stays the evidence record with the full origin of every entry. **Status: LEARNING_ONLY.** Nothing here is a coefficient, cap or ranking override (`L-087`).

**Maintenance (`C-READING-GATE`).** Every new L-, G-L-, M- or test ID added to the register is added here in the same pass, with its status. If a line here and its register entry disagree, the register governs and this index is corrected.

**Status words.** PROMOTED = operative process/disclosure control · NARROWED = partly operative (the operative part is named) · TESTING = open prospective test, no ranking effect · REFERENCE = a measured rate used as context · WITHDRAWN / REJECTED / SUPERSEDED = never apply · CLOSED_UNTESTED = closed 2026-09-26 without a test (re-register with a v2 manifest).

---

## 1. What the settled record shows (2026-09-26 figures)

Source: `research/settled_rows_2026-09-25/` (rebuilt 2026-09-25(e); 1,264 graded rows from 315 cards, 641 with a probability). Hindsight on self-selected cards; card-cluster intervals.

1. **Calibration is good; skill is modest.** Decision Brier 0.2268, slope 1.01, skill +6.6% over climatology.
2. **No skill over a naive population table yet.** Seed check +0.0101 (card − baseline), interval [−0.059, +0.089]. Prospective count 0/100.
3. **Only strong rows carry information.** p ≥ 0.65 won about 80%; 0.50–0.65 won 53.6% (coin flips).
4. **Only Rank 1 separates:** 66.4% against 54–56% for Ranks 2–4.
5. **Underdog cushions outside baseball are over-confident:** 17/40 at a stated 0.642; the population cover for a small cushion is 0.32–0.54. Baseball +1.5 is calibrated.
6. **By sport:** soccer has the strongest resolution (74.8% at 0.700; 37 cards; interval spans 0). NPB/KBO show some. Cricket has resolution but is mis-stated. MLB (0.0075) and basketball (0.012) have near-zero resolution. Tennis, NFL/NCAA and AFL show none and are over-confident.
7. **By market:** phase totals, team totals and corners beat full-game totals and handicaps. On shared cards, phase 30/36 against full-game 27/41.
8. **Joint failure of the top two matches independence:** 14.4% observed against 14.5% expected.
9. **Cohort Brier trends follow the sport mix,** not method improvement.
10. **Widths run narrow:** basketball totals about 39% too narrow (mean z² 1.93). Centres are unbiased.
11. **No rebound anywhere measured;** the last game is the worst predictor in 6/6 competitions.
12. **High stated probabilities are not over-confident:** 79/100 prospective rows at p ≥ 0.70 won 91.1% against a stated 79.3%.

---

## 2. Recurring mistakes (check every card)

| ID | Mistake | Control |
|---|---|---|
| M1 | Exact-winner over-trust | G30.1 |
| M2 | Non-loss / double chance over-ranked | Soccer rules |
| M3 | Totals stacked off one factor | Baseball control 26 |
| M4 | Overtime/blowout tail ignored beside phase Unders | G-L1 |
| M5 | Cushion on a cold side missing its key player | Kill paths |
| M6 | Reputation or returning ace against a park suppressor | Baseball rules |
| M7 | Elite ceiling against a "tough venue" Under | Cricket rules |
| M8 | Bottom slot never tested | G23.1, G27 |
| M9 | Stale cached or proxy source | Source freshness |
| M10 | Kill path as prose, not mass | G-L1 |
| M11 | Uncertainty turned into a directional lean | G-L2 |
| M12 | Tier gap read as scoring shape | G-L3; no EPL-to-cup transfer |
| **M13** | **Aggregate used where the game log was one click away (highest-value check)** | G-L7 |
| M14 | Total probability not derived from the card's own centre and width | G-L8; `tools/card_math.py` |
| M15 | Control listed, not executed | `audit_card_controls.py`; `C-READING-GATE` |
| M16 | Complement not itemised | G-L9 |
| M17 | Small-sample rate used as direction | G-L11 |
| M18 | Top two structurally anti-coupled | G-L10 |
| M19 | Published lineup not retrieved | G14.2; `RETRIEVAL_MISS` |
| M20 | Model summary used as the record | G-L13 |
| M21 | Settlement route not consulted | G-L14 |
| M22 | Period-scope mismatch | G-L16 |
| M23 | "At least one O/U won" read as success | G-L15, G-L22 |
| M24 | State-contaminated evidence window | Cricket control 21; G-L7 |
| M25 | Personnel claim without retrieval or receipt | `C-LINEUP-DIFF`; S-1 Rev 2 receipt |
| M26 | Process record written, not read | `C-PROCESS-RECORD-PROVENANCE`; `C-SETTLEMENT-FROM-FEED` |
| M27 | Single-game predictive rule promoted | `C-PROMOTION-RECEIPT` |
| M28 | Covering-pair record read as skill | G-L22(c) `COVERING_PAIR` |
| M29 | Summary row retyped, not copied | `C-SUMMARY-FROM-CARD` |
| M30 | City forecast instead of the gamefeed wind | `RULES_BASEBALL.md` B-2 |
| M31 | Width chosen without a reference | `C-WIDTH-BENCHMARK`; `C-WIDTH-Z` |
| M32 | Non-baseball cushion priced like a baseball +1.5 | `C-PLUS-CUSHION`; RM-1 |
| M33 | Rule churn outruns evidence | `C-RULE-FREEZE`; one manifest per day |
| M34 | Self-selected sample read as the competition | `C-EVENT-UNIVERSE`; `T-UNIVERSE-VS-SELECTED` |

---

## 3. Promoted lessons L-001 to L-122

All PROMOTED unless marked. Origins and full wording: `LEARNING_REGISTER.md` §2 and the dated sections.

### Identity, time, state and custody
| ID | Lesson | Status |
|---|---|---|
| L-001 | Freeze identity, rules, contract, interval, state and information cutoff before analysis | PROMOTED |
| L-014 | Potential-winner aliases share the canonical contract ID | PROMOTED |
| L-016 | Freeze the whole candidate slate, geometry and dependence before ranking | PROMOTED |
| L-022 | Preserve the freeze basis and exact issued text | NARROWED (no git-only gate) |
| L-026 | Live analysis needs official state or two independent agreeing sources, else no live forecast | PROMOTED |
| L-027 | Decision-driving participants pass an identity handshake | PROMOTED |
| L-034 | One canonical ID per event; alias map; mark duplicate storage | PROMOTED |
| L-035 | A file's creation time proves only that version; later cards need their own hash | PROMOTED |
| L-036 | "Mathematically won" live rows stay open until the official final | PROMOTED |
| L-040 | Model event-before-termination and termination-before-event paths | PROMOTED |
| L-046 | Cutoff before scheduled start, else fail closed | PROMOTED |
| L-065 | Method version from a fresh in-session read | PROMOTED |
| L-071 | Host-qualified event IDs and explicit field semantics | PROMOTED |

### Sources and evidence
| ID | Lesson | Status |
|---|---|---|
| L-002 | Authority, freshness, importance and access are separate fields | PROMOTED |
| L-004 | Classify every source row against the exact line before computing a rate | PROMOTED |
| L-024 | Route each claim to its field owner; final refresh of volatile fields | PROMOTED |
| L-030 | Quarantine stale or zero-filled official placeholders | PROMOTED |
| L-044 | Validate IDs, dates and chronology even on official domains | PROMOTED |
| L-045 | Keep conflicting provider values; settle only when invariant across them | PROMOTED |
| L-049 | Atomic record per claim; count each underlying event once | PROMOTED |
| L-067 | Native-language search for KBO, NPB, CPBL, LMB | PROMOTED |
| L-074 | Verbatim page text on sparse sites (ETPL) | PROMOTED |
| L-079 | No synthetic (AI-generated) content | PROMOTED |
| L-080 | Structured endpoint before narrative | PROMOTED |
| L-081 | Derivative-row gradability is a coverage test, not a market-type ban | PROMOTED |
| L-092 | Settlement source pre-registered before any niche market is ranked | PROMOTED |
| L-100 | "Market-blind" means blind to prices, not market-independent | PROMOTED |
| L-111 | Base-rate populations state inclusion rules and reconcile identities | PROMOTED |
| L-113 | A "cannot fail" source rung can fail; allow UNKNOWN | PROMOTED |
| L-122 | Keep the toss fact separate from exact-strip evidence | PROMOTED |

### Building the distribution
| ID | Lesson | Status |
|---|---|---|
| L-003 | One coherent event distribution; every contract derived from it | PROMOTED |
| L-005 | Live forecasts use remaining exposure, not elapsed pace | PROMOTED |
| L-006 | Role-specific replacement chains; workload predicts availability, not performance | PROMOTED |
| L-007 | Model the target event itself (shots are not corners) | PROMOTED |
| L-008 | AFL chain: ruck/clearance → inside-50 → shot quality → conversion | PROMOTED |
| L-009 | Cricket phases, wickets and late acceleration are separate distributions | PROMOTED |
| L-010 | Handicaps decompose into win, narrow-loss and separation | PROMOTED |
| L-023 | A derivative market needs its own causal chain | PROMOTED |
| L-029 | Freeze baseline and current-regime branches when they conflict | PROMOTED |
| L-031 | Enumerate both sides' win paths | PROMOTED |
| L-032 | Win-conditioned cover counts are descriptive | PROMOTED |
| L-033 | Explain why a named adverse branch stays subordinate | PROMOTED |
| L-037 | Volume, allocation and margin are separate steps | PROMOTED |
| L-038 | Lineups become exposure by phase | PROMOTED |
| L-039 | Carry the full phase-end state forward | PROMOTED |
| L-041 | Sparse or new-regime data widens; it does not move the centre | PROMOTED |
| L-042 | Map participants to the target phase and role | PROMOTED |
| L-043 | Stress low/high × close/separated families | PROMOTED |
| L-047 | A line inside central support caps evidence at LOW; solve component budgets | PROMOTED |
| L-048 | Opposite-sign mechanisms modelled separately | PROMOTED |
| L-050 | Pre-toss cricket: bat-first/chase mixture | PROMOTED |
| L-051 | Run GFA-2 with the sport's SFA | PROMOTED |
| L-052 | Retrieve L5/L10/L15/L20 descriptively | NARROWED (the statistical trend test is WITHDRAWN) |
| L-053 | Record a reference base rate; extra-condition audit | NARROWED (band anchor and movement cap superseded) |
| L-054 | Venue classification and venue-coordinate hourly weather, wind as a vector | PROMOTED |
| L-056 | Two independent conditions signals | PROMOTED |
| L-058 | Separation budget for every margin row | PROMOTED |
| L-059 | A weak participant widens the opponent's branch only | PROMOTED |
| L-061 | Cricket cards show the pitch-report search trail | PROMOTED |
| L-062 | Streak persistence-versus-reversion audit, both directions | PROMOTED |
| L-063 | Extension endpoints use their own scoring rate | PROMOTED |
| L-064 | Competition/round-specific knockout baseline; no automatic suppression | NARROWED |
| L-066 | Reconcile a regime move against the latest continuity-qualified H2H | PROMOTED |
| L-068 | Native units and signed margins (tennis shortcut fixed) | PROMOTED |
| L-069 | Failed lineup gates propagate into final ranks | PROMOTED |
| L-070 | Both sides' win and separation states contract-evaluable | PROMOTED |
| L-075 | Reserve/debutant production propagated into the exposure chain | PROMOTED (disclosure); magnitude CLOSED_UNTESTED |
| L-076 | Exhibition margins excluded when a core rotation is absent | PROMOTED (exclusion); magnitude CLOSED_UNTESTED |
| L-077 | Personnel-loss discount conditioned on the opponent's roster | PROMOTED (disclosure); magnitude CLOSED_UNTESTED |
| L-082 | Coach, bench and rotation record | PROMOTED |
| L-083 | Phase totals retrieve runs and wickets | NARROWED by L-112 (no bimodal-shape claim from thin samples) |
| L-084 | Aggregate tail-budget disclosure | WITHDRAWN as construction (pseudo-tails, CR-3); tails come from the joint distribution |
| L-085 | Path-geometry disclosure | WITHDRAWN as a ranking device (CR-3) |
| L-105 | Dimensional check before any formula | PROMOTED |
| L-106 | "True union" is a settlement fact | PROMOTED |
| L-107 | Summed order statistics are a sensitivity scenario only | PROMOTED |
| L-112 | Two observations do not establish a distribution shape | PROMOTED |

### Ranking and coherence
| ID | Lesson | Status |
|---|---|---|
| L-011 | A streak moves a rank only once its cause is shown | PROMOTED |
| L-018 | Likelihood rank, proper scoring and the top-two portfolio are separate objectives | PROMOTED |
| L-055 | Classify slate geometry (forced pairs v free rows) | PROMOTED |
| L-057 | Rank 1 defines a state; re-solve the others conditional on it | PROMOTED |
| L-060 | Winner from win-branch mass; reconcile with a cushion | PROMOTED |
| L-073 | Blanket corners Rank-1 cap | SUPERSEDED by L-081 |
| L-088 | Rank-gap field | PROMOTED |
| L-097 | Tail/coherence blindspot already covered | PROMOTED (cross-reference) |
| L-098 | Winner/handicap/total coherence already covered on paper | PROMOTED (cross-reference) |
| L-108 | Marginal ranking ≠ joint coherence | PROMOTED |
| L-109 | A strong cushion doesn't force an underdog winner | PROMOTED |

### Scoring, evaluation and honesty
| ID | Lesson | Status |
|---|---|---|
| L-012 | Time-ordered validation, proper scores, frozen baselines | PROMOTED |
| L-013 | Outcome grade ≠ process grade | PROMOTED |
| L-015 | Pre-declared D0 case retrieval | PROMOTED |
| L-017 | Separate D0/H0/E1 sets and probability states | PROMOTED |
| L-019 | Train → tune → calibrate → untouched test | PROMOTED |
| L-020 | Features admitted with leakage tests | PROMOTED |
| L-021 | VALUE needs calibrated probabilities and same-time prices | PROMOTED (no value claim exists) |
| L-025 | Separate market-blind, market-only and market-informed lanes | PROMOTED; the post-settlement closing-line lane is `C-MARKET-BENCHMARK` |
| L-028 | Process-defective picks still count in the headline record | NARROWED |
| L-072 | User-confirmed freeze; honest denominators | PROMOTED |
| L-078 | Settlement is the eligibility gate | PROMOTED (all records currently LEARNING_ONLY) |
| L-086 | No archiving with unsettled cards unless the whole slate is preserved | PROMOTED |
| **L-087** | **Firewall: integrity/disclosure promote; weights need a prospective test** | PROMOTED (RM-1 is the one user-authorised exception) |
| L-089 | Two-pass retrospectives, result-blind first | PROMOTED |
| L-090 | Stratified scorecards | PROMOTED |
| L-091 | Raw W/L is never the headline | PROMOTED |
| L-093 | Unresolved rows are informative missing data | PROMOTED |
| L-094 | Issue-time grade separate from later-rule gap | PROMOTED |
| L-095 | Control classes (blocking / mechanism / context) | PROMOTED |
| L-096 | Control-effectiveness review | PROMOTED |
| L-099 | Evidence-density labels per sport | PROMOTED |
| L-101 | P-241–P-267 reproducibility-limited | PROMOTED |
| L-102 | Recompute rates from the table on the page | PROMOTED |
| L-103 | Check raw text before declaring an omission | PROMOTED |
| L-104 | The firewall applies to new gates too | PROMOTED |
| L-110 | Audit the reasoning, not only the result | PROMOTED |
| L-114 | A later match cannot prove an earlier cause | PROMOTED |
| L-115 | Check corridor containment numerically | PROMOTED |
| L-116 | Reconcile team identity before generalising | PROMOTED |
| L-117 | Knowable-before-issue v in-game shock, by timestamp | PROMOTED |
| L-118 | "Strengthened", not "new", when tightening a rule | PROMOTED |
| L-119 | Research grade v operator action | PROMOTED |
| L-120 | Numbered gates govern; dated sections explain | PROMOTED |
| L-121 | Cross-reference to L-090 | PROMOTED (cross-reference) |

---

## 4. General-algorithm lessons G-L1 to G-L24 (`RULES_GENERAL.md` §16)

| ID | Lesson | Status |
|---|---|---|
| G-L1 | Outcome families enumerated with mass; kill paths as weighted branches | PROMOTED |
| G-L2 | Uncertainty is width, not a lean (shrinkage may move mean and variance when declared) | PROMOTED (as corrected) |
| G-L3 | Tier/promotion translation | Watch item; disclosure via soccer control 31 |
| G-L4 – G-L6 | Winner ≠ margin; decompose creation/finishing; in-game shocks are aleatory | Reinforcements |
| G-L7 | Open the disaggregated record before an aggregate carries direction | PROMOTED |
| G-L8 | Derive each probability from the card's own distribution | PROMOTED; normalised-edge **ordering** WITHDRAWN |
| G-L9 | Itemise the complement across kill paths | PROMOTED |
| G-L10 | Print P(R1 ∧ R2) and its coupling sign | PROMOTED |
| G-L11 | Real denominators and uncertainty before a small-sample direction | PROMOTED (as corrected) |
| G-L12 | Declared margin prior; uncertainty widens, not centres toward pick'em | PROMOTED |
| G-L13 | A model-summarised retrieval is not a record | PROMOTED |
| G-L14 | Execute the settlement route | PROMOTED |
| G-L15 | Label O/U rows FORCED_PAIR or FREE | PROMOTED |
| G-L16 | Settling record's period scope matches the contract's | PROMOTED |
| G-L17 | Print P(¬R1 ∧ ¬R2) and name the shared state | PROMOTED |
| G-L18 | Allocation marginals and an opponent-contribution branch | PROMOTED |
| G-L19 | Complete end-state family (ties included) before any winner label | PROMOTED |
| G-L20 | A current comparable that already cleared the line gets mass | PROMOTED |
| G-L21 | P(all fail) with Fréchet bounds when three or more rows share a driver | PROMOTED |
| G-L22 | A forced pair is one decision; covering pairs labelled | PROMOTED |
| G-L23 | Read the process record before amending a control | PROMOTED |
| G-L24 | Exact signed-margin queries per competition | PROMOTED |

---

## 5. Dated lessons, 2026-09-12 to 2026-09-26

| ID | Lesson | Status |
|---|---|---|
| L-20260912-01 | Exact CDF/outcome mass and push handling replace absolute-edge ordering | PROMOTED |
| L-20260912-02 | Disjoint complete-game states and joint bounds | PROMOTED |
| L-20260912-03 | Real sample denominators; withdraw equal-n and two-SE claims | PROMOTED |
| L-20260912-04 | Starters, bench and coaches separately; no backdating | PROMOTED |
| L-20260912-05 | Record the first decisive checkpoint and extra-period exposure | PROMOTED (weights TESTING) |
| L-20260912-06 | Cricket wickets/resources × phase scoring | CANDIDATE (mechanism in cricket controls 19–21) |
| L-20260912-07 | Field-level source checks; branding can't certify every field | PROMOTED |
| L-20260912-08 | Exclude market-derived prose from MARKET_BLIND analysis | PROMOTED |
| L-20260912-09 | Frozen preferred O/U; explicit denominators | PROMOTED |
| L-20260912-10 | Document custody; restore before declaring absent | PROMOTED |
| L-20260915-01 | Test winner labels need a time budget, not a series aggregate | PROMOTED (cricket control 28) |
| L-20260915-02 | Current-series innings table is the Test phase prior | PROMOTED (cricket control 27) |
| L-20260915-03 | Quarantine numbers in search summaries | Reinforcement |
| L-20260915-04 | A missing log gets an inventory, not new IDs | PROMOTED |
| L-20260915-05 | UAE Pro League has no ESPN coverage | Source state |
| L-20260915-06 | Underdog cushions 10 W / 13 L at 0.61 → G-L12 | PROMOTED |
| L-20260915-07 | C-UNDERDOG-SEPARATION → C-MARGIN-TAIL-MASS | SUPERSEDED (2026-09-26: by T-PLUS-CUSHION / T-RM1) |
| L-20260915-08 | First 25-card review | REVIEW (primary population not beating 0.5) |
| L-20260915-09 | C-PROB-EXTREMITY not supported this cohort | TESTING continues |
| L-20260915-10 | C-RUN-CENTRE-BIAS not supported this cohort | TESTING continues |
| L-20260915-11 | Phase v full total: soccer 1H 7/9; cricket 3/3 | TESTING (`C-PHASE-VS-FULL-TOTAL`) |
| L-20260915-12 | Sparse fixtures confirmed at federation level | PROMOTED |
| L-20260915-13 | Derivatives settle from the official record | PROMOTED |
| L-20260915-14 | Team-corner rows need corner generators | PROMOTED (soccer control 33) |
| L-20260915-15 | Same-competition meeting is current evidence | PROMOTED (basketball control 25) |
| L-20260915-16 | Run-line decomposition; IL-return hook; home-last-bat mass | PROMOTED (baseball control 29) |
| L-20260915-17 | NFL margin prior, key numbers, prior-season ratings as width | PROMOTED (gridiron controls 17–19) |
| L-20260915-18 | Mini-log candidate dispositions | Recorded |
| L-20260915-19 | Import checks | PROMOTED |
| L-20260916-01 | A summarised fetch is not a record → G-L13 | PROMOTED |
| L-20260916-02 | Settlement route executed → G-L14 | PROMOTED |
| L-20260916-03 | League corner route table | PROMOTED (soccer control 35) |
| L-20260916-04 | P-418 origin correction | CORRECTION |
| L-20260916-05 | O/U geometry disclosure → G-L15; C-OU-GEOMETRY | PROMOTED; the test SUPERSEDED 2026-09-26 |
| L-20260916-06 | Disruption facts at settlement | PROMOTED (soccer control 34) |
| L-20260916-07 | NFL non-offensive TD branch (18.8% of games) | PROMOTED (gridiron control 20) |
| L-20260916-08 | P(favourite covers ∧ Under) | PROMOTED (gridiron control 21) |
| L-20260916-09 | Starter-exit transition inning | PROMOTED (baseball control 30) |
| L-20260916-10 | Repeatable-v-variance table; batting pitcher branch | PROMOTED (basketball 25; baseball 31b) |
| L-20260916-11 | Fingerprint every drop-location variant | PROMOTED |
| L-20260916-12 | Part-3 custody count | CORRECTION |
| L-20260916-13 | Period scope → G-L16 | PROMOTED |
| L-20260916-14 | UEFA match finder lane | Source promotion |
| L-20260916-15 | Threshold-invariant v knife-edge derivative rows | PROMOTED (disclosure) |
| L-20260917-01 | Shared failure state of the top two → G-L17 | PROMOTED |
| L-20260917-02 | Allocation marginals → G-L18 | PROMOTED |
| L-20260917-03 | Ties in the end-state family → G-L19 | PROMOTED |
| L-20260917-04 | Direct comparable already cleared the line → G-L20 | PROMOTED |
| L-20260917-05 | Single-team scoring rows above 0.80 without an XI | PROMOTED (soccer control 37; no cap) |
| L-20260917-06 | High probabilities not over-confident | TESTING continues |
| L-20260917-07 | O/U geometry development cohort | Historical only |
| L-20260917-08 | Cross-league defence widens the separation tail | PROMOTED (soccer control 39) |
| L-20260917-09 | Bowling replacement chain | PROMOTED (cricket control 31) |
| L-20260917-10 | Strikeout-floor prop gate | PROMOTED (baseball control 33) |
| L-20260917-11 | Start-crossing fail-close confirmed | Confirmation |
| L-20260917-12 | KBO scoreboard degraded | Source state |
| L-20260917b-01 | P(all fail) with Fréchet bounds → G-L21 | PROMOTED |
| L-20260917b-02 | Suppression lowers a −1.5 too → G-L21(2) | PROMOTED |
| L-20260917b-03 | Winner labels inherit ranked-row evidence → G-L21(3) | PROMOTED |
| L-20260917b-04 | Forced pairs score 2–2 by construction → G-L22 | PROMOTED (measurement) |
| L-20260917b-05 | Read the process record first → G-L23 | PROMOTED |
| L-20260917b-06 | MLB P(margin = 1 \| win) ≈ 28% | PROMOTED (baseball control 34, as corrected) |
| L-20260917b-07 | Extras: P(tie after 9) 8.75% | PROMOTED (baseball control 37, as corrected) |
| L-20260917b-08 | Push mass from the conditional distribution | PROMOTED (baseball control 35; the 12% cap WITHDRAWN) |
| L-20260917b-09 | Venue base rate beside the line | PROMOTED (disclosure) |
| L-20260917b-10 | Score-state relief ladder before a run line is Rank 1 | PROMOTED (baseball control 36) |
| L-20260917b-11 | Sibling phase lines from one distribution | PROMOTED (soccer control 40) |
| L-20260917b-12 | Conditional activation validated | PROMOTED (cricket control 32) |
| L-20260917b-13 | BK-P1 fail-close held | Confirmation |
| L-20260917b-14 | JS-only field owner is a render escalation | PROMOTED (basketball control 27) |
| L-20260917b-15 | Known settlement route not executed | Execution failure (G-L14) |
| L-20260917b-16 | Extremity failures cluster by card | TESTING continues |
| L-20260917b-17 | O/U geometry third cohort | Historical only |
| L-20260917b-18 | Phase Under held while the full Under died | Evidence for `C-PHASE-VS-FULL-TOTAL` |
| L-20260917b-19 | Lineups were not the binding constraint | OBSERVATION (no rule) |
| L-20260917b-20 | Good practice to preserve (official squad over third-party absence claims) | KEEP |
| L-20260917b-21 | `audit_card_controls.py` rebuilt and wired in | PROMOTED |
| L-20260917b-22 | Field 5a missing on 13/13 cards | Confirms M15 |
| L-20260917b-23 | Unauditable logs marked BODY_NOT_CARRIED | PROMOTED |
| L-20260917b-24 | Every sport has a cushion band → G-L24 | PROMOTED |
| L-20260917b-25 | One maintained `BASE_RATES_REGISTER.md` | PROMOTED |
| L-20260919-01 – 04 | No MLB rebound; calibre doesn't change it; no pitcher rebound; shorter windows predict worse | PROMOTED (`R-1`) |
| L-20260919-05 | P-453's win was directionally lucky | CORRECTION |
| L-20260919-06 – 07 | X, Reddit and Bluesky unusable; handle identity fails | Source state |
| L-20260919-08 | Press conferences: availability and role only | PROMOTED (`S-2`) |
| L-20260919-09 | `LINEUPS_NOT_YET_PUBLISHED` distinct from `RETRIEVAL_MISS` | PROMOTED |
| L-20260919-10 | Boxscore `battingOrder`/`bench`/`bullpen` route | Source upgrade |
| L-20260919-11 | Debutants are machine-detectable | PROMOTED |
| L-20260919-12 | Top O/U must win or get Rank-1 failure review | PROMOTED (review trigger, not a rank rule) |
| L-20260919-13 | Cricket ladder rungs 7–8 | SUPERSEDED by L-122's separate ladders |
| L-20260923-01 | Date, venue and starters must match before merging views | PROMOTED (`O-ID-DATE-STARTER-MATCH`) |
| L-20260923-02 | External ID claim sweep at import | PROMOTED |
| L-20260923-03 | ERA-built NPB centres add back unearned runs | TESTING (`O-NPB-ERA-CENTRE`) |
| L-20260923-04 | P-491 is the reference NPB construction | KEEP |
| L-20260923-05 | Run-centre residual signs conflict | TESTING continues (no tilt) |
| L-20260923-06 | Roster name collision | OBSERVATION |
| L-20260923-07, -13 | Actual start ≠ scheduled start | Field definition (`O-START-MARKER`) |
| L-20260923-08 | AI-generated NPB recaps excluded | Source state |
| L-20260923-09 | Live feed quirks | Source state |
| L-20260923-10 | Custody pointer drift | FIXED |
| L-20260923-11 | P-487 recovered | RESOLVED |
| L-20260923-12 | Announced minutes plans are intentions | OBSERVATION |
| L-20260924-01 | Beat-reporter lineups (`PROJECTED_BEAT_VERIFIED`) | Enforcement FAILED; receipt now mandatory (F03) |
| L-20260924-02 | Clay/low-tier handicap cap | REJECTED → `T-TEN-LOWTIER-HCP` |
| L-20260924-03 | FIBA qualifier pace coefficient | REJECTED → `T-BKB-SEASON-OPENER-WIDTH` |
| L-20260924-04 | Doubleheader Game 1 deflation | REJECTED (0.435 v 0.427) |
| L-20260924-05 | Derby Under suppression | REJECTED |
| L-20260924-06 | NHL preseason roster asymmetry | DEMOTED to disclosure + `T-NHL-PRESEASON-GOALIE` |
| L-20260924-F01 | Process facts carry endpoint and time | PROMOTED (`C-PROCESS-RECORD-PROVENANCE`) |
| L-20260924-F02 | Summaries copied from the card | PROMOTED (`C-SUMMARY-FROM-CARD`) |
| L-20260924-F03 | Lineup diff at settlement; receipts for projected lineups | PROMOTED (`C-LINEUP-DIFF`) |
| L-20260924-F04 – F08 | The six single-game rules withdrawn or demoted | REJECTED / DEMOTED |
| L-20260924-F09 | Covering pairs; "dual run-line arbitrage" | PROMOTED (measurement); arbitrage REJECTED |
| L-20260924-F10 | Run-centre residuals accrue | TESTING (no tilt) |
| L-20260924-F11 | Gamefeed weather at freeze | PROMOTED |
| L-20260924-F12 | Every rule carries a receipt | PROMOTED (`C-PROMOTION-RECEIPT`) |
| L-20260924-F13 | Reversed tennis set scores | FIXED |
| L-20260924-F14 | What worked (centres, tie branch, family tables) | KEEP |
| L-20260925-01 | Coherent winner + cushion + Over pathway existed | Existing control execution |
| L-20260925-02 | WTA exact-match source lane | Source state |
| L-20260925-03 | A volatile server widens both ways | OBSERVATION |
| L-20260925-04 | Early-wicket suppression | TESTING (`T-CRI-DOMINANT-HITTER`) |
| L-20260925-05 | NBL `jumpBall` is the actual tip | CONFIRMED |
| L-20260925-06 | Result-right / process-different example | IMPLEMENTED (G37) |
| L-20260925-07, -18 | Audit-script fixes | FIXED |
| L-20260925-08 | R-1 magnitudes for six leagues | REFERENCE + disclosure |
| L-20260925-09 | Basketball widths about 39% narrow | PROMOTED (`C-WIDTH-BENCHMARK`); TESTING (`C-WIDTH-Z`) |
| L-20260925-10 | NBL early season −8.5; WNBA +6.5 | REFERENCE |
| L-20260925-11 | WNBA 2026 +10.7 over 2024–25 | REFERENCE |
| L-20260925-12 | NHL empty-net structure; odd OT totals | REFERENCE |
| L-20260925-13 | Tennis population rates; P(−k.5) ≤ P(win) | REFERENCE; PROMOTED (`C-HCP-COHERENCE`) |
| L-20260925-14 | EPL and all-30-park references | REFERENCE |
| L-20260925-15 | NBA back-to-back −1.8; no totals effect | REFERENCE |
| L-20260925-16 | `receipts.py` | PROMOTED (tool) |
| L-20260925-17 | ESPN date ranges return HTTP 400 | Source state |
| L-20260925-19 | No skill over the naive baseline (seed) | TESTING (`C-BASELINE-SKILL`) |
| L-20260925-20 | MLB walk-off asymmetry; +1.5 ≈ 0.638 either side | REFERENCE |
| L-20260925-21 | Rules too large; `CURRENT_RULES.md` | PROMOTED (extended by `C-READING-GATE`) |
| L-20260925-22 – 25 | Repository hygiene, CI, manifests, literal `\n` | FIXED |
| L-20260925-26 | Settled-row dataset and calibration tool | PROMOTED (tool) |
| L-20260925-27 | Overall calibration good; no global shrink | REFERENCE |
| L-20260925-28 | Skill lives at p ≥ 0.65 | PROMOTED (`C-LOW-RESOLUTION-BAND`) |
| L-20260925-29 | Non-baseball cushions over-confident | CANDIDATE control + `T-PLUS-CUSHION`; M32 |
| L-20260925-30 | Sport track records | PROMOTED (`C-TRACK-RECORD`, `C-DEPARTURE-LEDGER`) |
| L-20260925-31 | Ranks 2–4 carry no ordering information | REFERENCE |
| L-20260925-32 | Top-two joint failure ≈ independence | REFERENCE |
| L-20260925-33 | Cohort trend follows sport mix | REFERENCE |
| L-20260925-34 | `card_math.py` reproduces issued probabilities | PROMOTED (tool) |
| L-20260925-35 | Extractor graded 17 rows backwards | FIXED |
| L-20260925-36 | Rank-1 success follows the q tier | REFERENCE + `C-TOP2-QUALITY` |
| L-20260925-37 | Decision-side slope ≈ 1.5 | OPERATIVE in RM-1 (user-authorised) |
| L-20260925-38 | The cushion term | OPERATIVE in RM-1; caveats in L-20260926-06 |
| L-20260925-39 | Population cushion cover rates | REFERENCE + construction rule |
| L-20260925-40 | RM-1X (per-sport terms) did not generalise | REJECTED for now |
| L-20260925-41 | TB-1 resolution map | PROMOTED (`C-TEAM-BASELINE`) |
| L-20260925-42 | NFL, AFL, NRL references | REFERENCE |
| L-20260925-43 | Script-typed settlement | PROMOTED (`C-SETTLEMENT-FROM-FEED`) |
| L-20260925-44 | Four mini-log rule candidates | REJECTED (M27) |
| L-20260925-45 | Finals bye-rust | TESTING (`T-NRL-BYE-RUST`, non-binding) |
| L-20260925-46 | Hockey +1.5 grouped with baseball | CORRECTED before issue |
| L-20260926-01 | No skill yet: gather evidence before rules | PROMOTED (`C-RULE-FREEZE`) |
| L-20260926-02 | The reading load broke execution | PROMOTED (`C-READING-GATE`) |
| L-20260926-03 | Self-selected sample | PROMOTED (`C-EVENT-UNIVERSE`) |
| L-20260926-04 | No market yardstick | PROMOTED (`C-MARKET-BENCHMARK`, post-settlement only) |
| L-20260926-05 | MLB pilot had no code | PROMOTED (`C-MLB-SHADOW`) |
| L-20260926-06 | RM-1 evidence limits | VALIDITY amendment to `T-RM1-PROSPECTIVE` |
| L-20260926-07 | Baseline tool pooled seed and prospective rows | FIXED |
| L-20260926-08 | Documentation drift | FIXED |
| L-20260926-09 | 80-item untested backlog | CLOSED_UNTESTED |
| L-20260926-10 | Repository clutter | FIXED |
| L-20260926-11 | Six manifests in one day | PROMOTED (one per day; M33) |

---

## 6. Audit findings and where they went

- **Second independent review, F01–F30 (2026-09-06(d)):** implemented as L-102–L-121 (for example F07 → L-104, F08 → L-106, F10 → L-105, F12 → L-108, F13 → L-109, F16 → L-112, F21 → L-115, F27 → L-119, F29 → L-120). F04, F05, F17, F20 and F25 needed no new rule.
- **External blindspot audit, B-01–B-15 (2026-09-06(c)):** implemented as L-087–L-101 (B-01 → L-087 and `C-WEIGHT-PROPAGATION`, B-02 → L-088, B-03 → L-089, … B-15 → L-101).
- **2026-09-24(f) verification audit:** L-20260924-F01–F14.
- **2026-09-26 review:** L-20260926-01–11.

---

## 7. Withdrawn — never apply

MLB run-line and push caps and fixed variance floors · order-statistic pseudo-tails · path-count or category ranking · universal 40–60% top-slot bands · blanket `DISJOINT` bans and `UNORDERED` escapes · normalised-edge ordering · "at least one O/U won" as evidence · rebound, hangover or "due" rules · doubleheader-G1 deflation · derby Under suppression · "dual run-line arbitrage" · the FIBA qualifier pace coefficient · the clay handicap cap · "bowl first means low-scoring" · "cushion implies underdog winner" and "winner implies games handicap" · guaranteed venue-history availability · the blanket corners Rank-1 cap · the automatic knockout Under · `C-ABSENCE-DEFENSIVE-PENALTY`, `C-KBO-PITCHER-VELOCITY-FILTER`, `C-NRL-SPINE-PEDIGREE-TOTAL-FLOOR`, "ace dominance" · a five-card test as validation · slot history as a prior · any single-game coefficient.

---

## 8. Open tests (no ranking effect until each concludes)

`python tools/evidence_status.py` prints the headline gates. The full list is `CURRENT_RULES.md` §D9:
- **Headline gates:** `C-BASELINE-SKILL` (0/100), `T-RM1-PROSPECTIVE` (0/25 cards, amended 2026-09-26), `C-MARKET-BENCHMARK` (0/100), `C-MLB-SHADOW` (0/150 games), `T-UNIVERSE-VS-SELECTED` (0/30 + 30 cards).
- **Calibration and width:** `C-WIDTH-Z`, `C-PROB-EXTREMITY` (79/100, not supported so far), `C-LOW-RESOLUTION-BAND`, `T-PLUS-CUSHION`, `T-TB1-ANCHOR`.
- **Direction and centre (accrue, no tilt):** `C-RUN-CENTRE-BIAS`, `T-TOTAL-DIRECTION-LEAGUE`, `C-PHASE-VS-FULL-TOTAL`, `O-NPB-ERA-CENTRE`.
- **Sport-specific:** `T-TEN-LOWTIER-HCP`, `C-TEN-FAV-SEPARATION`, `T-TEN-BENCHMARK-GAP`, `T-BKB-SEASON-OPENER-WIDTH` (6/15), `T-NHL-PRESEASON-GOALIE` (1/10), `T-MLB-WIND-IN-OVER` (2/10), `T-CRI-DOMINANT-HITTER` (2/10), `T-CRI-POST-TOSS-FREEZE`, `T-NRL-BYE-RUST`.

Closed on 2026-09-26 (`CLOSED_UNTESTED`, superseded or answered): 59 historical candidates, 21 early process tests, `C-RANK2-GAP`, `C-WEIGHT-PROPAGATION`, `C-MARGIN-TAIL-MASS`, `C-OU-GEOMETRY` (`LEARNING_REGISTER.md` §"2026-09-26" D).

---

## 9. Sport takeaways

Each `RULES_<SPORT>.md` now opens with a §0 live rules page: preconditions, construction order, row rules, track record, reference numbers, withdrawn items and a one-line index of every numbered control. Read that page for the sport's learnings.
