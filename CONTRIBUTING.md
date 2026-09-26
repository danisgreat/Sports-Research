# Contributing: branches, commits and checks

**Added 2026-09-25(c).** This applies to every session that writes to this repository: this one, peer Claude or Codex sessions, and manual edits.

## Why

On 2026-09-24 a peer session committed an invented settlement process record straight to `main` (`cb95acd`). It was caught only by a later audit. On 2026-09-25 a commit titled "c" added build files. Nothing reviewed either change before it landed. The rules below make every change pass the same automated checks first.

## Workflow

1. **Branch per session or topic.** Never commit straight to `main`.
   ```bash
   git switch -c session/2026-09-26-settle-p510     # session/<date>-<topic>
   ```
2. **Run the checks locally** (CI runs the same ones):
   ```bash
   python -m unittest discover -s . -p "test_*.py"
   python -m unittest discover -s tools -p "test_*.py"
   python tools/repo_hygiene.py
   python tools/verify_manifest.py
   python audit_card_controls.py "Mini logs (to be sent to actual log later)/<active>/<log>.md" --settlement --strict --allow-empty
   ```
3. **If you changed a governance file** (anything listed in the current `CONTROL_MANIFEST_*.md`, other than the two living logs):
   - check `python tools/evidence_status.py`: while `C-RULE-FREEZE` is in force, the change must be a validity repair, a retrieval/integrity control, a measurement/disclosure control or documentation (`RULES_GENERAL.md` §"2026-09-26"(b));
   - regenerate the receipt: `python tools/make_manifest.py --out CONTROL_MANIFEST_<date>.md --title "…" --note "…" --category <INTEGRITY|MEASUREMENT|DOCUMENTATION|VALIDITY_REPAIR|MODEL_CHANGE>`. One manifest per issuing day except validity repairs; a `MODEL_CHANGE` also needs `--model-change` and, during the freeze, `--freeze-override` quoting the user's instruction;
   - if you changed a sport file's controls, update its §0 live page in the same commit (`C-READING-GATE`);
   - repoint `METHOD.md`'s header ("Freeze the SHA-256 file receipt from …");
   - repoint the active mini log's "Freeze with every card" row, with the printed SHA;
   - re-run `tools/verify_manifest.py`.
4. **Push the branch and open a pull request:**
   ```bash
   git push -u origin HEAD
   gh pr create --fill
   ```
   Merge only when the **checks** workflow is green.
5. **Log edits are append-only.** Issued cards, probabilities and ranks are never rewritten. Corrections are appended (`METHOD.md` §6, §10).

## Commit messages

- Use `type(scope): what changed`, e.g. `settle(p-510): NBL Perth v Breakers, three lineages` or `docs(rules): …`. Types: `card`, `settle`, `audit`, `rules`, `docs`, `tools`, `data`, `chore`.
- The body explains *why*, names the cards or controls touched, and says whether a manifest was regenerated.
- One logical change per commit. Never use single-letter or empty messages.

## Never commit

- Dependency trees or tool scratch: `node_modules/`, `.codex_spreadsheet_tmp/`.
- Python build output: `__pycache__/`, `*.pyc`.
- Machine-local settings: `.claude/settings.local.json`.
- Raw API pulls, i.e. research caches and raw JSON. Commit derived results and small trimmed fixtures only.
- Odds, prices or betting-site content in any form. The single exception is `MARKET_BENCHMARK_LEDGER.md`: operator-entered, **post-settlement**, no-vig closing **probabilities** and the de-vig method only — never raw odds, never fetched by an agent (`C-MARKET-BENCHMARK`).
- Session scratch files (`scratch/` is ignored; the former folder is archived).

`.gitignore` covers the first four; `tools/repo_hygiene.py` fails CI if any of them is tracked.

## Protecting `main` on GitHub (owner action)

Branch protection is a repository setting and cannot be committed. The owner can enable it once:

```bash
gh api -X PUT repos/danisgreat/Sports-Research/branches/main/protection \
  -F "required_status_checks[strict]=true" -f "required_status_checks[contexts][]=checks" \
  -F enforce_admins=false -F required_pull_request_reviews=null -F restrictions=null
```

Or use the web UI: Settings → Branches → add a rule for `main` → "Require status checks to pass" → select `checks`.

## History size (owner decision)

About 140 MB of `node_modules` remains in the git **history** from commits made before 2026-09-25(c), although it is no longer tracked. Removing it requires rewriting history, for example `git filter-repo --path .codex_spreadsheet_tmp --path-glob '*/node_modules/*' --invert-paths`, followed by a force-push. That changes every commit SHA cited in the logs (e.g. `cb95acd`). It is therefore the owner's call, and it must be coordinated with every clone.
