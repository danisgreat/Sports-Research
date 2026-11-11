# External research lanes (EXT-v2)

**MDS-2026.11.11-v24.14 / CR-2026.11.11-R2 / P-2026.11.11-v24.12.** Owner-authorized corrections to all eighteen review findings. Replaces the unpublished EXT-v1 draft, preserved in [the archive](archive/integrity_2026-11-11_v24_14/working_draft/EXTERNAL_RESEARCH_PROTOCOL.md). No model is promoted; prospective improvement remains unproven.

## 1. One event, five roles, one issuing writer

| Lane | Work | Dependency |
|---|---|---|
| L1 | Both sides' availability, starters, bench and late changes | Frozen event/reference/history package |
| L2 | Exact-competition form, season and true window counts | Frozen package; explicit cricket innings view |
| L3 | Start, venue, conditions, rest/travel and contract rules | Frozen package |
| L4 | Re-open L1's exact decisive claims from independently collected evidence | Accepted L1 original and source identities |
| L5 | Price reviewed merged evidence, every supplied contract | Current accepted L1-L4 and source reviews |

Chats return research inputs. One repository writer appends and freezes one final card. The owner still transfers prompts/returns between chats; the coordinator tracks dependencies and versions, not autonomous chat execution. An L1 correction invalidates L4 and L5. L5 waits for the reviewed research package.

## 2. Immutable event package

Run `python -m ml external package-check`. Commit the reviewed release before using its SHA. Prepare UTF-8 CSVs:

- Event input uses [EVENT_FIELDS](ml/research_intake.py): verified sport, exact competition, native event ID, official home/away, offset-aware start, game number, mini path, LOCAL key, issuing writer and full committed SHA. Generated fields may be blank in the input.
- Contracts: `label,family,side,line,period,endpoint,action,unit`. Every supplied line exactly once, including requested sides/directions. Ambiguous endpoints need an explicit scenario package before pricing.
- Requirements: `lane,requirement_id,side,field,required,corroboration_required`. Unique IDs; YES/NO flags. Do not remove requirements to conceal a failed search. Revised requirements are a new immutable package.
- Artifact input: `role,path`. At least kit, params, phases, access and frozen reference; also include profile, lane brief, history packs and effect table actually used. Paths must exist unchanged at the pinned commit.

```text
python -m ml external init --event-csv EVENT.csv --contracts CONTRACTS.csv --requirements REQUIREMENTS.csv --artifacts ARTIFACT_INPUT.csv --out research/external/events/EV2-...
python -m ml external packet --event EVENT_DIR --lane L1
```

EV2 hashes sport, exact competition, native ID and game number. It excludes truncated names and mutable estimated dates. Aliases/reschedules retain native identity; changed participants/contracts require a reconciled new manifest. Legacy EV keys are diagnostic discovery references only. No canonical P-ID is allocated.

EVENT, CONTRACTS, REQUIREMENTS, LANES and ARTIFACTS CSVs are bound by MANIFEST_SHA256.txt. Source reviews and the hash-chained intake ledger are separate append-only observations. Returns/refusals are retained byte-for-byte. Occupied packages are never overwritten. Late initialization allows retention, never retrospective pregame admission.

## 3. Return validation

Use the [profile](research/external/EXTERNAL_PROFILE_v24.14.md) and [briefs](research/external/LANE_BRIEFS_v24.14.md). Every return carries event, exact profile/commit, manifest hash, current input-package hash, lane/chat, offset-aware start/completion and `outcome_exposure: NONE_DECLARED`. These claims are checked against retained evidence; they are not source certification.

EVIDENCE, PROBABILITIES and ACCESS_LOG use `ml.external.SECTIONS`. REQUIREMENTS has `requirement_id,status,reason`: DONE, UNAVAILABLE or NOT_APPLICABLE. DONE needs field evidence; unavailable/N/A needs a real reason. Unattempted procedures fail. Missing required facts prevent information-complete numerical admission while their research remains retained.

Clocks satisfy publication <= retrieval <= completion and start <= completion. Admitted pregame inputs/access observations precede official start. Unknown publication clocks cannot certify decisive evidence. Late/outcome-exposed returns are retained as refused inputs for diagnostic use.

```text
python -m ml external intake --event EVENT_DIR --return CHAT_RETURN.md
python -m ml external status --event EVENT_DIR
python -m ml external intake --event EVENT_DIR --return CORRECTION.md --parent ACCEPTED_RETURN_SHA256
```

Exact duplicates return ALREADY_EXISTS. A changed lane needs its exact accepted parent. Duplicate pricing rows, mixed commits and wrong profiles are rejected. A correction makes downstream packets STALE; originals are immutable.

## 4. Source lineage and reader access

Every evidence URL needs an OPENED access row and valid clock. The pinned reader artifact must permit the host/path and be unexpired. Blocked/unknown hosts, absent decisions and listed blocked paths are refused. Refresh the versioned package or find a permitted alternate; root permission is not page permission.

```text
python -m ml external review-source --event EVENT_DIR --url https://example.org/field --collector ORIGINAL_COLLECTOR --evidence LINEAGE_REVIEW.md --status VERIFIED
```

