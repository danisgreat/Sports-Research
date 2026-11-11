# External research operation (EXT-v3 / v24.15)

This is the current protocol for several chats researching one game. Read the current
[profile](research/external/EXTERNAL_PROFILE_v24.15.md) and
[lane briefs](research/external/LANE_BRIEFS_v24.15.md). The repository writer owns one
authoritative mini. Chat outputs are evidence inputs; agreement is not independent proof.

## 1. Prepare once, then pin each event

Use the working clone outside OneDrive: `C:\Users\danie\Projects\Sports-Research`.
The previous OneDrive checkout is retained as a backup/mirror, not a second writer.
Do not run event writers on two clones. Local exclusive locks and atomic replacement
protect cooperating local processes; Git commits and hashes detect later divergence.
They do not create a distributed lock between computers or prove public publication.

Run `python -m ml external package-check`. Commit the controls, kit and parameter
artifacts before creating an event. Pin a full Git SHA; never mix upload versions.
The source access snapshot has its own observation/expiry clock, independent of
the statistical method version. The current upload index is
[research/external/README.md](research/external/README.md).

`external init` consumes EVENT, CONTRACTS, REQUIREMENTS and ARTIFACTS input CSVs
as documented in the [prior format reference](EXTERNAL_RESEARCH_PROTOCOL_V2.md).
The exact event identity, participants, original scheduled start, supplied contracts,
requirements and initial artifacts remain immutable. `POLICY.csv` adds method version,
research mode, omitted lanes and an explicit reduction reason to the manifest hash.

```text
python -m ml external init --event-csv GAME_SPEC.csv --contracts CONTRACTS.csv --requirements REQUIREMENTS.csv --artifacts ARTIFACTS.csv --out EVENT_DIR
```

Default `FULL_FIVE` assigns L1 availability, L2 history, L3 conditions/contracts,
L4 independent checking and L5 pricing. L4 waits for L1; L5 waits for all assigned
research roles and the writer's reviewed collector mapping.

For an explicitly reduced request add `--mode REDUCED --lanes L2 L3 L5 --reason "..."`.
Two to four roles including L5 are supported. Supply requirements for exactly the
chosen roles; keep critical evidence/corroboration requirements that remain necessary.
Omitting a lane does not mean its work was completed. The card must name `research_mode:
REDUCED`; it is excluded from the confirmatory five-role cohort. `FULL_SIX` adds L6,
an independent extra audit role, upstream of L5; this is a separate experimental cohort.
No sixth chat gets a second primary price or writer.

## 2. Freeze the single-research comparison before exposure

For a paired experiment, the repository researcher first completes its own supported
forecast on the same supplied contracts without seeing external returns. Calculate a
PRIMARY kit receipt and freeze it **before releasing any chat packet**:

```text
python -m ml research-ops freeze-single --event EVENT_DIR --receipt SINGLE_RECEIPT.md
python -m ml external packet --event EVENT_DIR --lane L1 --out L1_PACKET.md
```

Repeat packet generation for available roles. Packets contain actual contracts,
requirements, artifacts and exact accepted dependencies. Packet release is recorded.
The freeze command refuses a late, replaced or already exposed SINGLE. It verifies
the receipt and uses the real coordinator clock. A local record is not publication
proof; publish the frozen comparison before the evidenced start to make that claim.
An unpaired game may still be researched and retained; label `UNPAIRED_NO_SINGLE`.
Never backfill a comparator after seeing returns or outcomes.

## 3. Research clocks and evidence

Every chat reads its actual sandbox clock using:

```python
from datetime import datetime, timezone
print(datetime.now(timezone.utc).isoformat(timespec="microseconds"))
```

Run this at start and completion, and record actual source retrieval clocks. The writer
can use `python -m ml research-ops clock --out CLOCK.csv`. If execution is unavailable,
state `CLOCK_UNAVAILABLE`; do not invent timestamps. Typed chat clocks remain declared
evidence, not independently trusted timestamps. Local intake time limits future claims;
only externally retained/published evidence can establish publication.

A page with no visible publication time uses `published_at: UNKNOWN`. An actual
pre-start retrieval establishes that the observed content was accessible by that
retrieval time; it does not establish its original publication date or earlier history.
Retrieval must be offset-aware, before completion and before the evidenced start.
A known publication time cannot be after retrieval. No post-start retrieval is made
pregame by a claimed old publication. Outcome exposure remains an exclusion.

