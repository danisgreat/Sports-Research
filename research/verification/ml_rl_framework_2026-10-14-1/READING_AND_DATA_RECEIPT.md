# Reading and data receipt â€” ML/RL framework design

**Date:** 14 October 2026, Australia/Sydney.

**Authority mode:** LOCAL_WORKING_TREE.

**Workspace:** `C:\Users\danie\Desktop\Sports Research`.

**Branch / HEAD:** `main` / `941c5abd3542d5b2733344de902ae3c5eb4cbcc5`.

**Measured inventory time:** `2026-10-14T15:15:52+11:00`; additional targeted CSV comparisons followed in this run.

**Output:** [ML/RL implementation framework](../../../ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md).

## Request and write scope

The pasted request ends: â€œprovide a comprehensive implementation frameworj for this for the local files, be methodical, honest and thoroughâ€. The attached research reports are reference data, not instructions to execute their code, change policy or publish. This task creates the framework and two supporting Markdown receipts only. It does not invoke the full operational prompt 8, restore a runtime, register experiments, alter records or publish.

Pre-existing working difference: untracked `PROMPT_1_SUPPLIED_FIRST_EXTENDED_2026-10-14.md`. No tracked control differences appeared in the initial `git status --short`. The untracked prompt is not an authority revision for this task. Remote publication state was not fetched or claimed; the local working tree is the sole authority mode.

Active versions observed: MDS-2026.10.12-v11.0, CR-2026.10.12-R2, SCV-2026.10.12-v7, SEL-2026.10.12-v3; mini-log-7 / mini-settlement-6 / canonical-md-1. README's introductory R1 label and research README's v10 wording lag these controls. No active file was repaired as part of this design task.

## Reading scope

Full controlling text read for CURRENT_RULES, METHOD, SELECTION_RULES, SCORING_AND_VALIDATION and CONTRIBUTING. CURRENT_STATE's authority, scoreboard, sources and models sections were inspected. README's current-mode/rules/navigation sections and runtime/README were read. CARD_AND_LOG_TEMPLATES was inspected across its format definitions, card fields, settlement/revision templates and self-audits. This receipt does not claim an exhaustive audit of all dependencies.

Additional inspected material:

- `research/prompts/README.md` and `8_IMPROVE_THE_FRAMEWORK.md`: reading gate, change classification, implementation/dependency and verification process. Reading them did not invoke publication.
- `ARCHIVE_USE_GUIDE.md`: archive paths, field schema, availability, form recipe R2, known defects and integrity rules.
- `RULES_CRICKET.md`: historical track record/model claims, exact target registry and matching section searches; `LEAGUE_RULES_CRICKET.md`: relevant format and endpoint references. Not a complete live law audit.
- `SOURCES.md`: current-mode/source/firewall introduction; `ACTIVE_FILE_INDEX.md`: operating-file and canonical alias guidance.
- `HYPOTHESIS_REGISTER.md`: current amendment introduction and example acceptance blocks; `VERIFICATION_PROTOCOL.md`: scope/byte/CSV/framework checks and evidence limits.
- `MODEL_PROBABILITY_ML_RECOMMENDATIONS_2026-10-12.md`: introductory status, priorities and event-state/conditioning recommendations.
- `archive/root_documents_2026-10-14/NUMERICAL_MODEL_REGISTER.md`: location and relevant historical design references, not active capability certification.
- `Previous Sports Results/_canonical/README.md`: legacy export design and retired commands, contradicted in availability by current runtime removal.
- `Previous Sports Results/Soccer/Premier League/DATA_PROVENANCE.md`: origin, field classes, rebuilt scope and discarded market columns.
- `research/verification/framework_change_2026-10-14-1/IMPLEMENTATION.md`: opening defect/rebuild/status account. Its reported original-source verification was not independently rerun.
- The two supplied Downloads reports and pasted blueprint, including code examples, claims, phase plans and caveats.

No applicable AGENTS.md was found in the workspace scan or explicit ancestor checks through the drive root. One guessed prompt filename was absent; the actual indexed filename `8_IMPROVE_THE_FRAMEWORK.md` was then found and read. No required file remained unavailable for this design output.

## Supplied-source identity

SHA-256 values identify actual raw local bytes read in this task. They do not validate factual claims in those bytes.

