"""Competition discovery and configuration for the model workshop.

Optional maintainer discovery uses ``research/reviewed_history/<Sport>/<Competition>/``.
The retired store is never read or restored; new primary runs use reviewed web metadata/history.
Its columns, stage vocabulary, extra-time rule, tune/test seasons and comparator constants are derived from the
files themselves plus a small table of sport rules. Overrides exist only for facts a file cannot show
(franchise renames, the TB-1 constants that PROBABILITY_TOOLKIT §4.3 validated for nine leagues).

A competition that cannot be modelled is still listed, with the reason (header-only, alias copy, single-game
subset, suspected default dates, too little history, unsupported endpoint). Nothing is silently skipped.
"""
from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field, replace
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = REPO_ROOT / "research" / "reviewed_history"
SHADOW_ROOT = REPO_ROOT / "research" / "model_shadow"

csv.field_size_limit(10**9)


@dataclass(frozen=True)
class TB1:
    """PROBABILITY_TOOLKIT §4.3 constants (k, margin width, total width, home edge)."""

    k: float
    sd_margin: float | None
    sd_total: float | None
    home_edge: float
    poisson: bool = False


TB1_VALIDATED = {  # verbatim from PROBABILITY_TOOLKIT §4.3
    "NBA": TB1(2, 15.1, 19.4, 1.71), "WNBA": TB1(2, 13.3, 19.5, 1.73), "NBL": TB1(5, 15.2, 18.7, 1.57),
    "NFL": TB1(2, 13.6, 13.4, 1.95), "AFL": TB1(2, 36.8, 29.1, 6.57), "NRL": TB1(2, 19.9, 13.9, 1.91),
    "Premier League": TB1(2, None, None, 0.30, poisson=True), "NHL": TB1(20, 2.57, 2.29, 0.13),
    "MLB": TB1(20, 4.57, 4.50, 0.07),
}
# Toolkit §4.3 "Other competitions": nearest sport's constants, printed as TEAM_BASELINE_P (UNVALIDATED:<league>)
TB1_NEAREST = {"Soccer": "Premier League", "Basketball48": "NBA", "Basketball40": "NBL", "AFL": "AFL",
               "State Level AFL": "AFL", "American Football": "NFL", "College Football": "NFL",
               "Canadian Football": "NFL", "Rugby League": "NRL", "Ice Hockey": "NHL", "Baseball": "MLB"}

# Sport rules: engine, endpoint and the tie (extra-time) rule. Facts of the sport, not fitted.
SPORT_RULES = {
    "Soccer": dict(engine="dixon_coles", endpoint="REGULATION_90", tie_rule="draw", code="SOC", tag="DC"),
    "Basketball": dict(engine="gaussian", endpoint="FULL_GAME_INCL_OT", tie_rule="overtime", code="BKB", tag="JOINT"),
    "AFL": dict(engine="gaussian", endpoint="FULL_GAME", tie_rule="draw", code="AUS", tag="JOINT"),
    "State Level AFL": dict(engine="gaussian", endpoint="FULL_GAME", tie_rule="draw", code="AUSST", tag="JOINT"),
    "American Football": dict(engine="gaussian", endpoint="FULL_GAME_INCL_OT", tie_rule="overtime_residual",
                              winner_bonus=3, extra_fraction=1 / 6, code="AMF", tag="JOINT"),
    "College Football": dict(engine="gaussian", endpoint="FULL_GAME_INCL_OT", tie_rule="overtime_residual",
                             winner_bonus=3, extra_fraction=1 / 6, code="CFB", tag="JOINT"),
    "Canadian Football": dict(engine="gaussian", endpoint="FULL_GAME_INCL_OT", tie_rule="overtime_residual",
                              winner_bonus=3, extra_fraction=1 / 6, code="CFL", tag="JOINT"),
    "Rugby League": dict(engine="gaussian", endpoint="FULL_GAME_INCL_GOLDEN_POINT", tie_rule="overtime_residual",
                         winner_bonus=1, extra_fraction=1 / 8, code="RL", tag="JOINT"),
    "Rugby Union": dict(engine="gaussian", endpoint="FULL_GAME", tie_rule="draw", code="RU", tag="JOINT"),
    "Ice Hockey": dict(engine="count", endpoint="FULL_GAME_INCL_OT_SO", tie_rule="hockey_regulation",
                       winner_bonus=1, code="IH", tag="REG"),
    "Baseball": dict(engine="count", endpoint="FULL_GAME_INCL_EXTRAS", tie_rule="extras", winner_bonus=1,
                     negbin=True, code="BSB", tag="NB"),
    "Cricket T20": dict(engine="cricket", endpoint="FIRST_INNINGS_FULL_LENGTH", overs_cap=20.0, code="CRT20", tag="FI"),
    "Cricket One-Day Format": dict(engine="cricket", endpoint="FIRST_INNINGS_FULL_LENGTH", overs_cap=50.0,
                                   code="CROD", tag="FI"),
    "Cricket Tests": dict(engine="cricket_multiday", code="CRTEST", tag="FI"),
    "Tennis": dict(engine="unsupported", code="TEN", tag="NA"),
    "Hockey": dict(engine="unsupported", code="FH", tag="NA"),
}

