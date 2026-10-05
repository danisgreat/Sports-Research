"""Bounded read-only field-owner refreshes; every failure remains explicit."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import hashlib
import json
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from research.src.sources import fetch_source, verified_body
OUT=Path(__file__).parent
JOBS=[
 ('npb_final','https://npb.jp/scores/2026/1001/c-d-25/','P-525'),
 ('npb_schedule','https://npb.jp/games/2026/schedule.html','P-525'),
 ('carp_report','https://www.carp.co.jp/game/carp-digest/2026/1001','P-525'),
 ('kbo_schedule','https://www.koreabaseball.com/Schedule/Schedule.aspx?month=10&year=2026','P-524 P-526'),
 ('kbo_home','https://www.koreabaseball.com/','P-524 P-526'),
 ('kfu_owner','https://www.kfu.kg/','P-537'),
 ('kfu_news','https://www.kfu.kg/news','P-537'),
 ('fff_owner','https://www.fff.fr/','P-176 P-178 P-179'),
 ('cfa_owner','https://www.thecfa.cn/','P-233 P-234 P-235 P-250'),
 ('lega_owner','https://www.legaseriea.it/','P-251 P-399'),
 ('uae_owner','https://www.uaeproleague.ae/en/fixtures','P-368 P-369'),
 ('allsvenskan_owner','https://allsvenskan.se/matcher','P-401 P-419'),
 ('guatemala_owner','https://ligagt.com/','P-377'),
 ('bhutan_owner','https://bhutanfootball.org/','P-418'),
 ('slovak_owner','https://futbalsfz.sk/slovnaft-cup/','P-342'),
 ('lfp_event','https://plus.ligue1.com/live/306887','P-409'),
 ('uefa_inter','https://matchstats.uefa.com/v1/team-statistics/2049369','P-255'),
 ('uefa_psg','https://matchstats.uefa.com/v1/team-statistics/2049367','P-256'),
 ('afc_owner','https://www.the-afc.com/en/club/afc_champions_league_elite.html','P-430'),
 ('leaguescup_owner','https://www.leaguescup.com/','P-265'),
 ('toluca_report','https://www.tolucafc.com/noticias/estan-invictas','P-148'),
 ('dfl_event','https://www.bundesliga.com/en/bundesliga/matchday/2026-2027/3/rb-leipzig-vs-hamburger-sv/stats','P-410'),
 ('proleague_event','https://www.proleague.be/fr/matchs/saison-2026-2027-jupiler-pro-league-6-club-brugge-vs-royal-antwerp-fc-646','P-407'),
]
def sha(raw):return hashlib.sha256(raw).hexdigest()
def main():
 registry=dict(schema_version=1,scope='DATED_READ_ONLY_SETTLEMENT_OWNER_ROUTES; not live model admission',sources={})
 for key,url,ids in JOBS:
  registry['sources'][key]=dict(publisher=url.split('/')[2],allowed_url_prefixes=[url.split('?')[0]],
   access_mode='AUTOMATED_ALLOWED',market_fields_possible=False,parser_id='MANUAL_EVENT_FIELD_AUDIT',
   upstream_lineage_id='OWNER_COLLECTION_IDENTITY_REQUIRES_EVENT_AUDIT',independence_status='UNKNOWN')
 rp=OUT/'owner_route_registry.json'
 with rp.open('x',encoding='utf-8') as f:json.dump(registry,f,indent=2);f.write('\n')
 def get(job):
  key,url,ids=job
  try:
   receipt=fetch_source(key,url,registry_path=rp,timeout=15,attempts=1)
   raw=verified_body(receipt,ROOT)
   return dict(key=key,canonical_ids=ids.split(),status='BODY_RETAINED_TARGET_NOT_YET_VERIFIED',receipt=receipt)
  except Exception as e:return dict(key=key,canonical_ids=ids.split(),status='UNAVAILABLE',url=url,error=f'{type(e).__name__}: {e}')
 rows=[]
 with ThreadPoolExecutor(max_workers=4) as pool:
  for r in pool.map(get,JOBS):rows.append(r);print(r['key'],r['status'],flush=True)
 # Read-only POST native KBO scoreboard, same verified endpoint and parameters as original observation.
 url='https://www.koreabaseball.com/ws/Main.asmx/GetKboGameList'
 params=dict(leId='1',srId='0,1,3,4,5,6,7,8,9',date='20261001')
 try:
  with urlopen(Request(url,data=urlencode(params).encode(),headers={'User-Agent':'SportsResearch/2026.10','Content-Type':'application/x-www-form-urlencoded'}),timeout=20) as reply:
   raw=reply.read(12000001);ctype=reply.headers.get('Content-Type','');final=reply.geturl()
  if not raw or len(raw)>12000000:raise ValueError('Empty or excessive body')
  stamp=datetime.now(timezone.utc).isoformat(); body=OUT/'kbo_native_final.body'
  with body.open('xb') as f:f.write(raw)
  receipt=dict(source_id='kbo_native_final',source_url=url,final_url=final,request_method='POST',request_params=params,
   retrieved_utc=stamp,response_sha256=sha(raw),response_bytes=len(raw),body_path=body.relative_to(ROOT).as_posix(),
   content_type=ctype,independence_status='UNKNOWN',assessment='BYTES_ONLY; validate exact native game IDs and terminal state')
  rp2=ROOT/'research/data/source_receipts'/('kbo_native_final_'+stamp.replace(':','').replace('+','_')+'.json')
  with rp2.open('x',encoding='utf-8') as f:json.dump(receipt,f,indent=2);f.write('\n')
  rows.append(dict(key='kbo_native_final',canonical_ids=['P-524','P-526'],status='BODY_RETAINED_TARGET_NOT_YET_VERIFIED',receipt={**receipt,'receipt_path':rp2.relative_to(ROOT).as_posix()}))
 except Exception as e:rows.append(dict(key='kbo_native_final',canonical_ids=['P-524','P-526'],status='UNAVAILABLE',url=url,error=f'{type(e).__name__}: {e}'))
 with (OUT/'source_refresh.json').open('x',encoding='utf-8') as f:json.dump(dict(created_utc=datetime.now(timezone.utc).isoformat(),results=rows),f,indent=2);f.write('\n')
 print('retained',sum('receipt' in r for r in rows),'of',len(rows))
if __name__=='__main__':main()
