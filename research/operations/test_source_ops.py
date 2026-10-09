"""Tests for the registry lint, lineage audits and the reachability matrix (SRC-04, SRC-07, SRC-08)."""
import copy
import json
import hashlib

import pytest

from research.operations import lineage_audit, reachability, registry_lint

SOURCES = {
    'a_official': {'leagues': ['XL'], 'official': True, 'upstream_lineage_id': 'A', 'access_mode': 'AUTOMATED_ALLOWED'},
    'b_stats': {'leagues': ['XL'], 'official': False, 'upstream_lineage_id': 'B', 'access_mode': 'AUTOMATED_ALLOWED'},
    'c_syndicated': {'leagues': ['XL'], 'official': False, 'upstream_lineage_id': 'A', 'access_mode': 'AUTOMATED_ALLOWED'},
    'd_other': {'leagues': ['XL'], 'official': False, 'upstream_lineage_id': 'D', 'access_mode': 'AUTOMATED_ALLOWED'},
}


def audit(sid, status='INDEPENDENT', collector=None, shares=None):
    return {'schema': 'lineage-audit-1', 'source_id': sid, 'audited_utc': '2026-10-09T10:00:00+00:00', 'terminal_collector': collector or sid,
            'upstream_lineage_id': sid.upper(), 'independence_status': status, 'shares_feed_with': shares or [], 'method': 'publisher documentation',
            'evidence': [{'url': 'https://example.org/about', 'sha256': hashlib.sha256(sid.encode()).hexdigest(), 'retrieved_utc': '2026-10-09T09:00:00+00:00',
                          'quote': 'Data are collected by the league.'}]}


def test_valid_audit_and_each_failure():
    assert lineage_audit.validate(audit('a_official'), SOURCES) == []
    bad = audit('a_official'); bad['evidence'] = []
    assert any('evidence' in e for e in lineage_audit.validate(bad, SOURCES))
    bad = audit('a_official'); bad['evidence'][0]['sha256'] = 'abc'
    assert any('sha256' in e for e in lineage_audit.validate(bad, SOURCES))
    bad = audit('a_official'); bad['evidence'][0]['retrieved_utc'] = '2026-10-09T09:00:00'
    assert any('retrieved_utc' in e for e in lineage_audit.validate(bad, SOURCES))
    assert any('shares' in e for e in lineage_audit.validate(audit('c_syndicated', 'SHARED_FEED'), SOURCES))
    assert any('must not list' in e for e in lineage_audit.validate(audit('a_official', shares=['c_syndicated']), SOURCES))
    assert any('not in the source registry' in e for e in lineage_audit.validate(audit('zzz'), SOURCES))
    assert lineage_audit.validate({'schema': 'lineage-audit-1', 'source_id': 'a_official', 'independence_status': 'UNKNOWN',
                                   'audited_utc': '2026-10-09T10:00:00+00:00'}, SOURCES) == []


def test_quorum_needs_distinct_collectors_and_an_official_one():
    audits = {'a_official': audit('a_official'), 'b_stats': audit('b_stats')}
    assert not lineage_audit.quorum(SOURCES, audits, 'XL')['satisfied']
    audits['d_other'] = audit('d_other')
    q = lineage_audit.quorum(SOURCES, audits, 'XL')
    assert q['satisfied'] and q['distinct_collectors'] == 3
    # a syndicated copy on the same collector adds nothing; a shared feed adds nothing
    audits = {'a_official': audit('a_official'), 'c_syndicated': audit('c_syndicated', collector='a_official'), 'b_stats': audit('b_stats')}
    assert lineage_audit.quorum(SOURCES, audits, 'XL')['distinct_collectors'] == 2
    audits = {'b_stats': audit('b_stats'), 'd_other': audit('d_other'), 'c_syndicated': audit('c_syndicated')}
    q = lineage_audit.quorum(SOURCES, audits, 'XL')
    assert q['distinct_collectors'] == 3 and not q['has_official'] and not q['satisfied']
    audits = {'a_official': audit('a_official'), 'b_stats': audit('b_stats'), 'd_other': audit('d_other', 'SHARED_FEED', shares=['b_stats'])}
    assert not lineage_audit.quorum(SOURCES, audits, 'XL')['satisfied']


