"""Leave-one-season-out, all held-out seasons scored together: each season's postseason (or early window) gets the multiplier
fitted on the other seasons only; paired CRPS and Brier against no multiplier, season-block bootstrap."""
import csv, math, random, sys
from collections import defaultdict
SD = {"NBA": 19.4, "MLB": 4.5, "AFL": 29.1, "NRL": 13.9}
def cdf(z): return 0.5 * (1 + math.erf(z / math.sqrt(2)))
def pdf(z): return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)
def sc(mu, y, f, sd):
    z = (y - mu) / sd
    line = (round(f * 2) / 2) if sd > 10 else math.floor(f) + 0.5
    step = max(1.0, round(sd / 4)) if sd < 10 else 4
    b = sum((1 - cdf((line + d - mu) / sd) - (1.0 if y > line + d else 0.0)) ** 2 for d in (-step, 0, step)) / 3
    return sd * (z * (2 * cdf(z) - 1) + 2 * pdf(z) - 1 / math.sqrt(math.pi)), b
out = []
for lg, path in (("NBA", "outputs/NBA_WALKFORWARD_TOTALS.csv"), ("MLB", "outputs/MLB_WALKFORWARD_TOTALS.csv"), ("AFL", "outputs/AFL_WALKFORWARD_TOTALS.csv"), ("NRL", "outputs/NRL_WALKFORWARD_TOTALS.csv")):
    rows = [dict(r, forecast_total=float(r["forecast_total"]), actual_total=float(r["actual_total"]), day=int(r["day"])) for r in csv.DictReader(open(path))]
    for name, pick in (("postseason", lambda r: r["stage"] == "PLAYOFFS"), ("early 14 days", lambda r: r["stage"] == "REGULAR" and r["day"] < 14),
                       ("early 28 days", lambda r: r["stage"] == "REGULAR" and r["day"] < 28)):
        sub = [r for r in rows if pick(r)]
        seasons = sorted({r["season"] for r in sub})
        diffs = defaultdict(list); ms = []; bias0 = bias1 = 0; n = 0
        for s in seasons:
            tr = [r for r in sub if r["season"] != s]
            m = sum(r["actual_total"] for r in tr) / sum(r["forecast_total"] for r in tr)
            ms.append(m)
            for r in sub:
                if r["season"] != s: continue
                c0, b0 = sc(r["forecast_total"], r["actual_total"], r["forecast_total"], SD[lg])
                c1, b1 = sc(r["forecast_total"] * m, r["actual_total"], r["forecast_total"], SD[lg])
                diffs[s].append((c1 - c0, b1 - b0)); n += 1
                bias0 += r["actual_total"] - r["forecast_total"]; bias1 += r["actual_total"] - r["forecast_total"] * m
        allc = [d[0] for v in diffs.values() for d in v]; allb = [d[1] for v in diffs.values() for d in v]
        rng = random.Random(20261108); bc = []; bb = []
        for _ in range(4000):
            ks = [rng.choice(seasons) for _ in seasons]
            c = [d[0] for k in ks for d in diffs[k]]; b = [d[1] for k in ks for d in diffs[k]]
            bc.append(sum(c) / len(c)); bb.append(sum(b) / len(b))
        bc.sort(); bb.sort()
        better = sum(1 for s in seasons if sum(d[0] for d in diffs[s]) < 0)
        out.append(dict(league=lg, window=name, seasons=len(seasons), n=n, held_out_multipliers=f"{min(ms):.4f}-{max(ms):.4f}",
                        bias_without=round(bias0 / n, 3), bias_with=round(bias1 / n, 3),
                        crps_diff=round(sum(allc) / n, 5), crps_ci=f"[{bc[100]:.5f}, {bc[3899]:.5f}]",
                        brier_diff=round(sum(allb) / n, 5), brier_ci=f"[{bb[100]:.5f}, {bb[3899]:.5f}]",
                        seasons_improved=f"{better}/{len(seasons)}"))
with open("outputs/LOSO_HELD_OUT.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
for o in out: print(o)
