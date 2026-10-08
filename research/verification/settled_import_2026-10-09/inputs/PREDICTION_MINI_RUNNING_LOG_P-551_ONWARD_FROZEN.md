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
- **LOCAL_NEXT_WORKING_ID AT OPENING:** `P-551` — mini creation consumed no ID; current next ID is P-555 in running footer
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

### P-551 — TENNIS / ATP MASTERS 1000 SHANGHAI — Adolfo Daniel Vallejo vs Valentin Royer — 2026-10-08

> **LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT.** This is not a GitHub or canonical-ledger committed ID. **NO SETTLEMENT / NO RETROSPECTIVE.**
>
> **Original published research/card timestamp:** 2026-10-08 16:23:53 AEDT (UTC+1100); UTC `2026-10-08T05:23:53+00:00`. Issued after user supplied an estimated `15:30 AEST` (which means `16:30 AEDT` in Melbourne on 8 October). **Observed actual-start status: START_UNVERIFIED / POSSIBLY_LIVE.** In-match points, games and scores are deliberately excluded from inputs. No unsupported pre-match certification claim is made.

#### A. Repository/control snapshot and event identity

- **Repository/branch:** `danisgreat/Sports-Research`, `main`; HEAD `1ffbd9f52c63926bf7b1f5df9796e37477c1e9a3` (fresh-read).
- **Method:** `MDS-2026.10.01-v8.0`; **control:** `CR-2026.10.08-R3`; **manifest:** `CONTROL_MANIFEST_2026-10-08-3.md`; **scoring:** `SCV-2026.10.01-v3`.
- **Official schedule identity:** Shanghai Rolex Masters, men's singles, first round / R128, **8 October 2026**, **Court 7, second after Camilo Ugo Carabelli vs Ilia Simakin**, no guaranteed second-match clock. Surface **outdoor hard**; **best of 3 sets** with standard 7-point tiebreak sets. Both opponents shown without `(Q)`: this is their main-draw match. No official durable native match ID authenticated. Source: https://en.rolexshanghaimasters.com/en/scores/schedule?dayToDisplay=8 .
- **Home/away semantics:** neutral tennis; Vallejo (PAR), Royer (FRA). Both right-handed with two-handed backhands. ATP published rankings: Vallejo **No. 52**, Royer **No. 105**; official prior ATP tour head-to-head **0-0** (no directly informative prior meeting): https://en.rolexshanghaimasters.com/en/scores/head-to-head/singles/v0dp/r0eb .
- **Event key:** `ATP_SHANGHAI_2026_10_08_R128_VALLEJO_ROYER`; **native ATP match ID:** `UNKNOWN_NOT_VERIFIED`; **local tracking alias:** `LOCAL-20261008-P-551-ATP-SHANGHAI-VALLEJO-ROYER`.
- **Canonical state:** GitHub committed highest `P-549`; repository next-ID snapshot `P-550`. Earlier local NHL card already uses P-550. **P-551 is the next unused LOCAL working ID** and has not been imported. Future canonical collision must be resolved in a separate authorized import procedure, not by changing this issued card.
- **Injury / withdrawal / action:** no reliable player-specific new withdrawal or medical confirmation established; fitness **UNKNOWN**, not "confirmed fit." Operator retirement, completed-set and abandonment definitions **NOT SUPPLIED / UNKNOWN_DEFINITION** for eventual contract settlement. Shanghai match may be delayed; actual start **not verified**.
- **SPORTS_ONLY / MARKET_BLIND:** no prices, implied odds, previews, public tips, in-play data or market movement entered the scenario.

#### B. Sports-only pre-event evidence and opponent adjustment

- **Tour-level trajectory:** On 1 Oct Tokyo hard, Vallejo defeated Rafael Jodar **6-1, 6-3**; on 3 Oct defeated Matteo Berrettini **7-6(6), 6-1**, winning all **10/10 service games** with **5 aces, 0 double faults, 49/64 first serves in, 38/49 first-serve and 11/15 second-serve points won**; on 4 Oct lost to Jiri Lehecka **1-6, 1-6**. The Berrettini score and serve denominators are independently published by Tennis.com; the loss prevents unqualified form extrapolation. https://www.tennis.com/tournaments/rakuten-japan-open-tennis-championships/matches/m-berrettini-vs-a-vallejo-2026-10-03 ; https://www.tennismajors.com/matches/atp/rolex-shanghai-masters/adolfo-daniel-vallejo-vs-valentin-royer .
- **Recent workload/rest:** Vallejo played Tokyo qualifying on **28–29 September** and three main-draw rounds **1–4 October**; at least five matches within seven days, last Oct 4, approximately four calendar days before Shanghai. Travel Tokyo to Shanghai; specific arrival/recovery unverified.
- **Royer:** defeated Adam Walton **6-3, 6-4** on **23 Sep**, including **14 aces, 1 double fault and 10/10 service games held**; lost **6-7(6), 3-6** to Daniil Medvedev on **26 Sep**, holding **9/10 service games**; lost to Botic van de Zandschulp in Beijing qualifying on **28 Sep** (Royer score recorded as **6-4, 2-6, 4-6**). Last documented contest ten calendar days earlier; longer rest may improve freshness or introduce rhythm uncertainty. https://www.tennis.com/tournaments/hangzhou-open/matches/v-royer-vs-a-walton-2026-09-23 ; https://www.hangzhouopen.com/en/media/news/medvedev-royer-hangzhou-2026-saturday ; https://tennis-db.com/players/56/valentin-royer/matches .
- **Tennis Abstract comparable hard-court 52-week aggregates** (source shows no service/return point denominators for split; use shrunk population/model assumptions rather than inventing sample sizes): Vallejo hard **10-7** matches, **62.8% service points won**, **37.1% return points won**, **78.7% holds**, **25.3% breaks**, **5.7% ace rate**, **63.1% first-serve in**, **70.7% first-serve points won**, **49.2% second-serve points won**; hard tiebreaks **1-2** (small sample). Royer hard **14-22**, **62.5% service points won**, **35.1% return points won**, **78.7% holds**, **20.1% breaks**, **7.7% ace rate**, **61.3% first serves in**, **70.3% first-serve points won**, **50.1% second-serve points won**; hard tiebreaks **6-13**. Both show stronger holding than breaking, but level and opponent mix differ. https://www.tennisabstract.com/cgi-bin/player-classic.cgi?f=ACareerqq&p=209226%2FAdolfo-Daniel-Vallejo&q=PabloCarrenoBusta ; https://www.tennisabstract.com/cgi-bin/player-classic.cgi?f=ACareerqqDOeiras_1_Challengerqq&p=208316%2FValentin-Royer .
- **Opponent-adjusted raw serve cross-check:** Vallejo's own hard SPW 62.8% and Royer's 35.1% RPW imply **64.9%** opponent serve-point retention against Royer; equal-weight synthesis **63.85%**. Royer's 62.5% hard SPW and Vallejo's 37.1% hard RPW imply **62.9%** retention; synthesis **62.7%**. Shrinking and rounding yields scenario **63.7% Vallejo points won on own serve / 63.0% Royer**. *These point rates are explicit analyst assumptions, not trained, opponent-calibrated H0 coefficients.*
- **Tennis Abstract dated-availability caveat:** accessed `2026-10-08T05:23:53+00:00`; original point-in-time version/update timestamp not independently proven. Overall Elo **1698.2 Vallejo vs 1686.2 Royer**; hard-court Elo **1569.7 Vallejo vs 1638.6 Royer**. Simple best-of-three Elo logistic proxies: overall Vallejo **51.7%**, hard **40.2%**, 50:50 overall/hard blend Vallejo **45.9%**. The surface Elo explicitly favours Royer and is a caution against a ranking-based favourite. Scenario Vallejo 53.5% is about **+7.6 percentage points** above blended proxy; mechanism is Vallejo's recent Tokyo high-level form plus cross-adjusted serve/return, offset by his Lehecka loss and workload. https://www.tennisabstract.com/reports/atp_elo_ratings.html .
- **H2H:** official ATP 0-0; no prior comparable match is used. Individual double-fault, break-point saving and tiebreak rates are volatile at the match level. No confirmed new illness/medical reports, practice observations or arrival times were authenticated. Shanghai outdoor delays could widen uncertainty. No weather value is invented.

#### C. Coherent, reproducible match/set/game scenario

**Probability status of every numeric row: `UNCALIBRATED_ANALYST_SCENARIO`; performance `NOT_CERTIFIED`; numerical model `SHADOW: NO_LANE / UNVALIDATED`.** No fit on D0, no approved live H0 tennis model and no confidence statement equivalent to a calibrated probability. Original supplied contracts:

1. `Vallejo -1.5` — **assumed FULL MATCH TOTAL GAMES handicap -1.5**; unit otherwise undefined.
2. `Royer +1.5` — **assumed FULL MATCH TOTAL GAMES handicap +1.5**; unit otherwise undefined.
3. `TOTAL GAMES OVER 22.5` — all games in a normally completed best-of-three match.
4. `TOTAL GAMES UNDER 22.5` — complementary total.

*Do not silently use games probabilities for set handicaps.* If the unnamed 1.5 units are **SETS**, the same joint scenario instead returns Vallejo -1.5 sets (must win 2-0) **27.4%**, Royer +1.5 sets (must take at least one set) **72.6%**. This is an analytical fork; the contract cannot be definitively certified or operator-settled without explicit unit/retirement terms.

**Distribution mechanics (one common joint scenario):** point-on-serve `p_V=0.6370`, `p_R=0.6300`; exact deuce game chain gives hold probability `H_V=0.80733`, `H_R=0.79468`; tiebreak-point service alternation; game-by-game set scores 6-0 … 7-6; tiebreak at 6-6; two sets to win; random 50:50 first server; first-service alternation follows set length. Sum over the **entire discrete joint (Vallejo aggregate games, Royer aggregate games, Vallejo sets, Royer sets)**. Normal completion assumed; retirements and abandonment are a separate operator-unknown risk. A single constant hold chain ignores state, opponent adaptation, post-rest uncertainty and concentration; no prospective validation exists.

