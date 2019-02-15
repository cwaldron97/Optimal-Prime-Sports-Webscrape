#
# Ducumentation at https://openpyxl.readthedocs.io/en/stable/index.html
#

from openpyxl import Workbook, load_workbook

#opens the excel file
wb = load_workbook('Fantasy_Football_Example_stats_to_work_with.xlsx')

#loops through worksheets (ws)
for ws in wb:

    #prints the name of the worksheet
    print(ws.title)

    statName = []
    
    #saves the first row of column names from the worksheet
    statNamesRow = ws[1]

    #saves the row as a list
    for cell in statNamesRow:
        statName.append(cell.value)
    
    #itterates through rows 2 and down and takes their values
    for row in ws.iter_rows(min_row=2,values_only=True):
        #saves the row as a list of values
        playerStats = []
        for cell in row:
            playerStats.append(cell)
        
        #prints the name of each value type and then the value itself
        for index, val in enumerate(playerStats):
            print(statName[index],val)

    