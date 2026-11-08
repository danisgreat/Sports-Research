"""Pooled ratio (actual / reference forecast) for each regime window, with a season-block bootstrap interval."""
import csv, random
out = []
for lg in ("NBA", "MLB", "AFL", "NRL"):
    rows = [dict(r, f=float(r["forecast_total"]), y=float(r["actual_total"]), day=int(r["day"])) for r in csv.DictReader(open(f"outputs/{lg}_WALKFORWARD_TOTALS.csv"))]
    for name, pick in (("postseason", lambda r: r["stage"] == "PLAYOFFS"), ("early 28 days", lambda r: r["stage"] == "REGULAR" and r["day"] < 28),
                       ("regular season after day 28 (control)", lambda r: r["stage"] == "REGULAR" and r["day"] >= 28)):
        sub = [r for r in rows if pick(r)]
        by = {}
        for r in sub: by.setdefault(r["season"], []).append(r)
        ks = sorted(by); rng = random.Random(20261108); bs = []
        for _ in range(4000):
            s = [r for k in (rng.choice(ks) for _ in ks) for r in by[k]]
            bs.append(sum(r["y"] for r in s) / sum(r["f"] for r in s))
        bs.sort()
        ratio = sum(r["y"] for r in sub) / sum(r["f"] for r in sub)
        out.append(dict(league=lg, window=name, seasons=f"{ks[0]}..{ks[-1]} ({len(ks)})", n=len(sub), ratio=round(ratio, 4),
                        ci_low=round(bs[100], 4), ci_high=round(bs[3899], 4), proportional_estimate=round(ratio - 1, 4),
                        mean_forecast=round(sum(r["f"] for r in sub) / len(sub), 2), mean_actual=round(sum(r["y"] for r in sub) / len(sub), 2)))
with open("outputs/REGIME_SIZES.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
for o in out: print(o)
