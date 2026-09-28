# Current rules — the operating manual

**Method MDS-2026.09.28-v5.0 (md-only) · Control revision CR-2026.09.28-MD1 · Scoring SCV-2026.09.19-v2.** The freeze receipt is the control manifest named in `METHOD.md`'s header. Every record is LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

**What changed on 2026-09-28.** The user instructed that the forecasting model uses Markdown documents only: no Python and no non-Markdown repository file, in the future. So this manual is now self-contained.
- **Every step that used a tool** has a Markdown procedure. The probability arithmetic, the team baseline (TB-1-MD) and the ranking model (RM-1) are in `PROBABILITY_TOOLKIT.md`, and were checked against the tools they replace. The card, settlement and log formats, and the self-audit, are in `CARD_AND_LOG_TEMPLATES.md`.
- **Sources** were merged into one register and re-verified by live request (`SOURCES.md`).
- **Redundant documents** were retired to `archive/superseded_2026-09-28/`, with a map of where every live rule went (`archive/superseded_2026-09-28/README.md`).
- **No probability, width, centre or ranking rule changed** (`C-RULE-FREEZE`), with two measured effects (`PROBABILITY_TOOLKIT.md` §4.3–§4.4):
  - the hand-computed baseline is at least as accurate as the tool it replaces;
  - under the existing rule "anchor on TB-1 where it has resolution", a preregistered held-out test (P6) extended the anchor to four more soccer leagues' results and two leagues' totals.

**Precedence.**
1. The user's current instructions.
2. This manual.
3. The sport file's §0 page.
4. `PROBABILITY_TOOLKIT.md`, `CARD_AND_LOG_TEMPLATES.md` and `SOURCES.md`.
5. Everything else, which is reference or history.

A dated section, archived text or old card never reinstates a withdrawn rule (§I). Python in `tools/` is maintainer tooling only (CI, research, manifests). The model never needs it, and a card never waits for it.

---

## 0. Reading order (`C-READING-GATE`)

**Before every card, read in full:**
1. this manual;
2. the sport file's **§0 live page** (`RULES_<SPORT>.md`), plus `LEAGUE_RULES_CRICKET.md` or `LEAGUE_RULES_SOCCER.md` for those sports;
3. `CARD_AND_LOG_TEMPLATES.md` §1 (the card) and §5 (the self-audit);
4. the sport's section of `SOURCES.md` (§3.x) and §1 (source rules);
5. the active mini log's header and its unsettled section, plus the active canonical log's top snapshot (next ID, open follow-ups).

**Read by citation when the card needs it:** `PROBABILITY_TOOLKIT.md` (every calculation), `BASE_RATES_REGISTER.md` (reference rows and widths), the rest of the sport file, and `LEARNINGS_INDEX.md` (lessons, one line each).

---

## A. Non-negotiables

1. **Sports only, market-blind.** Odds, prices, line movement, tipsters, betting previews, prediction markets and fantasy/DFS material are never evidence, anchors or sanity checks (`SOURCES.md` §1.4).
   - A supplied line is contract metadata. It is quarantined until the distribution is frozen.
   - The only market use is after settlement, by the operator (`C-MARKET-BENCHMARK`, `MARKET_BENCHMARK_LEDGER.md`). The model never reads that ledger.
2. **Never fabricate.** A missing lineup, timestamp, probability or record stays missing: `UNAVAILABLE`, `NOT_RETRIEVED`, `NOT_YET_DERIVED`. A number that cannot be reproduced from the printed distribution is invented precision.
3. **Learning-only.** No performance, calibration, ROI or value claim follows from any record.
4. **Three independent lineages** to issue an event, and three to settle it. Mirrors and syndication count once; snippets never count (`SOURCES.md` §1.1).
5. **Pregame means before the actual start** (the first ball, pitch, puck or tip; NBL: the first `jumpBall` event).
   - Take as long as the research needs. Refresh volatile news as late as possible, and freeze just before the start.
   - A card completed after the start is labelled `LIVE_ISSUED`. It is logged, but excluded from pregame scoring, and it uses no in-game information.
