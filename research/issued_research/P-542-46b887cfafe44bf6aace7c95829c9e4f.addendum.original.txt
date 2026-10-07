

# Settlement refresh and retrospective corrections — 2026-10-08

Authority main: `de0edc6b0822e88edb7fccd4d11bc33011b5cceb`. Input mini SHA-256: `972413bfa59b9a1a1807dc30e8e9bc50f02113ea9aab17ed57d1835ed060ebc8` (259626 bytes).

The supplied addenda and summary remain frozen earlier-cutoff observations. This dated refresh supersedes their censored outcomes and NDCG calculations. All grades below are sporting diagnostics; operator action, original point-in-time source custody, actual start and independently audited terminal quorum are not certified.

NDCG correction: DCG@2 is divided by ideal DCG@2 using every WIN in the entire frozen ranked slate. P-539 is 0.6131471928 (not 1.000); P-548 is 0.3868528072 (not 0.63093). The earlier four-card mean becomes 0.7500. Unranked complementary rows are graded separately and do not enter the frozen slate metric.

## Settlement refresh for P-538 — Florida Panthers @ Los Angeles Kings

### R1. Original prediction
Rank 1 Panthers ML; Rank 2 full-game Under 5.5; Rank 3 Kings ML; Rank 4 full-game Over 5.5. The original card used `UNCALIBRATED_QUALITATIVE / NOT_ESTIMATED` probabilities and selected Florida as the potential winner.

### R2. Final event
Florida 2-1 Los Angeles; regulation, 3 goals.

### R3. Exact contracts
Rank 1 Panthers ML: WIN; Rank 2 Under 5.5 goals: WIN; Rank 3 Kings ML: LOSS; Rank 4 Over 5.5 goals: LOSS

### R4. Rank diagnostics
{"rank1": 1, "rank2": 1, "hit_at_2": 1, "wins_at_2": 2, "ndcg_at_2": 1.0}

### R5. Winner call
CORRECT sporting winner call; not operator certification

### R6. Line assessment
Florida 2-1 Los Angeles; regulation, 3 goals. Literal thresholds are tested against this endpoint only; complementary and overlapping rows are dependent.

### R7. Expected versus realised mechanism
The low-goal branch and Florida winner direction both realised. They share an event and cannot count as independent successes.

### R8. Missed mechanism and uncertainty
A low final does not by itself verify five-on-five suppression. Official boxscore has Florida 28 shots and Los Angeles 20; no xG mechanism is inferred from score alone.

### R9. Source and timing
Original state, evidence cutoff, ranks and probabilities remain literal. - **Research completion timestamp:** 2026-10-07 13:32 AEDT / 02:32 UTC - **Verified event state:** `START_UNVERIFIED / LATE_RESEARCH`. The official scheduled time had passed, but the accessible official NHL material still presented pregame/gamecenter information and did not expose a reliable current clock/state in the retrieved body. No observed score, shot, penalty, goal, or other in-game event was used as predictive evidence. - **Admission state:** no NHL entry was found in `research/admission_registry.json`; no current NHL model is `LIVE_QUALIFIED` - **Prediction cutoff:** research completed after the nominal 13:00 AEDT scheduled start, with event state not reliably observable in the accessible official body; therefore this is `LATE_RESEARCH / START_UNVERIFIED`, not certified pregame research - **Missingness:** no qualified NHL probability model; exact operator ML action rules absent; event start state not independently verified at research completion 1. **Timing/state:** official scheduled time had passed by research completion, but a reliable live state was not exposed in the accessible official body. The card is therefore `START_UNVERIFIED`, not claimed pregame. Role: official event identity, venue, team records, team/goaltender statistical context. Accessible body did not expose a trustworthy live clock/state at research time. **Source confidence:** official league/team sources dominate identity, roster and current-process evidence. Current state remains `START_UNVERIFIED` because accessible official Gamecenter rendering did not provide a reliable current clock/state at the time of analysis. Source-body retrieval now establishes terminal facts only; it cannot prove pregame availability. No independently audited quorum or complete original source bundle is manufactured.

### R10. Error/process classification
DESCRIPTIVE_CENTRE_WIDTH_RANKING_REVIEW; causal attribution and calibration remain unproven

### R11. Testable hypothesis
Prospectively test side/low-total dependence from one regulation/OT model, retaining joint top-two failure mass and goalie status on the identical future event cohort. Freeze candidate/comparator, sample/power plan, endpoint, acceptance and identical event/line cohort before testing; this event cannot be the untouched test.

### R12. Disposition
MONITOR / PROPOSE_EXPERIMENT; PROPOSED_NOT_TESTED. Implemented process controls are recorded separately; no fitted model parameter changes or promotion.

