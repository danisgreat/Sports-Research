# Changelog

**Opened 2026-09-25(c).** This is the project's dated history. Until 2026-09-25(c) it lived in the body of `README.md`, which had grown into about twenty dated sections. That buried what the project is and how to use it. The complete former README body is preserved **verbatim** below, in its original order (SHA-256 of the whole former README: `003a7eaecb6b64e70a28811449a34e5f4a7572ef03dffca621675c7d200a9b71`). Its links are unchanged and still resolve, because this file sits in the same folder.

New entries go at the top, under **Entries from 2026-09-25(c)**. The governing rules live in [`CURRENT_RULES.md`](CURRENT_RULES.md) and the files it cites; this changelog is history, not instruction (`METHOD.md` §9).

## Entries from 2026-09-25(c)

### 2026-09-26(e) — predictability across sports

**Why.** The user asked for predictability across all sports to be improved properly, then to continue thoroughly and accurately. **Category:** MEASUREMENT plus validity repairs. No probability, rank, width, centre or model constant moved (`C-RULE-FREEZE`).

- **Preregistered first.** P1–P4 were committed in `cc447c9` before any run (`research/predictability_2026-09-26/PREREGISTRATION.md`).
- **P1, the MLB declared-starter term:** not demonstrated on results in 2025 or 2026. It helped 2026 totals only.
- **P2, coverage:**
  - NBL 2025-26: A1 beat the population and TB-1.
  - NBL 2024-25: not significant on results.
  - NRL 2026: not significant on results.
- **P3, cards against models on 98 of the cards' own contracts (54 cards):** card 0.2438, A1 0.2505, population 0.2680. Card − A1 = −0.007 [−0.025, +0.011], so anchoring the cards on the models is not supported.
- **P4, the registry:** `tools/model_anchor.py` (+ tests), status `REFERENCE`, applied as `C-MODEL-ANCHOR`.
- **P5, the predictability map** (exploratory; `BASE_RATES_REGISTER.md` §7.8; `C-PREDICTABILITY-MAP`): the share of STRONG (≥ 0.70) favourites runs from AFL 39% (90.6% won) and basketball 26–29% (80–84%) to MLB 0%.
- **`T-MLB-V2-2025` concluded, replicated:** A1 − A0 = −0.0023 [−0.0042, −0.0005] over 2,121 unseen 2025 games.
- **Validity repairs:**
  - TB-1 `resolution` withdrawn for NRL sides and NFL totals (their intervals cross 0). NBA totals were kept on 2023–26 evidence.
  - `tools/mlb_model.py`'s claim that historical starters cannot be reconstructed was corrected.
- **Opened:** `T-FAV70-BAND` (NFL/NRL favourites at 0.70–0.80 look over-confident; tested prospectively, not fitted).
- **C1 (2026-09-27), the user's bar for a model change: none meets it.** The test was preregistered in `1bc57d7`.
  - NFL 2021–24 favourites at 0.70–0.80 won 66.7% at 0.744 (replicated).
  - NRL 2025 reversed (82.8%).
  - An NFL-only shrink did not improve Brier (exploratory).
- **Docs updated:**
  - `RULES_GENERAL.md` §"2026-09-26(e)" and `CURRENT_RULES.md`;
  - every sport's §0 page, with the NRL and American-football anchors corrected;
  - `CONTROLS.md` and `BASE_RATES_REGISTER.md` §7.8;
  - `LEARNING_REGISTER.md` §"2026-09-26(e)" (L-20260926-27–33) and `LEARNINGS_INDEX.md`;
  - `NUMERICAL_MODEL_REGISTER.md`, `research/sport_shadow/README.md` and `research/sport_models_2026-09-26/README.md`;
  - `CONTROL_MANIFEST_2026-09-27.md`.

### 2026-09-26(d) — second validation pass; shadow lanes for tennis and cricket; the settlement record

**Why.** The user asked to continue the implementation across the framework, for every sport, accurately and carefully.

- **Validation, second pass** (`research/sport_models_2026-09-26/`, constants unchanged except cricket):
  - **NBA 2023–26 and WNBA 2022–26:** A1 beat A0 and TB-1 on results and totals.
  - **NHL 2023–26:** A1 beat A0 and TB-1 on results, and was worse on totals.
  - **IPL cricket:** v1 was worse than a coin flip. v2 (elo_k 4, lam_team 200, re-selected on 2016–19; disclosed) is only level.

  Sources: sportsdataverse (research-only pyarrow dependency) and an IPL dataset. The NHL shootout flag is missing in the source, so shootouts were read from the scoring file.
