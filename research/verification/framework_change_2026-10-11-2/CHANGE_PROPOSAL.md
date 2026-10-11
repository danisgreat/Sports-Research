# Change proposal: finish the latest retrospective's recommendations (run 2)

Date: 2026-10-11 (Australia/Sydney). Base: local `main` at `abb3e98d7ab2dfc3bd33bcdf42b4a3bf3a11a7d4` (the user's v10 release, committed 23:27 and **not yet pushed**), on top of published `origin/main` `2d6d86350ce4d6bd9f4ae0f34a42351e71ff0e4b`. Worktree clean at the start.

## Authority and scope

User instruction, verbatim:

> implement all of the recommendations from the latest framework review/retrospective if it already hasnt been implemented and do it methodically without mistakes

**Reading taken.** "Latest retrospective" = the cohort retrospective of 2026-10-11 and its seven proposals RET-01 to RET-07 (the newest retrospective in the repository). "If it hasn't already been implemented" = check the live documents first, because the v10 release (commit `abb3e98d7`, same evening) already claims all seven. The Oct 9 framework review's 57-item register was read for items still open (SRC-07, PRD-08, DST-02) but not re-opened as a whole. The user's instruction is authority for document, data and process changes. It cannot make any predictive claim true, and a written acceptance rule is not a passed experiment.

## Defects and gaps found

| # | Finding | Evidence | Remedy in this run |
|---|---|---|---|
| 1 | v10 documents RET-02 to RET-07 as controls; they are present where it says (see IMPLEMENTATION §2). RET-01's freshness control exists but the **profile refresh itself was `DATA_PENDING`** | v10 IMPLEMENTATION §3; LEAGUE_PROFILES header | Carry out the refresh (prompt 7 §4) with a coverage audit |
| 2 | The NBL profile (2022-24, n 425) was one season stale and included the lowest-scoring season | [NBL_PROFILE_AUDIT](NBL_PROFILE_AUDIT.md) §3 | New 2023-25 row; prior retained as comparator; windows compared before pooling |
| 3 | NBL 2025 file: blank dates on all regular-season rows; 14 post-season rows typed `Regular Season`; some quarter columns inconsistent | audit §2 | Recorded and guarded in ARCHIVE_USE_GUIDE §8; date evidence sidecar; **no existing cell changed** |
| 4 | No 2026-27 NBL file existed, so no NBL card could read a current-season game from the archive (P-560, P-565 and P-566 record the 2026 file as not found; P-575 records `ARCHIVE_PARTIAL`) | the four cards' `Archive check` and R9 text | New partial snapshot (29 games), with provenance, checks and 10 independent confirmations |
| 5 | KBO and NPB extra-innings shares in LEAGUE_PROFILES (0.1% and 0.0%) are default-filled column artefacts, contradicted by ties | [KBO_NPB_EXTRAS_AUDIT](KBO_NPB_EXTRAS_AUDIT.md) | Withdrawn as `NOT_ESTIMABLE`; correction note; no replacement number invented |
| 6 | Reachability matrix `local_windows` column never probed (SRC-07, FC10-05) | SOURCES §F | One hand probe of 12 sources, dated; no weekly-refresh claim |
| 7 | FC10-PROFILE-v1's candidate and baseline were not defined precisely enough to freeze | HYPOTHESIS_REGISTER | Definitions frozen before any card cites the refreshed row; effect size and tolerance left unregistered (inputs unknown) |

## Change class

Data repair/extension (finding 4), integrity/process repair (3, 5), administrative (6, 7), **profile update** (2), which is a data update governed by prompt 7 §4, not a selection or model experiment. No selection rule, threshold, ranking, gate, scoring definition, prompt, template or version string changed. The method, control and scoring versions (MDS-2026.10.11-v10.0, CR-2026.10.11-R1, SCV-2026.10.11-v6, SEL-2026.10.11-v2) are unchanged; only the profile document version moves (LP-2026.10.09-v1 to LP-2026.10.11-v2).

## Affected dependencies

LEAGUE_PROFILES (NBL row, KBO/NPB extras, version), ARCHIVE_USE_GUIDE (§1 row, new §8), SOURCES (matrix, §F note), HYPOTHESIS_REGISTER (dated status), CURRENT_STATE (implementation paragraph), CHANGELOG, one new archive CSV. Prompt 1's basketball block and prompt 7 already refer to "the correct league/era profile" and to the NBL refresh and need no edit. Cards issued before this version keep the row they cited; the refresh cannot alter an earlier baseline (LEAGUE_PROFILES rule 3).

## Verification plan and rollback

Verification: [VERIFICATION_REPORT.md](VERIFICATION_REPORT.md). Rollback is a forward revision (restore the retained row as the default and mark the 2026 CSV withdrawn), never a rewrite of issued cards or git history; archived originals of every edited document are in `archive/superseded_2026-10-11/profile_refresh/`.
