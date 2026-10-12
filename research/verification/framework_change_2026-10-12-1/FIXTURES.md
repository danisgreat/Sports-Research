# Fixtures for the new checks (R35) — manual walkthroughs

**These are manual documentation walkthroughs, not an executed test suite.** No validator runtime exists (CURRENT_RULES §0). Each fixture states an input, the check that must reject it (negative) or accept it (edge case), and the result obtained when the rule text was applied by hand on 2026-10-12. Values are synthetic unless a real file is named. EXAMPLE IDs are not P-IDs.

| # | Fixture | Kind | Rule / check applied | Expected | Walkthrough result |
|---|---|---|---|---|---|
| F01 | Prompt-1 cricket section citing "SOURCES §3.6" | Negative | R08: semantic source section | §3.6 is rugby league, so wrong | Was present at base; now an anchored link to SOURCES §3.3 in prompt 1 ([target](../../../SOURCES.md#33-cricket)); anchor resolves (link check 0 problems) |
| F02 | Ice-hockey card for Liiga using only the NHL route §3.9 | Negative | R08 hockey text: "an NHL route is never assumed to cover another league" | Fails C9/C12 | Rejected by the prompt-1 hockey reading line |
| F03 | Run receipt citing published `CURRENT_RULES` at SHA X while applying a dirty local `SELECTION_RULES` | Negative | R09 one authority mode; C1 | Fails C1 (mixed revisions) | Rejected: the receipt must name one mode and list the difference |
| F04 | Same dirty local rule, receipt `LOCAL_WORKING_TREE` listing the difference and saying it applied the local version | Edge (pass) | R09 | Passes | Accepted |
| F05 | Archive column `Red Cards` = 0 on every row of a season | Edge (pass) | R26 `SUSPECTED_DEFAULT` → checked → `MEASURED` | Kept as a real zero | Accepted after the check; never auto-blanked |
| F06 | Czech builder `Attendance` 5,420 on 13,972 rows, proven by the builder line `"Attendance": "5,420"` | Negative | R26 `CONFIRMED_PLACEHOLDER`; R01 | Removed from measurement | Rebuilt archive: 0 attendance values |
| F07 | Football HT score = ⌊FT/2⌋ for 1975–95 rows | Negative | R02 / ARCHIVE_USE_GUIDE §9 rule 3 | Rejected | Rebuilt archive: HT blank before 1995-96 (0 rows filled) |
| F08 | Hockey row "2-2* " with periods printed summing 1-2 | Negative | R27: flag, never balance | `PERIOD_SUM_MISMATCH`, row kept as printed | 55 such rows flagged; 0 adjusted |
| F09 | Tennis: player wins 6-0, loses 4-6, 4-6 | Edge (pass) and negative for the old bound | R12 | Match LOSS; −1.5 games WIN (14-12, margin +2). The old bound "P(−k.5) ≤ P(win)" must not be enforced | Arithmetic: games 14-12, sets 1-2, match LOSS, −1.5 WIN. Toolkit §6 now includes the deciding-set-loss term |
| F10 | KBO card pricing a moneyline as losing on a 9-9 tie without a frozen contract convention | Negative | R13; SELECTION_RULES §4 ties row | Fails C10 (UNKNOWN_DEFINITION until frozen) | Rejected |
| F11 | Rank-1 p_card 0.6215, alternative 0.5810, ε 0.002 | Negative for PASS | R14: \|0.6215 − 0.62\| = 0.0015 ≤ ε | `GATE_UNRESOLVED_PRECISION`, not PASS | Computed: 0.0015 ≤ 0.002 → unresolved |
| F12 | NFL −3.5 priced by adding 0.07 key-number mass to the row only | Negative | R14 / toolkit §1.3 | Fails C4 (complement −3.5 / +3.5 no longer sums to 1) | Rejected; the corrected recipe renormalises the integer margin distribution |
| F13 | Two minis both preparing working ID P-580, one with an unexpired lease | Negative | R15 | Second mini blocked | Rejected by prompt 2 §2 |
| F14 | Card appended to a mini after its FROZEN_SOURCE receipt (source 11,052 → 12,300 bytes) | Negative | R16; S14 | `GROWTH_DETECTED`; block routed, not covered | Rejected; the example package shows an unchanged byte count |
| F15 | Revision-2 changes one contract key; revision-3 and revision-3b both name revision-2 as parent | Negative | R17; S13 | Unchanged keys keep revision-1/2 grades; keys in 3 vs 3b are `REVISION_CONFLICT` → UNRESOLVED | Applied: resolution by parent chain, not by file position |
| F16 | Settlement BEGIN P-NNN revision-2 closed by END P-NNN revision-1 | Negative | R19 marker check | Import blocked before mutation | Rejected |
| F17 | Legacy mini-settlement-4 block without a revision key | Edge (pass) | R19 legacy declaration | Imports once under the declared legacy format | Accepted |
| F18 | Status register edited with a text editor: 80 CRLF + 868 LF became 948 CRLF | Negative | R20 identity check | Fails (whole-file ending change) | **Real incident, 2026-10-12**: caught by the CRLF/LF count and repaired at byte level from the blob (1 line changed, 80 CRLF kept) |
| F19 | Second settlement revision for P-560 (closed Part 6 card) written into Part 6 | Negative | R21 cross-part routing | Must go to the active part with a pointer | Rejected |
| F20 | Rollover requested when Part 7 is 1.26 MB with 30 entries | Edge | R21 triggers (1.5 MB / 50 entries) | No automatic trigger; user request still valid | Correct: not triggered automatically |
| F21 | Retrospective claiming 100% request coverage from cards alone (mini-log-6 cohort) | Negative | R22 | Request coverage `NOT_COMPUTABLE` | Rejected |
| F22 | Headline Brier computed with a C-grade row included silently | Negative | R23 | Headline A/B only; C in the sensitivity view | Rejected |
| F23 | Summary saying "the cohort shows no skill" from 20 cards without paired baselines | Negative | R24 | Must say "does not establish" | CURRENT_STATE wording corrected |
| F24 | Card with an L5 of 3 games labelled "L5" | Negative | PR-01; C17 | True n printed ("L5 (n = 3)") | Rejected unless the true n is shown |
| F25 | Card using L5 > L20 to move the total up, with no mechanism named | Negative | PR-01; CURRENT_RULES §7 | Width only, not a lean | Rejected (C17) |
| F26 | Card labelling its starter "unconfirmed" but pricing from the base case only | Negative | PR-03; C19 | Must price the mixture and print p_base | Rejected |
| F27 | Symmetric low/high cases (example EXAMPLE-001) | Edge (pass) | PR-03 | Mixture = base; p_card = p_base | Accepted (toy masses .45/.25/.20/.10) |
| F28 | Ranked row without line distance | Negative | R33; C18 | Fails C18 | Rejected |
| F29 | Card with 3 numeric rows, 2 baselines, missing reason "n/a" | Negative | PR-06 enumerated reasons | Fails C18 | Rejected; must use an enumerated reason |
| F30 | Archive date of a re-dated postponement used as known before its correction | Negative | R28 | `KNOWN_AT_UNVERIFIED`; may not decide Rank 1 | Rejected |
| F31 | Aggregation over both `Basketball/BSL` and `…/Austria Basketball Bundesliga` | Negative | ARCHIVE_USE_GUIDE §9 rule 1; alias note | Each game counted twice | Rejected; the alias note says count once |
| F32 | Prompt change adding a field, recorded as "wording only" | Negative | R34 | Must be FORMAT and bump the major version | Rejected |

**Example pair check (structural, executed):** `EXAMPLE_ACTIVE_MINI.md` (11,052 bytes) is an exact byte prefix of `EXAMPLE_SETTLED_MINI.md` (16,534 bytes): `cmp -n 11052` PASS. The legacy v10 pair in `legacy_mini_log_6/` is unchanged (moved with `git mv`).
