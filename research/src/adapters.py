"""Registered source adapters: one parser per provider contract, mapping a retained body onto a standard game record (SRC-01).

An adapter is (registry entry in sources_registry_adapters.json or sources_registry.json) + (parser here). The registry entry carries
the allowed URL prefixes, parser ID, endpoint taxonomy and the settlement fields the provider can supply; `fetch` stores the body
and returns a hashed receipt through `research.src.sources.fetch_source` (so redirects stay inside the allow-list and the response
hash is recorded), then parses it. Parsers read only the provider's own fields, name which fields they used (`fields`), and never
default a missing score: a missing value is `None`.

Every parser's status is stated in the registry:
  RECORDED_BODY_TESTED   unit-tested against a body retained from the provider in this repository
  SYNTHETIC_FIXTURE_ONLY unit-tested against a fixture constructed from the provider's documented schema; it MUST be probed against a
                         real body (`probe`) before any card relies on it
  PLANNED_NO_ADAPTER     registered with its blocker; fetch is refused
"""
from __future__ import annotations
import csv
import io
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Optional

ROOT = Path(__file__).resolve().parents[2]
ADAPTER_REGISTRY = ROOT / 'research/sources_registry_adapters.json'
STATUSES = ('FINAL', 'SCHEDULED', 'LIVE', 'CANCELLED', 'POSTPONED', 'UNKNOWN')
ENDPOINT_TAXONOMY = ('REGULATION', 'FULL_GAME', 'FIRST_HALF', 'PERIODS', 'CORNERS', 'SERVE_STATS', 'FINAL_SCORE', 'SCHEDULE')


@dataclass
class Game:
    """One event as a provider reports it. Unknown values are None, never zero."""
    source_id: str
    native_event_id: Optional[str]
    date: Optional[str]                          # local calendar date YYYY-MM-DD
    home: Optional[str]
    away: Optional[str]
    status: str = 'UNKNOWN'
    start_utc: Optional[str] = None
    home_score: Optional[int] = None
    away_score: Optional[int] = None
    home_periods: Optional[list[int]] = None
    away_periods: Optional[list[int]] = None
    innings: Optional[int] = None
    extra_innings: Optional[bool] = None
    overtime: Optional[bool] = None
    shootout: Optional[bool] = None
    home_halftime: Optional[int] = None
    away_halftime: Optional[int] = None
    home_corners: Optional[int] = None
    away_corners: Optional[int] = None
    fields: dict[str, str] = field(default_factory=dict)       # standard field -> provider field(s) it was read from

    def as_dict(self) -> dict:
        return dict(self.__dict__)


@dataclass
class TennisMatch:
    tourney: str
    date: str
    surface: str
    best_of: int
    winner: str
    loser: str
    score: str
    stats: dict[str, Optional[int]]
    fields: dict[str, str] = field(default_factory=dict)


def _int(value: Any) -> Optional[int]:
    if value is None or value == '' or isinstance(value, bool):
        return None
    try:
        return int(str(value).strip())
    except ValueError:
        return None


def _json(raw: bytes) -> Any:
    return json.loads(raw.decode('utf-8-sig'))


# --------------------------------------------------------------------------------------- KBO
KBO_STATE = {'1': 'SCHEDULED', '2': 'LIVE', '3': 'FINAL', '4': 'CANCELLED'}


