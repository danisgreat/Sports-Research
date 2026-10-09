"""Candidate ladder, Rank-1 gate, Rank-2 diversification and adjustment dependence (PRD-02, PRD-03, PRD-04, PRD-05).

Everything here is priced from ONE joint outcome space built from a `ScoreDistribution`, so win, push and loss mass of any two
rows are exactly consistent and the joint top-two failure mass is a real probability, not an assumption of independence.

Outcome space: mass[h, a, c] with c = 0 (home wins the event), 1 (away wins), 2 (no winner / draw). Engines whose winner
is a function of the score put each cell in one class; tennis supplies `home_win_given_cell` because the winner is not a
function of the games grid.

Rules (thresholds live in `runtime/config/selection_rules.json`, provisional until confirmed prospectively):
  - Rows with p_card above 0.90 are excluded (degenerate); p_card is win / (win + loss), push leaves the denominator.
  - Rank 1 is the highest p_card. The Rank-1 gate passes only if p_card >= 0.62 and the lead over the best
    non-complementary alternative is >= 0.04; otherwise the card is labelled RANK1_UNSTABLE and scored in its own cohort.
  - Rank 2 is chosen from remaining rows with p_card >= 0.58 to minimise P(Rank 1 and Rank 2 both lose); ties go to p_card.
    Ranks 3 and 4 follow in p_card order and never exceed Rank 2's p_card (the card validator requires non-increasing p).
  - Rows from a different outcome space than Rank 1 (for example a first-half row against a full-game row) have no exact
    joint, so their joint failure is the conservative upper bound min(P(lose_1), P(lose_2)).
"""

from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

from .contracts import ScoreDistribution
from .errors import MissingInputs

RULES_PATH = Path(__file__).resolve().parents[2] / "config" / "selection_rules.json"
HOME, AWAY, NONE = 0, 1, 2


