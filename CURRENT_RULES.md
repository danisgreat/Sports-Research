# Current rules — the live operating summary

**Opened 2026-09-25(c). Revised 2026-09-25(e):** the Rank-1/Rank-2 pass. It adds RM-1 ranking, TB-1 team baselines, the NFL/AFL/NRL references and settlement from the feed (`RULES_GENERAL.md` §"2026-09-25(e)").
- **Method:** MDS-2026.09.19-v4.3.
- **Control revision:** CR-2026.09.21-3.
- **Scoring:** SCV-2026.09.19-v2.
- **Freeze receipt:** the manifest named in `METHOD.md`'s header.
- **Status of every record:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

**What this is.** One document that says what is *live*, in the order a session needs it. The governing files keep their dated addenda as the evidence record, so they read like a history. This page is the map: each rule below cites where its full text lives.

**Precedence.** This page is a derived summary.
- If it disagrees with the section it cites, **the cited section governs** (`METHOD.md` §9; `RULES_GENERAL.md` §0), and the disagreement is a documentation defect to fix *here* in the same pass.
- It never reinstates a withdrawn rule (§I).
- Current user instructions outrank everything.

**Reading order.** This page is **step 0**. The standing reading gate still applies in full: `RULES_GENERAL.md` §1, then the sport file in its entirety, then the log sweep of the nearest same-sport retrospectives. This page makes that read navigable; it does not replace it.

---

## A. Non-negotiables

1. **Sports only, market-blind.** Odds, prices, line movement, tipsters, betting previews, prediction markets and fantasy/DFS material are never evidence, anchors or sanity checks. RotoWire, RotoGrinders and FPTrack are prohibited. A supplied line is contract metadata, quarantined until the distribution is frozen (`METHOD.md` §1.1; `RULES_GENERAL.md` §"2026-09-19 deep-research addendum").
2. **Never fabricate.** A missing lineup, timestamp, probability or record stays missing (`UNAVAILABLE`, `NOT_RETRIEVED`, `NOT_YET_DERIVED`). A number that cannot be reproduced from the printed distribution is invented precision (`METHOD.md` §6, §12).
3. **Learning-only.** No performance, calibration, ROI or value claim follows from any record. Missing prices or validated probabilities mean `NO VALUE DETERMINABLE` (`METHOD.md` §1; `PERFORMANCE_ELIGIBILITY_POLICY.md`).
4. **Three independent lineages** to issue an event and three to settle it. Mirrors and syndication count once; search snippets and generated summaries never count (`METHOD.md` §"Universal three-source … gate").
5. **Pregame means before the start.** A card cannot issue after the first ball, pitch, puck or tip. Use the feed's actual start marker, e.g. the NBL `jumpBall` event (`RULES_GENERAL.md` §2; `RULES_BASKETBALL.md` K-3).
6. **Issued records are immutable.** Corrections are appended, never rewritten (`METHOD.md` §6, §10).
7. **Distribution first.** One coherent joint outcome distribution per event. Every row's probability is read from it, and rows are ranked by that probability (`METHOD.md` §12; `RULES_GENERAL.md` §16.11, G23.1).
8. **No coefficient from this log's own results.** A single game can expose a bug or open a prospective test. It never creates a weight, cap or ranking override (`L-087`; `RULES_GENERAL.md` §16.10 item 11; `C-PROMOTION-RECEIPT`).
   - **The one user-authorised exception is RM-1** (2026-09-25(e)). It is pooled and pre-specified, validated out of sample, refitted only at the 25-card review, and printed beside the unchanged stated p (`RULES_GENERAL.md` §"2026-09-25(e)"(h)).
9. **Read the record; don't write it.** Every settlement fact comes from a named endpoint with its retrieval time (`C-PROCESS-RECORD-PROVENANCE`).
10. **Honest labels.** Coin flips are called coin flips (`NEAR_TIED`). Forced and covering pairs are labelled. A mechanical win is not skill (G-L22, `COVERING_PAIR`).

## B. The workflow

Source: `METHOD.md` §3. The tools are in §G.