def parse_kbo_gamelist(raw: bytes) -> list[Game]:
    """koreabaseball.com Main.asmx/GetKboGameList: T_* is the away (top) side, B_* the home (bottom) side."""
    out = []
    for g in _json(raw).get('game', []):
        day = str(g.get('G_DT', ''))
        status = KBO_STATE.get(str(g.get('GAME_STATE_SC')), 'UNKNOWN')
        if str(g.get('CANCEL_SC_ID', '0')) not in ('0', '') and status != 'FINAL':
            status = 'CANCELLED'
        final = status == 'FINAL' and g.get('GAME_RESULT_CK') == 1
        innings = _int(g.get('GAME_INN_NO'))
        out.append(Game('kbo_official', g.get('G_ID'), f'{day[:4]}-{day[4:6]}-{day[6:8]}' if len(day) == 8 else None, g.get('HOME_NM') or g.get('HOME_ID'),
                        g.get('AWAY_NM') or g.get('AWAY_ID'), status, home_score=_int(g.get('B_SCORE_CN')) if final else None,
                        away_score=_int(g.get('T_SCORE_CN')) if final else None, innings=innings if final else None,
                        extra_innings=(innings > 9) if final and innings else None,
                        fields={'home_score': 'B_SCORE_CN', 'away_score': 'T_SCORE_CN', 'status': 'GAME_STATE_SC+GAME_RESULT_CK+CANCEL_SC_ID',
                                'innings': 'GAME_INN_NO', 'native_event_id': 'G_ID'}))
    return out


# --------------------------------------------------------------------------------------- MLB
def _mlb_status(state: dict) -> str:
    return {'Final': 'FINAL', 'Live': 'LIVE', 'Preview': 'SCHEDULED'}.get(state.get('abstractGameState', ''), 'UNKNOWN')


def _mlb_linescore(ls: dict) -> tuple[Optional[list[int]], Optional[list[int]]]:
    innings = ls.get('innings') or []
    if not innings:
        return None, None
    return [(_int(i.get('away', {}).get('runs')) or 0) for i in innings], [(_int(i.get('home', {}).get('runs')) or 0) for i in innings]


def parse_mlb_schedule(raw: bytes) -> list[Game]:
    """statsapi.mlb.com /api/v1/schedule (hydrate=linescore for innings)."""
    out = []
    for day in _json(raw).get('dates', []):
        for g in day.get('games', []):
            status = _mlb_status(g.get('status', {}))
            ls = g.get('linescore') or {}
            away_p, home_p = _mlb_linescore(ls)
            final = status == 'FINAL'
            played = len(away_p) if away_p else None
            out.append(Game('mlb_official', str(g.get('gamePk')), g.get('officialDate'), g['teams']['home']['team']['name'], g['teams']['away']['team']['name'], status,
                            start_utc=g.get('gameDate'), home_score=_int(g['teams']['home'].get('score')) if final else None,
                            away_score=_int(g['teams']['away'].get('score')) if final else None, home_periods=home_p, away_periods=away_p,
                            innings=played, extra_innings=(played > (ls.get('scheduledInnings') or 9)) if final and played else None,
                            fields={'home_score': 'teams.home.score', 'away_score': 'teams.away.score', 'innings': 'linescore.innings[].num',
                                    'extra_innings': 'linescore.innings vs linescore.scheduledInnings'}))
    return out


def parse_mlb_livefeed(raw: bytes) -> list[Game]:
    """statsapi.mlb.com /api/v1.1/game/{pk}/feed/live."""
    d = _json(raw)
    gd, ls = d['gameData'], d['liveData']['linescore']
    status = _mlb_status(gd.get('status', {}))
    away_p, home_p = _mlb_linescore(ls)
    final = status == 'FINAL'
    played = len(away_p) if away_p else None
    return [Game('mlb_official', str(d.get('gamePk')), gd.get('datetime', {}).get('officialDate'), gd['teams']['home']['name'], gd['teams']['away']['name'], status,
                 start_utc=gd.get('datetime', {}).get('dateTime'), home_score=_int(ls.get('teams', {}).get('home', {}).get('runs')) if final else None,
                 away_score=_int(ls.get('teams', {}).get('away', {}).get('runs')) if final else None, home_periods=home_p, away_periods=away_p,
                 innings=played, extra_innings=(played > (ls.get('scheduledInnings') or 9)) if final and played else None,
                 fields={'home_score': 'liveData.linescore.teams.home.runs', 'away_score': 'liveData.linescore.teams.away.runs',
                         'periods': 'liveData.linescore.innings[].{home,away}.runs'})]