Sources: [nhl_owner](https://api-web.nhle.com/v1/gamecenter/2026020052/boxscore), [nhl_report](https://www.nhl.com/news/florida-panthers-los-angeles-kings-game-recap-october-6-2026).

## Settlement refresh for P-539 — Aleksandar Kovacevic vs Matteo Berrettini

### R1. Original prediction
Rank 1 Panthers ML; Rank 2 full-game Under 5.5; Rank 3 Kings ML; Rank 4 full-game Over 5.5. The original card used `UNCALIBRATED_QUALITATIVE / NOT_ESTIMATED` probabilities and selected Florida as the potential winner.

### R2. Final event
Berrettini 6-7(3), 6-1, 6-4; aggregate 18-12, total 30.

### R3. Exact contracts
Rank 1 Berrettini -2.5 games: WIN; Rank 2 Under 24.5 games: LOSS; Rank 3 Kovacevic +2.5 games: LOSS; Rank 4 Over 24.5 games: WIN

### R4. Rank diagnostics
{"rank1": 1, "rank2": 0, "hit_at_2": 1, "wins_at_2": 1, "ndcg_at_2": 0.6131471927654584}

### R5. Winner call
CORRECT sporting winner call; not operator certification

### R6. Line assessment
Berrettini 6-7(3), 6-1, 6-4; aggregate 18-12, total 30. Literal thresholds are tested against this endpoint only; complementary and overlapping rows are dependent.

### R7. Expected versus realised mechanism
Favourite separation worked for the game handicap, while the deciding-set path defeated the Under.

### R8. Missed mechanism and uncertainty
Tiebreak plus three sets was an identified failure route. A single realisation cannot establish that its probability was miscalibrated.

### R9. Source and timing
Original state, evidence cutoff, ranks and probabilities remain literal. - **Research completion timestamp:** `2026-10-07 14:59:57 AEDT / 11:59:57 Shanghai time` - **Verified event state at observation:** `PREGAME` — official tournament order of play listed the match first on Stadium Court at 12:00 local, and current time was still before that scheduled start; Tennis.com also showed the fixture as upcoming. No in-match score or point data was used. **Availability assessment:** both players were present in the official Shanghai order of play and no pre-match withdrawal was identified at the evidence cutoff. This does not certify medical fitness or operator retirement terms. - **Evidence cutoff:** 2026-10-07 14:58:26 AEDT, before the 15:00 AEDT scheduled start 7. **Surface/roof state:** official tournament material confirms Deco-Turf hard court; no current roof-state adjustment is made. `FORECAST_CLASSIFICATION: PREGAME_EVIDENCE_CUTOFF_UNCALIBRATED_QUALITATIVE` Source-body retrieval now establishes terminal facts only; it cannot prove pregame availability. No independently audited quorum or complete original source bundle is manufactured.

### R10. Error/process classification
DESCRIPTIVE_CENTRE_WIDTH_RANKING_REVIEW; causal attribution and calibration remain unproven

### R11. Testable hypothesis
Test explicit set-count and tiebreak mixtures against the unchanged comparator on future surface/format-matched fixtures; retain this result solely as a diagnostic example. Freeze candidate/comparator, sample/power plan, endpoint, acceptance and identical event/line cohort before testing; this event cannot be the untouched test.

### R12. Disposition
MONITOR / PROPOSE_EXPERIMENT; PROPOSED_NOT_TESTED. Implemented process controls are recorded separately; no fitted model parameter changes or promotion.

Sources: [shanghai_owner](https://en.rolexshanghaimasters.com/en/scores/results?resultDay=7).

## Settlement refresh for P-540 — Adrian Mannarino vs Nikoloz Basilashvili

### R1. Original prediction
Rank 1 Panthers ML; Rank 2 full-game Under 5.5; Rank 3 Kings ML; Rank 4 full-game Over 5.5. The original card used `UNCALIBRATED_QUALITATIVE / NOT_ESTIMATED` probabilities and selected Florida as the potential winner.

### R2. Final event
Mannarino advanced 6-3, 2-2 RET; partial aggregate 8-5 and 13 observed games do not settle full-match contracts.

### R3. Exact contracts
Rank 1 Mannarino -0.5 games: UNKNOWN_DEFINITION; Rank 2 Over 22.5 games: UNKNOWN_DEFINITION; Rank 3 Basilashvili +0.5 games: UNKNOWN_DEFINITION; Rank 4 Under 22.5 games: UNKNOWN_DEFINITION

### R4. Rank diagnostics
NOT_SCORED: original retirement/action rule unavailable

### R5. Winner call
CORRECT sporting winner call; not operator certification

### R6. Line assessment
Mannarino advanced 6-3, 2-2 RET; partial aggregate 8-5 and 13 observed games do not settle full-match contracts. Literal thresholds are tested against this endpoint only; complementary and overlapping rows are dependent.

### R7. Expected versus realised mechanism
Retirement terminated the completed-match forecast branch. Advancement is sportingly correct for the separate winner call.

### R8. Missed mechanism and uncertainty
The frozen operator action definition is absent. Do not grade the partial total, impose VOID, or retrieve a current rule and pretend it was the original ticket rule.

### R9. Source and timing
Original state, evidence cutoff, ranks and probabilities remain literal. - **Research completion / forecast freeze:** 2026-10-07 16:30:51 AEDT - **Verified event state at freeze:** `PREGAME` - **Cutoff:** 2026-10-07 16:30:51 AEDT - **Post-cutoff/in-match inputs used:** `NONE` - **Medical state:** no current official injury/withdrawal was found, but absence of a withdrawal is not proof of full fitness. Role: match-specific `Upcoming` state at freeze; broader H2H scope including Rennes 2024. Source-body retrieval now establishes terminal facts only; it cannot prove pregame availability. No independently audited quorum or complete original source bundle is manufactured.

### R10. Error/process classification
CONTRACT / RETIREMENT_ACTION_UNKNOWN

### R11. Testable hypothesis
Retain the exact named operator/action/retirement rule and its issue-time source when available on future cards. Preserve unknown terms explicitly; compare unknown-definition rates without changing sporting predictions. Freeze candidate/comparator, sample/power plan, endpoint, acceptance and identical event/line cohort before testing; this event cannot be the untouched test.

### R12. Disposition
SOURCE_PROCESS_CHANGE_CANDIDATE; PROPOSED_NOT_TESTED. Implemented process controls are recorded separately; no fitted model parameter changes or promotion.

Sources: [shanghai_owner](https://en.rolexshanghaimasters.com/en/scores/results?resultDay=7).

## Settlement refresh for P-541 — Mattia Bellucci vs Yi Zhou

### R1. Original prediction
Rank 1 Panthers ML; Rank 2 full-game Under 5.5; Rank 3 Kings ML; Rank 4 full-game Over 5.5. The original card used `UNCALIBRATED_QUALITATIVE / NOT_ESTIMATED` probabilities and selected Florida as the potential winner.

### R2. Final event
Yi Zhou 6-4, 3-6, 7-6(4); aggregate games 16-16, total 32.

### R3. Exact contracts
Rank 1 Bellucci -3.5 games: LOSS; Rank 2 Under 21.5 games: LOSS; Rank 3 Over 21.5 games: WIN; Rank 4 Yi Zhou match winner: WIN

### R4. Rank diagnostics
{"rank1": 0, "rank2": 0, "hit_at_2": 0, "wins_at_2": 0, "ndcg_at_2": 0.0}

### R5. Winner call
INCORRECT sporting winner call; not operator certification

### R6. Line assessment
Yi Zhou 6-4, 3-6, 7-6(4); aggregate games 16-16, total 32. Literal thresholds are tested against this endpoint only; complementary and overlapping rows are dependent.

### R7. Expected versus realised mechanism
The deciding set and tiebreak realised; Bellucci neither won nor exceeded a 3.5-game margin. Equal aggregate games demonstrate why set winner and game margin must be separated.

### R8. Missed mechanism and uncertainty
The 77% analyst winner scenario lost; this is a high-probability miss, not standalone proof of miscalibration. Three-set/tiebreak exposure dominated the 21.5 Under.

### R9. Source and timing
Original state, evidence cutoff, ranks and probabilities remain literal. - **Original research cutoff:** `2026-10-07 18:39:11 AEDT` - **Verified state at forecast cutoff:** `PREGAME` — match-specific secondary source showed `Upcoming`; official order of play still listed the match pending - No credible current withdrawal or medical restriction was established before the forecast cutoff. Role: match-specific `Upcoming` status at the forecast cutoff and player context. Source-body retrieval now establishes terminal facts only; it cannot prove pregame availability. No independently audited quorum or complete original source bundle is manufactured.

### R10. Error/process classification
DESCRIPTIVE_CENTRE_WIDTH_RANKING_REVIEW; causal attribution and calibration remain unproven

### R11. Testable hypothesis
Test a serve/return and set-count mixture on independent ATP hard-court population data, including equal-game matches; evaluate full-slate proper scores and unchanged supplied lines. Freeze candidate/comparator, sample/power plan, endpoint, acceptance and identical event/line cohort before testing; this event cannot be the untouched test.

### R12. Disposition
MONITOR / PROPOSE_EXPERIMENT; PROPOSED_NOT_TESTED. Implemented process controls are recorded separately; no fitted model parameter changes or promotion.

Sources: [shanghai_owner](https://en.rolexshanghaimasters.com/en/scores/results?resultDay=7), [bellucci_tennis](https://www.tennis.com/tournaments/rolex-shanghai-masters/matches/m-bellucci-vs-y-zhou-2026-10-07), [bellucci_lapresse](https://ae.lapresse.it/sport-ae/2026/10/07/tennis-atp-masters-1000-shanghai-bellucci-knocked-out-in-the-first-round/).

## Settlement refresh for P-542 — Adelaide 36ers vs Melbourne United

### R1. Original prediction
Rank 1 Panthers ML; Rank 2 full-game Under 5.5; Rank 3 Kings ML; Rank 4 full-game Over 5.5. The original card used `UNCALIBRATED_QUALITATIVE / NOT_ESTIMATED` probabilities and selected Florida as the potential winner.

### R2. Final event
Melbourne 96-91 Adelaide; total 187, Melbourne margin 5.

### R3. Exact contracts
Rank 1 Under 187.5 points: WIN; Rank 2 Adelaide +9.0 points: WIN; Rank 3 Over 175.5 points: WIN; Rank 4 Melbourne -1.5 points: WIN

### R4. Rank diagnostics
{"rank1": 1, "rank2": 1, "hit_at_2": 1, "wins_at_2": 2, "ndcg_at_2": 1.0}

### R5. Winner call
CORRECT sporting winner call; not operator certification

### R6. Line assessment
Melbourne 96-91 Adelaide; total 187, Melbourne margin 5. Literal thresholds are tested against this endpoint only; complementary and overlapping rows are dependent.

### R7. Expected versus realised mechanism
The 176-187 total band and 2-8 Melbourne margin band both held. All four wins are dependent rows on one event.

### R8. Missed mechanism and uncertainty
The Under won by only 0.5. Melbourne club text has a conflicting 94-91 opening sentence but concludes 96-91; the official league final agrees with the conclusion. Retain the internal conflict rather than silently cherry-pick it.

### R9. Source and timing
Original state, evidence cutoff, ranks and probabilities remain literal. - **Forecast cutoff:** `2026-10-07 19:19:26 AEDT` - **Verified state at forecast cutoff:** `PREGAME / START_UNVERIFIED` — the match-specific NBL Game Centre still appeared in the upcoming fixture set and no verified first `jumpBall` was observed - **Starting-five certainty:** complete official starting fives were not verified at the forecast cutoff. Per BK-P2, this keeps lineup-dependent confidence capped and requires an uncalibrated minutes/availability mixture rather than a fully qualified issue. Source-body retrieval now establishes terminal facts only; it cannot prove pregame availability. No independently audited quorum or complete original source bundle is manufactured.

### R10. Error/process classification
DESCRIPTIVE_CENTRE_WIDTH_RANKING_REVIEW; causal attribution and calibration remain unproven

### R11. Testable hypothesis
Test early-season total centres and widths separately using independent possession/efficiency data and paired chronological evaluation; monitor narrow threshold wins without moving this forecast retrospectively. Freeze candidate/comparator, sample/power plan, endpoint, acceptance and identical event/line cohort before testing; this event cannot be the untouched test.

### R12. Disposition
MONITOR / PROPOSE_EXPERIMENT; PROPOSED_NOT_TESTED. Implemented process controls are recorded separately; no fitted model parameter changes or promotion.

Sources: [nbl_owner](https://league.nbl.com.au/news/trevor-gleeson-adelaide-36ers-scared-outworked-united), [nbl_club](https://www.melbourneutd.com.au/news/nbl27-match-recap-adelaide-36ers-vs-melbourne-united-7-october-2026).

## Settlement refresh for P-543 — Hiroshima Toyo Carp @ Hanshin Tigers

### R1. Original prediction
Rank 1 Panthers ML; Rank 2 full-game Under 5.5; Rank 3 Kings ML; Rank 4 full-game Over 5.5. The original card used `UNCALIBRATED_QUALITATIVE / NOT_ESTIMATED` probabilities and selected Florida as the potential winner.

### R2. Final event
Hanshin 2-1 Hiroshima after 11 innings; total 3, Hanshin margin 1; regulation through nine was 1-1.

### R3. Exact contracts
Rank 1 Carp +1.5 runs: WIN; Rank 2 Hanshin win: WIN; Rank 3 Under 5.5 runs: WIN; Rank 4 Over 5.5 runs: LOSS

### R4. Rank diagnostics
{"rank1": 1, "rank2": 1, "hit_at_2": 1, "wins_at_2": 2, "ndcg_at_2": 1.0}

### R5. Winner call
CORRECT sporting winner call; not operator certification

### R6. Line assessment
Hanshin 2-1 Hiroshima after 11 innings; total 3, Hanshin margin 1; regulation through nine was 1-1. Literal thresholds are tested against this endpoint only; complementary and overlapping rows are dependent.

### R7. Expected versus realised mechanism
The exact one-run Hanshin win is the covering-pair branch in which both top picks win. Extra innings were needed.

### R8. Missed mechanism and uncertainty
A stale pregame mirror and a secondary 1-1 row were superseded by the exact official 11-inning terminal body. The 1-1 regulation score cannot settle a full-game moneyline.

### R9. Source and timing
Original state, evidence cutoff, ranks and probabilities remain literal. - **Forecast cutoff:** `2026-10-07 19:59:00 AEDT` (17:59 JST) - **Verified state at cutoff:** `PREGAME` — official NPB page still displayed `試合開始前` and 0 pitches/0 plate appearances **Official starting lineups at the cutoff** Source-body retrieval now establishes terminal facts only; it cannot prove pregame availability. No independently audited quorum or complete original source bundle is manufactured.

### R10. Error/process classification
DESCRIPTIVE_CENTRE_WIDTH_RANKING_REVIEW; causal attribution and calibration remain unproven

### R11. Testable hypothesis
Test endpoint-specific baseball adapters on tied-through-nine/extra-innings fixtures; require explicit final state, inning count and tie semantics before deriving full-game contracts. Freeze candidate/comparator, sample/power plan, endpoint, acceptance and identical event/line cohort before testing; this event cannot be the untouched test.

### R12. Disposition
MONITOR / PROPOSE_EXPERIMENT; PROPOSED_NOT_TESTED. Implemented process controls are recorded separately; no fitted model parameter changes or promotion.

Sources: [npb_owner](https://npb.jp/scores/2026/1007/t-c-25/).

## Settlement refresh for P-544 — Doosan Bears @ LG Twins

### R1. Original prediction
Rank 1 Panthers ML; Rank 2 full-game Under 5.5; Rank 3 Kings ML; Rank 4 full-game Over 5.5. The original card used `UNCALIBRATED_QUALITATIVE / NOT_ESTIMATED` probabilities and selected Florida as the potential winner.

### R2. Final event
LG 7-5 Doosan; nine innings, total 12, LG margin 2.

### R3. Exact contracts
Rank 1 Doosan +1.5 runs: LOSS; Rank 2 LG +0.5 runs: WIN; Rank 3 Over 7.5 runs: WIN; Rank 4 Under 7.5 runs: LOSS

### R4. Rank diagnostics
{"rank1": 0, "rank2": 1, "hit_at_2": 1, "wins_at_2": 1, "ndcg_at_2": 0.38685280723454163}

### R5. Winner call
CORRECT sporting winner call; not operator certification

### R6. Line assessment
LG 7-5 Doosan; nine innings, total 12, LG margin 2. Literal thresholds are tested against this endpoint only; complementary and overlapping rows are dependent.

### R7. Expected versus realised mechanism
The LG direction and Over realised. Doosan +1.5 missed by 0.5 runs; a competitive score did not ensure a winning cushion.

### R8. Missed mechanism and uncertainty
The official inning line has five Doosan runs in the third, and LG runs in the second, third and fifth. Do not claim a bullpen or fatigue cause without pitcher-level evidence.

### R9. Source and timing
Original state, evidence cutoff, ranks and probabilities remain literal. - **Forecast/research cutoff:** `2026-10-07 20:15:20 AEDT` / `18:15:20 KST`. - **Observed state at cutoff:** `PREGAME / START_UNVERIFIED`. The official KBO Game Center still listed the fixture as scheduled. No observed runs, pitches, plate appearances or other in-game outcomes were used. Source-body retrieval now establishes terminal facts only; it cannot prove pregame availability. No independently audited quorum or complete original source bundle is manufactured.

### R10. Error/process classification
DESCRIPTIVE_CENTRE_WIDTH_RANKING_REVIEW; causal attribution and calibration remain unproven

### R11. Testable hypothesis
Test starter-to-relief transition uncertainty and key run margins with pre-cutoff usage data on a fixed KBO cohort; separate total and margin errors. Freeze candidate/comparator, sample/power plan, endpoint, acceptance and identical event/line cohort before testing; this event cannot be the untouched test.

### R12. Disposition
MONITOR / PROPOSE_EXPERIMENT; PROPOSED_NOT_TESTED. Implemented process controls are recorded separately; no fitted model parameter changes or promotion.

Sources: [kbo_owner](https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-10-07), [kbo_lg_onsite](https://sports.khan.co.kr/article/202610072126013).

## Settlement refresh for P-545 — Hanwha Eagles @ Kiwoom Heroes

### R1. Original prediction
Rank 1 Panthers ML; Rank 2 full-game Under 5.5; Rank 3 Kings ML; Rank 4 full-game Over 5.5. The original card used `UNCALIBRATED_QUALITATIVE / NOT_ESTIMATED` probabilities and selected Florida as the potential winner.

### R2. Final event
Kiwoom 5-3 Hanwha; nine innings, total 8, Kiwoom margin 2.

### R3. Exact contracts
Rank 1 Kiwoom +2.5 runs: WIN; Rank 2 Over 9.5 runs: LOSS; Rank 3 Hanwha ML: LOSS; Rank 4 Under 9.5 runs: WIN

### R4. Rank diagnostics
{"rank1": 1, "rank2": 0, "hit_at_2": 1, "wins_at_2": 1, "ndcg_at_2": 0.6131471927654584}

### R5. Winner call
INCORRECT sporting winner call; not operator certification

### R6. Line assessment
Kiwoom 5-3 Hanwha; nine innings, total 8, Kiwoom margin 2. Literal thresholds are tested against this endpoint only; complementary and overlapping rows are dependent.

### R7. Expected versus realised mechanism
The underdog cushion survived, but Hanwha winner and high-total directions failed. The Under complement won.

### R8. Missed mechanism and uncertainty
Starter uncertainty did not produce the anticipated high-scoring branch. The supplementary NewsPim report is AI-assisted and is not used to certify an independent collection lineage.

### R9. Source and timing
Original state, evidence cutoff, ranks and probabilities remain literal. - **Forecast-input cutoff:** `2026-10-07 20:19:48 AEDT` / `18:19:48 KST`, before scheduled first pitch. `PREGAME_INPUT_CUTOFF: 2026-10-07 20:19:48 AEDT` Source-body retrieval now establishes terminal facts only; it cannot prove pregame availability. No independently audited quorum or complete original source bundle is manufactured.

### R10. Error/process classification
DESCRIPTIVE_CENTRE_WIDTH_RANKING_REVIEW; causal attribution and calibration remain unproven

### R11. Testable hypothesis
Test separate centre/width effects of starter-role uncertainty using verified pre-start roles and relief usage; measure fixed-line winner and total errors without replacing the comparator. Freeze candidate/comparator, sample/power plan, endpoint, acceptance and identical event/line cohort before testing; this event cannot be the untouched test.

### R12. Disposition
MONITOR / PROPOSE_EXPERIMENT; PROPOSED_NOT_TESTED. Implemented process controls are recorded separately; no fitted model parameter changes or promotion.

Sources: [kbo_owner](https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-10-07), [kbo_kiwoom_report](https://www.newspim.com/news/view/20261007001640).

## Settlement refresh for P-546 — Samsung Lions @ KT Wiz

### R1. Original prediction
Rank 1 KT +1.5 (74.0%); Rank 2 Samsung +1.5 (62.8%); Rank 3 Over 9.5 (53.0%); Rank 4 Under 9.5 (47.0%). Potential winner KT 55.5%.

### R2. Final event
KT 9-3 Samsung; nine innings, total 12, KT margin 6.

### R3. Exact contracts
Rank 1 KT +1.5 runs: WIN; Rank 2 Samsung +1.5 runs: LOSS; Rank 3 Over 9.5 runs: WIN; Rank 4 Under 9.5 runs: LOSS

### R4. Rank diagnostics
{"rank1": 1, "rank2": 0, "hit_at_2": 1, "wins_at_2": 1, "ndcg_at_2": 0.6131471927654584}

### R5. Winner call
CORRECT sporting winner call; not operator certification

### R6. Line assessment
KT 9-3 Samsung; nine innings, total 12, KT margin 6. Literal thresholds are tested against this endpoint only; complementary and overlapping rows are dependent.

### R7. Expected versus realised mechanism
KT winner/cushion and Over realised. Samsung +1.5 failed; the covering pair wins together only on a sufficiently close game.

### R8. Missed mechanism and uncertainty
The official inning line has five KT runs in the eighth. A six-run realised margin exposes width risk but does not establish a permanent favourite-separation adjustment.

### R9. Source and timing
Original state, evidence cutoff, ranks and probabilities remain literal. **Forecast cutoff:** 2026-10-07 18:26:54 KST / 20:26:54 AEDT **Observed state at cutoff:** PREGAME / START_UNVERIFIED KBO's October 7 schedule lists Samsung at KT in Suwon at 18:30 KST. Same-day lineup reporting confirmed **Won Tae-in** for Samsung and **So Hyeong-jun** for KT, with both starting nines published before the cutoff. Official KBO team batting through the October 7 pregame state: Suwon has been a high-run 2026 venue in the available park split (10.50 runs/game). Because an official field-weather receipt was not recovered before cutoff, no wind/temperature directional adjustment is applied. Weather is therefore **NOT USED DIRECTIONALLY**. Samsung beat KIA 5-4 on October 6. The official English scoreboard records Lee Jae-hee as winning pitcher and Bae Chan-seung as the save pitcher. A full verified reliever-usage ladder was not recovered before cutoff, so Samsung bullpen availability is widened rather than guessed. - No official same-day injury bulletin beyond the posted active starting lineups was recovered before cutoff; availability inferences are limited to published lineups/rosters. - Complete Samsung relief usage from October 6 was not recovered before cutoff, so no unverified bullpen-depletion claim is made. - An official field-weather receipt was not recovered before cutoff, so weather is not used directionally. Source-body retrieval now establishes terminal facts only; it cannot prove pregame availability. No independently audited quorum or complete original source bundle is manufactured.

### R10. Error/process classification
DESCRIPTIVE_CENTRE_WIDTH_RANKING_REVIEW; causal attribution and calibration remain unproven

### R11. Testable hypothesis
Test upper margin tails and late-inning total clustering on independently collected KBO population games, retaining both winning and losing cushion rows. Freeze candidate/comparator, sample/power plan, endpoint, acceptance and identical event/line cohort before testing; this event cannot be the untouched test.

### R12. Disposition
MONITOR / PROPOSE_EXPERIMENT; PROPOSED_NOT_TESTED. Implemented process controls are recorded separately; no fitted model parameter changes or promotion.

Sources: [kbo_owner](https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-10-07), [kbo_kt_onsite](https://isplus.com/article/view/isp202610070243).

## Settlement refresh for P-547 — NC Dinos @ SSG Landers

### R1. Original prediction
Rank 1 NC +1.5 (61.8%); Rank 2 SSG ML (56.0%); Rank 3 Over 9.5 (54.6%); Rank 4 Under 9.5 (45.4%). Potential winner SSG 56.0%.

### R2. Final event
SSG 6-3 NC; nine innings, total 9, SSG margin 3.

### R3. Exact contracts
Rank 1 NC +1.5 runs: LOSS; Rank 2 SSG ML: WIN; Rank 3 Over 9.5 runs: LOSS; Rank 4 Under 9.5 runs: WIN

### R4. Rank diagnostics
{"rank1": 0, "rank2": 1, "hit_at_2": 1, "wins_at_2": 1, "ndcg_at_2": 0.38685280723454163}

### R5. Winner call
CORRECT sporting winner call; not operator certification

### R6. Line assessment
SSG 6-3 NC; nine innings, total 9, SSG margin 3. Literal thresholds are tested against this endpoint only; complementary and overlapping rows are dependent.

### R7. Expected versus realised mechanism
The SSG winner direction and Under won. The NC cushion missed; the Over missed by 0.5 runs.

### R8. Missed mechanism and uncertainty
Official innings place four SSG runs in the third, two in the seventh and three NC runs in the eighth. No missing lineup or bullpen cause is inferred from final alone.

### R9. Source and timing
Original state, evidence cutoff, ranks and probabilities remain literal. **Research/log cutoff:** 2026-10-07 20:31:13 AEDT / 18:31:13 KST **Timing classification:** scheduled start had just passed; actual first pitch was not independently verified at the analysis cutoff. Only pre-start/static information was used. No observed game action was used. - The scheduled start had just passed when the research cutoff was recorded; actual first pitch was not independently verified. This card is therefore `LATE_START_UNVERIFIED`, not falsely backdated as pregame. Source-body retrieval now establishes terminal facts only; it cannot prove pregame availability. No independently audited quorum or complete original source bundle is manufactured.

### R10. Error/process classification
DESCRIPTIVE_CENTRE_WIDTH_RANKING_REVIEW; causal attribution and calibration remain unproven

### R11. Testable hypothesis
Test lineup-missingness sensitivity and margin-tail width with future prospectively frozen KBO scenarios. Preserve LATE_START_UNVERIFIED as a separate cohort label. Freeze candidate/comparator, sample/power plan, endpoint, acceptance and identical event/line cohort before testing; this event cannot be the untouched test.

### R12. Disposition
MONITOR / PROPOSE_EXPERIMENT; PROPOSED_NOT_TESTED. Implemented process controls are recorded separately; no fitted model parameter changes or promotion.

Sources: [kbo_owner](https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-10-07), [kbo_ssg_onsite](https://www.starnewskorea.com/en/sports/2026/10/07/2026100716313989473).

## Settlement refresh for P-548 — Busan KCC Egis vs Daegu Korea Gas Corporation Pegasus

### R1. Original prediction
Rank 1 Under 178.5 (64.5%); Rank 2 Korea Gas +8.5 (59.5%); Rank 3 Over 168.5 (57.9%); Rank 4 KCC -2.5 (56.8%). Potential winner KCC 63.5%.

### R2. Final event
KCC 103-98 Korea Gas; quarter scores 30-32, 28-18, 29-28, 16-20; regulation total 201, margin 5.

### R3. Exact contracts
Rank 1 Under 178.5 points: LOSS; Rank 2 Korea Gas +8.5 points: WIN; Rank 3 Over 168.5 points: WIN; Rank 4 KCC -2.5 points: WIN

### R4. Rank diagnostics
{"rank1": 0, "rank2": 1, "hit_at_2": 1, "wins_at_2": 1, "ndcg_at_2": 0.38685280723454163}

### R5. Winner call
CORRECT sporting winner call; not operator certification

### R6. Line assessment
KCC 103-98 Korea Gas; quarter scores 30-32, 28-18, 29-28, 16-20; regulation total 201, margin 5. Literal thresholds are tested against this endpoint only; complementary and overlapping rows are dependent.

### R7. Expected versus realised mechanism
The five-point margin agrees with the scenario centre, while the 172-point total centre was 29 points too low. Side/cushion rows held and the leading Under lost.

### R8. Missed mechanism and uncertainty
Centre and width require separate diagnosis. Changed foreign-player usage is a plausible regime hypothesis, not a causal conclusion established by this one high total.

### R9. Source and timing
Original state, evidence cutoff, ranks and probabilities remain literal. - **Forecast-input cutoff:** approximately 20:58 AEDT / 18:58 KST, before the scheduled tip. - **Research completion:** after the scheduled tip, but no observed game action, score, possessions or live statistics were used. - **State:** `PREGAME_INPUT_CUTOFF / RESEARCH_COMPLETION_AFTER_SCHEDULED_START`. - No authoritative static source with both confirmed starting fives was recovered before the modelling cutoff. Probable core exposure was therefore used rather than inventing a confirmed five. Source-body retrieval now establishes terminal facts only; it cannot prove pregame availability. No independently audited quorum or complete original source bundle is manufactured.

### R10. Error/process classification
DESCRIPTIVE_CENTRE_WIDTH_RANKING_REVIEW; causal attribution and calibration remain unproven

### R11. Testable hypothesis
Test KBL same-season possession and PPP centre shifts separately from width under the changed roster regime, using chronological independent population data and preregistered acceptance. Freeze candidate/comparator, sample/power plan, endpoint, acceptance and identical event/line cohort before testing; this event cannot be the untouched test.

### R12. Disposition
MONITOR / PROPOSE_EXPERIMENT; PROPOSED_NOT_TESTED. Implemented process controls are recorded separately; no fitted model parameter changes or promotion.

Sources: [kbl_yna](https://www.yna.co.kr/amp/view/AKR20261007201300007), [kbl_basketkorea](https://www.basketkorea.com/news/newsview.php?ncode=1065613721301888), [kbl_sbs](https://news.sbs.co.kr/english/article.do?news_id=N1008787988).

## Settlement refresh for P-549 — Foshan Nanshi vs Guangxi Hengchen

### R1. Original prediction
Rank 1 Guangxi X2 (81.85%); Rank 2 Guangxi team Over 0.5 (79.81%); Rank 3 Under 3.5 (78.29%); Rank 4 1H Over 0.5 (61.33%); Rank 5 Under 2.5 (57.49%). Potential winner Guangxi 56.90%, draw 24.95%, Foshan 18.15%.

### R2. Final event
Foshan 1-0 Guangxi, halftime 0-0; regulation full-game total 1 and Guangxi total 0.

### R3. Exact contracts
Rank 1 Guangxi X2: LOSS; Rank 2 Guangxi team Over 0.5 goals: LOSS; Rank 3 Under 3.5 goals: WIN; Rank 4 1H Over 0.5 goals: LOSS; Rank 5 Under 2.5 goals: WIN

### R4. Rank diagnostics
{"rank1": 0, "rank2": 0, "hit_at_2": 0, "wins_at_2": 0, "ndcg_at_2": 0.0}

### R5. Winner call
INCORRECT sporting winner call; not operator certification

### R6. Line assessment
Foshan 1-0 Guangxi, halftime 0-0; regulation full-game total 1 and Guangxi total 0. Literal thresholds are tested against this endpoint only; complementary and overlapping rows are dependent.

### R7. Expected versus realised mechanism
Both leading Guangxi-dependent rows lost together. Low full-time totals won, while the first-half Over lost. The scoreless-away branch was an issued failure route.

### R8. Missed mechanism and uncertainty
No verified pre-cutoff XI existed. Final score cannot demonstrate which absent player/tactical feature caused the miss; table rank and urgency do not establish causal motivation.

### R9. Source and timing
Original state, evidence cutoff, ranks and probabilities remain literal. - **Forecast-input cutoff:** 2026-10-07 19:27:37 CST / 22:27:37 AEDT, before scheduled kickoff. - **State at cutoff:** `PREGAME / START_UNVERIFIED`. - A verified current starting XI, complete bench, formation and penalty/set-piece-taker sheet for both teams was **not recovered before the cutoff**. - No reliable same-day source establishing additional injuries/suspensions was recovered before cutoff; missing information remains uncertainty rather than an assumption of full health. **Status:** `UNCALIBRATED_ANALYST_SCENARIO — PARTICIPANT-CAPPED` because a verified current XI/bench was not recovered before cutoff. Source-body retrieval now establishes terminal facts only; it cannot prove pregame availability. No independently audited quorum or complete original source bundle is manufactured.

### R10. Error/process classification
DESCRIPTIVE_CENTRE_WIDTH_RANKING_REVIEW; causal attribution and calibration remain unproven

### R11. Testable hypothesis
Test participant-missingness mixtures and joint away-scoreless/home-win tail mass on a fixed China League One cohort, with untouched chronology and identical supplied contracts. Freeze candidate/comparator, sample/power plan, endpoint, acceptance and identical event/line cohort before testing; this event cannot be the untouched test.

### R12. Disposition
MONITOR / PROPOSE_EXPERIMENT; PROPOSED_NOT_TESTED. Implemented process controls are recorded separately; no fitted model parameter changes or promotion.

Additional unranked issued complement: 1H Under 0.5 goals — **WIN**.

Additional unranked issued complement: Full-time Over 2.5 goals — **LOSS**.

Sources: [soccer_sportradar](https://statshub.sportradar.com/sportradar/en/match/69456656), [soccer_dongqiudi](https://pc.dongqiudi.com/articles/6450059.html).

## Counts and interpretation

```json
{
  "events": 12,
  "fully_sporting_graded": 11,
  "partially_graded": 1,
  "ranked_rows": 49,
  "win": 26,
  "loss": 19,
  "unknown_definition": 4,
  "push": 0,
  "void": 0,
  "no_action": 0,
  "terminal_censored": 0,
  "additional_unranked_rows": 2,
  "additional_unranked_win": 1,
  "additional_unranked_loss": 1,
  "rank1": 6,
  "rank2": 6,
  "hit_at_2": 9,
  "wins_at_2": 12,
  "mean_ndcg_at_2": 0.5454545454545454,
  "winner_calls_correct": 9,
  "winner_calls_total": 12,
  "performance_certified": 0,
  "prior_retained_carryovers": 53,
  "prior_active_sporting_carryovers": 32
}
```

Rank-1/Rank-2 each 6/11; Hit@2 9/11; Wins@2 12/22; mean full-slate NDCG@2 0.545455; sporting winner calls 9/12. Four unresolved retirement rows are excluded, explicitly, from ranking metrics. No baseline skill, calibration, monetary return or independent-row trial count is inferred.

## Historical carryover audit

All 53 selected historical records were matched against the mini carryover inventory; all remain retained once under their original IDs. The mini divides them into 32 active sporting/contract gaps and 21 certification/reference pointers. Operator terms, identity conflicts, exact periods/provider fields, original source custody and independent collection gaps cannot be closed from new-event finals. Embedded DO NOT SETTLE text is source-document context, not an instruction overriding the user. This pass does not manufacture historical closure or reallocate any carried ID. Full per-record remaining requirements are reproduced in UNRESOLVED_CARRYOVER.md and carryover.json.

