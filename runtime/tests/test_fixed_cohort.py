"""Unit tests for fixed-cohort comparative evaluation."""

import numpy as np

from runtime.src.common.evaluation import FixedCohortEvaluator


def weeks(n, per_week=10):
    """Block ids: `per_week` consecutive forecasts share a week."""
    return [f"W{i // per_week:02d}" for i in range(n)]


def test_fixed_cohort_promotion_pass():
    np.random.seed(42)
    n = 100
    y_true = np.random.binomial(1, 0.6, size=n).astype(float)
    
    # Baseline is noisy around 0.55
    p_base = np.clip(np.random.normal(0.55, 0.15, size=n), 0.1, 0.9)
    # Candidate has genuine skill and matches true probability
    p_cand = np.clip(y_true * 0.4 + 0.4 + np.random.normal(0, 0.05, size=n), 0.1, 0.9)
    events = [f"e_{i}" for i in range(n)]
    lines = [0.0] * n

    res = FixedCohortEvaluator.evaluate(
        y_true, p_cand, p_base,
        event_ids_cand=events, event_ids_base=events,
        lines_cand=lines, lines_base=lines,
        require_calibration=False, block_ids=weeks(n), n_resamples=300,
    )
    assert res["n_samples"] == n
    assert res["delta_brier"] < -0.010
    assert res["delta_log_loss"] < 0.0
    assert res["delta_brier_ci"][1] < 0.0 and res["delta_log_loss_ci"][1] < 0.0
    assert res["decision_stable"] is True and res["power"]["brier"]["minimum_detectable_delta"] < 0.0
    assert res["is_promotable"] is True


def test_fixed_cohort_promotion_fail_on_log_loss():
    n = 50
    y_true = np.array([1.0] * 25 + [0.0] * 25)
    p_base = np.array([0.6] * 25 + [0.4] * 25)
    # Candidate makes one extreme overconfident wrong prediction
    p_cand = p_base.copy()
    p_cand[0] = 0.0001  # True is 1! Huge log loss explosion
    events = [f"e_{i}" for i in range(n)]
    lines = [0.0] * n

    res = FixedCohortEvaluator.evaluate(
        y_true, p_cand, p_base,
        event_ids_cand=events, event_ids_base=events,
        lines_cand=lines, lines_base=lines,
        require_calibration=False, block_ids=weeks(n, 5), n_resamples=200,
    )
    assert res["delta_log_loss"] > 0.0
    assert res["is_promotable"] is False
    assert any("LogLoss" in r for r in res["promotion_reasons"])


def test_fixed_cohort_empty_dataset_fails():
    """Verify that an empty dataset strictly returns is_promotable=False."""
    res = FixedCohortEvaluator.evaluate(np.array([]), np.array([]), np.array([]))
    assert res["is_promotable"] is False
    assert res["n_samples"] == 0
    assert any("Empty" in r for r in res["promotion_reasons"])


def test_fixed_cohort_nan_predictions_fail():
    """Verify that predictions containing NaN strictly return is_promotable=False."""
    y_true = np.array([1.0, 0.0, 1.0, 0.0] * 15)  # n = 60
    p_base = np.array([0.5] * 60)
    p_cand = np.array([0.5] * 60)
    p_cand[5] = np.nan
    events = [f"e_{i}" for i in range(60)]
    lines = [0.0] * 60

    res = FixedCohortEvaluator.evaluate(
        y_true, p_cand, p_base,
        event_ids_cand=events, event_ids_base=events,
        lines_cand=lines, lines_base=lines,
    )
    assert res["is_promotable"] is False
    assert any("NaN" in r for r in res["promotion_reasons"])


