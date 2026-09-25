"""Tests for tools/rank_model.py (RM-1, 2026-09-25(e))."""
import importlib.util
import io
import math
import random
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rank_model as rm  # noqa: E402

REPO = HERE.parent
EXTRACTOR = REPO / "research" / "settled_rows_2026-09-25" / "extract_settled_rows.py"


class TestClassification(unittest.TestCase):
    def test_family_rules_match_extractor(self):
        spec = importlib.util.spec_from_file_location("extract_settled_rows", EXTRACTOR)
        ex = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(ex)
        samples = ["Over 8.5 runs", "1st Half Under 1.5", "Hawks +1.5", "Bullets -1.5", "Pirates ML",
                   "Combined corners Over 8.5", "Racing team total Over 0.5", "Brøndby or Draw X2, 90 min",
                   "Gauff -4.5 games", "Aryan Jit Singh — Match Winner", "First 5 innings Under 4.5",
                   "Player strikeouts Over 6.5", "Total games Over 21.5", "Club Brugge +0.5 / double chance 1X"]
        for s in samples:
            self.assertEqual(rm.classify_family(s), ex.classify_family(s), s)
            self.assertEqual(rm.direction(s), ex.direction(s), s)

    def test_market_classes(self):
        cases = [("mlb", "Cardinals +1.5", "hcp_plus_low"), ("nbl", "Hawks +1.5", "hcp_plus_nb"),
                 ("nfl", "Broncos +2.5", "hcp_plus_nb"), ("epl", "Everton +1.5", "hcp_plus_soccer"),
                 ("soccer", "Sydney +0.5 / 1X", "dc"), ("nba", "Celtics -4.5", "hcp_minus"),
                 ("mlb", "Over 6.5 Runs", "total_over"), ("soccer", "1st Half Under 1.5", "phase_under"),
                 ("kbo", "Dinos ML", "ml"), ("soccer", "Monterrey or Draw 1X", "dc")]
        for sport, contract, want in cases:
            g = rm.sport_group(sport)
            got = rm.market_class(g, rm.classify_family(contract), rm.direction(contract), contract)
            self.assertEqual(got, want, contract)

    def test_sport_groups(self):
        self.assertEqual(rm.sport_group("baseball-MLB"), "mlb")
        self.assertEqual(rm.sport_group("baseball-NPB/KBO/CPBL"), "asia_bb")
        self.assertEqual(rm.sport_group("american-football"), "oval")
        self.assertEqual(rm.sport_group("AFL"), "oval")
        self.assertEqual(rm.sport_group("ice-hockey"), "hockey")
        with self.assertRaises(ValueError):
            rm.sport_group("curling")


class TestCalibration(unittest.TestCase):
    coef = {"weights": {"intercept": -0.2, "logit_p": 1.5, "cushion_nb": -1.2}, "terms": ["cushion_nb"], "lam": 0.0}

    def test_complements_sum_to_one(self):
        for g, cls in (("nbl", "hcp_plus_nb"), ("mlb", "total_over"), ("soccer", "phase_under"), ("nfl", "hcp_minus")):
            grp = rm.sport_group(g)
            for p in (0.51, 0.58, 0.66, 0.8):
                a = rm.calibrate(self.coef, grp, cls, p)
                b = rm.calibrate(self.coef, grp, rm.complement_class(cls, grp), 1 - p)
                self.assertAlmostEqual(a + b, 1.0, places=9, msg=(g, cls, p))

    def test_exact_tie(self):
        self.assertEqual(rm.calibrate(self.coef, "mlb", "total_over", 0.5), 0.5)

    def test_cushion_flip(self):
        row = rm.score_row(self.coef, "nbl", "Hawks +1.5", 0.60)
        self.assertLess(row["q"], 0.45)
        self.assertIn("SIDE_FLIP", row["flags"])
        self.assertIn("CUSHION_NB", row["flags"])
        fav = rm.score_row(self.coef, "nbl", "Bullets -1.5", 0.40)
        self.assertGreater(fav["q"], 0.55)
        self.assertNotEqual(fav["tier"], "STRONG")   # a flipped side is capped at SUPPORTED

    def test_baseball_cushion_not_penalised(self):
        row = rm.score_row(self.coef, "mlb", "Cardinals +1.5", 0.62)
        self.assertGreater(row["q"], 0.55)
        self.assertNotIn("SIDE_FLIP", row["flags"])

    def test_near_tied_flip_keeps_stated_side(self):
        ranked = rm.rank_rows(self.coef, "nrl", [("Under 45.5", 0.635), ("Dolphins -2.5", 0.514),
                                                 ("Roosters +2.5", 0.486), ("Over 45.5", 0.365)])
        order = [r["contract"] for r in ranked]
        self.assertLess(order.index("Dolphins -2.5"), order.index("Roosters +2.5"))
        self.assertTrue(any("NEAR_TIED_FLIP" in r["flags"] for r in ranked))

    def test_clipped(self):
        self.assertLessEqual(rm.calibrate(self.coef, "soccer", "phase_under", 0.999), rm.Q_MAX)

    def test_rank_order_and_statement(self):
        ranked = rm.rank_rows(self.coef, "nbl", [("Under 188.5", 0.646), ("Hawks +1.5", 0.54),
                                                 ("Bullets -1.5", 0.46), ("Over 188.5", 0.354)])
        self.assertEqual([r["rm1_rank"] for r in ranked], [1, 2, 3, 4])
        self.assertEqual(ranked[0]["contract"], "Bullets -1.5")
        self.assertIn("TOP2_QUALITY", rm.top_two_statement(ranked))


class TestFit(unittest.TestCase):
    def test_recovers_synthetic_coefficients(self):
        rng = random.Random(3)
        rows = []
        for i in range(3000):
            p = rng.uniform(0.5, 0.9)
            cush = rng.random() < 0.2
            eta = -0.1 + 1.4 * math.log(p / (1 - p)) + (-1.0 if cush else 0.0)
            y = 1 if rng.random() < 1 / (1 + math.exp(-eta)) else 0
            rows.append({"card": f"C{i}", "group": "basketball", "cls": "hcp_plus_nb" if cush else "total_over",
                         "p": p, "y": y})
        w = rm.fit(rows)["weights"]
        self.assertAlmostEqual(w["logit_p"], 1.4, delta=0.35)
        self.assertAlmostEqual(w["cushion_nb"], -1.0, delta=0.35)

    def test_challenger_terms_fit(self):
        rows = [{"card": f"C{i}", "group": g, "cls": c, "p": 0.6 + 0.01 * (i % 20), "y": i % 3 != 0}
                for i, (g, c) in enumerate([("soccer", "phase_over"), ("mlb", "total_under")] * 60)]
        c = rm.fit(rows, lam=8.0, terms=rm.TERMS)
        self.assertEqual(len(c["weights"]), len(rm.feature_names(rm.TERMS)))


class TestShippedCoefficients(unittest.TestCase):
    def test_file_loads_and_cli_runs(self):
        coef = rm.load_coef()
        self.assertEqual(coef["model"], "RM-1")
        self.assertEqual(coef["terms"], ["cushion_nb"])
        self.assertLess(coef["weights"]["cushion_nb"], 0)
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = rm.main(["rank", "--sport", "mlb", "--row", "Cardinals +1.5=0.602", "--row", "Over 6.5 Runs=0.596"])
        self.assertEqual(rc, 0)
        self.assertIn("TOP2_QUALITY", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