6. **Issued records are immutable.** Corrections are appended, never rewritten.
7. **Distribution first.** One coherent joint outcome distribution per event. Every row's probability p is read from it with the toolkit arithmetic, shown on the card.
8. **No coefficient from this log's own results.** A single game can expose a bug or open a prospective test. It never creates a weight, cap or ranking override (L-087).
9. **Read the record; don't write it.** Every settlement fact comes from a named endpoint with its retrieval time (`C-PROCESS-RECORD-PROVENANCE`, `C-SETTLEMENT-FROM-FEED`).
10. **Honest labels.** Coin flips are called coin flips (`NEAR_TIED`, `TOP2_COIN_FLIP`). Forced and covering pairs are labelled; a mechanical win is not skill.
11. **Markdown only (2026-09-28).** The model reads and writes `.md` files only. It uses no Python, JSON, CSV or other repository file. Web sources in any format are fine (`SOURCES.md`).

## B. The workflow

| Step | What to do | Hard stop if … |
|---|---|---|
| 0 | **Read** §0. **Check the queue:** settle any earlier final first. Get the next canonical ID from the active log's top snapshot; if it is unclear or on hold, use `TMP-YYYYMMDD-<LEAGUE>-<HOME>-<AWAY>`. **Declare the universe:** before the day's first card, write the day's `UNIVERSE` table in the mini log (`CARD_AND_LOG_TEMPLATES.md` §4): every event in the leagues you intend to card, with IDs and start times (`C-EVENT-UNIVERSE`) | The next ID or the event state is unclear: use a TMP ID |
| 1 | **Identity and state.** Event, competition, venue, venue-local date and time, IANA timezone, AEST/AEDT conversion (with any date rollover). State from the feed (`SOURCES.md` §2.1 or the league's own feed): PREGAME / LIVE / FINAL. Never infer state from the clock alone. User-supplied times are estimates until verified | Not PREGAME: finish only as `LIVE_ISSUED` |
| 2 | **Contract.** Parse each supplied row exactly: target, period, line, and push/void/overtime/tie terms. Quarantine the line | Ambiguous: flag it; never silently "fix" a row |
| 3 | **Participants.** Official lineup, starters, goalie, pitchers and team sheet first, with fetch time (`SOURCES.md` §1.5). Injuries, suspensions, rest and coaching changes. Mark each as confirmed or projected | A Rank-1 total or margin row depends on an unretrieved lineup (G14.2) |
| 4 | **Environment.** Outdoor events: an hourly venue-coordinate forecast for the match window (`SOURCES.md` §2.2). MLB: the gamefeed weather block | An outdoor card without it |
| 5 | **Evidence.** Game logs before aggregates (M13). L5/L10/L15/L20 descriptively. The season rate plus the opponent (§D5) | An aggregate carries direction while the game log is one click away: mark `AGGREGATE_ONLY` and cap the row |
| 6 | **Baselines and distribution.** Print `BASELINE_P` (the population row) and `TEAM_BASELINE_P` (TB-1-MD, `PROBABILITY_TOOLKIT.md` §4). Build the prior plus named adjustments → centre and width → the family table with masses. Print the reference row and reference width (`BASE_RATES_REGISTER.md` §7). Read every row's p off the distribution with the toolkit arithmetic, shown | p cannot be reproduced from what is printed |
| 7 | **Rank.** RM-1 q for each row (`PROBABILITY_TOOLKIT.md` §5): tier, flags, order by q, `TOP2_QUALITY`. Label `FORCED_PAIR`/`FREE` and `COVERING_PAIR`. Print P(R1∧R2) and P(¬R1∧¬R2) from p, the complement decomposition, and kill paths as weighted branches | A joint number is invented: use `JOINT_UNQUANTIFIED` with Fréchet bounds |
| 8 | **Freeze.** Final volatile refresh; freeze time; the method, control revision and manifest name with its SHA (copied from the **Current freeze receipt** line at the top of `GAME_LOG_STATUS_CURRENT.md`); `UNIVERSE:` or `OUT_OF_UNIVERSE`. Run the self-audit (`CARD_AND_LOG_TEMPLATES.md` §5). **Append the card to the active mini log before delivering it** | A blocking self-audit item fails |
| 9 | **Settle** (only when final). Three terminal lineages; the process record read from the feed with its endpoint and time; the lineup diff; z-scores; the p **and** q grades; enhanced reviews (§D8). Use `CARD_AND_LOG_TEMPLATES.md` §2 | Any credible live or conflicting source |
| 10 | **Learn.** The three questions; dispositions to the mini log's learnings and its **document mapping**; the baseline ledger row (`SKILL_BASELINE_LEDGER.md`); skips for uncarded universe events | A new predictive rule while `C-RULE-FREEZE` is in force: open a TESTING row instead |

## C. The card

The exact template is `CARD_AND_LOG_TEMPLATES.md` §1. It has six fields plus the completeness block:

| Field | Must contain |
|---|---|
| 1 Identity and contract | ID; participants; competition; times (venue-local, UTC, AEST); state; exact contracts; method, control revision and manifest |
| 2 Evidence and exposure | Sources with owner, time and status (OPENED / SNIPPET / ASSUMED); participants per side (confirmed or projected); injuries and workload; environment; windows; disaggregated records; settlement route |
| 3 Joint distribution | Prior with provenance; named signed adjustments; centre, median and width; the **family table with masses summing to 1**; phase and team marginals; representative score; **reference row** and **reference width**; the arithmetic that turns the distribution into each row's p |
| 4 Contract queries and ranks | Per row: p (`UNVALIDATED_SUBJECTIVE`), **`BASELINE_P`**, **`TEAM_BASELINE_P`**, **RM-1 q, tier and flags**; ranks by q; **`TOP2_QUALITY`**; `FORCED_PAIR`/`FREE`; preferred side; push mass; departure ledger; track-record row; **predictability row** (§D6); `LOW_RESOLUTION` at 0.50–0.65; the `C-PLUS-CUSHION` decomposition for non-baseball +k.5; projected winner with its probability; alternatives (unranked) |
| 5 Dependence and checks | P(R1∧R2), P(¬R1∧¬R2), and P(all fail) where three or more rows share a driver; complement decomposition; kill paths with mass; `COVERING_PAIR` |
| 6 Freeze and follow-up | Freeze receipt, manifest SHA, settlement route, `UNIVERSE:` line, and `SHADOW: NO_LANE (md-only)`. At settlement: sourced process record, lineup diff (names must be on the card), z, p and q grades, reviews |

## D. Rules by topic

### D1 Identity, time and state
- Verify the venue-local time and zone, and convert to AEST/AEDT. Print any correction to the user's time.
- **Merging two views** requires date, venue, home/away and starters all to match (`O-ID-DATE-STARTER-MATCH`). Otherwise it is a new event and a new ID.
- **A new competition, or a new season after a gap:** re-verify the rules and format with the field owner before modelling (sport file §9).
- **Preseason is not the regular season.** Its scoring, rotation and goalie rules differ; use the preseason rows (e.g. NHL preseason totals 5.3–5.7).

### D2 Sources
All in `SOURCES.md`:
- **Ladder:** field owner → official team or player → structured API → independent quality media → fallback.
- **Access modes:** API / Browser / Proxy (`r.jina.ai`). ESPN routes reject a browser user-agent. NHL api-web, Tennis Abstract, UEFA and Squiggle need one.
- **Critical dynamic fields** (lineup, starter, toss, goalie): the field owner, or two genuinely independent current lineages, or leave the field unresolved.
- **Excluded:** market material, synthetic content, and search summaries as facts.

### D3 Participants and lineups (M19, M25)
- **An official lineup published before the freeze always wins,** printed with its fetch time.
- `PROJECTED_BEAT_VERIFIED` needs a printed S-1 Rev 2 receipt: outlet, reporter, timestamp, verbatim quote, and two sources.
- Preseason goalies stay `PROJECTED`. Social media is not a lineup source.
- **Every decision-driving player has a quantified line** (minutes, usage, the rate) or is marked `AGGREGATE_ONLY`.

### D4 Environment
- **Outdoor:** an hourly forecast at the venue's coordinates, from about an hour before the start to the plausible end, in venue-local time. Downgrade for rain only inside the match window (G15.1).
- **MLB:** the statsapi gamefeed `weather` block at freeze (field-relative wind), or `WEATHER_NOT_YET_PUBLISHED`. **Never substitute a city forecast** (M30).

### D5 Building the distribution
- **Anchor.** Start each row at its baseline:
  - where the toolkit's §4.3 table says TB-1-MD has resolution, anchor on `TEAM_BASELINE_P`:
    - sides and results: NBA, WNBA, NBL, NFL, AFL, and soccer's EPL, La Liga, Bundesliga, Serie A and Ligue 1;
    - totals: NBA, WNBA, La Liga and the Bundesliga;
  - everywhere else, anchor on the population `BASELINE_P`.
- **Signed adjustments need a named mechanism:** a confirmed absence, a pitch limit, a role change, a lineup change, a weather reading, a tactical change. **Uncertainty goes into the width, not a lean** (G-L2, M11).
- **Recency (R-1).** Recent results revise a rate only through a named mechanism. There is no rebound in any competition measured. The last game is the worst predictor in 6 of 6 competitions. In basketball, the opponent's defence to date beats any recency window.
- **Reference row and width** (`BASE_RATES_REGISTER.md` §7). Print both beside the card's centre and width, or print `NOT_YET_DERIVED`. **A width below 0.85 × the reference names what the card knows.** Reference widths:

  | League | Total | Margin |
  |---|---:|---:|
  | NBA | 19.4 | 15.1 |
  | WNBA | 19.5 | 13.3 |
  | NBL | 18.7 | 15.2 |
  | NFL | 13.4 | 13.6 |
  | AFL | 29.1 | 36.8 |
  | NRL | 13.9 | 19.9 |
  | NHL | 2.29 | 2.57 |
  | MLB | 4.50 | 4.57 |
  | EPL | 1.61 | 1.51 |
  | WTA best-of-3 total games (raw SD) | 5.79 | — |

  Recent basketball total widths ran about 39% too narrow (M31).
- **Windows and regimes:**
  - NBL early season **−8.5** points; WNBA early season **+6.5**.
  - WNBA 2026 ran **+10.7** over 2024–25: exclude or adjust those seasons (M24).
  - NHL and NBA preseason use preseason rows.
- **Coherence.** Each total's probability comes from the card's own centre and width (M14). Keep mean and median distinct.
- **Departure ledger** (`C-DEPARTURE-LEDGER`; `PROBABILITY_TOOLKIT.md` §8). Print each row's logit departure from its anchor, attributed to named mechanisms. More than 10% unattributed is `UNEXPLAINED_DEPARTURE`, and the grade is capped at LOW.

### D6 Ranking, predictability and dependence
- **Order by RM-1 q** (`PROBABILITY_TOOLKIT.md` §5). Stated p is printed unchanged beside q, and breaks ties within 0.005. Rows that cannot be separated get unique ordinals labelled `NEAR_TIED`, with the non-predictive tie-break stated.
- **`SIDE_FLIP`** (q crosses 0.5 by ≥ 0.05): the flipped side is ranked by q, capped at SUPPORTED, and given a reconciliation line.
  - The stated side may be kept only when TB-1-MD, where it has resolution, gives that side ≥ 0.55. A narrative is never an override.
  - `NEAR_TIED_FLIP` keeps the stated side as a coin flip.
- **q is a ranking score, not an event probability.** Never multiply q values, and never use q for joint or pair numbers (use p).
- **`TOP2_QUALITY`:** STRONG / SUPPORTED / TOP1_ONLY / COIN_FLIP, from the effective tiers. Under `TOP2_COIN_FLIP`, the delivery says plainly that the top two are near coin flips.
  - **Rank 1 is only "far more likely to win than lose" in the STRONG tier** (q ≥ 0.70). Historically that won 81% of decisions (73% as Rank 1); below it, 52–63%.
- **Predictability row (`C-PREDICTABILITY-MAP`; `BASE_RATES_REGISTER.md` §7.8).** Print the league's share of games with a 0.70+ favourite and how often those won. Where a league rarely produces STRONG favourites, say that the *slate* cannot produce a STRONG Rank 1:

  | League | Favourite ≥ 0.70 | Those won |
  |---|---:|---:|
  | AFL | 39% | 90.6% |
  | WNBA, NBA, NBL | 26–29% | 80–84% |
  | NFL | 27% | 73.1% (the 0.70–0.80 band won about 2 in 3) |
  | NRL | 19% | 68.3% |
  | NHL | 6% | 72.9% |
  | Soccer (three-way) | 6% | small n |
  | MLB | 0% | — |

  Totals rarely reach 0.70 anywhere.
- **Optional `SLATE_ADVISORY`:** up to two same-event contracts that the card's own distribution prices at q ≥ 0.70. They are not ranked, not scored and not a betting recommendation.
- **No pooled band forces an ordinal:** no 40–60% floor, no slot-history fade. Ranks 2–4 carried no ordering information historically (54–56% each), so report probabilities, not slots.
- **Bottom row (G27):** write its best case in full and run the swap test against the row above it.
- **Pairs:**
  - label each over/under pair `FORCED_PAIR` or `FREE`, and freeze the preferred side;
  - a `COVERING_PAIR` (two rows covering every outcome) has a mechanical Hit@2 that is excluded from top-two summaries. Never seek such a pair to guarantee a win;
  - a supplied slate of two complementary pairs always settles 2 W / 2 L. Say so in the delivery.
- **Print:** P(R1∧R2) with its coupling sign; P(¬R1∧¬R2), and P(all fail) where three or more rows share a driver; the complement decomposition of R1 and R2 across the kill paths (M16); every kill path as a weighted branch, not prose (M10).

### D7 Probability, baselines and scoring
- **Every ranked row carries an `UNVALIDATED_SUBJECTIVE` p** that can be reproduced from the printed distribution.
- **`BASELINE_P`** (`C-BASELINE-SKILL`) is the naive population probability of the same contract, from completed games before the event, knowing only home/away. It comes from `BASE_RATES_REGISTER.md`. For a non-baseball +k.5 on the TB-1 underdog, use the §7.7(c) cushion table. If none exists, print `NOT_YET_DERIVED`.
- **`TEAM_BASELINE_P`** is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4):
  - where TB-1 has no resolution, print it with `TB1_NO_RESOLUTION:<target>`;
  - in uncovered leagues, print `NOT_COVERED` or `UNVALIDATED:<league>`.
