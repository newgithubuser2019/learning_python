import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet["A1"] = "Tall Row"
sheet["B2"] = "Wide Column"
sheet.row_dimensions[1].height = 70
sheet.column_dimensions["B"].width = 20
wb.save("dimensions.xlsx")