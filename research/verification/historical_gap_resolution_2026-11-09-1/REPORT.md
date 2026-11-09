# Historical closure and full-log sweep ·9 November 2026

The remaining operational P126/P418 tasks are closed at explicit evidence limits. No live sporting-settlement item was found in the effective historical view, active mini or frozen league-day queue. This does **not** mean every historical source, issue time, operator definition or training feature has been recovered. Those limits are recorded separately below.

Owner authority: “close and settle the remaining gaps, and then do a sweep of all the logs and see if there is any other gaps that need to be accounted for”. Base commit: `0782afa0d55b3983d68a435b6a06c0619cd1ce07`. No prediction-method change, retraining, promotion or canonical ID allocation occurred. The nine previously permanent closures were not researched or reopened.

## Exact closure decisions

| Record | Effective decision | What remains unavailable |
|---|---|---|
| P126 rank 2: first-half Over 0.5 | **UNATTAINABLE / COMPLETELY_RESOLVED / DO_NOT_RETRY**; replaces a missing-data VOID | No admitted halftime or goal-time field |
| P126 rank 4: corners Over 7.5 | **UNATTAINABLE / COMPLETELY_RESOLVED / DO_NOT_RETRY**; replaces a missing-data VOID | No compatible corner count |
| P418 record/custody | **CLOSED_NO_RECOVERED_ISSUED_CONTRACT / NO_SCORED_TRIAL** | Original propositions, ranks, lines, probabilities and authenticated issue core |
| P523 rank 5: corners, threshold never defined | **CLOSED_UNDEFINED_PROPOSITION / NO_SCORED_TRIAL** | No defined threshold; the old administrative VOID is preserved literally |
| P537 rank 4: corners Over 9.5 | **UNATTAINABLE / COMPLETELY_RESOLVED / DO_NOT_RETRY**; replaces a missing-data VOID | Exact-match pages supply no corner values |

[Exact keys and source hashes](SOURCE_EXHAUSTION_CLOSURES.csv), [immutable closure evidence](RESEARCH_CLOSURES.md), [current open sporting queue](OPEN_ITEMS.csv). The empty queue has a header and zero items; unavailable values remain missing and excluded from sporting scores/model labels. These terminal closures do not become sporting losses, wins, pushes or operator-certified voids.

P126's owner-intended target is **28 August**, working 11:00 IST / 15:30 AEST, bounded by the neighbouring records. The Away End still has an unscored schedule entry. Sport24's actual team-result HTML, RTL layout and linked score-direction CSS support **Aakraman 3–0 Sikkim Boys** conditionally. Both team pages share upstream lineage and count as one collector. The old winner/Over 2.5 WIN labels remain unchanged, with no independent field-owner certification or actual-start proof added. Neither a three-goal final nor a search snippet can settle halftime/corners. [Earlier owner chronology](../historical_chronology_2026-11-09-1/REPORT.md).

P418 is the **September** target. RSSSF's retrieved round-15 record gives **14 September, Drukpa 1–3 RTC** as secondary evidence. June/July meetings are excluded. Reachable Git custody search read **1,666 unique text blobs / 151,800,883 bytes** and found 129 matching blobs. The archived `card_excerpts/P-418.txt` is an index excerpt saying **five rows issued, none graded**; other summaries say none issued/not preserved. No authentic original contract was recovered. Closing custody does not assert that no forecast ever existed, and the final cannot create an invented five-row slate. [Search scope](GIT_CUSTODY_SEARCH_SCOPE.csv), [matches and paths](GIT_CUSTODY_SEARCH.csv).

P537's event date is **4 October**, independently scheduled by KFU and recorded in exact-match result pages; 5 October was a record/review date. FootballInfo has empty corner cells in both retrieved HTML and the supported reader. Its scorer attribution at 64 minutes disagrees with 11v11, so no player-scorer finding is admitted. The date overlay distinguishes **OWNER_INTENDED_DATE**, **SECONDARY_EVENT_DATE** and **VERIFIED_EVENT_DATE**; none is an issue timestamp.

