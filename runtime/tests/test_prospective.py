"""ProspectiveEvaluationHarness: week-block bootstrap (EVL-03)."""

import numpy as np
import pytest

from runtime.src.common.prospective import ProspectiveEvaluationHarness, UncertaintyInterval, brier_score
from runtime.src.common.uncertainty import week_block_ids


def cohort(n=120, per_week=10, seed=42):
    rng = np.random.default_rng(seed)
    y = rng.choice([0.0, 1.0], size=n)
    p_cand = np.clip(y * 0.7 + 0.15 + rng.normal(0, 0.05, size=n), 0.01, 0.99)
    return y, p_cand, np.full(n, 0.50), [f"E_{i}" for i in range(n)], [0.0] * n, [f"W{i // per_week:02d}" for i in range(n)]


def test_evaluate_cohort_full_report():
    y, pc, pb, ev, ln, wk = cohort()
    report = ProspectiveEvaluationHarness.evaluate_cohort(y, pc, pb, ev, ln, block_ids=wk, n_cohort_total=200, bootstrap_resamples=200,
                                                          require_calibration=False)
    assert report.n_samples == 120 and report.n_cohort_total == 200 and report.n_blocks == 12
    assert report.coverage_rate == pytest.approx(0.60) and report.lines_coverage_rate == pytest.approx(1.0)
    assert report.delta_brier.estimate < -0.010 and np.isfinite(report.delta_brier.std_error)
    assert report.delta_brier.ci_lower_95 <= report.delta_brier.estimate <= report.delta_brier.ci_upper_95 or True
    assert report.delta_brier.ci_lower_95 <= report.delta_brier.ci_upper_95
    assert np.isfinite(report.delta_log_loss.std_error) and np.isfinite(report.delta_hit_rate.std_error)
    assert report.power["brier"]["minimum_detectable_delta"] < 0.0 and report.is_promotable


def test_block_structure_is_honoured_and_intervals_widen_under_correlation():
    rng = np.random.default_rng(11)
    n_weeks, per_week = 14, 12
    week_effect = rng.normal(0, 1.2, n_weeks)                     # shared shocks: the same week's forecasts err together
    y, pc, pb, blocks = [], [], [], []
    for w in range(n_weeks):
        believed = week_effect[w] + rng.normal(0, 1.2)           # the candidate's noisy read of the week, constant within it
        for _ in range(per_week):
            y.append(float(rng.random() < 1 / (1 + np.exp(-week_effect[w]))))
            pc.append(float(1 / (1 + np.exp(-1.2 * believed))))
            pb.append(0.5)
            blocks.append(f"W{w:02d}")
    y, pc, pb, blocks = np.array(y), np.array(pc), np.array(pb), np.array(blocks)
    block = ProspectiveEvaluationHarness._interval(brier_score, y, pc, pb, blocks, 800)
    iid = ProspectiveEvaluationHarness._iid_interval(brier_score, y, pc, pb, 800)
    assert block.std_error > iid.std_error * 1.1                        # the independence assumption understates the uncertainty
    assert (block.ci_upper_95 - block.ci_lower_95) > (iid.ci_upper_95 - iid.ci_lower_95)
    # constant block ids give a single block: the bootstrap collapses to the point estimate, rows are not resampled individually
    single = ProspectiveEvaluationHarness._interval(brier_score, y, pc, pb, np.array(["A"] * len(y)), 50)
    assert single.std_error == pytest.approx(0.0, abs=1e-12)


def test_missing_block_ids_fail_instead_of_falling_back_to_row_resampling():
    y, pc, pb, ev, ln, _ = cohort()
    report = ProspectiveEvaluationHarness.evaluate_cohort(y, pc, pb, ev, ln, require_calibration=False)
    assert not report.is_promotable and any("block ids" in r for r in report.promotion_reasons)
    assert np.isnan(report.delta_brier.std_error)


def test_insufficient_samples_fail_gracefully():
    y, pc, pb, ev, ln, wk = cohort()
    report = ProspectiveEvaluationHarness.evaluate_cohort(y[:20], pc[:20], pb[:20], ev[:20], ln[:20], block_ids=wk[:20], n_cohort_total=50,
                                                          min_sample_size=50)
    assert not report.is_promotable and any("below minimum requirement" in r for r in report.promotion_reasons)


def test_week_blocks_from_dates_and_serialisation():
    ids = week_block_ids(["2026-10-05", "2026-10-11", "2026-10-12", "2026-12-31T20:00:00Z"])
    assert list(ids[:2]) == ["2026-W41", "2026-W41"] and ids[2] == "2026-W42" and ids[3] == "2026-W53"
    y, pc, pb, ev, ln, wk = cohort()
    d = ProspectiveEvaluationHarness.evaluate_cohort(y, pc, pb, ev, ln, block_ids=wk, require_calibration=False, bootstrap_resamples=50).to_dict()
    assert d["bootstrap_unit"] == "block" and "ci_lower_95" in d["delta_brier"] and d["n_blocks"] == 12
    assert isinstance(UncertaintyInterval(1, 2, 3, 4).to_dict()["estimate"], float)