- **Lanes.** Tennis and cricket now freeze and settle from the ESPN scoreboards (`tools/sport_data.py`). Tennis retirements void the games rows. Cricket's first innings is priced 50/50 on the toss, and scored only when it was full-length.
- **Integrity.** Shadow commands are blind and print the row ID only (both tools). Settlements print `SHADOW: <row id>` / `NO_LANE` / `MISSED`; this is audit field `10s`, strict from `CONTROL_MANIFEST_2026-09-26.md`.
- **Docs.** `RULES_GENERAL.md` §"2026-09-26" (k), (l), `CONTROLS.md`, `CURRENT_RULES.md`, the hockey, basketball, tennis and cricket §0 pages, `NUMERICAL_PROGRAM.md`, `NUMERICAL_MODEL_REGISTER.md`, the lane READMEs, `LEARNING_REGISTER.md` §"2026-09-26(d)" (L-20260926-19–25; `T-CRICKET-V2-UNSEEN`), `LEARNINGS_INDEX.md` and README are updated.
- **Tests.** Offline end-to-end shadow → settle → score for team sports, tennis and cricket; ESPN tennis and cricket parsers; audit `10s`.
- **Independent review** (a separate agent, before any shadow row existed).
  - **Leakage:** no look-ahead leakage; scrambling every later result left all forecasts identical.
  - **Protocol:** only the four disclosed constants changed after ac6fdc5.
  - **Fixed in the lanes:**
    - a stale cached pre-game scoreboard could never settle;
    - one unfindable event stopped all settlement;
    - a cricket super-over tie scored as a home loss;
    - cricket innings with no overs shown counted as full-length;
    - partial tennis scores without retirement text counted as complete;
    - soccer extra time was scored against a 90-minute model;
    - a side result was counted once per frozen line (also in `mlb_model.py score`).
  - **Wording corrected:** AFL and NFL against TB-1 (the intervals cross 0), cricket v2 ("no clear difference"), the not-validated lists, and the thinness of the v2 selections.

### 2026-09-26(c) — a numerical model for every sport

**Why.** The user asked for the numerical model to cover every sport, not only MLB.

- **Models.** `tools/sport_models.py` (with `tools/sport_data.py` for ESPN, CSV, TML-Database and cricsheet results) gives every sport an A0 baseline and a reduced-feature A1:
  - soccer: Poisson ratings with linked halves;
  - ice hockey: regulation Poisson plus OT/SO;
  - basketball, American football, AFL, rugby league and rugby union: ridge ratings, key-number weights and residual widths;
  - NPB, KBO and CPBL: the MLB joint with the league's tie rate;
  - tennis: surface Elo plus an exact serve chain;
  - cricket: Elo plus a first-innings ridge model.

  None reads odds.
- **Shadow lane.** `C-SPORT-SHADOW` (`research/sport_shadow/`, per league). It works like the MLB lane and is never a card input. `evidence_status.py` prints it.
- **Validation** (`research/sport_models_2026-09-26/`). Priors were committed before the first run (ac6fdc5). The comparisons are rolling origin on public results.
  - **Results and margins:** A1 beat A0 in soccer (five leagues), the NFL, AFL and NBA, and beat TB-1 on results in the EPL, AFL and NBA.
  - **Totals:** A1 rarely helped.
  - **MLB and tennis:** each failed at v1 and was re-selected on an earlier TUNE window. MLB's team prior went from 20 to 120, now also in `tools/mlb_model.py`; tennis got a gap effect of 0.09. Both are disclosed as not independent.
  - **Dixon–Coles:** no gain.
  - **Not validated:** NHL, WNBA, NBL, NRL, rugby union, cricket, NPB, KBO and CPBL.
- **Docs.**
  - Every sport's §0 page now says what its model is and what the validation showed.
  - `RULES_GENERAL.md` §"2026-09-26" (k), `CONTROLS.md`, `CURRENT_RULES.md`, `NUMERICAL_PROGRAM.md`, `NUMERICAL_MODEL_REGISTER.md` §"2026-09-26(c)", `MODEL_IMPLEMENTATION_RECIPES.md` §4, `LEARNING_REGISTER.md` §"2026-09-26(c)" (L-20260926-12–18; `T-MLB-V2-2025`) and `LEARNINGS_INDEX.md` are updated.
- **Receipt.** `CONTROL_MANIFEST_2026-09-26.md` was regenerated in place before merge; no card was issued under its earlier version.

### 2026-09-26(b) — review implementation: evidence before rules

**Why.** The 2026-09-26 repository review rated the project 6.5/10. It found careful honesty and tooling, but no demonstrated skill over a simple baseline, six control revisions in one day with no card issued under them, a self-selected event sample, no market benchmark, an MLB pilot that existed only in Markdown, and a reading gate of about 65,000 words per card. The user asked for every recommendation to be implemented. Record: `RULES_GENERAL.md` §"2026-09-26"; `LEARNING_REGISTER.md` §"2026-09-26". **No forecasting coefficient, cap or ranking override changed.**

