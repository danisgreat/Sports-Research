"""Tennis point -> game -> set -> match: exact recursion plus a form-shock integral (SIM-v2).

Given each player's probability of winning a point on their own serve, the distribution of every set score, of the games
each player wins, and of the match winner is computed EXACTLY (dynamic programming, no sampling). A simulation is needed only
for what the chain cannot express:

* a match-level form shock, because points are not independent and identically distributed (Klaassen & Magnus 2001) and
  the framework's own failure class TENNIS_IID_UNDERDISPERSION shows the i.i.d. chain is too narrow. ``with_form_shock``
  integrates the exact chain over a normal shock on the relative level of the two players with Gauss-Hermite nodes, so the
  result is still exact in the shock grid and has no Monte Carlo error;
* retirements and walkovers, which are settlement conventions and are not modelled here.

Game totals and game handicaps come from the joint pmf of games won, with a tie-break counted as one game (7-6 totals 13).
A match-winner probability is NOT P(games A > games B): covering a game handicap does not imply winning the match (SELECTION_RULES
section 4), so winner, set handicap and game handicap each read their own distribution.

    python -m ml sim tennis --pa 0.66 --pb 0.62 --best-of 3 --shock 0.0
"""
from __future__ import annotations

import numpy as np

from ml.sim import core

TB_POINT_CAP = 80
ADV_GAME_CAP = 60


def p_game(p: float) -> float:
    """Probability the server wins a game when winning each point with probability ``p`` (closed form, deuce included)."""
    q = 1 - p
    return p ** 4 * (1 + 4 * q + 10 * q * q) + 20 * p ** 5 * q ** 3 / (1 - 2 * p * q)


def p_tiebreak(pa: float, pb: float, a_first: bool, to: int = 7) -> float:
    """P(A wins a tie-break to ``to`` points, win by two). ``pa``/``pb``: each player's point probability on own serve.

    Service: the first server serves one point, then the players alternate every two points.
    """
    memo: dict = {}

    def server_is_a(k: int) -> bool:   # k = points already played
        first = (k + 1) // 2 % 2 == 0
        return first if a_first else not first

    def go(a: int, b: int) -> float:
        if a >= to and a - b >= 2:
            return 1.0
        if b >= to and b - a >= 2:
            return 0.0
        if a + b >= TB_POINT_CAP:
            return 0.5
        if (a, b) in memo:
            return memo[(a, b)]
        pt = pa if server_is_a(a + b) else 1 - pb      # P(A wins the point)
        value = pt * go(a + 1, b) + (1 - pt) * go(a, b + 1)
        memo[(a, b)] = value
        return value

    return go(0, 0)


def set_pmf(pa: float, pb: float, a_first: bool, kind: str = "standard_tb") -> dict:
    """Distribution of the final games (a, b) of one set. ``kind``: standard_tb (tie-break at 6-6, counted as 7-6),
    advantage (win by two games, no tie-break), or super_tb10 (a match tie-break to 10 replaces the set, counted 1-0)."""
    if kind == "super_tb10":
        p = p_tiebreak(pa, pb, a_first, 10)
        return {(1, 0): p, (0, 1): 1 - p}
    hold_a, hold_b = p_game(pa), p_game(pb)
    out: dict = {}
    memo: dict = {}

    def go(a: int, b: int) -> dict:
        if (a, b) in memo:
            return memo[(a, b)]
        res: dict = {}
        if (a >= 6 and a - b >= 2) or (a == 7 and b == 5):
            res = {(a, b): 1.0}
        elif (b >= 6 and b - a >= 2) or (b == 7 and a == 5):
            res = {(a, b): 1.0}
        elif kind == "standard_tb" and a == 6 and b == 6:
            first_a = a_first                                  # game 13 is served by the set's first server
            p = p_tiebreak(pa, pb, first_a, 7)
            res = {(7, 6): p, (6, 7): 1 - p}
        elif a + b >= ADV_GAME_CAP:
            res = {(a, b): 1.0}
        else:
            game = a + b                                       # games already played; the first server serves games 0, 2, 4...
            a_serves = a_first if game % 2 == 0 else not a_first
            p_a_wins = hold_a if a_serves else 1 - hold_b
            for (x, y), w in go(a + 1, b).items():
                res[(x, y)] = res.get((x, y), 0.0) + p_a_wins * w
            for (x, y), w in go(a, b + 1).items():
                res[(x, y)] = res.get((x, y), 0.0) + (1 - p_a_wins) * w
        memo[(a, b)] = res
        return res

    out = go(0, 0)
    total = sum(out.values())
    return {k: v / total for k, v in out.items()}


