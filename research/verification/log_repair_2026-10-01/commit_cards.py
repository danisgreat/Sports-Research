from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from research.operations.log_card import commit,next_id,verify_projection,research_cards
from research.src.issue import PART6,CANONICAL_LEDGER,_custody
from research.src.ledger import read_records
A=Path(__file__).resolve().parent
D=Path((A/'delivery_dir.txt').read_text(encoding='utf-8'))
receipt=json.loads((D/'kbo_game_receipt.json').read_text(encoding='utf-8'))
game=next(g for g in json.loads((D/'kbo_game.body').read_text(encoding='utf-8'))['game'] if g['G_ID']=='20261001HHSS0')
if (game['T_SCORE_CN'],game['B_SCORE_CN'],game['GAME_INN_NO'],game['GAME_TB_SC']) != ('0','0',3,'T'):
    raise ValueError('new state needs analysis review before commitment')
analysis=A/'KBO_HANWHA_SAMSUNG_ANALYSIS.md'
text=analysis.read_text(encoding='utf-8')
text+='\n## Final refresh before canonical logging\n\n'
text+=f"Owner response at **{receipt['retrieved_utc']} / 20:31 AEST**: **Hanwha 0–0 Samsung, top third**; zero outs, first-base occupancy marker, Won pitching and Jung Eun-won batting in the feed. Body `{receipt['body_path']}`, SHA `{receipt['response_sha256']}`. The first TWO innings have now finished without a run. This strengthens the preferred Under 11.5; ranks remain Under, Samsung −0.5, Hanwha +2.5, Over, with Samsung the potential winner. This is an after-start analysis at its real logging time, conditional on the retained state, not a pregame freeze. Posted-order confirmation was refreshed alongside the state. No final score, grade or retrospective is added.\n"
analysis.write_text(text,encoding='utf-8')
freeze=ROOT/'CONTROL_MANIFEST_2026-10-01-3.md'
freeze_sha=hashlib.sha256(freeze.read_text(encoding='utf-8-sig').replace('\r\n','\n').replace('\r','\n').replace('\n','\r\n').encode('utf-8')).hexdigest()
admin=(b'> CURRENT OPERATING STATUS - October 1 v7.1: Requested research cards are canonically logged regardless of calibration, with honest live/late times. Read GAME_LOG_STATUS_CURRENT.md or research.operations.log_card next-id for the actual next ID. The September opening and earlier audit snapshots below are historical. Preserve all original forecast bytes; no mandatory pre-start buffer applies to current requested analysis.\r\n\r\n')
before,_=_custody(PART6)
if not before.startswith(admin):
    # An added administrative prefix; all prior Part 6 bytes stay contiguous.
    PART6.write_bytes(admin+before)
