# Append-only runtime store

`journal.jsonl` is the canonical runtime record after the executable rebuild. Its current count and head are established by `node scripts/sportsctl.mjs verify-store`.

Only the recording paths in `sportsctl` may append records: decision packets, qualitative analysis inputs/outputs, structured user-facing publications, settlements and evaluations. Every line is canonical JSON with a SHA-256 payload hash, predecessor hash and record hash. `verify-store` recomputes the complete chain, hashes, identifier uniqueness and foreign-key order. `head_anchor.json` records the expected count and head after each durable append so accidental tail truncation is also detected. Successful recording commands regenerate `PREDICTION_RESULTS_LOG_v5.md` as the copy-friendly view.

This is tamper-evident local storage, not write-once media or a digital signature. A person who can rewrite both the journal and its local anchor could replace history. Operational use therefore requires copying each release anchor to separately controlled or signed storage. Editing, reordering or duplicating a line is detected; deletion is detected when the retained anchor or external copy is available. The four handwritten PASS entries in `PREDICTION_RESULTS_LOG_v4.md` predate this runtime and remain non-operative migration evidence; they are not silently copied into this store.

The journal line is flushed before the anchor is atomically replaced. A crash between those steps produces a valid chain with a stale anchor and therefore fails closed. `init-store` will never bless a non-empty unanchored journal. Recovery requires the separately retained expected head hash and record count through the explicit `recover-anchor` command.