def match(pa: float, pb: float, best_of: int = 3, a_first: bool = True, final_set: str = "standard_tb") -> dict:
    """Exact match distribution: winner, set scores, and the joint pmf of games won by each player."""
    if best_of not in (3, 5):
        raise core.SimulationError("best_of must be 3 or 5")
    need = (best_of + 1) // 2
    states = {(0, 0, a_first): {(0, 0): 1.0}}       # (sets a, sets b, A serves first in this set) -> pmf of (games a, games b)
    winner_a, winner_b = {}, {}
    set_scores: dict = {}
    frontier = states
    while frontier:
        nxt: dict = {}
        for (sa, sb, first_a), games in frontier.items():
            deciding = sa == need - 1 and sb == need - 1
            kind = final_set if deciding else "standard_tb"
            for (ga, gb), w_set in set_pmf(pa, pb, first_a, kind).items():
                # Servers alternate every game (a tie-break counts as one game), so after an odd number of games the
                # first server served last and the other player opens the next set; after an even number it is the same
                # player's turn again. (A tie-break's first server receives first in the next set: the same rule.)
                next_first_a = (not first_a) if (ga + gb) % 2 == 1 else first_a
                a_won = ga > gb
                new = (sa + a_won, sb + (not a_won), next_first_a)
                bucket = (winner_a if new[0] == need else winner_b if new[1] == need else nxt).setdefault(new, {})
                for (xa, xb), w in games.items():
                    key = (xa + ga, xb + gb)
                    bucket[key] = bucket.get(key, 0.0) + w * w_set
                if new[0] == need or new[1] == need:
                    key = (new[0], new[1])
                    set_scores[key] = set_scores.get(key, 0.0) + sum(games.values()) * w_set
        frontier = nxt
    pmf: dict = {}
    for table in (winner_a, winner_b):
        for _, games in table.items():
            for key, w in games.items():
                pmf[key] = pmf.get(key, 0.0) + w
    p_a = sum(sum(g.values()) for g in winner_a.values())
    total = sum(pmf.values())
    pmf = {k: v / total for k, v in pmf.items()}
    top = max(max(k) for k in pmf) + 1
    grid = np.zeros((top, top))
    for (ga, gb), w in pmf.items():
        grid[ga, gb] = w
    return dict(p_a=p_a / total, set_scores={k: v / total for k, v in set_scores.items()}, games_grid=grid, best_of=best_of)


def with_form_shock(pa: float, pb: float, sigma: float, best_of: int = 3, a_first: bool = True, final_set: str = "standard_tb",
                    nodes: int = 15) -> dict:
    """Integrate ``match`` over a normal shock on the logit of both players' point probabilities: A's serve moves up and
    B's moves down by ``sigma * z``. sigma = 0 returns the i.i.d. chain. Estimate sigma from history; never guess it."""
    if sigma < 0:
        raise core.SimulationError("sigma must be non-negative")
    if sigma == 0:
        return match(pa, pb, best_of, a_first, final_set)
    x, w = np.polynomial.hermite_e.hermegauss(nodes)
    w = w / w.sum()
    logit = lambda p: np.log(p / (1 - p))
    expit = lambda v: 1 / (1 + np.exp(-v))
    results = [match(float(expit(logit(pa) + sigma * z)), float(expit(logit(pb) - sigma * z)), best_of, a_first, final_set) for z in x]
    size = max(r["games_grid"].shape[0] for r in results)
    grid = np.zeros((size, size))
    for wt, r in zip(w, results):
        g = r["games_grid"]
        grid[: g.shape[0], : g.shape[1]] += wt * g
    sets: dict = {}
    for wt, r in zip(w, results):
        for k, v in r["set_scores"].items():
            sets[k] = sets.get(k, 0.0) + wt * v
    return dict(p_a=float(sum(wt * r["p_a"] for wt, r in zip(w, results))), set_scores=sets, games_grid=grid / grid.sum(), best_of=best_of)


