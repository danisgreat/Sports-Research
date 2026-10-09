"""Rolling top-two scoreboard: determinism, cohort separation, staleness (EVL-01, EVL-05)."""
import json
from pathlib import Path

from research.operations import scoreboard

ROOT = Path(__file__).resolve().parents[2]


def record(cid, grades, ps, sport='Soccer', gate=None, event_key='X:2026-27:1:2026-10-10', state='SETTLED', fc=None):
    contracts = ['Home win', 'Over 2.5 goals', 'Under 3.5 goals', 'Away +1.5']
    rows = [[i + 1, contracts[i], g, 'B', 'basis', p] for i, (g, p) in enumerate(zip(grades, ps))]
    return {'id': cid, 'state': state, 'sport': sport, 'event': cid, 'event_key': event_key, 'rows': rows, 'winner_call': 'CORRECT',
            'failure_class': fc, 'joint_failure': 0.2, 'rank1_gate': gate}


def make_root(tmp_path, records):
    folder = tmp_path / 'research/verification/mini_x'
    folder.mkdir(parents=True)
    (folder / 'settlement_table.json').write_text(json.dumps({'schema': 'mini-settlement-2', 'created_utc': '2026-10-10T00:00:00+00:00',
                                                              'records': records}), encoding='utf-8')
    (tmp_path / 'research/canonical_ledger.jsonl').write_text('', encoding='utf-8')
    return tmp_path


RECORDS = [
    record('P-900', 'WWLL', [0.77, 0.70, 0.55, 0.50], gate='PASS'),
    record('P-901', 'LWWL', [0.66, 0.64, 0.60, 0.55], gate='RANK1_UNSTABLE', event_key='X:2026-27:2:2026-11-02', fc='VARIANCE'),
    record('P-902', 'WLWW', [0.71, 0.66, 0.62, 0.58], sport='Basketball', event_key='X:2026-27:3:2026-11-09'),
    record('P-903', 'LLWW', [0.55, 0.52, 0.51, 0.50], sport='Tennis', event_key='X:2026-27:4:2026-11-10'),      # legacy rule: Rank 1 < 60%
]


def test_cohorts_are_separated_and_counted_cohort_excludes_unstable_cards(tmp_path):
    data = scoreboard.build(make_root(tmp_path, RECORDS))
    counted, unstable = data['headline_counted_cohort'], data['rank1_unstable_cohort']
    assert counted['cards'] == 2 and unstable['cards'] == 2 and data['all_forecast_cards']['cards'] == 4
    assert counted['counted_wins'] == 3 and counted['live_rows'] == 4         # P-900 WW + P-902 WL
    assert unstable['counted_wins'] == 1 and unstable['live_rows'] == 4       # P-901 LW + P-903 LL
    assert unstable['failure_classes'] == {'VARIANCE': 1} or 'VARIANCE' in unstable['failure_classes']
    info = data['informational_ranks_3_4']
    assert info['W'] + info['L'] == 8 and info['with_p'] == 8                 # ranks 3-4 of all four cards, calibration only
    assert set(data['by_month']) == {'2026-10', '2026-11'} and set(data['by_sport']) == {'Basketball', 'Soccer'}
    assert data['by_month']['2026-10']['cards'] == 1


def test_rank_slots_never_mix_informational_rows_into_counted_wins(tmp_path):
    data = scoreboard.build(make_root(tmp_path, RECORDS))
    every = data['all_forecast_cards']
    assert every['counted_wins'] == sum(1 for r in RECORDS for row in r['rows'][:2] if row[2] == 'W')
    assert data['slots']['ranks_1_2']['W'] + data['slots']['ranks_1_2']['L'] == every['live_rows']


def test_publish_is_deterministic_and_verify_detects_a_stale_scoreboard(tmp_path):
    root = make_root(tmp_path, RECORDS)
    first = scoreboard.publish(root)
    one = (root / 'research/scoreboard/SCOREBOARD.json').read_bytes(), (root / 'research/scoreboard/SCOREBOARD.md').read_bytes()
    scoreboard.publish(root)
    two = (root / 'research/scoreboard/SCOREBOARD.json').read_bytes(), (root / 'research/scoreboard/SCOREBOARD.md').read_bytes()
    assert one == two and first['cards'] == 4
    assert scoreboard.verify(root) == []
    table = root / 'research/verification/mini_x/settlement_table.json'
    payload = json.loads(table.read_text(encoding='utf-8'))
    payload['records'].append(record('P-904', 'WWLL', [0.7, 0.65, 0.6, 0.55], gate='PASS', event_key='X:2026-27:5:2026-11-12'))
    table.write_text(json.dumps(payload), encoding='utf-8')
    problems = scoreboard.verify(root)
    assert problems and all('stale' in p for p in problems)
    (root / 'research/scoreboard/SCOREBOARD.md').write_bytes((root / 'research/scoreboard/SCOREBOARD.md').read_bytes().replace(b'\n', b'\r\n'))
    scoreboard.publish(root)
    (root / 'research/scoreboard/SCOREBOARD.md').write_bytes((root / 'research/scoreboard/SCOREBOARD.md').read_bytes().replace(b'\n', b'\r\n'))
    assert scoreboard.verify(root) == []                                         # a CRLF checkout is not "stale"


def test_missing_scoreboard_is_reported(tmp_path):
    root = make_root(tmp_path, RECORDS)
    assert len(scoreboard.verify(root)) == 2


def test_published_repository_scoreboard_is_current():
    assert scoreboard.verify(ROOT) == []


def test_legacy_history_reads_the_rank_log():
    legacy = scoreboard.legacy_history(ROOT / 'GAME_PREDICTION_RANK_LOG.csv')
    assert legacy['cards'] == 522 and set(legacy['slots']) == {'1', '2', '3', '4'}
    assert legacy['slots']['1']['W'] + legacy['slots']['1']['L'] > 400
