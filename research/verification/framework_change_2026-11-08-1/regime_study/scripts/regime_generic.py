"""PRD-07 regime multipliers, MLB and AFL: the same walk-forward test as regime_nba.py on a season-to-date additive
(TB-2-MD form) total, with k and sd_total from ml.config.TB1_VALIDATED and the prior-season league mean blended in with
200 team-games. Data: MLB Stats API schedules (statsapi.mlb.com, robots 404) and AFL Tables season pages (afltables.com,
robots 404), captured into the study folder with SHA-256 hashes. These are study inputs, not learning-store admissions.

    python regime_generic.py mlb|afl RAWDIR OUTDIR
"""
import csv
import hashlib
import html
import json
import math
import random
import re
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

LEAGUE, RAW, OUT = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
OUT.mkdir(parents=True, exist_ok=True)
PARAMS = {"mlb": dict(k=20, sd=4.5, early=0.999, finals=0.924, early_rec=1.000, finals_rec=0.924),
          "afl": dict(k=2, sd=29.1, early=1.013, finals=0.943, early_rec=1.000, finals_rec=0.943),
          "nrl": dict(k=2, sd=13.9, early=0.938, finals=0.938, early_rec=0.938, finals_rec=0.938)}[LEAGUE]
K, SD, W = PARAMS["k"], PARAMS["sd"], 200.0


def load_mlb():
    games = {}
    for f in sorted(RAW.glob("mlb_*.json")):
        season, kind = f.stem.split("_")[1], f.stem.split("_")[2]
        for d in json.loads(f.read_text(encoding="utf-8")).get("dates", []):
            for g in d["games"]:
                if g["status"].get("codedGameState") != "F" or "score" not in g["teams"]["home"]:
                    continue
                games[g["gamePk"]] = dict(season=season, stage="REGULAR" if kind == "R" else "PLAYOFFS",
                                          d=date.fromisoformat(g.get("officialDate") or d["date"]), start=g["gameDate"],
                                          home=g["teams"]["home"]["team"]["name"], away=g["teams"]["away"]["team"]["name"],
                                          hs=g["teams"]["home"]["score"], as_=g["teams"]["away"]["score"], key=f"MLB:{g['gamePk']}")
    return sorted(games.values(), key=lambda g: (g["start"], g["key"]))


ROW = re.compile(r'<tr[^>]*><td width=16%><a href="\.\./teams/[^"]+">([^<]+)</a></td><td (?:nowrap )?width=20% align=center><tt>.*?</tt></td>'
                 r'<td width=5% align=center>\s*(\d+)</td><td>(.*?)</td></tr>', re.S)
HEAD = re.compile(r'<td align=center(?: width=60%)?><b>(Round \d+|Opening Round|Qualifying Final|Elimination Final|Semi Final|'
                  r'Preliminary Final|Grand Final|Wildcard Final)')


def load_afl():
    games = []
    for f in sorted(RAW.glob("afl_*.html")):
        season = f.stem.split("_")[1]
        t = f.read_text(encoding="latin-1")
        marks = [(m.start(), m.group(1)) for m in HEAD.finditer(t)]
        rows = [(m.start(), m) for m in ROW.finditer(t)]
        for i in range(0, len(rows) - 1):
            a, b = rows[i][1], rows[i + 1][1]
            dm = re.search(r"(\d{2}-[A-Z][a-z]{2}-\d{4})", a.group(3))
            if not dm or "won by" not in b.group(3) and "Match drawn" not in b.group(3) and "drew" not in b.group(3).lower():
                continue
            label = [h for p, h in marks if p < rows[i][0]][-1]
            games.append(dict(season=season, stage="REGULAR" if label.startswith(("Round", "Opening")) else "PLAYOFFS",
                              d=datetime.strptime(dm.group(1), "%d-%b-%Y").date(), start=dm.group(1), round=label,
                              home=html.unescape(a.group(1)), away=html.unescape(b.group(1)), hs=int(a.group(2)), as_=int(b.group(2)),
                              key=f"AFL:{season}:{len(games)}"))
    return sorted(games, key=lambda g: (g["d"], g["key"]))