# --------------------------------------------------------------------------------------- NBL
def parse_nbl_schedule(raw: bytes) -> list[Game]:
    """schedule.nbl.com.au calendar API: scores are full-game (overtime included); quarter splits are not in this feed."""
    out = []
    for m in _json(raw).get('matches', []):
        complete = m.get('phase') == 'complete'
        start = m.get('starts_at_ms')
        start_utc = datetime.fromtimestamp(start / 1000, tz=timezone.utc).isoformat() if isinstance(start, (int, float)) else None
        out.append(Game('nbl_official', m.get('id'), start_utc[:10] if start_utc else None, (m.get('home') or {}).get('name'), (m.get('away') or {}).get('name'),
                        'FINAL' if complete else ('SCHEDULED' if m.get('phase') in (None, 'upcoming', 'pre') else 'UNKNOWN'), start_utc=start_utc,
                        home_score=_int(m.get('home_score')) if complete else None, away_score=_int(m.get('away_score')) if complete else None,
                        fields={'home_score': 'home_score', 'away_score': 'away_score', 'status': 'phase', 'start_utc': 'starts_at_ms'}))
    return out


# --------------------------------------------------------------------------------------- NPB
def parse_npb_scorepage(raw: bytes) -> list[Game]:
    """npb.jp /scores/YYYY/MMDD/<teams>-NN/ line-score page (HTML). Top row is the visitor; a bottom 9th shown as 'x' was not batted."""
    text = raw.decode('utf-8', errors='replace')
    url = re.search(r'rel="canonical" href="https://npb\.jp/scores/(\d{4})/(\d{2})(\d{2})/([^"]+?)/?"', text)
    table = re.search(r'<table id="tablefix_ls">(.*?)</table>', text, re.S)
    if not url or not table:
        return []
    rows = re.findall(r'<tr class="(top|bottom)">(.*?)</tr>', table[1], re.S)
    sides = {}
    for kind, body in rows:
        name = re.search(r'<span class="hide_sp">([^<]+)</span>', body)
        cells = [re.sub(r'<[^>]+>|&nbsp;|\s', '', c) for c in re.findall(r'<td[^>]*>(.*?)</td>', body, re.S)]
        total = re.search(r'<td class="total-1">\s*(\d+)\s*</td>', body)
        innings = [c for c in cells[:-3] if c != ''] if len(cells) > 3 else []
        sides[kind] = (name[1] if name else None, [(_int(c) if c != 'x' else None) for c in innings], _int(total[1]) if total else None)
    if len(sides) != 2:
        return []
    final = '【試合終了】' in text
    away, home = sides['top'], sides['bottom']
    played = len(home[1])
    return [Game('npb_official', f'{url[1]}{url[2]}{url[3]}-{url[4]}', f'{url[1]}-{url[2]}-{url[3]}', home[0], away[0], 'FINAL' if final else 'LIVE',
                 home_score=home[2] if final else None, away_score=away[2] if final else None,
                 home_periods=[v or 0 for v in home[1]], away_periods=[v or 0 for v in away[1]], innings=played if final else None,
                 extra_innings=(played > 9) if final else None,
                 fields={'home_score': 'tablefix_ls tr.bottom td.total-1', 'away_score': 'tablefix_ls tr.top td.total-1', 'status': '【試合終了】 marker'})]


# --------------------------------------------------------------------------------------- NHL
def parse_nhl_gamecenter(raw: bytes) -> list[Game]:
    """api-web.nhle.com /v1/gamecenter/{id}/boxscore. gameOutcome.lastPeriodType is REG, OT or SO (SO = shootout decided)."""
    d = _json(raw)
    state = str(d.get('gameState', '')).upper()
    status = 'FINAL' if state in ('FINAL', 'OFF') else 'LIVE' if state in ('LIVE', 'CRIT') else 'SCHEDULED' if state in ('FUT', 'PRE') else 'UNKNOWN'
    last = (d.get('gameOutcome') or {}).get('lastPeriodType') or (d.get('periodDescriptor') or {}).get('periodType')
    final = status == 'FINAL'
    name = lambda team: (team.get('commonName') or team.get('name') or {}).get('default') or team.get('abbrev')
    return [Game('nhl_official', str(d.get('id')), d.get('gameDate'), name(d['homeTeam']), name(d['awayTeam']), status, start_utc=d.get('startTimeUTC'),
                 home_score=_int(d['homeTeam'].get('score')) if final else None, away_score=_int(d['awayTeam'].get('score')) if final else None,
                 overtime=(last in ('OT', 'SO')) if final and last else None, shootout=(last == 'SO') if final and last else None,
                 fields={'home_score': 'homeTeam.score', 'away_score': 'awayTeam.score', 'overtime': 'gameOutcome.lastPeriodType', 'status': 'gameState'})]


