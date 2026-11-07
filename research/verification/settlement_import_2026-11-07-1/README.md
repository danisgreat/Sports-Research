# Settlement revisions import 2026-11-07-1

Settles what remained of the owner drop `MINI LOGS TO BE SETTLED/` (archived at `archive/owner_drop_settled_2026-11-07-1/`). Start with [CANONICAL_IMPORT_REPORT.md](CANONICAL_IMPORT_REPORT.md).

| File | What it holds |
|---|---|
| [CANONICAL_IMPORT_REPORT.md](CANONICAL_IMPORT_REPORT.md) | What was settled, the append receipt and the effective counts |
| [UNRESOLVED_POST_IMPORT.md](UNRESOLVED_POST_IMPORT.md) | The queue after this import (supersedes the 2026-10-21 queue row by row) |
| [VERIFICATION.md](VERIFICATION.md) | Checks and results |
| [IMPORT_READBACK.csv](IMPORT_READBACK.csv) | Source and destination offsets and hashes of each wrapped core |
| [SOURCE_FILE_INVENTORY.csv](SOURCE_FILE_INVENTORY.csv) | Retained revision documents with bytes and SHA-256 |
| [SOURCE_UNIT_DISPOSITIONS.csv](SOURCE_UNIT_DISPOSITIONS.csv) | Where every source unit went |
| [SOURCE_DISCOVERY_REGISTER.csv](SOURCE_DISCOVERY_REGISTER.csv) | Sources read for these settlements |
| [OWNER_DROP_RECONCILIATION.csv](OWNER_DROP_RECONCILIATION.csv) | Each owner-drop file, its hash and its identical retained copy |
| `inputs/` | Byte-identical copies of the two revision documents |
