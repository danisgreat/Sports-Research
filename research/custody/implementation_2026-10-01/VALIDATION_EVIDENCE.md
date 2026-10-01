# Validation evidence and historical source bundle

**Preserved 2026-09-28; current status: historical evaluation evidence, not a new validation run.** The old research directory was removed to satisfy the Markdown-only repository rule. The original preregistration, aggregate outputs, inputs, and implementation text are embedded below, with line endings normalized for Markdown. The original Git blobs remain in parent commit `3fbf0c981b40a1d0e3ffff9725dcc8e383ff05fa`.

The Probability Toolkit tables and claims were created before this cleanup. This bundle permits inspection of the historical method and reported outputs. The original game-level input files, dependent research modules, and source snapshots are not present in the current tree, so the full game-by-game evaluation cannot be rerun from this Markdown tree alone. Aggregate JSON does not prove leak-free sequencing or population cohort completeness. Treat the published result as a historical claim pending a fresh, source-backed, game-level replication. It does not establish card-level predictive skill.

| Evidence | Parent Git path | Blob SHA-1 | Original bytes |
|---|---|---|---:|
| P6 preregistration | `research/md_only_2026-09-28/PREREGISTRATION_P6.md` | `c5aad890f910ab9aa04629506a1a9da6e03bafbe` | 2657 |
| TB-1-MD cross-sport aggregate results | `research/md_only_2026-09-28/validate_tb1_md.json` | `30de0bb7f3c6e7febe1e4cfc11a0e5f1c0a54b13` | 8850 |
| P6 soccer aggregate results | `research/md_only_2026-09-28/p6_soccer_tb1md.json` | `e4db2a6dfa6762ec7120f8f065c17b12cd3b1ab4` | 6399 |
| Cross-sport home-edge inputs | `research/md_only_2026-09-28/home_edges.json` | `2bb00235aad768b4992522c82c1035d2515fc406` | 3303 |
| P6 previous-season home edges | `research/md_only_2026-09-28/p6_soccer_home_edges.json` | `b2de0aaaf443cbb905524fc2f93f346a3f03d825` | 2249 |
| Probability-table arithmetic checks | `research/md_only_2026-09-28/tables_check.json` | `6b8f45a2b83ce3eacfe022b39f7ee2ba5adf6598` | 140 |
| Historical cross-sport evaluation implementation | `research/md_only_2026-09-28/validate_tb1_md.py` | `4ee3ea71d16c2420b90cb47996ce3dc6c6c1bac8` | 6808 |
| Historical P6 evaluation implementation | `research/md_only_2026-09-28/p6_soccer_tb1md.py` | `40b7b99553d5cbc88b3886a7bcf10b9656719907` | 4664 |
| Historical table-generation implementation | `research/md_only_2026-09-28/make_tables.py` | `22aef1e10fab9956c2eb5a56149b0859d112d390` | 8093 |

## Evaluation interpretation

- P6 used results-only openfootball data, seasons 2020–21 through 2025–26, with 2020–21 supplying the first previous-season home edge. Its preregistered decision gate required a pooled week-block 95% interval below zero and improvement in at least four of five scored seasons; EPL result replication had to pass first. The result is a historical out-of-sample team-baseline evaluation, not evidence that issued card probabilities or RM-1 ranks beat an alternative.
- The cross-sport TB-1-MD comparison reports Brier differences against the historical tool and a running population prior. Some home edges were measured in the scored season, as disclosed in the Probability Toolkit; do not describe all nine cohorts as strictly out of sample with respect to every input.
- Table checks report zero RM-1 mismatches versus the prior tool, but this does not test decision validity, source custody, or prospective skill.
- Any current reference-anchor promotion remains provisional until the original source cohort, derivation, and output can be replicated from preserved game-level evidence. A card must still print its own baseline source and cutoff; unsupported competitions remain NOT_YET_DERIVED.

## P6 preregistration

Original path: `research/md_only_2026-09-28/PREREGISTRATION_P6.md`. SHA-256 of original Git blob bytes: `6e9d494c82294d00b796dd200245425487b538a8636e56dc88fa635da509f7d0`.

```markdown
# P6 — does TB-1-MD have resolution in the other top soccer leagues? (preregistered 2026-09-28, before any run)

**Why.** About 80 soccer cards spread over more than 30 competitions, but TB-1 is validated only for the EPL. The existing rule, authorised by the user on 2026-09-25(e), is "anchor on TB-1 where it has resolution". A league that passes this test gains the anchor under that rule. This is not a new coefficient: k = 2 and the formula are the EPL's, unchanged. The user's bar applies: held-out, 95% interval below 0.

**Data.** openfootball `football.json` (results only: date, teams, full-time score), seasons 2020-21 to 2025-26:
- EPL (`en.1`), as the replication control;
- La Liga (`es.1`), Bundesliga (`de.1`), Serie A (`it.1`), Ligue 1 (`fr.1`).

No odds are read.

**Model.** TB-1-MD exactly as in `PROBABILITY_TOOLKIT.md` §4:
- Poisson, with k = 2 fixed (the EPL tool value, not tuned);
- λh = (T + M)/2 and λa = (T − M)/2;
- home edge HE = the previous season's mean home goal margin in the same league. So 2020-21 only supplies HE, and the scored seasons are 2021-22 to 2025-26;
- each game is forecast only from games strictly before its date. A team must have played at least 1 game and the league at least 10 games;
- no previous-season carry-over.

**Comparator (population).** The running, in-season league rates before each game: P(home), P(draw), P(away), and P(total ≥ 3).

**Metrics.**
- **Primary, results:** three-way Brier, the sum over home/draw/away of (p − y)².
- **Primary, totals:** the Brier of P(Over 2.5).
- **Secondary:** the Brier of P(home win).
- **Intervals:** 95% ISO-week block bootstrap (2,000 draws, seed 20260928) on the per-game difference MD − population.

**Decision rule, per league and target.** Fixed now; it cannot move after the results are seen.
- **RESOLUTION:** the pooled 2021-22 to 2025-26 difference has its 95% interval entirely below 0 **and** the difference is below 0 in at least 4 of the 5 seasons.
- **Otherwise NO RESOLUTION.** The league's cards keep the population anchor, and TB-1-MD is printed as `UNVALIDATED`/reference.
- **The EPL result is the replication check.** It is expected to pass for results and fail for totals, as in 2025-26. If the EPL fails results, the whole test is reported, and nothing is promoted for any league.

**What happens next.**
- A league that passes becomes a TB-1-MD anchor for the passed target in `PROBABILITY_TOOLKIT.md` §4.3 and the soccer §0 page.
- A league that fails keeps the population anchor.
- Either way the result is recorded in `LEARNING_REGISTER.md`.

Script: `p6_soccer_tb1md.py`, results in `p6_soccer_tb1md.json` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)).
```

## TB-1-MD cross-sport aggregate results

Original path: `research/md_only_2026-09-28/validate_tb1_md.json`. SHA-256 of original Git blob bytes: `b0a51cdb552613f026086de4c3701a44767feae8c82cc748e320d76a6741f15f`.

