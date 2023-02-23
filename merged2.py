import openpyxl
wb = openpyxl.load_workbook("merged.xlsx")
sheet = wb.active
sheet.unmerge_cells("A1:D3")
wb.save("merged.xlsx")