# Third external review of 23 November 2026: findings, checks and decisions (v29.4)

The owner passed on a read-only external review of clean `main` at `4d78b5113`. It rated the framework 7.3/10 overall
(recordkeeping and validation 8/10; evidence that it can deliver two winning picks 3/10, a rating of evidence, not a
chance of winning). The owner's instruction was to implement what actually needs implementing. This page records each
finding, what was reproduced here, and what v29.4 did or deferred. Local absolute paths in the review are omitted.

## Reproduced here before acting

| # | Claim | Check | Result |
|---|---|---|---|
| 1 | The shadow decision can pass without issuing a single pair | `SELECTION_SHADOW_PLAN_v1` §4 and `compare` | **Confirmed**: per-pick hit rate with a 50% volume floor; a one-pick-per-card policy qualifies |
| 2 | Confirmatory mode trusts the caller's coverage file and timestamp; a later grade overwrites an earlier one | `selection_shadow.main`, `read_grades` | **Confirmed** on both points |
| 3 | 74.5 and 80.5 are compared although they may be different periods; 130.5 at 0.40 and 180.5 at 0.60 escape | `incoherent_labels` (v29.3, 25% rule) | **Confirmed** on both points |
| 4a | NPB/KBO `+0.5` becomes a two-way winner although those leagues allow ties | `prepare` on an NPB request | **Confirmed**; `RULES_BASEBALL` says tie-permitting leagues never get a two-way winner label |
| 4b | Two different totals (140.5, 145.5) are rejected as duplicates | `prepare` on that text | **Confirmed**: one key per family dropped the second line |
| 4c | A supplied line can vanish from the retained contract rows | `prepare` on "A ML" + "B ML", and "A -3.5" + "B +3.5" | **Confirmed**: the second side's request excerpt was replaced by the first |
| 5 | Over 0.50 / Under 0.36 / push 0.14 is 58.14% given a decision, yet the shadow dropped it as `NO_DIRECTION` | shadow `select` on that card | **Confirmed** |
| 6 | 228/476 required facts observed; all 26 ranked picks carry `UNMEASURED_AVAILABILITY_PRICED` | intake `2026-11-22-2` FACTS and PICKS | Consistent with the 22 November finding; not re-counted field by field |
| 7 | "Australia NBL" and "NBA Cup group stage" reach the generic FIBA prior | `kit_row_note` / `sr_kit.row` | **Confirmed** (already known on 22 November; the packet only warned) |
| 8 | Registered-ranker pairs carry no dependence marker | shadow `select` | **Confirmed** |
| 9 | No frozen league comparator on any registered contract row | request `baseline_id` | **Confirmed**: `UNAVAILABLE:NO_FROZEN_LEAGUE_BASELINE` throughout |
| 10 | Requests arrive within ten minutes of the start; one first-play capture in the inputs | latest score | **Confirmed**: 12 of 13 sealed games await a verified first play |
| — | CURRENT_STATE's manual table says P-696 / P-697 while the generated block says P-703 / P-704; one passage says nothing has been sealed | CURRENT_STATE | **Confirmed** on both points |
| — | 95 distinct capture paths in the competition-route register, 7 present locally | `COMPETITION_ROUTES.csv` `capture_path` | **Confirmed**: 7 of 95; all are temporary or machine folders; every row keeps its `capture_sha256` |

## Implemented in v29.4

No sealed card, the registered rank, the registered score and
[EVALUATION_PLAN_v29.0](../../external/EVALUATION_PLAN_v29.0.md) are unchanged. Intake `2026-11-22-2` (all 13 sealed
cards) rescored with the new code: **0 custody problems**. (Intake `2026-11-22-1` reports 2, both because G0007 was
sealed after that intake was taken, as before.)

- **Contract identity (priority 4).** `forecast_integrity.no_draw`, `winner_by_margin` and `_contract_identity` take the
  competition. Baseball counts as tie-free only in MLB (`TIE_FREE_BASEBALL`). Any other baseball competition is treated
  as tie-permitting, so NPB/KBO `±0.5` stays a handicap at preparation and at registration. In `prepare`, a total's
  key includes its line (two totals become two contracts; the same applies to soccer and cricket totals). Each side of a
  winner or paired spread keeps the excerpt of the line that named it, so every supplied line maps to a retained row.
