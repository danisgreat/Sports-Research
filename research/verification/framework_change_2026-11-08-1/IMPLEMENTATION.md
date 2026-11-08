# Framework change 2026-11-08-1 — owner decisions and competition rules (v24.4 / CR-2026.11.08-R1)

**Owner instructions, 8 November 2026**, answering the four items left open by [CR-2026.11.07-R3](../framework_change_2026-11-07-3/CONTRADICTIONS.md) §4:

1. "do comprehensive research on them to see if they can improve the accuracy of predictions and see if this is still necessary and include/exclude them accordingly" (regime multipliers);
2. "do the same for number 1 and do accordingly" (the external-chat route);
3. "keep it as a separate contributor, dont let it add to the main prediction calculation" (the decision lab);
4. "Yes I still require it, in fact i need it if the top spread/moneyline and top over/under prediction loses, and it has to be a deep and comprehensive review, that is brutally honest and accurate and comprehensive" (the loss review);
5. "Re-verify the sports rules for each competition in each sport that has been covered through the game logs, and make the necessary changes to the files."

**Class.** STATISTICAL (new effect-table rows move card numbers in four regimes) + PROCEDURE (route, firewall, review, rules). Versions: method **MDS-2026.11.08-v24.4**, control **CR-2026.11.08-R1**, prompt suite **P-2026.11.08-v24.2** (prompts 3 and 6 changed, external requests removed). No issued card, grade, ID or settled record is changed.

## 1. Regime multipliers (REGIME-v2)

Study: [regime_study/REGIME_STUDY.md](regime_study/REGIME_STUDY.md).

**Method.** Each archive multiplier was tested against a walk-forward replication of the reference on verified finals:
- NBA: the repository's 2020-21 to 2025-26 store;
- MLB: MLB Stats API, 2021–2026;
- AFL: AFL Tables, 2015–2026;
- NRL: Rugby League Project, 2021–2026.

Each held-out season's multiplier was fitted on the other seasons only, and the paired CRPS and Brier were bootstrapped by season.

**Result.** The raw archive ratios were the wrong quantity. What a card needs is the reference's own bias in the regime.

| Decision | Rows |
|---|---|
| Included at full size (`MEASURED_CONFIRMED`) | NBA playoffs −4.5%; MLB postseason −10.9%; NRL first 28 days −2.5% |
| Included at half size (`MEASURED_NOT_CONFIRMED`) | AFL finals −3.2% |
| Excluded (`MEASURED_NULL`) | NBA, MLB and AFL early season; NRL finals. The NBA early-season 0.988 made every window worse |
| Not measurable here (`NOT_ESTIMATED`, scenario only) | NHL (one verified season; the NHL API disallows Anthropic agents); NFL (no permitted bulk source) |
| Retired | NRL six-again |

