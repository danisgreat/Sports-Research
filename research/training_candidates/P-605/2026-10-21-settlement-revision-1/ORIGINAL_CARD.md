<!-- BEGIN CANONICAL RESEARCH P-605 -->
## P-605 — ICE HOCKEY / Finnish Liiga · HPK vs Ilves · 2026-10-16
Import: 2026-10-21T01:07:13+11:00; prompt 4 NEW_CANONICAL_EVENT. Local event key `LOCAL-2026101679B3FBCC8D-G0005` → canonical **P-605**; native identity Liiga game 2701384. Source mini `2026101679B3FBCC8D`, frozen source SHA-256 `b7478342e7ecba6861d9d79e4fc98b1dcd686356260f8b21911989847115ad7e` (313,155 bytes). Card core SHA-256 `820e287fd0beb136ad7148a3b5d908745509a07c15425c70e4f32b14fc8cb24c` (24,186 bytes) = the exact bytes between the local BEGIN/END CARD marker lines (source offsets 147629–171815); markers and headings outside them remain in the preserved source. Original method, probabilities, ranks, statuses, timing and gaps are literal; any NOT_ASSIGNED / PENDING wording inside the core is historical. Import is not a forecast timestamp and confers no certification.

## Card · LOCAL-2026101679B3FBCC8D-G0005 · ICE HOCKEY / Finnish Liiga · HPK vs Ilves · 2026-10-16
- **Local identity:** `LOCAL-2026101679B3FBCC8D-G0005`; native Liiga game ID `2701384`; canonical P-ID `NOT_ASSIGNED / PROMPT_4_IMPORT`; no canonical assignment/reservation. Duplicate scan in accessible 4-card cumulative mini found none. Owner desktop and unimported independent mini scopes incompletely enumerated.
- **GitHub authority:** `PUBLISHED_MAIN_PINNED` HEAD `27e013c35477dbffb7b7699b269a0b978fb69b7f` (updated relative to historical header); `MDS/P-2026.10.16-v20.0`, `CURRENT_RULES CR-R7`, `SCV-v11`, `SEL-2026.10.12-v3`, `PRIMARY-v3.3`, `CYCLE-v1`, `MINI-v1`, `EXH-v1`. Published `main` READ-ONLY; no checkout claiming code run.
- **Fixture:** HPK (Hämeenlinnan Pallokerho) home vs Tampereen Ilves, Liiga 2026-27 regular season, Pohjantähti Areena (Hämeenlinna), Finnish local 16 Oct 2026 18:30 UTC+03; UTC 2026-10-16 15:30Z; AEDT 2026-10-17 02:30+11. Native event ID 2701384; references `https://liiga.fi/en/game/2027/2701384/events` and both clubs.
- **Timing:** requested scheduled 02:30 AEDT; research completion/file assembled `2026-10-17T02:40:32+11:00`, after scheduled start. Actual first puck drop not verified, and no live score, shots or actual event outcome used to choose inputs; **POST_SCHEDULED_START_RESEARCH / NO_VERIFIED_PRE_START_ISSUE**; `CLEAN_PRE_START_INPUTS` not certified because first-publication capture time for lineup and historical source snapshots was not verified. Not a graded prospective forecast; issue_at issuance NOT_GRANTED, cutoff for eligible pre-start data scheduled 2026-10-17T02:30+11:00 (all historical games dated before that).
- **Model disposition:** `RESEARCH_ONLY_NO_MODEL / UNCALIBRATED_ANALYST_SCENARIO / NOT_PRIMARY` for all four candidate directions; no fitted primary `p_card`, original rank or execution manifest success invented. Settlement NOT_PERFORMED; GitHub writes NO. Stable local candidate key is a draft pointer, not an allocated canonical or authorised issued ID.

### A1. Identity, rule and endpoint interpretation
2026-27 Liiga regular season: 3×20 minute regulation; ties proceed to overtime and potentially shootout. Full-match moneyline **assumed** to include OT/SO, while a regulation 3-way result is a different contract. HPK +1.5 is assumed to use the officially recorded full-match goal margin including the single OT/SO deciding goal. Over/Under 5.5 assumes officially recorded full-match goals including the OT/SO decider, and a shootout contributes one official winning goal. **Operator-specific wording was not supplied and remains UNKNOWN_DEFINITION.** In the central idealised model, a tied 0, 2 or 4 regulation-goal game becomes 1, 3 or 5 full-match goals after a decider; consequently the 5.5 half-line classification is invariant, but other thresholds need separate handling. A 60-minute-only total and +1.5 are separately retained as sensitivity readings; no change at these half-lines under this single-goal-decider simplifying assumption. No push at integer-count half-lines. Return/void/postponement provisions unknown.

