<!-- BEGIN CANONICAL RESEARCH P-609 -->
## P-609 — RUGBY UNION / Bledisloe Cup · Australia vs New Zealand · 2026-10-17
Import: 2026-10-21T01:07:13+11:00; prompt 4 NEW_CANONICAL_EVENT. Local event key `LOCAL-2026101679B3FBCC8D-G0009` → canonical **P-609**; native identity RUGBY_UNION:2026-10-17:AUS:NZ:BLEDISLOE_TEST_2 (surrogate). Source mini `2026101679B3FBCC8D`, frozen source SHA-256 `b7478342e7ecba6861d9d79e4fc98b1dcd686356260f8b21911989847115ad7e` (313,155 bytes). Card core SHA-256 `290e721cc647e08f72f588b03a446ea4eb0c613bffd0a48446093ab021f43861` (28,187 bytes) = the exact bytes between the local BEGIN/END CARD marker lines (source offsets 244763–272950); markers and headings outside them remain in the preserved source. Original method, probabilities, ranks, statuses, timing and gaps are literal; any NOT_ASSIGNED / PENDING wording inside the core is historical. Import is not a forecast timestamp and confers no certification.

## Card · LOCAL-2026101679B3FBCC8D-G0009 · RUGBY UNION / Bledisloe Cup · Australia vs New Zealand · 2026-10-17

**Status:** `READ_ONLY_DRAFT / NOT_ISSUED / RESEARCH_ONLY_NO_MODEL / ANALYST_SCENARIO_NOT_PRIMARY` — new card in **separate cumulative sandbox copy only**. The original owner desktop mini is not writable/controlled here. `canonical P-ID = NOT_ASSIGNED`, assignment only on `PROMPT_4_IMPORT`. Evidence researched after the advertised start, not retroactively a frozen pregame forecast. Actual first-play time NOT_VERIFIED; the official sites disagree on 15:45 vs 16:00 AEDT. No live or target final score entered as an input.

### Decision block — research-only estimates

| Analyst rank | Supplied direction | analyst_p, NOT p_card | Endpoint/action |
|---:|---|---:|---|
| 1 | Australia +9.5 | 52.82% | M=NZ−AU ≤ 9; 80-minute total |
| 2 | Under 60.5 points | 52.51% | T=AU+NZ ≤ 60; 80-minute total |
| 3 | Over 60.5 points | 47.49% | T ≥ 61; 80-minute total |
| 4 | New Zealand −9.5 | 47.18% | M≥10; 80-minute total |

**Estimated score (NOT_FITTED): Australia 25.53 – New Zealand 33.96.** Expected combined points **59.49**, expected New Zealand margin **+8.44**. Winner lean NZ, but no computed winner probability (the same joint-normal method could derive a conditional standalone estimate; winner contract was not supplied). The strongest supplied contract is Australia +9.5 at 52.82%; second is Under 60.5 at 52.51%. **Neither passes the 0.62 Rank-1 floor; lead ~0.31 percentage points, below 4.00.** All probabilities are explicitly UNCALIBRATED; no numeric PRIMARY gate is claimed. At the even-split 50% reference, these are small model preferences, not evidence of monetary value or established predictive skill. No odds/payout data consumed.

**Winner-only auxiliary diagnostic:** Treat margin M=NZ−AUS as a continuous normal with integer half-point continuity bins: P(NZ win, M≥1) = 0.70165508, P(draw M=0) = 0.02270163, P(Australia win, M≤−1) = 0.27564329. This is a conditional analyst score-margin derivative, not a separately fitted winner classification or certified primary model.

### A1. Authority, identity and issuance/timing

