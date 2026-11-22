# Mini settlement · 20261120-495CEEB69E9540938CF6A7DAA7B546B4 · P-697 to P-703 (mini-settlement-10)

<!-- SETTLEMENT-FORMAT: mini-settlement-10 -->
**Settled:** 2026-11-22T22:30:00+11:00 (P-697–P-700) and 2026-11-23T07:00:00+11:00 (P-701–P-703) · **Framework:** MDS-2026.11.22-v29.2 / CR-2026.11.22-R1 / SCV-2026.11.18-v20 / P-2026.11.22-v29.2 · **Authority:** `LOCAL_WORKING_TREE`, branch `settle/mini-20261120-495CEEB6` from `main` `ad70fdb04`.
**Cards were written under:** MDS-2026.11.18-v29.1 (main `cb97bbc2a`). They are settled on their own frozen contracts; no v29.2 rule is applied to them retroactively.

**Frozen original:** mini `20261120-495CEEB69E9540938CF6A7DAA7B546B4`, pulled byte for byte on 22 November 2026 from `origin/forecast-seals` at `ad9df53e10c6` (requests, three sealed cards, seal ledger rows) and `origin/card-drops` at `3939f9b2b778` (four refused card drops). Archived unchanged at [archive/settled_minis_2026-11-22/20261120-495CEEB69E9540938CF6A7DAA7B546B4/](../../../archive/settled_minis_2026-11-22/20261120-495CEEB69E9540938CF6A7DAA7B546B4/README.md).
**FROZEN_SOURCE receipt:** written at the pull, before any settlement text: [FROZEN_MANIFEST.csv](../../../archive/settled_minis_2026-11-22/20261120-495CEEB69E9540938CF6A7DAA7B546B4/FROZEN_MANIFEST.csv) (38 files, each with bytes, SHA-256 and source ref); per-card bytes and hashes in [FROZEN_SOURCE.csv](FROZEN_SOURCE.csv).
**Source growth check:** rechecked at 2026-11-23T06:50 AEDT: `card-drops` had no drop for this mini after G0007 and `forecast-seals` no later seal. A later drop under this key goes to the next settlement run.
**Inventory:** 7 registered requests, 7 cards (G0001–G0007): 3 sealed (G0001, G0003, G0007), 4 refused at sealing (G0002, G0004, G0005, G0006). **All 7 settled**; nothing pending ([UNRESOLVED_POST_IMPORT.csv](UNRESOLVED_POST_IMPORT.csv) is empty). G0005–G0007 had no permitted final on the evening of 22 November and were settled the next morning, before the import.

## Executive summary

- **Games settled:** 7 distinct events, **P-697 to P-703**, **30 contract rows**: 15 WIN, 15 LOSS, 0 PUSH, 0 VOID, **0 UNRESOLVED**.
- **Descriptive slot counts:** Rank 1 **3W / 4L**; Rank 2 **2W / 5L**. Four of the seven cards are refused drops; their ranks are the registered rule computed on the card, never registered ranks.
- **Card-mean Brier:** P-697 0.2568, P-698 0.1999, P-699 0.3106, P-700 0.3002, P-701 0.2386, P-702 0.1494, P-703 0.2931; mean 0.2498 (`d = +0.0002`). The three sealed cards (P-697, P-699, P-703): 0.2868 (`d = -0.0368`). Descriptive only.
- **Track P:** no game here qualifies yet. The three sealed cards have no verified first play; two of them (G0001, G0007) were sealed after their scheduled start, so they count only if a permitted first-play capture shows play began after the seal. The other four were never sealed.
- **Deep loss reviews:** **9 reviews** (`DLR-2026-11-22-011` to `019`) plus joint sections for P-699, P-700 and P-703.
- **Contract defect carried literally:** P-700 L1 ("Blue Jackets +0.5") and L2 ("Maple Leafs +0.5") are one winner contract registered twice, as v29.2 now refuses. Both rows are settled as issued; the duplicate is flagged in every table that uses them.

## Local identity and canonical handoff

LOCAL_ID_MAPPING: each settled key keeps `LOCAL-<card key>` and its native identity; the prompt-4 import in this same session assigned P-697 to P-703 in scheduled-start order ([LOCAL_ID_MAPPING.csv](LOCAL_ID_MAPPING.csv), [ALL_RECORD_MAPPING.csv](ALL_RECORD_MAPPING.csv)).

## Source discovery, corroboration and reuse register (EXH-v1 / SRC-ALT-v3)

Information completion: **INFORMATION_INCOMPLETE**. Every final, linescore and grade is closed; actual first play is open on all seven cards.

Every URL was audited with `ml.source_audit` (the eight-name script rule) and fetched only through `ml.source_access.fetch_bytes`, which re-audits each redirect. Captures are byte-exact under `../one_chat_captures/2026-11-22-2/` with [CAPTURE_MANIFEST.csv] and the audit rows in [SOURCE_ACCESS_AUDIT.csv](SOURCE_ACCESS_AUDIT.csv). Refused or unknown hosts were not opened: `www.nba.com`, `api.foxsports.com`, `api-web.nhle.com`, `apnews.com`, `sports.yahoo.com`, `www.landofbasketball.com`, `www.espn.com.au`, `www.sportingnews.com`, `www.abc.net.au` (`BLOCKED_FOR_AI`), `www.thecfa.cn`, `www.sofascore.com`, `www.besoccer.com`, `www.dongqiudi.com` (`RULES_UNKNOWN`). Betting widgets on shaiba.kz were not read.

| Source ID / exact scope | URL | Fields observed / missing | Lineage | Retrieval | Capture / reuse |
|---|---|---|---|---|---|
| SRC-20261122-2-697-1 · IBSL game page | https://basket.co.il/game-zone.asp?GameId=26688&lang=en | quarters, box score; no wall-clock tip | IBSL (owner) | 2026-11-22 ~10:10Z | `G0001_ibsl_game26688.html` |
| SRC-20261122-2-697-2 · IBSL results list | https://basket.co.il/results-by-date.asp?Board=5&lang=en | 90-80, date, venue | IBSL, same owner | 2026-11-22 ~10:04Z | `G0001_ibsl_results.html`; not independent |
| SRC-20261122-2-698-1 · FotMob match | https://www.fotmob.com/matches/beijing-guoan-vs-shanghai-port/9g2g0by | score, goal minutes, cards, corners, shots, halves | FotMob data feed | ~10:04Z | `G0002_fotmob.html` |
| SRC-20261122-2-698-2 · Beijing Guoan FC report (zhibo8) | https://news.zhibo8.com/zuqiu/2026-11-20/6b004dfca4060native.htm | 0-2, 26' VAR penalty and red card, HT 0-1, Vital 59'; no corners | the home club | ~10:40Z | `G0002_zhibo8_report.html`; independent of FotMob |
| SRC-20261122-2-699-1 · StatMuse box | https://www.statmuse.com/nba/ask/pacers-vs-cavaliers-box-score-november-20-2026 | quarters, team and player stats, plays (game clock) | NBA stats via StatMuse | ~10:20Z | `G0003_statmuse.html` |
| SRC-20261122-2-699-2 · Fox Sports game page | https://www.foxsports.com/nba/indiana-pacers-vs-cleveland-cavaliers-nov-20-2026-game-boxscore-106761 | "defeated the Pacers, 128-119" (club recap text); linescore placeholders only | Fox / Cavaliers | ~10:12Z | `G0003_fox_box.html`; score only |
| SRC-20261122-2-700-1 · StatMuse box | https://www.statmuse.com/nhl/ask/blue-jackets-vs-maple-leafs-box-score-november-21-2026 | goals by period, shots, PP, goalies | NHL stats via StatMuse | ~10:20Z | `G0004_statmuse.html` |
| SRC-20261122-2-700-2 · Fox Sports game page | https://www.foxsports.com/nhl/columbus-blue-jackets-vs-toronto-maple-leafs-nov-21-2026-game-boxscore-44917 | "the Leafs 4-3 loss" (club video text) | Fox / Maple Leafs | ~10:12Z | `G0004_fox_box.html`; score only |
| SRC-20261122-2-701-1 · NBL Fixtures game page | https://www.nblfixtures.com/games/brisbane-bullets-vs-sydney-kings-2026-11-22 | quarters, game leaders, play-by-play (game clock) | NBL data via nblfixtures | ~19:47Z | `G0005_nblfixtures_r3.html` (earlier captures showed "Awaiting final result") |
| SRC-20261122-2-701-2 · Brisbane Bullets recap | https://www.brisbanebullets.com.au/news/recap-full-power-bullets-take-down-kings | 115-104, 21/49 3PT, offensive rebounds 19-8, assists 33, Kings absences | the home club | ~19:55Z | `G0005_bullets_recap.html`; independent |
| SRC-20261122-2-702-1 · shaiba.kz match report | https://shaiba.kz/news/812431 | 6:3 (3:1, 0:1, 3:1), every goal with time, goalies | shaiba.kz | ~19:58Z | `G0006_shaiba_report.html` |
| SRC-20261122-2-702-2 · shaiba.kz match page | https://shaiba.kz/match/39216/mkhk_aktobe-mkhk_torpedo/22-11-2026 | live feed at 5:3 in the 3rd period | shaiba.kz, same owner | ~10:04Z | `G0006_shaiba.html`; not independent; betting widgets not read |
| SRC-20261122-2-703-1 · sportsguff scorecard | https://sportsguff.com/scorecard/women-s-big-bash-league-2026-27/melbourne-renegades-women-vs-melbourne-stars-women-32nd-match | toss, Stars 159/7, phases 57/0 + 78/3 + 24/4, fall of wickets | sportsguff | ~19:50Z | `G0007_sg_try.html` (frozen during the chase; the Stars innings is complete in it) |
| SRC-20261122-2-703-2 · cricket.com.au match page | https://www.cricket.com.au/matches/CA:40652/melbourne-stars-women-melbourne-renegades-women-match-32 | none: renders client-side | Cricket Australia | ~19:48Z | `G0007_ca.html`; no independent second lineage found |

