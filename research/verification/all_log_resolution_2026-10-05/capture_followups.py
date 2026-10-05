"""Retain exact-event followups discovered in owner pages and original reports."""
from pathlib import Path
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT))
from research.src.sources import fetch_source
JOBS=[('newsis_terminal','https://v.daum.net/v/20261001223101462',['P-524','P-526']),
 ('khan_terminal','https://v.daum.net/v/20261001230913192',['P-524']),
 ('nikkan_terminal','https://www.nikkansports.com/baseball/professional/score/2026/cl2026100102.html',['P-525']),
 ('championat_terminal','https://www.championat.com/football/news-6644730-kyrgyzstan-livan-rezultat-matcha-4-oktyabrya-2026-schet-3-1-tovarischeskij-match.html',['P-537']),
 ('sportkg_terminal','https://sport.kg/main_news/95100-sbornaja-kyrgyzstana-pobedila-livan-v-tovarischeskom-matche-no-voprosy-est.html',['P-537'])]
def main():
 reg=dict(schema_version=1,scope='EXACT_SPORTS_REPORTS_ONLY; independent upstream collection not inferred',sources={k:dict(publisher=u.split('/')[2],allowed_url_prefixes=[u],access_mode='AUTOMATED_ALLOWED',market_fields_possible=(k=='championat_terminal'),parser_id='MANUAL_EXACT_EVENT',upstream_lineage_id='REQUIRES_AUDIT',independence_status='UNKNOWN') for k,u,_ in JOBS})
 rp=OUT/'followup_route_registry.json'
 with rp.open('x',encoding='utf-8') as f:json.dump(reg,f,indent=2);f.write('\n')
 def get(job):
  k,u,ids=job
  try:return dict(key=k,canonical_ids=ids,status='RETAINED',receipt=fetch_source(k,u,registry_path=rp,timeout=15,attempts=1))
  except Exception as e:return dict(key=k,canonical_ids=ids,status='UNAVAILABLE',url=u,error=f'{type(e).__name__}: {e}')
 with ThreadPoolExecutor(max_workers=4) as p:rows=list(p.map(get,JOBS))
 api=[('kbo_ajax_games','/ws/Main.asmx/GetKboGameList',dict(leId='1',srId='0,1,3,4,5,6,7,8,9',date='20261001')),
  ('kbo_ajax_schedule','/ws/Schedule.asmx/GetScheduleList',dict(leId='1',srIdList='0,9,6',seasonId='2026',gameMonth='10',teamId='')),
  ('kbo_box_kt','/ws/Schedule.asmx/GetBoxScoreScroll',dict(leId='1',srId='0',seasonId='2026',gameId='20261001KTHT0')),
  ('kbo_box_hh','/ws/Schedule.asmx/GetBoxScoreScroll',dict(leId='1',srId='0',seasonId='2026',gameId='20261001HHSS0'))]
 def post(job):
  k,route,params=job;u='https://www.koreabaseball.com'+route
  try:
   req=Request(u,data=urlencode(params).encode(),headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Referer':'https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx','User-Agent':'Mozilla/5.0','X-Requested-With':'XMLHttpRequest'})
   with urlopen(req,timeout=20) as r:raw=r.read(12000001);ct=r.headers.get('Content-Type');final=r.geturl()
   if not raw or len(raw)>12000000:raise ValueError('Invalid body length')
   body=OUT/(k+'.body')
   with body.open('xb') as f:f.write(raw)
   receipt=dict(source_id=k,source_url=u,final_url=final,request_method='POST',request_params=params,retrieved_utc=datetime.now(timezone.utc).isoformat(),response_sha256=hashlib.sha256(raw).hexdigest(),response_bytes=len(raw),body_path=body.relative_to(ROOT).as_posix(),content_type=ct,independence_status='UNKNOWN')
   target=ROOT/'research/data/source_receipts'/(k+'_20261005.json')
   with target.open('x',encoding='utf-8') as f:json.dump(receipt,f,indent=2);f.write('\n')
   try:data=json.loads(raw);status='JSON_RETAINED'
   except ValueError:data=None;status='HTML_SHELL_OR_ERROR_RETAINED'
   return dict(key=k,status=status,receipt={**receipt,'receipt_path':target.relative_to(ROOT).as_posix()},data=data)
  except Exception as e:return dict(key=k,status='UNAVAILABLE',url=u,error=f'{type(e).__name__}: {e}')
 with ThreadPoolExecutor(max_workers=4) as p:rows+=list(p.map(post,api))
 with (OUT/'source_followups.json').open('x',encoding='utf-8') as f:json.dump(dict(results=rows),f,ensure_ascii=False,indent=2);f.write('\n')
 for r in rows:print(r['key'],r['status'],flush=True)
if __name__=='__main__':main()