OVERRIDES = {  # facts a results file cannot show
    "Basketball/NBA": dict(aliases={"LA Clippers": "Los Angeles Clippers"}),
    "American Football/NFL": dict(aliases={
        "Washington Redskins": "Washington Commanders", "Washington Football Team": "Washington Commanders",
        "Oakland Raiders": "Las Vegas Raiders", "San Diego Chargers": "Los Angeles Chargers",
        "St. Louis Rams": "Los Angeles Rams"}),
    "Ice Hockey/NHL": dict(aliases={"Arizona Coyotes": "Utah Mammoth", "Utah Hockey Club": "Utah Mammoth"}),
    "Baseball/MLB": dict(aliases={"Cleveland Indians": "Cleveland Guardians", "Oakland Athletics": "Athletics"}),
    "Cricket T20/IPL": dict(aliases={"Delhi Daredevils": "Delhi Capitals", "Kings XI Punjab": "Punjab Kings",
                                     "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
                                     "Rising Pune Supergiants": "Rising Pune Supergiant"}),
    "Soccer/Premier League": dict(promoted_prior=True),
}

ALIAS_FOLDERS = {  # ACTIVE_FILE_INDEX §2: byte-identical copies, never aggregated
    "American Football/College Football": "College Football/NCAA Division I FBS",
    "Basketball/BSL": "Basketball/Austria Basketball Bundesliga",
    "Cricket One-Day Format/Men's ODI International": "Cricket One-Day Format/ODI International",
    "Ice Hockey/Metal Ligaen": "Ice Hockey/Danish Metal Ligaen",
}


@dataclass(frozen=True)
class League:
    path: str                      # "<Sport>/<Competition>"
    sport: str
    competition: str
    model_id: str
    engine: str
    endpoint: str = "FULL_GAME"
    tie_rule: str = "draw"
    extra_fraction: float = 0.0
    winner_bonus: int = 1
    negbin: bool = False
    promoted_prior: bool = False
    overs_cap: float | None = None
    history_seasons: int = 3
    tune_seasons: tuple[int, ...] = ()
    test_seasons: tuple[int, ...] = ()
    eval_stages: tuple[str, ...] = ("REG",)
    tb1: TB1 | None = None
    tb1_label: str = "NONE"
    aliases: dict = field(default_factory=dict)
    columns: dict = field(default_factory=dict)   # detected column names
    season_counts: dict = field(default_factory=dict)
    data_warnings: tuple[str, ...] = ()            # integrity gate (see integrity_warnings)

    @property
    def code(self) -> str:  # short name used in tables
        return self.competition


def slug(s: str) -> str:
    return re.sub(r"[^A-Z0-9]+", "-", s.upper()).strip("-")


def _first(header: list[str], *cands: str, prefix: tuple[str, ...] = ()) -> str | None:
    for c in cands:
        if c in header:
            return c
    for p in prefix:
        for h in header:
            if h.startswith(p):
                return h
    return None


def detect_columns(header: list[str]) -> dict:
    cols = {
        "home": _first(header, "Home", "Home Team"),
        "away": _first(header, "Away", "Away Team"),
        "home_score": _first(header, "Home Score", "Full Time Home Goals", "Home Goals"),
        "away_score": _first(header, "Away Score", "Full Time Away Goals", "Away Goals"),
        "score_text": _first(header, "Game Score", "Match Score"),
        "stage": _first(header, prefix=("Game Type", "Match Type")) or _first(header, "Season Phase"),
        "date": _first(header, "Date"),
        "id": _first(header, "Game ID", "Match ID", "Game ID (MLB gamePk)", "Native Game ID"),
        "total": _first(header, "Total Points", "Total Goals", "Total Runs"),
        "margin": _first(header, "Winning Margin"),
        "decision": _first(header, "Decision Type"),
        "overtime": _first(header, "Overtime", "Overtime Periods"),
        "shootout": _first(header, "Shootout", "Shootout Score (as printed)", "SO Home"),
        "extras": _first(header, "Extra Innings"),
        "period_format": _first(header, "Period Format"),
        # cricket
        "fi_team": _first(header, "First Innings Team", "Innings 1 Team"),
        "si_team": _first(header, "Second Innings Team", "Innings 2 Team"),
        "fi_runs": _first(header, "First Innings Runs", "Innings 1 Runs"),
        "fi_wkts": _first(header, "First Innings Wickets", "Innings 1 Wickets"),
        "fi_overs": _first(header, "First Innings Overs", "Innings 1 Overs"),
        "method": _first(header, "Method"),
        "venue": _first(header, "Venue"),
        "season_year": _first(header, "Season Year"),
    }
    if cols["home_score"] is None or cols["away_score"] is None:
        cols["parser"] = "text" if cols["score_text"] else None
    else:
        cols["parser"] = "columns"
    return cols


