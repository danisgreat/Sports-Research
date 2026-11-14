"""Chat-local uncalibrated exploratory NBA Cup score simulation (not repo ml.run)."""
from math import erf, sqrt
import json
import numpy as np
from datetime import datetime
from zoneinfo import ZoneInfo
SEED=20261114011; N=200000
rng=np.random.default_rng(SEED)
# Published 2026-27 pregame Basketball-Reference per-team figures: games NYK11 IND12
ny={'ortg':116.2,'drtg':109.0,'pace':94.9,'scored':110.3,'allowed':103.5}
ind={'ortg':111.4,'drtg':113.8,'pace':100.2,'scored':111.6,'allowed':114.0}
pace=2/(1/ny['pace']+1/ind['pace'])
# Opponent-strength SHRUNK heuristic, mean of own OffRtg and opposition DefRtg
raw_away=pace*(ny['ortg']+ind['drtg'])/200
raw_home=pace*(ind['ortg']+ny['drtg'])/200
# Assumed 2 point home shift in margin, allocated half to each score
mu_away=raw_away-1.;mu_home=raw_home+1.
# NON-COMPETITION-FITTED widths: NBA 2026 repository development minimum 18.7 total,14.05 margin
st=18.7; sm=14.05
rng_total=rng.standard_normal(N)
rng_margin=rng.standard_normal(N)
# Continuous total & margin, then implied half points (no rounding; approximation)
# No fractional pushes on integer-score basketball at half-point lines
T=mu_away+mu_home+st*rng_total
M=mu_away-mu_home+sm*rng_margin
# illustrative overtime branch to make endpoint explicit; 0.045 assumed; not learned
# Shift final total equally in OT by an independent positive total.
OT=(rng.random(N)<0.046)
OTextra=rng.gamma(shape=12,scale=1.0,size=N)*OT
T=T+OTextra
# OT margin flips possible (OT scoring approx independent symmetric)
M=M+(rng.normal(0,4.0,size=N)*OT)
NY=(T+M)/2; IN=(T-M)/2
# Completed game: no actual game tie, rare tie from continuous model zero
central={'nyk':float(NY.mean()),'ind':float(IN.mean()),'total':float(T.mean()),'nyk_margin':float(M.mean()),'reg_total':float(mu_away+mu_home),'reg_margin':float(mu_away-mu_home),'ot_rate_assumed':0.046,
         'p_ind_plus7_5':float(np.mean(M<7.5)), 'p_nyk_minus7_5':float(np.mean(M>7.5)), 'p_under219_5':float(np.mean(T<219.5)), 'p_over219_5':float(np.mean(T>219.5)), 'p_nyk_win':float(np.mean(M>0))}
# paired hypothetical assumptions moved before reviewing return
sens=[]
for tag,pm,pt in [('base',0,0),('Nesmith-out margin +2 NYK',2,0),('Knicks offense stronger margin +4 NYK',4,0),('Indiana slows tempo total -6',0,-6),('pace lifts total +6',0,6),('cross-raw net gap +4 NYK, total +2',4,2),('Pacers efficient margin -3 NYK',-3,0)]:
    mm=M+pm;tt=T+pt
    sens.append({'scenario':tag,'p_ind_plus7_5':round(float(np.mean(mm<7.5)),4),'p_nyk_minus7_5':round(float(np.mean(mm>7.5)),4),'p_under219_5':round(float(np.mean(tt<219.5)),4),'p_over219_5':round(float(np.mean(tt>219.5)),4)})
res={'seed':SEED,'N':N,'source_year':2026,'inputs':{'nyk':ny,'ind':ind,'pace_harmonic':pace,'raw_away':raw_away,'raw_home':raw_home,'mu_reg_away':mu_away,'mu_reg_home':mu_home,'total_sd':st,'margin_sd':sm},'central':central,'sensitivity':sens,'method':'Independent normal marginal total/margin shocks with 4.6%-probability illustrative 12pt OT; correlation captured by score-transform; uncalibrated; no repo issuance.','notes':['Evidence known at report date; event first possession state must be checked before declaring pre-start','No actual opponent adjusted regression or fitted WNBA/NBA reference run']}
path='/mnt/data/nba_nyk_ind_20261114_results.json'
with open(path,'w') as f:json.dump(res,f,indent=2)
print(json.dumps(res,indent=2))
