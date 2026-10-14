# Import verification

Executed external byte/CSV/arithmetic helper C:\Users\danie\Downloads\canonical_import_P585_P589_2026-10-14_custody (helper source is in Windows temporary folder, not repository). Checks are actual executions on all eleven source units; synthetic failure/recovery cases run in memory and never modify real originals. Not the retired repository validator, not sporting source certification.

| Check | Result | Evidence / limit |
|---|---|---|
| Current identity/allocation | PASS | P-584/P-585 before; all existing canonical bodies and retained mini routes searched; no collision; new sequence 585-589 and reserved 518-522 unchanged |
| Raw supplied checksum identities | PASS | Six supplied bodies match bytes/SHA in checksum inventory; JSON retained raw outside repository |
| Original/settled complete prefix | PASS | Entire 208588-byte original equals settled[0:208588], includes footer/headers/addendum |
| Full destination prefix | PASS | Entire 1474973-byte old working prefix unchanged, raw SHA ce6b0d43c9e5aa8101d46e04f5f119d488d78f56949d2877e40cc5025f9ae290 |
| Full imported cores/source blocks | PASS | Five entire original cards, one entire research addendum, five entire settlements; [byte offsets/hashes](SOURCE_BLOCK_MAP.csv); every original row/core compared, not samples |
| Sporting row arithmetic | PASS conditional on supplied results | Tennis games 13+10=23, margin 3; EuroCup quarters 100/88, total 188, margin 12; CGY 4 / ANA 2, total 6 integer PUSH/PUSH; GSW 101 / LAL 89, total 190, margin 12; BOS 6 / SJS 3, total 9,margin 3. Source truth/individual observation times not independently fetched |
| Proper-score arithmetic | PASS | All 18 decisive rows and all 6 decisive baseline pairs recomputed from literal original row precision, plus separate 10-row base-case shadow; ledger differences<1e-12 |
| Review coverage | PASS | All five R1-R12; P-585 Rank 1 loss includes 8-part review; no model output/alternate replaces original |
| Evidence/policy/queue separation | PASS | A/B vs C/E/X, operator UNKNOWN, descriptive SUPPLIED_FIRST_V1 separate from current P_ORDER_V2; P-581-P-584 no new effective revision |
| Freeze-source growth chronology | NOT_VERIFIED | Separate freeze receipt absent; inaccessible live/mnt source; current downloaded inputs stable and preserved |
| Certified/prospective performance | NOT_VERIFIED | Actual starts/known-at/lineage unverified; 1 week; no release or automatic scheduling |

## Executed synthetic edge/recovery cases

| Case | Result | Actual observation |
|---|---|---|
| balanced source and same-ID canonical nesting | PASS | accepted as expected |
| exact full rerun produces zero new units | PASS | accepted as expected |
| valid partial recovery skips one complete block; plans the other ten | PASS | accepted as expected |
| truncated block blocks recovery | PASS | rejected as expected |
| same ID with changed core blocks recovery | PASS | rejected as expected |
| duplicate exact wrapper blocks | PASS | rejected as expected |
| cross-ID nested markers fail | PASS | rejected as expected |
| mismatched END revision fails | PASS | rejected as expected |
| duplicate revision key fails | PASS | rejected as expected |
| legacy keyless settlement markers remain valid | PASS | accepted as expected |
| single revision chain valid | PASS | accepted as expected |
| competing child revisions fail | PASS | rejected as expected |
| missing revision parent fails | PASS | rejected as expected |

Full rerun compares complete wrapper bytes, not ID existence; changed/partial blocks fail before mutations. Clean partial recovery can skip completed exact wrappers and import missing whole units without new IDs. Parent-chain fixture rejects branches rather than last-row-wins. These tests validate the disclosed external import logic, not every legacy historical repository format. Existing P-581-P-584 complete revision-1 blocks are unchanged; source branch parents are all NONE for new events.

## Transformation rules (manual reproduction)

Read raw inputs as bytes; compare supplied file lengths and SHA256; require exact settled prefix. Recognise only standalone known CARD/RESEARCH ADDENDUM/SETTLEMENT BEGIN/END markers with same ID/key; require stack-balanced same-ID nesting and unique keys. Slice complete blocks including their terminating source LF. Wrap each card in canonical-md-1 and each addendum/settlement in a unique dated same-ID wrapper; write original destination bytes followed by wrappers, never decode/re-encode a core. Preserve unmarked headers/footer/carryover text in the complete raw inputs, retain four evidence leads and queues without regrading. Compute conditional Brier=(p-y)^2 and log loss=-ln(p for WIN,1-p for LOSS); exclude PUSH; compare only originally frozen identical baseline rows. Average paired rows within each of the two events, then their single ISO 2026-W42 week; no uncertainty interval for 1 week. Update current summaries, leaving old dated views readable. Byte-read every output and compare all old prefix/source slices; only explicit paths stage. Committed text conversion is checked separately; no historical normalisation silently claimed as raw identity.

## Additional complete readbacks

[Expected-score readback](EXPECTED_SCORE_READBACK.csv) independently recomputes all 20 source observed-minus-issued-mean errors; missing SDs remain missing, no cross-sport aggregation. [Committed blob receipt](COMMITTED_BLOB_READBACK.csv) checks every other staged artifact, excluding its own self-referential hash. Old committed log blob equals the raw pre-import snapshot. Participant spelling candidates use the old destination snapshot, before this append.

Whitespace: default staged check identifies only two supplied EOF blank-line diagnostics; raw inputs are immutable. Full-scope `cr-at-eol,-blank-at-eof` and strict authored-file `cr-at-eol` checks pass. No spaces/tabs or historical source bodies are edited to manufacture a clean check.
