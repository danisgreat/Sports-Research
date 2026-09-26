"""Tests for tools/evidence_status.py (added 2026-09-26)."""
import csv
import datetime as dt
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import evidence_status as es  # noqa: E402
import slate_universe as su  # noqa: E402

BASE_HEAD = ("| Decision | Card | Rank | Contract (as issued) | Family | Card p | Baseline p | "
             "Baseline population (leak-free) | Result |\n|---|---|---|---|---|---:|---:|---|---|\n")


def write(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


class EvidenceStatus(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def gate(self, rows, name):
        return next(r for r in rows if r["gate"] == name)

    def test_empty_repository_reports_accruing_and_freeze_in_force(self):
        rows = es.collect(self.repo, [])
        self.assertEqual(self.gate(rows, "C-BASELINE-SKILL")["status"], "ACCRUING")
        self.assertEqual(self.gate(rows, "C-EVENT-UNIVERSE")["status"], "NO UNIVERSE DECLARED YET")
        self.assertTrue(self.gate(rows, "C-RULE-FREEZE")["status"].startswith("IN FORCE"))
        self.assertIn("| `C-RULE-FREEZE` |", es.render(rows))

    def test_seed_rows_never_count_toward_the_checkpoint(self):
        seed = "".join(f"| S{i} | Q-{i % 40} | 1 | x | total | 0.6 | 0.5 | pop | W |\n" for i in range(150))
        write(self.repo / "SKILL_BASELINE_LEDGER.md", "## Seed rows\n\n" + BASE_HEAD + seed +
              "\n## Prospective rows\n\n" + BASE_HEAD + "| P1 | P-600 | 1 | x | total | 0.6 | 0.5 | pop | W |\n")
        g = self.gate(es.collect(self.repo, []), "C-BASELINE-SKILL")
        self.assertEqual(g["progress"], "1 decisions / 1 cards")
        self.assertFalse(g["done"])

    def test_checkpoints_lift_the_freeze(self):
        pro = "".join(f"| P{i} | P-{600 + i % 35} | 1 | x | total | {0.55 + (i % 5) / 100} | 0.5 | pop | "
                      f"{'W' if i % 2 else 'L'} |\n" for i in range(110))
        write(self.repo / "SKILL_BASELINE_LEDGER.md", "## Prospective rows\n\n" + BASE_HEAD + pro)
        ds = self.repo / "research" / "settled_rows_2026-09-25" / "settled_rows.csv"
        ds.parent.mkdir(parents=True)
        with ds.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["card", "p", "result"])
            w.writeheader()
            for c in range(517, 545):      # P-517 predates RM-1 and must not count
                w.writerow({"card": f"P-{c}", "p": "0.6", "result": "W"})
        rows = es.collect(self.repo, [])
        self.assertTrue(self.gate(rows, "C-BASELINE-SKILL")["done"])
        rm1 = self.gate(rows, "T-RM1-PROSPECTIVE")
        self.assertEqual(rm1["progress"].split()[0], "27")
        self.assertTrue(rm1["done"])
        self.assertTrue(self.gate(rows, "C-RULE-FREEZE")["status"].startswith("LIFTED"))

    def test_universe_coverage_and_tamper_detection(self):
        now = dt.datetime(2026, 9, 27, 12, 0, tzinfo=dt.timezone.utc)
        u = su.declare("2026-09-27", ["mlb"], now, None, None, str(HERE.parent / "tests_fixtures" / "universe"))
        path = self.repo / "universe" / "UNIVERSE_2026-09-27.json"
        su.write_new(path, u)
        log = self.repo / "log.md"
        write(log, "card for gamePk 900001\n")
        g = self.gate(es.collect(self.repo, [log]), "C-EVENT-UNIVERSE")
        self.assertIn("1 carded", g["progress"])
        self.assertIn("2 missing", g["status"])
        path.write_text(path.read_text(encoding="utf-8").replace("900003", "900009"), encoding="utf-8")
        g = self.gate(es.collect(self.repo, [log]), "C-EVENT-UNIVERSE")
        self.assertIn("EDITED AFTER DECLARATION", g["status"])

    def test_shadow_counts_only_settled_frozen_games(self):
        d = self.repo / "research" / "mlb_shadow"
        write(d / "shadow_log.csv", "row_id,game_pk\n1-8.5,1\n1-9.5,1\n2-8.5,2\n")
        write(d / "shadow_results.csv", "game_pk,home_runs,away_runs\n1,5,3\n99,1,0\n")
        g = self.gate(es.collect(self.repo, []), "C-MLB-SHADOW")
        self.assertEqual(g["progress"], "2 games frozen, 1 settled")

    def test_sport_shadow_counts_per_league(self):
        d = self.repo / "research" / "sport_shadow"
        write(d / "shadow_log.csv", "row_id,league\nepl:1:2.5:None,epl\nepl:2:2.5:None,epl\nnba:9:220.5:-3.5,nba\n")
        write(d / "shadow_results.csv", "row_id,home_score\nepl:1:2.5:None,2\n")
        g = self.gate(es.collect(self.repo, []), "C-SPORT-SHADOW")
        self.assertEqual(g["progress"], "epl 2 frozen/1 settled; nba 1 frozen/0 settled")
        self.assertFalse(g["done"])


if __name__ == "__main__":
    unittest.main()
