"""Full-history card table and retrospective summaries (prompt 6, LEARN-v1 §7) — reproducible, never hand counts.

Builds one row per (card, original rank) from the committed records, without re-grading anything:

    GAME_PREDICTION_RANK_LOG.csv                      literal ranks/grades/stated p, P-001 onward (with source lines)
    HISTORICAL_PRIMARY_RECONCILIATION.csv             effective final-settlement Rank 1/2 grades P-126–P-576
                                                      (cross-check; a disagreement is reported and the effective
                                                      grade wins for Ranks 1–2)
    mini_import_*/ inventories                       discovered at run time; supported historical and local-key
                                                      schemas, with research-only probabilities kept NOT_PRIMARY

Each card gets a date (first ISO date in its original block, else the status register), an era (date windows that
follow documented policy changes), a sport and a proposition family (keyword rules, with UNCLASSIFIED counted, never
guessed further). Summaries: slot win rates, card classes, calibration bins, Brier and logistic calibration, ISO-week
clustered intervals of the Rank-1 rate against its own stated probability, sport/family/era cells and stated-p bands.
Everything is descriptive and outcome-exposed: no gate, model or grade is changed.
"""
from __future__ import annotations

import argparse
import math
import re
import secrets
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from ml.core.metrics import calibration_fit, iso_week, paired_week_interval, wilson

ROOT = Path(__file__).resolve().parents[2]
V = ROOT / "research" / "verification"
RANK_LOG = ROOT / "GAME_PREDICTION_RANK_LOG.csv"
RECON = V / "mini_import_P-577_P-584_2026-10-13-1" / "HISTORICAL_PRIMARY_RECONCILIATION.csv"
STATUS = ROOT / "GAME_LOG_STATUS_CURRENT.md"
NOT_PRIMARY = {"LEGACY_ANALYST_NOT_PRIMARY", "RESEARCH_ONLY_NOT_PRIMARY"}


def combined_logs() -> list[Path]:
    """Discover numbered parts, excluding backup names; do not stop at a former active part."""
    pattern = re.compile(r"PREDICTION_LOG_COMBINED(?:_(\d+))?\.md$")
    paths = [(int(m.group(1) or 1), p) for p in (ROOT / "prediction logs").glob("*.md")
             if (m := pattern.fullmatch(p.name))]
    return [p for _, p in sorted(paths)]


def import_inventories() -> list[Path]:
    paths = []
    for folder in sorted(V.glob("mini_import_*")):
        if not folder.is_dir():
            continue
        effective = folder / "EFFECTIVE_SETTLEMENT_ROWS.csv"
        original = folder / "IMPORTED_ROW_INVENTORY.csv"
        if effective.exists():
            paths.append(effective)
        elif original.exists():
            paths.append(original)
    return paths

ERAS = (("E1a", "2026-07-01", "2026-09-08"), ("E1b", "2026-09-09", "2026-09-24"), ("E2", "2026-09-25", "2026-10-08"),
        ("E3", "2026-10-09", "2026-10-11"), ("E4", "2026-10-12", "2026-12-31"))