| File | Bytes | SHA-256 |
|---|---:|---|
| `C:\Users\danie\Downloads\deep-research-report (8).md` | 24,584 | `26fda1d5a34952a6f3ba2f8323b6afb526dd385ce615d21af3030ccebec3ef26` |
| `C:\Users\danie\Downloads\compass_artifact_wf-b05206ec-5c08-5396-b913-fff940377666_text_markdown.md` | 51,335 | `08f8910480e4cecac443881634cb952612f1070e54f8e465142384356a3ea380` |
| `C:\Users\danie\.codex\attachments\f26dd181-1d65-473f-9ea3-c720953e8e0d\Pasted text.txt` | 49,954 | `7d3bbad30cb9f59802791572d1c3a0b370f21b8097ac85e645ff001e9a0b8454` |
| Pre-existing untracked prompt | 167,581 | `ec5dab2e30617b50afe13479e39f9c6935b04f0da2e11ca4eb6a9437f8dd639d` |

## How data was inspected

Read-only inline Python standard-library helpers were passed through the shell; no helper script was added to the repository. `csv.DictReader` counted logical records and read actual headers, rather than counting physical lines. `hashlib.sha256` compared current file bytes with stored origin hashes. No rows were transformed, repaired, dropped or admitted for training.

1. Counted all records in processed EPL/NBL, current selected EPL/NBL yearly files, every 2025 T20/one-day CSV, and two selected 2025 Test files.
2. Printed actual schemas and selected first-record fields for populated examples.
3. Counted nonblank availability fields and listed seasons/endpoints in both processed tables.
4. Read headers and the first record of `_canonical/events.csv` and `_canonical/seasons.csv`; the first event is explicitly excluded in that export, not evidence that all export rows are invalid.
5. Scanned seasons.csv to find exactly three 2025 origin records and compared their stored SHA-256 to current source bytes.

### Results

| Data | Logical rows | Additional finding |
|---|---:|---|
| Processed EPL | 2,280 | 2020-21 through 2025-26; REGULATION; availability 0/2,280 |
| Processed NBL | 738 | NBL22â€“NBL26; INCL_OT; availability 0/738 |
| EPL yearly 2025 | 380 | Explicit final/half goals and field provenance columns |
| NBL yearly 2025 | 206 | Mixed-stage schema; row count is not regular-season admission |
| NBL yearly 2026 | 29 | Partial snapshot |
| IPL 2025 | 74 | Aggregate innings/toss fields; not ball-level data |
| Other eleven T20 2025 files | 0 each | Big Bash, CPL, ILT20, Men's T20 World Cup, MLC, PSL, SA20, The Hundred, WBBL, Women's T20 World Cup, WPL |
| ODI International 2025 | 115 | Canonical folder per archive guidance |
| Men's ODI International 2025 | 115 | Alias; matching first-row fields observed, full byte identity across seasons is reported by the guide, not recomputed here |
| Other six one-day 2025 files | 0 each | Marsh One-Day Cup, Men's Champions Trophy, Men's Cricket World Cup, Metro Bank One Day Cup, Vijay Hazare Trophy, Women's Cricket World Cup |
| County Championship 2025 | 126 | Multi-innings/declaration schema |
| ICC World Test Championship 2025 | 0 | Header-only selected Test example |

| Current 2025 source compared with canonical seasons export | Export's recorded rows | Stored origin hash matches current bytes |
|---|---:|---|
| Soccer/Premier League | 0 | NO |
| Basketball/KBL | 0 | NO |
| Basketball/NBL | 206 | NO |

Observed canonical file sizes: events.csv 264,946,922 bytes; narratives.csv 129,483,028; provenance.csv 83,504,262; seasons.csv 8,090,235. These files are present locally. No current manifest.json appeared in the direct `_canonical` file listing, despite the historical README describing one. Their producing code was not run.

## Limits

No full source-population reconciliation, retained-source-body audit, all-sport CSV scan, ball corpus validation or predictive experiment was performed. Counts do not prove unique events, source truth, completeness or point-in-time admission. Reported archive repairs and historical Brier figures remain attributed to their local documents. Current upstream software was consulted through official documentation; no new packages were installed. MCC full-page/PDF retrieval failed, so exact current cricket-rule verification remains outstanding.

The engineering specifications, proposed statuses, tolerances, model choices and work packages are recommendations. They are not registered hypotheses, executed tests or amended rules.
