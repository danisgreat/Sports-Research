# Model card: `CRT20-IPL-FI-r1`

**Status: `DEVELOPMENT_ONLY`.** Not a card input.

| Field | Value |
|---|---|
| Contract | runs of the team batting first, full-length innings (20 overs bowled or all out) |
| Population | scorecards in `Previous Sports Results/Cricket T20/IPL`; excluded: {'method:Not applicable': 33, 'short_first_innings': 13, 'method:DLS': 22, 'method:Weather Abandonment': 11, 'invalid_identity_or_date': 2} |
| Ladder | C0 league-only (time-decayed mean and SD) · C1 + shrunk venue effect · C2 + batting and bowling team strengths (weighted ridge) · C2PRE = 50/50 mixture over who bats first (pre-toss price) |
| Distribution | discretised normal on 0–350 runs |
| Hyperparameters | CricketParams(half_life_days=91.25, ridge=320.0, k_venue=20.0, sd_inflation=1.0) |
| Known limits | no ball-by-ball phase data yet (WP-05), no XI, pitch or weather; Impact Player era (2023+) handled only through time decay |

See [DEVELOPMENT_RESULTS.md](DEVELOPMENT_RESULTS.md).

## Receipt

- `run_utc`: 2026-10-14T09:13:42Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: CRT20-IPL-FI-r1
- `params`: CricketParams(half_life_days=91.25, ridge=320.0, k_venue=20.0, sd_inflation=1.0)
- `dropped_rows`: {'method:Not applicable': 33, 'short_first_innings': 13, 'method:DLS': 22, 'method:Weather Abandonment': 11, 'invalid_identity_or_date': 2}
- `rows_used`: 1132
- `seconds`: 676
