# Settlement revisions import 2026-11-16-1

Applied 2026-11-16T19:22:52+11:00. Prompts 3→4 (P-2026.11.16-v25.0) under the owner order of 16 November 2026 (S-1: retry the unresolved queue). Records only: no card, rank, probability, earlier grade or canonical ID changed.

## What was settled

| ID | Game | Rows | WIN | LOSS | Evidence | Basis |
|---|---|---:|---:|---:|---|---|
| P-647 | Urawa Red Diamonds v Cerezo Osaka · 2026-11-11 · J.League YBC Levain Cup, first leg | 3 | 1 | 2 | A | corners Urawa 8 + Cerezo 4 = 12 |
| P-661 | Hobart Hurricanes Women v Brisbane Heat Women · 2026-11-14 · WBBL|12 | 10 | 5 | 5 | C | Hobart 23-24 after six completed overs (threshold bound; one unplaced run) |
| P-662 | Perth Scorchers Women v Adelaide Strikers Women · 2026-11-14 · WBBL|12 Match 22 | 12 | 6 | 6 | C | Adelaide 39-40 after six completed overs (threshold bound; one unplaced run) |
| P-664 | Tappara U20 v HPK U20 · 2026-11-14 · Finland U20 SM-sarja | 24 | 12 | 12 | C | Tappara 2-4 HPK (1-1, 0-1, 1-2); total 6 |
| P-678 | Australia v England · 2026-11-15 · second ODI, Adelaide | 2 | 1 | 1 | C | England 19-1 after five completed overs |
| P-683 | Kashiwa Reysol v Kawasaki Frontale · 2026-11-15 · J.League YBC Levain Cup | 2 | 1 | 1 | A | corners Kashiwa 4 + Kawasaki 3 = 7 |

Total: 53 rows, 26 WIN, 27 LOSS. The effective-settlement view now holds **0 UNRESOLVED rows** (it held 53). All rows are chat-local research; the primary count stays zero.

## Evidence and limits

- Every figure comes from a capture the owner's recovery saved outside the repository ([manifest](../source_recovery_2026-11-15-1/CAPTURE_MANIFEST.csv)). In this run each capture was re-hashed (all match) and the settling figure re-read from the capture itself.
- The two WBBL six-over grades rest on a threshold bound (one run the feed did not place by ball). Hobart's margin is at least 17.5 runs; Adelaide's is 1.5. Exact scores are not asserted.
- The open Cricsheet WBBL and ODI archives were downloaded through the repository fetcher (robots ALLOWED for every reader) to look for a second lineage; they reached only 2 November 2026. Three checks stay open with grades settled: [UNRESOLVED_POST_IMPORT.csv](UNRESOLVED_POST_IMPORT.csv).
- The Guardian page is BLOCKED for the repository agent's reader at that path and was not opened; the England figure is read from the ChatGPT reader's retained capture.

## Deep loss review

One: P-662, card DDA525E495, first lean Adelaide 6 overs Over 41.5 at 0.648 — MIXED (variance in the outcome; small-sample strength treated as a direction). It is in the [revision document](SETTLEMENT_REVISION_2.md) and the deep loss register. No other ranked first lean, top side or top total lost in these rows.

## Append receipt

Part 11 before: 3,834 bytes, SHA-256 `ef2ff4db206a800f066c1bdf13eb8ab60fda810e24bf8a3aaa60f92be6cc1b36`. After: 22,101 bytes, SHA-256 `b0ea1474d58d8bfd7027380f2562c39eb4f383dd0c4fc6dca67d7335d2ca2d1f`; the earlier bytes are an exact prefix. Six addendum blocks, each read back byte-exact once: [IMPORT_READBACK.csv](IMPORT_READBACK.csv). Revision chain: [SETTLEMENT_REVISIONS.csv](SETTLEMENT_REVISIONS.csv) (53 rows, revision-2 on revision-1), validated by `ml settlement-view`.

## Learning

CARD-TRAIN-v1 was run after this import (run named in CURRENT_STATE). The finals are not ingested into the learning store here: the store's export columns need the full final score with two lineages for these games, which this revision does not have for the phase and corner fields.