- GitHub pinned authority `7e59f83b7f29e034a82ceecf147fe4e5b63e73a3` on `main`, read-only, accessed during this response after the earlier mini's different pinned authority. Current methods `MDS-2026.10.16-v20.0`, `CR-2026.10.16-R7`, `P-2026.10.16-v20.0`, `SEL-2026.10.12-v3`, `SCV-2026.10.16-v11`, `PRIMARY-v3.3`, `MINI-v1`, `EXH-v1`, `RETAIN-v2`, `CYCLE-v1`. No uncommitted local Git checkout promoted to authority. No GitHub writes.
- Identity: Australia Wallabies (home) vs New Zealand All Blacks (away), **second Test** of the 2026 Bledisloe Cup, Accor Stadium, Sydney; stable SURROGATE `RUGBY_UNION:2026-10-17:AUS:NZ:BLEDSIOE_TEST_2`, federation/native match ID `NOT_VERIFIED`. Older local mini G0001–G0008 scanned, target aliases not already present as marked cards; canonical/current other minis not exhaustively scanned, so final import collision check remains mandatory.
- Owner supplied scheduled kickoff **2026-10-17 15:45 AEDT UTC+11 = 04:45 UTC**; Accor Stadium event confirms 15:45 (source `https://www.accorstadium.com.au/events/n2026_bledisloe_cup_wallabies_v_all_blacks`). NZ federation team release states **16:00** local in its match detail (source `https://www.allblacks.com/news/all-blacks/all-blacks-team-named-to-play-australia-in-second-bledisloe-cup-test`), 15-minute official source conflict. Actual first play, any delay and exact current event state NOT_VERIFIED. This **post-advertised-start** analyst card cannot claim pregame issue even if actual first play later; `ISSUE_PHASE=POST_SCHEDULED_START_RESEARCH` and `KNOWN_AT_UNVERIFIED`. Original owner submission time not captured by programmatic intake.
- 80-minute international Test, standard rugby union scoring (try 5, conversion 2, penalty/drop 3, penalty try 7); no scheduled extra time in this non-knockout Test, game draw is possible. Target spread +/-9.5 and totals 60.5 apply to **full 80-minute score**, absent named operator rules for cancellation/abandonment and extra time (no push at half-point lines if match completed). The contract action/void terms remain UNKNOWN_DEFINITION. World Rugby time rule: `https://passport.world.rugby/laws-of-the-game/laws-by-number/5-time/`.
- No target live or final score accessed for pricing. Research URLs were consulted during the response, but per-page raw capture and precise `known_at` availability stamps are not independently preserved. Certain sources have mutable/live pages—**never** assert their content was published before kickoff merely because the event page existed earlier.

### A2. Exact supplied owner block / candidate definitions

> Upcoming game — RUGBY UNION  
> Competition details: Australia vs New Zealand, Bledisloe Cup  
> Scheduled start: 3:45 PM AEDT, 17 October 2026 (can be delayed, so continue research and processes as normal)  
> Supplied contracts: Australia +9.5; New Zealand -9.5; combined total points Over / Under 60.5  
> Research constraints: continue pregame research even if game starts, continue until research is properly done. Need probability issue and expected value using GitHub/ML/RL if available.

Definitions are full-match 80-minute points and half-point non-push handicap/total. Exact supplied directions 4/4 retained. This block is a faithful normalization of owner request, not byte-verbatim. No unsupported alternative contracts added to the primary slate.

### A3. Team selection, absences, playing conditions, actual prior games

**Australia official originally named XV (15 October):** 1. Aidan Ross; 2. Josh Nasser; 3. Allan Alaalatoa; 4. Jeremy Williams; 5. Lukhan Salakaia-Loto; 6. Rob Valetini; 7. Fraser McReight; 8. Harry Wilson (c); 9. Ryan Lonergan; 10. Declan Meredith; 11. Harry Potter; 12. Isaac Henry; 13. Joseph-Aukuso Suaalii; 14. Max Jorgensen; 15. Tom Wright. **Bench:** 16. Billy Pollard; 17. Angus Bell; 18. Massimo De Lutiis; 19. Josh Canham; 20. Carlo Tizzano; 21. Kalani Thomas; 22. Harry McLaughlin-Phillips; 23. Filipo Daugunu. Federation: `https://www.rugby.com.au/news/wallabies-team-confirmed-to-play-new-zealand-in-sydney-20261015`; secondary independent report: `https://www.skysports.com/rugby-union/australia-vs-new-zealand/preview/111860`. Ben Donaldson (upper leg), Carter Gordon (leg), Len Ikitau (concussion) ruled out; Hunter Paisami suspended. Will Skelton/Taniela Tupou not on announced squad; reason/contract eligibility not independently confirmed here. Starting playmaker Meredith, 5/3 bench balance and new midfield raise continuity uncertainty. Named is confirmed selection release, NOT separately proof of actual on-field starters.

