"""Fail-closed joins from the baseline ledger to structured prospective evidence."""
import json
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prospective_eligibility as pe  # noqa: E402
import rank_model as rm  # noqa: E402

COEF_SHA = hashlib.sha256((Path(__file__).resolve().parent / "rank_model_coefficients.json").read_bytes()).hexdigest()
CODE_SHA = hashlib.sha256((Path(__file__).resolve().parent / "rank_model.py").read_bytes()).hexdigest()


def record():
    event = "official-event-1"
    decision = "P-600-D1"
    target = "P-600-T1"
    contract_id = "P-600-C1"
    return {
        "schema_version": 1, "event_id": event, "event_cluster_id": event,
        "forecast_id": "forecast-600", "card_id": "P-600", "decision_id": decision,
        "target_id": target, "contract_id": contract_id, "contract": "Home ML",
        "contract_spec": {"measure": "winner", "period": "full_game", "line": None, "side": "HOME", "units": "team",
                           "overtime_rule": "included", "draw_rule": "official_draw", "push_rule": "not_applicable",
                           "void_rule": "official_void", "action_rule": "official_action", "contract_version": "v1"},
        "sport": "mlb", "competition": "MLB", "season": "2026", "participant_ids": ["team-home", "team-away"], "rank": 1,
        "horizon": "PREGAME", "input_cutoff_utc": "2026-09-25T10:00:00Z",
        "input_availability_latest_utc": "2026-09-25T09:59:00Z", "issued_at_utc": "2026-09-25T10:10:00Z",
        "event_start_utc": "2026-09-25T11:00:00Z", "probabilities": {"W": 0.6, "P": 0.0, "L": 0.4},
        "distribution_id": "dist-600", "distribution_type": "MANUAL_JOINT_SCORE_GRID", "distribution_sha256": "d" * 64,
        "q": rm.score_row(rm.load_coef(), "mlb", "Home ML", 0.6)["q"],
        "q_semantics": "ROW_CALIBRATED_NOT_JOINT", "baseline": {
            "p": 0.5, "status": "FROZEN_VALID", "event_id": event, "target_id": target,
            "contract_id": contract_id, "horizon": "PREGAME", "input_cutoff_utc": "2026-09-25T10:00:00Z",
            "training_cutoff_utc": "2026-09-24T23:00:00Z", "version": "baseline-v1"},
        "method_version": "MDS-test", "method_sha256": "a" * 64, "control_sha256": "b" * 64,
        "manifest_sha256": "c" * 64, "ranking_model_version": "RM-1", "ranking_model_sha256": COEF_SHA,
        "ranking_model_code_sha256": CODE_SHA, "selection_policy_version": "preferred-v1",
        "complementary_pair_id": None, "covering_pair_id": None, "target_weight": 1.0,
        "settlement_revision_id": "P-600-S1", "observed_value": 1, "result": "W",
        "outcome_verified": True, "preferred_at_issue": True, "missingness": [],
        "issue_receipts": [
            {"event_id": event, "lineage_id": lineage, "observed_at_utc": "2026-09-25T09:50:00Z",
             "sha256": digit * 64, "source_ref": f"https://{lineage}.example/{event}",
             "fields": {"event_id": event, "event_state": "PREGAME", "event_start_utc": "2026-09-25T11:00:00Z"}}
            for lineage, digit in (("league", "1"), ("broadcaster", "2"), ("data", "3"))],
        "terminal_receipts": [
            {"event_id": event, "terminal": True, "lineage_id": lineage, "sha256": digit * 64,
             "source_ref": f"https://{lineage}.example/{event}/final", "observed_at_utc": "2026-09-25T12:00:00Z",
             "fields": {"event_id": event, "result": "W", "terminal_status": "FINAL"}}
            for lineage, digit in (("league", "4"), ("broadcaster", "5"), ("data", "6"))],
    }


def ledger_row(**changes):
    row = {"section": "prospective", "decision": "P-600-D1", "card": "P-600", "contract": "Home ML",
           "rank": 1, "p": 0.6, "b": 0.5, "result": "W", "eligible": True,
           "eligibility_receipt": "prospective_records.json#P-600-D1"}
    row.update(changes)
    return row


class ProspectiveEligibility(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "prospective_records.json"

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, *records):
        self.path.write_text(json.dumps({"schema_version": 1, "records": list(records)}), encoding="utf-8")

    def test_exact_verified_join_passes(self):
        self.write(record())
        accepted, failures = pe.join_binary_baseline_rows([ledger_row()], self.path)
        self.assertEqual(len(accepted), 1)
        self.assertEqual(failures, {})

    def test_markdown_eligibility_label_without_structured_receipt_does_not_pass(self):
        accepted, failures = pe.join_binary_baseline_rows([ledger_row()], self.path)
        self.assertEqual(accepted, [])
        self.assertIn("VERIFIED_STRUCTURED_RECORD_MISSING", failures["P-600-D1"])

    def test_every_scored_value_must_match_the_verified_record(self):
        self.write(record())
        accepted, failures = pe.join_binary_baseline_rows([ledger_row(p=0.65)], self.path)
        self.assertEqual(accepted, [])
        self.assertIn("LEDGER_CARD_PROBABILITY_MISMATCH", failures["P-600-D1"])

    def test_push_mass_is_not_discarded_by_binary_ledger(self):
        item = record()
        item["probabilities"] = {"W": 0.6, "P": 0.1, "L": 0.3}
        self.write(item)
        accepted, failures = pe.join_binary_baseline_rows([ledger_row()], self.path)
        self.assertEqual(accepted, [])
        self.assertIn("PUSH_OR_VOID_VECTOR_REQUIRES_VECTOR_AWARE_LEDGER", failures["P-600-D1"])

    def test_duplicate_structured_decision_is_blocked(self):
        item = record()
        duplicate = dict(item, settlement_revision_id="P-600-S2")
        self.write(item, duplicate)
        accepted, failures = pe.join_binary_baseline_rows([ledger_row()], self.path)
        self.assertEqual(accepted, [])
        self.assertIn("DUPLICATE_DECISION_ID", failures["P-600-D1"])

    def test_rm1_q_must_reproduce_from_the_hashed_build(self):
        item = record()
        self.assertEqual(pe.rm1_blockers(item), [])
        item["q"] = 0.9
        self.assertIn("RM1_Q_DOES_NOT_REPRODUCE_FROM_FROZEN_BUILD", pe.rm1_blockers(item))

    def test_rm1_prospective_row_with_push_is_blocked_until_conditioning_is_validated(self):
        item = record()
        item["probabilities"] = {"W": 0.55, "P": 0.1, "L": 0.35}
        self.assertIn("RM1_PUSH_CONDITIONING_UNVALIDATED", pe.rm1_blockers(item))


if __name__ == "__main__":
    unittest.main()
