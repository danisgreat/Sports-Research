# Prediction Mini Running Log — P-510 onward (started 2026-09-25)

| Field | Value |
|---|---|
| Created | 2026-09-25 about 01:00 +10:00 (Australia/Melbourne, AEST UTC+10; AEDT from 4 Oct 2026) |
| Status | **ACTIVE MINI LOG.** No events issued yet. |
| Next canonical ID | **P-510** |
| Temporary IDs awaiting canonical reconciliation | `TMP-20260923-NPB-CHU-DB-G25` (settled; DeNA 4–3 F/12) and `TMP-20260923-NBL-CNS-TAS` (settled). Both still await a canonical number (operator decision). No live temporary ID. |
| Governing method for the next issue | METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**. **Freeze with every card:** `CONTROL_MANIFEST_2026-09-25-3.md`, SHA-256 `619a3fda2829723d633efcd320a517f1eaaae3b91ef01719c7ae4aaa86b7dbc0`. It is the post-repository-review content receipt (2026-09-25 about 02:00 AEST; 82 files hashed in CRLF checkout form). Verify it with `python tools/verify_manifest.py`. It supersedes `CONTROL_MANIFEST_2026-09-25-2.md` (`8f65c60e…`) and `CONTROL_MANIFEST_2026-09-25.md` (`7b6efc56…`); no card was issued under either. Before issuing, re-hash the listed governance files: they must match, except the two living logs (Part 5 and the status register), which change with every card. |
| Operating mode | **SPORTS_ONLY / MARKET_BLIND.** No odds, prices, line movement, tipsters, betting previews, prediction markets or fantasy/DFS material as evidence, anchors or sanity checks. Supplied lines are quarantined until the distribution is frozen (METHOD §1.1). |
| Performance status | **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** No ROI, EV, calibrated-edge or validated-model claim. `NO VALUE DETERMINABLE` unless a governing value gate is explicitly satisfied. |
| Drive scope | Google Drive is the reference copy of the methodology and learnings; this session reads the repository mirror at `C:\Users\danie\Desktop\Sports Research`. **No Drive file is created, edited, moved or renamed from this workflow.** This log lives in the local `Mini logs (to be sent to actual log later)/` folder; the operator uploads it. |
| Predecessor | `archive/mini_logs/Mini Prediction Log - P-509 SETTLED - 2026-09-24/`. P-509 was settled in `PREDICTION_LOG_COMBINED_5.md` §"2026-09-24(g)" (PER 98–97 ADL). Nothing is carried over. |

## Standing learnings to apply to every new card (audit closure, 2026-09-25)

The full set is in the governing files. These are the ones most often missed: the M-items in `LEARNING_REGISTER.md` §"2026-09-25 audit closure" B.

1. **Identity match before any "same-event" label.** Check date, venue, home/away and starters/participants (`O-ID-DATE-STARTER-MATCH`).
2. **Freeze before the first ball, pitch or tip-off**, and stamp the freeze time. The actual start marker is the official feed's first event, e.g. the NBL `jumpBall`, which has run about six minutes after schedule.
3. **Six-field object (METHOD §4) on every card.** No rank without a derived probability from one joint distribution. An `UNVALIDATED_SUBJECTIVE` number must be reproducible from the printed distribution (METHOD §5, §12). When the joint states are explicit, print the joint masses as numbers (field 5).
4. **Lineups (M19, M25).**
   - An official lineup published before the freeze always wins. Print it with its fetch time: MLB statsapi `battingOrder`; NPB and KBO official orders; NBA, WNBA and NBL official starters; the NHL official goalie.
   - `PROJECTED_BEAT_VERIFIED` counts **only** with a printed `S-1 Rev 2 receipt:` line (outlet, reporter, timestamp, verbatim quote, two sources). Otherwise the state is `NOT_RETRIEVED` / `RETRIEVAL_MISS`, and G14.2 blocks a full-game total or margin at Rank #1.
   - Pre-season goalies stay `PROJECTED`.
5. **MLB totals (M30).** Print the statsapi gamefeed `weather` block (field-relative wind) retrieved at freeze.
6. **Covering pairs (M28).** Label two rows that jointly cover every outcome `COVERING_PAIR` in field 5b. Never cite their Hit@2 as skill, and never seek such a pair to guarantee a win.
7. **Cricket.**
   - Phase totals are a bat-first/chase mixture before the toss, or the realised branch after it, with the team and venue phase windows split by innings order (control 21; M24).
   - Name the incoming Nos. 3–4 and both new-ball bowlers (control 20).
   - Check the toss at toss + 5 minutes via ESPN `notes[]`.
