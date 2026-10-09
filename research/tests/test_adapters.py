"""Source adapters (SRC-01): recorded-body tests where a body is retained, labelled synthetic fixtures where it is not."""
import hashlib
import json
from pathlib import Path

import pytest

from research.src import adapters, sources
from research.src.sources import allowed_url

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / 'research/data/raw/source_snapshots'
KBO_BODY = ROOT / 'research/verification/all_log_resolution_2026-10-05/kbo_ajax_games.body'


def recorded(pattern):
    found = sorted(RAW.glob(pattern))
    if not found:
        pytest.skip(f'no retained body for {pattern} in this checkout')
    return found[0].read_bytes()


# ---------------------------------------------------------------------------- recorded bodies
def test_kbo_gamelist_recorded_body():
    if not KBO_BODY.exists():
        pytest.skip('retained KBO body absent')
    games = {g.native_event_id: g for g in adapters.parse('KBO_GAMELIST_V1', KBO_BODY.read_bytes())}
    kt = games['20261001KTHT0']
    assert (kt.away_score, kt.home_score, kt.status) == (7, 5, 'FINAL')            # the scores verify_all_logs checks against the owner body
    hh = games['20261001HHSS0']
    assert (hh.away_score, hh.home_score) == (2, 3) and hh.extra_innings is False and hh.innings == 9
    assert games['20261001NCOB0'].home == '두산' and games['20261001NCOB0'].date == '2026-10-01'
    assert all(g.fields['home_score'] == 'B_SCORE_CN' for g in games.values())


def test_mlb_livefeed_recorded_body():
    games = adapters.parse('MLB_LIVEFEED_V1', recorded('mlb_p492_*.body'))
    g = games[0]
    assert g.native_event_id == '823897' and g.status == 'FINAL' and g.innings == len(g.home_periods) == len(g.away_periods)
    assert g.home_score == sum(g.home_periods) and g.away_score == sum(g.away_periods)             # the inning runs add up to the final score


def test_mlb_schedule_recorded_body_detects_extra_innings():
    games = adapters.parse('MLB_STATSAPI_V1', recorded('mlb_official_20261001T012020993578Z_*.body'))
    phillies = next(g for g in games if g.native_event_id == '849841')
    assert (phillies.away, phillies.home, phillies.away_score, phillies.home_score) == ('Philadelphia Phillies', 'Atlanta Braves', 4, 3)
    assert phillies.extra_innings is True and phillies.innings == 10 and phillies.status == 'FINAL'
    assert sum(phillies.away_periods) == 4 and sum(phillies.home_periods) == 3
    assert all(g.home_score is None for g in games if g.status != 'FINAL')                            # unfinished games never get a score


def test_nbl_schedule_recorded_body():
    games = adapters.parse('NBL_SCHEDULE_V1', recorded('nbl_official_20261001T012020221951Z_*.body'))
    played = [g for g in games if g.status == 'FINAL']
    sem = next(g for g in games if g.home == 'South East Melbourne Phoenix' and g.away == 'B League United')
    assert (sem.home_score, sem.away_score) == (113, 60) and played and all(g.home_score is not None for g in played)
    assert all(g.home_score is None for g in games if g.status != 'FINAL')


def test_npb_scorepage_recorded_body():
    games = adapters.parse('NPB_SCOREPAGE_V1', recorded('npb_final_*.body'))
    assert len(games) == 1
    g = games[0]
    assert (g.away, g.home, g.away_score, g.home_score, g.status) == ('中日ドラゴンズ', '広島東洋カープ', 1, 5, 'FINAL')
    assert g.date == '2026-10-01' and g.innings == 9 and g.extra_innings is False
    assert sum(g.away_periods) == 1 and sum(g.home_periods) == 5                                     # bottom 9th was 'x' (not batted): counted as 0