**New Zealand official originally named XV (15 October):** 1. George Bower; 2. Codie Taylor (c); 3. Fletcher Newell; 4. Scott Barrett; 5. Fabian Holland; 6. Tupou Vaa’i; 7. Peter Lakai; 8. Wallace Sititi; 9. Cam Roigard; 10. Damian McKenzie; 11. Josh Moorby; 12. Jordie Barrett (original Oct15); 13. Quinn Tupaea; 14. Will Jordan; 15. Beauden Barrett. **Bench:** 16. Samisoni Taukei’aho; 17. Xavier Numia; 18. Pasilio Tosi; 19. Shannon Frizell; 20. Du’Plessis Kirifi; 21. Cortez Ratima; 22. Timoci Tavatavanawai (original Oct15); 23. Rieko Ioane. Federation: `https://www.allblacks.com/news/all-blacks/all-blacks-team-named-to-play-australia-in-second-bledisloe-cup-test`; corroboration `https://www.rugby.com.au/news/bledisloe-cup-wallabies-all-blacks-new-zealand-team-rugby-union-20261015`; Reuters contemporary report `https://www.reuters.com/sports/all-blacks-make-three-changes-starting-side-second-bledisloe-cup-test-2026-10-15/`. Unavailable Leroy Carter (ankle), Anton Segner (concussion), Asafo Aumua (concussion), Ethan Blackadder (calf), Richie Mo'unga (calf), Fehi Fineanganofo (hamstring). `Ethan de Groot` replaced by George Bower as selection; injury status not asserted.

**Subsequent revised New Zealand selection:** Official federation `https://www.allblacks.com/news/all-blacks/tavatavanawai-to-start-as-jordie-barrett-ruled-out-of-sydney-test` names **Timoci Tavatavanawai** at 12 in place of **Jordie Barrett** (tight calf), with **Chay Fihaki** on bench at 22; all other original named NZ roles unchanged. **The exact publication clock/time relative to 15:45 AEDT is not independently proven**, so this update is *not* included in the base historical-input centre; separately priced as sensitivity with NZ -1 point. Matchday 23 check beyond these federated releases remains OPEN.

**Playing conditions:** home Australia, Accor Stadium Sydney, earlier international/sevens matches scheduled on same field, possible wear. Independent kickoff-time wind/rain/pitch surface evidence NOT_VERIFIED to known-at cutoff; no fixed weather adjustment inserted. Teams last met 10 Oct 2026 (NZ 50-19 Australia), 4 Oct 2025 (NZ 28-14 in Perth) and 27 Sep 2025 (NZ 33-24 in Auckland); **3-game H2H** is not an independent sample beyond L20 and is treated as one explicit diagnostic overlay, not extra unique games. Rugby Australia 2026 exact results `https://www.rugby.com.au/news/wallabies-team-confirmed-to-play-new-zealand-in-sydney-20261015`; 2025 Rugby Championship `https://www.skysports.com/rugby-union/competitions/the-rugby-championship/results/2025-26`; 2025 Australia internationals `https://www.skysports.com/rugby-union/teams/australia/results/2025-26`; 2026 NZ results `https://www.rugbypass.com/teams/new-zealand/fixtures-results/`; 2025 NZ `https://www.newzealandrugby.net/p/all-blacks-2025-schedule.html`. Some individual 2025 rows corroborated by BBC/Sky; field-level independent collector lineage NOT_CLOSED.

**Full dated history:** `HISTORICAL_40_TEST_MATCHES.csv`, 20 deduplicated senior national XV Tests per team before scheduled start, newest first. Excludes four New Zealand 2026 *tour games versus clubs/provincial franchises* (Stormers, Sharks, Bulls, Lions), NOT counted as Tests or equal-strength league examples. Rows are historical targets captured for research, not training-admitted due to missing raw captures/exact known_at and incomplete row-level independent corroboration.

