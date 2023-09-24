# import altair
# from altair import Chart, X, Y, Axis, SortField
import sys

# import sidetable
import matplotlib.pyplot as plt
import pandas as pd

# ---------------------------------------------------------------------------------------------------------------------------------------------
df = pd.read_csv('https://github.com/chris1610/pbpython/blob/master/data/school_transform.csv?raw=True', index_col=0)
print("df")
print(df)
# print("\n")
# print(df_sidetable.dtypes)

# ---------------------------------------------------------------------------------------------------------------------------------------------
df_sidetable = df.stb.freq(['State'])
print("\n------------------------------------------------------------------------------------------------------------")
print("df_sidetable")
print(df_sidetable)

df_sidetable = df.stb.freq(['Region', 'Model Selected'])
print("\n------------------------------------------------------------------------------------------------------------")
print("df_sidetable")
print(df_sidetable)

df_sidetable = df.stb.freq(['Region'], value='Award_Amount')
print("\n------------------------------------------------------------------------------------------------------------")
print("df_sidetable")
print(df_sidetable)

"""
df_sidetable = df.stb.freq(['Region'], value='Award_Amount', style=True) # requires jinja2 dependency
# The way the pandas style API works - the styled object will display in a notebook
# but if you try to print, you get the styler object instead
print("\n------------------------------------------------------------------------------------------------------------")
print("df_sidetable")
print(df_sidetable)
"""

df_sidetable = df.stb.freq(['Region', 'Model Selected'], value='Award_Amount', thresh=40, other_label='Remaining')  # thresh should be expressed as a percentage
print("\n------------------------------------------------------------------------------------------------------------")
print("df_sidetable")
print(df_sidetable)

df_sidetable = df.stb.missing()
print("\n------------------------------------------------------------------------------------------------------------")
print("df_sidetable")
print(df_sidetable)

df_sidetable = df.stb.freq(['State'], thresh=50, other_label='Rest of states')  # thresh should be expressed as a percentage
print("\n------------------------------------------------------------------------------------------------------------")
print("df_sidetable")
print(df_sidetable)

# ---------------------------------------------------------------------------------------------------------------------------------------------
# MATPLOTLIB

# fig, (ax0, ax1) = plt.subplots(nrows=1,ncols=2, sharey="all", figsize=(7, 4))
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey="all")

# Get the figure and the axes for plot 1
df_sidetable.plot(kind='barh', y="count", x="State", ax=ax0)  # y must be numeric
# ax0.set_xlim([-10000, 140000])
ax0.set(title='Revenue', xlabel='count', ylabel='states')
# Plot the average as a vertical line
avg = df_sidetable['count'].mean()
ax0.axvline(x=avg, color='b', label='Average', linestyle='--', linewidth=1)

# Get the figure and the axes for plot 2
df_sidetable.plot(kind='barh', y="percent", x="State", ax=ax1)  # y must be numeric
# Plot the average as a vertical line
avg = df_sidetable['percent'].mean()
ax1.set(title='Units', xlabel='percent', ylabel='')
ax1.axvline(x=avg, color='b', label='Average', linestyle='--', linewidth=1)

# Title the figure
fig.suptitle('Count and percent', fontsize=14, fontweight='bold')

# Hide the legends
ax1.legend().set_visible(False)
ax0.legend().set_visible(False)

plt.show()
