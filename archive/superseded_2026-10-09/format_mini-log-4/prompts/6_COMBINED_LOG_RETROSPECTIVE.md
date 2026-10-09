# PROMPT 6 — COMPREHENSIVE RETROSPECTIVE OF THE COMBINED LOG

**Run by:** Claude Code in a local checkout of the repository · **GitHub:** write (report folder, scoreboard and state only) · **Mode:** `COHORT_RETROSPECTIVE`

Run this once enough cards are settled to learn from: at least **30 newly settled cards** since the last retrospective, or whenever the user asks. The retrospective measures, explains and recommends. It does **not** change rules, models, forecasts, grades or prompts. Every recommendation stays `PROPOSED_NOT_TESTED` until the user approves its implementation. All counting is done by hand from the settled tables, with the arithmetic shown; there is no cohort program.

---

## 0. Reading gate

Print the **reading receipt** ([research/prompts/README.md](README.md)) after opening: [CURRENT_STATE.md](../../CURRENT_STATE.md), [METHOD.md](../../METHOD.md), [CURRENT_RULES.md](../../CURRENT_RULES.md) (T2, R1, P4), [SELECTION_RULES.md](../../SELECTION_RULES.md) (all), [SCORING_AND_VALIDATION.md](../../SCORING_AND_VALIDATION.md) (all), [HYPOTHESIS_REGISTER.md](../../HYPOTHESIS_REGISTER.md), [FRAMEWORK_RETROSPECTIVE_2026-10-09.md](../../FRAMEWORK_RETROSPECTIVE_2026-10-09.md) (the recommendation register, its implementation-status table and the failure-class baseline), [LEAGUE_PROFILES.md](../../LEAGUE_PROFILES.md), [ARCHIVE_USE_GUIDE.md](../../ARCHIVE_USE_GUIDE.md) §6, [research/scoreboard/SCOREBOARD.md](../../research/scoreboard/SCOREBOARD.md) and the most recent earlier retrospective (`research/verification/retrospective_*/`), if any.

## 1. Authority and scope

1. Check out the current `main`, record its HEAD SHA, and confirm `git status` is clean in the paths you will write.
2. Fix the scope **before you look at results**, and write it down:
   - **New cohort:** from the first card after the last retrospective, through the highest settled ID.
   - **Comparison cohort:** everything before that.

   This keeps the analysis from drifting toward a convenient window.
3. Gather the data: for each ID in scope, the latest settlement block in the Combined Logs (search `Final settlement` and `BEGIN SETTLEMENT` blocks, or the settled-mini import folders under `research/verification/mini_import_*` and `final_settlement_*`). Never use a `PENDING_EVENT` record. For each ID use only the latest settlement. List the IDs and the file and line of the block you used in `$O/DATA_INVENTORY.md`.

   Let `$O` be `research/verification/retrospective_<YYYY-MM-DD>`.

## 2. Build the tables (by hand, with the arithmetic shown)

Create `$O/COHORT_TABLES.md`, one table per cohort (new, comparison, all), from the settlement blocks. Do not hand-edit numbers after you build them; rebuild from the blocks.

For each cohort report, under Rule T2:
- counted wins over live top-two rows, with the Wilson 95% interval (SCORING_AND_VALIDATION §3);
- card classes: all won, split, all lost, void;
- Rank-1, Rank-2 and ranks-3+ win rates side by side;
- results by sport and by Rank-1 proposition family;
- Rank-1 failure classes, normalised to the SELECTION_RULES §8 taxonomy (aliases mapped);
- evidence-grade counts (A, B, C, E, OP, X);
- the calibration table of every stated `p_card` (SCORING_AND_VALIDATION §4) with Brier score and skill against climatology;
- the joint-failure comparison: mean stated P(both lose) against the realised `TOP2_ALL_LOST` share and its Wilson interval.

Then update the rolling scoreboard (SCORING_AND_VALIDATION §7): the `COUNTED` (gate passed), `RANK1_UNSTABLE`, `LEGACY_P_ONLY` and `UNKNOWN_GATE` cohorts are never mixed; ranks 3 and 4 never count. Update CURRENT_STATE with the headline numbers.

Spot-check five random IDs against their settlement blocks. If any number disagrees, fix your table from the source block; never edit a settlement.

## 3. Quantitative analysis

Answer each question with numbers and intervals. Mark a conclusion as established only when the interval supports it; otherwise write `INSUFFICIENT_EVIDENCE` and the sample size needed (HYPOTHESIS_REGISTER describes the week-block test for comparisons).