| Team | Window | Actual n | Points for | Points against | PF per game | PA per game | Avg margin |
|---|---|---:|---:|---:|---:|---:|---:|
| Australia | L5 | 5 | 172 | 154 | 34.40 | 30.80 | +3.60 |
| Australia | L10 | 10 | 354 | 319 | 35.40 | 31.90 | +3.50 |
| Australia | L15 | 15 | 432 | 459 | 28.80 | 30.60 | -1.80 |
| Australia | L20 | 20 | 570 | 596 | 28.50 | 29.80 | -1.30 |
| New Zealand | L5 | 5 | 161 | 140 | 32.20 | 28.00 | +4.20 |
| New Zealand | L10 | 10 | 353 | 269 | 35.30 | 26.90 | +8.40 |
| New Zealand | L15 | 15 | 475 | 380 | 31.67 | 25.33 | +6.33 |
| New Zealand | L20 | 20 | 635 | 486 | 31.75 | 24.30 | +7.45 |

**2026 exact Test season-to-date:** Australia n=9, PF=35.67, PA=30.11; New Zealand n=8, PF=35.25, PA=26.25. **2026 top-tier Test opponents diagnostic:** Australia n=6 PF=28.83/PA=35.33; NZ n=7 PF=33.57/PA=27.57. Top-tier subset definition explicitly includes France/Ireland/SA/Argentina/NZ/Australia, excludes Japan/Italy; it is analyst-assigned, not a trained opponent-strength coefficient. L5/L10/L15/L20 overlap, do not quadruple-count evidence. 2025/test cohort changes and different rival strength affect transportability.

### A4. Primary model attempt, reproducible analyst calculation and expected values

**Primary runtime status** `RESEARCH_ONLY_NO_MODEL / PRIMARY_P_NOT_ESTIMATED`. Actual shell commands from sandbox: `python -m ml capability` **EXIT=1**, stderr `/opt/pyvenv/bin/python: No module named ml`; `timeout 12 git ls-remote https://github.com/danisgreat/Sports-Research.git HEAD` **EXIT=128**, stderr `Could not resolve host: github.com`. GitHub connector successfully read control files at pinned commit but is NOT a local checkout/executable worker. No model competition release; no `python -m ml.workflow research`, verified `EXECUTION.csv`, `PREDICTIONS.csv`, blend-weight/η, fitted model or RL feedback exists. `BASELINE_LEAGUE_V1` also NOT_ESTIMATED—current league profiles retired and no point-in-time admitted international competition history release. Analyst model never populates primary `p_card`.

**Analyst scalar process, deterministic arithmetic `UNCALIBRATED_ANALYST_SCENARIO / NOT_PRIMARY`:**

- Start from 2026 *peer-Test* pooled attack/defence means. Australia against NZ-peer attack {AU PF n=6} = 28.833, New Zealand against peers defence {NZ PA n=7} = 27.571; AU matchup base = arithmetic mean **28.202**. NZ peer attack = 33.571, AU peer defence = 35.333; NZ matchup base **34.452**.
- Matchup/home regime assumes +/- 1.50 point move (AU +1.50, NZ −1.50), then 75% matchup/home and 25% the 3 historical H2H team means AU **19.00**, NZ **37.00**. Thereafter AU -1.50 for named flyhalf change uncertainty and NZ +0; no additional post-publication Jordie adjustment in central. **Every weight and adjustment is declared a sensitivity assumption, not a learned or validated model**; the three H2H events also occur within L20 and are deliberately an overlay on peer rates, not three new independent observations.
- Therefore E[AUS] = 0.75*(28.20238+1.50)+0.25*19−1.50 = **25.52679**; E[NZ] = 0.75*(34.45238−1.50)+0.25*37 = **33.96429**. E[total] = **59.49107**; E[NZ−AUS] = **8.43750**.
- Define latent full-game margin `M=NZ−AUS ~ Normal(8.43750, 15^2)` and total `T=NZ+AUS ~ Normal(59.49107,16^2)`, with cov(T,M)=0 **for analyst illustration only**. Team scores are continuous approximations; actual World Rugby scores are discrete and subject to tries/kicks, pitch/lineups and dependence. Historical L20 marginal variation AU margin SD 19.1, NZ margin SD 16.7; AU total SD 13.7, NZ total SD 10.9; SD margin=15 and SD total=16 are research-informed judgement calls, **not fitted out-of-sample dispersions**. Expected play does not use live target score.
- For half-point lines, no integer push. `P(AUS+9.5)=Phi((9.5−E[M])/15)=0.52823480`; `P(NZ−9.5)=1−that=0.47176520`. `P(Under 60.5)=Phi((60.5−E[T])/16)=0.52513985`; Over = complement **0.47486015**. Computed using Python `math.erf`; floating approximation error ε from numerical CDF effectively negligible, but structural model uncertainty dominant (>0.01), so gate resolution NOT_CERTIFIED.
- **Expected contract value in POINTS (not financial EV):** Australia +9.5 residual `9.5−E[NZ−AUS]` = **+1.063 points**; NZ −9.5 residual = **-1.063**. Under 60.5 residual `60.5−E[T]` = **+1.009 points**; Over = **-1.009**. These expected signed distances are **not** payoff or monetary EV; without an operator's payout/price, monetary EV is UNAVAILABLE and SPORTS_ONLY forbids injecting odds.
- Arithmetic reproduction: `CALCULATION_RECEIPT.json`, `SCENARIOS.csv`, generator source `build_bledisloe.py` (standalone), 40-game input CSV.