Every attempt, including partial, refused and mistaken ones (a neighbouring IBSL game captured by mistake and not used), is in [SOURCE_SEARCH_ATTEMPTS.csv](SOURCE_SEARCH_ATTEMPTS.csv); requirement status per event in [REQUIREMENT_CLOSURE.csv](REQUIREMENT_CLOSURE.csv).

## Per-card settlements, R1–R12 retrospectives and DEEPLOSS-v1 reviews

<!-- BEGIN SETTLEMENT P-697 LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0001 revision-1 -->
### P-697 · Basketball/Israel Super League (IBSL GameId 26688, Winner League Game 7) — Ironi Hai Motors Ness Ziona @ Hapoel Altshuler Shaham Beer Sheva/Dimona · 2026-11-20 IST · revision-1

**Revision:** revision-1 · parent NONE · effective 2026-11-22T22:30:00+11:00 · affected ALL · changes NONE.
**Card state:** SETTLED.
- **Local key / native ID:** `LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0001` · `REQ:BASKETBALL:ISRAEL_SUPER_LEAGUE:HAPOEL_BEER_SHEVA:IRONI_NESS_ZIONA:2026-11-20T11:10:00Z`.
- **Custody & timing:** `SEALED` (server push `2026-11-20T11:15:24Z`, commit `824758df2`; scheduled tip `2026-11-20T11:10:00Z`, so sealed 5m24s after it; research `11:07:49Z`–`11:14:40Z`). Assessment `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`. Actual first play `NOT_VERIFIED`: no permitted page gives a wall-clock tip-off. It counts for Track P only if a later capture shows tip-off after 11:15:24Z.
- **Verified final (B):** **Hapoel Altshuler Shaham Beer Sheva/Dimona 90-80 Ironi Hai Motors Ness Ziona**, regulation. By quarter BSD 27-19-22-22=90, NZ 20-24-24-12=80 (sum check 27+19+22+22=90, 20+24+24+12=80; box check BSD 23×2+11×3+11=90, NZ 24×2+7×3+11=80). Home margin +10, total 170.
- **Source & capture:** IBSL game page `G0001_ibsl_game26688.html` (SHA-256 in [EVENT_FINALS.csv](EVENT_FINALS.csv)); IBSL results list (same owner). Evidence B: one owner lineage.
- **Definition:** HANDICAP and TOTAL on the final score including any overtime (`INCLUDE_OVERTIME` in the registered CONTRACTS.csv). Operator terms unknown and not needed.
- **Expected vs final:** home margin centre −9.020 (SD 12.566), observed +10: error +19.02, z = +1.51 (PIT 0.935). Total centre 171.313 (SD 18.795), observed 170: z = −0.07.
- **Card-mean Brier / d:** 0.2568 / −0.0068.

| Rank | Exact original proposition | Original p | BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| NOT_RANKED | Beer Sheva/Dimona +7.5 | 0.45186 | UNAVAILABLE | **WIN** | B | no | margin +10 + 7.5 > 0 |
| R1 | Ness Ziona −7.5 | 0.54814 | UNAVAILABLE | **LOSS** | B | yes (rank 1) | away margin −10 − 7.5 < 0 |
| R2 | Over 169.5 | 0.53843 | UNAVAILABLE | **WIN** | B | yes (rank 2) | 170 > 169.5 |
| NOT_RANKED | Under 169.5 | 0.46157 | UNAVAILABLE | **LOSS** | B | no | 170 > 169.5 |

**R1–R12 retrospective:** The card was a thin six-game form model: 0.4 × season + 0.6 × last five, no home edge, no opponent adjustment, and it said itself that no row reached its own 62% / 58% rank gates. The registered ranker still ranked both favoured sides, at 0.548 and 0.538, both inside the 0.05 no-direction band. Beer Sheva, 1–5 coming in, won by ten on 11/24 from three (45.8%) and 23/40 on twos (57.5%), against Ness Ziona's 7/21 (33.3%) and 24/52 (46.2%). Ness Ziona's 17 offensive rebounds to 8 did not make up for 18 turnovers to 15. The total landed half a point over the line. Grades come from the box score; nothing was backfilled.

**Deep-review triggers (DEEPLOSS-v1):** top side Ness Ziona −7.5 (0.548, LOSS) = rank 1 · top total Over 169.5 (0.538, WIN) → one review.

#### Deep loss review · P-697 · TOP_SIDE_AND_RANK_1 · Ironi Hai Motors Ness Ziona −7.5 (`DLR-2026-11-22-011`)

