# RESEARCH-DRAFT-09 — Urawa Red Diamonds vs Cerezo Osaka — v24.15

**Custody:** `CHAT_LOCAL_RESEARCH_ONLY / UNSETTLED / NOT_ISSUED / NO_OFFICIAL_CARD / NO_EV2_EVENT_KEY / NO_PRIMARY_P_CARD`.
**Correction parent:** `LOCAL-INTAKE-09-IDENTITY-CONFLICT`: this is the correctly specified new fixture Urawa vs Cerezo. Do not rewrite the older Urawa-vs-Kashima request; link it as superseded by corrected user identity, **not** as an official issued-card revision.
**Research completion clock (UTC):** `2026-11-11T10:27:41+00:00`; local AEDT `2026-11-11T21:27:41+11:00`. Scheduled cutoff `2026-11-11T21:30:00+11:00`; saved-before-scheduled-kickoff=True. Actual first play `NOT_VERIFIED`. **No pre-start freeze or GitHub issuance occurred**, even if saved before scheduled kickoff.
**Repository:** read-only `main` `4d8bd1771d20974bcbfc7c694a009cd44e95a693`, v24.15 (MDS-2026.11.11-v24.15, P-2026.11.11-v24.13, EXT-v3). Required core/sport sources read through connected GitHub; no local kit/official writer execution or external event manifest. Formal model registry had header only.

## A1. Identity, exact contracts, match state

- Official event: J.League YBC Levain Cup 2026/27, prime round quarter-final **first leg**, Urawa Red Diamonds (HOME) v Cerezo Osaka (AWAY), Wednesday 11 Nov 2026 19:30 JST / 10:30 UTC / 21:30 AEDT, Saitama Stadium 2002, Saitama, Japan.
- Official fixture: https://www.jleague.jp/match/leaguecup/2026/111102/ ; Urawa announcement https://www.urawa-reds.co.jp/topteamtopics/9030127.html ; Cerezo preview https://www.cerezo.jp/news/2026-1110-1830/ .
- Contracts: first-half goals Over/Under 0.5 (45 min + added time); full-time goals Over/Under 2.5 (90 min + added time); full-time corners Over/Under 10.5 (90 min + added time; J.League provider match CK definition needed for official settlement).
- J.League Cup rules: quarterfinal first leg ends drawn if level at FT; extra time/penalties apply after second leg only if needed, not in first leg. https://www.jleague.jp/en/outline/leaguecup/ .
- Pre-match fixture page and match-day starters were consulted; **no live score, play-by-play or final result was consulted**, so there is no outcome settlement here. Operator-specific corners definition remains `UNKNOWN_DEFINITION` beyond the named official CK source.

## A2. Source-backed recent form, corners taken, H2H

Official team records: https://www.jleague.jp/en/club/urawa/ and https://www.jleague.jp/en/club/cosaka/. Published club CK is **corners won by that club**, NOT combined corners per match. All rows are dated prior to event; mixed J1, League Cup and Emperor's Cup (competition regimes distinguishable). L5/L10/L15/L20 are overlapping windows, not independent likelihood observations. 19 source-listed rows per team are available (20th not silently fabricated).

| Team | Window | True n | W-D-L | For/game | Against/game | Combined goals/game | CK taken/game |
|---|---|---:|---|---:|---:|---:|---:|
| Urawa | L5 | 5 | 3-1-1 | 1.60 | 1.80 | 3.40 | 6.00 |
| Urawa | L10 | 10 | 7-1-2 | 1.90 | 1.60 | 3.50 | 6.10 |
| Urawa | L15 | 15 | 11-1-3 | 2.00 | 1.53 | 3.53 | 5.73 |
| Urawa | L20 | 19 | 12-1-6 | 2.00 | 1.79 | 3.79 | 5.26 |
| Cerezo | L5 | 5 | 2-2-1 | 2.00 | 2.00 | 4.00 | 3.40 |
| Cerezo | L10 | 10 | 5-3-2 | 1.90 | 1.70 | 3.60 | 3.90 |
| Cerezo | L15 | 15 | 6-5-4 | 1.53 | 1.67 | 3.20 | 4.87 |
| Cerezo | L20 | 19 | 9-5-5 | 1.53 | 1.58 | 3.10 | 4.63 |