def _read_head(path: Path, sample_rows: int = 0) -> tuple[list[str], list[dict], int]:
    with open(path, newline="", encoding="utf-8-sig", errors="replace") as fh:
        r = csv.DictReader(fh)
        rows = list(r)
        return list(r.fieldnames or []), rows[:sample_rows] if sample_rows else rows, len(rows)


OT_SPORTS = {"Basketball", "Ice Hockey", "American Football", "College Football", "Canadian Football"}
# Sports where a 0-0 final is a genuine result: soccer, ice hockey (old-era ties). Everywhere else a 0-0 row is a
# placeholder (cancelled, postponed or unrecorded game), except a baseball row that records extra innings (a scoreless
# tie after extras, allowed in NPB and KBO).
ZERO_ZERO_GENUINE = {"Soccer", "Ice Hockey"}


def is_placeholder_zero(sport: str, hs: float, as_: float, extras_flag: bool) -> bool:
    if hs != 0 or as_ != 0 or sport in ZERO_ZERO_GENUINE:
        return False
    return not (sport == "Baseball" and extras_flag)


def integrity_warnings(sport: str, ot_recent: tuple[int, int, int], margins: dict[int, list[int]]) -> tuple[str, ...]:
    """Automatic plausibility checks on a competition's own rows. A blank field is missing data, not a warning.

    OVERTIME_FIELD_IMPLAUSIBLE: the overtime/decision field is explicitly filled on >= 90% of the last five seasons'
        rows (>= 500 games) yet shows extra time in < 1% of games. Genuine leagues in this archive show 4-25%
        (EuroCup 5.1%, KBL 3.7%, NHL ~23%); an always-'No' field is the default-value pattern of the fabricated
        builds quarantined on 2026-10-12 (ARCHIVE_USE_GUIDE §9 rule 4).
    IMPLAUSIBLE_SCORE_DISPERSION: a season with >= 30 games whose margin SD is below 0.4 x the competition's median
        season margin SD.
    """
    out = []
    n_rows, n_explicit, n_extra = ot_recent
    if sport in OT_SPORTS and n_explicit >= 500 and n_explicit >= 0.9 * n_rows and n_extra < 0.01 * n_explicit:
        out.append(f"OVERTIME_FIELD_IMPLAUSIBLE:{n_extra}/{n_explicit}")
    sds = {}
    for y, m in margins.items():
        if len(m) >= 30:
            mu = sum(m) / len(m)
            sds[y] = (sum((x - mu) ** 2 for x in m) / len(m)) ** 0.5
    if len(sds) >= 5:
        med = sorted(sds.values())[len(sds) // 2]
        low = sorted(y for y, v in sds.items() if v < 0.4 * med)
        if low:
            out.append(f"IMPLAUSIBLE_SCORE_DISPERSION:{','.join(map(str, low))}")
    return tuple(out)


@dataclass
class Discovery:
    league: League | None
    path: str
    status: str
    reason: str
    seasons: int
    rows: int


def _choose_seasons(counts: dict[int, int]) -> tuple[tuple[int, ...], tuple[int, ...], str]:
    """Contiguous recent seasons with a full-sized evaluation population; the last 3 test, the 2 before tune.

    A season with fewer than half the median of the last six non-empty seasons (a partial current season, a
    COVID-shortened season or an off-year placeholder) is not eligible for tune/test but still trains.
    """
    ys = sorted(y for y, n in counts.items() if n > 0)
    if not ys:
        return (), (), "no evaluation-stage rows"
    recent = [counts[y] for y in ys[-6:]]
    med = sorted(recent)[len(recent) // 2]
    floor = max(20, 0.5 * med)
    elig = [y for y in ys if counts[y] >= floor]
    if len(elig) < 3:
        return (), (), f"only {len(elig)} season(s) with >= {floor:.0f} evaluation games"
    test = tuple(elig[-3:])
    tune = tuple(elig[-5:-3]) if len(elig) >= 5 else tuple(elig[-len(elig):-3])
    if not tune:
        tune = (elig[-4],) if len(elig) >= 4 else ()
    if not tune:
        return (), (), f"{len(elig)} eligible seasons: no season left for tuning before the 3 test seasons"
    return tune, test, "ok"


def discover() -> list[Discovery]:
    return list(_discover_cached())


@__import__("functools").lru_cache(maxsize=128)
def _discover_cached(only_path: str | None = None) -> tuple:
    from ml.data.archive import stage_of, flag_state, missing_text, score_int  # local import: archive imports config

    out: list[Discovery] = []
    if not ARCHIVE.is_dir():
        return ()
    for sport_dir in sorted(p for p in ARCHIVE.iterdir() if p.is_dir() and not p.name.startswith("_")):
        sport = sport_dir.name
        if only_path is not None and sport != only_path.split("/", 1)[0]:
            continue
        rules = SPORT_RULES.get(sport)
        for comp_dir in sorted(p for p in sport_dir.iterdir() if p.is_dir()):
            path = f"{sport}/{comp_dir.name}"
            if only_path is not None and path != only_path:
                continue
            files = sorted(p for p in comp_dir.glob("*/*_games.csv") if p.parent.name.isdigit())
            counts, stage_counts, header, rows_total = {}, {}, None, 0
            md_counter: dict[str, int] = {}
            margins: dict[int, list[int]] = {}
            ot_rows: dict[int, list[int]] = {}
            for f in files:
                h, rows, n = _read_head(f)
                if n == 0:
                    continue
                header = h
                rows_total += n
                cols = detect_columns(h)
                y = int(f.parent.name)
                for r in rows:
                    tot = (r.get(cols["total"]) or "").strip() if cols["total"] else ""
                    hsv = (r.get(cols["home_score"]) or "").strip() if cols["home_score"] else ""
                    asv = (r.get(cols["away_score"]) or "").strip() if cols["away_score"] else ""
                    ext = bool(cols["extras"]) and (r.get(cols["extras"]) or "").strip().upper() in ("Y", "YES")
                    try:
                        zero = (is_placeholder_zero(sport, float(hsv), float(asv), ext) if hsv and asv
                                else (tot not in ("", "N/A") and float(tot) == 0 and sport not in ZERO_ZERO_GENUINE))
                    except ValueError:
                        zero = False
                    if zero:
                        continue  # placeholder rows never count towards a season's size
                    st = stage_of(r.get(cols["stage"], "")) if cols["stage"] else "REG"
                    stage_counts.setdefault(y, {}).setdefault(st, 0)
                    stage_counts[y][st] += 1
                    d = (r.get(cols["date"]) or "") if cols["date"] else ""
                    teams_ok = cols["home"] and (r.get(cols["home"]) or "").strip() not in ("", "N/A")
                    if teams_ok and re.match(r"^\d{4}-\d{2}-\d{2}", d):  # ISO dates of real games only
                        md_counter[d[5:10]] = md_counter.get(d[5:10], 0) + 1
                    if cols["home_score"] and cols["away_score"]:
                        try:
                            margins.setdefault(y, []).append(score_int(r[cols["home_score"]]) - score_int(r[cols["away_score"]]))
                        except (TypeError, ValueError):
                            pass
                    otc = cols["decision"] or cols["overtime"]
                    if otc and teams_ok:
                        v = (r.get(otc) or "").strip().lower()
                        acc = ot_rows.setdefault(y, [0, 0, 0])
                        acc[0] += 1
                        if not missing_text(v):
                            acc[1] += 1
                            acc[2] += flag_state(v) is True
            nseas = len(stage_counts)
            if rows_total == 0:
                out.append(Discovery(None, path, "NOT_MODELLED", "header-only folder (no data rows)", 0, 0))
                continue
            if path in ALIAS_FOLDERS:
                out.append(Discovery(None, path, "NOT_MODELLED",
                                     f"alias copy of {ALIAS_FOLDERS[path]} (ACTIVE_FILE_INDEX §2)", nseas, rows_total))
                continue
            if rules is None or rules["engine"] == "unsupported":
                out.append(Discovery(None, path, "NOT_MODELLED", f"no supported engine for sport '{sport}'", nseas,
                                     rows_total))
                continue
            if rules["engine"] == "cricket_multiday":
                out.append(Discovery(None, path, "NOT_MODELLED",
                                     "multi-day first-class cricket: first-innings totals mix declarations, follow-on "
                                     "and weather and need a separate session/declaration model (framework §8.4)",
                                     nseas, rows_total))
                continue
            per_season = [sum(v.values()) for v in stage_counts.values()]
            if per_season and max(per_season) <= 2:
                out.append(Discovery(None, path, "NOT_MODELLED",
                                     "single-game-per-season subset (e.g. a final); its games are modelled inside the "
                                     "parent competition", nseas, rows_total))
                continue
            top_md, top_n = max(md_counter.items(), key=lambda kv: kv[1]) if md_counter else ("", 0)
            n_dated = sum(md_counter.values())
            if n_dated >= 200 and top_n / n_dated > 0.25:
                out.append(Discovery(None, path, "NOT_MODELLED",
                                     f"SUSPECTED_DEFAULT dates: {top_n}/{n_dated} dated rows on month-day {top_md}; "
                                     "the known-at rule cannot be applied", nseas, rows_total))
                continue
            cols = detect_columns(header)
            required = ("fi_team", "si_team", "fi_runs", "fi_wkts", "fi_overs", "date") if rules["engine"] == "cricket" else ("home", "away", "date", "parser")
            if any(cols[key] is None for key in required):
                out.append(Discovery(None, path, "NOT_MODELLED", "missing required columns: " + ",".join(key for key in required if cols[key] is None), nseas,
                                     rows_total))
                continue
            reg_total = sum(v.get("REG", 0) for v in stage_counts.values())
            eval_stages = ("REG",) if reg_total >= 0.5 * rows_total else ("REG", "POST")
            counts = {y: sum(v.get(s, 0) for s in eval_stages) for y, v in stage_counts.items()}
            tune, test, why = _choose_seasons(counts)
            comp = comp_dir.name
            ov = OVERRIDES.get(path, {})
            extra_fraction = rules.get("extra_fraction", 0.0)
            tb_key = None
            if sport == "Basketball":
                fmt = ""
                if cols["period_format"]:
                    _, sample, _ = _read_head(files[-1], 50)
                    fmt = " ".join(r.get(cols["period_format"], "") for r in sample)
                is48 = "12-minute" in fmt or "48" in fmt
                extra_fraction = 5 / 48 if is48 else 5 / 40
                tb_key = "Basketball48" if is48 else "Basketball40"
            if comp in TB1_VALIDATED and (sport, comp) != ("AFL", "AFLW"):
                tb1, tb1_label = TB1_VALIDATED[comp], "VALIDATED"
            elif rules["engine"] != "cricket":
                near = TB1_NEAREST.get(tb_key or sport)
                tb1 = TB1_VALIDATED.get(near) if near else None
                tb1_label = f"CALIBRATED_PREV_EDITION(k:{near})" if tb1 else "NONE"
            else:
                tb1, tb1_label = None, "NONE"
            elig_years = sorted(y for y, n in counts.items() if n >= 20)
            gaps = sorted(b - a for a, b in zip(elig_years, elig_years[1:])) or [1]
            history = 3 * max(1, gaps[len(gaps) // 2])  # three editions: 3 seasons for a league, ~9-12 years for a quadrennial
            mid = f"{rules['code']}-{slug(comp)}-{rules['tag']}-r1"
            recent = sorted(ot_rows)[-5:]
            ot_recent = tuple(sum(ot_rows[y][i] for y in recent) for i in range(3)) if recent else (0, 0, 0)
            warnings = integrity_warnings(sport, ot_recent, margins)
            lg = League(path=path, sport=sport, competition=comp, model_id=mid, engine=rules["engine"],
                        endpoint=rules.get("endpoint", "FULL_GAME"), tie_rule=rules.get("tie_rule", "draw"),
                        extra_fraction=extra_fraction, winner_bonus=rules.get("winner_bonus", 1),
                        negbin=rules.get("negbin", False), promoted_prior=ov.get("promoted_prior", False),
                        overs_cap=rules.get("overs_cap"), history_seasons=history, tune_seasons=tune, test_seasons=test,
                        eval_stages=eval_stages, tb1=tb1, tb1_label=tb1_label, aliases=ov.get("aliases", {}),
                        columns=cols, season_counts=counts, data_warnings=warnings)
            if why != "ok":
                out.append(Discovery(lg, path, "NOT_MODELLED", f"insufficient history: {why}", nseas, rows_total))
            else:
                out.append(Discovery(lg, path, "MODELLED", "ok", nseas, rows_total))
    return tuple(out)


def get_league(path: str) -> League:
    # Per-event inference need not parse every other sport's archive. Retain
    # exactly the same discovery checks/configuration for the requested scope.
    for d in _discover_cached(path):
        if d.path == path and d.league is not None:
            return d.league
    raise KeyError(path)
