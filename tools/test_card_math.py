"""Tests for tools/card_math.py and tools/calibration_report.py (2026-09-25(d))."""
import math
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import calibration_report as cr  # noqa: E402
import card_math as cm  # noqa: E402


class Distributions(unittest.TestCase):
    def test_probabilities_sum_to_one_with_push(self):
        for d in (cm.Dist("normal", mean=8.4, sd=4.0), cm.Dist("negbin", mean=8.4, sd=4.0), cm.Dist("poisson", mean=2.75)):
            for line in (2.5, 3, 7.5, 8):
                total = cm.p_over(d, line) + cm.p_under(d, line) + cm.p_push(d, line)
                self.assertAlmostEqual(total, 1.0, places=6)

    def test_negbin_moments(self):
        d = cm.Dist("negbin", mean=8.95, sd=4.51)
        ks = list(d._support())
        mass = sum(d.pmf(k) for k in ks)
        mean = sum(k * d.pmf(k) for k in ks)
        var = sum((k - mean) ** 2 * d.pmf(k) for k in ks)
        self.assertAlmostEqual(mass, 1.0, places=6)
        self.assertAlmostEqual(mean, 8.95, places=3)
        self.assertAlmostEqual(math.sqrt(var), 4.51, places=2)

    def test_poisson_closed_form(self):
        lam = 2.75
        expected = 1 - math.exp(-lam) * (1 + lam + lam * lam / 2)
        self.assertAlmostEqual(cm.p_over(cm.Dist("poisson", mean=lam), 2.5), expected, places=9)

    def test_skellam_symmetry_and_mean(self):
        d = cm.Dist("skellam", mu=1.3, mu_opp=1.3)
        self.assertAlmostEqual(cm.p_over(d, 0.5), cm.p_under(d, -0.5), places=9)
        d2 = cm.Dist("skellam", mu=1.6, mu_opp=1.1)
        self.assertAlmostEqual(sum(k * d2.pmf(k) for k in d2._support()), 0.5, places=6)

    def test_continuous_normal_half_line(self):
        d = cm.Dist("normal", mean=0.0, sd=1.0, integer=False)
        self.assertAlmostEqual(cm.p_over(d, 0.5), 1 - cm._norm_cdf(0.5), places=12)

    def test_no_zero_removes_ties(self):
        d = cm.Dist("normal", mean=1.44, sd=13.63, no_zero=True)
        self.assertEqual(d.pmf(0), 0.0)
        side_minus, _ = cm.p_cover(d, -1.5)
        opp = cm.Dist("normal", mean=-1.44, sd=13.63, no_zero=True)
        opp_plus, _ = cm.p_cover(opp, 1.5)
        self.assertAlmostEqual(side_minus + opp_plus, 1.0, places=6)  # exact complements


class ReproducesIssuedCards(unittest.TestCase):
    """The issued P-509 card (Part 5 §"2026-09-24(g)") printed P(Under 184.5) 0.613 and P(36ers −1.5) 0.516
    from centre 179.75 / width 17.07 and margin +1.44 / 13.63. The closed forms land within simulation error."""

    def test_p509_total_and_handicap(self):
        tot = cm.Dist("normal", mean=179.75, sd=17.07)
        self.assertAlmostEqual(cm.p_under(tot, 184.5), 0.613, delta=0.01)
        mar = cm.Dist("normal", mean=1.44, sd=13.63, no_zero=True)
        self.assertAlmostEqual(cm.p_cover(mar, -1.5)[0], 0.516, delta=0.01)

    def test_p500_total(self):
        self.assertAlmostEqual(cm.p_over(cm.Dist("negbin", mean=8.40, sd=3.97), 7.5), 0.536, delta=0.015)


class JointAndLedger(unittest.TestCase):
    def test_joint_threshold_is_band_mass(self):
        d = cm.Dist("negbin", mean=8.4, sd=4.0)
        band = sum(d.pmf(k) for k in (8, 9, 10))
        self.assertAlmostEqual(cm.joint_threshold(d, ("Over", 7.5), ("Under", 10.5)), band, places=9)

    def test_departure_ledger(self):
        led = cm.departure_ledger(0.613, 0.530, [("pace", 0.6), ("lineup", 0.4)])
        self.assertAlmostEqual(led["logit_departure"], cm.logit(0.613) - cm.logit(0.530), places=12)
        self.assertEqual(led["flag"], "OK")
        led2 = cm.departure_ledger(0.70, 0.50, [("pace", 0.3)])
        self.assertEqual(led2["flag"], "UNEXPLAINED_DEPARTURE")
        self.assertEqual(cm.departure_ledger(0.51, 0.50, [])["flag"], "OK")   # negligible departure

    def test_cli_runs(self):
        self.assertEqual(cm.main(["total", "--dist", "poisson", "--mean", "2.75", "--line", "2.5"]), 0)
        self.assertEqual(cm.main(["departure", "--p", "0.6", "--baseline", "0.5", "--mech", "x:1"]), 0)


class CalibrationReport(unittest.TestCase):
    def test_murphy_identity_and_slope(self):
        rows = [{"card": f"C{i}", "p": p, "y": y, "family": "total", "sport": "s", "direction": "Over", "rank": "1"}
                for i, (p, y) in enumerate([(0.9, 1), (0.8, 1), (0.7, 0), (0.6, 1), (0.55, 0), (0.3, 0), (0.2, 0), (0.45, 1)])]
        m = cr.murphy(rows, bins=10)
        # with one row per bin the decomposition is exact
        self.assertAlmostEqual(m["reliability"] - m["resolution"] + m["uncertainty"], m["brier"], places=9)
        a, b, se = cr.logistic_calibration(rows)
        self.assertTrue(b > 0 and se > 0)

    def test_report_from_csv(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "rows.csv"
            lines = ["card,p,result,family,sport,direction,rank"]
            for i in range(30):
                lines.append(f"C{i % 10},{0.55 + (i % 5) * 0.08:.2f},{'W' if i % 3 else 'L'},total,soccer,Over,1")
            lines.append("C99,,W,total,soccer,Over,1")      # no p: ignored
            lines.append("C98,0.6,P,total,soccer,Over,1")   # push: ignored
            p.write_text("\n".join(lines), encoding="utf-8")
            rows = cr.load(p)
            self.assertEqual(len(rows), 30)
            text = cr.report(rows, min_n=5, boot=200)
            self.assertIn("Murphy decomposition", text)
            self.assertIn("| soccer |", text)


if __name__ == "__main__":
    unittest.main()
