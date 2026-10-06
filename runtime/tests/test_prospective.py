"""Unit tests for ProspectiveEvaluationHarness."""
import unittest
import numpy as np

from runtime.src.common.prospective import ProspectiveEvaluationHarness, UncertaintyInterval


class TestProspectiveHarness(unittest.TestCase):

    def setUp(self):
        np.random.seed(42)
        self.n = 60
        self.y = np.random.choice([0.0, 1.0], size=self.n, p=[0.5, 0.5])
        # Candidate is better than baseline
        self.p_cand = np.clip(self.y * 0.7 + 0.15 + np.random.normal(0, 0.05, size=self.n), 0.01, 0.99)
        self.p_base = np.full(self.n, 0.50)
        self.events = [f"E_{i}" for i in range(self.n)]
        self.lines = [0.0] * self.n

    def test_evaluate_cohort_full_report(self):
        report = ProspectiveEvaluationHarness.evaluate_cohort(
            y_true=self.y,
            p_cand=self.p_cand,
            p_base=self.p_base,
            event_ids=self.events,
            lines=self.lines,
            n_cohort_total=100,
            bootstrap_resamples=200,
            require_calibration=False,
        )

        self.assertEqual(report.n_samples, 60)
        self.assertEqual(report.n_cohort_total, 100)
        self.assertAlmostEqual(report.coverage_rate, 0.60, places=4)
        self.assertAlmostEqual(report.lines_coverage_rate, 1.0, places=4)

        # Delta metrics should have valid estimates and bootstrap intervals
        self.assertLess(report.delta_brier.estimate, -0.010)
        self.assertTrue(np.isfinite(report.delta_brier.std_error))
        self.assertTrue(report.delta_brier.ci_lower_95 <= report.delta_brier.ci_upper_95)

        self.assertTrue(np.isfinite(report.delta_log_loss.std_error))
        self.assertTrue(np.isfinite(report.delta_hit_rate.std_error))

    def test_insufficient_samples_fails_gracefully(self):
        report = ProspectiveEvaluationHarness.evaluate_cohort(
            y_true=self.y[:20],
            p_cand=self.p_cand[:20],
            p_base=self.p_base[:20],
            event_ids=self.events[:20],
            lines=self.lines[:20],
            n_cohort_total=50,
            min_sample_size=50,
        )
        self.assertFalse(report.is_promotable)
        self.assertTrue(any("below minimum requirement" in r for r in report.promotion_reasons))

    def test_to_dict_serializable(self):
        report = ProspectiveEvaluationHarness.evaluate_cohort(
            y_true=self.y,
            p_cand=self.p_cand,
            p_base=self.p_base,
            event_ids=self.events,
            lines=self.lines,
            require_calibration=False,
            bootstrap_resamples=50,
        )
        d = report.to_dict()
        self.assertIn("coverage_rate", d)
        self.assertIn("delta_brier", d)
        self.assertIn("ci_lower_95", d["delta_brier"])


if __name__ == "__main__":
    unittest.main()
