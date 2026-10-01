from pathlib import Path
import json,hashlib
from urllib.request import Request,urlopen
from urllib.parse import urlencode
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
A=Path(__file__).resolve().parent;ROOT=A.parents[2]
base={'leId':'1','srId':'0','seasonId':'2026','gameId':'20261001HHSS0'}
jobs={
 'api_games':('/ws/Main.asmx/GetKboGameList',{'leId':'1','srId':'0,1,3,4,5,6,7,8,9','date':'20261001'}),
 'api_lineup':('/ws/Schedule.asmx/GetLineUpAnalysis',base),
 'api_team':('/ws/Schedule.asmx/GetTeamRecord',{**base,'groupSc':'SEASON'}),
 'api_pitch':('/ws/Schedule.asmx/GetPitcherRecordAnalysis',{**base,'awayTeamId':'HH','homeTeamId':'SS','awayPitId':'54729','homePitId':'69446','groupSc':'SEASON'}),
 'api_previous_box':('/ws/Schedule.asmx/GetBoxScoreScroll',{**base,'gameId':'20260930HHSS0'})}
def fetch(item):
    label,(route,params)=item;url='https://www.koreabaseball.com'+route
    request=Request(url,data=urlencode(params).encode(),headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Referer':'https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx','User-Agent':'Mozilla/5.0','X-Requested-With':'XMLHttpRequest'})
    try:
        with urlopen(request,timeout=15) as r:raw=r.read(12000000);ctype=r.headers.get('Content-Type');final=r.geturl()
        stamp=datetime.now(timezone.utc).isoformat();digest=hashlib.sha256(raw).hexdigest()
        body=A/(label+'.body');body.write_bytes(raw)
        receipt={'source_url':url,'request_method':'POST','request_params':params,'retrieved_utc':stamp,'response_sha256':digest,'response_bytes':len(raw),'body_path':body.relative_to(ROOT).as_posix(),'content_type':ctype,'final_url':final,'independence_status':'UNKNOWN','upstream_lineage_id':'KBO_OWNER','parser_id':'KBO_NATIVE_JSON_MANUAL_READBACK_V1'}
        (A/(label+'_receipt.json')).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
        try:data=json.loads(raw);status='JSON'
        except Exception:data=raw[:120].decode(errors='replace');status='NON_JSON_SHELL_OR_ERROR'
        return label,{'status':status,'receipt':receipt,'data':data}
    except Exception as e:return label,{'status':'FAILED','source_url':url,'params':params,'reason':str(e)}
with ThreadPoolExecutor(max_workers=5) as pool:out=dict(pool.map(fetch,jobs.items()))
(A/'api_results.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
for k,v in out.items():print(k,v['status'],json.dumps(v.get('data'),ensure_ascii=False)[:2500])
