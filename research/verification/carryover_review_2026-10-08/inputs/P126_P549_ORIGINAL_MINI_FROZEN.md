# Prediction Mini Running Log — P-551 onward

**LOCAL WORKING LOG — REFERENCE/FALLBACK — PENDING CANONICAL IMPORT**

Opened **2026-10-08 (Australia/Melbourne)**, under **LOCAL_MINI_STAGING**. GitHub `main` at the pinned HEAD is repository/methodology authority and is strictly **READ ONLY**. The active local P-550 log, separately preserved as prior local evidence, has one complete NHL card under **P-550**, not canonically committed and still unsettled. This new mini carries that unchanged P-550 card plus the GitHub-selected 65 current register records. The next unused local working identifier is **P-551**. No P-ID is consumed merely by opening this new mini.

**No settlement, score/result research, retrospective, grading, model or rule changes, canonical import, GitHub writes, or historical/local evidence deletion is performed.**

---

## A. Authority snapshot

- **Repository:** `danisgreat/Sports-Research`
- **Branch:** `main`
- **GitHub main HEAD SHA:** `68f890dca1691bfad83b93299063b75b40f36c2f`
- **Method:** `MDS-2026.10.01-v8.0`
- **Control revision:** `CR-2026.10.08-R2`
- **Scoring version:** `SCV-2026.10.01-v3`
- **Active control manifest:** `CONTROL_MANIFEST_2026-10-08-2.md`
- **Active manifest normalized-CRLF SHA-256:** `6db924b2e18c213f56e4dbfb64b64fe54193fad052e50fc4e3ebfee773e63b90`
- **Active Combined Log:** `prediction logs/PREDICTION_LOG_COMBINED_7.md`
- **Current settlement/carryover selector:** `research/current_settlement_register.json`
- **Selected carryover register:** `research/verification/mini_rollover_2026-10-08/carryover.json`
- **Selected carryover register SHA-256:** `0c3f0fdb057f9f23f926c9247bbb20416723ddd17f5ba3b344d7e3e9c5444ab3`
- **Highest committed repository P-ID:** `P-549`
- **REPOSITORY_NEXT_ID_SNAPSHOT:** `P-550`
- **Highest local working P-ID actually used before this new mini:** `P-550`
- **First working P-ID for this mini:** `P-551`
- **LOCAL_NEXT_WORKING_ID:** `P-551` — mini creation consumes no ID
- **Mode:** `LOCAL_MINI_STAGING`
- **Source firewall:** `SPORTS_ONLY / MARKET_BLIND`
- **PERFORMANCE_ELIGIBILITY:** `NOT_CERTIFIED`
- **CANONICAL_IMPORT_STATUS:** `PENDING`

### Fresh-read receipt

The CURRENT `main` authority was read at GitHub HEAD `68f890dca1691bfad83b93299063b75b40f36c2f`. The authority gate included:

- `METHOD.md`
- `CURRENT_RULES.md`
- `CARD_AND_LOG_TEMPLATES.md`
- `GAME_LOG_STATUS_CURRENT.md`
- `SCORING_AND_VALIDATION.md`
- `VERIFICATION_PROTOCOL.md`
- `research/README.md`
- `NUMERICAL_MODEL_REGISTER.md`
- `H0_DATASET_CARD.md`
- `DATA_SOURCE_REGISTER.md`
- active manifest `CONTROL_MANIFEST_2026-10-08-2.md`
- `research/canonical_ledger.jsonl`
- `research/current_settlement_register.json`
- selected carryover `research/verification/mini_rollover_2026-10-08/carryover.json`
- latest active combined log `prediction logs/PREDICTION_LOG_COMBINED_7.md`
- October 8 rollover evidence under `research/verification/mini_rollover_2026-10-08/`
- `research/verification/closure_2026-10-05/mini_archive_manifest.json`
- relevant archived/local mini evidence, including the settled P-538–P-549 cycle, the earlier empty P-550 mini, and the latest local P-550 working mini containing the NHL P-550 card.

### Authority reconciliation note

`METHOD.md`, `CURRENT_RULES.md` and the living status register now select **CR-2026.10.08-R2**. Combined Log 7’s immutable opening header records the earlier R1 rollover checkpoint; that historical header is not rewritten here.

GitHub has canonically imported P-538–P-549. GitHub's unconsumed repository next-ID remains **P-550**, but locally **P-550 has already been issued** for Edmonton @ Anaheim in the preceding local mini. That original local ID is preserved unchanged. The next local working ID is therefore **P-551**, and P-550 remains pending import/reconciliation. This is an intentional temporary divergence of working and canonical sequences, not a ledger commitment.

---

## B. Local ID and duplicate rules

- Mini creation consumes **no** P-ID.
- One genuinely new event uses one local working P-ID.
- The first available working ID is `P-551`.
- Working IDs advance only after a complete new card is successfully written and verified locally.
- Corrections and dated addenda retain the original P-ID.
- Duplicate events consume no ID.
- Tracking/temporary aliases consume no ID.
- Local working IDs remain stable once issued.
- GitHub being behind never rewinds a valid local sequence.
- GitHub advancing does not silently renumber an already-issued local card.
- Existing canonical P-001–P-549 and repository-reserved IDs are never reused.
- Event identity, native event ID, participants, league/tournament, date and tracking alias must be checked before each append.
- Final canonical import/reconciliation is a separately requested workflow.
- A local working ID must be labelled `LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT` until imported.

### Duplicate/event identity gate at rollover

- The earliest opening snapshot for P-550 contained **0 event cards**, but the **latest** preceding local P-550 mini contains **1 complete new NHL card**, P-550 for Edmonton Oilers @ Anaheim Ducks, with tracking alias `LOCAL-20261008-P-550-NHL-EDM-ANA` and official native ID `2026020055`. The former opening snapshot is superseded for local ID occupancy.
- **P-550 is already used locally**, despite remaining the repository next-ID snapshot. It is carried over exactly once; the next new event must use **P-551**.
- P-538–P-549 now exist canonically in GitHub and must never be reissued as new events.
- No unresolved mapping remains from the P-538–P-549 cycle. **P-550 has a pending local-to-canonical mapping** and is not double-counted as a separate reconciliation item.
- No duplicate event is created by this rollover.

---

## C. Active carryover

The CURRENT selected GitHub carryover register contains **65 exact records**. The immediately preceding local P-550 mini additionally contains one successfully written and verified, still-unsettled **P-550** event card. All 65 selected-register records retain their original descriptions and current statuses verbatim; the complete P-550 card is carried forward byte-for-byte under the local carryover heading. The **total active/reference carryover universe is 66 unique IDs**, of which P-550 remains LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT.

Classification for this local staging workflow:

- **ACTIVE SPORTING/CONTRACT CARRYOVER:** `34` (33 from current selected GitHub register + locally staged P-550)
- **CANONICAL-RECONCILIATION CARRYOVER:** `0`
- **CERTIFICATION-ONLY REFERENCE:** `32`
- **FULLY CLOSED in active queue:** `0`
- **Total retained current-register records:** `65`
- **Additional locally staged carryover:** `1` (P-550)
- **Total unique carryovers in new mini:** `66`

This classification is derived from the current selected register, not from the stale earlier P-550 mini. The earlier local mini classified 40 sporting/contract + 4 reconciliation + 21 reference records before GitHub completed the October 8 import and additional sporting reviews. Those stale classifications are not carried forward as current state.

**DO NOT SETTLE IN THIS WORKFLOW.**

### C1. ACTIVE SPORTING/CONTRACT CARRYOVER — 34 records (33 canonical-register + 1 local)

### P-126 — Sikkim Aakraman FC vs Sikkim Boys Club — SFA A Division S-League

- **P-ID/local ID:** `P-126`
- **Aliases:** `TMP-OPEN-20260909-03`
- **Sport/league:** SFA A Division S-League
- **Event:** Sikkim Aakraman FC vs Sikkim Boys Club — SFA A Division S-League
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_IDENTITY`
- **Unresolved contracts/fields:** Original exact contract field not authenticated | Current secondary schedule still has an unscored Aug 28 row. Prior 1–0 versus secondary 3–0 and Aug 28/29 conflict remain; SFA exact-event final and corners required. Sofa route now 403. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** Current secondary schedule still has an unscored Aug 28 row. Prior 1–0 versus secondary 3–0 and Aug 28/29 conflict remain; SFA exact-event final and corners required. Sofa route now 403. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:189`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-136 — James Duckworth vs Arthur Fery — ATP Winston-Salem Open 2026 Semifinal

- **P-ID/local ID:** `P-136`
- **Aliases:** —
- **Sport/league:** ATP Winston-Salem Open semifinal
- **Event:** James Duckworth vs Arthur Fery — ATP Winston-Salem Open 2026 Semifinal
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_OPERATOR`
- **Unresolved contracts/fields:** Over 22.5 total games; Duckworth +1.5 games; Fery -1.5 games; Under 22.5 total games | Recovered original continuation says Arthur Fery advanced after James Duckworth retired. All four total/game-handicap contracts froze UNKNOWN_DEFINITION retirement rules. Parent FINAL/SETTLED is incomplete at contract level. Require original ticket/operator retirement/action terms; no arbitrary VOID or numeric Brier.
- **Remaining requirement:** Recovered original continuation says Arthur Fery advanced after James Duckworth retired. All four total/game-handicap contracts froze UNKNOWN_DEFINITION retirement rules. Parent FINAL/SETTLED is incomplete at contract level. Require original ticket/operator retirement/action terms; no arbitrary VOID or numeric Brier.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:199`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-148 — Toluca Femenil v León Femenil

