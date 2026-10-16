# Failed initial league-discovery attempt

The NHL standings endpoint did not supply a complete club inventory; an alternate standings date returned HTTP 403. No row was ingested from this attempt. The next attempt discovered clubs from the accessible official Toronto season schedule and fetched each official club schedule, with duplicate-owner checks and independent ESPN corroboration. This is alternate public-source discovery, not an access-control bypass.