### A2. Original supplied contracts and independent probability comparison
**Verbatim owner intake:** “Upcoming game — ICE HOCKEY; Competition details: <Hpk vs Ilves, Finland SM Liiga>; Scheduled start: <17 October 2026, 2:30 AM AEDT> (can be delayed, so don’t stop/delay/alter research due to this); Active local mini: <current active running/mini log>; Supplied contracts: <Hpk +1.5>, <Ilves ML>, <Combined Total Goals: Over/Under 5.5 Goals>; Research constraints: <none apart from the specified requirements and rules; only-confirmed issuance if expressly required>; need probability issue and expected value based on research and/or GitHub ML/RL.”

**All numerical rows below are scenario calculations and are NOT primary/p_card or calibrated.**
| Analyst probability order | Supplied proposition | Endpoint assumption | W | L | V | p_analyst=W/(W+L) | Estimated fair probability (not odds) |
|---|---|---|---:|---:|---:|---:|---:|
| 1 | Ilves ML | Full match incl OT/SO, assumed | 0.660 | 0.340 | 0 | 66.03% | 66.03% |
| 2 | Combined total Under 5.5 goals | Full match incl OT/SO, assumed | 0.637 | 0.363 | 0 | 63.68% | 63.68% |
| 3 | HPK +1.5 goals | Full match incl OT/SO, assumed | 0.620 | 0.380 | 0 | 61.96% | 61.96% |
| 4 | Combined total Over 5.5 goals | Full match incl OT/SO, assumed | 0.363 | 0.637 | 0 | 36.32% | 36.32% |
60-minute three-way diagnostic: HPK regulation win 26.18%; regulation draw 17.31%; Ilves regulation win 56.50%. Ilves full-match ML uses a **hypothetical** 55% share of regulation draws, never a fitted OT advantage.
**Financial EV:** NOT_ESTIMATED; supplied contracts have no defined payout or price. This research is market-blind. “Expected value” below refers to sporting quantities, not financial return.
**Selection checks (diagnostic only):** provisional 0.62 Rank-1 floor: Ilves ML 66.03% >62%; best non-complementary supplied alternative Under 5.5 63.68%, gap 0.023 <0.04, thus provisional gate **RANK1_UNSTABLE** even on these unfitted numbers. No primary selection pass. Unconfirmed goalie materially affects a fragile total; do not promote it to Rank 1. Selection ceiling 90% not binding. Unsupported named primary runtime prevents certified numeric ranking, shadows, Δ-vs-baseline and η loss updates.

### A3. Web-sourced form and source custody (L5/L10/L15/L20)
Official Liiga current-season schedule and club listings, league prior-season playoffs and independent indexed schedules were searched. Actual opened/extracted references:
- official: https://liiga.fi/en/game/2027/2701384/events
- hpkclub: https://hpk.fi/biorex-otteluennakko-hpk-ilves-16-10-vieraita-tampereelta/
- ilvesclub: https://www.ilves.com/otteluennakko/ilves-matkustaa-perjantaina-hpkn-vieraaksi/
- lineups: https://www.jatkoaika.com/LIIGA/Kokoonpanot/HPK-Ilves/62530
- hpk_curr: https://liiga.fi/en/schedule/?joukkue=hpk&kausi=2026-2027&sarja=runkosarja
- hpk2: https://omnihockey.com/teams/liiga-hpk/schedule
- ilv_curr: https://www.ilves.com/ottelut-2026-27/
- ilv2: https://omnihockey.com/teams/liiga-ilves/schedule
- hpk_old: https://liiga.fi/fi/ohjelma/?joukkue=hpk&kausi=2025-2026&sarja=playoffs
- ilv_old: https://liiga.fi/fi/ohjelma/?joukkue=ilves&kausi=2025-2026&sarja=playoffs
- hpk_old2: https://www.eliteprospects.com/team/610/hpk/scores/2025-2026
- ilv_old2: https://www.ilves.com/ottelut-2025-26/
- hpk15: https://omnihockey.com/teams/liiga-saipa/schedule
- hpk_oct10: https://liiga.fi/fi/peli/2027/2701372/tilastot
- hpk_oct09: https://liiga.fi/fi/peli/2027/2701371/tilastot
- official_template: https://github.com/danisgreat/Sports-Research/blob/27e013c35477dbffb7b7699b269a0b978fb69b7f/LEARNING_PIPELINE_PROTOCOL.md