- **P-ID/local ID:** `P-148`
- **Aliases:** `TMP-OPEN-20260909-04`
- **Sport/league:** Liga MX Femenil Apertura
- **Event:** Toluca Femenil v León Femenil
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** Toluca team corners Over 4.5 | Toluca official report supports 1–0 but is not an aggregate-corner record. Prior Toluca 2 / ordering 2–6 versus 6–2 is unresolved; provisional LOSS only. Raw local P-147 maps to canonical P-148. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** Toluca official report supports 1–0 but is not an aggregate-corner record. Prior Toluca 2 / ordering 2–6 versus 6–2 is unresolved; provisional LOSS only. Raw local P-147 maps to canonical P-148. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:211`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-149 — Colorado Rapids 2 v Ventura County

- **P-ID/local ID:** `P-149`
- **Aliases:** `TMP-OPEN-20260909-05`
- **Sport/league:** MLS NEXT Pro
- **Event:** Colorado Rapids 2 v Ventura County
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** Club-origin release supports Ventura 3–2, but has no aggregate corners; its syndicated copy is not an independent lineage. Prior research WIN remains provisional. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** Club-origin release supports Ventura 3–2, but has no aggregate corners; its syndicated copy is not an independent lineage. Prior research WIN remains provisional. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:212`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-166 — Melbourne Mustangs vs Canberra Brave — AIHL Goodall Cup Semifinal

- **P-ID/local ID:** `P-166`
- **Aliases:** —
- **Sport/league:** AIHL Goodall Cup semifinal
- **Event:** Melbourne Mustangs vs Canberra Brave — AIHL Goodall Cup Semifinal
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_OPERATOR`
- **Unresolved contracts/fields:** Melbourne +1.5; Over 7.5 goals; Under 7.5 goals; Canberra -1.5 | Regulation 4–4, final 5–4 after overtime, inherited sporting grades retained. Ticket/definition specifying overtime treatment NOT_RETRIEVED; no sporting-result search can reconstruct it. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** Regulation 4–4, final 5–4 after overtime, inherited sporting grades retained. Ticket/definition specifying overtime treatment NOT_RETRIEVED; no sporting-result search can reconstruct it. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:229`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-176 — Amiens SC vs FC Versailles — France Ligue 3

- **P-ID/local ID:** `P-176`
- **Aliases:** `TMP-OPEN-20260909-06`
- **Sport/league:** France Ligue 3
- **Event:** Amiens SC vs FC Versailles — France Ligue 3
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** Amiens Team Under 1.5; Under 2.5 Goals; Versailles ML; 1st Half Over 0.5; Total match corners Under 10.5 | Secondary final 3–0 and corner commentary do not prove a complete aggregate. Prior 8 = 5+3 research WIN retained; FFF exact match-stat sheet required. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** Secondary final 3–0 and corner commentary do not prove a complete aggregate. Prior 8 = 5+3 research WIN retained; FFF exact match-stat sheet required. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:239`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-178 — AS Cannes vs Le Puy-en-Velay — France Ligue 3

- **P-ID/local ID:** `P-178`
- **Aliases:** `TMP-OPEN-20260909-07`
- **Sport/league:** France Ligue 3
- **Event:** AS Cannes vs Le Puy-en-Velay — France Ligue 3
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** Under 2.5 Goals; Cannes Team Under 1.5; 1st Half Over 0.5; BTTS — No | L’Équipe exact-event route 403, FFF 403. Prior 16 = 8+8 research LOSS retained; no new official aggregate. Competition is Ligue 3, not silently relabelled National 2. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** L’Équipe exact-event route 403, FFF 403. Prior 16 = 8+8 research LOSS retained; no new official aggregate. Competition is Ligue 3, not silently relabelled National 2. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:241`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-179 — Thionville Lusitanos vs Paris 13 Atletico — France Ligue 3

- **P-ID/local ID:** `P-179`
- **Aliases:** `TMP-OPEN-20260909-08`
- **Sport/league:** France Ligue 3
- **Event:** Thionville Lusitanos vs Paris 13 Atletico — France Ligue 3
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** Thionville Team Over 0.5; 1st Half Over 0.5; Paris 13 Team Under 1.5; Under 2.5 Goals; Under 10.5 Corners | Exact-event secondary route 403 and FFF 403. Prior 9 = 8+1 research WIN retained. The two penalty goals in the 1–1 result are not a shootout. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** Exact-event secondary route 403 and FFF 403. Prior 9 = 8+1 research WIN retained. The two penalty goals in the 1–1 result are not a shootout. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:242`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-200 — Herning Blue Fox vs Rungsted Seier Capital — Danish Metal Ligaen

- **P-ID/local ID:** `P-200`
- **Aliases:** —
- **Sport/league:** Danish Metal Ligaen
- **Event:** Herning Blue Fox vs Rungsted Seier Capital — Danish Metal Ligaen
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_OPERATOR`
- **Unresolved contracts/fields:** Original exact contract field not authenticated | Regulation 3–3 and final 4–3 OT change the endpoint of total 6.5. Sporting facts retained; actual ticket/house definition missing. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** Regulation 3–3 and final 4–3 OT change the endpoint of total 6.5. Sporting facts retained; actual ticket/house definition missing. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:263`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-217 — Trinbago Knight Riders vs Guyana Amazon Warriors — CPL

- **P-ID/local ID:** `P-217`
- **Aliases:** —
- **Sport/league:** Caribbean Premier League
- **Event:** Trinbago Knight Riders vs Guyana Amazon Warriors — CPL
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_OPERATOR`
- **Unresolved contracts/fields:** GAW 20-over Under 174.5; GAW after 6 Over 46.5; GAW after 6 Under 46.5; GAW 20-over Over 174.5 | Inherited 16-over 185/5 versus 172/7, Guyana by 9 runs DLS. Total 174.5 research O WIN/U LOSS; six completed overs 31/2 versus mandatory powerplay 4.5 overs 24/2 are different contracts. Ticket/action definition missing. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** Inherited 16-over 185/5 versus 172/7, Guyana by 9 runs DLS. Total 174.5 research O WIN/U LOSS; six completed overs 31/2 versus mandatory powerplay 4.5 overs 24/2 are different contracts. Ticket/action definition missing. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:280`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-233 — Beijing Guoan vs Lanzhou Longyuan Athletic — China FA Cup 2026 (quarterfinal, corrected)

- **P-ID/local ID:** `P-233`
- **Aliases:** `TMP-OPEN-20260909-09`
- **Sport/league:** China FA Cup quarterfinal
- **Event:** Beijing Guoan vs Lanzhou Longyuan Athletic — China FA Cup 2026 (quarterfinal, corrected)
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** Beijing team goals Over 1.5; 1st-half Over 0.5 goals; Total goals Over 2.5; BTTS — No; Corners Over 8.5 | CFA landing page is not a match sheet; original Xinhua report supplies terminal corroboration only. Prior 13-corner research WIN retained; quarterfinal, not Round of 16. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** CFA landing page is not a match sheet; original Xinhua report supplies terminal corroboration only. Prior 13-corner research WIN retained; quarterfinal, not Round of 16. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:296`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-234 — Dalian Yingbo vs Shanghai Shenhua — China FA Cup 2026 (quarterfinal, corrected)

- **P-ID/local ID:** `P-234`
- **Aliases:** `TMP-OPEN-20260909-10`
- **Sport/league:** China FA Cup quarterfinal
- **Event:** Dalian Yingbo vs Shanghai Shenhua — China FA Cup 2026 (quarterfinal, corrected)
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** 1st-half Over 0.5 goals; Dalian team goals Over 0.5; Corners Over 8.5; BTTS — Yes; Total goals Over 2.5 | Titan exact route retrieval miss; original Xinhua says Dalian 1–0, no corner aggregate. Prior 10-corner WIN provisional; keeper red-card disruption must not be mistaken for a pregame input. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** Titan exact route retrieval miss; original Xinhua says Dalian 1–0, no corner aggregate. Prior 10-corner WIN provisional; keeper red-card disruption must not be mistaken for a pregame input. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:297`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-235 — Shandong Taishan vs Shanghai Port — China FA Cup 2026 (quarterfinal, corrected)

- **P-ID/local ID:** `P-235`
- **Aliases:** `TMP-OPEN-20260909-11`
- **Sport/league:** China FA Cup quarterfinal
- **Event:** Shandong Taishan vs Shanghai Port — China FA Cup 2026 (quarterfinal, corrected)
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** 1st-half Over 0.5 goals; Shanghai Port team goals Over 0.5; BTTS — Yes; Total goals Over 2.5; Corners Over 8.5 | CFA landing page lacks target statistics. Xinhua terminal report supports Port 3–0; prior 14-corner WIN is provisional, not revalidated. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** CFA landing page lacks target statistics. Xinhua terminal report supports Port 3–0; prior 14-corner WIN is provisional, not revalidated. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:298`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-250 — Yunnan Yukun vs Chongqing Tonglianglong

