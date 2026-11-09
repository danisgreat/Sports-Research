# Log-source sweep and coverage follow-up ·9 November 2026

The source register now has **175 pregame source rows**, with **36 additional exact URLs** beyond the owner's R4 register. The competition catalogue has **300 rows**, including 64 additional field/discovery routes across 49 competition labels and all ten sports. **43 opened field/index observations** are documented, four as reference-only. No source is certified universally accurate, comprehensive, current or free of technical filters.

[Social, source-cycling and per-metric history procedure](../../source_routes/RESEARCH_COVERAGE_PLAYBOOK.md). [Mini lifecycle, review clocks and ML evidence](MINI_AND_LEARNING.md). [Exact source observations](FIELD_DECISIONS.csv), [new pregame rows](PREGAME_SOURCES_ADDED.csv), [candidate dispositions](CANDIDATE_FIELD_DISPOSITIONS.csv).

## Scope and owner changes

The structural sweep began at `ebe37cab429bc255801b3d8160d8390d60152bc0`. While it was running, the owner published R4 (`2356fbf90`, a separate source sweep) and R5 (`df9d2bea2`, model separation and per-game learning logs). This follow-up re-baselined to R5, preserved its changes and used the new 139-row PREGAME_SOURCES register as the addition baseline. The owner had already committed this sweep's initial CSVs unchanged in R5. Those dated inventories remain snapshots; the report and supplemental decisions are added here without replacing them.

This work is a source/coverage and status review, with retrospective outcome exposure. It creates no forecast, revised sporting grade, canonical ID, historical point-in-time feature or model promotion. The nine exact permanently closed contracts were not researched or reopened. Policy checks of retained references are distinct from retrieving a closed event's result; new content tests use current provider/news routes.

## Full structural sweep, then field-specific tests

[LOG_FILE_INVENTORY.csv](LOG_FILE_INVENTORY.csv) records complete-byte/line inspection of **370 artifacts**, 333 unique byte bodies and 34,888,319 bytes. It includes 19 canonical-log/index artifacts, 150 extracted issued originals/addenda and 201 mini, package or control artifacts. Duplicated bodies are scanned once. This is not a claim that 370 distinct issued minis exist.

The inventory covers all 638 retained canonical cards. [LOG_SOURCE_OCCURRENCES.csv](LOG_SOURCE_OCCURRENCES.csv) has **10,778 URL occurrences**, 2,992 distinct pointers and 775 host strings. [Source-host profile](SOURCE_HOST_PROFILE.csv), [card association coverage](CARD_SOURCE_COVERAGE.csv). Heading/wrapper associations are approximate: cross-card references, revisions, live views, old alias labels, bare domains and mixed review sections can associate a citation with the wrong phase or card. A zero associated-URL count does not establish that no source was researched. These tables are a structural inventory, not a semantic verification of every old pregame assertion.

Most frequently cited hosts include ESPN APIs, MLB, Basketball-Reference, AFL, NPB, ESPN, MLB Stats API, KBO, NHL, NBL, NBA and B.League. Current access checks reject many historically common paths: ESPN consumer pages, Basketball-Reference, Cricbuzz, Korean KBO and tennis.com block named agents; some ESPN API and ESPNcricinfo robots reads are unknown. MLB, NPB, NBL and several actual field-owner pages remain usable by the recorded routes. The exact path and check time control, not the reputation or age of the citation.

The initial sweep checked 3,563 exact URL paths against policy across 960 host strings; these include discovery and reference pointers, not just usable sporting data. The latest [consolidated table](ACCESS_OBSERVATIONS_CONSOLIDATED.csv) combines both agents' dated checks and the social follow-up into 3,982 exact URL observations, choosing the newest recorded check per URL. The source catalogue's latest access table is the same view; original check tables remain unchanged. A classifier may reuse a robots response within the bounded research session. A pre-use current audit is still required.

**Content testing is narrower than the policy inventory:** 84 candidate URLs, 65 successful raw retrievals, followed by manual field/freshness/lineage decisions. HTTP success, a 2026 marker and a nonempty title do not prove a usable field. [Candidate captures](CANDIDATE_RETRIEVALS.csv) preserve raw paths/hashes; [field dispositions](CANDIDATE_FIELD_DISPOSITIONS.csv) say what was actually admitted, rejected or limited. Normal supported readers were also tried for permitted Premier League, NWSL, ATP and Liiga paths; their missing tables, errors or shells were retained as failures. [External discovery/reader receipts](DISCOVERY_RECEIPTS.csv).

## Useful additions and limits

