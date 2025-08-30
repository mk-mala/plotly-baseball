# %%
import streamlit as st
import plotly.express as px
import pybaseball as pyb
import pandas as pd
import numpy as np

st.title("Line Charts")

plotly_config = {'displayModeBar': False}

# Game-by-game results from the 1952 season
df_schedule_and_record_2011_sea = pyb.schedule_and_record(2001, 'SEA')

df_schedule_and_record_2011_sea['Win'] = np.where(
    df_schedule_and_record_2011_sea['W/L'].str[0] == 'W',
    1,
    0,
)

df_schedule_and_record_2011_sea['Wins'] = df_schedule_and_record_2011_sea['Win'].cumsum()

###############################################################################
# Standard Line Chart

with st.container(border=True):

    st.write("Standard Line Chart")

    fig_line = px.line(
        df_schedule_and_record_2011_sea,
        x='Date',
        y='Wins',
        title='Most Wins in a Season',
        subtitle='2001 Seattle Mariners'
    )

    st.plotly_chart(fig_line, config=plotly_config)

    with st.expander("Code:"):
        
        fig_line_code = '''
        fig_line = px.line(
            df_schedule_and_record_2011_sea,
            x='Date',
            y='Wins',
            title='Most Wins in a Season',
            subtitle='2001 Seattle Mariners'
        )
        '''
        
        st.code(fig_line_code, language="python")
