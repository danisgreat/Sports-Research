"""Tests for tools/sport_models.py and tools/sport_data.py (C-SPORT-SHADOW, added 2026-09-26).
Offline: synthetic seasons whose true structure is known, so the tests check arithmetic, leak-freedom and
that each A1 can find real structure. They say nothing about accuracy on real competitions."""
import datetime as dt
import json
import math
import random
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sport_data as sd  # noqa: E402
import sport_models as sm  # noqa: E402


def pois(rng, lam):
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1


def round_robin(teams, rng):
    order = teams[:]
    rng.shuffle(order)
    return list(zip(order[0::2], order[1::2]))


def soccer_season(seasons=2, seed=5, ht=True):
    rng = random.Random(seed)
    teams = [f"T{i:02d}" for i in range(12)]
    att = {t: 1.6 - 0.1 * i for i, t in enumerate(teams)}
    dfn = {t: 0.6 + 0.08 * i for i, t in enumerate(teams)}
    games, gid = [], 0
    for s in range(seasons):
        start = dt.date(2023 + s, 8, 1)
        for wk in range(30):
            d = (start + dt.timedelta(days=7 * wk)).isoformat()
            for h, a in round_robin(teams, rng):
                mh, ma = 1.15 * att[h] * dfn[a], 0.9 * att[a] * dfn[h]
                h1h, h1a = pois(rng, 0.44 * mh), pois(rng, 0.44 * ma)
                gid += 1
                games.append({"id": str(gid), "date": d, "season": 2023 + s, "home": h, "away": a,
                              "hs": h1h + pois(rng, 0.56 * mh), "as": h1a + pois(rng, 0.56 * ma),
                              "hs_ht": h1h if ht else None, "as_ht": h1a if ht else None, "neutral": False})
    return games


def gridiron_season(seasons=3, seed=7):
    """Scores built from touchdowns (7) and field goals (3), so margins have real key numbers."""
    rng = random.Random(seed)
    teams = [f"G{i:02d}" for i in range(16)]
    q = {t: 1.4 - 0.05 * i for i, t in enumerate(teams)}
    games, gid = [], 0
    for s in range(seasons):
        start = dt.date(2022 + s, 9, 8)
        for wk in range(17):
            d = (start + dt.timedelta(days=7 * wk)).isoformat()
            for h, a in round_robin(teams, rng):
                sh = 7 * pois(rng, 2.3 * q[h] / q[a] * 1.05) + 3 * pois(rng, 1.6)
                sa = 7 * pois(rng, 2.3 * q[a] / q[h] * 0.95) + 3 * pois(rng, 1.6)
                gid += 1
                games.append({"id": str(gid), "date": d, "season": 2022 + s, "home": h, "away": a,
                              "hs": sh, "as": sa, "neutral": False})
    return games


def hoops_season(seed=9):
    rng = random.Random(seed)
    teams = [f"B{i:02d}" for i in range(12)]
    off = {t: 8 - 1.4 * i for i, t in enumerate(teams)}
    games, gid = [], 0
    start = dt.date(2025, 10, 20)
    for day in range(150):
        d = (start + dt.timedelta(days=day)).isoformat()
        if day % 2:
            continue
        for h, a in round_robin(teams, rng):
            sh = round(rng.gauss(112 + off[h] - off[a] / 2 + 1.5, 11))
            sa = round(rng.gauss(112 + off[a] - off[h] / 2 - 1.5, 11))
            if sh == sa:
                sh += 5 if rng.random() < 0.5 else 0
                sa += 0 if sh > sa else 5
            gid += 1
            games.append({"id": str(gid), "date": d, "season": 2026, "home": h, "away": a, "hs": sh, "as": sa,
                          "neutral": False, "finish": "REG"})
    return games


def hockey_season(seed=11):
    rng = random.Random(seed)
    teams = [f"H{i:02d}" for i in range(12)]
    s = {t: 1.3 - 0.05 * i for i, t in enumerate(teams)}
    games, gid = [], 0
    start = dt.date(2025, 10, 5)
    for day in range(0, 180, 2):
        d = (start + dt.timedelta(days=day)).isoformat()
        for h, a in round_robin(teams, rng):
            rh, ra = pois(rng, 3.1 * s[h] / s[a] * 1.03), pois(rng, 3.1 * s[a] / s[h] * 0.97)
            finish = "REG"
            if rh == ra:
                finish = "OT" if rng.random() < 0.62 else "SO"
                if rng.random() < 0.5:
                    rh += 1
                else:
                    ra += 1
            gid += 1
            games.append({"id": str(gid), "date": d, "home": h, "away": a, "hs": rh, "as": ra, "finish": finish,
                          "neutral": False})
    return games


