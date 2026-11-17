# ONECHAT_V1 template: Tennis (v29.0)

Use the skeleton in your chat packet when you have one. Otherwise copy this block: the card key and the header values come from the owner's registered request; write one PICKS row per side of every supplied line (two rows per line, same label); keep every FACTS row, writing MISSING with the reason when a value cannot be found. Replace every FILL and every field ending in ?.

```text
<!-- BEGIN ONECHAT_V1 CARD_KEY -->
format: ONECHAT_V1
card_key: FILL
sport: Tennis
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
HOME,elo_overall,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,elo_surface,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,ranking,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,last10_win_pct,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,last10_games_won_pct,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,matches_last_14d,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,h2h_wins,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,retirement_last_30d,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,venue,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,travel_km,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,opponent_strength,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,opponent_strength_method,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,availability_effect,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,adjustment_basis,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
HOME,last20_win_pct,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,elo_overall,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,elo_surface,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,ranking,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,last10_win_pct,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,last10_games_won_pct,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,matches_last_14d,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,h2h_wins,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,retirement_last_30d,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,venue,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,travel_km,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,opponent_strength,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,opponent_strength_method,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,availability_effect,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,adjustment_basis,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
AWAY,last20_win_pct,VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?
<!-- END ONECHAT_V1 CARD_KEY -->
```