- **P-ID/local ID:** `P-250`
- **Aliases:** `TMP-AUDIT-20260912-01`
- **Sport/league:** China FA Cup
- **Event:** Yunnan Yukun vs Chongqing Tonglianglong
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** 1H Over 0.5; Full Over 2.5; Full Under 2.5; 1H Under 0.5 | China FA Cup field-owner/data-partner aggregate still missing. No inferred grade; historical ESPN noncoverage does not establish that the match was cancelled. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** China FA Cup field-owner/data-partner aggregate still missing. No inferred grade; historical ESPN noncoverage does not establish that the match was cancelled. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:313`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-251 — Sassuolo vs Frosinone

- **P-ID/local ID:** `P-251`
- **Aliases:** `TMP-AUDIT-20260912-02`
- **Sport/league:** Coppa Italia
- **Event:** Sassuolo vs Frosinone
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** 1H Over 0.5; Full Over 2.5; Corners Over 8.5; Full Under 2.5; 1H Under 0.5 | ESPN 401911806 final after penalties, 1–1, corners 6+5=11: research WIN. Lega / reconciled issued provider still required; no substitution of the unregistered feed. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** ESPN 401911806 final after penalties, 1–1, corners 6+5=11: research WIN. Lega / reconciled issued provider still required; no substitution of the unregistered feed. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:314`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-255 — Inter Women vs VfL Wolfsburg Women

- **P-ID/local ID:** `P-255`
- **Aliases:** `TMP-AUDIT-20260912-03`
- **Sport/league:** UEFA Women Champions League
- **Event:** Inter Women vs VfL Wolfsburg Women
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_PERIOD`
- **Unresolved contracts/fields:** 1H Over 0.5; Full Over 2.5; Full Under 2.5; 1H Under 0.5 | UEFA 2049369 FINISHED: regulation 2–0, whole match 3–1, penalties 5–4. Whole-match corners 12+12=24 include extra time. No 90-minute split or defensible bound; old bounded WIN stays withdrawn. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** UEFA 2049369 FINISHED: regulation 2–0, whole match 3–1, penalties 5–4. Whole-match corners 12+12=24 include extra time. No 90-minute split or defensible bound; old bounded WIN stays withdrawn. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:318`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-256 — Paris Saint-Germain Women vs Eintracht Frankfurt Women

- **P-ID/local ID:** `P-256`
- **Aliases:** `TMP-AUDIT-20260912-04`
- **Sport/league:** UEFA Women Champions League
- **Event:** Paris Saint-Germain Women vs Eintracht Frankfurt Women
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_PERIOD`
- **Unresolved contracts/fields:** 1H Over 0.5; Full Under 2.5; Full Over 2.5; 1H Under 0.5 | UEFA 2049367 FINISHED: regulation 1–1, whole match 5–1. Whole-match corners 11+4=15 include extra time. No regulation split or justified bound; old bounded WIN stays withdrawn. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** UEFA 2049367 FINISHED: regulation 1–1, whole match 5–1. Whole-match corners 11+4=15 include extra time. No regulation split or justified bound; old bounded WIN stays withdrawn. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:319`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-265 — Toluca vs Club León

- **P-ID/local ID:** `P-265`
- **Aliases:** `TMP-AUDIT-20260912-05`
- **Sport/league:** Leagues Cup
- **Event:** Toluca vs Club León
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** Corners Over 8.5; Full Over 2.5; First-half Over 0.5; Full Under 2.5; first-half Under 0.5 | ESPN 401914297 final 2–0, corners 4+5=9: research WIN at the first winning integer. Leagues Cup exact field-owner aggregate required; particularly sensitive to one-corner definition changes. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** ESPN 401914297 final 2–0, corners 4+5=9: research WIN at the first winning integer. Leagues Cup exact field-owner aggregate required; particularly sensitive to one-corner definition changes. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:328`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-274 — San Francisco Giants @ Pittsburgh Pirates

- **P-ID/local ID:** `P-274`
- **Aliases:** —
- **Sport/league:** MLB
- **Event:** San Francisco Giants @ Pittsburgh Pirates
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_OPERATOR`
- **Unresolved contracts/fields:** Giants +1.5; Pirates ML; Over 9.0 runs; Under 9.0 runs | Inherited Pirates 5–2, actual starter Bachar versus listed Jared Jones. Actual ticket / listed-pitcher action or void terms missing; no invented operator settlement. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** Inherited Pirates 5–2, actual starter Bachar versus listed Jared Jones. Actual ticket / listed-pitcher action or void terms missing; no invented operator settlement. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:337`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-341 — BUL FC vs Ntugasaze FC — Uganda Premier League R3

- **P-ID/local ID:** `P-341`
- **Aliases:** `TMP-OPEN-20260909-01`
- **Sport/league:** Uganda Premier League
- **Event:** BUL FC vs Ntugasaze FC — Uganda Premier League R3
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** 1H Over 0.5; Under 2.5; Over 2.5; 1H Under 0.5 | ESPN uga.1 still returns season 2025 / 2025–26 with zero events for Sep 8. UNSETTLEABLE to frozen standard retained; empty/stale response is not proof of cancellation or zero corners. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** ESPN uga.1 still returns season 2025 / 2025–26 with zero events for Sep 8. UNSETTLEABLE to frozen standard retained; empty/stale response is not proof of cancellation or zero corners. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:404`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-342 — MŠK Novohrad Lučenec vs KFC Komárno — Slovnaft Cup R3

- **P-ID/local ID:** `P-342`
- **Aliases:** `TMP-OPEN-20260909-02`
- **Sport/league:** Slovnaft Cup
- **Event:** MŠK Novohrad Lučenec vs KFC Komárno — Slovnaft Cup R3
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** 1H Over 0.5; Over 2.5; Under 2.5; 1H Under 0.5 | Slovak owner route not recovered as a target statistics record. Prior 16-corner research WIN retained; require exact Slovnaft Cup owner record. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** Slovak owner route not recovered as a target statistics record. Prior 16-corner research WIN retained; require exact Slovnaft Cup owner record. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:405`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-368 — Al Jazira v Al Nasr — UAE Pro League

- **P-ID/local ID:** `P-368`
- **Aliases:** `TMP-OPEN-20260911-01`
- **Sport/league:** UAE Pro League
- **Event:** Al Jazira v Al Nasr — UAE Pro League
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** 1st-half Over 0.5; Total corners Over 7.5 (no frozen provider); Over 2.5 goals; Under 2.5 goals; 1st-half Under 0.5 | UAE fixture shell reached, no target aggregate verified. Prior 9-corner research WIN; no frozen provider and secondary independence unverified. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** UAE fixture shell reached, no target aggregate verified. Prior 9-corner research WIN; no frozen provider and secondary independence unverified. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:431`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-369 — Dubai United v Shabab Al Ahli — UAE Pro League

- **P-ID/local ID:** `P-369`
- **Aliases:** `TMP-OPEN-20260911-02`
- **Sport/league:** UAE Pro League; retained competition label requires exact identity confirmation
- **Event:** Dubai United v Shabab Al Ahli — UAE Pro League
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** Total corners Under 10.5 (no frozen provider); 1st-half Over 0.5; Over 2.5 goals; Under 2.5 goals; 1st-half Under 0.5 | UAE shell reached, no exact target aggregate. Prior 11-corner research LOSS retained; missing frozen provider remains a distinct gate. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** UAE shell reached, no exact target aggregate. Prior 11-corner research LOSS retained; missing frozen provider remains a distinct gate. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:432`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-377 — Xelajú MC vs Cobán Imperial — Guatemala Liga Nacional Apertura 2026

- **P-ID/local ID:** `P-377`
- **Aliases:** `TMP-OPEN-20260912-01`
- **Sport/league:** Guatemala Liga Nacional Apertura
- **Event:** Xelajú MC vs Cobán Imperial — Guatemala Liga Nacional Apertura 2026
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** 1H Over 0.5 goals; Over 8.5 total corners; Over 2.5 total goals; Under 2.5 total goals; 1H Under 0.5 goals | League landing route returns a tiny shell, not a match-stat record. Prior secondary 7 research LOSS retained; ESPN historical summary lacks aggregate statistics. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** League landing route returns a tiny shell, not a match-stat record. Prior secondary 7 research LOSS retained; ESPN historical summary lacks aggregate statistics. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:440`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-399 — Genoa vs Frosinone — Serie A

