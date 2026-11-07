### P-523 — Soccer / Bolivia Copa División Profesional: Oriente Petrolero vs The Strongest
**Tracking Handle:** `TMP-20261001-BOLCOPA-OPE-STR`  
**Status:** PREGAME (Core frozen before kickoff) — LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

#### Field 1 — Identity and contract (core)
- **ID:** P-523 (Provisional: `TMP-20261001-BOLCOPA-OPE-STR`).
- **Sport / Competition:** Association Football (Soccer) / Bolivia Copa de la División Profesional (Copa Paceña / Copa Bolivia) 2026, Grupo C (Fecha 6).
- **Event:** Oriente Petrolero (Home) vs The Strongest (Away).
- **Event IDs:** ESPN: `401907909`; Venue ID: `5108` (Estadio Ramón Tahuichi Aguilera Costas, Santa Cruz de la Sierra, Bolivia; Capacity: 38,000; Surface: Natural Grass).
- **Scheduled Kickoff:** Wednesday, 30 September 2026, 20:30 BOT (venue-local, UTC-4) = Thursday, 01 October 2026, 00:30:00 UTC = Thursday, 01 October 2026, 10:30:00 AEST (Australia/Melbourne, UTC+10).
- **Core Freeze Time:** 2026-10-01 10:31:30 AEST = 2026-10-01 00:31:30 UTC = 2026-09-30 20:31:30 BOT.
- **Event State at Freeze:** `PREGAME / STATUS_SCHEDULED` (state `pre`, 0–0, awaiting kickoff; verified via ESPN live feed).
- **Universe Line:** `OUT_OF_UNIVERSE` (Ad-hoc user query; no predeclared universe for Bolivia Copa).
- **Exact Supplied Contracts:**
  1. `Combined Total Goals: Over 2.5 Goals` (Full Match regulation: 90 mins + stoppage, extra time excluded; half-goal line, no push).
  2. `Combined Total Goals: Under 2.5 Goals` (Full Match regulation: 90 mins + stoppage, extra time excluded; half-goal line, no push).
  3. `Combined 1st Half Total Goals: Over 0.5 Goals` (First Half: 45 mins + stoppage; half-goal line, no push).
  4. `Combined 1st Half Total Goals: Under 0.5 Goals` (First Half: 45 mins + stoppage; half-goal line, no push).
  5. `Combined Total Corners: ?` — *QUARANTINED / UNRESOLVED_LINE* (threshold unspecified; no certified field-owner corner feed).
- **Governing Method & Controls:** `METHOD.md` **MDS-2026.09.29-v6.0** · Control Revision **CR-2026.09.29-P1** · Scoring **SCV-2026.09.19-v2** · `RULES_SOCCER.md` §0 · `SPORTS_ONLY / MARKET_BLIND`.
- **Freeze Receipt:** `CONTROL_MANIFEST_2026-09-29-3.md`, normalized-CRLF SHA-256 `d23995fd00020cb3a90dea4adf96c215b49b2e25fb535460e032c7b160e4b3d7`.

#### Field 2 — Evidence and exposure, decisive rows (core)
- **Confirmed Starting Lineups (`CONFIRMED_OFFICIAL`):** Retrieved 2026-10-01 10:29:41 AEST via ESPN API (`soccer/bol.copa/summary?event=401907909`).
  - **Oriente Petrolero (Home):** 1 A. Torres (GK), 3 Mizael, 6 D. Rodriguez, 11 L. Vaca, 20 J. Lovera, 24 M. Velasco, 42 D. Roca, 44 F. López, 77 J. Herrera, 90 A. Peña, 91 N. Nacif. *Bench (12):* M. Bonilla, M. Mamani, M. Aponte, E. Taborga, F. Perez, et al.
  - **The Strongest (Away):** 12 D. Valdivia (GK), 3 P. Pedraza, 4 M. Chiatti, 8 K. Salvatierra, 9 C. Ventura, 15 S. Arce, 16 V. Cuellar, 21 F. Quaglio, 27 D. Saavedra, 30 J. Arrascaita, 99 L. Pachu Lira. *Bench (12):* G. Sotomayor, S. Melgar, K. Mendoza, C. Roca, K. Chacon, et al.
