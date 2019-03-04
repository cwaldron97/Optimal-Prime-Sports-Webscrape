from bs4 import BeautifulSoup


html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
Players = html_soup.find_all('tr')
player = Players[0]
player_name = player.td.find('td', class_ = 'player-label')
player_team = player.td.find('td', class_ = 'center')
player_team = player_team.text

