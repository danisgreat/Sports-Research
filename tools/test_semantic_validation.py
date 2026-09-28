"""Semantic regressions for scoring, event geometry, ranking and prospective gates."""
import sys
import hashlib
import json
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import semantic_validation as sv  # noqa: E402

COEF_SHA = hashlib.sha256((Path(__file__).resolve().parent / "rank_model_coefficients.json").read_bytes()).hexdigest()
CODE_SHA = hashlib.sha256((Path(__file__).resolve().parent / "rank_model.py").read_bytes()).hexdigest()
import rank_model as rm  # noqa: E402


def record(**overrides):
    row = {
        "schema_version": 1, "event_id": "official-100", "event_cluster_id": "event-100",
        "forecast_id": "forecast-100-pre", "card_id": "P-600", "decision_id": "P-600-D1",
        "target_id": "P-600-T1", "contract_id": "P-600-C1", "contract": "Over 8.0",
        "contract_spec": {"measure": "runs", "period": "full_game", "line": 8.0, "side": "OVER", "units": "runs",
                           "overtime_rule": "included", "draw_rule": "not_applicable", "push_rule": "at_8_push",
                           "void_rule": "official_void", "action_rule": "official_action", "contract_version": "v1"},
        "sport": "mlb", "competition": "MLB", "season": "2026", "participant_ids": ["team-home", "team-away"], "rank": 1,
        "horizon": "PREGAME", "input_cutoff_utc": "2026-09-25T10:00:00Z",
        "input_availability_latest_utc": "2026-09-25T09:59:00Z", "preferred_at_issue": True,
        "issued_at_utc": "2026-09-25T10:10:00Z", "event_start_utc": "2026-09-25T11:00:00Z",
        "distribution_id": "dist-100", "distribution_type": "MANUAL_JOINT_SCORE_GRID", "distribution_sha256": "d" * 64,
        "probabilities": {"W": 0.45, "P": 0.13, "L": 0.42},
        "q": rm.score_row(rm.load_coef(), "mlb", "Over 8.0", 0.45)["q"],
        "q_semantics": "ROW_CALIBRATED_NOT_JOINT", "baseline": {
            "p": 0.50, "status": "FROZEN_VALID", "event_id": "official-100", "target_id": "P-600-T1",
            "contract_id": "P-600-C1", "horizon": "PREGAME", "input_cutoff_utc": "2026-09-25T10:00:00Z",
            "training_cutoff_utc": "2026-09-24T23:00:00Z", "version": "A0-test"},
        "method_version": "MDS-test", "method_sha256": "a" * 64, "control_sha256": "b" * 64,
        "manifest_sha256": "c" * 64, "ranking_model_version": "RM-1", "ranking_model_sha256": COEF_SHA,
        "ranking_model_code_sha256": CODE_SHA, "selection_policy_version": "preferred-v1",
        "complementary_pair_id": None, "covering_pair_id": None, "target_weight": 1.0,
        "settlement_revision_id": "P-600-S1", "observed_value": 9, "result": "W",
        "outcome_verified": True, "issue_receipts": [
            {"event_id": "official-100", "lineage_id": "league", "observed_at_utc": "2026-09-25T09:50:00Z", "sha256": "4" * 64,
             "source_ref": "https://league.example/event/100", "fields": {"event_id": "official-100", "event_state": "PREGAME", "event_start_utc": "2026-09-25T11:00:00Z"}},
            {"event_id": "official-100", "lineage_id": "broadcaster", "observed_at_utc": "2026-09-25T09:51:00Z", "sha256": "5" * 64,
             "source_ref": "https://broadcaster.example/event/100", "fields": {"event_id": "official-100", "event_state": "PREGAME", "event_start_utc": "2026-09-25T11:00:00Z"}},
            {"event_id": "official-100", "lineage_id": "data-provider", "observed_at_utc": "2026-09-25T09:52:00Z", "sha256": "6" * 64,
             "source_ref": "https://data.example/event/100", "fields": {"event_id": "official-100", "event_state": "PREGAME", "event_start_utc": "2026-09-25T11:00:00Z"}},
        ], "terminal_receipts": [
            {"event_id": "official-100", "terminal": True, "lineage_id": "league", "sha256": "1" * 64,
             "source_ref": "https://league.example/event/100/final", "observed_at_utc": "2026-09-25T12:00:00Z",
             "fields": {"event_id": "official-100", "result": "W", "terminal_status": "FINAL"}},
            {"event_id": "official-100", "terminal": True, "lineage_id": "broadcaster", "sha256": "2" * 64,
             "source_ref": "https://broadcaster.example/event/100/final", "observed_at_utc": "2026-09-25T12:01:00Z",
             "fields": {"event_id": "official-100", "result": "W", "terminal_status": "FINAL"}},
            {"event_id": "official-100", "terminal": True, "lineage_id": "data-provider", "sha256": "3" * 64,
             "source_ref": "https://data.example/event/100/final", "observed_at_utc": "2026-09-25T12:02:00Z",
             "fields": {"event_id": "official-100", "result": "W", "terminal_status": "FINAL"}},
        ], "missingness": [],
    }
    row.update(overrides)
    return row