**Regulation goals, correctly removing OT/SO deciding goals; L15 and L20 include previous-season PLAYOFFS and are diagnostic only, not identically weighted with current league form.**
| Window | HPK regulation GF–GA | Ilves regulation GF–GA | Last-season playoff games |
|---|---|---|---|
| L5 (n=5/5) | 11–9 | 14–13 | HPK 0, Ilves 0 |
| L10 (n=10/10) | 19–27 | 32–19 | HPK 0, Ilves 0 |
| L15 (n=15/15) | 29–41 | 41–36 | HPK 2, Ilves 3 |
| L20 (n=20/20) | 40–49 | 57–49 | HPK 7, Ilves 8 |

Current-season exact-population rates: HPK n=13 regulation 26 GF, 37 GA ⇒ 2.000 GF/g and 2.846 GA/g; Ilves n=12 regulation 35 GF, 24 GA ⇒ 2.917 GF/g and 2.000 GA/g. Team/league adjustments not fitted. HPK last 5 11/9 regulation includes latest SaiPa loss; Ilves last 5 14/13 includes recent 1-5 vs Lukko and 3-0 vs Jokerit. They are overlapping diagnostics, not independent observations or p shifts.

**HPK — 20 most recent reconstructed Liiga games, newest first (last-season playoffs included):**

| Date | Season/stage | Opponent | Home/away | Final GF–GA | 60-min GF–GA | Deciding endpoint |
|---|---|---|---|---|---|---|
| 2026-10-15 | 2026-27 REGULAR | SaiPa | away | 1–2 | 1–2 | REG |
| 2026-10-10 | 2026-27 REGULAR | KooKoo | home | 5–3 | 5–3 | REG |
| 2026-10-09 | 2026-27 REGULAR | Ässät | away | 3–2 | 2–2 | SO |
| 2026-10-03 | 2026-27 REGULAR | Kärpät | home | 2–1 | 1–1 | OT |
| 2026-10-02 | 2026-27 REGULAR | JYP | home | 2–1 | 2–1 | REG |
| 2026-09-29 | 2026-27 REGULAR | Jokerit | away | 0–3 | 0–3 | REG |
| 2026-09-26 | 2026-27 REGULAR | Ässät | home | 5–4 | 4–4 | OT |
| 2026-09-22 | 2026-27 REGULAR | Lukko | home | 1–3 | 1–3 | REG |
| 2026-09-19 | 2026-27 REGULAR | TPS | home | 3–1 | 3–1 | REG |
| 2026-09-15 | 2026-27 REGULAR | KalPa | away | 0–7 | 0–7 | REG |
| 2026-09-08 | 2026-27 REGULAR | Ilves | home | 0–4 | 0–4 | REG |
| 2026-09-04 | 2026-27 REGULAR | HIFK | away | 3–5 | 3–5 | REG |
| 2026-09-01 | 2026-27 REGULAR | Jukurit | away | 4–1 | 4–1 | REG |
| 2026-04-07 | 2025-26 PLAYOFF | Tappara | away | 0–1 | 0–1 | REG |
| 2026-04-04 | 2025-26 PLAYOFF | Tappara | home | 3–4 | 3–3 | OT |
| 2026-04-02 | 2025-26 PLAYOFF | Tappara | away | 1–3 | 1–3 | REG |
| 2026-03-30 | 2025-26 PLAYOFF | Tappara | home | 2–1 | 2–1 | REG |
| 2026-03-28 | 2025-26 PLAYOFF | Tappara | away | 1–2 | 1–2 | REG |
| 2026-03-24 | 2025-26 PLAYOFF | Lukko | home | 4–1 | 4–1 | REG |
| 2026-03-23 | 2025-26 PLAYOFF | Lukko | away | 3–1 | 3–1 | REG |

