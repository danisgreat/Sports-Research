# Comprehensive audit on request · 16 November 2026 · P-001 to P-685

Written for the owner and for the next prompt 8 run. Scope and exclusions: [SCOPE](SCOPE.md). Tables: [COHORT_TABLES.csv](COHORT_TABLES.csv), [CALIBRATION_TABLES.csv](CALIBRATION_TABLES.csv), [DEEP_LOSS_TALLY.csv](DEEP_LOSS_TALLY.csv). Improvement plan: [CHANGE_PROPOSAL](../framework_change_2026-11-16-1/CHANGE_PROPOSAL.md).

Everything below is retrospective: the outcomes were known. Intervals are 95%, taken over cards, and assume cards are independent, which they are not fully (shared teams, dates and chats), so they are optimistic.

## 1. The main finding

**Nothing the framework produces today can be judged, because no current card is a forecast of record.**

| Measure | Value | Source |
|---|---|---|
| Cards issued under the v24 reference-first design (ledger rows) | 0 contract rows on 0 cards | `ml state`, ADJUSTMENT_LEDGER.csv |
| Games frozen in the three model lanes | 0, 0 and 0 (MLB, NHL, NBA); all three releases STALE_FOR_CURRENT_CODE | `ml pregame status` |
| Games eligible for the registered 100-game assessment | 0. The FIVE_LANES against SINGLE_RESEARCH comparison has never run on a real game | research/external/README.md |
| Games in the learning-log dataset | 0 built, 0 admitted | `ml learning-log build` |
| Cards from 12 November onward that are issued forecasts | 0 of 47 games (P-639 to P-685); all are chat-local research, NOT_ISSUED | import packages |
| Prospective shadow ledger | 12 rows on 2 games, both in October | CYCLE_SHADOW_LEDGER.csv |

The rules describe a reference-first, ledgered, linted card made in this repository, and a five-lane external comparison. The work actually done is one ChatGPT chat per game writing its own card, settled here afterwards. The two no longer meet, so every scoring, promotion and learning route is empty. More rules cannot fix this; the chat's card has to become the measured object.

## 2. What the 685 settled cards show

### 2.1 Stated probabilities

1,273 rows on 279 cards carry a stated probability. Compared with a constant 0.5:

| Cohort | Rows / cards | Stated p | Won | Brier | Card-mean Brier minus 0.25 |
|---|---|---|---|---|---|
| All | 1,273 / 279 | 0.565 | 0.568 | 0.2312 | **-0.0203 [-0.0312, -0.0093]** |
| Rank 1 | 233 / 233 | 0.674 | 0.627 | 0.2231 | -0.0269 [-0.0502, -0.0036] |
| Rank 2 | 224 / 224 | 0.624 | 0.616 | 0.2201 | -0.0299 [-0.0480, -0.0118] |
| Unranked chat rows | 345 / 47 | 0.505 | 0.501 | 0.2488 | +0.0019 [-0.0203, +0.0242] |
| September | 622 / 159 | 0.556 | 0.566 | 0.2329 | -0.0165 [-0.0298, -0.0032] |
| October | 359 / 87 | 0.628 | 0.616 | 0.2150 | -0.0352 [-0.0579, -0.0125] |
| November (chat research) | 288 / 31 | 0.509 | 0.510 | 0.2470 | **+0.0003 [-0.0297, +0.0303]** |

The stated numbers were better than a coin through October. In November they are not distinguishable from one: the chats print numbers close to 0.5 and win at 0.5.

### 2.2 Where the information sits

