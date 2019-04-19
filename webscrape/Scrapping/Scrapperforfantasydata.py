from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/rocky/Downloads/chromedriver_win32/chromedriver.exe")
loginurl = 'https://fantasydata.com/user/login?redirecturi=/'
driver.get(loginurl)
driver.find_element_by_id("username").send_keys("rockysbuddy.colin@gmail.com")
driver.find_element_by_id("password").send_keys("kfj4DJP6WV2PUfZ")
driver.find_element_by_tag_name('button').click()

dataurl = 'https://fantasydata.com/nfl-stats/fantasy-football-leaders?season=2018'

html_soup = BeautifulSoup(dataurl, 'html.parser')
type(html_soup)
Players = html_soup.find('table').find('tr')
for x in range(0,49):
    player = Players[x]
    container = player.find('td', class_="align-left align-top")
    name = (container.find('a', style_="font-weight: bold;")).text
    position = (container.find('span')).text
    team = (container.findNext('span')).text


