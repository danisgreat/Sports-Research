# Local prediction-log reconciliation receipt — 2026-09-23

Scope: local files only. No Google Drive document was written. No result-state refresh or retrospective was performed.

## Final ID decisions

- WNBA retains P-484. The Padres card held the duplicate P-484 claim and is now canonical P-492, the next available ID per the current user instruction. Its prior provisional P-490 mapping is retired; P-490 is not reused.
- P-493 is the recovered KIA Tigers @ Doosan Bears card, frozen at 19:28:29 AEST before its 19:30 scheduled start.
- The recovered Cairns–Tasmania card has no original issue timestamp. Preserve it as TMP-20260923-NBL-CNS-TAS, with P-487 on issue-time hold; do not promote it until sequence evidence exists.
- Chunichi R1 is the same NPB event as P-489; it consumes no new ID.
- Next canonical ID: P-494.

## Byte-exact pre-edit source files

| Original local file | Bytes | SHA-256 | Preserved copy |
|---|---:|---|---|
| Mini Prediction Log - P-482 onward - 2026-09-21/PREDICTION_MINI_RUNNING_LOG_P482_ONWARD.md | 146703 | ce2057b70b786670edb7842cfdbb832b4eb2e70e35826c4fd829108de99cbeea | PREDICTION_MINI_RUNNING_LOG_P482_ONWARD_PRE_RECON_2026-09-23.md |
| Mini Prediction Log - P-484 onward - 2026-09-23/PREDICTION_MINI_RUNNING_LOG_P484_ONWARD.md | 89568 | a79c9e377a3949c8b33449213b2be801fdd5a4a5520a1504bc0405fd38fc9c0a | PREDICTION_MINI_RUNNING_LOG_P484_ONWARD_PRE_RECON_2026-09-23.md |
| Active merged mini log before edits | 153605 | 1629d4efde1cdc802f01331a46a6a8f1eeafb921819a373d53c7a375741b07ac | PREDICTION_MINI_RUNNING_LOG_MERGED_P482_ONWARD_PRE_RECON_2026-09-23.md |
| Part 5 before edits | 111446 | bc70b69ecb088cb68bcb0a97cb05f5b15f250e28011c34e155bbb2ba126b09b2 | PREDICTION_LOG_COMBINED_5_PRE_RECON_2026-09-23.md |
| GAME_LOG_STATUS_CURRENT before edits | 121939 | 9a098fb84f027f046e9f52b048dd90993dffb05b0cf7be0ad5e613d16f34ab65 | GAME_LOG_STATUS_CURRENT_PRE_RECON_2026-09-23.md |

Each archived source copy was verified against original byte length and SHA-256 before the temporary working copy was replaced by a receipt.

## Post-reconciliation files

| Local file | Bytes | SHA-256 |
|---|---:|---|
| C:\Users\danie\Documents\Sports Research\PREDICTION_MINI_RUNNING_LOG_MERGED_P482_ONWARD.md | 181259 | 942d344e848cf7e5523d38cc7c3c689a99d62fda336f66dc8f01eb958b179f8a |
| C:\Users\danie\Desktop\Sports Research\PREDICTION_LOG_COMBINED_5.md | 114939 | c7249aa3dc458aa54f28ee641bf893b7d701c7b44bb8352ad642302f03f79b7f |
| C:\Users\danie\Desktop\Sports Research\GAME_LOG_STATUS_CURRENT.md | 124127 | d74c6d7096fe6ee5c05ded751b006ddd4bdafe87b5f155d37d1bac5dacc4eda3 |
| C:\Users\danie\Desktop\Sports Research\Mini logs (to be sent to actual log later)\Mini Prediction Log - P-494 onward - 2026-09-23\PREDICTION_MINI_RUNNING_LOG_P494_ONWARD.md | 48895 | 12eedf606d72f94b7baa4d120fe5fbed9cb93f44a24197ce7c36274041240f00 |
| C:\Users\danie\Desktop\Sports Research\Mini logs (to be sent to actual log later)\Mini Prediction Log - P-482 onward - 2026-09-21\PREDICTION_MINI_RUNNING_LOG_P482_ONWARD.md | 572 | 914503c6f3c46799ebfbb1d4dbbed82c3a0a54f7dea46e14419d7ca89a2c59d1 |
| C:\Users\danie\Desktop\Sports Research\Mini logs (to be sent to actual log later)\Mini Prediction Log - P-484 onward - 2026-09-23\PREDICTION_MINI_RUNNING_LOG_P484_ONWARD.md | 728 | 88cf046f68bf6517595b0ee4768415dea48931a635468bedfca767566c58a20a |

## Supplemental reconciliation — 2026-09-23, WTA live view P-494

- Canonical ID **P-494** is assigned to Mirra Andreeva vs Aliaksandra Sasnovich, WTA Singapore Open, live-issued view frozen at **20:51:54 AEST** (official WTA feed observation 20:51:14 AEST). This is a separate live horizon, not a pregame card; no result state or retrospective was added.
- The event's source handle `TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH` is retired as an alias. The full 21,560-byte source log was copied before clearing the temporary folder; SHA-256 `449B1235A5E87949DB02B9DDF7E72E9265B8D97A9513B43829CEE9B574595D0E`; the archived copy is `PREDICTION_MINI_RUNNING_LOG_TMP_20260923_WTA_SGP_PRE_RECON_2026-09-23.md`.
- The WTA card was frozen after P-493 and before the later Khonkaen United–Navy request. The soccer request received no prediction, so it consumes no ID.
- Active mini log: `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-494 onward - 2026-09-23/PREDICTION_MINI_RUNNING_LOG_P494_ONWARD.md`. Part 5 and the status register now include P-494. **Next canonical ID: P-495.**
- Local files only. No Drive documents or rules were modified. No retrospective or terminal-state refresh was performed.
- The temporary WTA prediction body was cleared after archive/hash verification and replaced by a short retired-ID receipt; the folder is retained for the pointer only.