class Scores(unittest.TestCase):
    def test_push_capable_score_and_decisive_score_are_separate(self):
        p = {"W": 0.45, "P": 0.13, "L": 0.42}
        self.assertAlmostEqual(sv.score_wpl_brier(p, "W"), 0.2479)
        self.assertAlmostEqual(sv.score_decisive_brier(p, "W"), (0.45 / 0.87 - 1) ** 2)
        with self.assertRaisesRegex(ValueError, "W/L"):
            sv.score_decisive_brier(p, "P")

    def test_missing_push_mass_is_not_filled(self):
        with self.assertRaisesRegex(ValueError, "sum to 1"):
            sv.score_wpl_brier({"W": 0.45, "P": 0.0, "L": 0.42}, "W")


class RecordValidation(unittest.TestCase):
    def test_record_schema_and_semantic_gate_share_required_fields(self):
        schema_path = Path(__file__).resolve().parent.parent / "research" / "settled_rows_2026-09-28" / "prospective_record.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        declared = set(schema["$defs"]["record"]["required"])
        self.assertEqual(sv.REQUIRED, declared)
        self.assertTrue(sv.REQUIRED.issubset(schema["$defs"]["record"]["properties"]))

    def test_complete_record_passes(self):
        self.assertEqual(sv.validate_document({"schema_version": 1, "records": [record()]}), [])

    def test_contract_action_terms_are_mandatory(self):
        item = record()
        item["contract_spec"].pop("void_rule")
        self.assertTrue(any("contract_spec must declare" in error for error in sv.validate_record(item)))

    def test_duplicate_decisions_are_rejected(self):
        r = record()
        errors = sv.validate_document({"schema_version": 1, "records": [r, dict(r, settlement_revision_id="P-600-S2")]})
        self.assertTrue(any("duplicate forecast_id/decision_id" in e for e in errors))

    def test_verified_outcome_requires_declared_category_and_source_receipts(self):
        r = record(result="UNRESOLVED", outcome_verified=True, terminal_receipts=[])
        errors = sv.validate_record(r)
        self.assertTrue(any("verified outcome cannot be unresolved" in e for e in errors))
        self.assertIn("FEWER_THAN_THREE_INDEPENDENT_TERMINAL_LINEAGES", sv.performance_blockers(r))

    def test_live_record_is_blocked_from_pregame_progress(self):
        reasons = sv.performance_blockers(record(horizon="LIVE_ISSUED"))
        self.assertIn("HORIZON_NOT_VERIFIED_PREGAME", reasons)

    def test_issue_at_start_is_blocked(self):
        reasons = sv.performance_blockers(record(issued_at_utc="2026-09-25T11:00:00Z"))
        self.assertIn("ISSUED_AT_OR_AFTER_EVENT_START", reasons)

    def test_baseline_must_match_the_frozen_target_and_cutoff(self):
        r = record()
        r["baseline"]["contract_id"] = "different-contract"
        self.assertIn("BASELINE_CONTRACT_ID_MISMATCH", sv.performance_blockers(r))
        r = record()
        r["baseline"]["training_cutoff_utc"] = "2026-09-25T10:01:00Z"
        self.assertIn("BASELINE_TRAINING_CUTOFF_MISSING_OR_AFTER_INPUT_CUTOFF", sv.performance_blockers(r))

    def test_source_receipts_must_support_the_claimed_issue_and_result(self):
        r = record()
        r["terminal_receipts"][0]["fields"]["result"] = "L"
        self.assertIn("FEWER_THAN_THREE_INDEPENDENT_TERMINAL_LINEAGES", sv.performance_blockers(r))
        r = record()
        r["issue_receipts"][0]["fields"]["event_state"] = "LIVE"
        self.assertIn("FEWER_THAN_THREE_INDEPENDENT_ISSUE_LINEAGES", sv.performance_blockers(r))