TEAMS = (  # unambiguous club names, checked before generic keywords (first match wins)
    ("Rugby League", ("brisbane broncos", "melbourne storm", "sydney roosters", "rabbitohs", "manly", "sea eagles",
                      "penrith panthers", "cronulla", "parramatta", "canberra raiders", "newcastle knights",
                      "north queensland cowboys", "gold coast titans", "st george illawarra", "new zealand warriors",
                      "canterbury-bankstown", "wests tigers", "dolphins (nrl)")),
    ("Australian Rules", ("west coast eagles", "hawthorn", "collingwood", "carlton", "essendon", "richmond", "geelong",
                          "fremantle", "sydney swans", "gws", "brisbane lions", "gold coast suns", "port adelaide",
                          "adelaide crows", "melbourne demons", "north melbourne", "st kilda", "western bulldogs")),
    ("Baseball", ("diamondbacks", "guardians", "padres", "nationals", "orioles", "astros", "mets", "red sox", "yankees",
                  "rockies", "braves", "brewers", "phillies", "marlins", "dodgers", "cubs", "pirates", "royals",
                  "white sox", "mariners", "athletics", "angels", "blue jays", "rays", "reds ", "twins @", "twins at",
                  "fighters", "marines", "chunichi", "hanshin", "golden eagles", "buffaloes", "swallows", "baystars",
                  "carp", "seibu", "softbank", "yomiuri", "doosan", "kt wiz", "landers", "kiwoom", "nc dinos",
                  "hanwha", "lotte", "samsung lions", "kia tigers", "lg twins")),
    ("American Football", ("falcons", "dolphins", "buccaneers", "jaguars", "seahawks", "broncos", "chiefs", "patriots",
                           "ravens", "steelers", "bengals", "browns", "texans", "colts", "raiders", "chargers",
                           "cowboys", "commanders", "packers", "vikings", "saints", "49ers", "giants @ jets")),
    ("Basketball", ("sun @ fever", "fever", "liberty", "mercury", "lynx", "valkyries", "sparks", "mystics",
                    "aces @", "@ aces", "sky @", "@ sky", "wings @", "@ wings", "dream @", "@ dream")),
)
SPORTS = (  # first match wins; keywords are lower-case substrings of event + contract text
    *TEAMS,
    ("Rugby Union", ("sevens", "npc round", "hilux npc")),
    ("American Football", ("meac/swac", "ncaa fbs", "ncaa fcs")),
    ("Basketball", ("lnbp", "hapoel tel aviv vs real madrid")),
    ("American Football", ("ncaa football",)),
    ("Baseball", ("uni-lions", "cpbl", "sultanes", "toros", "lmb", "pcl")),
    ("Cricket", ("overs", "first six", "etpl", "tri-series", "pp over", "pp under")),
    ("Soccer", ("brazil série", "série a", "first division", "club brugge", "boca juniors", "lanús", "necaxa", "cruz azul",
                "corinthians", "flamengo", "rapids", "gotham", "nwsl", "1h over 0.5",
                "1h under", "manchester city", "yunnan", "chongqing")),
    ("Ice Hockey", ("hc saryarka", "arlan kokshetau")),
    ("Tennis", (".5 games", "atp ", "wta ", "itf ", "tennis", "challenger", "total games", "aggregate games", " games —", "sets ",
                "set handicap", "us open", "roland", "wimbledon", "grand slam", "davis cup", "billie jean")),
    ("Cricket", ("cricket", "t20", "odi", "test match", "the hundred", "ipl", "cpl", "bbl ", "wbbl", "100-ball",
                 "powerplay", "innings", "wickets", "sheffield shield", "county championship", "psl")),
    ("Australian Rules", ("afl", "aflw", "vfl", "sanfl", "wafl")),
    ("Rugby League", ("nrl", "rugby league", "super league", "state of origin", "nrlw")),
    ("Rugby Union", ("rugby union", "super rugby", "six nations", "top 14", "premiership rugby", "urc ", "rugby championship")),
    ("American Football", ("nfl", "ncaaf", "college football", "cfl", "touchdown")),
    ("Ice Hockey", ("nhl", "khl", "shl", "liiga", "extraliga", "hockey", " ahl ", "puck", "goalie", "metal ligaen", "pucks")),
    ("Baseball", ("mlb", "kbo", "npb", "cpbl", "lmb", "baseball", "run line", "runs", "innings pitched", "strikeouts", "f5")),
    ("Basketball", ("nba", "wnba", "nbl", "basket", "euroleague", "eurocup", "acb", "liga endesa", "b.league", "b.premier",
                    "kbl", "fiba", "lkl", "aba ", "bbl", "korisliiga", "points", "rebounds", "assists")),
    ("Soccer", ("soccer", "football club", " fc", "fc ", "uefa", "premier league", "liga", "serie a", "bundesliga",
                "ligue 1", "eredivisie", "mls", "cup", "goals", "corners", "btts", "both teams", "draw", "half-time",
                "first half", "afc ", "conmebol", "libertadores", "sudamericana", "a-league", "j1", "k league")),
    ("Soccer", ("women v", "women vs", "friendly")),
)
FAMILIES = (
    ("CORNERS", r"corner"), ("CARDS", r"\bcards?\b|booking"),
    ("PERIOD", r"first[- ]half|\b1h\b|half-time|halftime|first[- ]\d+[- ]balls|powerplay|\bpp\b|first period|1st period|"
               r"quarter|\bq[1-4]\b|first five|\bf5\b|first inning(?!s)|second half|\b2h\b|set 1|first set|first six|"
               r"\d+ overs"),
    ("PLAYER", r"strikeouts|rebounds|assists|disposals|tries scorer|anytime|player|\d\+? aces\b|aces (over|under)|shots on (goal|target)|"
               r"\d\+ (goals?|wickets?|sot)|\bsot\b|\bouts\b|(?<!innings )\b\d{2,3}\+$"),
    ("BTTS", r"btts|both teams"),
    ("HANDICAP", r"(?<![pP])[+\-−–]\s?\d+(\.\d+)?\b(?!\s*(runs?|goals?|points?)\s*(over|under))|handicap|spread|run ?line|puck ?line"),
    ("TOTAL", r"\bover\b|\bunder\b|\btotal\b|(^|\s)[ou]\s?\d"),
    ("WINNER", r"\bml\b|moneyline|to win|\bwins?\b|winner|double chance|\b1x\b|\bx2\b|\b12\b|draw no bet|\bdnb\b|\bdraw\b"),
)


def card_num(card: str) -> int:
    return int(re.search(r"P-(\d+)", card).group(1))


PREFIX = re.compile(r"^\s*(baseball|basketball|soccer|football \(soccer\)|ice hockey|tennis|cricket|american football|"
                    r"australian rules(?: football)?|afl|aflw|rugby league|rugby union|nrl)\s*/", re.I)
PREFIX_MAP = {"football (soccer)": "Soccer", "australian rules": "Australian Rules", "australian rules football": "Australian Rules",
              "afl": "Australian Rules", "aflw": "Australian Rules", "nrl": "Rugby League"}
