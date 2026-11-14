"""Reproducible, uncalibrated Kazakhstan hockey scenario arithmetic.
This is NOT the GitHub repository's ml/reference, certified model or issued forecast.
Sports inputs: official pro.ligasy.kz pre-event team schedules and standings.
No betting prices, tips or market inputs are used.
"""
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from math import exp, factorial, fsum
import json, hashlib
from pathlib import Path
import numpy as np

# Chronological played matches. Scored totals are provider FINAL score including an
# overtime or shootout winner where flagged. No retrospective 60m reconstruction.
# (YYYY-MM-DD, opponent, home/away, GF, GA, endpoint)
TOR=[
('2026-09-02','Almaty','H',9,0,'REG'),('2026-09-03','Almaty','H',3,2,'REG'),
('2026-09-06','Arlan','A',2,3,'REG'),('2026-09-07','Arlan','A',4,3,'OT'),
('2026-09-10','Saryarqa','A',0,2,'REG'),('2026-09-11','Saryarqa','A',3,2,'SO'),
('2026-09-16','Qulager','H',3,2,'OT'),('2026-09-17','Qulager','H',6,3,'REG'),
('2026-09-20','Gornyak','H',4,3,'REG'),('2026-09-21','Gornyak','H',1,2,'REG'),
('2026-09-27','Aqtobe','A',9,1,'REG'),('2026-09-28','Aqtobe','A',6,2,'REG'),
('2026-10-01','Beibarys','A',4,3,'REG'),('2026-10-02','Beibarys','A',9,2,'REG'),
('2026-10-06','Nomad','H',2,3,'OT'),('2026-10-07','Nomad','H',2,3,'SO'),
('2026-10-11','Ertis','H',13,0,'REG'),('2026-10-12','Ertis','H',8,0,'REG'),
('2026-10-15','Ertis','A',9,2,'REG'),('2026-10-16','Ertis','A',12,1,'REG'),
('2026-10-19','Almaty','A',9,1,'REG'),('2026-10-20','Almaty','A',4,0,'REG'),
('2026-10-25','Aqtobe','H',4,2,'REG'),('2026-10-26','Aqtobe','H',3,1,'REG'),
('2026-10-29','Nomad','H',6,3,'REG'),('2026-10-30','Nomad','H',3,0,'REG')]
ARL=[
('2026-09-02','Gornyak','H',3,1,'REG'),('2026-09-03','Gornyak','H',1,3,'REG'),
('2026-09-06','Torpedo','H',3,2,'REG'),('2026-09-07','Torpedo','H',3,4,'OT'),
('2026-09-11','Aqtobe','A',5,2,'REG'),('2026-09-12','Aqtobe','A',5,4,'REG'),
('2026-09-15','Beibarys','A',3,1,'REG'),('2026-09-16','Beibarys','A',1,0,'REG'),
('2026-09-22','Saryarqa','A',5,0,'TECHNICAL_FORFEIT_EXCLUDE'),
('2026-09-23','Saryarqa','A',2,5,'REG'),
('2026-09-27','Ertis','H',11,2,'REG'),('2026-09-28','Ertis','H',5,3,'REG'),
('2026-10-02','Almaty','H',1,2,'REG'),('2026-10-03','Almaty','H',3,2,'REG'),
('2026-10-06','Qulager','A',4,3,'REG'),('2026-10-07','Qulager','A',4,3,'REG'),
('2026-10-10','Nomad','H',3,2,'OT'),('2026-10-11','Nomad','H',2,4,'REG'),
('2026-10-14','Saryarqa','H',1,4,'REG'),('2026-10-15','Saryarqa','H',4,3,'SO'),
('2026-10-20','Ertis','H',5,1,'REG'),('2026-10-21','Ertis','H',9,2,'REG'),
('2026-10-25','Almaty','H',3,0,'REG'),('2026-10-26','Almaty','H',4,3,'REG'),
('2026-10-29','Gornyak','A',3,2,'REG'),('2026-10-30','Gornyak','A',4,0,'REG')]