| Sport | Added evidence routes | What remains separate |
|---|---|---|
| Basketball | Timed NBA injury PDF; NBL all-club injury update; B.PREMIER/B.ONE/B.NEXT injury registrations; ACB round-7 medical bulletin; conditional EuroLeague reporting; Finnish federation incident/news and German/Lithuanian league discovery | Active list, medical status and confirmed starters are different fields; EuroCup is not EuroLeague; secondary injury trackers need per-player club checks |
| Baseball | MLB injury-story index and NPB current-year registration notices | Offseason reports do not establish a game lineup; MyKBO news sample was stale, Korean KBO registration blocked and CPBL links failed for the tested fields |
| Ice hockey | NHL projected lines, goalies, injuries/scratches and dated previews; AHL official news | A projection is not a confirmed goalie/lineup. Liiga raw/reader pages were shells; smaller leagues need their own sources |
| Australian rules | Separate AFLW finals injury article; AFL and Fremantle samples retained only as references | Men's AFL season-end and undated club tables are not current fitness evidence; no transfer from men's AFL to AFLW |
| Rugby league | Current international casualty report; NRL/NRLW injury-news navigation; Super League club-news routes | NRL hub table errors do not imply no injuries. A legacy NRL-season slug now carries World Cup content; scope the body |
| Rugby union | IRFU exact starting XV and bench announcement; World Rugby disciplinary/news discovery | Ireland only for that fixture; opponent and late replacements need separate confirmation |
| American football | NFL weekly practice/game-status tables and CFL division-final daily practice tables | Current NFL sample is regular season; playoff week needs recheck. CFL source is specific to its actual teams/week, not NCAA |
| Soccer | Separate A-League men/women extended squads and absences; dated MLS status report; club injury and J.League announcements; FAI national squad; UEFA lineup sample retained only as reference | Extended/camp squads are not starting XI or bench. A rolling post-event lineup page does not prove pre-kickoff knowledge |
| Cricket | Australia, England and India squad announcements; ICC relay of updated Pakistan squad; newer England withdrawal report | Different formats/game numbers have different squads. The newer withdrawal supersedes an initial list; none is a toss-confirmed XI |
| Tennis | WTA current event-state and news routes, including an explicit weather postponement | Does not supply every player's fitness or ATP/ITF history. ATP news raw/reader attempts failed; blocked archive subpaths remain blocked |

The NBA PDF is printed 8 November 17:00 ET; the NBL article says 8 November 14:00 AEDT despite a legacy `nbl26` slug. B.League's registration table is dated 6 November. The A-League squad reports are 5 November and still name omissions to be made. These are useful fields with explicit timing, not inferred starting lineups.

Basket.fi reports a **7 November live-statistics service incident** affecting its Synergy views and says statistics appear after the game. That is evidence of delayed publication, not absent play or an automatically repaired service. The current ACB round-7 bulletin supersedes the October round-5 sample. The opened ICC report of Josh Tongue's withdrawal supersedes his inclusion in the initial England ODI squad. These examples show why a page being reachable and a squad announcement being official are not enough for currentness.

The four reference-only samples are the AFL season-end injury table, an undated Fremantle table, the superseded initial England squad and a UEFA article retrieved after its matches. They are excluded from the 36 current-pregame source additions. Two conditional EuroLeague news sources are retained with their mixed-season/lineage limits; inferred missed-game flags from another tracker were not admitted as medical confirmation.

The [competition matrix](COMPETITION_COVERAGE_AFTER.csv) covers the existing exact competition labels. It does not upgrade every league from a major-league proxy or a generic federation index. The owner's R4 gaps—including broad soccer xG, WNBA/NCAA/KBL/PBA fields and several inaccessible specialist datasets—remain field-specific gaps until an actual compatible source is verified. Today's source sweep cannot retroactively certify old issue times, independent collectors, operator terms or all historical metrics.

## Social evidence and source cycling

The [new execution guide](../../source_routes/RESEARCH_COVERAGE_PLAYBOOK.md) operationalises the existing rules: verify organisation ownership, exact post, claim and media, separate publication/edit/retrieval clocks, distinguish confirmed selections from projections, trace shared lineage and recheck late changes. Social statistics need an explicit definition and match record; photos and training clips are not fitness certificates.

The tested X, Instagram and Facebook paths were blocked by the current eight-agent policy; they were not opened. YouTube and Bluesky passed policy and raw retrieval for the tested channel/root, but neither response established any game-specific fact. No account, transcript or general social API coverage is certified. Do not use old syndication, oEmbed or mirror instructions to work around a current restriction. Seek an organisation's own permitted web/PDF release or another original publisher's reporting of the same field, retaining its lineage.