```json
{
  "NBL": {
    "seasons_scored": [
      "NBL 2024-25",
      "NBL 2025-26"
    ],
    "home_edge_ref": [
      2.829,
      1.386
    ],
    "home_edge_source": "previous season",
    "k": 5,
    "sd_margin": 15.2,
    "sd_total": 18.7,
    "n": 289,
    "brier_home": {
      "tb1_tool": 0.2293,
      "tb1_md": 0.2248,
      "a0": 0.2538
    },
    "brier_over": {
      "tb1_tool": 0.24,
      "tb1_md": 0.2398,
      "a0": 0.2518
    },
    "home_md_minus_tool": {
      "mean": -0.00454,
      "ci95": [
        -0.00883,
        -0.00049
      ],
      "n": 289
    },
    "home_md_minus_a0": {
      "mean": -0.02904,
      "ci95": [
        -0.04127,
        -0.01593
      ],
      "n": 289
    },
    "over_md_minus_tool": {
      "mean": -0.00019,
      "ci95": [
        -0.00093,
        0.00068
      ],
      "n": 289
    },
    "over_md_minus_a0": {
      "mean": -0.01197,
      "ci95": [
        -0.02245,
        -0.00105
      ],
      "n": 289
    },
    "max_abs_p_home_gap": 0.1299
  },
  "WNBA": {
    "seasons_scored": [
      "WNBA 2025",
      "WNBA 2026"
    ],
    "home_edge_ref": [
      0.804,
      2.505
    ],
    "home_edge_source": "previous season",
    "k": 2,
    "sd_margin": 13.3,
    "sd_total": 19.5,
    "n": 593,
    "brier_home": {
      "tb1_tool": 0.2191,
      "tb1_md": 0.2181,
      "a0": 0.2533
    },
    "brier_over": {
      "tb1_tool": 0.2379,
      "tb1_md": 0.2377,
      "a0": 0.2558
    },
    "home_md_minus_tool": {
      "mean": -0.00101,
      "ci95": [
        -0.00444,
        0.00296
      ],
      "n": 593
    },
    "home_md_minus_a0": {
      "mean": -0.03526,
      "ci95": [
        -0.04405,
        -0.02619
      ],
      "n": 593
    },
    "over_md_minus_tool": {
      "mean": -0.00014,
      "ci95": [
        -0.00082,
        0.00051
      ],
      "n": 593
    },
    "over_md_minus_a0": {
      "mean": -0.01812,
      "ci95": [
        -0.02467,
        -0.01176
      ],
      "n": 593
    },
    "max_abs_p_home_gap": 0.2615
  },
  "NBA": {
    "seasons_scored": [
      "NBA 2025-26"
    ],
    "home_edge_ref": [
      1.705
    ],
    "home_edge_source": "same season (in-sample)",
    "k": 2,
    "sd_margin": 15.1,
    "sd_total": 19.4,
    "n": 1217,
    "brier_home": {
      "tb1_tool": 0.2161,
      "tb1_md": 0.2159,
      "a0": 0.248
    },
    "brier_over": {
      "tb1_tool": 0.2389,
      "tb1_md": 0.239,
      "a0": 0.2487
    },
    "home_md_minus_tool": {
      "mean": -0.0002,
      "ci95": [
        -0.00111,
        0.00063
      ],
      "n": 1217
    },
    "home_md_minus_a0": {
      "mean": -0.03216,
      "ci95": [
        -0.03966,
        -0.02493
      ],
      "n": 1217
    },
    "over_md_minus_tool": {
      "mean": 0.0001,
      "ci95": [
        -0.0001,
        0.00039
      ],
      "n": 1217
    },
    "over_md_minus_a0": {
      "mean": -0.00969,
      "ci95": [
        -0.01812,
        -0.00108
      ],
      "n": 1217
    },
    "max_abs_p_home_gap": 0.0938
  },
  "NHL": {
    "seasons_scored": [
      "NHL 2025-26 (ESPN)"
    ],
    "home_edge_ref": [
      0.129
    ],
    "home_edge_source": "same season (in-sample)",
    "k": 20,
    "sd_margin": 2.57,
    "sd_total": 2.29,
    "n": 1291,
    "brier_home": {
      "tb1_tool": 0.2477,
      "tb1_md": 0.2469,
      "a0": 0.2503
    },
    "brier_over": {
      "tb1_tool": 0.249,
      "tb1_md": 0.249,
      "a0": 0.2502
    },
    "home_md_minus_tool": {
      "mean": -0.00074,
      "ci95": [
        -0.00176,
        -3e-05
      ],
      "n": 1291
    },
    "home_md_minus_a0": {
      "mean": -0.00339,
      "ci95": [
        -0.00559,
        -0.00142
      ],
      "n": 1291
    },
    "over_md_minus_tool": {
      "mean": -1e-05,
      "ci95": [
        -7e-05,
        5e-05
      ],
      "n": 1291
    },
    "over_md_minus_a0": {
      "mean": -0.00115,
      "ci95": [
        -0.003,
        0.00093
      ],
      "n": 1291
    },
    "max_abs_p_home_gap": 0.1185
  },
  "EPL": {
    "seasons_scored": [
      "EPL 2025-26"
    ],
    "home_edge_ref": [
      0.303
    ],
    "home_edge_source": "same season (in-sample)",
    "k": 2,
    "sd_margin": 1.51,
    "sd_total": 1.61,
    "n": 370,
    "brier_home": {
      "tb1_tool": 0.2308,
      "tb1_md": 0.2296,
      "a0": 0.2469
    },
    "brier_over": {
      "tb1_tool": 0.2584,
      "tb1_md": 0.2583,
      "a0": 0.2502
    },
    "home_md_minus_tool": {
      "mean": -0.00128,
      "ci95": [
        -0.00354,
        0.0006
      ],
      "n": 370
    },
    "home_md_minus_a0": {
      "mean": -0.01731,
      "ci95": [
        -0.02492,
        -0.00875
      ],
      "n": 370
    },
    "over_md_minus_tool": {
      "mean": -5e-05,
      "ci95": [
        -0.0008,
        0.00069
      ],
      "n": 370
    },
    "over_md_minus_a0": {
      "mean": 0.0082,
      "ci95": [
        0.00267,
        0.0141
      ],
      "n": 370
    },
    "max_abs_p_home_gap": 0.0756
  },
  "NFL": {
    "seasons_scored": [
      "NFL 2025"
    ],
    "home_edge_ref": [
      1.719
    ],
    "home_edge_source": "previous season",
    "k": 2,
    "sd_margin": 13.6,
    "sd_total": 13.4,
    "n": 256,
    "brier_home": {
      "tb1_tool": 0.2311,
      "tb1_md": 0.2271,
      "a0": 0.2516
    },
    "brier_over": {
      "tb1_tool": 0.2462,
      "tb1_md": 0.2464,
      "a0": 0.254
    },
    "home_md_minus_tool": {
      "mean": -0.004,
      "ci95": [
        -0.00874,
        6e-05
      ],
      "n": 256
    },
    "home_md_minus_a0": {
      "mean": -0.02447,
      "ci95": [
        -0.03381,
        -0.01584
      ],
      "n": 256
    },
    "over_md_minus_tool": {
      "mean": 0.00028,
      "ci95": [
        -0.00015,
        0.00092
      ],
      "n": 256
    },
    "over_md_minus_a0": {
      "mean": -0.00752,
      "ci95": [
        -0.01773,
        0.00499
      ],
      "n": 256
    },
    "max_abs_p_home_gap": 0.114
  },
  "AFL": {
    "seasons_scored": [
      "AFL 2026"
    ],
    "home_edge_ref": [
      6.034
    ],
    "home_edge_source": "previous season",
    "k": 2,
    "sd_margin": 36.8,
    "sd_total": 29.1,
    "n": 193,
    "brier_home": {
      "tb1_tool": 0.2051,
      "tb1_md": 0.2032,
      "a0": 0.2491
    },
    "brier_over": {
      "tb1_tool": 0.2453,
      "tb1_md": 0.2454,
      "a0": 0.2534
    },
    "home_md_minus_tool": {
      "mean": -0.00191,
      "ci95": [
        -0.00765,
        0.00369
      ],
      "n": 193
    },
    "home_md_minus_a0": {
      "mean": -0.0459,
      "ci95": [
        -0.06346,
        -0.02634
      ],
      "n": 193
    },
    "over_md_minus_tool": {
      "mean": 0.00017,
      "ci95": [
        -0.00047,
        0.0008
      ],
      "n": 193
    },
    "over_md_minus_a0": {
      "mean": -0.00795,
      "ci95": [
        -0.01982,
        0.00524
      ],
      "n": 193
    },
    "max_abs_p_home_gap": 0.1714
  },
  "NRL": {
    "seasons_scored": [
      "NRL 2026"
    ],
    "home_edge_ref": [
      3.773
    ],
    "home_edge_source": "previous season",
    "k": 2,
    "sd_margin": 19.9,
    "sd_total": 13.9,
    "n": 201,
    "brier_home": {
      "tb1_tool": 0.241,
      "tb1_md": 0.2374,
      "a0": 0.2529
    },
    "brier_over": {
      "tb1_tool": 0.2518,
      "tb1_md": 0.2516,
      "a0": 0.255
    },
    "home_md_minus_tool": {
      "mean": -0.0036,
      "ci95": [
        -0.01395,
        0.00689
      ],
      "n": 201
    },
    "home_md_minus_a0": {
      "mean": -0.01556,
      "ci95": [
        -0.02823,
        -0.00263
      ],
      "n": 201
    },
    "over_md_minus_tool": {
      "mean": -0.00019,
      "ci95": [
        -0.00077,
        0.00036
      ],
      "n": 201
    },
    "over_md_minus_a0": {
      "mean": -0.00335,
      "ci95": [
        -0.01141,
        0.00515
      ],
      "n": 201
    },
    "max_abs_p_home_gap": 0.17
  },
  "MLB": {
    "seasons_scored": [
      "MLB 2026"
    ],
    "home_edge_ref": [
      0.073
    ],
    "home_edge_source": "same season (in-sample)",
    "k": 20,
    "sd_margin": 4.57,
    "sd_total": 4.5,
    "n": 2358,
    "brier_home": {
      "tb1_tool": 0.248,
      "tb1_md": 0.2478,
      "a0": 0.2497
    },
    "brier_over": {
      "tb1_tool": 0.2491,
      "tb1_md": 0.2491,
      "a0": 0.25
    },
    "home_md_minus_tool": {
      "mean": -0.00017,
      "ci95": [
        -0.00033,
        0.0
      ],
      "n": 2358
    },
    "home_md_minus_a0": {
      "mean": -0.0019,
      "ci95": [
        -0.00352,
        -0.00023
      ],
      "n": 2358
    },
    "over_md_minus_tool": {
      "mean": 1e-05,
      "ci95": [
        -4e-05,
        5e-05
      ],
      "n": 2358
    },
    "over_md_minus_a0": {
      "mean": -0.00091,
      "ci95": [
        -0.00235,
        0.00051
      ],
      "n": 2358
    },
    "max_abs_p_home_gap": 0.1017
  }
}
```

