"""Regression checks for strict identity joins and conflict quarantine in the Markdown extractor."""
import importlib.util
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PATH = REPO / "research" / "settled_rows_2026-09-25" / "extract_settled_rows.py"
spec = importlib.util.spec_from_file_location("strict_settled_extractor", PATH)
ex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex)


def row(**overrides):
    value = {"part": "log.md", "line": 10, "card": "P-600", "rank": 1,
             "contract": "Over 8.5", "p": 0.61, "q": 0.59, "baseline_p": 0.55,
             "preferred_at_issue": True, "result": "W"}
    value.update(overrides)
    return value


class StrictExtraction(unittest.TestCase):
    def test_exact_identical_duplicates_deduplicate_and_keep_every_source(self):
        a, b = row(), row(part="mini.md", line=90)
        accepted, conflicts = ex.reconcile_occurrences([a, b], {})
        self.assertEqual(len(accepted), 1)
        self.assertEqual(accepted[0]["source_occurrences"], "log.md:10 ; mini.md:90")
        self.assertEqual(conflicts, [])

    def test_different_results_are_quarantined_not_last_wins(self):
        accepted, conflicts = ex.reconcile_occurrences([row(), row(part="audit.md", result="L")], {})
        self.assertEqual(accepted, [])
        self.assertIn("CONFLICTING_RESULT", conflicts[0]["reason"])

    def test_different_contracts_at_same_rank_are_quarantined(self):
        accepted, conflicts = ex.reconcile_occurrences([row(), row(part="audit.md", contract="Under 8.5")], {})
        self.assertEqual(accepted, [])
        self.assertIn("MULTIPLE_CONTRACTS_FOR_CARD_RANK", conflicts[0]["reason"])

    def test_issued_probabilities_join_only_on_exact_normalized_contract(self):
        issue = {("P-600", 1): [{"contract": "OVER 8.5", "p": 0.61, "q": 0.59,
                                 "baseline_p": 0.55, "preferred_at_issue": True}]}
        accepted, conflicts = ex.reconcile_occurrences([row(p=None, q=None, baseline_p=None,
                                                              preferred_at_issue=None)], issue)
        self.assertEqual(conflicts, [])
        self.assertEqual(accepted[0]["p"], 0.61)  # case and formatting normalize; contract terms are identical
        issue[("P-600", 1)][0]["contract"] = "Under 8.5"
        accepted, conflicts = ex.reconcile_occurrences([row(p=None, q=None, baseline_p=None,
                                                              preferred_at_issue=None)], issue)
        self.assertEqual(accepted[0]["p"], None)
        self.assertEqual(conflicts, [])

    def test_issue_settlement_baseline_disagreement_is_quarantined(self):
        issue = {("P-600", 1): [{"contract": "Over 8.5", "p": 0.61, "q": 0.59,
                                 "baseline_p": 0.63, "preferred_at_issue": True}]}
        accepted, conflicts = ex.reconcile_occurrences([row(baseline_p=0.5)], issue)
        self.assertEqual(accepted, [])
        self.assertIn("ISSUE_SETTLEMENT_BASELINE_P_DISAGREEMENT", conflicts[0]["reason"])

    def test_horizon_is_labeled_but_not_promoted_to_eligibility(self):
        self.assertEqual(ex.infer_horizon("Status: LIVE-ISSUED VIEW"), "LIVE_ISSUED")
        self.assertEqual(ex.infer_horizon("Status: PREGAME"), "PREGAME_LABEL_ONLY")
        self.assertEqual(ex.infer_horizon("Card details pending"), "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
