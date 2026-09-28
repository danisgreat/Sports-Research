"""Reference home edges (mean home margin, non-neutral games) and league scoring per season, for the
TB-1-MD table in PROBABILITY_TOOLKIT.md. Same cached seasons as validate_tb1_md.py. Writes home_edges.json."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "research", "team_baseline_2026-09-25e"))
import validate_team_baseline as vtb  # noqa: E402


def stats(games):
    ng = [g for g in games if not g["neutral"]]
    he = sum(g["hs"] - g["as"] for g in ng) / len(ng)
    hw = sum(1 for g in ng if g["hs"] > g["as"]) / len(ng)
    tot = sum(g["hs"] + g["as"] for g in games) / len(games)
    return {"games": len(games), "home_edge": round(he, 2), "home_win_rate": round(hw, 3), "mean_total": round(tot, 2)}


out = {}
chains = {lg: vtb.load_chain(lg) for lg in vtb.CHAINS}
chains["MLB"] = vtb.load_mlb()
for lg, seasons in chains.items():
    labels = vtb.CHAINS.get(lg, ["MLB 2026"])
    out[lg] = {lab: stats(s) for lab, s in zip(labels, seasons)}
    allg = [g for s in seasons for g in s]
    out[lg]["pooled"] = stats(allg)
    print(lg, json.dumps(out[lg]))
json.dump(out, open(os.path.join(HERE, "home_edges.json"), "w"), indent=2)