## P6 soccer aggregate results

Original path: `research/md_only_2026-09-28/p6_soccer_tb1md.json`. SHA-256 of original Git blob bytes: `d6f34ecfbce7ba5d392a7e572f075d2da40e284682ab30c0bb0d4b43a65c2149`.

```json
{
  "preregistration": "PREREGISTRATION_P6.md",
  "k": 2,
  "epl": {
    "per_season": {
      "2021": {
        "n": 370,
        "he": 0.011,
        "r3_diff": -0.06258,
        "o_diff": 0.00128,
        "h_diff": -0.03059
      },
      "2022": {
        "n": 370,
        "he": 0.208,
        "r3_diff": -0.04211,
        "o_diff": -0.00847,
        "h_diff": -0.02473
      },
      "2023": {
        "n": 370,
        "he": 0.416,
        "r3_diff": -0.06347,
        "o_diff": 0.00238,
        "h_diff": -0.03211
      },
      "2024": {
        "n": 370,
        "he": 0.321,
        "r3_diff": -0.04889,
        "o_diff": -0.0012,
        "h_diff": -0.02298
      },
      "2025": {
        "n": 370,
        "he": 0.092,
        "r3_diff": -0.02945,
        "o_diff": 0.00856,
        "h_diff": -0.01639
      }
    },
    "r3": {
      "mean": -0.0493,
      "ci95": [
        -0.05816,
        -0.04076
      ],
      "n": 1850,
      "seasons_below_0": "5/5",
      "verdict": "RESOLUTION"
    },
    "over25": {
      "mean": 0.00051,
      "ci95": [
        -0.00234,
        0.00343
      ],
      "n": 1850,
      "seasons_below_0": "2/5",
      "verdict": "NO RESOLUTION"
    },
    "home": {
      "mean": -0.02536,
      "ci95": [
        -0.03035,
        -0.0202
      ],
      "n": 1850
    }
  },
  "laliga": {
    "per_season": {
      "2021": {
        "n": 370,
        "he": 0.229,
        "r3_diff": -0.04187,
        "o_diff": -0.0002,
        "h_diff": -0.02053
      },
      "2022": {
        "n": 370,
        "he": 0.339,
        "r3_diff": -0.03274,
        "o_diff": -0.00142,
        "h_diff": -0.01793
      },
      "2023": {
        "n": 370,
        "he": 0.397,
        "r3_diff": -0.06157,
        "o_diff": -0.00622,
        "h_diff": -0.03658
      },
      "2024": {
        "n": 360,
        "he": 0.324,
        "r3_diff": -0.05763,
        "o_diff": -0.00655,
        "h_diff": -0.0298
      },
      "2025": {
        "n": 370,
        "he": 0.292,
        "r3_diff": -0.03752,
        "o_diff": -0.00403,
        "h_diff": -0.02164
      }
    },
    "r3": {
      "mean": -0.0462,
      "ci95": [
        -0.05477,
        -0.03766
      ],
      "n": 1840,
      "seasons_below_0": "5/5",
      "verdict": "RESOLUTION"
    },
    "over25": {
      "mean": -0.00367,
      "ci95": [
        -0.00695,
        -0.00051
      ],
      "n": 1840,
      "seasons_below_0": "5/5",
      "verdict": "RESOLUTION"
    },
    "home": {
      "mean": -0.02527,
      "ci95": [
        -0.02973,
        -0.02073
      ],
      "n": 1840
    }
  },
  "bundesliga": {
    "per_season": {
      "2021": {
        "n": 296,
        "he": 0.32,
        "r3_diff": -0.04469,
        "o_diff": -0.00661,
        "h_diff": -0.022
      },
      "2022": {
        "n": 296,
        "he": 0.405,
        "r3_diff": -0.02944,
        "o_diff": 0.00478,
        "h_diff": -0.01454
      },
      "2023": {
        "n": 296,
        "he": 0.539,
        "r3_diff": -0.07344,
        "o_diff": -0.01166,
        "h_diff": -0.032
      },
      "2024": {
        "n": 296,
        "he": 0.395,
        "r3_diff": -0.02965,
        "o_diff": -0.00707,
        "h_diff": -0.01412
      },
      "2025": {
        "n": 296,
        "he": 0.127,
        "r3_diff": -0.05489,
        "o_diff": -0.0019,
        "h_diff": -0.03061
      }
    },
    "r3": {
      "mean": -0.04642,
      "ci95": [
        -0.05721,
        -0.03558
      ],
      "n": 1480,
      "seasons_below_0": "5/5",
      "verdict": "RESOLUTION"
    },
    "over25": {
      "mean": -0.00449,
      "ci95": [
        -0.00825,
        -0.00067
      ],
      "n": 1480,
      "seasons_below_0": "4/5",
      "verdict": "RESOLUTION"
    },
    "home": {
      "mean": -0.02265,
      "ci95": [
        -0.02918,
        -0.01591
      ],
      "n": 1480
    }
  },
  "seriea": {
    "per_season": {
      "2021": {
        "n": 370,
        "he": 0.208,
        "r3_diff": -0.0544,
        "o_diff": -0.00513,
        "h_diff": -0.02785
      },
      "2022": {
        "n": 370,
        "he": 0.139,
        "r3_diff": -0.05716,
        "o_diff": 0.00088,
        "h_diff": -0.02531
      },
      "2023": {
        "n": 370,
        "he": 0.263,
        "r3_diff": -0.06109,
        "o_diff": -0.00306,
        "h_diff": -0.02956
      },
      "2024": {
        "n": 360,
        "he": 0.258,
        "r3_diff": -0.0615,
        "o_diff": 0.00069,
        "h_diff": -0.0266
      },
      "2025": {
        "n": 370,
        "he": 0.141,
        "r3_diff": -0.05118,
        "o_diff": 0.00318,
        "h_diff": -0.02388
      }
    },
    "r3": {
      "mean": -0.05704,
      "ci95": [
        -0.06533,
        -0.04861
      ],
      "n": 1840,
      "seasons_below_0": "5/5",
      "verdict": "RESOLUTION"
    },
    "over25": {
      "mean": -0.0007,
      "ci95": [
        -0.00363,
        0.00223
      ],
      "n": 1840,
      "seasons_below_0": "2/5",
      "verdict": "NO RESOLUTION"
    },
    "home": {
      "mean": -0.02664,
      "ci95": [
        -0.03079,
        -0.02244
      ],
      "n": 1840
    }
  },
  "ligue1": {
    "per_season": {
      "2021": {
        "n": 370,
        "he": 0.034,
        "r3_diff": -0.03806,
        "o_diff": 0.00038,
        "h_diff": -0.02394
      },
      "2022": {
        "n": 370,
        "he": 0.355,
        "r3_diff": -0.05542,
        "o_diff": 0.00196,
        "h_diff": -0.03103
      },
      "2023": {
        "n": 296,
        "he": 0.171,
        "r3_diff": -0.03531,
        "o_diff": 0.00152,
        "h_diff": -0.01638
      },
      "2024": {
        "n": 296,
        "he": 0.196,
        "r3_diff": -0.05087,
        "o_diff": -0.0075,
        "h_diff": -0.02563
      },
      "2025": {
        "n": 295,
        "he": 0.239,
        "r3_diff": -0.0346,
        "o_diff": 0.0013,
        "h_diff": -0.01565
      }
    },
    "r3": {
      "mean": -0.04321,
      "ci95": [
        -0.05208,
        -0.03403
      ],
      "n": 1627,
      "seasons_below_0": "5/5",
      "verdict": "RESOLUTION"
    },
    "over25": {
      "mean": -0.00032,
      "ci95": [
        -0.00402,
        0.00336
      ],
      "n": 1627,
      "seasons_below_0": "1/5",
      "verdict": "NO RESOLUTION"
    },
    "home": {
      "mean": -0.02298,
      "ci95": [
        -0.02809,
        -0.01812
      ],
      "n": 1627
    }
  }
}
```

