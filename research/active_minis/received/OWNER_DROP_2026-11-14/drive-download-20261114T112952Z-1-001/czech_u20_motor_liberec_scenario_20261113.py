#!/usr/bin/env python3
"""Read-only, market-blind, uncalibrated local research diagnostic.
NOT a repository/ml execution or issued forecast. Exact finite Poisson grid.
Inputs transcribed from dated official 2026-27 KB ELJ team table and October results.
Full-game 5-minute OT then SO represented by awarding exactly one scoreboard
point to one team if regulation is tied (winner proxy proportional to lambdas).
Empty-net events cannot be separated in available final-score history; no
fabricated empty-net coefficient is applied.
"""
import json, math, hashlib
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

out=Path('/mnt/data/czech_u20_motor_liberec_scenario_20261113.json')
league={'goals_for':910,'team_games':296,'mean_goals_per_team_game':910/296}
motor={'gp':19,'gf':69,'ga':45,'last5_gf':16,'last5_ga':10,
       'last5':[('2026-10-31','at Pardubice','2-3 SO'),('2026-10-30','at Mountfield HK','3-4'),('2026-10-23','vs Plzeň','5-1'),('2026-10-19','vs Slavia Praha','3-1'),('2026-10-17','at Litvínov','3-1')]}
lib={'gp':17,'gf':41,'ga':71,'last5_gf':14,'last5_ga':16,
     'last5':[('2026-10-31','vs Vítkovice','5-4 SO'),('2026-10-30','vs Třinec','1-5'),('2026-10-28','vs Poruba','3-2'),('2026-10-24','at Litvínov','4-3 OT'),('2026-10-23','at Karlovy Vary','1-2')]}
for d in (motor,lib):
    d['gf_pg']=d['gf']/d['gp'];d['ga_pg']=d['ga']/d['gp']
    d['last5_gf_pg']=d['last5_gf']/5;d['last5_ga_pg']=d['last5_ga']/5
    d['blended_gf_pg']=.75*d['gf_pg']+.25*d['last5_gf_pg'];d['blended_ga_pg']=.75*d['ga_pg']+.25*d['last5_ga_pg']
lambda_m=(motor['blended_gf_pg']+lib['blended_ga_pg'])/2
lambda_l=(lib['blended_gf_pg']+motor['blended_ga_pg'])/2
scenarios=[{'name':'constrained','weight':.25,'lambda_motor':3.2,'lambda_liberec':2.1},
           {'name':'base_additive_cross','weight':.5,'lambda_motor':lambda_m,'lambda_liberec':lambda_l},
           {'name':'open_play','weight':.25,'lambda_motor':4.1,'lambda_liberec':2.75}]
maxg=30
mix={}
rows=[]
for sc in scenarios:
    a,b,w=sc['lambda_motor'],sc['lambda_liberec'],sc['weight']
    pa=[math.exp(-a)*a**i/math.factorial(i) for i in range(maxg+1)]
    pb=[math.exp(-b)*b**i/math.factorial(i) for i in range(maxg+1)]
    grid={}
    for i in range(maxg+1):
        for j in range(maxg+1):
            mass=pa[i]*pb[j]
            if mass<1e-17:continue
            if i==j:
                q=a/(a+b)
                grid[(i+1,j)]=grid.get((i+1,j),0)+mass*q
                grid[(i,j+1)]=grid.get((i,j+1),0)+mass*(1-q)
            else:grid[(i,j)]=grid.get((i,j),0)+mass
    for key,val in grid.items():mix[key]=mix.get(key,0)+w*val
    p_over=sum(v for (i,j),v in grid.items() if i+j>=6)
    p_motorcover=sum(v for (i,j),v in grid.items() if i-j>=2)
    p_motorwin=sum(v for (i,j),v in grid.items() if i>j)
    p_drawreg=sum(pa[k]*pb[k] for k in range(maxg+1))
    rows.append({'name':sc['name'],'weight':w,'lambda_motor':a,'lambda_liberec':b,'reg_expected_total':a+b,'reg_expected_margin':a-b,'P_over_5_5':p_over,'P_under_5_5':1-p_over,'P_motor_minus_1_5':p_motorcover,'P_liberec_plus_1_5':1-p_motorcover,'P_motor_winner_proxy':p_motorwin,'P_regulation_draw':p_drawreg,'grid_mass':sum(grid.values())})
M=sum(i*v for (i,j),v in mix.items());L=sum(j*v for (i,j),v in mix.items())
T=M+L;D=M-L
VT=sum(v*((i+j)-T)**2 for (i,j),v in mix.items())
VD=sum(v*((i-j)-D)**2 for (i,j),v in mix.items())
p_over=sum(v for (i,j),v in mix.items() if i+j>=6)
p_cover=sum(v for (i,j),v in mix.items() if i-j>=2)
p_win=sum(v for (i,j),v in mix.items() if i>j)
joint_fail=sum(v for (i,j),v in mix.items() if (i+j<=5 and i-j>=2))
now=datetime.now(ZoneInfo('Australia/Melbourne')).isoformat(timespec='seconds')
result={'status':'UNCALIBRATED_ASSUMPTION_ONLY_NOT_PRIMARY_NOT_ISSUED','computed_at_melbourne':now,
        'source_urls':{'official_league_table':'https://www.czehockey.cz/souteze-juniori/komercni-banka-extraliga-junioru',
        'official_fixture':'https://czehockey.cz/game/detail/178203',
        'club_h2h':'https://hcmotor.cz/zapasy.asp?filtrTym=LIB&kde=vsechno&sezona=2026&stats=true',
        'motor_history':'https://www.eliteprospects.com/team/3143/hc-motor-ceske-budejovice-u20',
        'liberec_history':'https://www.eliteprospects.com/team/3993/bili-tygri-liberec-u20',
        'rules':'https://ceskyhokej.cz/competition/description/1'},
        'league':league,'motor':motor,'liberec':lib,'raw_additive_cross_base':[lambda_m,lambda_l],
        'scenarios':rows,'mixture':{'P_over_5_5':p_over,'P_under_5_5':1-p_over,
        'P_motor_minus_1_5':p_cover,'P_liberec_plus_1_5':1-p_cover,'P_motor_win_proxy':p_win,
        'E_motor_score_proxy':M,'E_liberec_score_proxy':L,'E_total_proxy':T,'E_margin_proxy':D,
        'SD_total_proxy':math.sqrt(VT),'SD_margin_proxy':math.sqrt(VD),'joint_failure_over_and_L_plus':joint_fail,
        'P_both_decisive':1.,'grid_mass':sum(mix.values())},
        'notes':['30 goals per team finite grid with tail mass displayed, independent Poisson before OT','regulation tie split proportional to assumed means and adds exactly one scoreboard goal for OT/SO winner','empty-net effects not separately identifiable; no fabricated correction','supplied half-goal totals and handicap invariant to one-goal tie-break in OT/SO','uncertain starting goalies, U20 roster, L10-L20 per-game history and operator settlement convention','scenario weights 0.25/0.50/0.25 declared before calculation']}
canonical=json.dumps(result,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()
result['sha256_payload_without_hash']=hashlib.sha256(canonical).hexdigest()
out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'time':now,'scenario_summary':[{k:v for k,v in r.items() if k.startswith('P_') or k=='name'} for r in rows], 'mixture':result['mixture'],'output':str(out)},indent=2))