- **Normalized scenario mass:** `1.00000000`.
- **Match Vallejo win:** **53.5%**; Royer win **46.5%**.
- **Sets distribution:** Vallejo 2-0 **27.4%**, Vallejo 2-1 **26.1%**, Royer 2-0 **22.7%**, Royer 2-1 **23.8%**.
- **Deciding set:** **49.9%**, above historical men best-of-three reference **35.8%** because players are treated near even; uncalibrated set-count model may overstate closeness.
- **Games margin ±1.5 complement:** Vallejo -1.5 games **46.0%**; Royer +1.5 games **54.0%**; sum 100.0% in the assumed no-retirement endpoint.
- **Totals complement:** Over 22.5 **60.9%**; Under 22.5 **39.1%**; sum 100.0%, no integer push possible at .5.
- **Representative coherent route:** Vallejo **6-4, 4-6, 7-6**, aggregate Vallejo **17 games**, Royer **16**, total **33**, Vallejo wins, **Over 22.5** and **Royer +1.5 games** both win while **Vallejo -1.5 games** and **Under 22.5** lose. Illustrative route only, not most probable single exact scoreline.

#### D. Ranked four supplied picks — strongest to weakest (assuming ±1.5 GAMES)

| Rank | Exact sporting proposition | p_card | Probability status | Supporting evidence | Principal failure route |
|---:|---|---:|---|---|---|
| **1** | **Over 22.5 total completed match games** | **60.9%** (`0.60885`) | `UNCALIBRATED_ANALYST_SCENARIO` | Nearly level hard-court serve/return expectations, hold probabilities near 80%, tiebreak exposure, deciding set **49.9%** | One player dominates with short straight sets (e.g. 6-2, 6-3), or retirement/void semantics |
| **2** | **Royer +1.5 FULL MATCH total games**: Royer's aggregate games +1.5 > Vallejo's aggregate games | **54.0%** (`0.53958`) | `UNCALIBRATED_ANALYST_SCENARIO` | Royer's superior hard Elo; similar expected service holds and ability to cover by staying within one game even in a Vallejo win | Vallejo separates by at least two net games, particularly repeated breaks or two-set control |
| **3** | **Vallejo -1.5 FULL MATCH total games**: Vallejo's aggregate games −1.5 > Royer's aggregate games | **46.0%** (`0.46042`) | `UNCALIBRATED_ANALYST_SCENARIO` | Tokyo win over Berrettini and slightly higher cross-adjusted serve points; has an edge in forecast winner mass but not reliably margin | Royer wins or loses narrowly, or Vallejo wins in three close sets with ≤1 net game margin |
| **4** | **Under 22.5 total completed match games** | **39.1%** (`0.39115`) | `UNCALIBRATED_ANALYST_SCENARIO` | Lehecka 6-1 6-1 shows possible Vallejo vulnerability, and early breaks can compress both sets | Deciding set, repeated 7-5 / 7-6 outcomes, or two long straight sets |

**Most likely winner (full completed match): Adolfo Daniel Vallejo — 53.5%**, Royer **46.5%**; *narrow, uncalibrated*, not a high-confidence claim. Winner includes a standard third set where played; **no retirement settlement assumption**. Opponent Elo and the more rested Royer create meaningful upside risk. Ranked supplied picks are mutually dependent: ranks 1 and 4 are opposite totals, ranks 2 and 3 are opposite games handicaps. They are **not four independent trials** and should not be aggregated as such.

#### E. Source provenance, timing and failure gates

- **Official dated match schedule, participant entry / main draw / court sequence:** https://en.rolexshanghaimasters.com/en/scores/schedule?dayToDisplay=8 ; official H2H https://en.rolexshanghaimasters.com/en/scores/head-to-head/singles/v0dp/r0eb .
- **ATP venue/surface:** https://www.atptour.com/en/tournaments/rolex-shanghai-masters/5014/overview ; outdoor hard match detail https://www.sofascore.com/tennis/match/adolfo-daniel-vallejo-valentin-royer/ZiccsZNFc .
- **Player public sports metrics:** https://www.tennisabstract.com/reports/atp_elo_ratings.html , https://www.tennisabstract.com/cgi-bin/player-classic.cgi?f=ACareerqq&p=209226%2FAdolfo-Daniel-Vallejo&q=PabloCarrenoBusta , https://www.tennisabstract.com/cgi-bin/player-classic.cgi?f=ACareerqqDOeiras_1_Challengerqq&p=208316%2FValentin-Royer .
- **Individual pre-event sporting match data:** https://www.tennis.com/tournaments/rakuten-japan-open-tennis-championships/matches/m-berrettini-vs-a-vallejo-2026-10-03 , https://www.tennis.com/tournaments/hangzhou-open/matches/v-royer-vs-a-walton-2026-09-23 , https://www.hangzhouopen.com/en/media/news/medvedev-royer-hangzhou-2026-saturday , https://www.tennis.com/tournaments/hangzhou-open/matches/d-medvedev-vs-v-royer-2026-09-26 , https://www.tennismajors.com/matches/atp/rolex-shanghai-masters/adolfo-daniel-vallejo-vs-valentin-royer .
- **Official event source time:** scheduled Court 7 sequence, **NOT a native event-start confirmation**; clock estimate from user **may differ**. Tennis score-site displayed match status may already be live or delayed, **but no current point, game or set observation is used**. `START_UNVERIFIED / POSSIBLY_LIVE` blocks any strict pregame admission.
- **Point-in-time and source independence:** precise underlying Tennis Abstract update time, raw source-body hashes, upstream provider independence, certified cutoff receipt and model dependencies are **not established**; card is research-only. No fabricated historical pre-cutoff source fetch.
- **Injuries/fitness:** fresh injury or retirement-specific reports for either player **NOT VERIFIED**; no assertion both confirmed fit. Official roster status may change.
- **Operator:** ±1.5 **games-vs-sets ambiguity**, exact retirement/walkover/action semantics not verified; `UNKNOWN_DEFINITION` at settlement if unresolved. These missing terms are disclosed now; **no result or grade is supplied**.
- **Sources were consulted at actual card preparation time `2026-10-08T05:23:53+00:00`**, not claimed as known at a hypothetical earlier freeze. Any later line movement or in-match information is excluded.

#### F. Local logging receipt — forecast only

- **Local P-ID:** `P-551` once appended and byte-verified; **canonical import:** `PENDING`.
- **Duplicate comparison:** no Vallejo–Royer Shanghai 2026 entry found among prior local P-550, selected carryovers and published committed ledger through P-549. The same fixture shall return **P-551**, without allocating another ID.
- **Exact original supplied contract strings retained** above; games assumption and set alternative are explicitly separate.
- **Settlements:** `NONE`; **retrospectives:** `NONE`; **grade:** `NOT_PERFORMED`; **performance eligibility:** `NOT_CERTIFIED`.
- **GitHub writes:** `NO`; **Combined Log writes:** `NO`; **canonical-ledger writes:** `NO`.



### P-552 — BASKETBALL / AUSTRALIA NBL27 — Cairns Taipans vs Brisbane Bullets — 2026-10-08

> **LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT.** The repository's unconsumed canonical next ID was P-550; P-550 and P-551 are already occupied by earlier LOCAL cards, so P-552 is the first unused LOCAL working identifier. **NO SETTLEMENT / NO RETROSPECTIVE / NO GITHUB WRITE.**

#### A. Identity, timing, contract and source gate

- **Research/card recording time:** `2026-10-08T19:35:49+11:00` Australia/Melbourne. Official scheduled tip was 2026-10-08 **19:30 AEDT = 18:30 AEST**, **not** 19:30 AEST as estimated by user; Cairns Convention Centre, Round 4, 2026–27 regular season, NBL men's basketball. Actual jump-ball time **NOT VERIFIED**. Because this card was recorded after scheduled tip, `ANALYSIS_STATUS: LATE_START_UNVERIFIED_PREGAME_ONLY`. This is not an authenticated pre-tip forecast. NO game-action statistics, live score, play-by-play, final or result news used.
- **Identity key:** `NBL27_2026-10-08_CNS_BRI_R4`; native NBL durable match ID: `NOT_VERIFIED`; tracking alias: `LOCAL-20261008-P-552-NBL-CNS-BRI`.
- **Home:** Cairns Taipans; **away:** Brisbane Bullets; 4×10-minute regulation quarters; normal NBL 5-minute overtime periods to determine the full-game winner. Forecast horizon: full game including OT, conditional on game being played to completion. The supplied contract's bookmaker/operator-specific settlement/void/OT definition was not provided; standard full-game including OT is an explicitly conditional modelling assumption, not a verified operator contract. Exact operator semantics: `UNKNOWN_DEFINITION`.
- **Repository snapshot:** GitHub `danisgreat/Sports-Research` `main` HEAD `1ffbd9f52c63926bf7b1f5df9796e37477c1e9a3`; `MDS-2026.10.01-v8.0`; `CR-2026.10.08-R3`; manifest `CONTROL_MANIFEST_2026-10-08-3.md`; scoring `SCV-2026.10.01-v3`. Repository highest COMMITTED `P-549`, repository next snapshot P-550. LOCAL next after this card P-553.
- **Probability status:** `UNCALIBRATED_ANALYST_SCENARIO` for each pick, not historically validated or certified; `PERFORMANCE_ELIGIBILITY: NOT_CERTIFIED`; `SPORTS_ONLY / MARKET_BLIND`. All supplied handicaps and totals treated solely as thresholds, no market evidence.
- **Lineage / start gate:** official NBL published preview, official NBL injury-list at October 8, 16:00 AEDT, pregame club previews and Cairns game-day Shaun Bruce fitness announcement. News and match-report contents published before scheduled tip only. **No independent audit of all collectors, no source-body immutable captures, no official first jumpBall receipt, no confirmed starting-five feed**. `START_UNVERIFIED` and `LINEUP_UNCONFIRMED`. Do not mislabel this card as certified pregame.

#### B. Pre-event sports-only evidence and player roles

