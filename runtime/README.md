# MDS-v8.0 Numerical Predictive Modeling Runtime

The **MDS-v8.0 Numerical Predictive Modeling Runtime** provides the core quantitative infrastructure underlying the repository's sports analysis and research standards.

---

## 1. Core Principles

1. **Event-First Distribution Modeling**: All contracts (Moneyline, Spread, Total, Double Chance, Draw-No-Bet, BTTS, Team Total) are derived strictly from a coherent underlying joint score probability distribution matrix $P(Y_{\text{home}} = s_1, Y_{\text{away}} = s_2)$.
2. **Mathematical Invariant Guarantees**:
   - Monotonicity: For any lines $L_1 < L_2$, $P(\text{Over } L_1) \ge P(\text{Over } L_2)$ and $P(\text{Under } L_1) \le P(\text{Under } L_2)$.
   - Covering Pair Consistency: $P(\text{Home } +k) \ge P(\text{Home ML})$ for all $k \ge 0$.
   - Probability Sum Rule: $P(\text{Over } L) + P(\text{Under } L) + P(\text{Push } L) = 1.0$.
3. **Point-in-Time Provenance & Leakage Protection**: Strict enforcement of $t_{\text{known\_at}} \le t_{\text{cutoff\_at}}$. Accessing any feature timestamped after the pregame cutoff immediately raises `DataLeakageError`.
4. **Chronological Rolling-Origin Splits**: Partitions data into sequential folds:
   $$\text{TRAIN} \longrightarrow \text{TUNE} \longrightarrow \text{CAL} \longrightarrow \text{TEST}$$
   Model weights are never fit on `CAL` or `TEST`. Probability calibrators (Platt scaling, Isotonic regression) are fit exclusively on `CAL`.
5. **Frozen D0 vs Independent H0 Separation**: The historical benchmark log D0 is permanently frozen for qualitative error taxonomy. Numerical models are trained exclusively on independent population H0 datasets.

---

## 2. Directory Layout

```
runtime/
├── pyproject.toml
├── README.md
├── config/
│   ├── sources/sources.json
│   ├── models/models.json
│   └── sports/
│       ├── cricket.json
│       ├── basketball.json
│       ├── nfl.json
│       ├── baseball.json
│       ├── afl.json
│       ├── nrl.json
│       ├── soccer.json
│       └── nhl.json
├── src/
│   ├── common/
│   │   ├── identity.py
│   │   ├── provenance.py
│   │   ├── contracts.py
│   │   ├── splits.py
│   │   ├── calibration.py
│   │   ├── evaluation.py
│   │   └── bigquery_ml.py
│   └── sports/
│       ├── base.py
│       ├── cricket/engine.py
│       ├── basketball/engine.py
│       ├── nfl/engine.py
│       ├── baseball/engine.py
│       ├── afl/engine.py
│       ├── nrl/engine.py
│       ├── soccer/engine.py
│       └── nhl/engine.py
├── r_ingestion/
│   ├── afl_fitzroy.R
│   └── nrl_nrlr.R
└── tests/
    ├── test_identity.py
    ├── test_provenance.py
    ├── test_contracts.py
    ├── test_splits.py
    ├── test_calibration.py
    ├── test_evaluation.py
    ├── test_bigquery_ml.py
    └── test_sport_engines.py
```

---

## 3. Running the Test Suite

Execute pytest across the full repository test suite:
```bash
py -3.14 -B -m pytest -p no:cacheprovider research/tests research/operations runtime/tests -q
```

