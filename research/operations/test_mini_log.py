import json
from pathlib import Path

import pytest

from research.operations import mini_log, top_two

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = ROOT / 'research/prompts/examples/legacy_mini_log_2'
ACTIVE = (EXAMPLES / 'EXAMPLE_ACTIVE_MINI.md').read_bytes()
SETTLED = (EXAMPLES / 'EXAMPLE_SETTLED_MINI.md').read_bytes()


def errors_for(raw):
    return mini_log.analyse(raw)['errors']


def test_golden_examples_validate():
    report = mini_log.analyse(ACTIVE)
    assert report['errors'] == [] and report['warnings'] == []
    assert [c['id'] for c in report['cards']] == ['P-900', 'P-901'] and report['next_id'] == 'P-902'
    assert [a['id'] for a in report['addenda']] == ['P-900']
    settled = mini_log.analyse_settled(ACTIVE, SETTLED)
    assert settled['errors'] == []
    totals = settled['table']['summary']['totals']
    assert (totals['counted_wins'], totals['counted_live_rows'], totals['rank1_W'], totals['rank1_L']) == (2, 4, 1, 1)
    assert settled['table']['summary']['rank1_failure_classes'] == {'VARIANCE': 1}
    assert settled['table']['records'][0]['rows'][0][5] == pytest.approx(0.771)


@pytest.mark.parametrize('old,new,message', [
    ('| 1 | PICK | ANALYST_DERIVED (replaces supplied Under 6.5) | Total goals Under 7.5 — full game incl. OT/SO | 77.1%',
     '| 1 | PICK | ANALYST_DERIVED (replaces supplied Under 6.5) | Total goals Under 7.5 — full game incl. OT/SO | 50.1%',
     'non-increasing in p_card'),
    ('| 4 | INFORMATIONAL | ANALYST_DERIVED (replaces supplied Over 6.5) | Total goals Over 5.5 — full game incl. OT/SO | 52.2%',
     '| 4 | INFORMATIONAL | ANALYST_DERIVED (replaces supplied Over 6.5) | Total goals Over 5.5 — full game incl. OT/SO | NOT_ESTIMATED',
     'probabilities are mandatory'),
    ('| 2 | PICK | SUPPLIED | Northfield', '| 2 | INFORMATIONAL | SUPPLIED | Northfield', 'role must be PICK'),
    ('- **Event key:** `EXAMPLE:2026-27:EX-0002:2026-10-10`', '- **Event key:** `EXAMPLE:2026-27:EX-0001:2026-10-10`',
     'same Event key'),
    ('**P(Rank 1 and Rank 2 both lose):** 9.3%', '', 'both lose'),
    ('| Next local working P-ID | P-902 |', '| Next local working P-ID | P-903 |', 'Next local working P-ID'),
    ('## Card · P-901 ·', '## P-901 ·', 'first line must be'),
    ('`P-900 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`', '`P-900`', 'PENDING_CANONICAL_IMPORT'),
])
def test_active_mini_rule_violations(old, new, message):
    text = ACTIVE.decode('utf-8')
    assert old in text
    errors = errors_for(text.replace(old, new, 1).encode('utf-8'))
    assert any(message in e for e in errors), errors


def test_degenerate_probability_rejected():
    text = ACTIVE.decode('utf-8').replace('Total goals Under 7.5 — full game incl. OT/SO | 77.1%',
                                          'Total goals Under 7.5 — full game incl. OT/SO | 93.0%', 1)
    assert any('degenerate' in e for e in errors_for(text.encode('utf-8')))


def test_unstable_rank1_warns():
    text = ACTIVE.decode('utf-8')
    for old, new in [('77.1%', '59.0%'), ('68.2%', '58.0%'), ('56.8%', '56.0%'), ('52.2%', '52.0%')]:
        text = text.replace(old, new, 1)
    report = mini_log.analyse(text.encode('utf-8'))
    assert any('RANK1_UNSTABLE' in w for w in report['warnings'])


@pytest.mark.parametrize('old,new,message', [
    ('| 1 | Total goals Under 7.5 — full game incl. OT/SO | 77.1% | WIN | YES |',
     '| 1 | Total goals Under 7.5 — full game incl. OT/SO | 77.1% | WIN | NO |', 'Counts toward wins'),
    ('| 1 | Combined total Over 152.5 — full game incl. OT | 68.2% | LOSS |',
     '| 1 | Combined total Over 152.0 — full game incl. OT | 68.2% | LOSS |', 'proposition differs'),
    ('**Failure class.** `VARIANCE`', '**Failure class.** `BAD_LUCK`', 'Failure class must be one of'),
    ('**Knowability.**', '**Knowable?**', 'missing **Knowability.**'),
    ('**R7. Expected vs realised mechanism.** Goalie-led', '**R7 Expected** Goalie-led', 'R7.'),
    ('| 2 | Combined total Under 168.5 — full game incl. OT | 66.2% | WIN | YES | A |',
     '| 2 | Combined total Under 168.5 — full game incl. OT | 66.2% | WIN | YES | X |', 'evidence X'),
    ('**Top-two result:** `TOP2_SPLIT` — 1 counted win(s) of 2 live top-two row(s). Rank 1: WIN',
     '**Top-two result:** `TOP2_ALL_WON` — 2 counted win(s) of 2 live top-two row(s). Rank 1: WIN', 'Top-two result'),
])
def test_settled_mini_rule_violations(old, new, message):
    text = SETTLED.decode('utf-8')
    assert old in text
    outcome = mini_log.analyse_settled(ACTIVE, text.replace(old, new, 1).encode('utf-8'))
    assert any(message in e for e in outcome['errors']), outcome['errors']