- **Rules you read.** Every `RULES_<SPORT>.md` opens with a §0 live rules page (560–1,650 words against 6,800–18,700 for the full files). `RULES_GENERAL.md` §1 is now a two-tier reading gate (`C-READING-GATE`). Nothing was deleted.
- **Rule freeze.** `C-RULE-FREEZE` holds new predictive rules until `C-BASELINE-SKILL` and `T-RM1-PROSPECTIVE` report. `tools/make_manifest.py` requires `--category`, allows one manifest per issuing day except validity repairs, and refuses a `MODEL_CHANGE` during the freeze without the user's instruction.
- **New measurement lanes.** `C-EVENT-UNIVERSE` (`tools/slate_universe.py`; audit field `UV`); `C-MARKET-BENCHMARK` (`MARKET_BENCHMARK_LEDGER.md`, `tools/market_benchmark.py`; post-settlement closing probabilities only; forecasting stays market-blind); `C-MLB-SHADOW` (`tools/mlb_model.py`, the numerical programme's MLB A0/A1 pilot as tested code; declared priors, not fit; never a card input); `tools/evidence_status.py` (every gate in one table; also run in CI).
- **Fixes.** `tools/skill_baseline.py` had pooled seed and prospective rows; it now reports them separately. README calibration figures updated to the rebuilt dataset (0.2268 / slope 1.01 / +6.6%). RM-1 is described as promising and unproven, with a stricter reversion rule for its cushion term. Soccer's record is "strongest resolution", not proof.
- **Learning register.** `LEARNINGS_INDEX.md` indexes every lesson, test and recurring mistake with its status. M33 (rule churn) and M34 (self-selected sample) added. 80 untested historical candidates and early tests are `CLOSED_UNTESTED`; `C-RANK2-GAP` is answered; `C-WEIGHT-PROPAGATION`, `C-MARGIN-TAIL-MASS` and `C-OU-GEOMETRY` are closed or superseded.
- **Repository.** `drive_settlement_2026-09-21/`, the Drive-sync manifests and `scratch/` moved into `archive/`. 319 byte-identical retired-runtime copies were removed (`archive/DEDUP_INDEX_2026-09-26.md`); tracked files went from 952 to 648. `tools/repo_hygiene.py` fails on live duplicates.
- **Tests.** Tool tests went from 51 to 90; root tests from 77 to 78.
- **Receipt.** `CONTROL_MANIFEST_2026-09-26.md`.

### 2026-09-26(a) — canonical IDs for the two settled temporary IDs; merge to main

- **Assignments.** On the operator's instruction:
  - **P-516** = `TMP-20260923-NPB-CHU-DB-G25` (NPB game 25, frozen 23 Sep 18:59:17 AEST);
  - **P-517** = `TMP-20260923-NBL-CNS-TAS` (NBL Cairns v Tasmania, untimestamped).
- **Order rule.** The verifiably timestamped card takes the lower number.
- **Records.** The issued records are unchanged and keep their temporary headings as retired aliases. The record is Part 5 §"2026-09-26(a)".
- **Next ID: P-518.**
- **Extractor.** It maps the aliases to their canonical IDs. The dataset and RM-1 are unchanged: those rows carry no stated p.
- **Receipt.** `CONTROL_MANIFEST_2026-09-25-6.md`.

### 2026-09-25(e) — Rank 1 and Rank 2: the ranking model, the team baseline, oval references, settlement integrity

- **Ask.** A sport-by-sport review of sources and reasoning, to make Rank 1 and Rank 2 far more likely to win than lose, and a new probability model if one could be built.
- **Data fixes.**
  - The settled-row extractor was reading narrative columns: 17 rows had been graded the wrong way round and 55 dropped. P-514 was classed as NPB.
  - The dataset is rebuilt: 1,264 rows; 641 with p.
- **RM-1** (`tools/rank_model.py`; user-authorised `L-087` exception).
  - The model: logit(q) = −0.187 + 1.543·logit(p) − 1.127·[a +k.5 cushion outside baseball, hockey and soccer].
  - It beat the stated p on log loss in grouped CV and in four forward splits.
  - Ranking by q raised held-out top-two wins by +0.068 per card [+0.007, +0.128] and never lowered Rank 1 or Rank 2 in any forward split.
  - A per-sport/per-class challenger failed.
  - Controls: `C-RANK-MODEL`, `C-TOP2-QUALITY` (`SLATE_ADVISORY`).
- **TB-1** (`tools/team_baseline.py`).
  - A leak-free team-strength baseline, validated on 12 league-seasons plus 1,704 newly pulled NFL, AFL and NRL games.
  - It has resolution for sides in NBA, WNBA, NBL, NFL, AFL, NRL and EPL (5–19% Brier) and for NBA, WNBA and NFL totals; none in MLB or the NHL.
  - Control: `C-TEAM-BASELINE`.
- **References.**
  - The first NFL, AFL and NRL population rows, and the NFL key numbers.
  - Underdog-cushion cover rates by league (`BASE_RATES_REGISTER.md` §7.7). A small cushion on the weaker team covers 32–54%: the mechanism of M32.
  - `C-PLUS-CUSHION` amended.
- **Settlement integrity.**
  - The P-510–P-515 settlement had been script-typed. P-510, P-511 and P-514 lineup diffs were false; P-515's score was 36–20, not 36–14. Grades are unchanged.
  - New controls: `C-SETTLEMENT-FROM-FEED` and audit field `10n`.
  - P-514 is a `LINEUP_CLAIM_FALSE` process defect.
  - P-510–P-515 are imported into Part 5 §"2026-09-25(f)"; that mini log is archived; the next ID is P-516.
- **Sources.** Verified and admitted: ESPN NFL, AFL and NRL scoreboards; ESPN team schedules; the KBO English scoreboard; the NPB official score page. The NRL team schedule returns HTTP 500.
- **Audit.** New fields `RM`, `TB` and `10n`.
- **Sport files.** Each has a §"2026-09-25(e)".
- **Receipt.** `CONTROL_MANIFEST_2026-09-25-5.md`.

### 2026-09-25(d) — review of every settled log: calibration findings, construction tools

- **Dataset.** `research/settled_rows_2026-09-25/` extracts every graded row from Parts 1–5: 1,185 rows from 307 cards, 600 with probabilities from 149 cards. It reproduces the logged cohort figures.
- **Findings.**
  - Calibration overall is good: Brier 0.2249, slope 1.06, reliability 0.002. Skill is modest (resolution 0.019).
  - The skill sits at p ≥ 0.65 (80.3% won); 0.50–0.65 is coin-flip-grade (53.6%).
  - Non-baseball underdog cushions are over-confident: 17/40 at 0.642.
  - Soccer shows clear skill; MLB and basketball near-zero resolution; tennis, NFL/NCAA and AFL none.
  - Ranks #2–#4 are indistinguishable. Top-two joint failure equals independence.
- **Controls.** `C-PLUS-CUSHION` (CANDIDATE, audit field `PC`, M32), `C-DEPARTURE-LEDGER` (audit field `DL`), `C-TRACK-RECORD`, `C-LOW-RESOLUTION-BAND`, and the `SCORING_AND_VALIDATION.md` §14 review standard.
- **Tools.** `tools/card_math.py`: normal, negative-binomial, Poisson and Skellam queries, `no_zero` margins, push mass, exact joints, and the departure ledger. It reproduces the issued P-509 and P-500 probabilities. `tools/calibration_report.py`: reliability, Murphy decomposition, slope, card-cluster slices. A canonical settlement table format.
- **Tests.** `T-PLUS-CUSHION`, `T-TOTAL-DIRECTION-LEAGUE`, `C-LOW-RESOLUTION-BAND`; interim rows for `C-PROB-EXTREMITY` and `C-PHASE-VS-FULL-TOTAL`.
- **Receipt.** `CONTROL_MANIFEST_2026-09-25-4.md`.

### 2026-09-25(c) — repository hygiene, CI, current-rules summary, baseline skill check

- **Hygiene.** Untracked 16,142 files: two `node_modules` trees in `.codex_spreadsheet_tmp/`, a retired runtime's `node_modules`, `__pycache__`/`.pyc` and `.claude/settings.local.json`. They stay on disk. Added `.gitignore` and `.gitattributes` (CRLF checkout everywhere, so manifest hashes reproduce on any platform) and `LICENSE` (all rights reserved; third-party note). Removed three betting domains from the local permission allowlist. Fixed two literal-`\n` rendering bugs (README custody table; RULES_GENERAL header).
- **CI.** `.github/workflows/checks.yml` runs every test, `tools/repo_hygiene.py`, `tools/verify_manifest.py` and the strict card audit of the active mini logs on every push and pull request.
- **Tools.** `tools/verify_manifest.py`, `tools/make_manifest.py`, `tools/repo_hygiene.py`, `tools/skill_baseline.py` (with tests). `audit_card_controls.py` gains `--allow-empty` and field `BP`.
- **Docs.** `CURRENT_RULES.md` is the live operating summary and step 0 of the reading gate. `README.md` is rewritten as an overview and quickstart. `CONTRIBUTING.md` covers the branch/PR workflow, commit conventions and local checks.
- **Skill check.** `SKILL_BASELINE_LEDGER.md` and `C-BASELINE-SKILL`. The seed comparison of 29 decisions from 9 cards shows no demonstrated skill over a naive population baseline: card Brier 0.2461 v baseline 0.2360, interval [−0.059, +0.089].
- **Receipt.** `CONTROL_MANIFEST_2026-09-25-3.md`.

## Former README body (verbatim, as of 2026-09-25(b))

Current method: **MDS-2026.09.19-v4.3**, control revision **CR-2026.09.21-3**. All existing game logs remain **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. This project records research forecasts, exact settlement evidence and testable model improvements in Markdown; no numerical model is fitted or validated yet.




<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
## Universal event-verification gate — CR-2026.09.19-4 component (preserved under CR-2026.09.21-3)




Every new sports event now requires **at least three distinct reliable upstream source lineages**. Mirrors, syndicated copies, reposts, search-result snippets and generated summaries do not create independent verification.




Before issue or refresh, verify the official venue-local date/time and IANA timezone, then convert that exact instant to `Australia/Melbourne`, recording the correct **AEST/AEDT** label and any calendar-date rollover. User-supplied start times are estimates until independently verified.




Settlement requires **three independent reliable lineages** agreeing on the exact event/date, explicit terminal state and final result. A score without a terminal marker is insufficient; any credible current live/in-progress source or material source conflict blocks settlement. P-469 is the reference false-final incident that prompted this gate.




The executable preflight now enforces source-count/lineage diversity, event time-zone conversion and normal pregame state before a new card can pass.




## Cricket source-control implementation — 2026-09-21




**CR-2026.09.21-1** preserves the current forecasting method and CR-4 cross-sport gates while repairing cricket source retrieval.




- Separate `TOSS STATUS`, `STRIP STATUS` and `MATCH CONDITIONS STATUS`.
- Use field-owner match centres first for the toss; add verified board/competition/rightsholder video and sanctioned NV Play/board-branded Match Centre to the late-information ladder.
- Only named current-match P1–P5 sources in `RULES_CRICKET.md` §2 can establish today's strip. Previous same-venue matches, venue averages and ICC post-match ratings are context.
- A transcript and its underlying broadcast are one lineage. Identical/near-identical unusual pitch metadata across front ends is one suspected upstream feed until provenance proves independence.
- `AUTOMATED_PITCH_METADATA` cannot masquerade as an observed strip.
- `INSUFFICIENT_VENUE_HISTORY` is valid; no fabricated venue sample.
- Official dynamic pages are field-specifically stale when fresher reliable evidence proves the displayed state is outdated.
- Toss-window and final pre-issue refreshes are required.




See [Cricket rules](RULES_CRICKET.md) §2, [source register](DATA_SOURCE_REGISTER.md) §6A, [sources](SOURCES.md), [research guide](UPCOMING_GAME_RESEARCH_GUIDE.md), [implementation ledger](archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-21.md), and [control manifest](CONTROL_MANIFEST_2026-09-21.md). This is an integrity/retrieval change; no predictive-lift claim is made.








## Current canonical rollover — 21 September 2026




Part 4 is closed at P-481. Part 5 (`PREDICTION_LOG_COMBINED_5.md`) is the active queue/next-ID authority; the rollover next ID is P-482. `GAME_LOG_STATUS_CURRENT.md` is the current state register. All current log material remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.




## Historical state snapshot — 17 September 2026(c) *(superseded for active queue state)*




- Active canonical log remains [Part 4](PREDICTION_LOG_COMBINED_4.md). **Do not use this README to infer the next ID**; read the top Part-4 snapshot or the active mini-log reconciliation. P-372 remains reserved/unused.
- **No live event; 23 primary result/derivative handles plus 5 separate documentary/period follow-ups.** The top Part-4 snapshot is the sole queue/next-ID authority. The [status register](GAME_LOG_STATUS_CURRENT.md) provides the per-ID details.
- P-255-C05/P-256-C05 are **UNRESOLVED_PERIOD**. Whole-match corner counts do not prove their regulation Overs; existing audit handles -03/-04 are reopened. Other recorded rows remain unchanged.
- Corrected legacy scorecard: **477 rows, 114 cards, 273 W/204 L, mean 0.2265475891**. PRIMARY_SCORED subset: **136 rows, 33 cards, mean 0.246825**. P-344's mean is **0.283425**. These are descriptive legacy diagnostics, not improved-model results or calibration evidence.
- C-OU-GEOMETRY has **zero verified prospective cards** under the required timestamp/control-version join. Historical imports are development evidence.




## Audit and implementation - 2026-09-19




**Tested the bounce-back hypothesis empirically and it does not hold.** MLB 2026, 4,594 team-games and 108 starters: after a 0-run game teams score **0.102 runs BELOW** their own mean next time (95% CI [−0.456, +0.251]); top-10 offences behave no differently from bottom-10 (−0.126 vs −0.093); a starter's next-start ER after being hit for 6+ lands **−0.017** from his own average and his strikeouts do **not** spike (−0.070). Out-of-sample, shorter recency windows predict monotonically **worse** — last-1 RMSE 2.7677 against a flat league constant's 1.9844. New document [`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md) and control **`R-1`**: recent results revise an estimated *rate* through a named mechanism, never forecast a *deviation*.




- **New user directive implemented:** a loss **or push** on the card's highest-ranked over/under now triggers the same enhanced failure review as a Rank #1 loss (`METHOD.md` §7, logged as `TOP_OU_REVIEW`).
- **Social media tested directly, and it fails.** X: HTTP 200 login wall, 1,644 chars of visible text, zero post content; syndication lane 0 bytes; jina proxy 403 abuse-blocked. Reddit: interstitial, no JSON. Bluesky: API works but **6 of 6 sports handles failed identity** — `jeffpassan.bsky.social` is a squatter who posts *"I continue to not be Jeff Passan"*, `fabrizioromano.bsky.social` is a different Fabrizio posting in Turkish. New control **`S-1`**.
- **Press conferences (`S-2`):** admissible for availability, workload and role intent; never a signed adjustment to pace, efficiency or scoring rate.
- **Three structured lanes added instead:** MLB `hydrate=lineups` (distinguishes `LINEUPS_NOT_YET_PUBLISHED` from a `RETRIEVAL_MISS` — most prior flags were the former), `boxscore` `battingOrder`/`bench`/`bullpen`, and **debutant detection** via MLB `mlbDebutDate` and ESPN cricket `debuts[]`. A 6-day rookie batted 6th in `P-455` unflagged.
- **Cricket pitch-ladder drift repaired prospectively by CR-2026.09.21-1:** toss facts and exact-strip evidence now use separate ladders; preceding same-venue matches remain different-strip context unless reuse is confirmed; official video/NV Play are explicit late-information lanes; duplicate structured pitch feeds are one lineage; `INSUFFICIENT_VENUE_HISTORY` is legitimate.
- **One recorded success reclassified:** `P-453`'s Rank #1 rested on three-start form — the third-worst predictor measured. Directionally lucky, not validation.




[Recency & rebound](RECENCY_AND_REBOUND.md) · [Controls](CONTROLS.md) · [Sources](SOURCES.md) · [Forecast preflight manifest](FORECAST_PREFLIGHT_MANIFEST.md) · [Control manifest](CONTROL_MANIFEST_2026-09-19.md).




## Audit implementation




[Implementation ledger](archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-17.md) · [Original model review](archive/audit_documents_implemented_2026-09-25/MODEL_REVIEW_2026-09-17.md) · Original evidence (`audit_2026-09-17_models/REVIEW_EVIDENCE.md`, not present in this repository) · Validation and control hashes (`audit_2026-09-17_implementation/VALIDATION.md`, not present in this repository).




The revision fixes integer push scoring, removes unsupported MLB run-line/push caps and fixed variance floors, corrects extra-inning completion logic, replaces overlapping-window pseudo-tests, permits declared hierarchical uncertainty, and prevents numerical row caps from contradicting a printed distribution. It preserves frozen issued predictions and appends settlement/score corrections. The old README's dated history is preserved in the before snapshot (`audit_2026-09-17_implementation/before/README_with_margin_band_addition.md`, not present in this repository); it is not current policy.




## Read first




| Document | Purpose |
|---|---|
| [METHOD](METHOD.md) | Single workflow, six-field forecast object, current authority and honesty rules |
| [Scoring and validation](SCORING_AND_VALIDATION.md) | Exact W/P/L/action conditioning, decision/event denominators, baseline comparison and prospective admission |
| [Controls](CONTROLS.md) | Compact current gate index and candidate dispositions |
| [General rules](RULES_GENERAL.md) | Detailed gate definitions and historical origins; METHOD replaces repeated presentation lists |
| Relevant RULES sport file and competition file | Sport-native exposures, state transitions, endpoints and source requirements |
| [Sources](SOURCES.md) / [full source register](DATA_SOURCE_REGISTER.md) | Field-owner routes, availability and numerical admission requirements |
| [Learning register](LEARNING_REGISTER.md) | Historical observations, current dispositions and prospective manifests |




## Numerical model work




| Document | Purpose / real state |
|---|---|
| [Numerical program](NUMERICAL_PROGRAM.md) | MLB A0/A1 first, soccer phase/full-match second; one stage/publication sequence |
| [Implementation recipes](MODEL_IMPLEMENTATION_RECIPES.md) | Executable empirical/count/scoring/phase/extra-state primitives and sport-specific estimation specifications inside Markdown |
| [H0 dataset card](H0_DATASET_CARD.md) | Restored root dependency; schema and source/time-join gates; NOT BUILT / NOT QUALITY-APPROVED |
| [Numerical model register](NUMERICAL_MODEL_REGISTER.md) | Existing models plus explicit tennis/union scopes; all NOT FIT; M0/M1 retired; advanced models dormant |
| [Training specification](NUMERICAL_TRAINING_SPEC.md), [model/data specification](MODEL_AND_DATA_SPEC.md), [algorithm portfolio](ALGORITHM_PORTFOLIO_AND_EVALUATION.md) | Detailed design reference under the current method, scoring specification and numerical program |
| [Base-rates register](BASE_RATES_REGISTER.md) | Historical reference estimates with populations and provenance; never universal matchup limits |




The user has authorized the audit implementation and asked for improvements within Markdown as far as possible. No new permission gate is imposed on this work. Real data admission, fitting, held-out comparison and future prospective shadow cannot be claimed as completed by writing their specifications. No external data was pulled or fitted for this implementation. The supplied calculation tests are synthetic correctness checks, not measured prediction gains.




## Canonical custody




| Part | Coverage | Custody |
|---|---|---|
| [Part 1](PREDICTION_LOG_COMBINED.md) | P-001–P-271 | Closed; settlement corrections only, including reopened P-255/P-256 period questions |
| [Part 2](PREDICTION_LOG_COMBINED_2.md) | P-272–P-332 | Closed; nine inherited primary follow-up handles |
| [Part 3](PREDICTION_LOG_COMBINED_3.md) | P-333–P-423; P-372 reserved | Closed; 13 primary follow-up handles |
| [Part 4](PREDICTION_LOG_COMBINED_4.md) | P-424–P-481 | Closed at P-481; historical custody and unresolved follow-up handles remain tracked in the status register |
| [Part 5](PREDICTION_LOG_COMBINED_5.md) | P-482 onward | **ACTIVE queue / next-ID authority** |




The [current status register](GAME_LOG_STATUS_CURRENT.md) supersedes dated status indexes for current questions. Older component logs, archived mini variants and dated audits remain evidence; they do not create extra forecasts or new instructions. Preserve canonical IDs and temporary aliases. Follow [external-log workflow](EXTERNAL_LOGGING_WORKFLOW.md) for variant discovery, reconciliation and archival.




## Complete Markdown recording




Record every substantive change, source status, lesson, forecast, settlement correction and validation result in Markdown. Preserve issued records and immutable archival copies. Do not invent missing probabilities, lineups, timestamps or model outputs. Odds and market analysis never enter the SPORTS_ONLY / MARKET_BLIND forecast. Missing validated probabilities or required prices/terms means **NO VALUE DETERMINABLE**.




<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## Deep-research implementation — 19 September 2026




This revision makes the project **strictly market-independent at prediction time** and converts the audit findings into blocking controls.




- **Hard source firewall:** sportsbook/bookmaker material, odds aggregators, betting previews/picks/tipsters, prediction-market sentiment, fantasy/DFS projections/rankings/ownership/start-sit advice, and secondary material derived from those sources are **PROHIBITED as predictive evidence**. RotoWire, RotoGrinders and FPTrack are explicitly prohibited. They may only be used as discovery pointers to an upstream valid source; if the upstream fact cannot be recovered, the fact is `UNAVAILABLE`.
- **Threshold quarantine:** a user-supplied total/spread/alternate line is contract metadata only. It is kept out of priors, features, model inputs, scenario weights, calibration and narrative direction until the independent sports-outcome distribution has been frozen. Only then is the line queried.
- **Point-in-time provenance:** every material predictive fact records source class, field owner, upstream lineage, publication/first-known time, retrieval time, cutoff compatibility and freshness. Mirrors that share one upstream feed count as one lineage.
- **Fail closed:** contaminated source, post-cutoff fact, stale critical state, missing lineage, line leakage, postgame leakage or method/control-version mismatch blocks a normal forecast rather than merely lowering confidence.
- **Distribution-first evaluation:** future numerical builds are evaluated with distribution scores (CRPS/RPS/log score where applicable), W/P/L Brier/log loss, RMSE/MAE, interval coverage/width and calibration diagnostics, with chronological event-grouped validation. Hit rate and Rank@k remain secondary diagnostics.
- **No performance claim from documentation changes:** these controls are expected to reduce leakage and false confidence, but no accuracy improvement is claimed until a frozen out-of-sample/prospective comparison demonstrates it.




Executable gate: [`prediction_preflight.py`](prediction_preflight.py). Full rationale and implementation record: [`archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-19.md`](archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-19.md).




## Final implementation synchronization — CR-2026.09.19-3




CR-3 is a **control/read-back synchronization revision**, not a new forecasting method. It removes stale active references to v4.1/v0.4 and obsolete hard-coded next-ID state, aligns the preflight schema/executable with the current authority, and records a fresh control-file receipt. Forecasting semantics remain MDS-2026.09.19-v4.2.




This synchronization does **not** establish predictive skill. H0 remains not built/quality-approved and no numerical model has been fitted, calibrated, held-out validated or prospectively promoted.




<!-- ALL-SPORTS-AUDIT-RECONCILIATION-2026-09-21-CR2 -->
## All-sports historical-audit reconciliation — CR-2026.09.21-2




[`archive/audit_documents_implemented_2026-09-25/AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md`](archive/audit_documents_implemented_2026-09-25/AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md) is the current supersession/duplication ledger for historical audit findings across baseball, cricket, soccer, basketball, AFL/AFLW, rugby league, rugby union/sevens, American football, ice hockey and tennis. It prevents an older finding from being reintroduced after later evidence rejected or narrowed it, and prevents an already-implemented finding from being double-counted.




This reconciliation does not claim improved prediction accuracy and does not complete empirical tasks by documentation. H0 remains not quality-approved; no numerical champion is promoted; non-MLB rebound/recency magnitudes remain un-derived; and historical settlement/documentary gaps remain separate operational work.








## All-sports live-rule cleanup — CR-2026.09.21-3




CR-3 removes residual active wording that conflicted with the CR-2 supersession ledger, synchronizes the active log to Part 5 / P-482, and aligns the preflight control revision. Current analysis is distribution-first; rejected historical shortcut rules remain provenance only. This is a governance/consistency correction, not a predictive-lift claim.


<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-23 -->
## Consolidated mini-log import — 23 September 2026

- Four mini-log files were consolidated, settled and imported to Part 5 §"2026-09-23(c)":
  - **P-489**: the 22 Sep game 24, DeNA 7–3. Rank #1 Under 6.5 lost; `TOP_OU_REVIEW`.
  - **P-491**: Orix 1–0; both top rows won.
  - Two temporary-ID records: the NBL card and a previously unregistered WNBA card, which both claim **P-487**. P-487 is held.
- The P-489 "R1" was a **different game** (23 Sep game 25) and is now `TMP-20260923-NPB-CHU-DB-G25`.
- Live records (TMP-G25, P-493, P-494) were carried unsettled to the new active mini log, `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-495 onward - 2026-09-23/`.
- The consolidated log is archived at `archive/mini_logs/Mini Prediction Log - P-487 to P-494 CONSOLIDATED - 2026-09-23/`.
- Content receipt: [CONTROL_MANIFEST_2026-09-23.md](CONTROL_MANIFEST_2026-09-23.md). Method and control revision are unchanged (MDS-2026.09.19-v4.3 / CR-2026.09.21-3).
- Everything remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.


<!-- AUDIT-2026-09-24F -->
## Verification audit of the P-495–P-508 import — 24 September 2026(f)

**Scope.**
- A peer session settled TMP-G25 and P-493–P-508 at 22:47 AEST (`cb95acd`).
- This pass re-verified every final against field-owner or structured feeds and checked every causal claim against the real process record. Full record: Part 5 §"2026-09-24(f)".
- **P-509 (NBL, Perth v Adelaide) was live throughout and is not settled**, per the operator's instruction. It stays in the active mini log `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-509 onward - 2026-09-24/`.

**Finals and grades.** All 17 finals are right. **One grade pair was wrong**: P-496 Vasa +0.5 is now a WIN and Marek −0.5 a LOSS, because the ITF draw sheet gives 15–15 games.

**The peer's process record was largely invented.** Linescores, decisions, goal types, goalies, quarter lines, coaches and game IDs were written rather than read. For example, TMP-G25 went 12 innings, not 9, and P-503 had no empty-net goal. The six single-game rules built on those narratives are **withdrawn or demoted**:
- doubleheader-G1 deflation: 2026 G1 P(total ≤ 7) is 0.435 (n=23) against 0.427 for other games;
- derby Under suppression: P-508's margin came from 4/41 three-point shooting;
- "dual run-line arbitrage": a mechanical cover, since both opposite +1.5 rows win in any one-run game (27.6%);
- FIBA qualifier pace;
- the clay handicap cap;
- NHL pre-season asymmetry.

**The biggest real defect is at issue time.** In 5 of the 7 cards that could be checked, the printed "reported/confirmed" lineups were wrong. P-501's Rank-1 Over was built on a Baltimore lineup of which only 2 of the 9 named players started. Two losing MLB Overs also printed the wind as blowing out when the official record says it was blowing in.

**Controls added.** All are integrity, measurement or retrieval controls; none is a forecasting coefficient: `C-PROCESS-RECORD-PROVENANCE`, `C-LINEUP-DIFF` with S-1 Rev 2 receipt enforcement, `G-L22(c) COVERING_PAIR`, `C-SUMMARY-FROM-CARD`, `C-PROMOTION-RECEIPT`, and MLB gamefeed weather at freeze.

**Where to look.** The descriptive batch record, the verified source lanes and the base rates are in Part 5 §(f) part M, `DATA_SOURCE_REGISTER.md` §"2026-09-24(f)" and `BASE_RATES_REGISTER.md` §5. Everything remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.


<!-- AUDIT-CLOSURE-2026-09-25 -->
## Audit closure and archive — 25 September 2026

**Every audit's implementable recommendations are now in the governing files, and the audit documents are archived.** The 15 audit documents (2026-09-05 to 2026-09-23) moved to [`archive/audit_documents_implemented_2026-09-25/`](archive/audit_documents_implemented_2026-09-25/). Their index and item-by-item receipt is [`AUDIT_CLOSURE_LEDGER_2026-09-25.md`](archive/audit_documents_implemented_2026-09-25/AUDIT_CLOSURE_LEDGER_2026-09-25.md).

**What was still missing** came mainly from three sources:
- the 2026-09-22 cohort audit, whose mapping had never been written in;
- the 2026-09-23 read-only audit, items 4–10;
- the propagation of the 2026-09-24(f) controls.

**Key changes:**
- cricket phase totals by innings order;
- the tennis benchmark as a blocking precondition, and matchup holds from serve × return;
- the METHOD probability-wording contradiction resolved;
- `COVERING_PAIR` and settlement-integrity labels;
- the recurring-mistake registry (M1–M30) now in-repo;
- the audit script repaired (it had silently truncated issue-time cards) and extended;
- a preflight `participants` object.

**Still open** (empirical, not documentable): the H0 dataset, chronological fits, prospective shadow, ~~non-MLB `R-1` magnitudes~~ (derived for five competitions in the 2026-09-25(b) research pass, below) and every TESTING manifest. These are tracked in `NUMERICAL_PROGRAM.md`, `H0_DATASET_CARD.md` and `LEARNING_REGISTER.md`.

**Custody:**
- P-509 settled (Part 5 §"2026-09-24(g)").
- P-484–P-486, P-488 and P-492 imported verbatim (Part 5 §"2026-09-25(a)").
- Active mini log: `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-510 onward - 2026-09-25/PREDICTION_MINI_RUNNING_LOG_P510_ONWARD.md`.
- Next ID: **P-510**.
- Control receipt: [`CONTROL_MANIFEST_2026-09-25.md`](CONTROL_MANIFEST_2026-09-25.md), superseded the same day by `CONTROL_MANIFEST_2026-09-25-2.md` (below).
- Everything remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.

<!-- RESEARCH-2026-09-25 -->
## Research pass — 25 September 2026(b)

**Question asked:** what else can be implemented to improve future results? **Answer, in short:** the recurring losses of the last cohorts were mostly *retrieval* failures (lineups, weather, invented process records) and *uncalibrated widths*, not missing model sophistication. This pass therefore did two kinds of work.

**1. Derived the base rates the framework had marked `NOT_YET_DERIVED`,** from population data rather than the log's own cards.
- **Recency (`R-1`) in five more competitions** (NBA, WNBA, NBL, NHL, EPL) — [`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md) §7. There is no rebound anywhere. The previous game is the worst predictor in 6 of 6 competitions, 18–40% worse than the league average. In basketball, the opponent's defence to date is worth more than any recency window.
- **Reference rates** — [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md) §7:
  - league totals, margin bands, quarter shapes and width benchmarks;
  - NBL early season **−8.5** and WNBA early season **+6.5** points (three seasons each, opposite signs);
  - the WNBA 2026 regime shift of **+10.7** points;
  - the NHL empty-net structure (73% of two-goal wins) and preseason rates;
  - EPL first-half goals and corners;
  - WTA/ATP total-games and games-handicap conditionals, which close the recorded WTA gap;
  - all 30 MLB parks and first-five-innings rates.
- **Width check** of the 2026-09-24 cohort: basketball total widths ran about 39% too narrow (mean z² 1.93, n = 7).

**2. Built and wired the controls that act on it.**
- [`receipts.py`](receipts.py) prints freeze and settlement receipts with endpoints: MLB lineups, weather and probables; NHL goalies and empty-net goals; ESPN starters and DNPs; the regulation score; and the `C-LINEUP-DIFF` lines. It replays the settled P-500, P-503, P-504 and P-506 facts exactly. Tests: [`test_receipts.py`](test_receipts.py), 17.
- The controls themselves are in [`RULES_GENERAL.md`](RULES_GENERAL.md) §"2026-09-25(b)":
  - `C-WIDTH-BENCHMARK` (disclosure);
  - `C-WIDTH-Z` (measurement; prospective manifest in `LEARNING_REGISTER.md`);
  - `C-RECEIPT-TOOL`;
  - early-season and regime references;
  - the `R-1` one-game corollary;
  - tennis `C-HCP-COHERENCE`.
- The sport files each have a §"2026-09-25(b)"; the research guide and logging workflow have new checklist steps.
- `audit_card_controls.py` gained fields `WB`, `HC` and `10z`, and a settlement-key fix. Tests: 70 in total.
- Registry item **M31** was added: width chosen without a reference.

**None of this moves a probability, centre, width or rank by itself.** Everything is disclosure, measurement or retrieval, and no coefficient was fitted from the log (`L-087`).
- Queries, scripts and results: [`research/base_rates_2026-09-25/`](research/base_rates_2026-09-25/README.md).
- Custody: the stray root `PREDICTION_MINI_RUNNING_LOG_P474_ONWARD.md` was checked and moved intact into its archive folder.
- Control receipt: [`CONTROL_MANIFEST_2026-09-25-2.md`](CONTROL_MANIFEST_2026-09-25-2.md).