| Stated p band | Rows / cards | Stated | Won | Card-mean Brier minus 0.25 |
|---|---|---|---|---|
| below 0.50 | 454 / 199 | 0.418 | 0.474 | +0.0002 [-0.0100, +0.0105] |
| 0.50 to 0.55 | 173 / 122 | 0.526 | 0.491 | +0.0003 [-0.0047, +0.0054] |
| 0.55 to 0.60 | 192 / 142 | 0.569 | 0.578 | -0.0003 [-0.0110, +0.0105] |
| **0.60 to 0.65** | 147 / 114 | 0.621 | **0.517** | +0.0089 [-0.0123, +0.0301] |
| 0.65 to 0.70 | 73 / 64 | 0.670 | 0.685 | -0.0264 [-0.0653, +0.0124] |
| 0.70 to 0.75 | 59 / 44 | 0.722 | 0.729 | -0.0374 [-0.0945, +0.0197] |
| 0.75 to 0.80 | 47 / 39 | 0.769 | 0.723 | -0.0383 [-0.1125, +0.0358] |
| 0.80 to 0.90 | 122 / 45 | 0.864 | 0.852 | **-0.1030 [-0.1704, -0.0356]** |

- Below 0.65 the numbers carry no measurable information. That is 966 of the 1,273 rows.
- The 0.60 to 0.65 band is overconfident: stated 62%, won 52%; card-mean gap -10 points [-19, -1].
- Nearly all the measured gain comes from 0.80 and above, which is mostly October cards on lines the analyst derived, not lines the owner supplied. That is line choice, not forecasting of a supplied line. FREEZE-v1's `rank_scope: SUPPLIED_ONLY` already answers this for counting.
- Rank 1 was stated at 67% and won 63%.

### 2.3 By sport (rows with a stated p)

| Sport | Rows / cards | Card-mean Brier minus 0.25 | Reading |
|---|---|---|---|
| Cricket | 64 / 17 | -0.0508 [-0.0817, -0.0199] | better than a coin |
| Basketball | 312 / 62 | -0.0376 [-0.0628, -0.0123] | better than a coin |
| Soccer | 264 / 59 | -0.0352 [-0.0669, -0.0034] | better than a coin |
| Ice hockey | 113 / 16 | -0.0284 [-0.0619, +0.0052] | not resolved |
| Baseball | 301 / 81 | -0.0087 [-0.0231, +0.0056] | not resolved |
| Tennis | 125 / 20 | +0.0282 [-0.0068, +0.0631] | leaning worse than a coin |
| American football | 28 / 7 | +0.0377 [+0.0135, +0.0619] | worse than a coin, 7 cards |
| Australian rules | 14 / 4 | +0.0989 [+0.0443, +0.1534] | worse than a coin, 4 cards |

Rank 1 win rates over all 609 Rank 1 rows, with or without a number: soccer 76.1% (142), baseball 63.7% (193), tennis 61.7% (47), cricket 60.7% (56), basketball 54.5% (77), rugby league 47.4% (19), Australian rules 44.1% (34), American football 36.8% (19). Overall 62.6% [58.7, 66.3]; Rank 2 57.1%, Rank 3 55.6%, Rank 4 55.5%. The order of ranks holds; the size of the gap is small.

### 2.4 By contract

Totals 55.3% (1,536 rows), handicaps 53.8% (906), winners 57.8% (237), period lines 58.2% (208), corners 67.5% (117). Period Overs won 67.6% (102) and corner Overs 67.5% (83), against period Unders 45.8% (96). These are raw rates on lines of unequal difficulty; they are hypotheses, not edges.

### 2.5 Share of rows with no number

1,756 of 3,029 decisive rows (58%) have no stated probability, including 264 of the 552 November rows. A row without a number can only be counted as a win or a loss, never scored for calibration, and cannot enter the 100-game assessment.

## 3. Deep loss reviews, P-660 to P-685

21 reviews: 10 ERROR, 5 VARIANCE, 3 MODEL_LIMIT, 2 VARIANCE with MODEL_LIMIT, 1 MIXED. The reviews did not record a registered failure class or count earlier reviews of the same class, as the template's item 11 asks; the classes in [DEEP_LOSS_TALLY.csv](DEEP_LOSS_TALLY.csv) were assigned for this audit from each review's own verdict text.

| Pattern (alias → registered class) | Reviews | IDs |
|---|---|---|
| UNMEASURED_AVAILABILITY_PRICED → UNFITTED_ANALYST_ADJUSTMENT | 4 | P-674 (two), P-676 (two) |
| LEAN_AGAINST_OWN_PRINTED_EVIDENCE → OTHER | 4 | P-662, P-671, P-678, P-680 |
| PLUS_HANDICAP_WITHOUT_OPPONENT_CHECK → SMALL_SAMPLE_STRENGTH_OVERREACH | 2 | P-660, P-685 |