- **The seed comparison:** the cards have not yet beaten the naive baseline (0.2461 against 0.2360; n = 29; the interval spans 0).
- **Scoring:** half-scaled W/P/L Brier for push-capable rows. A forced pair counts once in decision metrics. Score both p and q (`PROBABILITY_TOOLKIT.md` §10).
- **Top-slot measures:** the Rank-1 record; the preferred side of the top over/under; Hit@2 excluding covering pairs. "At least one O/U won" is never a success measure (M23).
- **Historical calibration is a diagnostic only.** The 2026-09-26 figures used a `p ≥ 0.5` proxy. Strict extraction (2026-09-28) certifies zero performance-eligible legacy rows.

### D8 Settlement and retrospectives
Template: `CARD_AND_LOG_TEMPLATES.md` §2.
- **Three terminal lineages** agree on the event, an explicit final marker and the score. A score without a final marker, or any credible live source, blocks settlement.
- **The process record is read from a named endpoint** with its retrieval time. It is never typed from memory or narrative. Unsourced causal facts make the record `PROCESS_RECORD_UNVERIFIED`, and nothing may cite it.
- **Lineup diff:** "k of n named starters started" per side. The names must be on the card. A Rank-1 driver who did not play is `PROCESS_DEFECT: LINEUP_CLAIM_FALSE`.
- **Period scope:** a regulation-only contract settles on the regulation score (G-L16, M22).
- **Frozen fields are copied, never replaced.** Settlement tables copy p, q, `BASELINE_P` and `TEAM_BASELINE_P` exactly as issued, missingness labels included. Never substitute 0.500 for a missing baseline (the 2026-09-28 review found 20 of 20 settlement baseline cells replaced).
- **z-scores:** z_total and z_margin = (actual − centre)/width (`C-WIDTH-Z`).
- **Enhanced failure review** when Rank 1 loses, or when the top over/under loses or pushes (`TOP_OU_REVIEW`). Inspect wins as well as losses.
- **The three questions:** what the outcome turned on; whether it was knowable before issue (with evidence); the smallest justified change.
- **Summaries are copied from the issued Field 4 table,** never retyped (`C-SUMMARY-FROM-CARD`).
- **Kill paths are checked honestly.** If a named kill-path state occurred, say so, even when the row won.
- **Self-audit at settlement:** `CARD_AND_LOG_TEMPLATES.md` §5, settlement block.