### A5. Exact contract scenario pricing / dependence / selection limits

| Contract | Win p (analyst) | Loss p | Push p | Void p (conditioned on valid match) | line distance from model centre |
|---|---:|---:|---:|---:|---|
| Australia +9.5 | 0.52823480 | 0.47176520 | 0 | 0 | margin point line +1.063; z=0.071 |
| New Zealand −9.5 | 0.47176520 | 0.52823480 | 0 | 0 | margin point line −1.063; z=-0.071 |
| Under 60.5 | 0.52513985 | 0.47486015 | 0 | 0 | total point line +1.009; z=0.063 |
| Over 60.5 | 0.47486015 | 0.52513985 | 0 | 0 | total point line −1.009; z=-0.063 |

Validity assumes 80-minute regulation completion and named thresholds; no operator-specified void route, so unconditional W/P/L/V over cancellation status cannot be fully determined. The displayed four p values are **conditional on a valid played full match**. Original `p_card` is **NOT_ESTIMATED** for all; baseline p 0/4, reason `NO_LEAGUE_PROFILE` and `OTHER: unexecuted frozen competition release` (choose primary enumerated reason `NO_LEAGUE_PROFILE`). Ranks 1–4 are analyst diagnostic ranks only, not primary selections.

**Provisional gates (analyst-only diagnostic, never primary PASS):** Rank-1 0.528235 below 0.62. Next best non-complement quantity is Under 60.5 0.525140; lead 0.003095 below 0.04. Rank-2 p=0.525140 below 0.58. The parallel same-quantity complement (NZ −9.5) cannot be counted as independent support. `SHADOW_GATE_RET03=NOT_PASS`, `RET04=NOT_PRIMARY`, `SHADOW_RANK_DELTA=NOT_COMPUTABLE_NO_BASELINE`, `SHADOW_BASE_ONLY=NOT_COMPUTABLE_NO_MIXTURE`.

**Paired losses:** Australia+9.5 loses on M≥10, Under60.5 loses on T≥61. Conditional analyst independence of T and M implies P(both lose) ≈ **0.2240**. Model-free Fréchet bounds **[0.0000, 0.4718]**, wide because empirical covariance unmeasured. The opposite spread contracts are complementary on valid final scores, with disjoint losing sets; that does not imply improved forecasting skill.

### A6. Sensitivities and distinct uncertainty regimes