- **Team state:** Cairns **2–3**, Brisbane **2–2** through R3; Cairns 1–0 at home and Brisbane 0–1 on road from the limited current sample. Cairns' previous game: 107–95 road win over Melbourne on Oct 3; Jaylon Brown 20, Jack McVeigh 20, Keanu Pinder 27 and Reyne Smith 21. Brisbane's last game: 99–109 *in OT* loss to Tasmania on Oct 3; regulation was 91–91. Earlier Brisbane games: 88–85 New Zealand, 103–95 Illawarra, 78–93 Sydney. Thus both had ~five calendar days since last competition game, neither on a back-to-back; Brisbane travels to Cairns, home court belongs to Cairns.
- **Cairns five pre-event full-game scores:** at Sydney 90–111 (20 Sep); vs Tasmania 93–87 (23 Sep); at Adelaide 69–83 (27 Sep); at NZ 75–98 (30 Sep); at Melbourne 107–95 (3 Oct). Scored average 86.8, allowed average 94.8; this five-match sample is highly noisy. Previous match total 202 not projected blindly into next contest.
- **Brisbane four completed final scores:** 88–85 NZ, 103–95 Illawarra, 78–93 Sydney, 99–109 Tasmania (OT); actual all-endpoint scored 92.0 and conceded 95.5 PPG, but the OT game inflates both. Replacing OT final with its documented 91–91 regulation score yields regulation averages **90.0 scored and 91.0 allowed**, across four games. Historical opponent quality and schedule confound interpretation; do not equate these means to trained possession efficiencies.
- **Cairns official expected depth chart:** PG Jaylon Brown / Shaun Bruce (officially *cleared*) / Luke Paul (NBL debut); SG Reyne Smith (Jaylin Galloway OUT), SF Malique Lewis (Sunday Dech OUT), PF Jack McVeigh / Kyrin Galloway, C Keanu Pinder / Jonah Bolden. **Provisional starting five:** Jaylon Brown, Reyne Smith, Malique Lewis, Jack McVeigh, Keanu Pinder; **NOT CONFIRMED**. Bruce passed official game-day fitness test and will suit up. Paul debut confirmed but coach projected approximately 5–8 minutes as initial target; his actual minutes remain uncertain.
- **Brisbane official expected depth chart:** PG Arnas Velička / Mitch Norton; SG Max Mackinnon (Taine Murray OUT); SF Nate Hinton (Sam McDaniel OUT); PF Jaylin Williams / Lat Mayen; C Tyrell Harrison / Jacob Holt. **Provisional starters:** Velička, Mackinnon, Hinton, Williams, Harrison; **NOT CONFIRMED**. No exact minute assurances supplied.
- **Injury snapshot:** Cairns Jaylin Galloway shoulder OUT (league expects R6); Sunday Dech hamstring OUT (R8); Shaun Bruce's groin test changed from doubtful/test on earlier team sheet to **available** on October 8, according to Cairns official release; Luke Paul fit to debut, first-game exposure risk. Brisbane Sam McDaniel lower leg OUT (R10) and Taine Murray lower-limb OUT (R4–6). No authenticated later withdrawals from official active roster; absent official active-list verification, other players remain expected rather than confirmed.
- **Current usage/minutes:** Cairns: Jack McVeigh 16.2 PPG, Keanu Pinder 15.8, Jaylon Brown 12.8, Malique Lewis 10.4, Reyne Smith 9.2 (club team leaders before fixture); Jonah Bolden 7.8 RPG. Brisbane's Arnas Velička 15.3 PPG/10.8 APG through four; Cairns plans Lewis' defensive length as point-of-attack counter. In the Oct 3 five-period loss: Velička ~37:04, Mackinnon ~35:09, Hinton ~32:58, Harrison ~33:55; these are *OT-inclusive historical exposure*, not predicted regulation minutes. Harrison had 24 points / 12 rebounds, Mackinnon 21 with 5/8 threes, Hinton 21; Velička 6 points on 2/14 FG with 13 assists. Regression risk cuts both ways.
- **Shot profile/turnovers/free throws:** Velička shot just 26.9% over two losses per NBL preview (season 35.7%); one miss-heavy stretch cannot prove persistent suppression. Mackinnon 5-of-8 from three on Oct 3 is high-variance evidence, not a repeatable 62.5% expectation. Harrison's rim scoring/offensive boards, and FTA 6/7 against Tasmania, offer points without three-point dependence. Melbourne last game produced extreme Cairns single-game conversion. Cairns Pinder and Bolden can contend for boards; both clubs have turnover/control risk under primary-guard pressure. Team-level season-adjusted possession counts, ORtg, DRtg, FTA and rebound denominators were **not independently verified**, so no false numeric efficiencies were invented.
- **Recent opponent adjustment:** Sydney defeated both; Cairns also lost to Adelaide and NZ before defeating Melbourne. Brisbane beat NZ and Illawarra, lost at Sydney and to Tasmania in OT. Opponent-adjusted ratings lack sufficient archived point-in-time inputs for a fitted model; low-sample volatility widens rather than justifies large departures. No playoffs/series.

#### C. Transparent coherent full-game joint score scenario

- **Anchor calculation:** using regulation means, simple attack-vs-opponent-defence midpoint estimates: Cairns (86.8+91.0)/2 = **88.9**; Brisbane (90.0+94.8)/2 = **92.4**. A pooled +3.5 home-court differential and a tentative +1.5 difference for current player availability/recent observed form give **home expected 91.4, away 89.9**; combined mean **181.3**, home-minus-away mean **+1.5**. These shifts are *analyst assumptions* (not fitted effects), with substantial model uncertainty. `TEAM_BASELINE_P (TB-1-MD): NOT_COMPUTED`; no claim of registered baseline qualification or measurable edge.
- **Width:** historical NBL basketball reference `SD(total)=18.7`, `SD(margin)=15.2` points, adopted without narrowing; correlation of latent total/margin `rho=-0.05` (scenario assumption). Overtime mass `P(OT)=0.048`, in league-referenced ~4–5.5% range, with pre-OT 4-quarter tie and an additional approximately 22 combined OT points. All derivations from one discrete home/away final-score grid with non-OT (95.2%) and OT (4.8%) branches; aggregate output normalizes to 1.
- **Numerical receipt:** `P-552_MODEL_RECEIPT.json`, plus deterministic script `P-552_MODEL_CALCULATION.py`. Distribution over integer scores; non-OT conditioned non-tie, OT conditioned tied regulation then two independent Poisson scoring increments conditioned non-tie. Exact operator OT semantics remain unknown; predictions refer to standard full game including OT *only*.
- **Primary predicted score illustration:** **Cairns 91 – Brisbane 90** (illustrative integer score near mean, not a likely exact scoreline). Expected combined about **181**. Small player-availability changes, shooting volatility or 3P concentration can move these scenario probabilities materially.
- **Score distribution checks:** P(CNS wins) **0.5405**, P(BRI wins) **0.4595**; P(CNS margin>=3) **0.4805**, P(BRI margin<=2) **0.5195**; P(total<=188) **0.6285**, P(total>=189) **0.3715**. Push mass for half-point lines zero (completed game). Spread pair 1.0000, total pair 1.0000, winner pair 1.0000.
- **Scenario branches:** (i) low-efficiency half-court game and mild scoring suppression -> under, (ii) Cairns guard return enables tight home win, (iii) Brisbane Velička bounceback and Harrison rim/offensive board scoring -> Brisbane wins/cover, (iv) rapid shooting pace and sustained threes from Reyne Smith/Mackinnon -> over, (v) 4.8% OT tail -> total over and a late win/cover flip. Late fouling and team foul bonus remain in full-game variance; not fitted separately. **Over 188.5 AND Cairns -2.5 joint mass approximately 16.90%**, illustrating dependent risks, not independent picks.

#### D. Four ranked exact propositions (ranking by p_card; no demonstrated RM-1 q edge)

| Rank | Exact supplied proposition (full game incl. OT) | p_card | Status | Supporting evidence | Principal failure route |
|---|---|---:|---|---|---|
| **1** | **COMBINED TOTAL UNDER 188.5 points** | **62.85%** | `UNCALIBRATED_ANALYST_SCENARIO` | Regression after Cairns' 202-point previous game; Brisbane's last 208 included OT and was 182 regulation; 181.3 projected mean against 188.5 | Cairns/Brisbane both shoot efficiently from three, fast possessions, late fouling or overtime |
| **2** | **Brisbane Bullets +2.5 points** | **51.95%** | `UNCALIBRATED_ANALYST_SCENARIO` | Narrow projected Cairns margin 1.5; Brisbane Harrison rim play, Velička creation, recent OT competitiveness | Cairns controls turnover/defensive glass, McVeigh/Pinder/Brown carry offensive momentum, wins by 3+ |
| **3** | **Cairns Taipans -2.5 points** | **48.05%** | `UNCALIBRATED_ANALYST_SCENARIO` | Home court, Bruce available, Pinder/McVeigh and Brown creation, Melbourne comeback | Brisbane wins outright or loses by 1–2; Brisbane guard and Harrison execute effectively |
| **4** | **COMBINED TOTAL OVER 188.5 points** | **37.15%** | `UNCALIBRATED_ANALYST_SCENARIO` | Both teams have shown scoring bursts; OT tail; potent McVeigh/Pinder and Harrison/Mackinnon options | Half-court slowdown, turnover clusters, poorer three-point shooting; no overtime |

**Most likely full-game winner:** **Cairns Taipans 54.05%** (Brisbane 45.95%), including OT; low confidence/essentially coin-flip at model error scale. Preferred ranking is not a betting recommendation and confidence in numeric precision is low. Ranks 2 and 3 are a dependent complement; ranks 1 and 4 are a dependent complement. `RM-1 q: NOT_VALIDATED/NOT_CALCULATED` because calibrated baseline and contract-specific priors not available; straightforward scenario p_card used with disclosure.

#### E. Conditions, compliance and failure audit

- `NO_DEMONSTRATED_PROSPECTIVE_SKILL` / `NOT_CERTIFIED`, no training on the user-selected D0 log, no promoted numerical NBL lane. Position/scoring evidence season-opening small sample, official starting five and individual minutes not confirmed. Source independence not demonstrated; only first-party field owners and historical official box/reports used.
- No odds, market prices, implied probabilities, bookmaker analysis or in-play data were consulted for forecast adjustments. Source-scoping firewall remains `SPORTS_ONLY / MARKET_BLIND`. Line definitions assumed full game incl OT, operator specific settlement unknown.
- Tip had been scheduled before research timestamp; **do not label frozen before tip or performance-eligible**, even if start later delayed. This card is deliberately late/start-unverified and draws only from news/current stats available ahead of the match; `IN_GAME_EVIDENCE_USED: NO`.
- **No result search, NO W/L/P, NO retrospective or settlement.** All unresolved carryover states retained.