Historical head-to-head, last 5 per J.League pre-match preview (older rosters and contexts): Cerezo 2–0 Urawa (16 Jul 2023); Cerezo 2–1 Urawa (15 Jun 2024); Urawa 0–1 Cerezo (5 Oct 2024); Cerezo 1–1 Urawa (28 Mar 2025); Urawa 0–0 Cerezo (28 May 2025). FT totals 2,3,1,2,0; **mean 1.6**; four of five Under 2.5. First-half and corner splits for these are `NOT_VERIFIED`.

Source-row extraction (team CK own only):

| Team | Date JST | Opponent | Competition | Score for–against | Team CK |
|---|---|---|---|---|---:|
| Urawa | 2026-11-08 | Kobe | J1 | 2–2 | 5 |
| Urawa | 2026-10-31 | Kashiwa | J1 | 0–4 | 6 |
| Urawa | 2026-10-28 | Nagoya | YLC | 2–1 | 6 |
| Urawa | 2026-10-25 | Nagasaki | J1 | 1–0 | 7 |
| Urawa | 2026-10-21 | Chiba | J1 | 3–2 | 6 |
| Urawa | 2026-10-17 | Mito | J1 | 1–0 | 13 |
| Urawa | 2026-10-14 | Yokohama FC | YLC | 4–0 | 6 |
| Urawa | 2026-10-10 | FC Tokyo | J1 | 0–3 | 3 |
| Urawa | 2026-10-07 | Omiya | Emperor | 3–2 | 6 |
| Urawa | 2026-09-29 | Toyama | YLC | 3–2 | 3 |
| Urawa | 2026-09-19 | Tokyo Verdy | J1 | 3–1 | 8 |
| Urawa | 2026-09-13 | Okayama | J1 | 1–2 | 4 |
| Urawa | 2026-09-06 | Kashima | J1 | 1–0 | 8 |
| Urawa | 2026-09-02 | Fukuoka | J1 | 3–2 | 1 |
| Urawa | 2026-08-29 | Yokohama FM | J1 | 3–2 | 4 |
| Urawa | 2026-08-26 | Yamanashi Gakuin | Emperor | 3–0 | 4 |
| Urawa | 2026-08-23 | Machida | J1 | 1–3 | 3 |
| Urawa | 2026-08-15 | Hiroshima | J1 | 1–4 | 1 |
| Urawa | 2026-08-07 | G Osaka | J1 | 3–4 | 6 |
| Cerezo | 2026-11-08 | G Osaka | J1 | 3–2 | 6 |
| Cerezo | 2026-10-31 | Kashima | J1 | 1–4 | 2 |
| Cerezo | 2026-10-28 | Mito | YLC | 3–1 | 3 |
| Cerezo | 2026-10-25 | Chiba | J1 | 2–2 | 5 |
| Cerezo | 2026-10-21 | Nagoya | J1 | 1–1 | 1 |
| Cerezo | 2026-10-17 | Kawasaki | J1 | 2–4 | 3 |
| Cerezo | 2026-10-14 | Tottori | YLC | 3–2 | 3 |
| Cerezo | 2026-10-10 | Yokohama FM | J1 | 0–0 | 5 |
| Cerezo | 2026-10-07 | Kagoshima | Emperor | 2–0 | 4 |
| Cerezo | 2026-09-29 | Fujieda | YLC | 2–1 | 7 |
| Cerezo | 2026-09-19 | Nagasaki | J1 | 1–1 | 4 |
| Cerezo | 2026-09-12 | Hiroshima | J1 | 1–6 | 4 |
| Cerezo | 2026-09-06 | Tokyo Verdy | J1 | 0–0 | 10 |
| Cerezo | 2026-09-02 | Kashiwa | J1 | 2–0 | 7 |
| Cerezo | 2026-08-29 | Kobe | J1 | 0–1 | 9 |
| Cerezo | 2026-08-26 | Gifu | Emperor | 3–1 | 1 |
| Cerezo | 2026-08-22 | Shimizu | J1 | 1–0 | 7 |
| Cerezo | 2026-08-15 | Fukuoka | J1 | 0–3 | 2 |
| Cerezo | 2026-08-08 | Okayama | J1 | 2–1 | 5 |

