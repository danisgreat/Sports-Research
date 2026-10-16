"""Source-addressed historical identity reconciliation without renumbering issued P-IDs.

An issued P-ID is an alias, never a unique sporting-event key. Each colliding
original heading receives a source/body address. Grade linkage stays unresolved
unless an original body and exact contract can be located; title similarity alone
does not prove a settlement belongs to it.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re

from ml import primary as p
from ml.evaluation.card_history import LOGS, id_collisions

FIELDS = ('issued_card_id','record_uid','event_title','source_path','heading_line','body_end_line',
          'source_sha256','body_sha256','identity_status','grade_link_status')


def reconcile(logs=LOGS):
    collision_ids=set(id_collisions(logs).card)
    heading=re.compile(r'^#{1,4} .{0,8}`?(P-\d{3})`?(?: \([^)]*\))? — (.+)')
    records=[]
    for path in logs:
        path=Path(path)
        if not path.exists(): continue
        raw=path.read_bytes(); lines=raw.decode('utf-8-sig',errors='strict').splitlines(keepends=True)
        matches=[(i,heading.match(line)) for i,line in enumerate(lines) if heading.match(line)]
        for j,(i,match) in enumerate(matches):
            card,title=match.groups()
            if card not in collision_ids: continue
            if re.match(r'(settlement|retrospective|deep|addendum|r1[^0-9]|revision|correction|post-|import)',title,re.I): continue
            if re.search(r'\d+\s*[-–]\s*\d+|\d+;|settle|retro|result|final score',title,re.I) or re.match(r'(#|both top|original rank|retained historical|successful|\d+ under)',title,re.I): continue
            end=matches[j+1][0] if j+1<len(matches) else len(lines)
            body=''.join(lines[i:end]).encode('utf-8')
            source=path.as_posix()
            if path.is_absolute():
                try: source=path.relative_to(Path.cwd()).as_posix()
                except ValueError: pass
            record_uid='HREC-'+p.digest((source+'|'+str(i+1)+'|'+p.digest(body)).encode())[:24]
            records.append(dict(issued_card_id=card,record_uid=record_uid,event_title=title.strip(),source_path=source,
                                heading_line=i+1,body_end_line=end,source_sha256=p.digest(raw),body_sha256=p.digest(body),
                                identity_status='SOURCE_RECORD_DISAMBIGUATED',grade_link_status='UNRESOLVED_UNTIL_EXACT_BODY_CONTRACT_MATCH'))
    return records


def verify(path):
    records=p.read_rows(Path(path)); seen=set()
    if not records or tuple(records[0])!=FIELDS: raise p.AdmissionError('identity map schema/coverage missing')
    for row in records:
        if row['record_uid'] in seen: raise p.AdmissionError('duplicate historical record UID')
        seen.add(row['record_uid']); raw=p.receipt_file(row['source_path'],row['source_sha256'])
        lines=raw.decode('utf-8-sig').splitlines(keepends=True)
        body=''.join(lines[int(row['heading_line'])-1:int(row['body_end_line'])]).encode()
        if p.digest(body)!=row['body_sha256']: raise p.AdmissionError('historical identity body changed')
    expected=reconcile()
    if {r['record_uid'] for r in expected}!={r['record_uid'] for r in records}: raise p.AdmissionError('incomplete historical collision inventory')
    return records


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('command',choices=('build','verify')); parser.add_argument('--map',type=Path,required=True)
    args=parser.parse_args(argv)
    if args.command=='build':
        rows=reconcile(); args.map.parent.mkdir(parents=True,exist_ok=True)
        with args.map.open('xb') as f: f.write(p.csv_bytes(rows))
    rows=verify(args.map)
    print(f'{len(rows)} source-addressed records across {len({r["issued_card_id"] for r in rows})} colliding aliases; grade links remain explicit')


if __name__=='__main__': main()
