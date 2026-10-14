# H0 Independent Dataset Card & Specification

> **SUSPENDED: design note (2026-10-09).** This card specified the independent H0 training datasets and the point-in-time feature store. The executable runtime, its fitted models, its data pipelines and the JSON registries that this document specifies were removed on 2026-10-09 when the framework became Markdown-only (commits `a64675cf7` to `a93352c30`; last working state at commit `37203fc2b`). Nothing in this document is a rule or is implemented; no model it describes exists. Current rules: [CURRENT_RULES.md](CURRENT_RULES.md). Cards are built by hand ([PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md), [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md)). Bringing any of it back needs an explicit user instruction (prompt 8).

**Authority:** MDS-2026.10.01-v8.0 / CR-2026.10.06-NUMERICAL-1.
**Status:** Mandatory Standard for Numerical Model Training and Calibration.

---

## 1. Separation of D0 and H0

### 1.1 The D0 Frozen Benchmark (Governance & Process Only)
- **Role**: Qualitative evaluation, error mechanism discovery, QA scenario design, retrospective rule auditing, and contract geometry verification.
- **Strict Prohibition**: **Never fit numerical model coefficients, hyperparameter tuning, or probability calibrators on D0.** D0 consists of user-selected events with changing contract geometries and selective coverage. Training on D0 introduces catastrophic selection bias.

### 1.2 The H0 Population Standard (Numerical Machine Learning)
- **Role**: The sole authoritative training, validation, and calibration dataset for numerical sports prediction models.
- **Requirements**:
  1. **Declared Universe**: Contains *all* eligible matches in a declared competition and season window without ad-hoc selection.
  2. **Point-in-Time Safe**: Every feature represents facts demonstrably known *prior* to match or prediction cutoff (`known_at <= cutoff_at`).
  3. **Standardized Labels**: Pure sporting outcomes (runs, points, goals, margins, wickets, periods) rather than bookmaker betting lines.

---

## 2. Feature Schema & Point-in-Time Contract

Every feature record in the H0 feature store must satisfy the canonical schema:

| Column | Type | Description | Invariant / Constraint |
|---|---|---|---|
| `event_id` | STRING | Durable canonical event ID | Unique per sporting match |
| `entity_id` | STRING | Team or player ID | Normalized across seasons |
| `feature_name` | STRING | Standardized feature identifier | Snake_case, descriptive |
| `value` | FLOAT / INT / JSON | Feature value | Null if unobserved or missing |
| `effective_at` | TIMESTAMP (UTC) | Time the sporting fact occurred | e.g. previous game end |
| `known_at` | TIMESTAMP (UTC) | Earliest time publicly known | Must be <= cutoff_at |
| `observed_at` | TIMESTAMP (UTC) | When feature was recorded | Audit trail |
| `retrieved_at` | TIMESTAMP (UTC) | When pipeline fetched data | Audit trail |
| `source_id` | STRING | Authoritative provider ID | e.g. `cricsheet_json` |
| `source_version` | STRING | Version of the upstream API/file | e.g. `2026.10` |
| `transform_version` | STRING | Feature calculation code version | Semver |
| `cutoff_at` | TIMESTAMP (UTC) | Model prediction boundary | Usually scheduled start |
| `quality_flag` | STRING | `VALID`, `MISSING`, `STALE`, `CONFLICT` | Non-valid features penalized |
| `raw_snapshot_hash` | STRING (SHA-256) | Hash of raw source body | Cryptographic reproducibility |

### Invariant:
$$\text{If } known\_at > cutoff\_at \implies \text{Feature is marked MISSING and masked from model input.}$$

---

## 3. Declared H0 Populations

| Population ID | Sport | Target Scope | Date Range | Primary Grain | Primary Sources |
|---|---|---|---|---|---|
| `H0-CRICKET-TEST-v1` | Cricket | Men's Test Cricket | 2006–2026 | Session / Day / Match | Cricsheet JSON + ESPNcricinfo |
| `H0-CRICKET-LO-v1` | Cricket | ODI & T20 Internationals | 2006–2026 | Over / Phase / Match | Cricsheet JSON |
| `H0-BASKETBALL-NBA-v1` | Basketball | NBA Regular Season & Playoffs | 2010–2026 | Game / Team Possessions | NBA Official Stats / Balldontlie |
| `H0-NFL-v1` | Football | NFL Regular Season & Postseason | 2000–2026 | Drive / Play / Game | `nflfastR` / `nflverse` |
| `H0-MLB-v1` | Baseball | MLB Regular Season | 2015–2026 | Plate Appearance / Inning / Game | Baseball Savant / `pybaseball` |
| `H0-AFL-v1` | Australian Rules | AFL Men's Premiership | 2010–2026 | Match / Quarter / Team | `fitzRoy` (Footywire & AFL Tables) |
| `H0-NRL-v1` | Rugby League | NRL Premiership | 2020–2026 | Match / Half / Team | `nrlR` / Rugby League Project |
| `H0-SOCCER-EPL-v1` | Soccer | English Premier League | 2010–2026 | Match / Half / Team | Football-Data.co.uk / StatsBomb |
| `H0-NHL-v1` | Ice Hockey | NHL Regular Season | 2010–2026 | Period / Shot / Game | MoneyPuck / NHL API |
| `H0-TENNIS-v1` | Tennis | ATP & WTA Tour Main Draws | 2011–2026 | Point / Game / Set / Match | Tennis Abstract / Sackmann MCP |

---

## 4. Chronological Splitting Manifest

Random splits (e.g. k-fold cross-validation or random 80/20) are **strictly forbidden** in H0. All evaluations must follow rolling-origin time-series cross-validation:

```text
[   TRAIN BLOCK   ] ---> [ TUNE BLOCK ] ---> [ CALIBRATION BLOCK ] ---> [ UNTOUCHED TEST ]
      (e.g. 70%)               (10%)                    (10%)                  (10%)
<-------------------------- Chronological Time Progression -------------------------->
```

1. **TRAIN (Training)**: Model coefficient and tree fitting.
2. **TUNE (Validation)**: Hyperparameter selection, feature selection, EWMA decay parameter selection, early stopping.
3. **CAL (Calibration)**: Probability calibration (Platt/sigmoid, isotonic, temperature scaling). **Never calibrate on training predictions.**
4. **TEST (Untouched Test)**: Evaluated only once per model release. No feedback loop into tuning.

---

## 5. Label Definitions & Coherence

Models are trained on full-event target distributions, **never on individual bookmaker lines**:

- **Basketball**: Joint team score matrix $(S_{home}, S_{away}) \implies P(\text{Win}), P(\text{Margin} \ge M), P(\text{Total} \ge T)$.
- **Cricket**: Test Day/Session Runs $R \sim \text{PMF}(r)$, Wickets $W \sim \text{PMF}(w)$; chase stopping rule $S_2 \le S_1 + 1$.
- **American Football**: Team drives and discrete scoring events.
- **Baseball**: Team runs from starter duration + bullpen degradation chains.
- **AFL**: Team scoring shots and conversion $(G, B) \implies 6G + B$.
- **NRL**: Sets and tries/conversions $(T, C) \implies 4T + 2C + \text{FG}$.
- **Soccer**: Team goals $(G_{home}, G_{away})$ and independent corners count $(C_{home}, C_{away})$.
- **NHL**: Team goals $(G_{home}, G_{away})$ with explicit regulation and empty-net tail components.
- **Tennis**: Match winner and joint games $(G_1, G_2) \implies P(\text{Match Win}), P(\text{Handicap } \Delta G), P(\text{Total Games } \ge K)$.

