"""Tests for tools/evidence_status.py (added 2026-09-26)."""
import csv
import datetime as dt
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import evidence_status as es  # noqa: E402
import slate_universe as su  # noqa: E402
import rank_model as rm  # noqa: E402

COEF_SHA = hashlib.sha256((HERE / "rank_model_coefficients.json").read_bytes()).hexdigest()
CODE_SHA = hashlib.sha256((HERE / "rank_model.py").read_bytes()).hexdigest()

BASE_HEAD = ("| Decision | Card | Rank | Contract (as issued) | Family | Card p | Baseline p | "
             "Baseline population (leak-free) | Result | Performance Eligible | Eligibility Receipt |\n"
             "|---|---|---|---|---|---:|---:|---|---|---|---|\n")


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
        seed = "".join(f"| S{i} | Q-{i % 40} | 1 | x | total | 0.6 | 0.5 | pop | W | no | seed |\n" for i in range(150))
        write(self.repo / "SKILL_BASELINE_LEDGER.md", "## Seed rows\n\n" + BASE_HEAD + seed +
              "\n## Prospective rows\n\n" + BASE_HEAD + "| P1 | P-600 | 1 | x | total | 0.6 | 0.5 | pop | W | eligible | receipt-1 |\n")
        g = self.gate(es.collect(self.repo, []), "C-BASELINE-SKILL")
        self.assertEqual(g["progress"], "0 verified eligible decisions / 0 cards; 1 unqualified row(s) excluded")
        self.assertFalse(g["done"])

    def test_checkpoints_lift_the_freeze(self):
        records = []
        lines = []
        for i in range(110):
            card_num = 518 + i % 35
            card = f"P-{card_num}"
            decision = f"{card}-D{i // 35 + 1}"
            target = f"{card}-T{i}"
            contract_id = f"{card}-C{i}"
            event = f"event-{card_num}"
            p = round(0.55 + (i % 5) / 100, 2)
            result = "W" if i % 2 else "L"
            contract = f"Contract {i}"
            lines.append(f"| {decision} | {card} | 1 | {contract} | total | {p:.2f} | 0.5 | pop | {result} | eligible | prospective_records.json#{decision} |\n")
            records.append({
                "schema_version": 1, "event_id": event, "event_cluster_id": event,
                "forecast_id": f"forecast-{card_num}", "card_id": card, "decision_id": decision,
                "target_id": target, "contract_id": contract_id, "contract": contract,
                "contract_spec": {"measure": "runs", "period": "full_game", "line": 8.5, "side": "OVER", "units": "runs",
                                   "overtime_rule": "included", "draw_rule": "not_applicable", "push_rule": "half_line_no_push",
                                   "void_rule": "official_void", "action_rule": "official_action", "contract_version": "v1"},
                "sport": "mlb", "competition": "MLB", "season": "2026", "participant_ids": ["team-home", "team-away"], "rank": 1,
                "horizon": "PREGAME", "input_cutoff_utc": "2026-09-25T10:00:00Z",
                "input_availability_latest_utc": "2026-09-25T09:59:00Z", "issued_at_utc": "2026-09-25T10:10:00Z",
                "event_start_utc": "2026-09-25T11:00:00Z", "probabilities": {"W": p, "P": 0.0, "L": round(1 - p, 2)},
                "distribution_id": f"dist-{decision}", "distribution_type": "MANUAL_JOINT_SCORE_GRID", "distribution_sha256": "d" * 64,
                "q": rm.score_row(rm.load_coef(), "mlb", contract, p)["q"],
                "q_semantics": "ROW_CALIBRATED_NOT_JOINT", "baseline": {
                    "p": 0.5, "status": "FROZEN_VALID", "event_id": event, "target_id": target,
                    "contract_id": contract_id, "horizon": "PREGAME", "input_cutoff_utc": "2026-09-25T10:00:00Z",
                    "training_cutoff_utc": "2026-09-24T23:00:00Z", "version": "baseline-v1"},
                "method_version": "MDS-test", "method_sha256": "a" * 64, "control_sha256": "b" * 64,
                "manifest_sha256": "c" * 64, "ranking_model_version": "RM-1", "ranking_model_sha256": COEF_SHA,
                "ranking_model_code_sha256": CODE_SHA, "selection_policy_version": "preferred-v1",
                "complementary_pair_id": None, "covering_pair_id": None, "target_weight": 1.0,
                "settlement_revision_id": f"{card}-S{i}", "observed_value": 9, "result": result,
                "outcome_verified": True, "preferred_at_issue": True, "missingness": [],
                "issue_receipts": [
                    {"event_id": event, "lineage_id": lineage, "observed_at_utc": "2026-09-25T09:50:00Z", "sha256": digit * 64,
                     "source_ref": f"https://{lineage}.example/{event}",
                     "fields": {"event_id": event, "event_state": "PREGAME", "event_start_utc": "2026-09-25T11:00:00Z"}}
                    for lineage, digit in (("league", "1"), ("broadcaster", "2"), ("data", "3"))],
                "terminal_receipts": [
                    {"event_id": event, "terminal": True, "lineage_id": lineage, "sha256": digit * 64,
                     "source_ref": f"https://{lineage}.example/{event}/final", "observed_at_utc": "2026-09-25T12:00:00Z",
                     "fields": {"event_id": event, "result": result, "terminal_status": "FINAL"}}
                    for lineage, digit in (("league", "4"), ("broadcaster", "5"), ("data", "6"))],
            })
        pro = "".join(lines)
        write(self.repo / "SKILL_BASELINE_LEDGER.md", "## Prospective rows\n\n" + BASE_HEAD + pro)
        ds = self.repo / "research" / "settled_rows_2026-09-28" / "prospective_records.json"
        ds.parent.mkdir(parents=True)
        ds.write_text(__import__("json").dumps({"schema_version": 1, "records": records}), encoding="utf-8")
        rows = es.collect(self.repo, [])
        self.assertTrue(self.gate(rows, "C-BASELINE-SKILL")["done"])
        rm1 = self.gate(rows, "T-RM1-PROSPECTIVE")
        self.assertEqual(rm1["progress"].split()[0], "35")
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