results=[]
for file in json.loads((A/'cards_to_import.json').read_text(encoding='utf-8')):
    card=json.loads(Path(file).read_text(encoding='utf-8'))
    if card['league']=='NPB':
        first=card['body'].index('**New assessment:')
        table=card['body'].index('| Rank |',first)
        card['body']=card['body'][:first]+f"**New assessment: UNCALIBRATED_QUALITATIVE; numerical p and baseline NOT_ESTIMATED.** The initial owner capture at 09:40 UTC showed 2–0/bottom third; the 09:57 refresh showed 2–0/top fifth. The latest owner snapshot in `{D.relative_to(ROOT).as_posix()}/npb_game.body`, retained about 10:31 UTC, shows **HIROSHIMA 4–1 CHUNICHI, TOP SEVENTH**. This current owner state controls the new live ranks. Sportsnavi's 0–0/bottom-first update at 18:05 JST is stale and not an agreeing current-state source. The schedule remains 18:00 JST/19:00 AEST. This is a dated live assessment, not a reconstructed pregame forecast.\n\n"+card['body'][table:]
        start=card['body'].index('| Rank |');end=card['body'].index('**Potential winner:',start)
        newtable=('| Rank | Pick | Reason and limitation |\n|---:|---|---|\n'
          '| 1 | Carp +1.5 | Hiroshima leads 4–1 in the retained owner state. The cushion still succeeds on a final home win, tie or one-run defeat; Chunichi would need a substantial late reversal to defeat it. Current lead and innings outweigh the earlier starter ERA comparison. |\n'
          '| 2 | Over 6.5 runs | Five runs are already recorded entering the seventh; two more satisfy this proposition. There are remaining offensive innings and potential relief/extra-inning runs. This is a modest qualitative preference, not a measured probability. |\n'
          '| 3 | Under 6.5 runs | It needs at most one additional run from the retained state. The earlier low-ERA starter context and scoreless innings support this route, but only a small remaining allowance remains. A two-run inning defeats it. |\n'
          '| 4 | Dragons +1.5 | Chunichi currently trails by three and must reduce the final deficit to at most one, tie or win. Five recorded hits show scoring opportunities, but a late two-plus-run net comeback is a weaker view than preserving Hiroshima’s cushion. |\n\n')
        card['body']=card['body'][:start]+newtable+card['body'][end:]
        card['body']=card['body'].replace('based on its verified two-run lead','based on its verified three-run lead')
    if card['event_key']=='KBO:2026:20261001HHSS0':card['body']=analysis.read_text(encoding='utf-8')
    card['body']=(f"Operating authority for this canonical action: **MDS-2026.10.01-v7.1 / CR-2026.10.01-I2**; scoring SCV-2026.10.01-v3. Selected control receipt `CONTROL_MANIFEST_2026-10-01-3.md`, normalized-CRLF SHA `{freeze_sha}`. Original text below keeps its own historical method/receipt claims.\n\n"+card['body'])
    frozen=A/(card['tracking_handle']+'_committed_input.json')
    with frozen.open('x',encoding='utf-8') as handle:json.dump(card,handle,indent=2,ensure_ascii=False);handle.write('\n')
    result=commit(card);results.append({**result,'event_key':card['event_key'],'tracking_handle':card['tracking_handle'],'input_path':str(frozen)})
    print(result['card_id'],card['title'])
if [r['card_id'] for r in results] != ['P-523','P-524','P-525','P-526'] or next_id()!='P-527':raise ValueError('unexpected canonical ID sequence')
mini=next((ROOT/'Mini logs (to be sent to actual log later)').rglob('PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md'))
old=mini.read_bytes();retained=A/'originals/mini_at_retirement.md'
with retained.open('xb') as handle:handle.write(old)
old_sha=hashlib.sha256(old).hexdigest()
mini.write_text('# Mini log retired — canonical cards imported into Part 6\n\n'
 'This is a reference pointer, not an active running log. Use `prediction logs/PREDICTION_LOG_COMBINED_6.md` and `research.operations.log_card` for all new requested cards, regardless of calibration. The current next ID is **P-527**; the live register/allocator controls later changes.\n\n'
 '| Canonical ID | Retained card |\n|---|---|\n| P-523 | Oriente Petrolero vs The Strongest |\n| P-524 | KT Wiz @ Kia Tigers |\n| P-525 | Chunichi Dragons @ Hiroshima Toyo Carp |\n| P-526 | Hanwha Eagles @ Samsung Lions |\n\n'
 f'Full previous mini text, including its earlier audit and inherited rules, is preserved byte-for-byte at `research/verification/log_repair_2026-10-01/originals/mini_at_retirement.md` (SHA `{old_sha}`). The individual original cards are retained under `research/issued_research/`, hashed in the canonical ledger and displayed in Part 6 with dated corrections. Original forecasts and timestamps are unchanged. No new retrospective is performed.\n',encoding='utf-8')
for card in research_cards(read_records(CANONICAL_LEDGER)):verify_projection(card,PART6)
(A/'COMMIT_RECEIPTS.json').write_text(json.dumps({'logged_utc':datetime.now(timezone.utc).isoformat(),'cards':results,'next_id':next_id(),'freeze_sha256':freeze_sha,'mini_original_sha256':old_sha,'part6_previous_bytes_retained_contiguously':PART6.read_bytes().count(before)==1},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Verified four canonical cards; next P-527. Mini retired with exact original retained.')