- **Coherence (priority 3).** Lines are compared only when the registered request gives both the same family, period,
  endpoint, action and unit (`contract_scopes`, from the registered `CONTRACTS.csv`). Within one quantity, any two lines
  are compared, however far apart. With no definitions, nothing is compared, and the check-drop preview says so.
  Intake reads the registered definitions (staging, working tree, then the seal branch); the scorer reads the ones
  verified in the seal. Both therefore compute identical flags, and a test runs intake and score end to end. Team totals
  are not compared, because no registered field names the team.
- **Pair-success selection test (priorities 1, 2, 5, 8).** [SELECT-SHADOW-v2](../../external/SELECTION_SHADOW_PLAN_v2.md)
  replaces v1 before v1 reached any eligible game.
  - The decision is two distinct picks both winning per eligible request, against the registered ranker on the same
    requests, with a pair-coverage floor of 0.5 fixed now.
  - One probability is used throughout: conditional on a decision, with the stated p and the push probability shown
    beside it. The `NO_DIRECTION` flag is no longer used.
  - Confirmatory mode needs a registered score folder with 0 custody problems. It takes that score's eligible sequence
    and seal times, and the plan's publication time from git and GitHub, never from the caller.
  - Conflicting grades stop the run; a missing grade for a pick of an eligible request stops the decision.
  - Every pair, the ranker's included, is marked `SAME_QUANTITY` or `SAME_GAME`.
  - Per-pick, per-slot, both/one/neither and coverage counts are reported.
  - On the 13 development cards the ranker issued both-won pairs on 4/13 requests and SIGNAL on 1/13, matching the
    review's replay.
- **Kit aliases (priority 7, partly).** [KIT_COMPETITION_ALIASES.csv](../../one_chat/KIT_COMPETITION_ALIASES.csv)
  holds six reviewed aliases (for example, Australia NBL and NBA Cup group stage), each with its basis. The packet now
  names the exact row to pass to the kit and print on the card. The kit's own lookup and parameters are unchanged: kit
  and rank stay frozen until v30.0.
- **Current state.** The manual P-696 / P-697 rows are replaced by a pointer to the generated block. The undated "0
  qualifying games" and "nothing sealed" sentences are dated or pointed at the scorer.

Tests: `ml/tests/test_v29_2_review_fixes.py` and `ml/tests/test_v29_2_request_shape.py` (coherence by registered
quantity, intake–score consistency, kit aliases, the shadow v2 decision, the 50/36/14 case, conflicting and missing
grades, pair markers, two totals, and NPB/KBO/MLB run lines).

## Not implemented now, with reasons

| Item | Why not now | Where it goes |
|---|---|---|
| 6. Missing facts (lineups, opponent-adjusted strength, rest, travel) | This is data collection on future cards, not code. The fields already exist and the cards leave them blank. | v30.0 kit and card work |
| 7. Resolving competition inside the kit calculation | Kit and rank are frozen until v30.0. The packet now names the row, which removes the ambiguity at the operator. | v30.0: move `KIT_COMPETITION_ALIASES.csv` into `sr_kit.row` and save the row used |
| 8. Joint both-win / one-win / neither probabilities | Needs a scenario model and later games to validate it. The pair markers now record dependence for every pair. | Research, tested under its own registration |
| 9. Frozen league comparator | 5,382 of 5,402 learning-store events are NBA, NHL or MLB. A comparator for the other competitions would be thin and would need freezing before use. | v30.0, starting with competitions that have frequent requests and reliable data |
| 10. Timing evidence | Operational: requests arrive late, and first-play captures are collected at settlement. Late requests stay allowed (owner, 22 November). | Settlement checklist: capture the official actual start separately from the final score |
| Capture paths | The raw bytes of 88 captures sat in cleared temporary folders and cannot be recovered; their hashes are preserved. Raw third-party pages are not committed to this public repository. | Owner decision on a durable capture store indexed by hash; new captures already go beside the repository by run |
| Recalibration and promotion | The review agrees they stay in research. Stated p beat pooled and per-sport recalibration on the walk-forward rows. | No change (ML-SEP-v1) |
| Additional sporting factors | A list to test one at a time on later games, not a defect. | Research backlog |