### D9 Learning discipline and the rule freeze
- **`C-RULE-FREEZE`.** Until `C-BASELINE-SKILL` (100 prospective decisions / 30 cards) and `T-RM1-PROSPECTIVE` (25 cards) report, a change may only be:
  - a validity repair;
  - a retrieval or integrity control;
  - a measurement or disclosure control that moves no probability, rank, width or centre;
  - documentation.

  A `MODEL_CHANGE` needs the user's explicit instruction. **The user's bar (2026-09-27):** change a model only if it is demonstrably better, meaning a preregistered test with a 95% interval below 0 on held-out data that did not suggest it.
- **Gates at 2026-09-28** (counted from `SKILL_BASELINE_LEDGER.md` and the logs):

  | Gate | Progress |
  |---|---|
  | `C-BASELINE-SKILL` | 0/100 |
  | `T-RM1-PROSPECTIVE` | 0/25 cards |
  | `C-MARKET-BENCHMARK` | 0/100 |
  | `T-FAV70-BAND` | 0/100 band games per league |
  | `T-TB1MD-NRL` | awaits NRL 2027 |

  Maintainers can print the live counts with `python tools/evidence_status.py`; the model counts from the ledgers.
- **Every rule carries a receipt:** a status (`TESTING`, `PROMOTED_PROCESS` or `REFERENCE`), an evidence count and, if it is predictive, a prospective-test ID. A predictive idea from one or two events is `TESTING` and non-binding.
- **Open tests** (none has a ranking effect until it concludes):
  - `C-WIDTH-Z`, `C-PROB-EXTREMITY`, `C-RUN-CENTRE-BIAS`, `C-PHASE-VS-FULL-TOTAL`;
  - `T-TEN-LOWTIER-HCP`, `T-BKB-SEASON-OPENER-WIDTH`, `T-NHL-PRESEASON-GOALIE`, `T-MLB-WIND-IN-OVER`;
  - `C-TEN-FAV-SEPARATION`, `T-TEN-BENCHMARK-GAP`, `T-CRI-DOMINANT-HITTER`, `T-CRI-POST-TOSS-FREEZE`;
  - `T-PLUS-CUSHION`, `C-LOW-RESOLUTION-BAND`, `T-TOTAL-DIRECTION-LEAGUE`;
  - `T-RM1-PROSPECTIVE`, `T-TB1-ANCHOR`, `T-NRL-BYE-RUST`, `T-FAV70-BAND`, `T-TB1MD-NRL`;
  - `O-NPB-ERA-CENTRE`, `T-UNIVERSE-VS-SELECTED`, `C-MARKET-BENCHMARK`, `T-CRICKET-V2-UNSEEN`.

  Definitions are in `LEARNINGS_INDEX.md`.
