import openpyxl
from openpyxl.styles import Font
wb = openpyxl.Workbook()
sheet = wb["Sheet"]
italics24Font = Font(size = 24, italic = True)
sheet["A1"].font = italics24Font
sheet["A1"] = "Hellow, World"
wb.save("styles.xlsx")