# Manual classification from the event text where players/clubs identify the sport unambiguously (reviewed by hand,
# 2026-10-16). Events whose sport is genuinely uncertain stay UNCLASSIFIED.
OVERRIDES = {"P-241": "Tennis", "P-242": "Tennis", "P-243": "Tennis", "P-254": "Tennis", "P-263": "Tennis",
             "P-267": "Tennis", "P-272": "Tennis", "P-152": "Soccer", "P-309": "American Football",
             "P-359": "Basketball", "P-360": "Basketball"}


def classify_sport(text: str) -> str:
    m = PREFIX.match(str(text))
    if m:
        key = m.group(1).lower()
        return PREFIX_MAP.get(key, key.title() if key != "ice hockey" else "Ice Hockey")
    t = " " + str(text).lower() + " "
    for sport, keys in SPORTS:
        if any(k in t for k in keys):
            return sport
    return "UNCLASSIFIED"


def classify_family(contract: str) -> str:
    t = str(contract).lower()
    for fam, pattern in FAMILIES:
        if re.search(pattern, t):
            return fam
    return "OTHER"


def era_of(date) -> str:
    if date is None or (isinstance(date, float) and math.isnan(date)) or pd.isna(date):
        return "UNDATED"
    d = pd.Timestamp(date).strftime("%Y-%m-%d")
    for name, lo, hi in ERAS:
        if lo <= d <= hi:
            return name
    return "UNDATED"


def _grade(value) -> str:
    v = str(value).strip().upper()
    if v in {"WIN", "LOSS", "PUSH", "VOID", "UNRESOLVED", "CONFLICT"}:
        return v
    return {"W": "WIN", "L": "LOSS", "P": "PUSH", "V": "VOID", "U": "UNRESOLVED"}.get(v, "CONFLICT" if "/" in v else "UNRESOLVED")


def _p(value):
    try:
        x = float(str(value).strip().rstrip("%"))
    except ValueError:
        return math.nan
    if x > 1:
        x /= 100
    return x if 0 <= x <= 1 else math.nan


def _event_date(text):
    """This card history begins in 2026; earlier biographical/source dates are not card dates."""
    first_year = min(int(start[:4]) for _, start, _ in ERAS)
    for match in re.finditer(r"\b(\d{4}-(?:0[1-9]|1[0-2])-[0-3]\d)\b", text):
        if int(match.group(1)[:4]) >= first_year:
            return match.group(1)
    return None


def card_dates(logs=None, status=STATUS) -> dict:
    """card -> (date, basis). First ISO date within 60 lines after the card's first original heading."""
    logs = combined_logs() if logs is None else logs
    out = {}
    head = re.compile(r"^#{1,4} .{0,8}P-(\d{3,})\b")
    for path in logs:
        if not Path(path).exists():
            continue
        lines = Path(path).read_text(encoding="utf-8", errors="replace").split("\n")
        for i, line in enumerate(lines):
            m = head.match(line)
            if not m:
                continue
            card = f"P-{m.group(1)}"
            if card in out:
                continue
            for j in range(i, min(i + 60, len(lines))):
                d = _event_date(lines[j])
                if d:
                    out[card] = (d, f"{Path(path).name}:{j + 1}")
                    break
    if Path(status).exists():
        for line in Path(status).read_text(encoding="utf-8", errors="replace").split("\n"):
            m = re.match(r"^\| \*\*(P-\d{3,})\*\* \| (.*?) \|", line)
            if m and m.group(1) not in out:
                d = _event_date(m.group(2))
                if d:
                    out[m.group(1)] = (d, "GAME_LOG_STATUS_CURRENT.md")
    return out


def fallback_dates(R: pd.DataFrame, found: dict, logs=None) -> dict:
    """For undated cards: nearest date to the card's own grade-source line, else to its first mention (labelled)."""
    logs = combined_logs() if logs is None else logs
    texts = {Path(p).name: Path(p).read_text(encoding="utf-8", errors="replace").split("\n") for p in logs if Path(p).exists()}
    out = {}

    def nearest(lines, i, before=80, after=20):
        for k in range(0, max(before, after)):
            for j in (i - k, i + k):
                if 0 <= j < len(lines) and (i - before) <= j <= (i + after):
                    d = _event_date(lines[j])
                    if d:
                        return d
        return None

    for card, src in R.drop_duplicates("card")[["card", "source"]].itertuples(index=False):
        if card in found:
            continue
        m = re.match(r"(PREDICTION_LOG_COMBINED(?:_\d+)?\.md):(\d+)$", str(src))
        if m and m.group(1) in texts:
            d = nearest(texts[m.group(1)], int(m.group(2)) - 1)
            if d:
                out[card] = (d, f"NEAR_GRADE_SOURCE:{m.group(1)}:{m.group(2)}")
                continue
        token = re.compile(re.escape(card) + r"(?![\d–\-])")
        for name, lines in texts.items():
            hit = next((i for i, ln in enumerate(lines) if token.search(ln)), None)
            if hit is not None:
                d = nearest(lines, hit, before=10, after=40)
                if d:
                    out[card] = (d, f"NEAR_FIRST_MENTION:{name}:{hit + 1}")
                    break
    return out


