"""One model per sport, tested on held-out competitions (POOLED-v1, CR-2026.11.11-R1).

The owner asks about far too many competitions for anything per league, so a sport gets ONE recipe whose settings are chosen
on some competitions and judged on others it never saw. This module runs that test for soccer on the open bulk history
(research/bulk_history/soccer/MATCHES.csv) and writes the decision, the per-competition width floors and the parameter rows.

    python -m ml pooled soccer --out NEW_FOLDER

The recipe is the repository's own season-to-date reference: attack and defence rates shrunk toward the league mean with
k, a home edge, and a Poisson score grid. It compares, on identical games:

    AVERAGE    TB-1-MD as used today for goal leagues (each side's goals = mean of own attack and opponent defence)
    ADDITIVE   TB-2-MD (own attack + opponent defence - league mean), the form that fixed the NBA reference's slope
    rho        the Dixon-Coles low-score correction, in {0, -0.05, -0.10}

DECISION RULE (registered here before any result was read): competitions are split alphabetically-by-hash into a tuning half
and a held-out half. Settings (form, k, rho, home edge) are chosen on the tuning half by mean three-way Brier. A change from
the current reference (AVERAGE, k = 2, rho = 0) is adopted only if, on the held-out half, its paired mean difference in
three-way Brier is below zero with a 95% competition-block bootstrap interval entirely below zero AND its Over/Under 2.5
log loss is not worse (interval upper bound <= 0.001). Otherwise the current reference stays. Matches before each team has
played three league games, and each season's first 30 league games, are scored but excluded from the decision.

Captured today means known today: this is development evidence on current-capture open data, never a claim about what was
known before any past card.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import math
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
MATCHES = ROOT / "research" / "bulk_history" / "soccer" / "MATCHES.csv"
CURRENT = dict(form="average", k=2.0, rho=0.0)
FORMS = ("average", "additive")
KS = (2.0, 5.0, 10.0)
RHOS = (0.0, -0.05, -0.10)
MIN_TEAM_GAMES = 3
SEASON_WARMUP = 30
MIN_COMPETITION_GAMES = 300


def _rows(path=MATCHES) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def split(competition: str) -> str:
    """Deterministic tuning/held-out assignment that no one chose by looking at results."""
    return "TUNE" if int(hashlib.sha256(competition.encode()).hexdigest(), 16) % 2 == 0 else "HELD_OUT"


def _poisson_probs(lh: float, la: float, rho: float, top: int = 15):
    k = np.arange(top + 1)
    g = np.outer(stats.poisson.pmf(k, lh), stats.poisson.pmf(k, la))
    if rho:
        lo, hi = max(-1 / lh, -1 / la), min(1 / (lh * la), 1.0)
        r = min(max(rho, 0.99 * lo), 0.99 * hi)
        g[0, 0] *= 1 - lh * la * r
        g[0, 1] *= 1 + lh * r
        g[1, 0] *= 1 + la * r
        g[1, 1] *= 1 - r
    g /= g.sum()
    m = k[:, None] - k[None, :]
    t = k[:, None] + k[None, :]
    return float(g[m > 0].sum()), float(g[m == 0].sum()), float(g[m < 0].sum()), float(g[t >= 3].sum()), g


def walk_forward(rows: list[dict], form: str, k: float, rho: float, home_edge: float | None = None) -> list[dict]:
    """Season-to-date predictions for every match, from earlier matches of the same competition and season only."""
    out = []
    by = defaultdict(list)
    for r in rows:
        by[(r["competition"], r["season"])].append(r)
    for (comp, season), games in by.items():
        games.sort(key=lambda r: (r["date"], r["home"]))
        stat = defaultdict(lambda: [0.0, 0.0, 0])          # goals for, goals against, games
        league_goals = league_games = 0.0
        home_margin_sum = 0.0
        played = 0
        i = 0
        while i < len(games):
            day = games[i]["date"]
            todays = []
            while i < len(games) and games[i]["date"] == day:
                todays.append(games[i])
                i += 1
            lm = league_goals / league_games if league_games else 1.35
            # the league's season-to-date home margin, shrunk toward 0.3 goals with the weight of 50 games
            he = home_edge if home_edge is not None else (home_margin_sum + 50 * 0.3) / (played + 50)
            for g in todays:                                # same-day games never see each other
                h, a = stat[g["home"]], stat[g["away"]]
                rate = lambda s, x: (s[x] + k * lm) / (s[2] + k)
                oh, dh, oa, da = rate(h, 0), rate(h, 1), rate(a, 0), rate(a, 1)
                if form == "average":
                    total = (oh + da) / 2 + (oa + dh) / 2
                    margin = ((oh - dh) - (oa - da)) / 2 + he
                else:
                    total = (oh + da - lm) + (oa + dh - lm)
                    margin = (oh - dh) - (oa - da) + he
                lh, la = max((total + margin) / 2, 0.05), max((total - margin) / 2, 0.05)
                ph, pd, pa, po, grid = _poisson_probs(lh, la, rho)
                fh, fa = int(g["ft_home"]), int(g["ft_away"])
                out.append(dict(competition=comp, season=season, date=day, home=g["home"], away=g["away"], fh=fh, fa=fa,
                                ph=ph, pd=pd, pa=pa, p_over25=po, exp_total=total, exp_margin=margin,
                                eligible=min(h[2], a[2]) >= MIN_TEAM_GAMES and played >= SEASON_WARMUP, split=split(comp)))
            for g in todays:
                fh, fa = int(g["ft_home"]), int(g["ft_away"])
                stat[g["home"]][0] += fh; stat[g["home"]][1] += fa; stat[g["home"]][2] += 1
                stat[g["away"]][0] += fa; stat[g["away"]][1] += fh; stat[g["away"]][2] += 1
                league_goals += fh + fa
                league_games += 2
                home_margin_sum += fh - fa
                played += 1
    return out


def scores(preds: list[dict]) -> np.ndarray:
    """Per match: three-way Brier (sum over outcomes) and Over/Under 2.5 log loss."""
    out = np.zeros((len(preds), 2))
    for i, p in enumerate(preds):
        y = (1.0 if p["fh"] > p["fa"] else 0.0, 1.0 if p["fh"] == p["fa"] else 0.0, 1.0 if p["fh"] < p["fa"] else 0.0)
        out[i, 0] = (p["ph"] - y[0]) ** 2 + (p["pd"] - y[1]) ** 2 + (p["pa"] - y[2]) ** 2
        over = p["fh"] + p["fa"] >= 3
        q = min(max(p["p_over25"], 1e-9), 1 - 1e-9)
        out[i, 1] = -math.log(q if over else 1 - q)
    return out


def block_interval(diff: np.ndarray, groups: list[str], reps: int = 2000, seed: int = 20261111) -> tuple[float, float, float]:
    """Mean paired difference with a 95% bootstrap interval resampling whole competitions (games inside one are dependent)."""
    g = np.random.default_rng(seed)
    names = sorted(set(groups))
    idx = {n: np.flatnonzero(np.array(groups) == n) for n in names}
    means = []
    for _ in range(reps):
        pick = g.choice(names, len(names), replace=True)
        rows = np.concatenate([idx[n] for n in pick])
        means.append(diff[rows].mean())
    return float(diff.mean()), float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def study(rows: list[dict] | None = None) -> dict:
    rows = rows if rows is not None else _rows()
    counts = defaultdict(int)
    for r in rows:
        counts[r["competition"]] += 1
    rows = [r for r in rows if counts[r["competition"]] >= MIN_COMPETITION_GAMES]
    settings = [dict(form=f, k=k, rho=r) for f in FORMS for k in KS for r in RHOS]
    results = {}
    for s in settings:
        preds = walk_forward(rows, s["form"], s["k"], s["rho"])
        results[(s["form"], s["k"], s["rho"])] = (preds, scores(preds))
    base_preds = results[(CURRENT["form"], CURRENT["k"], CURRENT["rho"])][0]
    elig = np.array([p["eligible"] for p in base_preds])
    tune = np.array([p["split"] == "TUNE" for p in base_preds]) & elig
    held = np.array([p["split"] == "HELD_OUT" for p in base_preds]) & elig
    table = []
    for key, (preds, sc) in results.items():
        table.append(dict(form=key[0], k=key[1], rho=key[2], tune_brier3=float(sc[tune, 0].mean()), tune_logloss_ou25=float(sc[tune, 1].mean()),
                          held_brier3=float(sc[held, 0].mean()), held_logloss_ou25=float(sc[held, 1].mean())))
    best = min(table, key=lambda t: t["tune_brier3"])
    best_key = (best["form"], best["k"], best["rho"])
    base_sc = results[(CURRENT["form"], CURRENT["k"], CURRENT["rho"])][1]
    best_sc = results[best_key][1]
    groups = [p["competition"] for p, h in zip(base_preds, held) if h]
    d_brier = block_interval(best_sc[held, 0] - base_sc[held, 0], groups)
    d_ll = block_interval(best_sc[held, 1] - base_sc[held, 1], groups)
    adopt = best_key != (CURRENT["form"], CURRENT["k"], CURRENT["rho"]) and d_brier[2] < 0 and d_ll[2] <= 0.001
    # separate, pre-declared single-factor contrasts on the held-out half (reported whatever the decision)
    contrasts = {}
    for name, key in (("ADDITIVE_k2_rho0", ("additive", 2.0, 0.0)), ("AVERAGE_k2_rho-0.05", ("average", 2.0, -0.05)),
                      ("AVERAGE_k2_rho-0.10", ("average", 2.0, -0.10))):
        sc = results[key][1]
        contrasts[name] = dict(brier3=block_interval(sc[held, 0] - base_sc[held, 0], groups),
                               logloss_ou25=block_interval(sc[held, 1] - base_sc[held, 1], groups))
    chosen = best_key if adopt else (CURRENT["form"], CURRENT["k"], CURRENT["rho"])
    return dict(table=table, best=best, adopt=adopt, chosen=chosen, d_brier=d_brier, d_ll=d_ll, contrasts=contrasts,
                n_tune=int(tune.sum()), n_held=int(held.sum()), tune_comps=sorted({p["competition"] for p, t in zip(base_preds, tune) if t}),
                held_comps=sorted(set(groups)), preds=results[chosen][0])


def competition_rows(rows: list[dict], preds: list[dict]) -> list[dict]:
    """Per competition: league numbers, first-half share and the width floors (residual SDs of the chosen reference)."""
    out = []
    by = defaultdict(list)
    for r in rows:
        by[r["competition"]].append(r)
    pred_by = defaultdict(list)
    for p in preds:
        if p["eligible"]:
            pred_by[p["competition"]].append(p)
    for comp, games in sorted(by.items()):
        fh = np.array([int(g["ft_home"]) for g in games], float)
        fa = np.array([int(g["ft_away"]) for g in games], float)
        ht = [g for g in games if g["ht_home"] != "" and g["ht_away"] != ""]
        ht_goals = sum(int(g["ht_home"]) + int(g["ht_away"]) for g in ht)
        ft_goals_ht = sum(int(g["ft_home"]) + int(g["ft_away"]) for g in ht)
        ps = pred_by.get(comp, [])
        resid_m = np.array([(p["fh"] - p["fa"]) - p["exp_margin"] for p in ps])
        resid_t = np.array([(p["fh"] + p["fa"]) - p["exp_total"] for p in ps])
        # z: residual over the model's own Poisson SD (margin and total both have variance lambda_home + lambda_away)
        model_sd = np.array([math.sqrt(max(p["exp_total"], 0.1)) for p in ps])
        z_m = resid_m / model_sd if len(ps) else np.array([])
        z_t = resid_t / model_sd if len(ps) else np.array([])
        seasons = sorted({g["season"] for g in games})
        dates = sorted(g["date"] for g in games)
        out.append(dict(
            competition=comp, n_games=len(games), seasons=",".join(seasons), first_date=dates[0], last_date=dates[-1],
            mean_total=round(float((fh + fa).mean()), 4), mean_home_margin=round(float((fh - fa).mean()), 4),
            home_win_rate=round(float((fh > fa).mean()), 4), draw_rate=round(float((fh == fa).mean()), 4),
            raw_margin_sd=round(float((fh - fa).std(ddof=1)), 4), raw_total_sd=round(float((fh + fa).std(ddof=1)), 4),
            resid_margin_sd=round(float(resid_m.std(ddof=1)), 4) if len(ps) >= 30 else "",
            resid_total_sd=round(float(resid_t.std(ddof=1)), 4) if len(ps) >= 30 else "",
            z_margin_sd=round(float(z_m.std(ddof=1)), 3) if len(ps) >= 30 else "", z_total_sd=round(float(z_t.std(ddof=1)), 3) if len(ps) >= 30 else "",
            n_scored=len(ps), first_half_share=round(ht_goals / ft_goals_ht, 4) if ft_goals_ht else "", n_half_time=len(ht)))
    return out


def _csv(rows: list[dict]) -> bytes:
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=list(rows[0]), lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue().encode("utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="sport", required=True)
    so = sub.add_parser("soccer")
    so.add_argument("--out", type=Path, required=True)
    so.add_argument("--matches", type=Path, default=MATCHES)
    args = parser.parse_args(argv)
    rows = _rows(args.matches)
    res = study(rows)
    args.out.mkdir(parents=True, exist_ok=False)
    (args.out / "SETTINGS_TABLE.csv").write_bytes(_csv(res["table"]))
    comp = competition_rows([r for r in rows], res["preds"])
    (args.out / "COMPETITION_ROWS.csv").write_bytes(_csv(comp))
    summary = [dict(item="matches_file_sha256", value=hashlib.sha256(Path(args.matches).read_bytes()).hexdigest()),
               dict(item="tuning_competitions", value="; ".join(res["tune_comps"])),
               dict(item="held_out_competitions", value="; ".join(res["held_comps"])),
               dict(item="n_tune_scored", value=res["n_tune"]), dict(item="n_held_out_scored", value=res["n_held"]),
               dict(item="best_on_tuning", value=f"{res['best']['form']} k={res['best']['k']} rho={res['best']['rho']}"),
               dict(item="held_out_brier3_diff_vs_current", value="%.5f [%.5f, %.5f]" % res["d_brier"]),
               dict(item="held_out_logloss_ou25_diff_vs_current", value="%.5f [%.5f, %.5f]" % res["d_ll"]),
               dict(item="decision", value=("ADOPT " if res["adopt"] else "KEEP_CURRENT ") + "%s k=%s rho=%s" % res["chosen"])]
    for name, c in res["contrasts"].items():
        summary.append(dict(item=f"contrast_{name}_brier3", value="%.5f [%.5f, %.5f]" % c["brier3"]))
        summary.append(dict(item=f"contrast_{name}_logloss_ou25", value="%.5f [%.5f, %.5f]" % c["logloss_ou25"]))
    (args.out / "DECISION.csv").write_bytes(_csv(summary))
    for s in summary:
        print(s["item"], "=", s["value"])


if __name__ == "__main__":
    main()
