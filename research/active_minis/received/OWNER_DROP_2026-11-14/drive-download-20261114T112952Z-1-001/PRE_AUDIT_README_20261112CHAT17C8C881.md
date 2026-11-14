# Sports Research Mini — Pre-audit Handoff

**MINI_KEY:** `20261112CHAT17C8C881`  
**Primary file:** `mini/20261112CHAT17C8C881.md`  
**Source authority snapshot inside log:** GitHub `danisgreat/Sports-Research`, read-only published `main` at `008cedc4ff469e7a808292aa3667a7bffe22e273`  
**Disposition:** `CHAT_ONLY_LOCAL_DRAFT`, `NOT_FROZEN`, `NOT_PERFORMANCE_ELIGIBLE`, no canonical P-ID allocated.

## Inventory

- 1 current primary Markdown mini containing **9** local event cards (G0001–G0009).
- 9 standalone Python calculation scripts (one per event). **Syntax parsing only** was performed here; scientific validity and runtime execution were *not* audited.
- 2 auxiliary Markdown artifacts: original initialization snapshot and G0009 working append.
- This README, a machine-readable `MANIFEST.json`, and per-file `SHA256SUMS.txt`.
- Primary document request intake: **9 entries**; evidence queue: **52 open unique items**; current footer points from G0009 to G0010.

## Event/Script pairing

| Event | Sport | Script |
|---|---|---|
| G0001 | Tennis, Svrčina vs Virtanen | `tennis_markov_20261112G0001.py` |
| G0002 | Ice hockey, Torpedo vs Arlan | `hockey_research_G0002.py` |
| G0003 | Tennis, Tirante vs Shevchenko | `tennis_markov_20261112G0003.py` |
| G0004 | Basketball WNBL, Geelong vs Perth | `wnbl_scoregrid_G0004.py` |
| G0005 | Basketball KBL, Wonju vs Suwon KT | `kbl_scoregrid_G0005.py` |
| G0006 | Basketball B.League, Kawasaki vs Saga | `bleague_scoregrid_G0006.py` |
| G0007 | Ice hockey U20, Motor vs Liberec | `icehockey_poisson_G0007.py` |
| G0008 | Tennis, Piros vs Altmaier | `tennis_markov_20261113G0008.py` |
| G0009 | Tennis, Tabilo vs Tirante | `tennis_markov_20261114G0009.py` |

## Pre-audit flags (unchanged from source)

1. This bundle is a local chat-only pre-audit handoff. It is not a certified model-run, issued prediction log, or repository commit.
2. The primary mini is mini/20261112CHAT17C8C881.md; the support/ files are historical/working sidecars and MUST NOT replace the primary mini.
3. There are nine documented local events G0001..G0009. Card G0002 uses a nonstandard heading ("## LOCAL-...") instead of "## CARD LOCAL-...". Its body remains intact; the bundle preserves original bytes.
4. There are 52 OPEN_UNVERIFIED evidence records. Research cards and calculations must not be treated as validated calibrated probabilities.
5. The original initialization snapshot has zero cards and is preserved only as a historical provenance source; it is NOT the latest log.
6. The G0009 append sidecar is not byte-identical to the G0009 section in the canonical local mini. Treat it as a nonauthoritative working artifact; avoid double importing it.
7. No owner-local Git checkout, ml source audit, model certification, league calibration, card lint, official canonical import or settlement is evidenced by this bundling step.
8. No changes to original source files or the GitHub repository were made; the originals have only been copied into this archive.

## Suggested audit order

1. Validate ZIP integrity and verify each original file against SHA256SUMS.txt.
2. Use the primary mini only for card count, intake, queue, original chronology, and footer. Treat both support files as nonauthoritative.
3. Reconcile card G0002's nonstandard heading before using strict card-header parser (do not silently change its original text).
4. Independently verify time-state, exact market/settlement definitions, roster data, source admissibility, model assumptions and reference construction for each event.
5. Only then assess selection, calibration, settlement, repository import eligibility and any required governance controls.

**Important:** Neither packaging nor AST parsing represents an official pre-audit pass or a new prospective forecast issuance.