**ILVES — 20 most recent reconstructed Liiga games, newest first (last-season playoffs included):**

| Date | Season/stage | Opponent | Home/away | Final GF–GA | 60-min GF–GA | Deciding endpoint |
|---|---|---|---|---|---|---|
| 2026-10-10 | 2026-27 REGULAR | Jokerit | away | 3–0 | 3–0 | REG |
| 2026-10-09 | 2026-27 REGULAR | Lukko | home | 1–5 | 1–5 | REG |
| 2026-10-07 | 2026-27 REGULAR | Sport | away | 1–2 | 1–2 | REG |
| 2026-10-03 | 2026-27 REGULAR | K-Espoo | home | 6–4 | 6–4 | REG |
| 2026-09-29 | 2026-27 REGULAR | Jukurit | home | 3–2 | 3–2 | REG |
| 2026-09-27 | 2026-27 REGULAR | TPS | home | 3–2 | 3–2 | REG |
| 2026-09-25 | 2026-27 REGULAR | KooKoo | home | 6–0 | 6–0 | REG |
| 2026-09-18 | 2026-27 REGULAR | KalPa | away | 2–1 | 2–1 | REG |
| 2026-09-16 | 2026-27 REGULAR | Kärpät | away | 4–3 | 3–3 | OT |
| 2026-09-08 | 2026-27 REGULAR | HPK | away | 4–0 | 4–0 | REG |
| 2026-09-04 | 2026-27 REGULAR | Ässät | away | 1–5 | 1–5 | REG |
| 2026-09-01 | 2026-27 REGULAR | Lukko | away | 2–0 | 2–0 | REG |
| 2026-04-30 | 2025-26 PLAYOFF | SaiPa | away | 2–7 | 2–7 | REG |
| 2026-04-27 | 2025-26 PLAYOFF | Tappara | home | 3–4 | 3–4 | REG |
| 2026-04-25 | 2025-26 PLAYOFF | Tappara | away | 1–2 | 1–1 | OT |
| 2026-04-23 | 2025-26 PLAYOFF | Tappara | home | 1–5 | 1–5 | REG |
| 2026-04-21 | 2025-26 PLAYOFF | Tappara | away | 2–3 | 2–3 | REG |
| 2026-04-19 | 2025-26 PLAYOFF | Tappara | home | 6–0 | 6–0 | REG |
| 2026-04-16 | 2025-26 PLAYOFF | Tappara | away | 3–2 | 3–2 | REG |
| 2026-04-11 | 2025-26 PLAYOFF | KalPa | away | 4–3 | 4–3 | REG |

**Source review caveat:** 40 dated prior match results reconstructed, crosschecked on major sources and official fixtures, but original per-row saved HTML captures, publication `known_at`, native IDs for every prior game, independent two-collector confirmation for every row and current player status are not all verified. `RESEARCH_EXPORT` rows are deliberately QUARANTINED until that verification. No retired store or archived league profile was used. Last-season playoff opponent concentration (Tappara) and roster churn constrain transferability.

