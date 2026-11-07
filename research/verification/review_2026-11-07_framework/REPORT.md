# Framework review, 7 November 2026

**Status: REVIEW AND PROPOSAL ONLY.** Owner request: "do a comprehensive review of the sports research framework and tell me what is good, what needs to change, what files can be archived and/or merged, and if there is anything else that needs to be done so the framework improves completely". Nothing here changes a rule, prompt, model, ID, grade or record. Each item takes effect only by owner decision through prompt 8 (or prompts 3, 4 and 6 for the settlement backlog).

Read at `main` `d6a6502db` (MDS v24.1 / CR-2026.11.07-R1), working tree clean. Measurements were taken on the working tree: file sizes, how many other active files link to each root file, last-change dates and folder sizes. The 22 October [framework revamp review](../review_2026-10-22_framework_revamp/REPORT.md) is the evidence base for the prediction findings; this review checks what happened after it.

## 1. Summary

The framework is honest and well defended, but it is not yet measuring what matters. The v24 redesign of 22 October was the right answer to the 22 October evidence. Since then it has barely run:
- the adjustment ledger has **0 rows**;
- **6 cards and 2 frozen NBA model rows have been unsettled for 16 days**;
- the 8-week / 50-paired-game decision clock has not really started.

Meanwhile the rulebook keeps growing. A basketball card's named reading set is about 536 KB, and the method went from v10 to v24 in 11 days. The most valuable next step is not another rule. It is **running and settling the v24 cycle every day for two months with the rules frozen**, while cutting the documents to what a card actually uses.

## 2. What is good (keep it)

1. **Integrity.** It is market-blind and refuses to invent data. Outcomes stay unknown instead of being guessed, and labels are honest (`NOT_PRIMARY`, `INFORMATION_INCOMPLETE`, `NOT_ISSUED`). The custody chain is append-only: frozen sources are hashed, settlements are revisions with parents, and closed log parts are never edited. The 7 November settlement could prove every byte of the owner drop was already retained.
2. **Honest self-measurement.** The 22 October review found the uncomfortable truths and wrote them down:
   - stated probabilities between 0.40 and 0.65 do not separate winners from losers (slope 0.15, 525 rows);
   - the cards lost to a simple league baseline where one existed;
   - fitted models price widths better than the cards.
   Few personal frameworks get this far.
3. **The v24 design is right.** Each card:
   - starts from a frozen reference model;
   - adds research only as logged, bounded adjustments that are scored separately;
   - gives a probability for every supplied contract, with abstaining allowed;
   - is scored with paired proper scores against the reference and the baseline.
   This is the only design that can show whether research adds accuracy.
4. **Code.** The `ml/` package passes 633 tests. It includes a hash-chained prospective ledger, a picks linter, seeded simulators for path-dependent contracts, and walk-forward studies for NBA and NHL.
5. **Domain knowledge.** The sport rule files, `SOURCES.md` and `RESEARCH_SOURCE_REGISTER.md` hold real, reusable knowledge: competition rules, reachable statistics routes and failure modes per site.
6. **Settlement conventions are starting to replace operator terms** (BK-OT-1, 7 November). This is the right direction under the owner's no-bookmaker rule; see §3.3.

## 3. What needs to change (in priority order)