- **After every settlement or import,** implement or explicitly disposition each row of the document-mapping table. Unexecuted mapping tables are how improvements were lost before.

### D10 Custody and logging
- **Part 5 (`PREDICTION_LOG_COMBINED_5.md`) is the only active canonical log.** Parts 1–4 are closed. Its top snapshot controls the next ID; `GAME_LOG_STATUS_CURRENT.md` is the state register.
  - **2026-09-28:** P-518–P-522 are reserved while they are reconciled (`reviews/2026-09-28/`). Until the snapshot names the next ID, new cards use TMP IDs.
  - **The P-518 onward mini log must stay byte-for-byte unchanged** during that reconciliation. New cards go into a **new** mini log (`PROMPTS.md` §1; `CARD_AND_LOG_TEMPLATES.md` §3).
- **New cards go to the active mini log before delivery.** It lives in `Mini logs (to be sent to actual log later)/` in the repository, or the one designated Drive folder. Cards are registered in Part 5 at the next import.
- **IDs:** use a TMP ID whenever a collision is possible. Never renumber or overwrite an issued ID. The verifiably timestamped card takes the lower number.
- **The manifest:** copy its name and SHA onto every card, from the **Current freeze receipt** line at the top of `GAME_LOG_STATUS_CURRENT.md`. Governance edits and new manifests are maintainer work, done in a repository session (`CONTRIBUTING.md`).
- **The universe** is declared in the mini log (`CARD_AND_LOG_TEMPLATES.md` §4). A declared universe is never edited; skips are appended.

