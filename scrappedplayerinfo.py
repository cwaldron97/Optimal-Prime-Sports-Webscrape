import requests
import json


teamstats = {}

    url = http://games.espn.com/ffl/api/v2/playerInfo + '?leagueId=' + str(leagueId) + '&playerId=' \
    + str(player_id) + '&include=gamesLog|news|projections|playerInfos'

    r = requests.get(url)

    json_data = json.loads(r.text)

    print(json_data)