**Sources (original sporting/official evidence):**
- https://www.nbl.com.au/news/how-to-watch-talking-points-cairns-taipans-v-brisbane-bullets
- https://www.nbl.com.au/news/nbl26-the-latest-injury-updates
- https://www.taipans.com/news/game-day-update-8-october
- https://www.taipans.com/news/game-preview-taipans-v-bullets-nbl27-round-4
- https://www.brisbanebullets.com.au/news/preview-r4-away-v-cairns
- https://www.brisbanebullets.com.au/news/recap-bullets-lose-entertaining-ot-contest
- https://www.nbl.com.au/news/kings-lock-down-bullets-to-go-3-0
- https://www.nbl.com.au/news/jackjumpers-prevail-over-bullets-in-ot
- https://www.nbl.com.au/club-schedule/cairns
- https://www.nbl.com.au/club-schedule/bri
- https://www.taipans.com/
- https://www.basketball.com.au/games/brisbane-bullets-v-tasmania-jackjumpers-men-03-10-2026

**Local forecast custody:** One unique new event `P-552`; `CANONICAL_IMPORT_STATUS: PENDING`; exact event/alias duplicate check against P-550/P-551/local carryovers; new card written to this local mini only. If already in GitHub under another canonical ID at later reconciliation, keep local P-552 stable and explicitly map it; no silent renumber.

---

## P-553 — Kobe Storks vs Chiba Jets — B.PREMIER — 2026-10-08

- **Working identity:** `P-553`; alias `LOCAL-20261008-P-553-BP-KOB-CHJ`; official league match key `506439`; `CANONICAL_MAPPING: PENDING_IMPORT`; GitHub main HEAD `1ffbd9f52c63926bf7b1f5df9796e37477c1e9a3`, repository next canonical ID `P-550` (unchanged). LOCAL next after issue P-554.
- **Recording timestamp:** `2026-10-08T21:03:35+11:00` Australia/Melbourne. Official published tip: 19:05 JST = 21:05 AEDT, 8 October 2026, GLION ARENA KOBE. `ANALYSIS_STATUS: PREGAME_ISSUED_START_UNVERIFIED`. Actual jump ball and officially authenticated starter list not verified. **No observed current-match play, score, lines or final used.** Period: four 10-minute quarters plus 5-minute OT periods if tied. Full game including OT assumed; exact operator-specific OT/void semantics remain `UNKNOWN_DEFINITION`.
- **Sport / competition:** Basketball / Japan 2026–27 B.LEAGUE PREMIER men's regular season; home Kobe Storks, away Chiba Jets, both entered with 1–3 records. Not a playoff or series. `SPORTS_ONLY/MARKET_BLIND`, no odds or implied-price inputs. Method MDS-2026.10.01-v8.0, control CR-2026.10.08-R3, basketball rules §0. Not a calibrated production lane, `PERFORMANCE_ELIGIBILITY: NOT_CERTIFIED`, `MODEL_STATUS: UNCALIBRATED_ANALYST_SCENARIO`.

### Pregame research and availability

- **Kobe results:** vs Osaka L 69–79 on Sep 26; W 84–78 on Sep 27; at Hiroshima L 73–96 on Oct 2; L 72–83 on Oct 4. Aggregate **74.5 scored, 84.0 conceded**, 39.1% FG (25.3/64.5), **26.7% 3P (7.0/26.3)**, 17.0/23.3 free throws, 40.5 RPG, 17 APG, 13.3 TOPG. Home this season 1–1; away 0–2. Osaka/Hiroshima opponent-strength imbalance limits any home split conclusion. B2 2025–26 55–5 is lower-division data and not pooled unadjusted with B.PREMIER.
- **Chiba results:** at Tokyo SR W 97–92 Sep 25; L 79–95 Sep 26; vs Alvark Tokyo L **131–138 on Oct 2 after *FOUR* five-minute overtime periods**; L 71–96 Oct 4. The quadruple-OT game was 97–97 after 40 minutes. **Regulation-only team scoring across four: (97+79+97+71)/4=86.0 PPG; opponent regulation conceded: (92+95+97+96)/4=95.0**. Official unadjusted full-game 94.5 scored / 105.3 conceded and 88.3 PACE are **OT-distorted** (225 team-player minutes per game, versus the normal 200, due to 4OT). Other official totals: 41.8% FG, 28.5% 3P (37/130 season), 75.5% FT (71/94), 45.5 RPG, 19.8 APG, 11.8 TOPG. Away record 1–1. Four-OT fatigue from six days earlier, plus Oct 4 game, adds uncertainty; neither is on a conventional back-to-back before Oct 8.
- **Kobe player exposures (pregame historical):** Yori Childs 18.0 PPG, 34:57 MPG, 8.5 RPG, 4.8 APG and 9.5 FTA PG; Fardaws Aimaq 15.8 PPG, 30:53 MPG, **12.3 RPG**; Shuto Terazono 11.5 PPG, 26:20 MPG, 5.3 APG; Asato Ogawa 8.3 PPG, 12:32 MPG, 47.4% 3P in small sample; Hayato Yamaguchi 5.0 PPG at 27:48 MPG, only 16.7% 3P. Jalen McDaniels 6.3 PPG, 17:39 MPG. Large starters' workloads and offensive-rebounding second chances are important.
- **Chiba player exposures (pregame historical):** Nate Williams **30.0 PPG**, 35:22 MPG, 55.3% FG, 9.8 FTA PG (four-OT minutes inflate some averages); Yuki Togashi 16.3 PPG, 24:37 MPG, 4.5 APG, 32.3% 3P; Yuta Watanabe 14.3 PPG, 30:47 MPG, 6.5 RPG; Luke May 11.5 PPG, 31:07 MPG, 12.3 RPG; Ryuku Segawa 7.3 PPG, 21:12 MPG, 4.0 APG; Ren Kanechika 6.0 PPG, 22:19 MPG. Matt Costello has only one 6:52 appearance, availability/role unclear.
- **Official injury status:** Chiba **Brandon Randolph registered on injury list September 9; return ineligibility through October 9** (left hamstring injury). The league note says he cannot be re-registered until after the date and removal application. Do not assume active tonight. Additional injuries hinted in Yuki Togashi's 2 October remarks, but no independently current named game-day list obtained. Kobe named-out injury changes and both active 12-player rosters unverified. Starting fives **NOT CONFIRMED**. Expected major minutes are descriptive recent averages; actual starting role, substitution choices and restrictions remain unverified and widen forecasts.
- **Basketball mechanisms:** Kobe's interior Childs/Aimaq rebounding and foul drawing challenge Chiba's short-handed front court; Chiba's Williams/Togashi/Watanabe have superior individual scoring threat. Both clubs shot **below 29% from three in the four-game sample**, creating two-sided regression and tail risk. Turnovers modest advantage Chiba (11.8 vs Kobe 13.3 per game), though OT biases Chiba's figure. Chiba has a much higher shot-attempt rate because OT inflated the 4-game average. Sample sizes tiny; raw pace/efficiency **must not be assumed neutral**. Comparative opponent adjustment from Tokyo SR/Alvark for Chiba and Osaka/Hiroshima for Kobe is qualitative, not fitted.

### Single coherent full-game scenario (including explicit OT branch)

- **Regulation-time anchor:** Kobe scored 74.5, Chiba conceded **95.0 in regulation**, midpoint 84.75. Chiba scored **86.0 in regulation**, Kobe conceded 84.0, midpoint 85.0. To capture B.PREMIER transition, quality of previous defensive opponents, Kobe's low 3P shooting and venue, use analyst-adjusted **Kobe mean 81.0, Chiba mean 86.0**, mean total **167.0**, home-minus-away **−5.0**. The ~−3.75 Kobe adjustment is judgment, **not a fitted or independently calibrated coefficient**. No league-specific B.PREMIER total/width benchmark has been validated. `TEAM_BASELINE_P: NOT_COVERED` for this league.
- **Joint regulation distribution:** integer home and away scores 35–144, with approximately Gaussian total mean 167.0 SD 19.5, margin (home−away) mean −5.0 SD 15.0, correlation −0.08; conditional on a no-tie result, mixture weight 96%. Remaining 4% is tied regulation, modelled with a drawn tied score and independent Poisson(10) five-minute OT contributions, conditioned non-tie. All outputs from this **same** mixture, not independent guesses. The 4% OT probability is an unvalidated basketball scenario parameter. Detailed receipt and reproducible code retained alongside this mini. Normalisation and complement consistency verified.
- **Representative score:** Kobe Storks **81**, Chiba Jets **86**, total **167**; this is the model mean illustration, not a claim about the exact score. Overtime, fourth-quarter foul strategy, rested rotation uncertainty and 3P volatility affect the tails. Match could be much faster; credible uncertainty spans roughly 20 points on total and 15 on margin (scenario, not empirical B.PREMIER validation).

### Four ranked propositions (provisional full-game incl OT)

| Rank | Exact proposition | p_card | Status | Supporting evidence | Principal failure route |
|---|---|---:|---|---|---|
| **1** | **COMBINED TOTAL UNDER 171.5 points** | **57.63%** | `UNCALIBRATED_ANALYST_SCENARIO` | 167-point scoring mean, Kobe 74.5 PPG and 26.7% 3P, Chiba 94.5 PPG badly distorted by four OT periods; both teams' official shooting below 29% from three | Williams/Togashi explosive shooting, Kobe 3P rebound, fouling/high possessions or five-minute OT |
| **2** | **Kobe Storks +6.5 points** | **54.37%** | `UNCALIBRATED_ANALYST_SCENARIO` | Projected Chiba win margin around five, Kobe at home with Childs/Aimaq rebounding and FTA, Randolph unavailable for Jets | Chiba's shot creators produce early separation and Kobe's weak shooting persists, Jets win by seven or more |
| **3** | **Chiba Jets -6.5 points** | **45.63%** | `UNCALIBRATED_ANALYST_SCENARIO` | Chiba's higher-quality individual creators and Kobe's weak four-game offense/defensive pressure; win-by-7 path exists | Kobe's offensive boards, home tempo and Chiba's injuries keep margin within six or Kobe wins |
| **4** | **COMBINED TOTAL OVER 171.5 points** | **42.37%** | `UNCALIBRATED_ANALYST_SCENARIO` | Chiba has scored 97 twice in *regulation*; Kobe's home match against Osaka reached 162 with some potential shooting regression; OT/FT tails | Kobe's struggling outside shooting and 40-minute defensive control suppress both teams' scoring |

