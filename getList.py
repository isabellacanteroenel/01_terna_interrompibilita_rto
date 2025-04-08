
import openpyxl

path = "20211024 Interrompibilita spreadsheet.xlsx"

wb_obj = openpyxl.load_workbook(path)


sheet_obj = wb_obj.active

energyTeamServer = []
energyTeamUPMC = []
tecnowattUPCM = []

for row in range(6, 66):
    cell_value = sheet_obj[f'B{row}'].value
    energyTeamServer.append(cell_value)

print(energyTeamServer)

