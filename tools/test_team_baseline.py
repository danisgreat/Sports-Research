"""Offline tests for tools/team_baseline.py (TB-1, 2026-09-25(e)). No network."""
import random
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import team_baseline as tb  # noqa: E402


def season(n_rounds=12, seed=5, strengths=None, base=85.0, sd=11.0, home_edge=2.0):
    rng = random.Random(seed)
    teams = list(range(8))
    strengths = strengths or {t: (t - 3.5) * 2.0 for t in teams}
    games, day = [], 0
    for _ in range(n_rounds):
        order = teams[:]
        rng.shuffle(order)
        for i in range(0, len(order), 2):
            h, a = order[i], order[i + 1]
            hs = base + strengths[h] / 2 - strengths[a] / 2 + home_edge / 2 + rng.gauss(0, sd)
            as_ = base + strengths[a] / 2 - strengths[h] / 2 - home_edge / 2 + rng.gauss(0, sd)
            if round(hs) == round(as_):
                hs += 1
            games.append({"date": f"2026-01-{day // 4 + 1:02d}T00:00Z", "home": h, "away": a,
                          "hs": round(hs), "as": round(as_), "neutral": False})
            day += 1
    return games


class TestSeasonState(unittest.TestCase):
    def test_no_leak_and_ordering(self):
        gs = season()
        a, b = tb.SeasonState(k=5), tb.SeasonState(k=5)
        for g in gs[:40]:
            a.add(g)
            b.add(g)
        self.assertEqual(a.predict(7, 0), b.predict(7, 0))        # deterministic from the same history
        b.add(gs[40])
        self.assertNotEqual(a.predict(7, 0), b.predict(7, 0))     # only completed games move the ratings

    def test_strong_team_favoured(self):
        st = tb.SeasonState(k=5)
        for g in season(n_rounds=20):
            st.add(g)
        p = st.predict(7, 0)          # strongest at home v weakest
        self.assertGreater(p["margin"], 5)
        self.assertLess(st.predict(0, 7)["margin"], 0)
        self.assertAlmostEqual(st.league_total_mean(), 170, delta=6)

    def test_shrinkage(self):
        gs = season(n_rounds=2)
        raw, shrunk = tb.SeasonState(k=0), tb.SeasonState(k=50)
        for g in gs:
            raw.add(g)
            shrunk.add(g)
        self.assertLess(abs(shrunk.predict(7, 0)["margin"] - shrunk.home_edge()),
                        abs(raw.predict(7, 0)["margin"] - raw.home_edge()))

    def test_carry_over(self):
        prev = tb.SeasonState(k=5)
        for g in season(n_rounds=20):
            prev.add(g)
        prior = prev.final_ratings()
        cur = tb.SeasonState(prior=prior, k=5, carry=0.75)
        cold = tb.SeasonState(k=5)
        for g in season(n_rounds=1, seed=9)[:10]:
            cur.add(g)
            cold.add(g)
        self.assertGreater(cur.predict(7, 0)["margin"], cold.predict(7, 0)["margin"])

    def test_margin_share(self):
        st = tb.SeasonState()
        for i in range(40):
            st.add({"date": f"d{i:03d}", "home": "A", "away": "B", "hs": 3 if i % 4 else 5, "as": 2, "neutral": False})
        self.assertAlmostEqual(st.abs_margin_share(2), 0.25)


class TestContractProbs(unittest.TestCase):
    def test_basketball_coherent(self):
        pr = tb.contract_probs("nba", {"total": 220.0, "margin": 4.0}, 15.0, 19.0, total_line=219.5, home_line=-3.5)
        self.assertAlmostEqual(pr["home_win"] + pr["away_win"], 1.0, places=9)
        self.assertAlmostEqual(pr["over_219.5"] + pr["under_219.5"] + pr["push_219.5"], 1.0, places=6)
        self.assertLessEqual(pr["home_-3.5"], pr["home_win"])
        self.assertGreater(pr["over_219.5"], 0.5)

    def test_baseball_plus_one_point_five(self):
        st = tb.SeasonState()
        for i in range(100):   # 28 of 100 one-run games
            st.add({"date": f"d{i:03d}", "home": "A", "away": "B", "hs": 5 if i >= 28 else 4, "as": 3, "neutral": False})
        pr = tb.contract_probs("mlb", {"total": 9.0, "margin": 0.1}, 4.57, 4.5, total_line=8.5, home_line=-1.5, state=st)
        self.assertAlmostEqual(pr["home_-1.5"], pr["home_win"] * 0.72, places=6)
        self.assertGreater(pr["away_+1.5"], 0.6)

    def test_soccer_three_way(self):
        pr = tb.contract_probs("epl", {"total": 2.8, "margin": 0.3}, 1.5, 1.6, total_line=2.5)
        self.assertAlmostEqual(pr["home_win"] + pr["draw"] + pr["away_win"], 1.0, places=6)
        self.assertGreater(pr["draw"], 0.15)

    def test_team_matching(self):
        teams = {"1": {"displayName": "Brisbane Bullets", "location": "Brisbane"},
                 "2": {"displayName": "Illawarra Hawks", "location": "Illawarra"}}
        self.assertEqual(tb.match_team("Brisbane Bullets", teams), "1")
        self.assertEqual(tb.match_team("Illawarra", teams), "2")
        with self.assertRaises(ValueError):
            tb.match_team("Perth Wildcats", teams)


if __name__ == "__main__":
    unittest.main()