**Most likely full-game winner: Chiba Jets 62.85%** (Kobe 37.15%), **low-confidence, uncalibrated**. The winner call does not imply -6.5 cover. Complementary spreads/totals are dependent rows, not independent bets. `RM-1 q: NOT_ESTIMATED`; no validated family-specific calibration or ranking prior. No alternate unsupported contract introduced.

### Audit, source custody and limitations

- Both teams 1–3 in this season; tiny opponent-adjusted sample; no demonstrably calibrated Japan B.PREMIER A2 engine. No market/price evidence considered. Official in-game and final match data excluded by design. Actual first possession/start not verified; if timestamp is after planned start, label late and **not** authenticated pregame.
- Official starters, active player list, late withdrawal list and exact operator-specific OT/void rules remain `UNVERIFIED`; cannot claim a fully compliant injury/lineup gate or `LIVE_QUALIFIED` status. No player game-prop forecast.
- **Official/sporting sources before tip:** https://www.bleague.jp/game_detail/?ScheduleKey=506439&tab=1 ; https://www.storks.jp/schedule/list/?month=10&year=2026 ; https://chibajets.jp/schedule/list/?month=10&year=2026 ; https://www.storks.jp/stats/ ; https://chibajets.jp/stats/ ; https://www.alvark-tokyo.jp/news/detail/team/id=261002 ; https://www.bleague.jp/media_news/detail/id=624329 ; https://www.bleague.jp/news/injury.html?lang=hb ; https://www.bleague.jp/bmagazine/detail/id=625105 .
- **No settlement, retrospective, grading, W/L/P or results for this event performed.** `LOCAL_WORKING_ID: P-553`; `CANONICAL_IMPORT_STATUS: PENDING`. Keep all prior P-550/551/552 originals verbatim.

---

## P-554 — Nagasaki Velca vs Shinshu Brave Warriors — B.PREMIER — 2026-10-08

- **Local custody:** `LOCAL_WORKING_ID: P-554`; alias `LOCAL-20261008-P-554-BP-NAG-SHI`; B.LEAGUE match key `506440`. `CANONICAL_MAPPING: PENDING_IMPORT` (`GitHub main` HEAD `1ffbd9f52c63926bf7b1f5df9796e37477c1e9a3`; repository next official canonical ID still `P-550`). The next **local** working ID after this card is `P-555`.
- **Event/time:** Nagasaki Velca HOME vs Shinshu Brave Warriors AWAY, B.LEAGUE PREMIER 2026–27 regular season, Happiness Arena, Nagasaki, **8 October 2026, 19:05 JST = 21:05 AEDT = 20:05 AEST**. Schedule source predates game. League uses four 10-minute quarters and 5-minute overtime, repeated as necessary.
- **Timing integrity:** research undertaken after the scheduled 21:05 AEDT start. Actual tip was **not independently authenticated**. `TIMING_STATUS: LATE_OR_IN_PROGRESS_START_UNVERIFIED`. This is a retrospective *construction of a pregame-input analyst scenario*, **NOT a certified pre-tip prediction**. Pregame inputs (4 earlier games, player stats published by Oct 7, official Oct 5 injury list, dated pregame previews) only. **NO current-match scores, first possessions, period play, live rotations or final result observed/used.** Do not settle or grade as prospective.
- **Status:** `UNCALIBRATED_ANALYST_SCENARIO`; `LEARNING_ONLY`; `NOT_PERFORMANCE_ELIGIBLE`. Method `MDS-2026.10.01-v8.0`, control `CR-2026.10.08-R3`, basketball §0, `SPORTS_ONLY/MARKET_BLIND`, supplied lines used only as thresholds, no odds.

### A. Verified pregame fixture, form and matchup

- **Current record and offense/defense:** Nagasaki 0–4, **70.8 PPG scored/87.0 PPG conceded**; Shinshu 2–2, **87.8 PPG scored/87.3 PPG conceded**. These are **full-game official aggregates**, Nagasaki includes its overtime game in Kyoto; do not portray as regulation-only. Nagasaki last four results versus Shimane (64–89, 78–85) and Kyoto (76–84 OT, 65–90); Shinshu versus Toyama (85–99, 99–81) and Yokohama B-Corsairs (78–85, 89–84). Nagasaki has faced stronger modern B.PREMIER opposition than Shinshu's mix; Nagasaki's 2025–26 championship is a material, but roster-changed, strength prior. **Current-vs-prior separation not numerically fitted.** Both last played Oct 4, three calendar days earlier (rest broadly symmetric), Nagasaki travelled back from Kyoto to home, Shinshu travels from the Yokohama region through its Nagano base to Kyushu, exact travel logistics unverified. Regular season, no playoff/series urgency.
- **Shot/rebounding comparison (four-game small sample):** Nagasaki FG **43.4% (105/242)**, 3P **29.8% (31/104)**, FT **63.6% (42/66)**, rebounds **31.5/game**, offensive rebounds **7.5/game**, turnovers **14.5/game**, assists **16.5/game**. Shinshu FG **40.7% (109/268)**, 3P **29.8% (37/124)**, FT **75.0% (96/128)**, rebounds **47.3/game**, offensive rebounds **17.8/game**, turnovers **15.8/game**, assists **18.0/game**. Shinshu's +15.8 total rebounding rate, huge offensive board opportunities and 32 FTA/game versus Nagasaki's 16.5 are the most tangible matchup threats; rebound denominator/opponent shooting must be considered, not interpreted wholly as player dominance.
- **Possession approximations (not official pace):** possessions~FGA−offensive rebounds+turnovers+0.44×FTA: Nagasaki **74.8**, Shinshu **79.1** per game. The 4-game sample, Nagasaki OT game, possession formula and shot miss rates induce significant pace uncertainty. Nagasaki has struggled to create FT and second chances; Shinshu's shooting is not efficient enough to assume uninterrupted scoring.
- **Opponent-adjusted caution:** Nagasaki's previous losses to Shimane and Kyoto are higher-quality opponents than some Shinshu opponents, so raw 0–4 vs 2–2 is *not* a fitted point margin. Nagasaki at home offers a rebound path; do not simply imply the 2025–26 championship roster is unchanged. Current opponent-strength coefficient **not estimated**.

### B. Players, availability and role exposure — only pre-existing evidence

- **Official major Nagasaki minute/scorer exposure (4 games):** Jarrell Brantley **18.0 PPG/30:16 MPG/6.8 RPG**; Levi Randolph **17.8 PPG/31:52 MPG/3.8 APG**; Yudai Baba **15.8 PPG/34:01 MPG/7.3 RPG**; Masaki Morikawa **7.5 PPG/27:30 MPG**; Wataru Kumagai **3.0 PPG/27:51 MPG/3.8 APG**. Morikawa has resumed playing after an extended injury absence; historical sample limited. Brantley/Randolph/Baba account for much of scoring creation; guard shooting and rebounding vulnerabilities matter. Bench roles and replacement minute efficiency cannot be quantified from current sources alone.
- **Official major Shinshu exposure (4 games):** Mike Daum **22.5 PPG/29:50 MPG/11.3 RPG**, including 2.8/6.0 threes per game (45.8%), 7.8/9.5 FT per game; Kevon Harris **18.0 PPG/27:10 MPG/5.3 APG**, 5.8/7.3 FT/game; Marcus Lee **10.3 PPG/29:05 MPG/9.8 RPG**, 72.7% FG (16/22) on restricted inside attempts; Eliet Donley **11.8 PPG/20:25 MPG**; Daiki Tsuchiya **7.5 PPG/19:52 MPG**; Takatoshi Furukawa **7.0 PPG/23:54 MPG**. Daum's 45.8% 3P is based on **11 made/24 attempted** threes — a volatile four-game rate.
- **Confirmed out:** Nagasaki forward/centre **Akil Mitchell**, injury list 29 Sep through earliest re-registration 29 Oct, right biceps femoris/hamstring injury; cannot legally play this match under the league's injury-list registration rule. This is important against Daum/Lee's interior size and offensive boards. Masaki Morikawa's prior injury-list status was removed 28 Aug; he has played all four 2026–27 matches. No registered Shinshu player was found on the league's Oct 5 list, **but lack of listing does not prove full health or game-day active status**. Both confirmed starting fives, exact active benches, game-time injuries and minute caps are **UNVERIFIED**; historical minutes are illustrative exposure only, not confirmed tonight. `BK-P2: NOT PASSED`.

### C. One coherent analyst-score distribution

- **Available numerical anchors:** unadjusted PPG/allowed midpoint Nagasaki (70.8+87.3)/2 = 79.05, Shinshu (87.8+87.0)/2 = 87.4; that yields raw total **166.45** and raw home margin **−8.35**. Those estimates were *not* accepted without shrinkage: Nagasaki was last season's B1 champion with changed roster, has home court and opponent-quality context, while Shinshu's offensive rebounding/FTA and Mitchell's absence counteract that. Analyst judgement sets **regulation home 80, away 83, total 163, home margin −3**. These are **not fitted adjustments**; a 3.45-point reduction in total from the crude midpoint is a conservative pace/scoring regime assumption and a 5.35-point shift of margin towards Nagasaki is an informal prior/home/opponent-quality adjustment. `TEAM_BASELINE_P: NOT_COVERED` for exact Japan B.PREMIER league; no calibrated historical game family.
- **One score model:** discrete final team scores home and away 30–160. Regulation branch **95.5%** (T mean 163, SD 19.5; home−away M mean −3, SD 15; correlation T/M −0.06), exclude final ties, and separate OT branch **4.5%** (T mean 180, SD 21; final M mean 0, SD 6, exclude ties). Normalise each bivariate branch into a joint integer score PMF and mix. OT branch is assumption, not league-calibrated; approximates resolved OT rather than precise possession-by-possession tie mechanics. Scoreline illustration **Nagasaki 80–83 Shinshu**. Receipt stored separately `P-554_SCENARIO_RECEIPT.json`. All sides/winner/totals derived from the **same** PMF, with no independent guesses.
- **No certified pace/efficiency or total width:** four-game possessions with an OT, new championship roster and no team-level lineup-stint possession data. Normal joint SD20-ish is analyst width, not a validated B.PREMIER reference. Full-game including OT *assumed* for generic lines; sportsbook/operator-specific regulation/OT/void clauses `UNKNOWN_DEFINITION` until operator supplied. Distinct complementary rows are correlated outcomes, not separate trials. No odds used; `RM-1 q: NOT_ESTIMATED`.