def test_fixed_cohort_insufficient_sample_size_fails():
    """Verify that sample sizes below min_sample_size (default 50) fail promotion."""
    y_true = np.array([1.0, 0.0, 1.0, 0.0] * 5)  # n = 20
    p_base = np.array([0.5] * 20)
    p_cand = np.array([0.9, 0.1] * 10)
    events = [f"e_{i}" for i in range(20)]
    lines = [0.0] * 20

    res = FixedCohortEvaluator.evaluate(
        y_true, p_cand, p_base,
        event_ids_cand=events, event_ids_base=events,
        lines_cand=lines, lines_base=lines,
        min_sample_size=50
    )
    assert res["is_promotable"] is False
    assert any("minimum requirement" in r for r in res["promotion_reasons"])


def test_fixed_cohort_non_binary_labels_fail():
    """Verify that non-binary outcome labels fail promotion."""
    y_true = np.array([1.0, 0.5, 0.0, 2.0] * 15)  # n = 60, non-binary
    p_base = np.array([0.5] * 60)
    p_cand = np.array([0.6] * 60)
    events = [f"e_{i}" for i in range(60)]
    lines = [0.0] * 60

    res = FixedCohortEvaluator.evaluate(
        y_true, p_cand, p_base,
        event_ids_cand=events, event_ids_base=events,
        lines_cand=lines, lines_base=lines,
    )
    assert res["is_promotable"] is False
    assert any("binary" in r for r in res["promotion_reasons"])


def test_fixed_cohort_missing_or_empty_event_ids_fail():
    """Verify that omitted or empty event IDs fail promotion."""
    y_true = np.array([1.0, 0.0] * 30)
    p_base = np.array([0.5] * 60)
    p_cand = np.array([0.6] * 60)
    lines = [0.0] * 60

    # None event IDs
    res1 = FixedCohortEvaluator.evaluate(y_true, p_cand, p_base, lines_cand=lines, lines_base=lines)
    assert res1["is_promotable"] is False
    assert any("event IDs missing" in r for r in res1["promotion_reasons"])

    # Empty list event IDs
    res2 = FixedCohortEvaluator.evaluate(
        y_true, p_cand, p_base,
        event_ids_cand=[], event_ids_base=[],
        lines_cand=lines, lines_base=lines
    )
    assert res2["is_promotable"] is False
    assert any("event IDs missing" in r for r in res2["promotion_reasons"])


def test_fixed_cohort_mismatched_fixtures_and_lines_fail():
    """Verify that mismatched event IDs or lines fail promotion (preventing line-selection fallacy)."""
    y_true = np.array([1.0, 0.0, 1.0, 0.0] * 15)  # n = 60
    p_base = np.array([0.5] * 60)
    p_cand = np.array([0.7, 0.3] * 30)

    ev_cand = [f"event_{i}" for i in range(60)]
    ev_base = [f"event_{i}" for i in range(1, 61)]  # Mismatched fixtures
    lines_same = [0.0] * 60

    res_ev = FixedCohortEvaluator.evaluate(
        y_true, p_cand, p_base,
        event_ids_cand=ev_cand, event_ids_base=ev_base,
        lines_cand=lines_same, lines_base=lines_same,
    )
    assert res_ev["is_promotable"] is False
    assert any("event IDs" in r for r in res_ev["promotion_reasons"])

    ev_same = [f"event_{i}" for i in range(60)]
    lines_cand = [-2.5] * 60
    lines_base = [-5.5] * 60  # Mismatched handicaps
    res_line = FixedCohortEvaluator.evaluate(
        y_true, p_cand, p_base,
        event_ids_cand=ev_same, event_ids_base=ev_same,
        lines_cand=lines_cand, lines_base=lines_base,
    )
    assert res_line["is_promotable"] is False
    assert any("lines" in r for r in res_line["promotion_reasons"])




def make_cohort(n=200, seed=3, skill=0.15):
    rng = np.random.default_rng(seed)
    p_true = np.clip(rng.normal(0.55, 0.15, n), 0.15, 0.85)
    y = (rng.random(n) < p_true).astype(float)
    p_base = np.clip(0.55 + 0.0 * p_true, 0, 1)
    p_cand = np.clip(0.55 + skill * (p_true - 0.55) / 0.15 * 0.5 + 0.0, 0.05, 0.95)
    return y, p_cand, p_base, [f"e{i}" for i in range(n)], [0.0] * n