## Cross-sport home-edge inputs

Original path: `research/md_only_2026-09-28/home_edges.json`. SHA-256 of original Git blob bytes: `82da7481cb62b954aacf6e30d427b34115fe62beef5a711082c8e0a7f1628201`.

```json
{
  "NBL": {
    "NBL 2023-24": {
      "games": 140,
      "home_edge": 2.83,
      "home_win_rate": 0.593,
      "mean_total": 181.21
    },
    "NBL 2024-25": {
      "games": 145,
      "home_edge": 1.39,
      "home_win_rate": 0.552,
      "mean_total": 185.7
    },
    "NBL 2025-26": {
      "games": 165,
      "home_edge": 0.65,
      "home_win_rate": 0.503,
      "mean_total": 182.5
    },
    "pooled": {
      "games": 450,
      "home_edge": 1.57,
      "home_win_rate": 0.547,
      "mean_total": 183.13
    }
  },
  "WNBA": {
    "WNBA 2024": {
      "games": 242,
      "home_edge": 0.8,
      "home_win_rate": 0.525,
      "mean_total": 163.67
    },
    "WNBA 2025": {
      "games": 288,
      "home_edge": 2.51,
      "home_win_rate": 0.557,
      "mean_total": 163.7
    },
    "WNBA 2026": {
      "games": 327,
      "home_edge": 1.72,
      "home_win_rate": 0.54,
      "mean_total": 174.41
    },
    "pooled": {
      "games": 857,
      "home_edge": 1.73,
      "home_win_rate": 0.542,
      "mean_total": 167.78
    }
  },
  "NBA": {
    "NBA 2025-26": {
      "games": 1235,
      "home_edge": 1.71,
      "home_win_rate": 0.555,
      "mean_total": 230.73
    },
    "pooled": {
      "games": 1235,
      "home_edge": 1.71,
      "home_win_rate": 0.555,
      "mean_total": 230.73
    }
  },
  "NHL": {
    "NHL 2025-26 (ESPN)": {
      "games": 1312,
      "home_edge": 0.13,
      "home_win_rate": 0.521,
      "mean_total": 6.25
    },
    "pooled": {
      "games": 1312,
      "home_edge": 0.13,
      "home_win_rate": 0.521,
      "mean_total": 6.25
    }
  },
  "EPL": {
    "EPL 2025-26": {
      "games": 380,
      "home_edge": 0.3,
      "home_win_rate": 0.426,
      "mean_total": 2.75
    },
    "pooled": {
      "games": 380,
      "home_edge": 0.3,
      "home_win_rate": 0.426,
      "mean_total": 2.75
    }
  },
  "NFL": {
    "NFL 2024": {
      "games": 272,
      "home_edge": 1.72,
      "home_win_rate": 0.524,
      "mean_total": 45.82
    },
    "NFL 2025": {
      "games": 272,
      "home_edge": 2.18,
      "home_win_rate": 0.536,
      "mean_total": 46.03
    },
    "pooled": {
      "games": 544,
      "home_edge": 1.95,
      "home_win_rate": 0.53,
      "mean_total": 45.92
    }
  },
  "AFL": {
    "AFL 2025": {
      "games": 207,
      "home_edge": 6.03,
      "home_win_rate": 0.565,
      "mean_total": 168.61
    },
    "AFL 2026": {
      "games": 207,
      "home_edge": 7.12,
      "home_win_rate": 0.585,
      "mean_total": 178.22
    },
    "pooled": {
      "games": 414,
      "home_edge": 6.57,
      "home_win_rate": 0.575,
      "mean_total": 173.42
    }
  },
  "NRL": {
    "NRL 2025": {
      "games": 216,
      "home_edge": 3.77,
      "home_win_rate": 0.551,
      "mean_total": 46.12
    },
    "NRL 2026": {
      "games": 213,
      "home_edge": 0.03,
      "home_win_rate": 0.545,
      "mean_total": 47.84
    },
    "pooled": {
      "games": 429,
      "home_edge": 1.91,
      "home_win_rate": 0.548,
      "mean_total": 46.98
    }
  },
  "MLB": {
    "MLB 2026": {
      "games": 2373,
      "home_edge": 0.07,
      "home_win_rate": 0.529,
      "mean_total": 8.95
    },
    "pooled": {
      "games": 2373,
      "home_edge": 0.07,
      "home_win_rate": 0.529,
      "mean_total": 8.95
    }
  }
}
```