def id_collisions(logs=None) -> pd.DataFrame:
    """IDs whose original-card headings name more than one distinct event (historical duplicate allocations)."""
    logs = combined_logs() if logs is None else logs
    head = re.compile(r"^#{1,4} .{0,8}`?P-(\d{3,})`?(?: \([^)]*\))? — (.{0,60})")
    seen = {}
    for path in logs:
        if not Path(path).exists():
            continue
        for line in Path(path).read_text(encoding="utf-8", errors="replace").split("\n"):
            m = head.match(line)
            if not m:
                continue
            title = re.sub(r"[`*]", "", m.group(2)).strip().lower()
            if re.match(r"(settlement|retrospective|deep|addendum|r1[^0-9]|revision|correction|post-|import)", title) \
                    or re.search(r"\d+\s*[-–]\s*\d+|\d+;|settle|retro|result|final score", title) \
                    or re.match(r"(#|both top|original rank|retained historical|successful|\d+ under)", title):
                continue  # result/settlement headings name the same event with its score
            key = re.sub(r"[^a-z]", "", title)[:18]
            seen.setdefault(f"P-{m.group(1)}", {}).setdefault(key, (Path(path).name, title))
    stop = {"women", "live", "hold", "pregame", "forecast", "preseason", "regular", "season", "league", "match",
            "round", "final", "game", "card", "with", "from", "late", "import", "original", "united", "city"}

    def words(title):
        return {w for w in re.findall(r"[a-zà-ÿ]{4,}", title) if w not in stop}

    rows = []
    for c, v in sorted(seen.items()):
        titles = list(v.values())
        groups = []  # same event if titles share a significant word (e.g. a team name)
        for f, t in titles:
            for g in groups:
                if words(t) & g["words"]:
                    g["words"] |= words(t)
                    g["titles"].append((f, t))
                    break
            else:
                groups.append(dict(words=words(t), titles=[(f, t)]))
        if len(groups) > 1:
            rows.append(dict(card=c, events=len(groups),
                             titles=" || ".join(f"{g['titles'][0][1]} ({g['titles'][0][0]})" for g in groups)))
    return pd.DataFrame(rows, columns=["card", "events", "titles"])


def inventory_rows(path: Path) -> list[dict]:
    """Read an admitted import layout. Unknown layouts/roles fail instead of dropping cards."""
    frame = pd.read_csv(path, dtype=str, keep_default_na=False)
    columns = set(frame.columns)
    local = {"canonical_id", "local_key", "probability_role", "original_rank", "original_contract",
             "original_probability", "sporting_grade", "effective_revision", "evidence_class", "note"}
    legacy = {"event_id", "event", "original_contract", "original_analyst_p", "original_rank_type", "sporting_grade"}
    supplied = {"id", "rank", "proposition", "grade", "p_numeric", "baseline_numeric"}
    original = {"id", "rank", "proposition", "grade", "p", "baseline"}
    layout = next((name for name, required in (("local", local), ("legacy", legacy),
                    ("supplied", supplied), ("original", original)) if required <= columns), None)
    if layout is None:
        raise ValueError(f"Unsupported import inventory schema: {path}")
    mapping = path.parent / "LOCAL_ID_MAPPING.csv"
    events = {}
    if layout == "local" and mapping.exists():
        meta = pd.read_csv(mapping, dtype=str, keep_default_na=False)
        if not {"canonical_id", "event"} <= set(meta.columns) or meta.canonical_id.duplicated().any():
            raise ValueError(f"Invalid or duplicate canonical mapping: {mapping}")
        events = dict(zip(meta.canonical_id, meta.event))
    order = {"ORIGINAL_RANK_1": 1, "ORIGINAL_RANK_2": 2, "ORIGINAL_RANK_2_INFORMATIONAL": 2,
             "ORIGINAL_RANK_3": 3, "ORIGINAL_RANK_4": 4}
    rows = []
    for line, r in enumerate(frame.to_dict("records"), 2):
        row = dict(event="", q=math.nan, baseline=math.nan, local_key="", probability_role="",
                   effective_revision="", evidence="", record_status="IMPORTED_CONDITIONAL_SPORTING_REVIEW",
                   source=f"{_label(path)}:{line}")
        if layout == "local":
            role = r["probability_role"]
            primary = role == "ANALYST_PRIMARY_V1" or role.startswith("ANALYST_PRIMARY_V1 ")
            research = role == "ANALYST_NOT_PRIMARY" or role.startswith("ANALYST_NOT_PRIMARY ")
            if not (primary or research):
                raise ValueError(f"Unsupported probability role at {path}:{line}: {role}")
            rank = r["original_rank"]
            if primary and rank != "-" and (not rank.isdigit() or int(rank) < 1):
                raise ValueError(f"Invalid original primary rank at {path}:{line}")
            baseline = re.fullmatch(r"BASELINE_P\s+([01](?:\.\d+)?)", r["note"].strip())
            row.update(card=r["canonical_id"], rank=int(rank) if primary and rank.isdigit() else 0,
                       contract=r["original_contract"], event=events.get(r["canonical_id"], ""),
                       grade=_grade(r["sporting_grade"]), p=_p(r["original_probability"]),
                       baseline=_p(baseline.group(1)) if baseline else math.nan,
                       grade_basis=role, cohort="ANALYST_PRIMARY_V1" if primary else "RESEARCH_ONLY_NOT_PRIMARY",
                       probability_role=role, local_key=r["local_key"],
                       effective_revision=r["effective_revision"], evidence=r["evidence_class"])
        elif layout == "legacy":
            kind = r["original_rank_type"]
            row.update(card=r["event_id"], rank=order.get(kind, 0), contract=r["original_contract"], event=r["event"],
                       grade=_grade(r["sporting_grade"]), p=_p(r["original_analyst_p"]), grade_basis=kind,
                       cohort="LEGACY_ORIGINAL_RANK" if kind in order else "LEGACY_ANALYST_NOT_PRIMARY")
        else:
            row.update(card=r["id"], rank=int(r["rank"]), contract=r["proposition"], grade=_grade(r["grade"]),
                       p=_p(r["p_numeric"] if layout == "supplied" else r["p"]),
                       baseline=_p(r["baseline_numeric"] if layout == "supplied" else r["baseline"]),
                       grade_basis="IMPORTED_ROW_INVENTORY",
                       cohort="SUPPLIED_FIRST_V1" if layout == "supplied" else "IMPORT_P577_P582")
        if not re.fullmatch(r"P-\d+", row["card"]) or not row["contract"].strip():
            raise ValueError(f"Missing/invalid card or contract at {path}:{line}")
        rows.append(row)
    keys = [(r["card"], r["rank"], r["contract"]) for r in rows]
    if len(keys) != len(set(keys)):
        raise ValueError(f"Duplicate effective contract rows: {path}")
    return rows