## E. Sport quick cards

The live rules are in each sport file's §0 page. This section lists only what every card must print, plus the traps that recur.

**Every sport** prints: `BASELINE_P`; `TEAM_BASELINE_P` (TB-1-MD or its status); RM-1 q; the reference row and width; the predictability row; and `SHADOW: NO_LANE (md-only)`.

**Shadow models.** The shadow models (`tools/mlb_model.py`, `tools/sport_models.py`) need Python. From 2026-09-28 they run only if a maintainer happens to run them before the start; otherwise print `SHADOW: NO_LANE (md-only)`. `C-MLB-SHADOW` and `C-SPORT-SHADOW` are suspended, not failed.

**MLB, NPB and KBO** (`RULES_BASEBALL.md`)
- **Before first pitch:** probables, official orders (`battingOrder`), gamefeed wind and umpires. Re-check within 60 minutes of first pitch.
- **Reference rows:**
  - the venue row (`BASE_RATES_REGISTER.md` §7.5, all 30 parks);
  - the league total, mean 8.95, SD 4.51;
  - the first five innings, P(tied) 0.154.
- **Totals and run lines:**
  - totals come from the negative binomial tables (`PROBABILITY_TOOLKIT.md` §3);
  - run lines come from the home/away shares: home −1.5 = P(home wins) × 0.684; away −1.5 = P(away wins) × 0.769;
  - both +1.5 rows sit at the 0.638 baseline; one-run games are 27.6% (covering pairs).
