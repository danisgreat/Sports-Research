#!/usr/bin/env python3
"""Transparent sports-only, not-calibrated WNBL score scenario. No market data or repository model run."""
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from hashlib import sha256
from pathlib import Path
import json
import numpy as np

SEED=20261113
N=600000
SEASON={
 'Geelong':[("2026-10-15","Tasmania Jewels","A",90,103),("2026-10-24","Southside Melbourne Flyers","H",74,69),("2026-10-31","UC Capitals","H",68,77),("2026-11-02","Bendigo Spirit","A",77,70),("2026-11-05","Townsville Fire","H",67,80)],
 'Perth':[("2026-10-17","Townsville Fire","H",86,83),("2026-10-24","Adelaide Lightning","A",90,82),("2026-11-03","Townsville Fire","A",86,99),("2026-11-10","Bendigo Spirit","H",94,84)]
}
# Predeclared sensitivity mixture. The base case is a 65/35 season/opponent average and venue-split blend.
# P(G) = .65*[Geelong PF+Perth PA]/2 + .35*[Geelong home PF + Perth away PA]/2
# P(P) = .65*[Perth PF+Geelong PA]/2 + .35*[Perth away PF + Geelong home PA]/2
GseasonPF=75.2; GseasonPA=79.8; PseasonPF=89.0; PseasonPA=87.0
GhomePF=(74+68+67)/3; GhomePA=(69+77+80)/3
PawayPF=(90+86)/2; PawayPA=(82+99)/2
Gbase=.65*(GseasonPF+PseasonPA)/2+.35*(GhomePF+PawayPA)/2
Pbase=.65*(PseasonPF+GseasonPA)/2+.35*(PawayPF+GhomePA)/2
SCENARIOS=[('low',0.25,75.5,83.0),('base',0.50,Gbase,Pbase),('high',0.25,84.0,87.0)]
TOTAL_SD=20.0
MARGIN_SD=16.5
rng=np.random.default_rng(SEED)
results={}
counts_all={'geelong_plus_6_5':0,'perth_minus_6_5':0,'over_163_5':0,'under_163_5':0,'geelong_winner':0,'perth_winner':0,'joint_Gplus_Under_fail':0}
allG=[];allP=[];allregT=[];allRegM=[];allOT=[]
for label,w,mG,mP in SCENARIOS:
 n=int(N*w)
 # One bivariate latent score object from independent total and signed margin factors;
 # a derived positive team-score covariance follows when SD(total)>SD(margin).
 total=rng.normal(mG+mP,TOTAL_SD,n)
 margin=rng.normal(mG-mP,MARGIN_SD,n)
 G=np.rint(np.maximum(0,(total+margin)/2)).astype('int16')
 P=np.rint(np.maximum(0,(total-margin)/2)).astype('int16')
 regT=G+P;regM=G-P
 tied=G==P
 ot_periods=np.zeros(n,dtype='int8')
 # 5-minute overtime periods; independent Poisson 9.5 pts/team is transparent
 # scenario assumption (not verified WNBL OT scoring or player rotation).
 for _ in range(8):
  idx=np.where(tied)[0]
  if not idx.size: break
  G[idx]+=rng.poisson(9.5,len(idx)).astype('int16')
  P[idx]+=rng.poisson(9.5,len(idx)).astype('int16')
  ot_periods[idx]+=1
  tied[idx]=G[idx]==P[idx]
 # Failsafe after eight 5-minute OTs: a single random winning point, never a draw.
 idx=np.where(tied)[0]
 if len(idx):
  geelong_wins=rng.integers(0,2,len(idx)).astype('int16')
  G[idx]+=geelong_wins
  P[idx]+=(1-geelong_wins)
 finalT=G+P; finalM=G-P
 indicators={
 'geelong_plus_6_5':finalM>=-6,
 'perth_minus_6_5':finalM<=-7,
 'over_163_5':finalT>=164,
 'under_163_5':finalT<=163,
 'geelong_winner':finalM>0,
 'perth_winner':finalM<0,
 'joint_Gplus_Under_fail':(finalM<=-7)&(finalT>=164)}
 vals={k:float(np.mean(v)) for k,v in indicators.items()}
 for k,v in indicators.items():counts_all[k]+=int(v.sum())
 results[label]={ 'weight':w,'n':n,'regulation_mean_G_assumed':mG,'regulation_mean_P_assumed':mP,
 'proportions':vals,'observed_mean_G':float(G.mean()),'observed_mean_P':float(P.mean()),
 'observed_total_mean':float(finalT.mean()),'observed_margin_G_minus_P':float(finalM.mean()),
 'overtime_rate':float(np.mean(ot_periods>0)), 'mean_OT_periods':float(ot_periods.mean())}
 allG.append(G);allP.append(P);allregT.append(regT);allRegM.append(regM);allOT.append(ot_periods)

