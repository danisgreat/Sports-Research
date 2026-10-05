from pathlib import Path
from datetime import datetime, timezone
from urllib.request import urlopen, Request
from concurrent.futures import ThreadPoolExecutor
import json, hashlib
from research.src.sources import fetch_source

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
QUARANTINE=ROOT/'research/data/benchmark/reconciliation_2026-10-05'
QUARANTINE.mkdir(parents=True,exist_ok=True)
JOBS=[
 ('nbl_schedule','nbl_official','https://schedule.nbl.com.au/api/calendar/schedule?league=NBL&limit=500&offset=0&year=2026'),
 ('mlb_feed','mlb_official','https://statsapi.mlb.com/api/v1.1/game/849844/feed/live'),
 ('nhl_summary',None,'https://www.nhl.com/scores/htmlreports/20262027/GS020009.HTM'),
 ('nhl_box',None,'https://api-web.nhle.com/v1/gamecenter/2026020009/boxscore'),
 ('euro_games',None,'https://feeds.incrowdsports.com/provider/euroleague-feeds/v2/competitions/E/seasons/E2026/games'),
 ('wnba_box',None,'https://cdn.wnba.com/static/json/liveData/boxscore/boxscore_1042600123.json'),
 ('wnba_espn',None,'https://site.api.espn.com/apis/site/v2/sports/basketball/wnba/summary?event=401918022'),
 ('kbo_owner',None,'https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-10-03'),
 ('nrl_owner',None,'https://www.nrl.com/draw/data?competition=111&season=2026&round=31'),
 ('gbl_club',None,'https://www.paobc.gr/schedule/panathinaikos-bc-aktor-vikos-falcons-04-10-2026/'),
 ('bbl_owner',None,'https://www.easycredit-bbl.de/de/n/news/2026/oktober/niederlage-mit-negativrekord-spitzenreiter-oldenburg-geht-in-muenchen-unter'),
 ('ahl_club',None,'https://griffinshockey.com/news/october-2-2026-griffins-5-at-monsters-2'),
 ('soccer_owner_schedule',None,'https://www.kfu.kg/index.php/calendars'),
]
def collect(job):
 name,sid,url=job
 result=dict(name=name,url=url,attempted_utc=datetime.now(timezone.utc).isoformat(),independence='UNKNOWN',usage='MANUAL_RESEARCH_ONLY_NOT_CERTIFIED')
 try:
  if sid:
   result.update(fetch_source(sid,url,attempts=1,timeout=20))
  else:
   with urlopen(Request(url,headers={'User-Agent':'SportsResearch/2026.10 (source-custody research)'}),timeout=20) as response:
    raw=response.read(12000000); final=response.geturl()
   target=QUARANTINE/(name+'.body'); target.write_bytes(raw)
   result.update(body_path=target.relative_to(ROOT).as_posix(),response_sha256=hashlib.sha256(raw).hexdigest(),response_bytes=len(raw),retrieved_utc=datetime.now(timezone.utc).isoformat(),final_url=final,parser_id='MANUAL_BODY_FIELD_REVIEW_NOT_REGISTERED',registry_sha256=hashlib.sha256((ROOT/'research/sources_registry.json').read_bytes()).hexdigest(),market_quarantined=True)
  result['status']='FETCHED_BYTES_REQUIRE_FIELD_REVIEW'
 except Exception as exc: result.update(status='SOURCE_FAILURE',error=str(exc))
 return result
if __name__=='__main__':
 import sys
 if '--more' in sys.argv:
  JOBS=[
   ('euro_first',None,'https://feeds.incrowdsports.com/provider/euroleague-feeds/v2/competitions/E/seasons/E2026/games?page=7'),
   ('ahl_home',None,'https://griffinshockey.com/'),
   ('ahl_results',None,'https://griffinshockey.com/schedule/results'),
   ('wnba_recap',None,'https://www.wnba.com/watch/video/game-recap-las-vegas-aces-94-indiana-fever-83-10-1-2026?collection=game-recaps'),
   ('kbo_naver',None,'https://api-gw.sports.naver.com/schedule/games?fields=basic&upperCategoryId=kbaseball&categoryId=kbo&fromDate=2026-10-03&toDate=2026-10-03'),
   ('bbl_club',None,'https://fcbayern.com/basketball/de/news/2026-27/10/bayern-vs.-oldenburg'),
   ('soccer_espn',None,'https://site.api.espn.com/apis/site/v2/sports/soccer/fifa.friendly/scoreboard?dates=20261004'),
  ]
 with ThreadPoolExecutor(max_workers=5) as pool: results=list(pool.map(collect,JOBS))
 (OUT/('collection_receipts_more.json' if '--more' in sys.argv else 'collection_receipts.json')).write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print(json.dumps([{k:x.get(k) for k in ['name','status','response_bytes','error']} for x in results],indent=2))
