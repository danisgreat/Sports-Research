# Training releases (LEARN-v1)

Each subfolder is one immutable release built by `python -m ml training build`: ROWS.csv, EXCLUSIONS.csv, COVERAGE.csv and MANIFEST.csv (store view, digest, feature specification, code and file hashes). `python -m ml training verify` rebuilds the rows from the recorded store view and requires identical bytes. A correction creates a new release; existing releases are never overwritten. A release is training data only. See [LEARNING_PIPELINE_PROTOCOL](../../LEARNING_PIPELINE_PROTOCOL.md) §5.