def test_block_ids_are_mandatory_and_enough_blocks_are_required():
    y, pc, pb, ev, ln = make_cohort()
    missing = FixedCohortEvaluator.evaluate(y, pc, pb, event_ids_cand=ev, event_ids_base=ev, lines_cand=ln, lines_base=ln,
                                            require_calibration=False)
    assert missing["is_promotable"] is False and any("block ids" in r for r in missing["promotion_reasons"])
    wrong_len = FixedCohortEvaluator.evaluate(y, pc, pb, event_ids_cand=ev, event_ids_base=ev, lines_cand=ln, lines_base=ln,
                                              require_calibration=False, block_ids=["a"] * 3)
    assert wrong_len["is_promotable"] is False
    few = FixedCohortEvaluator.evaluate(y, pc, pb, event_ids_cand=ev, event_ids_base=ev, lines_cand=ln, lines_base=ln,
                                        require_calibration=False, block_ids=weeks(200, 50), n_resamples=100)
    assert few["is_promotable"] is False and any("blocks" in r for r in few["promotion_reasons"])


def test_a_point_improvement_driven_by_two_blocks_is_not_promoted():
    rng = np.random.default_rng(8)
    n = 60                                                    # ten blocks of six
    y = rng.integers(0, 2, n).astype(float)
    p_base = np.full(n, 0.5)
    p_cand = p_base.copy()
    p_cand[:12] = np.where(y[:12] == 1.0, 0.9, 0.1)           # skill shows up in two blocks only
    ids = [str(i) for i in range(n)]
    res = FixedCohortEvaluator.evaluate(y, p_cand, p_base, event_ids_cand=ids, event_ids_base=ids, lines_cand=[0.0] * n, lines_base=[0.0] * n,
                                        require_calibration=False, block_ids=weeks(n, 6), n_resamples=400)
    assert res["delta_brier"] < -0.010 and res["delta_log_loss"] < 0.0           # the old fixed -0.010 threshold would have passed
    assert res["is_promotable"] is False
    assert any("95% CI upper bound" in r or "depends on the resampling seed" in r for r in res["promotion_reasons"])


def test_calibration_slope_ci_must_contain_one():
    rng = np.random.default_rng(4)
    n = 600
    z = rng.normal(0, 1.0, n)
    y = (rng.random(n) < 1 / (1 + np.exp(-z))).astype(float)
    base = np.full(n, 0.5)
    ids = [str(i) for i in range(n)]
    good = FixedCohortEvaluator.evaluate(y, 1 / (1 + np.exp(-z)), base, event_ids_cand=ids, event_ids_base=ids, lines_cand=[0.0] * n, lines_base=[0.0] * n,
                                         block_ids=weeks(n, 12), n_resamples=300)
    over = FixedCohortEvaluator.evaluate(y, 1 / (1 + np.exp(-3.0 * z)), base, event_ids_cand=ids, event_ids_base=ids, lines_cand=[0.0] * n, lines_base=[0.0] * n,
                                         block_ids=weeks(n, 12), n_resamples=300)
    assert good["cal_slope_ci"][0] <= 1.0 <= good["cal_slope_ci"][1] and good["is_promotable"] is True
    assert over["cal_slope_beta"] < 0.6 and over["is_promotable"] is False
    assert any("slope" in r for r in over["promotion_reasons"])


def test_gate_decision_does_not_depend_on_the_seed():
    y, pc, pb, ev, ln = make_cohort(n=240, skill=0.25)
    kw = dict(event_ids_cand=ev, event_ids_base=ev, lines_cand=ln, lines_base=ln, require_calibration=False, block_ids=weeks(240, 8), n_resamples=400)
    outcomes = {FixedCohortEvaluator.evaluate(y, pc, pb, seeds=(s, s + 1, s + 2), **kw)["is_promotable"] for s in (1, 100, 5000)}
    assert len(outcomes) == 1
