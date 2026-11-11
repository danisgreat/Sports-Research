# v24.14 implementation and explanation

**Owner instruction:** implement all eighteen issues in the framework review, commit the intended files and explain every change. Release MDS-2026.11.11-v24.14 / CR-2026.11.11-R2 / prompt P-2026.11.11-v24.12.

## Scope and preserved work

The starting HEAD was f79559b45183ca63a2ce5fc2611321975bae744f (v24.12). Seventy-four dirty/untracked draft files were snapshotted before editing. The related unpublished v24.13 work is included in this release, with its provenance and explicit development limits; it was not treated as a completed or certified release. [Baseline inventory and originals](../../../archive/integrity_2026-11-11_v24_14/BASELINE.csv).

All prior Combined Logs, issued originals, active minis, learning-store records and prospective ledgers are protected by a pre/post byte-hash inventory. No live card, historical probability, grade, canonical ID, source clock or player availability is fabricated. Reference-only overtime arithmetic stays outside the frozen model cycle's code; the shared competition reference parameter table remains unchanged.

## Related draft components included in the commit

- Per-sport request formats now retain official home side, winner-versus-spread interpretation, cricket format/batting order, tennis surface/best-of and the owner's ranking scope. Supplied-line ranking is explicit; an easier analyst-derived line cannot silently inflate that denominator.
- Reader-specific source auditing distinguishes ChatGPT browsing, the repository agent and strict eight-token scripts. Versioned host lists and sport source slices retain observation/expiry clocks, blocked paths and alternatives. Official social releases and received owner captures remain evidence-bound.
- The existing openfootball soccer and Cricsheet innings/phase aggregates are retained with download receipts and DATA_PROVENANCE. Raw downloads stay outside the repository. The prior held-out-competition soccer study is preserved with its input hash and decision to keep the existing reference; no new numerical advantage is inferred.
- The standalone arithmetic kit and parameter builder are included as working release files, with exact receipt verification and explicit sensitivity/uncalibrated/proxy status. The builder now writes only versioned upload/evidence files, without silently editing the frozen shared reference table.
- New learning cards require both sides' availability observations or a genuine NONE_PUBLISHED record. This does not manufacture missing historical availability or establish an injury effect.
- League-name routing is sport-specific, preventing a hockey/basketball Bundesliga from receiving soccer constants. The unfinished real-period basketball overtime reference is repaired outside the frozen cycle, with coherent score mass and numerical agreement tests.
- CORE, state, request templates, source/rule/reference documents, all eight prompts, sport briefs and indexes identify the current v24.14 method and v24.12 prompt suite. Original draft/committed source text is archived rather than erased.

## Issue-by-issue changes

| Review issue | Implemented change | Practical result / remaining evidence limit |
|---|---|---|
| 1 Event identity collisions | EV2 hashes sport, exact competition, native event ID and game number; immutable EVENT.csv binds official participants/start, LOCAL key and writer | Doubleheaders/competition collisions are distinguished; aliases/reschedules keep the native identity. Native IDs still require actual source verification. |
| 2 False independence | Merge uses centrally reviewed original collector IDs and retained review-note hashes; two domains alone are INDEPENDENCE_UNVERIFIED | Copied feeds cannot create a second collector. A reviewed provenance note is auditable judgement, not automatic source truth. |
| 3 Pregame chronology | Offset-aware clocks, publication/retrieval/completion order, official horizon and outcome-exposure gate | Late/unknown/exposed inputs are retained with refusal reasons and cannot become clean pregame evidence. |
| 4 Invalid numbers | Finite [0,1] probabilities, coherent masses, exact decisive calculation, finite lines and all-push rejection | NaN/infinity/out-of-range/undefined decisive probabilities fail. Unsupported rows retain a nonnumeric disposition. |
| 5 Weak calculation receipts | Exact output coverage, unique labels, family/side/line comparison, required hashes, trusted rerun Monte Carlo error, finite output and matching cited receipt | Missing rows, changed contracts, absent/fake receipts and inflated submitted tolerances cannot certify the calculation. |
| 6 Missing contracts/endpoint conflicts | Immutable complete CONTRACTS.csv, requirement coverage, extended single-valued conflicts, card contract_definitions | Supplied contracts and period/endpoint/action/unit are bound to the final card. Ambiguity requires an explicit scenario/revised package. |
| 7 Version declaration only | Committed artifact-byte verification, exact profile/commit, immutable manifest hash | Uncommitted, changed or mixed-release inputs cannot be admitted under a pinned SHA. Legacy check/merge is diagnostic only. |
| 8 Inflated consensus | Full-original idempotent intake, unique lane/chat runs and contract labels, explicit parented replacements | Duplicate uploads add no run/ordinal; corrections preserve originals and invalidate downstream packets. |
| 9 Empty research accepted | Exact per-lane REQUIREMENTS dispositions and matching field/access evidence; expired/blocked/unknown reader decisions refused | Empty/unattempted work cannot masquerade as completed research. Genuine unavailable/N/A results remain explicit and retained. |
| 10 Wrong competition history | Soccer and cricket exact filters; no fallback when the requested competition is missing | Form windows cannot silently mix leagues/formats. An alternative scope requires an explicit separate view. |
| 11 Mislabelled cricket form | Named BATTING_FIRST, CHASING and BOWLING_FIRST views; sample_scope and true n in rows/windows; current-capture metadata | Conditional innings samples are never presented as the last N matches or historical pregame proof. |
| 12 Simulator admission mismatch | PRIMARY rejects cricket simulation and tennis form shock; explicit SENSITIVITY and qualification/parameter basis | Development structural checks are retained without promoting a simulator or claiming exact-scope calibration. Exact arithmetic remains labelled uncalibrated. |
| 13 Manual coordination / shared mini | Dependency-bound packets, append-only intake chain, writer/lease and hash-compare atomic append, binding to central receipt/learning/ledger | L4 waits for L1, L5 waits for current L1-L4 and source review. Owner chat transfers remain manual. One writer maintains one authoritative mini. |
| 14 Incomplete publication package | Matching v24.14 profile/brief/access/source/kit files, preserved prior development outputs and provenance, package-check, generated state refresh | A committed release can be checked from a fresh checkout. Local commit is separate from remote publication; no push is implied by this owner's commit request. |
| 15 Unproven predictive benefit | Existing scoreboard/evidence labels preserved; no promotion or new sporting claims | Predictive improvement remains UNPROVEN until genuinely frozen future paired outcomes exist. Code cannot manufacture this evidence. |
| 16 Experiment does not isolate five roles | SINGLE_RESEARCH versus FIVE_LANES, reference/baseline secondaries; exact 100-event/eight-week stopping and immutable first completed-week cohort | Existing verified prospective ledger/effective outcomes drive proper scores and strata. Publication/source/causal audits remain explicit; floors do not guarantee power. |
| 17 Learning evidence missing | Learning-log readiness reports actual stored/captured availability; prospective capture requirements retained | Zero historical availability remains FEATURE_EVIDENCE_INCOMPLETE. No outcome-exposed feature backfill or invented absence effect. |
| 18 Tests weaker than promises | Negative reproductions plus real temporary-Git five-lane intake/correction/mini/learning/ledger/settlement lifecycle and cohort-stability tests | Passing checks establish mechanics only. Actual source truth, ChatGPT runtime access and predictive qualification remain separate. |