8. **Tennis.**
   - Print the dated Elo benchmark (`TE-P5`, blocking; explain or rebuild if the gap exceeds 10 points).
   - Derive matchup holds from serve × return with numerators (`TE-S4`).
   - Print P(decisive straight sets) and P(three sets) beside any best-of-three total from 18.5 to 21.5.
9. **Coin flips say so.** A row whose normalised edge is under about 0.15 is a near-tie (`NEAR_TIED` / LOW; G23.1).
10. **Mechanisms carry both signs (G-L2).** Workload, fatigue, rest and "rests starters when ahead" branches widen the distribution before they move a centre.
11. **Withdrawn, do not apply:** doubleheader-G1 deflation; derby Under suppression; "dual run-line arbitrage"; the FIBA qualifier pace coefficient; the clay handicap cap. See `RULES_GENERAL.md` §"2026-09-24(f)"(a).
12. **At settlement.** Read every process fact from a named record, with endpoint and time (`C-PROCESS-RECORD-PROVENANCE`). Add the `C-LINEUP-DIFF` line. Copy summaries from Field 4. Run `python audit_card_controls.py <this log> --settlement --strict`.

**Added by the 2026-09-25(b) research pass** (`RULES_GENERAL.md` §"2026-09-25(b)"; all disclosure, measurement or retrieval; none moves a number by itself):

13. **Receipts, not memory (`C-RECEIPT-TOOL`).**
    - MLB freeze: `python receipts.py pregame mlb <gamePk>`. It prints probables, gamefeed weather, official batting orders and umpires, or `LINEUPS_NOT_YET_PUBLISHED` / `WEATHER_NOT_YET_PUBLISHED`. Paste it, and re-run within 60 minutes of first pitch.
    - ESPN leagues: `pregame espn <sport/league> <eventId>` gives the state and injuries.
    - Settlement: `settle mlb|nhl|espn …` with `--card-*` for the lineup diff. It is one lineage.
14. **Reference row and reference width beside the card's numbers (field BR; `C-WIDTH-BENCHMARK`).** Take them from `BASE_RATES_REGISTER.md` §7. Reference widths:
    - totals: NBA 19.4, WNBA 19.5, NBL 18.7, NHL 2.29, MLB 4.50, EPL 1.61, WTA 5.79;
    - margins: NBA 15.1, WNBA 13.3, NBL 15.2.

    A width below 0.85 × the reference needs a one-line reason. Leagues without a benchmark (LKL, EuroLeague, LMB …) print `REFERENCE_WIDTH_NOT_YET_DERIVED`.
15. **Windows and regimes.**
    - NBL rounds 1–3: the early-season reference is **−8.5** points.
    - WNBA openers: **+6.5**.
    - WNBA 2026 is **+10.7** over 2024–25, so exclude or adjust those seasons.
    - NHL preseason: mean 5.68 (2025) / 5.33 (2026 to date), and P(total ≤ 5) about 0.56.
16. **The previous game never outweighs the season rate** (`R-1` corollary). It is the worst predictor in 6 of 6 competitions measured. In basketball, use the opponent's defence to date.
17. **Tennis handicaps (`C-HCP-COHERENCE`).**
    - P(−k.5) ≤ P(win).
    - Print c_s and c_d beside the population values (WTA −5.5: 0.663 / 0.168).
    - Print P(deciding set) beside the reference (WTA 0.340).
18. **NHL puck line.** 73% of two-goal regulation wins contain an empty-net goal. A −1.5 row carries the empty-net branch as mass; a +1.5 row names it as its main kill path. Overtime and shoot-out totals are odd (a 2–2 tie lands Under 5.5; a 3–3 tie lands Over 6.5).
19. **At settlement, print z_total and z_margin = (actual − centre)/width (`C-WIDTH-Z`).**

**Added 2026-09-25(c)** (`RULES_GENERAL.md` §"2026-09-25(c)"):

20. **`BASELINE_P` beside every ranked row** (`C-BASELINE-SKILL`). This is the naive population probability for the same contract, from games completed before this event, knowing only which side is at home. Examples: MLB total 7.5 Over ≈ 0.573 (2026 to date); MLB +1.5 ≈ 0.638 for either side; tennis winner 0.5. If no population exists, print `BASELINE_P: NOT_YET_DERIVED`. At settlement, append the decisions to `SKILL_BASELINE_LEDGER.md`. **The seed check found no skill over this baseline yet** (card 0.2461 v baseline 0.2360, n = 29). Beating it is the job.
21. **Start with `CURRENT_RULES.md`**, and run `python tools/verify_manifest.py` before freezing. Work on a `session/<date>-<topic>` branch and merge through a pull request with green checks (`CONTRIBUTING.md`).