**1. Exact frozen claim.** L1 HANDICAP AWAY −7.5 on the final score including overtime, p = 0.54814; centre: Ness Ziona by 9.020; no reference p, no BASELINE_P (`UNAVAILABLE:NO_FROZEN_SPORTING_BASELINE`), no ledger rows. Server seal 2026-11-20T11:15:24Z, after the 11:10:00Z scheduled tip; actual tip unverified.
**2. Verified outcome.** Beer Sheva/Dimona 90-80 (quarters above, sum and box checks pass); regulation. Ness Ziona needed to win by 8 or more; it lost by 10, missing the line by 17.5 points (1.39 frozen SDs).
**3. Distribution check.** In the frozen N(−9.02, 12.566) home-margin model the actual +10 sits at PIT 0.935 (z = +1.51). The card gave a home win by 10 or more 7.0%. Row Brier 0.3005 against 0.2500 for a constant 0.5; log loss 0.794 against 0.693. The card's own work made this row worse than no forecast.
**4. Error decomposition.** The centre (−9.02) came wholly from the blend of six-game for/against means. No home edge was added: the card says "no numeric home adjustment made", so the centre carried 0 for home court. No opponent adjustment was made, though the card notes Beer Sheva had already faced Hapoel Tel Aviv and Hapoel Jerusalem. The width (12.57, from the two teams' six margins) was not the failure: a 19-point miss in a 12.6-point SD is uncommon but not extreme.
**5. Research audit, fact by fact.** Fixture, date, venue and both teams' six results: TRUE (IBSL pages, captured before the game per the card). Records W1–L5 and W4–L2: TRUE as of the cutoff. Rest days 3 and 4: not re-verified (NOT_ASSESSABLE). Starting fives and absences: marked MISSING by the card; Amari Bailey, whom the card noted as season-inactive, does not appear in the box score, consistent with the card. Missed before the cutoff: home court and schedule strength, both knowable from the same IBSL pages. No market, exposure or invention breach.
**6. What decided the game.** Three-point shooting: Beer Sheva 11/24 (45.8%) against 7/21 (33.3%), +12 points from three. Two-point efficiency: 57.5% against 46.2%. Turnovers: Ness Ziona 18, Beer Sheva 15, with Beer Sheva 11 steals. Ness Ziona 17 offensive rebounds to 8 kept it within ten. Beer Sheva led 27-20 after one and 68-68 after three, then won the fourth 22-12.
**7. Knowable at the cutoff?** Home court: KNOWABLE (fixture page). Schedule strength behind Beer Sheva's 1–5: KNOWABLE (its six opponents were on the results list). Shooting splits: NOT_KNOWABLE. Fourth-quarter 22-12: NOT_KNOWABLE.
**8. Process audit.** No reference or effect-table row was declared; there is no IBSL home-edge row in the repository, and the card set it to 0 rather than declare a scenario. The L5 and season windows overlap (five of six games), so the 0.6 weight on L5 counts most games twice. The line choice was supplied by the owner. p = 0.548 sits inside the no-direction band, and the card itself refused to rank it; the registered ranker ranked it anyway. Arithmetic reproduces (Φ((−9.02 + 7.5)/12.566) = 0.452 home side).
**9. Verdict.** **MIXED.** A MODEL_LIMIT part: a six-game, unshrunk, schedule-blind centre with home court set to 0, in a league with no repository parameters. A VARIANCE part: a 12-point three-point swing. The pick should not have been made. The card already said so, and the 0.548 number carried no direction.
**10. Cutoff-only counterfactual.** Declared scenario, diagnostic only: shrink the form margin 50% toward 0 (six games) and add a +3.0 home edge, a scenario value, not a measured IBSL row. The home-margin centre becomes −1.5, and P(Ness Ziona −7.5) = Φ((−7.5 + 1.5)/12.566) ≈ 0.32. The card's side would have flipped.
**11. Failure class and recurrence.** `SMALL_SAMPLE_STRENGTH_OVERREACH`. `ml deep-loss tally` groups by printed alias. Without an alias the class now has 2 reviews (P-662, P-697), below the threshold of 3. The same registered class has 3 more reviews under the alias `PLUS_HANDICAP_WITHOUT_OPPONENT_CHECK` (P-660, P-685, P-693), and that group is already routed to prompt 8. Five reviews in all share the underlying failure: small, unadjusted early-season samples.
**12. Correction.** Already in the v30.0 list ([TRIAGE](../external_reviews_2026-11-22/TRIAGE.md)): empirical-Bayes shrinkage of early-season form, plus an opponent-adjusted centre and a declared home-edge row before pricing a small-sample league. Owner: prompt 8 under a new registration. Acceptance test: on held-out IBSL/FIBA-40 games, Brier of the shrunk, home-adjusted centre below the unshrunk one. Rollback: keep the current recipe. No change is made under FREEZE-v1.
**13. Matched wins.** Over 169.5 (rank 2) won by half a point with the same unshrunk recipe: a coin-flip number on a 0.5-point margin is not evidence the recipe works.
**14. Honesty checklist.** PASS: no post-game fact used as if known; the variance part is quantified (+12 from three); no percentages of blame; frozen rows, ranks and grades unchanged.

<!-- END SETTLEMENT P-697 LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT P-698 LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0002 revision-1 -->
### P-698 · Soccer/China FA Cup semi-final — Shanghai Port @ Beijing Guoan · 2026-11-20 CST · revision-1

**Revision:** revision-1 · parent NONE · effective 2026-11-22T22:30:00+11:00 · affected ALL · changes NONE.
**Card state:** SETTLED.
- **Local key / native ID:** `LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0002` · `REQ:SOCCER:CHINA_FA_CUP:BEIJING_GUOAN:SHANGHAI_PORT:2026-11-20T11:35:00Z`.
- **Custody & timing:** `UNSEALED`: the drop was refused for having no not-started page and no `not_started_observed_at`. The card's research began 2026-11-20T11:36:22Z. FotMob's half-time record gives the first half starting at "20.11.2026 12:35:27" on its own clock, about 11:35:27Z if that clock is UTC+1 (unofficial). If so, research began about a minute after kick-off. The card records no outcome seen. Assessment `UNSEALED_DROP_REFUSED`; research only.
- **Verified final (A):** **Beijing Guoan 0-2 Shanghai Port**, 90 minutes, no extra time. First half 0-1 (Wu Lei, penalty, about 30'); second half 0-1 (Mateus Vital 59'). Sum check 0+0=0, 1+1=2. Corners 3-3 = 6. Beijing's Wang Gang sent off at 26-27' (VAR handball, penalty).
- **Sources & captures:** FotMob `G0002_fotmob.html`; Beijing Guoan FC's own report, republished by zhibo8, `G0002_zhibo8_report.html` (2026-11-20 21:42:53 CST). Two independent lineages; corners from FotMob only.
- **Definition:** L1 first half including stoppage time; L2 goals and L3 corners in regulation 90 minutes (registered contracts). No extra time was played, so regulation equals the full match.
- **Expected vs final:** goals λ 3.061, observed 2 (P(T ≤ 2) = 0.410); first-half λ 1.265, observed 1; corners μ 9.99 (NB r 20.52), observed 6 (P(C ≤ 6) = 0.184).
- **Card-mean Brier / d:** 0.1999 / +0.0501.

| Rank | Exact original proposition | Original p | BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| R1 | First-half goals Over 0.5 | 0.71775 | UNAVAILABLE | **WIN** | A | yes (rank 1) | 1 > 0.5 |
| NOT_RANKED | First-half goals Under 0.5 | 0.28225 | UNAVAILABLE | **LOSS** | A | no | 1 > 0.5 |
| R2 | Total goals Over 2.5 | 0.59034 | UNAVAILABLE | **LOSS** | A | yes (rank 2) | 2 < 2.5 |
| NOT_RANKED | Total goals Under 2.5 | 0.40966 | UNAVAILABLE | **WIN** | A | no | 2 < 2.5 |
| NOT_RANKED | Total corners Over 10.5 | 0.41429 | UNAVAILABLE | **LOSS** | A (FotMob) | no | 6 < 10.5 |
| R3 | Total corners Under 10.5 | 0.58571 | UNAVAILABLE | **WIN** | A (FotMob) | no (rank 3) | 6 < 10.5 |

Ranks are the registered rule computed on this refused card, not registered ranks.

**R1–R12 retrospective:** The card's Poisson (λ 3.061) and negative-binomial corner (μ 9.99) arithmetic reproduces exactly (0.59034 and 0.58571). The match turned at 26': VAR gave a penalty and a red card against Beijing's Wang Gang, one of the card's confirmed starters, and Wu Lei scored it. That settled the first-half Over by itself. A ten-man Beijing then had 1 shot on target all match. Shanghai had 18 shots, 9 on target and 13 big chances (FotMob), and scored once more. The research began after kick-off, so the card is research-only whatever its grades.

**Deep-review triggers (DEEPLOSS-v1):** top side none (no winner or handicap row) · top total Over 2.5 goals (0.590, LOSS) · rank 1 first-half Over 0.5 (0.718, WIN) → one review.

#### Deep loss review · P-698 · TOP_TOTAL · Total goals Over 2.5 (`DLR-2026-11-22-012`)

**1. Exact frozen claim.** L2 TOTAL OVER 2.5 goals, regulation 90 minutes, p = 0.59034 from an independent-Poisson total with λ = 3.061 (60% season actual/xG mix, 25% L10, 15% L5). No reference, BASELINE_P or ledger rows. Never sealed; research began about a minute after kick-off.
**2. Verified outcome.** 0-2 at 90 minutes (both sources); 2 goals, missing the line by 0.5. In the frozen model a 2-goal game had probability 0.219, and at most 2 goals 0.410.
**3. Distribution check.** PIT for 2 goals is between P(T ≤ 1) = 0.190 and P(T ≤ 2) = 0.410: a mid-low outcome, not a tail. Row Brier 0.3485 against 0.25; log loss 0.892 against 0.693.
**4. Error decomposition.** Centre 3.061 against an observed 2: −1.06 goals. The centre already exceeded both teams' season means (Beijing 58 for/36 against, Shanghai 56/37 in 30 games). It was raised by recent Shanghai scoring (16 in its last five). No adjustment was made for a cup semi-final, the cold, or Beijing's three listed absences. The Poisson width is set by λ, so there is no separate width error.
**5. Research audit, fact by fact.** Starting XIs: TRUE as far as the club report and FotMob show (Wang Gang, Wu Lei and Mateus Vital all started). Season records and goals: not re-verified against an official CSL table (NOT_ASSESSABLE; the cited sites were not re-opened). H2H 0-0 on 5 September: TRUE (FotMob h2h). Timing: research after kick-off, which the card disclosed. No market, exposure or invention breach found.
**6. What decided the game.** The 26' red card and penalty. Then Shanghai's finishing: 13 big chances and 9 shots on target for 2 goals, against Beijing's 2 big chances and 1 shot on target. A ten-man home side cuts its own attack, which lowers expected goals even as the visitors dominate. Shanghai had 66% of the ball in the second half.
**7. Knowable at the cutoff?** Red card: NOT_KNOWABLE. Shanghai's conversion: NOT_KNOWABLE. Cup-semi tempo: PARTLY (a signal; no measured size).
**8. Process audit.** L1 (first half Over 0.5) and L2 (Over 2.5) share one goal process. The card said so ("Correlated with L1") and did not rank them as independent evidence. The overlapping L5 inside L10 inside the season gives recent games extra weight. The arithmetic reads back exactly. Research started after kick-off, the card's largest process failure; it makes the card unusable for Track P regardless of the result.
**9. Verdict.** **VARIANCE**, shown by the numbers in 3 and 6: a 41% outcome in the frozen model, decided by a 26' red card and 13 big chances turned into 2 goals. Whether the pick should have been made: the number was a fair reading of both teams' scoring, but the card was written after kick-off and should not have been carded as a pre-game card.
**10. Cutoff-only counterfactual.** NOT_ASSESSABLE: no knowable driver had a measurable effect to price.
**11. Failure class and recurrence.** `VARIANCE` (11 earlier VARIANCE reviews; VARIANCE is never a pattern).
**12. Correction.** NO_CHANGE for the forecast. The timing failure is already handled: from v29.2 the brief allows late requests, and the card counts only with a not-started page during research and a seal before the captured first play.
**13. Matched wins.** First-half Over 0.5 (rank 1) won from the same process, but on a penalty after a red card: that win says nothing for the first-half model. Corners Under (rank 3) won with 6 against a 9.99 centre (P(≤ 6) = 0.18 in the card's own model); no measured effect explains the low count, so the win is not evidence for the corner model.
**14. Honesty checklist.** PASS.

<!-- END SETTLEMENT P-698 LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT P-699 LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0003 revision-1 -->
### P-699 · Basketball/NBA Cup East Group B (game 0022600045) — Indiana Pacers @ Cleveland Cavaliers · 2026-11-20 ET · revision-1

**Revision:** revision-1 · parent NONE · effective 2026-11-22T22:30:00+11:00 · affected ALL · changes NONE.
**Card state:** SETTLED.
- **Local key / native ID:** `LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0003` · `NBA:0022600045`.
- **Custody & timing:** `SEALED` (server push `2026-11-21T00:28:31Z`, commit `deccbd118`; scheduled tip 00:30:00Z, so sealed 89 s before it; research 00:24:09Z–00:27:02Z, not-started check 00:25:14Z). Assessment `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`. Actual first play `NOT_VERIFIED`: nba.com is refused under the script rule, and StatMuse gives only the game clock. The most likely Track P candidate in this mini, once a permitted tip-off time is found.
- **Verified final (A):** **Cleveland Cavaliers 128-119 Indiana Pacers**, regulation. IND 29-32-22-36=119, CLE 29-33-43-23=128 (sum checks pass; box check IND 2×29+3×14+19=119, CLE 2×27+3×19+17=128). Home margin +9, total 247.
- **Sources & captures:** StatMuse box `G0003_statmuse.html`; Fox Sports page with the Cavaliers' recap text "128-119" `G0003_fox_box.html`.
- **Definition:** final score including overtime (registered).
- **Expected vs final:** CLE margin centre +4.24 (SD 14.05), observed +9: z = +0.34 (PIT 0.633). Total centre 230.81 (SD 18.70), observed 247: z = +0.87 (PIT 0.807).
- **Card-mean Brier / d:** 0.3106 / −0.0606.

| Rank | Exact original proposition | Original p | BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| R2 | Indiana Pacers +5.5 | 0.53574 | UNAVAILABLE | **LOSS** | A | yes (rank 2) | −9 + 5.5 < 0 |
| NOT_RANKED | Cleveland Cavaliers −5.5 | 0.46426 | UNAVAILABLE | **WIN** | A | no | 9 − 5.5 > 0 |
| NOT_RANKED | Over 234.5 | 0.42185 | UNAVAILABLE | **WIN** | A | no | 247 > 234.5 |
| R1 | Under 234.5 | 0.57815 | UNAVAILABLE | **LOSS** | A | yes (rank 1) | 247 > 234.5 |

**R1–R12 retrospective:** The card used a real pace × efficiency centre: 103.4 possessions with season offence/defence pairings, plus L10 and L5 pairings and a league home edge of +1.66 (split). Its availability list held up in the box score: Haliburton, Sheppard and Furphy out for Indiana; Mobley, Tyson, Tomlin and Diop out for Cleveland; Nembhard available; Watson, listed questionable, played. Both teams shot well from three: CLE 19/44 (43.2%), IND 14/34 (41.2%). Harden scored 51 with 7/11 from three. Cleveland won the third quarter 43-22. Estimated possessions (FGA + 0.44·FTA − OREB + TO) were about 106 (IND) and 111 (CLE), above the card's 103.4.

**Deep-review triggers (DEEPLOSS-v1):** top side Indiana +5.5 (0.536, LOSS) · top total Under 234.5 (0.578, LOSS) = rank 1 → two reviews and a joint section.

#### Deep loss review · P-699 · TOP_TOTAL_AND_RANK_1 · Under 234.5 (`DLR-2026-11-22-013`)

**1. Exact frozen claim.** L2 TOTAL UNDER 234.5 points including overtime, p = 0.57815. Centre 230.809 from 60% season-efficiency pairing (230.4), 25% L10 (228.85) and 15% L5 (235.6), plus a 4.68% overtime branch adding 10 points. SD 18.70, the NBA residual floor. No reference p, no BASELINE_P, no ledger rows. Sealed 00:28:31Z, 89 s before the scheduled tip.
**2. Verified outcome.** 247 points (sum checks pass), regulation; over the line by 12.5 (0.67 SD) and over the centre by 16.2 (0.87 SD).
**3. Distribution check.** PIT 0.807. The card gave a total of 247 or more about 20%. Row Brier 0.3343 against 0.25; log loss 0.863 against 0.693.
**4. Error decomposition.** Pace: about 108 average possessions against 103.4, worth about +10 points at the card's efficiencies. Efficiency: Cleveland about 1.16 points per possession (128 / about 111) against the card's 1.127 pairing. The weighting: the L5 pairing (235.6) was already above the line, and the card gave it 15%. The width matched the league floor.
**5. Research audit, fact by fact.** Availability list: TRUE throughout (box score, inactive list). Rest days and no back-to-back: TRUE (both last played 18 November). Efficiency and pace figures from TeamRankings: plausible but not re-verified (NOT_ASSESSABLE without re-opening). Season scoring rows: consistent with the records (IND 5-10 → 5-11, CLE 8-8 → 9-8 per the Fox recap). No market or exposure breach; the card says the source's betting sections were not used.
**6. What decided the game.** Three-point shooting: 33/78 combined (42.3%). Cleveland's 43-point third quarter. Harden's 51 points. Possessions about 5% above the card's figure.
**7. Knowable at the cutoff?** Harden's 51: NOT_KNOWABLE. The shooting: NOT_KNOWABLE. Higher pace: PARTLY (both teams' L5 scored more, a signal the 15% weight mostly discounted).
**8. Process audit.** A pace model was used, so this is not `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`. Overlapping windows (L5 inside L10 inside the season) are weighted as if independent. The overtime branch's +10 is an unlearned analyst constant (disclosed). p = 0.578 sits just under the card's own 58% Rank 2 gate; the card ranked nothing, the registered ranker ranked it first.
**9. Verdict.** **VARIANCE**, shown by the numbers: a PIT 0.81 outcome driven by 42% three-point shooting and a 51-point game. Whether the pick should have been made: the number was honest and the card did not claim a pick; it was not a strong edge.
**10. Cutoff-only counterfactual.** Declared scenario, diagnostic only: weight L5, L10 and season equally. The centre becomes about 232.1 (with the overtime branch) and P(Under 234.5) about 0.55. Nothing knowable would have flipped it.
**11. Failure class and recurrence.** `VARIANCE`.
**12. Correction.** NO_CHANGE for this row. The recency-weighting issue is in the v30.0 list (fitted, non-overlapping recency weights).
**13. Matched wins.** None on this card.
**14. Honesty checklist.** PASS.

#### Deep loss review · P-699 · TOP_SIDE · Indiana Pacers +5.5 (`DLR-2026-11-22-014`)

**1. Exact frozen claim.** L1 HANDICAP AWAY +5.5 including overtime, p = 0.53574; CLE margin centre +4.24 (including +1.66 home), SD 14.05. Flags `NO_DIRECTION`, `UNMEASURED_AVAILABILITY_PRICED`, `PLUS_HANDICAP`. Rank 2.
**2. Verified outcome.** Cleveland by 9; Indiana +5.5 lost by 3.5 points (0.25 SD).
**3. Distribution check.** PIT of the margin 0.633 (z = +0.34). The card gave Cleveland by 6 or more 46.4%. Row Brier 0.2870; log loss 0.767 against 0.693.
**4. Error decomposition.** Centre +4.24 against +9: a 4.8-point miss. The third quarter alone went 43-22 to Cleveland. The width is right for the league.
**5. Research audit, fact by fact.** As above: availability TRUE; both teams' records TRUE. Mobley out was priced at 0 (UNMEASURED) while Cleveland was the side missing its best defender. Cleveland won anyway.
**6. What decided the game.** Cleveland's third quarter (43-22) and Harden's 51. Indiana won the fourth 36-23 to get within 9.
**7. Knowable at the cutoff?** NOT_KNOWABLE for both drivers. Mobley's absence was known, but its effect was not measurable from the card's sources.
**8. Process audit.** p = 0.536 has no direction, and the card refused to rank it; the registered ranker ranked it second. Both unmeasured absences (Haliburton, Mobley) were priced as 0. That is honest, but it puts an unmeasured line in a ranked slot. A plus handicap was taken without an opponent-strength adjustment beyond season efficiency.
**9. Verdict.** **VARIANCE**: a 0.34-SD miss on a no-direction number. The pick should not have been ranked; it was a coin flip.
**10. Cutoff-only counterfactual.** NOT_ASSESSABLE: no effect-table row exists for Haliburton or Mobley.
**11. Failure class and recurrence.** `VARIANCE`.
**12. Correction.** NO_CHANGE under FREEZE-v1. The shadow selection policy (SELECT-SHADOW-v1, registered today) drops no-direction rows and is the test of whether that helps.
**13. Matched wins.** None.
**14. Honesty checklist.** PASS.

**Joint section (P-699).** Both rows lost to one shared driver: Cleveland's 43-point third quarter raised the total and widened the margin at once. The card priced them as two independent one-dimensional normals; it said it had not identified their correlation. Indiana +5.5 with the Under is a positively correlated pair, since a high-scoring Cleveland game hurts both. Ranking both in the top two concentrated one risk. Class note: `SHARED_DRIVER_TOP_TWO`, recorded in prose only, since each row has its own class above.

<!-- END SETTLEMENT P-699 LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0003 revision-1 -->

<!-- BEGIN SETTLEMENT P-700 LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0004 revision-1 -->
### P-700 · Ice Hockey/NHL Regular Season (game 2026020364) — Columbus Blue Jackets @ Toronto Maple Leafs · 2026-11-21 ET · revision-1

**Revision:** revision-1 · parent NONE · effective 2026-11-22T22:30:00+11:00 · affected ALL · changes NONE.
**Card state:** SETTLED.
- **Local key / native ID:** `LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0004` · `NHL:2026020364`.
- **Custody & timing:** `UNSEALED`: the drop was refused because labels L1 and L2 each had one side. The request was registered at 00:06:32Z, after the 00:00:00Z scheduled puck drop; research ran 00:06:33Z–00:11:01Z. The card disclosed that its not-started evidence was a stale preview page. Assessment `UNSEALED_DROP_REFUSED`; research only.
- **Verified final (A):** **Columbus Blue Jackets 4-3 Toronto Maple Leafs**, regulation. CBJ 1-1-2=4, TOR 2-1-0=3 (sum checks pass). Goals: 1st 18:38 TOR (PP), 19:43 CBJ, 19:55 TOR; 2nd 05:10 TOR, 15:26 CBJ (PP); 3rd 15:40 CBJ, 16:32 CBJ. Shots 35-26 CBJ; power plays 1/3 each; goalies Talbot (CBJ) 23/26, Stolarz (TOR) 31/35 in 58 minutes; no empty-net goal.
- **Sources & captures:** StatMuse box `G0004_statmuse.html`; Fox Sports page with the Maple Leafs' video text "the Leafs 4-3 loss" `G0004_fox_box.html`.
- **Definition:** both +0.5 rows and the 6.5 total include overtime and the shootout (registered). No overtime was played.
- **Contract defect (carried literally):** "Blue Jackets +0.5" (L1) and "Maple Leafs +0.5" (L2) are the same two-way winner contract, since no draw is possible with OT/SO. Each was registered as its own one-sided label, so this card counts one result twice: once as a win and once as a loss. v29.2 refuses such a request at registration.
- **Expected vs final:** TOR margin centre +0.21, observed −1; total centre 6.046, observed 7. The frozen grid gave P(total ≥ 7, or 3-3 then OT) = 0.421.
- **Card-mean Brier / d:** 0.3002 / −0.0502 (three labels, two of them one contract).

| Rank | Exact original proposition | Original p | BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| R3 | Columbus Blue Jackets +0.5 | 0.46831 | UNAVAILABLE | **WIN** | A | no (rank 3) | CBJ won in regulation |
| R2 | Toronto Maple Leafs +0.5 | 0.53169 | UNAVAILABLE | **LOSS** | A | yes (rank 2) | TOR lost |
| NOT_RANKED | Over 6.5 | 0.42098 | UNAVAILABLE | **WIN** | A | no | 7 > 6.5 |
| R1 | Under 6.5 | 0.57902 | UNAVAILABLE | **LOSS** | A | yes (rank 1) | 7 > 6.5 |

Ranks are the registered rule computed on this refused card: each one-sided label's only row counts as its favoured side.

**R1–R12 retrospective:** The card's facts held: Stolarz and Talbot started; Monahan and Garland did not play; Marchenko, acquired by Toronto, was in a non-contact jersey. Its negative-binomial regulation grid and 50/50 overtime split were coherent, and the arithmetic is internally consistent. Toronto led 3-1 five minutes into the second; Columbus scored three unanswered, two of them 52 seconds apart late in the third. Columbus outshot Toronto 35-26, with 78 shot attempts to 49. The card was researched after the scheduled puck drop and never sealed, so it is research only.

**Deep-review triggers (DEEPLOSS-v1):** top side Maple Leafs +0.5 (0.532, LOSS) · top total Under 6.5 (0.579, LOSS) = rank 1 → two reviews and a joint section.

#### Deep loss review · P-700 · TOP_TOTAL_AND_RANK_1 · Under 6.5 (`DLR-2026-11-22-016`)

**1. Exact frozen claim.** L3 TOTAL UNDER 6.5 goals including OT/SO, p = 0.57902. Grid: negative binomial (k = 28.03), regulation λ CBJ 2.838 and TOR 3.046, 3-3 sent to OT. No reference p, no BASELINE_P, no ledger rows. Researched after the scheduled puck drop; not sealed.
**2. Verified outcome.** 7 goals in regulation (sum checks pass); over the line by 0.5 and over the centre by 0.95.
**3. Distribution check.** The card gave 7 or more goals (including a 3-3 regulation tie) 42.1%: a common outcome, not a tail. Row Brier 0.3353 against 0.25; log loss 0.865 against 0.693.
**4. Error decomposition.** The centre (6.05) was 0.95 low. Both goalies stopped about 88.5% (Talbot .885, Stolarz .886) against season rates of .909 and .904 cited by the card. That is roughly a goal above expectation at these shot counts (61 shots × about 2 points of save percentage ≈ 1.2 goals).
**5. Research audit, fact by fact.** Goalies: TRUE. Absences (Monahan, Garland; Marchenko on Toronto's side): TRUE per the box score and morning-skate report. Records and last-ten scorelines: consistent (Toronto's losing run continued). Timing: research after the scheduled puck drop, disclosed. No market breach.
**6. What decided the game.** Three goals in 77 seconds at the end of the first period, two Columbus goals in 52 seconds in the third, and both goalies at about .885.
**7. Knowable at the cutoff?** NOT_KNOWABLE: the goal bursts and save rates.
**8. Process audit.** Coherent grid; goalie effect set to 0 (UNMEASURED, disclosed). p = 0.579 is just under the card's own 58% gate; the card ranked nothing. The research was after the scheduled start, the card's main process failure.
**9. Verdict.** **VARIANCE**: a 42% outcome reached through about a goal of below-average goaltending.
**10. Cutoff-only counterfactual.** NOT_ASSESSABLE: no measured goalie row.
**11. Failure class and recurrence.** `VARIANCE`.
**12. Correction.** NO_CHANGE.
**13. Matched wins.** Over 6.5 and Columbus +0.5 are the complements of the losing rows, not independent wins.
**14. Honesty checklist.** PASS.

#### Deep loss review · P-700 · TOP_SIDE · Toronto Maple Leafs +0.5 (`DLR-2026-11-22-015`)

**1. Exact frozen claim.** L2 HANDICAP HOME +0.5 including OT/SO, which is "Toronto wins", p = 0.53169. Regulation win 0.451 plus half of the 0.162 tie mass; home edge +0.31 goals from the repository's NHL row. The same contract as L1 (Columbus +0.5, p = 0.46831), registered separately.
**2. Verified outcome.** Columbus 4-3 in regulation: Toronto lost.
**3. Distribution check.** A Columbus regulation win had probability 0.387 in the card's grid: an ordinary outcome. Row Brier 0.2827; log loss 0.759 against 0.693.
**4. Error decomposition.** The centre (Toronto +0.21) was near even, so no material error. Toronto led 3-1 and lost the last 35 minutes 0-3 while being outshot.
**5. Research audit, fact by fact.** As in the review above: TRUE where checkable. Toronto's eight-game losing run before the game: TRUE per the card's sources; it was priced only through form windows.
**6. What decided the game.** Columbus's 35 shots to 26 and 3-0 in the final 35 minutes.
**7. Knowable at the cutoff?** NOT_KNOWABLE.
**8. Process audit.** p = 0.532 has no direction. The contract defect means this row and L1 are scored as two results. The card itself treated them, correctly, as one exclusive, exhaustive event ("Neither contract is a two-goal puck line; their events are exclusive and exhaustive").
**9. Verdict.** **VARIANCE**: a no-direction number on a near-even game. The pick should not have been ranked.
**10. Cutoff-only counterfactual.** NOT_ASSESSABLE.
**11. Failure class and recurrence.** `VARIANCE`.
**12. Correction.** Already made in v29.2: a one-sided label, or the same contract twice, is refused at registration.
**13. Matched wins.** Columbus +0.5 "won" only as the complement of this row.
**14. Honesty checklist.** PASS.

**Joint section (P-700).** One shared driver, Columbus's late scoring, beat both the Toronto row and the Under. The card's grid priced them jointly and coherently. The ranker put the Under first and the Toronto row second, so the top two shared Toronto keeping the score down. Class note: `SHARED_DRIVER_TOP_TWO`, prose only.

<!-- END SETTLEMENT P-700 LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0004 revision-1 -->

<!-- BEGIN SETTLEMENT P-701 LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0005 revision-1 -->
### P-701 · Basketball/Australia NBL 2026-27 Round 10 — Sydney Kings @ Brisbane Bullets · 2026-11-22 AEST · revision-1

**Revision:** revision-1 · parent NONE · effective 2026-11-23T07:00:00+11:00 · affected ALL · changes NONE.
**Card state:** SETTLED.
- **Local key / native ID:** `LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0005` · `REQ:2026-11-22:NBL:BRI:SYD`.
- **Custody & timing:** `UNSEALED`: the drop was refused because FACTS AWAY `adjustment_basis` named `ANALYST_UNMEASURED_SCENARIO` as its source instead of a page. Scheduled tip 2026-11-22T06:00:00Z. Assessment `UNSEALED_DROP_REFUSED`; research only. Actual first play `NOT_VERIFIED` (game clock only).
- **Verified final (A):** **Brisbane Bullets 115-104 Sydney Kings**, regulation. By quarter BRI 30-24-33-28=115, SYD 26-26-23-29=104 (sum check 30+24+33+28=115, 26+26+23+29=104). Home margin +11, total 219.
- **Sources & captures:** nblfixtures.com game page `G0005_nblfixtures_r3.html`; Brisbane Bullets club recap `G0005_bullets_recap.html` (22 Nov). Two independent lineages.
- **Definition:** final score including overtime (registered). No overtime was played.
- **Expected vs final:** home margin centre −2.06 (SD 15.03), observed +11: z = +0.87. Total centre 187.86 (SD 18.12), observed 219: z = +1.72 (PIT 0.957).
- **Card-mean Brier / d:** 0.2386 / +0.0114.

| Rank | Exact original proposition | Original p | BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| R1 | Brisbane Bullets +4.5 | 0.56444 | UNAVAILABLE | **WIN** | A | yes (rank 1) | 11 + 4.5 > 0 |
| NOT_RANKED | Sydney Kings −4.5 | 0.43556 | UNAVAILABLE | **LOSS** | A | no | −11 − 4.5 < 0 |
| NOT_RANKED | Over 189.5 | 0.46386 | UNAVAILABLE | **WIN** | A | no | 219 > 189.5 |
| R2 | Under 189.5 | 0.53614 | UNAVAILABLE | **LOSS** | A | yes (rank 2) | 219 > 189.5 |

Ranks are the registered rule computed on this refused card, not registered ranks.

**R1–R12 retrospective:** The card used raw points for and against: 60% season, 25% L10 and 15% L5, crossed between the teams, plus the repository NBL home edge (+1.40). It then took 3.0 points off Sydney for Kendric Davis's absence as an "analyst scenario, NOT measured". It knew Velička was returning; it listed no other Brisbane return. The Bullets' recap says four players returned (Velička, McDaniel, Holt, Mackinnon), and Mackinnon top-scored with 23. Brisbane shot 21/49 from three, won the offensive boards 19-8 and had 33 assists. Sydney also lost Dellavedova and Maluach during the game. The side pick (+4.5) won by 15.5; the total went 29.5 over.

**Deep-review triggers (DEEPLOSS-v1):** top side Brisbane +4.5 (0.564, WIN) = rank 1 · top total Under 189.5 (0.536, LOSS) → one review.

#### Deep loss review · P-701 · TOP_TOTAL · Under 189.5 (`DLR-2026-11-22-017`)

**1. Exact frozen claim.** L2 TOTAL UNDER 189.5 points including overtime, p = 0.53614. Centre 187.856, SD 18.12 (the repository NBL residual floor). The centre included a −3.0 Sydney "scenario" for Davis's absence, disclosed as unmeasured. No reference p, no BASELINE_P, no ledger rows. Never sealed.
**2. Verified outcome.** 219 points (sum checks pass), regulation; over the line by 29.5 (1.63 SD) and over the centre by 31.1 (1.72 SD).
**3. Distribution check.** PIT 0.957. The card gave 219 or more about 4.5%. Row Brier 0.2874 against 0.25; log loss 0.768 against 0.693.
**4. Error decomposition.** The total was built from raw points per game, with no possessions or efficiency, from a season in which Brisbane averaged 94.4 and Sydney 98.6. Brisbane scored 115, 21 above its season mean. The Davis scenario moved the total 3 points toward the Under (centre 190.9 without it, P(Under) 0.470). It did not decide the row: the miss was 31 points.
**5. Research audit, fact by fact.** Davis OUT: TRUE (recap). Torrey Craig available, Velička returning: consistent with the recap. "No other Brisbane injury listed": the recap names three more returning players (McDaniel, Holt, Mackinnon); whether they were listed as returning before the game is NOT_ASSESSABLE from the captured pages. Records and raw game rows: consistent. Rest: six days off for both, consistent with both last playing 15 November. No market or exposure breach.
**6. What decided the game.** Brisbane's three-point shooting (21/49, 42.9%), offensive rebounding (19-8, 22 second-chance points to 12), 14 more shots than Sydney, and a full-strength Brisbane against a Sydney side that lost two more guards in the game.
**7. Knowable at the cutoff?** Brisbane at full strength: PARTLY (Velička's return was known; the others NOT_ASSESSABLE). Shooting and in-game injuries: NOT_KNOWABLE.
**8. Process audit.** No pace or efficiency model for a basketball total, the registered pattern class. The unmeasured Davis adjustment was priced into both rows; the card flagged it and refused to rank, and the registered ranker ranked the Under second anyway. The card also put the adjustment in FACTS with a non-page source, which is why the drop was refused.
**9. Verdict.** **MIXED.** A MODEL_LIMIT part: a raw-points total with an unmeasured downward adjustment. A VARIANCE part: 42.9% three-point shooting and in-game injuries. p = 0.536 had no real direction; the pick should not have been ranked.
**10. Cutoff-only counterfactual.** Declared scenario, diagnostic only: remove the unmeasured −3. The centre becomes 190.9, and P(Under 189.5) about 0.47: the card's lean flips to the Over.
**11. Failure class and recurrence.** `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`. Earlier reviews: P-687, P-688, P-693 (`ml deep-loss tally`). This is the 4th, an established pattern routed to prompt 8. Secondary: `UNFITTED_ANALYST_ADJUSTMENT` (prose only).
**12. Correction.** In the v30.0 list: possessions × opponent-adjusted efficiency for basketball totals, and no unmeasured adjustments in a priced row. Acceptance test: on held-out NBL games, Brier of the pace model's total below the raw-points total. No change under FREEZE-v1.
**13. Matched wins.** Brisbane +4.5 (rank 1) won by 15.5 from the same raw-points recipe. The unmeasured Davis adjustment helped that row, so the win is not evidence for the adjustment.
**14. Honesty checklist.** PASS.

<!-- END SETTLEMENT P-701 LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0005 revision-1 -->

<!-- BEGIN SETTLEMENT P-702 LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0006 revision-1 -->
### P-702 · Ice Hockey/Jastar Hokei Ligasy 2026-27 (shaiba 39216) — MHK Torpedo Ust-Kamenogorsk U20 @ MHK Aktobe U20 · 2026-11-22 AQTT · revision-1

**Revision:** revision-1 · parent NONE · effective 2026-11-23T07:00:00+11:00 · affected ALL · changes NONE.
**Card state:** SETTLED.
- **Local key / native ID:** `LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0006` · `JASTAR:39216`.
- **Custody & timing:** `UNSEALED`: the drop was refused because L1's two handicap lines were not equal and opposite, `availability_basis` used a non-vocabulary value, and L1's probabilities summed to 1.109. The request was registered at 18:57:39 AEDT for a 19:00 start, and research lasted 81 seconds (18:58:41–19:00:02). Assessment `UNSEALED_DROP_REFUSED`; research only.
- **Verified final (B):** **MHK Aktobe U20 6-3 MHK Torpedo U20**, regulation. By period 3:1, 0:1, 3:1 (sum check 3+0+3=6, 1+1+1=3). Goals 11:38, 13:07, 17:31, 19:07, 39:10, 41:11, 46:31, 50:14, 59:11 (empty net). Goalies Shpigun (AKT), Grokhotov (TOR). Margin +3, total 9.
- **Sources & captures:** shaiba.kz match report `G0006_shaiba_report.html` (posted 22 Nov 15:22 local); shaiba.kz match page's live feed at 5:3 in the 3rd period (same owner). Evidence B: one owner lineage. Betting widgets on the pages were not read.
- **Definition:** both handicap rows and the 7.5 total include overtime and the shootout (registered). No overtime. L1's rows are two different contracts ("Aktobe +4.5", "Torpedo −3.5"), each graded on its own.
- **Expected vs final:** margin centre Aktobe −2.06 (the card's own sign: Torpedo favoured by 2.06), observed Aktobe +3. Total centre 7.75, observed 9.
- **Card-mean Brier / d:** 0.1494 / +0.1006 (L1 is the mean of its two non-complementary rows).

| Rank | Exact original proposition | Original p | BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| R1 | MHK Aktobe U20 +4.5 | 0.814437 | UNAVAILABLE | **WIN** | B | yes (rank 1) | 3 + 4.5 > 0 |
| NOT_RANKED | MHK Torpedo U20 −3.5 | 0.294680 | UNAVAILABLE | **LOSS** | B | no | −3 − 3.5 < 0 |
| R2 | Over 7.5 | 0.512002 | UNAVAILABLE | **WIN** | B | yes (rank 2) | 9 > 7.5 |
| NOT_RANKED | Under 7.5 | 0.487998 | UNAVAILABLE | **LOSS** | B | no | 9 > 7.5 |

Ranks are the registered rule computed on this refused card. Rank 1 rests on a malformed label whose two rows are different contracts.

**R1–R12 retrospective:** The card made Torpedo favourites by about two goals, while giving Aktobe +4.5 81% and Torpedo −3.5 29%. Two different contracts were placed in one label, so the probabilities summed to 1.109 and could not be complementary. Aktobe won 6-3: up 3-1 after one period, pegged back to 3-3, then three unanswered goals, the last into an empty net. Both rows the card favoured won. That does not rescue a card researched in 81 seconds whose structure was invalid. No deep review is triggered: top side (Aktobe +4.5), top total (Over 7.5) and rank 1 all won. Matched-win check: the Aktobe +4.5 "win" is consistent with the card's own centre (Torpedo by about 2) only because +4.5 is a wide cushion. Its 0.81 came from that cushion, not from a read on Aktobe.

**Deep-review triggers (DEEPLOSS-v1):** top side Aktobe +4.5 (0.814, WIN) = rank 1 · top total Over 7.5 (0.512, WIN) → NONE_REQUIRED.

<!-- END SETTLEMENT P-702 LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0006 revision-1 -->

<!-- BEGIN SETTLEMENT P-703 LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0007 revision-1 -->
### P-703 · Cricket/Weber WBBL 12 Match 32 (CA:40652) — Melbourne Renegades Women @ Melbourne Stars Women · 2026-11-22 AEDT · revision-1

**Revision:** revision-1 · parent NONE · effective 2026-11-23T07:00:00+11:00 · affected ALL · changes NONE.
**Card state:** SETTLED.
- **Local key / native ID:** `LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0007` · `CA:40652`.
- **Custody & timing:** `SEALED` (server push `2026-11-22T08:12:42Z`, commit `ad9df53e1`; scheduled first ball 08:10:00Z, so sealed 2m42s after it; request registered 19:08:31 AEDT). Assessment `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`. Actual first ball `NOT_VERIFIED`. The sportsguff page lists the start as "22 Nov 2026, 1:55 PM" in an unstated time zone. If that were IST, the first ball would have been 19:25 AEDT, after the seal, but this is not an official capture and settles nothing. It counts for Track P only with a permitted first-ball capture later than 19:12:42 AEDT.
- **Verified final (B):** **Melbourne Stars Women 159/7 (20 overs; 57/0 after 6 overs)**, batting first after winning the toss. Phases 57/0 (1–6) + 78/3 (7–16) + 24/4 (17–20) = 159/7 (sum check 57+78+24=159; batters 150 + extras 9 = 159). Fall of wickets 1-80 (8.5 ov) … 7-159 (19.6 ov). Both contracts depend only on the Stars innings, which is complete in the capture; the match result is not needed.
- **Sources & captures:** sportsguff scorecard `G0007_sg_try.html` (captured during the Renegades chase); cricket.com.au match page `G0007_ca.html` renders client-side and has no score. Evidence B: one lineage.
- **Definition:** Stars innings at the 20-over cap, and Stars runs at the end of 6 overs (registered; no super over). The innings was not interrupted.
- **Expected vs final:** 20-over centre 145.69 (assumed SD 32), observed 159: z = +0.42 (PIT 0.661). 6-over centre 40.0 (assumed SD 12.5), observed 57: z = +1.36 (PIT 0.913).
- **Card-mean Brier / d:** 0.2931 / −0.0431.

| Rank | Exact original proposition | Original p | BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| NOT_RANKED | Stars 20-over total Over 148.5 | 0.465013 | UNAVAILABLE | **WIN** | B | no | 159 > 148.5 |
| R2 | Stars 20-over total Under 148.5 | 0.534987 | UNAVAILABLE | **LOSS** | B | yes (rank 2) | 159 > 148.5 |
| NOT_RANKED | Stars 6-over total Over 41.5 | 0.452242 | UNAVAILABLE | **WIN** | B | no | 57 > 41.5 |
| R1 | Stars 6-over total Under 41.5 | 0.547758 | UNAVAILABLE | **LOSS** | B | yes (rank 1) | 57 > 41.5 |

Ranks are the registered ranks from intake `2026-11-22-2`.

**R1–R12 retrospective:** The card weighted the Stars' last five innings (mean 137.8, a slump) at 55%, the Renegades' opponents' runs at 25% and the venue at 20%. For six overs it used four checked samples (mean 39) and assumed SDs of 32 and 12.5. It said itself that neither row qualified for a rank. Meg Lanning (44 off 29) and Amy Jones (57 off 43) put on 80 for the first wicket: 57/0 after the powerplay. After that the Stars added only 102 in 14 overs while losing 7 wickets (24/4 in the last four). The toss information came from a Reddit match thread; it was correct (the scorecard confirms the Stars chose to bat).

**Deep-review triggers (DEEPLOSS-v1):** top side none · top total Stars 20-over Under 148.5 (0.535, LOSS) · rank 1 Stars 6-over Under 41.5 (0.548, LOSS) → two reviews and a joint section.

#### Deep loss review · P-703 · RANK_1 · Stars 6-over total Under 41.5 (`DLR-2026-11-22-019`)

**1. Exact frozen claim.** L2 TOTAL UNDER 41.5, Stars runs at the end of 6 overs, p = 0.547758. Normal(40.0, 12.5): four checked six-over scores (34, 36, 50, 36; mean 39.0) plus a +1 venue/toss scenario. SD declared as an assumption. Sealed 2m42s after the scheduled first ball.
**2. Verified outcome.** 57/0 after 6 overs (phase sum checks pass); over the line by 15.5 (1.24 SD).
**3. Distribution check.** PIT 0.913. The card gave 57 or more about 9%. Row Brier 0.3000 against 0.25; log loss 0.794 against 0.693.
**4. Error decomposition.** Centre 40 against 57. The sample was four innings, one of them 50, and the fifth (2 November) was not verified. The SD was assumed, not measured. Using the card's own SD, the standard error of a four-innings mean is about 6 runs, half the assumed SD: the centre itself was very uncertain.
**5. Research audit, fact by fact.** The four six-over scores: as cited (not re-opened). Toss "Stars chose to bat": TRUE (scorecard), though sourced from a Reddit match thread, a live-match venue that carries outcome-exposure risk; the card recorded no outcome seen. Squad threats (Matthews, Molineux, Wareham): all bowled (Wareham 2/24, Matthews 2/20, Molineux 0/19). Rain: the innings was not interrupted.
**6. What decided the game.** An 80-run opening stand, 9.5 an over through the powerplay: Lanning 44 off 29, Jones 57 off 43, no wicket in the first six overs.
**7. Knowable at the cutoff?** NOT_KNOWABLE: the opening stand. PARTLY: the Stars' 2026 six-over scores already included a 50.
**8. Process audit.** A four-sample mean with an assumed SD, priced to three decimals. p = 0.548 has no direction, and the card refused to rank it; the registered ranker ranked it first. The 6-over and 20-over rows were priced as independent normals on one innings; the card disclosed this.
**9. Verdict.** **VARIANCE**, by the numbers: a PIT 0.91 outcome from one partnership, on a no-direction number. The pick should not have been ranked.
**10. Cutoff-only counterfactual.** NOT_ASSESSABLE: no phase model or measured six-over distribution exists for WBBL in the repository.
**11. Failure class and recurrence.** `VARIANCE`.
**12. Correction.** NO_CHANGE under FREEZE-v1. Coupled phase-to-innings simulation (`sr_kit.cricket_innings`) is in the v30.0 list.
**13. Matched wins.** None on this card.
**14. Honesty checklist.** PASS. The outcome-exposure risk of the Reddit source is recorded; no outcome was used.

#### Deep loss review · P-703 · TOP_TOTAL · Stars 20-over total Under 148.5 (`DLR-2026-11-22-018`)

**1. Exact frozen claim.** L1 TOTAL UNDER 148.5, Stars innings at the 20-over cap, p = 0.534987. Normal(145.69, 32), the SD assumed.
**2. Verified outcome.** 159/7 in 20 overs; over the line by 10.5 (0.33 SD).
**3. Distribution check.** PIT 0.661. The card gave 159 or more about 34%. Row Brier 0.2862; log loss 0.766 against 0.693.
**4. Error decomposition.** The 55% weight on a five-innings slump (137.8) pulled the centre below the Stars' own season mean (149.3). With the season mean in place of the slump, the centre is about 152.0 and P(Under) about 0.46. The overs after the powerplay were slow (102 in 14), so the miss came almost entirely from the first six overs.
**5. Research audit, fact by fact.** As in the review above. Season and last-five Stars totals: consistent with the scorecards cited.
**6. What decided the game.** The 57/0 powerplay, then 78/3 and 24/4.
**7. Knowable at the cutoff?** NOT_KNOWABLE.
**8. Process audit.** The 20-over row and the 6-over row are one innings. They were priced as independent normals and both put in the top two. Overweighting a five-game slump is a recency choice the card made without a measured basis.
**9. Verdict.** **VARIANCE**: a PIT 0.66 outcome. The 0.535 number had no direction.
**10. Cutoff-only counterfactual.** Declared scenario, diagnostic only: weight the season mean (149.3) instead of the last five. The centre is about 152.0 and P(Under 148.5) about 0.46: the lean flips.
**11. Failure class and recurrence.** `VARIANCE`.
**12. Correction.** NO_CHANGE under FREEZE-v1. Fitted, non-overlapping recency weights are in the v30.0 list.
**13. Matched wins.** None.
**14. Honesty checklist.** PASS.

**Joint section (P-703).** Both rows are the same innings: the 6-over score is the first part of the 20-over total. One opening stand beat both. The card priced them as independent marginal normals (disclosed) and the ranker put both in the top two. Class note: `PHASE_INCOHERENCE` / `SHARED_DRIVER_TOP_TWO`, recorded in prose only.

<!-- END SETTLEMENT P-703 LOCAL-20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0007 revision-1 -->

## Learning record (LEARN-v2)

| P-ID | Final | Regulation | Decision | Terminal source |
|---|---|---|---|---|
| P-697 | BSD 90-80 NZ | 90-80 | Regulation | basket.co.il GameId 26688 |
| P-698 | BEI 0-2 SHA (HT 0-1; corners 6) | 0-2 | 90 minutes | FotMob; Beijing Guoan FC report |
| P-699 | CLE 128-119 IND | 128-119 | Regulation | StatMuse; Fox Sports |
| P-700 | CBJ 4-3 TOR | 4-3 | Regulation | StatMuse; Fox Sports |
| P-701 | BRI 115-104 SYD | 115-104 | Regulation | nblfixtures; Brisbane Bullets recap |
| P-702 | AKT 6-3 TOR | 6-3 | Regulation | shaiba.kz report |
| P-703 | Stars 159/7 (57/0 after 6) | n/a | Stars innings complete | sportsguff scorecard |

These ONECHAT_V1 cards carried no LEARNLOG packet before the game, so none is built after the result (LEARNLOG-v1). They carry no v24.0 PICKS_V2 ledger rows (no RESULTS.csv/ACTUALS.csv) and no frozen model bundles (`NOT_APPLICABLE_NO_MODEL`).

## Mini-level diagnostics and review row

Preliminary only, seven games: Rank 1 3W/4L, Rank 2 2W/5L. Five of the seven rank-1 rows had p within 0.08 of 0.5; the other two were P-698 (0.72) and P-702 (0.81, on a malformed label). Six of the seven cards priced every row with `UNMEASURED` availability (G0006 used a non-vocabulary basis). Four of the seven cards were refused at sealing; three of those refusals were registration or format defects that v29.2 now catches at registration or in a check drop. MINI_SETTLEMENT review row: `NO_CHANGE` ([REVIEW_LOG_CANDIDATE.csv](REVIEW_LOG_CANDIDATE.csv)).

## SETTLEMENT_MANIFEST

[EVENT_FINALS.csv](EVENT_FINALS.csv), [MASTER_GRADES.csv](MASTER_GRADES.csv), [EFFECTIVE_SETTLEMENT_ROWS.csv](EFFECTIVE_SETTLEMENT_ROWS.csv), [CARD_TIMING.csv](CARD_TIMING.csv), [FROZEN_SOURCE.csv](FROZEN_SOURCE.csv), [INPUT_MANIFEST.csv](INPUT_MANIFEST.csv) with `inputs/cards/`, [LOCAL_ID_MAPPING.csv](LOCAL_ID_MAPPING.csv), [ALL_RECORD_MAPPING.csv](ALL_RECORD_MAPPING.csv), [REQUIREMENT_CLOSURE.csv](REQUIREMENT_CLOSURE.csv), [SOURCE_DISCOVERY_REGISTER.csv](SOURCE_DISCOVERY_REGISTER.csv), [SOURCE_SEARCH_ATTEMPTS.csv](SOURCE_SEARCH_ATTEMPTS.csv), [SOURCE_ACCESS_AUDIT.csv](SOURCE_ACCESS_AUDIT.csv), [CITED_URL_ACCESS_AUDIT_CHATGPT.csv](CITED_URL_ACCESS_AUDIT_CHATGPT.csv), [UNRESOLVED_POST_IMPORT.csv](UNRESOLVED_POST_IMPORT.csv), [SETTLEMENT_CHECKS.csv](SETTLEMENT_CHECKS.csv), [AUDIT_REPORT.md](AUDIT_REPORT.md), [CANONICAL_IMPORT_REPORT.md](CANONICAL_IMPORT_REPORT.md), `research/one_chat/outcomes/2026-11-22-2/OUTCOMES.csv` (the three sealed cards) and `research/one_chat/intake/2026-11-22-2/` (intake from every sealed card, superseding 2026-11-22-1 as the complete census).
