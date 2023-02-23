# import datashader as ds
import pandas as pd
# import hvplot.pandas
# import dask.dataframe as dd
# import hvplot.dask
# import colorcet as cc
# from hvplot import hvPlot
import holoviews as hv
# from holoviews.element.tiles import EsriImagery
# from holoviews.operation.datashader import datashade


hv.extension('bokeh')
pd.options.plotting.backend = 'holoviews'

# filename = "D:\\Android\\Android Sync\\!one-way to device - other\\programming\\Python\\programs\\exercises\\!datasets\\nyc_taxi_wide.parq"
filename = "D:\\Android\\Android Sync\\!one-way to device - other\\programming\\Python\\programs\\exercises\\!datasets\\cereal_data.csv"
# df = pd.read_parquet(filename, columns=['dropoff_x', 'dropoff_y'])
# df = pd.read_parquet(filename)
# usecols = ['dropoff_x','dropoff_y']
# df = dd.read_parquet(filename)[usecols]
df = pd.read_csv(filename)
print(df.head())
# fig = df.hvplot()
# fig.show()
