"""Do the PRD-07 regime multipliers improve the NBA totals forecast?  Walk-forward replication of the declared NBA reference
(TB-2-MD additive, ml.reference constants), with each game's standings built only from verified finals dated before it.

Data: research/verified_history/2026-10-17-nba (CANONICAL_EVENTS CORROBORATED_FINAL, scores from OWNER_RESULTS).
Test seasons 2020-21 .. 2025-26; 2019-20 supplies only the first prior-season league mean.
Scores: bias (actual - forecast), RMSE, CRPS and log score of the reference's own normal total (sd_total 19.4), and
Brier of P(over) at the reference's own centre rounded to the nearest .5 plus and minus 4 points (lines the model did not
choose after the fact). Paired differences are bootstrapped by season-week blocks.
Run from the repository root:  python <this file> OUTDIR
"""
import csv
import math
import random
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))
from ml.reference import TB1_MD, LM_PRIOR_WEIGHT  # noqa: E402

P = Path("research/verified_history/2026-10-17-nba")
OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
SPEC = TB1_MD["NBA"]
K, HE, SD = SPEC["k"], SPEC["he"], SPEC["sd_total"]
MULT = {"EARLY_SEASON": 0.988, "FINALS_COMPRESSION": 0.970}


def load():
    can = {r["event_key"]: r for r in csv.DictReader(open(P / "CANONICAL_EVENTS.csv", encoding="utf-8"))
           if r["result_disposition"] == "CORROBORATED_FINAL" and r["stage"] in ("REGULAR", "PLAYOFFS", "PLAY_IN")}
    own = {r["event_key"]: r for r in csv.DictReader(open(P / "OWNER_RESULTS.csv", encoding="utf-8"))}
    games = []
    for k, c in can.items():
        o = own.get(k)
        if not o or not o["home_score"]:
            continue
        games.append(dict(key=k, season=c["season"], stage=c["stage"], d=date.fromisoformat(o["event_date"]),
                          start=c["scheduled_start_utc"], home=c["home"], away=c["away"],
                          neutral=c["neutral_flag"] == "1", hs=int(o["home_score"]), as_=int(o["away_score"])))
    games.sort(key=lambda g: (g["start"], g["key"]))
    return games


def centre(st, home, away, lm, neutral):
    def rate(t, key):
        return (st[t][key] + K * lm) / (st[t]["n"] + K)
    oh, dh, oa, da = rate(home, "pf"), rate(home, "pa"), rate(away, "pf"), rate(away, "pa")
    total = (oh + da - lm) + (oa + dh - lm)
    margin = (oh - dh) - (oa - da) + (0.0 if neutral else HE)
    return total, margin


def crps_normal(mu, sd, y):
    z = (y - mu) / sd
    return sd * (z * (2 * stats_cdf(z) - 1) + 2 * stats_pdf(z) - 1 / math.sqrt(math.pi))


def stats_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def stats_pdf(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)


def p_over(mu, line):
    return 1 - stats_cdf((line - mu) / SD)