class Distributions(unittest.TestCase):
    def test_disc_normal_and_weights(self):
        p = sm.disc_normal(2.3, 12.0)
        self.assertAlmostEqual(sum(p.values()), 1.0, places=12)
        self.assertAlmostEqual(sm.pmf_mean(p), 2.3, delta=0.05)
        no_tie = sm.disc_normal(0.0, 5.0, lambda k: 0.0 if k == 0 else 1.0)
        self.assertNotIn(0, no_tie)
        self.assertAlmostEqual(sum(no_tie.values()), 1.0, places=12)
        self.assertTrue(all(k >= 0 for k in sm.disc_normal(1.0, 3.0, floor0=True)))

    def test_rps_is_proper_on_a_point_mass(self):
        self.assertEqual(sm.rps({3: 1.0}, 3), 0.0)
        self.assertGreater(sm.rps({3: 1.0}, 5), sm.rps({4: 0.5, 5: 0.5}, 5))

    def test_forecast_query_identities(self):
        fc = sm.Forecast.from_joint(sm.indep_joint(1.5, 1.1))
        q = fc.probs(total=2.0, line=-1.0, home_total=1.5)
        self.assertAlmostEqual(q["p_home_win"] + q["p_draw"] + q["p_away_win"], 1.0, places=9)
        self.assertAlmostEqual(q["p_over"] + q["p_push"] + q["p_under"], 1.0, places=9)
        self.assertAlmostEqual(q["p_home_cover"] + q["p_line_push"] + q["p_away_cover"], 1.0, places=9)
        self.assertAlmostEqual(q["p_home_cover"], sum(p for m, p in fc.margin.items() if m >= 2), places=9)
        self.assertAlmostEqual(q["mean_total"], 2.6, places=6)
        self.assertEqual(fc.probs(total=2.5)["p_push"], 0.0)

    def test_dixon_coles(self):
        j = sm.dixon_coles_joint(1.4, 1.1, -0.1)
        self.assertAlmostEqual(sum(j.values()), 1.0, places=12)
        self.assertGreater(j[(1, 1)], sm.indep_joint(1.4, 1.1)[(1, 1)] / sum(sm.indep_joint(1.4, 1.1).values()))
        with self.assertRaises(ValueError):
            sm.dixon_coles_joint(3.0, 3.0, 0.5)


class Goals(unittest.TestCase):
    def setUp(self):
        self.games = soccer_season()
        self.cfg = sm.config("epl")

    def test_ratings_recover_structure_and_phases_link(self):
        m = sm.GoalsModel(self.games, "2024-12-01", self.cfg)
        self.assertGreater(m.rt.A["T00"], m.rt.A["T11"])
        self.assertLess(m.rt.D["T00"], m.rt.D["T11"])
        self.assertGreater(m.rt.lh, 0)
        fc = m.a1("T00", "T11")
        self.assertGreater(fc.probs()["p_home_win"], 0.6)
        h1, h2 = fc.extra["h1"], fc.extra["h2"]
        self.assertAlmostEqual(sm.pmf_mean(h1.total) + sm.pmf_mean(h2.total), sm.pmf_mean(fc.total), places=6)
        mid = m.a1("T05", "T06")
        share = sm.pmf_mean(mid.extra["h1"].total) / sm.pmf_mean(mid.total)
        self.assertAlmostEqual(share, 0.44, delta=0.05)
        self.assertTrue(all(0.05 <= sm.pmf_mean(f.extra["h1"].total) / sm.pmf_mean(f.total) <= 0.95
                            for f in (fc, mid)))
        self.assertAlmostEqual(m.s_home, 0.44, delta=0.05)

    def test_leak_free_same_day_and_future(self):
        m1 = sm.GoalsModel(self.games, "2024-12-01", self.cfg)
        doctored = [dict(g, hs=g["hs"] + 9) if g["date"] >= "2024-12-01" else g for g in self.games]
        m2 = sm.GoalsModel(doctored, "2024-12-01", self.cfg)
        self.assertEqual(m1.rt.means("T03", "T07"), m2.rt.means("T03", "T07"))

    def test_rolling_validation_finds_signal(self):
        res = sm.validate_team(self.cfg, self.games, "2024-09-01", "2025-03-01", dc=True, boot=200)
        self.assertGreater(res["win_brier"]["n"], 100)
        self.assertLess(res["win_brier"]["a1_minus_a0"], 0)
        self.assertLess(res["result_rps3"]["a1_minus_a0"], 0)
        self.assertIn("h1_total_rps", res)
        self.assertIn("a1dc", res["result_rps3"])
        lo, hi = res["result_rps3"]["ci95_block"]
        self.assertLessEqual(lo, hi)


