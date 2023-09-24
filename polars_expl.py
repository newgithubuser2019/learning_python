import os
import sys
import time
from datetime import datetime, timedelta

import numpy as np
import polars as pl
import rich
from rich.console import Console
from rich.traceback import install

install(suppress=[rich], show_locals=False)
console = Console()

USERPROFILE = os.environ["USERPROFILE"]

# df = pl.read_csv("https://j.mp/iriscsv")
filename = USERPROFILE + "\\OneDrive\\MEGA\\programming\\_datasets\\iris.csv"
# -------------------------------------------------------------eager
# with console.status("Working...", spinner="material"):
start = time.time()
df = pl.read_csv(filename)
print(df.filter(pl.col("sepal_length") > 5)
    .groupby("species", maintain_order=True)
    .agg(pl.all().sum())
)
end = time.time()
# print(end - start)
# rich.inspect(df, methods=False)
# console.print(df, style="reverse")
# console.print(df)
sys.exit()

# -------------------------------------------------------------lazy
# Going from eager to lazy is often as simple as starting your query with .lazy() and ending with .collect()
"""
print(
    pl.read_csv(filename)
    .lazy()
    .filter(pl.col("sepal_length") > 5)
    .groupby("species", maintain_order=True)
    .agg(pl.all().sum())
    .collect()
)
"""
start = time.time()
# df = pl.read_csv(filename)
df = pl.scan_csv(filename) # for local files
df = (
    df.lazy()
    .filter(pl.col("sepal_length") > 5)
    .groupby("species", maintain_order=True)
    .agg(pl.all().sum())
    .collect()
)
print(df)
end = time.time()
print(end - start)
# sys.exit()


# -------------------------------------------------------
# series = pl.Series([1, 2, 3, 4, 5])
"""
dataframe = pl.DataFrame({"integer": [1, 2, 3], 
                          "date": [
                              (datetime(2022, 1, 1)), 
                              (datetime(2022, 1, 2)), 
                              (datetime(2022, 1, 3))
                          ], 
                          "float":[4.0, 5.0, 6.0]})

dataframe.write_parquet('polars_output.parquet')
df_parquet = pl.read_parquet('polars_output.parquet')
print(df_parquet)

#
df = pl.DataFrame({"a": np.arange(0, 8), 
                   "b": np.random.rand(8), 
                   "c": [datetime(2022, 12, 1) + timedelta(days=idx) for idx in range(8)],
                   "d": [1, 2.0, np.NaN, np.NaN, 0, -5, -42, None]
                  })

#print(df)
#df.head(5)
#df.tail(5)
print(df.sample(n=3))
print(df.describe())

df2 = df.select(
    pl.col(['a', 'b'])
)
print(df2)

df3 = df.select([
    pl.exclude('a')
])
print(df3)

df2 = df.filter(
    (pl.col('a') <= 3) & (pl.col('d').is_not_nan())
)
print(df2)

df3 = df.filter(
    pl.col("c").is_between(datetime(2022, 12, 2), datetime(2022, 12, 8)),
)
print(df3)

newdf = df.with_columns([
    pl.col('b').sum().alias('e'),
    (pl.col('b') + 42).alias('b+42')
])
print(newdf)
#
"""
# groupby
df2 = pl.DataFrame({
                    "x": np.arange(0, 8), 
                    "y": ['A', 'A', 'A', 'B', 'B', 'C', 'X', 'X'],
})
df2 = df2.with_columns([pl.when(pl.col("y") == "A").then("WWW").otherwise(pl.col("y")).alias('y')])
print(df2)
# sys.exit()

df2 = df2.groupby("y", maintain_order=True).agg([
    pl.col("*").count().alias("count"),
    pl.col("*").sum().alias("sum")
])
print(df2)

#
df = pl.DataFrame(
    {
        "col1": [1, 2, 3],
        "col2": [1, None, 3],
    },
)
print(df)

# fill na
df2 = df.with_column(
    # pl.col("col2").fill_null(pl.lit(2)),
    # pl.col("col2").fill_null(strategy="forward"),
    pl.col("col2").fill_null(pl.median("col2")),
)
print(df2)
