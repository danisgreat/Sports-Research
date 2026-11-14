"""Chat-local illustrative KBL normal proxy, NOT repository-issued or calibrated.
Inputs from KBL/StatGG/recent dated matches as of 2026-11-13 before tipoff.
Full-game-including-OT approximate endpoints: no explicitly calibrated KBL OT mixture.
"""
from math import erf, sqrt
from statistics import mean
from datetime import datetime, timezone

norm_cdf=lambda z: 0.5*(1.0+erf(z/sqrt(2)))
wonju_last5_for=[65,84,104,74,90]
wonju_last5_against=[81,76,98,90,95]
kt_last5_for=[78,92,103,92,79]
kt_last5_against=[85,81,96,90,90]
season_W=(90.1+86.5)/2
season_K=(85.0+89.3)/2
form_W=(mean(wonju_last5_for)+mean(kt_last5_against))/2
form_K=(mean(kt_last5_for)+mean(wonju_last5_against))/2
pace=(77.2+72.7)/2
pace_W=pace*(113.8+116.7)/200
pace_K=pace*(111.8+113.1)/200
base_W=.55*season_W+.25*form_W+.20*pace_W
base_K=.55*season_K+.25*form_K+.20*pace_K
# Disclosed analyst sensitivities, not learned effect sizes:
venue_W=0.65; venue_K=-0.65; net_ellenson=2.5
mu_W=base_W+venue_W+net_ellenson
mu_K=base_K+venue_K
mu_total=mu_W+mu_K
mu_margin=mu_W-mu_K
sd_total=18.4; sd_margin=14.5
probs={
  'Wonju -5.5':norm_cdf((mu_margin-5.5)/sd_margin),
  'Suwon +5.5':norm_cdf((5.5-mu_margin)/sd_margin),
  'Over 179.5':norm_cdf((mu_total-179.5)/sd_total),
  'Under 179.5':norm_cdf((179.5-mu_total)/sd_total),
  'Wonju win (regulation-continuous proxy)':norm_cdf(mu_margin/sd_margin),
}
print(f'season means {season_W:.3f}/{season_K:.3f} | form means {form_W:.3f}/{form_K:.3f} | pace means {pace_W:.3f}/{pace_K:.3f}')
print(f'base {base_W:.3f}/{base_K:.3f}; central expected Wonju={mu_W:.3f} Suwon={mu_K:.3f} total={mu_total:.3f} margin={mu_margin:.3f}')
for k,v in probs.items():print(f'{k}: {100*v:.3f}%')
for delta in [-2.5,0,3.5]:
 tt=mu_total+delta;mm=mu_margin+delta
 print('Ellenson net shift vs central',delta,'Under P',round(norm_cdf((179.5-tt)/sd_total),4),'KT+5.5 P',round(norm_cdf((5.5-mm)/sd_margin),4))
print('STATUS: LOCAL_UNCALIBRATED_SCENARIO, NOT official freeze; OT explicit branch unavailable; independent official odds/props not used')
