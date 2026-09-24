# Sources — quick reference


> **CR-2026.09.21-3:** all historical source-audit findings are reconciled in `AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md`; older source claims marked superseded/rejected there cannot be revived. CR-3 changes no source-admission semantics; it synchronizes the live control revision after rule read-back.


> **Current revision — 2026-09-19:** METHOD **MDS-2026.09.19-v4.3** is the workflow/template authority; **SCORING_AND_VALIDATION.md** controls conditioning, exact scoring, event-level evaluation and prospective evidence. All existing logs remain LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. NUMERICAL_PROGRAM controls authorized implementation scope and actual build state; MODEL_IMPLEMENTATION_RECIPES contains the executable Markdown reference. Older dated policy blocks are historical where inconsistent. No source, dataset or model is approved/fitted by this banner.




Status: **ACTIVE SOURCE REGISTER — NO H0 FIELD QUALITY-APPROVED YET. New in v4.0 comprehensive overhaul, 2026-09-06.**


This document is the compact source table the origin review (`FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md` §7.1) called for. `DATA_SOURCE_REGISTER.md` — now labelled the **full source register** — retains every dated addendum, full source-card audit trail, per-competition prose citation, and the numerical-approval gate mechanics in complete detail. Consult it when a specific source's full audit history is needed; this document is what's consulted per card.


**No source below is `APPROVED FOR FEATURE`.** A source being public, official, popular, searchable or technically accessible does not establish permitted automation, retention, redistribution, complete coverage, or a stable definition for numerical training. This table governs prediction-time research and settlement only.


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
## Universal minimum source and event-state standard — CR-2026.09.19-4 component (preserved under CR-2026.09.21-1)


Every event must use **at least three distinct reliable upstream source lineages**. Multiple pages that ultimately depend on the same feed/report count once. Search-result snippets, generated summaries, copied headlines and reposts are discovery only and do not satisfy the minimum.


Preferred event-verification mix, where available:
1. governing league/federation/field-owner exact-event source;
2. official club/team/participant source or second independent primary source;
3. independent high-quality secondary source.


Material identity, schedule, participant, availability and final-state facts must be reconciled across those lineages. If credible sources conflict, retain the conflict and fail closed rather than silently choosing one.


For every event verify the **venue-local date/time and IANA timezone** and convert it to `Australia/Melbourne` with the correct exact-date UTC offset and **AEST/AEDT** label. User-supplied start time is not authoritative until independently verified.


Settlement requires three independent reliable lineages explicitly agreeing that the event is terminal and giving the same final result. A score alone is not proof of finality. Any credible live/in-progress source blocks settlement. Search summaries never establish `FINAL`.


## 1. Status vocabulary


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
### 1.1 HARD source-independence firewall — predictive evidence


**PROHIBITED for forecasting:** sportsbooks/bookmakers/operators; odds aggregators and line-movement sites; betting previews, picks, tips, best-bet/handicapping/tout material; prediction-market or market-sentiment signals; fantasy/DFS projections, rankings, ownership, start/sit, waiver or optimizer output; and any article/model that merely republishes or transforms those signals. This includes **RotoWire, RotoGrinders and FPTrack** regardless of whether a particular page also contains a true factual statement.


A prohibited page may be used only as a **discovery pointer**. The fact must be re-retrieved from a valid upstream source before it can enter the forecast. If that cannot be done, record `UNAVAILABLE_FROM_VALID_SOURCE`.


**Factual lineup and availability disclosures:** Factual lineup cards, batting orders, morning skate line combinations, shootaround reports, and confirmed scratch notices reported by accredited beat reporters or official team media channels are **factual availability evidence**, not tout material. They are governed by Control `S-1 Rev 2` and may be used for pre-game participant and rotation modeling.


**User-supplied lines and totals are not sources.** They define the contract threshold and remain quarantined until after an independent predictive distribution has been frozen. No odds, implied probability, line movement or closing line may be used to set or calibrate the sports forecast.


### 1.2 Preferred source hierarchy by field


1. **Field owner / governing body / competition official:** schedule, rules, final result, gamebook/scorecard, roster/team sheet, official injury/availability release, official tracking/stat feed.
2. **Official team/club/player communication:** own-team availability, transactions, role/lineup announcements; scope is limited to what that entity can authoritatively know.
2b. **Credentialed beat reporting and official team media channels:** Accredited journalists (AP, regional newspapers, verified team beat writers, accredited broadcast desks, and official team PR portals/game notes). Scope: starter confirmations, batting orders, morning skate/shootaround line combinations, confirmed scratches/inactives, pitch limits, and rotation intent. Valid pre-game availability evidence under Control `S-1 Rev 2`.
3. **Independent structured sports-data provider with known lineage/definitions:** historical/process features where coverage and licensing are documented.
4. **Named reputable reporter / broadcaster / wire service:** availability, workload and tactical context, with timestamp and sourcing; corroborate material claims when possible.
5. **Generic derivative score/stat sites:** discovery/corroboration only unless a field-specific source card proves definitions, lineage and point-in-time fitness.


Web-search snippets are never evidence. A second website using the same upstream feed is not a second source.


### 1.3 High-value valid source lanes to expand


| Sport / field | Preferred primary lanes | Valid historical/secondary lanes subject to source-card admission |
|---|---|---|
| Baseball | MLB StatsAPI / official game feeds and Baseball Savant/Statcast; official NPB/KBO league feeds; official club transactions/lineups | process/stat databases with documented definitions and lineage; accredited beat reporters and official team PR game notes for batting orders, scratches, and bullpen availability (`PROJECTED_BEAT_VERIFIED`) |
| Cricket | ICC / national-board / competition official scorecards, toss/team sheets and rules | Cricsheet JSON for historical ball-level research with coverage/revision checks; accredited pitch-side reporters/broadcasters for pitch, toss, and XI availability |
| Soccer | FIFA/UEFA/competition/federation official match centres; official club lineups/injury releases | Hudl/StatsBomb open data where competition coverage exists; official club social/PR releases and accredited beat journalists for starting XI, bench, and tactical news |
| Basketball | NBA/FIBA/WNBA/NBL or competition official stats, injury reports and rosters; official club/team releases | independent structured stats with known lineage; accredited beat reporting and official team shootaround/pre-game notes for starters, inactives, and rotation intent (`PROJECTED_BEAT_VERIFIED`) |
| American football | NFL/competition official gamebooks, injury/practice reports, transactions and tracking products | nflverse sports-statistical lanes for historical research with lineage/definition checks; accredited beat reporters and official team 90-min inactives/depth charts |
| Ice hockey | NHL/competition official Gamecenter/stats/EDGE; official team roster/goalie news | independent structured stats with documented lineage; accredited beat reporters for morning skate lines, starting goaltender off-ice cues, and scratches (`PROJECTED_BEAT_VERIFIED`) |
| AFL | AFL official match centre, team sheets, injury/availability and club releases | government weather, official club team announcements (60-min pre-bounce), and accredited AFL Media reporting |
| Rugby league | NRL/competition official team lists, match centre, judiciary/availability and club releases | government weather, official club 24h/1h cut team announcements, and accredited rugby league beat reporting |
| Rugby union/sevens | World Rugby / union / competition official match centres, team lists and rules | government weather, official union/club 48h team sheets, and accredited rugby media for warm-up changes |
| Tennis | ATP/WTA/ITF official draws, results, rankings/order-of-play and tournament releases | accredited tennis journalists and tournament media for verified injury/withdrawal/strapping context; government weather for outdoor play |
| Weather/environment | National meteorological agencies (for example BOM/NOAA/Met Office equivalents) and verified venue/roof/surface owners | reputable local authority fallback where the primary national service lacks the required field |


These entries are **source priorities**, not automatic `APPROVED FOR FEATURE` status. Numerical admission still requires point-in-time coverage, definition, retention/licensing and quality checks in the full register/H0 card.




`CANDIDATE` (plausible lane, no H0 use) · `RESEARCH ONLY` (may support cited prediction-time research; no retained H0 ingestion) · `RESTRICTED` (licence/access/automation limits) · `BLOCKED` (access failure confirmed) · `PROHIBITED` (excluded as a settlement source entirely) · `APPROVED FOR SNAPSHOT` / `APPROVED FOR FEATURE` (numerical-training states; none reached yet).


## 2. The primary structured lane — `SRC-ESPN-SITE-API-*` (verified 2026-09-06)


The single highest-value discovery in this repository's history — keyless, structured, stable event IDs, JSON, no scraping.


```
https://site.api.espn.com/apis/site/v2/sports/<sport>/<league>/scoreboard?dates=YYYYMMDD
https://site.api.espn.com/apis/site/v2/sports/<sport>/<league>/summary?event=<eventId>
```