class ProbabilityGeometry(unittest.TestCase):
    def test_complementary_contracts_swap_win_loss_and_preserve_push(self):
        left = record()
        right = record(forecast_id="forecast-100-pre", decision_id="P-600-D2", contract_id="P-600-C2",
                       contract="Under 8.0", probabilities={"W": 0.42, "P": 0.13, "L": 0.45},
                       baseline={"p": 0.5, "status": "FROZEN_VALID", "event_id": "official-100",
                                 "target_id": "P-600-T1", "contract_id": "P-600-C2", "horizon": "PREGAME",
                                 "input_cutoff_utc": "2026-09-25T10:00:00Z", "training_cutoff_utc": "2026-09-24T23:00:00Z",
                                 "version": "A0-test"})
        doc = {"schema_version": 1, "records": [left, right], "complements": [
            {"left_decision_id": "P-600-D1", "right_decision_id": "P-600-D2"}]}
        self.assertEqual(sv.validate_document(doc), [])
        right["probabilities"]["P"] = 0.12
        self.assertTrue(any("complement/push identity fails" in e for e in sv.validate_document(doc)))

    def test_complements_must_share_the_same_event_and_freeze(self):
        left = record()
        right = record(decision_id="P-600-D2", contract_id="P-600-C2", target_id="P-600-T1",
                       event_id="another-event", event_cluster_id="another-event",
                       probabilities={"W": 0.42, "P": 0.13, "L": 0.45})
        doc = {"schema_version": 1, "records": [left, right], "complements": [
            {"left_decision_id": "P-600-D1", "right_decision_id": "P-600-D2"}]}
        self.assertTrue(any("disagree on event_id" in e for e in sv.validate_document(doc)))

    def test_covering_pair_below_union_bound_is_rejected(self):
        doc = {"schema_version": 1, "records": [], "geometry": [{
            "p_left": 0.535, "p_right": 0.342, "p_intersection": 0.0,
            "union_covers": True, "semantics": "MARGINAL_EVENT_PROBABILITY",
        }]}
        errors = sv.validate_document(doc)
        self.assertTrue(any("covering pair union probability must equal 1" in e for e in errors))

    def test_row_calibration_scores_cannot_be_used_as_marginal_geometry(self):
        doc = {"schema_version": 1, "records": [], "geometry": [{
            "p_left": 0.535, "p_right": 0.342, "p_intersection": 0.0,
            "union_covers": True, "semantics": "ROW_CALIBRATED_NOT_JOINT",
        }]}
        self.assertTrue(any("cannot be tested using row scores" in e for e in sv.validate_document(doc)))

    def test_malformed_optional_arrays_return_errors_without_crashing(self):
        errors = sv.validate_document({"schema_version": 1, "records": [], "complements": None,
                                       "geometry": {}, "rankings": "not-an-array"})
        self.assertTrue(any("complements must be an array" in e for e in errors))
        self.assertTrue(any("geometry must be an array" in e for e in errors))
        self.assertTrue(any("rankings must be an array" in e for e in errors))

    def test_nested_event_probability_is_monotone(self):
        doc = {"schema_version": 1, "records": [], "nested_events": [{"p_inner": 0.61, "p_outer": 0.59}]}
        self.assertTrue(any("inner event probability exceeds" in e for e in sv.validate_document(doc)))

    def test_distribution_queries_reproduce_from_frozen_states(self):
        good = {"schema_version": 1, "records": [], "distributions": [{
            "states": [{"id": "low", "mass": 0.4}, {"id": "high", "mass": 0.6}],
            "queries": [{"decision_id": "D1", "matching_state_ids": ["high"], "p": 0.6}],
        }]}
        bad = {"schema_version": 1, "records": [], "distributions": [{
            "states": [{"id": "low", "mass": 0.4}, {"id": "high", "mass": 0.6}],
            "queries": [{"decision_id": "D1", "matching_state_ids": ["high"], "p": 0.64}],
        }]}
        self.assertEqual(sv.validate_document(good), [])
        self.assertTrue(any("does not reproduce" in e for e in sv.validate_document(bad)))