## A3. Availability, exact-game XI and bench

The following starters and bench were explicitly reported on 11 Nov 2026 by Sakanowa and Uragi (two sport-news outlets, but collector/feed independence not independently verified). Match-day selected player lists; no claim of independent club-team-sheet verification:

- **Urawa starting XI:** Eisuke Arai, Yuta Miyamoto, Danilo Boza, Kota Kudo, Yoichi Naganuma, Tatsuki Seko, Renji Hidano, Hayate Ueki, Jumpei Hayakawa, Harumi Minamino, Ado Onaiwu.
- **Urawa bench:** Shusaku Nishikawa, Kenta Nemoto, Eiichi Katayama, Takuro Kaneko, Matheus Savio, Samuel Gustafson, Ryoma Watanabe, Kaito Yasui, Hiiro Komori.
- **Cerezo starting XI:** Koto Abe, Javi Hernandez, Dion Cools, Travis Takahashi, Takumi Nakamura, Shunta Tanaka, Reiya Sakata, Kosei Okazawa, Yota Komi, Lucas Fernandes, Tomoaki Uejo.
- **Cerezo bench (eight listed):** Ken Ishibow, Rikito Inoue, Kyohei Noborizato, Hayato Okuda, Shinnosuke Hatanaka, Teppei Shiojiri, Solomon Sakuragawa, Thiago Andrade.
- Key rotation: Urawa goalkeeper Nishikawa and attackers Matheus Savio, Ryoma Watanabe, Hiiro Komori on bench; Cerezo Solomon Sakuragawa and Thiago Andrade on bench. Bench listing is not a guarantee of minutes.
- Urawa **Shuta Sasa** absent on Japan U-21 international duty; Cerezo **Yumeki Yokoyama** likewise absent (official J.League preview); absence for these individuals is not incorrectly labelled a physical injury.
- Named sources: https://sakanowa.jp/topics/114463 and https://uragi.com/?p=55530 ; official preview https://www.jleague.jp/match/leaguecup/2026/111102/ . Unknown additional injuries `NOT_VERIFIED`, never 'none'.

## A4. Coaching, tactics, schedule, external conditions

- Urawa coach **Cho Kwi Jae**, Cerezo **Pablo Machín**; club/league roster sources.
- Urawa previously drew 2–2 at Vissel Kobe on 8 Nov; Cerezo previously won 3–2 at Gamba Osaka same day. Both have two clear rest days from Sunday to Wednesday evening and rotated starters. Cerezo's official preview describes recent 4-4-2 press, transitional defensive vulnerabilities, and the two-leg importance.
- Urawa's two preceding match results: 2–2 Kobe; 0–4 Kashiwa, then 2–1 Nagoya in Cup. Cerezo: 3–2 Gamba; 1–4 Kashima, then 3–1 Mito in Cup. Short-run scoring volatility wide; not a certified boost to attack.
- Weather: Saitama Stadium forecasts clear/dry, approximately 10–12 °C at kickoff, ~0 mm precipitation and light wind. Sources https://www.mapion.co.jp/weather/spot/L1041850/ and https://www.sototenki.jp/spot/9987/3hours . Forecast timestamps need separate observation clocks for reproducibility. No measured scoring adjustment.
- Referee Junpei Iida reported in Uragi match-team-sheet page; independent official crew publication `NOT_VERIFIED`.

## A5. Numerical methods and research boundary

**Official v24.15 `REFERENCE tier/run`: NOT_RUN. SR-KIT-v24.15: NOT_RUN.** No repository append, no `PICKS_V2`, no frozen pre-exposure reference, no qualifying model promotion, no source-hashed official forecast. All `p_card=NOT_ESTIMATED`.