def test_settled_must_extend_frozen_bytes_and_cover_every_card():
    tampered = SETTLED.replace(b'Fictional league', b'Fictional leagues', 1)
    assert any('exact bytes' in e for e in mini_log.analyse_settled(ACTIVE, tampered)['errors'])
    start = SETTLED.index(b'<!-- BEGIN SETTLEMENT P-901 -->')
    end = SETTLED.index(b'<!-- END SETTLEMENT P-901 -->') + len(b'<!-- END SETTLEMENT P-901 -->')
    missing = SETTLED[:start] + SETTLED[end:]
    assert any('P-901: no settlement block' in e for e in mini_log.analyse_settled(ACTIVE, missing)['errors'])


def test_pending_event_carries_forward(tmp_path):
    text = SETTLED.decode('utf-8')
    start = text.index('<!-- BEGIN SETTLEMENT P-901 -->')
    end = text.index('<!-- END SETTLEMENT P-901 -->')
    pending = ('<!-- BEGIN SETTLEMENT P-901 -->\n### Settlement · P-901 · Westbay Gulls vs Eastvale Pines\n\n'
               '**Card state:** `PENDING_EVENT`\nPostponed; carried forward.\n')
    settled = (text[:start] + pending + text[end:]).encode('utf-8')
    outcome = mini_log.analyse_settled(ACTIVE, settled)
    assert outcome['errors'] == [] and outcome['table']['pending_event_ids'] == ['P-901']
    carry = mini_log.carryover_from_pending(outcome['table'], ACTIVE.decode('utf-8'))
    assert len(carry) == 1 and '### Carryover · P-901 ·' in carry[0]
    assert '| 4 | INFORMATIONAL | SUPPLIED | Eastvale Pines +6.5' in carry[0]
    assert mini_log.parse_carryover(mini_log.blocks(carry[0].encode('utf-8'))[0])['errors'] == []


def test_append_inserts_before_footer_and_refreshes(tmp_path):
    text = ACTIVE.decode('utf-8')
    head = text[:text.index('<!-- BEGIN CARD P-901 -->')]
    footer = mini_log.footer('P-900', 'P-900', 0, 1, 'P-900')
    mini = tmp_path / 'mini.md'
    mini.write_text(head + footer, encoding='utf-8')
    assert mini_log.analyse(mini.read_bytes())['errors'] == []
    card = text[text.index('<!-- BEGIN CARD P-901 -->'):text.index('<!-- END CARD P-901 -->') + len('<!-- END CARD P-901 -->')]
    card_path = tmp_path / 'card.md'
    card_path.write_text(card + '\n', encoding='utf-8')
    before = mini.read_bytes()
    report = mini_log.append(mini, card_path)
    assert report['highest_id'] == 'P-901' and report['next_id'] == 'P-902'
    assert mini.read_bytes().startswith(before[:before.index(b'# RUNNING FOOTER')])
    with pytest.raises(mini_log.MiniLogError, match='next local working ID'):
        mini_log.append(mini, card_path)


ADDENDUM = ('<!-- BEGIN ADDENDUM {id} -->\n### Addendum · {id} · 2026-10-10T19:00:00+11:00\n\n'
            'Late news; ranking unchanged.\n<!-- END ADDENDUM {id} -->\n\n')


def with_addendum(cid, anchor='# RUNNING FOOTER'):
    text = ACTIVE.decode('utf-8')
    return text.replace(anchor, ADDENDUM.format(id=cid) + anchor, 1).encode('utf-8')


def test_addendum_rules():
    assert mini_log.analyse(with_addendum('P-901'))['errors'] == []
    report = mini_log.analyse(with_addendum('P-850'))
    assert report['errors'] == [] and any('earlier canonical ID' in w for w in report['warnings'])
    assert any('not a card in this mini' in e for e in errors_for(with_addendum('P-905')))
    assert any('must follow the card' in e for e in errors_for(with_addendum('P-901', '<!-- BEGIN CARD P-901 -->')))
    assert any('belong after' in e for e in errors_for(with_addendum('P-850', '## C. Active carryover')))
    bad_time = with_addendum('P-901').replace(b'2026-10-10T19:00:00+11:00', b'evening', 1)
    assert any('ISO 8601' in e for e in errors_for(bad_time))
    nested = with_addendum('P-901').replace(b'Late news; ranking unchanged.', b'## P-901 revised', 1)
    assert any('new canonical card' in e for e in errors_for(nested))


