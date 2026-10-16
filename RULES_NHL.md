> **Primary ML/RL (15 October 2026):** [PRIMARY_PREDICTION_PROTOCOL](PRIMARY_PREDICTION_PROTOCOL.md) supplies actual model-assisted original probabilities in the supported exact competition/endpoint. Keep these sport-specific physical/source/family checks. Unsupported model/phase/participant regimes remain NO_FORECAST, not another league's model. This amendment overrides older blanket manual-model exclusions, not sporting truth or the market firewall.

**Executable forecast cycle (CYCLE-v1).** Apply [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md). New contextual forecasts use MODEL_ASSISTED_CYCLE_V1 with a frozen exact-competition release, actual execution receipt, identical-contract baseline shadows and verified settlement feedback. Existing V3/tennis adapters retain their own cohorts; missing/unsupported inputs require a real failure receipt and retained research. This statistical/procedure release authorises experimental execution, not predictive qualification.

**Local keys until import; updated mini after every game (MINI-v1).** Apply [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md). Prompts 1–3 use stable local event keys and never assign/reserve canonical P-IDs; prompt 4 alone assigns them during verified import. After each prompt-1 game request, append the research/addendum, update and read back the mini, and return its complete updated .md document. Preserve every owner-entered Upcoming game block and all earlier issued bytes. New formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

> **Manual research timing (15 October 2026):** [TIMING_RESEARCH_PROTOCOL](TIMING_RESEARCH_PROTOCOL.md) supersedes older fixed advance research/freeze targets. Complete this sport's research even after play starts when needed. Record verified pre-start inputs, actual issue phase and outcome exposure separately; freeze only the completed original. A post-start-issued card remains in its own research cohort, not a pre-start-release claim.

> **v11 precedence (2026-10-12, audit R09/R11).** [CURRENT_RULES](CURRENT_RULES.md), [SELECTION_RULES](SELECTION_RULES.md), [SCORING_AND_VALIDATION](SCORING_AND_VALIDATION.md), [CARD_AND_LOG_TEMPLATES](CARD_AND_LOG_TEMPLATES.md) and prompt 1 govern new work (MDS-2026.10.12-v11.0). This file remains the sport's reference for playing rules, mechanisms, sources and historical lessons. **Non-operative here:**

