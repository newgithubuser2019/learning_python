# IMPORTS
import datetime
import decimal
import json
import os
import pprint
import re
import shutil
import sys
from functools import reduce

import numpy as np
import openpyxl
import pandas as pd
import plotly.express as px

# import sidetable
from pandas.tseries.offsets import DateOffset

import функции

pd.set_option("display.max_rows", 1500)
pd.set_option("display.max_columns", 100)
pd.set_option("max_colwidth", 30)
pd.set_option("expand_frame_repr", False)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# global variables
USERPROFILE = os.environ["USERPROFILE"]

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# empty lists

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# empty dictionaries

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# empty dataframes
# findf = pd.DataFrame()
df_bez_korma = pd.DataFrame()

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
# path_1 = USERPROFILE + "\\Documents\\Работа\\отчетность\\ежедневно\\накопительный отчет\\время поднятия кормушки\\"
# listoffiles_1 = os.listdir(path_1)
# file names
# filename0a = USERPROFILE + "\\Documents\\Работа\\отчетность\\ежедневно\\накопительный отчет\\_промежуточный файл df_впк.xlsx"
# filename = USERPROFILE + "\\Documents\\Google Sheets Test.xlsx"
# filename5 = USERPROFILE + "\\Documents\\Работа\\отчетность\\ежедневно\\накопительный отчет\\время поднятия кормушки\\время поднятия кормушки.xlsx"
# filename5 = "D:\\programming\\_datasets\\просмотры резюме.xlsx"
filename0 = USERPROFILE + "\\Documents\\Работа\\отдельные поручения\\Тест excel.xlsm"
filename0b = USERPROFILE + "\\Documents\\Работа\\отдельные поручения\\задание 6 - df.xlsx"
filename2a = USERPROFILE + "\\Documents\\Работа\\отдельные поручения\\задание 2 - федеральный округ.xlsx"
filename2b = USERPROFILE + "\\Documents\\Работа\\отдельные поручения\\задание 2 - функциональный блок.xlsx"

# ------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# ЗАДАНИЕ 1
df_from_excel = pd.read_excel(
    filename0,
    sheet_name="Штатное расписание",
    # index_col=0,
    # engine = "openpyxl",
    header=2,
    # usecols = "A:L",
    usecols = "A,C,G,H,I,K",
    )
