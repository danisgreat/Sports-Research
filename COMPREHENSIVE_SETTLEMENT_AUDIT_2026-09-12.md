# Settlement, retrospective and algorithm audit - 2026-09-12

**Learning only; not performance eligible.** All changes are local to this workspace. No forecast was issued. The original probabilities, ranks and selections remain frozen. A final sporting result, an accepted research grade, an operator settlement, and an evidence-quality judgment are separate states.

The supplied mini logs already reached canonical P-371 in the September 11 import. This pass adds corrections and missing evidence rather than importing those games a second time. Next canonical ID remains **P-372**. Twenty raw mini logs have been moved into [archive/mini_logs](archive/mini_logs), with byte sizes and unchanged SHA-256 hashes in the [archive manifest](audit_2026-09-12/archive_manifest.md). The refreshed/settled/pre-settlement variants remain separate provenance artifacts, not separate games. The complete chronological enumeration is [GAME_LOG_STATUS_CURRENT.md](GAME_LOG_STATUS_CURRENT.md).

## Current settlement state

There are **14 result-evidence follow-ups**: one live Test-winner label, one identity/state-conflicted event and twelve corner fields. There are also four inherited operator-only exception records and P-366's censored fixed-20-over target; these are not live sporting-result requests. The nine historical follow-ups retain custody in Part 2. The live Test does not prevent work on other events.

