# PROMPT 2 — Start a new local mini

**Mode:** LOCAL_MINI_STAGING. **Writes:** one new Markdown mini at the selected local path. **GitHub repository (`main` branch):** read-only mode (no canonical or remote writes). This task creates no card, forecast, settlement, retrospective or canonical ID.

Inputs: `Output location: <path, or choose the established mini folder>`; `Previous mini/settlement/import receipts: <paths if known>`. Locate existing files before asking for missing paths; never assume an inaccessible previous mini does not exist.

## 1. Reading and state reconciliation

Reference the GitHub repository (`main` branch) in read-only mode. Read the common controls in [README](README.md), CARD_AND_LOG_TEMPLATES §2, this prompt, GAME_LOG_STATUS_CURRENT, current canonical entry tail/dated state addenda, the latest completed import report, and [the active example](examples/EXAMPLE_ACTIVE_MINI.md). Print the receipt with actual revision/time on `main`.

Resolve active log and next canonical ID dynamically from CURRENT_STATE, current status and actual canonical records. The log's opening header is historical; do not require its old next ID to equal today. Current-record disagreement blocks allocation and is reported with exact evidence.

## 2. Inventory outstanding local work

Read previous active/settled minis and their manifests, mappings and unresolved queues. List every unimported working ID, owner mini and event key, including minis created after the last settlement. Verify local IDs form the expected contiguous unimported continuation. Account for duplicates/aliases/reservations and competing writers.

First local ID = max(current next canonical ID, highest accounted-for local working ID+1). Use that formula only after proving the sequence is accounted for; an unexplained gap or overlap blocks ID preparation. No previous mini can be reported NONE only after inspection or an explicit user statement. Creating the file consumes no ID. A previous unimported mini remains a documented dependency, not silently canonical.

## 3. Carryover

Retain two queues: non-terminal PENDING_EVENT and terminal UNRESOLVED_EVIDENCE. Copy/reference original ID, exact identity, original card path/table, frozen endpoint/definitions, latest settlement revision, remaining field, next action and known due time. Preserve LOCAL_UNIMPORTED versus canonical status accurately. Already settled rows are referenced only where needed for a partially unresolved card; never copied as new forecasts.

Report pending-event count above five as an alert and retain every record. Do not remove evidence gaps to meet a cap. Reconcile every previous queue item to carried, resolved-with-pointer or an explicitly retained disposition.

## 4. Create and read back

Create the exact mini-log-6 structure in CARD_AND_LOG_TEMPLATES §2: authority table, local-ID rules, carryover/evidence queues, empty NEW LOCAL EVENT CARDS, footer. Populate real current authority values; use explicit NONE/N/A/NOT_VERIFIED, never placeholder facts. New-card counts zero, highest new ID NONE, next working ID the reconciled first ID. No placeholder P-card headings.

If the output already exists, inspect it: exact existing empty mini is an idempotent return; a populated or different mini is never overwritten. Choose a new non-colliding name only when it represents a genuinely new lifecycle, not to escape a custody conflict.

Audit actual file readback: first/next ID match; carryover items/counts reconcile; original tables match; no candidate/card created; current destination correct; no unfilled template values. Allowed changes are only the new file. Report any inability to write as READ_ONLY_DRAFT / NOT_ISSUED.

## 5. Return

Provide the complete mini and path, authority receipt, canonical next snapshot, outstanding local ranges, first/next working ID, both queue counts and checks. State `New cards: 0; canonical IDs consumed: 0; settlements: 0; GitHub writes: 0 (read-only mode on main)`. This prompt contains no hidden game-research step; use prompt 1 for the next event.
