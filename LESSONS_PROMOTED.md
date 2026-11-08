# Promoted lessons (operative)

**Extracted 2026-11-07, CR-2026.11.07-R2 (FORMAT).** These are the lines of the lesson index that are still operative, copied verbatim: every lesson marked PROMOTED or NARROWED, the recurring mistakes to check on every card, and the withdrawn list (never apply). The full index and the lesson register (402 KB) are kept unchanged at [archive/consolidation_2026-11-07/archived/LEARNINGS_INDEX.md](archive/consolidation_2026-11-07/archived/LEARNINGS_INDEX.md) and [archive/consolidation_2026-11-07/archived/LEARNING_REGISTER.md](archive/consolidation_2026-11-07/archived/LEARNING_REGISTER.md); the register governs where a line here and its entry disagree.

**Status words.** PROMOTED = operative process/disclosure control · NARROWED = partly operative (the operative part is named) · WITHDRAWN = never apply.

**Applicability (LESSON-STATUS-v1, CR-2026.11.08-R2).** Every lesson below now carries a version status, because the lessons were learned on cards made under earlier rules:

- `PRE_V24`: learned before P-2026.10.22-v24.0. It is historical evidence and a checklist prompt. It is not a current rule unless a current document restates it, and where a current rule differs, the current rule governs.
- `V24`: learned on v24 cards.
- `CHECKLIST`: a recurring-mistake check that applies to every card.

