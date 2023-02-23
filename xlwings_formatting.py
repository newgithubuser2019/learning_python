import xlwings as xw
from xlwings import Range, constants
app1 = xw.apps
wb = app1.active.books.active
Range('A1:H500').autofit()  # autofit column(s) and row(s)
print("done formatting with XLWINGS")

"""app = xw.apps.active
wb = app.books.active
sht = xw.sheets.active
xw.Range('A23:E57').autofit()  # autofit column(s) and row(s)"""