## Source research and access

[SOURCE_ACCESS_AUDIT](SOURCE_ACCESS_AUDIT.csv), [SOURCE_CAPTURES](SOURCE_CAPTURES.csv) and [FIELD_DECISIONS](FIELD_DECISIONS.csv) retain **19 exact URL attempts**, including linked CSS and indexes rather than 19 independent game records. The relevant fields were sought through schedule publishers, team-result pages, federation announcements, RSSSF, local news, 11v11 and FootballInfo. A permitted response was tested for its actual field, event, date and completeness.

Unknown Sofascore/ESPN rules and blocked ScanGoal/TheSportsDB/KICKINDI paths were refused. Their snippets were not admitted. Championat returned a sign-in shell; BFF/BBS pages did not establish the exact September target. Missing table cells were not interpreted as zero, and no source quorum was manufactured from related endpoints. The source register links these findings for future compatible work; exact paths/policy must be checked again. No mirror, proxy, CAPTCHA bypass or blocked-source syndication was used.

## What the all-log sweep found and repaired

[Complete-byte inventory](LOG_FILE_INVENTORY.csv): **372 log/mini/issued/control artifacts**, **335 unique byte bodies**, **35,506,154 bytes**, covering all **638 retained card IDs**. [URL occurrences](LOG_SOURCE_OCCURRENCES.csv): **11,165 occurrences**, **2,992 distinct pointers**, **775 host strings**. Archived copies and control templates are included; these are not 372 distinct issued minis. The 224 current competition labels include a weather scope alongside the ten sports. Heading/source-phase association is heuristic, not proof of pregame sourcing or a semantic re-verification of every historical assertion.

The final generated view has **2,549 rows / 638 cards**, with **zero CONFLICT rows** and **zero UNRESOLVED rows classified RETAINED_CONTRACT**. [Generated report](final_history_release/CARD_HISTORY.md), [all effective rows](final_history_release/CARD_ROWS.csv). Earlier preview/history folders are explicitly intermediate snapshots; this verified output is operative for this sweep.

| Finding | Repair or retained disposition |
|---|---|
| 11 artificial CONFLICT cells across P012/P013/P018/P035/P036/P040/P060 | Replace 28 lossy rank aggregates with **72 literal source-bound view/contract rows**. Preserve tied ranks, original/live versions, withdrawal and source eligibility text. All 72 remain diagnostic; no successful version is selected as primary |
| 58 old W/L labels without usable propositions or with no-trial status | Recover **54 literal proposition labels** from original cards or preserved slates, without changing grade/p/q/baseline. Keep **four P157 no-action labels excluded** |
| Recovered rows with timing/eligibility limits | P306's five start-crossed rows, P509's four learning-only rows and P517's four ambiguous/untimestamped rows remain diagnostic. P517's 18.5/186.5 clerical ambiguity is disclosed, not operator-certified |
| Missing-evidence VOID labels | Three become UNATTAINABLE; P523's undefined proposition closes with no scored trial. Eight tennis retirement rows retain their stated legacy convention. Three recovered P040 VOID entries are withdrawn diagnostic versions, not sporting voids |
| 29 literal UNRESOLVED placeholders | P418 is explicitly closed as unrecovered custody; the other 28 are rank-zero/no-issuance/alias placeholders or four unactivated P445 conditions. None is an active sporting W/L task |
| Scores could admit non-scorable W/L labels | The card-history and legacy calibration summary paths now exclude no-trial/missing-proposition/closed records and diagnostic views; negative regression tests exercise this exclusion |

[Recovered propositions and source literals](RECOVERED_PROPOSITIONS.csv), [before: 58 unsafe labels](NONSCORABLE_LABELS_BEFORE.csv), [retired aggregates](RETIRED_LOSSY_AGGREGATES.csv), [literal unresolved classifications](UNRESOLVED_LITERAL_CLASSIFICATION.csv). Hash-bound view guards fail if the aggregate, source prefix, row, rank, contract, grade or role changes. A row with a numeric forecast cannot have it erased by this view recovery. Recovery cannot promote a row into the primary lane.