| Step | What to do | Hard stop if … |
|---|---|---|
| 0 | Read this page, then the reading gate (above). Check the active log's top snapshot for the next ID and open items | the next ID or event state is unclear: use a `TMP-` ID |
| 1 | **Identity and state.** Event, competition, venue, venue-local date and time, IANA timezone, AEST/AEDT conversion. Classify the state from the feed: PREGAME, LIVE or FINAL (`receipts.py pregame …`) | the state is not PREGAME: live-issued view only, clearly labelled |
| 2 | **Contract.** Parse the supplied rows exactly: target, period, line, push/void terms. Quarantine the lines | the contract is ambiguous: flag it, don't guess |
| 3 | **Participants.** Official lineup, starters, goalie and pitchers first, with fetch time. Otherwise `LINEUPS_NOT_YET_PUBLISHED`, `RETRIEVAL_MISS` or a receipted `PROJECTED_BEAT_VERIFIED` (§D3) | a Rank-1 total or margin row depends on an unretrieved lineup (G14.2) |
| 4 | **Environment.** Outdoor events: a venue-coordinate hourly forecast for the game window. MLB: the gamefeed weather block (§D4) | outdoor card without it |
| 5 | **Evidence.** Disaggregated records before aggregates (M13); L5/L10/L15/L20 descriptively; the season rate plus the opponent (§D5) | an aggregate carries direction while the game log sits one click away: mark `AGGREGATE_ONLY` and cap it |
| 6 | **Distribution.** Prior plus named adjustments → centre and width → family table with masses. Print the **reference row, reference width, `BASELINE_P` and `TEAM_BASELINE_P`** (`tools/team_baseline.py`; §D5, §D7). The departure ledger anchors on TB-1 where it has resolution | the probabilities can't be reproduced from the table |
| 7 | **Rank and dependence.** Derive each row's p, then run **`tools/rank_model.py rank`**. **Rank by RM-1 q** and print the `TOP2_QUALITY` line. Label FORCED_PAIR/FREE and COVERING_PAIR; print P(R1∧R2), P(¬R1∧¬R2) and the complement decomposition (§D6) | a joint number is invented: use `JOINT_UNQUANTIFIED` with bounds |
| 8 | **Freeze.** Final volatile refresh, freeze time, manifest SHA. Append the card to the active mini log **before** delivery | — |
| 9 | **Settle.** Three terminal lineages; the `receipts.py settle …` process record, **read from the feed, never typed** (`C-SETTLEMENT-FROM-FEED`); lineup diff; z-scores; p **and** q grades; enhanced reviews (§D8) | any credible live or conflicting source |
| 10 | **Learn.** Retrospective questions; dispositions to `LEARNING_REGISTER.md` with a receipt; baseline ledger row appended (§D9) | a predictive rule from one or two games |

## C. The card: six fields plus the completeness block

Source: `METHOD.md` §4; `RULES_GENERAL.md` §16.3, §16.8. The audit field IDs are those checked by `audit_card_controls.py`; **B** marks a field that blocks by default, and **S** one that blocks under `--strict`, which is required for every card from the 2026-09-25 manifests onward.

| Field | Must contain | Audit |
|---|---|---|
| 1 Identity and contract | IDs, participants, competition, times (venue-local, UTC, AEST), state, exact contracts, method and manifest | 1 |
| 2 Evidence and exposure | Sources with owner, time and status (OPENED/SNIPPET/ASSUMED); participants per side; injuries and workload; environment; windows; disaggregated records; settlement route | 7 **B**, 7r **S**, 8, 9 |
| 3 Joint distribution | Prior with provenance; named signed adjustments; centre, median and width; family table with masses; phase and team marginals; representative score; **reference row** and **reference width** | 2 **B**, 3 **B**, BR, WB **S**, T13 **S** (tennis), CVW (cricket) |
| 4 Contract queries and ranks | Exact probability per row (UNVALIDATED_SUBJECTIVE, reproduced with `tools/card_math.py`); **RM-1 q, tier and flags per row; ranks by q; `TOP2_QUALITY`** (optional `SLATE_ADVISORY`); FORCED_PAIR/FREE; preferred side; push mass; **`BASELINE_P` and `TEAM_BASELINE_P` per row**; **departure ledger**; **track-record row**; `LOW_RESOLUTION` label at 0.50–0.65; `C-PLUS-CUSHION` for non-baseball +k.5 | BP **S**, DL **S**, PC **S**, **RM S, TB S** (from manifest 2026-09-25-5), 5b, HC **S** (tennis handicap) |
| 5 Dependence and checks | P(R1∧R2), P(¬R1∧¬R2), P(all fail) where three or more rows share a driver; complement decomposition; kill paths with mass; COVERING_PAIR | 4, 5, 5a **B**, 6 |
| 6 Freeze and follow-up | Freeze receipt, manifest SHA, settlement route. At settlement: sourced process record, lineup diff (names must be on the card), z, grades, reviews | 10 **B**, 10p **S**, 10l **S**, 10z **S**, **10n S** |

## D. Rules by topic

### D1 Identity, time and state
- Verify venue-local time and zone, and convert to AEST/AEDT. User times are estimates until verified (`RULES_GENERAL.md` §"Universal event-verification hard gate").
- **Merging views** requires date, venue, home/away and starters all to match (`O-ID-DATE-STARTER-MATCH`). Otherwise it is a new event and a new ID.
- **New competition, or new season after a gap:** re-verify the rules and format against the field owner before modelling (`RULES_GENERAL.md` §3; each sport file §9).

### D2 Sources
- **Ladder:** field owner → official team or player → structured API → independent quality media → fallback (`SOURCES.md`; `DATA_SOURCE_REGISTER.md`).
- **Access ladder:** keyless APIs (MLB statsapi, NHL api-web via **curl**, ESPN site API **without a browser User-Agent** and **one date per scoreboard call**) → StatMuse (US sports baselines) → WebFetch → the `r.jina.ai` proxy (check dates; it can be stale) → browser.
- **Excluded:** sportsbook, tipster and fantasy material; AI-generated recaps (e.g. archysport); search-result summaries as facts (M20, the synthetic-content trap).
- **Critical dynamic fields** (lineup, starter, toss, goalie): the field owner, or two genuinely independent current lineages, or leave the field unresolved.