- **Extras identity:** a tie at 9 adds at least one run. NPB and KBO can end tied; print P(tie).
- **TB-1 has no resolution in MLB,** so anchor on the population. Typical slates are `TOP2_COIN_FLIP` or `LEAN`: MLB has no STRONG favourites.
- **Track record:** resolution is near zero, so itemise every departure. NPB/KBO/CPBL Unders won 11/14 (`T-TOTAL-DIRECTION-LEAGUE`, accrue only).

**Basketball: NBA, WNBA, NBL, FIBA, EuroLeague, ACB, LKL, LNBP** (`RULES_BASKETBALL.md`)
- **Before the tip:** official starters and the injury report. The NBL tip is the first `jumpBall`.
- **Sides:** anchor on TB-1-MD in the NBA, WNBA and NBL. **Totals:** anchor on TB-1-MD in the NBA and WNBA, and on the population in the NBL.
- **Game shape:** overtime is 4–5.5% of games and adds about 25 points. The NBA Q4 is lower; the NBL second half is lower.
- **The weaker team's +1.5/+2.5/+3.5 covers only 0.32–0.45** (`C-PLUS-CUSHION`). RM-1 flips unsupported cushions.
- **Basketball sides are the most predictable team-sport rows here:** 26–29% of games have a 0.70+ favourite, and those win 80–84%.

**NHL** (`RULES_ICE_HOCKEY.md`)
- **Before puck drop:** the official or confirmed goalie; preseason goalies stay projected.
- **Overtime structure:** 24.8% of games reach overtime, and overtime and shoot-out totals are odd.
- **Puck line:** −1.5 = P(win) × 0.568, and it is mostly an empty-net goal.
- **Anchoring:** no TB-1 resolution, so anchor on the population. Preseason totals are 5.3–5.7.

**Soccer** (`RULES_SOCCER.md`; `LEAGUE_RULES_SOCCER.md`)
- **Lineups:** the club's official XI about 60 minutes before kick-off.
- **Endpoints:** regulation and extra time are kept separate; a draw is a third outcome.
- **Probabilities:** from the Poisson tables (`PROBABILITY_TOOLKIT.md` §2).
- **Anchors (P6, 2026-09-28):** results anchor on TB-1-MD in the EPL, La Liga, the Bundesliga, Serie A and Ligue 1. Totals anchor on it in La Liga and the Bundesliga, and on the population elsewhere.
- **Corners** settle with the field owner (`SOURCES.md` §3.4).
- **Transfer:** never carry EPL rates to cups or lower tiers (M12).
- **Track record:** the strongest resolution of any sport, mostly phase and team-total rows. Underdog cushions won 8/13 at a stated 0.77.

**Tennis** (`RULES_TENNIS.md`)
- **The dated Tennis Abstract Elo benchmark is blocking** (`PROBABILITY_TOOLKIT.md` §6). Explain any gap above 10 points.
- **Match structure:**
  - holds come from serve × return, with their numerators;
  - print P(deciding set) against the 0.340 reference (WTA);
  - total games is bimodal: 18.2 in straight sets, 28.6 in three.
- **Handicaps:** P(−k.5) ≤ P(win). **Retirements** follow the stated void rules.
- **`NO_DEMONSTRATED_SKILL`:** stay near Elo unless the numerators justify moving.

**Cricket** (`RULES_CRICKET.md`; `LEAGUE_RULES_CRICKET.md`)
- **Toss, strip and conditions** are separate fields, each with its own ladder (`SOURCES.md` §3.3).
- **"1st innings"** means the team batting first; say what happens if the named team bats second.
- **Phase totals:** a bat-first/chase mixture before the toss, the realised branch after it.
- **The chase is capped near the target.**
- **Settlement:** from the official scorecard, never a narrative. Zero runs is not a duck without a dismissal.