The repository writer reviews original collection and retains the sporting-only note/hash. Two sites using one feed share a collector ID. Unknown independence stays UNKNOWN. Two reviewed independent collectors are required for corroboration; domain count alone never suffices. The lineage review is auditable judgement, not automatic proof of fact truth. Reopen exact sporting evidence and retain publication/retrieval provenance.

OWNER_CAPTURE names its real received file inside the event folder. Preserve URL/account/post time; no agent opens the blocked platform. It is one collector and still needs independent corroboration for decisive facts. Never manufacture clocks.

## 5. Exact pricing and capability

Probabilities are finite in [0,1], W/P/L coherent, final_p = W/(W+L). All-push has no decisive probability. Expected supplied contracts appear once each; final identity also binds period, endpoint, action and unit.

Each cited receipt must exist and reproduce under pinned kit/parameter/phase hashes. Verify exact row coverage, unique labels, family/side/line and finite values. NOT_USED cannot bypass a required hash. Monte Carlo tolerance comes from the trusted rerun.

The kit reports parameter basis/qualification. Family priors are labelled proxies. Reference arithmetic remains uncalibrated. Cricket simulation and tennis form shock are SENSITIVITY only: PRIMARY refuses them. Exact tennis without the shock is arithmetic, not empirical calibration. Hockey's exact regulation/OT grid is separate from the unvalidated empty-net simulator. [Simulation admission](SIMULATION_PROTOCOL.md).

```text
python -m ml external packet --event EVENT_DIR --lane L5
python -m ml external admit --event EVENT_DIR
```

READY_FOR_CARD requires five current accepted lanes, complete required facts, independent collectors where required and no unresolved single-valued conflicts. It never qualifies a predictor. Endpoint rules, stage, neutral venue, rest/travel and player statuses are conflict-checked. Scenarios need explicit reconciled packages. Legacy check/merge commands remain diagnostic only.

## 6. One authoritative mini

The central card contains A1-A9, PICKS_V2 and adjustments. Its header carries EV2 identity, external_manifest_sha256, external_packet_sha256 and contract_definitions: `LABEL=period~endpoint~action~unit` in manifest order. One central verified pricing supplies its numbers. Replicate pricing is a diagnostic comparison, never a substituted average.

```text
python -m ml external append-card --event EVENT_DIR --card COMPLETE_CARD.md --receipt CENTRAL_RECEIPT.md --expected-mini-sha256 SHA --writer WRITER
python -m ml learning-log init --mini MINI --key LOCAL_KEY --game GAME.csv --sport Basketball
python -m ml learning-log check --key LOCAL_KEY --stage pregame
python -m ml ledger add --mini MINI --key LOCAL_KEY
python -m ml external bind-card --event EVENT_DIR --receipt CENTRAL_RECEIPT.md
```

Append checks writer/lease, next LOCAL key, complete card, pricing, mini hash/footer/freeze state; takes an exclusive writer lock; rechecks immediately before atomic replacement; preserves every earlier byte before the footer; updates counts/ordinal; reads back. It assigns zero P-IDs. Binding verifies learning, adjustments, existing ledger and central receipt, then freezes the package/card relation. Unchanged reruns are idempotent. Later corrections are dated addenda.

Run the existing pregame freeze, commit and externally publish before start for a pre-start-publication claim. CARD_BOUND is explicitly not publication proof; source publication clocks remain separate.

```text
python -m ml external append-research --event EVENT_DIR --card FULL_RESEARCH.md --disposition NO_FORECAST --expected-mini-sha256 SHA --writer WRITER
```

Incomplete/late/unsupported research retains CARD markers, A1-A9, exact event key/competition/start and `<!-- RESEARCH_STATUS: NO_FORECAST -->` (or QUALITATIVE), with no priced PICKS_V2. Counts/custody advance; no numerical/pregame issuance, grade, feature or P-ID is fabricated. Real writer/access conflicts preserve a full separate draft and BLOCKED write disposition.

## 7. Settlement and evaluation

Existing prompt-3/4 settlement, effective revisions and LOCAL-to-canonical mapping remain unchanged. Capture availability prospectively; empty historical availability is a limitation, never permission to backfill outcome-exposed features.

[Evaluation plan](research/external/EVALUATION_PLAN_v24.14.md): exact 100 paired settled events, at least eight settled ISO weeks, one decision at the first completed week meeting both, identical supplied contracts and predeclared 0.01 Brier effect. Freeze SINGLE_RESEARCH before external evidence and FIVE_LANES after it, plus REFERENCE and BASELINE, in separate prospective lanes with one evidence horizon. Report effort, exclusions and competition strata. `external evaluate` uses the existing verified prospective ledger/effective outcomes; it never treats agreement as truth or promotes a model.


**Hash convention.** ARTIFACTS.csv hashes canonical LF UTF-8 text, matching the kit and committed text across Windows line endings. Returned originals, intake files, mini prefixes, source-review notes and custody inventories use raw bytes. This distinction is explicit; a newline conversion is never called raw identity. The release marks immutable packages and archives -text in .gitattributes.