### D3 Participants and lineups (M19, M25; `RULES_GENERAL.md` §"2026-09-24(f)"(c))
- **An official lineup published before the freeze always wins.** Print it with its fetch time. Official sources: MLB statsapi `battingOrder`; NPB and KBO official orders; NBA, WNBA and NBL official starters; the NHL official goalie.
- **`PROJECTED_BEAT_VERIFIED`** is valid only with a printed `S-1 Rev 2 receipt:` (outlet, reporter, timestamp, verbatim quote, two sources). Otherwise the state is `NOT_RETRIEVED` / `RETRIEVAL_MISS`.
- Preseason goalies stay `PROJECTED`.
- **Social media is not a lineup source** (S-1).

### D4 Environment
- **Outdoor events:** a venue-coordinate hourly forecast from about one hour before the start to the plausible end, in venue-local time. Downgrade for rain only within the match window (G15.1).
- **MLB:** the statsapi gamefeed `weather` block at freeze (field-relative wind), via `receipts.py pregame mlb`. If it says `WEATHER_NOT_YET_PUBLISHED`, print that. **Never substitute a city forecast** (M30).

### D5 Building the distribution (`METHOD.md` §1.2, §4 field 3; `RULES_GENERAL.md` §16.5)
- **Signed adjustments** need a named mechanism: a confirmed absence, pitch limit, role change, lineup change, weather reading or tactical change. **Uncertainty goes into the width, not a signed lean** (G-L2, M11).
- **Recency (`R-1`).** Recent results revise a *rate* through a named mechanism; they never forecast a deviation.
  - There is no rebound in any competition measured (MLB, NBA, WNBA, NBL, NHL, EPL).
  - **The last game is the worst predictor in 6 of 6.** It never outweighs the season rate.
  - In basketball, the opponent's defence to date beats any recency window (`RECENCY_AND_REBOUND.md` §7).
- **Reference row (field BR).** Print the competition's population row from `BASE_RATES_REGISTER.md` §7 beside the centre, or `REFERENCE_BASE_RATE: NOT_YET_DERIVED`. A large departure is explained on the card.
- **Reference width (`C-WIDTH-BENCHMARK`).** Print the reference width beside the card's width. **Below 0.85 × the reference, name what the card knows.**

  | Competition | Total | Margin |
  |---|---:|---:|
  | NBA | 19.4 | 15.1 |
  | WNBA | 19.5 | 13.3 |
  | NBL | 18.7 | 15.2 |
  | NHL | 2.29 | 2.57 |
  | MLB | 4.50 | 4.57 |
  | EPL | 1.61 | 1.51 |
  | WTA best-of-3 total games (raw SD) | 5.79 | — |

  Recent basketball total widths ran about 39% too narrow (M31).
- **Windows and regimes** (`RULES_GENERAL.md` §"2026-09-25(b)"(d)):
  - NBL early season **−8.5** points; WNBA early season **+6.5**. The signs are opposite, so there is no cross-league rule.
  - WNBA 2026 runs **+10.7** over 2024–25: exclude or adjust those seasons in any average (M24).
  - NHL preseason: use preseason rates.
- **Coherence.** The total probability is derived from the card's own centre and width, with the normalised edge printed (G-L8, M14). Mean and median are kept distinct. **Use `tools/card_math.py`** (normal / negative binomial / Poisson / Skellam, with `--no-zero` for margins that cannot tie) so the numbers reproduce.
- **Baseline-anchored construction (`C-DEPARTURE-LEDGER`, 2026-09-25(d)).** Start each row at `BASELINE_P`. Print its log-odds departure and attribute it to named mechanisms (`tools/card_math.py departure`). More than 10% unattributed is `UNEXPLAINED_DEPARTURE`, and the grade is capped at LOW.

### D6 Ranking and dependence (`RULES_GENERAL.md` G23.1, G27, G-L9, G-L10, G-L17, G-L21, G-L22; §"2026-09-25(e)")
- **Order (`C-RANK-MODEL`, from 2026-09-25(e)).** Rank by **RM-1 q**, the calibrated probability of the exact settlement event, from `python tools/rank_model.py rank --sport <league> --row "<contract>=<p>" …`.
  - Stated p is printed unchanged beside q and breaks ties within 0.005.
  - Rows that cannot be separated still get unique ordinals, labelled `NEAR_TIED` with the non-predictive tie-break stated.
- **`SIDE_FLIP`** (q crosses 0.5 by ≥ 0.05). The flipped side is ranked by q, capped at SUPPORTED, and given a reconciliation line.
  - Override is allowed only when a TB-1 target with resolution gives the stated side ≥ 0.55. A narrative is never an override.
  - `NEAR_TIED_FLIP` (within 0.05 of 0.5) keeps the stated side as a coin flip.