- **P-ID/local ID:** `P-399`
- **Aliases:** `TMP-OPEN-20260914-01`
- **Sport/league:** Serie A
- **Event:** Genoa vs Frosinone — Serie A
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** 1H Over 0.5; Combined corners Over 8.5; FT Under 2.5; FT Over 2.5; 1H Under 0.5 | ESPN 401874991 final 1–1, corners 8+9=17: research WIN. Lega exact field-owner record still missing; do not treat its landing-page redirect as success. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** ESPN 401874991 final 1–1, corners 8+9=17: research WIN. Lega exact field-owner record still missing; do not treat its landing-page redirect as success. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:462`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-401 — IFK Göteborg vs Halmstads BK — Allsvenskan

- **P-ID/local ID:** `P-401`
- **Aliases:** `TMP-OPEN-20260914-02`, `TMP-OPEN-20260914-03`
- **Sport/league:** Allsvenskan
- **Event:** IFK Göteborg vs Halmstads BK — Allsvenskan
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** Combined corners Over 8.5; Halmstad team total Under 1.5; IFK team corners Over 4.5; 1H Under 0.5; FT Over 2.5 | ESPN 401874088 final 2–1, Sep 12 15:30 UTC, corners 8+9=17: research WIN. Sep 13 search missed the event; flag date correction, retain original card. Allsvenskan owner route not recovered. | Same owner gap, ESPN IFK 8: research WIN. This is one event with two open derivative handles, not two independent trials. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** ESPN 401874088 final 2–1, Sep 12 15:30 UTC, corners 8+9=17: research WIN. Sep 13 search missed the event; flag date correction, retain original card. Allsvenskan owner route not recovered. | Same owner gap, ESPN IFK 8: research WIN. This is one event with two open derivative handles, not two independent trials. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:464`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-409 — Lille OSC vs ESTAC Troyes — French Ligue 1

- **P-ID/local ID:** `P-409`
- **Aliases:** `TMP-OPEN-20260915-02`
- **Sport/league:** France Ligue 1
- **Event:** Lille OSC vs ESTAC Troyes — French Ligue 1
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** Lille team goals Over 0.5; Lille or Draw (90 min); 1st Half total goals Over 0.5; Full match total goals Under 3.5 | ESPN 401876462 final Lille 2–0, Troyes corners 5: research WIN. LFP live/306887 empty to HTTP and rendered UI (video error, no aggregate); owner still missing. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** ESPN 401876462 final Lille 2–0, Troyes corners 5: research WIN. LFP live/306887 empty to HTTP and rendered UI (video error, no aggregate); owner still missing. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:472`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-418 — Drukpa FC vs Royal Thimphu College (RTC) FC — Bhutan Premier League

- **P-ID/local ID:** `P-418`
- **Aliases:** `TMP-OPEN-20260915-04`
- **Sport/league:** Bhutan Premier League
- **Event:** Drukpa FC vs Royal Thimphu College (RTC) FC — Bhutan Premier League
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** Original exact contract field not authenticated | RSSSF updated Sep 25 now reports Sep 14 Drukpa 1–3 RTC. This is progress from its unscored prior row, not official settlement. BFF current page is stale; 12:00/13:00 UTC conflict remains. June 13 1–1 and July 17 BBS report are wrong events. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** RSSSF updated Sep 25 now reports Sep 14 Drukpa 1–3 RTC. This is progress from its unscored prior row, not official settlement. BFF current page is stale; 12:00/13:00 UTC conflict remains. June 13 1–1 and July 17 BBS report are wrong events. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:481`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-419 — Djurgårdens IF vs GAIS — Sweden Allsvenskan

- **P-ID/local ID:** `P-419`
- **Aliases:** `TMP-OPEN-20260915-05`
- **Sport/league:** Allsvenskan
- **Event:** Djurgårdens IF vs GAIS — Sweden Allsvenskan
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** Djurgården team goals Over 0.5; Djurgården or Draw (1X); GAIS team goals Under 1.5; Under 3.5 total goals | ESPN 401873992 final 2–0, corners 2+2=4: research LOSS. Three red cards recorded at 59, 86 and 90+10. Allsvenskan field-owner aggregate not reached; no retroactive coefficient from the disruption. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** ESPN 401873992 final 2–0, corners 2+2=4: research LOSS. Three red cards recorded at 59, 86 and 90+10. Allsvenskan field-owner aggregate not reached; no retroactive coefficient from the disruption. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:482`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-430 — Al Ain FC vs Al Nassr — AFC Champions League Elite MD1

- **P-ID/local ID:** `P-430`
- **Aliases:** `TMP-OPEN-20260917-01`
- **Sport/league:** AFC Champions League Elite
- **Event:** Al Ain FC vs Al Nassr — AFC Champions League Elite MD1
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNRESOLVED_TARGET_FIELD_OR_PROVIDER`
- **Unresolved contracts/fields:** Al Nassr team total Over 0.5; Match Over 1.5; 1st Half Over 0.5; Al Nassr +0.5 / X2 | ESPN 401912656 final Al Ain 4–0, corners 2–10: research LOSS. Frozen AFC owner record does not supply corners; ESPN not pre-registered. Need AFC field or explicit approved-provider reconciliation; no automatic fallback booking. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Remaining requirement:** ESPN 401912656 final Al Ain 4–0, corners 2–10: research LOSS. Frozen AFC owner record does not supply corners; ESPN not pre-registered. Need AFC field or explicit approved-provider reconciliation; no automatic fallback booking. A certified issue core and issue-time source receipts are not recovered. Actual-start semantics and three independently audited agreeing terminal collections are not certified. Historical eligibility remains false.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`; `GAME_LOG_STATUS_CURRENT.md:493`; `research/verification/settlement_2026-10-01/REPORT.md`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-523 — Oriente Petrolero vs The Strongest — retained October 1 card

- **P-ID/local ID:** `P-523`
- **Aliases:** —
- **Sport/league:** BoliviaCopa
- **Event:** Oriente Petrolero vs The Strongest — retained October 1 card
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `EXISTING_HISTORICAL_AUDIT_NOT_CERTIFIED; corners UNRESOLVED_LINE`
- **Unresolved contracts/fields:** 1H Over 0.5 goals | 90m Under 2.5 goals | 90m Over 2.5 goals | 1H Under 0.5 goals | Corners: undefined threshold
- **Remaining requirement:** Existing October-1 diagnostic goal review is retained; undefined corner threshold cannot be graded. Original operator rules, actual-start/issue-time conflict and independently audited terminal quorum remain missing; preserve W/W/L/L goal diagnostics as conditional only.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-537 — Kyrgyzstan vs Lebanon (International Friendly, FIFA Window)

- **P-ID/local ID:** `P-537`
- **Aliases:** —
- **Sport/league:** International Friendly
- **Event:** Kyrgyzstan vs Lebanon (International Friendly, FIFA Window)
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `PARTIALLY_DIAGNOSTICALLY_SETTLED_PERIOD_AND_PROVIDER_OPEN`
- **Unresolved contracts/fields:** 1H Over 0.5 goals | Full match Over 2.5 | Lebanon win (unsupported alternative) | Corners Over 9.5 (also called unranked alternative) | Kyrgyzstan +0.5 (unsupported alternative)
- **Remaining requirement:** First-half field remains contradictory: fresh Sport.kg detailed narrative supports goals 19 and 31 (2–0), but original ESPN display 0–0 disagrees and fresh KFU pages are still pregame. Owner period/timeline, exact corners aggregate for Over 9.5, original operator definitions and audited independent terminal quorum required. Do not certify either conflicting halftime solely from a final 3–1.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-540 — Adrian Mannarino vs Nikoloz Basilashvili

- **P-ID/local ID:** `P-540`
- **Aliases:** —
- **Sport/league:** ATP Shanghai
- **Event:** Adrian Mannarino vs Nikoloz Basilashvili
- **Original state:** NOT RESTATED IN CURRENT SELECTED CARRYOVER REGISTER — preserve original canonical/source record; no inference made.
- **Current state:** `UNKNOWN_DEFINITION_RETIREMENT`
- **Unresolved contracts/fields:** Four ranked retirement-dependent contracts need original operator action terms.
- **Remaining requirement:** Retain exact original issue-time/operator terms and complete admitted source/actual-start/independence evidence. Do not backfill or certify historical uncalibrated scenarios.
- **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_6.md`
- **Source/reference pointer:** `research/verification/mini_rollover_2026-10-08/carryover.json`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

### P-550 — Edmonton Oilers @ Anaheim Ducks — NHL 2026-27 — LOCAL SPORTING/CONTRACT CARRYOVER

- **P-ID/local ID:** `P-550` — `LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`
- **Aliases:** `LOCAL-20261008-P-550-NHL-EDM-ANA`
- **Native event ID:** `2026020055`
- **Sport/league:** Ice hockey / NHL regular season 2026-27
- **Event:** Edmonton Oilers @ Anaheim Ducks — 2026-10-07 Anaheim-local / 2026-10-08 AEDT
- **Original state:** `LATE_START_UNVERIFIED`; `LOCALLY_STAGED_UNSETTLED`; original working card not certified as pregame
- **Current state:** `LOCALLY_STAGED_UNSETTLED`; `CANONICAL_IMPORT_STATUS: PENDING`; unchanged; no result lookup or settlement in this workflow
- **Unresolved contracts/fields:** `Oilers ML`; `Ducks +1.5`; `TOTAL GOALS OVER 6.5`; `TOTAL GOALS UNDER 7.5` — full-game endpoint including OT/shootout; operator-specific rules not supplied
- **Remaining requirement:** Retain original issue-time/card evidence; separately verify exact native identity, final result and contract/period definitions in an explicitly authorised settlement; reconcile P-550 local ID to canonical ledger without reissuing a second event or renumbering the local ID; preserve original warm-up/start and evidence gaps
- **Canonical pointer:** `NONE — P-550 local only; GitHub main currently committed through P-549`
- **Source/reference pointer:** previously issued local `PREDICTION_MINI_RUNNING_LOG_P-550_ONWARD(2).md`, original complete P-550 card; source bytes SHA-256 `d38771e7c145365188841aca30a76cec86219d226dcdb9e0a3ec7bd8c3d4b0cd`
- **Task lock:** **DO NOT SETTLE IN THIS WORKFLOW.**