# ------------------------------------------------------------------------ synthetic fixtures
NHL_FIXTURE = json.dumps({'id': 2026020052, 'gameDate': '2026-10-06', 'startTimeUTC': '2026-10-07T02:00:00Z', 'gameState': 'OFF',
                          'homeTeam': {'abbrev': 'LAK', 'commonName': {'default': 'Kings'}, 'score': 2}, 'awayTeam': {'abbrev': 'FLA', 'commonName': {'default': 'Panthers'}, 'score': 3},
                          'gameOutcome': {'lastPeriodType': 'SO'}, 'periodDescriptor': {'number': 5, 'periodType': 'SO'}}).encode()
ESPN_FIXTURE = json.dumps({'header': {'id': '704512', 'competitions': [{'date': '2026-10-04T14:00Z', 'status': {'type': {'completed': True}}, 'competitors': [
    {'homeAway': 'home', 'id': '359', 'score': '2', 'team': {'displayName': 'Arsenal'}, 'linescores': [{'displayValue': '1'}, {'displayValue': '1'}]},
    {'homeAway': 'away', 'id': '363', 'score': '1', 'team': {'displayName': 'Chelsea'}, 'linescores': [{'displayValue': '0'}, {'displayValue': '1'}]}]}]},
    'boxscore': {'teams': [{'homeAway': 'home', 'team': {'id': '359'}, 'statistics': [{'name': 'wonCorners', 'displayValue': '7'}]},
                           {'homeAway': 'away', 'team': {'id': '363'}, 'statistics': [{'name': 'wonCorners', 'displayValue': '3'}]}]}}).encode()


def sackmann_fixture(n=60):
    header = 'tourney_id,tourney_name,surface,best_of,tourney_date,winner_name,loser_name,score,w_ace,w_df,w_svpt,w_1stIn,w_1stWon,w_2ndWon,w_SvGms,w_bpSaved,w_bpFaced,l_ace,l_df,l_svpt,l_1stIn,l_1stWon,l_2ndWon,l_SvGms,l_bpSaved,l_bpFaced'
    rows = [header]
    for i in range(n):
        rows.append(f'2026-{i},Test Open,Hard,3,20260105,Player A,Player B,6-4 6-3,5,1,70,45,35,14,10,3,5,2,3,68,40,28,13,9,2,6')
    rows.append('2026-x,Test Open,Clay,3,20260106,Player C,Player D,6-4 RET,,,,,,,,,,,,,,,,,,')              # a retirement without statistics
    return '\n'.join(rows).encode()


def test_nhl_synthetic_fixture_reads_overtime_and_shootout():
    g = adapters.parse('NHL_GAMECENTER_V1', NHL_FIXTURE)[0]
    assert (g.home, g.away, g.home_score, g.away_score, g.overtime, g.shootout, g.status) == ('Kings', 'Panthers', 2, 3, True, True, 'FINAL')
    live = json.loads(NHL_FIXTURE)
    live['gameState'] = 'LIVE'
    assert adapters.parse('NHL_GAMECENTER_V1', json.dumps(live).encode())[0].home_score is None


def test_espn_synthetic_fixture_reads_halftime_and_corners():
    g = adapters.parse('ESPN_SUMMARY_V1', ESPN_FIXTURE)[0]
    assert (g.home, g.away, g.home_score, g.away_score) == ('Arsenal', 'Chelsea', 2, 1)
    assert (g.home_halftime, g.away_halftime, g.home_corners, g.away_corners) == (1, 0, 7, 3) and g.home_periods == [1, 1]
    assert g.fields['corners'].endswith('wonCorners]')


def test_sackmann_synthetic_fixture_feeds_the_tennis_engine():
    from runtime.src.sports.tennis.engine import TennisEngine
    matches = adapters.parse('SACKMANN_ATP_V1', sackmann_fixture())
    assert matches[0].surface == 'hard' and matches[-1].surface == 'clay' and matches[0].stats['w_svpt'] == 70 and matches[-1].stats['w_svpt'] is None
    records = adapters.tennis_fit_records(matches)
    assert len(records) == 60                                                                      # the retirement without statistics is skipped, not zero-filled
    engine = TennisEngine(form_sigma=0.04).fit(records)
    assert engine.is_fitted and 0.55 < engine.tour_avg_serve < 0.75


