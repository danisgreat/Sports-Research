"""Tests for tools/skill_baseline.py (C-BASELINE-SKILL, 2026-09-25(c))."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skill_baseline as sb  # noqa: E402

TABLE = """Intro text.

| Decision | Card | Rank | Contract (as issued) | Family | Card p | Baseline p | Baseline population (leak-free) | Result |
|---|---|---|---|---|---:|---:|---|---|
| A-TOT | A | 1 | Under 7.5 | total | 0.700 | 0.500 | pop | W |
| A-TOT | A | 4 | Over 7.5 (complement, duplicate id) | total | 0.300 | 0.500 | pop | L |
| A-ML | A | 2 | Home ML | moneyline | 0.600 | 0.530 | pop | L |
| B-TOT | B | 1 | Over 8.0 | total | 0.550 | 0.480 | pop | P |
| B-HCP | B | 2 | Away +1.5 | handicap | 0.650 | 0.640 | pop | W |

Trailing paragraph.
"""


class SkillBaseline(unittest.TestCase):
    def test_parse_and_dedupe_and_push_exclusion(self):
        rows = sb.parse(TABLE)
        self.assertEqual(len(rows), 5)
        s = sb.summarise(rows, boot=200)
        self.assertEqual(s["n"], 3)  # duplicate decision id and the push are excluded
        self.assertEqual(s["cards"], 2)

    def test_brier_arithmetic(self):
        s = sb.summarise(sb.parse(TABLE), boot=200)
        card = ((0.7 - 1) ** 2 + (0.6 - 0) ** 2 + (0.65 - 1) ** 2) / 3
        base = ((0.5 - 1) ** 2 + (0.53 - 0) ** 2 + (0.64 - 1) ** 2) / 3
        self.assertAlmostEqual(s["card_brier"], card, places=9)
        self.assertAlmostEqual(s["baseline_brier"], base, places=9)
        self.assertAlmostEqual(s["diff"], card - base, places=9)
        self.assertEqual(s["by_family"]["total"]["n"], 1)

    def test_bootstrap_is_deterministic_and_ordered(self):
        a = sb.summarise(sb.parse(TABLE), boot=500, seed=1)
        b = sb.summarise(sb.parse(TABLE), boot=500, seed=1)
        self.assertEqual(a["ci95"], b["ci95"])
        self.assertLessEqual(a["ci95"][0], a["ci95"][1])

    def test_render_verdicts(self):
        s = sb.summarise(sb.parse(TABLE), boot=200)
        self.assertIn("Scored decisions: 3", sb.render(s))
        self.assertEqual(sb.render({"n": 0}), "No scored decisions with a baseline yet.")

    def test_repository_ledger_parses(self):
        ledger = Path(__file__).resolve().parent.parent / "SKILL_BASELINE_LEDGER.md"
        if ledger.exists():
            rows = sb.parse(ledger.read_text(encoding="utf-8-sig"))
            self.assertGreater(len(rows), 0)
            for r in rows:
                self.assertTrue(0.0 <= r["p"] <= 1.0 and 0.0 <= r["b"] <= 1.0, r)
                self.assertIn(r["result"], ("W", "L", "P"))


if __name__ == "__main__":
    unittest.main()
