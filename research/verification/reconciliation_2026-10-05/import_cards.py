from pathlib import Path
from datetime import datetime, timezone
import json,re,hashlib
from research.operations.log_card import commit,next_id,research_cards,pending
from research.src.ledger import read_records
from research.src.issue import CANONICAL_LEDGER,PART6,_custody

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
ORIGINALS=OUT/'originals'
if __name__=='__main__':
    records=read_records(CANONICAL_LEDGER)
    if pending(records): raise ValueError('Recover pending canonical transaction first')
    print('Opening verified next ID:',next_id(),flush=True)
    raw,_=_custody(PART6)
    old=(ORIGINALS/'prediction logs/PREDICTION_LOG_COMBINED_6.md').read_bytes()
    if raw!=old: raise ValueError('Part 6 changed since opening inventory')
    mini_path=ORIGINALS/'fallback_mini_source.txt'
    mini=mini_path.read_text(encoding='utf-8-sig')
    source_path=ORIGINALS/'consolidated_source.txt'
    supplied=source_path.read_text(encoding='utf-8-sig')
    sections=re.split(r'(?m)(?=^## \d+\. )',supplied)[1:]
    sections[-1]=sections[-1].split('**End of consolidated log entries.**')[0].rstrip()
    assert len(sections)==10
    header='Historical research import on 2026-10-05 (Australia/Sydney). Authority: MDS-2026.10.01-v7.1 / CR-2026.10.01-I2; SCV-2026.10.01-v3. Selected freeze CONTROL_MANIFEST_2026-10-01-5.md, normalized-CRLF SHA-256 1fc4151afd0e9dfa0202ab8f1de1ee5487e41df8fb443d1fa83f5d95df644754. Opening freeze/custody failures are documented in the dated reconciliation report. Canonical projection/source and ledger checks passed. Actual import time is retained by the transactional logger. Original observations, states and VERIFIED labels below are source claims, not newly certified facts. NO_PROSPECTIVE_ISSUE / NOT PERFORMANCE_ELIGIBLE. Missing probabilities, baseline and operator terms remain missing.\n\n'
    first=[
      ('P-527','Hapoel Tel Aviv vs Real Madrid — October 1, 2026','EuroLeague','TMP-20261002-EUR-HTA-RMA','UNKNOWN','HISTORICAL_UNCALIBRATED_RESEARCH_IMPORT'),
      ('P-528','Grand Rapids Griffins @ Cleveland Monsters — October 2, 2026','AHL','LOCAL-P528-GR-CLE-20261002','1029073','HISTORICAL_UNCALIBRATED_RESEARCH_IMPORT'),
      ('P-529','Philadelphia Flyers @ New Jersey Devils — October 1, 2026','NHL','TMP-20261002-NHL-PHI-NJD','2026020009','HISTORICAL_RESEARCH_IMPORT_LIVE_CLAIM_IN_LATER_SUMMARY'),
      ('P-530','Philadelphia Phillies @ Atlanta Braves — NL Wild Card Game 3','MLB','TMP-20261002-MLB-PHI-ATL-G3','849844','HISTORICAL_LATE_UNCALIBRATED_RESEARCH_IMPORT'),
      ('P-531','Indiana Fever @ Las Vegas Aces — First Round Game 3','WNBA','TMP-20261002-WNBA-IND-LVA-G3','1042600123','HISTORICAL_LATE_UNCALIBRATED_RESEARCH_IMPORT'),
    ]
    results=[]
    for expected,title,league,alias,native,status in first:
        row=next(line for line in mini.splitlines() if line.startswith('| **'+expected+'** |'))
        body=header+'### Original fallback summary\n\n'+mini[mini.index('| Local reservation |'):mini.index('| **P-527** |')]+row+'\n\n'
        body+='Only the summary survives for the first four fallback records. Original full rationale/cutoff/contract terms are NOT_RETAINED_IN_SUMMARY; they cannot be reconstructed from the result. The next heading is an original-source exhibit, not a new issue.\n\n'
        if expected=='P-531':
            full=mini[mini.index('## P-531 —'):mini.index('## Queue / Custody')]
            full=re.sub(r'^## P-531 —.*$', '### Original retained WNBA card',full,flags=re.M)
            body+=full
        else:
            body+='Original summary p, q, p_model, p_card and baseline literals: NOT_RETAINED_IN_SUMMARY. Later supplied missingness labels stay separately attributed to their source.\n'
        if next_id()!=expected: raise ValueError('Canonical order drift')
        result=commit(dict(event_key=alias,title=title,league=league,native_event_id=native,tracking_handle=alias,analysis_status=status,source_path=str(mini_path),body=body))
        results.append(dict(**result,title=title,tracking_handle=alias,source_version='ORIGINAL_FALLBACK_MINI',supplied_section=None))
        print(result['card_id'],title,flush=True)
    # Four overlapping versions belong to the existing IDs as dated additions.
    overlaps={1:'P-527',2:'P-529',3:'P-530',4:'P-531'}
    extra_native={0:'36f713cb-58ad-11f1-b8d2-f1316c48f9c2',5:'UNKNOWN (Naver provider 20261003HTLG02026)',6:'UNKNOWN (owner route /draw/nrl-premiership/2026/grand-final/game-1/)',7:'UNKNOWN',8:'2006888',9:'UNKNOWN (ESPN provider 401921339)'}
    leagues={0:'NBL',5:'KBO',6:'NRL',7:'Greek Basket League',8:'BBL',9:'International Friendly'}
    append='\n<!-- BEGIN SOURCE RECONCILIATION 2026-10-05 -->\n## October 5 source reconciliation — original versions retained\n\nThe five formerly local reservations above are now transactionally canonical. Four entries in the supplied consolidated source refer to those same events and retain conflicting ranks/contracts/statuses. They are source-version addenda against the existing IDs, not replacements and not new forecasts. No retrospectively preferred version is selected.\n\n'
    for i,section in enumerate(sections):
        alias=re.search(r'\*\*Tracking Reference:\*\* ([^\s]+)',section)[1]
        title=section.splitlines()[0].split(' — ',1)[1]
        if i in overlaps:
            cid=overlaps[i]
            append+=f'### Consolidated-source addendum against {cid}\n\n'+section+'\n\n'
            results.append(dict(card_id=cid,title=title,tracking_handle=alias,source_version='CONSOLIDATED_ADDENDUM',supplied_section=i+1))
        else:
            status='HISTORICAL_INTAKE_NO_FORECAST_ISSUED' if i==0 else 'HISTORICAL_UNCALIBRATED_RESEARCH_IMPORT'
            result=commit(dict(event_key=alias,title=title,league=leagues[i],native_event_id=extra_native[i],tracking_handle=alias,analysis_status=status,source_path=str(source_path),body=header+'### Supplied consolidated source — literal retained content\n\n'+section))
            results.append(dict(**result,title=title,tracking_handle=alias,source_version='CONSOLIDATED_IMPORT',supplied_section=i+1)); print(result['card_id'],title,flush=True)
    append+='<!-- END SOURCE RECONCILIATION 2026-10-05 -->\n'
    projection=append.replace('\n','\r\n').encode('utf-8')
    (OUT/'source_reconciliation_projection.bin').write_bytes(projection)
    with PART6.open('ab') as f:f.write(projection);f.flush();__import__('os').fsync(f.fileno())
    if PART6.read_bytes().count(projection)!=1:raise ValueError('Addendum readback failed')
    (OUT/'import_results.json').write_text(json.dumps(dict(logged_utc=datetime.now(timezone.utc).isoformat(),records=results,next_id=next_id(),addendum_sha256=hashlib.sha256(projection).hexdigest()),indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('Verified next ID:',next_id())