class Hockey(unittest.TestCase):
    def test_final_has_no_ties_and_regulation_route(self):
        games = hockey_season()
        m = sm.HockeyModel(games, "2026-02-01", sm.config("nhl"))
        fc = m.a1("H05", "H06")
        self.assertEqual(fc.margin.get(0, 0.0), 0.0)
        reg = fc.extra["reg"]
        self.assertGreater(reg.margin.get(0, 0.0), 0.15)
        self.assertAlmostEqual(sum(fc.margin.values()), 1.0, places=9)
        self.assertGreater(fc.probs()["p_home_win"], reg.probs()["p_home_win"])
        self.assertAlmostEqual(m.p_ot_decided, 0.62, delta=0.12)
        self.assertEqual(sm.reg_score({"hs": 4, "as": 3, "finish": "SO"}), (3, 3))
        res = sm.validate_team(sm.config("nhl"), games, "2025-12-15", "2026-04-01", boot=100)
        self.assertIn("reg_rps3", res)


class Points(unittest.TestCase):
    def test_key_numbers_and_ratings(self):
        games = gridiron_season()
        cfg = sm.config("nfl")
        m = sm.PointsModel(games, "2024-12-20", cfg)
        self.assertGreater(m.rt.o["G00"] + m.rt.d["G00"], m.rt.o["G15"] + m.rt.d["G15"])  # d: points kept out
        self.assertGreater(m.rt.hfa, 0)
        w = m.weight
        self.assertIsNotNone(w)
        self.assertGreater(w(7), 1.2)
        self.assertGreater(w(3), 1.0)
        self.assertLess(w(1), 1.0)
        fc = m.a1("G05", "G06")
        self.assertGreater(fc.margin.get(7, 0) + fc.margin.get(-7, 0), fc.margin.get(8, 0) + fc.margin.get(-8, 0))
        res = sm.validate_team(cfg, games, "2024-09-01", "2025-01-10", tb1_league="nfl", boot=100)
        self.assertLess(res["margin_rps"]["a1_minus_a0"], 0)
        self.assertIn("tb1", res["win_brier"])

    def test_basketball_has_no_draw_and_widths_come_from_residuals(self):
        games = hoops_season()
        cfg = sm.config("nba")
        eng = sm.TeamEngine(cfg, [g for g in games if g["date"] < "2026-02-20"])
        f0, f1 = eng.predict("B00", "B11", "2026-02-20")
        self.assertEqual(f1.margin.get(0, 0.0), 0.0)
        self.assertGreater(eng.book.margin and len(eng.book.margin), 50)
        self.assertLess(eng.model.sd_margin, eng.model.a0_sd_margin)   # A1 explains part of the spread
        self.assertGreater(f1.probs()["p_home_win"], 0.8)
        self.assertAlmostEqual(f0.probs()["p_home_win"] + f0.probs()["p_away_win"], 1.0, places=9)


class Baseball(unittest.TestCase):
    def test_tie_rate_is_kept_where_ties_exist(self):
        rng = random.Random(3)
        teams = [f"N{i}" for i in range(6)]
        games = []
        for day in range(120):
            d = (dt.date(2026, 4, 1) + dt.timedelta(days=day)).isoformat()
            for h, a in round_robin(teams, rng):
                hs, as_ = pois(rng, 4.1), pois(rng, 3.9)
                if hs == as_ and rng.random() < 0.8:
                    hs += 1
                games.append({"date": d, "home": h, "away": a, "hs": hs, "as": as_})
        m = sm.BaseballModel(games, "2026-07-20", sm.config("npb"))
        fc = m.a1("N0", "N1")
        self.assertAlmostEqual(fc.margin.get(0, 0.0), m.tie, places=6)
        self.assertGreater(m.tie, 0.02)
        mlb = sm.BaseballModel(games, "2026-07-20", sm.config("mlb-teamonly"))
        self.assertEqual(mlb.a1("N0", "N1").margin.get(0, 0.0), 0.0)


