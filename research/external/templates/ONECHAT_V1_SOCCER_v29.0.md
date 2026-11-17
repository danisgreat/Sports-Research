# ONECHAT_V1 template: Soccer (v29.0)

Use the skeleton in your chat packet when you have one. Otherwise copy this block: the card key and the header values come from the owner's registered request; write one PICKS row per side of every supplied line (two rows per line, same label); keep every FACTS row, writing MISSING with the reason when a value cannot be found. Replace every FILL and every field ending in ?.

```text
<!-- BEGIN ONECHAT_V1 CARD_KEY -->
format: ONECHAT_V1
card_key: FILL
sport: Soccer
competition: FILL
home: FILL
away: FILL
scheduled_start: FILL
request_at: FILL
research_start_at: FILL
research_end_at: FILL
not_started_source: FILL
not_started_observed_at: FILL
outcome_exposure: FILL

PICKS
label,family,side,line,p,lean,centre,availability_basis,result_source
L1,FAMILY?,SIDE?,LINE?,P?,,CENTRE?,BASIS?,RESULT_URL?
L1,FAMILY?,SIDE?,LINE?,P?,,CENTRE?,BASIS?,RESULT_URL?

FACTS
side,field,value,source,observed_at
HOME,season_games,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,season_score_for_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,season_score_against_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,last5_score_for_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,last5_score_against_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,last10_score_for_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,last10_score_against_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,last10_first_half_goals_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,last10_corners_for_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,last10_corners_against_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,rest_days,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,key_absences,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,lineup_confirmed,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,venue,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,travel_km,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,opponent_strength,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,opponent_strength_method,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,availability_effect,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,adjustment_basis,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,last20_score_for_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,last20_score_against_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,season_games,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,season_score_for_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,season_score_against_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,last5_score_for_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,last5_score_against_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,last10_score_for_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,last10_score_against_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,last10_first_half_goals_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,last10_corners_for_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,last10_corners_against_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,rest_days,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,key_absences,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,lineup_confirmed,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,venue,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,travel_km,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,opponent_strength,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,opponent_strength_method,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,availability_effect,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,adjustment_basis,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,last20_score_for_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,last20_score_against_pg,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
<!-- END ONECHAT_V1 CARD_KEY -->
```