### 3.1 Run the v24 cycle, and settle the backlog (highest value)
- **The backlog:**
  - Active mini `20261022F6K3OJNO`: 6 cards (`LOCAL-20261021OKCSASR01-G0001`, `LOCAL-20261022F6K3OJNO-G0001`…`G0005`), unsettled since 21–22 October.
  - Two frozen NBA league-day bundles (`research/cycle_attempts/LOCAL-LEAGUE-NBA-20261022-G0001/G0002`), and their prospective-ledger rows, never settled.
  - Legacy P-584.
  - The unimported 8-event package `SETTLEMENT_20261016A691119714D1_REV1_COMPLETE.zip` (U-610).
  - The held card MELILL01-G0004 (U-608, needs the owner's corrected file).
- **The ledger:** `research/adjustment_ledger/ADJUSTMENT_LEDGER.csv` has only its header. No v24 card has logged an adjustment yet, so the question "does research add accuracy?" still has no data.
- **The clock:** a model is judged after 8 weeks and 50 paired games. With almost no frozen-and-settled rows, it is not moving. NBA and NHL are in season, so `python -m ml league-day freeze` and `settle`, run daily for those two leagues, would collect the 50 paired games in about a week. That needs no cards at all.
- **Do:** run prompts 3 and 4 on the active mini and the two NBA bundles now. Then run daily league-day freezes and settles for NBA and NHL (this can be scheduled). Have every new card log its adjustments. Run prompt 6 ledger scoring monthly.

### 3.2 Freeze the rules for a measurement window
The method changed 14 times between 11 and 22 October. Each change resets comparability and adds custody overhead: there are 43 `archive/superseded_*` snapshots in two weeks. **Do:** declare a measurement window, for example to 15 January 2027, in which only bug fixes and owner-ordered conventions change the rules. Score v24.1 unchanged until the window closes.

### 3.3 Replace "operator terms" with settlement conventions in every sport
The open queue item U-601 (operator action, void and overtime terms for every contract) can never close: under the owner's rule, bookmaker terms are not researched. BK-OT-1 fixed this for basketball. **Do (owner decides each):** write one frozen convention per sport, so that every grade is `FROZEN_FRAMEWORK_CONVENTION`. Candidates:
- **soccer:** 90 minutes plus stoppage, no extra time or penalties;
- **ice hockey:** decide whether overtime and the shootout count for totals, handicaps and winner;
- **baseball:** extra innings included;
- **cricket:** the completed match as officially decided, including DLS, and a no-result void;
- **tennis:** retirement rule for completed-set and total-games lines;
- **rugby league and union, AFL and American football:** extra time or golden point in or out;
- **abandonment, postponement and void:** one rule for all sports.
Then retire U-601 and the word "operator" from settlement templates.

### 3.4 Cut the reading burden (REV-08 is still undone)
- **The size:** a basketball card names about 536 KB of required or linked documents. That includes the 202 KB SOURCES file, PROBABILITY_TOOLKIT 60 KB, RULES_BASKETBALL 51 KB, CARD_AND_LOG_TEMPLATES 47 KB and CURRENT_RULES 40 KB. CORE still needs the line "where a pre-v24 sentence contradicts this page, this page governs", which admits that contradictions remain.
- **The banners:** 49 active documents open with the same 7–9 banner paragraphs ("… Defined in X; summarised in CORE"), about 40 KB of repetition. **Do:** remove the banners and keep one protocol index in CORE.
- **Do:** follow the file plan in §4, so that a card reads CORE (about 20 KB), its sport file and the sport's rules page only.

### 3.5 Make the state files trustworthy and short
- **CURRENT_STATE.md is stale.** It still says the active mini's "next new key LOCAL-20261022F6K3OJNO-G0002", although G0002–G0005 exist. It is 42 KB, mostly release history.
- **GAME_LOG_STATUS_CURRENT.md** (224 KB) says "current section at the top", but imports append at the bottom.
- **Do:**
  - Generate CURRENT_STATE (one screen: versions, IDs, active log and mini, open queues with counts) from the files by a small `python -m ml state` command, checked by a test.
  - Move release history to CHANGELOG.
  - Split GAME_LOG_STATUS into a current queue file and a dated history file.

### 3.6 Settle one route for game requests
ENV-v2 (22 October) says every prompt runs in this repository and the external-chat route is retired. The same day, REQ-v2 added paste-ready requests for external chats, and GITHUB_REFERENCE_PROTOCOL and GOOGLE_DRIVE_EXCHANGE_PROTOCOL still describe external access. **Do:** the owner picks one route. If it is the repository, archive the external requests and the two access protocols. If it is both, write one short page saying which prompts may run outside and how their output comes in.

### 3.7 Retire or confirm the decision lab
`ml/decision/` holds `kelly.py`, `devig.py` and `bandit.py`: staking and de-vigging studies on prices, behind a firewall (owner instruction of 14 October). That predates the owner's standing rule that forecasts never refer to bookmakers, odds or prices, and it conflicts with that rule's spirit. **Do (owner decides):** move `ml/decision/`, its tests and the benchmark price cache to `archive/`, or reaffirm the firewall in writing.

### 3.8 Fix the repository mechanics
- **Line endings.** On Windows the default `core.autocrlf=true` rewrote LF files as CRLF, so every committed hash failed to match until the clone was reconfigured. **Do:** add `* text=auto eol=lf` to `.gitattributes`, keeping the existing `-text` exceptions, and document it in CONTRIBUTING.
- **Long paths.** 7 tracked paths exceed 150 characters, the longest 191. On Windows and OneDrive they need `core.longpaths`. **Do:** shorten them; they are all under `research/verification/*/originals/Mini logs (to be sent to actual log later)/…`.
- **Size.** `research/verified_history` is 797 MB on disk, from NBA archive CSVs of 30–42 MB each per season. The packed repository is 229 MB. **Do:** keep manifests, hashes and the derived training views in the repository. Move raw bulk to the external cache (`ML_CACHE`) or Git LFS.

### 3.9 Build models for the competitions actually requested (REV-07)
Fitted references exist for NBA and NHL (and MLB). Recent requests were CBA, PBA, B.League, B.ONE, LBA, NBL, ISL, J1, CSL, Algeria Ligue 1, KBO, Test and T20 cricket, Czech women's basketball and more. Those all fall to a league-only baseline or the hand TB-1/TB-2 references. **Do:** count requests per competition from the logs, then build verified history and a TB-2-MD or fitted reference for the top 8–10, basketball and soccer first.

## 4. Files: archive, merge, keep

Inbound = active files linking to it, so links must be updated (and recorded in HISTORICAL_LINK_INDEX) when it moves.

### 4.1 Archive (history, not instructions)
| File | Size | Inbound | Why |
|---|---:|---:|---|
| BASKETBALL.txt | 10 KB | 5 | Owner drop: a 17 October CBA game request already handled as a not-issued draft |
| PROMPT_1_SUPPLIED_FIRST_EXTENDED_2026-10-14.md | 168 KB | 8 | Superseded prompt; "reference only" |
| ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md | 78 KB | 17 | Dated proposal, partly implemented; its live parts are in the protocols |
| MODEL_PROBABILITY_ML_RECOMMENDATIONS_2026-10-12.md | 33 KB | 6 | Dated recommendations, superseded by the 22 October review |
| VALIDATION_EVIDENCE.md | 51 KB | 24 | Titled "current validation authority — 2026-10-01"; superseded by SCORING_AND_VALIDATION |
| RESULTS_REBUILD_PLAN.md | 5 KB | 7 | Proposal "not executed"; overtaken by `research/verified_history` |
| LEARNING_REGISTER.md + LEARNINGS_INDEX.md | 402 KB | 56 / 37 | Lesson archive, last changed 12–15 October; keep a one-page index of promoted lessons only |
| LEAGUE_PROFILES.md | 2 KB | 40 | Every profile RETIRED; fold its one live rule into COMPETITION_PARAMETERS |
| GITHUB_REFERENCE_PROTOCOL.md, GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md, research/prompts/external_requests/ | 8 KB + | 34 / 13 | Only if the owner retires the external route (§3.6) |
| GAME_PREDICTION_RANK_LOG.csv | 2.1 MB | 27 | Frozen 16 October; it is data, so move it to `research/data/` rather than the root |
| research/verification/* folders older than one month | 54 MB, 939 files | — | Dated work; move to `archive/verification_2026-10/` with an index |
| research/custody/implementation_2026-10-01/ | — | — | Historical copies of rules files |

The 40-odd `archive/superseded_*` snapshot folders can stay, but stop making a new full snapshot for each change: git history already keeps every version.

### 4.2 Merge
| Merge | Into | Notes |
|---|---|---|
| RULES_NHL.md (5 KB, still cites MDS v7.1) | RULES_ICE_HOCKEY.md | One file per sport |
| LEAGUE_RULES_SOCCER.md (45 KB) | RULES_SOCCER.md, as its competition-rules section | Same for cricket: LEAGUE_RULES_CRICKET → RULES_CRICKET |
| METHOD.md (4 KB, 159 inbound) | CORE.md | Leave METHOD.md as a three-line pointer, because so much links to it |
| CURRENT_RULES (40 KB) + SELECTION_RULES (18 KB) + CORE (16 KB) | One rulebook: CORE about 20 KB for cards, RULES_REFERENCE for the rest | REV-08's "core of about 30 KB" |
| RESEARCH_COMPLETION + RESEARCH_EXHAUSTIVENESS + RESEARCH_RETENTION + RESEARCH_CHECKLISTS + TIMING_RESEARCH | RESEARCH_PROTOCOL.md | All five govern "how much research, and when it counts" |
| MINI_LOG_IDENTITY + EXECUTION_ENVIRONMENT (+ the two access protocols if kept) | WORKFLOW.md | Who runs what, where outputs go, how IDs are assigned |
| PRIMARY_PREDICTION + FORECAST_CYCLE + ML_EXECUTION + REFERENCE_MODEL + LEARNING_PIPELINE | REFERENCE_MODEL_PROTOCOL (card side) + ML_PIPELINE (workshop side) | Five overlapping ML documents into two |
| BASE_RATES_REGISTER + COMPETITION_PARAMETERS + LEAGUE_PROFILES + EFFECT_TABLES | PARAMETERS.md (prose) + `research/competition_parameters/` (data) | One home for numbers a card may use |

Result: about 67 root files fall to about 30. A card reads CORE, its sport file and its RULES page.

### 4.3 Keep as they are
README, CHANGELOG, CONTRIBUTING, LICENSE, ACTIVE_FILE_INDEX (regenerate after the moves), CARD_AND_LOG_TEMPLATES (trim the legacy formats into an appendix), SCORING_AND_VALIDATION, VERIFICATION_PROTOCOL, ADJUSTMENT_LEDGER_PROTOCOL, BENCHMARK_PROTOCOL, SIMULATION_PROTOCOL, PROBABILITY_TOOLKIT, SOURCES (consider splitting per sport), RESEARCH_SOURCE_REGISTER, HISTORICAL_SOURCE_PROTOCOL, ROSTER_AVAILABILITY_PROTOCOL, HYPOTHESIS_REGISTER, HISTORICAL_LINK_INDEX, the RULES_<SPORT> files, `prediction logs/`, `ml/`, `research/` live data.

## 5. Everything else needed for the framework to improve

1. **Measure the right thing, first on the scoreboard.** The scoreboard still leads with rank win rates (for example Rank 1 342–201). Lead with the v24 headline instead: paired Brier of the card against its frozen reference, against the league baseline and against the line-implied 0.5 benchmark, with intervals, plus the adjustment ledger's per-adjustment scores. Win rates on self-chosen lines measure line choice, not forecasting.
2. **Use the abstain flag.** Rows at 0.40–0.65 have not been informative. Report them as information-only, and count a pick only where the reference and a priced adjustment move it out of that band. This is already in SEL-v4; the cards should apply it visibly.
3. **Requests earlier, research never rushed.** Request a game when its line is first known, not minutes before the start. FASTCARD-v1 lets a reference-based card exist before the start while the full research continues as an addendum, which fits the owner's rule never to rush research.
4. **A weekly routine.**
   - Daily: league-day freeze and settle for NBA and NHL.
   - After each game: prompt 3 and 4.
   - Monthly: prompt 6 (ledger scoring, review log, learning ingest of the new settlement revisions).
   - Prompt 8 only at the end of the measurement window.
   These can be scheduled so they do not depend on memory.
5. **One automated consistency check.** Extend `test_prompt_consistency` so that:
   - CURRENT_STATE's IDs and active-mini key match the files;
   - every root document is linked from ACTIVE_FILE_INDEX;
   - no active document repeats the banner text;
   - no live rule defers to "operator" terms.
6. **Owner decisions this review needs:**
   - the per-sport settlement conventions (§3.3);
   - the request route (§3.6);
   - the decision lab (§3.7);
   - the measurement-window end date (§3.2);
   - approval of the archive and merge plan (§4).