G=np.concatenate(allG); P=np.concatenate(allP);regT=np.concatenate(allregT);regM=np.concatenate(allRegM);OT=np.concatenate(allOT)
vals={k:v/N for k,v in counts_all.items()}
assert abs(vals['geelong_plus_6_5']+vals['perth_minus_6_5']-1)<1e-12
assert abs(vals['over_163_5']+vals['under_163_5']-1)<1e-12
out={
 'disposition':'UNCALIBRATED_SCENARIO_ONLY_NOT_PRIMARY','run_time':datetime.now(ZoneInfo('Australia/Melbourne')).isoformat(timespec='seconds'),
 'seed':SEED,'n':N,'competition':'Australia WNBL 2026-27','fixture':'Geelong Venom vs Perth Lynx',
 'scheduled_start_AEDT':'2026-11-13T19:00:00+11:00',
 'source_sporting_records':SEASON,
 'season_means':{'G_PF':GseasonPF,'G_PA':GseasonPA,'P_PF':PseasonPF,'P_PA':PseasonPA},
 'venue_means':{'G_home_PF':GhomePF,'G_home_PA':GhomePA,'P_away_PF':PawayPF,'P_away_PA':PawayPA},
 'base_regulation_mean_formula':'0.65*season matchup and 0.35*home-away matchup, both equally opponent-adjusted',
 'base_regulation_means':{'Geelong':Gbase,'Perth':Pbase},
 'assumptions':{'scenario_weights':[0.25,0.5,0.25],'total_sd':TOTAL_SD,'margin_sd':MARGIN_SD,
 'total_margin_latent_correlation':0,'team_score_correlation_implied':(TOTAL_SD**2-MARGIN_SD**2)/(TOTAL_SD**2+MARGIN_SD**2),
 'score_rounding':'nearest integer each team','OT_trigger':'equal regulation scores', 'OT_points_team':'Poisson mean 9.5 for each team in each 5-minute OT until untied',
 'form_gap':'Current WNBL possession/efficiency inputs, stable minute usage and starting fives unavailable; using team PF/PA proxies with widened SD; no fitted model'},
 'scenarios':results,
 'mixture_probabilities':vals,
 'moment_estimates':{'Geelong_points_mean':float(G.mean()),'Perth_points_mean':float(P.mean()),'Geelong_points_sd':float(G.std()),'Perth_points_sd':float(P.std()),'total_mean':float((G+P).mean()),'total_sd':float((G+P).std()),'margin_GminusP_mean':float((G-P).mean()),'margin_sd':float((G-P).std()),'overtime_probability':float(np.mean(OT>0)),'regulation_tie_prob':float(np.mean(regM==0))},
 'sampling_SE_upper_bound':0.5/np.sqrt(N),
 'no_market_data':True, 'no_repository_model':True
}
path=Path('/mnt/data/wnbl_geelong_perth_scenario_20261113.json');path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'base_regulation_means':out['base_regulation_means'],'mixture_probabilities':vals,'moment_estimates':out['moment_estimates'],'scenario_range':{k:[results[s]['proportions'][k] for s in ['low','base','high']] for k in vals},'SE_max':out['sampling_SE_upper_bound']},indent=2))
