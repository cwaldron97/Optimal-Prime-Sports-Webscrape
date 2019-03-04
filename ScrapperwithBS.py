from requests import get

url = 'https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2018'

response = get(url)
print response(response.txt[:510])