df_from_excel = df_from_excel.drop([0], axis = 0) # drop row with index 0
# print(df_from_excel.head())
print(df_from_excel.isna().sum())
df_from_excel["Полная/ неполная ставка"] = df_from_excel["Полная/ неполная ставка"].fillna("")
df_from_excel = df_from_excel.loc[df_from_excel["Тип назначения"] != "Внутренний совместитель"]
df_from_excel = df_from_excel.loc[(df_from_excel["Полная/ неполная ставка"] == 1) | (df_from_excel["Полная/ неполная ставка"] == "")]
# ШЧ --------------------------------------------------
df_ШЧ = df_from_excel.copy(deep=True)
# АЧ --------------------------------------------------
df_АЧ = df_from_excel.copy(deep=True)
df_АЧ = df_АЧ.loc[df_АЧ["Статус назначения"] == "Активное назначение"]
# MERGED - функциональный блок --------------------------------------------------------------------
df_ШЧ_фб = df_ШЧ.copy(deep=True)
df_ШЧ_фб = df_ШЧ_фб.groupby(["Функциональный Блок"], as_index=False).agg({"Должность": "count"})
df_ШЧ_фб = df_ШЧ_фб.rename(columns={"Должность": "ШЧ"})
"""
df_ШЧ_фб["minmax"] = ""
for i in df_ШЧ_фб['ШЧ'].nlargest(3):
    df_ШЧ_фб.loc[df_ШЧ_фб['ШЧ']==i, ["minmax"]] = "топ3"
for i in df_ШЧ_фб['ШЧ'].nsmallest(3):
    df_ШЧ_фб.loc[df_ШЧ_фб['ШЧ']==i, ["minmax"]] = "мин3"
print(df_ШЧ_фб)
fig = px.bar(
    df_ШЧ_фб,
    x='Функциональный Блок',
    y='ШЧ',
    # hover_name='name',
    color='minmax',
    # size='calories',
    # facet_row='shelf',
    # facet_col='type',
    # barmode="group",
    pattern_shape="minmax",
    pattern_shape_sequence=["", "x", "+"],
    title='Штатная численность по функциональным блокам',
    )
# fig.show()
# fig.write_image('6.1.png')
sys.exit()
"""
#
df_АЧ_фб = df_АЧ.copy(deep=True)
df_АЧ_фб = df_АЧ_фб.groupby(["Функциональный Блок"], as_index=False).agg({"Должность": "count"})
df_АЧ_фб = df_АЧ_фб.rename(columns={"Должность": "АЧ"})
"""
df_АЧ_фб["minmax"] = ""
for i in df_АЧ_фб['АЧ'].nlargest(3):
    df_АЧ_фб.loc[df_АЧ_фб['АЧ']==i, ["minmax"]] = "топ3"
for i in df_АЧ_фб['АЧ'].nsmallest(3):
    df_АЧ_фб.loc[df_АЧ_фб['АЧ']==i, ["minmax"]] = "мин3"
print(df_АЧ_фб)
"""
# sys.exit()
df_merged = pd.merge(df_ШЧ_фб, df_АЧ_фб, how = "left", on = ["Функциональный Блок"])
print(df_merged)
ШЧ = df_merged["ШЧ"].sum()
print(ШЧ)
АЧ = df_merged["АЧ"].sum()
print(АЧ)
df_long = pd.melt(df_merged, id_vars=['Функциональный Блок'], value_vars=['ШЧ', 'АЧ'])

df_long["minmax"] = ""
for i in df_long.loc[df_long["variable"] == "ШЧ"]["value"].nlargest(3):
    df_long.loc[df_long['value']==i, ["minmax"]] = "топ3"
for i in df_long.loc[df_long["variable"] == "ШЧ"]["value"].nsmallest(3):
    df_long.loc[df_long['value']==i, ["minmax"]] = "мин3"
for i in df_long.loc[df_long["variable"] == "АЧ"]["value"].nlargest(3):
    df_long.loc[df_long['value']==i, ["minmax"]] = "топ3"
for i in df_long.loc[df_long["variable"] == "АЧ"]["value"].nsmallest(3):
    df_long.loc[df_long['value']==i, ["minmax"]] = "мин3"
print(df_long)

# sys.exit()

fig = px.funnel(
    df_long,
    x='Функциональный Блок',
    y='value',
    # hover_name='name',
    color='variable',
    # size='calories',
    # facet_row='shelf',
    # facet_col='type',
    # barmode="group",
    # pattern_shape="minmax",
    # pattern_shape_sequence=[".", "x", "+"],
    facet_row="minmax",
    facet_col="variable",
    title='Штатная и экономически активная численность по функциональным блокам',
    )
fig.show()
sys.exit()
df_from_excel = df_from_excel.loc[df_from_excel["Тип назначения"].str.contains("Основное")]
df_from_excel = df_from_excel.loc[df_from_excel["Полная/ неполная ставка"]==1]

# ----------------------------------------------------------------------------------------------------
# ЗАДАНИЕ 2
df_from_excel = pd.read_excel(
    filename0,
    sheet_name="Принятые и уволенные",
    # index_col=0,
    # engine = "openpyxl",
    header=2,
    usecols = "A:L",
    )