### A4. Distribution construction, baseline and expected sporting quantities
The primary GitHub `MODEL_ASSISTED_CYCLE_V1` adapter was **not executed**: `python -m ml capability --out CAPABILITY_RECEIPT.csv` exited 1 (`No module named ml`); repository `git clone` exited 128 (`Could not resolve host: github.com`). A GitHub connector successfully read pinned published rules but supplied no runnable checkout. No real fitted dataset/release, expert mixture, feedback or model bundle exists in this mini; baseline `BASELINE_LEAGUE_V1` NOT_EXECUTED (no source-reviewed identical-contract cohort).
**Independent analyst calculation (scenario, not a GitHub model):** independent Poisson 60-minute regulation goals. `λ_HPK = sqrt(HPK_GF_2026/13 × ILVES_GA_2026/12) = sqrt((26/13) × (24/12)) = 2.000`; `λ_ILVES = sqrt(ILVES_GF_2026/12 × HPK_GA_2026/13) = sqrt((35/12) × (37/13)) = 2.881`. Skellam difference (HPK−Ilves) and Poisson sum; both tails numerically computed using SciPy; exact one-goal OT/SO decider added to tied regulation states. No empirical home-ice, back-to-back, goalie, xG, pace, PP/PK, pulled-goalie or empty-net coefficient was fitted; these remain explicit sensitivity/qualitative limitations.
- **Expected 60-minute goals:** HPK 2.000; Ilves 2.881; combined 4.881; expected regulation margin Ilves +0.881.
- **Expected recorded full-match goals under a single goal in every OT/SO decision:** 5.054 = 4.881+P(60m tied) 0.173. Hypothetical 55% Ilves tiebreak split gives Ilves 2.976 and HPK 2.078 expected displayed goals. OT timing/type and the operator’s counting rules are not independently established.
- **Exact supplied-line probabilities:** `P(Under5.5)=PoissonCDF(k=5, λ=4.881)=63.68%`; `P(Over5.5)=36.32%`; `P(HPK +1.5)=P(HPK_reg−Ilves_reg ≥ −1)=61.96%`; `P(Ilves ML)=P(Ilves_reg>HPK_reg)+0.55×P(tie)=66.03%`. No pushes at half-goals.
Error due to Poisson numerical truncation in SciPy negligible compared with data/model uncertainty (~1e-10); **this is not a calibration error bound**. No p_card exists to satisfy numerical gating or warm/feedback learning requirements. Historic form windows overlap.

### A5. Selection, dependence and contract definitions
- Descriptive analyst order: Ilves ML 66.03%, Under5.5 63.68%, HPK+1.5 61.96%, Over5.5 36.32%. This is **not** a frozen or eligible PRIMARY_V3 card. Both opposite 5.5 totals retained but never selected simultaneously. Every supplied item assessed, no market-based candidate construction.
- Under/Over 5.5 are exact complements with no push under the stated endpoint. Ilves ML loss and HPK+1.5 loss are **mechanically disjoint** in an ordinary one-goal OT/SO decision: a defeated Ilves implies HPK +1.5 wins; an Ilves victory by ≥2 means Ilves ML wins. Not an empirical skill guarantee.
- Under the common independent-Poisson scenario, the exact joint probability that **both** analyst first and second rows lose (Ilves ML loses AND Under 5.5 loses) is 11.13%, evaluating every integer 60-minute score state and assigning HPK a 45% win share on regulation ties. No independence product was used; OT/SO counting convention assumed.
- Original proper baselines, opposite-family shadow, best non-complementary gate across expanded candidate universe, RET03, RET04, SHADOW_RANK_DELTA, SHADOW_BASE_ONLY and minimum-joint-failure freeze were NOT_EXECUTED without the primary bundle. This audit is a scenario comparison, not scored ML prediction.

### A6. Goaltending, skaters, schedule and mechanics
- Exact-match independently indexed Jatkoaika team-sheet supplies HPK first line Roope Vesterinen / Sami Päivärinta / Brendan Ranford; additional skaters include Olli Korhonen, Ethan De Jong, Olli Palola; HPK goalie roster **Jakob Crespin #65 and Kim Saarinen #1**. Ilves first line Topias Hynninen / Luke Henman / Jens Lööke; Ilves goalie roster **Mantas Armalis #40 and Christoffer Rifalk #65**. Source: https://www.jatkoaika.com/LIIGA/Kokoonpanot/HPK-Ilves/62530. These are game-specific reported lines, NOT proven starting goalie by goalie-list ordering; publication time/official corroboration incomplete, so goalie status START_UNCONFIRMED. Injuries, scratches, medically eligible/ineligible absences, precise special teams and ice-time not independently closed. A reported lineup does not prove a player will play normal minutes.
- Ilves club report confirms Armalis achieved four shutouts by 10 Oct and shut out Jokerit 3–0 with 16 saves; NOT evidence that he necessarily starts against HPK. Ilves 12 games/26 points and HPK 13/18 points in club report. HPK played SaiPa on 15 Oct, losing 2–1; Ilves has not played since 10 Oct, rest advantage favoring Ilves qualitatively. The latest head-to-head on 8 Sep ended HPK 0–4 Ilves, but this is one match and not a stable 4-goal expected margin.
- Confirm venue Pohjantähti Areena in Hämeenlinna from Ilves and HPK club previews. No verified pregame weather/ice-surface issue. Hockey ice is indoor; outside air only matters with actual rink mechanism. Empty-net late-game risk, power plays and first-change advantage not fitted. Special teams scoring and xG not independently aggregated for both teams; do not infer PP advantage from shots alone.

