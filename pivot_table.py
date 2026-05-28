import sys

import numpy as np
import pandas as pd



df = pd.read_excel("D:\\programming\\datasets\\время поднятия кормушки.xlsx")
# print(df.head())

# import xlwings as xw
# xw.view(df)

#import dtale
#d = dtale.show(df)
#d.open_browser()
#d.kill()
#if __name__ == '__main__':
      #dtale.show(df, subprocess=False)
#sys.exit()

import df2tables
df2tables.render(df)

sys.exit()

# np.select exploration -----------------------------------------------------------------
# you can use np.select for numeric analysis as well as the text
patterns = [
    (df['Name'].str.contains("Trantow-Barrows", case=False,  regex=False), "repl1"),
    (df['Name'].str.contains('Kiehn-Spinka',  regex=False, case=False), 'repl2'),
]
criteria, values = zip(*patterns)
# df['Group_1'] = np.select(criteria, values, 'other')
df['Group_1'] = np.select(criteria, values, None)
df["Group_1"] = df['Group_1'].combine_first(df['Name'])
# print(df.head())

# -----------------------------------------------------------------------------

df["Status"] = df["Status"].astype("category")
df["Status"].cat.set_categories(["won", "pending", "presented", "declined"], inplace=True)

# -----------------------------------------------------------------------------------------

# df_pivot = pd.pivot_table(df,index=["Name"])
# df_pivot = pd.pivot_table(df,index=["Manager","Rep"])
df_pivot = pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"])
df_pivot = pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"], aggfunc=np.sum)
df_pivot = pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"], aggfunc=[np.mean, len])
# xw.view(df_pivot)
df_pivot = pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"], columns=["Product"], aggfunc=[np.sum])
df_pivot = pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"], columns=["Product"], aggfunc=[np.sum], fill_value=0)
df_pivot = pd.pivot_table(df, index=["Manager", "Rep"], values=["Price", "Quantity"], columns=["Product"], aggfunc=[np.sum], fill_value=0)
df_pivot = pd.pivot_table(df, index=["Manager", "Rep", "Product"], values=["Price", "Quantity"], aggfunc=[np.sum], fill_value=0)
# margins=True adds totals row at the bottom
df_pivot = pd.pivot_table(
    df, index=["Manager", "Rep", "Product"], values=["Price", "Quantity"], aggfunc=[np.sum, np.mean], fill_value=0, margins=True
    )
df_pivot = pd.pivot_table(df, index=["Manager", "Status"], values=["Price"], aggfunc=[np.sum], fill_value=0, margins=True)
df_pivot = pd.pivot_table(
    df, index=["Manager", "Status"], columns=["Product"], values=["Quantity", "Price"], aggfunc={"Quantity": len, "Price": np.sum}, fill_value=0
    )
df_pivot = pd.pivot_table(
    df, index=["Manager", "Status"], columns=["Product"], values=["Quantity", "Price"], aggfunc={"Quantity": len, "Price": [np.sum, np.mean]}, fill_value=0
    )
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print(df_pivot)
df_query = df_pivot.query('Manager == ["Debra Henley"]')
# df_query = df_pivot.query('Status == ["pending","won"]')
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print(df_query)