## Additional defects found while implementing

The starting draft called a missing ScoreGrid overtime method. The reference now uses the standalone kit calculation outside the cycle, with FFT full convolution replacing the repeated dense convolution. The numerical reference tests compare both implementations. This avoids changing the frozen model runtime merely to repair reference arithmetic.

Unchanged card bindings now verify the exact original card block, rather than invalidating the binding when a later unrelated game/footer is appended to the mini. A later clock does not turn an unchanged idempotent read into a new issue. New initial bindings still require pregame admission. Exclusive writer locks and immediate-before-write hash comparisons protect the append; the previous prefix is verified on readback.

Research-only append is separate from numerical admission. A full A1-A9 QUALITATIVE/NO_FORECAST record can be retained even when evidence is unavailable or the request is late. It advances only the LOCAL ordinal and correct count; no PICKS_V2, sporting grade, pregame issuance or canonical ID is invented.

## Release artifacts and provenance

The two kit CSVs are generated from the existing competition table and the retained prior draft study/simulator outputs. The builder does not silently rewrite the frozen reference table. [Prior output lineage](../framework_change_2026-11-11-1/RETAINED_OUTPUT_LINEAGE.csv) records every original external path and raw SHA-256. Access/source v24.14 files copy the v24.13 observations byte-for-byte and keep their original checked_at/valid_until dates; they are not falsely described as a fresh network audit. Simulator results remain development evidence.

The unpublished v24.13 document/code originals are preserved under archive/integrity_2026-11-11_v24_14/working_draft (Python is stored as .py.txt). Original committed versions of previously dirty files are preserved separately. The new source code stays under ml/; generated controls/evidence remain Markdown/CSV/text.

## Running the workflow

Read [EXT-v2](../../../EXTERNAL_RESEARCH_PROTOCOL_V2.md) and the [upload package](../../external/README.md). Start with package-check after committing this release, then initialize the event manifest and issue each dependency-bound lane packet. Retain raw returns through intake, review source collectors, admit the current package, append the central card, fill/check learning, ledger it, then bind the card. Existing pregame freeze/publication and settlement/import remain required. Chat 5's probabilities do not become five independent forecasts.

For future evaluation use [the registered plan](../../external/EVALUATION_PLAN_v24.14.md). Record the single-research comparator before exposing outside evidence. No comparison is backfilled once the outcome or external research has been seen.

## Verification

Executed checks, custody and the final commit are recorded in VERIFICATION.md in this folder. This implementation explanation does not substitute for those results.


Artifact admission compares canonical LF UTF-8 hashes across Windows/Git checkouts. Intake originals, forensic archives, mini prefixes and lineage notes retain raw byte hashes. New immutable package/archive paths are explicitly -text in .gitattributes; the two identities are not conflated.