class RankingSemantics(unittest.TestCase):
    def test_capped_second_row_prevents_top_two_strong_label(self):
        slate = {"rows": [
            {"rank": 1, "contract_id": "A", "q": 0.72, "tier": "STRONG", "flags": [], "stated_rank": 1},
            {"rank": 2, "contract_id": "B", "q": 0.73, "tier": "SUPPORTED", "flags": ["SIDE_FLIP"], "stated_rank": 2},
        ], "top_two_label": "TOP2_STRONG"}
        errors = sv.validate_document({"schema_version": 1, "records": [], "rankings": [slate]})
        self.assertTrue(any("expected TOP2_SUPPORTED" in e for e in errors))

    def test_near_tied_order_exception_must_be_named_and_bounded(self):
        row = {"rank": 1, "contract_id": "A", "q": 0.48, "p": 0.51, "tier": "COIN_FLIP",
               "flags": ["NEAR_TIED_FLIP"], "ordering_exception": "NEAR_TIED_FLIP_STATED_SIDE", "stated_rank": 1}
        other = {"rank": 2, "contract_id": "B", "q": 0.49, "p": 0.49, "tier": "COIN_FLIP", "flags": [], "stated_rank": 2}
        slate = {"rows": [row, other], "top_two_label": "TOP2_COIN_FLIP"}
        errors = sv.validate_document({"schema_version": 1, "records": [], "rankings": [slate]})
        self.assertFalse(any("near-tied flip" in e or "order does not follow" in e for e in errors))
        row["ordering_exception"] = None
        self.assertTrue(any("named, bounded ordering exception" in e for e in
                            sv.validate_document({"schema_version": 1, "records": [], "rankings": [slate]})))

    def test_independence_product_is_not_reported_without_basis(self):
        slate = {"rows": [
            {"rank": 1, "contract_id": "A", "q": 0.55, "tier": "LEAN", "flags": [], "stated_rank": 1},
            {"rank": 2, "contract_id": "B", "q": 0.54, "tier": "COIN_FLIP", "flags": [], "stated_rank": 2},
        ], "top_two_label": "TOP2_COIN_FLIP", "independence_product_claim": 0.25}
        self.assertTrue(any("explicit independence basis" in e for e in
                            sv.validate_document({"schema_version": 1, "records": [], "rankings": [slate]})))

    def test_malformed_rank_rows_return_errors_instead_of_crashing(self):
        slate = {"rows": [{"rank": "first", "contract_id": "A"}], "top_two_label": "TOP2_COIN_FLIP"}
        errors = sv.validate_document({"schema_version": 1, "records": [], "rankings": [slate]})
        self.assertTrue(any("rank must be an integer" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