**AFL, AFLW, NRL, rugby union and the NFL** (`RULES_AFL.md`, `RULES_NRL_RUGBY.md`, `RULES_RUGBY_UNION.md`, `RULES_AMERICAN_FOOTBALL.md`)
- **TB-1-MD anchors sides** in the NFL and the men's AFL. NRL sides, all their totals, and AFLW/rugby union anchor on the population.
- **Underdog cushions cover:** NFL +1.5/+2.5/+3.5 0.35–0.54; NRL +1.5/+2.5 0.41–0.49; AFL +6.5 0.38–0.43.
- **NFL key numbers:** P(|m| = 3) 0.136–0.151; P(|m| = 7) 0.074–0.096.
- **An NFL model favourite at 0.70–0.80 has won about 2 in 3.**
- **Track record:** Rank 1/Rank 2 went 12 W / 20 L, the worst group. The grade is capped at LOW, and the departure ledger and `C-PLUS-CUSHION` are required.

## F. Recurring mistakes to check on every card (M1–M34)

| # | Mistake | # | Mistake |
|---|---|---|---|
| M1 | Exact-winner over-trust | M18 | Top two structurally anti-coupled |
| M2 | Non-loss / double chance over-ranked | M19 | Published lineup not retrieved |
| M3 | Totals stacked off one factor | M20 | Model summary used as the record |
| M4 | Overtime or blowout tail ignored beside phase unders | M21 | Settlement route not consulted |
| M5 | Cushion on a cold side missing its key player | M22 | Period-scope mismatch |
| M6 | Reputation over current power or park facts | M23 | "At least one O/U won" read as success |
| M7 | Elite ceiling against a "tough venue" under | M24 | State-contaminated evidence window |
| M8 | Bottom slot not tested | M25 | Personnel claim without retrieval or receipt |
| M9 | Stale cached or proxy source | M26 | Process record written, not read |
| M10 | Kill path as prose, not mass | M27 | Single-game predictive rule promoted |
| M11 | Uncertainty turned into an Over lean | M28 | Covering-pair record read as skill |
| M12 | Tier gap read as scoring shape | M29 | Summary retyped, not copied |
| **M13** | **Aggregate used where the game log was available (the highest-value check)** | M30 | City forecast used instead of the gamefeed wind |
| M14 | Total probability not derived from the card's own centre and width | **M31** | **Width chosen without a reference** |
| M15 | Control listed but not executed | **M32** | **Non-baseball underdog cushion priced like a baseball +1.5** |
| M16 | Complement not itemised | **M33** | **Rule churn outruns evidence** |
| M17 | Small-sample rate used as direction | **M34** | **Self-selected sample read as the competition** |

**M35 (added 2026-09-28): frozen field replaced at settlement.** A baseline, q or missingness label was retyped (e.g. 0.500) instead of copied. Control: §D8, "Frozen fields are copied, never replaced".

## G. Where things live

| Need | File |
|---|---|
| This manual | `CURRENT_RULES.md` |
| All probability arithmetic, TB-1-MD, RM-1, Elo, scoring | `PROBABILITY_TOOLKIT.md` |
| Card, settlement, mini log, universe, ledger rows, self-audit | `CARD_AND_LOG_TEMPLATES.md` |
| Prompts to paste into a chat | `PROMPTS.md` |
| Sources and access | `SOURCES.md` |
| Sport rules | `RULES_<SPORT>.md` (§0 is live), `LEAGUE_RULES_CRICKET.md`, `LEAGUE_RULES_SOCCER.md` |
| Reference rates, widths, the predictability map | `BASE_RATES_REGISTER.md` |
| Lessons, tests and M-registry, one line each | `LEARNINGS_INDEX.md` (the evidence is in `LEARNING_REGISTER.md`) |
| Skill against the baseline | `SKILL_BASELINE_LEDGER.md` |
| Active log and state register | `PREDICTION_LOG_COMBINED_5.md` / `GAME_LOG_STATUS_CURRENT.md` |
| Method version and freeze receipt | `METHOD.md` (header) |
| Scoring and evaluation mathematics (maintainers) | `SCORING_AND_VALIDATION.md` |
| History of changes | `CHANGELOG.md` |
| Retired documents, and where their rules went | `archive/superseded_2026-09-28/README.md` |
| Maintainer tooling (never needed by the model) | `tools/`, `CONTRIBUTING.md` |

## I. Withdrawn or non-operative: never apply

- MLB run-line and push caps; fixed variance floors.
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
- Anchoring cards on the numerical shadow models (P3, 2026-09-26(e): not better than the cards).
- The favourite-band shrink (C1, 2026-09-27: not better on held-out seasons).
