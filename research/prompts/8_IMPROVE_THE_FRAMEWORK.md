# PROMPT 8 — IMPROVE THE FRAMEWORK (RULES, PROMPTS, FORMATS)

**Run by:** Claude Code in a local checkout of the repository · **GitHub:** write (documents only) · **Mode:** `FRAMEWORK_CHANGE`

Use this prompt for any change to a rule, a constant, a format, a prompt or a document of record. The framework is Markdown, so a change is a reviewed edit to documents plus a pre-registered test. It never adds code, JSON, notebooks or workflow files, and it never changes a rule on the strength of one event.

---

## 0. Reading gate

Print the **reading receipt** ([research/prompts/README.md](README.md)) after opening: [CURRENT_STATE.md](../../CURRENT_STATE.md), [METHOD.md](../../METHOD.md), [CURRENT_RULES.md](../../CURRENT_RULES.md) (all, especially §9 custody and §11 change control), [SELECTION_RULES.md](../../SELECTION_RULES.md), [CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md), [HYPOTHESIS_REGISTER.md](../../HYPOTHESIS_REGISTER.md), [CONTRIBUTING.md](../../CONTRIBUTING.md), [CHANGELOG.md](../../CHANGELOG.md) (the last 3 entries), the latest retrospective report and the document or prompt you are changing.

## 1. State the problem and the hypothesis

Write, in `research/verification/framework_change_<YYYY-MM-DD>-<k>/CHANGE_PROPOSAL.md`:
- the exact problem (a failure class from SELECTION_RULES §8, a retrospective finding, a source failure, a user instruction), with the evidence (card IDs, counts, intervals);
- one versioned hypothesis and what would falsify it;
- the document(s) and section(s) to change, and which prompts, examples and checklists depend on them;
- the acceptance test (pre-registered, with a minimum sample and a rollback condition), or the statement that the change is an **administrative correction** (a typo, a broken link, a clarified sentence) that changes no number or behaviour.

A **user instruction** is a valid reason for a change without a statistical test. Record it verbatim and the date, and apply it as written.

## 2. Decide the class of change

| Class | Examples | Requirement |
|---|---|---|
| Administrative | Typos, links, wording that changes no rule | One commit; CHANGELOG line |
| Constant or threshold | Gate numbers, floors, ladders, family rules | Pre-registered test in HYPOTHESIS_REGISTER and the prospective window complete; or a recorded user instruction |
| Procedure | How a distribution is built or a check is done | Hypothesis, test, updated sport block and checklist |
| Format | Fields in a card, settlement or log | New format version (`mini-log-5`), updated templates, updated golden examples, old format stays valid for minis in progress |
| Prompt | Wording or steps of a prompt | Update the prompt, its examples and research/prompts/README.md together |

## 3. Make the change

1. Copy the text you will replace into `archive/superseded_<YYYY-MM-DD>/` (create it with a README line saying what and why) in the same commit.
2. Edit the controlling document first, then every document that depends on it, then the prompts and the golden examples. Search for the old text (`grep -rn`) in the operating set and fix every live reference; leave historical documents alone.
3. Bump the version strings that changed (method, control revision, scoring, format) in [METHOD.md](../../METHOD.md), [CURRENT_STATE.md](../../CURRENT_STATE.md) and [CURRENT_RULES.md](../../CURRENT_RULES.md) together.
4. Add a dated [CHANGELOG.md](../../CHANGELOG.md) entry: what, why, evidence, files, and what stays unchanged.
5. If the change adds a hypothesis, register it in [HYPOTHESIS_REGISTER.md](../../HYPOTHESIS_REGISTER.md) before any card uses it.
6. Do not alter an issued card, a settled mini, a Combined Log above its end marker, or a dated verification report.

## 4. Verify

Run [VERIFICATION_PROTOCOL.md](../../VERIFICATION_PROTOCOL.md) §6 and print the evidence: only intended paths changed; no code or JSON entered the repository; every changed link resolves; a card written with the new text passes the card self-audit (write a throwaway example in the change folder, not in a mini); version strings agree across METHOD, CURRENT_STATE and CURRENT_RULES; the golden examples still match the templates.

## 5. Publish

Commit by path with a message that states what changed and why, push to `main` without force, re-read the remote HEAD. If the change affects minis in progress, tell the user which format they finish in.

## 6. Report

```text
READING RECEIPT: <as printed>
Change class: <…> · reason (evidence or instruction):
Documents changed: <list> · archived text: <path>
Versions before / after: <method · control · scoring · format>
Hypothesis registered: <id or none> · acceptance test: <…>
Checks: <each with its result>
Commit SHA / publication status:
Effect on minis in progress:
```