1. **Headline.** Counted win rate and its interval in the new cohort against the comparison cohort. Are Rank 1 and Rank 2 individually better than the 2026-10-09 baseline (Rank 1 40-28, 58.8%; Rank 2 39-27, 59.1%)?
2. **Does each slot carry information?** Rank 1 should beat Rank 2, and Rank 2 should beat ranks 3+. If not, ranking is not separating propositions. Say so plainly.
3. **Calibration.** Within each `p_card` bin, does the stated probability match the win rate? An over-confident pattern (high bins under-performing) is the single most important finding to report.
4. **Joint failure.** Did `TOP2_ALL_LOST` happen more often than the cards' stated `P(Rank 1 and Rank 2 both lose)`?
5. **Stability gates.** How did `RANK1_UNSTABLE` cards perform against `PASS` cards? The gate for `mini-log-3` and `mini-log-4` cards is `p_card` at least 62% with a lead of at least 4 points; cards before it used the legacy 60% cut. State whether the data so far supports keeping, tightening or relaxing the numbers, and whether the 8-week window of experiment SEL-1 is complete. Until it is, the gate stays provisional and you do not change it.
6. **By sport and family.** Which sport × family cells are reliably below 50% at Rank 1 with enough n? Which are strong?
7. **Failure classes.** Counts, and their change from the baseline. Is any class still recurring after its proposed correction?
8. **Evidence quality.** The share of rows settled on C, E, OP or X. Does the result change if C and E rows are excluded?
9. **Process.** Count the R9/R10 `Process: DEFICIENT` cards by deficiency, and compare their results with sound-process cards.
10. **New-format checks (cards from the first `mini-log-3` or `mini-log-4` mini).** Share of cards with `ADJUSTMENT_DEPENDENT` and their results; share with a regime flag and whether the multiplier was applied; share with `Evidence quotes: NONE`; evidence mix by provider; SLA breaches; whether any `TENNIS_IID_UNDERDISPERSION`, `FIRST_HALF_GOAL_OVERSELECTION` or `RUNLINE_CUSHION_CEILING` loss recurred after the family rules took effect.
11. **Rules, sources and past results used.** For each card in the new cohort, did `Rules read` name the sport file, the SELECTION_RULES sections and the SOURCES route? Did `Archive check` show files and rows, or `ARCHIVE_UNAVAILABLE`? Compare results between cards with a real archive check and cards without one. For each sport compare the cohort's realised rates (home-win share, overtime share, one-run share, total SD) with the LEAGUE_PROFILES row and the archive; report gaps and any profile more than one season old.
12. **Fitted models.** None exist. State that, and list the XCARD experiments in HYPOTHESIS_REGISTER with their current row counts against the rows required.

Complementary rows on one card are dependent outcomes. Never treat four rows of one card as four independent trials. Use cards or slot-level rates as the unit of analysis.

## 4. Qualitative analysis of the deep retrospections

Read every Rank-1 deep retrospection in the new cohort (the settlement blocks in the Combined Log). For each failure class with two or more cases: name the shared mechanism; say whether it was knowable before the cutoff; identify which card section, sport block, rule, source route or archive file should have caught it. Read a matched sample of Rank-1 **wins** to find what worked and must be kept.

## 5. Review the recommendation register

For each recommendation in FRAMEWORK_RETROSPECTIVE_2026-10-09.md §5 (start from its implementation-status table) and in any later retrospective, record its status: `IMPLEMENTED` (with a pointer to the commit or file), `PARTLY_IMPLEMENTED`, `NOT_IMPLEMENTED`, `NOT_MET_OFFLINE`, `SUPERSEDED`, or **`SUSPENDED_MD_ONLY`** (it needed the removed runtime, tools or CI). For each one that is implemented, test it against its own acceptance test using the new cohort where possible and report `MET`, `NOT_MET` or `INSUFFICIENT_EVIDENCE`.

## 6. Recommendations

Write new or revised recommendations in the register format: `ID · Priority (P0 to P3) · Addresses (finding or failure class) · Recommendation · Acceptance test · Effort`. Each needs a pre-registered, falsifiable acceptance test with a minimum sample, and a rollback condition. Prefer changes to (1) the distribution method, (2) the candidate and ranking rule, (3) the source and settlement process, in that order; never to narrative heuristics. Every recommendation is `PROPOSED_NOT_TESTED`, and each is also added to [HYPOTHESIS_REGISTER.md](../../HYPOTHESIS_REGISTER.md) under a dated heading.

## 7. Write the report

Write `$O/RETROSPECTIVE_REPORT.md` with these sections:
1. Scope, ranges, HEAD and data sources (`DATA_INVENTORY.md`, `COHORT_TABLES.md`).
2. Executive summary: five findings and five recommendations, each with its number and interval.
3. Quantitative analysis (section 3, one subsection per question).
4. Failure-class and mechanism analysis (section 4).
5. What worked.
6. Recommendation register status (section 5).
7. New recommendations (section 6).
8. Limits: the sample sizes, dependence between rows, evidence-grade mix, and that the cards are uncalibrated analyst scenarios rather than certified performance.

Write only inside `$O/`, plus the updated `research/scoreboard/SCOREBOARD.md`, `CURRENT_STATE.md`, the dated section of `HYPOTHESIS_REGISTER.md` and a `CHANGELOG.md` entry. Do not edit rules, prompts, the Combined Logs or any issued card text. If the user wants a rule or prompt change, that is prompt 8.

## 8. Verify and publish

Run [VERIFICATION_PROTOCOL.md](../../VERIFICATION_PROTOCOL.md) §5 and print the evidence: scope written first; five random numbers recomputed from the blocks; `git status` shows only the allowed paths; `git diff --numstat` on the Combined Logs is empty. Commit with a message such as `Add cohort retrospective <date> (P-AAA–P-BBB)` and push without force.

## 9. Report

```text
READING RECEIPT: <as printed>
HEAD:
New cohort: <range> (<n> cards) · Comparison cohort: <range> (<n> cards)
Counted (new): <w>/<n> = <x.x%> [CI] · (comparison): <w>/<n> = <x.x%> [CI]
Rank 1 / Rank 2 / Ranks 3+ (new): <rates with CIs>
Calibration (new): Brier <x>, skill <x>
Mean stated joint failure vs realised all-lost share: <x%> vs <y%>
Top failure classes (new): <class × n>
Archive check coverage (new): <n with files / n total> · profile gaps: <list>
Recommendations: <n new> · register items implemented <n> / met <n> / suspended <n>
Report: research/verification/retrospective_<date>/RETROSPECTIVE_REPORT.md
Rules, prompts, logs changed: NO · Commit SHA:
```