- **`TOP2_QUALITY` on every card:** STRONG / SUPPORTED / TOP1_ONLY / COIN_FLIP. Under `TOP2_COIN_FLIP`, the delivery says in plain words that the top two are near coin flips.
  - Optional **`SLATE_ADVISORY`**: up to two same-event contracts the card's own distribution prices at q ≥ 0.70. Not ranked, not scored, not a betting recommendation.
  - **Rank 1 is only "far more likely to win than lose" in the STRONG tier.** Held out, q ≥ 0.70 won 81% of decisions and 73% as Rank 1; below 0.70, 52–63%.
- **No pooled band forces an ordinal:** no 40–60% floor, no slot-history fade (G26.1).
- **Bottom row (G27):** write its best case in full and run the swap test against the row above.
- **Pairs.**
  - Label each over/under row `FORCED_PAIR` or `FREE`, and freeze the preferred side.
  - `COVERING_PAIR`: two rows whose union covers every outcome, e.g. opposite +1.5 in MLB, or a moneyline plus the opponent's +1.5. Hit@2 is then mechanical and excluded from top-two summaries. Never seek such a pair to guarantee a win.
- **Print:**
  - P(R1∧R2) with its coupling sign;
  - P(¬R1∧¬R2), and P(all fail) where three or more rows share a driver;
  - the complement decomposition of R1 and R2 across the kill paths (M16);
  - every kill path as a weighted branch, not prose (M10).

### D7 Probability and scoring (`SCORING_AND_VALIDATION.md`)
- **Every ranked row carries an `UNVALIDATED_SUBJECTIVE` probability** reproducible from the printed distribution.
- **Scoring:** half-scaled W/P/L Brier for push-capable contracts. A forced pair is counted once in decision metrics.
- **Baseline (`C-BASELINE-SKILL`, from `CONTROL_MANIFEST_2026-09-25-3.md`).** Every ranked row also prints `BASELINE_P`: the naive population probability for the same contract, from games completed before the event, knowing only home/away (`SKILL_BASELINE_LEDGER.md` rules).
  - Settled rows are appended to the ledger.
  - `python tools/skill_baseline.py` reports card minus baseline.
  - **Seed result: the cards have not yet beaten the baseline** (0.2461 v 0.2360, n = 29, interval spans 0).
- **Top-slot measures:** Rank-1 record; top O/U preferred side; Hit@2 excluding covering pairs. "At least one O/U won" is never a success measure (M23). **Ranks 2–4 carry no ordering information** in the full record (54–56% each), so report probabilities, not slots.
- **RM-1 (2026-09-25(e); `research/rank_model_2026-09-25e/README.md`).** logit(q) = −0.187 + 1.543·logit(p) − 1.127·[a +k.5 cushion outside baseball, hockey and soccer].
  - It beat the stated p on log loss in grouped CV and in four forward splits.
  - Ranking by q raised the top-two win count on held-out cards: leave-one-card-out +0.068 per card [+0.007, +0.128]; Rank 1 64.2% → 68.9%; Rank 2 60.1% → 62.2%.
  - Rank 1 and Rank 2 were never lower in any forward split (from P-450: 66.7% → 69.0% and 59.5% → 69.0%).
  - The gains are in the oval sports, basketball and tennis. MLB, NPB/KBO, soccer and cricket are unchanged.
  - A richer per-sport and per-class model failed.
  - Both p and q are scored at settlement (`T-RM1-PROSPECTIVE`). If q's Brier is worse than p's over 25 cards, RM-1 reverts to disclosure.
- **The dataset was rebuilt in 2026-09-25(e):** 17 rows had been graded the wrong way round, 55 had been dropped, and the P-510+ mini log was added (1,264 rows).
- **What the full record says** (2026-09-25(d); `research/settled_rows_2026-09-25/README.md`; 598 rows, 149 cards):
  - **Calibration overall is good:** slope 1.06, Brier 0.2249. **Skill is modest:** +7.7% over the base rate. No global shrink is warranted.
  - **Skill lives at p ≥ 0.65:** 80.3% at a stated 0.744. **Rows at 0.50–0.65 are coin-flip-grade:** 53.6% at 0.574. Label them `LOW_RESOLUTION` (`C-LOW-RESOLUTION-BAND`).
  - **Non-baseball underdog cushions (+k.5) are over-confident:** 17/40 at 0.642. `C-PLUS-CUSHION` applies: margin band, `BASELINE_P`, the P(win) + P(lose by ≤ k) decomposition and a named reason, or `PLUS_CUSHION_UNSUPPORTED` (M32).
  - **Print the sport's own track record** (`C-TRACK-RECORD`; `tools/calibration_report.py`). **`NO_DEMONSTRATED_SKILL`:** tennis, NFL/NCAA, AFL. Near-zero resolution: MLB, basketball. Clear skill: soccer.

