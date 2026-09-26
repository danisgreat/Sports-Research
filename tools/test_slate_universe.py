"""Tests for tools/slate_universe.py (C-EVENT-UNIVERSE, added 2026-09-26). Offline: fixtures only."""
import datetime as dt
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import slate_universe as su  # noqa: E402

FIX = str(HERE.parent / "tests_fixtures" / "universe")
NOW = dt.datetime(2026, 9, 27, 12, 0, tzinfo=dt.timezone.utc)


class DeclareTests(unittest.TestCase):
    def test_only_unstarted_events_are_in_scope(self):
        u = su.declare("2026-09-27", ["mlb", "epl"], NOW, None, None, FIX)
        ids = [e["id"] for e in u["events"]]
        # leagues in the order given, each sorted by start time
        self.assertEqual(ids, ["mlb:900001", "mlb:900002", "mlb:900003", "epl:740001", "epl:740002"])
        self.assertNotIn("mlb:900004", ids)  # live
        self.assertNotIn("mlb:900005", ids)  # postponed
        self.assertNotIn("epl:740003", ids)  # final
        why = {e["id"]: e["why"] for e in u["excluded"]}
        self.assertEqual(why["mlb:900004"], "STATE_IN")
        self.assertEqual(why["mlb:900005"], "STATE_POSTPONED")
        self.assertEqual(why["epl:740003"], "STATE_POST")

    def test_start_time_passed_is_excluded_even_if_feed_says_pre(self):
        late = dt.datetime(2026, 9, 27, 18, 0, tzinfo=dt.timezone.utc)
        u = su.declare("2026-09-27", ["mlb"], late, None, None, FIX)
        why = {e["id"]: e["why"] for e in u["excluded"]}
        self.assertEqual(why["mlb:900001"], "START_TIME_PASSED")
        self.assertEqual([e["id"] for e in u["events"]], ["mlb:900002", "mlb:900003"])

    def test_seeded_sample_is_reproducible(self):
        a = su.declare("2026-09-27", ["mlb"], NOW, 7, 2, FIX)
        b = su.declare("2026-09-27", ["mlb"], NOW, 7, 2, FIX)
        self.assertEqual([e["id"] for e in a["events"]], [e["id"] for e in b["events"]])
        self.assertEqual(len(a["events"]), 2)
        self.assertEqual(sum(e["why"] == "NOT_SAMPLED" for e in a["excluded"]), 1)

    def test_market_keys_are_quarantined(self):
        payload = su.load_schedule("epl", "2026-09-27", FIX)
        text = json.dumps(payload)
        self.assertNotIn("pickcenter", text)
        self.assertNotIn("QUARANTINED", text)


class FileTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "UNIVERSE_2026-09-27.json"
        self.u = su.declare("2026-09-27", ["mlb", "epl"], NOW, None, None, FIX)
        su.write_new(self.path, self.u)

    def tearDown(self):
        self.tmp.cleanup()

    def test_never_overwritten(self):
        with self.assertRaises(SystemExit):
            su.write_new(self.path, self.u)

    def test_edit_after_declaration_is_detected(self):
        u = json.loads(self.path.read_text(encoding="utf-8"))
        u["events"] = u["events"][:-1]
        self.path.write_text(json.dumps(u), encoding="utf-8")
        with self.assertRaises(SystemExit):
            su.load_universe(self.path)

    def test_skip_keeps_hash_and_validates_reason(self):
        su.add_skip(self.path, "mlb:900002", "GATE_FAIL:BB-P2", NOW)
        u = su.load_universe(self.path)  # hash still verifies
        self.assertEqual(u["skips"][0]["id"], "mlb:900002")
        with self.assertRaises(SystemExit):
            su.add_skip(self.path, "mlb:900002", "BORED", NOW)
        with self.assertRaises(SystemExit):
            su.add_skip(self.path, "mlb:123", "OTHER:x", NOW)

    def test_coverage_counts_carded_skipped_missing(self):
        su.add_skip(self.path, "mlb:900002", "POSTPONED", NOW)
        u = su.load_universe(self.path)
        log = "### P-600 — MLB\nreceipts.py pregame mlb 900001\n### P-601 — EPL event 740002\n"
        rows = {r["id"]: r["status"] for r in su.coverage(u, [log])}
        self.assertEqual(rows["mlb:900001"], "CARDED")
        self.assertEqual(rows["epl:740002"], "CARDED")
        self.assertEqual(rows["mlb:900002"], "SKIPPED: POSTPONED")
        self.assertEqual(rows["mlb:900003"], "MISSING")
        self.assertEqual(rows["epl:740001"], "MISSING")
        text = su.render_status(su.coverage(u, [log]), u)
        self.assertIn("2 carded, 1 skipped, 2 missing", text)

    def test_id_match_is_whole_token(self):
        u = su.load_universe(self.path)
        rows = {r["id"]: r["status"] for r in su.coverage(u, ["gamePk 9000011 and 7400012"])}
        self.assertEqual(rows["mlb:900001"], "MISSING")
        self.assertEqual(rows["epl:740001"], "MISSING")


if __name__ == "__main__":
    unittest.main()