**Files changed:**
- [EFFECT_TABLES.csv](../../effect_tables/EFFECT_TABLES.csv): 11 rows;
- [RULES_REFERENCE](../../../RULES_REFERENCE.md#part-b-selection_rules) Part B §6 (REGIME-v2);
- [PARAMETERS](../../../PARAMETERS.md#part-b-effect_tables) Part B §4 and Part C (tested table).

**Finding left for prompt 8.** The reference itself under-forecasts NRL totals by 5.5% after day 28 and over-forecasts AFL totals by 1.7%. This is a calibration matter for the reference, not a regime effect, and it waits for STATFREEZE-v1.

## 2. External-chat route

**Question.** Does the outside-chat route make predictions more accurate, and is it still needed?

**Evidence from the repository's own records:**
- **Accuracy.** On paired rows, external-chat cards did not beat the frozen league baseline. The card-minus-baseline Brier differences were:
  - P-581–P-582: −0.0007 on 4 rows (13 October scoreboard);
  - P-585–P-589: +0.022 on 10 rows (14 October);
  - P-612–P-622: +0.024 on 8 rows ([retrospective 2026-10-21](../retrospective_2026-10-21/RETROSPECTIVE_REPORT.md)).
  The research-only P-601–P-611 rows scored an MSE of 0.2429, close to a coin flip.
- **Verifiable timing.** None of the 11 recent primary cards had a verifiable pre-start issue time, because chat delivery clocks are not captured (retrospective F-08).
- **Learning data.** Chats cannot save or hash captures, so their prior-game and availability tables cannot become learning data (F-10).
- **Settlement.** The P-606 score error came from a recap-video title (F-01).
- **References.** Chats hand-compute the reference (`:HAND`) and cannot run the linter, the freeze or a simulator.
- **Workload.** The route needed 211 KB of request text kept in step with every rule change; it still named the retired SELECTION_RULES file.
- **What it offered.** Nothing the repository route lacks. The repository agent has the same internet research and runs the code.

**Decision (REQ-v3).** The route is retired and its files are archived unchanged in [archive/retired_2026-11-08/](../../../archive/retired_2026-11-08/):
- `research/prompts/external_requests/` (11 requests and their README);
- GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md;
- GITHUB_REFERENCE_PROTOCOL.md.

REF-v1's operative rule (read an unreadable local file from `main` at a printed SHA) is kept as REF-v2 in [WORKFLOW](../../../WORKFLOW.md#part-a-execution_environment_protocol) Part A §2. Text the owner brings from a chat is an owner-supplied research note: it is copied byte for byte, every fact is re-opened before use, and it is never issued or scored as a card. The moved paths and their hashes are in [HISTORICAL_LINK_INDEX](../../../HISTORICAL_LINK_INDEX.md). Every banner and link in live documents was repointed.

## 3. Decision lab (DECISION-LAB-v2)

The decision lab is kept as a **separate contributor** that never adds to the main prediction ([RULES_REFERENCE](../../../RULES_REFERENCE.md#5-sources-event-state-and-time) Part A §5a):
- Its aggregate results live only in `research/model_shadow/DECISION_LAB/`.
- Nothing it produces enters the reference, an adjustment or effect-table row, p_card, the picks, ranks, widths, grades, learning data or releases.

New test, [test_decision_firewall.py](../../../ml/tests/test_decision_firewall.py), enforces this:
- only the run-all orchestrator's `run_decision_lab` may import `ml.decision`;
- no module on the forecast path may import the lab, its orchestrator or its writer;
- only the writers may name the lab's output folder.

## 4. Deep loss review (DEEPLOSS-v1)

[RULES_REFERENCE](../../../RULES_REFERENCE.md#3-rule-r1-outcome-review-without-hindsight) Part A §3, prompt 3 §3 and the template in [CARD_AND_LOG_TEMPLATES](../../../CARD_AND_LOG_TEMPLATES.md) §6 now require one deep review for each losing row of:
- the **top side** (the highest final-p winner, moneyline or spread row on the full game);
- the **top total** (the highest final-p full-game over/under);
- **rank 1**, when it is neither.

A joint section is added when the side and the total both lose.

The 14 sections are:
1. claim;
2. verified outcome;
3. distribution check, with the card against its reference and baseline;
4. error decomposition;
5. fact-by-fact research audit;
6. what decided the game, in numbers;
7. knowable at the cutoff;
8. process audit;
9. a plain verdict (ERROR, MODEL_LIMIT, VARIANCE or MIXED), including whether the pick should have been made;
10. a cutoff-only counterfactual;
11. failure class and its recurrence;
12. a testable correction;
13. matched wins;
14. an honesty checklist.

"Variance" is allowed only with numbers that show it. Check S8 enforces the review. Prompt 6 tallies verdicts and routes any failure class seen three or more times to prompt 8. Records settled before 8 November are not reopened.

## 5. Competition rules

All competitions in the game logs were re-verified for the rules that change a card or its settlement ([COMPETITION_RULES_VERIFICATION.md](COMPETITION_RULES_VERIFICATION.md)). The files now carry dated registers: basketball §9.5a, ice hockey §9.5a and soccer §8a, plus review notes in every other sport file.

| Status | Competitions |
|---|---|
| Changed | FIBA rules 2026; the NBA Cup; NBL27; B.League; KBL; the EuroCup; Greece's GBL; the NHL's 84-game season; Liiga; Belgium (no play-offs); J1 (August–June); the ISL; the Leagues Cup; MLS NEXT Pro; the IFAB Laws; the CFL (no ties); the ICC and MCC Laws; World Rugby's 20-minute red card |
| `CONFLICT` | Liga MX Apertura 2026 play-in; Czech Extraliga format |
| `NOT_RE_VERIFIED` | Mostly minor leagues, plus the AHL, Denmark, Argentina and Asia's club competitions, with rule G2 to apply before their next card |

## 6. Versions and other files

- **Version tags.** CORE, README, PROMPTS, CURRENT_STATE (method, control and suite rows, release paragraph), CHANGELOG, every prompt (suite tag) and [DEPENDENCY_MAP](../../prompts/DEPENDENCY_MAP.md) (regenerated).
- **Memory.** Not part of the repository.

## 7. Verification

- The full test suite was run before the commit (result in the commit message).
- Link check: no new broken links in live documents.
- Every edit script asserted exactly one match per replacement and LF line endings.