def test_addendum_never_changes_ids_or_footer(tmp_path):
    mini = tmp_path / 'mini.md'
    mini.write_bytes(ACTIVE)
    block = tmp_path / 'addendum.md'
    block.write_text(ADDENDUM.format(id='P-901'), encoding='utf-8')
    report = mini_log.add_addendum(mini, block)
    raw = mini.read_bytes()
    cut = ACTIVE.index(b'# RUNNING FOOTER')
    assert raw.startswith(ACTIVE[:cut]) and raw.endswith(ACTIVE[cut:])
    assert report['next_id'] == 'P-902' and [a['id'] for a in report['addenda']] == ['P-900', 'P-901']
    block.write_text(ADDENDUM.format(id='P-950'), encoding='utf-8')
    with pytest.raises(mini_log.MiniLogError, match='not a card in this mini'):
        mini_log.add_addendum(mini, block)


def test_frozen_sha_is_recorded_and_checked():
    digest = mini_log.sha(ACTIVE).encode()
    wrong = SETTLED.replace(digest, b'0' * 64, 1)
    assert any('does not match' in e for e in mini_log.analyse_settled(ACTIVE, wrong)['errors'])
    later = SETTLED.replace(digest, b'NOT_COMPUTED', 1)
    outcome = mini_log.analyse_settled(ACTIVE, later)
    assert outcome['errors'] == [] and any('NOT_COMPUTED' in w for w in outcome['warnings'])


def test_settlement_tail_holds_only_settlement_blocks():
    settled = SETTLED + ADDENDUM.format(id='P-901').encode('utf-8')
    assert any('only SETTLEMENT blocks' in e for e in mini_log.analyse_settled(ACTIVE, settled)['errors'])


def test_next_id_takes_first_unused_above_both_sequences():
    report = mini_log.analyse(ACTIVE)
    assert mini_log.local_next_id(report, 'P-880') == 'P-902'
    assert mini_log.local_next_id(report, 'P-950') == 'P-950'


def test_top_two_reproduces_final_settlement_cohort():
    table = json.loads((ROOT / 'research/verification/final_settlement_2026-10-09/settlement_table.json').read_text(encoding='utf-8'))
    cards = [{'id': r['id'], 'sport': r['sport'], 'no_forecast': r.get('no_forecast', False), 'winner_call': r['winner_call'][1],
              'rows': [(row[0], row[2], None, row[1]) for row in r['rows']]} for r in table['records']]
    totals = top_two.summarise(cards)['totals']
    assert (totals['counted_wins'], totals['counted_live_rows']) == (79, 134)
    assert (totals['rank1_W'], totals['rank1_L'], totals['rank1_V']) == (40, 28, 3)
    assert (totals['TOP2_ALL_WON'], totals['TOP2_SPLIT'], totals['TOP2_ALL_LOST'], totals['VOID']) == (27, 26, 15, 3)
    assert totals['hit_at_2'] == 53 and totals['no_forecast_cards'] == 1


def test_top_two_primitives():
    assert top_two.card_outcome([(1, 'W'), (2, 'V'), (3, 'L')]) == ('TOP2_ALL_WON', 1, 1)
    assert top_two.card_outcome([(1, 'V'), (2, 'P')]) == ('VOID', 0, 0)
    assert top_two.card_outcome([(1, 'L'), (2, 'L'), (3, 'W'), (4, 'W')]) == ('TOP2_ALL_LOST', 0, 2)
    assert top_two.grade_code('**WIN**') == 'W' and top_two.grade_code('void') == 'V'
    lo, hi = top_two.wilson(304, 491)
    assert round(lo, 3) == 0.575 and round(hi, 3) == 0.661
    assert top_two.family('1st Half Over 0.5 goals') == 'first_half_goals'
    assert top_two.family('Bellucci -3.5 games') == 'tennis_games'
    assert top_two.family('Guangxi double chance X2') == 'side_cushion_or_handicap'
    assert top_two.family('Total corners Under 10.5') == 'corners'
    assert top_two.ndcg_at_2([(1, 'W'), (2, 'L'), (3, 'W'), (4, 'W')]) == pytest.approx(1 / (1 + 1 / 1.584962500721156))


def test_join_builds_the_settled_mini_byte_exactly(tmp_path):
    frozen = tmp_path / 'frozen.md'; frozen.write_bytes(ACTIVE)
    section = tmp_path / 'section.md'
    tail = SETTLED[len(ACTIVE):].replace(mini_log.sha(ACTIVE).encode(), b'NOT_COMPUTED', 1)
    section.write_bytes(tail.lstrip(b'\n'))
    out = tmp_path / 'settled.md'
    outcome = mini_log.join(frozen, section, out)
    assert out.read_bytes() == SETTLED and outcome['errors'] == [] and outcome['warnings'] == []
    assert mini_log.join(frozen, out, out)['errors'] == []  # a full settled copy is accepted unchanged
    edited = tmp_path / 'edited.md'; edited.write_bytes(SETTLED.replace(b'Fictional league', b'Fictional leagues', 1))
    with pytest.raises(mini_log.MiniLogError, match='frozen part was edited'):
        mini_log.join(frozen, edited, tmp_path / 'other.md')
