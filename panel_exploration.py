import datetime as dt
# import hvplot
# import hvplot.pandas
# import holoviews as hv
import sys

import altair as alt
import pandas as pd
import panel as pn
# from altair import Chart
# from altair import SortField
from altair import Axis, X, Y, datum

# hv.extension('bokeh')
pd.options.plotting.backend = 'holoviews'
alt.renderers.enable("default")
pn.extension("vega")

"""
def f(x):
    return x * x
pn.interact(f, x=10)
"""

filename = "D:\\Android\\Android Sync\\!one-way to device - other\\programming\\Python\\programs\\exercises\\!datasets\\stocks.csv"
df = pd.read_csv(filename)
print(df.head())

#  create list of company names (tickers) to use as options
tickers = df["symbol"].unique()
#  this creates the dropdown widget
ticker = pn.widgets.Select(name="Company", options=[i for i in tickers])

#  this creates the date range slider
date_range_slider = pn.widgets.DateRangeSlider(
    name="Date Range Slider",
    start=dt.datetime(2001, 1, 1),
    end=dt.datetime(2010, 1, 1),
    value=(dt.datetime(2001, 1, 1), dt.datetime(2010, 1, 1))
)

title = "Stock Price Dashboard"
subtitle = "This dashboard allows you to select a company and date range to see stock prices."


@pn.depends(ticker.param.value, date_range_slider.param.value)
def get_plot(ticker, date_range):
    #  Load and format the data
    df = pd.read_csv(filename)
    df["date"] = pd.to_datetime(df["date"])

    #  create date filter using values from the range slider
    #  store the first and last date range slider value in a var
    start_date = date_range_slider.value[0]
    end_date = date_range_slider.value[1]

    #  create filter mask for the dataframe
    mask = (df["date"] > start_date) & (df["date"] <= end_date)
    #  filter the dataframe
    df = df.loc[mask]

    #  create the Altair chart object
    chart = alt.Chart(df)
    chart = chart.mark_line()
    chart = chart.encode(
        x=X(
            "date:T",  # sort=SortField(field='count', order='descending')
            axis=Axis(title="")),
        y=Y(
            "price:Q",
            axis=Axis(title="")),
        # color = "symbol",
        tooltip=alt.Tooltip(["date", "price"]),
        )
    chart = chart.transform_filter((datum.symbol == ticker))
    # chart = df.hvplot(x='date', y=['price'], kind = 'line', by='symbol')
    # chart = df.hvplot(x='date', y=['price'], kind = 'line', groupby='symbol', widgets={'symbol': pn.widgets.DiscreteSlider})
    return chart


dashboard = pn.Row(pn.Column(title, subtitle, ticker, date_range_slider), get_plot)
dashboard.servable()
# panel serve --show panel_exploration.py
