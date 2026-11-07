# Reference model, tiers and the model lane (REFMODEL-v1 / REFSEL-v1 / TIER-v1 / FASTCARD-v1)

**P-2026.10.22-v24.0 · CR-2026.10.22-R2.** Owner instruction, 22 October 2026, implementing recommendations REV-01, REV-06, REV-13, REV-15 and REV-22 of the [framework revamp review](research/verification/review_2026-10-22_framework_revamp/REPORT.md). It changes how a card's probability is produced, so the prompt major version moves to v24.0 and cards before it keep their own method.

## 1. Why

The review of 862 stated-probability rows found no detectable discrimination between 0.40 and 0.65 (calibration slope 0.15, SE 0.31), where almost every supplied spread and total sits, and a card has been compared with a same-row baseline on only 4 of its first 600 cards. A hand-built distribution re-derived from nothing on every card is slow, drifts wide or narrow from card to card, and cannot be scored against anything. A **reference** fixes that: every card starts from one frozen, scored number per contract, produced before the analyst writes, and the analyst's own work is the logged departure from it ([ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md)).

## 2. Tiers (TIER-v1)

`python -m ml reference tier --competition "<Sport/Competition>"` prints the tier. It is deterministic.

| Tier | Rule | Reference the card starts from |
|---|---|---|
| A | The competition has an active experimental release in [CURRENT_RELEASES.csv](research/cycle_releases/CURRENT_RELEASES.csv) | The declared choice in [REFERENCE_CHOICE.csv](research/competition_parameters/REFERENCE_CHOICE.csv) (section 4), by default the release's model |
| B | At least 100 verified final events in the learning store, or TB-1-MD league constants | TB-2-MD (points leagues) or TB-1-MD (goal leagues) from a dated standings table; else the league-only baseline |
| C | Anything else | The league-only baseline from the competition's parameter row or its family prior, with widths widened by 10%; or NONE |

Today: tier A NBA, NHL and MLB; tier B the NBL, WNBA, NFL, AFL, NRL and the five major soccer leagues (constants) and any competition with 100 stored finals; everything else tier C. A competition moves up when its history is ingested and its release gate passes (section 6). The tier is printed on every card and linted against the rule.

## 3. The reference stage (before the card)

The reference is produced and written to the working tree **before any probability is typed into the card**. The analyst's research (availability, history, conditions) can proceed in parallel; only the number must not precede the reference.

| Declared reference | Commands | Output |
|---|---|---|
| `RELEASE:<id>` (NHL, MLB) | `python -m ml pregame reference --game GAME.csv --lines LINES.csv --capture SOURCE.txt --confirm-no-outcome-seen` | Model and league baseline frozen in the shadow ledger; Reference block; receipt `research/pregame/<key>/…_REFERENCE_CYCLE.csv` |
| `TB2-MD` / `TB1-MD` | `python -m ml reference standings --competition C --home H --away A --out STANDINGS.csv --cache <dir outside the repository>` then `python -m ml reference run --game GAME.csv --lines LINES.csv --standings STANDINGS.csv --confirm-no-outcome-seen` | Reference rows and receipt `research/pregame/<key>/…_REFERENCE.csv` + `…_REFERENCE_ROWS.csv` with input hashes |
| `BASELINE_ONLY` | `python -m ml reference run` without `--standings` | League-only rows; `BASELINE_ONLY` |

When the declared reference is not the release (NBA today), tier A cards also run `python -m ml pregame reference` so that the fitted model is frozen beside the reference as the **challenger** (`model_p` in the picks block). Competitions without a release record `NOT_RUN_NO_RELEASE`.

After the card is written, `python -m ml pregame run …` freezes the card's own final `p_card` on the same contracts. If a reference stage already ran for that key it is **reused, never run twice**; if none did (a late request, or a release that appeared after the card began), `run` keeps the MLSCOPE-v2 behaviour and the model is only a shadow (stage `SHADOW`, `reference_status` `NOT_AVAILABLE` unless a tier B/C reference was produced).

Failure is recorded, not hidden: `NOT_RUN_NO_RELEASE`, `NOT_RUN_STALE_RELEASE`, `NOT_RUN_INPUT_REFUSED`, `FAILED`. A card whose reference could not run says so in `reference_status`, prices its own distribution as before and is scored in its own stratum.

The reference is never edited. A change of mind is an adjustment in the ledger, with its fact, source, time and size.

## 4. Choosing the reference (REFSEL-v1)