| Lane | Fields | Status |
|---|---|---|
| `SRC-ESPN-SITE-API-SOCCER` | Confirmed XI, bench, formation, referee, venue, attendance; `wonCorners`, possession, shots, fouls, cards, offsides, saves; final score and scorers | `CANDIDATE` — verified working |
| `SRC-ESPN-SITE-API-CRICKET` | Powerplay runs/wickets per innings; toss note; innings totals, target, winner flag; both XIs; full batting/bowling matchcards | `CANDIDATE` — verified working |
| `SRC-ESPN-SITE-API-BASEBALL` | `injuries[]` with status/body part; `gameInfo.officials` (umpire crew); plays, at-bats, win-probability series | `CANDIDATE` — verified working |


**Verified coverage (HTTP 200), 2026-09-06:** `soccer/eng.1`, `soccer/ita.coppa_italia`, `soccer/arg.1`, `soccer/fra.2`, `soccer/chn.1`, `soccer/mex.copa_mx`, `soccer/usa.usl.1`, `cricket/<seriesId>`, `baseball/mlb`.


**Route failures observed (HTTP 400), 2026-09-06:** tested league-slug routes for Liga MX Femenil, MLS NEXT Pro, Championnat National (FRA tier 3) and China FA Cup failed. This does not prove competition-wide non-coverage or prohibit targeted research through a correct event ID, official match centre or newly available provider.


**Route failures observed (HTTP 400), 2026-09-09:** **all Slovak competitions.** Ten slug forms tested — `svk.1`, `svk.2`, `svk.cup`, `svk.slovnaft_cup`, `svk.slovak_cup`, `svk.slovakia_cup`, `svk.fortuna_liga`, `svk.super_liga`, `slk.1`, `slovak.1` — all HTTP 400, with `eng.1` returning HTTP 200 as a positive control in the same pass. Independently corroborated by the core directory below. Slovak Cup / Slovnaft Cup is therefore outside this lane (`P-342-C03`).


**Coverage state — covered but stale (2026-09-09):** `soccer/uga.1` returns **HTTP 200** and resolves as **"Ugandan Premier League"**, but the feed was still on **season 2025 ("2025-26"), newest event 2026-05-23**, with zero events across 2026-09-01 → 2026-09-15. A 2026-27 fixture (`P-341-C03`) is therefore absent for a **season-rollover** reason, not a coverage reason. **Concrete retry trigger:** re-query `uga.1` for the target date once the feed advances to 2026-27. Distinguish this state from true non-coverage in every disposition note.


**The core league directory is NOT authoritative for what the site API serves — always probe the site API directly (2026-09-09).** `sports.core.api.espn.com/v2/sports/soccer/leagues?limit=1000` returns a complete 218-league list (`count` = 218) whose only sub-Saharan African entry is `rsa.1` — **and which omits `uga.1` entirely**, even though the site API serves that slug with a real league name. Treating the directory as the coverage test would have wrongly written Uganda off as uncovered. Use the directory only as *corroboration*: Slovakia is absent from **both** the directory and every site-API probe, which is why that non-coverage finding is solid, whereas a directory-only absence proves nothing.


**Access note:** earlier tested requests failed with a custom browser User-Agent while default-client requests succeeded. This is an observation about those requests, not a universal header rule; record route, date and response before generalizing.


## 3. Cross-sport lanes


| Source ID | Role | Status |
|---|---|---|
| `SRC-OFFICIAL-EVENT-*` | Identity, schedule, rules, participants, live state, official final | `CANDIDATE` |
| `SRC-OFFICIAL-STATIC-REPORT-*` | Dated official report/gamebook fallback when a dynamic page is stale or inconsistent | `CANDIDATE` |
| `SRC-GOV-WEATHER-*` | Venue-local game-window forecasts/observations — **mandatory for every outdoor `G15.1` gate**; a city forecast does not satisfy this | `CANDIDATE` |
| `SRC-MARKET-OPERATOR-*` / `SRC-MARKET-ARCHIVE-*` | Exact user-requested contract/action terms only when explicitly needed after forecast freeze; never sporting evidence | **`CONTRACT_ONLY / PROHIBITED_PREDICTIVE`** |
| `SRC-STATMUSE-RESEARCH` | Transient searchable splits/hypothesis checks | `CANDIDATE` — attribution and no-systematic-retention terms apply |
| `SRC-REPORTING-NAMED-*` | Late injury/role/lineup/pitch reports pending official confirmation | `CANDIDATE` |


## 4. Synthetic-content exclusion — `L-079` (hard, applies to every lane)


Content generated, simulated, projected or previewed — labelled "AI Simulation," "simulated," "projected result," "prediction," "preview," "who will win," "Dream11," "fantasy tips," "expert tips," or produced by a model rather than a scorer — is `PROHIBITED` as a settlement source regardless of how complete the narrative appears. `sportscafe.in`'s "AI Simulation" articles are the confirmed origin case: a fabricated `P-305` report with the wrong winner, margin, venue and player of the match, indexed alongside genuine scorecards. A search-result *summary* is not a source; open the underlying record and confirm it is a scoreboard/scorecard, not a narrative article, before any figure enters a settlement.


## 5. Per-sport lanes


### Cricket
`SRC-CRIC-OFFICIAL-*`, `SRC-CRIC-BOARD-BRANDED-SCORECARD`, `SRC-CRIC-ICC-MATCH` — event/format/toss/XI/scorecard/result — `CANDIDATE`. `SRC-CRIC-OFFICIAL-VIDEO-*` / `SRC-CRIC-RIGHTS-BROADCAST-TOSS-*` — match-specific toss/XI/pitch evidence — `RESEARCH ONLY`. `SRC-CRIC-NVPLAY-OFFICIAL-*` — sanctioned board/competition Match Centre lane where applicable — `CANDIDATE / RESEARCH ONLY`. `SRC-CRIC-BROADCAST-TRANSCRIPT-*` — transcript/access lane to a named broadcast, counted as the **same lineage as that broadcast**. `SRC-CRIC-AUTOMATED-PITCH-METADATA-*` — weak structured context only; never a human observed strip. `SRC-CRIC-CRICSHEET-JSON`/`-REGISTER` — historical delivery data, versioned — `CANDIDATE`. `SRC-CRIC-SPECIALIST-SCORECARD`, `SRC-CRIC-PITCH-REPORT` — `CANDIDATE`. `SRC-CRIC-ICC-PITCH-RATING` — official retrospective venue-reputation context — `CANDIDATE`. `SRC-CRIC-CRICVIZ-PITCHVIZ` — citation-only, numeric index not publicly exposed. Native-language sourcing (`L-067`) applies to non-English-primary boards. Current toss/strip protocol: separate TOSS FACT and STRIP/PITCH ladders in `DATA_SOURCE_REGISTER.md` §6A / `RULES_CRICKET.md` §2.


### Basketball
`SRC-BB-LNBP-OFFICIAL` and equivalents — `CANDIDATE / RESEARCH ONLY`; access reliability audited and found inconsistent (403 on scripted access to `lnbp.mx`) — treat as `RESTRICTED` in practice until re-verified.


### American football
`SRC-AF-OFFICIAL-*`, `SRC-AF-CFL-OFFICIAL` — rules/rosters/injuries/state/final — `CANDIDATE`. `SRC-AF-NFLVERSE-PBP`, `SRC-AF-NGS-*` — `CANDIDATE`/`RESTRICTED`. `SRC-AF-GOV-WEATHER` — `CANDIDATE`, mandatory for outdoor venues.


### Baseball (`PRIMARY_SCORED` — see `METHOD.md` §2)
`SRC-BS-OFFICIAL-LEAGUE-*` (MLB `statsapi` gives field-relative wind and umpires — the best structured data of any population here), `SRC-BS-NPB-BIS`, `SRC-BS-KBO-OFFICIAL`, `SRC-BS-CPBL-ADVANCED`, `SRC-BS-MILB-OFFICIAL-SCORE`, `SRC-BS-LMB-OFFICIAL-CLUB` — `CANDIDATE`. `SRC-BS-MLB-STATCAST` — `CANDIDATE`, tracking-era regime caveats. `SRC-BS-RETROSHEET-EVENT` — historical, `CANDIDATE`. `SRC-ESPN-SITE-API-BASEBALL` (§2 above) is the fastest-verified lane for injuries/officials/state.


### AFL/AFLW (`PRIMARY_SCORED`)
`SRC-AFL-OFFICIAL-*` — `CANDIDATE`. `SRC-AFL-SQUIGGLE` — external-model consensus, **`DISCOVERY_ONLY / NOT PREDICTIVE EVIDENCE`**; it may not anchor this project's forecast. `SRC-AFL-BOM` — venue weather, `CANDIDATE`, mandatory for outdoor grounds.


