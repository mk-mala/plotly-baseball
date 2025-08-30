import streamlit as st
import plotly.express as px
import pybaseball as pyb

st.title("Bar Charts")

plotly_config = {'displayModeBar': False}

# Team Batting Data from 2000-2004
df_team_batting = pyb.team_batting(2000, 2024)

df_angels = df_team_batting[df_team_batting['Team'] == 'LAA']

###############################################################################
# Standard Bar Chart

with st.container(border=True):

    st.write("Standard Bar Chart")

    fig_bar = px.bar(
        df_angels,
        x='Season',
        y='HR',
        title='Los Angeles Angels',
        subtitle='2000-2024 Team Home Runs',
    )

    st.plotly_chart(fig_bar, config=plotly_config)

    with st.expander("Code:"):
        
        fig_bar_code = '''
        fig_bar = px.bar(
            df_angels,
            x='Season',
            y='HR',
            title='Los Angeles Angels',
            subtitle='2000-2024 Team Home Runs',
        )
        '''
        
        st.code(fig_bar_code, language="python")
