# Markdown repository verification protocol

**Scope:** current `main` tree and its active custody pointers. Run before each governance receipt and push. This procedure is text in a Markdown file; it does not require adding executable or data files to the repository.

## 1. Structural and Git custody gate

From the repository root, verify that every tracked and working file outside `.git` has a `.md` suffix, lives either at the root or directly in `prediction logs/`, and that no other content directory exists. The folder must contain exactly `PREDICTION_LOG_COMBINED.md` and Parts `_2` through `_6`, with no separate running logs or intermediate Part-5 snapshots. Check `git status --short --branch`, `git branch -a`, and `git remote -v` before attributing a result to `main`. A clean tree before editing is a baseline, not proof of forecast quality.

After the edit, inspect `git diff --check`, `git diff --stat`, and the changed content. In [Part 6](prediction%20logs/PREDICTION_LOG_COMBINED_6.md), extract the bytes **after the CRLF following** `<!-- BEGIN ORIGINAL P518 SOURCE BYTES -->` and **before the CRLF preceding** `<!-- END ORIGINAL P518 SOURCE BYTES -->`. Confirm that 141,740-byte block remains SHA-256 `c4d497bf339010eae2ff5df23a2d76290983585671666e74791618342565cf30`; never normalize or reformat those bytes. The former standalone mini log is available at Git `753f0a9`.

## 2. Queue and baseline custody gate

Compare the first snapshot in [Part 5](prediction%20logs/PREDICTION_LOG_COMBINED_5.md), the controlling note in Part 6, the first line of [Current Status](GAME_LOG_STATUS_CURRENT.md), and [P-518–P-522 reconciliation](P518_P522_RECONCILIATION.md). The present required state is: canonical history through P-517; P-518–P-522 reserved, not certified imports and ineligible; next new prediction ID P-523 by explicit user instruction. The embedded historical source's “P-523 next” line does not validate P-518–P-522 or supply the authority for this continuation.

For each of the 20 disputed rows, compare the issued p, q, contract, and literal `BASELINE_P` to the working settlement. The table in the reconciliation record identifies the current mismatches. A numeric `0.500` placeholder never replaces `NOT_YET_DERIVED` or a different issued baseline. Keep issued forecasts frozen; append sourced settlement corrections only after the event, cutoff, and independent result lineage gates pass.

## 3. Evidence and statistical gate

Check the historical preregistration and outputs in [Validation Evidence](VALIDATION_EVIDENCE.md) against the Git blob IDs and byte hashes listed there. Label these as historical aggregate results. A full rerun requires game-level source data and dependent modules absent from the current tree. Do not convert these results into a prospective card-skill claim.

For the [Skill Baseline Ledger](SKILL_BASELINE_LEDGER.md), independently recompute `(card p - y)^2` and `(baseline p - y)^2` for the 29 seed rows. Required rounded means are 0.2461 and 0.2360, so card minus baseline is +0.0101. Confirm that the prospective section still has zero rows and that its 100-decision, 30-card read-out point has not been reached. Which rows count, and what the read-out means, are defined once, in the ledger's rule 7.

RM-1 q is a row-calibrated ranking score. It is scored only in `T-RM1-PROSPECTIVE`'s paired Brier(q) against Brier(p) diagnostic, under the admission rules in `SCORING_AND_VALIDATION.md` §15. It is never scored or reported as the card's event probability.

Check that the four documents that state these rules still agree: `CURRENT_RULES.md` §D7/§D9, `PROBABILITY_TOOLKIT.md` §10, `SCORING_AND_VALIDATION.md` §13/§15, and `RECORD_ELIGIBILITY_SCHEMA.md`.

## 4. Link and freeze receipt gate

**Scope: every operating document.** That is every root `.md` file except:
- the preserved historical ledgers (`CHANGELOG.md`, `LEARNING_REGISTER.md`, `PREDICTION_LOG_COMBINED*.md`, `CONTROL_MANIFEST_*.md`, `VERIFICATION_RECEIPT_*.md`);
- `HISTORICAL_LINK_INDEX.md` itself;
- the body of `GAME_LOG_STATUS_CURRENT.md`, whose header line is checked.

So the scope includes all ten `RULES_<SPORT>.md` files and both `LEAGUE_RULES_*.md` files, which the model reads before every card. (Before 2026-09-28(e) this gate listed only nine documents and missed a broken link on line 5 of every sport file.)

**What counts as a repository path:**
- any local Markdown link target;
- any code span that starts with a directory the repository has ever had (`tools/`, `research/`, `archive/`, `reviews/` and so on; all removed, see the [index](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents));
- any code span that is a bare file name, with a `.md`, `.py`, `.json`, `.csv`, `.txt` or `.yml` extension, that exists anywhere in Git history.

API route slugs (for example `football/nfl`) and URL fragments are not repository paths.

**Two rules, both must pass:**
- **L1.** Every local Markdown link resolves in the current tree. A broken link is repointed to its pinned Git commit or to a current document; a recovery note beside it does not excuse it.
- **L2.** A code-span path that does not resolve is qualified on its own line or the next non-blank line by one of:
  - a link to [Removed paths cited in operating documents](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents);
  - a pinned GitHub commit link;
  - a Git object ID;
  - the words "Original path:".

  Every such path must have a row in that index section.

A text instruction to run a removed tool is not repaired by a link. Rewrite it as the Markdown procedure that replaced it.

The [Historical Link Index](HISTORICAL_LINK_INDEX.md) also records broken old paths inside preserved ledgers, with immutable Git recovery links where available. Do not silently edit frozen historical text merely to repair a link.

Create the next `CONTROL_MANIFEST_*.md` after all stable document edits. Hash UTF-8 contents normalized to CRLF as specified in the manifest, list the stable governance and frozen source files, and exclude the manifest itself and the two living logs if their contents will change. Point `METHOD.md` to the new manifest and put that manifest's own normalized-CRLF SHA-256 into the first line of `GAME_LOG_STATUS_CURRENT.md`. Recheck every listed file and the receipt after those pointer updates.

## 5. Publish gate

Stage only the intended Markdown files. Check the staged diff, commit on `main`, push to `origin/main`, then verify local `HEAD` equals `origin/main` and the worktree is clean. List local and remote branches and retain only `main`. Record the executed checks and unresolved evidence limits in a dated Markdown verification receipt.
