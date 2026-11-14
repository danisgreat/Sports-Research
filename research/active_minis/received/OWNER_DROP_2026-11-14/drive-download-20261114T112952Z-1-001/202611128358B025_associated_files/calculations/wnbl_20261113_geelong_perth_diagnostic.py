"""Transparent exploratory WNBL conditional score model, NOT a frozen repository forecast.
Matches manually transcribed from official WNBL schedule result listings, 15 Oct--12 Nov 2026.
No bookmaker prices, odds or post-start facts used. Synthetic parameters are assumptions.
"""
import math, statistics, numpy as np
from scipy.stats import norm
from datetime import datetime
# all rows sorted by date; home, away, home_points, away_points
rows=[
('2026-10-15','Tasmania','Geelong',103,90),
('2026-10-16','Southside','Sydney',73,77),
('2026-10-17','Canberra','Bendigo',94,92),
('2026-10-17','Perth','Townsville',86,83),
('2026-10-18','Sydney','Adelaide',95,68),
('2026-10-20','Adelaide','Townsville',68,86),
('2026-10-22','Southside','Tasmania',91,77),
('2026-10-23','Sydney','Canberra',82,70),
('2026-10-24','Geelong','Southside',74,69),
('2026-10-24','Adelaide','Perth',82,90),
('2026-10-25','Townsville','Sydney',77,90),
('2026-10-27','Bendigo','Townsville',68,91),
('2026-10-31','Tasmania','Sydney',93,85),
('2026-10-31','Geelong','Canberra',68,77),
('2026-11-01','Southside','Adelaide',74,81),
('2026-11-02','Bendigo','Geelong',70,77),
('2026-11-03','Townsville','Perth',99,86),
('2026-11-05','Geelong','Townsville',67,80),
('2026-11-07','Adelaide','Tasmania',100,68),
('2026-11-07','Bendigo','Canberra',83,97),
('2026-11-08','Sydney','Southside',86,69),
('2026-11-10','Perth','Bendigo',94,84),
('2026-11-12','Tasmania','Southside',99,79),
]
assert len(rows)==23
summaries={}
for team in ('Geelong','Perth'):
    xs=[]
    for date,h,a,p,q in rows:
        if team==h: xs.append((date,'H',p,q))
        elif team==a:xs.append((date,'A',q,p))
    summaries[team]=xs
    print(team,'n',len(xs),'games',xs,'PF',statistics.mean(x[2] for x in xs),'PA',statistics.mean(x[3] for x in xs),'totals',[x[2]+x[3] for x in xs])
G=summaries['Geelong'];P=summaries['Perth']
mm=lambda a,k:sum(x[k] for x in a)/len(a)
g_home=[x for x in G if x[1]=='H'];p_away=[x for x in P if x[1]=='A']
# overall cross-offense defense: each team's PF vs opponent PA, 50/50 arithmetic
muG_over=(mm(G,2)+mm(P,3))/2
muP_over=(mm(P,2)+mm(G,3))/2
# venue sample same calculation, over five small matches, so use blend
muG_venue=(mm(g_home,2)+mm(p_away,3))/2
muP_venue=(mm(p_away,2)+mm(g_home,3))/2
prior=(muG_over+muP_over,muG_over-muP_over)
venue=(muG_venue+muP_venue,muG_venue-muP_venue)
T_raw=np.array([x[3]+x[4] for x in rows]);M_raw=np.array([x[3]-x[4] for x in rows]);
league_total=float(np.mean(T_raw));league_home_margin=float(np.mean(M_raw));
print('LEAGUE 2026 n',len(rows),'mean total',league_total,'total sample sd',float(np.std(T_raw,ddof=1)),'home margin',league_home_margin,'margin sample sd',float(np.std(M_raw,ddof=1)),'cov T M',float(np.cov(T_raw,M_raw)[0,1]));
# 50% season-based + 50% venue-conditioned expectation; add weak regularization (20%) to all-league total.
muG=.5*(muG_over+muG_venue);muP=.5*(muP_over+muP_venue)
raw_total=muG+muP
mu_total=.8*raw_total+.2*league_total
mu_margin=muG-muP # positive Geelong; home already accounted in venue split
# widen to league *raw* sample scatter (not WNBA fitted width): no false precision
sdT=max(17.0,float(np.std(T_raw,ddof=1)))
sdM=max(14.0,float(np.std(M_raw,ddof=1)))
# Normal approximate continuity-correct for integer final scores
# exact -> G +6.5 means Geelong margin >=-6, Perth -6.5 means margin <= -7
prob_G_plus=norm.sf((-6.5-mu_margin)/sdM)
prob_P_minus=1-prob_G_plus
# Under 163.5 means integer total <= 163, continuity cut at 163.5
prob_under=norm.cdf((163.5-mu_total)/sdT)
prob_over=1-prob_under
# regulation tie and OT unknown, 40-minute 5min OT needs mixture; approximation includes OT from final score histories
print('ALL',{'overall':(muG_over,muP_over),'venue':(muG_venue,muP_venue),'raw':(muG,muP),'league_total':league_total,'mean total':mu_total,'mean margin Geelong':mu_margin,'SDtotal':sdT,'SDmargin':sdM,'PGeelong+6.5':prob_G_plus,'PPerth-6.5':prob_P_minus,'PUnder163.5':prob_under,'POver163.5':prob_over,'EG':(mu_total+mu_margin)/2,'EP':(mu_total-mu_margin)/2})
# perturb team points and total mean within plausible variation from limited sample, not CI
for tot in (mu_total-5,mu_total,mu_total+5):
    print('total scenario',tot,'P Under 163.5',norm.cdf((163.5-tot)/sdT))
for margin in (mu_margin-5,mu_margin,mu_margin+5):
    print('margin scenario',margin,'P Geelong +6.5',norm.sf((-6.5-margin)/sdM))
# 100k seeded simulation of correlated total and margin normal, but analytic calculations above primary
rng=np.random.default_rng(20261113);n=100000
# residual zero covariance conditional: assumes normal total/margin independent; not demonstrated
sT=rng.normal(mu_total,sdT,n);sM=rng.normal(mu_margin,sdM,n)
print('SIMULATION CHECK n',n,'SEmax',.5/math.sqrt(n),'under',np.mean(sT<163.5),'geelongplus',np.mean(sM>-6.5))