# print(df_from_excel.dtypes)
дата_нач = "2013.01.01"
дата_кон = "2013.04.01"
дата_min = datetime.datetime.strptime(дата_нач, "%Y.%m.%d")
дата_max = datetime.datetime.strptime(дата_кон, "%Y.%m.%d")
df_from_excel = df_from_excel.loc[df_from_excel["Тип назначения"].str.contains("Основное")]
df_from_excel = df_from_excel.loc[df_from_excel["Полная/ неполная ставка"].str.contains("Полная")]
# ПРИНЯТЫЕ--------------------------------------------------------------------
df_принятые = df_from_excel.copy(deep=True)
df_принятые = df_принятые.loc[(df_принятые["дата приема"]>=дата_min) & (df_принятые["дата приема"]<дата_max)]
# УВОЛЕННЫЕ--------------------------------------------------------------------
df_уволенные = df_from_excel.copy(deep=True)
df_уволенные = df_уволенные.loc[(df_уволенные["дата увольнения"]>=дата_min) & (df_уволенные["дата увольнения"]<дата_max)]
# MERGED - федеральный округ --------------------------------------------------------------------
df_принятые_фо = df_принятые.copy(deep=True)
df_принятые_фо = df_принятые_фо.groupby(["Федеральный округ"], as_index=False).agg({"дата приема": "count"})
df_уволенные_фо = df_уволенные.copy(deep=True)
df_уволенные_фо = df_уволенные_фо.groupby(["Федеральный округ"], as_index=False).agg({"дата увольнения": "count"})
df_merged = pd.merge(df_принятые_фо, df_уволенные_фо, how = "left", on = ["Федеральный округ"])
df_merged = df_merged.rename(columns={
    "дата приема": "принято",
    "дата увольнения": "уволено",
    })
print(df_merged)
принято = df_merged["принято"].sum()
print(принято)
уволено = df_merged["уволено"].sum()
print(уволено)
функции.pd_toexcel(
        pd,
        #
        filename = filename2a,
        разновидность = "Лист1",
        df_для_записи = df_merged,
        header_pd = "True",
        rowtostartin_pd = 0,
        coltostartin_pd = 0,
    )
# MERGED - функциональный блок --------------------------------------------------------------------
df_принятые_фб = df_принятые.copy(deep=True)
df_принятые_фб = df_принятые_фб.groupby(["Функциональный Блок"], as_index=False).agg({"дата приема": "count"})
df_уволенные_фб = df_уволенные.copy(deep=True)
df_уволенные_фб = df_уволенные_фб.groupby(["Функциональный Блок"], as_index=False).agg({"дата увольнения": "count"})
df_merged = pd.merge(df_принятые_фб, df_уволенные_фб, how = "left", on = ["Функциональный Блок"])
df_merged = df_merged.rename(columns={
    "дата приема": "принято",
    "дата увольнения": "уволено",
    })
print(df_merged)
принято = df_merged["принято"].sum()
print(принято)
уволено = df_merged["уволено"].sum()
print(уволено)
функции.pd_toexcel(
        pd,
        #
        filename = filename2b,
        разновидность = "Лист1",
        df_для_записи = df_merged,
        header_pd = "True",
        rowtostartin_pd = 0,
        coltostartin_pd = 0,
    )

# ----------------------------------------------------------------------------------------------------
# ЗАДАНИЕ 6
df_from_excel = pd.read_excel(
    filename0b,
    sheet_name="Лист1",
    # index_col=0,
    # engine = "openpyxl",
    header=0,
    # usecols = "A:L",
    usecols = "A:F",
    )
df_from_excel = df_from_excel.drop(["уволено"], axis = 1)
df_from_excel["minmax"] = ""
for i in df_from_excel['АЧ'].nlargest(3):
    df_from_excel.loc[df_from_excel['АЧ']==i, ["minmax"]] = "топ3"
for i in df_from_excel['АЧ'].nsmallest(3):
    df_from_excel.loc[df_from_excel['АЧ']==i, ["minmax"]] = "мин3"