NRL_HEAD = re.compile(r'<tr><th colspan="11">\s*(.*?)\s*</th></tr>', re.S)
NRL_ROW = re.compile(r'<tr><td><a href="/competitions/\d+"><a href="/competitions/\d+">[^<]*</a></a></td><td align="right">([^<]*)</td>'
                     r'<td>[^<]*</td><td class="team"><a [^>]*>([^<]+)</a></td><td class="n">(\d+)</td><td class="team"><a [^>]*>([^<]+)</a></td>'
                     r'<td class="n">(\d+)</td>')


def load_nrl():
    games = []
    for f in sorted(RAW.glob("nrl_*.html")):
        season = f.stem.split("_")[1]
        t = f.read_text(encoding="utf-8", errors="replace")
        marks = [(m.start(), re.sub(r"<[^>]+>", "", html.unescape(m.group(1))).strip()) for m in NRL_HEAD.finditer(t)]
        month = None
        for m in NRL_ROW.finditer(t):
            parts = m.group(1).split()
            if len(parts) == 2:
                month, dd = parts[0], int(parts[1])
            else:
                dd = int(parts[0])
            label = [h for p, h in marks if p < m.start()][-1]
            final = not label.lower().startswith("round")
            games.append(dict(season=season, stage="PLAYOFFS" if final else "REGULAR",
                              d=datetime.strptime(f"{dd} {month} {season}", "%d %b %Y").date(), start="", round=label,
                              home=html.unescape(m.group(2)), away=html.unescape(m.group(4)), hs=int(m.group(3)), as_=int(m.group(5)),
                              key=f"NRL:{season}:{len(games)}"))
    return sorted(games, key=lambda g: (g["d"], g["key"]))


def cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def pdf(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)


def walk(games):
    by = defaultdict(list)
    for g in games:
        by[g["season"]].append(g)
    rows, prior = [], None
    for s in sorted(by):
        gs = by[s]
        reg = [g for g in gs if g["stage"] == "REGULAR"]
        first = min(g["d"] for g in reg)
        st = defaultdict(lambda: dict(pf=0.0, pa=0.0, n=0))
        lg = dict(pf=0.0, n=0)
        pending, day = [], None
        for g in gs:
            if g["d"] != day:
                for h in pending:
                    if h["stage"] == "REGULAR":
                        for t, f, a in ((h["home"], h["hs"], h["as_"]), (h["away"], h["as_"], h["hs"])):
                            st[t]["pf"] += f; st[t]["pa"] += a; st[t]["n"] += 1
                        lg["pf"] += h["hs"] + h["as_"]; lg["n"] += 2
                pending, day = [], g["d"]
            pending.append(g)
            if prior is None:
                continue
            cur = lg["pf"] / lg["n"] if lg["n"] else prior
            lm = (lg["n"] * cur + W * prior) / (lg["n"] + W)
            rate = lambda t, key: (st[t][key] + K * lm) / (st[t]["n"] + K)
            total = (rate(g["home"], "pf") + rate(g["away"], "pa") - lm) + (rate(g["away"], "pf") + rate(g["home"], "pa") - lm)
            d = (g["d"] - first).days
            rows.append(dict(season=s, stage=g["stage"], date=g["d"].isoformat(), day=d,
                             week=f"{s}:{d // 7}" if g["stage"] == "REGULAR" else f"{s}:PO{d // 7}",
                             lm_prior=round(prior, 3), forecast_total=round(total, 3), actual_total=g["hs"] + g["as_"], key=g["key"]))
        prior = sum(g["hs"] + g["as_"] for g in reg) / (2 * len(reg))
    return rows


