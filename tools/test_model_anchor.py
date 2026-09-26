"""Offline tests for tools/model_anchor.py (C-MODEL-ANCHOR, 2026-09-26(e))."""
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import model_anchor as ma  # noqa: E402


class TestSelectionRule(unittest.TestCase):
    def test_rule_cases(self):
        self.assertEqual(ma.select({"A1": [-0.02, -0.01], "TB1": None, "A1vTB1": None}), "A1")
        self.assertEqual(ma.select({"A1": [-0.02, 0.001], "TB1": [-0.02, -0.01], "A1vTB1": None}), "TB1")
        # both qualify: A1 only if it beat TB-1 with its interval below 0
        self.assertEqual(ma.select({"A1": [-0.03, -0.01], "TB1": [-0.02, -0.01], "A1vTB1": [-0.01, -0.001]}), "A1")
        self.assertEqual(ma.select({"A1": [-0.03, -0.01], "TB1": [-0.02, -0.01], "A1vTB1": [-0.01, 0.002]}), "TB1")
        self.assertEqual(ma.select({"A1": [-0.01, 0.01], "TB1": [0.001, 0.01], "A1vTB1": None}), "POP")
        self.assertEqual(ma.select({"A1S": [-0.006, -0.0002], "A1": None, "TB1": None}), "A1S")

    def test_interval_touching_zero_does_not_qualify(self):
        self.assertFalse(ma.below0([-0.02, 0.0]))
        self.assertTrue(ma.below0([-0.02, -1e-6]))
        self.assertFalse(ma.below0(None))


class TestRegistry(unittest.TestCase):
    def test_registry_is_derived(self):
        reg = ma.registry()
        for lg, targets in ma.EVIDENCE.items():
            for t, ev in targets.items():
                self.assertEqual(reg[lg][t]["anchor"], ma.select(ev), (lg, t))

    def test_known_rows(self):
        reg = ma.registry()
        self.assertEqual(reg["nba"]["side"]["anchor"], "A1")
        self.assertEqual(reg["nba"]["total"]["anchor"], "A1")
        self.assertEqual(reg["nhl"]["total"]["anchor"], "POP")     # A1 totals worse than the population
        self.assertEqual(reg["nfl"]["side"]["anchor"], "TB1")      # A1 not separated from TB-1
        self.assertEqual(reg["nrl"]["side"]["anchor"], "POP")      # neither model beat the population
        self.assertEqual(reg["mlb"]["side"]["anchor"], "TB1")
        for lg in ma.COVERED_NO_EVIDENCE:
            self.assertEqual(reg[lg]["side"]["anchor"], "POP")

    def test_every_interval_is_ordered(self):
        for lg, targets in ma.EVIDENCE.items():
            for t, ev in targets.items():
                for k, ci in ev.items():
                    if ci is not None:
                        self.assertLessEqual(ci[0], ci[1], (lg, t, k))

    def test_status_is_reference_until_user_instruction(self):
        # C-RULE-FREEZE: the registry may not be a card input until the user explicitly instructs it.
        self.assertIn(ma.STATUS, ("REFERENCE", "ACTIVE"))
        rules = (Path(__file__).resolve().parent.parent / "RULES_GENERAL.md").read_text(encoding="utf-8-sig")
        if ma.STATUS == "ACTIVE":
            self.assertIn("C-MODEL-ANCHOR", rules)
            self.assertRegex(rules, r"C-MODEL-ANCHOR[^\n]*ACTIVATED")

    def test_registry_cli(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.assertEqual(ma.main(["registry"]), 0)
        self.assertIn("| nba | A1 | A1 |", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
