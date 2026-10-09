# Contribution procedure

The repository holds Markdown, CSV and text only. Do not add code, JSON, notebooks, workflow files or binary data; a framework change is a change to documents. Read [CURRENT_RULES.md](CURRENT_RULES.md) and [CURRENT_STATE.md](CURRENT_STATE.md) first. The pre-rewrite procedure is kept in [archive/superseded_2026-10-09/CONTRIBUTING.md](archive/superseded_2026-10-09/CONTRIBUTING.md).

1. **Inventory first.** Run `git status` and `git log -3`. Note branch, HEAD and any uncommitted work that is not yours. Preserve it; never overwrite unrelated edits.
2. **Preserve originals.** Never edit an issued card, a settled mini, a Combined Log above its end marker, a preserved original in `research/issued_research/`, or a dated verification report. Corrections are dated addenda. If a document must change, copy the old text into `archive/` in the same commit.
3. **Keep contracts explicit.** Identity, endpoint and time stay explicit. Never replace missing data with a guess or a q with a probability.
4. **Sources.** Use the routes in [SOURCES.md](SOURCES.md); record source failures and unknown independence. Keep odds-bearing material out.
5. **Check by hand.** Run the checklist that matches your change ([VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md) §2 to §6) and print the evidence. `git diff --numstat` on any log you touched must show 0 deleted lines.
6. **Rule or prompt changes.** Bump the version strings in [METHOD.md](METHOD.md) and [CURRENT_STATE.md](CURRENT_STATE.md), add a dated [CHANGELOG.md](CHANGELOG.md) entry, and add the hypothesis and its acceptance test to [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md). Never change a rule on one event.
7. **Publish deliberately.** Inspect the full diff, stage only intended files by path, verify the remote and a clean state before claiming publication. Do not push over someone else's work and do not force-push. No publication is implied by a local edit.

Verify archived source length and coverage before deleting any redundant working mini, and keep unique archive bodies and audit evidence. Scientific and process failures must be visible; a green check shows only what it checks.