def build_rows(rank_log: Path = RANK_LOG, *, inventories=None, logs=None) -> tuple[pd.DataFrame, pd.DataFrame]:
    """(rows, reconciliation) — one row per card x original rank, plus effective-grade cross-check.

    Inventory rows are appended only for cards the rank log does not already contain, so a refreshed rank log that
    already carries P-585 onward is never double counted.
    """
    g = pd.read_csv(rank_log, encoding="utf-8-sig", dtype=str)
    rows = []
    for r in g.itertuples():
        rows.append(dict(card=r.card_id, rank=int(r.rank) if str(r.rank).isdigit() else 0, contract=r.selection_or_contract, event=r.event,
                         grade=_grade(r.logged_result), p=_p(r.stated_p), q=_p(r.ranking_q),
                         record_status=r.record_status, grade_basis=r.grade_basis, source=r.grade_source,
                         cohort="RANK_LOG_LITERAL", baseline=math.nan))
    R = pd.DataFrame(rows)
    # Cross-check Ranks 1-2 with the effective final-settlement reconciliation (P-126..P-576).
    recon = pd.read_csv(RECON, dtype=str)
    recon["grade_eff"] = recon.literal_grade.map(_grade)
    # An issued alias is not a unique event. Never transfer a settlement across collided P-IDs.
    logs = combined_logs() if logs is None else logs
    collided = set(id_collisions(logs).card)
    recon = recon[~recon.id.isin(collided)]
    merged = R.merge(recon[["id", "rank", "grade_eff"]].rename(columns={"id": "card"}).assign(rank=lambda d: d["rank"].astype(int)),
                     on=["card", "rank"], how="left")
    diff = merged[merged.grade_eff.notna() & (merged.grade_eff != merged.grade)][["card", "rank", "grade", "grade_eff"]]
    R = merged.assign(grade=np.where(merged.grade_eff.notna(), merged.grade_eff, merged.grade)).drop(columns="grade_eff")
    # Imported cards after the rank log (P-584 pending: absent by design).
    have = set(R.card)
    extra = []
    owners = {}
    for path in import_inventories() if inventories is None else inventories:
        imported = inventory_rows(path)
        all_cards = {r["card"] for r in imported}
        # Local-key imports carry the original probability role. A refreshed rank log must not erase it.
        for r in imported:
            if r["card"] not in have or r["cohort"] not in {"ANALYST_PRIMARY_V1", "RESEARCH_ONLY_NOT_PRIMARY"}:
                continue
            match = (R.card == r["card"]) & (R["rank"] == r["rank"]) & (R.contract == r["contract"])
            if not match.any():
                extra.append(r)
                continue
            if match.sum() != 1 or R.loc[match, "grade"].iloc[0] != r["grade"] \
                    or not np.isclose(R.loc[match, "p"].iloc[0], r["p"], equal_nan=True, rtol=0, atol=1e-12):
                raise ValueError(f"Rank log disagrees with local import; reconcile {r['card']}: {r['contract']}")
            for key in ("cohort", "baseline", "local_key", "probability_role", "effective_revision", "evidence", "grade_basis"):
                R.loc[match, key] = r[key]
        cards = all_cards - have
        overlap = all_cards & owners.keys()
        if overlap:
            raise ValueError(f"Overlapping import inventories require explicit reconciliation: {sorted(overlap)}; {path}")
        owners.update({card: path for card in all_cards})
        extra.extend(r for r in imported if r["card"] in cards)
    R = pd.concat([R, pd.DataFrame(extra)], ignore_index=True)
    R["identity_status"] = np.where(R.card.isin(collided), "COLLIDING_ALIAS_GRADE_LINK_UNRESOLVED", "NO_DETECTED_ALIAS_COLLISION")
    R["literal_grade"] = R.grade
    R.loc[R.card.isin(collided), "grade"] = "UNRESOLVED"
    # Imported P-577..P-582 rows also exist in the rank log; prefer the rank-log row and record agreement.
    R["n"] = R.card.map(card_num)
    R["informational_r2"] = (R.grade_basis == "ORIGINAL_RANK_2_INFORMATIONAL")
    events = R.groupby("card").event.agg(lambda s: next((x for x in s if isinstance(x, str) and x.strip()), ""))
    R["sport"] = [classify_sport(f"{events[c]} {k}") for c, k in zip(R.card, R.contract)]
    def vote(s: pd.Series) -> str:  # most common classified sport across the card's rows
        known = s[s != "UNCLASSIFIED"]
        return known.value_counts().index[0] if len(known) else "UNCLASSIFIED"
    R["sport"] = R.card.map(R.groupby("card").sport.agg(vote))
    R["sport"] = [OVERRIDES.get(c, s) for c, s in zip(R.card, R.sport)]
    R["family"] = R.contract.map(classify_family)
    dates = card_dates(logs)
    dates.update(fallback_dates(R, dates, logs))
    R["date"] = R.card.map(lambda c: dates.get(c, (None, ""))[0])
    R["date_basis"] = R.card.map(lambda c: dates.get(c, (None, "NOT_FOUND"))[1])
    R["era"] = R.date.map(era_of)
    R["week"] = [iso_week(pd.Series([pd.Timestamp(d)])).iloc[0] if isinstance(d, str) else "UNDATED" for d in R.date]
    R["y"] = R.grade.map({"WIN": 1.0, "LOSS": 0.0})
    R["counted_slot"] = R["rank"].isin([1, 2]) & ~R.informational_r2 & ~R.cohort.isin(NOT_PRIMARY)
    return R.sort_values(["n", "rank"]).reset_index(drop=True), diff