### D. Best four literal supplied contracts (full game including OT, provisional)

| Rank | Exact issued proposition | p_card | Probability status | Supporting pregame evidence | Principal failure route |
|---|---|---:|---|---|---|
| **1** | **Shinshu Brave Warriors +4.5 points** | **68.7%** | `UNCALIBRATED_ANALYST_SCENARIO` | Current +17 PPG over Nagasaki, 47.3 vs 31.5 RPG and 32 vs 16.5 FT attempts, Mitchell out; Nagasaki's home/champion prior narrows projected defeat to three so Shinshu covers by win or narrow loss | Nagasaki's defending-champion core and home-court offensive regression, reduced Shinshu 3P/FT conversion, or early separation; Velca wins by 5+ |
| **2** | **COMBINED TOTAL UNDER 164.5 points** | **51.7%** | `UNCALIBRATED_ANALYST_SCENARIO` | Nagasaki's four scored totals 64/78/76/65, limited boards and FT, current 29.8% 3P both sides; 163-point assumed reg total | Shinshu's offensive rebounds and huge FT opportunity plus Nagasaki home shooting recovery, late fouling, overtime |
| **3** | **COMBINED TOTAL OVER 164.5 points** | **48.3%** | `UNCALIBRATED_ANALYST_SCENARIO` | Shinshu 87.8 PPG and allowed 87.3, Nagasaki conceded 87.0; 32 FTA per game for Shinshu, high possession branch and overtime could lift score | Nagasaki's league-poor offense, depleted frontcourt/shot creation and weak 3P/FT finishing drag scoring down |
| **4** | **Nagasaki Velca -4.5 points** | **31.3%** | `UNCALIBRATED_ANALYST_SCENARIO` | Defending 2025–26 B1 champion remains home with Brantley/Randolph/Baba and 2025–26 strength prior; a win by 5+ path exists | Shinshu's rebounding and FTs, Nagasaki 0–4 offensive issues, and absent Akil Mitchell make clear margin less likely |

**Full-game winner:** **Shinshu Brave Warriors 57.8%**; Nagasaki Velca **42.2%** — LOW confidence, *uncalibrated*. Winner probability need not equal +4.5 cover. Sensitivities: a five-point move towards Nagasaki can reverse outright favourite; small total centre moves can flip O/U order. Do **NOT** portray this as a qualified pregame probability or publish as verified pre-tip card.

### E. Source/time audit, no-game-play guarantee

- Primary official: B.LEAGUE fixture/season table and club statistical tables; official 5 Oct injury register and Nagasaki 29 Sep Mitchell notice; season roster/manager club releases, source-date 7 Oct/earlier. Official league pregame 8 Oct 11:00 JST editorial used only where published before 19:05 JST. Source urls:
- https://www.bleague.jp/game_detail/?ScheduleKey=506440&tab=1
- https://www.velca.jp/lp/game_20261008/
- https://www.bleague.jp/club_detail/?TeamID=2488
- https://www.bleague.jp/club_detail/?TeamID=716
- https://www.velca.jp/stats/
- https://www.b-warriors.net/stats/
- https://www.bleague.jp/news/injury.html
- https://www.velca.jp/news/detail/id=50949
- https://sports.yahoo.co.jp/official/detail/2026100700097-spnaviow
- https://www.b-warriors.net/news/detail/id=20391
- https://www.velca.jp/schedule/calendar/?month=10&year=2026
- https://www.b-warriors.net/schedule/list/
- https://www.bleague.jp/basketball_rule/?tab=5
- **Source restrictions:** No observed October 8 scores, player events, starters confirmed via in-progress box scores, period data, match-ending reports, market prices or betting editorial used. Actual jump-ball not authenticated. `BK-P2: FAIL` due missing verified active roster/starting five; `BK-P4: UNKNOWN_DEFINITION` for operator-specific terms. Information quality limited, but user authorized explicit uncalibrated research scenario.
- **NO settlement, retrospective, retrospective scoring, card revision, historical forecast change, GitHub/Combined Log/canonical ledger writes.** Keep P-550 / P-551 / P-552 / P-553 retained text intact. Local ID P-554 is **NOT** the repository-assigned canonical ID.

---

## P-555 — TENNIS / ATP SHANGHAI MASTERS — Vít Kopřiva vs Zizou Bergs — 2026-10-08

**LOCAL_WORKING_P_ID:** `P-555` | **Alias:** `LOCAL-20261008-P-555-ATP-SHA-KOP-BER` | **CANONICAL_MAPPING:** `PENDING_IMPORT` (repository next-ID snapshot `P-550`; P-550..P-554 retained locally) | **Record type:** `LOCAL_UNIMPORTED_EVENT`.

**Research/issue timestamp:** `2026-10-08T22:34:33+11:00` Australia/Melbourne (AEDT, UTC+11); **event time:** Thursday 8 October 2026, fourth scheduled match on Grandstand 2, not-before time unverified; user estimate 21:30 AEST = 22:30 AEDT. **Timing:** `LATE_OR_START_UNVERIFIED`, `NOT_PERFORMANCE_ELIGIBLE`; exact first point/time unverified. Official tournament page showed event `VS` when checked; that is not affirmative evidence of no play. Observed in-match stats, points, games, sets and result information were excluded. **No settlement or retrospective.**

**Method/control:** `MDS-2026.10.01-v8.0` / `CR-2026.10.08-R3`; GitHub main HEAD `1ffbd9f52c63926bf7b1f5df9796e37477c1e9a3`; `RULES_TENNIS.md` §0. Tennis status `NO_DEMONSTRATED_SKILL`; **p_card status for every row:** `UNCALIBRATED_ANALYST_SCENARIO`; `SHADOW: NO_LANE` / `LEARNING_ONLY`; **source regime:** `SPORTS_ONLY / MARKET_BLIND`.

### A. Event identity and contract gate

- **Tournament/round:** 2026 Rolex Shanghai Masters ATP Masters 1000, men's singles Round 1/R128; neither player marked `(Q)` in official draw/schedule: main draw, not this event's qualifiers. **Court:** Grandstand 2, fourth match following Munar–Brooksby, Navone–Carreno Busta, Landaluce–Struff; no guaranteed exact start.
- **Surface/format:** outdoor hard, best-of-three tiebreak sets; standard set tiebreak at 6–6 (third set not a match-tiebreak). Both players right-handed, two-handed backhands.
- **Supplied literal contracts:** (1) `Kopriva +3.5` (interpreted full-match aggregate games +3.5), (2) `Bergs -3.5` (aggregate games), (3) `TOTAL GAMES OVER 22.5`, (4) `TOTAL GAMES UNDER 22.5`. ±3.5 set interpretation is invalid for best-of-three; games interpretation used with explicit operator verification pending.
- **Operator retirement/walkover terms:** provider unknown -> `TE-P3 UNKNOWN_DEFINITION`; settlement after retirement may differ by operator; all model numbers conditional on normally completed match, not certified operator contract probabilities. Named bookmaker deliberately not accessed.
- **Medical/withdrawal status:** neither withdrawn as of the consulted official listing, but that does **not** establish full fitness or a confirmed actual start. No independently confirmed current match-day injury, medical time-out or late withdrawal report. Precise actual on-court readiness `UNKNOWN`.

### B. Dated numerical prior and current evidence

| Pre-existing comparison | Vít Kopřiva | Zizou Bergs | Source/regime |
|---|---:|---:|---|
| Approx ATP singles ranking | 68 | 38–39 | ATP event/player listings; source timestamps vary |
| Overall Elo | 1687.4 | 1781.6 | Tennis Abstract, last updated **28 Sep 2026** |
| Hard Elo | 1634.1 | 1725.5 | Same, dated 28 Sep |
| Recent hard-court serve points won | 60.4% | 65.0% | Tennis Abstract reported hard split, last-52 observation, mixed levels |
| Recent hard-court return points won | 37.2% | 35.8% | Same; sample denominators not provided in public split |
| Recent hard-court hold% | about 73.9% | 81.6% | Same, historical realised rates, not matchup-adjusted |
| Hard-court ace rate (% service points) | 5.9% | 9.3% | Same; not aces/game |
| Hard-court first serve in | 61.5% | 56.6% | Same |
| Hard-court first serve points won | 66.8% | 74.4% | Same |
| Hard-court second serve points won | 50.3% | 52.8% | Same |
| Hard-court tiebreak records | 4–6 | 8–13 | Historical hard splits, very small and non-independent |

- **Hard-surface Elo benchmark:** `P(Bergs win) = 1 / (1 + 10^(-91.4/400)) = 62.9%`; overall Elo analogue `63.2%`; neither rating current beyond 28 September. The model's 63.3% winner mass departs by less than 1 percentage point.
- **Verified recent Kopřiva form:** lost to Alex Molčan in Beijing qualifying on 28 September 6–7(3), 6–2, 6–7(8); match involved 114 Kopřiva service points, 11 aces, 6 double faults; first serve 72/114, first-serve points 55/72, second-serve points 17/36, total 72/108 displayed serve points won with slight on-screen denominator inconsistencies in source; do not use that single match as baseline. Lost Denis Shapovalov 2–6,3–6 on 25 September, after beating Jia Hu 6–4,7–5 in Chengdu. Beijing entry was qualifying; Shanghai entry is main draw.
- **Verified recent Bergs form:** Tokyo R32 loss to Jiří Lehečka 3–6, 7–6(3), 3–6 on 30 Sep/1 Oct event labelling, 104 recorded Bergs serve-point attempts with 60 first serves, 45/60 first-serve points won and 21/41 second-serve points won in Tennis.com display (minor consistency gap versus 104 total); 1 ace, 3 double faults; 0/2 break conversions and 12/14 holds. His September Davis Cup and multi-hour US Open matches indicate workload/variance, not an injury diagnosis. Approx rest one week since Tokyo, versus about ten days for Kopřiva since Beijing qualifying; travel from Tokyo or Beijing to Shanghai, precise arrival unverified.
- **H2H:** two Challenger-level matches in March/July **2021** split 1–1, one on clay and one indoor. No tour-level H2H shown. Five-year-old lower-level H2H carries minimal weight due to evolved form/surface differences.
- **Missing:** no audited per-match rolling service/return numerators and denominators for full comparable hard-court population, no first/second-serve opponent-adjusted full sample, no point-level current health confirmation, no provider retirement contract, no verified actual start time. `TE-P4` partially met with missingness; `TE-S2/S4` insufficient for calibrated fitting.

