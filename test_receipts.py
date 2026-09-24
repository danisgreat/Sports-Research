"""Tests for receipts.py (added 2026-09-25).

Fixtures in tests_fixtures/receipts/ are trimmed field-owner JSON for games already settled in
PREDICTION_LOG_COMBINED_5.md (P-500 = MLB 824223, P-506 = MLB 823086, P-503 = NHL 2026010034,
P-504 = ESPN WNBA 401857213), plus two pregame captures (MLB 824703, NBL 401875254). They contain
no price or market keys: test_fixtures_are_market_free enforces that. The assertions pin facts the
log already records, so a parser regression shows up as a disagreement with the settled record.
"""
import glob
import io
import json
import os
import unittest
from contextlib import redirect_stdout

import receipts as r

FX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests_fixtures", "receipts")
NOW = "2026-09-25T00:00:00Z"


def run(*argv):
    buf = io.StringIO()
    with redirect_stdout(buf):
        r.main(list(argv) + ["--now", NOW])
    return buf.getvalue()


class NameMatching(unittest.TestCase):
    def test_accents_and_case(self):
        self.assertEqual(r.name_match("andres chaparro", ["Andrés Chaparro"]), "Andrés Chaparro")

    def test_initial_and_surname(self):
        self.assertEqual(r.name_match("J. Oettinger", ["Jake Oettinger", "Casey DeSmith"]), "Jake Oettinger")

    def test_no_false_match_on_shared_surname(self):
        # Two official players share a surname, and the card's initial matches neither.
        self.assertIsNone(r.name_match("X. Jones", ["Jonquel Jones", "Brionna Jones"]))

    def test_lineup_diff_counts(self):
        d = r.lineup_diff(["Riley Greene", "Colt Keith"], ["Riley Greene", "Kevin McGonigle"])
        self.assertEqual((d["matched"], d["card_count"], d["not_in_official"]), (1, 2, ["Colt Keith"]))


class GameState(unittest.TestCase):
    def test_mlb_final_codes(self):
        now = r.parse_iso(NOW)
        self.assertEqual(r.game_state("mlb", "F", None, now), "FINAL")
        self.assertEqual(r.game_state("mlb", "In Progress", None, now), "LIVE")

    def test_start_crossed_without_final_is_not_pregame(self):
        now = r.parse_iso(NOW)
        start = r.parse_iso("2026-09-24T23:00:00Z")
        self.assertEqual(r.game_state("espn", "pre", start, now), "START_CROSSED_STATUS_NOT_FINAL")

    def test_aest_is_utc_plus_10(self):
        self.assertEqual(r.aest(r.parse_iso("2026-09-24T00:00:00Z")), "2026-09-24 10:00 AEST")


class MlbReceipts(unittest.TestCase):
    def test_p500_final_weather_and_pitchers(self):
        out = run("settle", "mlb", "824223", "--fixture", os.path.join(FX, "mlb_824223_final.json"),
                  "--card-sp-away", "Richard Lovelady", "--card-sp-home", "Framber Valdez")
        self.assertIn("WSH 4 – 2 DET", out)
        self.assertIn("In From LF", out)  # the card said "out"; the gamefeed says in (M30)
        self.assertIn("official Framber Valdez → MATCH", out)
        self.assertIn("statsapi.mlb.com/api/v1.1/game/824223/feed/live", out)

    def test_replaced_starter_recovered(self):
        out = run("settle", "mlb", "824223", "--fixture", os.path.join(FX, "mlb_824223_final.json"))
        # Keibert Ruiz entered in slot 7 as a substitute (702); the starter was Harry Ford.
        self.assertIn("7. Harry Ford C", out)
        self.assertNotIn("Keibert Ruiz C;", out.split("Starting lineup — WSH")[1].split("\n")[0])

    def test_p506_regulation_score_printed_for_extras(self):
        out = run("settle", "mlb", "823086", "--fixture", os.path.join(FX, "mlb_823086_extras.json"))
        self.assertIn("HOU 5 – 6 SEA; innings played 10 (scheduled 9)", out)
        self.assertIn("Score after regulation | 4–4", out)

    def test_pregame_not_published_states(self):
        out = run("pregame", "mlb", "824703", "--fixture", os.path.join(FX, "mlb_824703_pregame.json"))
        self.assertIn("**PREGAME**", out)
        self.assertIn("LINEUPS_NOT_YET_PUBLISHED", out)
        self.assertIn("WEATHER_NOT_YET_PUBLISHED", out)
        self.assertNotIn("Final score", out)

    def test_card_lineup_diff_flags_absent_player(self):
        out = run("settle", "mlb", "824223", "--fixture", os.path.join(FX, "mlb_824223_final.json"),
                  "--card-home", "Kevin McGonigle;Riley Greene;Colt Keith")
        self.assertIn("2/3 card-named starters started; not in official lineup: Colt Keith", out)


class NhlReceipt(unittest.TestCase):
    def test_p503_confirmed_goalie_did_not_play(self):
        out = run("settle", "nhl", "2026010034", "--fixture", os.path.join(FX, "nhl_2026010034_final.json"),
                  "--card-goalie-home", "Jake Oettinger")
        self.assertIn("MIN 0 – 2 DAL; decided in REG", out)
        self.assertIn("R. Poirier 59:29", out)
        self.assertIn("card Jake Oettinger → **DID NOT PLAY", out)
        self.assertIn("gameType 1", out)


class EspnReceipts(unittest.TestCase):
    def test_p504_final_and_starters(self):
        out = run("settle", "espn", "basketball/wnba", "401857213", "--fixture",
                  os.path.join(FX, "espn_wnba_401857213_final.json"), "--card-home", "Sabrina Ionescu;Breanna Stewart")
        self.assertIn("ATL 83 – 65 NY", out)
        self.assertIn("Period scores — NY | 19 7 18 21", out)
        self.assertIn("1/2 card-named starters started; not in official starters: Breanna Stewart", out)

    def test_nbl_pregame(self):
        out = run("pregame", "espn", "basketball/nbl", "401875254", "--fixture",
                  os.path.join(FX, "espn_nbl_401875254_pregame.json"))
        self.assertIn("2026-09-26 21:30 AEST", out)
        self.assertIn("**PREGAME**", out)


class MarketBlind(unittest.TestCase):
    def test_quarantine_strips_nested_keys(self):
        d = r._strip_quarantined({"a": 1, "odds": [1], "x": {"pickcenter": 2, "y": [{"winprobability": 3, "z": 4}]}})
        self.assertEqual(d, {"a": 1, "x": {"y": [{"z": 4}]}})

    def test_fixtures_are_market_free(self):
        for path in glob.glob(os.path.join(FX, "*.json")):
            with open(path, encoding="utf-8") as fh:
                text = fh.read().casefold()
            for bad in ('"odds"', '"pickcenter"', '"againstthespread"', '"winprobability"', '"oddspartners"',
                        "moneyline", "spread", "sportsbook"):
                self.assertNotIn(bad, text, f"{os.path.basename(path)} contains {bad}")
            json.loads(text)


if __name__ == "__main__":
    unittest.main()