A competition's reference is **declared before the season and frozen for it** in `REFERENCE_CHOICE.csv`, with the development evidence that justified it. The order of evidence is: a walk-forward study on verified history (`python -m ml context-study`) comparing the candidates on identical games, with paired week-block intervals; calibration slope between 0.9 and 1.1; and no data-quality flag (`python -m ml release-gate`).

Declared on 22 October 2026 (evidence: [NBA studies](research/verification/framework_change_2026-10-22-2/), three seasons, 3,693 stored finals):

| Competition | Reference | Evidence |
|---|---|---|
| Basketball/NBA | **TB-2-MD** | Season-to-date, no fitted parameter. Brier 0.2113 (2024-25) and 0.2054 (2025-26); calibration slope 1.00 and 1.07. It beats the fitted cycle mixture with online Hedge by 0.0064 [0.0014, 0.0114] and 0.0072 [0.0008, 0.0137] and beats TB-1-MD by 0.0080 and 0.0100. The fitted model's slope is 1.30-1.60 (under-confident) and a recalibration map fitted on 2024-25 still leaves it at 0.2106 on the same 2025-26 games against TB-2-MD's 0.2054, so no calibration layer is added |
| Ice Hockey/NHL | the NHL-CYCLE-4 release | 2024-25 within-season (1,106 games): release 0.2423, TB-2-MD 0.2413, difference +0.0014 with an interval spanning zero. No evidence for a change |
| Baseball/MLB | the MLB-CYCLE-4 release | 374 stored finals: no walk-forward is possible yet |