# ------------------------------------------------------------------------------------------------- summaries
def _rate(d: pd.DataFrame) -> str:
    k, n = int(d.y.sum()), int(d.y.notna().sum())
    if not n:
        return "—"
    lo, hi = wilson(k, n)
    return f"{k}–{n - k} ({100 * k / n:.1f}%, {100 * lo:.1f}–{100 * hi:.1f})"


def slot_table(R: pd.DataFrame, by: str | None = None) -> pd.DataFrame:
    D = R[R.y.notna() & ~R.cohort.isin(NOT_PRIMARY)]
    groups = [("ALL", D)] if by is None else list(D.groupby(by))
    rows = []
    for key, d in groups:
        rows.append({by or "scope": key, "cards": d.card.nunique(),
                     "rank1": _rate(d[d["rank"] == 1]), "rank2": _rate(d[(d["rank"] == 2) & ~d.informational_r2]),
                     "ranks3_4": _rate(d[d["rank"].isin([3, 4])]), "ranks5_plus": _rate(d[d["rank"] >= 5])})
    return pd.DataFrame(rows)


def card_classes(R: pd.DataFrame) -> pd.DataFrame:
    D = R[R.counted_slot]
    rows = []
    for card, d in D.groupby("card"):
        g = d.sort_values("rank").grade.tolist()
        live = [x for x in g if x in ("WIN", "LOSS")]
        if len(live) < 2:
            cls = "INCOMPLETE"
        else:
            cls = "ALL_WON" if live.count("WIN") == len(live) else ("ALL_LOST" if live.count("LOSS") == len(live) else "SPLIT")
        rows.append(dict(card=card, era=d.era.iloc[0], sport=d.sport.iloc[0], cls=cls))
    return pd.DataFrame(rows)


def calibration_table(R: pd.DataFrame, edges=(0, .3, .4, .5, .6, .7, .8, .9, 1.0001)) -> tuple[pd.DataFrame, dict]:
    D = R[R.y.notna() & R.p.notna() & ~R.cohort.isin(NOT_PRIMARY)]
    rows = []
    for lo, hi in zip(edges, edges[1:]):
        d = D[(D.p >= lo) & (D.p < hi)]
        k, n = int(d.y.sum()), len(d)
        ci = wilson(k, n) if n else (math.nan, math.nan)
        rows.append(dict(bin=f"{lo:.1f}–{min(hi, 1):.1f}", rows=n, cards=d.card.nunique(),
                         mean_p=d.p.mean() if n else math.nan, realised=k / n if n else math.nan,
                         wilson_lo=ci[0], wilson_hi=ci[1]))
    fit = calibration_fit(D.p, D.y)
    yb = D.y.mean()
    stats = dict(rows=len(D), cards=D.card.nunique(), brier=float(((D.p - D.y) ** 2).mean()),
                 climatology=float(yb * (1 - yb)), half=0.25, **fit)
    return pd.DataFrame(rows), stats