SEASON={'Torpedo': {'played_or_official_G':26,'official_GF':138,'official_GA':46},
        'Arlan': {'played_or_official_G':26,'official_GF':92,'official_GA':58}}
LEAGUE_GF=[138,92,102,108,90,87,66,69,48,31]
LEAGUE_GA=[46,58,61,55,68,62,92,117,85,187]
LEAGUE_G=[26,26,25,26,26,24,26,26,25,24]
assert sum(LEAGUE_GF)==sum(LEAGUE_GA)==831
assert (sum(x[3] for x in TOR),sum(x[4] for x in TOR))==(138,46)
assert (sum(x[3] for x in ARL if x[-1]!='TECHNICAL_FORFEIT_EXCLUDE'),sum(x[4] for x in ARL if x[-1]!='TECHNICAL_FORFEIT_EXCLUDE'))==(92,58)

# Latest 5/10/15/20 PLAYED, rather than taking the technical score as a played fixture.
def windows(rows):
    valid=[r for r in rows if r[-1]!='TECHNICAL_FORFEIT_EXCLUDE']
    out={}
    for n in (5,10,15,20):
      items=valid[-n:]
      out[f'L{n}']={'n':len(items),'GF':sum(x[3] for x in items),'GA':sum(x[4] for x in items),
        'GFpg':sum(x[3] for x in items)/len(items),'GApg':sum(x[4] for x in items)/len(items),
        'from':items[0][0], 'through':items[-1][0], 'items':items}
    return out
form={'Torpedo':windows(TOR),'Arlan':windows(ARL)}

# Scenario centres chosen by analyst judgement, not fitted to a formal reference.
# Values shrink blowout-distorted season and L10 vs stronger recent opponent profile.
# Reflect elite defensive rates and H2H, but no goalie-confirmation adjustment.
SCENARIOS=[{'id':'LOW','home_lambda':3.20,'away_lambda':1.75,'weight':0.25},
           {'id':'BASE','home_lambda':3.60,'away_lambda':2.00,'weight':0.50},
           {'id':'HIGH','home_lambda':4.10,'away_lambda':2.35,'weight':0.25}]
assert sum(s['weight'] for s in SCENARIOS)==1

# Exact full finite grid with 0..39 goals (tiny Poisson mass beyond 39).
G=40; i=np.arange(G);H=i[:,None]; A=i[None,:]
def pois_pmf(k,lmb):return np.array([exp(-lmb)*lmb**int(z)/factorial(int(z)) for z in k])

def evaluate(lh,la):
    mat=np.outer(pois_pmf(i,lh),pois_pmf(i,la)); mat/=mat.sum()
    reg_t=H+A; d=H-A
    # Explicit hypothetical full-game settlement: every tied regulation score
    # gains exactly one OT/SO goal to whichever team wins; no empty-net adjustment.
    # This is a sensitivity case, NOT verified league/operator settlement.
    full_t=reg_t+(d==0)
    metrics={
      'Torpedo_-1.5_reg':float(mat[d>=2].sum()),
      'Arlan_+1.5_reg':float(mat[d<=1].sum()),
      'Under_6.5_reg':float(mat[reg_t<=6].sum()),
      'Over_6.5_reg':float(mat[reg_t>=7].sum()),
      'Under_6.5_ot_goal_scenario':float(mat[full_t<=6].sum()),
      'Over_6.5_ot_goal_scenario':float(mat[full_t>=7].sum()),
      'Regulation_Torpedo_win':float(mat[d>0].sum()),
      'Regulation_Arlan_win':float(mat[d<0].sum()),
      'Regulation_draw':float(mat[d==0].sum()),
      'Total_goals_60m_mean':float(((reg_t)*mat).sum()),
      'Torpedo_goals_mean':float(((H)*mat).sum()),
      'Arlan_goals_mean':float(((A)*mat).sum()),
      'Torpedo_margin_mean':float((d*mat).sum()),
      'Total_goals_60m_sd':float(np.sqrt((((reg_t)-lh-la)**2*mat).sum())),
      'Torpedo_margin_sd':float(np.sqrt(((d-lh+la)**2*mat).sum())),
      'Joint_failure_Under6.5_and_Torpedo_-1.5_reg':float(mat[(reg_t>=7)&(d<=1)].sum()),
      'Joint_failure_Under6.5_and_Torpedo_-1.5_ot_scenario':float(mat[(full_t>=7)&(d<=1)].sum()),
      'Both_win_Under6.5_and_Torpedo_-1.5_ot_scenario':float(mat[(full_t<=6)&(d>=2)].sum()),
      'Reg_3_3':float(mat[3,3]),
    }
    return metrics
