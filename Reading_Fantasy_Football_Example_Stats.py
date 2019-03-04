#
# Ducumentation at https://openpyxl.readthedocs.io/en/stable/index.html
#

from openpyxl import Workbook, load_workbook

#opens the excel file
wb = load_workbook('Fantasy_Football_Example_stats_to_work_with.xlsx')

positions = {} #positions 

#loops through worksheets (ws)
for ws in wb:

    #saves the name of the worksheet
    positionName = ws.title
    
    playerList = []
    #saves the first row of column names from the worksheet
    statNamesRow = ws[1]

    #saves the row as a list
    statName = []
    for cell in statNamesRow:
        statName.append(cell.value)
    
    #itterates through rows 2 and down and takes their values
    for row in ws.iter_rows(min_row=2,values_only=True):
        #saves the row as a list of values
        playerStats = {}

        #saves a player's stats as a dictionary
        index = 0
        for cell in row:
            playerStats[statName[index]] = cell
            index += 1

        #saves list of player dictionaries
        playerList.append(playerStats)
    #saves the list of player dictionaries to their position
    positions[positionName] = playerList

#prints each player and their stats for each position
for key in positions:
    print(key)
    for player in positions[key]:
        print(player)
          