print(df_from_excel)
fig = px.bar(
    df_from_excel,
    x='Функциональный Блок',
    y=['ШЧ', 'АЧ'],
    # hover_name='name',
    # color='minmax',
    # size='calories',
    barmode="group",
    # pattern_shape="minmax",
    # pattern_shape_sequence=[".", "x", "+"],
    # facet_row="minmax",
    # facet_col="variable",
    # category_orders={"minmax": ["топ3", "", "мин3"], "variable": ["ШЧ", "АЧ"]},
    title='Штатная и экономически активная численность по функциональным блокам',
    )
fig.show()
fig = px.bar(
    df_from_excel,
    x='Функциональный Блок',
    y='АЧ',
    # hover_name='name',
    color='minmax',
    # size='calories',
    # barmode="group",
    # pattern_shape="minmax",
    # pattern_shape_sequence=[".", "x", "+"],
    # facet_row="minmax",
    # facet_col="variable",
    # category_orders={"minmax": ["топ3", "", "мин3"], "variable": ["ШЧ", "АЧ"]},
    title='Штатная и экономически активная численность по функциональным блокам',
    ).add_traces(px.line(df_from_excel, x="Функциональный Блок", y="принято").update_traces(showlegend=True, name="Функциональный Блок").data)
fig.show()
sys.exit()
# df_long = pd.melt(df_from_excel, id_vars=['Функциональный Блок', "minmax"], value_vars=['АЧ', 'принято', 'отток'])
print(df_long)
fig = px.bar(
    df_long,
    x='Функциональный Блок',
    y="value",
    # hover_name='name',
    color='отток',
    # size='calories',
    # barmode="group",
    # pattern_shape="minmax",
    # pattern_shape_sequence=[".", "x", "+"],
    facet_row="minmax",
    # facet_col="variable",
    # category_orders={"minmax": ["топ3", "", "мин3"], "variable": ["ШЧ", "АЧ"]},
    title='Штатная и экономически активная численность по функциональным блокам',
    )
fig.show()
sys.exit()
df_long = pd.melt(df_from_excel, id_vars=['Функциональный Блок'], value_vars=['ШЧ', 'АЧ', 'принято', 'отток'])
print("\n")
df_long["minmax"] = ""
for i in df_long.loc[df_long["variable"] == "ШЧ"]["value"].nlargest(3):
    df_long.loc[df_long['value']==i, ["minmax"]] = "топ3"
for i in df_long.loc[df_long["variable"] == "ШЧ"]["value"].nsmallest(3):
    df_long.loc[df_long['value']==i, ["minmax"]] = "мин3"
for i in df_long.loc[df_long["variable"] == "АЧ"]["value"].nlargest(3):
    df_long.loc[df_long['value']==i, ["minmax"]] = "топ3"
for i in df_long.loc[df_long["variable"] == "АЧ"]["value"].nsmallest(3):
    df_long.loc[df_long['value']==i, ["minmax"]] = "мин3"
print(df_long)
fig = px.bar(
    df_long,
    x='Функциональный Блок',
    y='value',
    # hover_name='name',
    color='variable',
    # size='calories',
    barmode="group",
    # pattern_shape="minmax",
    # pattern_shape_sequence=[".", "x", "+"],
    facet_row="minmax",
    # facet_col="variable",
    # category_orders={"minmax": ["топ3", "", "мин3"], "variable": ["ШЧ", "АЧ"]},
    title='Штатная и экономически активная численность по функциональным блокам',
    )
fig.show()
sys.exit()
fig = px.funnel(
    df_long,
    x='Функциональный Блок',
    y='value',
    # hover_name='name',
    color='variable',
    # size='calories',
    # facet_row='shelf',
    # facet_col='type',
    # barmode="group",
    # pattern_shape="minmax",
    # pattern_shape_sequence=[".", "x", "+"],
    facet_row="minmax",
    facet_col="variable",
    # category_orders={"minmax": ["топ3", "", "мин3"], "variable": ["ШЧ", "АЧ"]},
    title='Штатная и экономически активная численность по функциональным блокам',
    )
fig.show()
sys.exit()