## P6 previous-season home edges

Original path: `research/md_only_2026-09-28/p6_soccer_home_edges.json`. SHA-256 of original Git blob bytes: `7871d8dee990d17f2bdd2c060fad1058da7298540cf87c20c30ca4bc30aa1aab`.

```json
{
  "epl": {
    "home_edge": {
      "2020": 0.011,
      "2021": 0.208,
      "2022": 0.416,
      "2023": 0.321,
      "2024": 0.092,
      "2025": 0.303
    },
    "mean_total": {
      "2020": 2.69,
      "2021": 2.82,
      "2022": 2.85,
      "2023": 3.28,
      "2024": 2.93,
      "2025": 2.75
    },
    "games": {
      "2020": 380,
      "2021": 380,
      "2022": 380,
      "2023": 380,
      "2024": 380,
      "2025": 380
    }
  },
  "laliga": {
    "home_edge": {
      "2020": 0.229,
      "2021": 0.339,
      "2022": 0.397,
      "2023": 0.324,
      "2024": 0.292,
      "2025": 0.453
    },
    "mean_total": {
      "2020": 2.51,
      "2021": 2.5,
      "2022": 2.51,
      "2023": 2.64,
      "2024": 2.62,
      "2025": 2.69
    },
    "games": {
      "2020": 380,
      "2021": 380,
      "2022": 380,
      "2023": 380,
      "2024": 370,
      "2025": 380
    }
  },
  "bundesliga": {
    "home_edge": {
      "2020": 0.32,
      "2021": 0.405,
      "2022": 0.539,
      "2023": 0.395,
      "2024": 0.127,
      "2025": 0.32
    },
    "mean_total": {
      "2020": 3.03,
      "2021": 3.12,
      "2022": 3.17,
      "2023": 3.22,
      "2024": 3.13,
      "2025": 3.24
    },
    "games": {
      "2020": 306,
      "2021": 306,
      "2022": 306,
      "2023": 306,
      "2024": 306,
      "2025": 306
    }
  },
  "seriea": {
    "home_edge": {
      "2020": 0.208,
      "2021": 0.139,
      "2022": 0.263,
      "2023": 0.258,
      "2024": 0.141,
      "2025": 0.126
    },
    "mean_total": {
      "2020": 3.06,
      "2021": 2.87,
      "2022": 2.56,
      "2023": 2.61,
      "2024": 2.55,
      "2025": 2.43
    },
    "games": {
      "2020": 380,
      "2021": 380,
      "2022": 380,
      "2023": 380,
      "2024": 370,
      "2025": 380
    }
  },
  "ligue1": {
    "home_edge": {
      "2020": 0.034,
      "2021": 0.355,
      "2022": 0.171,
      "2023": 0.196,
      "2024": 0.239,
      "2025": 0.344
    },
    "mean_total": {
      "2020": 2.76,
      "2021": 2.81,
      "2022": 2.81,
      "2023": 2.7,
      "2024": 2.98,
      "2025": 2.83
    },
    "games": {
      "2020": 380,
      "2021": 380,
      "2022": 380,
      "2023": 306,
      "2024": 306,
      "2025": 305
    }
  }
}
```

## Probability-table arithmetic checks

Original path: `research/md_only_2026-09-28/tables_check.json`. SHA-256 of original Git blob bytes: `04b0e7a2c0952624ef5085e1b64c86f2860765de9420b184de85633707af78ed`.

```json
{
  "rm1_table_mismatches_vs_tool": 0,
  "skellam_by2_gap": 9.43689570931383e-16,
  "no_zero_formula_gap": 0.0,
  "no_zero_cover_gap": 0.0
}
```

## Historical cross-sport evaluation implementation

Original path: `research/md_only_2026-09-28/validate_tb1_md.py`. SHA-256 of original Git blob bytes: `b5a03ed665d53c485f229ef1dc24d5778a1e5b208d6228ba6fe9ec42216e9295`.