def games_grid(result: dict):
    """The joint pmf of games won as a ScoreGrid (home = player A) for game totals and game handicaps."""
    from ml.core.distributions import ScoreGrid
    return ScoreGrid(result["games_grid"])


def set_handicap(result: dict, line: float, side: str = "A") -> dict:
    """P(win/push/loss) of a set handicap from the exact set-score distribution."""
    win = push = loss = 0.0
    for (sa, sb), p in result["set_scores"].items():
        x = (sa - sb + line) if side == "A" else (sb - sa + line)
        win += p * (x > 0)
        push += p * (x == 0)
        loss += p * (x < 0)
    return dict(w=win, p=push, l=loss, p_decisive=win / (win + loss) if win + loss else float("nan"))


def simulate_match(pa: float, pb: float, best_of: int, n: int, seed: int, a_first: bool = True, final_set: str = "standard_tb") -> dict:
    """Point-by-point Monte Carlo of the same chain; used to test the exact recursion, never to price a card."""
    g = core.rng(seed)
    need = (best_of + 1) // 2
    wins = 0
    total_games = []
    for _ in range(n):
        sa = sb = 0
        first_a = a_first
        games_total = 0
        while sa < need and sb < need:
            deciding = sa == need - 1 and sb == need - 1
            kind = final_set if deciding else "standard_tb"
            ga = gb = 0
            if kind == "super_tb10":
                a_point = _tb(g, pa, pb, first_a, 10)
                ga, gb = (1, 0) if a_point else (0, 1)
            else:
                while True:
                    if (ga >= 6 and ga - gb >= 2) or (ga == 7 and gb == 5) or (gb >= 6 and gb - ga >= 2) or (gb == 7 and ga == 5):
                        break
                    if kind == "standard_tb" and ga == 6 and gb == 6:
                        if _tb(g, pa, pb, first_a, 7):
                            ga = 7
                        else:
                            gb = 7
                        break
                    a_serves = first_a if (ga + gb) % 2 == 0 else not first_a
                    p = p_game(pa) if a_serves else 1 - p_game(pb)
                    if g.random() < p:
                        ga += 1
                    else:
                        gb += 1
                    if ga + gb >= ADV_GAME_CAP:
                        break
            games_total += ga + gb
            if ga > gb:
                sa += 1
            else:
                sb += 1
            first_a = (not first_a) if (ga + gb) % 2 == 1 else first_a
        wins += sa == need
        total_games.append(games_total)
    return dict(p_a=wins / n, mean_total_games=float(np.mean(total_games)), n=n, seed=seed)


def _tb(g, pa: float, pb: float, a_first: bool, to: int) -> bool:
    a = b = 0
    while True:
        k = a + b
        first = (k + 1) // 2 % 2 == 0
        a_serves = first if a_first else not first
        p = pa if a_serves else 1 - pb
        if g.random() < p:
            a += 1
        else:
            b += 1
        if a >= to and a - b >= 2:
            return True
        if b >= to and b - a >= 2:
            return False
        if a + b >= TB_POINT_CAP:
            return g.random() < 0.5


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pa", type=float, required=True, help="A's point probability on own serve")
    parser.add_argument("--pb", type=float, required=True, help="B's point probability on own serve")
    parser.add_argument("--best-of", type=int, default=3)
    parser.add_argument("--shock", type=float, default=0.0)
    parser.add_argument("--final-set", default="standard_tb", choices=("standard_tb", "advantage", "super_tb10"))
    args = parser.parse_args(argv)
    result = with_form_shock(args.pa, args.pb, args.shock, args.best_of, True, args.final_set)
    grid = games_grid(result)
    tv, tp = grid.total_pmf()
    print(f"exact recursion (no Monte Carlo); form shock sigma {args.shock}")
    print(f"P(A wins match) {result['p_a']:.4f}; mean total games {float(tv @ tp):.2f}")
    print("set scores:", {f"{a}-{b}": round(v, 4) for (a, b), v in sorted(result['set_scores'].items())})


if __name__ == "__main__":
    main()
