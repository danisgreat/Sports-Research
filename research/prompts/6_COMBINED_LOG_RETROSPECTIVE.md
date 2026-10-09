# PROMPT 6 — COMPREHENSIVE RETROSPECTIVE OF THE COMBINED LOG

**Run by:** Claude Code in a local checkout of the repository · **GitHub:** write (report folder only) · **Mode:** `COHORT_RETROSPECTIVE`

Run this once enough cards are settled to learn from. The rule of thumb is at least **30 newly settled cards** since the last retrospective, or whenever the user asks. The retrospective measures, explains and recommends. It does **not** change rules, models, forecasts, grades or prompts. Every recommendation stays `PROPOSED_NOT_TESTED` until the user approves its implementation.

---

## 1. Authority and scope

1. Check out the current `main` and record its HEAD SHA.
2. Read:
   - `CURRENT_STATE.md`, `METHOD.md`, `CURRENT_RULES.md` (Rules T2, R1, P4) and `SCORING_AND_VALIDATION.md` (SCV-2026.10.09-v4);
   - `FRAMEWORK_RETROSPECTIVE_2026-10-09.md` (the recommendation register, its implementation-status table and the failure-class baseline);
   - `runtime/config/selection_rules.json` (the provisional Rank-1 gate) and `research/experiment_measures.json` with `research/experiments/cross_card_v1.json` (the pre-registered prospective experiments XCARD-1..6 and SEL-1);
   - the most recent earlier retrospective, if any (`research/verification/retrospective_*/`).
3. Fix the scope before you look at results:
   - **New cohort:** from the first card after the last retrospective, through the highest settled ID.
   - **Comparison cohort:** everything before that.

   Write both ranges down first, so the analysis cannot drift toward a convenient window.

## 2. Generate the scoreboard (deterministic)

```powershell
$O = "research/verification/retrospective_<YYYY-MM-DD>"
py -3.14 -B -m research.operations.cohort_review --out "$O/new"        --from <first new ID> --to <last ID>
py -3.14 -B -m research.operations.cohort_review --out "$O/comparison" --to <last comparison ID>
py -3.14 -B -m research.operations.cohort_review --out "$O/all"
```

`cohort_review` reads every retained `settlement_table.json`:
- the final-settlement and mini-import tables;
- for each ID, only the latest settlement;
- never `PENDING_EVENT` records.

It reports, under Rule T2:
- counted wins over live top-two rows, with Wilson 95% CIs;
- card classes;
- Rank-1, Rank-2 and ranks-3+ win rates side by side;
- results by sport and by Rank-1 proposition family;
- Rank-1 failure classes, normalised to the taxonomy;
- evidence-grade counts;
- a calibration table of every stated `p_card`, with Brier score, log loss and skill against climatology.

Do not hand-edit the generated files.

Then regenerate and check the rolling scoreboard, which is the standing view of the same data:

```powershell
py -3.14 -B -m research.operations.scoreboard publish
py -3.14 -B -m research.operations.scoreboard verify
py -3.14 -B -m research.experiments.cross_card verify
py -3.14 -B -m research.experiments.cross_card power --delta <effect> --sd <sd> --rows-per-week <n>
```

