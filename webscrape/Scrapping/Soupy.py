from requests import get
from bs4 import BeautifulSoup


url = 'https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2018'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
Players = html_soup.find_all('tr')
for x in range(0, 500):
    player = Players[x]
    statistics = player.find_all('td')
    player_name = player.td.find('td', class_='player-label')
    #insert function to pass player name to database

    player_team = statistics.td.find('a', class_='center')
    player_team = player_team.text
    #insert function to pass player team to database

    playerpositiontemp = statistics[4]
    playerposition = playerpositiontemp.text
    #insert function to pass player position to database

    playerpointstemp = statistics[5]
    playerpoints = playerpositiontemp.float
    #insert function to pass player points to database

    playergamestemp = statistics[6]
    playergames = playergamestemp.float
    #insert function to pass player games to database

    playeravgtemp = statistics[7]
    playeravg = playeravgtemp.float
    #insert function to pass player avg to database





