# Record eligibility schema

Machine implementation: [eligibility.py](research/src/eligibility.py), [ledger.py](research/src/ledger.py), [issue.py](research/src/issue.py). Current rules: [CURRENT_RULES.md](CURRENT_RULES.md).

| Record type | Eligibility | Required custody |
|---|---|---|
| Historical literal learning | Always performance-ineligible | Original rank/log pointer; preserved missingness/conflicts |
| Provisional current observation | Never a forecast | Immutable body, exact parse/field and retrieval hash |
| Model-only shadow | Always performance-ineligible | Before-start forecast, input/build hashes, family/endpoint, full coverage |
| Prepared live draft | No issued trial yet | Complete evidence-derived admission and unconsumed proposed ID |
| Committed live issue | Pending terminal admission | Frozen universe, three independent pregame lineages, exact qualification, transaction/core/bundle hashes |
| Settlement revision | Eligible only if all gates pass | Unchanged issue core, three independent finals, audited actual start, chained correction reason |

The bundle schema is `forecast-evidence-1`; the lock schema is `pilot-lock-2`. Required source admissions bind league/parser/endpoint, upstream collector audit and event/body-specific lineage audit. Required model admissions bind exact version and family plus untouched holdout and prospective-shadow/issuer/adapter evidence. An old generic holdout pass does not qualify a new model or totals/BTTS. Current registries retain SHADOW_ONLY model status and UNKNOWN independent collectors.

Temporal gates are strict: input/artifact availability <= cutoff < issue < verified scheduled start. Pregame receipts and lineage review must be available before cutoff and sufficiently fresh. Terminal scoring additionally proves issue < actual_start and final observation after that start. A scheduled start alone is not actual start. Naive timestamps fail.

All model/card/baseline probabilities are re-derived from retained distributions joined to the exact input checksum and contract. Direct per-row p edits, mismatched state hashes, duplicate contracts, endpoint changes and unsupported adjustments fail. Integer score states and finite lines are checked. NONE adjustments cannot change state mass.

Canonical ledger records use a SHA-256 previous-record chain and file locks. Issue preparation is journaled before the append; commitment verifies the projection. A pending transaction blocks the next ID. Corrections append instead of overwriting. Historical rows can never acquire prospective eligibility through a correction.

An excluded event carries a reason. Registered fixtures without decisions, abstentions, unresolved settlements, changed bodies, missing source fields and unavailable sources remain visible in coverage. Empty scored cohorts are reported as empty, never zero loss or perfect performance.