Numbers inside lessons (for example "skill lives at p ≥ 0.65") are descriptive findings on the cohort they were measured on. The current selection constants are provisional in [RULES_REFERENCE](RULES_REFERENCE.md#part-b-selection_rules) Part B, and prompt 8 re-estimates them. Precedence is defined once, in [RULES_REFERENCE](RULES_REFERENCE.md#part-a-current_rules) Part A §0 (PREC-v1).

## 2. Recurring mistakes (check every card)

| ID | Mistake | Control |
|---|---|---|
| M1 | Exact-winner over-trust | G30.1 · applies: `CHECKLIST` |
| M2 | Non-loss / double chance over-ranked | Soccer rules · applies: `CHECKLIST` |
| M3 | Totals stacked off one factor | Baseball control 26 · applies: `CHECKLIST` |
| M4 | Overtime/blowout tail ignored beside phase Unders | G-L1 · applies: `CHECKLIST` |
| M5 | Cushion on a cold side missing its key player | Kill paths · applies: `CHECKLIST` |
| M6 | Reputation or returning ace against a park suppressor | Baseball rules · applies: `CHECKLIST` |
| M7 | Elite ceiling against a "tough venue" Under | Cricket rules · applies: `CHECKLIST` |
| M8 | Bottom slot never tested | G23.1, G27 · applies: `CHECKLIST` |
| M9 | Stale cached or proxy source | Source freshness · applies: `CHECKLIST` |
| M10 | Kill path as prose, not mass | G-L1 · applies: `CHECKLIST` |
| M11 | Uncertainty turned into a directional lean | G-L2 · applies: `CHECKLIST` |
| M12 | Tier gap read as scoring shape | G-L3; no EPL-to-cup transfer · applies: `CHECKLIST` |
| **M13** | **Aggregate used where the game log was one click away (highest-value check)** | G-L7 · applies: `CHECKLIST` |
| M14 | Total probability not derived from the card's own centre and width | G-L8; `tools/card_math.py` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)) · applies: `CHECKLIST` |
| M15 | Control listed, not executed | `audit_card_controls.py` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `C-READING-GATE` · applies: `CHECKLIST` |
| M16 | Complement not itemised | G-L9 · applies: `CHECKLIST` |
| M17 | Small-sample rate used as direction | G-L11 · applies: `CHECKLIST` |
| M18 | Top two structurally anti-coupled | G-L10 · applies: `CHECKLIST` |
| M19 | Published lineup not retrieved | G14.2; `RETRIEVAL_MISS` · applies: `CHECKLIST` |
| M20 | Model summary used as the record | G-L13 · applies: `CHECKLIST` |
| M21 | Settlement route not consulted | G-L14 · applies: `CHECKLIST` |
| M22 | Period-scope mismatch | G-L16 · applies: `CHECKLIST` |
| M23 | "At least one O/U won" read as success | G-L15, G-L22 · applies: `CHECKLIST` |
| M24 | State-contaminated evidence window | Cricket control 21; G-L7 · applies: `CHECKLIST` |
| M25 | Personnel claim without retrieval or receipt | `C-LINEUP-DIFF`; S-1 Rev 2 receipt · applies: `CHECKLIST` |
| M26 | Process record written, not read | `C-PROCESS-RECORD-PROVENANCE`; `C-SETTLEMENT-FROM-FEED` · applies: `CHECKLIST` |
| M27 | Single-game predictive rule promoted | `C-PROMOTION-RECEIPT` · applies: `CHECKLIST` |
| M28 | Covering-pair record read as skill | G-L22(c) `COVERING_PAIR` · applies: `CHECKLIST` |
| M29 | Summary row retyped, not copied | `C-SUMMARY-FROM-CARD` · applies: `CHECKLIST` |
| M30 | City forecast instead of the gamefeed wind | `RULES_BASEBALL.md` B-2 · applies: `CHECKLIST` |
| M31 | Width chosen without a reference | `C-WIDTH-BENCHMARK`; `C-WIDTH-Z` · applies: `CHECKLIST` |
| M32 | Non-baseball cushion priced like a baseball +1.5 | `C-PLUS-CUSHION`; RM-1 · applies: `CHECKLIST` |
| M33 | Rule churn outruns evidence | `C-RULE-FREEZE`; one manifest per day; rule inventory closed, lessons parked (§10, 2026-09-28(e)) · applies: `CHECKLIST` |
| M34 | Self-selected sample read as the competition | `C-EVENT-UNIVERSE`; `T-UNIVERSE-VS-SELECTED` · applies: `CHECKLIST` |
| M35 | Frozen field replaced at settlement (e.g. a missing baseline retyped as 0.500) | `CURRENT_RULES.md` §D8; `CARD_AND_LOG_TEMPLATES.md` §2 (added 2026-09-28) · applies: `CHECKLIST` |

---

## 3. Promoted lessons L-001 to L-122

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
| L-105 | Dimensional check before any formula | PROMOTED |
| L-106 | "True union" is a settlement fact | PROMOTED |
| L-107 | Summed order statistics are a sensitivity scenario only | PROMOTED |
| L-112 | Two observations do not establish a distribution shape | PROMOTED |
| L-011 | A streak moves a rank only once its cause is shown | PROMOTED |
| L-018 | Likelihood rank, proper scoring and the top-two portfolio are separate objectives | PROMOTED |
| L-055 | Classify slate geometry (forced pairs v free rows) | PROMOTED |
| L-057 | Rank 1 defines a state; re-solve the others conditional on it | PROMOTED |
| L-060 | Winner from win-branch mass; reconcile with a cushion | PROMOTED |
| L-088 | Rank-gap field | PROMOTED |
| L-097 | Tail/coherence blindspot already covered | PROMOTED (cross-reference) |
| L-098 | Winner/handicap/total coherence already covered on paper | PROMOTED (cross-reference) |
| L-108 | Marginal ranking ≠ joint coherence | PROMOTED |
| L-109 | A strong cushion doesn't force an underdog winner | PROMOTED |
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

## 4. General-algorithm lessons G-L1 to G-L24 (RULES_GENERAL §16)

| ID | Lesson | Status |
|---|---|---|
| G-L1 | Outcome families enumerated with mass; kill paths as weighted branches | PROMOTED |
| G-L2 | Uncertainty is width, not a lean (shrinkage may move mean and variance when declared) | PROMOTED (as corrected) |
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

## 5. Dated lessons, 2026-09-12 to 2026-09-26

| ID | Lesson | Status |
|---|---|---|
| L-20260912-01 | Exact CDF/outcome mass and push handling replace absolute-edge ordering | PROMOTED · applies: `PRE_V24` |
| L-20260912-02 | Disjoint complete-game states and joint bounds | PROMOTED · applies: `PRE_V24` |
| L-20260912-03 | Real sample denominators; withdraw equal-n and two-SE claims | PROMOTED · applies: `PRE_V24` |
| L-20260912-04 | Starters, bench and coaches separately; no backdating | PROMOTED · applies: `PRE_V24` |
| L-20260912-05 | Record the first decisive checkpoint and extra-period exposure | PROMOTED (weights TESTING) · applies: `PRE_V24` |
| L-20260912-07 | Field-level source checks; branding can't certify every field | PROMOTED · applies: `PRE_V24` |
| L-20260912-08 | Exclude market-derived prose from MARKET_BLIND analysis | PROMOTED · applies: `PRE_V24` |
| L-20260912-09 | Frozen preferred O/U; explicit denominators | PROMOTED · applies: `PRE_V24` |
| L-20260912-10 | Document custody; restore before declaring absent | PROMOTED · applies: `PRE_V24` |
| L-20260915-01 | Test winner labels need a time budget, not a series aggregate | PROMOTED (cricket control 28) · applies: `PRE_V24` |
| L-20260915-02 | Current-series innings table is the Test phase prior | PROMOTED (cricket control 27) · applies: `PRE_V24` |
| L-20260915-04 | A missing log gets an inventory, not new IDs | PROMOTED · applies: `PRE_V24` |
| L-20260915-06 | Underdog cushions 10 W / 13 L at 0.61 → G-L12 | PROMOTED · applies: `PRE_V24` |
| L-20260915-12 | Sparse fixtures confirmed at federation level | PROMOTED · applies: `PRE_V24` |
| L-20260915-13 | Derivatives settle from the official record | PROMOTED · applies: `PRE_V24` |
| L-20260915-14 | Team-corner rows need corner generators | PROMOTED (soccer control 33) · applies: `PRE_V24` |
| L-20260915-15 | Same-competition meeting is current evidence | PROMOTED (basketball control 25) · applies: `PRE_V24` |
| L-20260915-16 | Run-line decomposition; IL-return hook; home-last-bat mass | PROMOTED (baseball control 29) · applies: `PRE_V24` |
| L-20260915-17 | NFL margin prior, key numbers, prior-season ratings as width | PROMOTED (gridiron controls 17–19) · applies: `PRE_V24` |
| L-20260915-19 | Import checks | PROMOTED · applies: `PRE_V24` |
| L-20260916-01 | A summarised fetch is not a record → G-L13 | PROMOTED · applies: `PRE_V24` |
| L-20260916-02 | Settlement route executed → G-L14 | PROMOTED · applies: `PRE_V24` |
| L-20260916-03 | League corner route table | PROMOTED (soccer control 35) · applies: `PRE_V24` |
| L-20260916-05 | O/U geometry disclosure → G-L15; C-OU-GEOMETRY | PROMOTED; the test SUPERSEDED 2026-09-26 · applies: `PRE_V24` |
| L-20260916-06 | Disruption facts at settlement | PROMOTED (soccer control 34) · applies: `PRE_V24` |
| L-20260916-07 | NFL non-offensive TD branch (18.8% of games) | PROMOTED (gridiron control 20) · applies: `PRE_V24` |
| L-20260916-08 | P(favourite covers ∧ Under) | PROMOTED (gridiron control 21) · applies: `PRE_V24` |
| L-20260916-09 | Starter-exit transition inning | PROMOTED (baseball control 30) · applies: `PRE_V24` |
| L-20260916-10 | Repeatable-v-variance table; batting pitcher branch | PROMOTED (basketball 25; baseball 31b) · applies: `PRE_V24` |
| L-20260916-11 | Fingerprint every drop-location variant | PROMOTED · applies: `PRE_V24` |
| L-20260916-13 | Period scope → G-L16 | PROMOTED · applies: `PRE_V24` |
| L-20260916-15 | Threshold-invariant v knife-edge derivative rows | PROMOTED (disclosure) · applies: `PRE_V24` |
| L-20260917-01 | Shared failure state of the top two → G-L17 | PROMOTED · applies: `PRE_V24` |
| L-20260917-02 | Allocation marginals → G-L18 | PROMOTED · applies: `PRE_V24` |
| L-20260917-03 | Ties in the end-state family → G-L19 | PROMOTED · applies: `PRE_V24` |
| L-20260917-04 | Direct comparable already cleared the line → G-L20 | PROMOTED · applies: `PRE_V24` |
| L-20260917-05 | Single-team scoring rows above 0.80 without an XI | PROMOTED (soccer control 37; no cap) · applies: `PRE_V24` |
| L-20260917-08 | Cross-league defence widens the separation tail | PROMOTED (soccer control 39) · applies: `PRE_V24` |
| L-20260917-09 | Bowling replacement chain | PROMOTED (cricket control 31) · applies: `PRE_V24` |
| L-20260917-10 | Strikeout-floor prop gate | PROMOTED (baseball control 33) · applies: `PRE_V24` |
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
| L-20260917b-14 | JS-only field owner is a render escalation | PROMOTED (basketball control 27) |
| L-20260917b-21 | `audit_card_controls.py` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)) rebuilt and wired in | PROMOTED |
| L-20260917b-23 | Unauditable logs marked BODY_NOT_CARRIED | PROMOTED |
| L-20260917b-24 | Every sport has a cushion band → G-L24 | PROMOTED |
| L-20260917b-25 | One maintained `BASE_RATES_REGISTER.md` | PROMOTED |
| L-20260919-01 – 04 | No MLB rebound; calibre doesn't change it; no pitcher rebound; shorter windows predict worse | PROMOTED (`R-1`) |
| L-20260919-08 | Press conferences: availability and role only | PROMOTED (`S-2`) · applies: `PRE_V24` |
| L-20260919-09 | `LINEUPS_NOT_YET_PUBLISHED` distinct from `RETRIEVAL_MISS` | PROMOTED · applies: `PRE_V24` |
| L-20260919-11 | Debutants are machine-detectable | PROMOTED · applies: `PRE_V24` |
| L-20260919-12 | Top O/U must win or get Rank-1 failure review | PROMOTED (review trigger, not a rank rule) · applies: `PRE_V24` |
| L-20260923-01 | Date, venue and starters must match before merging views | PROMOTED (`O-ID-DATE-STARTER-MATCH`) · applies: `PRE_V24` |
| L-20260923-02 | External ID claim sweep at import | PROMOTED · applies: `PRE_V24` |
| L-20260924-F01 | Process facts carry endpoint and time | PROMOTED (`C-PROCESS-RECORD-PROVENANCE`) |
| L-20260924-F02 | Summaries copied from the card | PROMOTED (`C-SUMMARY-FROM-CARD`) |
| L-20260924-F03 | Lineup diff at settlement; receipts for projected lineups | PROMOTED (`C-LINEUP-DIFF`) |
| L-20260924-F09 | Covering pairs; "dual run-line arbitrage" | PROMOTED (measurement); arbitrage REJECTED |
| L-20260924-F11 | Gamefeed weather at freeze | PROMOTED |
| L-20260924-F12 | Every rule carries a receipt | PROMOTED (`C-PROMOTION-RECEIPT`) |
| L-20260925-09 | Basketball widths about 39% narrow | PROMOTED (`C-WIDTH-BENCHMARK`); TESTING (`C-WIDTH-Z`) · applies: `PRE_V24` |
| L-20260925-13 | Tennis population rates; P(−k.5) ≤ P(win) | REFERENCE; PROMOTED (`C-HCP-COHERENCE`) · applies: `PRE_V24` |
| L-20260925-16 | `receipts.py` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)) | PROMOTED (tool) · applies: `PRE_V24` |
| L-20260925-21 | Rules too large; `CURRENT_RULES.md` | PROMOTED (extended by `C-READING-GATE`) · applies: `PRE_V24` |
| L-20260925-26 | Settled-row dataset and calibration tool | PROMOTED (tool) · applies: `PRE_V24` |
| L-20260925-28 | Skill lives at p ≥ 0.65 | PROMOTED (`C-LOW-RESOLUTION-BAND`) · applies: `PRE_V24` |
| L-20260925-30 | Sport track records | PROMOTED (`C-TRACK-RECORD`, `C-DEPARTURE-LEDGER`) · applies: `PRE_V24` |
| L-20260925-34 | `card_math.py` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)) reproduces issued probabilities | PROMOTED (tool) · applies: `PRE_V24` |
| L-20260925-41 | TB-1 resolution map | PROMOTED (`C-TEAM-BASELINE`) · applies: `PRE_V24` |
| L-20260925-43 | Script-typed settlement | PROMOTED (`C-SETTLEMENT-FROM-FEED`) · applies: `PRE_V24` |
| L-20260926-01 | No skill yet: gather evidence before rules | PROMOTED (`C-RULE-FREEZE`) · applies: `PRE_V24` |
| L-20260926-02 | The reading load broke execution | PROMOTED (`C-READING-GATE`) · applies: `PRE_V24` |
| L-20260926-03 | Self-selected sample | PROMOTED (`C-EVENT-UNIVERSE`) · applies: `PRE_V24` |
| L-20260926-04 | No market yardstick | PROMOTED (`C-MARKET-BENCHMARK`, post-settlement only) · applies: `PRE_V24` |
| L-20260926-05 | MLB pilot had no code | PROMOTED (`C-MLB-SHADOW`) · applies: `PRE_V24` |
| L-20260926-11 | Six manifests in one day | PROMOTED (one per day; M33) · applies: `PRE_V24` |
| L-20260926-12 | Every sport has a numerical A0/A1 model; A1 beats the baseline on results in soccer, NFL, AFL, NBA | PROMOTED (`C-SPORT-SHADOW`; shadow only) · applies: `PRE_V24` |
| L-20260926-23 | Unrecorded lanes produce no evidence | PROMOTED (audit `10s`) · applies: `PRE_V24` |
| L-20260926-27 | Predictability map: STRONG favourites by league (AFL 39% … MLB 0%) | PROMOTED (disclosure, `C-PREDICTABILITY-MAP`) · applies: `PRE_V24` |
| L-20260928-01 | Markdown-only operation: every tool step has a Markdown procedure | PROMOTED (process; `CURRENT_RULES.md` A11) · applies: `PRE_V24` |
| L-20260928-04 | 60+ sources re-verified by live request; about 30 added (standings, injuries, official ladders, Elo, weather) | PROMOTED (`SOURCES.md`) · applies: `PRE_V24` |
| L-20260928-05 | Settlement tables replaced frozen baselines with 0.500 (20/20 cells, review F2) | PROMOTED (M35; frozen fields copied, never replaced) · applies: `PRE_V24` |
| L-20260928-09 | P6: TB-1-MD has resolution for results in the top five soccer leagues, and for totals in La Liga and the Bundesliga | PROMOTED (anchor extension) · applies: `PRE_V24` |
| L-20260928-10 | Four of the five cards before this change were `LIVE_ISSUED`, so none could count toward a checkpoint | PROMOTED (process, user-instructed): core frozen before the start, annex after; reading once per session (`CURRENT_RULES.md` §B, §0) · applies: `PRE_V24` |
| L-20260928-14 | Rule churn continued after M33 (three manifests on 2026-09-28 before this pass) | PROMOTED (governance, user-instructed): the rule inventory is closed and lessons are parked (§10) until the checkpoints read out · applies: `PRE_V24` |

## 7. Withdrawn — never apply

MLB run-line and push caps and fixed variance floors · order-statistic pseudo-tails · path-count or category ranking · universal 40–60% top-slot bands · blanket `DISJOINT` bans and `UNORDERED` escapes · normalised-edge ordering · "at least one O/U won" as evidence · rebound, hangover or "due" rules · doubleheader-G1 deflation · derby Under suppression · "dual run-line arbitrage" · the FIBA qualifier pace coefficient · the clay handicap cap · "bowl first means low-scoring" · "cushion implies underdog winner" and "winner implies games handicap" · guaranteed venue-history availability · the blanket corners Rank-1 cap · the automatic knockout Under · `C-ABSENCE-DEFENSIVE-PENALTY`, `C-KBO-PITCHER-VELOCITY-FILTER`, `C-NRL-SPINE-PEDIGREE-TOTAL-FLOOR`, "ace dominance" · a five-card test as validation · slot history as a prior · any single-game coefficient.

---