def main():
    games = load()
    by_season = defaultdict(list)
    for g in games:
        by_season[g["season"]].append(g)
    seasons = sorted(by_season)
    rows = []
    prior_mean = None
    for s in seasons:
        gs = by_season[s]
        reg = [g for g in gs if g["stage"] == "REGULAR"]
        first = min(g["d"] for g in reg)
        st = defaultdict(lambda: dict(pf=0.0, pa=0.0, n=0))
        league = dict(pf=0.0, n=0)
        pending = []
        cur_day = None
        for g in gs:
            if g["d"] != cur_day:        # standings move only between dates: same-day results are not known
                for h in pending:
                    if h["stage"] == "REGULAR":
                        for t, f, a in ((h["home"], h["hs"], h["as_"]), (h["away"], h["as_"], h["hs"])):
                            st[t]["pf"] += f; st[t]["pa"] += a; st[t]["n"] += 1
                        league["pf"] += h["hs"] + h["as_"]; league["n"] += 2
                pending = []
                cur_day = g["d"]
            pending.append(g)
            if prior_mean is None:
                continue
            cur = league["pf"] / league["n"] if league["n"] else prior_mean
            lm = (league["n"] * cur + LM_PRIOR_WEIGHT * prior_mean) / (league["n"] + LM_PRIOR_WEIGHT)
            total, margin = centre(st, g["home"], g["away"], lm, g["neutral"])
            day = (g["d"] - first).days
            team_games = min(st[g["home"]]["n"], st[g["away"]]["n"])
            rows.append(dict(season=s, stage=g["stage"], date=g["d"].isoformat(), day=day, week=f"{s}:{day // 7 if g['stage'] == 'REGULAR' else 'PO' + str((g['d'] - first).days // 7)}",
                             min_team_games=team_games, league_team_games=league["n"], lm=round(lm, 3), lm_prior=round(prior_mean, 3),
                             forecast_total=round(total, 3), actual_total=g["hs"] + g["as_"], key=g["key"]))
        prior_mean = sum(g["hs"] + g["as_"] for g in reg) / (2 * len(reg))
    with open(OUT / "NBA_WALKFORWARD_TOTALS.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    return rows


def score(rows, m):
    out = []
    for r in rows:
        mu = r["forecast_total"] * m
        y = r["actual_total"]
        base_line = round(r["forecast_total"] * 2) / 2
        brier = sum((p_over(mu, base_line + d) - (1.0 if y > base_line + d else 0.0)) ** 2 for d in (-4, 0, 4)) / 3
        z = (y - mu) / SD
        out.append(dict(err=y - mu, sq=(y - mu) ** 2, crps=crps_normal(mu, SD, y), logs=-(math.log(stats_pdf(z) / SD)), brier=brier, week=r["week"]))
    return out


def summarise(name, subset, m, seed=20261108, B=4000):
    if not subset:
        return None
    a, b = score(subset, 1.0), score(subset, m)
    n = len(subset)
    res = dict(test=name, multiplier=m, n=n,
               mean_actual=round(sum(r["actual_total"] for r in subset) / n, 2),
               mean_forecast=round(sum(r["forecast_total"] for r in subset) / n, 2),
               bias_without=round(sum(x["err"] for x in a) / n, 2), bias_with=round(sum(x["err"] for x in b) / n, 2),
               rmse_without=round(math.sqrt(sum(x["sq"] for x in a) / n), 3), rmse_with=round(math.sqrt(sum(x["sq"] for x in b) / n), 3))
    for metric in ("crps", "logs", "brier"):
        d = [y[metric] - x[metric] for x, y in zip(a, b)]      # with minus without: negative = multiplier helps
        res[f"{metric}_without"] = round(sum(x[metric] for x in a) / n, 4)
        res[f"{metric}_with"] = round(sum(y[metric] for y in b) / n, 4)
        blocks = defaultdict(list)
        for x, v in zip(a, d):
            blocks[x["week"]].append(v)
        keys = list(blocks)
        rng = random.Random(seed)
        boots = []
        for _ in range(B):
            s = [v for k in (rng.choice(keys) for _ in keys) for v in blocks[k]]
            boots.append(sum(s) / len(s))
        boots.sort()
        res[f"{metric}_diff"] = round(sum(d) / n, 5)
        res[f"{metric}_diff_ci"] = f"[{boots[int(0.025 * B)]:.5f}, {boots[int(0.975 * B)]:.5f}]"
    return res


if __name__ == "__main__":
    rows = main()
    reg = [r for r in rows if r["stage"] == "REGULAR"]
    po = [r for r in rows if r["stage"] == "PLAYOFFS"]
    tests = []
    for days in (7, 14, 28, 42):
        sub = [r for r in reg if r["day"] < days]
        tests.append(summarise(f"EARLY_SEASON first {days} days, 0.988", sub, MULT["EARLY_SEASON"]))
    rest = [r for r in reg if r["day"] >= 42]
    tests.append(summarise("Regular season after day 42 (control), 0.988", rest, MULT["EARLY_SEASON"]))
    tests.append(summarise("FINALS_COMPRESSION playoffs, 0.970", po, MULT["FINALS_COMPRESSION"]))
    # leave-one-season-out: the playoff multiplier refitted on the other seasons' playoffs, scored on the held-out one
    loso = []
    for s in sorted({r["season"] for r in po}):
        train = [r for r in po if r["season"] != s]
        m = sum(r["actual_total"] for r in train) / sum(r["forecast_total"] for r in train)
        loso.append((s, m))
        tests.append(summarise(f"Playoffs {s}, refit on other seasons ({m:.4f})", [r for r in po if r["season"] == s], m))
    for s in sorted({r["season"] for r in reg}):
        sub = [r for r in reg if r["season"] == s and r["day"] < 14]
        train = [r for r in reg if r["season"] != s and r["day"] < 14]
        m = sum(r["actual_total"] for r in train) / sum(r["forecast_total"] for r in train)
        tests.append(summarise(f"Early (14 days) {s}, refit on other seasons ({m:.4f})", sub, m))
    # descriptive replication of the register's quantity: early-season raw mean / season mean
    desc = []
    for s in sorted({r["season"] for r in reg}):
        sr = [r for r in reg if r["season"] == s]
        e = [r["actual_total"] for r in sr if r["day"] < 28]
        desc.append(dict(season=s, early28_mean=round(sum(e) / len(e), 2), season_mean=round(sum(r["actual_total"] for r in sr) / len(sr), 2),
                         ratio=round((sum(e) / len(e)) / (sum(r["actual_total"] for r in sr) / len(sr)), 4),
                         prior_season_team_mean_x2=round(sr[0]["lm_prior"] * 2, 2),
                         playoff_mean=round(sum(r["actual_total"] for r in po if r["season"] == s) / max(1, len([r for r in po if r["season"] == s])), 2)))
    tests = [t for t in tests if t]
    with open(OUT / "NBA_REGIME_TESTS.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(tests[0]))
        w.writeheader(); w.writerows(tests)
    with open(OUT / "NBA_REGIME_DESCRIPTIVE.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(desc[0]))
        w.writeheader(); w.writerows(desc)
    for t in tests:
        print({k: t[k] for k in ("test", "n", "bias_without", "bias_with", "crps_diff", "crps_diff_ci", "brier_diff", "brier_diff_ci")})
    for d in desc:
        print(d)
