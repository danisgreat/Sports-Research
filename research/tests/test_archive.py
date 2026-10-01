"""Evidence admission regressions use synthetic fixtures, never live requests."""
import csv
import gzip
import io
import json
import tempfile
import unittest
from pathlib import Path

try:
    from research.src.archive import (build, validate, read_events, normalize_row, parse_score, team_key,
                                     repair, refresh_supported, inventory, EVENT_FIELDS)
    from research.src.archive_sources import EvidenceError, read_receipt, sha256, EvidenceIndex, parse_afl_tables, mlb_schedule_url
except ModuleNotFoundError:
    from src.archive import (build, validate, read_events, normalize_row, parse_score, team_key,
                            repair, refresh_supported, inventory, EVENT_FIELDS)
    from src.archive_sources import EvidenceError, read_receipt, sha256, EvidenceIndex, parse_afl_tables, mlb_schedule_url

FIELDS = ["Game Number", "Game Type", "Team A", "Team B", "Home", "Away", "Venue", "Date",
          "Game Score", "Total Points", "Winning Margin", "Notable Players", "Game comment"]


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "Previous Sports Results"
        self.root.mkdir()
        self.url = "https://afltables.com/afl/seas/2025.html"
        self.body = b'''<table style="font: 12px Verdana;" width=100% border=1>
<tr><td><a href="../teams/swans_idx.html">Sydney</a></td><td>11.10</td><td>76</td><td>Fri 07-Mar-2025 7:40 PM <b>Venue:</b> <a href="../venues/scg.html">S.C.G.</a></td></tr>
<tr><td><a href="../teams/hawthorn_idx.html">Hawthorn</a></td><td>14.12</td><td>96</td><td>Hawthorn won by 20 pts [<a href="../stats/games/2025/101620250307.html">Match stats</a>]</td></tr></table>'''
        self.receipt = self.make_receipt(self.url, self.body)
        self.raw = {"Game Number": "1", "Game Type": "Regular Season", "Team A": "Sydney", "Team B": "Hawthorn",
                    "Home": "Sydney", "Away": "Hawthorn", "Venue": "S.C.G.", "Date": "2025-03-07",
                    "Game Score": "Hawthorn 14.12 (96) def. Sydney 11.10 (76)", "Total Points": "172",
                    "Winning Margin": "20", "Notable Players": "Season Brownlow winner", "Game comment": "Postgame summary"}

    def tearDown(self):
        self.temp.cleanup()

    def make_receipt(self, url, body, official=False):
        folder = self.root / ("_custody/official_sources" if official else "_football_research/sources")
        folder.mkdir(parents=True, exist_ok=True)
        key = sha256(url.encode())
        path = folder / (key + ".json")
        (folder / (key + ".gz")).write_bytes(gzip.compress(body))
        path.write_text(json.dumps({"url": url, "http_status": 200, "stored_body": key + ".gz",
                                   "stored_sha256": sha256(body), "retrieved_utc": "2026-10-01T00:00:00+00:00"}), encoding="utf-8")
        return path

    def write_rows(self, competition="AFL", year="2025", rows=None, sport="AFL"):
        path = self.root / sport / competition / year / (year + "_games.csv")
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, FIELDS)
            writer.writeheader(); writer.writerows(rows if rows is not None else [self.raw])
        return path

    def normalized(self, raw=None, year="2025", competition="AFL", evidence=True):
        index = EvidenceIndex(self.root, team_key).load() if evidence else None
        return normalize_row(raw or self.raw, "AFL", competition, year, "sample.csv", 2, "original", index)

    def test_exact_aliases_preserve_distinct_clubs(self):
        self.assertNotEqual(team_key("Melbourne"), team_key("North Melbourne"))
        self.assertNotEqual(team_key("Port Adelaide"), team_key("Adelaide Crows"))
        self.assertNotEqual(team_key("Brisbane Bears"), team_key("Brisbane Lions"))
        self.assertEqual(team_key("Kangaroos"), team_key("North Melbourne"))
        self.assertEqual(team_key("South Melbourne"), team_key("Sydney Swans"))

    def test_score_parser_preserves_endpoint_and_zero(self):
        self.assertEqual(parse_score("Port Adelaide 0.0 (0) def. by St Kilda 2.2 (14)"), ("Port Adelaide", 0, "St Kilda", 14))
        self.assertEqual(parse_score("A 0 drew with B 0"), ("A", 0, "B", 0))
        self.assertIsNone(parse_score("unknown"))

    def test_hash_and_receipt_identity_fail_closed(self):
        receipt, body = read_receipt(self.receipt)
        self.assertEqual(body, self.body)
        (self.receipt.parent / receipt["stored_body"]).write_bytes(gzip.compress(b"altered"))
        with self.assertRaises(EvidenceError):
            read_receipt(self.receipt)

    def test_receipt_body_path_cannot_escape_cache(self):
        receipt = json.loads(self.receipt.read_text())
        receipt["stored_body"] = "../outside.gz"
        self.receipt.write_text(json.dumps(receipt))
        with self.assertRaises(EvidenceError):
            read_receipt(self.receipt)

    def test_missing_source_never_becomes_training_eligible(self):
        row = self.normalized(evidence=False)
        self.assertEqual(row["training_eligible"], "false")
        self.assertIn("missing_exact_result_source", row["exclusion_reasons"])
        self.assertEqual(row["source_url"], "")

    def test_arithmetic_disagreement_is_excluded(self):
        raw = dict(self.raw, **{"Total Points": "0"})
        row = self.normalized(raw)
        self.assertEqual(row["training_eligible"], "false")
        self.assertIn("total_score_disagreement", row["exclusion_reasons"])
        self.assertEqual(row["total_score"], 172)

    def test_invalid_nonexistent_season_is_excluded(self):
        row = self.normalized(year="1900", competition="NFL", evidence=False)
        self.assertEqual(row["training_eligible"], "false")
        self.assertIn("competition_not_founded", row["exclusion_reasons"])

    def test_retrieval_is_not_historical_publication_time(self):
        row = self.normalized()
        self.assertEqual(len(row), len(EVENT_FIELDS))
        self.assertEqual(row["training_eligible"], "true")
        self.assertEqual(row["available_at_utc"], "")
        self.assertEqual(row["retrieved_at_utc"], "2026-10-01T00:00:00+00:00")
        self.assertIn("prior_dates_only", row["availability_rule"])

    def test_home_score_mapping_follows_score_owner(self):
        row = self.normalized()
        self.assertEqual((row["home_score"], row["away_score"], row["margin_signed_home"]), (76, 96, -20))

    def test_duplicates_narratives_and_empty_seasons(self):
        self.write_rows(rows=[self.raw, dict(self.raw, **{"Game Number": "2"})])
        self.write_rows(competition="AFLW", year="1900", rows=[])
        manifest = build(self.root)
        self.assertEqual(manifest["counts"]["duplicate_event"], 1)
        self.assertEqual(manifest["counts"]["header_only_files"], 1)
        self.assertEqual(manifest["counts"]["canonical_events"], 1)
        self.assertTrue(validate(self.root)["valid"])
        self.assertEqual(len(read_events(self.root / "_canonical/events.csv")), 1)
        with (self.root / "_canonical/narratives.csv").open(newline="") as handle:
            narratives = list(csv.DictReader(handle))
        self.assertTrue(all(row["pregame_feature_eligible"] == "false" for row in narratives))
        with (self.root / "_canonical/seasons.csv").open(newline="") as handle:
            seasons = list(csv.DictReader(handle))
        self.assertEqual(next(row for row in seasons if row["season_folder"] == "1900")["coverage_status"], "not_founded")

    def test_subset_and_mirror_admission(self):
        self.write_rows()
        self.write_rows(competition="AFL Grand Final")
        self.write_rows(competition="College Football", sport="American Football")
        manifest = build(self.root)
        self.assertEqual(manifest["counts"]["subset_collection"], 1)
        self.assertEqual(manifest["counts"]["mirrored_collection"], 1)
        self.assertEqual(len(read_events(self.root / "_canonical/events.csv")), 1)

    def test_input_and_output_hash_drift_are_detected(self):
        raw = self.write_rows()
        build(self.root)
        raw.write_bytes(raw.read_bytes() + b"\n")
        self.assertFalse(validate(self.root)["valid"])
        export = self.root / "_canonical/events.csv"
        export.write_bytes(export.read_bytes() + b"\n")
        with self.assertRaises(EvidenceError):
            read_events(export)

    def test_parser_extracts_field_owner_match_id(self):
        events = parse_afl_tables(self.body, self.url)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["source_event_id"], "https://afltables.com/afl/stats/games/2025/101620250307.html")

    def test_correction_requires_evidence_and_is_journaled_idempotently(self):
        raw = dict(self.raw, **{"Home": "Iowa State", "Away": "Kansas State", "Team A": "Kansas State",
            "Team B": "Iowa State", "Date": "2025-08-23", "Game Score": "Kansas State 21 def. Iowa State 20",
            "Total Points": "41", "Winning Margin": "1", "Game Type": "pre-Season"})
        path = self.write_rows(competition="NCAA Division I FBS", sport="College Football", rows=[raw])
        original = path.read_bytes()
        self.assertEqual(repair(self.root)["changed_rows"], 0)
        url = "https://cyclones.com/sports/football/stats/2025/kansas-state/boxscore/17234"
        receipt_path = self.make_receipt(url, b"synthetic official-source fixture: Iowa State 24 Kansas State 21", official=True)
        receipt, body = read_receipt(receipt_path)
        fact = {"competition_id": "ncaa-division-i-fbs", "event_date": "2025-08-23", "home_team": "Iowa State",
            "away_team": "Kansas State", "home_score": 24, "away_score": 21, "venue": "Aviva Stadium",
            "source_event_id": "IowaState-17234", "season_id": "2025", "stage": "Regular Season",
            "source_receipt_path": str(receipt_path.relative_to(self.root.parent)), "source_body_sha256": sha256(body),
            "verification_method": "manual_primary_source_event_and_fields"}
        (self.root / "_custody/verified_facts.json").write_text(json.dumps([fact]), encoding="utf-8")
        result = repair(self.root)
        self.assertEqual(result["changed_rows"], 1)
        self.assertIn(b"Iowa State 24 def. Kansas State 21", path.read_bytes())
        journal = json.loads((self.root / "_custody/corrections.jsonl").read_text().strip())
        self.assertEqual(journal["original_sha256"], sha256(original))
        backup = self.root / "_custody/originals" / sha256(original) / path.name
        self.assertEqual(backup.read_bytes(), original)
        self.assertEqual(repair(self.root)["changed_rows"], 0)

    def test_source_identity_and_date_drift_fail_closed(self):
        index = EvidenceIndex(self.root, team_key).load()
        row = self.normalized(dict(self.raw, **{"Date": "2025-03-08"}))
        self.assertEqual(row["training_eligible"], "false")
        receipt = json.loads(self.receipt.read_text())
        receipt["url"] = "https://afltables.com/afl/seas/2024.html"
        self.receipt.write_text(json.dumps(receipt))
        with self.assertRaises(EvidenceError):
            read_receipt(self.receipt)

    def test_historic_bears_repair_requires_exact_source_and_era(self):
        body = self.body.replace(b"2025", b"1987").replace(b"Hawthorn", b"Brisbane Bears")
        self.make_receipt("https://afltables.com/afl/seas/1987.html", body)
        raw = dict(self.raw, **{"Date": "1987-03-07", "Away": "Brisbane", "Team B": "Brisbane",
            "Game Score": "Brisbane 14.12 (96) def. Sydney 11.10 (76)"})
        path = self.write_rows(year="1987", rows=[raw])
        result = repair(self.root)
        self.assertEqual(result["changed_rows"], 1)
        with path.open(encoding="utf-8", newline="") as handle:
            corrected = next(csv.DictReader(handle))
        self.assertEqual(corrected["Away"], "Brisbane Bears")
        self.assertEqual(corrected["Notable Players"], "")
        self.assertEqual(repair(self.root)["changed_rows"], 0)
        index = EvidenceIndex(self.root, team_key).load()
        self.assertIsNone(index.match("afl", "2025-03-07", "Sydney", "Brisbane", 76, 96))
        self.assertIsNone(index.match("afl", "1987-03-07", "Sydney", "Brisbane", 76, 95))

    def test_1905_round_date_repair_uses_owned_match_date(self):
        body = self.body.replace(b"2025", b"1905").replace(b"07-Mar", b"03-Jun").replace(b"Sydney", b"Melbourne").replace(b"Hawthorn", b"Fitzroy")
        self.make_receipt("https://afltables.com/afl/seas/1905.html", body)
        raw = dict(self.raw, **{"Date": "1905-06-05", "Home": "Melbourne", "Away": "Fitzroy",
            "Team A": "Melbourne", "Team B": "Fitzroy", "Game Score": "Fitzroy 14.12 (96) def. Melbourne 11.10 (76)"})
        path = self.write_rows(year="1905", rows=[raw])
        self.assertEqual(repair(self.root)["changed_rows"], 1)
        with path.open(encoding="utf-8", newline="") as handle:
            corrected = next(csv.DictReader(handle))
        self.assertEqual(corrected["Date"], "1905-06-03")
        self.assertEqual(repair(self.root)["changed_rows"], 0)

    def test_refresh_appends_only_evidenced_mlb_result_and_preserves_missingness(self):
        game = {"gamePk": 44, "officialDate": "2026-09-30", "gameDate": "2026-09-30T23:00:00Z",
            "gameType": "R", "season": "2026", "status": {"abstractGameState": "Final"},
            "teams": {"home": {"score": 5, "team": {"id": 1, "name": "Home Club"}},
                      "away": {"score": 3, "team": {"id": 2, "name": "Away Club"}}}, "venue": {"name": "Park"}}
        self.make_receipt(mlb_schedule_url(2026), json.dumps({"dates": [{"date": "2026-09-30", "games": [game]}]}).encode(), official=True)
        fields = ["Game Number", "Game ID (MLB gamePk)", "Season", "Season Phase", "Game Type", "Date",
            "Start Time (UTC)", "Home Team", "Away Team", "Venue", "Home Score", "Away Score", "Total Runs",
            "Winning Margin", "Winning Team", "Losing Team", "Result", "Game Score", "Primary Data Source",
            "Independent Check (Retrosheet or ESPN)", "Check Details", "Home Starting Pitcher", "Notable Players"]
        path = self.root / "Baseball/MLB/2026/2026_games.csv"
        path.parent.mkdir(parents=True)
        with path.open("w", encoding="utf-8", newline="") as handle:
            csv.DictWriter(handle, fields).writeheader()
        original = path.read_bytes()
        self.assertEqual(refresh_supported(self.root)["game_ids"], ["44"])
        with path.open(encoding="utf-8", newline="") as handle:
            row = next(csv.DictReader(handle))
        self.assertEqual((row["Home Score"], row["Away Score"]), ("5", "3"))
        self.assertEqual(row["Home Starting Pitcher"], "")
        self.assertEqual(row["Notable Players"], "")
        self.assertEqual(refresh_supported(self.root)["appended_results"], 0)
        self.assertEqual((self.root / "_custody/originals" / sha256(original) / path.name).read_bytes(), original)
        self.assertEqual(build(self.root)["counts"]["training_eligible"], 1)
        self.assertTrue(validate(self.root)["valid"])

    def test_unused_receipt_metadata_is_bound_and_inventory_is_measured(self):
        self.write_rows()
        self.write_rows(competition="NFL", sport="American Football", year="1900", rows=[])
        unused = self.make_receipt("https://example.invalid/unused-fixture", b"unused but retained", official=True)
        manifest = build(self.root)
        self.assertEqual(manifest["all_source_custody"]["receipt_count"], 2)
        measured = inventory(self.root)
        self.assertEqual(measured["counts"]["rows"], 1)
        self.assertEqual(measured["counts"]["header_only"], 1)
        self.assertTrue(measured["canonical_input_snapshot_current"])
        metadata = json.loads(unused.read_text())
        metadata["retrieved_utc"] = "changed metadata, same source body"
        unused.write_text(json.dumps(metadata))
        result = validate(self.root)
        self.assertFalse(result["valid"])
        self.assertIn("all_source_custody_snapshot_changed", result["issues"])


if __name__ == "__main__":
    unittest.main()