| Declared scenario change | E score AU–NZ | P(AU +9.5) | P(Under 60.5) |
|---|---|---:|---:|
| central_25pct_H2H_bench_named | 25.5–34.0 | 52.8% | 52.5% |
| no_H2H_weight | 28.2–33.0 | 62.4% | 48.4% |
| 35pct_H2H_weight | 24.5–34.4 | 48.9% | 54.2% |
| NZ_late_Jordie_Barrett_out_minus_1 | 25.5–33.0 | 55.5% | 55.0% |
| Australia_flyhalf_uncertainty_minus_3 | 24.0–34.0 | 48.8% | 56.2% |
| larger_margin_sd_19_total_sd_19 | 25.5–34.0 | 52.2% | 52.1% |
| smaller_margin_sd_12_total_sd_12 | 25.5–34.0 | 53.5% | 53.4% |
| NZ_fast_attack_plus_4 | 25.5–38.0 | 42.2% | 42.6% |
| AUS_home_reply_plus_4 | 29.5–34.0 | 63.2% | 42.6% |

Expected probability ranges are model *sensitivity*, **not confidence intervals**. Key unresolved channels: late NZ Barrett/Tavatavanawai publication/selection, Australia inexperienced fly-half and midfield, Australian home advantage versus recent H2H, 2025 vs 2026 coach/roster regime, opponent tier assignments, and pitch/weather unknown. Any change in score centre changes rank order: `ADJUSTMENT_DEPENDENT` applies to this analyst slate. A genuine World Rugby scoring-process/possession model would require tries/penalty conversion components, territory, lineouts, scrums, referee, injuries and confirmed actual starters; not fitted here.

### A7. Evidence routes / detailed source register / official playing laws

| Source ID | Owner / lineage | Fact/field opened | URL | Publication and capture limitations |
|---|---|---|---|---|
| R01 | Accor Stadium direct organizer | Ground, 15:45 advertised start; full stadium quad-header | https://www.accorstadium.com.au/events/n2026_bledisloe_cup_wallabies_v_all_blacks | Publication exact UNKNOWN; page retrieval in response after advertised start |
| R02 | Rugby Australia field owner | 15 Oct named XV, 23, injuries, 2026 nine results | https://www.rugby.com.au/news/wallabies-team-confirmed-to-play-new-zealand-in-sydney-20261015 | Dated 15 Oct; exact time stamp ambiguous vs browser zone; raw capture missing |
| R03 | All Blacks federation owner | 15 Oct original XV/23, injuries, 16:00 competing start | https://www.allblacks.com/news/all-blacks/all-blacks-team-named-to-play-australia-in-second-bledisloe-cup-test | Original team list recorded, subsequent revision separate; federation native time zone ambiguous |
| R04 | All Blacks federation owner | NZ replacement of Jordie Barrett by Tavatavanawai and bench Chay Fihaki | https://www.allblacks.com/news/all-blacks/tavatavanawai-to-start-as-jordie-barrett-ruled-out-of-sydney-test | Article marked 17 Oct; exact publication before scheduled kickoff NOT_VERIFIED |
| R05 | Reuters editorial | 15 Oct roster changes, injured Australian fly-half | https://www.reuters.com/sports/donaldson-injury-late-blow-wallabies-ahead-all-blacks-clash-2026-10-15/ | Independent journalism; no independent official source of each medical diagnosis beyond team release |
| R06 | RugbyPass / commercial fixture aggregator | 2026 NZ 8 internationals, 4 excluded club tours | https://www.rugbypass.com/teams/new-zealand/fixtures-results/ | Some cached extracts stale; per-game official league corroboration incomplete |
| R07 | Sky Sports / news scoreboard compiler | Australia 2025 Rugby Championship results | https://www.skysports.com/rugby-union/competitions/the-rugby-championship/results/2025-26 | Some other match histories share downstream provider; independent raw owner event IDs absent |
| R08 | Sky Sports / news scoreboard compiler | Australia other 2025 tests | https://www.skysports.com/rugby-union/teams/australia/results/2025-26 | Crossed with BBC Nov match results where available |
| R09 | Secondary NZ historical compiler | 2025 NZ 13 Test scores, latest 12 included | https://www.newzealandrugby.net/p/all-blacks-2025-schedule.html | Not official federation; future owner-record corroboration needed |
| R10 | World Rugby official laws | 80-min Test endpoint, five-point tries and other scoring terms | https://passport.world.rugby/laws-of-the-game/laws-by-number/5-time/ | Public current rule; no additional match-specific overtime demonstrated |