Two classes reach three reviews, so prompt 6 routes them to prompt 8 (proposals H-AVAIL-CHAT and H-OWN-EVIDENCE). Both are already forbidden for issued cards by AUDIT-v1; the chats were never checked against it because the linter runs only on repository cards. The P-639 to P-659 package holds 30 further reviews whose verdicts are free text and could not be tallied.

## 4. Learning and models

- **Learning store.** 5,402 events, of which 5,382 are NBA, NHL and MLB backfill. 20 are games the cards covered. It holds 8 team-statistic rows and no availability rows. The cards cover eleven sports and many competitions the store has never seen.
- **Review clocks.** `ml learning-status` counts store results, so it reported 3,716 games "settled since the last review", almost all of them backfilled NBA games. It also ignored the October owner-requested review because its level was written USER_REQUEST (fixed today, [implementation](../framework_change_2026-11-16-1/IMPLEMENTATION.md)).
- **Model lanes.** Three per-league releases, all stale for the current code, none with a frozen game. 29 per-league workshop model folders remain as HISTORICAL_DEVELOPMENT. The owner's rule is one model per sport for any competition; only soccer has that test (POOLED-v1).
- **Card training (CARD-TRAIN-v1, run 2026-11-15-2).** Recalibrating the stated numbers does not improve them (+0.0005 [-0.0016, +0.0026]) and an outcome model adds nothing beyond them (+0.0041 [-0.0004, +0.0086]). The rows hold sport, contract type, rank and p only; none of the research the chats did is captured in a form a model can read.

Dispositions (appended to REVIEW_LOG.csv): ALL — DATA_REPAIR_REQUIRED. Every sport and competition — INSUFFICIENT_EVIDENCE for any model decision; no frozen paired games exist.

## 5. Settlement and sources

- 82 rows on 32 cards are UNRESOLVED. In the latest drop 50 of 325 rows are unresolved and 13 of 26 games rest on one source.
- In that drop 80 of 451 URLs the chats cited were not permitted for their reader or had unchecked access rules, and nine prediction or preview pages were cited for statistics without the exact fields taken.
- Timing in that drop: 41 cards last written before the scheduled start, 22 after it, 12 with no usable clock; none recorded a not-started observation.
- Eight settlement routes were added on 16 November (SRC-RECOVERY-20261116R1); the queue has not been retried with them.

## 6. The framework itself

| Measure | Value |
|---|---|
| Root operating documents | 46 files, 2.0 MB |
| Tracked files | 4,420, of which about 60% are archive or dated verification folders |
| Framework changes since 11 October | 45 folders in 37 days |
| Named versioned controls cited in live documents | 111 (AUDIT-v1, TIMING-v3, SRC-ALT-v3 and so on) |
| Control revisions / prompt versions cited in live documents | 50 / 38 |
| Paragraphs repeated in eight or more documents | 30 |
| CORE.md | 27.7 KB against the "about 16 KB" its own release note gives |

Stale or contradictory current text found: PROMPTS.md named suite v24.14 (current v24.18; fixed today); CURRENT_STATE named the 11 October retrospective as the last one although 16 and 21 October exist (pointer fixed today) and its scoreboard still leads with imports of 13 and 14 October; prompt 6 opens with "this 21-game batch"; the chat upload package (profile, lane briefs, audit supplement) still assigns lanes L1 to L6 although each chat now writes a whole card.

FREEZE-v1 gives the reason this matters: "every cohort so far has been 3 to 16 cards under a different policy, too few to judge any of them". That is still true on 16 November.

## 7. Defects fixed in this run

Four code defects, none of which changes a forecast or a score already recorded: see [IMPLEMENTATION](../framework_change_2026-11-16-1/IMPLEMENTATION.md).

## 8. What this audit does not establish

No predictive advantage, for any sport, contract or method. The band, sport and contract tables are outcome-exposed and were not registered before the results; each is a hypothesis for the next cohort, not a rule.
