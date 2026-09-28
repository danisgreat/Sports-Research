"""Regressions for strict calibration admission and same-event baseline pairing."""
import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import calibration_report as cr  # noqa: E402
import rank_model as rm  # noqa: E402
from test_semantic_validation import record  # noqa: E402


CSV_FIELDS = [
    "card", "rank", "contract", "family", "sport", "direction", "event_id",
    "event_cluster_id", "forecast_id", "decision_id", "target_id", "p", "baseline_p",
    "preferred_at_issue", "baseline_match_valid", "result", "outcome_verified",
    "horizon", "input_cutoff_utc", "performance_eligible",
]


def csv_row(**overrides):
    row = {
        "card": "P-600", "rank": "1", "contract": "Over 8.0", "family": "total",
        "sport": "mlb", "direction": "over", "event_id": "official-100",
        "event_cluster_id": "event-100", "forecast_id": "forecast-100-pre",
        "decision_id": "P-600-D1", "target_id": "P-600-T1", "p": "0.45",
        "baseline_p": "0.5", "preferred_at_issue": "true", "baseline_match_valid": "true",
        "result": "W", "outcome_verified": "true", "horizon": "PREGAME",
        "input_cutoff_utc": "2026-09-25T10:00:00Z", "performance_eligible": "true",
    }
    row.update(overrides)
    return row


class CalibrationAdmission(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.csv_path = self.root / "rows.csv"
        self.records_path = self.root / "prospective_records.json"

    def tearDown(self):
        self.tmp.cleanup()

    def write_data(self, rows, records):
        with self.csv_path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        self.records_path.write_text(json.dumps({"schema_version": 1, "records": records}), encoding="utf-8")

    def test_forged_csv_eligibility_flags_do_not_admit_row(self):
        self.write_data([csv_row()], [])
        self.assertEqual(cr.load(self.csv_path, eligible_only=True, records_path=self.records_path), [])

    def test_exact_verified_binary_record_join_is_admitted(self):
        frozen = record(probabilities={"W": 0.45, "P": 0.0, "L": 0.55})
        frozen["q"] = rm.score_row(rm.load_coef(), "mlb", frozen["contract"], 0.45)["q"]
        self.write_data([csv_row()], [frozen])
        rows = cr.load(self.csv_path, eligible_only=True, records_path=self.records_path)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["event_cluster_id"], "event-100")
        self.assertEqual(rows[0]["baseline_contract_id"], frozen["contract_id"])

    def test_changed_csv_probability_or_result_is_excluded(self):
        frozen = record(probabilities={"W": 0.45, "P": 0.0, "L": 0.55})
        frozen["q"] = rm.score_row(rm.load_coef(), "mlb", frozen["contract"], 0.45)["q"]
        self.write_data([csv_row(p="0.46"), csv_row(decision_id="P-600-D1", result="L")], [frozen])
        self.assertEqual(cr.load(self.csv_path, eligible_only=True, records_path=self.records_path), [])

    def test_paired_baseline_uses_event_cluster_identity(self):
        row = {
            "baseline_match_valid": True, "baseline_probability": 0.5, "event_id": "event-a",
            "event_cluster_id": "cluster-a", "target_id": "target-a", "contract_id": "contract-a",
            "horizon": "PREGAME", "input_cutoff_utc": "2026-09-25T10:00:00Z",
            "baseline_event_id": "event-a", "baseline_target_id": "target-a",
            "baseline_contract_id": "contract-a", "baseline_horizon": "PREGAME",
            "baseline_input_cutoff_utc": "2026-09-25T10:00:00Z",
            "p": 0.6, "y": 1,
        }
        summary = cr.paired_baseline_summary([row], boot=20)
        self.assertEqual(summary["events"], 1)
        self.assertEqual(summary["n"], 1)


if __name__ == "__main__":
    unittest.main()