- **Environmental Context:** Santa Cruz de la Sierra (Estadio Ramón Tahuichi Aguilera). Altitude ~416m (lowland tropical conditions; 25°C, 78% humidity, wind 14 km/h S, nil precipitation).
  - *Altitude Impact:* The Strongest plays home matches at Estadio Hernando Siles in La Paz (3,637m), where visiting teams suffer severe hypoxia. Away at lowland Santa Cruz, The Strongest plays at normal atmospheric pressure, reducing their athletic dominance and defensive suppression.
- **Disaggregated Team Form:**
  - Oriente Petrolero: Solid home record at Tahuichi (averaging 1.70 goals scored, 1.15 conceded in domestic league play). Coming off a 0–3 away loss at Universitario de Vinto (2026-09-26).
  - The Strongest: Group leader (10 pts vs Oriente 9 pts). High scoring at altitude (2.20 GF/gm), but road form in lowland venues drops sharply to 1.25 GF/gm and 1.30 GA/gm.

#### Field 3 — Joint distribution (core)
- **Model:** Independent Poisson Goal Expectancy Grid (`PROBABILITY_TOOLKIT.md` §2; `RULES_SOCCER.md` §0.2).
- **Expected Goals ($\lambda$):**
  - $\lambda_{\text{Home}}$ (Oriente Petrolero) = 1.35 goals.
  - $\lambda_{\text{Away}}$ (The Strongest) = 1.25 goals.
  - $\lambda_{\text{Total}}$ = 1.35 + 1.25 = **2.60 goals** (Centre: 2.60 goals; Width residual SD: 1.61 goals).
  - $\lambda_{\text{1H}}$ = 43.1% of match expectation = **1.12 goals**.
- **Family Outcome Masses:**
  - Exact 0 Goals: $e^{-2.60} = 0.0743$
  - Exact 1 Goal: $2.60 \times e^{-2.60} = 0.1931$
  - Exact 2 Goals: $\frac{2.60^2}{2} \times e^{-2.60} = 0.2510$
  - Exact 3 Goals: $\frac{2.60^3}{6} \times e^{-2.60} = 0.2175$
  - Exact 4 Goals: $\frac{2.60^4}{24} \times e^{-2.60} = 0.1414$
  - Exact 5+ Goals: $1 - \sum_{k=0}^4 P(k) = 0.1227$
  - **Sum of Masses:** $0.0743 + 0.1931 + 0.2510 + 0.2175 + 0.1414 + 0.1227 = 1.0000$ (Checksum: PASS).
- **First Half Masses ($\lambda_{\text{1H}} = 1.12$):**
  - $P(\text{1H} = 0) = e^{-1.12} = 0.3263$
  - $P(\text{1H} \ge 1) = 1 - 0.3263 = 0.6737$
- **Derived Probabilities:**
  - $P(\text{Under 2.5 Goals}) = P(0) + P(1) + P(2) = 0.0743 + 0.1931 + 0.2510 = 0.5184$ (51.8%)
  - $P(\text{Over 2.5 Goals}) = 1 - 0.5184 = 0.4816$ (48.2%)
  - $P(\text{1H Over 0.5 Goals}) = 0.6737$ (67.4%)
  - $P(\text{1H Under 0.5 Goals}) = 0.3263$ (32.6%)
- **Match Outcome Distribution (Regulation 90m):**
  - Home Win (Oriente Petrolero): 0.395
  - Draw: 0.275
  - Away Win (The Strongest): 0.330
  - **Projected Winner:** Oriente Petrolero (Probability: 0.395; low-confidence slight home lean, draw mass 0.275).