def rank1_weekly(R: pd.DataFrame) -> dict:
    """Rank-1 realised minus stated p, averaged within card then ISO week (dependence-aware)."""
    D = R[(R["rank"] == 1) & R.y.notna() & R.p.notna() & (R.week != "UNDATED") & ~R.cohort.isin(NOT_PRIMARY)]
    return paired_week_interval(D.y - D.p, D.card, D.week)


def rank1_tests(R: pd.DataFrame) -> dict:
    """Dependence-aware Rank-1 checks, clustered by ISO week (rows averaged within card, cards within week).

    (a) Rank 1 realised minus stated p (calibration-in-the-large at Rank 1).
    (b) Rank 1 win minus the same card's mean Ranks 3-4 win (does Rank 1 beat the card's own lower rows?).
    """
    from ml.core.metrics import cluster_bootstrap_mean
    D = R[~R.cohort.isin(NOT_PRIMARY) & (R.week != "UNDATED")]
    r1 = D[(D["rank"] == 1) & D.y.notna()]
    a = r1[r1.p.notna()]
    res = dict(calibration=paired_week_interval(a.y - a.p, a.card, a.week))
    res["calibration"]["card_weighted_mean"] = float((a.y - a.p).mean())
    res["calibration"]["week_bootstrap_95"] = cluster_bootstrap_mean((a.y - a.p).to_numpy(), a.week.to_numpy())
    low = D[D["rank"].isin([3, 4]) & D.y.notna()].groupby("card").y.mean()
    both = r1.drop_duplicates("card").set_index("card")[["y", "week"]].join(low.rename("low"), how="inner")
    diff = both.y - both.low
    res["rank1_vs_lower"] = paired_week_interval(diff, pd.Series(both.index), both.week)
    res["rank1_vs_lower"]["card_weighted_mean"] = float(diff.mean())
    res["rank1_vs_lower"]["week_bootstrap_95"] = cluster_bootstrap_mean(diff.to_numpy(), both.week.to_numpy())
    return res


def cohort_summary(R: pd.DataFrame) -> pd.DataFrame:
    """Separate probability roles; count coverage even when no primary score exists."""
    rows = []
    for cohort, d in R.groupby("cohort"):
        slots = d[d.counted_slot]
        scored = slots[slots.y.notna() & slots.p.notna()]
        paired = d[d.y.notna() & d.p.notna() & d.baseline.notna()]
        rows.append(dict(cohort=cohort, cards=d.card.nunique(), rows=len(d), primary_slots=len(slots),
                         wins=int((slots.grade == "WIN").sum()), losses=int((slots.grade == "LOSS").sum()),
                         pushes=int((slots.grade == "PUSH").sum()), decisive_scored=len(scored),
                         primary_brier=float(((scored.p - scored.y) ** 2).mean()),
                         baseline_rows=int(d.baseline.notna().sum()), paired_decisive_rows=len(paired),
                         paired_brier_difference=float((((paired.p - paired.y) ** 2) - ((paired.baseline - paired.y) ** 2)).mean())))
    return pd.DataFrame(rows)


def canonical_coverage(R: pd.DataFrame, logs=None) -> pd.DataFrame:
    """Expose canonical cards with no reporting rows, including genuine no-forecast/pending records."""
    counts = R.groupby("card").size()
    seen = {}
    for path in combined_logs() if logs is None else logs:
        for line, text in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            match = re.fullmatch(r"<!-- BEGIN CANONICAL RESEARCH (P-\d+) -->", text.strip())
            if match:
                card = match.group(1)
                seen.setdefault(card, dict(card=card, rows=int(counts.get(card, 0)),
                                           status="ROWS_PRESENT" if card in counts else "NO_CONTRACT_ROWS_REVIEW_REQUIRED",
                                           source=f"{path.name}:{line}"))
    return pd.DataFrame(seen.values(), columns=["card", "rows", "status", "source"])


def build_report(R: pd.DataFrame, diff: pd.DataFrame, *, logs=None) -> dict:
    cal, cal_stats = calibration_table(R)
    classes = card_classes(R)
    collisions = id_collisions(logs)
    clean = R[~R.card.isin(set(collisions.card))]
    out = dict(rows=R, diff=diff, slots=slot_table(R), slots_without_collisions=slot_table(clean), slots_era=slot_table(R, "era"), slots_sport=slot_table(R, "sport"),
               slots_family=slot_table(R[R["rank"] == 1], "family"), calibration=cal, cal_stats=cal_stats,
               classes=classes, rank1_week=rank1_weekly(R), rank1_tests=rank1_tests(R), collisions=collisions,
               cohorts=cohort_summary(R), slots_cohort=slot_table(R, "cohort"), coverage=canonical_coverage(R, logs))
    D1 = R[(R["rank"] == 1) & R.y.notna() & R.p.notna() & ~R.cohort.isin(NOT_PRIMARY)]
    band = pd.cut(D1.p, [0, .5, .55, .6, .65, .7, .8, .9, 1.0001], right=False)
    out["rank1_band"] = D1.groupby(band, observed=True).apply(
        lambda d: pd.Series(dict(rows=len(d), mean_p=d.p.mean(), realised=d.y.mean(), expected=d.p.sum(), wins=d.y.sum())),
        include_groups=False).reset_index().rename(columns={"p": "band"})
    out["rank1_band"]["band"] = out["rank1_band"]["band"].astype(str)
    weekly = D1.groupby("week").apply(lambda d: pd.Series(dict(cards=d.card.nunique(), wins=d.y.sum(), expected=d.p.sum())),
                                      include_groups=False).reset_index()
    out["weekly"] = weekly
    return out