### Rugby league / union
`SRC-RL-OFFICIAL-*` (NRL — `PRIMARY_SCORED`), `SRC-RL-GOV-WEATHER` — `CANDIDATE`. Rugby union: `SRC-RU-WORLD-RUGBY-LAWS`, `SRC-RU-OFFICIAL-COMP-*`, `SRC-RU-NZR-NPC-*`, `SRC-RU-SPECIALIST-STATS-*` — `CANDIDATE`, qualitative-only (no numerical model authorised).


### Soccer (`PRIMARY_SCORED` — EPL specifically)
`SRC-SOC-OFFICIAL-*`, `SRC-SOC-UEFA-MATCH`, `SRC-SOC-OFFICIAL-CLUB-REPORT` — `CANDIDATE`. `SRC-ESPN-SITE-API-SOCCER` (§2) is the primary EPL lane, verified for `wonCorners` and full match stats. `SRC-SOC-STATSBOMB-OPEN` — selective historical, `CANDIDATE`. `SRC-SOC-XG-*` — provider-dependent, `CANDIDATE / RESTRICTED`, never mix providers silently. **Negative source-state example, retained as a standing warning:** the Uzbekistan PFL match centre stayed an all-zero 0-0 placeholder while independent reports documented a real 0-4 result — a placeholder is never converted into a final.


### Tennis
`SRC-TEN-ATP-WTA-ITF-*`, `SRC-TEN-OFFICIAL-EVENT-*` — `CANDIDATE`. `SRC-TEN-SPECIALIST-STATS-*`, `SRC-TEN-TENNISCOM-CURRENT` — cross-check tier, official score controls conflicts.


### Ice hockey
`SRC-IH-NHL-OFFICIAL` — `CANDIDATE`. `SRC-IH-MONEYPUCK-DL`, `SRC-IH-SPECIALIST-SHOTS-*` — `CANDIDATE / RESTRICTED`. `SRC-IH-METALLIGAEN-OFFICIAL`, `SRC-IH-AIHL-SPECIALIST` — no league-branded structured feed located; specialist reporting only.


## 6. Re-graded / newly excluded (2026-09-06)


| Source | Change |
|---|---|
| `api.sofascore.com` | Downgraded `CANDIDATE → BLOCKED` — `403 Forbidden` on every programmatic route tested; interactive page fetches may still work |
| `sportscafe.in` "AI Simulation" articles, and any similarly-labelled content | `PROHIBITED` — see §4 |
| ETPL powerplay via `etplofficial.com` | Prior "no reproducible source" cap **withdrawn** — `SRC-ESPN-SITE-API-CRICKET` supplies the field reproducibly |
| ESPNcricinfo via `r.jina.ai` proxy | `CANDIDATE — cross-check only`; agreed exactly with the direct API in both tested cases; prefer the structured API directly |


## 7. Approval gate (numerical use — unaffected by this consolidation)


A field moves to `APPROVED FOR FEATURE` only after access/use terms, exact coverage, identities, definitions, rules eras, correction replay, prediction-time `known_at`, completeness, uniqueness, ranges, joins, negative controls and feature admission all pass (`DATA_SOURCE_REGISTER.md` §16). **No source in this document has passed that gate.** Full mechanics, market-snapshot schema, and the complete session-by-session access audit trail: `DATA_SOURCE_REGISTER.md`.


## 2026-09-06(f) — settlement and retrospective addendum