Each used source still needs reader/path permission and an OPENED access row.
Source lineage is reviewed by original collector, not domain count. One supporting
note can cover several URLs when it actually documents their collector relationships.
`research-ops review-sources --event EVENT_DIR --mapping COLLECTORS.csv --evidence NOTE.md`
accepts exact `source_url,collector_id,lineage_status` rows. Unknown remains unknown.
It does not automatically turn URLs into independent sources.

## 4. Intake, delay amendments and partial pricing

Save raw returns unchanged. `research-ops intake-batch --event EVENT_DIR --files L1.md
L2.md L3.md` handles independent roles in the listed order, retaining every refusal.
Issue L4 after L1; review collectors and issue L5 after all chosen upstream roles.
Corrections still require the exact accepted parent hash and invalidate dependencies.

An official delay does not rewrite the manifest or discard accepted originals:

```text
python -m ml research-ops delay --event EVENT_DIR --new-start ISO_WITH_OFFSET --url OFFICIAL_URL --authority OFFICIAL_AUTHORITY --observed-at ACTUAL_OBSERVATION --evidence SPORTING_NOTE.txt
```

The note must establish no play has begun and the official revised start. Observation
must be within 15 minutes of amendment; the new start must still be in the future.
Amendments are hash-chained with retained evidence. Recheck facts affected by the delay
(lineups, weather, start and conditions); replace only affected lanes. Final card/ledger
uses the effective start while retaining the original schedule. Issued/frozen events
cannot extend their horizon. A delay cannot turn an actually started game into a
pregame game. If no revised official time is available, retain NO_FORECAST research.
Changed-horizon SINGLE/FIVE pairs are excluded from the unchanged-horizon experiment.

L5 returns exactly one disposition per supplied contract: either its existing numeric
PROBABILITIES row with a verified PRIMARY receipt, or:

```text
[UNPRICED]
label,status,reason
Corners Over 9.5,UNSUPPORTED,No permitted exact-scope corners parameters
```

Allowed statuses: UNSUPPORTED, UNAVAILABLE, ALL_PUSH, NOT_VALIDATED. Reasons must be
evidence-bound. No duplicate, overlap or silent omission is allowed. Supported goals
can be priced while corners remain unpriced. All-unpriced cricket work is retained as
`READY_RESEARCH_ONLY`, never a fabricated forecast. Failed cricket simulation and tennis
form shock remain sensitivity-only. Hockey structural checks do not establish calibration.

The final card includes every contract definition, numeric rows only in PICKS_V2, and
the exact unpriced rows between `<!-- BEGIN UNPRICED LOCAL-... -->` / END markers.
Cards must match admitted L5 prices/dispositions. Unpriced rows have no rank, probability,
sporting score or invented zero. The mini/learning/ledger/binding sequence remains as
in EXT-v2, with the effective start and numeric-only ledger coverage. A zero-numeric
card uses `external append-research`; a partial numeric card uses `external append-card`.
The exclusive writer, live lease, immediate hash comparison and prefix readback remain.

## 5. Refresh sources without changing the method

Weekly, run the existing actual source audit and `write_lists`/sport-slice commands with
a date-based snapshot ID. Do not extend `checked_at`/`valid_until` without an actual audit.
Commit the new reader-access and do-not-open snapshots; update CURRENT_ACCESS.csv with
their canonical-LF hashes. For an active event:

```text
python -m ml research-ops refresh-access --event EVENT_DIR --path research/external/access/READER_ACCESS_YYYY-MM-DD.csv --commit FULL_SNAPSHOT_COMMIT
```

This appends a committed, verified snapshot activated at the actual coordinator time.
It changes neither method version nor event identity. Earlier facts use permission valid
at their original retrieval; new opens use the active snapshot. Expired observations
cannot authorize new retrieval. Changed or backdated snapshot bytes are refused.

## 6. Finish, measure and settle

Admit, append, lint, learning-check, ledger and bind using the existing commands.
For eligible FULL_FIVE comparisons freeze the current PRIMARY receipt using
`research-ops freeze-five --event EVENT_DIR --receipt FINAL_RECEIPT.md` before start.
Supply `--unpriced UNPRICED.csv` to either comparator freeze when needed. Preserve
publication evidence and the same complete contract keys. Neither command promotes a model.