P-364 remained live when checked: Pakistan 133 and 449 all out, England 453, Day-3 stumps at the final 23:43 UTC refresh; the earlier in-session score was 233/4. Only its England-winner label stays open. Its four ranked innings/45-over rows already have completed targets and retain their grades. [Exact live record](https://www.cricbuzz.com/live-cricket-scores/129596/pak-vs-eng-3rd-test-pakistan-tour-of-england-2026). This is a timestamped retrieval snapshot, not continuous monitoring. [Detailed five-row recent check](audit_2026-09-12/recent_queue_evidence.md).

No pending corner was upgraded without its required evidence. A result-report link or another secondary website does not establish a missing official corner count or an unfrozen provider definition. No fabricated WIN, LOSS, VOID or operator action was entered.


## Additional historical recovery completed in this pass

A deeper archive check found that the missing P267 settlement artifact had led to an overbroad statement about absent per-event detail. **The supplied mini log 8 retained 19 issued/admin cards (P-249-P-267) and eleven intermediate settlement/process blocks, including ten issued-event retrospectives.** Its 242,045-character relevant payload is now copied intact into Part 1. Eleven additional historical event tables/narratives were reconstructed from the preserved forecasts and newly retrieved evidence: P-241/P-242/P-243/P-259/P-260/P-262/P-263/P-264/P-265/P-266/P-267. Five additional deep rank-1 failure reviews cover P-242/P-259/P-262/P-263/P-266. [Recovered tables, detailed retrospectives and source limits](audit_2026-09-12/recovered_historical_retrospectives.md); [official MLB inning/workload evidence](audit_2026-09-12/recovered_mlb_evidence.md).

**Five documentary-audit tasks remain:** P-250-C05, P-251-C05, P-255-C05, P-256-C05 and P-265-C05. Their minis retain unresolved/provisional corners, while the missing later artifact is cited as having closed the cohort. No new source recovered that later adjudication. They have TMP-AUDIT-20260912-01 through -05 handles, separate from the fourteen primary result/derivative follow-ups. Their inherited closed status is now visibly qualified in the full register. No rank-1 corner success is newly certified from a secondary count alone. The P-265 first-half goal was freshly verified at 41 minutes by competition and club reporting.

The full 371-ID register therefore classifies **330 settled, 5 inherited closed with documentary gaps, 14 open result/field records, 4 research settled with operator exceptions, 15 administrative/no-trial records, 1 alias, 1 old terminal field gap and 1 event with censored targets**. These mutually exclusive categories sum to 371. LOCAL-GEELONG-20260904 and TMP-SETTLED-20260911-01 are additionally listed. This is record accounting, not a count of independent predictions. Full historical retrospective certification remains limited by the five named adjudication gaps and inherited source/timestamp limitations; none is hidden behind a claim that every log is fully verified.

Useful recovered patterns: P-266 was 1-1 after nine but 6-3 after ten, defeating both leading rows despite correct starter suppression; P-260 finished on the integer line and both totals pushed; P-262 had 43/1 at six but 183/4 at twenty; P-243 had equal total games despite a match winner. These strengthen exact endpoint, resource-state and score-allocation controls without a retrospective coefficient change. A WTA page's mixed state labels/incomplete service-game field and Sofascore's community-editor attribution reinforce field-level source validation.

## Numerical and completeness corrections

The P-345-P-371 contract tables contain **109 issued ranked rows: 105 graded, two provisional corner rows and two censored 20-over rows**. Direct recomputation gives 61 wins, 44 losses and mean Brier **0.243439** over the 105 graded rows. These are learning diagnostics with dependent rows, not an accuracy or calibration verdict. The historical running figures are carried, not revalidated across all older probability cohorts in this pass.

| Question | Correct answer | Why the earlier statement was insufficient |
|---|---|---|
| Top-ranked row | 16 W / 9 L; P-369 rank 1 provisional | The provisional corner loss must not be booked as final |
| Both top two won | 6 / 23 cards with both rows graded; 6 / 24 logically decidable outcomes | P-369 is already a both-win failure because rank 2 lost, even though rank 1 is provisional. P-368 is unresolved; P-366 rank 2 is censored. Earlier 6/25 included the censored case |
| Cohort card closure | 26 issued cards: 22 with every ranked row graded and closed; P-366 terminal/censored; P-364/P-368/P-369 partial | Earlier 24 fully settled + 2 corner-partial + 1 live-partial added to 27 |
| Lineups/bench/coaches | See the 26-card matrix below | Earlier complete 7 + partial 6 + missing 12 added to 25 and mixed player-complete with coach-incomplete cases |
| Main-line O/U claim | Earlier 13 W / 13 L aggregate is not accepted as a reconciled comparison | Its Over/Under subtotals added to 12 W / 13 L and included different supplied/analyst-selected/phase populations. Replace it with the explicit preferred-target table generated below; do not manufacture a missing success |
| Source agreement | Agreement by opened field, with explicit coverage | A correct final does not certify every statistic, lineup, weather statement or causal narrative on the page |

The six fully verified both-top-two successes are P-346, P-349, P-351, P-355, P-363 and P-367. Counting complementary pairs inflates raw row-level coverage and does not increase the number of independent games.

## Detailed failed-top-pick review

These supplements sit beside the original settlement blocks in Part 3. Previously verified but not re-fetched figures are labelled as inherited; newly opened gamebooks/reports and route limits are in the [sport evidence record](audit_2026-09-12/sport_evidence.md). A loss warrants scrutiny, but it does not by itself prove the stated probability was too high. No new historical probability was estimated.

| Card | What went right | What went wrong and evidence boundary | Concrete next-game change and previous lesson |
|---|---|---|---|
| P-345 Brugge-Villa | Brugge team scoring, first-half Over and the now owner-confirmed corner row won | Inherited final Villa 3-2, including three first-half goals, defeated Brugge +0.5 and full Under. A three-match domestic shot-on-target drought was used too confidently against a changed attack. A burst of goals alone does not establish that it was not finishing variance | Retrieve shots by quality/opponent and current personnel; show uncertainty and Villa-win/separation branches. Revisit soccer control 23, G-L7 and cross-competition translation. Do not automatically erase a directional effect solely because it is small-sample |
| P-350 Shelton-Alcaraz | The issued extension, games Over and Shelton handicap all won; they describe a long match that actually occurred | Alcaraz winner lost. **The deciding tiebreak was 10-7, not 9-7.** Match games remain 49. Elo agreement does not demonstrate the 76% estimate was correct or separate variance from model error. Coaches were not captured on the issued card | Keep the upset/extension tree; examine return-from-layoff and opponent-adjusted serve/return sensitivity with pre-cutoff evidence. Benchmark only; no automatic layoff penalty. Tennis controls 13-14 and G-L9, corrected by section 16.9. [Tennis Australia report](https://ausopen.com/articles/news/i-feel-myself-becoming-more-complete-says-shelton-after-alcaraz-upset) |
| P-352 Namibia-SA | Inherited five-over Under won at 18/0; SA winner and 250+ also won | SA reached 348/6, defeating Under 305.5. A low-run phase without wicket losses retained batting resources. Hermann 150 and de Zorzi 72 are individual innings, not an established 222-run partnership. Same-ground T20 totals do not prove the same physical strip or justify direct ODI transfer | Record wickets/resources with phase pace, exact strip evidence and conditional innings scenarios. Cross-format results are context pending comparability, not mandatory signed uplift. Cricket controls 16/19/25, G-L7 and G-L9 |
| P-356 KT-Samsung | The three lower rows captured KT protection and a low total; the original card printed more arithmetic than many peers | Inherited KT 2-0 and Ko's seven scoreless innings defeated Samsung Over 3.5. A single poor recent start and larger recent sample were given offsetting terms without a defensible uncertainty calculation. KT lineup/bench evidence was incomplete. Opposing winning rows are not automatically logically inconsistent unless their joint states make them so | Disaggregate opponent-adjusted starts, actual workload and walk/strikeout/contact evidence; show sensitivity to the outlier and ordinary long-start outcome. Baseball 24/26/28; corrected G-L11. Do not use a binomial formula for runs allowed |
| P-357 Dublin-Belfast | Inherited 43/3 phase Under and innings Under won | Belfast 150+ and winner failed at 107, with three wickets falling at 62. Current XIs were not captured. A completed toss establishes nomination, not publicly accessible publication before the cutoff; the earlier certainty that this was a retrievable-publication miss was unsupported | Search exact toss/team-sheet routes, save publication time, and record unavailable versus not retrieved honestly. Model the selected attack and collapse state jointly with innings exposure. Cricket 3/26, G14.2 and G-L9; the five-wicket haul itself was not knowable |
| P-358 Puerto Rico-China | Puerto Rico +9.5 won and China won outright, supporting the broad competitive-game view | Inherited 75-72 defeated Under 141.5. Puerto Rico's cold prior 3P rate did not persist and San Antonio scored 35. The missing quantified player exposure and starting-five capture are real process gaps; the exact individual scoring explosion was not predicted | Print player usage/minutes and shooting attempts, then examine efficiency/turnover/transition scenarios without assigning hindsight weights. Basketball 20-22 and G-L7. Top-two split outcomes do not establish negative correlation |
| P-364 England-Pakistan | Original XI and known batting-resource evidence were useful; the issued Over complements won | Under 179.5 at 45 overs and innings Under 336.5 failed: England added 54 over the six-over restart and finished 453. Awarding credit merely because the opposite sides won is not selection success. The mini's Sporting Life betting-tips preview breached MARKET_BLIND; the claim that all sources/gates passed is withdrawn | Use comparable restart-state evidence, ball age, batters and remaining resources; keep generic restart slowdown as an explicit assumption to stress-test. Retrieve original market-blind conditions reporting. Historic 2022/era scoring averages alone do not establish an exact 2026 six-over baseline. Cricket 27 and G-L2/G-L9. Winner remains pending |
| P-365 Uni-Brothers | Under 6.5 won at six; Uni's winner call was correct | Brothers +1.5 lost by six. The original card already named a low-total separation state, but its occurrence does not identify the correct pregame mass. Dykxhoorn delivered seven scoreless; Yu allowed seven hits, **five walks and four runs/three earned** in 4.2 innings. Missing lineups/bench/coaches remain a process defect | Model control-loss/early-hook as well as contact variance; show full-game scoring after the starter exits. A long strong start is not itself a guaranteed full-game Under. Baseball 17/28 and G14.2. [CPBL gamebook](https://stats.cpbl.com.tw/schedule/2026-A-321) |
| P-369 United-Shabab | Inherited full-game Under and underdog side won at 1-1 | Rank-1 corners Under 10.5 remains a provisional loss at reported 11; first-half Over lost at 0-0. The corner outcome cannot be promoted by secondary agreement. A half-corner miss does not justify choosing a new line retrospectively | Record exact corner provider and phase-specific route before issue. Keep no-goal early states despite favourite territory. Soccer phase/corner controls, G10.2 and G-L9. Outcome explanation for corners remains provisional, process retrospective complete |
| P-371 Belgium-Germany | Availability/coaches and German-positive mechanisms were recorded; Over and German cushion won as complements | Both leading picks lost, Belgium -6.5 and Under 144.5, at Germany 93-74. Germany had four prior games versus Belgium three, with no frozen attempt counts. The old assumed equal n and 'mostly noise' claim is withdrawn. Germany won all four quarters but did not lead throughout. Rebounding/bench/crowd as the causal explanation remains incomplete without the full box/game report | Retrieve attempts/minutes and opponent mix, allow Germany to separate in the scenario table, and test shooting/rest/rotation sensitivity. Do not infer the 19-point outcome or correct probability from qualitative possibilities. Basketball 20-24 and corrected G-L8/G-L10/G-L11. [FIBA game](https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128150-BEL-GER) |

## Additional successes and misses that matter

P-353's Chunichi Under won, but the distribution between the teams was wrong: Yomiuri won 5-1 and Dalbec homered in the third. The [NPB gamebook](https://npb.jp/bis/eng/2026/games/s2026090901424.html) supports the scoring and workload facts; one opposite-handed hitter's home run does not prove the entire platoon mechanism was wrong. P-354's [NPB record](https://npb.jp/bis/eng/2026/games/s2026090901426.html) shows Tokoda eight scoreless, Hiroshima's three runs in the seventh and Hanshin's single ninth-inning homer. The pitching transition coincided with scoring; managerial causality remains unproved.

P-359's Taipei +10.5 won, while Under 162.5 lost by only half a point at 83-80. [Petra](https://www.petra.gov.jo/en/news/national%C2%A0basketball-team-stumbles-against-chinese-taipei) verifies final/identity but does not substantiate a player-level guard/Gilbeck explanation. Preserve that as a pregame hypothesis. P-360's Under won at 82-66: [Yonhap](https://en.yna.co.kr/view/AEN20260910008300315) reports a 21-0 third-quarter run and Korea's 3/20 fourth-quarter shooting. This is stronger phase-specific evidence than asserting that every blowout lowers totals.

**P-361's temporal explanation is corrected:** the [NPB inning record](https://npb.jp/bis/eng/2026/games/s2026091001427.html) was already 3-3 after four innings, so Under 5.5 had already lost. The two eighth-inning runs decided Yomiuri's 5-3 winner/margin, not that total loss. Record the first decisive target checkpoint in every future retrospective.

P-363's two leading rows won, but the [NRL chronology](https://www.nrl.com/news/2026/09/10/thursday-night-footy-roosters-v-bulldogs/) shows both a first-half Bulldogs lead and later disruption: Baxter's HIA and Tagoai's sin bin preceded the Roosters surge. The original competitive-first-half idea deserves credit; the exact injuries/cards do not become pregame knowledge. P-367's inherited France 90-61 win and Under were successful, but source-specific possession/turnover evidence is needed before concluding that all of the proposed causal budget was validated.

The retained positive cases P-346/P-349/P-355 show useful exact-target accounting and source rejection, while P-347/P-348/P-351/P-362 show why a winner, team total and handicap need distinct full-game grades. P-366 correctly remains censored for the fixed 20-over target; P-370 correctly has no forecast to grade. None of these observations validates the algorithm.

## Starting lineups, bench and coaching audit

This matrix reports **what the issued card says it captured**, checked against the preserved mini/canonical text; it does not backdate later source retrieval. A roster is not a confirmed starting lineup. Exact complete-match publication times were not independently recovered for every card. P-370 is administrative and excluded from the 26-card denominator.

| ID | Both starting lineups | Bench/reserves | Both coaches/managers | Combined answer |
|---|---|---|---|---|
| P-345 | Recorded official XIs | Both recorded | Both named | Recorded complete; source-time qualification retained |
| P-346 | Recorded official XIs | Secondary only | Both named | Partial source quality |
| P-347 | Pitchers official; batting orders secondary | Bullpen names, full reserves not demonstrated | Not named | Partial |
| P-348 | Pitchers official; batting orders secondary | Full reserves not demonstrated | Not named | Partial |
| P-349 | Pitchers official; orders mixed/TBD | Full reserves not demonstrated | Not named | Partial |
| P-350 | Tennis players identified; team starters N/A | N/A | Not captured | Coach field missing; team lineup N/A |
| P-351 | Pitchers official; batting orders secondary | Full reserves not demonstrated | Not named | Partial |
| P-352 | Both XIs recorded | Reserves not demonstrated | Not named | XI complete; combined answer no |
| P-353 | Both orders recorded | Both recorded | Both named | Recorded complete; pregame timestamps not reconstructed |
| P-354 | Both orders recorded | Both recorded | Hanshin missing | Combined answer no |
| P-355 | Not confirmed | Official squad context; bench roles unresolved | Both named | No; rejected an inconsistent secondary lineup |
| P-356 | Samsung order; KT unresolved | Not captured | Not captured | No |
| P-357 | Not captured before issue | Not captured | Not captured | No; public pre-cutoff availability not proved by toss alone |
| P-358 | Both fives unconfirmed | Final twelves, starter/bench split unresolved | Both named | No |
| P-359 | Both fives unconfirmed | Final twelves, split unresolved | Both named | No |
| P-360 | Both fives unconfirmed | Availability/roster context; full role split not demonstrated | Both named | No |
| P-361 | Both orders recorded | Both recorded | Carried from prior card, not refreshed here | Partial |
| P-362 | Not captured | Not captured | Not captured | No; missing bench gate affected top full-game total |
| P-363 | Both 1-17 recorded | Included in 1-17 | Not named before issue | Players complete; combined answer no |
| P-364 | Both XIs recorded | Remaining batting order known; reserves not demonstrated | Not named | XI complete; combined answer no |
| P-365 | Not captured | Not captured | Not captured | No; missing bench gate affected top handicap |
| P-366 | Not captured | Squad context only | Not established | No |
| P-367 | Both fives unconfirmed | Both final twelves, split unresolved | Both named | No |
| P-368 | Not confirmed | Not confirmed | Al Jazira missing | No |
| P-369 | Not confirmed | Not confirmed | Both named | No |
| P-371 | Both fives unconfirmed | Both final twelves, split unresolved | Both named | No |

The numerical 7/26 'complete' headline is withdrawn. Only P-345/P-353 are described as capturing all three categories on both sides in the reviewed text. That is **recorded completeness**, not fresh proof of every pre-cutoff publication or complete source accuracy. Coaches were missing even in several otherwise strong lineup captures. Positive retrieval should be preserved without overstating it.

## Shared and sport-specific algorithm changes

[RULES_GENERAL section 16.9](RULES_GENERAL.md#169-probability-dependence-and-retrospective-corrections---2026-09-12) and the dated additions in all ten sport files implement the [complete corrections](audit_2026-09-12/rule_corrections.md): exact signed CDF/threshold logic; mutually exclusive full-outcome branches; joint-probability bounds; real sample denominators; no automatic two-SE direction rule; participant publication provenance; target-crossing chronology; and field-specific source lineage.

These are logical, arithmetic and evidence-handling repairs. The same-session sporting findings do not fit new coefficients, force an Over/Under direction, or prove phase totals are more reliable. Each sport file explains the native exposure/roster/endpoint application; AFL, American football, ice hockey and rugby union receive transferable corrections only, because no new event in those sports was freshly settled here.

The aim of at least one useful O/U winner and two winning leading picks remains an objective, not a guarantee. Choose a preferred direction before play, calculate dependence only from an explicit joint object, and compare future performance within matching competitions and target definitions. If evidence cannot support a strong direction, say so instead of adding an opposite pick to manufacture coverage.

## Source improvements and remaining limits

The [source evidence record](audit_2026-09-12/sport_evidence.md) identifies working US Open AMP reports, NPB English inning/pitcher boxes plus dated rosters, CPBL's league-linked advanced-statistics page, NRL chronological live blogs, and claim-specific Petra/Yonhap/FIBA coverage. These are verified retrieval lanes for stated fields, not blanket endorsements or APPROVED FOR FEATURE admissions. Methodology references are NIST and the ASA; they do not supply a sports probability.

The current P-371 FIBA summary does not expose complete starting/bench usage. The UAE league and club shells did not yield corners. ESPN Uganda remains on a stale season for the requested date. P-126 lacks a resolved event identity. The older main-line O/U subtotal remains unreconciled and is explicitly replaced by a directly inspectable narrower metric below. The historical P-001-P-344 index is reconciled for identifiers/current dispositions; every old settled match was not independently re-fetched. Missing results stay missing.

## Next settlement pass

Read the active snapshot and current status list first. Recheck the live Test winner; settle only a verified final. Then retry each evidence follow-up with its exact target and recorded trigger. Leave live/unverified rows open and move on. Keep temporary handles stable, retire them only when a documented disposition closes the exact item, and archive each reconciled mini log with its hash and original-to-canonical map. Never reissue a historical card or create a duplicate game from a revised mini.


## Recomputed preferred scoring O/U table

Definition: the lowest-numbered ranked scoring total/threshold on each issued card; includes goals, runs, points, innings, phases and sets, and the literal 150+ threshold; excludes corner derivatives and handicap rows. This is not the earlier supplied-main-line population. One observation per card; no retrospective choice of the winner.

**16 W / 10 L over 26 graded preferred scoring targets.** Including corner totals in the selection definition instead gives 16 W / 9 L plus P-369 provisional: a different, explicitly labelled population.

| Card | Original rank | Preferred scoring target | Issued p | Existing research result |
|---|---:|---|---:|---|
| P-345 | 2 | Club Brugge team total Over 0.5 | 0.70 | **WIN** |
| P-346 | 2 | AEK team total Over 0.5 | 0.78 | **WIN** |
| P-347 | 2 | Mariners team total Under 4.5 | 0.71 | **LOSS** |
| P-348 | 1 | Blue Jays team total Over 3.5 | 0.73 | **WIN** |
| P-349 | 2 | Giants team total Under 4.5 | 0.66 | **WIN** |
| P-350 | 2 | Over 3.5 sets | 0.66 | **WIN** |
| P-351 | 1 | Reds team total Under 4.5 | 0.74 | **WIN** |
| P-352 | 1 | SA 1st innings Under 305.5 | 0.68 | **LOSS** |
| P-353 | 1 | Chunichi team total Under 4.5 | 0.75 | **WIN** |
| P-354 | 1 | Hiroshima team total Under 3.5 | 0.76 | **WIN** |
| P-355 | 1 | 1st-half Under 1.5 | 0.82 | **WIN** |
| P-356 | 1 | Samsung team total Over 3.5 | 0.70 | **LOSS** |
| P-357 | 1 | Belfast 1st innings 150+ | 0.72 | **LOSS** |
| P-358 | 1 | Under 141.5 | 0.64 | **LOSS** |
| P-359 | 2 | Under 162.5 | 0.62 | **LOSS** |
| P-360 | 1 | Under 160.5 | 0.59 | **WIN** |
| P-361 | 2 | Under 5.5 | 0.56 | **LOSS** |
| P-362 | 1 | Under 9.5 | 0.58 | **WIN** |
| P-363 | 2 | Under 59.5 | 0.55 | **WIN** |
| P-364 | 1 | England Under 179.5 after 45 overs | 0.61 | **LOSS** |
| P-365 | 2 | Under 6.5 | 0.56 | **WIN** |
| P-366 | 1 | Dockers first 6 overs Under 50.5 | 0.56 | **WIN** |
| P-367 | 2 | Under 153.5 | 0.54 | **WIN** |
| P-368 | 1 | 1st-half Over 0.5 | 0.68 | **WIN** |
| P-369 | 2 | 1st-half Over 0.5 | 0.64 | **LOSS** |
| P-371 | 2 | Under 144.5 | 0.53 | **LOSS** |

Reproduction: read the preserved pre-edit Part-3 settlement tables; for each P-345-P-371 card choose its lowest original rank meeting the definition above; exclude P-370 because no forecast exists. Grade exact original targets. Brier is sum((p-y)^2)/105 with y=1 for WIN and 0 for LOSS. All 105 printed row Briers agree to four decimals. The two provisional and two censored rows contribute neither W/L nor Brier.

## Validation and remaining limits

[Validation record](audit_2026-09-12/VALIDATION.md) documents exact coverage, original-pick preservation, recomputed recent diagnostics, archive hashes and link/table checks. [Change log](AUDIT_CHANGELOG_2026-09-12.md) identifies the changed document groups. No guarantee of top-two or O/U success is made: the improvements address demonstrable arithmetic, evidence and modelling omissions; predictive benefit requires a frozen prospective comparison. No new playing-law change was established, no H0 source was approved, and no full historical calibration/ROI test was performed.


### Latest state refresh - 2026-09-11 23:43 UTC / 2026-09-12 09:43 AEST

P-364 remains IN PROGRESS, at Day-3 stumps, not a final: Pakistan 133 and 449 all out (96.4), England 453. England's unstarted chase target is 130. [Cricbuzz exact commentary](https://www.cricbuzz.com/live-cricket-scores/129596/pak-vs-eng-3rd-test-pakistan-tour-of-england-2026) and [NDTV exact scorecard](https://sports.ndtv.com/cricket/eng-vs-pak-scorecard-live-cricket-score-pakistan-in-england-3-test-series-2026-3rd-test-enpk09092026264908) agree on the completed Pakistan innings and stumps state. Several official/venue pages still exposed Day-2 52/2, so they were not treated as the freshest state merely because they were official. PCB direct retrieval still failed. Ignore the sites' win-probability widgets. TMP-OPEN-20260911-03 stays open; the four already-graded ranked targets do not change. The earlier 233/4 snapshot below/elsewhere is historical, not the latest score. Recheck final on the next settlement request; no result is predicted or booked here.
