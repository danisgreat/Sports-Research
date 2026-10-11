# Change proposal: prompts 1–8 and the learning workflow

Date: 2026-10-11 (Australia/Sydney). Base: `2d6d86350ce4d6bd9f4ae0f34a42351e71ff0e4b`, local main and fetched origin/main aligned, worktree clean before this change.

## Authority and scope

User instructions, verbatim:

> carefully review the prompts from 1-8 and provide a fully improved version of them so that the best versions are used to get the best mini log, combined log, individual game log and prediction outcomes

> Replace the active prompts and align their supporting rules

> ALSO HAVE A LOOK AT THE MOST RECENT RETROSPECTIVE AND LEARNINGS PUBLISHED, AND PROVIDE AN IMPLEMENTATION DOCUMENT FOR THE BEST RECOMMENDATIONS, INCLUDE AS MANY OF THEM IF NEEDED

The user also explicitly invoked prompt 8, including scoped commit and push to main. This authorizes a document/procedure/format change and publication. It does not establish predictive skill or authorize retrospective forecast edits. No new event, settlement, archive dataset, fitted model or runtime is created.

## Evidence and defects

Read all eight operating prompts, their README, CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, SCORING_AND_VALIDATION, VERIFICATION_PROTOCOL, HYPOTHESIS_REGISTER, CONTRIBUTING and the latest three changelog entries. Also read the October 11 retrospective, the October 9 recommendation register, current learning-index/register guidance, source/profile/archive instructions and the live log header/status.

The [latest retrospective](../retrospective_2026-10-11/RETROSPECTIVE_REPORT.md) reports 20 new cards, 34/40 top-two wins, one ISO week, 0 gate passes, 20 mechanically protected pairs and 0 paired baseline rows. Those are reported audit findings, not a new independent outcome audit. Its in-sample climatology comparison cannot establish out-of-sample skill. Its four losses do not establish overconfidence; no numeric causal blame shares are identifiable from these games.

| Defect | Evidence | Remedy |
|---|---|---|
| Prompt 1's common core is buried in prompt 2 | Old prompts 1 and 2 | Put the complete game workflow in prompt 1 |
| Rank-by-probability conflicts with minimise-joint-failure Rank 2 | Old prompt 2 A5; selection §§2–3 | Deterministic primary probability ordering; diversification and different-quantity rules are separate shadows |
| Forced four numeric rows contradict qualitative research permission | Old prompt 2 A4/A6; CURRENT_RULES §6 | Up to four supported candidates; explicit qualitative/NO_FORECAST states |
| Missing evidence forced to VOID | Old prompt 3 §5 and templates S4 | UNRESOLVED for missing evidence; VOID only for a frozen rule |
| Opening header required to equal today's next ID | Prompts 2/4/5; Part 7 opening P-549/P-550 versus current P-579/P-580 | Treat opening header as historical; reconcile state, status and actual canonical entries |
| Three-card spot check described as faithful import | Prompt 4 §5 | Verify all imported card cores, addenda and settlements; resumable block map |
| Late input, baseline and adjustment gaps | RET-02, RET-05, P-568 discussion | Actual issue time, late cohort, frozen baseline, any-size rank-flip disclosure |
| Statistical shortcuts | Scoring §§1/4/5; RET acceptance rules | Historical climatology labelled descriptive; event/week comparisons; no inference from a CI merely containing the ideal |
| Archive false certainty | Prompt 7 line count; stale header-only assertions in sport blocks | Logical CSV records, current inspection, coverage and field provenance |
| Prompt 6 write scope disagrees with verification §5 | Old retrospective prompt and protocol | One explicit write scope; preserve dated reports |

## Change and acceptance

Class: procedure + format + scoring-definition clarification + prompt. Release: MDS-2026.10.11-v10.0 / CR-2026.10.11-R1 / SCV-2026.10.11-v6 / SEL-2026.10.11-v2; new `mini-log-6`, `mini-settlement-5`, retained `canonical-md-1` wrapper. Historical formats remain intact and receive only dated compatible addenda.

Immediate acceptance: all eight tasks have inputs, authority, write scope, steps, missing-evidence behavior, readback checks and deliverables; examples exercise supported and missing-data cases; rank, probability, baseline, settlement and ID rules agree; local links introduced here resolve; no issued log/data/report bytes change; archived originals equal the base files; only intended Markdown is staged. No statistical outcome test is claimed complete.

Hypotheses and future acceptance are registered as FC10/RET revisions in HYPOTHESIS_REGISTER. The implementation roadmap distinguishes implemented document controls, untested shadows, pending data repairs and suspended software work. Failure of document checks blocks this release; future model/selection changes need the separate pre-registered evidence. Rollback is a new forward document revision, never a rewrite of issued cards or git history.