for s in SCENARIOS:s['metrics']=evaluate(s['home_lambda'],s['away_lambda'])
mixture={k:sum(s['weight']*s['metrics'][k] for s in SCENARIOS) for k in SCENARIOS[0]['metrics']}
assert abs(mixture['Torpedo_-1.5_reg']+mixture['Arlan_+1.5_reg']-1)<1e-12
assert abs(mixture['Under_6.5_reg']+mixture['Over_6.5_reg']-1)<1e-12
assert abs(mixture['Under_6.5_ot_goal_scenario']+mixture['Over_6.5_ot_goal_scenario']-1)<1e-12
assert abs(mixture['Regulation_Torpedo_win']+mixture['Regulation_Arlan_win']+mixture['Regulation_draw']-1)<1e-12
league_per_team=sum(LEAGUE_GF)/sum(LEAGUE_G)
league_anchor=evaluate(league_per_team,league_per_team)

output={
 'event':'Pro Hokei Ligasy 2026/27 fixture #131 / game 2715 / 2026-11-12 Torpedo vs Arlan',
 'authority':'CHAT_LOCAL_DRAFT_NOT_ISSUED', 'method':'EXACT_FINITE_POISSON_60M_SCENARIO_MIX_NOT_PRIMARY',
 'sporting_inputs':'Official league schedule/team pages and 26-game standings as of 2026-10-30; technical forfeit excluded from Arlan form windows',
 'official_reference_status':'NOT_RUN_INPUT_UNAVAILABLE; no registered league model / calibrated reference / matchup goalie sheet',
 'settlement':'NOT_PERFORMED', 'market_inputs':'NONE', 'cutoff':'2026-11-12T18:30:00+05:00',
 'model_caveats':['not a fitted model','no goalie verification','independent Poisson ignores correlated scores/goal-differential and empty-net tails',
    'OT one-goal-on-regulation-draw is an illustrative sensitivity case, not a verified operator endpoint',
    'no claim of actual pre-event model issuance or certified likelihood'],
 'official_season':SEASON, 'form':form, 'scenario_inputs_and_outputs':SCENARIOS,'mixture':mixture,
 'league_only_anchor':{'goals_per_team_per_game':league_per_team,'reg_6.5_under':league_anchor['Under_6.5_reg'],
    'reg_6.5_over':league_anchor['Over_6.5_reg'], 'not_validated_same_line_baseline':True},
 'source_urls':['https://pro.ligasy.kz/ru/schedule','https://pro.ligasy.kz/ru/standings?date=&id_stage=&order=3&order_direction=2',
    'https://pro.ligasy.kz/ru/game/2715-tor-arl', 'https://pro.ligasy.kz/ru/team/12-torpedo/schedule/16-pro-hokei-ligasy-2026-2027?id_tab=articles&id_team=12&start=100',
    'https://pro.ligasy.kz/ru/team/2-arlan','https://pro.ligasy.kz/ru/documents']
 }
p=Path('/mnt/data/hockey_scenario_20261113.json');p.write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('scenario json',p,'sha256',hashlib.sha256(p.read_bytes()).hexdigest())
print('forms', {t:{k:{m:v[m] for m in ('n','GF','GA','GFpg','GApg')} for k,v in d.items()} for t,d in form.items()})
print('metrics',mixture)
