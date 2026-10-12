# PROMPT 8 — Improve rules, prompts and formats with a reviewable implementation

**Mode:** FRAMEWORK_CHANGE. Run by Claude Code/Codex in the local repository. **Writes:** declared Markdown documents, preserved prior text, templates/examples and a new verification/implementation folder. No code, JSON, notebooks, workflows or fitted-model claims. Publication is included when this full prompt is invoked unless the user specifies local-only.

Inputs: `<requested problem/change>`; `<relevant retrospective/learning references, or discover latest completed published ones>`; `<write constraints>`. Carry the authorized change through implementation, verification and publication; do not stop at a generic recommendation list.

## 1. Read current authority and latest learning

Print the [reading receipt](README.md) after CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, SCORING_AND_VALIDATION, VERIFICATION_PROTOCOL, HYPOTHESIS_REGISTER, CONTRIBUTING, the latest three CHANGELOG entries, all affected prompts/dependencies, latest completed retrospective and relevant learning-register entries. Inspect cwd/branch/HEAD/status, fetch publication state without overwriting local work, and record the exact source revision.

Read what is currently implemented, not just old status labels. An archived runtime test is not a current capability. Distinguish retrospective reported results from any independently recomputed evidence. Read raw supporting tables when a proposed change depends on a number; disclose gaps rather than claiming an independent audit not performed.

## 2. Write the concrete proposal first

Create a unique `research/verification/framework_change_<date>-<run>/CHANGE_PROPOSAL.md`: user instruction verbatim/date, exact defects and source sections/card IDs, scope, affected dependencies, change class, intended before/after behavior, versions, verification plan and rollback. Preserve unrelated work and issued records.

Classify separately: administrative correction; integrity/process repair; scoring/format definition; selection/model/threshold experiment; data repair; suspended software prerequisite. A user instruction can authorize a process change without a statistical test. It cannot make predictive success true. A paper criterion is not a passed experiment.

## 3. Provide an implementation document

Write IMPLEMENTATION.md with a prioritised recommendation-by-recommendation map: original ID/finding; adopt/adapt/shadow/defer/reject and why; precise change; files; dependencies; task/owner; acceptance evidence; future sample/cohort requirements; rollback; status. Include as many recommendations as materially useful, not an arbitrary fixed count. Separate implemented document controls from data work not performed, shadows not tested, and fitted work suspended by Markdown scope.

Review acceptance tests critically. A confidence interval containing zero/one is not proof of equivalence, an arbitrary mean-|z| band does not prove calibration, a reachable gate does not prove selection value, and lower joint failure from covering lines is not predictive skill. Preserve original registrations and append explicit revised protocols; no silent moving of goalposts or claimed power without calculation.

## 4. Implement in dependency order

1. Copy every replaced document into a unique archive preserving relative paths and the base revision; do not overwrite an earlier archive.
2. Register new/versioned hypotheses before any future card uses them. Freeze candidate/baseline definitions, prospective start trigger, cohort/unit, primary metric, meaningful effect/precision, sample plan, missingness, stopping and rollback. If a necessary power/design input is unknown, keep predictive promotion BLOCKED_DESIGN rather than inventing it.
3. Edit controlling rules first, then scoring/templates/source/profile guidance, all affected prompts/indexes and synthetic examples. Keep the workflow Markdown/CSV/text. Search the live operating set for contradictions and stale dependencies; distinguish historical mentions from active instructions.
4. Bump only the versions actually changed, consistently across METHOD, CURRENT_RULES, CURRENT_STATE, templates and examples. Preserve old in-progress formats and explain migration through addenda/new minis. Classify every prompt change as EDITORIAL, PROCEDURE, FORMAT or STATISTICAL (CURRENT_RULES §11). Bump the prompt suite accordingly (`P-<date>-v<major>.<minor>`), and write a before/after dependency map for anything that is not editorial. Never call a change "wording-only" when an operator must now do something different.
5. Add dated changelog and learning/status pointers. Preserve original cards, logs, historical grades and dated reports. Do not consume a P-ID for tests or administrative changes.

## 5. Verify behavior and scope

Run VERIFICATION_PROTOCOL §6 and print actual results. Use a throwaway EXAMPLE-ID card/settlement outside live minis; test supported numeric, qualitative/missing baseline, unresolved field, push/void, allowed draw, late issue, adjustment rank flip, duplicate import and rerun/partial recovery cases as relevant. Every new check gets at least one negative fixture, naming the check that rejects it, and one legitimate edge case that passes (R35). Keep them in the change folder's `FIXTURES.md`, and label manual walkthroughs as manual. Check formulas and templates together, all changed relative links, version strings, archive byte identity, old-format preservation and exact allowed paths. A manual scenario walkthrough is labelled as such, not an executed importer or prospective test.

Read back every deliverable. Document failures/limits and fix dependent contradictions. Verify no scripts/code/JSON or new log entries were introduced and no protected old bytes changed. Review full staged diff, not only a file list.

## 6. Publish and report

Commit intended paths with a concrete problem/behavior message. Push to main or named branch without force; fetch and compare remote SHA and key artifact contents. Preserve concurrent work; reconcile a normal remote advance without history rewrite. Never claim publication from an unfetched tracking ref.

Return active prompt/index and implementation links, important before/after changes, versions, validation evidence, exact commit/remote status, effect on in-progress minis and unresolved data/experiment dependencies. Distinguish completed engineering/document work from predictive improvement still unproven.
