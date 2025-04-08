import openpyxl

path = "20211024 Interrompibilita spreadsheet.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

def get_energy_team_server():
    energyTeamServer = []
    for row in range(6, 66):
        cell_value = sheet_obj[f'B{row}'].value
        energyTeamServer.append(cell_value)
    return energyTeamServer
