import pandas as pd
import numpy as np
import xlwings as xw


df = pd.read_excel("pivot_table sales-funnel.xlsx")
# Create a new workbook and add the DataFrame to Sheet1
# xw.view(df)
"""
s = df.style.format(formatter={('Price'): "{:,.2f}"})
headers = {
    'selector': 'th:not(.index_name)',
    'props': 'background-color: #000066; color: white;'
}
s.set_table_styles([headers])
"""
print(df.head())

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