#### Complete original P-550 locally issued card (verbatim preserved)

## P-550 — ICE HOCKEY / NHL — Edmonton Oilers @ Anaheim Ducks — 2026-10-07 (Anaheim)

**LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT**  
**EVENT_KEY:** `NHL:2026-27:2026020055:2026-10-07`  
**TRACKING_ALIAS:** `LOCAL-20261008-P-550-NHL-EDM-ANA`  
**MODE:** `LOCAL_MINI_STAGING` · **SPORTS_ONLY / MARKET_BLIND**  
**PERFORMANCE_ELIGIBILITY:** `NOT_CERTIFIED` · **CANONICAL_IMPORT_STATUS:** `PENDING`

### A. Identity, clock and analysis state

- **League and season:** NHL, 2026-27 regular season. **Away:** Edmonton Oilers. **Home:** Anaheim Ducks.
- **Official native event ID:** `2026020055` (`https://www.nhl.com/gamecenter/edm-vs-ana/2026/10/07/2026020055`).
- **Venue:** Honda Center, Anaheim, California.
- **Published schedule:** Wednesday 7 October 2026 at 7:00 pm PDT = Thursday 8 October at **1:00 pm AEDT** = **12:00 pm AEST**. The supplied `8 October 2026, 1:07 pm AEST` does not match the official scheduled clock.
- **Research completion / working-card write:** `2026-10-08T13:11:54+11:00` (AEDT, local-clock timestamp); the scheduled start was already in the past when research began.
- **Event state at card time:** `LATE_START_UNVERIFIED` — the actual first puck drop or live game state was NOT independently certified. **This is not a pregame-certified issue.**
- **Evidence cutoff:** only source information demonstrably about the teams **before the scheduled puck drop** (published team/league previews, morning reports and prior-game statistics). No goals, events, saves, shifts, penalty outcomes or play-by-play from this matchup were used.
- **Endpoint:** one completed NHL full game, **including regulation + overtime + shootout**; NHL shootout decision carries one final-score goal. The original operator's settlement terms, if any, were not supplied. These are analyst-defined sporting propositions, **not assertions about unknown operator action/void terms**.
- **Scope lock:** no score lookup, settlement, grading or retrospective for this event.

### B. Current repo authority and ID custody

- `main` HEAD: `68f890dca1691bfad83b93299063b75b40f36c2f`
- Method/control/scoring: `MDS-2026.10.01-v8.0 / CR-2026.10.08-R2 / SCV-2026.10.01-v3`
- Active freeze: `CONTROL_MANIFEST_2026-10-08-2.md`, normalized-CRLF SHA-256 `6db924b2e18c213f56e4dbfb64b64fe54193fad052e50fc4e3ebfee773e63b90`.
- Current sport rules: `RULES_NHL.md`, `RULES_ICE_HOCKEY.md` §0, under current `CURRENT_RULES.md`.
- Repo current next-ID snapshot before locally appending: `P-550`; latest committed research ID: `P-549`; `research/canonical_ledger.jsonl` contained no `P-550` commitment at last read.
- P-550 was unused in the previously opened local P-550 mini, which contained zero new cards. **P-550 is reserved here as a local working ID, not ledger-committed.** A separate explicitly authorised canonical import is required.

### C. Supplied contracts verbatim and analyst endpoint

1. `Oilers ML`: Edmonton wins the **completed game including OT/SO**. On the sporting endpoint, no draw remains.
2. `Ducks +1.5`: Anaheim final-goal margin +1.5, **including OT/SO**; Anaheim wins or loses by exactly one goal to cover. A two-plus-goal Edmonton final victory fails.
3. `TOTAL GOALS OVER 6.5`: at least **7 final-score goals**, including OT/SO score additions under the NHL scoring convention.
4. `TOTAL GOALS UNDER 7.5`: at most **7 final-score goals**, including OT/SO score additions.

**Important contract geometry:** Over 6.5 and Under 7.5 are **not complementary**: both win at exactly 7 goals. Their correlation and any same-game combination must not be counted as independent trials. There is no operator-specific settlement certification.

### D. Confirmed/probable roster and goalie availability — pregame reports only

**Goaltenders:**

- **EDM Devon Levi — reported/announced intended starter, no warm-up readback.** Coach Mike Babcock said he would start against Anaheim; independent goalie reporters reproduced that designation. Levi started Edmonton's preceding two games, stopping 15/22 in the 9-7 Vancouver game and 19/20 in the 3-1 Seattle game. The first two starts combined for 34/42 saves (`.810` SV%, 8 GA on 42 shots). NHL.com reports 52 AHL appearances in 2025-26 at `.904` SV%. The tiny current NHL sample is NOT a stable quality estimate. **Backup Tristan Jarry**, latest prior appearance the 6-5 OT loss to Vancouver (.739 in a single start). **Frederik Andersen injured** and unavailable. There is material Edmonton goaltending downside, with no assumption that either two-start SV% will persist.
- **ANA Lukas Dostal — coach/beat-reporter confirmed for the intended start, no warm-up readback.** Entered 2-0-0 with a `.918` save percentage and 2.42 GAA after starting both Anaheim games (27 saves vs Vegas; 29 vs Florida). This is a two-game observation, not a proven revised ability level. **Backup Ville Husso** had no 2026-27 start at the snapshot; historical 2025-26 backup form `.884` SV% over 19 starts (secondary archive statistics). A switch or in-game pull would materially alter goal tails.
- **Goalie uncertainty handling:** both starters were named in pregame team/coach or beat-source reports, meeting a provisional line-up research gate; **actual starting warm-up was not checked and cannot be certified after scheduled start**. The scenario reflects the reported Levi–Dostal pairing; large goalie-driven sensitivity is shown below. Neither goalie is represented as guaranteed to have actually played.

**Edmonton forwards (projected):** Podkolzin–McDavid–Draisaitl; Frederic–Dickinson–Kapanen; Jones–Samanski–Howard; Formenton–Michaels–Joseph. **Defence:** Ekholm–Bouchard; Shea–Murphy; Walman–Emberson. Team confirmed Dickinson activated from IR to make season debut, helping second-line defensive coverage and the penalty kill; Colton Dach moved to IR. The updated NHL.com projection includes Samanski for Dach. Reported scratched: Mukhamadullin and Hallander. Missing: Hyman, Nugent-Hopkins, Janmark, Matthew Savoie, Andersen, Regula, Dach. **Actual warm-up unit composition unverified.**

**Anaheim forwards (projected):** Greer–Carlsson–Gauthier; Sennecke–Granlund–Killorn; Nesterenko–Poehling–Klepov; Malott–Washe–Caulfield. **Defence:** LaCombe–Luneau; Mintyukov–Mitchell; Hinds–Warren. Scratched: Jensen, Vatrano and Colangelo. Injured: Terry (hip), Helleson and Moore (lower-body). NHL.com reporting says expected lines; no actual in-game shift composition was used.

### E. Hockey-specific pregame process assessment