Transparent *non-primary* Poisson sensitivity calculations in Wolfram (exact PDF/CDF, no Monte Carlo). Total-goal centre 2.55 is a declared illustrative low-to-medium tempo/rotation scenario, not a fitted exact 2026/27 J.League Cup rate; share of first-half goals 0.408 is borrowed only as an unvalidated proxy from the v24.15 `Soccer/J1 League` development kit row (same sport, different competition). `J1` 2025 coverage n=136, not a calibrated cup/season input. Corners proxy 10.0 = Urawa L10 corners taken 6.1 + Cerezo L10 corners taken 3.9, **not a matched sample of full-game corner totals**. Poisson count overdispersion unverified.

Mathematics: P(1H Over0.5)=1-exp(-2.55*0.408); P(FT Over2.5)=1-exp(-2.55)*(1+2.55+2.55^2/2); P(corners Under10.5)=PoissonCDF(10,lambda=10.0). Calculations executed in Wolfram Language (tool receipt in research conversation; no file-generated kit receipt).

| Exact contract direction | Nonprimary diagnostic | Formal p_card | Disposition |
|---|---:|---|---|
| 1H Over 0.5 | 64.67% | NOT_ESTIMATED | UNCALIBRATED_QUALITATIVE |
| 1H Under 0.5 | 35.33% | NOT_ESTIMATED | UNCALIBRATED_QUALITATIVE |
| FT Over 2.5 | 46.89% | NOT_ESTIMATED | UNCALIBRATED_QUALITATIVE |
| FT Under 2.5 | 53.11% | NOT_ESTIMATED | UNCALIBRATED_QUALITATIVE |
| Corners Over 10.5 | 41.70% | NOT_ESTIMATED | UNPRICED_IN_FORMAL_PICKS |
| Corners Under 10.5 | 58.30% | NOT_ESTIMATED | UNPRICED_IN_FORMAL_PICKS |

Sensitivity scenarios: expected full goals 2.30 / 2.55 / 2.90 -> 1H Over 0.5 60.9% / 64.7% / 69.4%, FT Over2.5 40.4% / 46.9% / 55.4%. Corners assumed mean 9.4 / 10.0 / 10.6 -> Under10.5 65.8% / 58.3% / 50.8%. This sensitivity demonstrates no robust ≥65% *qualified* ranked side.

## A6. Contract-specific assessment and rank

- **1H Over 0.5:** best conditional low-confidence lean. Recent combined 90-minute results are lively, with multiple goals on both sides, but the first-half proportion is a J1 proxy; rotations, prior low H2H and first-leg management could produce 0–0 HT. Full-season first-half scoring events were not reconstructed, so this row is not independently verified 1H-calibrated.
- **1H Under 0.5:** historical H2H low goals and rotated attackers support early caution, but both teams have shown defensive concessions against recent opposition. Not selected.
- **FT Under 2.5:** four of five historical H2H and cup first-leg strategy support; against that, both L10 total goal averages exceeded 3.5. Proxy near 53%, not decisive.
- **FT Over 2.5:** recent open games and Cerezo defensive volatility support; older direct games, first leg and rotation oppose. Proxy near 47%.
- **Corners Under 10.5:** official team CK per L10 averages total 10.0, central 58% diagnostic, but this adds two independently collected individual-team outcomes from different fixtures; exact fixture combined/opponent-adjusted CK, officiating and game-state changes not modelled. No formal price.
- **Corners Over 10.5:** Urawa presses, takes ~6 CK per game and recently hit 13 vs Mito; the Cerezo direct count is lower. No grounded expectation ≥11.
- No opponent-specific form adjustment or effect-table coefficient was executed, no player impact invented. All three two-way propositions unissued, ranked advisory only.

## A7. Recommendation, validation and timing

**Single conditional preference:** `FIRST_HALF_OVER_0.5_GOALS`, LOW-MODERATE_UNCALIBRATED, illustrative 64.7% under stated scenario. **Formal gate:** `NO_STRONG_PICK / ABSTAIN`, because 65% is not met for primary and exact first-half model and corners provider distribution are unqualified. The user did NOT request settling; no scores, halftime result or total corners for the fixture consulted.
**Timing:** saved at `{issued_aedt}`. Scheduled start 21:30 AEDT. Actual first play `NOT_VERIFIED` and **no formal original pre-start primary freeze**. Record is `RESEARCH_DRAFT / NOT_ISSUED`, whether saved before/after 21:30. No claims of a prospective issued card.

