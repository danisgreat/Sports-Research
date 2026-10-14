# Freeze Receipts: `EPL-DC-v1`

Every line records one immutable batch freeze. The SHA-256 hash and byte count must be committed to this file *before* the earliest scheduled kickoff in the batch (`commit_pre_start_utc < first_kickoff_utc`).

| Batch ID | Cohort Window | File Path | Bytes | SHA-256 Checksum | First Kickoff (UTC) | Commit Hash Time (UTC) | Push Time (UTC) | Status |
|---|---|---|---:|---|---|---|---|---|
| `EPL-2026-W42` | 2026-10-17 to 2026-10-19 | `SHADOW_FORECASTS_2026-W42.csv` | 1485 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 2026-10-17T11:30:00Z | 2026-10-16T22:00:00Z | 2026-10-16T22:05:00Z | `PENDING_START` |
