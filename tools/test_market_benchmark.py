"""Tests for tools/market_benchmark.py (C-MARKET-BENCHMARK, added 2026-09-26)."""
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import market_benchmark as mb  # noqa: E402

HEAD = ("| Decision | Card | Rank | Contract (as issued) | Family | Card p | Market p (no-vig close) | Method | "
        "Settled (UTC) | Entered (UTC) | Result |\n|---|---|---|---|---|---:|---:|---|---|---|---|\n")


def row(dec, card, fam, p, m, res, settled="2026-10-01T03:00:00Z", entered="2026-10-01T09:00:00Z", method="shin"):
    return f"| {dec} | {card} | 1 | x | {fam} | {p} | {m} | {method} | {settled} | {entered} | {res} |\n"


class DevigTests(unittest.TestCase):
    def test_each_method_sums_to_one_and_keeps_order(self):
        for method in mb.METHODS:
            p = mb.devig([1.80, 2.10], method)
            self.assertAlmostEqual(sum(p), 1.0, places=9)
            self.assertGreater(p[0], p[1])

    def test_fair_market_is_unchanged(self):
        for method in mb.METHODS:
            p = mb.devig([2.0, 2.0], method)
            self.assertAlmostEqual(p[0], 0.5, places=9)

    def test_power_and_shin_shade_longshots_more_than_multiplicative(self):
        odds = [1.25, 4.50]
        mult, powr, shin = (mb.devig(odds, m) for m in mb.METHODS)
        self.assertLess(powr[1], mult[1])
        self.assertLess(shin[1], mult[1])

    def test_three_way_market(self):
        p = mb.devig([2.40, 3.30, 3.10], "multiplicative")
        self.assertEqual(len(p), 3)
        self.assertAlmostEqual(sum(p), 1.0, places=9)

    def test_rejects_incomplete_or_invalid_markets(self):
        with self.assertRaises(ValueError):
            mb.devig([3.0, 3.0])  # implied sum 0.667: one side missing
        with self.assertRaises(ValueError):
            mb.devig([1.0, 5.0])
        with self.assertRaises(ValueError):
            mb.devig([2.0])

    def test_american_conversion(self):
        self.assertAlmostEqual(mb.american_to_decimal(-110), 1.9090909, places=6)
        self.assertAlmostEqual(mb.american_to_decimal(150), 2.5, places=9)
        with self.assertRaises(ValueError):
            mb.american_to_decimal(50)


class LedgerTests(unittest.TestCase):
    def test_entry_before_settlement_is_excluded(self):
        text = HEAD + row("D1", "P-600", "total", 0.6, 0.55, "W") + \
            row("D2", "P-600", "total", 0.6, 0.55, "W", entered="2026-10-01T02:00:00Z")
        ok, bad = mb.validate(mb.parse(text))
        self.assertEqual([r["decision"] for r in ok], ["D1"])
        self.assertIn("INVALID_ENTRY_ORDER", bad[0][1])

    def test_unknown_method_and_missing_timestamp_excluded(self):
        text = HEAD + row("D1", "P-600", "total", 0.6, 0.55, "W", method="eyeball") + \
            row("D2", "P-600", "total", 0.6, 0.55, "W", settled="")
        ok, bad = mb.validate(mb.parse(text))
        self.assertEqual(ok, [])
        self.assertEqual(sorted(b[1].split(" ")[0] for b in bad), ["MISSING_TIMESTAMP", "UNKNOWN_DEVIG_METHOD"])

    def test_paired_brier_and_cluster_interval(self):
        text = HEAD + "".join([
            row("A1", "P-601", "total", 0.70, 0.55, "W"),
            row("A2", "P-601", "handicap", 0.60, 0.50, "L"),
            row("B1", "P-602", "total", 0.55, 0.60, "W"),
            row("C1", "P-603", "moneyline", 0.65, 0.62, "P"),  # push excluded
            row("A1", "P-601", "total", 0.10, 0.90, "L"),      # duplicate decision counted once
        ])
        ok, _ = mb.validate(mb.parse(text))
        s = mb.summarise(ok, boot=500)
        self.assertEqual(s["n"], 3)
        self.assertEqual(s["cards"], 2)
        card = ((0.70 - 1) ** 2 + (0.60 - 0) ** 2 + (0.55 - 1) ** 2) / 3
        mkt = ((0.55 - 1) ** 2 + (0.50 - 0) ** 2 + (0.60 - 1) ** 2) / 3
        self.assertAlmostEqual(s["card_brier"], card)
        self.assertAlmostEqual(s["market_brier"], mkt)
        self.assertAlmostEqual(s["diff"], card - mkt)
        lo, hi = s["ci95"]
        self.assertLessEqual(lo, hi)
        self.assertIn("Scoring-only", mb.render(s, []))

    def test_empty_ledger_renders(self):
        self.assertIn("No scored decisions", mb.render(mb.summarise([]), []))

    def test_repository_ledger_parses(self):
        text = (HERE.parent / "MARKET_BENCHMARK_LEDGER.md").read_text(encoding="utf-8-sig")
        ok, bad = mb.validate(mb.parse(text))
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