Record real owner transfer/writer-review minutes with `research-ops effort --event
EVENT_DIR --category OWNER_TRANSFER --minutes N --notes "..."` (WRITER_REVIEW and
OTHER_LABOUR also supported). `research-ops report --event EVENT_DIR --out NEW_REPORT`
separates elapsed wall time, declared lane labour, actual entered effort and missing
effort. A missing time is not zero. Batch commands reduce transfer overhead but do not
simulate chat runs, source review or factual observations.

At settlement, `research-ops fact-template --event EVENT_DIR --out OBSERVATIONS.csv`
writes exact accepted fact IDs plus a claims companion. Review each against sporting
evidence and supply actual_value, CORRECT/INCORRECT/UNRESOLVED/NOT_APPLICABLE, URL,
observation time and reason. Then run `score-facts --event EVENT_DIR --observations
OBSERVATIONS.csv --final-at VERIFIED_FINAL --out NEW_SCORES`. Missing observations stay
UNRESOLVED. Projected statements are not scored as confirmed-fact accuracy. Reports
show lane/source-collector coverage and descriptive accuracy; overlapping facts are
dependent, and 20-30 games are an early diagnostic, not proof of forecasting skill.

Benchmarks retain BENCH-v1: settle first; accept exact-contract owner-supplied
post-final probabilities only; never search for prices or feed benchmarks into cards.
Run `ledger score` when such evidence exists and report missing coverage honestly.

The [current evaluation plan](research/external/EVALUATION_PLAN_v24.16.md) assesses the
first 100 eligible fully settled paired games immediately, with no week minimum or end-of-week wait. Source-only refreshes
do not restart it. Reduced/six-lane, late, exposed, changed-horizon and unpaired cases
retain separate denominators. Predictive improvement remains unproven.

## 7. Statistical release and pilot limits

The owner authorizes v24.15 before any issued v24.14 card. The 32 measured soccer
competition rows are now in the main table and upload kit; they are descriptive,
current-capture development baselines, not historical pregame evidence or calibration.
TEAM-CENTRE-v1 computes recent-team starting numbers from supported exact-scope history;
it is a separately tested shadow candidate. Missing sports and held-out coverage remain
explicit. No new player, weather, goalie or pitcher effect is invented.

A real five-chat pilot requires an actual owner-selected event/lines, genuine chat
returns, source reviews and measured transfers. Its status remains PENDING until these
exist. Offline lifecycle tests and retrospective studies do not count as that pilot.


**Evaluation collection:** `research-ops collect-comparisons --events EVENT_DIRS... --out NEW_COLLECTION` verifies the original per-event chains and exports FORECASTS.csv for `external evaluate`. It retains every source file hash and requested-event coverage. Rechaining this derived view is not new issuance or publication; original issue clocks are unchanged. Changed-horizon and separate-mode events are explicitly excluded.


**Secondary comparisons:** `research-ops freeze-reference` and `freeze-baseline` accept their separately calculated verified PRIMARY kit receipts before packet release/return exposure. They preserve distinct model identities and original issue clocks. Collection includes their verified original chains when supplied; an absent secondary comparator stays absent. Never label a single-research forecast as a league baseline merely to fill coverage.


**Required facts and partial coverage:** partial pricing does not waive a required fact for a numeric forecast. When preparing REQUIREMENTS.csv, keep identity, timing, access and facts necessary for supported numeric contracts required. Fields relevant only to an explicitly unsupported contract may be predeclared optional and retain an UNAVAILABLE reason. A genuinely missing critical shared fact still blocks numeric admission; the full research remains retainable. Never mark an attempted but missing fact DONE merely to obtain a partial card.


**Windows checkout:** use a short local path outside sync folders. The current working clone enables Git core.longpaths. For another Windows clone, set that option during clone when needed; preserve the exact-byte .gitattributes rules for historical evidence.


**Assessment policy v24.16 / EXT-EVAL-v2:** forecast/profile/kit remain v24.15. The first 100 eligible fully settled paired games trigger assessment immediately. Missing shared-contract settlements wait for their own evidence, not a calendar deadline. Freeze the first-100 cohort ordered by settlement availability and retain it with --cohort on later audits. Event-level uncertainty assumes independent games; report time/team dependence and all exclusions. READY means the assessment can be read, not that an advantage has been proved.