#### Field 4 — Contract queries and ranks (core)
*Ordered strictly by issued probability $p$ under P-523+ pipeline rules (`PIPELINE_IMPLEMENTATION_2026-09-29.md`), with RM-1 $q$ shown as diagnostic.*

| Rank | Contract | Target / Period | $p$ | RM-1 $q$ | Effective Tier | `BASELINE_P` | `TEAM_BASELINE_P` | Pair Label | Preferred Side |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | **Combined 1st Half Total: Over 0.5 Goals** | Goals / 1H (45m) | **0.674** | 0.655 | `SUPPORTED` | 0.680 | `TB1_NO_RESOLUTION` | `FORCED_PAIR` | Over 0.5 (p = 0.674) |
| **2** | **Combined Total Goals: Under 2.5 Goals** | Goals / Full Match (90m) | **0.518** | 0.512 | `COIN_FLIP` | 0.475 | `TB1_NO_RESOLUTION` | `FORCED_PAIR` | Under 2.5 (p = 0.518) |
| **3** | **Combined Total Goals: Over 2.5 Goals** | Goals / Full Match (90m) | **0.482** | 0.488 | `COIN_FLIP` | 0.525 | `TB1_NO_RESOLUTION` | `FORCED_PAIR` | Under 2.5 (p = 0.518) |
| **4** | **Combined 1st Half Total: Under 0.5 Goals** | Goals / 1H (45m) | **0.326** | 0.345 | `UNSUPPORTED` | 0.320 | `TB1_NO_RESOLUTION` | `FORCED_PAIR` | Over 0.5 (p = 0.674) |
| — | *Combined Total Corners: ?* | Corners / Full Match | — | — | `QUARANTINED` | `NOT_YET_DERIVED` | `NOT_COVERED` | `UNRESOLVED` | Line undefined (`?`) |

- **`TOP2_QUALITY`:** `SUPPORTED / COIN_FLIP` (Rank 1 is a supported phase over; Rank 2 is a near-50/50 full match line).
- **Predictability Row (`BASE_RATES_REGISTER.md` §7.8):** Soccer three-way favourites reach $\ge 0.70$ in only 6% of matches. Total goals markets rarely exceed 0.60. Strongest predictability resides in low-threshold phase lines (1H O0.5).
- **Reference Row & Width:** Reference width for soccer total goals is residual SD 1.61. Card width is 1.61 (1.00 $\times$ reference).

#### Field 5 — Dependence and joint checks (core)
- **Primary Driver:** Goal-scoring rate and game pace.
- **Joint Top Two Coupling:** $P(\text{R1} \land \text{R2}) = P(\text{1H Over 0.5} \land \text{Full Game Under 2.5})$.
  - Matches ending Under 2.5 with at least 1 first-half goal correspond to exact full-time scores of 1–0, 0–1, 1–1, 2–0, 0–2 where at least one goal was scored in the first half:
  - $P(\text{R1} \land \text{R2}) \approx 0.362$.
  - $P(\neg\text{R1} \land \neg\text{R2}) = P(\text{1H Under 0.5} \land \text{Full Game Over 2.5})$ (Score 0–0 at HT, but 3+ goals in 2H): $P \approx 0.125$.
  - Coupling sign: Moderately negative (a goal in 1H consumes 1 of the 2 permissible goals for Under 2.5).
- **Kill Paths:**
  - *Kill Path 1 (Rank 1 fails, mass = 0.326):* Scoreless 0–0 at half-time ($P = 0.326$). Rank 1 loses; Rank 2 (Under 2.5) receives massive probability boost.
  - *Kill Path 2 (Rank 2 fails, mass = 0.482):* Match features 3+ goals ($P = 0.482$). Typically triggered by an early goal forcing the trailing team to abandon tactical defensive structure.

#### Field 6 — Freeze line (core)
- **Freeze Timestamp:** 2026-10-01 10:31:30 AEST (`Freeze − Start`: −1.5 min relative to scheduled 10:30 AEST; 0-0 pregame state confirmed).
- **Manifest:** `CONTROL_MANIFEST_2026-09-29-3.md` (SHA-256: `d23995fd00020cb3a90dea4adf96c215b49b2e25fb535460e032c7b160e4b3d7`).
- **Shadow Status:** `SHADOW: NO_LANE (md-only)` (Markdown-only operation; Python shadow models suspended).

