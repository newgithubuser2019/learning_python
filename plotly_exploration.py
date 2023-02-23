import pandas as pd
# import streamlit as st
import plotly.express as px
pd.options.plotting.backend = "plotly"
pd.set_option('display.max_rows', 1500)
pd.set_option('display.max_columns', 100)
pd.set_option('max_colwidth', 16)
pd.set_option('expand_frame_repr', False)

# -----------------------------------------------------------------------------------------------------------------------------------------
filename = "D:\\Android\\Android Sync\\!one-way to device - other\\programming\\Python\\programs\\exercises\\!datasets\\cereal_data.csv"
# url = "https://cdn.jsdelivr.net/npm/vega-datasets@2.2.0/data/airports.csv"
# url = "https://github.com/chris1610/pbpython/blob/master/data/cereal_data.csv?raw=True"

# -----------------------------------------------------------------------------------------------------------------------------------------
df = pd.read_csv(filename)
# print(df)

# basic - scatter, line, bar, histogram, box, violin, strip
# advanced - funnel_chart, timeline, treemap, sunburst
fig = px.scatter(
    df,
    x='sugars',
    y='rating',
    hover_name='name',
    color='mfr',
    size='calories',
    # facet_row='shelf',
    facet_col='type',
    title='Cereal ratings vs. sugars',
    )
# fig = px.histogram(df, x='rating', title='Rating distribution')
# fig = px.treemap(df, path=['shelf', 'mfr'], values='cereal', title='Cereals by shelf location')
fig = px.sunburst(df, path=['mfr', 'shelf'], values='cereal')
fig.show()
# exit()

# saving image - Supported formats: ['png', 'jpg', 'jpeg', 'webp', 'svg', 'pdf', 'eps', 'json']
fig.write_image('plotly_exploration.pdf')
# saving html
fig.write_html(
    'plotly_exploration.html',
    include_plotlyjs='cdn',
    full_html=False,
    include_mathjax='cdn',
    )

# -----------------------------------------------------------------------------------------------------------------------------------------
# create a visualization using a combination of the pandas and Plotly API
fig = df[['sodium', 'potass']].plot(
    kind='hist',
    nbins=50,
    histnorm='probability density',
    opacity=0.75,
    marginal='box',
    title='Potassium and Sodium Distributions'
    )

# update figure
fig.update_layout(
    title_text='Sodium and Potassium Distribution',  # title of plot
    xaxis_title_text='Grams',
    yaxis_title_text='Count',
    bargap=0.1,  # gap between bars of adjacent location coordinates
    template='simple_white',  # choose from one of the pre-defined templates
)
#  Can call update_layout multiple times
fig.update_layout(legend=dict(yanchor="top", y=.74, xanchor="right", x=.99))

# add a vertical "target" line
fig.add_shape(
    type='line',
    line_color='gold',
    line_width=3,
    opacity=1,
    line_dash='dot',
    x0=100,
    x1=100,
    xref='x',
    y0=0,
    y1=15,
    yref='y'
    )

#  add a text callout with arrow
fig.add_annotation(
    text='USDA Target',
    xanchor='right',
    x=100,
    y=12,
    arrowhead=1,
    showarrow=True)

fig.show()
fig.write_image('plotly_exploration (potassium_sodium_plots).pdf')