```python
"""Does the hand-computable TB-1 (TB-1-MD, PROBABILITY_TOOLKIT.md §4) score like the tool's TB-1?

Why. From 2026-09-28 the forecasting model reads Markdown only and cannot run tools/team_baseline.py.
TB-1-MD is the same rating arithmetic done by hand from a standings page, with three simplifications:
1. the width is the league's fixed reference SD (the tool switches to a running residual SD after 20 games);
2. the home edge is a fixed reference (the previous season's mean home margin where one exists);
3. z is rounded to two decimals (a Phi-table lookup), and no previous-season carry-over is used.
This script scores both on the same games, leak-free (each game from games strictly before it), against
the running population rate A0. Brier on P(home win) and on P(total > running league mean).
Week-block 95% intervals for TB1MD - TB1 and TB1MD - A0. Writes validate_tb1_md.json.
"""
import datetime as dt
import json
import math
import os
import random
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "research", "team_baseline_2026-09-25e"))
import validate_team_baseline as vtb  # noqa: E402  (chdirs into the base-rate folder)

tb = vtb.tb
TOOL = {lg: tb.LEAGUES[lg.lower()] for lg in ("NBA", "WNBA", "NBL", "NHL", "EPL", "MLB", "NFL", "AFL", "NRL")}


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def phi_table(z):
    z = max(-3.49, min(3.49, round(z, 2)))
    return phi(z)


def md_ratings(pf, pa, n, lm, k):
    if n + k == 0:
        return lm, lm
    return (pf + k * lm) / (n + k), (pa + k * lm) / (n + k)


def season_rows(games, k_tool, r_tool, kind, sd_m_ref, sd_t_ref, he_ref, k_md):
    """Walk one season. Returns per-game rows with tool TB-1, TB-1-MD and A0 probabilities."""
    state = tb.SeasonState(prior=None, k=k_tool, carry=r_tool, sd_total=sd_t_ref, sd_margin=sd_m_ref)
    pf, pa, n = defaultdict(float), defaultdict(float), defaultdict(int)
    tot_pts, tot_gp = 0.0, 0
    rows = []
    for g in sorted(games, key=lambda x: x["date"]):
        h, a = g["home"], g["away"]
        if min(state.n_games(h), state.n_games(a)) >= 1 and state.n_league_games() >= 10:
            pred = state.predict(h, a, neutral=g["neutral"])
            sd_m, sd_t = state.resid_sd()
            ref_total = state.league_total_mean()
            lm = tot_pts / tot_gp
            oh, dh = md_ratings(pf[h], pa[h], n[h], lm, k_md)
            oa, da = md_ratings(pf[a], pa[a], n[a], lm, k_md)
            t_md = (oh + da) / 2 + (oa + dh) / 2
            m_md = ((oh - dh) - (oa - da)) / 2 + (0.0 if g["neutral"] else he_ref)
            if kind == "poisson":
                lh, la = tb.team_means(pred["total"], pred["margin"])
                p_tool = tb.poisson_win(lh, la)
                o_tool = tb.poisson_total_over(lh + la, ref_total)
                lh2, la2 = tb.team_means(t_md, m_md)
                p_md = tb.poisson_win(round(lh2, 1), round(la2, 1))     # a 0.1-step Poisson table
                o_md = tb.poisson_total_over(round(lh2 + la2, 1), ref_total)
            else:
                p_tool = phi(pred["margin"] / sd_m)
                o_tool = 1 - phi((ref_total - pred["total"]) / sd_t)
                p_md = phi_table(m_md / sd_m_ref)
                o_md = 1 - phi_table((ref_total - t_md) / sd_t_ref)
            y = 1 if g["hs"] > g["as"] else 0
            yo = 1 if g["hs"] + g["as"] > ref_total else 0
            rows.append({"week": str(dt.date.fromisoformat(g["date"][:10]).isocalendar()[:2]),
                         "bh_tool": (p_tool - y) ** 2, "bh_md": (p_md - y) ** 2,
                         "bh_a0": (state.home_win_rate() - y) ** 2,
                         "bo_tool": (o_tool - yo) ** 2, "bo_md": (o_md - yo) ** 2,
                         "bo_a0": (state.over_rate() - yo) ** 2,
                         "p_md": p_md, "y": y, "p_tool": p_tool})
        state.add(g)
        pf[h] += g["hs"]; pa[h] += g["as"]; pf[a] += g["as"]; pa[a] += g["hs"]
        n[h] += 1; n[a] += 1
        tot_pts += g["hs"] + g["as"]; tot_gp += 2
    return rows


def home_edge(games):
    ed = [g["hs"] - g["as"] for g in games if not g["neutral"]]
    return sum(ed) / len(ed)


def boot(rows, a, b, n=2000, seed=20260928):
    blocks = defaultdict(list)
    for r in rows:
        blocks[r["week"]].append(r[a] - r[b])
    keys = list(blocks)
    tot = sum(len(v) for v in blocks.values())
    mean = sum(sum(v) for v in blocks.values()) / tot
    rng = random.Random(seed)
    st = []
    for _ in range(n):
        s = [blocks[rng.choice(keys)] for _ in keys]
        st.append(sum(sum(v) for v in s) / sum(len(v) for v in s))
    st.sort()
    return {"mean": round(mean, 5), "ci95": [round(st[int(0.025 * n)], 5), round(st[int(0.975 * n) - 1], 5)], "n": tot}


def main():
    out = {}
    chains = {lg: vtb.load_chain(lg) for lg in vtb.CHAINS}
    chains["MLB"] = vtb.load_mlb()
    for lg, seasons in chains.items():
        cfg = TOOL[lg]
        kind = "poisson" if cfg["kind"] == "poisson" else "normal"
        rows, he_used = [], []
        for i, s in enumerate(seasons):
            if len(seasons) > 1 and i == 0:
                continue                      # the first season only supplies the reference home edge
            he_ref = home_edge(seasons[i - 1]) if i > 0 else home_edge(s)   # single-season chains: in-sample
            he_used.append(round(he_ref, 3))
            rows += season_rows(s, cfg["k"], 0.0, kind, cfg["sd_margin"], cfg["sd_total"], he_ref, cfg["k"])
        mean = lambda key: round(sum(r[key] for r in rows) / len(rows), 4)  # noqa: E731
        maxdiff = max(abs(r["p_md"] - r["p_tool"]) for r in rows)
        out[lg] = {"seasons_scored": vtb.CHAINS.get(lg, ["MLB 2026"])[1 if len(seasons) > 1 else 0:],
                   "home_edge_ref": he_used, "home_edge_source": "previous season" if len(seasons) > 1 else "same season (in-sample)",
                   "k": cfg["k"], "sd_margin": cfg["sd_margin"], "sd_total": cfg["sd_total"], "n": len(rows),
                   "brier_home": {"tb1_tool": mean("bh_tool"), "tb1_md": mean("bh_md"), "a0": mean("bh_a0")},
                   "brier_over": {"tb1_tool": mean("bo_tool"), "tb1_md": mean("bo_md"), "a0": mean("bo_a0")},
                   "home_md_minus_tool": boot(rows, "bh_md", "bh_tool"), "home_md_minus_a0": boot(rows, "bh_md", "bh_a0"),
                   "over_md_minus_tool": boot(rows, "bo_md", "bo_tool"), "over_md_minus_a0": boot(rows, "bo_md", "bo_a0"),
                   "max_abs_p_home_gap": round(maxdiff, 4)}
        print(lg, json.dumps(out[lg]), flush=True)
    json.dump(out, open(os.path.join(HERE, "validate_tb1_md.json"), "w"), indent=2)


if __name__ == "__main__":
    main()
```

## Historical P6 evaluation implementation

Original path: `research/md_only_2026-09-28/p6_soccer_tb1md.py`. SHA-256 of original Git blob bytes: `6f2170e8b5c04b25ca6a2e6df292dd08b6c6193965023ab6ce3e5dfd4c81dd5f`.