### D8 Settlement and retrospectives (`METHOD.md` §7; `RULES_GENERAL.md` §"2026-09-24(f)")
- **Three terminal lineages** agree on the event, the explicit final marker and the score. A score without a final marker, or any credible live source, blocks settlement.
- **Process record.** Use the output of `receipts.py settle …`, which is one lineage, or a hand record carrying the same endpoints. Unsourced causal facts make the record `PROCESS_RECORD_UNVERIFIED`, and nothing may cite it.
- **Lineup diff:** "k of n named starters started" per side. A Rank-1 driver who did not play is `PROCESS_DEFECT: LINEUP_CLAIM_FALSE`.
- **Period scope:** a regulation-only contract settles on the regulation score (the receipt prints it; G-L16, M22).
- **z-scores:** print z_total and z_margin = (actual − centre)/width (`C-WIDTH-Z`).
- **Enhanced failure review** when the Rank-1 row loses, or when the top O/U loses or pushes (`TOP_OU_REVIEW`). Inspect wins as well as losses.
- **The three questions:** what the outcome turned on; whether it was knowable before issue (with evidence); the smallest justified change.
- **Summaries are copied from the issued Field 4 table,** never retyped (`C-SUMMARY-FROM-CARD`).
- **Settlement is read, never written (`C-SETTLEMENT-FROM-FEED`).** Linescores, lineup diffs, scorers and statistics come from `receipts.py` or from a fetched endpoint pasted with its URL. A script may assemble fetched data but never contain narrative literals.
  - P-510 and P-511 lineup diffs listed players who did not play, and P-515's score was wrong. Audit field `10n` checks that the diff's names are on the card.
- Run `python audit_card_controls.py <log> --settlement --strict` and record its table.

### D9 Learning discipline (`LEARNING_REGISTER.md`; `RULES_GENERAL.md` §"2026-09-24(f)"(f))
- **Every rule carries a receipt:** a status (`TESTING`, `PROMOTED_PROCESS` or `REFERENCE`), an evidence count and, if it is predictive, a prospective-test ID. A predictive idea from one or two events is `TESTING` and non-binding.
- **Open prospective tests** (none has a ranking effect until it concludes):
  - `C-WIDTH-Z`, `C-BASELINE-SKILL`, `C-PROB-EXTREMITY`, `C-RUN-CENTRE-BIAS`, `C-PHASE-VS-FULL-TOTAL`;
  - `T-TEN-LOWTIER-HCP`, `T-BKB-SEASON-OPENER-WIDTH`, `T-NHL-PRESEASON-GOALIE`, `T-MLB-WIND-IN-OVER`;
  - `C-TEN-FAV-SEPARATION`, `T-TEN-BENCHMARK-GAP`, `T-CRI-DOMINANT-HITTER`, `T-CRI-POST-TOSS-FREEZE`;
  - from 2026-09-25(d): `T-PLUS-CUSHION`, `C-LOW-RESOLUTION-BAND`, `T-TOTAL-DIRECTION-LEAGUE`;
  - from 2026-09-25(e): `T-RM1-PROSPECTIVE` (q against p), `T-TB1-ANCHOR` (cards against TB-1 in covered leagues), `T-NRL-BYE-RUST` (non-binding).
- **After every settlement or audit pass,** implement or explicitly disposition its "document mapping" table. Unexecuted mapping tables are how improvements were lost before.

### D10 Custody, logging and the repository
- **Parts 1–4 are closed.** Part 5 (`PREDICTION_LOG_COMBINED_5.md`) is the only active canonical log. Its top snapshot alone controls the next ID. `GAME_LOG_STATUS_CURRENT.md` is the state register.
- **New cards go to the active mini log** (`Mini logs (to be sent to actual log later)/…`) before delivery, and are registered in Part 5 within 24 hours.
- **IDs.** Use a `TMP-YYYYMMDD-<SPORT>-<A>-<B>` ID whenever a collision is possible. Never renumber.
- **Manifest.** Freeze the current `CONTROL_MANIFEST_*.md` SHA with every card. Any governance edit needs a new manifest (`tools/make_manifest.py`), a repointed `METHOD.md` header and a repointed active mini log. CI fails otherwise.
- **Repository hygiene.** Never commit dependency trees, `.pyc` files or local settings (`.gitignore`). Work on a branch, and let CI pass before merging (`CONTRIBUTING.md`).

## E. Sport quick cards

Each card lists what the card must print, plus the traps that recur. The detail is in the sport file's latest dated section and its SFA checklist.

**MLB / NPB / KBO** (`RULES_BASEBALL.md`)
- `receipts.py pregame mlb`: probables, official orders, gamefeed wind, umpires. Re-run within 60 minutes of first pitch.
- The venue row from `BASE_RATES_REGISTER.md` §7.5 (all 30 parks). League total mean 8.95, SD 4.51. First five innings: P(tied) 0.154.
- **Extras identity:** a tie at 9 adds at least one run, so the total exceeds any line equal to the regulation total.
- Push mass comes from the conditional distribution, not a cap. KBO and NPB innings caps allow official ties (G-L19).
- **+1.5 rows:** the baseline is 0.638 for either side (walk-off asymmetry); one-run games are 27.6% (covering pairs). MLB +1.5 rows have been calibrated (18/30 at 0.604) but no better than that baseline.
- **Track record:** MLB resolution is near zero (0.0075), so itemise every departure from `BASELINE_P`. NPB/KBO/CPBL Unders won 11/14 against Overs 4/9 (`T-TOTAL-DIRECTION-LEAGUE`).
- An opener's first inning is width, not direction. Baseball centres have run high (`C-RUN-CENTRE-BIAS`: accrue, no coefficient).
- **2026-09-25(e).**
  - TB-1 has **no** resolution in MLB, so anchor on the population: away/home +1.5 0.617/0.659; +2.5 0.718/0.749; P(total > 6.5) 0.686; P(total > 8.5) 0.491 (9-inning games).
  - Rank 1 is the highest RM-1 q, not a +1.5 by habit. Typical slates are `TOP2_COIN_FLIP` or `LEAN`.
  - The settlement lineup diff comes from the statsapi boxscore (starters are the `X00` entries).
  - NPB and KBO terminal state: the official score pages.