Opened URLs are genuine search/retrieval routes; the downloadable per-game CSV is a compact **research ledger**, not a validated two-independent-collector history. Specific raw HTML, response headers, publication known_at, capture SHA256, exact league population expected n remain missing. `RESEARCH_SOURCE_REGISTER.md` cited for route discovery, but no previously saved capture adopted as present. No restricted/odds sources used. Each field with unavailable proof is kept OPEN in A8. Independent researcher exposure to post-start mutable source **does not establish** clean pre-start input status.

### A8. Missingness, custody, issue gates and next actions

| Required field | Status | Evidence attempted | Impact / next permitted work |
|---|---|---|---|
| Full both-team L5/L10/L15/L20 arithmetic | DONE rows, n20 each | Rugby Australia, NZ fixture archive, Sky, BBC, secondary NZ 2025 | Reconstruct verified 2025 NZ official match-by-match IDs/score, provenance and capture hashes before data admission |
| 2026 NZ club tour strength filter | DONE decision | RugbyPass 2026 12 listed scores | Four club games excluded from test-only 8/20; non-test sources not fed into scoring |
| Actual starters for both sides | PARTIAL published 15 Oct squad; updated NZ selection | Both federation official releases, Sky, Reuters | Obtain exact kickoff gamebook pregame issue timestamp or quarantine KNOWN_AT_UNVERIFIED; don't use postgame score sheets as pregame evidence |
| Timoci Tavatavanawai / Jordie Barrett switch | KNOWN_AT_UNVERIFIED | Official NZ 17 Oct replacement article | Exact time pre-15:45 vs pre-16:00 UNKNOWN; only analyst sensitivity, not base pre-start feature |
| Weather/pitch state | OPEN | Event stadium quadruple header; current-day weather reporting is not immutable pregame forecast | Obtain archived pre-cutoff conditions/credible pitch photo with source publication; no numeric adjustment |
| Main code and fitted release | FAILED_WITH_EXIT_CODES | python no module; git DNS failure; connector protocol read success | Run verified pinned checkout in authorized worker with Python dependency, >=30 reviewed same-competition matches, `ml.workflow` receipt; do not claim ML/RL |
| Admitted baseline, policy eta, warm/feedback separation | NOT_ESTIMATED | Current LEAGUE_PROFILES retired, CYCLE policy read | Verify baseline exact test population; no 0.5 placeholder; actual bundle needed for online expert weights |
| Contract/operator rules | UNKNOWN_DEFINITION | User half-point lines and World Rugby laws | Verify exact payout/void/abandonment conventions; current analyst probabilities conditional on valid completed 80-min match |
| Prestart timing/cohort | BLOCKED | Advertised 15:45; source NZ 16:00; model file created at 2026-10-17T16:05:12+11:00 | No frozen prestart issue; keep POST_START_RESEARCH; cannot enter prospective cohort |
| Writer / desktop mini lease | UNVERIFIED | Read entire last eight-card cumulative sandbox copy, no desktop OS lease | Separate copy `READ_ONLY_DRAFT / NOT_ISSUED`; owner/custodian imports or verifies handover explicitly, no silent authoritative mutation |
| Structured LEARN-v1 exports | PARTIAL_QUARANTINED | history and exact schema, original per-event observation URLs | Many rows lack raw capture SHA/known_at, so no dry-run accepted data and no shared store writes |

### A9. Execution receipts, research completion matrix, integrity and audit

