# Markdown repository verification protocol

**Scope:** current `main` tree and its active custody pointers. Run before each governance receipt and push. This procedure is text in a Markdown file; it does not require adding executable or data files to the repository.

## 1. Structural and Git custody gate

From the repository root, verify that every tracked and working file outside `.git` has a `.md` suffix, lives either at the root or directly in `prediction logs/`, and that no other content directory exists. Check `git status --short --branch`, `git branch -a`, and `git remote -v` before attributing a result to `main`. A clean tree before editing is a baseline, not proof of forecast quality.

After the edit, inspect `git diff --check`, `git diff --stat`, and the changed content. Confirm the [P-518 onward mini log](prediction%20logs/PREDICTION_MINI_RUNNING_LOG_P518_ONWARD.md) remains SHA-256 `c4d497bf339010eae2ff5df23a2d76290983585671666e74791618342565cf30`; never normalize or reformat frozen issue bytes.

## 2. Queue and baseline custody gate

Compare the first snapshot in [Part 5](PREDICTION_LOG_COMBINED_5.md), the first line of [Current Status](GAME_LOG_STATUS_CURRENT.md), and [P-518–P-522 reconciliation](P518_P522_RECONCILIATION.md). The present required state is: canonical through P-517; P-518–P-522 reserved, unimported, and ineligible; next ID HOLD. The working mini log's “P-523 next” language is a disputed historical claim, not a release authorization.

For each of the 20 disputed rows, compare the issued p, q, contract, and literal `BASELINE_P` to the working settlement. The table in the reconciliation record identifies the current mismatches. A numeric `0.500` placeholder never replaces `NOT_YET_DERIVED` or a different issued baseline. Keep issued forecasts frozen; append sourced settlement corrections only after the event, cutoff, and independent result lineage gates pass.

## 3. Evidence and statistical gate

Check the historical preregistration and outputs in [Validation Evidence](VALIDATION_EVIDENCE.md) against the Git blob IDs and byte hashes listed there. Label these as historical aggregate results. A full rerun requires game-level source data and dependent modules absent from the current tree. Do not convert these results into a prospective card-skill claim.

For the [Skill Baseline Ledger](SKILL_BASELINE_LEDGER.md), independently recompute `(card p - y)^2` and `(baseline p - y)^2` for the 29 seed rows. Required rounded means are 0.2461 and 0.2360, so card minus baseline is +0.0101. Confirm that the prospective section still has zero rows and that its 100-decision, 30-card checkpoint remains unopened. RM-1 q is a rank score and must not be scored as an event probability.

## 4. Link and freeze receipt gate

Resolve every local Markdown link in the current operating documents: `README.md`, `METHOD.md`, `CURRENT_RULES.md`, `PROBABILITY_TOOLKIT.md`, `CARD_AND_LOG_TEMPLATES.md`, `SOURCES.md`, `PROMPTS.md`, `BASE_RATES_REGISTER.md`, `CONTRIBUTING.md`, the current status header, and the reconciliation/validation documents. The [Historical Link Index](HISTORICAL_LINK_INDEX.md) records broken old paths inside preserved ledgers, with immutable Git recovery links where available. Do not silently edit frozen historical text merely to repair a link.

Create the next `CONTROL_MANIFEST_*.md` after all stable document edits. Hash UTF-8 contents normalized to CRLF as specified in the manifest, list the stable governance and frozen source files, and exclude the manifest itself and the two living logs if their contents will change. Point `METHOD.md` to the new manifest and put that manifest's own normalized-CRLF SHA-256 into the first line of `GAME_LOG_STATUS_CURRENT.md`. Recheck every listed file and the receipt after those pointer updates.

## 5. Publish gate

Stage only the intended Markdown files. Check the staged diff, commit on `main`, push to `origin/main`, then verify local `HEAD` equals `origin/main` and the worktree is clean. List local and remote branches and retain only `main`. Record the executed checks and unresolved evidence limits in a dated Markdown verification receipt.