**Basketball: NBA, WNBA, NBL, FIBA, LKL, LMB** (`RULES_BASKETBALL.md` K-1 to K-8)
- Official starters from the box or preview. The NBL's actual tip is the first `jumpBall` event.
- Print the league total, the margin band for the line and the quarter shape: NBA Q4 is lower; the NBL second half is lower.
- Overtime is 4–5.5% of games and adds about 25 points.
- Reference widths as in §D5. Early-season and regime windows. A back-to-back is worth about −1.8 margin in the NBA, and nothing on totals.
- Leagues without a benchmark print `NOT_YET_DERIVED`; a width below 13.6 (total) or 9.4 (margin) needs a reason.
- **Underdog cushions (+k.5) won 3/8 at 0.58**, so `C-PLUS-CUSHION` applies (`card_math.py cover … --no-zero`). Resolution is near zero (0.012), so the departure ledger is mandatory.
- **2026-09-25(e).**
  - Print **`TEAM_BASELINE_P`** (`tools/team_baseline.py --league nba|wnba|nbl`) and anchor on it. Its side Brier is 0.216–0.223 against 0.248–0.256 for the base rate; NBL totals have no resolution.
  - The weaker team's **+1.5/+2.5/+3.5 covers only 0.32–0.45** (§7.7(c)). An unsupported cushion is flipped by RM-1.

**NHL** (`RULES_ICE_HOCKEY.md` H-R1 to H-R6)
- The official or confirmed goalie; preseason goalies stay projected.
- 24.8% of games reach overtime, and **overtime and shoot-out totals are odd**: a 2–2 tie goes Under 5.5, a 3–3 tie goes Over 6.5.
- **73% of two-goal regulation wins contain an empty-net goal.** A −1.5 row carries the empty-net branch as mass.
- Preseason totals run 5.3–5.7 against 6.25 in the regular season.
- `receipts.py settle nhl` gives the goalies' time on ice, empty-net goals and the regulation score.
- **2026-09-25(e).** TB-1 has no resolution; anchor on the population. RM-1 treats a +1.5 puck line like a baseball +1.5, with no cushion penalty.

**Soccer** (`RULES_SOCCER.md`; `LEAGUE_RULES_SOCCER.md`)
- The confirmed XI via the ESPN summary `rosters[]` or the official source.
- Regulation versus extra time is kept separate (G-L16). A draw is a third terminal state (G-L19).
- EPL references: first half P(≥ 2) 0.334; Over 2.5 0.550; draw 0.274; corners mean 10.0. A first-half Under 1.5 above about 0.75 needs a reason.
- **Corners settle with the field owner:** pulselive for the EPL, the UEFA matchstats API for UEFA competitions, ESPN `wonCorners` otherwise.
- Don't transfer EPL rates to cups or lower tiers (M12).
- **Track record: the clearest skill of any sport** (107/143 at 0.70; Brier 0.170), mainly phase and team-total rows. **Exception: underdog cushions won 8/13 at a stated 0.77**, so `C-PLUS-CUSHION` applies (Skellam margin).
- **2026-09-25(e).**
  - Rank 1/Rank 2 went 55 W / 17 L, and RM-1 leaves soccer order almost unchanged.
  - Split out "+0.5 / 1X" rows as double chances (2/5 at 0.73); +1.5 cushions won 7/8.
  - EPL `TEAM_BASELINE_P` has resolution for results, **not totals**.

**Tennis** (`RULES_TENNIS.md` TE-P5, TE-S2, TE-S4, TE-R1 to TE-R3)
- **The dated Elo benchmark (Tennis Abstract) is blocking.** Explain or rebuild if the gap exceeds 10 points.
- Matchup holds come from serve × return, with numerators and denominators.
- **Print P(deciding set)** against the reference (WTA 0.340). Total games is bimodal: 18.2 in straight sets, 28.6 in three.
- **Handicap coherence:** P(−k.5) ≤ P(win). Print c_s and c_d (WTA −5.5 references: 0.663 / 0.168).
- A walkover or retirement follows the stated void rules. ITF has no population reference.
- **`NO_DEMONSTRATED_SKILL`** (8/16 at 0.60; Brier 0.281). Stay near the Elo benchmark and the population rates unless serve/return numerators justify moving; the departure ledger is required.
- **2026-09-25(e).** RM-1's cushion term applies to +k.5 games handicaps (q ≈ 0.30 at a stated 0.58). A total-games Over at Rank 1 prints P(deciding set) against 0.340.

