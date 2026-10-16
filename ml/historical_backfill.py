"""Fetch MLB/NHL owner results, independently reconcile ESPN, then ingest only matching finals.

Raw HTTP bodies stay in the external cache; durable CSV projections retain native IDs,
source URLs, retrieval times, raw hashes and endpoint evidence. A newly captured historical
fact becomes known NOW, never on its game date. final_at is explicitly an OBSERVED_FINAL
upper bound, not an invented final whistle time. No retrospective pregame claim follows.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import urllib.request

import pandas as pd

from ml import primary as p, research_ingest as ri


def fetch(url, cache):
    cache=Path(cache); cache.mkdir(parents=True,exist_ok=True)
    raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'SportsResearch result verification'}),timeout=45).read()
    at=datetime.now(timezone.utc).isoformat(); sha=p.digest(raw)
    (cache/(sha+'.json')).write_bytes(raw)
    return json.loads(raw),dict(source_url=url,retrieved_at=at,raw_sha256=sha,raw_bytes=len(raw),external_raw_capture=str(cache/(sha+'.json')))


def name(value):
    return re.sub(r'[^a-z0-9]','',value.lower().replace('la angels','los angeles angels').replace('la dodgers','los angeles dodgers'))


def nhl_abbrev(value):
    # Reviewed provider code aliases; the sporting franchise identity is unchanged.
    return {'NJ':'NJD','LA':'LAK','TB':'TBL','SJ':'SJS','UTAH':'UTA'}.get(value,value)


def espn_rows(data, requested_date):
    rows=[]
    for ev in data.get('events',[]):
        co=ev['competitions'][0]; sides={r['homeAway']:r for r in co['competitors']}
        if not ev['status']['type']['completed']: continue
        rows.append(dict(date=requested_date,event_id=ev['id'],home=sides['home']['team']['displayName'],away=sides['away']['team']['displayName'],
                         home_abbrev=sides['home']['team']['abbreviation'],away_abbrev=sides['away']['team']['abbreviation'],
                         hs=int(sides['home']['score']),as_=int(sides['away']['score']),event_at=ev['date'],status='FINAL',
                         home_periods=';'.join(f"{int(x.get('period',i+1))}:{int(x['value'])}" for i,x in enumerate(sides['home'].get('linescores',[]))),
                         away_periods=';'.join(f"{int(x.get('period',i+1))}:{int(x['value'])}" for i,x in enumerate(sides['away'].get('linescores',[])))))
    return rows


def mlb_rows(data):
    rows=[]
    for day in data['dates']:
        for g in day['games']:
            if g['status']['abstractGameState']!='Final' or g['gameType']!='R': continue
            line=g.get('linescore',{}); innings=line.get('innings',[]); scheduled=line.get('scheduledInnings',9)
            if not innings: continue
            totals={s:int(g['teams'][s]['score']) for s in ('home','away')}
            if any(sum(i.get(s,{}).get('runs',0) for i in innings)!=totals[s] for s in totals): continue
            reg={s:sum(i.get(s,{}).get('runs',0) for i in innings if i['num']<=scheduled) for s in totals}
            extra=max(i['num'] for i in innings)>scheduled
            # Shortened games do not stand in for a regulation-length training endpoint.
            if max(i['num'] for i in innings)<scheduled: continue
            rows.append(dict(date=day['date'],event_id='MLB:'+str(g['gamePk']),provider_id=str(g['gamePk']),event_at=g['gameDate'],
                             home=g['teams']['home']['team']['name'],away=g['teams']['away']['team']['name'],venue=g['venue']['name'],
                             hs=totals['home'],as_=totals['away'],reg_hs=reg['home'],reg_as=reg['away'],decision='EXTRAS' if extra else 'Regulation',
                             endpoint='FULL_GAME_INCL_EXTRAS',competition='Baseball/MLB',season=str(g['season']),
                             innings=';'.join(f"{i['num']}:{i.get('home',{}).get('runs','X')}:{i.get('away',{}).get('runs','X')}" for i in innings)))
    return rows


def nhl_rows(data):
    rows=[]
    for g in data['games']:
        if g['gameState'] not in ('OFF','FINAL') or g['gameType']!=2: continue
        h,a=g['homeTeam'],g['awayTeam']; hs,away=int(h['score']),int(a['score'])
        period=g['gameOutcome']['lastPeriodType']; extra=period in ('OT','SO')
        if extra and abs(hs-away)!=1: continue
        reg=min(hs,away) if extra else None
        rows.append(dict(date=g['gameDate'],event_id='NHL:'+str(g['id']),provider_id=str(g['id']),event_at=g['startTimeUTC'],
                         home=h['abbrev'],away=a['abbrev'],venue=g['venue']['default'],hs=hs,as_=away,
                         reg_hs=reg if extra else hs,reg_as=reg if extra else away,
                         decision={'OT':'Overtime','SO':'Shootout'}.get(period,'Regulation'),endpoint='FULL_GAME_INCL_OT_SO',
                         competition='Ice Hockey/NHL',season=str(g['season']),innings=period))
    return rows


def run(kind, start, end, cache, out, store, club='TOR', season='20242025'):
    out=Path(out); out.mkdir(parents=True,exist_ok=False)
    if kind=='mlb':
        url=f'https://statsapi.mlb.com/api/v1/schedule?sportId=1&startDate={start}&endDate={end}&hydrate=linescore,gameInfo'
    else: url=f'https://api-web.nhle.com/v1/club-schedule-season/{club}/{season}'
    if kind=='nhl' and club=='ALL':
        discovery,discovery_receipt=fetch(f'https://api-web.nhle.com/v1/club-schedule-season/TOR/{season}',cache)
        clubs=sorted({g[s]['abbrev'] for g in discovery['games'] for s in ('homeTeam','awayTeam') if g['gameType']==2})
        if len(clubs)<20: raise p.AdmissionError('incomplete NHL competition discovery')
        def club_fetch(code):
            source=f'https://api-web.nhle.com/v1/club-schedule-season/{code}/{season}'
            data,receipt=fetch(source,cache)
            return [dict(r,owner_source_url=source) for r in nhl_rows(data)],receipt
        with ThreadPoolExecutor(max_workers=6) as pool: club_data=list(pool.map(club_fetch,clubs))
        owner_by_id={}
        for rows,_ in club_data:
            for row in rows:
                old=owner_by_id.get(row['event_id'])
                if old and any(old[k]!=row[k] for k in row if k!='owner_source_url'):
                    raise p.AdmissionError('owner club schedules disagree on event identity/result')
                owner_by_id[row['event_id']]=row
        owner=list(owner_by_id.values()); owner_receipts=[discovery_receipt]+[r for _,r in club_data]
    else:
        data,owner_receipt=fetch(url,cache)
        owner=[dict(r,owner_source_url=url) for r in (mlb_rows if kind=='mlb' else nhl_rows)(data)]
        owner_receipts=[owner_receipt]
    owner=[r for r in owner if start<=r['date']<=end]
    dates=sorted({r['date'] for r in owner})
    sport='baseball' if kind=='mlb' else 'hockey'
    def secondary(day):
        url=f"https://site.api.espn.com/apis/site/v2/sports/{sport}/{kind}/scoreboard?dates={day.replace('-','')}&limit=100"
        try:
            data,receipt=fetch(url,cache); return espn_rows(data,day),receipt
        except Exception as exc:
            return [],dict(source_url=url,retrieved_at=datetime.now(timezone.utc).isoformat(),raw_sha256='',raw_bytes=0,external_raw_capture='',error=type(exc).__name__+': '+str(exc))
    with ThreadPoolExecutor(max_workers=6) as pool: secondary_data=list(pool.map(secondary,dates))
    other=[r for rows,_ in secondary_data for r in rows]
    receipts=[dict(**r,error='') for r in owner_receipts]+[dict(**r,error=r.get('error','')) if 'error' not in r else r for _,r in secondary_data]
    # Captures are fact-only tabular projections; raw HTTP identity is retained separately.
    owner_path=out/'OWNER_RESULTS.csv'; other_path=out/'INDEPENDENT_RESULTS.csv'
    if not owner or not other: raise p.AdmissionError('no owner/independent final results: preserve diagnostics; do not ingest')
    owner_path.write_bytes(p.csv_bytes(owner)); other_path.write_bytes(p.csv_bytes(other)); (out/'HTTP_RECEIPTS.csv').write_bytes(p.csv_bytes(receipts))
    games=[]; decisions=[]; used=set()
    for r in owner:
        participant_matches=[s for s in other if s['date']==r['date'] and
                 ((name(s['home'])==name(r['home']) and name(s['away'])==name(r['away'])) if kind=='mlb' else (nhl_abbrev(s['home_abbrev'])==r['home'] and nhl_abbrev(s['away_abbrev'])==r['away']))]
        matches=[s for s in participant_matches if p.clock(s['event_at'])==p.clock(r['event_at'])]
        time_note=''
        # ESPN sometimes lists the TV window ten minutes before MLB's first pitch.
        # Resolve timing at the field owner only for a unique same-day matchup, never a doubleheader.
        owner_pair=[s for s in owner if (s['date'],s['home'],s['away'])==(r['date'],r['home'],r['away'])]
        if not matches and kind=='mlb' and len(participant_matches)==len(owner_pair)==1:
            offset=(p.clock(r['event_at'])-p.clock(participant_matches[0]['event_at'])).total_seconds()/60
            if 0<abs(offset)<=15:
                matches=participant_matches; time_note=f';START_TIME_OWNER_PRIORITY_ESPN_OFFSET_MINUTES={offset:g}'
        matching=[s for s in matches if (s['hs'],s['as_'])==(r['hs'],r['as_'])]
        if len(matching)!=1:
            decisions.append(dict(event_id=r['event_id'],status='NOT_INGESTED',reason='INDEPENDENT_ID_OR_SCORE_MATCH_NOT_UNIQUE',independent_event_id=''))
            continue
        s=matching[0]
        def reg_periods(text, maximum):
            return sum(int(value) for period,value in (entry.split(':') for entry in text.split(';') if entry) if int(period)<=maximum)
        if not s['home_periods'] or not s['away_periods']:
            decisions.append(dict(event_id=r['event_id'],status='NOT_INGESTED',reason='INDEPENDENT_PERIOD_COVERAGE_MISSING',independent_event_id=s['event_id']))
            continue
        maximum=9 if kind=='mlb' else 3
        if (reg_periods(s['home_periods'],maximum),reg_periods(s['away_periods'],maximum))!=(r['reg_hs'],r['reg_as']):
            decisions.append(dict(event_id=r['event_id'],status='NOT_INGESTED',reason='INDEPENDENT_REGULATION_CONFLICT',independent_event_id=s['event_id']))
            continue
        if s['event_id'] in used:
            raise p.AdmissionError('independent result joined to multiple owner events')
        used.add(s['event_id'])
        secondary_receipt=next(rec for _,rec in secondary_data if f"dates={r['date'].replace('-','')}" in rec['source_url'])
        owner_receipt=next(rec for rec in owner_receipts if rec['source_url']==r['owner_source_url'])
        # Conservative first-observed availability: both current captures must have been retrieved.
        known=max(owner_receipt['retrieved_at'],secondary_receipt['retrieved_at'])
        values=dict(competition=r['competition'],endpoint=r['endpoint'],native_event_id=r['event_id'],season=r['season'],event_at=r['event_at'],home=r['home'],away=r['away'],venue=r['venue'],status='FINAL',
                    **{k:str(r[k]) for k in ('hs','as_','reg_hs','reg_as','decision')},final_at=known,source_kind='WEB_RECOVERED',published_at='',retrieved_at=known,known_at=known,review_status='RESEARCH_INPUT_REVIEWED',collected_by='SOURCE_BACKFILL_CURRENT_CAPTURE_FINAL_UPPER_BOUND')
        # Retain both observations; independent scores corroborate finals, owner line scores define regulation.
        games.append(dict(**values,source_url=r['owner_source_url'],capture_path=owner_path.as_posix(),capture_sha256=p.digest(owner_path.read_bytes())))
        games.append(dict(**values,source_url=secondary_receipt['source_url'],capture_path=other_path.as_posix(),capture_sha256=p.digest(other_path.read_bytes())))
        decisions.append(dict(event_id=r['event_id'],status='VERIFIED_FOR_FUTURE_TRAINING',reason='OWNER_INNINGS_OR_PERIOD_AND_INDEPENDENT_FINAL_AGREE;FINAL_AT_OBSERVED_UPPER_BOUND;KNOWN_NOW'+time_note,independent_event_id=s['event_id']))
    export=out/'EXPORT'; export.mkdir()
    for filename,fields in ri.EXPORT_FILES.items():
        rows=games if filename=='GAME_OBSERVATIONS.csv' else []
        (export/filename).write_bytes(p.csv_bytes(rows) if rows else (','.join(fields)+'\n').encode())
    (out/'RECONCILIATION.csv').write_bytes(p.csv_bytes(decisions))
    rec=ri.ingest(export,Path(store)); (out/'INGEST.csv').write_bytes(p.csv_bytes([rec]))
    (out/'README.md').write_text('# Verified historical backfill\n\nOwner results and ESPN finals matched by date, participants, exact scheduled UTC instant and score. Native provider IDs distinguish doubleheaders. Regulation derives from owner innings or NHL OT/SO rule; the independent source corroborates finals only. `final_at` is the current observed-final upper bound, not an actual final whistle time. `known_at` is current retrieval, so these rows cannot enter historical pregame replays. Player lineups are not reconstructed from final box scores. Raw HTTP bodies remain in the external cache named in HTTP_RECEIPTS.csv; the committed fact projections and hashes are the ingest evidence. Every owner candidate has a reconciliation disposition. This is a bounded backfill, not closure of all historical cards.\n',encoding='utf-8')
    return rec


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--kind',choices=('mlb','nhl'),required=True)
    for name in ('start','end','cache','out','store'): parser.add_argument('--'+name,required=True)
    parser.add_argument('--club',default='TOR'); parser.add_argument('--season',default='20242025'); args=parser.parse_args(argv)
    print(run(args.kind,args.start,args.end,Path(args.cache),Path(args.out),Path(args.store),args.club,args.season))


if __name__=='__main__': main()