A reference changes only (a) at the start of a season, (b) when a lane reaches `DECISION_FLOOR_MET` with a paired interval below zero against the current reference, and (c) with an owner decision, recorded as a new row with a new `declared_for` and its evidence (ANCHOR path). Editing the table mid-season is a change of statistical method and follows STATFREEZE-v1 ([CURRENT_RULES](RULES_REFERENCE.md#part-a-current_rules) section 11).

## 5. TB-2-MD

TB-1-MD ([PROBABILITY_TOOLKIT](PROBABILITY_TOOLKIT.md) section 4) sets each side's expected score to the **mean** of its own attack and the opponent's defence. That halves the margin signal: the two net ratings enter as (net_home − net_away) / 2. TB-2-MD **adds** the two deviations from the league mean instead (score = attack + opponent defence − league mean), so the margin is the net-rating difference plus the home edge:

- ratings O = (PF + k·LM) / (n + k) and D = (PA + k·LM) / (n + k), with the toolkit's k, widths and home edge unchanged;
- expected total T = (Oh + Da − LM) + (Oa + Dh − LM); expected home margin M = (Oh − Dh) − (Oa − Da) + HE;
- probabilities from one coherent score grid (`ml.reference`), with overtime resolved from the margin.

No parameter is fitted. Measured, season to date, on stored finals (the games before each game in the same season; Brier of home win; slope of the outcome on logit p):

| Competition (games) | TB-1-MD Brier / slope | TB-2-MD Brier / slope |
|---|---|---|
| NBA 2023-26 (3,603) | 0.2189 / 2.12 (SE 0.10) | **0.2106 / 1.04 (SE 0.05)** |
| NHL 2024-25 (1,282) | 0.2429 / 1.90 (SE 0.34) | 0.2417 / 0.95 (SE 0.17) |
| MLB 2025 (344) | 0.2450 / 2.54 (SE 0.83) | 0.2427 / 1.26 (SE 0.41) |

TB-1-MD's slope near 2 is the halving. Shrinkage k = 2 is not the cause: for the NBA, k = 2 is within 0.0005 of the best of the grid {2, 5, 8, 12, 20, 30} in each of the three seasons, and larger k only raises the slope (1.0 at k = 2, 1.3 at k = 8, 1.8-2.0 at k = 30). TB-2-MD is the reference for points leagues. TB-1-MD is still computed on request and printed as `TEAM_BASELINE_P` for continuity with earlier cards; goal leagues (soccer) keep TB-1-MD, whose P6 validation stands and where no store history exists to test the additive form. TB-2-MD is registered for prospective confirmation (`REV-H1` in the [hypothesis register](HYPOTHESIS_REGISTER.md)).

The league mean per team-game enters only the total (it cancels from every margin). In the first weeks it rests on a handful of games, so it is blended with the competition's verified prior mean, (n·current + 200·prior)/(n + 200), and `LM_PRIOR_BLEND` is printed. The weight 200 is a starting value, not a tuned parameter.

## 6. The model lane (REV-06, REV-07, REV-22)

A model earns its place only by prospective evidence at league volume, because carded games alone cannot decide anything in under years.

1. **Data.** Verified finals enter the learning store through a two-lineage backfill (`python -m ml backfill-basketball`: ESPN and Basketball-Reference must agree on teams, final and overtime). 3,693 NBA finals (2023-24 to 2025-26) were ingested on 22 October 2026; every capture hash re-verifies.
2. **Gate.** `python -m ml release-gate --competition C` must pass before a release is frozen: enough finals over two seasons, no plausibility warning, nothing in quarantine, two source domains for every final, observed regulation scores for every extra-time final, no revision conflict.
3. **Development.** `python -m ml context-study` reports the walk-forward Brier, the paired differences against the league-only arm and TB-2-MD, the calibration slope and the width coverage on the previous seasons.
4. **Release.** `python -m ml cycle release …` freezes one version for the season. Edits outside the cycle's import closure (`ml/code_identity.py`) never retire it. An edit inside it needs a new version and a new lane, so statistical code is edited between seasons.
5. **Daily lane.** `python -m ml league-day freeze --competition C --date D --cache <dir> --confirm-no-outcome-seen` freezes every open fixture of the day, card or not: the release's model (CANDIDATE), the league baseline (CHAMPION) and the declared TB-2-MD reference (champion `TB2_MD_REFERENCE`) on two contracts, the home winner and the total at the half point below the league's verified mean. Commit and push before the first tip-off. `python -m ml league-day settle …` a day or two later ingests the date's finals (ESPN and Basketball-Reference must agree) and settles every frozen bundle of the date into `research/cycle_feedback/`. No automation is scheduled; the operator or prompt 1 runs both each day (R38).
6. **Judgement.** `python -m ml pregame status` flags a progress review at 8 settled weeks or 50 settled paired games, whichever comes first, and the decision floor when both are met. `python -m ml pregame compare-card --release R --champion TB2 --out DIR` pairs the fitted model against the reference on identical frozen rows.

NBA-CYCLE-1 was frozen on 22 October 2026 with the family defaults (fast 45 days, slow 180 days, ridge 12). It is a challenger: it does not feed a card. The first league-day freeze is recorded in the [implementation report](research/verification/framework_change_2026-10-22-2/IMPLEMENTATION.md).

## 7. Fast card (FASTCARD-v1)

Requests often arrive minutes before the start. When the full research will not finish before the scheduled start, issue the **fast card** first: the reference stage, the picks block built from the reference and whatever availability is already confirmed, `fast_card: YES`, committed and pushed. Then complete the full card and append it as a dated addendum under the same local key (the first issue is never edited). A fast card is scored in its own stratum. A request that arrives after the start is `POST_START_ISSUE` whatever the card contains.

## 8. Limits

- TB-2-MD's evidence is development evidence on current-capture labels, unadmitted at the field-owner level; it is not a pregame replay, and the walk-forward treats each final as usable one day after its game (a stated assumption).
- Historical context features (rest, form) are not fitted in the store-based models because the backfilled history has no known-at times; the live cycle behaves the same way.
- The NBA walk-forward covers three seasons from one provider pair. The NHL study is one season, and no study exists for MLB or any goal league.
- Nothing here claims a model or a reference is qualified; every release remains `EXPERIMENTAL_NOT_QUALIFIED`.

---

# Merged: FORECAST_CYCLE_PROTOCOL

*Merged 2026-11-07 (CR-2026.11.07-R2, FORMAT), verbatim. Formerly `FORECAST_CYCLE_PROTOCOL.md` (original title: Executable research, learning and forecast cycle). Original kept unchanged at [archive/consolidation_2026-11-07/merged_sources/FORECAST_CYCLE_PROTOCOL.md](archive/consolidation_2026-11-07/merged_sources/FORECAST_CYCLE_PROTOCOL.md).*

**ML/RL scope (MLSCOPE-v3).** Owner instruction, 22 October 2026 (second instruction of the day, adopting the framework revamp review): models run where they are needed and a competition's declared reference model runs **before** the card. For a tier A competition whose declared reference is its release (NHL, MLB), prompt 1 freezes the model first (`python -m ml pregame reference`) and the card starts from that frozen number; where another reference is declared (the NBA's TB-2-MD) the release is frozen the same way as a challenger. Tier B and C competitions start from TB-2-MD, TB-1-MD or the league-only baseline (`python -m ml reference run`). The analyst's `p_card` (ANALYST_PRIMARY_V1) is that reference plus logged adjustments with sizes from the effect tables ([REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md), [ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md)); a frozen reference is never edited, and the card's own final p is frozen beside it by `python -m ml pregame run`. If no reference could run first, the model is only a post-card shadow and the card says so. Prompt 3 settles the card, then the frozen rows; prompt 6 ingests and evaluates; prompt 8 builds releases and decides promotion. A model is judged only on frozen, pushed, pre-start rows after at least 8 settled weeks and 50 settled paired games; a progress review falls due when either is reached first. A release is frozen for a season and edits outside the cycle's import closure never retire it. RL has no forecasting role: the online expert weighting that updates at settlement is online learning. Supersedes MLSCOPE-v2 (card first, model never feeds the card), MLSCOPE-v1 and NOCODE-v1 for cards under P-2026.10.22-v24.0 and later; earlier cards keep their method.

**CYCLE-2026.10.16-v1 / MDS-2026.10.16-v20.0 / CR-2026.10.16-R7 / P-2026.10.16-v20.0.** Owner-authorised experimental implementation. Class: STATISTICAL + PROCEDURE. Amended by CHAT-EXEC-v1 (MDS-2026.10.17-v20.1 / CR-2026.10.17-R1 / P-2026.10.17-v20.1): browser-chat execution, below. Existing scoring v11, selection v3, canonical IDs, mini formats and issued originals retain their original meaning. No model is prospectively qualified by this release.

The operational path is research export -> reviewed store -> point-in-time training inputs -> frozen competition policy -> actual forecast bundle -> identical-contract baseline shadows -> verified settlement -> later fits and online expert weighting -> paired prospective evaluation. A supported request ends in a verified bundle or a verified failure receipt. Research is retained in both cases. Canonical P-IDs are assigned only at prompt 4; model event identity uses native provider IDs or stable local event keys.

## Reference stage, card freeze and the daily lane (MLSCOPE-v3 / PREGAME-v2)

Owner instruction, 22 October 2026. Prompt 1 runs in this repository (ENV-v2). The reference is produced and frozen **before the analyst writes a number**, and the card's own final probability is frozen after it, on the same contracts. The tiers, the reference ladder and the choice table are in [REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md).

```text
python -m ml pregame reference --game GAME.csv --lines LINES.csv --capture SOURCE.txt --confirm-no-outcome-seen
python -m ml pregame run --mini research/active_minis/<MINI_KEY>.md --game GAME.csv --lines LINES.csv --capture SOURCE.txt --confirm-no-outcome-seen
python -m ml pregame status
python -m ml pregame compare-card --release research/cycle_releases/<RELEASE>.csv [--champion CARD|TB2] --out <new folder>
python -m ml league-day freeze --competition "<Sport/Competition>" --date YYYY-MM-DD --cache <dir outside the repository> --confirm-no-outcome-seen
python -m ml league-day settle --competition "<Sport/Competition>" --date YYYY-MM-DD --cache <dir outside the repository>
```

GAME.csv has the CHAT-EXEC columns (`local_key,competition,native_event_id,season,scheduled_start,home,away,venue,source_url`). LINES.csv has `label,family,side,line`; for `run` it also carries `card_p` and `card_rank`, the card's printed final p_card and rank for that full-game winner, handicap or total row. SOURCE.txt is a text copy of the opened fixture source.

| Guard | Behaviour |
|---|---|
| `pregame reference`, no release for the competition | `NOT_RUN_NO_RELEASE` receipt (`…_REFERENCE_CYCLE.csv`); nothing frozen; the card proceeds with the reference ladder's next rung |
| `pregame reference`, release frozen for other forecast code | `NOT_RUN_STALE_RELEASE`; prompt 8 must freeze a new release version |
| `pregame reference`, input the cycle refuses (team name, family, time, capture) | `NOT_RUN_INPUT_REFUSED` with the exact reason |
| `pregame reference`, executed | The cycle bundle is verified and accepted; the model (CANDIDATE) and the league baseline (CHAMPION) are frozen in `research/prospective/CYCLE_SHADOW_LEDGER.csv` on identical contract keys with the actual clock. Receipt `research/pregame/<key>/<stamp>_REFERENCE_CYCLE.csv` (stage `REFERENCE`) |
| `pregame run`, card not yet in the mini | Refused: the card must hold exactly one complete `BEGIN CARD` / `END CARD` pair, and every `card_p` must appear verbatim in it |
| `pregame run`, an executed reference exists for the key | The attempt is **reused**: no second run or acceptance. Only the card's final p is frozen (`ANALYST_PRIMARY_V1:CARD`, champion). Stage `REFERENCE_REUSED` |
| `pregame run`, no reference was run | MLSCOPE-v2 behaviour: the cycle runs after the card, freezing model, baseline and card; stage `SHADOW`; the card says the model was not the reference |
| `league-day freeze` | For every open regular-season fixture of the day: model and baseline as above on two contracts (home winner; total at the half point below the verified mean), plus the declared TB-2-MD reference frozen as champion `TB2_MD_REFERENCE`. Commit and push before the first tip-off |

Every run writes a receipt under `research/pregame/<local key>/` (status, reason, release, mini and card-block SHA-256, attempt path, ledger rows). The printed Reference block is pasted into the card above the picks; the shadow block below it. **A frozen reference, a receipt or a ledger row is never edited.** Commit and push before the scheduled start: a row is PRE_START_VERIFIED only when generation and freeze precede the start, and only the pushed commit makes that externally checkable.

**Settlement.** Prompt 3 settles the card first, then runs `cycle settle` for each shadowed or league-day event.

**How long a model is watched.** A release's lane needs at least **8 settled ISO weeks and 50 settled paired events** before any decision. The frozen release enforces both: `cycle evaluate` returns INSUFFICIENT_EVIDENCE below 50 events and the paired evaluation below 8 weeks. `pregame status` reports `PROGRESS_REVIEW_DUE` when **either** floor is reached first and `DECISION_FLOOR_MET` when both are, and counts `card_paired_settled` and `reference_paired_settled`. These are floors, not power: some lanes need far longer ([review](research/verification/review_2026-10-21_league_neutral_ml_sim/REPORT.md) section 4). `compare-card --champion TB2` pairs the fitted model against the TB-2-MD reference on identical frozen rows; `--champion CARD` pairs it against the analyst's final p.

**Release scope (RELEASE-SCOPE-v1) and season freeze.** A release freezes the digest of the forecast cycle's own import closure (`ml/code_identity.py`: every ml module that `ml.cycle` or `ml.workflow` can import), not every ml file. Editing a report, chat, pregame, reference, ledger, picks, league-day or simulator module does not retire an active release; editing a file inside the closure does, and needs a new release version with its own lane. Statistical code is edited between seasons (STATFREEZE-v1).

## Research command and execution boundary

Run in a Python-capable worker with a pinned repository checkout. Install `python -m pip install -r ml/requirements.txt`, run `python -m ml capability`, then use the stdlib entry point below. A read-only browser session must hand the request and exact source captures to that worker; viewing GitHub is not executing a model. If Python/module checkout itself cannot start, retain the exact command, stderr, environment and bootstrap attempts in the mini's A9 and leave the model unestimated. Never invent an EXECUTION.csv. A process that cannot write its output directory reports the real filesystem error in A9.

```text
python -m ml cycle release --competition "Basketball/NBL" --endpoint FULL_GAME_INCL_OT --version NBL-CYCLE-1 --out research/cycle_releases/NBL-CYCLE-1.csv
python -m ml.workflow research --export RESEARCH_EXPORT --store research/learning_store --request REQUEST.csv --contracts CONTRACTS.csv --release research/cycle_releases/NBL-CYCLE-1.csv --out ATTEMPT --feedback-root research/cycle_feedback --ledger research/prospective/CYCLE_SHADOW_LEDGER.csv
python -m ml.workflow verify --attempt ATTEMPT
```

`ml.workflow` imports only Python's standard library until it has created STARTED.csv and captured request identity. It then imports the numerical runtime inside the receipt boundary. Dependency/import, source, identity, history, adapter, fit, publication and ledger failures retain the real exception and traceback, captured inputs and a hash manifest in a new immutable attempt directory. Nonzero exit means failed, even if a partial bundle exists. Reruns use new directories. EXECUTION.csv/FILES.csv verification checks all retained files. Neither a success receipt nor a hash certifies sporting source truth or independent pre-start publication.

Every new supported research request must attempt execution. `MODEL_ASSISTED_CYCLE_V1` requires the verified contextual cycle bundle. Existing `MODEL_ASSISTED_PRIMARY_V3` requires its actual V3 bundle. Unsupported/unavailable/failed work retains `RESEARCH_ONLY_NO_MODEL`, explicit stage/error and `NOT_ESTIMATED` model p. Use the existing execution manifest columns; execution.py now verifies both attempt types. Preserve the cumulative mini and return its complete updated Markdown after each request. Model diagnostic ranks do not waive selection, complement, family, probability-ceiling, rank-1 baseball +1.5 or research-completion checks. The cycle prices the complete frozen candidate slate; card eligibility is a separate decision.

## Browser-chat execution (CHAT-EXEC-v1)

A web chat's GitHub connector reads files; it cannot import or run `ml`. A chat with a Python sandbox can run the unchanged cycle from a runtime pack. Each step keeps the attempt receipts above; nothing here changes models, parameters, selection or scoring.

```text
python -m ml.chat pack --out <folder outside the repository>            # checkout: owner PC or coding agent
python -m ml.chat run --game GAME.csv --lines LINES.csv --capture SOURCE.txt --out OUT --confirm-no-outcome-seen   # sandbox, from the unzipped root
python -m ml.chat accept --attempt UPLOAD.zip --local-key LOCAL-<MINI_KEY>-G0001                                  # checkout, before the start
python -m ml.chat accept --attempt research/cycle_attempts/<key>/<attempt> --local-key <key> --freeze-basis commit # after a pre-start GitHub upload
```

| Step | What it does | Refuses |
|---|---|---|
| `pack` | `git archive` of a commit (default HEAD) with line-ending conversion off: `ml/`, `research/learning_store/`, `research/cycle_releases/`, `research/cycle_feedback/` when present, and every capture the store's SOURCE_OBSERVATIONS names. Adds CHAT_PACK_RECEIPT.csv (commit, normalized code digest, active releases, archive hash). Uncommitted edits are listed, never packed. | An output folder inside the repository (the zip is a binary and is never committed); a store capture absent from the commit; an active release whose file hash or frozen code digest differs from the packed code. |
| `run` | Validates GAME.csv (`local_key,competition,native_event_id,season,scheduled_start,home,away,venue,source_url`) and LINES.csv (`label,family,side,line`), copies the capture to `research/chat_captures/<local key>/`, writes the exact TARGET_EVENT export, REQUEST and CONTRACTS (definition FROZEN_FRAMEWORK_CONVENTION; winner THREE_WAY_DRAW_LOSES, handicap/total STANDARD_COMPLETED), runs `ml.workflow` with the competition's active release and verifies the attempt. Writes RESULT.csv (p_card, baseline_p, model rank, timing at generation) and `UPLOAD_<key>_<attempt>.zip` laid out at repository paths. A FAILED attempt is returned with its real error. | Missing outcome confirmation; running outside the runtime root; competitions without an active release; team names absent from the stored participants (the stored names are listed); P-IDs or unprefixed native IDs; times without a UTC offset; families other than full-game winner/handicap/total; non-numeric lines; non-text captures; a reused output folder. The cycle itself still refuses a release frozen after the information horizon. |
| `accept` | Extracts the upload only into `research/cycle_attempts/<key>/` and `research/chat_captures/<key>/` (CSV/TXT/MD members, no overwrite of different bytes), re-verifies the attempt and target capture, freezes CANDIDATE and CHAMPION shadow rows in `research/prospective/CYCLE_SHADOW_LEDGER.csv` and writes `<attempt>_ACCEPTANCE.csv` with the execution-manifest values. | Members outside those folders or of other types; a second acceptance; an attempt collected for another local key; `--freeze-basis commit` unless the attempt is committed unchanged and its adding commit is on origin/main. |

The freeze clock is the actual acceptance time, or with `--freeze-basis commit` the committer time of the pushed commit that first added the unchanged attempt. PRE_START_VERIFIED therefore needs generation, freeze and publication before the scheduled start; a later acceptance is TIMING_UNVERIFIED and a post-start generation is never pre-start. A sandbox ledger, screenshot or chat transcript is not a freeze. Pinned-version drift between the sandbox and `ml/requirements.txt` is recorded by `python -m ml capability`; the pack was exercised under Python 3.12 / pandas 2.2 / numpy 1.26 / scipy 1.13 with byte-identical bundle verification. Until 22 October 2026 changing any `ml/*.py` changed the frozen code digest (NHL-CYCLE-3 / MLB-CYCLE-3 replaced the unused v2 releases for that reason, and went stale in turn); under RELEASE-SCOPE-v1 only files in the cycle's import closure do.

## Adapter and endpoint scope

| Route | Exact supported scope | Inputs and limitations |
|---|---|---|
| `--adapter context` (default) | Competition-local basketball, AFL/state AFL, American/college/Canadian football, rugby league/union, soccer, ice hockey and baseball at the endpoint in ml.config.SPORT_RULES | Reviewed structured store, target export, frozen release, explicit contracts. At least 30 admitted events and previously observed participants. No borrowing a different competition's model or endpoint. |
| `--adapter primary --history HISTORY.csv [--competition-source COMPETITION_SOURCE.csv] [--feedback FEEDBACK.csv]` | Existing reviewed V3 adapters, including full-length limited-overs first innings | Actual legacy V3 bundle and same-line league baseline. For this route omit --release; HISTORY must contain the adapter's required source/innings fields. It retains V3's old recipe and adaptation; it does not inherit the new cycle's statistical claims. |
| `--adapter tennis --history HISTORY.csv [--feedback FEEDBACK.csv]` | Existing experimental completed singles best-of-3/5 tennis | Its actual point/surface/Elo bundle and COHORT_BASE comparator, in the experimental tennis shadow lane. Export target uses player1/player2 as home/away and COMPLETED_BEST_OF_N as endpoint. Omit --release. No automatic primary promotion. |
| Other formats, phases, corners, props, field hockey, multi-day cricket, unavailable inputs | Explicit failed attempt | Preserve source-backed research and exact unsupported reason; do not create a numerical adapter by analogy. |

Contextual models fit each competition separately. Points sports use joint final-score ridge distributions; low-count sports use final-score log-mean count distributions with fitted dispersion. All contracts are functions of a single score-grid mixture. Final endpoints are fitted directly: an overtime final is never treated as regulation and then given another extra-time branch. Regulation-only endpoints keep their own labels. Legacy regulation paths reject non-tied or final-as-regulation extra-time coordinates. Unobserved regulation remains NOT_OBSERVED in the store and is excluded from regulation training releases.

Baseball's final-score count grid is coherently reweighted using a separately fitted winner-class regression. This addresses the specific home-win inference defect caused by inferring winners from uncensored nine-inning mean runs. It is an experimental approximation; it does not reproduce inning-level walk-off/extra-run mechanics or prove run-line/tail calibration. No existing baseball artifact is restamped as repaired or qualified.

## Context and source timing

Derived form, statistics and availability snapshots use information visible at each historical event. Fixed event identity/venue labels may be verified in a current backfill for training future forecasts; that does not establish their historical pre-start capture or permit a retrospective timing claim. Features include L5/L10/L20 form, rest, pace when measured, confirmed starters/absences, lineup completeness, venue, reviewed NEUTRAL_VENUE statistics, and confirmed player identity/role indicators. Pitchers, goalies and other starting roles can enter through confirmed identity/role observations. Effects are estimated from the exact competition's historical data; there are no hand-invented injury/lineup point adjustments. A feature with fewer than five observed rows or no historical variation has no fitted coefficient. CONTEXT_STATUS.csv and the retained training context expose this limitation; material unsupported availability effects still require scenarios or qualitative/no-forecast treatment.

Projected players are not confirmed. Missing context retains missingness and a fitted missing indicator where the feature is estimable; zero absences never means an unknown roster is healthy. Venue coefficients are fitted where observed. Neutral-site effects require reviewed NEUTRAL_VENUE data with historical variation; unknown neutral status is not a verified home advantage adjustment. Mandatory online history and confirmed-player searches still apply to every sport. Reviewed historical backfills captured today are known today, not retroactively known at their match date.

## Historical identity and learning admission

`python -m ml historical-identity build --map MAP.csv` source-addresses every original record behind the 21 detected colliding historical P-ID aliases. `verify` checks the original file and exact body hashes. Originals and issued IDs stay unchanged. Distinct bodies cannot share a model event solely because their issued P-ID is the same. The learning store rejects a bare P-ID as native event identity, rejects reused native IDs on another UTC date, and rejects ambiguous native/alias matches. Provider IDs distinguish doubleheaders; date/participant surrogates alone cannot merge distinct same-day games.

Card-history analytics preserve literal grades but exclude collided aliases from effective-grade joins and use UNRESOLVED in derived metrics until exact body/contract/settlement linkage is verified. This repairs unsafe joins; it does not claim all historical grade links have been recovered. The source-address map and explicit repair queue are authoritative for what remains. No empty contract is reconstructed from a win/loss pattern.

The `historical-backfill` command retrieves MLB/NHL owner results and independently reconciles ESPN by date, participants, UTC scheduled instant, final score and regulation period/innings totals. Reviewed provider team-code aliases are explicit. A unique MLB matchup may retain the owner schedule with a disclosed provider start-time offset of at most 15 minutes. Two NHL games whose listed clocks differed by 30/35 minutes received separate manual review: unique same-day teams and both period/final scores were verified, owner scheduled time retained, actual start left NOT_VERIFIED. These current backfills cannot certify historical pre-start timing. Each owner candidate has an admitted or not-ingested disposition. Store rows retain reviewed captures, actual current availability and revision history. `final_at` in this bounded backfill is the current observed-final upper bound, explicitly labelled; it is not an exact historical finish time. Raw HTTP bodies stay outside the repository, with their hashes and retrieval receipts retained alongside committed fact-only CSV projections. The retired Previous Sports Results folder is never restored or read. Other competitions/cards remain a separately evidenced backfill queue.

## Settlement and online adaptation

```text
python -m ml cycle settle --bundle ATTEMPT/BUNDLE --export SETTLEMENT_EXPORT --store research/learning_store --out research/cycle_feedback/LOCAL_KEY_REV1
```

Settlement ingests the independently researched result export, rejects quarantine, verifies the frozen forecast and capture, and recomputes each expert's proper distribution score plus exact contract outcomes. It emits SETTLEMENT.csv, INGEST.csv and OUTCOMES.csv. Later research automatically reads effective feedback from --feedback-root and fits on admitted settled results. Results without a prior actual bundle can train future score/context models but never invent historical expert losses.

The frozen cycle uses fast and slow sport-family decay recipes plus a competition-only baseline. Recipes are predeclared experimental starting values, not tuned claims. Only exact-release, competition/endpoint feedback available by the next information horizon can affect weights. Each event is counted once; later verified result revisions replace that event's earlier effective feedback for later forecasts without rewriting past bundles. Conflicting effective revisions block execution.

Expert loss combines three-way winner Brier with scaled margin and total CRPS. Older feedback decays with a 20-event half-life; a range-adaptive learning rate is capped at 0.5 and each expert retains at least 0.05 weight. Newly settled outcomes can therefore move subsequent weights without thousands of retrospective warm losses dominating them. The retained ledger reproduces every weight. These engineering choices use actual sporting feedback and are experimental; no empirically optimal forgetting rate, predictive gain or RL control policy is claimed. The discounted-learning literature motivates testing forgetting, rather than certifying these particular values: [Zhang et al., ICML 2024](https://proceedings.mlr.press/v235/zhang24e.html).

## Frozen prospective experiment

Release CSVs freeze source digest, competition/endpoint, feature/model specification, decay, ridge, adaptation and evaluation thresholds. They are immutable. Changed code or settings require another version and cohort. LF/CRLF checkout changes do not alter the normalized cycle source digest. Each forecast retains fitted coefficients, covariance, dispersion, smearing, design columns/normalizers, feature/history snapshots and actual grids. Refitting on new settled data follows the frozen learning rule; changing the rule does not silently remain the same version.

Workflow success freezes model and baseline rows together for identical contracts, orientations and endpoints. Baseline is COMPETITION_FINAL_LEAGUE_V1 for the new final-score cycle; it is distinct from legacy BASELINE_LEAGUE_V1. Definition and action are hashed into the cycle's contract identity. Actual generation and freeze clocks govern prospective status; a backdated declared issue, post-start run or retrospective evaluation never becomes a pre-start forecast. Local receipts still need a real before-start publication/commit for externally auditable publication claims.

```text
python -m ml cycle evaluate --release research/cycle_releases/NBL-CYCLE-1.csv --ledger research/prospective/CYCLE_SHADOW_LEDGER.csv --feedback-root research/cycle_feedback --out NEW_EVALUATION
```

Evaluation verifies the chain, exact-release scope, settled evidence and identical contracts. Brier, log loss and calibration use the same decisive paired rows; pushes/voids stay outside binary labels. It reports both Brier and log-loss differences with event-then-week paired uncertainty intervals, calibration slope/intercept and reliability bins, coverage and exclusions. One game with multiple contracts is not multiple independent games. The frozen minimum is 50 paired events and eight weeks with a 0.01 preregistered Brier effect; power and calibration guards still apply. An empty/short future cohort returns INSUFFICIENT_EVIDENCE. A recommendation never automatically promotes a registry entry. Proper-score interpretation follows the [scoringrules reference](https://scoringrules.readthedocs.io/en/latest/theory.html).