def write(out: dict, folder: Path, receipt: dict) -> None:
    from ml.evaluation.report import md_table
    folder = Path(folder)
    if folder.exists():
        raise FileExistsError(folder)
    tmp = folder.parent / ("." + folder.name + "." + secrets.token_hex(6))
    tmp.mkdir(parents=True)
    cols = ["card", "rank", "cohort", "era", "date", "date_basis", "week", "sport", "family", "event", "contract", "p", "q", "identity_status", "literal_grade",
            "baseline", "grade", "counted_slot", "informational_r2", "record_status", "grade_basis", "source"]
    cols += [c for c in ("local_key", "probability_role", "effective_revision", "evidence") if c in out["rows"]]
    out["rows"][cols].to_csv(tmp / "CARD_ROWS.csv", index=False, lineterminator="\n")
    out["coverage"].to_csv(tmp / "CANONICAL_COVERAGE.csv", index=False, lineterminator="\n")
    sections = [("Coverage and primary scores by cohort", out["cohorts"]), ("Slots by cohort", out["slots_cohort"]),
                ("Canonical records without contract rows (review, not invented forecasts)", out["coverage"][out["coverage"].rows == 0]),
                ("Slots, all literal ranks", out["slots"]), ("Slots excluding colliding IDs (sensitivity)", out["slots_without_collisions"]), ("Slots by era", out["slots_era"]),
                ("Slots by sport", out["slots_sport"]), ("Rank 1 by proposition family", out["slots_family"]),
                ("Calibration, all graded rows with a stated p", out["calibration"]),
                ("Rank 1 by stated-p band", out["rank1_band"]), ("Rank 1 by ISO week", out["weekly"]),
                ("Effective-grade disagreements (effective settlement wins)", out["diff"]),
                ("Historical ID collisions in original headings", out["collisions"])]
    text = ["# Full-history card tables (generated)", "",
            f"Generated by `python -m ml card-history` — receipt below. Rows: {len(out['rows'])}; cards: {out['rows'].card.nunique()}.",
            "Descriptive and outcome-exposed; literal original ranks and grades; nothing re-graded.",
            "Pooled historical tables span different policies and timing strata; they do not validate the current method.",
            "Research-only analyst probabilities are retained as diagnostics and excluded from primary scores and calibration.",
            "Missing issue/known-at evidence is not inferred from import time or event date. No prospective eligibility is created.", ""]
    for title, frame in sections:
        text += [f"## {title}", "", md_table(frame, list(frame.columns), 3) if len(frame) else "None.", ""]
    cs = out["cal_stats"]
    text += ["## Calibration statistics", "", "\n".join(f"- `{k}`: {v}" for k, v in cs.items()), "",
             "## Rank-1 tests (card → ISO week)", "",
             "\n".join(f"- `{name}.{k}`: {v}" for name, d in out["rank1_tests"].items() for k, v in d.items()), "",
             "## Receipt", "", "\n".join(f"- `{k}`: {v}" for k, v in receipt.items())]
    (tmp / "CARD_HISTORY.md").write_text("\n".join(text) + "\n", encoding="utf-8", newline="\n")
    tmp.rename(folder)


def _label(path) -> str:
    path = Path(path).resolve()
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return "EXTERNAL:" + path.name


def main(argv=None):
    from ml import primary as p
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, required=True, help="new folder for CARD_ROWS.csv and CARD_HISTORY.md")
    parser.add_argument("--rank-log", type=Path, default=RANK_LOG, help="rank log to read (default: working copy)")
    args = parser.parse_args(argv)
    code = p.source_hash()
    inventories = import_inventories()
    logs = combined_logs()
    inputs = [args.rank_log, RECON, STATUS] + inventories + logs
    inputs += [path.parent / "LOCAL_ID_MAPPING.csv" for path in inventories]
    hashes = {f: p.digest(f.read_bytes()) if f.exists() else "MISSING" for f in inputs}
    R, diff = build_rows(args.rank_log, inventories=inventories, logs=logs)
    out = build_report(R, diff, logs=logs)
    if code != p.source_hash() or inventories != import_inventories() or logs != combined_logs() \
            or any((p.digest(f.read_bytes()) if f.exists() else "MISSING") != sha for f, sha in hashes.items()):
        raise ValueError("History inputs or generating source changed during reporting; rerun from a stable snapshot")
    receipt = dict(generated_at=datetime.now(timezone.utc).isoformat(), code_sha256=code,
                   repository_head=p.repository_head(),
                   **{f"input:{_label(f)}": sha for f, sha in hashes.items()})
    write(out, args.out, receipt)
    print(f"{len(R)} rows / {R.card.nunique()} cards -> {args.out}")


if __name__ == "__main__":
    main()
