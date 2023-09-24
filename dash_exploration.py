import sys

import dash
import pandas as pd
# import dash_bootstrap_components as dbc  # separate module - should be installed
import plotly.graph_objs as go
from dash import dcc, html

pd.set_option('display.max_rows', 1500)
pd.set_option('display.max_columns', 100)
pd.set_option('max_colwidth', 16)
pd.set_option('expand_frame_repr', False)

# -------------------------------------------------------------------------------------------
df = pd.read_excel("https://github.com/chris1610/pbpython/blob/master/data/salesfunnel.xlsx?raw=True")
# print(df)
pv = pd.pivot_table(df, index=['Name'], columns=["Status"], values=['Quantity'], aggfunc=sum, fill_value=0)
# print(pv)

app = dash.Dash()
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
"""
trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'declined')], name='Declined')
trace2 = go.Bar(x=pv.index, y=pv[('Quantity', 'pending')], name='Pending')
trace3 = go.Bar(x=pv.index, y=pv[('Quantity', 'presented')], name='Presented')
trace4 = go.Bar(x=pv.index, y=pv[('Quantity', 'won')], name='Won')

app.layout = html.Div(children=[
    html.H1(children='Sales Funnel Report'), # заголовок
    html.Div(children='''National Sales Funnel Report.'''), # подзаголовок
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2, trace3, trace4],
            'layout': go.Layout(title='Order Status by Customer', barmode='stack')
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)
"""

mgr_options = df["Manager"].unique()  # this is ndarray
managers_list = df["Manager"].tolist()
managers_list.append("All Managers")
managers_list = set(managers_list)
# print(managers_list)
# sys.exit()

app.layout = html.Div([
    html.H2("Sales Funnel Report"),
    html.Div(
        [dcc.Dropdown(id="Manager", options=[{'label': i, 'value': i} for i in managers_list], value='All Managers')],
        # [dcc.Dropdown(id="Manager", options=[{'label': i, 'value': i} for i in managers_list])], - this does not work
        style={'width': '25%', 'display': 'inline-block'}
        ),
    dcc.Graph(id='funnel-graph'),
])


@app.callback(
    dash.dependencies.Output('funnel-graph', 'figure'),
    [dash.dependencies.Input('Manager', 'value')])
def update_graph(Manager):
    if Manager == "All Managers":
        df_plot = df.copy()
    else:
        df_plot = df[df['Manager'] == Manager]
    #
    pv = pd.pivot_table(
        df_plot,
        index=['Name'],
        columns=["Status"],
        values=['Quantity'],
        aggfunc=sum,
        fill_value=0)
    #
    trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'declined')], name='Declined')
    trace2 = go.Bar(x=pv.index, y=pv[('Quantity', 'pending')], name='Pending')
    trace3 = go.Bar(x=pv.index, y=pv[('Quantity', 'presented')], name='Presented')
    trace4 = go.Bar(x=pv.index, y=pv[('Quantity', 'won')], name='Won')
    #
    return {
        'data': [trace1, trace2, trace3, trace4],
        'layout': go.Layout(title='Customer Order Status for {}'.format(Manager), barmode='stack')
    }


if __name__ == '__main__':
    app.run_server(debug=True)
# python dash_exploration.py