class Tennis(unittest.TestCase):
    def test_chain_identities(self):
        self.assertAlmostEqual(sm.hold_prob(0.5), 0.5, places=12)
        self.assertGreater(sm.hold_prob(0.64), 0.8)
        self.assertAlmostEqual(sm.tiebreak_prob(0.6, 0.6), 0.5, delta=0.02)
        self.assertAlmostEqual(sm.match_win_prob(0.64, 0.64, 3), 0.5, places=9)
        d = sm.match_distribution(0.66, 0.62, 5)
        self.assertAlmostEqual(sum(d.values()), 1.0, places=9)
        self.assertAlmostEqual(sum(p for (a, b, _, _), p in d.items() if a > b), sm.match_win_prob(0.66, 0.62, 5), places=9)
        self.assertGreater(sm.match_win_prob(0.66, 0.62, 5), sm.match_win_prob(0.66, 0.62, 3))
        tot = sm.tennis_forecast(sm.match_distribution(0.64, 0.64, 3)).total
        self.assertEqual(min(tot), 12)
        self.assertEqual(max(tot), 39)

    def test_serve_inversion(self):
        pa, pb = sm.serve_probs_for(0.73, 0.64, 3)
        self.assertAlmostEqual((pa + pb) / 2, 0.64, places=9)
        self.assertAlmostEqual(sm.match_win_prob(pa, pb, 3), 0.73, places=4)

    def test_score_parser(self):
        self.assertEqual(sm.parse_tennis_score("6-4 3-6 7-6(5)"),
                         {"games_w": 16, "games_l": 16, "sets_w": 2, "sets_l": 1, "complete": True})
        self.assertFalse(sm.parse_tennis_score("6-4 2-1 RET")["complete"])
        self.assertEqual(sm.parse_tennis_score("6-4 3-6 [10-8]")["games_w"], 10)
        self.assertIsNone(sm.parse_tennis_score("W/O"))

    def test_elo_learns_and_forecasts(self):
        cfg = sm.config("atp")
        elo = sm.TennisElo(cfg)
        rng = random.Random(1)
        for i in range(300):
            a, b = ("Strong", "Weak") if rng.random() < 0.5 else ("Weak", "Strong")
            w = "Strong" if rng.random() < 0.8 else "Weak"
            elo.update({"date": "2025-01-%02d" % (1 + i % 28), "winner": w, "loser": b if w == a else a,
                        "surface": "Clay", "best_of": 3, "complete": True, "total_games": 22, "serve_won": 120,
                        "serve_pts": 190})
        p0, g0, p1, f1 = elo.forecast("Strong", "Weak", "Clay", 3, "2025-03-01")
        self.assertGreater(p0, 0.65)
        self.assertAlmostEqual(f1.meta["p_a_win"], p1, places=3)
        self.assertIsNotNone(g0)
        self.assertAlmostEqual(elo.serve_avg("Clay", "2025-03-01"), (120 * 300 + 2000 * 0.62) / (190 * 300 + 2000), places=9)


class Cricket(unittest.TestCase):
    def match_json(self, i, bat, bowl, runs, winner, overs_faced=20, method=None):
        balls = [{"batter": "x", "bowler": "y", "runs": {"batter": 0, "extras": 0, "total": 0}}] * 6
        overs = [{"over": o, "deliveries": list(balls)} for o in range(overs_faced)]
        overs[0]["deliveries"][0] = {"batter": "x", "bowler": "y", "runs": {"batter": runs, "extras": 0, "total": runs}}
        outcome = {"winner": winner} if winner else {"result": "no result"}
        if method:
            outcome["method"] = method
        return {"info": {"dates": [f"2025-{1 + i // 28:02d}-{1 + i % 28:02d}"], "teams": [bat, bowl], "overs": 20,
                         "venue": "Ground A" if i % 2 else "Ground B", "outcome": outcome},
                "innings": [{"team": bat, "overs": overs}]}

    def test_cricsheet_parse_and_model(self):
        with tempfile.TemporaryDirectory() as tmp:
            rng = random.Random(4)
            for i in range(120):
                a, b = ("Kings", "Jets") if i % 2 else ("Jets", "Kings")
                runs = int(rng.gauss(180 if a == "Kings" else 150, 12)) + (15 if i % 2 else 0)
                win = "Kings" if rng.random() < 0.75 else "Jets"
                Path(tmp, f"{i}.json").write_text(json.dumps(self.match_json(i, a, b, runs, win)), encoding="utf-8")
            Path(tmp, "rain.json").write_text(json.dumps(self.match_json(3, "Kings", "Jets", 90, "Kings", 11, "D/L")),
                                              encoding="utf-8")
            ms = sd.load_cricsheet(tmp, 20)
        self.assertEqual(len(ms), 121)
        self.assertFalse(next(m for m in ms if m["first_innings_runs"] == 90)["first_innings_valid"])
        model = sm.CricketModel(sm.config("t20"))
        for m in ms:
            model.update(m)
        self.assertGreater(model.p_win("Kings", "Jets"), 0.6)
        f0, f1 = model.forecast("Kings", "Jets", "Ground A", "2025-12-31")
        self.assertGreater(sm.pmf_mean(f1.total), sm.pmf_mean(f0.total))
        f0b, f1b = model.forecast("Jets", "Kings", "Ground B", "2025-12-31")
        self.assertLess(sm.pmf_mean(f1b.total), sm.pmf_mean(f0b.total))