The scoreboard reports three cohorts that are never mixed: `COUNTED` (Rank 1 passed the gate), `RANK1_UNSTABLE` (own cohort) and informational ranks 3–4. `cross_card power` states how many weeks an effect of a given size needs at the observed rows per week (use each pre-registered experiment's own effect and SD from `cross_card_v1.json`). Run `current_state write` if the settled range changed the next ID or the active log.

Spot-check five random IDs against their settlement addenda in the Combined Log. If any number disagrees, stop and fix the source table through the supported import. Never patch the report.

## 3. Quantitative analysis

Answer each question with numbers and intervals. Mark a conclusion as established only when the interval supports it; otherwise write `INSUFFICIENT_EVIDENCE` and the sample size needed.

1. **Headline.** What are the counted win rate and its CI in the new cohort, compared with the comparison cohort? Are the Rank-1 and Rank-2 rates individually better than the 2026-10-09 baseline (Rank 1 40–28, 58.8%; Rank 2 39–27, 59.1%)?
2. **Does each slot carry information?** Rank 1 should beat Rank 2, and Rank 2 should beat ranks 3+. If not, ranking is not separating propositions. Say so plainly.
3. **Calibration.** Within each p bin, does the stated `p_card` match the win rate? Report the generated least-squares reliability line (win = a + b·p; perfect calibration is a = 0, b = 1) and the Brier skill score. An over-confident pattern (high bins under-performing) is the single most important finding to report.
4. **Joint failure.** Did `TOP2_ALL_LOST` happen more often than the cards' stated `P(Rank 1 and Rank 2 both lose)`? Compare the mean stated joint failure with the realised all-lost share and its CI (generated section *Joint top-two failure*).
5. **Stability gates.** How did `RANK1_UNSTABLE` cards perform compared with `PASS` cards (generated section *Rank-1 stability gate*, and the scoreboard's two cohorts)? Cards issued before the gate used the legacy cut (Rank 1 < 60%); the gate for new `mini-log-3` cards is p_card ≥ 62% with a margin of at least 4 points over the best non-complementary alternative. State whether the data so far supports keeping, tightening or relaxing those numbers, and whether the prospective window for experiment SEL-1 (8 or more weeks) has completed; until it has, the gate stays provisional and you do not change it.
6. **By sport and family.** Which sport × family cells are reliably below 50% at Rank 1, with enough n? Which are reliably strong?
7. **Failure classes.** What are the counts and their change from the baseline? Is any class still recurring after its proposed correction?
8. **Evidence quality.** What share of rows was settled on C, E, OP or X? Does the result change if C/E rows are excluded (sensitivity)?
9. **Process.** Count the R9/R10 `Process: DEFICIENT` cards by deficiency, and compare their results with sound-process cards.

10. **New-format checks (cards from the first `mini-log-3` mini).** Share of cards with `ADJUSTMENT_DEPENDENT`, and their results; share with a regime flag and whether the register's multiplier was applied; share with `Evidence snapshots: NONE`; share of settlements on evidence C/E/OP/X by provider; number of SLA breaches (`settlement_sla`); and whether any Rank-1 loss class in `TENNIS_IID_UNDERDISPERSION`, `FIRST_HALF_GOAL_OVERSELECTION` or `RUNLINE_CUSHION_CEILING` recurred after the family rules took effect.
11. **Runtime evidence.** Re-read `research/model_builds/runtime_h0/INDEX.json` and `challenger/INDEX.json`. Report which engines beat the baseline, and do not promote any engine on that evidence alone: promotion needs the EVL-02 gate (week-block bootstrap, calibration-slope interval containing 1, seed stability, power) on prospective cards.

Complementary rows on one card are dependent outcomes. Never treat four rows of one card as four independent trials. Use cards or slot-level rates as the unit of analysis.

## 4. Qualitative analysis of the deep retrospections

Read every Rank-1 deep retrospection in the new cohort; they are settlement addenda in the Combined Log. For each failure class with two or more cases:
- name the shared mechanism;
- say whether it was knowable before the cutoff;
- identify which card section, sport block or tool should have caught it.

Also read a matched sample of Rank-1 **wins**, to find what worked and must be kept.

## 5. Review the recommendation register

For each recommendation in `FRAMEWORK_RETROSPECTIVE_2026-10-09.md` §5 (start from its implementation-status table), and in any later retrospective, record its status:
- `IMPLEMENTED`, with a pointer to the commit or file;
- `PARTLY_IMPLEMENTED`;
- `NOT_IMPLEMENTED`;
- `NOT_MET_OFFLINE` (the tooling exists but the acceptance test needs data, web access or time the implementation could not supply);
- `SUPERSEDED`.

For each one that is implemented, test it against its own stated acceptance test using the new cohort where possible. Report the result as `MET`, `NOT_MET` or `INSUFFICIENT_EVIDENCE`.

## 6. Recommendations

Write new or revised recommendations in the register format: `ID · Priority (P0–P3) · Addresses (finding or failure class) · Recommendation · Acceptance test · Effort`.

Each recommendation needs:
- a pre-registered, falsifiable acceptance test with a minimum sample size;
- a rollback condition.

Prefer changes to:
1. the distribution model;
2. the candidate and ranking rule;
3. the source and settlement process;

in that order. Never prefer narrative heuristics.

Every recommendation is `PROPOSED_NOT_TESTED`.

## 7. Write the report

Write the report to `$O/RETROSPECTIVE_REPORT.md` with these sections:
1. Scope, ranges, HEAD and data sources (the three generated cohort folders).
2. Executive summary: five findings and five recommendations, each with its number and interval.
3. Quantitative analysis (section 3 above, one subsection per question).
4. Failure-class and mechanism analysis (section 4).
5. What worked.
6. Recommendation register status (section 5).
7. New recommendations (section 6).
8. Limits: the sample sizes, dependence between rows, evidence-grade mix, and that the cards are uncalibrated analyst scenarios rather than certified performance.

Write only inside `$O/` (an append store excluded from the control freeze, so no new manifest is needed), plus the regenerated `research/scoreboard/SCOREBOARD.*` and `CURRENT_STATE.md` (both generated and also excluded). Do not edit root documents. If the user wants a root-level pointer, it needs a new control manifest (prompt 5, step 5).

## 8. Verify and publish

```powershell
py -3.14 -B -m research.operations.log_card verify
py -3.14 -B -m research.operations.control_freeze --verify
git status
```

The ledger, the Combined Logs and every controlled file must be unchanged, and only `$O/` may be new. Commit with a message such as `Add cohort retrospective <date> (P-AAA–P-BBB)` and push without force.

## 9. Report

```text
HEAD:
New cohort: <range> (<n> cards) · Comparison cohort: <range> (<n> cards)
Counted (new): <w>/<n> = <x.x%> [CI] · (comparison): <w>/<n> = <x.x%> [CI]
Rank 1 / Rank 2 / Ranks 3+ (new): <rates with CIs>
Calibration (new): Brier <x>, skill <x>, slope <x>, intercept <x>
Mean stated joint failure vs realised all-lost share: <x%> vs <y%>
Top failure classes (new): <class × n>
Recommendations: <n new> · register items implemented <n> / met <n>
Report: research/verification/retrospective_<date>/RETROSPECTIVE_REPORT.md
Controlled files changed: NO · Commit SHA:
```