### C. Single coherent best-of-three match/set/game tree

- Tennis Abstract split input, equal-player pre-adjustment: `Bergs serve ≈ (65.0% + 100%-37.2%)/2 = 63.9%`; `Kopriva serve ≈ (60.4% + 100%-35.8%)/2 = 62.3%`. These are *not* independent point-level fitted rates; surfaces/levels differ and numerators unavailable.
- **Scenario adjustment (explicitly subjective):** Bergs service point `p=0.641` (+0.2 percentage point); Kopřiva service point `p=0.614` (−0.9 percentage point after qualitative level adjustment toward ~63% Bergs winner Elo benchmark). Rates are analyst hypotheses, **not calibrated forecasts**; they imply exact hold probabilities Bergs `81.4%`, Kopřiva `76.4%`. Do not confuse with empirical hard-surface holds above.
- Compute exact service-game hold from i.i.d. Bernoulli service points. Enumerate game-by-game set scores with alternating service and first-server 50/50, tiebreak at 6–6 with rotating serve and first point server equal to the opening server; enumerate first two sets and third only when split; aggregate both players' exact **completed-match** games. This single discrete score tree produces every row; no separately guessed handicaps/totals.
- **Branch masses:** Bergs 2–0 `34.8%`; Bergs 2–1 `28.5%`; Kopřiva 2–0 `16.8%`; Kopřiva 2–1 `19.8%`; 3 sets `48.4%` versus reference men's BO3 35.8%. Mass `1.000000`.
- Over 22.5 probability from 3-set branch `48.2%` of all match mass, from straight-set branch `10.4%`; at the 22.5 line the total is largely a deciding-set exposure.
- **Representative leading-row-consistent scoreline:** Bergs wins **6–4, 7–6** -> **23 total games**, Bergs +3 games -> **Over 22.5 and Kopřiva +3.5 both WIN**, despite Bergs winning. It illustrates one path, not an exact-score recommendation or highest-probability exact scoreline.
- **Sensitivity:** no levels adjustment `pB=.639, pK=.623` yields Bergs win 58.0%, Kopřiva +3.5 66.6%, Over 60.1%; stronger gap `pB=.646, pK=.609` yields Bergs win 68.0%, Kopřiva +3.5 57.0%, Over 57.1%. Top 2 order sensitive: narrow difference and scenario weakness explicit.
- **Coherence checks:** `P(Kopriva +3.5)+P(Bergs -3.5)=1` and `P(Over22.5)+P(Under22.5)=1` for completed match; `P(Bergs -3.5)<P(Bergs win)`; no push at half-game lines. These rows are dependent, not four independent events.

### D. Four ranked picks — conditional completed match, strongest to weakest

| Rank | Exact issued proposition | `p_card` | Probability status | Pre-existing evidence | Principal failure route |
|---|---|---:|---|---|---|
| **1** | **Vít Kopřiva +3.5 aggregate games** | **61.5%** | `UNCALIBRATED_ANALYST_SCENARIO` | Three-set branch 48.4% and close straight sets; can cover while losing match. Bergs favourite Elo does not imply games cover. | Bergs serves first and breaks Kopřiva repeatedly, winning two sets with ≥4 aggregate-game advantage. |
| **2** | **Total games OVER 22.5** | **58.6%** | `UNCALIBRATED_ANALYST_SCENARIO` | Both have recently played deciding sets; model projects near 48% three-set chance, and 7–6 sets elevate total. | Bergs straight-set control, e.g. 6–3,6–3; 20-game-or-less two-set outcome. |
| **3** | **Total games UNDER 22.5** | **41.4%** | `UNCALIBRATED_ANALYST_SCENARIO` | Bergs superior hard Elo, first-serve quality and serve hold may produce relatively quick two-set win. | Extended sets/tiebreak(s) or a full third set. |
| **4** | **Zizou Bergs -3.5 aggregate games** | **38.5%** | `UNCALIBRATED_ANALYST_SCENARIO` | Elo ~63% Bergs winner, stronger hard hold/serve; lopsided straight-set paths are live. | Kopřiva breaks often or takes a set, eroding the aggregate-game margin even in a Bergs match win. |

**Most likely match winner:** **Zizou Bergs 63.3%**, Kopřiva `36.7%`, best-of-three completed-match endpoint. **Calibration:** none demonstrated. Confidence grade: **LOW**. No official retirement settlement representation certified. Both highest-ranked rows are vulnerable to the same Bergs straight-set domination mechanism; no claim of independent picks.

### E. Sources, provenance and process gates

1. Official Rolex Shanghai Masters October 8 court list (R128 / court / order): https://en.rolexshanghaimasters.com/en/scores/schedule?dayToDisplay=8
2. Tennis Abstract weekly Elo table (as of 2026-09-28): https://tennisabstract.com/reports/atp_elo_ratings.html
3. Tennis Abstract Bergs 2026 and hard-surface splits: https://www.tennisabstract.com/cgi-bin/player-classic.cgi?f=A2026qq&p=200267%2FZizou-Bergs
4. Tennis Abstract Kopřiva recent hard split: https://www.tennisabstract.com/cgi-bin/player-classic.cgi?f=ACareerqq&p=200240%2FVit-Kopriva&q=HamadMedjedovic
5. Tennis.com Molčan vs Kopřiva (28 Sep): https://www.tennis.com/tournaments/china-open-atp/matches/a-molcan-vs-v-kopriva-2026-09-28
6. Tennis.com Lehečka vs Bergs (30 Sep): https://www.tennis.com/tournaments/rakuten-japan-open-tennis-championships/matches/j-lehecka-vs-z-bergs-2026-09-30
7. Historical Challenger H2H (2021, secondary): https://www.aiscore.com/head-to-head/tennis/vit-kopriva-vs-zizou-bergs
8. Additional event confirmation: https://www.tennis.com/tournaments/rolex-shanghai-masters/matches/v-kopriva-vs-z-bergs-2026-10-08
9. Repo authority (READ ONLY): https://github.com/danisgreat/Sports-Research , main HEAD above; `RULES_TENNIS.md`, `METHOD.md`, `CURRENT_RULES.md`, `CARD_AND_LOG_TEMPLATES.md`, current control manifest, status and canonical ledger.

**Gates:** TE-P1 PASS; TE-P2 PASS at schedule lookup only, no observed live confirmation; TE-P3 `UNKNOWN_DEFINITION`; TE-P4 PARTIAL/UNKNOWN CURRENT FITNESS; TE-P5 PASS dated 28 Sep. `SHADOW: NO_LANE`; source independence not audited, match start status UNVERIFIED. Not eligible for official performance certification.

**No pre-match contamination:** No current match point/game/set scores or results used. No sportsbook/external market probabilities, prices or editorial tips used as model input. **No settlement, no retrospective, no historical-card alteration, no GitHub/Combined Log/canonical-ledger writes**. Working `P-555` is not yet a committed canonical ID.

---

## P-556 — TENNIS / ATP SHANGHAI MASTERS — Cameron Norrie vs Dalibor Svrčina — 2026-10-08

**LOCAL_WORKING_P_ID:** `P-556` | **Alias:** `LOCAL-20261008-P-556-ATP-SHA-NOR-SVR` | **CANONICAL_MAPPING:** `PENDING_IMPORT` (repo next canonical ID `P-550` at snapshot; previous local working IDs `P-550`–`P-555` remain occupied); **record type:** `LOCAL_UNIMPORTED_EVENT`.

**Research/issue timestamp:** `2026-10-08T22:45:51+11:00` Australia/Melbourne (AEDT UTC+11). User estimated 10:30 PM **AEST**, equivalent to 11:30 PM **AEDT** in Melbourne. **Official timing**: 8 October Shanghai, Stadium Court fourth match following Van Assche vs Bu (third match not before 18:00 China UTC+8); no exact fourth-match starting time or exact first-point time certified. Official match listing displayed `VS`/upcoming at research, not proof of on-court start. **Timing status:** `START_UNVERIFIED / POTENTIALLY_LIVE`; `NOT_PERFORMANCE_ELIGIBLE` until a genuine pre-first-point freeze can be proven. **No live-match scoring, point, game, set, result, or betting-market information was used.** Research conducted after scheduled third match's not-before time, so a late-start caution is warranted.

**GitHub read-only authority:** `danisgreat/Sports-Research` `main` HEAD `1ffbd9f52c63926bf7b1f5df9796e37477c1e9a3`; method `MDS-2026.10.01-v8.0`, control `CR-2026.10.08-R3`, scoring `SCV-2026.10.01-v3`; `RULES_TENNIS.md` §0; sport skill status `NO_DEMONSTRATED_SKILL`; `SHADOW: NO_LANE`, learning-only. Every `p_card` below is `UNCALIBRATED_ANALYST_SCENARIO` (not calibrated/validated). `SPORTS_ONLY / MARKET_BLIND`.

### A. Identity and contract gates

- **Event:** Rolex Shanghai Masters ATP 1000, men's singles main-draw round 1/R128, outdoor hard at Qizhong Forest Sports City, Shanghai; best-of-three standard tiebreak sets, conventional third set (no match tiebreak). Norrie direct main draw; Svrčina qualifier.
- **Players:** Cameron Norrie (GBR, 31, left-handed, two-handed backhand, ATP approximately No. 40); Dalibor Svrčina (CZE, 24, right-handed, two-handed backhand, ATP approximately No. 124–126, feed variations). No previous ATP H2H found. Source: official event order + tennis.com/Tennis Abstract profiles.
- **Issued contract interpretations:** `Svrcina +3.5` = **+3.5 aggregate match games**; `Norrie -3.5` = −3.5 aggregate match games; `TOTAL GAMES OVER 21.5` and `TOTAL GAMES UNDER 21.5` = both players' games summed across completed match, tiebreak counts as one completed game. A ±3.5-set handicap cannot be meaningful for best of three. No market operator supplied; retirement/walkover and settlement terms `UNKNOWN_DEFINITION` (TE-P3), not certified operator action probabilities. All estimates are conditional on an ordinarily **completed** match.
- **Withdrawals/health:** Svrčina's 6 Oct qualifying opponent Yoshihito Nishioka **retired** at 2–5; that is *not* evidence that Svrčina was injured or retired. Official main-draw match remained listed; no independently verified Norrie/Svrčina current injury or withdrawal found in checked sources. Neither fitness nor first-point readiness is confirmed.