[Event-specific source table and limitations](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#general-learnings-rule-changes-observations-and-sources). Newly demonstrated coverage: official Chance Liga event 8382 supplies P-304 corners (Slavia 5, Brno 1), team/bench and substitution fields; it declares Stats Perform lineage. ESPN soccer mex.1/event 401876990 supplies P-290 corners (Juárez 1, Pachuca 3). No feature-admission approval is implied.


ESPN cricket 1547871/event 1547886 freshly confirms P-305 toss/PP/innings. ESPN cricket 1534175/event 1534200 confirms P-217 revised innings and mandatory PP **24/2 in 4.5**, not six overs. ESPN/ESPNcricinfo related endpoints count as one lineage. A cricket league-0 timeout is a failed request, not proof of non-coverage; the specific series routes succeeded.


Fresh supporting sources include official CPL and Wofford reporting, the official AFL P-315 report, MLB StatsAPI event feeds, completed Tennis.com match records and a named Xports News KBO venue report. KBO's official body was unpopulated; other human-report re-fetches were limited. A surfaced Nate `[AI상보]` report was excluded; “Nate + another hostname” is not automatically two independent sources. Earlier categorical HTTP/coverage claims are narrowed to their actual tested routes. Remaining eight corner fields are unconfirmed; no failed fetch upgrades a provisional result.


## 2026-09-09 — sources demonstrated during the `P-333`–`P-344` reconciliation


Full detail: `DATA_SOURCE_REGISTER.md` §"2026-09-09"; card mapping: `PREDICTION_LOG_COMBINED_3.md` §"2026-09-09". None reaches `APPROVED FOR FEATURE`; all are prediction-time research / settlement lanes.


| Source | Role | Grade | Note |
|---|---|---|---|
| **Asian Cricket Council** `asiancricket.org/match/<id>` | Field-owning scorecard / innings state for ACC events (Women's T20 Asia Cup — `P-333`, `P-343`) | `CANDIDATE` — field owner for ACC | Use ahead of aggregators for ACC finals |
| **FIBA** game-center reports + team/player profiles `fiba.basketball/en/events/.../games/<id>`, `.../teams/<team>/<playerId>` | Field-owning result, per-player tournament minutes, tournament context (`P-334`, `P-344`) | `CANDIDATE` — field owner for FIBA | Player-profile minutes confirmed Hayashi's 8-minute game post-hoc |
| **KBO** Korean-language news + `koreabaseball.com` scoreboard; **SBS English** `news.sbs.co.kr/english` as an English rung | Field-owning KBO final + match detail (`P-339`); SBS English an accurate independent English cross-check for KBO / K League | `CANDIDATE` — reinforces `L-067` | Korean body page still often slow/unpopulated; SBS English fills the English gap |
| **Kawowo Sports** `kawowo.com` | Specialist current Uganda football result + goal timeline when the league official match detail is sparse (`P-341`) | `CANDIDATE — RESEARCH ONLY / cross-check` | Not automatically a corner-stat field owner |
| **GHANAsoccernet** `ghanasoccernet.com` | Independent African-league result/scorer confirmation (`P-341`) | `CANDIDATE — RESEARCH ONLY / cross-check` | Secondary; corroborated Kawowo |
| **PlaymakerStats / zerozero / ceroacero / leballonrond** family | Post-final structured soccer fields — shots, SOT, corners, xG where present (`P-336`, `P-337`; Part-2 `P-178`/`P-176` update) | `CANDIDATE — RESEARCH ONLY / cross-check` | Declares Stats Perform lineage on some competitions; **still secondary** to an official/data-partner definition — aggregator agreement does not promote a niche field (`G10.2`/`L-081`). Often HTTP 403 to `WebFetch`; readable via search snippets. |
| **Futbol24** `futbol24.com` | Minute-by-minute event timelines incl. reconstructable corner events (`P-340`) | `CANDIDATE — RESEARCH ONLY / cross-check` | Provenance-clear cross-check only |
| **Forebet** post-final corner display | Corroborates niche corner counts in sparse competitions (`P-342-C03`; Part-2 `P-178`) | `CANDIDATE — RESEARCH ONLY / cross-check` | Cannot repair an unfrozen operator/provider definition |
| **matchcalendar.football** | Independent K League 1 result + scorer cross-check (`P-340`) | `CANDIDATE — RESEARCH ONLY` | Secondary aggregator |
| **`site.api.espn.com` public web box scores** `espn.com/fiba/boxscore`, `/soccer/match`, `/mlb/game` | Independent final confirmation for `P-335`/`P-336`/`P-337`/`P-338`/`P-344` | `CANDIDATE` — same lineage as `SRC-ESPN-SITE-API-*` (§2) | `fiba` box scores are exposed on the public web renderer; reliable settlement cross-check |


**Route-specific access observations (2026-09-09):** `ceroacero.es`, `forebet.com`, `sofascore.com` match pages returned **HTTP 403** to `WebFetch`; content still recoverable via `WebSearch` snippets. Consistent with the standing `api.sofascore.com` `BLOCKED` note. No niche corner field was upgraded from any of these; `P-341-C03` remains `UNSETTLEABLE` and `P-342-C03` `PROVISIONAL`.


## 2026-09-11 — sources demonstrated during the `P-345`–`P-371` reconciliation


Full detail: `DATA_SOURCE_REGISTER.md` §"2026-09-11"; card mapping: `PREDICTION_LOG_COMBINED_3.md` §"2026-09-11". None reaches `APPROVED FOR FEATURE`; all are prediction-time research or settlement lanes.


| Source | Role | Grade | Note |
|---|---|---|---|
| **UEFA `matchstats.uefa.com/v1/team-statistics/{matchId}`** (FAME provider) | Field-owning team statistics for UEFA club competitions — corners, attempts, attempts on target, possession, both teams | **`CANDIDATE` — field owner** | Settled `P-345-C03` (Brugge 4) and `P-346-C05` (10); verified three finals. Keyless JSON; **use `curl` and parse the array** — the WebFetch summariser returns only one team. Pre-register it for UEFA derivative rows (`RULES_SOCCER.md` control 30). |
| **FotMob match pages via `r.jina.ai`** | Opta-sourced FT/HT, shots, shots on target, possession, corners for leagues ESPN does not carry (A-League / Australia Cup, UAE Pro League) | `CANDIDATE — STRUCTURED SECONDARY` | Settled `P-355-C05` (its pre-registered provider); a third lineage on the UAE corner rows. Field-owner grade only where a card pre-registers it. Direct FotMob/Sofascore APIs remain blocked. |
| **KBO English scoreboard** `eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=YYYY-MM-DD` | Field-owning KBO line score, winning/losing/saving pitchers | `CANDIDATE — field owner` (English rung, `L-067`) | Verified `P-356`, `P-362`. |
| **FIBA game pages** `fiba.basketball/en/events/<event>/games/<id>` | Quarter scores, team shooting splits, biggest lead | `CANDIDATE — field owner` (reconfirmed) | `P-358`, `P-367`, `P-371`. |
| **ESPNcricinfo via `r.jina.ai`** | Live Test state; full scorecards (incl. the Windhoek T20Is that `P-352` set aside) | `RESEARCH` route | Direct fetch HTTP 403. The proxy can return a cached page — check the page's own state/time. |
| **MLB statsapi via `curl`** | MLB finals and linescores | field owner (existing) | **WebFetch returns HTTP 406**; a plain client works. `battingOrder` in the live feed is a candidate lineup route, not yet tested pre-game. |
| **Tennis Abstract Elo** `tennisabstract.com/reports/atp_elo_ratings.html` | Independent overall and surface Elo, with its update date | `CANDIDATE — BENCHMARK ONLY` | `P-350`: dated 2026-08-31 (pre-event); implied Alcaraz ≈71–77% best-of-five v the card's 76%. Never sets a probability (`RULES_TENNIS.md` control 13). |
| **Cricket Ireland-branded CricketArchive** | Full ETPL scorecards with XIs, fall of wickets, bowling figures | `CANDIDATE` ETPL settlement lane (reconfirmed) | `P-357`, `P-366`. |
| Guardian / VI match-stat corner counts | Media match statistics | **Re-graded: cross-check only** | Each was wrong by one corner against UEFA FAME (`P-346`, `P-345`). Never settles a derivative within ±1 of its line. |
| ETPL first-party match page | Competition status | status only | Stayed a stale "Yet to bat" shell for more than 24 hours after Match 19; later COMPLETED, still without scores. |
| ClubElo API `api.clubelo.com` | Cross-league club-strength rating (would have served `RULES_SOCCER.md` control 31) | **ACCESS FAILED (route-specific)** — not graded | 0 bytes on http and https, with and without a browser agent, from this environment. |
| ESPN `soccer/uga.1` | Uganda Premier League (retry trigger for `P-341-C03`) | covered-but-stale | Re-probed 2026-09-11: still season 2025, 0 events on 2026-09-08. |


**Route observations (2026-09-11, route-specific):** the WebFetch summariser truncates multi-entity JSON arrays — fetch raw JSON with `curl` and parse it; the A-Leagues match centre renders no statistics to a fetch; the UAE Pro League match centre shows corners as "–" (no field-owner corner lane found for that league).
# 2026-09-12 retrieval corrections (read before older source notes)


Source approval is field-specific. Re-open the exact event, season, sex/team level, date, phase and provider identity. Record publication time separately from retrieval time. A final score does not certify corners, lineups, weather or a causal explanation. Postgame lineup recovery is never labelled pregame confirmation. Multiple websites, mirrors and embedded widgets may share one upstream feed.


| Preferred route / current finding | Appropriate future use | Limit |
|---|---|---|
| [NPB dated box and inning record](https://npb.jp/bis/eng/2026/games/s2026091001427.html), dated roster pages | Innings, scoring checkpoints, starting orders, pitching workload | A roster list is not a complete role-labelled bench or pregame capture |
| [Official CPBL statistics gamebook](https://stats.cpbl.com.tw/schedule/2026-A-321) | Exact game ID, runs versus earned runs, innings, walks | League landing-page placeholders require the linked actual statistics page |
| [MLB exact live feed at Final](https://statsapi.mlb.com/api/v1.1/game/823983/feed/live) | Game ID, starters, innings and extra-inning scoring | Final bench is not automatically the originally nominated full bench; action terms remain separate |
| [CPL official newsroom](https://cplt20.prezly.com/falcons-close-in-on-playoffs) | Original competition reports, phase scores and chronology | Match report may omit full XI/reserves and exact pitch evidence |
| [FIBA exact match](https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128150-BEL-GER) | Quarter totals, lead changes, attempts where actually exposed | Twelve-player roster does not establish the starting five; fetch full box before bench/rebound attribution |
| [Toluca club match report](https://www.tolucafc.com/noticias/merecido-finalista) | Exact fixture, XI, used substitutes, coaches, first goal | Unused bench may be absent; official reports can differ by a minute on disciplinary events |
| [NRL match chronology](https://www.nrl.com/news/2026/09/10/thursday-night-footy-roosters-v-bulldogs/) | Late team news and verified postgame HIA/card chronology | Later HIA/substitutions cannot be backdated to pregame knowledge |
| [WTA match page](https://www.wtatennis.com/tournaments/us-open/scores/LS74150432) plus [LTA report/profile](https://www.lta.org.uk/fan-zone/british-tennis-players/francesca-jones/) | Final set scores with corroboration | This WTA extraction mixed state labels and incomplete service-game totals; quarantine those fields |
| [Sportnet Lucenec-Komarno commentary](https://sportnet.sme.sk/spravy/futbal-lucenec-komarno-online-prenos-3-kolo-slovnaft-cup-2026-2027/) | Secondary exact score/chronology | Embedded Onlajny is the same lineage; no certified full corner tally |
| [Sofascore Sikkim exact pairing](https://www.sofascore.com/football/match/aakraman-sc-sikkim-boys-club/zxuhsicEi) | Candidate identity/result lead only | Explicit community editor; cannot resolve the inherited organiser-level conflict alone |


Sporting Life betting-tips/in-play previews are excluded from future MARKET_BLIND feature retrieval even when they contain weather/pitch prose; locate the original non-market sporting source. Ignore prediction/odds widgets adjacent to otherwise useful score data. ESPN's empty 2026-09-08 Uganda query returned a stale 2025-26 season, not proof that no match occurred. UAE official fixture shells did not expose current corner totals. [Full evidence and limitations](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-12.md). All new lanes remain RESEARCH ONLY/CANDIDATE; no H0 feature approval or bulk-ingestion permission is implied.


## 2026-09-15 — sources demonstrated during the `P-364` final settlement and queue retry


None reaches `APPROVED FOR FEATURE`. Route observations are specific to this environment and date. Detail: [combined log §"2026-09-15"](PREDICTION_LOG_COMBINED_3.md) §6.4.


| Source | Role | Grade | Note |
|---|---|---|---|
| **ESPNcricinfo series results page via `r.jina.ai`** — `espncricinfo.com/series/<slug>/match-schedule-fixtures-and-results` | Every result in a series plus links to every full scorecard | `RESEARCH` route — **new; use first when building a current-series innings prior** (`RULES_CRICKET.md` controls 27–28) | Recovered England's Leeds/Lord's innings records for `P-364`. |
| ESPNcricinfo full scorecard via `r.jina.ai` | Settlement of Test results; innings runs/overs; day-by-day close-of-play log | `RESEARCH` route (reconfirmed) | Direct fetch HTTP 403. Check the page's own day log ("end of match") to rule out a cached copy. |
| Wikipedia series article | Result, scores, player of the match | **Corroboration only** | Agreed with ESPNcricinfo; probably the same upstream lineage — never counted as an independent scorer. |
| Web-search engine result summary | — | **Excluded** | Reported England's chase as "132 for 2"; opened scorecard 130/2. Quarantine every number in a search summary. |
| Cricbuzz; NDTV Sports | Live/complete cricket scorecards | `ACCESS FAILED (route-specific)` | WebFetch "unable to fetch" on 2026-09-15; try `r.jina.ai` next time. |
| ESPN site API `soccer/uae.1`, `are.1`, `uae.pro_league`, `uae.league` | UAE Pro League corners | **Verified non-coverage** (HTTP 400 × 4) | Add to the §2 non-coverage list: UAE Pro League has no ESPN route. `P-368-C02` / `P-369-C01` stay provisional. |
| ESPN site API `soccer/uga.1` | Uganda Premier League corners | covered-but-stale (unchanged) | Re-probed 2026-09-15 06:06 UTC: season 2025, 0 events on 2026-09-08. |




## 2026-09-15(b) — sources demonstrated during the `P-373`–`P-423` import


None reaches `APPROVED FOR FEATURE`. Access observations are route- and date-specific.


| Source | Role | Grade | Note |
|---|---|---|---|
| **Premier League official data** — `footballapi.pulselive.com/football/competitions/1/compseasons`, `/football/fixtures?comps=1&compSeasons=841&page=0&pageSize=40&sort=desc&statuses=C`, `/football/stats/match/<fixtureId>` | EPL field owner: final score, `won_corners`, `corner_taken`, `total_scoring_att` per team | **`CANDIDATE — FIELD OWNER`** (new; highest-value find of the pass) | Requires headers `Origin` and `Referer: https://www.premierleague.com`; `compSeasons` must be an integer (841 = 2026/27; a float returns HTTP 400). Settled P-402-C02/C03 (5+6) and P-408-C01 (Brighton 3). Pre-registered for EPL derivatives (soccer control 32) |
| ESPN site API — soccer `bel.1`, `fra.1`, `ger.1`, `swe.1`, `esp.1`, `ita.1`, `jpn.1`, `uefa.champions` | Final, goal minutes, `wonCorners`, both XIs + benches | `CANDIDATE` — coverage verified 2026-09-15 | Corner counts matched the Premier League record (P-402, P-408) and J.League `CK` (P-387). Stays **provisional** for rows that did not pre-register it |
| ESPN `soccer/gua.1` | Guatemala Liga Nacional | covered for score only | Summary returned **no statistics** — cannot settle P-377-C02 |
| ESPN `australian-football/afl`, `rugby-league/3` (NRL), `football/nfl` | Finals | `CANDIDATE` — verified | Re-verified P-386, P-388, P-396, P-397, P-376, P-412–P-414, P-422 |
| ESPN `soccer/bhu.1` | Bhutan | **HTTP 400** | No route |
| MLB statsapi `api/v1/game/<gamePk>/boxscore` | Starting pitcher, IP, R/ER, pitchers used | field owner (existing lane; new endpoint noted) | Confirmed all four log-C starters |
| NPB English `npb.jp/bis/eng/2026/games/gm<YYYYMMDD>.html` and box `s<gameId>.html` | NPB finals, line score, pitchers, HR | field owner (reconfirmed) | P-381–P-383, P-405, P-417 |
| KBO English scoreboard | KBO finals | field owner (reconfirmed) | P-384, P-385 |
| FIBA game page `fiba.basketball/en/events/<event>/games/<id>` | Quarter scores, shooting, biggest lead | field owner (reconfirmed) | P-411. A search summary gave the top scorer as 22 points; FIBA's page shows 28 — the search number was not used |
| **BBS — Bhutan Broadcasting Service** round reports (`bbs.bt`) | National broadcaster: dated round results and standings | `RESEARCH` (new) | 2026-09-15 report used for P-418's identity conflict |
| **Bhutan Football Federation** (`bhutanfootball.org`) match reports | Competition-owner reports | `CANDIDATE` (new) | Search listing is undated — open the article for its date before use |
| J.League official club result table (`CK` field) | J1 team corners | `CANDIDATE — FIELD OWNER` (from log A) | Settled P-387-C03 |
| Real Racing / LALIGA embedded event feed | LALIGA timeline and corner events | `CANDIDATE` (from log B) | P-398 |
| Liga Bantrab official feed; Guatefutbol | Guatemala final / local narrative | final score owner / secondary (from log A) | No corner field |
| Yahoo! Japan SportNavi | NPB native-language corroboration | secondary (from log B) | P-405 11-inning detail |
| Statz, OFStats, PlayerStats, ScoreBat, FootyMetrics | Soccer corner/score corroboration; ETPL scorecards (Statz) | `SECONDARY — corroboration only` (from log B) | Never settle a derivative alone |
| Sofascore, AiScore (web) | — | `ACCESS FAILED` (HTTP 403, 2026-09-15) | — |


**Route observations:** WebFetch/WebSearch reached a spend limit during this pass; plain `curl`/Python requests to keyless JSON endpoints (ESPN, MLB, Premier League) were unaffected — another reason to keep structured lanes first.


## 2026-09-16 — sources demonstrated during the queue retry and the C′ reconciliation


None reaches `APPROVED FOR FEATURE`. Route observations are specific to this environment and date. Detail: [combined log 3 §"2026-09-16"](PREDICTION_LOG_COMBINED_3.md); registry form in `DATA_SOURCE_REGISTER.md` §"2026-09-16".


| Source | Role | Grade | Note |
|---|---|---|---|
| **ESPN site API — cricket** `cricket/<seriesId>/summary?event=<id>` → `notes[]` (matchnotes grouped by innings `section`) | Exact phase checkpoint per innings: `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - N runs, W wickets)` | `CANDIDATE — settles phase rows` (reconfirmed; **use first**) | Settled `P-406-C01/C04` (series 1547871, event 1547895, note 767111: Edinburgh 68/2). Find the event via `cricket/<seriesId>/scoreboard?dates=YYYYMMDD`. Valid only for a full 6.0-over powerplay |
| ESPN site API — NFL `scoreboard?dates=<year>&seasontype=2&week=N` + `summary` `scoringPlays` | Season reference base rates | `REFERENCE_BASE_RATE` lane (new use) | 2025: 272 games; margin exactly 3 = 15.1 %, exactly 7 = 9.6 %; non-offensive TDs 0.217 a game |
| ESPN site API — soccer `keyEvents[]` | Red cards, penalties, goal minutes at settlement | `CANDIDATE` (soccer control 34) | Found the P-408 and P-419 red cards the canonical settlement omitted |
| MLB statsapi `api/v1.1/game/<gamePk>/feed/live` | Inning line score, every pitcher line, HR plays, weather, umpires | field owner (existing) | Verified C′'s MLB facts; caught its P-421 error |
| **bundesliga.com match `stats` page** | Would own Bundesliga corners | **`JS_ONLY / BLOCKED`** | Direct `curl` HTTP 403; `r.jina.ai` raw text = all-zero placeholders. A WebFetch summary's "corners 7–7" is **not on the page** — excluded (`G-L13`) |
| allsvenskan.se `matcher/<year>/<id>/<slug>` | Would own Allsvenskan match facts | `JS_ONLY` (cookie wall) | P-419 `6529990` |
| plus.ligue1.com `live/<id>` | Would own Ligue 1 match facts | `JS_ONLY` (empty raw text) | P-409 `306887` |
| proleague.be `wedstrijden/seizoen-<yyyy-yyyy>-jupiler-pro-league-<md>-<home>-vs-<away>` | Would own Pro League match facts | `NOT FOUND` for 2026-27 (404) | P-407 |
| Sky Sport Italia `…/partite/<year>/giornata-<n>/<slug>/tabellino-statistiche` | Serie A stats incl. corners | `SECONDARY` (broadcaster; provider unstated) | P-399 8–9 (same as ESPN) |
| **RSSSF** `rsssf.org/tablesb/<country><year>.html` | Sparse-league round-by-round fixtures, results, tables, "Last updated" footer | `RESEARCH` (new) | Bhutan 2026 R15 [Sep 14] Drukpa – RTC unscored (updated 11 Sep) — corrected the P-418 record. Read the raw HTML |
| BBS `bbs.bt/<id>` via `r.jina.ai` | Dated Bhutan round reports | `RESEARCH` — **date from `Published Time`** | 244138 = 2026-07-12; 244289 = 2026-07-17 |
| NFL.com player game logs; Reuters; club match reports; Guardian match stats; StatMuse FC; SoccerNews; Global Sports Archive; RedScores (all from C′) | Player logs / narrative / stat displays | NFL.com player logs `CANDIDATE — field owner`; the rest `SECONDARY` | Guardian/StatMuse/SoccerNews had Leipzig 7 corners where ESPN has 8 |
| Pro-Football-Reference via proxy | Season tables | `ACCESS BLOCKED` (security verification) | Not bypassed; ESPN used |
| WebFetch output / search-engine summaries | — | **Excluded as a record** (`G-L13`) | Three errors this pass (Bundesliga corners, BBS date, RSSSF score orientation) |


### 2026-09-16(b) — lanes exercised while re-probing the documentary-audit rows


| Source | Role | Grade | Note |
|---|---|---|---|
| **UEFA match finder** — `match.uefa.com/v5/matches?fromDate=YYYY-MM-DD&toDate=YYYY-MM-DD&competitionId=<id>&offset=0&limit=100` | Finds the UEFA `matchId` needed by `matchstats.uefa.com`, with kickoff, teams, round and a **score breakdown: `regular`, `total`, `penalty`, `aggregate`** | **`CANDIDATE — FIELD OWNER`** (new; the missing half of the UEFA lane) | Keyless `curl`. `offset` is required (omitting it returns HTTP 404). `competitionId` 28 = Women's Champions League, 1 = Champions League. Found matches 2049369 and 2049367 and gave the 90-minute (`regular`) scores that ESPN does not cover for UWCL qualifying |
| UEFA `matchstats.uefa.com/v1/team-statistics/<matchId>` (period-scope caveat) | Corners, attempts, possession | field owner, **but whole-match scope** | `played_time` 137 and 115 on the two ties — the feed totals extra time, so a 90-minute contract is graded `PERIOD_SCOPE_BOUNDED` (`RULES_GENERAL.md` §16.11(q)) |
| ESPN `soccer/ita.coppa_italia` | Coppa Italia final, `wonCorners` | `CANDIDATE` (coverage reconfirmed) | Event 401911806: Sassuolo 6, Frosinone 5 (P-251-C05) |
| ESPN `soccer/concacaf.leagues.cup` | Leagues Cup final, `wonCorners` | `CANDIDATE` (new slug verified) | Event 401914297: Toluca 4, León 5 (P-265-C05). Note the dots — `concacaf.leagues_cup` and `usa.leagues_cup` are both HTTP 400 |
| ESPN `soccer/uefa.wchampions` | Women's Champions League | covered, **but no qualifying-round events** | HTTP 200 with 0 events for 1–4 Sep 2026; use the UEFA lane above for qualifying |
| ESPN `soccer/chn.fa`, `chn.cup`, `chn.fa_cup`, `chn.super_cup`, `chn.2`; `mex.w.1`, `mex.femenil`, `mex.liga_mx_femenil`; `usa.nextpro`, `usa.mlsnp`; `fra.3`, `fra.national`; `ind.sikkim` | China FA Cup, Liga MX Femenil, MLS Next Pro, Championnat National, Sikkim | **Verified non-coverage (re-probed 2026-09-16, all HTTP 400)** | Confirms the Part-2 rows and P-250 remain routeless |




## 2026-09-17 — sources exercised during the `P-424`–`P-437` import


None reaches `APPROVED FOR FEATURE`. Route observations are environment- and date-specific. Detail: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md).


| Source | Role | Grade | Note |
|---|---|---|---|
| **ESPN `soccer/afc.champions`** | AFC Champions League Elite: finals, `wonCorners`, goal minutes, possession, shots | **`CANDIDATE` — newly verified lane** | Verified all five ACLE MD1 finals and every corner count on 2026-09-17 (events 401912672, 401912671, 401912656, 401912670, 401912654). Slug variants `afc.champions_elite`, `afc.cl` → HTTP 400. Data partner: it settles a row only where the card **pre-registers** it |
| **J.LEAGUE ACLE match-data route / club records (`CK`)** | Corners and match data for ACLE fixtures involving J.LEAGUE clubs | **`CANDIDATE — FIELD OWNER` for those fixtures** | Settled corners on `P-425`, `P-426`, `P-436`. Check before any aggregator for Japanese-club fixtures |
| **AFC official match reports** | ACLE score, scorers, narrative | field owner for **score only** | **No corner field.** This is the direct cause of `P-430-C05` remaining open — an official report is not automatically a derivative record |
| ESPN cricket API, ETPL series 1547871 | Innings totals, toss, `Powerplay 1: Overs 0.1 - 6.0` per innings | `CANDIDATE` (reconfirmed, third use) | Reproduced both powerplay figures exactly (`P-424` 48/2, `P-428` 54/2) and both finals |
| Cricket Ireland / CricketArchive ETPL scorecards | ETPL finals, toss, phase notes | `RESEARCH` route (reconfirmed) | Used by the mini log for `P-424`/`P-428` settlement |
| **KBO English scoreboard (`eng.koreabaseball.com`)** | KBO finals | **`ACCESS DEGRADED` (2026-09-17)** | Returned **174 bytes** direct and **385** via `r.jina.ai`; `mykbostats` and Naver are JS-only; ESPN has no KBO route (`kor.kbo`, `kbo` → 400). The four KBO finals could **not** be independently re-verified and are carried from the mini log's Korean reports. Previously graded a reconfirmed field owner on 2026-09-15(b) — this is a route degradation, not a policy change |
| Korean on-site reporting (fnnews, SPOTV, SportsChosun, OSEN, Nate) | KBO finals, pitcher lines, roster state | `RESEARCH` / named reporting (`L-067` native-language lane) | Carried the four KBO finals this pass in the absence of a reachable field owner |
| ICC / Reuters / ABC / NDTV cricket records | International cricket finals and mechanism corroboration | `RESEARCH` / secondary | Not independently re-verified this pass |
| Kolossos official report, SDNA, Eurohoops | BCL qualification result | club owner / named reporting | Not independently re-verified this pass |
| Betting, tipster, fantasy and preview pages | — | **PROHIBITED** (unchanged) | `P-424`'s pitch-report ladder correctly failed closed rather than using them |


## 2026-09-17(b) — sources exercised during the `P-438`–`P-451` import


None reaches `APPROVED FOR FEATURE`. Route observations are environment- and date-specific. Detail: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md).


**Three route discoveries and two degradations.** Every one of the fourteen records in this import was re-verified from a raw record in this pass — the first cohort in Part 4 with no carried-on-narrative final.


| Source | Role | Grade | Note |
|---|---|---|---|
| **ESPN `soccer/afc.cup`** | **= AFC Champions League Two** (not the defunct AFC Cup): finals, goal minutes, **red cards**, `wonCorners`, `totalShots`, `shotsOnTarget`, `possessionPct` | **`CANDIDATE` — new lane, first use, verified** | The slug is counter-intuitive and cost a search: `afc.champions_two`, `afc.champions.two`, `afc.acl2`, `afc.champions_league_two`, `afc.champions2` all return **HTTP 400**; only `afc.cup` works, and its `leagues[0].name` self-identifies as "AFC Champions League Two". Verified `P-438` (Al-Wahda 3–2 Kuwait SC) and `P-439` (Khaldiya 0–0 Nasaf) on 2026-09-17, events 401912815 / 401912814. **It carries fields the AFC official report does not** — it surfaced a 60' red card and a 41-vs-2 shot count that the narrative settlement missed entirely. **Caveat:** unlike `uefa.europa` it emits **no `Halftime` key event**; reconstruct the half-time state from goal minutes. Data partner — pre-register it to settle a row (§16.10(j)) |
| **`statsapi.mlb.com` bulk schedule + `hydrate=linescore`** | **Season-scale base rates**, in addition to its existing per-game role | **`CANDIDATE — FIELD OWNER`, new use** | `…/api/v1/schedule?sportId=1&startDate=&endDate=&gameType=R&hydrate=linescore` returns a full month of games with inning-by-inning linescores in ~2 MB. Six calls covered the whole 2026 season (n = 2,286) and produced the margin, extras, push-mass and park distributions now anchoring `RULES_BASEBALL.md` controls 34–37. **This is how a base rate gets sourced from the field owner instead of remembered.** It also settled the `P-443`/`P-444` regulation-versus-final question that no narrative recap could: regulation 4–4 and 2–2 respectively. Refresh per season and record `n` and retrieval date with any card citing it |
| **`lnbp.mx/<Team>/team_results.html`, rendered** | LNBP per-Jornada finals | **`CANDIDATE — FIELD OWNER`, `JS_ONLY — RENDER REQUIRED`** | `curl` returns **HTTP 200 with a ~16 KB JavaScript shell and no scores** — which is why every text rung reported "not found". Rendered in a browser the page returns the finals immediately with a Jornada selector; *Jornada 20* gave **Dorados 97 — El Calor 86**, closing `P-451`'s result recovery and correctly distinguishing it from the Jornada 19 91–89. **Supersedes the 2026-09-04 "HTTP 403" note in `RULES_BASKETBALL.md` §9.5 for results.** Settles finals only — it does not close `BK-P1`, and a regulations search on the same domain still returns nothing |
| ESPN `soccer/uefa.europa` | UEL finals, **explicit `Halftime` key event**, goal minutes, shots, corners, possession | `CANDIDATE` (reconfirmed) | Reproduced `P-440` (HT 0–2, 1–4) and `P-441` (HT 0–0, 1–0, Balkovec 88') exactly. Range queries (`dates=YYYYMMDD-YYYYMMDD`) are **not supported** — they return a gzip error blob; query one date at a time |
| ESPN cricket API, **CPL series `1534175`** | CPL innings order, `Powerplay 1: Overs 0.1 - 6.0` per innings, matchnotes, XIs, toss-implied batting order | `CANDIDATE` (reconfirmed, fourth successful use) | Verified `P-445`: matchnote `section 1` = Barbados, powerplay **24/4**, 144/6 (20); Jamaica chase powerplay **79/0**; Sadaqat 100 off 44. **The series ID was already in this register from `P-217` and was not consulted** — a `G-L14` execution miss that cost a settlement route |
| MLB official recaps, AP / Reuters / CBS | Mechanism narrative, injury and event context | `RESEARCH` / secondary (unchanged) | Accurate on mechanism and on final scores, but they gave **no regulation-versus-final split** — the field that actually decided the `P-443`/`P-444` analysis. Narrative corroborates; it does not settle a phase or endpoint row |
| AFC / UEFA official reports | Score, scorers, regulation identity | field owner for **score and scorers only** | Same limitation as 2026-09-17: no shot, corner or disciplinary field on the AFC report. Settling `P-438` from it alone is what lost the red card |
| **`hs-consumer-api.espncricinfo.com`** | (attempted) current / results / live match index | **`ACCESS DENIED` (2026-09-17)** | `HTTP 403 Access Denied` on `/v1/pages/matches/current`, `/results` and `/live`. Use the `site.api.espn.com/apis/site/v2/sports/cricket/<seriesId>/…` lane instead, which is unaffected |
| **`cricketworld.com` scorecards** | (the mini log's cited `P-445` settlement URL) | **`NOT REPRODUCIBLE`** | Returns a **Cloudflare "Performing security verification" interstitial through `r.jina.ai`**. A cited URL that this repository's ladder cannot re-open is not a settlement route; the ESPN series lane replaces it |
| `sportytrader.es` and similar | surfaced an "83-77 LNBP" line in search results | **PROHIBITED** (unchanged) | Tipster/odds display, not a field owner; the figure matched no verified Dorados–El Calor game. Correctly rejected |
| `sports.core.api.espn.com/v2/sports/cricket/leagues` | (attempted) cricket league/series discovery | **EMPTY** | Returns `count: 0`. There is no discovery endpoint for cricket series IDs — they must come from this register or from a scorecard URL, which is the reason `G-L14` requires the register to be read first |


**Two standing consequences.**


1. **The field owner is not always the richest record.** On three cards in this import the official competition report carried the score and nothing else, while a data partner carried the mechanism. The settlement route stays the pre-registered field owner (§16.10(j)); the **process record** required by the new `G-L23` comes from whichever feed actually publishes shots, cards, minutes and inning splits. Record both.
2. **"Not found" and "not rendered" are different states.** `lnbp.mx` was recorded as unreachable for two years of notes and is in fact a working field owner behind a client-side widget. Before grading a competition's own site as unavailable, check whether the 200 response is a shell (`JS_ONLY — RENDER REQUIRED`, basketball control 27).


## Numerical source admission clarification — 2026-09-17


Prior season-scale MLB retrieval is retrospective reference evidence, not a quality-approved H0. A general CANDIDATE or field-owner label does not admit numerical features. For each admitted field record target/endpoint, exact source and schema, available_at versus retrieved_at, revisions, population/missingness, joins and access constraints. Require actual pre-cutoff snapshots for historical pregame features; current corrected labels may be used only with their reconstruction status declared. Completed-season winner-minus-loser W% strata are descriptive and cannot be silently back-joined as pregame covariates. No new external source was queried or promoted during this Markdown implementation. Existing key-number/base-rate records are uncertain references, never universal conditional limits. Publication includes prospective shadow under NUMERICAL_PROGRAM.


## 2026-09-19 — social-media lanes tested directly, and three structured lanes added


Prompted by a direct question: *should reporters, journalists, team accounts or league accounts on X/Twitter or Reddit be used for starting line-ups and stats?* Every route below was **tested in this pass**, not assumed. The short answer is that the two named platforms are unusable, the third has a serious identity problem, and the fields wanted are already available — better — from structured endpoints.


### Social platforms — tested 2026-09-19


| Route | Result | Verdict |
|---|---|---|
| `x.com/<handle>` direct | **HTTP 200, but a login wall.** 220 KB of markup containing **1,644 characters of visible text** — "Log in / Sign up", the profile name and a post count. **Zero post content.** | **UNUSABLE** |
| `cdn.syndication.twimg.com/timeline/profile?screen_name=` | **HTTP 200, 0 bytes.** The legacy unauthenticated timeline lane returns an empty body | **UNUSABLE** |
| `r.jina.ai/https://x.com/...` | **HTTP 403 `AbuseAlleviationError`** — "Anonymous access to domain x.com blocked … DDoS attack suspected" | **UNUSABLE** |
| `nitter.net` | connection failure (`000`) | **UNUSABLE** |
| `www.reddit.com/r/<sub>/.json` | **HTTP 403** | **UNUSABLE** |
| `old.reddit.com/r/<sub>/.json` with a browser UA | HTTP 200 but serves the **"Welcome to Reddit" interstitial HTML**, not JSON | **UNUSABLE** |
| `public.api.bsky.app` (Bluesky) | **API works.** Content coverage is the problem — see below | **CONDITIONAL / HIGH RISK** |


**Correction to a standing note.** Earlier source notes recorded X as "402, fully blocked". The current state is **200 with a login wall and no post content**, and the proxy route is separately blocked for abuse. Different mechanism, same conclusion: no usable content.


### The Bluesky identity trap — the most important finding of this test


Bluesky's public API is reachable and returns well-formed JSON. **Its sports-media handle space is not trustworthy.** Six plausible handles were tested:


| Handle tried | What it actually is |
|---|---|
| `jeffpassan.bsky.social` | **A handle-squatter.** The account's own posts read *"I continue to not be Jeff Passan"* and *"I'm merely place-holding this account handle"*. Last post **16 Nov 2024** |
| `fabrizioromano.bsky.social` | **A different person named Fabrizio.** Posts are in Turkish about domestic life; last post **5 Jul 2023**. Not the football journalist |
| `cricinfo.bsky.social` | No display name, last post **17 Nov 2024**; presents as an abandoned auto-relay |
| `mlb.bsky.social`, `espn.bsky.social`, `nba.bsky.social`, `kenrosenthal.bsky.social`, `mlbnetwork.bsky.social`, `theathletic.bsky.social` | **Profile not found** |
| `afl.bsky.social` | exists, **empty feed** |


**Zero of the handles tested were the real, current entity.** Two were confidently wrong in a way that is invisible from the handle alone — exactly the failure mode that would put a fabricated or two-year-stale "lineup" onto a card. A handle that *looks* canonical is not evidence of identity.


**Control `S-1` — social identity and corroboration gate.** A social post may be used only when **all four** hold, each recorded on the card:


1. **Identity verified by a durable identifier**, not a handle string — the account's DID/verification record, or a link to that account published on the entity's **own official domain**. A plausible handle is not identity.
2. **Recency checked** — the post's own timestamp is inside the event's information window. An account whose latest post is months old is stale regardless of who owns it.
3. **Corroborated by a field owner before it changes anything on the card.** A social post may *prompt* a retrieval; it may never *be* the retrieval. A line-up, injury, scratch or toss taken from social and not confirmed at the field owner stays `SECONDARY_ONLY` and cannot lift a participant field to `CONFIRMED_OFFICIAL`.
4. **Quoted, not paraphrased**, with the account, timestamp and retrieval time.


**Disposition: social media is a latency instrument, not an authority instrument.** Its only genuine advantage is that a beat reporter may post a scratch or a line-up a few minutes before the official feed. That advantage is worth **nothing** here while X and Reddit return no content, and it is worth **less than the identity risk** on Bluesky at current coverage. Do not build a card's participant state on it. Re-test the platforms each quarter; the access position changes.


### Structured lanes added instead — these carry the fields social media was being considered for


| Source | Retrieval | Field | Why it is better than the social route |
|---|---|---|---|
| **`statsapi.mlb.com/api/v1/schedule?...&hydrate=lineups`** | keyless JSON | **Confirmed batting orders, both sides** | Verified this pass: populates with 9 named players per side once the club posts (checked on 17 Sep games); returns **empty arrays** for games still `Scheduled`. That empty/populated state is itself the finding — see the `NOT_YET_PUBLISHED` rule below |
| **`statsapi.mlb.com/api/v1/game/{pk}/boxscore`** | keyless JSON | **`battingOrder` (9 IDs), `bench`, `bullpen`, positions** | Gives the exact `BENCH_NOT_RETRIEVED` field that has capped Rank-#1 margin rows on nearly every MLB card. Verified: Dodgers/Reds 17 Sep returned both full orders, 3 bench and 9–10 bullpen arms each |
| **`statsapi.mlb.com/api/v1/people/{id}` → `mlbDebutDate`** | keyless JSON | **Debut date → service time** | Verified: Josue De Paula, batting 6th for the Dodgers in `P-455`, had debuted **2026-09-11** — six days earlier. No card flagged it |
| **ESPN cricket `summary` → `debuts[]`** | keyless JSON | **Explicit per-match debutant list** | Verified on `P-452`: flagged Noor ul Rahman as debuting for Afghanistan. A machine-readable answer to "is anyone in this XI an unknown?" |


### `NOT_YET_PUBLISHED` versus `RETRIEVAL_MISS` — a correction to how line-up misses are recorded


§16.8 field 7 treats a line-up not retrieved *after publication* as a `RETRIEVAL_MISS`, a process defect. Cards have been recording that flag without being able to tell the two states apart, because they were reading a human-facing page that says "TBD" either way.


`hydrate=lineups` resolves it deterministically. Tested this pass: for 2026-09-19 games still `Scheduled`, the field returned **`awayPlayers: 0, homePlayers: 0`** for all eight — the line-ups genuinely were not posted. For 17 September games it returned **9 and 9**.


**Rule.** At the final volatile refresh, query `hydrate=lineups` and record the result with its query time:


- **empty** → `LINEUPS_NOT_YET_PUBLISHED @ <time>` — a verified availability state, **not** a process defect, and not a `RETRIEVAL_MISS`;
- **populated but not captured** → `RETRIEVAL_MISS` — a genuine process defect;
- **populated and captured** → `CONFIRMED_OFFICIAL`.


Most of the `STARTING_LINEUPS_NOT_RETRIEVED_AT_FREEZE` flags across `P-442`–`P-455` are, on this evidence, the **first** category. The cards were penalising themselves for a publication schedule. The fix is the structured query and an honest label, not more searching.


### Press conferences and coaching-staff commentary — assessed, with a limit


Asked whether pre- and post-match press conferences can be mined for tactical intent (tempo, defensive focus, approach). Findings:


- **No structured transcript lane exists** in the keyless endpoints. `statsapi`'s `game/{pk}/content` returns 40 highlight/editorial items (video headlines, condensed game, `gameNotes`) — **not** press-conference text. Club and league sites publish pressers as prose articles, retrievable per-article but not as a feed.
- **Where they are genuinely useful: availability and role intent.** "He'll be back tomorrow", "he's on a pitch limit", "we're resting him", "he'll come off the bench". This is concrete, checkable, and already works — `P-444` captured Aaron Boone's stated plan to have Judge back, and `P-449` captured the Mason Adams pitch cap. Both were correct uses.
- **Where they are not: quantitative tactical adjustment.** A coach saying "we want to play faster" or "we need to defend better" is an intention, not a rate. Converting it into a pace or efficiency adjustment would be an unsupported signed adjustment of exactly the kind `G-L2` and §16.5 prohibit, and stated intent is weakly related to realised tempo.


**Control `S-2` — press-conference material.** Admissible as **participant, availability, workload and role evidence** — treated as `SECONDARY_ONLY` until the field owner confirms, and quoted with speaker, date and retrieval time. **Not admissible** as a signed adjustment to pace, efficiency, scoring rate or any modelled quantity. A stated tactical intention may widen a distribution or motivate a named branch with its own mass; it may not move a centre on its own.


## 2026-09-21 — cricket toss/pitch source audit implementation


**Prospective source rule under CR-2026.09.21-1.** Cricket toss retrieval and exact-strip retrieval are now separate. This corrects the prior six-rung/eight-rung drift and the duplicated toss-broadcast concept without weakening the valid historical lessons.


- **Official verified video is a first-class late-information lane.** Board/competition/rightsholder videos can own the toss and provide named pitch observations when the account and exact match are verified.
- **Sanctioned NV Play / board-branded Match Centre is an explicit route** for associate/domestic competitions when the competition officially uses it. Infrastructure ownership is not automatically event-field ownership; record the sanctioned relationship.
- **Broadcast transcripts are access routes, not extra independent sources.** A specialist commentary page explicitly transcribing the same presenter/captain/curator report is one upstream lineage with the broadcast.
- **Shared-feed fingerprint:** identical or near-identical unusual structured pitch labels across different websites are one suspected upstream feed until provenance proves independence.
- **`AUTOMATED_PITCH_METADATA` is not an observed strip.** Unattributed pitch/batting/pace/spin labels may support context but cannot set `STRIP STATUS: OBSERVED`.
- **Venue history can be missing.** `INSUFFICIENT_VENUE_HISTORY` is a valid state; never fabricate the same-venue sample.
- **Official-page staleness is field-specific.** An official page that remains `UPCOMING` while fresh reliable sources show live/final is `STALE` for event state; still-valid identity fields may remain usable.
- **Search snippets remain discovery only.** Open the exact underlying source.


Verified lane examples in the 2026-09-21 audit include ICC official toss/pitch videos, Pakistan Cricket's verified match-specific toss/pitch video, Cricket Australia Match Centre toss/team fields, BCCI Toss Report pages, Cricbuzz named broadcast pitch-report transcripts, NV Play scorer/Match Centre toss workflow, and the ETPL duplicate-feed/stale-official reference cases. These are research-lane demonstrations, not numerical-feature approvals.


<!-- ALL-SPORTS-AUDIT-RECONCILIATION-2026-09-21-CR2 -->
## Cross-audit source invariants — 2026-09-21


Across every sport, source quality is **field-specific and lineage-specific**, not brand-count based. The current retained rules are: field owner first where available; structured/raw evidence before narrative aggregates for decisive fields; `known_at <= cutoff_at`; current-state freshness for dynamic fields; mirrors/reposts/front ends of one feed count once; search snippets/generated summaries are discovery only; betting/tipster/fantasy/DFS-derived material is prohibited predictive evidence; and three independent reliable lineages are required for event verification and terminal settlement.


Historical source conclusions are explicitly superseded when later audits demonstrated a better route or disproved non-coverage (for example the old blanket corners-source gap). A source being official does not make a stale field current, and a source being structured does not make multiple front ends independent. Missing coverage remains explicit missingness rather than a fabricated fallback.




<!-- SOURCE-REVISION-SYNC-2026-09-21-CR3 -->
## CR-2026.09.21-3 source-policy synchronization


Source rules are unchanged from the reconciled CR-2 state: field ownership, independent upstream lineage, point-in-time cutoff safety, market/fantasy source quarantine, explicit missingness and three-lineage terminal settlement remain controlling. The revision bump reflects live-rule/read-back synchronization elsewhere, not a new source weight or predictive feature.


<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-23 -->
## 2026-09-23 — quick reference from the consolidated P-487–P-494 import

Full cards: `DATA_SOURCE_REGISTER.md` §"2026-09-23".

- **NPB settlement:** NPB box (raw HTML; field owner) + Sports Navi schedule page + Kyodo wire **or** Nikkan staff report. **Exclude Mynavi's AI-generated "プロ野球試合結果" recaps.**
- **NBL settlement:** the NBL match-data API (status/score fields only; skip the `betting`/`odds` keys) + ESPN (no browser UA; `?dates=`) + Flashscore results. ESPN and the NBL feed may share a vendor, so keep one fully independent lineage (Flashscore).
- **NBL availability:** the official preview's expected depth chart and the injury list come first. Print first names where surnames collide (Jaylin v Kyrin Galloway).
- **WTA live:** the match feed can drop a live match from its list; use the ESPN tennis scoreboard as the live cross-check.
- **Lineage rule reminder:** a league feed and a publisher on the same data vendor are one lineage until shown otherwise. Record the vendor where a feed exposes it (e.g., `sportradar_timestamp`).
