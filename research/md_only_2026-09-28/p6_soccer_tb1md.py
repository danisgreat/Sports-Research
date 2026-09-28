"""P6 (preregistered in PREREGISTRATION_P6.md) — TB-1-MD resolution in the top five soccer leagues."""
import datetime as dt
import json
import math
import os
import random
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "research", "sport_models_2026-09-26"))
import validate_public as vp  # noqa: E402

K = 2
LEAGUES = ["epl", "laliga", "bundesliga", "seriea", "ligue1"]
SCORED = [2021, 2022, 2023, 2024, 2025]
BOOT, SEED = 2000, 20260928


def pois(k, lam):
    return math.exp(-lam + k * math.log(lam) - math.lgamma(k + 1))


def probs(lh, la):
    lh, la = max(lh, 0.05), max(la, 0.05)
    ph = sum(pois(i, lh) * pois(j, la) for i in range(15) for j in range(i))
    pd = sum(pois(i, lh) * pois(i, la) for i in range(15))
    mu = lh + la
    po = 1 - sum(pois(k, mu) for k in range(3))
    return ph, pd, 1 - ph - pd, po


def season_rows(games, he):
    pf, pa, n = defaultdict(float), defaultdict(float), defaultdict(int)
    pts, gp = 0.0, 0
    hw = dr = aw = ov = tot = 0
    rows = []
    for g in sorted(games, key=lambda x: x["date"]):
        h, a = g["home"], g["away"]
        if n[h] >= 1 and n[a] >= 1 and tot >= 10:
            lm = pts / gp
            oh, dh = (pf[h] + K * lm) / (n[h] + K), (pa[h] + K * lm) / (n[h] + K)
            oa, da = (pf[a] + K * lm) / (n[a] + K), (pa[a] + K * lm) / (n[a] + K)
            t = (oh + da) / 2 + (oa + dh) / 2
            m = ((oh - dh) - (oa - da)) / 2 + he
            ph, pd, pa_, po = probs((t + m) / 2, (t - m) / 2)
            bh, bd, ba, bo = hw / tot, dr / tot, aw / tot, ov / tot
            yh, yd, ya = int(g["hs"] > g["as"]), int(g["hs"] == g["as"]), int(g["hs"] < g["as"])
            yo = int(g["hs"] + g["as"] >= 3)
            rows.append({"week": str(dt.date.fromisoformat(g["date"][:10]).isocalendar()[:2]), "season": g["season"],
                         "r3_md": (ph - yh) ** 2 + (pd - yd) ** 2 + (pa_ - ya) ** 2,
                         "r3_pop": (bh - yh) ** 2 + (bd - yd) ** 2 + (ba - ya) ** 2,
                         "o_md": (po - yo) ** 2, "o_pop": (bo - yo) ** 2,
                         "h_md": (ph - yh) ** 2, "h_pop": (bh - yh) ** 2})
        pf[h] += g["hs"]; pa[h] += g["as"]; pf[a] += g["as"]; pa[a] += g["hs"]
        n[h] += 1; n[a] += 1; pts += g["hs"] + g["as"]; gp += 2
        tot += 1; hw += g["hs"] > g["as"]; dr += g["hs"] == g["as"]; aw += g["hs"] < g["as"]
        ov += g["hs"] + g["as"] >= 3
    return rows


def boot(rows, a, b):
    blocks = defaultdict(list)
    for r in rows:
        blocks[(r["season"], r["week"])].append(r[a] - r[b])
    keys = list(blocks)
    tot = sum(len(v) for v in blocks.values())
    mean = sum(sum(v) for v in blocks.values()) / tot
    rng = random.Random(SEED)
    st = []
    for _ in range(BOOT):
        s = [blocks[rng.choice(keys)] for _ in keys]
        st.append(sum(sum(v) for v in s) / sum(len(v) for v in s))
    st.sort()
    return {"mean": round(mean, 5), "ci95": [round(st[int(0.025 * BOOT)], 5), round(st[int(0.975 * BOOT) - 1], 5)], "n": tot}


def main():
    out = {"preregistration": "PREREGISTRATION_P6.md", "k": K}
    for lg in LEAGUES:
        games = vp.soccer(lg)
        by = defaultdict(list)
        for g in games:
            by[g["season"]].append(g)
        rows, per = [], {}
        for s in SCORED:
            prev = by.get(s - 1, [])
            if not prev or not by.get(s):
                continue
            he = sum(g["hs"] - g["as"] for g in prev) / len(prev)
            r = season_rows(by[s], he)
            rows += r
            mean = lambda k: sum(x[k] for x in r) / len(r)  # noqa: E731
            per[str(s)] = {"n": len(r), "he": round(he, 3), "r3_diff": round(mean("r3_md") - mean("r3_pop"), 5),
                           "o_diff": round(mean("o_md") - mean("o_pop"), 5), "h_diff": round(mean("h_md") - mean("h_pop"), 5)}
        res = {"per_season": per, "r3": boot(rows, "r3_md", "r3_pop"), "over25": boot(rows, "o_md", "o_pop"),
               "home": boot(rows, "h_md", "h_pop")}
        for key, dk in (("r3", "r3_diff"), ("over25", "o_diff")):
            neg = sum(1 for v in per.values() if v[dk] < 0)
            res[key]["seasons_below_0"] = f"{neg}/{len(per)}"
            res[key]["verdict"] = "RESOLUTION" if res[key]["ci95"][1] < 0 and neg >= 4 else "NO RESOLUTION"
        out[lg] = res
        print(lg, json.dumps({k: res[k] for k in ("r3", "over25", "home")}), flush=True)
    json.dump(out, open(os.path.join(HERE, "p6_soccer_tb1md.json"), "w"), indent=2)


if __name__ == "__main__":
    main()