def score(rows, m):
    out = []
    for r in rows:
        mu, y = r["forecast_total"] * m, r["actual_total"]
        line = math.floor(r["forecast_total"]) + 0.5
        step = max(1.0, round(SD / 4))
        brier = sum((1 - cdf((line + dd - mu) / SD) - (1.0 if y > line + dd else 0.0)) ** 2 for dd in (-step, 0, step)) / 3
        z = (y - mu) / SD
        out.append(dict(err=y - mu, sq=(y - mu) ** 2, crps=SD * (z * (2 * cdf(z) - 1) + 2 * pdf(z) - 1 / math.sqrt(math.pi)),
                        brier=brier, week=r["week"]))
    return out


def summarise(name, sub, m, B=4000):
    if len(sub) < 10:
        return None
    a, b = score(sub, 1.0), score(sub, m)
    n = len(sub)
    res = dict(league=LEAGUE.upper(), test=name, multiplier=round(m, 4), n=n,
               mean_actual=round(sum(r["actual_total"] for r in sub) / n, 3), mean_forecast=round(sum(r["forecast_total"] for r in sub) / n, 3),
               bias_without=round(sum(x["err"] for x in a) / n, 3), bias_with=round(sum(x["err"] for x in b) / n, 3))
    for metric in ("crps", "brier"):
        d = [y[metric] - x[metric] for x, y in zip(a, b)]
        blocks = defaultdict(list)
        for x, v in zip(a, d):
            blocks[x["week"]].append(v)
        keys, rng, boots = list(blocks), random.Random(20261108), []
        for _ in range(B):
            s = [v for kk in (rng.choice(keys) for _ in keys) for v in blocks[kk]]
            boots.append(sum(s) / len(s))
        boots.sort()
        res[f"{metric}_without"] = round(sum(x[metric] for x in a) / n, 5)
        res[f"{metric}_with"] = round(sum(y[metric] for y in b) / n, 5)
        res[f"{metric}_diff"] = round(sum(d) / n, 5)
        res[f"{metric}_diff_ci"] = f"[{boots[int(0.025 * B)]:.5f}, {boots[int(0.975 * B)]:.5f}]"
    return res


if __name__ == "__main__":
    games = {"mlb": load_mlb, "afl": load_afl, "nrl": load_nrl}[LEAGUE]()
    with open(OUT / f"{LEAGUE.upper()}_RAW_HASHES.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["file", "bytes", "sha256"])
        for p in sorted(RAW.iterdir()):
            w.writerow([p.name, p.stat().st_size, hashlib.sha256(p.read_bytes()).hexdigest()])
    rows = walk(games)
    with open(OUT / f"{LEAGUE.upper()}_WALKFORWARD_TOTALS.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    reg = [r for r in rows if r["stage"] == "REGULAR"]
    po = [r for r in rows if r["stage"] == "PLAYOFFS"]
    tests = []
    for days in (14, 28):
        tests.append(summarise(f"EARLY_SEASON first {days} days, archive estimate {PARAMS['early']}", [r for r in reg if r["day"] < days], PARAMS["early"]))
    tests.append(summarise(f"FINALS_COMPRESSION postseason, recommended {PARAMS['finals_rec']}", po, PARAMS["finals_rec"]))
    for s in sorted({r["season"] for r in po}):
        train = [r for r in po if r["season"] != s]
        m = sum(r["actual_total"] for r in train) / sum(r["forecast_total"] for r in train)
        tests.append(summarise(f"Postseason {s}, refit on other seasons", [r for r in po if r["season"] == s], m))
    pooled = sum(r["actual_total"] for r in po) / sum(r["forecast_total"] for r in po)
    tests.append(summarise("Postseason pooled refit (in-sample, for the size only)", po, pooled))
    tests = [t for t in tests if t]
    with open(OUT / f"{LEAGUE.upper()}_REGIME_TESTS.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(tests[0]))
        w.writeheader(); w.writerows(tests)
    print(len(games), "games;", len(reg), "regular test rows;", len(po), "postseason test rows")
    for t in tests:
        print({k: t[k] for k in ("test", "multiplier", "n", "bias_without", "bias_with", "crps_diff", "crps_diff_ci", "brier_diff", "brier_diff_ci")})