1. **5v5 shot/chance quality:** Edmonton's McDavid–Draisaitl combination and Bouchard transition/power-play contribution give it the higher offensive ceiling, but injuries reduce proven forward depth. The historical 2025-26 Edmonton 5v5 descriptive sample had **50.9% Corsi share and 52.1% high-danger-chance share** (historical table, not a current-matchup forecast). An external pregame 2026-27 five-on-five high-danger sample with an audited consistent provider/definition was **not independently retained**, so it is not converted into a numeric edge. Puckalytics independently lists Edmonton 2025-26 **2.76 xGF/60 at 5v5** and, through three 2026-27 matches, **3.08 xGF/60 at 5v5**; it also reports 2026-27 five-on-five shooting **17.19% against an xG-based 10.80%**. Those three-game shooting and xG rates are descriptive exposure/quality clues, not independently audited current-matchup forecast parameters. Raw SOG volume is not interpreted as goals without quality/goalie conversion.
2. **Finishing/save regression:** Edmonton scored 17 goals in its first three (5, 9, 3), far above a sustainable fixed-rate assumption; Anaheim scored 7 in two (4, 3). The Edmonton 9-goal game cannot be multiplied into a forecast. Likewise a `.810` two-game Levi save percentage and `.918` two-game Dostal number should be shrunk toward a broader skill uncertainty distribution; exact regression coefficients are **not fitted**.
3. **Special teams/discipline:** NHL official pregame team figures show EDM PP 25%, PK 57.1%; ANA PP 50%, PK 85.7%. Anaheim's three power-play goals against Florida (two in regulation and OT winner) illustrate upside; its early PP% rests on very few opportunities. Edmonton regains Dickinson's PK role, reducing but not eliminating the vulnerability. Penalty draw and call rates are not known well enough to assert exact special-team chances for this game.
4. **Defensive pairs:** Ekholm–Bouchard provides Edmonton a high-event puck-moving top pairing; LaCombe–Luneau takes substantial Anaheim minutes. Each club has young/depth pairs with breakout or coverage risk. Specific matchup-induced changes to high-danger rate are **not established**.
5. **Rest/travel/home:** EDM last played Oct 3 against Seattle and had **three rest days** before visiting Anaheim; ANA last played Oct 4 versus Florida, with **two rest days**. Neither was on a back-to-back. Edmonton travels to Southern California; Anaheim has home ice. No unverified fatigue multiplier is applied.
6. **Score effects/empty net:** A one-goal Edmonton lead may turn into a two-goal final if Anaheim pulls Dostal and concedes an empty-net goal; the same pressure can create an equaliser. That tail especially threatens **Ducks +1.5** and either total. No separately measured empty-net conversion parameter was recovered, so the simplified distribution below **implicitly** spans such final totals and does **not** certify a separately modeled empty-net rate. This is a material model limitation.
7. **Alternative goalie cases:** an unreported change from Dostal to Husso, or Levi to Jarry, affects both winner and goal tails, not just one contract. No actual pre-start goalie replacement was established; stress cases are not official lineup claims.

### F. Reproducible research-only score-distribution scenario

**Probability status for all rows:** `UNCALIBRATED_ANALYST_SCENARIO` (NOT a registered, fitted, validated or certified NHL model output). These are scenario calculations, **not empirical hit-rate probabilities**, and must never be entered as calibrated performance forecasts.

- **Reference:** `RULES_ICE_HOCKEY.md` league regular-season total mean ~`6.25` goals and SD ~`2.30` as historical population context. Not a qualified matchup baseline.
- **Analyst assumptions, NOT fitted inputs:** independent regulation score counts `G_EDM ~ Poisson(3.25)`, `G_ANA ~ Poisson(3.00)`. Total regulation expectation `6.25`; modest EDM goal advantage encodes offensive process but is restrained by Anaheim home/goalie and Edmonton injuries. These values were **selected as a transparent scenario**, not obtained from a trained sportsbook, fantasy, or odds-based model.
- **OT/SO bridge:** if regulation is tied, assume EDM wins the extra-time/shootout decision with fixed probability `0.52`, ANA with `0.48`; add **one** goal to the winning side's final-score total. This is an openly assumed conditional mixture, not a fitted OT/SO parameter.
- **Scoring mathematics:** sum the joint independent-Poisson regulation grid `p(i,j) = exp(-3.25)*3.25^i/i! * exp(-3.00)*3.00^j/j!`, with full-game `T=i+j+1[i=j]`. Winner is `i>j` plus `0.52 × P(i=j)`. Ducks +1.5 is `P(i <= j+1)` because tied regulation games finish with a one-goal OT/SO margin.
- **Grid:** integer goals 0 through 25 for each side. Residual outside this support is negligible at these means.
- **Calculated regulation-tie mass:** `16.2%` (about `0.16` one-goal additions per game). Thus the scenario’s **full-game** expected goals are about `6.41`, slightly above the `6.25` historical reference; the scenario uses `6.25` as its **regulation** count mean, not as an exact full-game expected total. **Exactly seven final-score goals:** `19.2%` (both named total propositions succeed on this shared event).
- **Known limitations:** independent Poisson is not a verified joint xG/shot-quality/goalie/penalty/pull model; puck-line probabilities are particularly sensitive to score-dependent empty-net mechanisms, and totals to under/overdispersion. Do not infer high numeric precision from one decimal place.

| Scenario parameter | EDM full-game ML | ANA +1.5 | Under 7.5 | Over 6.5 |
|---|---:|---:|---:|---:|
| Baseline λEDM 3.25 / λANA 3.00 | **54.2%** | **69.7%** | **70.9%** | **48.3%** |
| ANA attack stronger, λEDM 3.00 / λANA 3.25 | 46.4% | 76.3% | 70.9% | 48.4% |
| EDM attack stronger, λEDM 3.50 / λANA 2.75 | 61.9% | 62.4% | 70.9% | 48.2% |
| Higher overall scoring λEDM 3.50 / λANA 3.25 | 54.1% | 69.0% | 63.6% | 56.0% |

The scenario rows above are sensitivity checks, not outcome-weighted alternative models or confidence intervals. No odds, sportsbook implied probabilities, tipster/fantasy projections or betting preview data entered the scenario.

### G. Four ranked picks — strongest to weakest

| Rank | Exact sporting proposition | `p_card` | Probability status | Evidence supporting scenario | Principal failure route |
|---:|---|---:|---|---|---|
| **1** | **Total goals UNDER 7.5** — full game, incl. OT/SO; 0–7 goals | **70.9%** | `UNCALIBRATED_ANALYST_SCENARIO` | Shrinks Edmonton's 17-goal/3-game opening finishing; Dostal's reported start and the teams’ respective three- and two-day breaks limit immediate fatigue; the high-scoring tail remains possible; league-goal mean anchored near 6.25 | A weak Levi outing, numerous special-team chances, consecutive defensive breakdowns or late empty-net scoring drives 8+ goals. |
| **2** | **Anaheim Ducks +1.5** — full-game goal margin incl. OT/SO | **69.7%** | `UNCALIBRATED_ANALYST_SCENARIO` | Anaheim home, Dostal's reported start and one-goal OT/SO coverage; both teams have been competitive early | McDavid/Draisaitl create a multi-goal lead, or Anaheim loses by two after conceding an empty-net goal. |
| **3** | **Edmonton Oilers ML** — win completed game incl. OT/SO | **54.2%** | `UNCALIBRATED_ANALYST_SCENARIO` | Elite top-line offensive skill and shot/chance-generation levers, Bouchard and defensive PK help from Dickinson; modelled narrow goals edge | Dostal steals expected goals, Anaheim's Carlsson/Gauthier PP exploits EDM PK/Levi or home last change wins the matchup. |
| **4** | **Total goals OVER 6.5** — full game incl. OT/SO; 7+ goals | **48.3%** | `UNCALIBRATED_ANALYST_SCENARIO` | Explosive EDM line, vulnerable early EDM PK, ANA special-team threat, empty-net/3–3 OT conversion potential | Regulation finishing normalises, Dostal and Levi/defences suppress high-danger chances, the game ends 3–2 or 4–2. |

**Top-two quality/dependence:** Rank 1 vs 2 gap = `1.2` percentage points, too small to be stable under goalie and empty-net uncertainty. Top two should not be described as highly confident independent choices. Rank 4 is weaker than 50% in the selected scenario; it is included as the fourth supplied contract rather than falsely represented as a strong selection. The ranked table chooses no unsupported additional proposition.

### H. Most likely winner and sporting endpoint

**Potential full-game winner: EDMONTON OILERS — `54.2%`**, vs Anaheim `45.8%`, **includes OT + shootout**. This is a slight, highly uncertain lean based on the same `UNCALIBRATED_ANALYST_SCENARIO`, **not** a verified prospective or calibrated win probability.

### I. Evidence provenance and missingness (no game result)

Pregame/read-ahead evidence used:

1. **NHL exact gamecenter/native event and official season-to-date pregame team/special-team figures:** `https://www.nhl.com/gamecenter/edm-vs-ana/2026/10/07/2026020055` (source page may change after puck drop; only pre-match snapshot fields were considered).
2. **NHL.com Oct 7 projected lines, injuries, scratches, goalie depth:** `https://www.nhl.com/news/edmonton-oilers-anaheim-ducks-game-preview-october-7-2026`.
3. **Edmonton Oct 6 preview/coach's goalie plan, roster, rest and recent prior results:** `https://www.nhl.com/oilers/news/preview-oilers-at-ducks-10-07-26`.
4. **Edmonton Oct 7 activation/updated line projection:** `https://www.nhl.com/oilers/news/projected-lineup-dickinson-activated-off-ir-to-make-season-debut-against-ducks`.
5. **Anaheim Oct 7 game preview/schedule:** `https://www.nhl.com/ducks/news/topic/game-previews/preview-ducks-look-to-keep-wins-rolling-in-rematch-with-oilers`.
6. **NHL Oct 4 Levi profile and previous start details:** `https://www.nhl.com/news/oilers-devon-levi-trying-to-make-most-of-chance-as-nhl-goalie`.
7. **Pregame coach/beat-source goalie notices:** `https://www.gamedaytweets.com/goalies` (reported by Edmonton team and Ducks beat reporter; the actual warm-up identity is not certified here).
8. **Historical 2025-26 Edmonton 5v5 attempt/chance definition context:** `https://www.hockey-reference.com/teams/EDM/2026.html` (archival historical table, not an event-level current process receipt).
9. **NHL 2026-27 gamecenter published pre-match snapshot:** official goals-for/against, goalie first-two-game records, PP and PK percentages. Values reflect just two/three matches and are deliberately not regression coefficients.
10. **Independent historical/current Puckalytics team 5v5 xG and shooting-conversion table:** `https://www.puckalytics.com/teams/edmonton-oilers` (three-game 2026-27 sample; not a fitted model input).
11. **Framework repository, read-only:** `METHOD.md`, `CURRENT_RULES.md`, `RULES_NHL.md`, `RULES_ICE_HOCKEY.md`, `CARD_AND_LOG_TEMPLATES.md`, status/ledger/config at the pinned HEAD.

