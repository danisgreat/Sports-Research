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

A reference changes only (a) at the start of a season, (b) when a lane reaches `DECISION_FLOOR_MET` with a paired interval below zero against the current reference, and (c) with an owner decision, recorded as a new row with a new `declared_for` and its evidence (ANCHOR path). Editing the table mid-season is a change of statistical method and follows STATFREEZE-v1 ([CURRENT_RULES](CURRENT_RULES.md) section 11).

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
