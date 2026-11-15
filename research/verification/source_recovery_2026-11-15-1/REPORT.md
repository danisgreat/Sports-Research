# Targeted unresolved-field source recovery

Started 15 November; completed 16 November 2026 AEDT. Source-only update
SRC-RECOVERY-20261116R1 on main 7acfa465603cb36f7b29e1ad798be750325d8afc.
The owner requested permitted sources for the outstanding settlement fields.
No original card, audit, sporting grade, canonical ID, training run or model changed.

## Located fields

| Record | Field evidence | Route and retained limit |
|---|---|---|
| P-664 | Tappara U20 2-4 HPK U20, 14 November 2026, 13:00 +02:00. Periods 1-1, 0-1, 1-2. | [Tulokset](https://tulokset.live/jaakiekko/ottelu/tappara-hpk-2026-11-14-2710291): public HTML description and JSON-LD identify the U20 competition, exact date and completion. The rendered text alone was a placeholder. Upstream independence is UNKNOWN. |
| P-661 | Hobart after six completed overs: bounded 23-24 runs, below 41.5. | [Cricket Field Guide](https://cricketfieldguide.com/match/hobart-hurricanes-women-v-brisbane-heat-women-01m7er2qx1er4sc03wmscpg0h8): represented first-six runs 3+4+3+6+2+5=23; whole-innings represented runs85 versus total86; the page explicitly discloses one unplaced run. Do not invent whether it occurred before or after six overs. |
| P-662 | Adelaide after six completed overs: bounded 39-40 runs, below 41.5. | [Cricket Field Guide](https://cricketfieldguide.com/match/adelaide-strikers-women-v-perth-scorchers-women-01m7er2qx1erbbjrzatatsg1s7): represented first-six runs6+6+3+9+8+7=39; innings represented201 versus total202, with one unplaced run. |
| P-678 | England 19/1 after five completed overs. | [Guardian oldest page](https://www.theguardian.com/sport/live/2026/nov/15/australia-vs-england-cricket-second-odi-mens-one-day-international-adelaide-live-scores-updates?page=with:block-6af7b2a58f080d8d1c27a584). Select England's innings, not Australia's. |
| P-683 | Kashiwa CK4 plus Kawasaki CK3 = seven corners, 15 November, YLC, 17:03 JST, score5-4. | Official [Kashiwa](https://www.jleague.jp/en/club/kashiwa/) and [Kawasaki](https://www.jleague.jp/en/club/kawasakif/) club-record tables. Use the CK column; match date, competition, score, venue and time agree. These two pages are ONE official lineage. |
| Older P-647 queue | Urawa CK8 plus Cerezo CK4 = twelve corners, 11 November, YLC, 19:30 JST, score2-0. | Official [Urawa](https://www.jleague.jp/en/club/urawa/) and [Cerezo](https://www.jleague.jp/en/club/cosaka/) club-record tables. Do not use the return leg. ONE official lineage. |

The two WBBL feeds are provisional. The bounds describe only the acknowledged
unplaced run, conditional on the represented feed being otherwise correct; they
are not statistical confidence intervals. Represented wides/no-balls are already
included in the Runs column and must not be added a second time. Six overs means
six completed legal overs, not WBBL's separately defined powerplay. The Hobart
final partial over is included only in the whole-innings reconciliation.

The Field Guide's Perth final is151 while the retained audit says150. That conflict
is explicitly outside the Adelaide first-innings-only observation; do not silently
rewrite the opponent's score or promote all fields from this provider. The site
credits Cricsheet for historical balls, but the collector for these recent feeds
is not independently certified. Its own projections and inferred wicketkeepers are
not evidence for these settlement targets. No prediction output was used.

These observations identify sources for all 50 outstanding rows of P-660-P-685
(24 hockey, 22 WBBL, two England phase and two Kashiwa corner rows), plus the three
older P-647 corner rows. They do NOT themselves publish revised settlements.
Exact WBBL six-over scores still require corroboration; no particular allocation
of the missing run is asserted. Both endpoints of each retained interval lie on
the same side of41.5, providing a reviewable threshold-bound derivation.

## Permission, retrieval and lineage are separate

The current per-reader access snapshot is
[observations_20261116R1](../../external/access/observations_20261116R1/).
Sixteen hosts were rechecked; the other1,168 retain their original checked_at and
valid_until values. No old observation clock was made fresh by merging it. As a
result, the overall packet still requires its ordinary expiry refresh when any
retained host observation expires; this targeted recovery is not an all-host audit.

Cricket Field Guide and Guardian permit interactive CHATGPT_BROWSING and
CLAUDE_AGENT reading at these paths but refuse SCRIPT access. They were read with
the web tool, not downloaded by a disguised script. Local copying/parsing of a
retained interactive extract is not a new HTTP fetch. J.League and Tulokset allow
the checked readers/scripts. Before every later visit re-audit the exact path,
redirect and actual reader. This observation does not establish historical access.

ESPNcricinfo and Sofascore remain RULES_UNKNOWN; Cricbuzz remains BLOCKED. They
were not made permitted to close a queue. Jatkoaika is blocked for ChatGPT while
its Claude decision differs; the ChatGPT reader did not open it. The official
Leijonat scoring subdomain currently has no rules file, but its root returned403;
permission is not successful extraction. Elite Prospects has an allowed reader
decision and a matching search-index clue, but target-row rereads timed out; it is
not counted as a second opened final-score source. No proxy, alternate identity,
CAPTCHA bypass or blocked-page mirror was used.

J.League's match summary/stats view lacked extractable CK values, but the official
club-record tables supply the exact same event's values. The first Kashiwa read
was stale; a later explicit reread included15 November. Always require the dated
row, not the presence of a CK header. Two official pages do not create independent
corroboration. The incorrect guessed Cerezo path was abandoned; cosaka is verified.

## Added and preserved files

- [SETTLEMENT_SOURCES_ADDED.csv](SETTLEMENT_SOURCES_ADDED.csv) records eight opened
  exact-field routes, mirrored in the new current
  [SETTLEMENT_SOURCES.csv](../../source_routes/SETTLEMENT_SOURCES.csv). Eight scoped
  rows were appended to COMPETITION_ROUTES.csv; existing routes were retained.
- FINAL_EXACT_URL_AUDIT.csv distinguishes readers for the final paths. The current
  navigational SOURCE_ACCESS_AUDIT remains a union/SCRIPT view; the actual reader
  snapshot and settlement catalogue govern hand-reader admission.
- OBSERVED_OVER_RUNS.csv contains the represented innings runs, making the two
  interval reconstructions reproducible. FIELD_EVIDENCE.csv maps the observations
  and source-found dispositions to the outstanding contracts.
- CAPTURE_MANIFEST.csv binds source bodies/extracts kept outside Git in
  C:/Users/danie/Projects/source_recovery_captures_20261115/. Exact per-URL web-tool
  fetch clocks were not captured; their later retained_at is an explicit conservative
  knowledge bound, not a fabricated earlier retrieval/publication time. Script HTTP
  captures and robot observations have their actual recorded clocks.
- Pre-change controls/tables are byte-preserved in
  [archive/source_recovery_2026-11-16-1](../../../archive/source_recovery_2026-11-16-1/).
  Source URLs and short factual observations are in Git; full captures are external.

Current source entry points and the external upload index link the new catalogue
and mixed-clock access pointer. Statistical profile/kit v24.15 and MDS v24.20 remain
unchanged. Existing event manifests keep their pinned access artifacts; activate a
new committed access refresh explicitly for an already-open external event.

For settlement, reopen/reconcile the exact fields, write a dated parented revision
under prompt3 and verify readback/import under prompt4. CARD-TRAIN-v1 then runs on
the resulting effective labels as prescribed. This source update neither runs that
settlement nor backdates any feature's known-at time. Existing 50+3 unresolved
grade rows remain in the original logs until that revision is performed.

## Validation

All88 source-access and prompt-consistency tests passed (0.93 seconds). All22 external capture hashes, all9 archived control/table originals, all8 exact-field route bindings and all9 current external-package files passed verification. The original P-660-P-685 settlement and Combined Log Part10 match their committed bytes. No Python/workshop file changed, so the full948-test ML suite was not rerun for this source-only update. Source/permission findings are observations, not predictive validation.