**Data not independently established:** exact actual start, actual goalie warm-up confirmations or opening shifts, fully reconciled 2026-27 high-danger chance counts per common named provider, GSAx per fixed keeper/puck model, exact penalty opportunities, line-ice matchup percentages, actual operator settlement rules, any fitted goal-distribution/OT/empty-net transition parameters and independently audited source custody. Such missing fields are NOT silently imputed as facts.

### J. Integrity and workflow receipt

`FORECAST_CLASSIFICATION: LATE_START_UNVERIFIED`  
`SCENARIO_CLASSIFICATION: UNCALIBRATED_ANALYST_SCENARIO`  
`MODEL_QUALIFICATION: NOT_LIVE_QUALIFIED`  
`EVENT_SPECIFIC_REGISTERED_NHL_MODEL_OUTPUT_USED: NO`  
`PERFORMANCE_ELIGIBILITY: NOT_CERTIFIED`  
`SPORTS_ONLY_MARKET_BLIND: PASS`  
`OBSERVED_IN_GAME_OUTCOME_USED: NO`  
`ACTUAL_PUCK_DROP_VERIFIED: NO`  
`GOALIE_WARMUP_ACTUAL_START_VERIFIED: NO`  
`LOCAL_WORKING_ID: P-550`  
`CANONICAL_LEDGER_COMMIT: NO`  
`CANONICAL_IMPORT_STATUS: PENDING`  
`LOCAL_LOG_WRITE_TIMESTAMP: 2026-10-08T13:11:54+11:00`  
`SETTLEMENT: NOT_PERFORMED`  
`RETROSPECTIVE: NOT_PERFORMED`  
`CARD_STATE: LOCALLY_STAGED_UNSETTLED`

**UNSETTLED — DO NOT SETTLE IN THIS WORKFLOW.**

### C2. CANONICAL-RECONCILIATION CARRYOVER — 0 records

None.

P-538–P-549 were imported canonically to Part 6 and journaled under the current ledger before this mini was opened. The earlier empty opening of the P-550 mini had no cards, but its subsequent latest local working version has **one** complete issued working card, P-550, now carried in C1 and pending canonical import. No P-538–P-549 ID mapping remains unresolved. P-550 is counted once in C1, not again here.

### C3. CERTIFICATION-ONLY REFERENCE — 32 records

These records are sportingly/diagnostically complete enough that they are not placed in the active sporting-result queue. They remain concise pointers because source/operator/actual-start/independence/performance-certification requirements remain unresolved.

