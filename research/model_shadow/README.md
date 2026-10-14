# Model Shadow Lane (`research/model_shadow/`)

**Authority:** MDS-2026.10.14-v11.1 Â· CR-2026.10.14-R3 Â· SCV-2026.10.14-v8.
**Framework change:** `2026-10-14-2` (implementing [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](../../ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md) per owner instruction).
**Operational mode:** Markdown, CSV, and text only. All model training and code execution occur in an external private workshop repository outside this folder. Only immutable CSV forecasts, settlements, model cards, parameter tables, and cryptographic SHA-256 receipts enter this directory.

---

## 1. The Reading-Gate Firewall Rule (Mandatory)

> [!IMPORTANT]
> **READING-GATE EXCLUSION FOR PROMPTS 1, 2, AND 3**
> Agents running game-card authoring, live research, or local mini-log drafting (Prompts 1, 2, and 3) **MUST NEVER** open, search, or read any file inside `research/model_shadow/` before freezing their own primary analyst card (`p_card`).
>
> This exclusion guarantees that analyst scenario cards remain genuinely independent research and are never anchored by shadow model probabilities. Prompts 3 (settlement) and 6 (retrospective) may read shadow files only after official event settlement to evaluate paired performance.

---

## 2. Commit, Then Reveal Protocol

To maintain complete point-in-time integrity without anchoring card writers who read published `main`:
1. **Pre-Start Freeze (Commit Hash):** Before the first scheduled start of any cohort in a forecast file, the SHA-256 checksum, file byte count, cutoff timestamp, and first kickoff time are committed to the model's `FREEZE_RECEIPTS.md`.
2. **Post-Start Reveal (Commit Content):** The CSV file containing the actual forecast rows (`SHADOW_FORECASTS_<yyyy-ww>.csv`) is committed immediately after that first scheduled start has passed.
3. **Audit Trail:** Both the commit time and remote push time are recorded. Late files are labelled `LATE_START` and excluded from the primary confirmatory cohort.

---

## 3. Active Shadow Model Register

| Model ID | Sport & League | Engine / Architecture | Target Contracts | Status | Earliest Shadow Start |
|---|---|---|---|---|---|
| `EPL-DC-v1` | Soccer (English Premier League) | Time-decayed Dixonâ€“Coles with low-score $\tau$ correction | Regulation 1X2, Over/Under totals, Asian handicaps | `SHADOW` | 2026-W42 (In season) |
| `NBA-JOINT-v1` | Basketball (NBA) | Discretised joint normal on integer lattice with overtime branch | Moneyline (incl OT), Spread, Total | `SHADOW` | 2026-W43 (Season tip-off) |
| `NBL-JOINT-v1` | Basketball (NBL Australia) | Discretised joint normal with conditional variance | Moneyline (incl OT), Spread, Total | `SHADOW` | 2026-W42 (In season) |
| `AFL-JOINT-v1` | Australian Rules Football (AFL) | Discretised joint normal; 6G+B goals/behinds converter | Match Winner, Line (+/-), Total Points | `SHADOW` | 2027-W12 (Round 1) |
| `IPL-FI-C1-v1` | Cricket (Indian Premier League) | Negative Binomial first-innings total with shrunk venue effect | 1st Innings Runs Over/Under, Phase totals | `SHADOW` | 2027-W12 (Tournament start) |
| `NFL-KEY-v1` | American Football (NFL) | Empirical margin key numbers (3, 7, 10) + Total normal | Moneyline (2-way), Spread, Over/Under | `SHADOW` | 2026-W42 (In season) |
| `NHL-REG-v1` | Ice Hockey (NHL) | Bivariate Poisson regulation model with OT/SO resolution | Regulation 3-way, Puck Line, Total Goals | `SHADOW` | 2026-W42 (In season) |
| `MLB-NB-v1` | Baseball (MLB) | Negative Binomial runs with 9th-inning home walk-off rule | Moneyline, Run Line (+/- 1.5), Over/Under | `SHADOW` | 2027-W13 (Opening Day) |
| `NRL-JOINT-v1` | Rugby League (NRL) | Discretised joint normal with Golden Point extra-time state | Head-to-Head, Line (+/-), Total Points | `SHADOW` | 2027-W10 (Round 1) |

---

## 4. Standard CSV Data Schemas

### 4.1 Forecast Row Schema (`SHADOW_FORECASTS_<yyyy-ww>.csv`)
Every row prices one specific proposition from the model's unified event state distribution:

```csv
shadow_row_id,model_id,model_version,event_key,competition,season,stage,scheduled_start_utc,cutoff_utc,frozen_utc,endpoint,family,orientation,line,mass_win,mass_push,mass_loss,mass_void,p_decisive,mean_home,mean_away,sd_margin,sd_total,cov_home_away,baseline_p,baseline_id,team_baseline_p,calibration,inputs_status,label_tier_trained_on,workshop_commit,data_snapshot_sha256,archive_commit,status
```

- `shadow_row_id`: Unique identifier `<model_id>:<event_key>:<contract_key>`.
- `p_decisive`: Decisive win probability $\frac{W}{W+L}$ (or `NOT_COMPUTED` if $W+L=0$).
- `mass_win`, `mass_push`, `mass_loss`, `mass_void`: Unconditional probability masses summing to 1.0.
- `baseline_p`: `BASELINE_LEAGUE_V1` probability on the identical contract.
- `team_baseline_p`: `TB-1` probability on the identical contract.
- `status`: `FROZEN` or `NOT_ISSUED:<reason>`. Never a silent fallback number.

### 4.2 Settlement Row Schema (`SHADOW_SETTLEMENTS.csv`)

```csv
shadow_row_id,revision,parent_revision,effective_utc,result,observed_value,evidence_grade,source_url,field,retrieved_utc,reason
```

- `result`: `WIN`, `PUSH`, `LOSS`, `VOID`, or `UNRESOLVED`.
- `evidence_grade`: Official source grade (`GRADE_A` or `GRADE_B`).
- Revision tracking adheres strictly to `CURRENT_RULES.md` Â§8 (R17).

---

## 5. Promotion Governance

A shadow model is never promoted based on development backtests. Promotion follows the pre-registered two-stage design in `HYPOTHESIS_REGISTER.md` and `SCORING_AND_VALIDATION.md` Â§17:
1. **Stage 1 (Pilot):** Minimum 8 weeks and 40 events to estimate weekly variance $\text{SD}_w$.
2. **Stage 2 (Confirmatory):** Sized from Stage 1 variance; requires 95% confidence interval strictly below 0 against **both** `BASELINE_LEAGUE_V1` and `TEAM_BASELINE_P`.
3. **Owner Authorization:** Any promotion to `REFERENCE` or `ANCHOR` requires a separate user instruction under Prompt 8.