def load_rules(path: Optional[Path] = None) -> Dict[str, Any]:
    return json.loads(Path(path or RULES_PATH).read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- outcome space
@dataclass
class Outcome:
    """Joint (home score, away score, winner class) probability space of one event and endpoint."""
    mass: np.ndarray                  # (H, A, 3)
    home: np.ndarray                  # (H, A) home score at each cell
    away: np.ndarray                  # (H, A)
    space_id: str = "full"
    endpoint: str = "unspecified"

    @property
    def margin(self) -> np.ndarray:
        return self.home - self.away

    @property
    def total(self) -> np.ndarray:
        return self.home + self.away

    def moments(self) -> Dict[str, float]:
        w = self.mass.sum(axis=2)
        m, t = self.margin, self.total
        mean_m, mean_t = float((w * m).sum()), float((w * t).sum())
        return {"margin_mean": mean_m, "margin_sd": float(np.sqrt((w * (m - mean_m) ** 2).sum())),
                "total_mean": mean_t, "total_sd": float(np.sqrt((w * (t - mean_t) ** 2).sum()))}


def outcome_space(dist: ScoreDistribution, space_id: str = "full") -> Outcome:
    """Build the joint outcome space of a distribution (tennis supplies a winner split; others derive it from the score)."""
    grid = dist.grid
    h = np.broadcast_to(np.asarray(dist.home_support, dtype=float)[:, None], grid.shape)
    a = np.broadcast_to(np.asarray(dist.away_support, dtype=float)[None, :], grid.shape)
    mass = np.zeros(grid.shape + (3,))
    split = dist.metadata.get("home_win_given_cell")
    if split is not None:
        split = np.asarray(split, dtype=float)
        mass[..., HOME] = grid * split
        mass[..., AWAY] = grid * (1.0 - split)
    else:
        mass[..., HOME] = np.where(h > a, grid, 0.0)
        mass[..., AWAY] = np.where(a > h, grid, 0.0)
        mass[..., NONE] = np.where(h == a, grid, 0.0)
    return Outcome(mass, np.array(h), np.array(a), space_id, dist.endpoint)


# ---------------------------------------------------------------------------------- rows
@dataclass
class Row:
    """A priced proposition: boolean masks over the outcome space for win and loss (everything else is a push)."""
    label: str
    family: str                        # winner | double_chance | handicap | total | team_total | btts | period_*
    kind: str                          # machine key for complement detection, e.g. "total:over:171.5"
    complement: Optional[str]          # kind of the logical complement (or None)
    win: np.ndarray = field(repr=False)
    lose: np.ndarray = field(repr=False)
    space_id: str = "full"
    tag: str = "ANALYST_DERIVED"
    replaces: Optional[str] = None
    p_win: float = 0.0
    p_lose: float = 0.0

    @property
    def p_push(self) -> float:
        return max(0.0, 1.0 - self.p_win - self.p_lose)

    @property
    def p_card(self) -> float:
        """Conditional win probability win / (win + loss): a push leaves the denominator."""
        denom = self.p_win + self.p_lose
        return self.p_win / denom if denom > 0 else 0.0


def _price(row: Row, outcome: Outcome) -> Row:
    row.p_win = float(outcome.mass[row.win].sum())
    row.p_lose = float(outcome.mass[row.lose].sum())
    return row


def _row(outcome: Outcome, label: str, family: str, kind: str, complement: Optional[str], win: np.ndarray, lose: np.ndarray,
         tag: str = "ANALYST_DERIVED") -> Row:
    return _price(Row(label, family, kind, complement, win, lose, outcome.space_id, tag), outcome)


def _classes(outcome: Outcome, *which: int) -> np.ndarray:
    mask = np.zeros(outcome.mass.shape, dtype=bool)
    for c in which:
        mask[..., c] = True
    return mask


def _cells(outcome: Outcome, cond: np.ndarray) -> np.ndarray:
    return np.broadcast_to(cond[..., None], outcome.mass.shape)


def fmt_line(line: float) -> str:
    return f"{line:+g}"


def winner_row(outcome: Outcome, side: str, tag: str = "ANALYST_DERIVED", name: Optional[str] = None) -> Row:
    side = side.lower()
    cls = {"home": HOME, "away": AWAY, "draw": NONE}[side]
    win = _classes(outcome, cls)
    comp = {"home": "winner:away", "away": "winner:home", "draw": None}[side]
    label = f"{name or side.capitalize()} to win"
    return _row(outcome, label, "winner", f"winner:{side}", comp, win, ~win, tag)


def double_chance_row(outcome: Outcome, selection: str, tag: str = "ANALYST_DERIVED", names: Tuple[str, str] = ("Home", "Away")) -> Row:
    sel = selection.upper()
    cls = {"1X": (HOME, NONE), "X2": (AWAY, NONE), "12": (HOME, AWAY)}[sel]
    win = _classes(outcome, *cls)
    comp = {"1X": "winner:away", "X2": "winner:home", "12": "winner:draw"}[sel]
    label = {"1X": f"{names[0]} or draw", "X2": f"{names[1]} or draw", "12": f"{names[0]} or {names[1]} (no draw)"}[sel]
    return _row(outcome, label, "double_chance", f"double_chance:{sel}", comp, win, ~win, tag)


def handicap_row(outcome: Outcome, side: str, line: float, tag: str = "ANALYST_DERIVED", name: Optional[str] = None) -> Row:
    """`side` receives `line` points: wins if (own margin + line) > 0, pushes at 0."""
    own = outcome.margin if side == "home" else -outcome.margin
    win, lose = _cells(outcome, own + line > 0), _cells(outcome, own + line < 0)
    other = "away" if side == "home" else "home"
    comp = f"handicap:{other}:{(-line) + 0.0:g}"
    return _row(outcome, f"{name or side.capitalize()} {fmt_line(line)}", "handicap", f"handicap:{side}:{line:g}", comp, win, lose, tag)


def total_row(outcome: Outcome, side: str, line: float, tag: str = "ANALYST_DERIVED") -> Row:
    t = outcome.total
    if side == "over":
        win, lose = _cells(outcome, t > line), _cells(outcome, t < line)
    else:
        win, lose = _cells(outcome, t < line), _cells(outcome, t > line)
    comp = f"total:{'under' if side == 'over' else 'over'}:{line:g}"
    return _row(outcome, f"Total {side.capitalize()} {line:g}", "total", f"total:{side}:{line:g}", comp, win, lose, tag)


def team_total_row(outcome: Outcome, team: str, side: str, line: float, tag: str = "ANALYST_DERIVED", name: Optional[str] = None) -> Row:
    score = outcome.home if team == "home" else outcome.away
    if side == "over":
        win, lose = _cells(outcome, score > line), _cells(outcome, score < line)
    else:
        win, lose = _cells(outcome, score < line), _cells(outcome, score > line)
    comp = f"team_total:{team}:{'under' if side == 'over' else 'over'}:{line:g}"
    return _row(outcome, f"{name or team.capitalize()} team total {side.capitalize()} {line:g}", "team_total",
                f"team_total:{team}:{side}:{line:g}", comp, win, lose, tag)


def btts_row(outcome: Outcome, yes: bool, tag: str = "ANALYST_DERIVED") -> Row:
    both = (outcome.home > 0) & (outcome.away > 0)
    win = _cells(outcome, both if yes else ~both)
    return _row(outcome, f"Both teams to score: {'Yes' if yes else 'No'}", "btts", f"btts:{'yes' if yes else 'no'}",
                f"btts:{'no' if yes else 'yes'}", win, ~win, tag)


def row_from_spec(outcome: Outcome, spec: Dict[str, Any]) -> Row:
    """A supplied contract as a priced row (tag SUPPLIED). Same spec shape as `BaseSportEngine.evaluate_contracts`."""
    ctype, side = spec["type"], str(spec.get("side", "")).lower()
    if ctype in ("spread", "total", "team_total") and spec.get("line") is None:
        raise MissingInputs(f"{ctype} contract needs a line: {spec}")
    line = float(spec.get("line", 0.0))
    if ctype == "moneyline":
        row = winner_row(outcome, side)
    elif ctype == "spread":
        row = handicap_row(outcome, side, line)
    elif ctype == "total":
        row = total_row(outcome, side, line)
    elif ctype == "team_total":
        row = team_total_row(outcome, str(spec.get("team", "home")).lower(), side, line)
    elif ctype == "double_chance":
        row = double_chance_row(outcome, side)
    elif ctype == "btts":
        row = btts_row(outcome, side in ("yes", "btts_yes"))
    else:
        raise MissingInputs(f"cannot price supplied contract type {ctype!r}")
    row.tag = "SUPPLIED"
    if spec.get("label"):
        row.label = str(spec["label"])
    return row


# --------------------------------------------------------------------------------- ladder
def _lines(lo: float, hi: float, step: float, integers: bool) -> List[float]:
    """Half-integer lines in [lo, hi] (every `step`-th one when step > 1), plus whole-number lines when `integers`."""
    stride = max(int(round(step)), 1)
    out: List[float] = []
    for offset in ((0.5, 0.0) if integers else (0.5,)):
        n = int(np.ceil(lo - offset))
        x = n + offset
        k = 0
        while x <= hi + 1e-9:
            if k % stride == 0:
                out.append(float(x))
            x += 1.0
            k += 1
    return sorted(set(out))


def ladder(outcome: Outcome, spec: Dict[str, Any], names: Tuple[str, str] = ("Home", "Away"), draws: Optional[bool] = None) -> List[Row]:
    """Every standard proposition on the sport's line ladder, priced from `outcome`.

    spec keys: handicap_step, total_step, span_sd (default 2.5), integer_lines (also price whole-number lines, which push),
    allow_draw (three-way sport). Half-integer lines are always priced; whole lines only if `integer_lines`.
    """
    moments = outcome.moments()
    span = float(spec.get("span_sd", 2.5))
    draws = bool(spec.get("allow_draw", False)) if draws is None else draws
    integers = bool(spec.get("integer_lines", False))
    rows: List[Row] = [winner_row(outcome, "home", name=names[0]), winner_row(outcome, "away", name=names[1])]
    if draws:
        rows += [winner_row(outcome, "draw", name="Draw"), double_chance_row(outcome, "1X", names=names),
                 double_chance_row(outcome, "X2", names=names), double_chance_row(outcome, "12", names=names)]
    h_lo, h_hi = moments["margin_mean"] - span * moments["margin_sd"], moments["margin_mean"] + span * moments["margin_sd"]
    h_step = float(spec.get("handicap_step", 1.0))
    # a handicap line L is "side receives L": cover the range of margins that can matter for either side
    for line in _lines(-h_hi, -h_lo, h_step, integers):
        rows.append(handicap_row(outcome, "home", line, name=names[0]))
    for line in _lines(h_lo, h_hi, h_step, integers):
        rows.append(handicap_row(outcome, "away", line, name=names[1]))
    t_step = float(spec.get("total_step", 1.0))
    t_lo, t_hi = moments["total_mean"] - span * moments["total_sd"], moments["total_mean"] + span * moments["total_sd"]
    for line in _lines(max(t_lo, 0.5), t_hi, t_step, integers):
        rows += [total_row(outcome, "over", line), total_row(outcome, "under", line)]
    w = outcome.mass.sum(axis=2)
    for team, score in (("home", outcome.home), ("away", outcome.away)):
        mean = float((w * score).sum())
        sd = float(np.sqrt((w * (score - mean) ** 2).sum()))
        for line in _lines(max(mean - span * sd, 0.5), mean + span * sd, float(spec.get("team_total_step", t_step)), integers):
            rows += [team_total_row(outcome, team, "over", line, name=names[0 if team == "home" else 1]),
                     team_total_row(outcome, team, "under", line, name=names[0 if team == "home" else 1])]
    if spec.get("btts"):
        rows += [btts_row(outcome, True), btts_row(outcome, False)]
    return rows


# ------------------------------------------------------------------- selection (P4, PRD)
def joint_failure(a: Row, b: Row, outcome: Outcome, other: Optional[Outcome] = None) -> Tuple[float, bool]:
    """(P(both lose), exact). Rows in different outcome spaces get the conservative bound min(P(lose_a), P(lose_b))."""
    if a.space_id != b.space_id or other is not None:
        return min(a.p_lose, b.p_lose), False
    return float(outcome.mass[a.lose & b.lose].sum()), True


def are_complements(a: Row, b: Row) -> bool:
    return (a.complement is not None and a.complement == b.kind) or (b.complement is not None and b.complement == a.kind)


@dataclass
class Pick:
    rank: int
    row: Row
    role: str
    p_card: float
    p_win: float
    p_push: float
    p_lose: float

    def as_dict(self) -> Dict[str, Any]:
        return {"rank": self.rank, "role": self.role, "tag": self.row.tag, "proposition": self.row.label, "family": self.row.family,
                "kind": self.row.kind, "p_card": self.p_card, "p_win": self.p_win, "p_push": self.p_push, "p_lose": self.p_lose,
                "replaces": self.row.replaces, "space": self.row.space_id}


@dataclass
class Proposal:
    picks: List[Pick]
    joint_failure_top2: Optional[float]
    joint_exact: bool
    rank1_gate: Dict[str, Any]
    flags: List[str]
    considered: int
    ladder_table: List[Dict[str, Any]]

    def as_dict(self) -> Dict[str, Any]:
        return {"picks": [p.as_dict() for p in self.picks], "joint_failure_top2": self.joint_failure_top2, "joint_exact": self.joint_exact,
                "rank1_gate": self.rank1_gate, "flags": self.flags, "considered": self.considered, "ladder": self.ladder_table}

    def pick_table(self, distribution_id: str = "dist") -> str:
        """Markdown pick table in the card format; evidence and failure-route cells are left as TO_FILL for the analyst."""
        lines = ["| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |", "|---|---|---|---|---|---|---|---|"]
        for p in self.picks:
            tag = p.row.tag + (f" (replaces {p.row.replaces})" if p.row.replaces else "")
            lines.append(f"| {p.rank} | {p.role} | {tag} | {p.row.label} | {100 * p.p_card:.1f}% | FROM_DISTRIBUTION:{distribution_id} | TO_FILL | TO_FILL |")
        return "\n".join(lines)


def rank1_gate(p1: float, best_alternative: float, rules: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    rules = rules or load_rules()
    gate = rules["rank1_gate"]
    margin = p1 - best_alternative
    passed = p1 >= gate["p_min"] and margin >= gate["margin_min"]
    return {"passed": bool(passed), "p_rank1": p1, "best_alternative": best_alternative, "margin": margin, "p_min": gate["p_min"],
            "margin_min": gate["margin_min"], "status": gate["status"]}


def propose(rows: Sequence[Row], outcome: Outcome, supplied: Sequence[Row] = (), rules: Optional[Dict[str, Any]] = None,
            ladder_summary: bool = True) -> Proposal:
    """Choose and rank four propositions from `rows` (ladder rows) plus `supplied` rows, under the PRD-02/03/04 rules."""
    rules = rules or load_rules()
    p_max = float(rules["p_card_max"])
    p2_min = float(rules["rank2"]["p_min"])
    pool: List[Row] = []
    seen = set()
    for row in list(supplied) + list(rows):                     # supplied first so a duplicate keeps its SUPPLIED tag
        if row.kind in seen:
            continue
        seen.add(row.kind)
        if row.p_card > p_max or row.p_win <= 0.0:
            continue
        pool.append(row)
    if len(pool) < 4:
        raise MissingInputs(f"only {len(pool)} propositions remain after excluding p_card > {p_max:.0%}; widen the ladder")
    supplied_by_family: Dict[str, List[Row]] = {}
    for row in supplied:
        supplied_by_family.setdefault(row.family, []).append(row)
    flags: List[str] = []
    ranked = sorted(pool, key=lambda r: (-r.p_card, r.p_push, r.label))
    first = ranked[0]
    alternatives = [r for r in ranked[1:] if not are_complements(first, r) and r.kind != first.kind]
    best_alt = alternatives[0].p_card if alternatives else 0.0
    gate = rank1_gate(first.p_card, best_alt, rules)
    if not gate["passed"]:
        flags.append("RANK1_UNSTABLE")
    remaining = [r for r in ranked[1:] if not are_complements(first, r)]
    eligible = [r for r in remaining if r.p_card >= p2_min]
    exact = True
    if eligible:
        scored = []
        for r in eligible:
            jf, is_exact = joint_failure(first, r, outcome)
            scored.append((jf, -r.p_card, r.label, r, is_exact))
        scored.sort(key=lambda t: t[:3])
        jf2, _, _, second, exact = scored[0]
    else:
        flags.append("RANK2_WEAK_SLATE")
        second = remaining[0]
        jf2, exact = joint_failure(first, second, outcome)
    if jf2 > float(rules["rank2"]["joint_failure_warn"]):
        flags.append("JOINT_FAILURE_HIGH")
    rest = [r for r in remaining if r is not second and r.p_card <= second.p_card + 1e-12]
    if len(rest) < 2:
        raise MissingInputs("fewer than two propositions remain below Rank 2's p_card; widen the ladder")
    chosen = [first, second, rest[0], rest[1]]
    for row in chosen:
        if row.tag != "SUPPLIED" and row.family in supplied_by_family:
            near = min(supplied_by_family[row.family], key=lambda s: abs(s.p_card - row.p_card))
            row.replaces = near.label
    picks = [Pick(i + 1, r, "PICK" if i < 2 else "INFORMATIONAL", r.p_card, r.p_win, r.p_push, r.p_lose) for i, r in enumerate(chosen)]
    table: List[Dict[str, Any]] = []
    if ladder_summary:
        table = [{"proposition": r.label, "family": r.family, "tag": r.tag, "p_card": round(r.p_card, 4), "p_win": round(r.p_win, 4),
                  "p_push": round(r.p_push, 4), "excluded_degenerate": r.p_card > p_max, "selected_rank": next((p.rank for p in picks if p.row is r), None)}
                 for r in sorted(list(supplied) + list(rows), key=lambda r: (r.family, -r.p_card))]
    return Proposal(picks, jf2, exact, gate, flags, len(pool), table)


# ------------------------------------------------------------------ adjustments (PRD-05)
@dataclass(frozen=True)
class Adjustment:
    """An analyst adjustment as a named parameter with a prior size and sign, never a free-text nudge."""
    name: str
    target: str                  # "margin" | "total" | "home_mean" | "away_mean" | ...
    size: float                  # in the target's own units (signed)
    sd_units: float              # |size| expressed in standard deviations of the target distribution
    prior_basis: str             # "fitted" | "archive_estimate" | "analyst_judgement"


def rank_by_p(rows: Sequence[Row], p_max: float = 0.90) -> List[Row]:
    """Rows ordered by p_card (descending), degenerate rows excluded; the plain Rule-P4 ordering used for replays."""
    return sorted((r for r in rows if r.p_card <= p_max), key=lambda r: (-r.p_card, r.p_push, r.label))


def _top_two(ranked: Any) -> List[str]:
    if isinstance(ranked, Proposal):
        return [p.row.kind for p in ranked.picks[:2]]
    return [r.kind for r in list(ranked)[:2]]


def adjustment_dependence(unadjusted: Any, adjusted: Any, adjustments: Sequence[Adjustment], threshold_sd: float = 0.25) -> Dict[str, Any]:
    """Flag ADJUSTMENT_DEPENDENT when an adjustment larger than `threshold_sd` changes the Rank-1 or Rank-2 proposition.

    `unadjusted` and `adjusted` are either `Proposal`s or ranked row lists (`rank_by_p`) priced without and with the adjustments.
    """
    big = [a for a in adjustments if abs(a.sd_units) > threshold_sd]
    before, after = _top_two(unadjusted), _top_two(adjusted)
    flips = before != after
    dependent = bool(big) and flips
    return {"flag": "ADJUSTMENT_DEPENDENT" if dependent else "NONE", "large_adjustments": [a.name for a in big], "top_two_before": before,
            "top_two_after": after, "ranks_changed": flips, "judgement_only": [a.name for a in adjustments if a.prior_basis == "analyst_judgement"]}