# --------------------------------------------------------------------------------- registry
def test_registry_entries_are_consistent_with_the_parsers_and_their_evidence():
    registry = adapters.read_adapter_registry()
    assert {'kbo_official', 'npb_official', 'nhl_official', 'espn_soccer', 'sackmann_tennis'} <= set(registry)
    for key, entry in registry.items():
        status = entry['adapter_status']
        assert status in ('RECORDED_BODY_TESTED', 'SYNTHETIC_FIXTURE_ONLY', 'PLANNED_NO_ADAPTER'), key
        if entry['access_mode'] == 'AUTOMATED_ALLOWED':
            assert entry['parser_id'] in adapters.ADAPTERS and entry['market_fields_possible'] is False, key
            assert allowed_url(entry['probe_url'], entry), f'{key}: probe URL outside its own allow-list'
            assert set(entry['settlement_fields']) <= set(adapters.ADAPTERS[entry['parser_id']].settlement_fields), key
            assert all(e in adapters.ENDPOINT_TAXONOMY + ('FULL_GAME',) for e in entry['endpoints']), key
        else:
            assert status == 'PLANNED_NO_ADAPTER' and entry['blocker'] and not entry['allowed_url_prefixes'], key
        if status == 'RECORDED_BODY_TESTED':
            body = ROOT / entry['recorded_body']
            if body.exists():
                parse = adapters.ADAPTERS[entry['parser_id']].parse
                assert parse(body.read_bytes()), key


def test_fetch_returns_a_hashed_receipt_and_parsed_games(tmp_path, monkeypatch):
    class Reply:
        headers = {'Content-Type': 'application/json'}
        def __init__(self, url): self.url = url
        def __enter__(self): return self
        def __exit__(self, *a): return False
        def geturl(self): return self.url
        def read(self, n): return NHL_FIXTURE
    class Opener:
        def open(self, request, timeout): return Reply(request.full_url)
    monkeypatch.setattr(sources, 'build_opener', lambda *a, **k: Opener())
    fake_root = tmp_path / 'checkout' / 'research'
    monkeypatch.setattr(sources, 'ROOT', fake_root)
    monkeypatch.setattr(sources, 'RECEIPTS', fake_root / 'data/source_receipts')
    monkeypatch.setattr(sources, 'RAW', fake_root / 'data/raw/source_snapshots')
    out = adapters.fetch('nhl_official', 'https://api-web.nhle.com/v1/gamecenter/2026020052/boxscore', cache_dir=fake_root / 'data/raw/source_snapshots')
    assert out['receipt']['response_sha256'] == hashlib.sha256(NHL_FIXTURE).hexdigest() and out['receipt']['parser_id'] == 'NHL_GAMECENTER_V1'
    assert out['games'][0].shootout is True
    with pytest.raises(ValueError, match='outside the source contract'):
        adapters.fetch('nhl_official', 'https://example.com/boxscore', cache_dir=fake_root / 'data/raw/source_snapshots')
    with pytest.raises(ValueError, match='PLANNED_NO_ADAPTER'):
        adapters.fetch('bleague_official', 'https://www.bleague.jp/game_detail/?ScheduleKey=1', cache_dir=fake_root / 'data/raw/source_snapshots')


def test_unknown_parser_and_malformed_bodies_are_not_guessed():
    with pytest.raises(ValueError, match='no parser registered'):
        adapters.parse('NOPE_V1', b'{}')
    assert adapters.parse('NPB_SCOREPAGE_V1', b'<html></html>') == []
    assert adapters.parse('KBO_GAMELIST_V1', b'{"game": []}') == []
