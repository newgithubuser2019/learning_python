import pandas as pd
import streamlit as st
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
@st.cache()
def load_data():
    df = pd.read_csv(filename)
    return df


#  Read in the cereal data
df = load_data()

st.title('Rating exploration')

#  Only a subset of options make sense
x_options = [
    'calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars',
    'potass'
]

#  Allow user to choose
x_axis = st.sidebar.selectbox('Which value do you want to explore?', x_options)

#  plot the value
fig = px.scatter(
    df,
    x=x_axis,
    y='rating',
    hover_name='name',
    title=f'Cereal ratings vs. {x_axis}',
    )

st.plotly_chart(fig)
# streamlit run streamlit_exploration.py
