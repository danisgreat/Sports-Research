# Learning store (LEARN-v1)

Append-only, point-in-time store of researched sporting observations, written only by `python -m ml ingest` during prompt 4 (verified canonical import) or an authorised prompt 8 change. Prompts 1–3 validate their `RESEARCH_EXPORT/` with `--dry-run` against a copy. Never hand-edit these CSVs: rows of a later ingest are appended, earlier rows never change, and `INGEST_RECEIPTS.csv` (written last) defines which rows exist. Schemas, identity, quarantine and known-at rules: [LEARNING_PIPELINE_PROTOCOL](../../LEARNING_PIPELINE_PROTOCOL.md) §3.

Empty at release (16 October 2026): no reviewed research export has been ingested yet. The retired results store is not a source.