### B. Predated player statistics, strength, and exposure

| Input (historical; not current-match action) | Cameron Norrie | Dalibor Svrčina | Source/limitations |
|---|---:|---:|---|
| Overall Elo, 28 Sep 2026 | 1835.7 | 1656.3 | Tennis Abstract weekly Elo, **not** Oct 8 current |
| Hard Elo, 28 Sep 2026 | 1796.8 | 1636.3 | Surface blend, level-adjusted rating |
| Recent last-52 hard match W–L | 23–15 | 17–15 | Tennis Abstract selectable split, mixed levels |
| Hard service points won | 66.0% | 58.9% | Tennis Abstract reported percentages; raw point denominators not exposed |
| Hard return points won | 36.6% | 42.6% | Svrcina's split is against materially different opposition |
| Hard first serve in | 64.1% | 57.9% | Historical sample |
| Hard first-serve points won | 71.5% | 66.7% | Historical sample |
| Hard second-serve points won | 56.1% | 48.0% | Historical sample |
| Hard service hold rate | 84.2% | 68.5% | Observed, not opponent-adjusted matchup holds |
| Hard break rate | 20.6% | 31.8% | Return games, level sensitive |
| Hard ace rate | 6.4% | 4.3% | % of service points, not aces/game |
| Hard tiebreak record | 11–12 | 9–6 | Small samples; sample composition differs |
| Double-fault profile | Not safely quantified | Not safely quantified | No reliable matched hard split numerator/denominator extracted |

**Elo gate:** Dated overall Elo delta Norrie +179.4 => `P(Norrie win)=1/(1+10^(-179.4/400)) ≈ 73.75%`. Hard Elo delta +160.5 => `≈71.58%` best-of-three benchmark. Card model Norrie win `70.57%`, approximately 1 percentage point below dated hard benchmark. No unsupported >10-point Elo departure. Uncertainty around old benchmark is not quantitatively calibrated.

**Recent, dated form/workload:** Norrie lost to Alexander Zverev in Beijing on 1 Oct, 6–7(1), 4–6 against a high-quality opponent, with several days of rest before Shanghai. Svrčina beat Billy Harris in Shanghai Q1 on Oct 5, 4–6 7–6(6) 7–5 (about 180 minutes), then advanced Oct 6 Q2 when Nishioka retired at 2–5 after approximately 48 minutes. Thus Svrčina is acclimatised but has greater immediate match workload; qualifier opposition weaker than Norrie's most recent opponent. His lower service figures may understate/overstate relative matchup quality due level shifts. No exact confirmed pre-match medical/physical assessment and no verified flight arrival times. Source: tournament records, Tennis.com, Reuters for Zverev-Norrie.

**Styles/matchup:** Norrie's left-handed baseline patterns and higher first/second-serve productivity can protect holds against a right-handed defender; Svrčina has counterpunching and return resilience, although his observed strong break rate arose against different-level opponents. Lack of verified current point-by-point denominators or same-surface comparable H2H limits confidence. Last-52 rates are *descriptive*, not a fitted point model.

### C. One coherent match/set/game scenario — uncalibrated

- **Input scenario, *not fitted*:** `P(Norrie wins point on serve)=0.653`, `P(Svrčina wins point on serve)=0.610`. These assumptions are a qualitative compromise between historical serve/return splits, a dated Elo strength benchmark, tour-level differences, and uncertainty; no validated regression supplies their coefficients.
- **Derived exact standard tennis service holds:** Norrie `83.46%`; Svrčina `75.62%`. Markov/deuce service games; tiebreak DP; full set score distribution; two-straight/three-set trees with each side capable of winning straight or in a decider. Service order averaged approximately at set boundaries. No retirements modelled.
- **Set-count mass:** `P(three sets)=46.03%` against men's best-of-three general reference `35.8%` in `RULES_TENNIS.md`, which is significantly lower. This is a **scenario departure**, not proof of a validated high three-set regime. `P(two sets)=53.97%`.
- **Match branches:** Norrie 2–0 `41.07%`, Norrie 2–1 `29.50%`, Svrčina 2–0 `12.90%`, Svrčina 2–1 `16.53%`. All branch probabilities sum to 100%; no underdog-only-decider shortcut.
- **Mean total games:** `24.88`; expected Norrie minus Svrčina aggregate games `2.05` (does not describe a median/representative scoreline).
- **Representative jointly possible Norrie win:** `6–4, 7–6` (23 games; Svrcina +3.5 wins, Over 21.5 wins, Norrie −3.5 loses), illustrating top-two dependence, not an exact-score prediction.

| Rank | Exact issued proposition | `p_card` | Status | Evidence/reasoning | Principal failure route |
|---|---|---:|---|---|---|
| **1** | **COMBINED TOTAL GAMES OVER 21.5** | **64.31%** | `UNCALIBRATED_ANALYST_SCENARIO` | The model's deciding-set share is 46.0%, and competitive straight sets also clear 21.5. | Norrie breaks repeatedly and wins 6–3 6–3, 6–4 6–4, or another short 2–0. |
| **2** | **Dalibor Svrčina +3.5 total games** | **54.73%** | `UNCALIBRATED_ANALYST_SCENARIO` | Svrčina wins some short-return sequences, may take a set, and close Norrie wins can still cover +3.5. | Norrie dominates second serves or secures an aggregate margin ≥4 games. |
| **3** | **Cameron Norrie −3.5 total games** | **45.27%** | `UNCALIBRATED_ANALYST_SCENARIO` | Superior Elo and stronger historical hard serve create a plausible 6–3 6–4 type of win. | Svrčina returns well or extends sets sufficiently to cover +3.5. |
| **4** | **COMBINED TOTAL GAMES UNDER 21.5** | **35.69%** | `UNCALIBRATED_ANALYST_SCENARIO` | Straight-set control and multiple breaks remain a material branch. | Deciding set or two close sets. |

**Most likely match winner:** **Cameron Norrie** `p_card=70.57%`, `UNCALIBRATED_ANALYST_SCENARIO`. Svrčina `p_card=29.43%`. No independently calibrated probability.

**RM-1 / coupling:** The two supplied handicaps are complementary at the half-game threshold; the two totals are complementary at 21.5 (no push for completed integer games). All come from the **same match score PMF**. Rank-1 Over and Rank-2 underdog cushion are **dependent**, not two independent strong opportunities; one close two-set or long three-set outcome may drive both. Sensitivity runs using alternative serve-point assumptions produced Over 21.5 roughly **62.3–65.4%**, Norrie win **68.4–74.4%**, and Svrčina +3.5 **50.6–56.8%**. These are scenario-sensitivity intervals, not statistical confidence bands. The games-handicap and winner claims are from the same tree. 

**Contract/action gate:** retirement terms and operator definition unknown; `UNKNOWN_DEFINITION` applies to any retirement settlement. No claim about guaranteed action. This record is `START_UNVERIFIED`; no certification, independent source-custody audit or currently qualified tennis model. `PROPOSED_NOT_TESTED` for any future model or rule change.

### D. Source receipts (predating or independent of current match action)

1. Official tournament order of play, Oct 8 (identity, R128, `(Q)` and court order): https://en.rolexshanghaimasters.com/en/scores/schedule?dayToDisplay=8
2. ATP Tour event overview (event venue/surface): https://www.atptour.com/en/tournaments/rolex-shanghai-masters/5014/overview
3. Tennis Abstract Elo (28 Sep dated table): https://tennisabstract.com/reports/atp_elo_ratings.html
4. Tennis Abstract Norrie hard split: https://www.tennisabstract.com/cgi-bin/player.cgi?f=ACareerqq&p=111815%2FCameron-Norrie&q=ValentinRoyer
5. Tennis Abstract Svrčina hard split: https://www.tennisabstract.com/cgi-bin/player.cgi?f=ACareerqq&p=207494%2FDalibor-Svrcina&q=RioNoguchi
6. Qualifier Q2, Nishioka retirement: https://www.tennis.com/tournaments/rolex-shanghai-masters/matches/y-nishioka-vs-d-svrcina-2026-10-06
7. Pre-existing qualifying and match custody: https://tennis-db.com/matches/4698004/cameron-norrie-vs-dalibor-svrcina
8. Pre-match participant/status page (not used for displayed win probability): https://www.tennis.com/tournaments/rolex-shanghai-masters/matches/c-norrie-vs-d-svrcina-2026-10-08
9. Zverev vs Norrie Beijing dated news: https://www.reuters.com/sports/tennis/atp-roundup-alexander-zverev-carlos-alcaraz-advance-asia--flm-2026-10-01/
10. Local independent calculations: `P-556_MODEL_SCRIPT.py`, `P-556_SCENARIO_RECEIPT.json`.

**Gates:** TE-P1 PASS, TE-P2 PASS for official listing (actual first point unverified), TE-P3 FAIL `UNKNOWN_DEFINITION`, TE-P4 PARTIAL injury/fitness status unknown, TE-P5 PASS dated surface/overall Elo. Eligible numerical model: NONE LIVE_QUALIFIED. Winner/handicap/total numbers are conditional analyst scenarios, not calibrated. `SHADOW: NO_LANE`.

**No result, settlement, or retrospective was researched or appended.** No points, games or sets observed in this match entered the forecast. No sportsbook odds or editorial win probabilities entered the forecast. No GitHub, Combined Log, status or canonical-ledger files changed. Original local P-550–P-555 bodies remain unchanged. P-556 awaits a future separately authorized canonical import.

---

## E. Running ID footer

- **Highest local working P-ID actually used:** `P-556` (six new cards issued in this mini; P-550 remains original carried ID)
- **Next local working P-ID:** `P-557`
- **Repository next-ID snapshot when mini opened:** `P-550`
- **Active sporting/contract carryovers:** `34` (33 selected register + P-550 local)
- **Canonical-reconciliation carryovers:** `0`
- **Reference-only carryovers:** `32`
- **Total selected-register carryovers retained:** `65`
- **Additional local sporting carryovers:** `1` (P-550)
- **Total unique carryovers retained:** `66`
- **New event cards:** `6`
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