### A7. Sensitivity and fragility of the supplied rows
The following are **plausible, deliberately assumed ±goal-intensity cases**, not statistical confidence intervals. OT/SO Ilves 55% share held fixed; no fitted distributions or validation.
| Case (unfitted) | λ_HPK | λ_Ilves | HPK +1.5 | Ilves ML | Under 5.5 | Over 5.5 |
|---|---:|---:|---:|---:|---:|---:|
| BASE_RAW_CURRENT_SEASON_GEOMEAN | 2.000 | 2.881 | 61.96% | 66.03% | 63.68% | 36.32% |
| LOW_TOTAL | 1.700 | 2.581 | 62.88% | 67.01% | 73.98% | 26.02% |
| HIGH_TOTAL | 2.300 | 3.181 | 61.21% | 65.20% | 53.21% | 46.79% |
| STRONG_ILVES | 1.800 | 3.181 | 53.13% | 73.62% | 61.93% | 38.07% |
| STRONG_HPK | 2.300 | 2.681 | 69.96% | 57.52% | 61.93% | 38.07% |
| REST_BACK_TO_BACK_STRESS | 1.800 | 3.031 | 55.90% | 71.67% | 64.56% | 35.44% |
| BACKUP_GOALIE_SWING | 2.250 | 3.131 | 61.32% | 65.33% | 54.94% | 45.06% |
Tiebreaker sensitivity: Ilves full-match moneyline probability increases/decreases by ~0.8656 percentage points for each ±0.05 change in conditional OT/SO win share, because P(tie)≈17.31%. Starter/empty-net uncertainty is not reducible to a confidence interval from the available data. Adjacent rank changes are ADJUSTMENT_DEPENDENT; do not claim a single robust top-two pair. Central predicted winner ILVES with 66.03% **scenario** full-match win, but significant model risk.

### A8. Sources, corroboration and field-level closure
| Field | Opened source and supporting comparison | Current closure / next required step |
|---|---|---|
| Fixture native ID/start | https://liiga.fi/en/game/2027/2701384/events; https://hpk.fi/biorex-otteluennakko-hpk-ilves-16-10-vieraita-tampereelta/; https://www.ilves.com/otteluennakko/ilves-matkustaa-perjantaina-hpkn-vieraaksi/ | Verified identity, scheduled local start and timezone; actual first puck drop unverified. |
| Home/away/venue | Both clubs’ separate announcements, Pohjantähti Areena | VERIFIED announced venue; exact condition UNKNOWN. |
| Current 2026-27 13/12 games and score | Liiga schedules, https://omnihockey.com/teams/liiga-hpk/schedule, https://omnihockey.com/teams/liiga-ilves/schedule, both club results. Official October 9 HPK SO and October 3 OT separately checked. | 13/12 dated current regular games reconstructed; full independent line-by-line corroboration and archived primary page snapshot INCOMPLETE. |
| Prior 2025-26 7/8 playoff results | https://liiga.fi/fi/ohjelma/?joukkue=hpk&kausi=2025-2026&sarja=playoffs vs https://www.eliteprospects.com/team/610/hpk/scores/2025-2026; https://liiga.fi/fi/ohjelma/?joukkue=ilves&kausi=2025-2026&sarja=playoffs vs https://www.ilves.com/ottelut-2025-26/ | 20 dated historical results/team reconstructed; true n=20. Some pregame publication provenance not independently captured; last-season playoff use diagnostic only. |
| Exact forward/defender roles and goalies | https://www.jatkoaika.com/LIIGA/Kokoonpanot/HPK-Ilves/62530; league official match-center lineup indexed but JavaScript/empty content | Jatkoaika provides specific listed lines and goalie pairs; independent full official confirmation including actual goalie starter and omissions still OPEN. |
| Injury/suspension/availability | Club preview https://www.ilves.com/otteluennakko/ilves-matkustaa-perjantaina-hpkn-vieraaksi/ and https://hpk.fi/biorex-otteluennakko-hpk-ilves-16-10-vieraita-tampereelta/; Jatkoaika exact roster; news cross-search | Named medical/suspension omissions NOT_CLOSED; verify club medical and final scratches. |
| Endpoint settlement | GitHub `RULES_ICE_HOCKEY.md` and Liiga gamebooks with OT/SO displays | Operator not named; UNKNOWN_DEFINITION, explicitly freeze full-match and regulation readings. |
| Primary/league baseline | GitHub pinned v20.0 controls, local `LOCAL_RUNTIME_ATTEMPT.json` | No executable source checkout or verified competition history/release; model & baseline p NOT_ESTIMATED. |
| Timing known-at | Historical game dates before match; retrieved after kickoff; event lineup publication time missing | POST_START_RESEARCH, CLEAN_PRE_START_INPUTS NOT_VERIFIED; external independent timestamped captures required. |
| Source register, custody and desktop state | Prior mini complete readback; current repository pinned control reads; no shared export store mutation | Outside desktop actual writer custody and import identities NOT verified; local draft only. |
This source table lists real attempted routes; no search failure is declared a final source exhaustion. Absence fields remain open, so global completion = RESEARCH_INFORMATION_INCOMPLETE.