| P-ID | Event | Competition | Current state | Remaining/reference pointer |
|---|---|---|---|---|
| P-407 | Club Brugge vs Royal Antwerp FC — Belgium Jupiler Pro League | Belgium Jupiler Pro League | `DIAGNOSTIC_ALL_RANKED_ROWS_COMPLETE` | League/Opta plus Robbie Maes original Voetbalkrant report establish two identifiable terminal collections; a third independently collected final, certified actual-start field and frozen forecast source/core remain required. ESPN/league Opta is not a third. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-410 | RB Leipzig vs Hamburger SV — German Bundesliga | German Bundesliga | `DIAGNOSTIC_ALL_RANKED_ROWS_COMPLETE` | DFL collection and HSV original report are identifiable; a third independently collected final and certified actual start are missing. Pre-cutoff XI, bench, coach and distribution receipts remain unverified. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-492 | MLB — San Diego Padres @ Los Angeles Dodgers | MLB | `ALL_ORIGINAL_SPORTING_ROWS_DIAGNOSTICALLY_COMPLETE` | All four original sporting selections are now diagnosed L/L/W/L and original ranks recovered. No first-five forecast was issued in the recovered table. Remaining: original operator action terms, issue-time/source/baseline certification and independently audited terminal quorum; START_CROSSED remains permanently excluded from pregame metrics. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-518 | MLB New York Mets at Washington Nationals | MLB | `DIAGNOSTIC_ALL_RANKED_ROWS_COMPLETE` | The official feed reconfirms the final, but independent terminal quorum, actual start and canonical issue transaction are absent. Original LIVE_ISSUED status stays excluded. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-519 | AFLW Gold Coast vs St Kilda | AFLW | `DIAGNOSTIC_ALL_RANKED_ROWS_COMPLETE` | Champion Data plus AAP original report are identifiable collections. Kimber is a distinct authored report, but independent collection of terminal facts versus the shared AFL stats feed remains unverified; do not promote it automatically as a third. Freeze 07:08:21Z follows scheduled 07:05Z; LIVE_ISSUED stays. Actual start, certified issue core and baseline lineage remain absent. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-520 | KBO Hanwha at Lotte | KBO | `OWNER_NATIVE_FINAL; ALL_FOUR_SPORTING_ROWS_DIAGNOSTICALLY_COMPLETE` | Owner native game 20260927HHLT0 is now verified: Hanwha 6–2 Lotte, September 27, scheduled 17:00 KST, normal final in the ninth. Scheduled time is not certified actual first pitch. Original operator action terms, actual-start semantics, canonical issue/source/baseline receipts and independently audited terminal collection status remain unresolved. No certification or performance eligibility is granted. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-521 | ACB Breogan vs Joventut | ACB | `DIAGNOSTIC_ALL_RANKED_ROWS_COMPLETE` | ACB native final plus EFE and original El Progreso terminal narratives agree; independently collected source status remains UNKNOWN in live registries. No actual-start field or canonical issue receipts; original LIVE_ISSUED remains excluded. ACB card-derived baseline rates are diagnostic, not approved population baselines. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-522 | ACB La Laguna Tenerife vs Casademont Zaragoza | ACB | `DIAGNOSTIC_ALL_RANKED_ROWS_COMPLETE` | Official ACB exact final is reconfirmed. Independent terminal quorum, actual-start semantics and canonical issue receipts remain missing; LIVE_ISSUED and missing approved baseline remain permanent exclusions. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-524 | KT Wiz @ Kia Tigers — retained October 1 card | KBO | `OWNER_FINAL; ALL_FOUR_SPORTING_ROWS_DIAGNOSTICALLY_COMPLETE` | Original operator/action terms and audited independent terminal collection status remain missing; no new pregame or prospective certification can be inferred from a live/historical import. Original p/baseline and timing labels unchanged. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-525 | Chunichi Dragons @ Hiroshima Toyo Carp — Game 25 | NPB | `OWNER_FINAL; ALL_FOUR_SPORTING_ROWS_DIAGNOSTICALLY_COMPLETE` | Original operator/action terms and audited independent terminal collection status remain missing; no new pregame or prospective certification can be inferred from a live/historical import. Original p/baseline and timing labels unchanged. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-526 | Hanwha Eagles @ Samsung Lions — October 1, 2026 | KBO | `OWNER_FINAL; ALL_FOUR_SPORTING_ROWS_DIAGNOSTICALLY_COMPLETE` | Original operator/action terms and audited independent terminal collection status remain missing; no new pregame or prospective certification can be inferred from a live/historical import. Original p/baseline and timing labels unchanged. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-527 | Hapoel Tel Aviv vs Real Madrid — October 1, 2026 | EuroLeague | `DIAGNOSTICALLY_SETTLED_NOT_CERTIFIED` | Obtain exact original operator action/period/OT/shortened-game terms and an audited three-independent-terminal-lineage bundle for this exact event. Retain UNKNOWN_DEFINITION and formal UNRESOLVED; never grant prospective eligibility to this historical import. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-528 | Grand Rapids Griffins @ Cleveland Monsters — October 2, 2026 | AHL | `DIAGNOSTICALLY_SETTLED_NOT_CERTIFIED` | Obtain exact original operator action/period/OT/shortened-game terms and an audited three-independent-terminal-lineage bundle for this exact event. Retain UNKNOWN_DEFINITION and formal UNRESOLVED; never grant prospective eligibility to this historical import. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-529 | Philadelphia Flyers @ New Jersey Devils — October 1, 2026 | NHL | `DIAGNOSTICALLY_SETTLED_NOT_CERTIFIED` | Obtain exact original operator action/period/OT/shortened-game terms and an audited three-independent-terminal-lineage bundle for this exact event. Retain UNKNOWN_DEFINITION and formal UNRESOLVED; never grant prospective eligibility to this historical import. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-530 | Philadelphia Phillies @ Atlanta Braves — NL Wild Card Game 3 | MLB | `DIAGNOSTICALLY_SETTLED_NOT_CERTIFIED` | Obtain exact original operator action/period/OT/shortened-game terms and an audited three-independent-terminal-lineage bundle for this exact event. Retain UNKNOWN_DEFINITION and formal UNRESOLVED; never grant prospective eligibility to this historical import. Preserve the duplicated supplied Over 7.5 row separately from the unsupported Under shadow alternative; no silent row repair. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-531 | Indiana Fever @ Las Vegas Aces — First Round Game 3 | WNBA | `DIAGNOSTICALLY_SETTLED_NOT_CERTIFIED` | Obtain exact original operator action/period/OT/shortened-game terms and an audited three-independent-terminal-lineage bundle for this exact event. Retain UNKNOWN_DEFINITION and formal UNRESOLVED; never grant prospective eligibility to this historical import. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-532 | Tasmania JackJumpers vs Melbourne United (NBL27, Round 3) | NBL | `DIAGNOSTICALLY_SETTLED_NOT_CERTIFIED` | Obtain exact original operator action/period/OT/shortened-game terms and an audited three-independent-terminal-lineage bundle for this exact event. Retain UNKNOWN_DEFINITION and formal UNRESOLVED; never grant prospective eligibility to this historical import. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-533 | KIA Tigers @ LG Twins (KBO League 2026, Regular Season) | KBO | `DIAGNOSTICALLY_SETTLED_NOT_CERTIFIED` | Obtain exact original operator action/period/OT/shortened-game terms and an audited three-independent-terminal-lineage bundle for this exact event. Retain UNKNOWN_DEFINITION and formal UNRESOLVED; never grant prospective eligibility to this historical import. Preserve unsupported KIA ML separately from the supplied KIA +1.5 contract. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-534 | Sydney Roosters vs Newcastle Knights (NRL 2026, Grand Final) | NRL | `DIAGNOSTICALLY_SETTLED_NOT_CERTIFIED` | Obtain exact original operator action/period/OT/shortened-game terms and an audited three-independent-terminal-lineage bundle for this exact event. Retain UNKNOWN_DEFINITION and formal UNRESOLVED; never grant prospective eligibility to this historical import. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-535 | Panathinaikos AKTOR vs Vikos Falcons (Greek Basket League 2026-27, Round 1) | Greek Basket League | `DIAGNOSTICALLY_SETTLED_NOT_CERTIFIED` | Obtain exact original operator action/period/OT/shortened-game terms and an audited three-independent-terminal-lineage bundle for this exact event. Retain UNKNOWN_DEFINITION and formal UNRESOLVED; never grant prospective eligibility to this historical import. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-536 | FC Bayern München vs EWE Baskets Oldenburg (easyCredit BBL 2026-27, Round 4) | BBL | `DIAGNOSTICALLY_SETTLED_NOT_CERTIFIED` | Obtain exact original operator action/period/OT/shortened-game terms and an audited three-independent-terminal-lineage bundle for this exact event. Retain UNKNOWN_DEFINITION and formal UNRESOLVED; never grant prospective eligibility to this historical import. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05` |
| P-538 | Florida Panthers @ Los Angeles Kings | NHL | `DIAGNOSTIC_SPORTING_COMPLETE_CERTIFICATION_UNRESOLVED` | Retain exact original issue-time/operator terms and complete admitted source/actual-start/independence evidence. Do not backfill or certify historical uncalibrated scenarios. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md` |
| P-539 | Aleksandar Kovacevic vs Matteo Berrettini | ATP Shanghai | `DIAGNOSTIC_SPORTING_COMPLETE_CERTIFICATION_UNRESOLVED` | Retain exact original issue-time/operator terms and complete admitted source/actual-start/independence evidence. Do not backfill or certify historical uncalibrated scenarios. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md` |
| P-541 | Mattia Bellucci vs Yi Zhou | ATP Shanghai | `DIAGNOSTIC_SPORTING_COMPLETE_CERTIFICATION_UNRESOLVED` | Retain exact original issue-time/operator terms and complete admitted source/actual-start/independence evidence. Do not backfill or certify historical uncalibrated scenarios. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md` |
| P-542 | Adelaide 36ers vs Melbourne United | NBL | `DIAGNOSTIC_SPORTING_COMPLETE_CERTIFICATION_UNRESOLVED` | Retain exact original issue-time/operator terms and complete admitted source/actual-start/independence evidence. Do not backfill or certify historical uncalibrated scenarios. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md` |
| P-543 | Hiroshima Toyo Carp @ Hanshin Tigers | NPB | `DIAGNOSTIC_SPORTING_COMPLETE_CERTIFICATION_UNRESOLVED` | Retain exact original issue-time/operator terms and complete admitted source/actual-start/independence evidence. Do not backfill or certify historical uncalibrated scenarios. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md` |
| P-544 | Doosan Bears @ LG Twins | KBO | `DIAGNOSTIC_SPORTING_COMPLETE_CERTIFICATION_UNRESOLVED` | Retain exact original issue-time/operator terms and complete admitted source/actual-start/independence evidence. Do not backfill or certify historical uncalibrated scenarios. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md` |
| P-545 | Hanwha Eagles @ Kiwoom Heroes | KBO | `DIAGNOSTIC_SPORTING_COMPLETE_CERTIFICATION_UNRESOLVED` | Retain exact original issue-time/operator terms and complete admitted source/actual-start/independence evidence. Do not backfill or certify historical uncalibrated scenarios. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md` |
| P-546 | Samsung Lions @ KT Wiz | KBO | `DIAGNOSTIC_SPORTING_COMPLETE_CERTIFICATION_UNRESOLVED` | Retain exact original issue-time/operator terms and complete admitted source/actual-start/independence evidence. Do not backfill or certify historical uncalibrated scenarios. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md` |
| P-547 | NC Dinos @ SSG Landers | KBO | `DIAGNOSTIC_SPORTING_COMPLETE_CERTIFICATION_UNRESOLVED` | Retain exact original issue-time/operator terms and complete admitted source/actual-start/independence evidence. Do not backfill or certify historical uncalibrated scenarios. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md` |
| P-548 | Busan KCC Egis vs Daegu Korea Gas Corporation Pegasus | KBL | `DIAGNOSTIC_SPORTING_COMPLETE_CERTIFICATION_UNRESOLVED` | Retain exact original issue-time/operator terms and complete admitted source/actual-start/independence evidence. Do not backfill or certify historical uncalibrated scenarios. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md` |
| P-549 | Foshan Nanshi vs Guangxi Hengchen | China League One | `DIAGNOSTIC_SPORTING_COMPLETE_CERTIFICATION_UNRESOLVED` | Retain exact original issue-time/operator terms and complete admitted source/actual-start/independence evidence. Do not backfill or certify historical uncalibrated scenarios. Pointer: `prediction logs/PREDICTION_LOG_COMBINED_6.md` |

### C4. FULLY CLOSED

No record from the selected 65-record current carryover register is removed as fully closed. Records outside the current selected register are not reintroduced into the active queue.

---

## D. New local event cards

# NEW LOCAL EVENT CARDS

**First available working P-ID:** `P-551`

_No new event card has been created for this mini. Creating this mini does not consume P-551. Existing local P-550 is preserved only as an active carryover in C1 above._

---

## E. Running ID footer

- **Highest local working P-ID actually used:** `P-550` (carried existing ID; no P-ID issued on new-mini creation)
- **Next local working P-ID:** `P-551`
- **Repository next-ID snapshot when mini opened:** `P-550`
- **Active sporting/contract carryovers:** `34` (33 selected register + P-550 local)
- **Canonical-reconciliation carryovers:** `0`
- **Reference-only carryovers:** `32`
- **Total selected-register carryovers retained:** `65`
- **Additional local sporting carryovers:** `1` (P-550)
- **Total unique carryovers retained:** `66`
- **New event cards:** `0`
- **LOCAL MINI STATUS:** `ACTIVE`
- **CANONICAL IMPORT:** `PENDING`
- **PERFORMANCE_ELIGIBILITY:** `NOT_CERTIFIED`
- **Mode:** `LOCAL_MINI_STAGING`
- **SPORTS_ONLY / MARKET_BLIND:** `REQUIRED`
- **Settlements performed:** `0`
- **Retrospectives performed:** `0`
- **Grades assigned:** `0`
- **Result research performed:** `0`
- **GitHub writes performed:** `NO`
- **Combined Log writes performed:** `NO`
- **Canonical-ledger writes performed:** `NO`
- **Historical/local evidence deleted:** `NO`

---

## F. Ongoing use

After every individual game-log request:

1. Re-read this current local mini.
2. Check event identity and aliases against this mini and the canonical repository state.
3. Use the current `Next local working P-ID`.
4. Append one complete new event card locally.
5. Verify the event/card appears exactly once.
6. Preserve all prior cards and carryover text byte-for-byte where practical.
7. Update the highest/next working ID and event count.
8. Do not modify GitHub in `LOCAL_MINI_STAGING`.
9. If GitHub advances, record the newer repository snapshot for reconciliation but do not renumber already-issued local cards.

---

## G. Absolute prohibitions for this workflow

NO:

- settlement;
- score/result research;
- W/L/P grading;
- retrospective;
- model retraining;
- model promotion;
- methodology change;
- GitHub write;
- Combined Log write;
- canonical-ledger write;
- deletion of historical/local evidence;
- backdating;
- invented data or probabilities.
