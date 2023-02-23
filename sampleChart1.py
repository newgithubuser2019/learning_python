import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1, 11):
    sheet["A" + str(i)] = i
ReferenceObject = openpyxl.chart.Reference(sheet, min_col = 1, min_row = 1, max_col = 1, max_row = 10)
SeriesObject = openpyxl.chart.Series(ReferenceObject, title = "first series")
ChartObject = openpyxl.chart.BarChart()
ChartObject.title = "My Chart"
ChartObject.append(SeriesObject)
sheet.add_chart(ChartObject, "C5")
wb.save("sampleChart.xlsx")