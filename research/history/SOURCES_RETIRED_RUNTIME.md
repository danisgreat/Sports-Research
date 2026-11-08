# Retired-runtime data sources (design record) formerly SOURCES.md Part D

Moved verbatim on 2026-11-08 (CR-2026.11.08-R2). Historical lineage, including failures; not an active source list.

## D. Data sources of the retired numerical runtime (design record)

Used to describe the training data of the removed runtime. They remain valid places to read historical data by hand; licences are as stated.

| Source id | Sport | Grain | URL | Update cadence | Available to the forecaster at | Licence |
|---|---|---|---|---|---|---|
| cricsheet | cricket | ball_by_ball | https://cricsheet.org | daily | match_start_utc | ODC-By 1.0 (Open Data Commons Attribution; corrected 2026-10-14 from "ODbL 1.0" against cricsheet.org/register) |
| nflfastr | american_football | play_by_play | https://github.com/nflverse/nflverse-data | weekly_in_season | kickoff_utc | MIT |
| nba_stats | basketball | possession_and_box | https://stats.nba.com | live_post_game | scheduled_tipoff_utc | fair_use_research |
| pybaseball_statcast | baseball | pitch_and_pa | https://baseballsavant.mlb.com | daily | first_pitch_utc | fair_use_research |
| fitzroy_afl | afl | match_and_player | https://jimmyday12.github.io/fitzRoy | post_round | bounce_utc | GPL-3 |
| nrlr_nrl | nrl | match_and_play | https://itsjase.github.io/nrlR | post_round | kickoff_utc | MIT |
| statsbomb_footballdata | soccer | match_and_xg | https://www.football-data.co.uk | weekly_post_match | kickoff_utc | open_research |
| moneypuck_nhl | nhl | shot_and_game | https://moneypuck.com/data.htm | daily_in_season | puck_drop_utc | open_attribution |
| tennis_abstract | tennis | point_and_match | https://github.com/JeffSackmann | daily_post_tournament | match_start_utc | cc_by_nc_sa_4.0 |