### A9. Execution, learning export, research completion and audit C1–C22
| Requirement | Performed / disposition |
|---|---|
| C1–C4 authority/identity/time | Pinned GitHub SHA `27e013c35477dbffb7b7699b269a0b978fb69b7f`; event 2701384, date/time, kickoff conversion; duplicate check within available 4-card copy. Desktop/pending canonical bodies not wholly scanned; POST_START_RESEARCH. |
| C5–C8 form | Two actual 20-row histories built, L5/L10/L15/L20 true n, separate 2026 regulation and 2025 playoffs; 40-row audit + structured export. Independent raw-source archival remains incomplete. |
| C9–C11/C20 players/availability | Exact-game named skaters and goalie pairs retrieved; confirmed *starting* goalie, scratches/medical and original provider timestamp UNKNOWN. |
| C12–C15 goal grid | Computed independent Poisson regulation goals, Skellam goal margin, OT/SO tie branch, winner, all four supplied numerical directions, sports expected values, full sensitivity; clearly NOT_PRIMARY. |
| C16–C19 selection/dependence | Uncalibrated diagnostic order, floor/gap, complementary states, mechanically disjoint losing sets and exact 11.13% joint loss; no primary gate or retained frozen baseline/shadow. |
| C21 ML execution | `python -m ml capability --out ...` EXIT 1, `No module named ml`; `git clone --depth 1 https://github.com/danisgreat/Sports-Research.git` EXIT 128 DNS. `pip install -r ml/requirements.txt` not executable because checkout missing; true error JSON retained. No asserted receipt or primary `p_card`. |
| Learning export | `RESEARCH_EXPORT/LOCAL-2026101679B3FBCC8D-G0005/` written with exact allowed schema for GAME_OBSERVATIONS (40 rows), TARGET_EVENT (1), AVAILABILITY (10), TEAM_GAME_STATS header only. Inputs intentionally QUARANTINED with known_at/published_at blank where not demonstrated; SOURCE_CAPTURE_NOTES is a generated extraction summary, not raw official webpage copy; dry-run ingest not executed without `ml`. No shared store write. |
| C22 prior bytes and manifest | Entire original mini read; original G0001–G0004 card blocks retained byte-for-byte, previous manifest rows retained byte-for-byte. Added G0005 as **candidate READ_ONLY_DRAFT** before running footer, refreshed intake/footer, readback verification recorded separately. |
**Research completion matrix:** identity PASS_PARTIAL; historical row acquisition PASS_PARTIAL (40 rows but corroboration incomplete); exact lineup/goalie PARTIAL; suspension/injury INCOMPLETE; endpoint UNKNOWN_DEFINITION; parameters and scenario arithmetic COMPLETE_NOT_PRIMARY; fitted model NO_RUNTIME; same-line baseline NO_RUNTIME; sensitivity COMPLETE_ASSUMPTION_ONLY; local custody UNVERIFIED; complete deliverable READY_AS_DRAFT. Overall `INFORMATION_INCOMPLETE / RESEARCH_ONLY_NO_MODEL / NOT_ISSUED`. No pre-start issuance, no settlement, no GitHub writes.
<!-- END CANONICAL RESEARCH P-605 -->