## Other gaps accounted for, without invented completion

[GAP_REGISTER](GAP_REGISTER.csv) contains **163 finding rows**; a source row can have multiple findings, so this is not 163 pending games. It accounts for terminal missing fields, no-action placeholders, diagnostic versions, withdrawals, retirement conventions and reserved-record certification. There are **12 effective UNATTAINABLE rows**: the original nine permanent closures plus the three new field-exhaustion closures. The original nine-row register is byte-identical.

[Retained certification limits](RETAINED_CERTIFICATION_LIMITS.csv) carries **56 prior dated limitations**, retaining the old wording and adding current notes for P126/P418. It is not a new retry queue. In particular:

- P518–P522 retain 20 legacy sporting grades and reserved-ID status; original issue/baseline/operator certification is not created. Old settlement baseline substitutions are not admitted as frozen observed baselines.
- Field-owner/independent-lineage certification, source-known-at/issue clocks, operator settlement definitions and exact final clocks remain unavailable for some older records. A current final cannot reconstruct them.
- **1,497 of 2,486 decisive literal rows lack numeric p**; this includes qualitative/diagnostic history and is not a count of missing prospective forecasts. Missing probabilities and paired baselines are not backfilled after seeing outcomes. [Coverage counts](DATA_COVERAGE_LIMITS.csv).
- The learning store still has **5,402 event/result pairs, eight team-statistic rows and zero player-availability rows**. The new per-game learning-log directory has no completed game folders. This work cannot turn result-only history into point-in-time training examples.

The active mini has **0 open cards**, frozen league-day events without settlement are **0**, and the imported local-key effective view has **228 rows / 16 revised / 0 UNRESOLVED**. Highest P638 / next P639; reservations unchanged. [Live record readback](CURRENT_STATE_READBACK.md).

Predictive evidence is unchanged: ANALYST_PRIMARY_V1 has **31 decisive primary rows on 16 cards**, Brier **0.192946**. The same-row paired comparison remains only **12 rows / six games**: card Brier **0.168247**, baseline **0.155932**. These outcome-exposed diagnostics do not establish improvement. No model promotion or new ML-ready feature was created; current model separation remains in force. The forecast runtime's import-closure digest is unchanged. MLB's existing stale release status is retained, not caused by this reporting edit.

## Custody, tests and publication

Original Part 1–8 bytes are unchanged. Part 9 retains its complete base prefix and receives one dated addendum. [Append receipt](LOG_APPEND_RECEIPT.csv), [archived replaced inputs](../../../archive/historical_gap_resolution_2026-11-09-1/MANIFEST.csv). Original issued texts, active/frozen minis, numeric probabilities/ranking scores/baselines, model releases, learning-store rows and the nine permanent closures are checked against the base. No IDs are consumed.

[Verification checks](VERIFICATION_CHECKS.csv), [query/helper identities](QUERY_RECEIPTS.csv) and [test/publication procedure](VERIFICATION.md) provide reproducibility. Raw web bodies and temporary research helpers remain outside the repository, with paths, hashes, times and field decisions committed. The Git search excludes dangling objects and unavailable external chats; missing original evidence is not proof of never-issuance. No automated future research was scheduled.

Publication is to authorized `origin/main`, after scoped staging and tests. The final commit SHA is reported only after push/fetch and equality of local HEAD, origin/main and the live remote main ref.

The older `ml cards` calibration command now consumes the same effective grades and exclusions, rather than raw PASS/FAIL cells, and its completion receipt binds every discovered history/correction input. It refuses unmatched revisions or input/discovery drift. All four P509 rows retain the source section's learning-only status; the additional three existing contracts are bound in [REPORTING_ROLE_CONTROLS](REPORTING_ROLE_CONTROLS.csv). Saved older model-shadow reports remain unchanged dated artifacts, not regenerated authoritative history. [Current calibration readback](CALIBRATION_READBACK.md).