**Cricket** (`RULES_CRICKET.md` §2, controls 19–21; `LEAGUE_RULES_CRICKET.md`)
- **Toss, strip and conditions are separate fields** with separate ladders. Retrieve the toss at toss + 5 minutes (ESPN `notes[]`).
- **Phase totals** are a bat-first/chase mixture before the toss, or the realised branch after it, with windows split by innings order.
- Name the incoming Nos. 3–4 and both new-ball bowlers.
- **The chase is capped near the target:** a high chasing team-total Over is structurally disadvantaged.
- Settle from official scorecards, never narrative reports. Zero is not a duck.
- **Track record:** there is resolution but the probabilities are mis-stated (reliability 0.022). Unders won 9/12 at 0.589; Overs 7/12 at 0.631 (`T-TOTAL-DIRECTION-LEAGUE`).
- **2026-09-25(e).** Global recalibration only. Settlement tables must carry the contract text (several cricket rows were blank).

**AFL / NRL / rugby union / NFL** (`RULES_AFL.md`, `RULES_NRL_RUGBY.md`, `RULES_RUGBY_UNION.md`, `RULES_AMERICAN_FOOTBALL.md`)
- Sport-native state and endpoint rules are in each file.
- **NFL key numbers (2026-09-25(e)):** P(\|m\| = 3) 0.136–0.151; P(\|m\| = 7) 0.074–0.096. The TB-1 residual width is 13.6 (the G-L12 benchmark of about 13.9 is confirmed).
- **`NO_DEMONSTRATED_SKILL`** for NFL/NCAA (3/12 at 0.544; cushions 1/6) and AFL (3/10 at 0.662; cushions 0/3), both over-confident. The grade is capped at LOW, and the departure ledger and `C-PLUS-CUSHION` are required.
- **Population references now exist** for the NFL, AFL and NRL (`BASE_RATES_REGISTER.md` §7.7). Rugby union is still `NOT_YET_DERIVED`.
- **`TEAM_BASELINE_P`** (`--league nfl|afl|nrl`) is the anchor for sides (AFL 0.202 v 0.249). Totals anchor on the population, except the NFL (marginal).
- **Cushions on the TB-1 underdog cover:** NFL +1.5/+2.5/+3.5 0.35–0.54; NRL +1.5/+2.5 0.41–0.49; AFL +6.5 0.38–0.43. RM-1 flips unsupported cushions.
- **Rank 1/Rank 2 record: 12 W / 20 L,** the worst group. RM-1 held-out Rank 1 was 62.5% against 37.5% issued.
- **P-515's score was 36–20**, not 36–14 (grades unchanged). The NRL regular season is ESPN season type 1.

## F. Recurring mistakes to check on every card (M1–M32)

The full evidence is in `LEARNING_REGISTER.md` §"2026-09-25 audit closure" B and §"2026-09-25(b)" C.

| # | Mistake | # | Mistake |
|---|---|---|---|
| M1 | Exact-winner over-trust | M17 | Small-sample rate used as direction |
| M2 | Non-loss / double chance over-ranked | M18 | Top two structurally anti-coupled |
| M3 | Totals stacked off one factor | M19 | Published lineup not retrieved |
| M4 | Overtime or blowout tail ignored beside phase unders | M20 | Model summary used as the record |
| M5 | Cushion on a cold side missing its key player | M21 | Settlement route not consulted |
| M6 | Reputation over current power or park facts | M22 | Period-scope mismatch |
| M7 | Elite ceiling v "tough venue" under | M23 | "At least one O/U won" read as success |
| M8 | Bottom slot not tested | M24 | State-contaminated evidence window |
| M9 | Stale cached or proxy source | M25 | Personnel claim without retrieval or receipt |
| M10 | Kill path as prose, not mass | M26 | Process record written, not read |
| M11 | Uncertainty turned into an Over lean | M27 | Single-game predictive rule promoted |
| M12 | Tier gap read as scoring shape | M28 | Covering-pair record read as skill |
| **M13** | **Aggregate used where the game log was available (highest-value check)** | M29 | Summary retyped, not copied |
| M14 | Total probability not derived from the card's own centre and width | M30 | City forecast used instead of the gamefeed wind |
| M15 | Control listed but not executed | **M31** | **Width chosen without a reference** |
| M16 | Complement not itemised | **M32** | **Non-baseball underdog cushion priced like a baseball +1.5 (17/40 at 0.642; population cover of a small cushion is 0.32–0.54, §7.7(c))** |

**M26 recurrence (2026-09-25(e)):** the P-510–P-515 settlement was generated from typed strings. It carried false lineup diffs (P-510, P-511) and a wrong score (P-515). `C-SETTLEMENT-FROM-FEED` and audit `10n` are the controls.

## G. Tools and commands

All are standard-library Python 3.10+. Run from the repository root.