class DataAndShadow(unittest.TestCase):
    def test_espn_parse_strips_market_blocks(self):
        ev = {"id": "401", "date": "2026-01-10T20:00Z", "season": {"year": 2026},
              "competitions": [{"neutralSite": False, "odds": [{"details": "X -3"}],
                                "status": {"period": 4, "type": {"state": "post", "completed": True, "shortDetail": "Final/OT"}},
                                "competitors": [{"homeAway": "home", "score": "4", "team": {"displayName": "Home H"}},
                                                {"homeAway": "away", "score": "3", "team": {"displayName": "Away A"}}]}]}
        clean = sd._strip(ev)
        self.assertNotIn("odds", clean["competitions"][0])
        g = sd.parse_espn_event(clean, "hockey")
        self.assertEqual((g["hs"], g["as"], g["finish"], g["start_utc"]), (4, 3, "OT", "2026-01-10T20:00:00Z"))
        soccer = {"id": "9", "date": "2026-01-10T15:00Z", "competitions": [{"status": {"type": {"state": "post", "completed": True}},
                  "competitors": [{"homeAway": "home", "score": "2", "team": {"displayName": "A"}, "linescores": [{"value": 1}, {"value": 1}]},
                                  {"homeAway": "away", "score": "1", "team": {"displayName": "B"}, "linescores": [{"value": 0}, {"value": 1}]}]}]}
        g = sd.parse_espn_event(soccer, "goals")
        self.assertEqual((g["hs_ht"], g["as_ht"]), (1, 0))

    def test_csv_loader_and_name_matching(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp, "r.csv")
            p.write_text("date,home,away,home_score,away_score,neutral,finish\n2026-05-01,Yomiuri Giants,Hanshin Tigers,3,3,,\n"
                         "2026-05-02,Hanshin Tigers,Yomiuri Giants,,,,\n", encoding="utf-8")
            rows = sd.load_csv(str(p))
        self.assertEqual(len(rows), 1)
        self.assertEqual((rows[0]["hs"], rows[0]["finish"], rows[0]["neutral"]), (3, "REG", False))
        self.assertEqual(sd.match_name("hanshin", ["Yomiuri Giants", "Hanshin Tigers"]), "Hanshin Tigers")
        with self.assertRaises(SystemExit):
            sd.match_name("Tigers", ["Hanshin Tigers", "Detroit Tigers"])

    def test_shadow_row_and_score(self):
        cfg = sm.config("epl")
        m = sm.GoalsModel(soccer_season(), "2024-12-01", cfg)
        ev = {"id": "77", "date": "2024-12-01T15:00:00Z", "start_utc": "2024-12-01T15:00:00Z", "home": "T00", "away": "T09"}
        now = dt.datetime(2024, 12, 1, 12, tzinfo=dt.timezone.utc)
        row = sm.shadow_row(cfg, ev, m.a0(), m.a1("T00", "T09"), m.n, "P-600", 2.5, -0.5, now)
        with tempfile.TemporaryDirectory() as tmp:
            log, res = Path(tmp, "log.csv"), Path(tmp, "res.csv")
            sm.append_row(log, sm.LOG_FIELDS, row)
            sm.append_row(res, sm.RESULT_FIELDS, {"row_id": row["row_id"], "event_id": "77", "home_score": 3,
                                                  "away_score": 0, "finish": "REG", "settled_at_utc": "x", "source": "y"})
            s = sm.score_shadow(log, res)
        self.assertEqual(s["epl"]["home_win"]["n"], 1)
        self.assertLess(s["epl"]["home_win"]["a1_brier"], s["epl"]["home_win"]["a0_brier"])
        self.assertIn("total_over", s["epl"])
        self.assertIn("home_cover", s["epl"])

    def test_every_league_has_a_valid_config(self):
        for lg in sm.LEAGUES:
            cfg = sm.config(lg)
            self.assertIn(cfg["family"], sm.FAMILY_DEFAULTS)
            self.assertEqual(len(sm.params_sha(cfg)), 16)
        with self.assertRaises(SystemExit):
            sm.config("quidditch")


if __name__ == "__main__":
    unittest.main()
