"""Read-only diagnostic for Torpedo–Arlan, 12 November 2026 (Kazakhstan local).
Independent regulation Poisson grid with deterministic OT/SO +1 goal on regulation tie.
NOT validated, calibrated, official card, or repository hockey simulator; empty-net mechanics unmodelled.
"""
from math import exp, factorial

def calc(mu_t,mu_a, maxgoals=25):
    pt=[exp(-mu_t)*mu_t**i/factorial(i) for i in range(maxgoals+1)]
    pa=[exp(-mu_a)*mu_a**j/factorial(j) for j in range(maxgoals+1)]
    scores=[(i,j,pt[i]*pa[j]) for i in range(maxgoals+1) for j in range(maxgoals+1)]
    totalmass=sum(p for i,j,p in scores)
    cover=sum(p for i,j,p in scores if i-j>=2)
    under=sum(p for i,j,p in scores if (i+j+(i==j))<=6)
    draw=sum(p for i,j,p in scores if i==j)
    regwin=sum(p for i,j,p in scores if i>j)
    return {'mu_t':mu_t,'mu_a':mu_a,'total_mean_reg':mu_t+mu_a,'grid_mass':totalmass, 'T_-1.5':cover/totalmass, 'A_+1.5':1-cover/totalmass, 'Under_6.5':under/totalmass, 'Over_6.5':1-under/totalmass,'reg_draw':draw/totalmass,'reg_T_win':regwin/totalmass, 'E_total_incl_tie_goal':mu_t+mu_a+draw/totalmass}

if __name__=='__main__':
  teams={'T':(138,46,26),'A':(92,58,26)}
  league=(138+102+92+108+87+90+66+69+48+31)/(26+25+26+26+24+26+26+26+25+24)
  b_t=(138/26)*(58/26)/league
  b_a=(92/26)*(46/26)/league
  print('LEAGUE goals per team-game',league,'multiplicative central:',b_t,b_a)
  cases={'low-scoring':(3.2,1.6),'base-rate':(b_t,b_a),'goalie-high-sensitivity':(4.0,2.4),'balanced-high':(3.35,2.55)}
  for k,v in cases.items():print(k,calc(*v))

# Historical rows transcribed from official Pro Hokei Ligasy 2026/27 team schedules,
# newest first, final including OT/SO. The one awarded 5-0 game is flagged.
TORPEDO_LAST20=[
 ('2026-10-30','Nomad',3,0,''),('2026-10-29','Nomad',6,3,''),
 ('2026-10-26','Aqtobe',3,1,''),('2026-10-25','Aqtobe',4,2,''),
 ('2026-10-20','Almaty',4,0,''),('2026-10-19','Almaty',9,1,''),
 ('2026-10-16','Ertis',12,1,''),('2026-10-15','Ertis',9,2,''),
 ('2026-10-12','Ertis',8,0,''),('2026-10-11','Ertis',13,0,''),
 ('2026-10-07','Nomad',2,3,'SO'),('2026-10-06','Nomad',2,3,'OT'),
 ('2026-10-02','Beibarys',9,2,''),('2026-10-01','Beibarys',4,3,''),
 ('2026-09-28','Aqtobe',6,2,''),('2026-09-27','Aqtobe',9,1,''),
 ('2026-09-21','Gornyak',1,2,''),('2026-09-20','Gornyak',4,3,''),
 ('2026-09-17','Qulager',6,3,''),('2026-09-16','Qulager',3,2,'OT')]
ARLAN_LAST20=[
 ('2026-10-30','Gornyak',4,0,''),('2026-10-29','Gornyak',3,2,''),
 ('2026-10-26','Almaty',4,3,''),('2026-10-25','Almaty',3,0,''),
 ('2026-10-21','Ertis',9,2,''),('2026-10-20','Ertis',5,1,''),
 ('2026-10-15','Saryarqa',4,3,'SO'),('2026-10-14','Saryarqa',1,4,''),
 ('2026-10-11','Nomad',2,4,''),('2026-10-10','Nomad',3,2,'OT'),
 ('2026-10-07','Qulager',4,3,''),('2026-10-06','Qulager',4,3,''),
 ('2026-10-03','Almaty',3,2,''),('2026-10-02','Almaty',1,2,''),
 ('2026-09-28','Ertis',5,3,''),('2026-09-27','Ertis',11,2,''),
 ('2026-09-23','Saryarqa',2,5,''),('2026-09-22','Saryarqa',5,0,'TECH'),
 ('2026-09-16','Beibarys',1,0,''),('2026-09-15','Beibarys',3,1,'')]

def summarize(rows,n):
 subset=[r for r in rows[:n] if r[4]!='TECH']
 return {'window':n,'n_played':len(subset), 'gf':sum(r[2] for r in subset),'ga':sum(r[3] for r in subset),'total_mean':round(sum(r[2]+r[3] for r in subset)/len(subset),3), 'under6.5':sum(r[2]+r[3]<=6 for r in subset), 'cover_minus1.5':sum(r[2]-r[3]>=2 for r in subset), 'over6.5':sum(r[2]+r[3]>=7 for r in subset)}
if __name__=='__main__':
  for name,rows in [('TORPEDO',TORPEDO_LAST20),('ARLAN',ARLAN_LAST20)]:
   for n in [5,10,15,20]:print(name,summarize(rows,n))
