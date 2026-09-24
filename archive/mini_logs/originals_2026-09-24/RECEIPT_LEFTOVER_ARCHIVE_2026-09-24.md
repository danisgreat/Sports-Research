# Receipt — leftover mini-log copies archived on 2026-09-24(f)

**Written:** 2026-09-24, about 23:35 AEST, by repository session `sports-research-78`, during the verification audit in `PREDICTION_LOG_COMBINED_5.md` §"2026-09-24(f)" part A.

**Why these files are here.** The Drive re-sync of 2026-09-24 10:27 AEST restored these two logs into `Mini logs (to be sent to actual log later)/`. Both had already been consolidated and settled on 2026-09-22 and 2026-09-23. Leaving them in the active folder would make them look like unprocessed mini logs. They were moved with `git mv`, not deleted, in line with the 2026-09-23 concurrency rule ("never delete a file whose hash differs from its archived copy").

| Archived as | Original location | Bytes | SHA-256 | Relationship to earlier archive | Events inside, and where they are settled |
|---|---|---:|---|---|---|
| `PREDICTION_MINI_RUNNING_LOG_P482_ONWARD_DRIVE_RESYNC_LEFTOVER_2026-09-24.md` | `Mini Prediction Log - P-482 onward - 2026-09-21/PREDICTION_MINI_RUNNING_LOG_P482_ONWARD.md` | 46,121 | `daa5a4629323a92f6453354d259c090dd469e0ba6621d4d0b025c823154f3482` | **Byte-identical** to `archive/mini_logs/originals_2026-09-22/PREDICTION_MINI_RUNNING_LOG_P482_ONWARD_PRE_SETTLEMENT.md` | P-482 and P-483 (Part 5 §"2026-09-22"); the P-484 claim (Part 5 custody row; §"2026-09-23(c)") |
| `PREDICTION_MINI_RUNNING_LOG_P484_ONWARD_DRIVE_RESYNC_LEFTOVER_2026-09-24.md` | `Mini Prediction Log - P-484 onward - 2026-09-23/PREDICTION_MINI_RUNNING_LOG_P484_ONWARD.md` | 62,393 | `d554a18f63f55a3762ad550794ea162abe86545a7f83127410d2b681c60eecc0` | **Not** byte-identical to any archived copy. The nearest are the `…P484_ONWARD_PRE_RECON_2026-09-23.md` and `…SETTLED_DOCUMENTS_COPY_2026-09-23.md` variants | Padres P-484 claim (now P-492); `TMP-20260923-{WNBA-ATL-NYL, NFL-NYG-LAR, MLB-MIN-SF, WTA-WOLFF-OLI}`, which are pre-reconciliation aliases of P-484 (WNBA), P-485, P-486 and P-488 (the file's own lines 496–499); P-489. All are settled; see the `GAME_LOG_STATUS_CURRENT.md` rows P-484–P-489 and P-492 |

**Verification.** Every event in both files was checked against the status register and Part 5 before the move. No unsettled event and no unregistered ID claim was found. The external-claim sweep of the Codex attachments and the Documents folder found no P-495+ claims outside the repository.

**Operator note.** If the Drive mirror of `Mini logs (to be sent to actual log later)/` still holds these two folders, a later sync may restore them again. Only the P-509-onward folder is active.
