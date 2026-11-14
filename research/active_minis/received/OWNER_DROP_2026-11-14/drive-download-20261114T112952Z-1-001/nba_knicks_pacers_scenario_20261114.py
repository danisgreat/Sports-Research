"""Chat-local uncalibrated NBA Cup match scenario, built from 2026-11-11 prior games.
No market odds used. Not the repository's calibrated model or frozen reference.
Competition: NBA, 48m + 5m OT; joint normal latent total/margin rounded to legal scores.
Seeded scenario Monte Carlo with explicit OT on regulatory ties.
"""
import numpy as np, json, math
from pathlib import Path
SEED=2026111401
N=600000
rng=np.random.default_rng(SEED)
# Source: BRef 2026-27 per-game logs, all matches before Nov 13 ET.
nyk=[('2026-10-20','PHI','H',100,106),('2026-10-23','BOS','A',103,107),('2026-10-25','ORL','H',102,111),('2026-10-27','DET','H',111,97),('2026-10-28','CHI','A',133,127),('2026-10-30','PHI','A',93,98),('2026-11-02','BKN','H',103,90),('2026-11-04','CHI','H',135,105),('2026-11-07','CLE','A',109,97),('2026-11-10','MIL','H',117,85),('2026-11-11','CLE','H',107,115)]
ind=[('2026-10-21','NOP','A',123,120),('2026-10-23','DAL','H',105,121),('2026-10-25','BKN','A',136,109),('2026-10-26','MIL','A',102,110),('2026-10-28','PHI','H',109,114),('2026-10-30','MIA','A',125,145),('2026-11-01','BKN','H',90,98),('2026-11-02','ATL','H',104,108),('2026-11-04','MEM','A',107,103),('2026-11-07','DEN','H',102,114),('2026-11-09','DAL','A',122,125),('2026-11-11','WAS','H',114,101)]
# Width floor: repo PARAMETERS.md NBA residual total SD18.7 margin SD14.05;
# multipliers 1.10 for current season uncertainty/lineup ambiguity (analyst assumption).
SD_TOTAL=18.7*1.10
SD_MARGIN=14.05*1.10
RHO=0.10
# Scenario centres fixed ex ante, combining opponent-adjusted per-100 ratings,
# low Knicks pace / high Indiana pace, a shrinkage toward season net differentials,
# and neutral-site-to-home correction. Not directly calibrated.
cases=[('slow',0.25,211.5,3.5),('base',0.50,219.0,5.5),('fast',0.25,228.0,7.5)]
all_nyk=[]; all_ind=[]; summary=[]
for label,w,mu_t,mu_m in cases:
 n=round(N*w)
 z1=rng.standard_normal(n); z2=rng.standard_normal(n)
 total=mu_t+SD_TOTAL*z1
 margin=mu_m+SD_MARGIN*(RHO*z1+np.sqrt(1-RHO**2)*z2)
 a=np.maximum(0,np.rint((total+margin)/2)).astype('int32')
 b=np.maximum(0,np.rint((total-margin)/2)).astype('int32')
 tie=np.flatnonzero(a==b)
 # A 5m overtime adds points for both sides. Repeat tied OT until decisive.
 active=tie.copy(); period=0
 while len(active) and period<10:
  period+=1
  aa=rng.poisson(11.8,size=len(active))
  bb=rng.poisson(11.8,size=len(active))
  a[active]+=aa; b[active]+=bb
  active=active[a[active]==b[active]]
 if len(active): a[active]+=1 # numerical termination safeguard, none expected.
 m=a-b; t=a+b
 summary.append(dict(name=label,weight=w,n=n,regulation_center_total=mu_t,regulation_center_margin=mu_m,actual_mean_total=round(float(t.mean()),3),actual_mean_margin=round(float(m.mean()),3),knicks_cover=round(float(np.mean(m>=8)),6),pacers_cover=round(float(np.mean(m<=7)),6),over=round(float(np.mean(t>=220)),6),under=round(float(np.mean(t<=219)),6),knicks_winner=round(float(np.mean(m>0)),6),ties_in_regulation=round(float(len(tie)/n),6)))
 all_nyk.append(a); all_ind.append(b)
a=np.concatenate(all_nyk);b=np.concatenate(all_ind);m=a-b;t=a+b
assert len(t)==N and not np.any(m==0)
def form(rows,n):
 sub=rows[-min(len(rows),n):]
 return dict(n=len(sub),wins=sum(a>b for _,_,_,a,b in sub),points_for=round(sum(r[3] for r in sub)/len(sub),3),points_against=round(sum(r[4] for r in sub)/len(sub),3),game_total=round(sum(r[3]+r[4] for r in sub)/len(sub),3))
result=dict(seed=SEED,n=N,method='3-scenario jointly correlated latent total-margin normal, integer-score + regulation tie NBA overtime by Poisson 11.8 points per side per 5m; UNCALIBRATED scenario diagnostic',endpoint='FULL_GAME_INCL_OT',population_width={'total_sd':SD_TOTAL,'margin_sd':SD_MARGIN,'rho':RHO},scenario_inputs=[{'name':k,'weight':w,'reg_total_mean':mt,'reg_knicks_margin_mean':mm} for k,w,mt,mm in cases],cases=summary,mean_knicks=round(float(a.mean()),3),mean_indiana=round(float(b.mean()),3),mean_total=round(float(t.mean()),3),mean_margin_nyk=round(float(m.mean()),3),sd_total=round(float(t.std()),3),sd_margin=round(float(m.std()),3),p={'Knicks -7.5':round(float(np.mean(m>=8)),6),'Pacers +7.5':round(float(np.mean(m<=7)),6),'Over 219.5':round(float(np.mean(t>=220)),6),'Under 219.5':round(float(np.mean(t<=219)),6),'Knicks winner':round(float(np.mean(m>0)),6),'Pacers winner':round(float(np.mean(m<0)),6)},joint_loss_pacers_and_under=round(float(np.mean((m>=8)&(t>=220))),6),joint_loss_pacers_and_over=round(float(np.mean((m>=8)&(t<=219))),6),form={'Knicks':{f'L{i}':form(nyk,i) for i in [5,10,15,20]},'Pacers':{f'L{i}':form(ind,i) for i in [5,10,15,20]}},prior_games={'Knicks':nyk,'Pacers':ind},source_urls={'Knicks':'https://www.basketball-reference.com/teams/NYK/2027.html','Pacers':'https://www.basketball-reference.com/teams/IND/2027.html'},notes=['No formal repo reference/ML release, calibration, or historical skill validation','Nesmith questionable; McConnell probable; starting fives unconfirmed','Cup game; FIBA early group stage irrelevant; NBA 48-minute basketball','No odds, prices, betting picks, or current-game outcomes were simulation inputs','Scheduled 2026-11-14T11:10:00+11:00; actual first tip unknown; commit/push not made'])
out='/mnt/data/nba_knicks_pacers_scenario_20261114.json'
Path(out).write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:result[k] for k in ['p','mean_knicks','mean_indiana','mean_total','mean_margin_nyk','joint_loss_pacers_and_under','form','cases']},indent=2))