```python
"""P6 (preregistered in PREREGISTRATION_P6.md) — TB-1-MD resolution in the top five soccer leagues."""
import datetime as dt
import json
import math
import os
import random
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "research", "sport_models_2026-09-26"))
import validate_public as vp  # noqa: E402

K = 2
LEAGUES = ["epl", "laliga", "bundesliga", "seriea", "ligue1"]
SCORED = [2021, 2022, 2023, 2024, 2025]
BOOT, SEED = 2000, 20260928


def pois(k, lam):
    return math.exp(-lam + k * math.log(lam) - math.lgamma(k + 1))


def probs(lh, la):
    lh, la = max(lh, 0.05), max(la, 0.05)
    ph = sum(pois(i, lh) * pois(j, la) for i in range(15) for j in range(i))
    pd = sum(pois(i, lh) * pois(i, la) for i in range(15))
    mu = lh + la
    po = 1 - sum(pois(k, mu) for k in range(3))
    return ph, pd, 1 - ph - pd, po


def season_rows(games, he):
    pf, pa, n = defaultdict(float), defaultdict(float), defaultdict(int)
    pts, gp = 0.0, 0
    hw = dr = aw = ov = tot = 0
    rows = []
    for g in sorted(games, key=lambda x: x["date"]):
        h, a = g["home"], g["away"]
        if n[h] >= 1 and n[a] >= 1 and tot >= 10:
            lm = pts / gp
            oh, dh = (pf[h] + K * lm) / (n[h] + K), (pa[h] + K * lm) / (n[h] + K)
            oa, da = (pf[a] + K * lm) / (n[a] + K), (pa[a] + K * lm) / (n[a] + K)
            t = (oh + da) / 2 + (oa + dh) / 2
            m = ((oh - dh) - (oa - da)) / 2 + he
            ph, pd, pa_, po = probs((t + m) / 2, (t - m) / 2)
            bh, bd, ba, bo = hw / tot, dr / tot, aw / tot, ov / tot
            yh, yd, ya = int(g["hs"] > g["as"]), int(g["hs"] == g["as"]), int(g["hs"] < g["as"])
            yo = int(g["hs"] + g["as"] >= 3)
            rows.append({"week": str(dt.date.fromisoformat(g["date"][:10]).isocalendar()[:2]), "season": g["season"],
                         "r3_md": (ph - yh) ** 2 + (pd - yd) ** 2 + (pa_ - ya) ** 2,
                         "r3_pop": (bh - yh) ** 2 + (bd - yd) ** 2 + (ba - ya) ** 2,
                         "o_md": (po - yo) ** 2, "o_pop": (bo - yo) ** 2,
                         "h_md": (ph - yh) ** 2, "h_pop": (bh - yh) ** 2})
        pf[h] += g["hs"]; pa[h] += g["as"]; pf[a] += g["as"]; pa[a] += g["hs"]
        n[h] += 1; n[a] += 1; pts += g["hs"] + g["as"]; gp += 2
        tot += 1; hw += g["hs"] > g["as"]; dr += g["hs"] == g["as"]; aw += g["hs"] < g["as"]
        ov += g["hs"] + g["as"] >= 3
    return rows


def boot(rows, a, b):
    blocks = defaultdict(list)
    for r in rows:
        blocks[(r["season"], r["week"])].append(r[a] - r[b])
    keys = list(blocks)
    tot = sum(len(v) for v in blocks.values())
    mean = sum(sum(v) for v in blocks.values()) / tot
    rng = random.Random(SEED)
    st = []
    for _ in range(BOOT):
        s = [blocks[rng.choice(keys)] for _ in keys]
        st.append(sum(sum(v) for v in s) / sum(len(v) for v in s))
    st.sort()
    return {"mean": round(mean, 5), "ci95": [round(st[int(0.025 * BOOT)], 5), round(st[int(0.975 * BOOT) - 1], 5)], "n": tot}


def main():
    out = {"preregistration": "PREREGISTRATION_P6.md", "k": K}
    for lg in LEAGUES:
        games = vp.soccer(lg)
        by = defaultdict(list)
        for g in games:
            by[g["season"]].append(g)
        rows, per = [], {}
        for s in SCORED:
            prev = by.get(s - 1, [])
            if not prev or not by.get(s):
                continue
            he = sum(g["hs"] - g["as"] for g in prev) / len(prev)
            r = season_rows(by[s], he)
            rows += r
            mean = lambda k: sum(x[k] for x in r) / len(r)  # noqa: E731
            per[str(s)] = {"n": len(r), "he": round(he, 3), "r3_diff": round(mean("r3_md") - mean("r3_pop"), 5),
                           "o_diff": round(mean("o_md") - mean("o_pop"), 5), "h_diff": round(mean("h_md") - mean("h_pop"), 5)}
        res = {"per_season": per, "r3": boot(rows, "r3_md", "r3_pop"), "over25": boot(rows, "o_md", "o_pop"),
               "home": boot(rows, "h_md", "h_pop")}
        for key, dk in (("r3", "r3_diff"), ("over25", "o_diff")):
            neg = sum(1 for v in per.values() if v[dk] < 0)
            res[key]["seasons_below_0"] = f"{neg}/{len(per)}"
            res[key]["verdict"] = "RESOLUTION" if res[key]["ci95"][1] < 0 and neg >= 4 else "NO RESOLUTION"
        out[lg] = res
        print(lg, json.dumps({k: res[k] for k in ("r3", "over25", "home")}), flush=True)
    json.dump(out, open(os.path.join(HERE, "p6_soccer_tb1md.json"), "w"), indent=2)


if __name__ == "__main__":
    main()
```

## Historical table-generation implementation

Original path: `research/md_only_2026-09-28/make_tables.py`. SHA-256 of original Git blob bytes: `cc7c2377c2a5cf47f70662ec31db4fc2ec9336593072a15b931409033c711025`.