## 1. Incomplete / Unsettled Logs

None. No event has been issued in this log.

## 2. Settled Logs

None yet. Settled predecessors are in `PREDICTION_LOG_COMBINED_5.md`: P-482–P-509 and the temporary IDs.

## 3. Sources

Every card lists every material source in its own **Sources** table, with:
- source name and link;
- field owner / lineage;
- what it contributed;
- retrieval time (AEST);
- status: `OPENED`, `SNIPPET` or `ASSUMED`.

**Preferred order** (`SOURCES.md`, `DATA_SOURCE_REGISTER.md`):
1. The official league or competition feed.
2. The official team or player release.
3. A structured statistical API: MLB statsapi, NPB box, KBO scoreboard, the ESPN site API without a browser User-Agent, the NHL api-web via curl, WTA and ATP feeds, ITF draws pages via `r.jina.ai`, Cricbuzz/ESPN cricket.
4. Independent high-quality reporting.
5. Fallback.

**Weather:** the statsapi gamefeed for MLB; Open-Meteo or the venue hourly forecast in venue-local time.

**Prohibited:** sportsbook and odds pages, betting previews, tipsters, prediction markets, fantasy/DFS, social media (S-1), AI-generated recaps (e.g. Mynavi's AI series, archysport), and search-result summaries as facts.

## 4. Document Mapping

| Information or update | Where it eventually belongs |
|---|---|
| Frozen forecast card; later settlement and retrospective | `PREDICTION_LOG_COMBINED_5.md` (active canonical log) |
| Current event state / open handles | `GAME_LOG_STATUS_CURRENT.md` |
| Cross-sport process control with recurring evidence | `RULES_GENERAL.md`, `METHOD.md` or `CONTROLS.md` (with a `C-PROMOTION-RECEIPT`) |
| Sport-specific rule, kill path or checklist item | The relevant `RULES_<SPORT>.md` |
| New or changed source, access method or reliability note | `DATA_SOURCE_REGISTER.md` (full card) and `SOURCES.md` (summary) |
| Hypothesis or candidate lesson with a prospective test | `LEARNING_REGISTER.md` (`TESTING` row with its evidence and test) |
| Base rate derived for an identity input or a reference row | `BASE_RATES_REGISTER.md` (§7 holds the 2026-09-25 cross-sport references; the query goes in `research/`) |
| Mini-log import / ID-custody procedure | `EXTERNAL_LOGGING_WORKFLOW.md` |
| One-event observation | This log only; never promoted from one game |

## 5. Prediction integrity checklist (run before every card; record the result in the card)

1. **Verify identity.** Check the event, competition, participants, venue, official venue-local date/time, IANA timezone and the AEST/AEDT conversion (CR-4, three independent lineages).
2. **Check state:** UPCOMING, DELAYED, LIVE, POSTPONED, CANCELLED or COMPLETED. Anything other than UPCOMING blocks a pregame card; a live view is labelled LIVE-ISSUED.
3. **Parse the supplied markets exactly.** Flag any inconsistency rather than silently correcting it, and quarantine the lines.
4. **Retrieve personnel from official sources first:** starters and lineups, bench and reserves, injuries, suspensions, rest, coaching and late changes. Print the official lineup where it is published. Otherwise record `LINEUPS_NOT_YET_PUBLISHED @ time`, `RETRIEVAL_MISS`, or a receipted `PROJECTED_BEAT_VERIFIED`.
5. **Build the distribution.** Construct one joint distribution (the six-field object). Derive every row's probability, rank by derived probability (Pick #1 = highest), and print P(R1 ∧ R2), the complement decomposition, the covering-pair label and the top-O/U target.
6. **Refresh and freeze.** Do a final volatile refresh immediately before the start, stamp the freeze time, and append the complete card here **before** delivering it.
7. **Mark anything unconfirmed as unconfirmed.** Never fabricate.

## 6. Continuity and ID custody

- Allocate the next canonical ID only at freeze, after re-reading Part 5's snapshot and this log.
- If another session may be issuing at the same time, or any collision or uncertainty appears, use `TMP-YYYYMMDD-<SPORT>-<A>-<B>` and propose the canonical ID for reconciliation. Never overwrite or renumber an existing ID.
- A later refresh of the same event (same date, venue and participants) is appended under the same ID as an append-only view. If any of those differ, it is a new event.
- Record every ID claimed in any external chat transcript here the moment it is claimed.

## 7. Output after every new prediction query

1. The requested prediction and analysis.
2. The complete card appended to §1.
3. All material sources recorded in the card.
4. Document mappings and candidate learnings noted in the card.
5. The entire updated mini log.

No retrospective is performed unless explicitly requested.