| Command | When |
|---|---|
| `python receipts.py pregame mlb <gamePk>` · `pregame espn <sport/league> <eventId>` | At freeze: state, lineups, weather, injuries |
| `python receipts.py settle mlb\|nhl\|espn … --card-away "A;B" --card-home "…"` | At settlement: sourced process record and lineup diff |
| `python audit_card_controls.py <log.md> --settlement --strict` | Every settlement pass (use `--allow-empty` for an empty log) |
| `python prediction_preflight.py <manifest.json>` | Automated pipelines only (interactive cards verify in the card body) |
| `python tools/skill_baseline.py` | After appending settled rows to `SKILL_BASELINE_LEDGER.md` |
| `python tools/card_math.py total\|cover\|departure …` | When building a card: derive every row from its own distribution; departure ledger |
| `python tools/team_baseline.py predict --league <nba\|wnba\|nbl\|nfl\|afl\|nrl\|epl\|mlb\|nhl> --home … --away … --date <local date> --total … --home-line …` | When building a card: `TEAM_BASELINE_P` and its flags |
| `python tools/rank_model.py rank --sport <league> --row "<contract>=<p>" …` | Field 4: RM-1 q, tiers, flags, the q order and `TOP2_QUALITY` |
| `python research/rank_model_2026-09-25e/validate_rank_model.py`, then `python tools/rank_model.py fit --fitted <date> --out tools/rank_model_coefficients.json` | At the 25-card review only, after rebuilding the dataset |
| `python research/settled_rows_2026-09-25/extract_settled_rows.py` then `python tools/calibration_report.py` | Every 25-card review: rebuild the settled-row dataset and report calibration and resolution |
| `python tools/verify_manifest.py` | Before issuing: governance files match the current manifest |
| `python tools/make_manifest.py --out CONTROL_MANIFEST_<date>-<n>.md --title … --note … [--model-change "…"]` | After any governance edit (`--model-change` whenever a coefficient, cap or ranking rule changes) |
| `python tools/repo_hygiene.py` | Before committing |
| `python -m unittest discover -s . -p "test_*.py"` and `… -s tools …` | Before committing (CI runs all of the above) |

## H. Where the detail lives

| Need | File |
|---|---|
| Workflow, card object, authority | `METHOD.md` |
| Scoring and evaluation maths | `SCORING_AND_VALIDATION.md` |
| Full gate definitions and dated controls | `RULES_GENERAL.md` (§16 controls what is mandatory; latest dated sections at the end) |
| Sport rules | `RULES_<SPORT>.md`, `LEAGUE_RULES_CRICKET.md`, `LEAGUE_RULES_SOCCER.md` |
| Control index | `CONTROLS.md` |
| Base rates and reference widths | `BASE_RATES_REGISTER.md` (§7) |
| Recency evidence | `RECENCY_AND_REBOUND.md` |
| Skill v baseline | `SKILL_BASELINE_LEDGER.md` |
| Sources and access | `SOURCES.md` (quick), `DATA_SOURCE_REGISTER.md` (full) |
| Lessons, tests, M-registry | `LEARNING_REGISTER.md` |
| Pregame research checklist | `UPCOMING_GAME_RESEARCH_GUIDE.md` (§19 one-page checklist and later dated steps) |
| Mini-log import, settlement procedure | `EXTERNAL_LOGGING_WORKFLOW.md` |
| Role and honesty boundary | `AGENT_ROLE_AND_TASK.md` |
| Numerical program (not built) | `NUMERICAL_PROGRAM.md`, `H0_DATASET_CARD.md` |
| Ranking model RM-1 (evidence, refit procedure) | `research/rank_model_2026-09-25e/README.md`; `tools/rank_model.py` |
| Team baseline TB-1, NFL/AFL/NRL references, cushion base rates | `research/team_baseline_2026-09-25e/README.md`; `tools/team_baseline.py`; `BASE_RATES_REGISTER.md` §7.7 |
| Active log / state register | `PREDICTION_LOG_COMBINED_5.md` / `GAME_LOG_STATUS_CURRENT.md` |
| History of changes | `CHANGELOG.md` |
| How to contribute and commit | `CONTRIBUTING.md` |

## I. Withdrawn or non-operative: never apply

- MLB run-line and push caps, and fixed variance floors.
- Order-statistic pseudo-tails; path-count or category ranking shortcuts.
- Universal 40–60% top-slot bands; blanket `DISJOINT` bans; `UNORDERED` escapes.
- Normalised-edge ordering.
- "At least one O/U won" as evidence.
- Rebound, hangover or "due" rules.
- MLB doubleheader-G1 deflation.
- Derby Under suppression.
- "Dual run-line arbitrage".
- The FIBA qualifier pace coefficient; the clay handicap cap.
- Bowl-first means low-scoring.
- Cushion implies underdog winner; winner implies games handicap.
- Guaranteed venue-history availability.
- Any single-game coefficient.

Sources: `RULES_GENERAL.md` §16.10–§16.11 and §"2026-09-24(f)"(a); `METHOD.md` §11.
