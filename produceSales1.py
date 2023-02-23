import openpyxl
wb = openpyxl.load_workbook("produceSales.xlsx")
sheet = wb["Sheet"]
updated_prices = {"Garlic": 3.07, "Celery": 1.19, "Lemon": 1.27}
print(updated_prices)

tuple(sheet["A2":"D23758"])
for rowsofcells in sheet["A2":"D23758"]:
    for cellsinrows in rowsofcells:
        produceType = sheet["A" + str(cellsinrows.coordinate[1:])].value
        for keysvar in updated_prices.keys():
            if keysvar == produceType:
                sheet["B" + str(cellsinrows.coordinate[1:])].value = updated_prices[produceType]

#print("Updating Data Completed")
wb.save("produceSalesUPDATED.xlsx")