**Read receipt:** GitHub `main` SHA `7e59f83b7f29e034a82ceecf147fe4e5b63e73a3`, 2026-10-17 AEDT; files `CURRENT_STATE.md`, `research/prompts/COMMON_OPERATING_PROTOCOL.md`, `research/prompts/1_GAME_CARD.md`, `RULES_RUGBY_UNION.md`, `SELECTION_RULES.md`, `CARD_AND_LOG_TEMPLATES.md`, `PRIMARY_PREDICTION_PROTOCOL.md`, `FORECAST_CYCLE_PROTOCOL.md`, `LEAGUE_PROFILES.md`, `RESEARCH_COMPLETION_PROTOCOL.md`, `HISTORICAL_SOURCE_PROTOCOL.md`, `ROSTER_AVAILABILITY_PROTOCOL.md`, `MINI_LOG_IDENTITY_PROTOCOL.md`, `LEARNING_PIPELINE_PROTOCOL.md`, `TIMING_RESEARCH_PROTOCOL.md`. `LEAGUE_RULES_RUGBY_UNION.md` was NOT_FOUND (404), rugby union sport/league-specific section in `RULES_RUGBY_UNION.md` serves sport control; no read claimed of missing path. Neither user desktop tree nor current external mini writer lease accessible. Historical game scores from opened web links documented A7. No canonical ID, no settlement, no GitHub write. `python -m ml capability` actual stderr in `ML_CAPABILITY_STDERR.txt`; `git ls-remote` error in `GIT_CHECKOUT_STDERR.txt`. Pinned GitHub API connector can read source files but cannot mount checkout.

| Completion component | State | Explanation |
|---|---|---|
| 1 Authority/identity/endpoint | PARTIAL | Official 15:45 vs 16:00 start conflict; current published controls verified |
| 2 Both-team L5/10/15/20 | DONE_ARITHMETIC / NOT_FULLY_CORROBORATED | 20 Tests each and source URLs; known_at/source lineage incomplete |
| 3 Starting XV/bench/absences | DONE_OFFICIAL_NAMED / LATE_KNOWN_AT_OPEN | Original lineups and late NZ revision tracked separately; current actual start not proven |
| 4 Conditions/venue/competition | PARTIAL | Quad-header context, no reliable source-known-at weather data |
| 5 All supplied contracts | DONE_ANALYST | 4/4 normalized and priced conditional on 80-minute final; operator unknown |
| 6 Expected score/point centre | DONE_ANALYST | Explicit formula, source GF/GA and assumptions; no fitted coefficients |
| 7 Baseline/primary model/ML/RL | BLOCKED_ACTUAL_CAPABILITY | No module and git DNS; 0/4 baseline, 0/4 primary |
| 8 Sensitivities/joint dependence | DONE_ANALYST | 13 scenarios; joint loss independence illustrative, Fréchet bounds |
| 9 Retention/learning/custody | PARTIAL / DRAFT_ONLY | Full cumulative draft and manifest, exact raw captures and owner desktop authority lacking |

**Audit C1–C22:** C1 event identity PARTIAL_NATIVE_ID; C2 competitions/endpoint PASS_RULES; C3 duplicate across minis PARTIAL; C4 actual start NOT_VERIFIED; C5 known-at NOT_VERIFIED; C6 confirmed squad report PASS and actual matchday changes PARTIAL; C7 historical 40 rows PASS_ARITHMETIC and source verification PARTIAL; C8 competition tier score filter DOCUMENTED_ASSUMPTION; C9 weather OPEN; C10 definitions conditional valid Test; C11 expected score arithmetic PASS_ANALYST; C12 all four contract probs PASS_ANALYST; C13 exact W/P/L/V qualifier PARTIAL_VOID; C14 sensitivity PASS_ANALYST; C15 primary model FAIL_WITH_RECEIPTS; C16 baseline 0/4; C17 numeric selection GATE_NOT_CERTIFIED; C18 earlier original cards MARKER_BYTE_PRESERVED (verified by external script after write); C19 no new canonical allocation; C20 roster timing open; C21 primary/analyst separation PASS; C22 full cumulative separate Markdown readback to be verified.

**Final disposition:** `RESEARCH_ONLY_NO_MODEL`, `UNCALIBRATED_ANALYST_SCENARIO / NOT_PRIMARY`; `INFORMATION_INCOMPLETE`, `READ_ONLY_DRAFT / NOT_ISSUED`, `NEW_CANONICAL_ID_NOT_ASSIGNED`. Forecast scores/contract ranks are research-only values produced post-scheduled-start, not valid pregame performance cohort. All previous eight cards must remain byte-identical, no revisions to earlier issued research, no shared learning store, no settlement and no GitHub write.
<!-- END CANONICAL RESEARCH P-609 -->
