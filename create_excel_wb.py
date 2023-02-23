import openpyxl
wb = openpyxl.Workbook()
inp0 = input("\nСколько книг необходимо создать?: ")
num = int(inp0)
for i in range(1, num + 1):
    if inp0 == "0":
        exit()
    if inp0 != "0":
        wb.save(filename="empty_workbook_" + str(i) + ".xlsx")
