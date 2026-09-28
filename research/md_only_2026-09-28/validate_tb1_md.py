"""Does the hand-computable TB-1 (TB-1-MD, PROBABILITY_TOOLKIT.md §4) score like the tool's TB-1?

Why. From 2026-09-28 the forecasting model reads Markdown only and cannot run tools/team_baseline.py.
TB-1-MD is the same rating arithmetic done by hand from a standings page, with three simplifications:
1. the width is the league's fixed reference SD (the tool switches to a running residual SD after 20 games);
2. the home edge is a fixed reference (the previous season's mean home margin where one exists);
3. z is rounded to two decimals (a Phi-table lookup), and no previous-season carry-over is used.
This script scores both on the same games, leak-free (each game from games strictly before it), against
the running population rate A0. Brier on P(home win) and on P(total > running league mean).
Week-block 95% intervals for TB1MD - TB1 and TB1MD - A0. Writes validate_tb1_md.json.
"""
import datetime as dt
import json
import math
import os
import random
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "research", "team_baseline_2026-09-25e"))
import validate_team_baseline as vtb  # noqa: E402  (chdirs into the base-rate folder)

tb = vtb.tb
TOOL = {lg: tb.LEAGUES[lg.lower()] for lg in ("NBA", "WNBA", "NBL", "NHL", "EPL", "MLB", "NFL", "AFL", "NRL")}


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def phi_table(z):
    z = max(-3.49, min(3.49, round(z, 2)))
    return phi(z)


def md_ratings(pf, pa, n, lm, k):
    if n + k == 0:
        return lm, lm
    return (pf + k * lm) / (n + k), (pa + k * lm) / (n + k)


def season_rows(games, k_tool, r_tool, kind, sd_m_ref, sd_t_ref, he_ref, k_md):
    """Walk one season. Returns per-game rows with tool TB-1, TB-1-MD and A0 probabilities."""
    state = tb.SeasonState(prior=None, k=k_tool, carry=r_tool, sd_total=sd_t_ref, sd_margin=sd_m_ref)
    pf, pa, n = defaultdict(float), defaultdict(float), defaultdict(int)
    tot_pts, tot_gp = 0.0, 0
    rows = []
    for g in sorted(games, key=lambda x: x["date"]):
        h, a = g["home"], g["away"]
        if min(state.n_games(h), state.n_games(a)) >= 1 and state.n_league_games() >= 10:
            pred = state.predict(h, a, neutral=g["neutral"])
            sd_m, sd_t = state.resid_sd()
            ref_total = state.league_total_mean()
            lm = tot_pts / tot_gp
            oh, dh = md_ratings(pf[h], pa[h], n[h], lm, k_md)
            oa, da = md_ratings(pf[a], pa[a], n[a], lm, k_md)
            t_md = (oh + da) / 2 + (oa + dh) / 2
            m_md = ((oh - dh) - (oa - da)) / 2 + (0.0 if g["neutral"] else he_ref)
            if kind == "poisson":
                lh, la = tb.team_means(pred["total"], pred["margin"])
                p_tool = tb.poisson_win(lh, la)
                o_tool = tb.poisson_total_over(lh + la, ref_total)
                lh2, la2 = tb.team_means(t_md, m_md)
                p_md = tb.poisson_win(round(lh2, 1), round(la2, 1))     # a 0.1-step Poisson table
                o_md = tb.poisson_total_over(round(lh2 + la2, 1), ref_total)
            else:
                p_tool = phi(pred["margin"] / sd_m)
                o_tool = 1 - phi((ref_total - pred["total"]) / sd_t)
                p_md = phi_table(m_md / sd_m_ref)
                o_md = 1 - phi_table((ref_total - t_md) / sd_t_ref)
            y = 1 if g["hs"] > g["as"] else 0
            yo = 1 if g["hs"] + g["as"] > ref_total else 0
            rows.append({"week": str(dt.date.fromisoformat(g["date"][:10]).isocalendar()[:2]),
                         "bh_tool": (p_tool - y) ** 2, "bh_md": (p_md - y) ** 2,
                         "bh_a0": (state.home_win_rate() - y) ** 2,
                         "bo_tool": (o_tool - yo) ** 2, "bo_md": (o_md - yo) ** 2,
                         "bo_a0": (state.over_rate() - yo) ** 2,
                         "p_md": p_md, "y": y, "p_tool": p_tool})
        state.add(g)
        pf[h] += g["hs"]; pa[h] += g["as"]; pf[a] += g["as"]; pa[a] += g["hs"]
        n[h] += 1; n[a] += 1
        tot_pts += g["hs"] + g["as"]; tot_gp += 2
    return rows