def test_shipped_registry_passes_lint_and_fantasy_is_excluded():
    assert registry_lint.lint() == []
    registry = json.loads(registry_lint.REGISTRY.read_text(encoding='utf-8'))['sources']
    excluded = json.loads(registry_lint.EXCLUDED.read_text(encoding='utf-8'))['sources']
    assert 'fantasy_premierleague' in excluded and 'fantasy_premierleague' not in registry


def test_lint_catches_excluded_sources_and_unaudited_independence(tmp_path):
    reg = json.loads(registry_lint.REGISTRY.read_text(encoding='utf-8'))
    bad = copy.deepcopy(reg)
    bad['sources']['fantasy_premierleague'] = {'publisher': 'x', 'access_mode': 'EXCLUDED_FANTASY', 'parser_id': 'EXCLUDED', 'allowed_url_prefixes': [],
                                               'upstream_lineage_id': 'E', 'independence_status': 'UNKNOWN', 'endpoints': [], 'market_fields_possible': True,
                                               'official': False, 'leagues': []}
    bad['sources']['mlb_official']['independence_status'] = 'INDEPENDENT'
    bad['sources']['nbl_official']['allowed_url_prefixes'] = ['http://schedule.nbl.com.au/']
    path = tmp_path / 'reg.json'
    path.write_text(json.dumps(bad), encoding='utf-8')
    problems = registry_lint.lint(path, registry_lint.EXCLUDED, registry_lint.ADAPTERS, tmp_path / 'none')
    joined = '\n'.join(problems)
    assert 'fantasy_premierleague' in joined and 'listed as excluded' in joined
    assert 'mlb_official: independence INDEPENDENT has no lineage audit' in joined
    assert 'must be https' in joined


def test_reachability_probe_render_and_verify(tmp_path):
    sources = {'s1': {'leagues': ['XL'], 'official': True, 'upstream_lineage_id': 'A', 'access_mode': 'AUTOMATED_ALLOWED'},
               's2': {'leagues': ['XL'], 'official': False, 'upstream_lineage_id': 'B', 'access_mode': 'AUTOMATED_ALLOWED'},
               's3': {'leagues': ['XL'], 'official': False, 'upstream_lineage_id': 'A', 'access_mode': 'AUTOMATED_ALLOWED'}}
    outcomes = {'s1': {'status': 'EXPECTED_CONTENT', 'detail': 'HTTP 200'}, 's2': {'status': 'UNAVAILABLE', 'detail': 'HTTP 403'}, 's3': {'status': 'EXPECTED_CONTENT', 'detail': 'HTTP 200'}}
    path = reachability.probe('local_windows', tmp_path, sources, prober=lambda sid, src: outcomes[sid])
    assert path.name.startswith('local_windows_') and reachability.verify(tmp_path) == []
    assert reachability.fallbacks(sources)['s1'] == ['s2'] and reachability.fallbacks(sources)['s2'] == ['s1', 's3']
    table = reachability.render(sources, reachability.observations(tmp_path))
    assert 'NOT_YET_PROBED' in table and 'UNAVAILABLE (HTTP 403' in table and '`s2`' in table
    with pytest.raises(ValueError):
        reachability.probe('Bad Name', tmp_path, sources)
    path.write_text(json.dumps({'schema': 'reachability-observation-1', 'environment': 'local_windows', 'sources': {'s1': {'status': 'MAYBE'}}}), encoding='utf-8')
    assert any('unknown status' in p for p in reachability.verify(tmp_path))


def test_sources_md_block_matches_the_generated_matrix():
    text = (reachability.ROOT / 'SOURCES.md').read_text(encoding='utf-8')
    block = text.split(reachability.BEGIN, 1)[1].split(reachability.END, 1)[0].strip()
    assert block == reachability.render()
    assert reachability.verify() == []
