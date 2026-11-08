# Failed evaluation export

The first live export stopped at PAIRED_INTERVALS.csv because log-loss intervals include infinite-loss count columns absent from Brier intervals. Its partial files are retained as failed evidence, not a complete evaluation. Fixed in ml/cycle.py with a regression test; the rerun is nba_shadow_evaluation_final/.