For history, the guide supplies an event spine plus per-game metric observations and a L5/L10/L15/L20 coverage matrix. Missing metric values do not change window membership; each window reports actual observed n and missing/conflicting n. Different provider definitions, extra time and rate denominators cannot be silently mixed. The new blank templates assist A9 review; they are **not** an implemented new automatic coverage gate.

## Previous logs: what is and is not unresolved

At the verified state snapshot:

- **Active mini:** 0 cards; no active unsettled event.
- **Frozen league-day events:** 0 without settlement; both older NBA shadow events now have feedback.
- **Imported effective contract view:** 228 rows, 16 revised, 0 UNRESOLVED.
- **Permanent closures:** all nine corner contracts remain UNATTAINABLE / COMPLETELY_RESOLVED / DO_NOT_RETRY, excluded from sporting scores and ML labels.
- **Operative historical custody queue:** **P-126 and P-418 remain open**. P126 has unresolved original event/date/final identity; P418 lacks recovered original issued-contract custody. [Exact retained requirements](OPEN_CUSTODY_ITEMS.csv). Neither is silently graded by a plausible rematch or alias.

**The old statement “only two unresolved items” is incomplete if it is read as covering every generated reporting flag.** The full historical report additionally has **11 CONFLICT rows across seven already-settled cards**. The underlying logs document terminal outcomes; the reporting view collapses tied ranks or distinct original/live/imported versions. [Exact rows](REPORTING_CONFLICTS.csv):

| Cards / ranks | Reporting issue |
|---|---|
| P012 rank3; P013 rank2 | Different propositions share an explicitly tied/unordered tier, with opposite outcomes; these were PASS/abstention rows |
| P018 ranks2/3 | Original and five-ball live-update ranks are collapsed |
| P035 ranks1/2; P036 ranks1/2 | Separate version/contract views share ranks |
| P040 rank3 | Historical, controlling and withdrawn/replacement contract views are mixed |
| P060 ranks3/4 | Original controlling V01 and late imported diagnostic V03 rank different propositions |

These need **reporting-key reconciliation**, not another search for final scores or a guessed grade. The full key should preserve event, view and contract identity, including tied rank metadata. This source task exposes and records the defect; it does not modify the historical parser or claim it repaired these 11 flags.

The same historical view has 29 UNRESOLVED-labelled rows: 25 rank-zero placeholders (including P418) and four unactivated conditional/no-action P445 rows. They are not 29 pending win/loss settlements. [Classification](UNRESOLVED_VIEW_CLASSIFICATION.csv). Administrative labels, source certification gaps and unresolved sporting outcomes must not be pooled into one backlog count. Existing certification limits stay visible; no original evidence or timing is upgraded.

## Custody, reproducibility and verification

The original sweep inventory records exact source hashes and line hashes. [Baseline recheck](LOG_BASELINE_RECHECK.csv) distinguishes owner-edited controls from immutable issued records. This follow-up changes no canonical log, extracted issued original, active/frozen mini, contract revision, permanent-closure register, model release, runtime code or learning-store row. The replaced navigational documents/CSV views were archived byte-for-byte with the R5 base HEAD in [archive manifest](../../../archive/source_followup_2026-11-09-1/MANIFEST.csv).

The structural query reads log/index files, minis identified by filename or format/card markers, active-mini trees and extracted issued-research text/Markdown; deduplicates byte-identical bodies; binds canonical headings where the chronological identity map supplies them; and emits URL occurrences with line hashes and heuristic phase labels. It does not infer point-in-time proof from a URL. [External helper/input identities](QUERY_RECEIPTS.csv) preserve the precise research script/config hashes; raw captures/helpers remain outside the repository. Source paths/hashes and concise field extracts are retained in the committed tables if temporary raw captures later disappear.

The analyst metric query filters `card_history/CARD_ROWS.csv` to ANALYST_PRIMARY_V1, counted primary slots, numeric issued p and decisive WIN/LOSS; y=1 for WIN, Brier=mean((p-y)^2). Its paired comparison further requires a frozen baseline on the identical rows. [ANALYST_METRICS.csv](ANALYST_METRICS.csv). The separate saved NBA shadow evaluation is cited without refitting or pooling it with analyst cards. Current learning status and the zero-row new learning-log build are saved locally in this package. [Detailed interpretation](MINI_AND_LEARNING.md).

Verification results and publication readback are recorded in [VERIFICATION.md](VERIFICATION.md). Access tests and software tests establish recorded retrieval/implemented checks, not factual infallibility or predictive skill. No automated future research/review was scheduled.