```python
"""Generate the lookup tables printed in PROBABILITY_TOOLKIT.md, and check them against the tools.

Outputs tables_*.md fragments in this folder plus tables_check.json. The toolkit copies the fragments
verbatim. Every table is a pure function of the stated inputs (no data, no odds):
- RM-1 q by stated p (tools/rank_model.py coefficients, verified row by row against rank_model.score_row);
- standard normal Phi(z);
- Poisson: soccer 1X2 grid, total goals, first half; hockey totals;
- negative binomial total runs (baseball) at three widths;
- no-tie normal margin win and cover probabilities (basketball, NFL, AFL, NRL);
- Elo difference -> win probability; logit(p).
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "tools"))
import card_math as cm  # noqa: E402
import rank_model as rm  # noqa: E402

COEF = rm.load_coef()
checks = {}


def write(name, text):
    with open(os.path.join(HERE, name), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text.rstrip() + "\n")


# ---------------------------------------------------------------- RM-1
def q_decision(p, cushion):
    w = COEF["weights"]
    lp = math.log(p / (1 - p))
    x = w["intercept"] + w["logit_p"] * lp + (w["cushion_nb"] if cushion else 0.0)
    return 1 / (1 + math.exp(-x))


rows = ["| Stated p | q, standard row | q, cushion row (C) | logit(p) |", "|---:|---:|---:|---:|"]
mism = 0
for i in range(50, 98):
    p = i / 100
    qs = min(max(q_decision(p, False), 0.03), 0.97) if p > 0.5 else 0.5
    qc = min(max(q_decision(p, True), 0.03), 0.97) if p > 0.5 else 0.5
    lg = math.log(p / (1 - p))
    rows.append(f"| {p:.2f} | {qs:.3f} | {qc:.3f} | {lg:+.3f} |")
    # check against the tool: a standard row (Over 8.5, mlb) and a cushion row (Hawks +3.5, nbl)
    t1 = rm.score_row(COEF, "mlb", "Over 8.5 runs", p)["q"]
    t2 = rm.score_row(COEF, "nbl", "Hawks +3.5", p)["q"]
    mism += (abs(round(t1, 3) - round(qs, 3)) > 0.0005) + (abs(round(t2, 3) - round(qc, 3)) > 0.0005)
    # below 0.5: the complement rule
    pb = 1 - p
    if pb < 0.5:
        t3 = rm.score_row(COEF, "mlb", "Under 8.5 runs", pb)["q"]          # standard row stated below 0.5
        t4 = rm.score_row(COEF, "nbl", "Hawks +3.5", pb)["q"]              # cushion stated below 0.5 -> 1 - q_std(1-p)
        t5 = rm.score_row(COEF, "nbl", "Bullets -3.5", pb)["q"]            # favourite -k.5 below 0.5 -> 1 - q_C(1-p)
        mism += (abs(t3 - (1 - min(max(q_decision(p, False), 0.03), 0.97))) > 1e-9)
        mism += (abs(t4 - (1 - min(max(q_decision(p, False), 0.03), 0.97))) > 1e-9)
        mism += (abs(t5 - (1 - min(max(q_decision(p, True), 0.03), 0.97))) > 1e-9)
checks["rm1_table_mismatches_vs_tool"] = mism
write("tables_rm1.md", "\n".join(rows))

# ---------------------------------------------------------------- Phi
lines = ["| z | .00 | .01 | .02 | .03 | .04 | .05 | .06 | .07 | .08 | .09 |", "|---:|" + "---:|" * 10]
for i in range(0, 35):
    z0 = i / 10
    cells = [f"{cm._norm_cdf(z0 + j / 100):.4f}" for j in range(10)]
    lines.append(f"| {z0:.1f} | " + " | ".join(cells) + " |")
write("tables_phi.md", "\n".join(lines))


# ---------------------------------------------------------------- Poisson
def pois(k, lam):
    return math.exp(-lam + k * math.log(lam) - math.lgamma(k + 1))


grid = [round(0.6 + 0.2 * i, 1) for i in range(11)]
hdr = "| λ home \\ λ away | " + " | ".join(f"{x:.1f}" for x in grid) + " |"
sep = "|---:|" + "---:|" * len(grid)
win_rows, draw_rows = [hdr, sep], [hdr, sep]
for lh in grid:
    w, d = [], []
    for la in grid:
        pw = sum(pois(i, lh) * pois(j, la) for i in range(20) for j in range(i))
        pd = sum(pois(i, lh) * pois(i, la) for i in range(20))
        w.append(f"{pw:.3f}")
        d.append(f"{pd:.3f}")
    win_rows.append(f"| **{lh:.1f}** | " + " | ".join(w) + " |")
    draw_rows.append(f"| **{lh:.1f}** | " + " | ".join(d) + " |")
write("tables_soccer_home.md", "\n".join(win_rows))
write("tables_soccer_draw.md", "\n".join(draw_rows))
by2 = [hdr, sep]
for lh in grid:
    cells = []
    for la in grid:
        p2 = sum(pois(i, lh) * pois(j, la) for i in range(20) for j in range(20) if i - j >= 2)
        cells.append(f"{p2:.3f}")
    by2.append(f"| **{lh:.1f}** | " + " | ".join(cells) + " |")
write("tables_soccer_home_by2.md", "\n".join(by2))
# check the soccer tables against card_math's Skellam
d = cm.Dist("skellam", mu=1.6, mu_opp=1.0)
checks["skellam_by2_gap"] = abs(cm.p_over(d, 1.5) - sum(pois(i, 1.6) * pois(j, 1.0) for i in range(20) for j in range(20) if i - j >= 2))

tot = ["| μ total | P(0) | P(≤1) | P(≤2) | P(≤3) | P(≤4) | P(≤5) | P(≤6) |", "|---:|" + "---:|" * 7]
for i in range(6, 51):
    mu = i / 10
    c, cells = 0.0, []
    for k in range(7):
        c += pois(k, mu)
        cells.append(f"{c:.3f}")
    tot.append(f"| {mu:.1f} | " + " | ".join(cells) + " |")
write("tables_goals_total.md", "\n".join(tot))

hk = ["| μ total | P(≤3) | P(≤4) | P(≤5) | P(≤6) | P(≤7) | P(≤8) |", "|---:|" + "---:|" * 6]
for i in range(45, 76):
    mu = i / 10
    cum = [sum(pois(k, mu) for k in range(n + 1)) for n in range(3, 9)]
    hk.append(f"| {mu:.1f} | " + " | ".join(f"{c:.3f}" for c in cum) + " |")
write("tables_hockey_total.md", "\n".join(hk))

# ---------------------------------------------------------------- negative binomial (baseball runs)
nb = []
for sd in (4.0, 4.5, 5.0):
    nb.append(f"**Width (SD) {sd:.1f}.** P(Over L) = P(total runs ≥ L + 0.5).\n")
    lines_ = [5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5]
    nb.append("| Mean | " + " | ".join(f"O {x}" for x in lines_) + " |")
    nb.append("|---:|" + "---:|" * len(lines_))
    for i in range(0, 25):
        mean = 6.0 + 0.25 * i
        d = cm.Dist("negbin", mean=mean, sd=sd)
        nb.append(f"| {mean:.2f} | " + " | ".join(f"{cm.p_over(d, L):.3f}" for L in lines_) + " |")
    nb.append("")
write("tables_baseball_total.md", "\n".join(nb))
# integer-line push masses at the reference width
push = ["| Mean | P(total = 7) | P(= 8) | P(= 9) |", "|---:|---:|---:|---:|"]
for i in range(0, 13):
    mean = 6.5 + 0.5 * i
    d = cm.Dist("negbin", mean=mean, sd=4.5)
    push.append(f"| {mean:.1f} | " + " | ".join(f"{d.pmf(k):.3f}" for k in (7, 8, 9)) + " |")
write("tables_baseball_push.md", "\n".join(push))

# ---------------------------------------------------------------- no-tie normal margins
def win_no_zero(m, sd):
    p0 = cm._norm_cdf((0.5 - m) / sd) - cm._norm_cdf((-0.5 - m) / sd)
    pgt = 1 - cm._norm_cdf((0.5 - m) / sd)
    return pgt / (1 - p0)


mt = ["| Expected margin m ÷ width | P(win), no tie | P(win), with continuity only |", "|---:|---:|---:|"]
for i in range(0, 21):
    r = i / 20
    mt.append(f"| {r:.2f} | {win_no_zero(r * 15.1, 15.1):.3f} | {cm._norm_cdf(r):.3f} |")
write("tables_margin_win.md", "\n".join(mt))
# check: the hand formula equals card_math's no-zero normal
d = cm.Dist("normal", mean=4.0, sd=15.1, no_zero=True)
checks["no_zero_formula_gap"] = abs(cm.p_over(d, 0) - win_no_zero(4.0, 15.1))
w_tool, _ = cm.p_cover(d, -3.5)
p0 = cm._norm_cdf(0.5 / 15.1 - 4 / 15.1) - cm._norm_cdf(-0.5 / 15.1 - 4 / 15.1)
hand = (1 - cm._norm_cdf((3.5 + 0.5 - 0.5 - 4.0) / 15.1)) / (1 - p0)   # P(X >= 4) = 1 - Phi((3.5 - m)/sd)
checks["no_zero_cover_gap"] = abs(w_tool - hand)

# ---------------------------------------------------------------- Elo and logit
el = ["| Elo gap | P(stronger wins) | Elo gap | P | Elo gap | P |", "|---:|---:|---:|---:|---:|---:|"]
vals = list(range(0, 510, 10))
third = (len(vals) + 2) // 3
for i in range(third):
    cells = []
    for j in range(3):
        k = i + j * third
        if k < len(vals):
            g = vals[k]
            cells += [str(g), f"{1 / (1 + 10 ** (-g / 400)):.3f}"]
        else:
            cells += ["", ""]
    el.append("| " + " | ".join(cells) + " |")
write("tables_elo.md", "\n".join(el))

json.dump(checks, open(os.path.join(HERE, "tables_check.json"), "w"), indent=2)
print(json.dumps(checks))
```