## A8. Source, publication/availability/access ledger

| Source | Scope | Provenance limitation |
|---|---|---|
| https://www.jleague.jp/en/match/leaguecup/2026/111102/ | Exact official fixture, preview, older H2H, notable absences, coaches | Original J.League content; no full squad confirmation on match page |
| https://www.urawa-reds.co.jp/topteamtopics/9030127.html | Club fixture event time (published 9 Nov) | Club source, separate publisher from league but likely same match manifest |
| https://www.cerezo.jp/news/2026-1110-1830/ | Club tactics, 8 Nov match, rest, coach first-leg comments (published 10 Nov) | Single club original, primary for club remarks only |
| https://sakanowa.jp/topics/114463 | Both starting XI and bench (article date 11 Nov) | Article gives exact lists, source feed's original league collector not verified |
| https://uragi.com/?p=55530 | Alternative starters and referee (11 Nov) | May share J.League collector with Sakanowa; not independent sporting proof |
| https://www.jleague.jp/en/club/urawa/ | 19 dated Urawa results with goals and team CK | J.League field owner, recent vs different opponents; as-of 10 Nov page update |
| https://www.jleague.jp/en/club/cosaka/ | 19 dated Cerezo results with goals and team CK | Same field-owner collector, distinct club rows; as-of 10 Nov page update |
| https://www.jleague.jp/en/outline/leaguecup/ | First-leg regulation and knockout format | Official rules page |
| https://www.mapion.co.jp/weather/spot/L1041850/ | Stadium hourly forecasts, local 11 Nov | Predicted not measured in-game conditions |
| https://www.sototenki.jp/spot/9987/3hours | Alternative local weather timing | Same weather upstream possible, not assured independent |

**Access:** J.League / club sites available through read-only web, and sport official route in repository used where available. Exact page `ml source-audit --reader ChatGPT-User` **NOT_RUN**; the current access snapshot was not re-audited live within this chat. No pages with bookmaker prices/predictions/fantasy claims were opened for sporting inputs, and no market probabilities were incorporated. The links above are cited research records, not fully preserved raw bytes. Actual per-URL independently instrumented retrieval clocks `NOT_AVAILABLE`; publication time `UNKNOWN` where article omits it.

## A9. Completion matrix, unresolved work, integrity

| Stage | Status |
|---|---|
| Correct event identity/venue/cup rules | OFFICIAL_CHECKED |
| Both squads XI and bench | REPORTED_MATCHDAY / direct official team-sheet unresolved |
| Special absences | VERIFIED_PREVIEW / other injuries unknown |
| H2H 5 games | VERIFIED_MATCH_RESULT / no halftime and corners split |
| L5/L10/L15/L20 | SOURCE_VERIFIED_ROWS; L20 true n=19/19, mixed competition |
| Home/away and league form | PARTIAL, team-match-split available in row list but not opponent-adjusted |
| First-half goals history | INCOMPLETE, half-specific actual performance unavailable |
| Exact combined corners history | INCOMPLETE, only team CK per match, no opposing CK reconciliation |
| Conditions/weather | FORECAST_CHECKED; officials independence incomplete |
| Reference/score grid/kit receipts | NOT_RUN / NOT_VERIFIED |
| Unpriced/unsupported contracts | ALL SIX FORMAL PRIMARY ROWS NOT_ESTIMATED; corners explicitly unpriced |
| Pre-start official issuance/lease and ledger | NOT_PERFORMED; GitHub READ_ONLY |
| Results check and settlement | NOT_PERFORMED; no outcome grading |

**Receipt:** `RESEARCH-DRAFT-09 / NO_FORECAST_PRIMARY / UNSETTLED / PRIMARY_P_CARD=NOT_ESTIMATED / NO_CANONICAL_ID / NO_OFFICIAL_KEY / GITHUB_WRITES=ZERO`.
