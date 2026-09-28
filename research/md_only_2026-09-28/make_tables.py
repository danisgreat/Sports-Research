"""Generate the lookup tables printed in PROBABILITY_TOOLKIT.md, and check them against the tools.

Outputs tables_*.md fragments in this folder plus tables_check.json. The toolkit copies the fragments
verbatim. Every table is a pure function of the stated inputs (no data, no odds):
- RM-1 q by stated p (tools/rank_model.py coefficients, verified row by row against rank_model.score_row);
- standard normal Phi(z);
- Poisson: soccer 1X2 grid, total goals, first half; hockey totals;
- negative binomial total runs (baseball) at three widths;
- no-tie normal margin win and cover probabilities (basketball, NFL, AFL, NRL);
- Elo difference -> win probability; logit(p).
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "tools"))
import card_math as cm  # noqa: E402
import rank_model as rm  # noqa: E402

COEF = rm.load_coef()
checks = {}


def write(name, text):
    with open(os.path.join(HERE, name), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text.rstrip() + "\n")


# ---------------------------------------------------------------- RM-1
def q_decision(p, cushion):
    w = COEF["weights"]
    lp = math.log(p / (1 - p))
    x = w["intercept"] + w["logit_p"] * lp + (w["cushion_nb"] if cushion else 0.0)
    return 1 / (1 + math.exp(-x))


rows = ["| Stated p | q, standard row | q, cushion row (C) | logit(p) |", "|---:|---:|---:|---:|"]
mism = 0
for i in range(50, 98):
    p = i / 100
    qs = min(max(q_decision(p, False), 0.03), 0.97) if p > 0.5 else 0.5
    qc = min(max(q_decision(p, True), 0.03), 0.97) if p > 0.5 else 0.5
    lg = math.log(p / (1 - p))
    rows.append(f"| {p:.2f} | {qs:.3f} | {qc:.3f} | {lg:+.3f} |")
    # check against the tool: a standard row (Over 8.5, mlb) and a cushion row (Hawks +3.5, nbl)
    t1 = rm.score_row(COEF, "mlb", "Over 8.5 runs", p)["q"]
    t2 = rm.score_row(COEF, "nbl", "Hawks +3.5", p)["q"]
    mism += (abs(round(t1, 3) - round(qs, 3)) > 0.0005) + (abs(round(t2, 3) - round(qc, 3)) > 0.0005)
    # below 0.5: the complement rule
    pb = 1 - p
    if pb < 0.5:
        t3 = rm.score_row(COEF, "mlb", "Under 8.5 runs", pb)["q"]          # standard row stated below 0.5
        t4 = rm.score_row(COEF, "nbl", "Hawks +3.5", pb)["q"]              # cushion stated below 0.5 -> 1 - q_std(1-p)
        t5 = rm.score_row(COEF, "nbl", "Bullets -3.5", pb)["q"]            # favourite -k.5 below 0.5 -> 1 - q_C(1-p)
        mism += (abs(t3 - (1 - min(max(q_decision(p, False), 0.03), 0.97))) > 1e-9)
        mism += (abs(t4 - (1 - min(max(q_decision(p, False), 0.03), 0.97))) > 1e-9)
        mism += (abs(t5 - (1 - min(max(q_decision(p, True), 0.03), 0.97))) > 1e-9)
checks["rm1_table_mismatches_vs_tool"] = mism
write("tables_rm1.md", "\n".join(rows))

# ---------------------------------------------------------------- Phi
lines = ["| z | .00 | .01 | .02 | .03 | .04 | .05 | .06 | .07 | .08 | .09 |", "|---:|" + "---:|" * 10]
for i in range(0, 35):
    z0 = i / 10
    cells = [f"{cm._norm_cdf(z0 + j / 100):.4f}" for j in range(10)]
    lines.append(f"| {z0:.1f} | " + " | ".join(cells) + " |")
write("tables_phi.md", "\n".join(lines))


# ---------------------------------------------------------------- Poisson
def pois(k, lam):
    return math.exp(-lam + k * math.log(lam) - math.lgamma(k + 1))


grid = [round(0.6 + 0.2 * i, 1) for i in range(11)]
hdr = "| λ home \\ λ away | " + " | ".join(f"{x:.1f}" for x in grid) + " |"
sep = "|---:|" + "---:|" * len(grid)
win_rows, draw_rows = [hdr, sep], [hdr, sep]
for lh in grid:
    w, d = [], []
    for la in grid:
        pw = sum(pois(i, lh) * pois(j, la) for i in range(20) for j in range(i))
        pd = sum(pois(i, lh) * pois(i, la) for i in range(20))
        w.append(f"{pw:.3f}")
        d.append(f"{pd:.3f}")
    win_rows.append(f"| **{lh:.1f}** | " + " | ".join(w) + " |")
    draw_rows.append(f"| **{lh:.1f}** | " + " | ".join(d) + " |")
write("tables_soccer_home.md", "\n".join(win_rows))
write("tables_soccer_draw.md", "\n".join(draw_rows))
by2 = [hdr, sep]
for lh in grid:
    cells = []
    for la in grid:
        p2 = sum(pois(i, lh) * pois(j, la) for i in range(20) for j in range(20) if i - j >= 2)
        cells.append(f"{p2:.3f}")
    by2.append(f"| **{lh:.1f}** | " + " | ".join(cells) + " |")
write("tables_soccer_home_by2.md", "\n".join(by2))
# check the soccer tables against card_math's Skellam
d = cm.Dist("skellam", mu=1.6, mu_opp=1.0)
checks["skellam_by2_gap"] = abs(cm.p_over(d, 1.5) - sum(pois(i, 1.6) * pois(j, 1.0) for i in range(20) for j in range(20) if i - j >= 2))

tot = ["| μ total | P(0) | P(≤1) | P(≤2) | P(≤3) | P(≤4) | P(≤5) | P(≤6) |", "|---:|" + "---:|" * 7]
for i in range(6, 51):
    mu = i / 10
    c, cells = 0.0, []
    for k in range(7):
        c += pois(k, mu)
        cells.append(f"{c:.3f}")
    tot.append(f"| {mu:.1f} | " + " | ".join(cells) + " |")
write("tables_goals_total.md", "\n".join(tot))

hk = ["| μ total | P(≤3) | P(≤4) | P(≤5) | P(≤6) | P(≤7) | P(≤8) |", "|---:|" + "---:|" * 6]
for i in range(45, 76):
    mu = i / 10
    cum = [sum(pois(k, mu) for k in range(n + 1)) for n in range(3, 9)]
    hk.append(f"| {mu:.1f} | " + " | ".join(f"{c:.3f}" for c in cum) + " |")
write("tables_hockey_total.md", "\n".join(hk))

# ---------------------------------------------------------------- negative binomial (baseball runs)
nb = []
for sd in (4.0, 4.5, 5.0):
    nb.append(f"**Width (SD) {sd:.1f}.** P(Over L) = P(total runs ≥ L + 0.5).\n")
    lines_ = [5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5]
    nb.append("| Mean | " + " | ".join(f"O {x}" for x in lines_) + " |")
    nb.append("|---:|" + "---:|" * len(lines_))
    for i in range(0, 25):
        mean = 6.0 + 0.25 * i
        d = cm.Dist("negbin", mean=mean, sd=sd)
        nb.append(f"| {mean:.2f} | " + " | ".join(f"{cm.p_over(d, L):.3f}" for L in lines_) + " |")
    nb.append("")
write("tables_baseball_total.md", "\n".join(nb))
# integer-line push masses at the reference width
push = ["| Mean | P(total = 7) | P(= 8) | P(= 9) |", "|---:|---:|---:|---:|"]
for i in range(0, 13):
    mean = 6.5 + 0.5 * i
    d = cm.Dist("negbin", mean=mean, sd=4.5)
    push.append(f"| {mean:.1f} | " + " | ".join(f"{d.pmf(k):.3f}" for k in (7, 8, 9)) + " |")
write("tables_baseball_push.md", "\n".join(push))

# ---------------------------------------------------------------- no-tie normal margins
def win_no_zero(m, sd):
    p0 = cm._norm_cdf((0.5 - m) / sd) - cm._norm_cdf((-0.5 - m) / sd)
    pgt = 1 - cm._norm_cdf((0.5 - m) / sd)
    return pgt / (1 - p0)


mt = ["| Expected margin m ÷ width | P(win), no tie | P(win), with continuity only |", "|---:|---:|---:|"]
for i in range(0, 21):
    r = i / 20
    mt.append(f"| {r:.2f} | {win_no_zero(r * 15.1, 15.1):.3f} | {cm._norm_cdf(r):.3f} |")
write("tables_margin_win.md", "\n".join(mt))
# check: the hand formula equals card_math's no-zero normal
d = cm.Dist("normal", mean=4.0, sd=15.1, no_zero=True)
checks["no_zero_formula_gap"] = abs(cm.p_over(d, 0) - win_no_zero(4.0, 15.1))
w_tool, _ = cm.p_cover(d, -3.5)
p0 = cm._norm_cdf(0.5 / 15.1 - 4 / 15.1) - cm._norm_cdf(-0.5 / 15.1 - 4 / 15.1)
hand = (1 - cm._norm_cdf((3.5 + 0.5 - 0.5 - 4.0) / 15.1)) / (1 - p0)   # P(X >= 4) = 1 - Phi((3.5 - m)/sd)
checks["no_zero_cover_gap"] = abs(w_tool - hand)

# ---------------------------------------------------------------- Elo and logit
el = ["| Elo gap | P(stronger wins) | Elo gap | P | Elo gap | P |", "|---:|---:|---:|---:|---:|---:|"]
vals = list(range(0, 510, 10))
third = (len(vals) + 2) // 3
for i in range(third):
    cells = []
    for j in range(3):
        k = i + j * third
        if k < len(vals):
            g = vals[k]
            cells += [str(g), f"{1 / (1 + 10 ** (-g / 400)):.3f}"]
        else:
            cells += ["", ""]
    el.append("| " + " | ".join(cells) + " |")
write("tables_elo.md", "\n".join(el))

json.dump(checks, open(os.path.join(HERE, "tables_check.json"), "w"), indent=2)
print(json.dumps(checks))