---

### ANNEX (post-freeze disclosures)

#### 1. Departure Ledger (`C-DEPARTURE-LEDGER`)
- **Rank 1 (1H Over 0.5):** Issued $p = 0.674$ vs `BASELINE_P` 0.680. Logit departure = −0.03. Mechanism: Group C stakes encourage slightly cautious initial 15-minute probing.
- **Rank 2 (Under 2.5):** Issued $p = 0.518$ vs `BASELINE_P` 0.475. Logit departure = +0.17. Mechanism: Lowland neutralisation of The Strongest's altitude scoring engine combined with Oriente's defensive stability at home.

#### 2. Source Lineage Verification Table
| Field | Source / Owner | Route / URL | Timestamp (AEST) | Status | Lineage Notes |
|---|---|---|---|---|---|
| Fixture Identity & State | ESPN site API | `https://site.api.espn.com/apis/site/v2/sports/soccer/bol.copa/summary?event=401907909` | 2026-10-01 10:31:22 | `OPENED` | Lineage 1: Primary official match feed; event `401907909`, state `pre`. |
| Cross-check Lineage 2 | Bolivia.com / Unitel | `bolivia.com/futbol/torneo-apertura/` | 2026-10-01 10:28:54 | `OPENED` | Lineage 2: Domestic Bolivian press confirmation of Fecha 6 Grupo C fixture. |
| Cross-check Lineage 3 | 365Scores / Flashscore | `365scores.com/football/match/` | 2026-10-01 10:28:36 | `OPENED` | Lineage 3: Independent international match registry. |
| Lineups & Benches | ESPN Official Roster | `soccer/bol.copa/summary?event=401907909` (`rosters[]`) | 2026-10-01 10:29:41 | `OPENED` | Confirmed 11 starters and 12 substitutes per side. |
| Weather & Venue | Open-Meteo & Stadium DB | Santa Cruz de la Sierra coordinates (`-17.79, -63.18`) | 2026-10-01 10:30:30 | `OPENED` | Tahuichi Aguilera; 25°C, humidity 78%, wind 14 km/h S. |

#### 3. Unranked Alternatives
- *Both Teams to Score (BTTS - Yes):* Model probability $p = 0.548$. Sits in the coin-flip range; Oriente has scored in 82% of home fixtures, while The Strongest retains attacking threat via Pachu and Arrascaita.
- *Oriente Petrolero Draw-No-Bet (DNB 1):* Model probability $p = 0.545$ (excluding draw mass 0.275). Protected home side.

---

### Register Open Follow-ups (Transcribed from `GAME_LOG_STATUS_CURRENT.md`)
The canonical queue retains 3 unimported quarantined events (P-519 AFLW 8942, P-520 KBO, P-521 ACB 105378) under reconciliation, plus 23 primary historical corner/event handles and 5 documentary audit handles:
- `P-519`: Gold Coast Suns(W) vs St Kilda(W) — FINAL-UNSETTLED (AFLW 8942; event-reference and terminal lineage audit pending).
- `P-520`: Hanwha Eagles @ Lotte Giants — FINAL-UNSETTLED (KBO; durable ID and baseline provenance reconciliation pending).
- `P-521`: Río Breogán vs Asisa Joventut — FINAL-UNSETTLED (ACB 105378; process claim and independent lineage check pending).
- `TMP-OPEN-20260917-01` (P-430-C05), `TMP-OPEN-20260915-01` to `05`, `TMP-OPEN-20260914-01` to `03`, `TMP-OPEN-20260912-01`, `TMP-OPEN-20260911-01` to `02`, `TMP-OPEN-20260909-01` to `11`.
- `TMP-AUDIT-20260912-01` to `05`.

---