def home_edge(games):
    ed = [g["hs"] - g["as"] for g in games if not g["neutral"]]
    return sum(ed) / len(ed)


def boot(rows, a, b, n=2000, seed=20260928):
    blocks = defaultdict(list)
    for r in rows:
        blocks[r["week"]].append(r[a] - r[b])
    keys = list(blocks)
    tot = sum(len(v) for v in blocks.values())
    mean = sum(sum(v) for v in blocks.values()) / tot
    rng = random.Random(seed)
    st = []
    for _ in range(n):
        s = [blocks[rng.choice(keys)] for _ in keys]
        st.append(sum(sum(v) for v in s) / sum(len(v) for v in s))
    st.sort()
    return {"mean": round(mean, 5), "ci95": [round(st[int(0.025 * n)], 5), round(st[int(0.975 * n) - 1], 5)], "n": tot}


def main():
    out = {}
    chains = {lg: vtb.load_chain(lg) for lg in vtb.CHAINS}
    chains["MLB"] = vtb.load_mlb()
    for lg, seasons in chains.items():
        cfg = TOOL[lg]
        kind = "poisson" if cfg["kind"] == "poisson" else "normal"
        rows, he_used = [], []
        for i, s in enumerate(seasons):
            if len(seasons) > 1 and i == 0:
                continue                      # the first season only supplies the reference home edge
            he_ref = home_edge(seasons[i - 1]) if i > 0 else home_edge(s)   # single-season chains: in-sample
            he_used.append(round(he_ref, 3))
            rows += season_rows(s, cfg["k"], 0.0, kind, cfg["sd_margin"], cfg["sd_total"], he_ref, cfg["k"])
        mean = lambda key: round(sum(r[key] for r in rows) / len(rows), 4)  # noqa: E731
        maxdiff = max(abs(r["p_md"] - r["p_tool"]) for r in rows)
        out[lg] = {"seasons_scored": vtb.CHAINS.get(lg, ["MLB 2026"])[1 if len(seasons) > 1 else 0:],
                   "home_edge_ref": he_used, "home_edge_source": "previous season" if len(seasons) > 1 else "same season (in-sample)",
                   "k": cfg["k"], "sd_margin": cfg["sd_margin"], "sd_total": cfg["sd_total"], "n": len(rows),
                   "brier_home": {"tb1_tool": mean("bh_tool"), "tb1_md": mean("bh_md"), "a0": mean("bh_a0")},
                   "brier_over": {"tb1_tool": mean("bo_tool"), "tb1_md": mean("bo_md"), "a0": mean("bo_a0")},
                   "home_md_minus_tool": boot(rows, "bh_md", "bh_tool"), "home_md_minus_a0": boot(rows, "bh_md", "bh_a0"),
                   "over_md_minus_tool": boot(rows, "bo_md", "bo_tool"), "over_md_minus_a0": boot(rows, "bo_md", "bo_a0"),
                   "max_abs_p_home_gap": round(maxdiff, 4)}
        print(lg, json.dumps(out[lg]), flush=True)
    json.dump(out, open(os.path.join(HERE, "validate_tb1_md.json"), "w"), indent=2)


if __name__ == "__main__":
    main()