# --------------------------------------------------------------------------------------- ESPN soccer
def parse_espn_soccer_summary(raw: bytes) -> list[Game]:
    """site.api.espn.com .../summary?event=ID: scores, per-half linescores and team statistics (wonCorners) when present."""
    d = _json(raw)
    comp = d['header']['competitions'][0]
    by_side = {c['homeAway']: c for c in comp['competitors']}
    done = bool(comp.get('status', {}).get('type', {}).get('completed'))
    halves = {side: [_int(x.get('displayValue')) for x in c.get('linescores', [])] for side, c in by_side.items()}
    corners: dict[str, Optional[int]] = {'home': None, 'away': None}
    for team in d.get('boxscore', {}).get('teams', []):
        side = team.get('homeAway') or next((s for s, c in by_side.items() if str(c.get('id')) == str(team.get('team', {}).get('id'))), None)
        for stat in team.get('statistics', []):
            if stat.get('name') == 'wonCorners' and side in corners:
                corners[side] = _int(stat.get('displayValue'))
    return [Game('espn_soccer', str(d['header'].get('id')), str(comp.get('date', ''))[:10] or None, by_side['home']['team'].get('displayName'),
                 by_side['away']['team'].get('displayName'), 'FINAL' if done else 'SCHEDULED', start_utc=comp.get('date'),
                 home_score=_int(by_side['home'].get('score')) if done else None, away_score=_int(by_side['away'].get('score')) if done else None,
                 home_periods=[x for x in halves['home'] if x is not None] if halves['home'] and None not in halves['home'] else None,
                 away_periods=[x for x in halves['away'] if x is not None] if halves['away'] and None not in halves['away'] else None,
                 home_halftime=halves['home'][0] if halves['home'] else None, away_halftime=halves['away'][0] if halves['away'] else None,
                 home_corners=corners['home'], away_corners=corners['away'],
                 fields={'home_score': 'header.competitions[0].competitors[home].score', 'halftime': 'competitors[].linescores[0].displayValue',
                         'corners': 'boxscore.teams[].statistics[name=wonCorners]'})]


# --------------------------------------------------------------------------------------- tennis
SERVE_FIELDS = ('svpt', '1stIn', '1stWon', '2ndWon', 'SvGms', 'bpSaved', 'bpFaced', 'ace', 'df')


def parse_sackmann_atp_csv(raw: bytes) -> list[TennisMatch]:
    """Sackmann-format match CSV (tennis_atp / tennis_wta): winner/loser names, surface, best_of and w_/l_ serve statistics."""
    out = []
    for row in csv.DictReader(io.StringIO(raw.decode('utf-8-sig'))):
        day = str(row.get('tourney_date', ''))
        stats = {f'{side}_{name}': _int(row.get(f'{side}_{name}')) for side in ('w', 'l') for name in SERVE_FIELDS}
        out.append(TennisMatch(row.get('tourney_name', ''), f'{day[:4]}-{day[4:6]}-{day[6:8]}' if len(day) == 8 else '', (row.get('surface') or '').lower(),
                               _int(row.get('best_of')) or 0, row.get('winner_name', ''), row.get('loser_name', ''), row.get('score', ''), stats,
                               {'stats': 'w_*/l_* columns', 'surface': 'surface', 'best_of': 'best_of'}))
    return out