> **Mandatory availability research (14 October 2026):** apply [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 under CURRENT_RULES §5b for every competition in this sport. Research both sides' starters/starting role, selected bench/replacements and current medical/absence/eligibility reports separately; use official team sheets, local-language discovery for obscure leagues and a final late-change recheck. Record evidence and actual failed attempts in existing A3/A8/C20. Probable players, rosters and missing injury reports never become confirmation.
> - RM-1 q ranking, q tiers, `TOP2_QUALITY` and cushion-term ranking: new cards rank by p_card (P_ORDER_V2).
> - TB-1 / TB-1-MD "anchoring": `BASELINE_P` is always the league-only `BASELINE_LEAGUE_V1`, and TB-1-MD is a printed team-model reference only.
> - Row-level numeric caps and grade caps not restated in CURRENT_RULES.
> - Steps of the retired RULES_GENERAL / GFA algorithm.
> - Any instruction to rank or settle that conflicts with the controls above.
>
> The two "October 5" authority notes below are historical. Authority mode now follows CURRENT_RULES §0: a run uses either the pinned published main or the local working tree, never both. Recent form follows ARCHIVE_USE_GUIDE online form recipe R2 (L5/L10/L15/L20 counted once).

> **Current authority (October 5):** [METHOD.md](METHOD.md) and [CURRENT_RULES.md](CURRENT_RULES.md) govern new work. Requested qualitative or explicitly uncalibrated research is retained under stable local keys regardless of calibration; prompt 4 alone assigns canonical IDs during import. Numerical performance certification is separate. Read current IDs/freeze from the [status register](GAME_LOG_STATUS_CURRENT.md), unresolved items from the [carryover](research/verification/closure_2026-10-05/carryover.md), and [current implementation evidence](research/verification/implementation_2026-10-05/REPORT.md). Earlier method, queue, freeze and eligibility statements below retain their historical scope.

# National Hockey League (NHL) & Professional Ice Hockey Numerical Rules

**Authority:** MDS-2026.10.01-v7.1 / CR-2026.10.05-I8 (with numerical runtime extension CR-2026.10.06-NUMERICAL-1).
**Companion Document:** [RULES_ICE_HOCKEY.md](RULES_ICE_HOCKEY.md) (Foundational Ice Hockey Governance).

---

## 1. Scope & Primary Numerical Pipeline

This document defines the numerical prediction pipeline for the **National Hockey League (NHL)** and North American professional ice hockey (including AHL).

The core generative process is modeled as:

$$\text{Shot Attempts (Corsi)} \longrightarrow \text{Unblocked Shots (Fenwick)} \longrightarrow \text{Shot Quality / Expected Goals (xG)} \longrightarrow \text{Goals}$$

```text
Team 5v5 Shot Pace × Shooting Efficiency (xG)
                     +
Special Teams Opportunities (PP/PK) × Conversion Rate
                     +
Score Effects & Trailing Aggression
                     +
Goalie Save Quality Above Expected (GSAx)
                     +
Late-Game Pulled Goalie & Empty-Net Tail
                     │
                     ▼
  Joint Regulation Score Matrix (Home Goals, Away Goals)
                     │
                     ├── Regulation 1X2 Probabilities (Home / Draw / Away)
                     ├── Puck Line (-1.5 / +1.5) Probabilities
                     ├── Over / Under Goals PMF
                     └── Overtime / Shootout Branch → Full Game Moneyline
```

---

## 2. Invariants & Mechanics

### 2.1 Starting Goaltender Gate (Strict Mandatory Prerequisite)
- Goalies represent the single highest-variance individual factor in ice hockey.
- **Unconfirmed Goalie Rule**: If a starting goaltender is not confirmed via official team announcement, beat reporter morning skate report, or starting warm-up handshake, the model must evaluate an explicit **mixture distribution**:
  $$P(\text{Goals}) = p_{\text{starter}} \cdot P(\text{Goals} \mid \text{Starter}) + (1 - p_{\text{starter}}) \cdot P(\text{Goals} \mid \text{Backup})$$
- Totals on games with unconfirmed starters are strictly barred from Rank #1.

### 2.2 Regulation vs. Overtime/Shootout (Contract Geometry)
- **Regulation 60-Minute Contract**: Settles on the exact score at the end of the third period. Ties settle as `DRAW` on 1X2, or against the regulation line.
- **Full Game (OT/Shootout Included)**:
  - Any game tied after 60 minutes proceeds to 3-on-3 sudden-death overtime (5 minutes) followed by a 3-round shootout.
  - The winner receives exactly **one additional goal**.
  - **Mathematical Consequence**: Every game decided in OT/SO adds exactly 1 goal to an even score, resulting in an **odd total**:
    - A 2–2 tie becomes 3–2 (Total = 5, strictly Under 5.5).
    - A 3–3 tie becomes 4–3 (Total = 7, strictly Over 6.5).
  - Models must account for this discrete odd-number mass when pricing 5.5 and 6.5 full-game totals.

### 2.3 Empty-Net Goals and the Puck Line (-1.5 / +1.5)
- Trailing teams pull their goaltender for a 6-on-5 extra attacker typically with 1:30–2:30 remaining when trailing by 1 or 2 goals.
- **Empirical Base Rate**: Over 70% of two-goal regulation victories in the modern NHL feature an empty-net goal.
- **Puck Line Requirement**: A candidate recommending a $-1.5$ handicap must explicitly compute the probability of an empty-net conversion; candidates backing $+1.5$ must account for the empty-net kill risk.

---

## 3. Data Sources & Regime Controls

1. **Shot-Level Tracking**: MoneyPuck (`moneypuck.com`) 2007–08 to present.
   - Note: MoneyPuck excludes blocked shots from its shot-level tables. Corsi (total shot attempts) must be supplemented via NHL API play-by-play.
2. **Official Verification**: NHL Web API (`api-web.nhle.com/v1/gamecenter/{gameId}/boxscore`) provides official time on ice, starting goalies, empty-net indicators, and period scoring.
3. **Preseason Separation**: Preseason hockey displays 0.6–0.9 fewer goals per game due to split-squad rosters and conditioning. Never combine regular season and preseason training records without an explicit regime indicator.

