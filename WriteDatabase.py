from openpyxl import Workbook, load_workbook

try:
    wb = load_workbook('Fantasy_Football_Database.xlsx')

    for ws in wb:
        if ws.title == "QB":
            wsQB = ws
        if ws.title == "RB":
            wsRB = ws
        if ws.title == "TE":
            wsTE = ws
        if ws.title == "Defence":
            wsDefence = ws
        if ws.title == "Kicker":
            wsKicker = ws
except FileNotFoundError:
    wb = Workbook()

    wsQB = wb.active
    wsQB.title = "QB"
    wsQB.append(["Player","otherStats"])

    wsRB = wb.create_sheet(title = "RB")
    wsRB.append(["Player","otherStats"])

    wsTE = wb.create_sheet(title = "TE")
    wsTE.append(["Player","otherStats"])

    wsDefence = wb.create_sheet(title = "Defence")
    wsDefence.append(["Player","otherStats"])

    wsKicker = wb.create_sheet(title = "Kicker")
    wsKicker.append(["Player","otherStats"])

    wb.save('Fantasy_Football_Database.xlsx')

def writeQB(playerName, otherData):
    wsQB.append([playerName, otherData])
    wb.save('Fantasy_Football_Database.xlsx')
    return

def writeRB(playerName, otherData):
    wsQB.append([playerName, otherData])
    wb.save('Fantasy_Football_Database.xlsx')
    return

def writeTE(playerName, otherData):
    wsTE.append([playerName, otherData])
    wb.save('Fantasy_Football_Database.xlsx')
    return

def writeDefence(playerName, otherData):
    wsDefence.append([playerName, otherData])
    wb.save('Fantasy_Football_Database.xlsx')
    return

def writeKicker(playerName, otherData):
    wsKicker.append([playerName, otherData])
    wb.save('Fantasy_Football_Database.xlsx')
    return