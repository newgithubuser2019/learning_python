# PREPARATION
import os
import datetime
from datetime import datetime
import re
import pprint
import shutil
import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font, colors
import json
import decimal
from decimal import Decimal
import pandas as pd
import numpy as np
import sidetable
from functools import reduce
from pandas.tseries.offsets import DateOffset
pd.set_option('display.max_rows', 1500)
pd.set_option('display.max_columns', 100)
pd.set_option('max_colwidth', 15)
pd.set_option('expand_frame_repr', False)
from функции import print_line
from функции import rawdata_budget
from функции import pd_movecol
from функции import pd_toexcel
from функции import pd_readexcel
from функции import writing_to_excel_openpyxl
from функции import json_dump_n_load
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# global variables
USERPROFILE = os.environ['USERPROFILE']

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# empty lists

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# empty dictionaries

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# empty dataframes
findf = pd.DataFrame()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# default lists

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# default dictionaries

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# prompts for user input
# prompt1 = "\nРеализация: "

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# user inputs
# inp1 = input(prompt1)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# file paths
filename3 = USERPROFILE + "\\Documents\\Работа\\отдельные поручения\\тест_g5.csv"
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
df_from_excel = pd.read_csv(filename3)
print(df_from_excel)
descr = df_from_excel.describe()
print(descr)
mean = df_from_excel["Salary Rate, $"].mean()
std = df_from_excel["Salary Rate, $"].std()
# print(mean)
# print(std)
df_from_excel['zscore'] = (df_from_excel['Salary Rate, $']-mean)/std
print(df_from_excel)
# exit()
cv = std/mean
print(cv)
# df_from_excel = df_from_excel.drop(df_from_excel[((df_from_excel['Salary Rate, $'] / df_from_excel["Salary Rate, $"].std()) > 3)].index)
df_from_excel = df_from_excel.drop(df_from_excel[((df_from_excel['zscore'] / 1) > 3)].index)
print(df_from_excel)
descr = df_from_excel.describe()
print(descr)