def tennis_fit_records(matches: list[TennisMatch]) -> list[dict]:
    """Records for `TennisEngine.fit`; a match without complete serve statistics for both players is skipped, not zero-filled."""
    out = []
    for m in matches:
        s = m.stats
        w_svpt, w_1st, w_2nd, l_svpt, l_1st, l_2nd = s['w_svpt'], s['w_1stWon'], s['w_2ndWon'], s['l_svpt'], s['l_1stWon'], s['l_2ndWon']
        if w_svpt is None or w_1st is None or w_2nd is None or l_svpt is None or l_1st is None or l_2nd is None or not w_svpt or not l_svpt:
            continue
        out.append({'player1': m.winner, 'player2': m.loser, 'p1_serve_won': w_1st + w_2nd, 'p1_serve_total': w_svpt,
                    'p2_serve_won': l_1st + l_2nd, 'p2_serve_total': l_svpt})
    return out


# --------------------------------------------------------------------------------------- registry
@dataclass(frozen=True)
class Adapter:
    parser_id: str
    parse: Callable[[bytes], list]
    settlement_fields: tuple[str, ...]


ADAPTERS: dict[str, Adapter] = {
    'KBO_GAMELIST_V1': Adapter('KBO_GAMELIST_V1', parse_kbo_gamelist, ('final_score', 'innings', 'extra_innings', 'status')),
    'MLB_STATSAPI_V1': Adapter('MLB_STATSAPI_V1', parse_mlb_schedule, ('final_score', 'innings', 'extra_innings', 'inning_runs', 'status')),
    'MLB_LIVEFEED_V1': Adapter('MLB_LIVEFEED_V1', parse_mlb_livefeed, ('final_score', 'innings', 'extra_innings', 'inning_runs', 'status')),
    'NBL_SCHEDULE_V1': Adapter('NBL_SCHEDULE_V1', parse_nbl_schedule, ('final_score_incl_ot', 'status')),
    'NPB_SCOREPAGE_V1': Adapter('NPB_SCOREPAGE_V1', parse_npb_scorepage, ('final_score', 'innings', 'extra_innings', 'inning_runs', 'status')),
    'NHL_GAMECENTER_V1': Adapter('NHL_GAMECENTER_V1', parse_nhl_gamecenter, ('final_score', 'overtime', 'shootout', 'status')),
    'ESPN_SUMMARY_V1': Adapter('ESPN_SUMMARY_V1', parse_espn_soccer_summary, ('final_score', 'halftime_score', 'corners', 'status')),
    'SACKMANN_ATP_V1': Adapter('SACKMANN_ATP_V1', parse_sackmann_atp_csv, ('serve_stats', 'final_score', 'surface')),
}


def read_adapter_registry(path: Path = ADAPTER_REGISTRY) -> dict:
    return json.loads(Path(path).read_text(encoding='utf-8'))['sources']


def parse(parser_id: str, raw: bytes) -> list:
    if parser_id not in ADAPTERS:
        raise ValueError(f'no parser registered for {parser_id!r}')
    return ADAPTERS[parser_id].parse(raw)


def fetch(source_id: str, url: str, cache_dir: Path | None = None, registry_path: Path = ADAPTER_REGISTRY, **kwargs) -> dict:
    """Fetch through the source contract (allow-listed URL, bounded size, SHA-256 receipt), then parse with the registered parser."""
    from . import sources
    entry = read_adapter_registry(registry_path)[source_id]
    if entry['access_mode'] != 'AUTOMATED_ALLOWED':
        raise ValueError(f"{source_id} is {entry['access_mode']}: {entry.get('blocker', 'no automated access')}")
    receipt = sources.fetch_source(source_id, url, cache_dir=cache_dir, registry_path=registry_path, **kwargs)
    path = Path(receipt['body_path'])
    body = (path if path.is_absolute() else sources.ROOT.parent / path).read_bytes()
    return {'receipt': receipt, 'games': parse(entry['parser_id'], body)}
