# %%
import streamlit as st
import plotly.express as px
import pybaseball as pyb

st.title("Bubble Charts")

plotly_config = {'displayModeBar': False}

# Team Batting Data from 2024
df_team_batting_2024 = pyb.team_batting(2024, 2024)

###############################################################################
# Standard Bubble Chart

with st.container(border=True):

    st.write("Standard Bubble Chart")

    fig_bubble = px.scatter(
        df_team_batting_2024,
        x="WAR",
        y="SLG",
        size="SB",
        color="Team",
        title="Slugging Drives Wins Above Replacement",
        subtitle="2024 Season"
    )

    st.plotly_chart(fig_bubble, config=plotly_config)

    with st.expander("Code:"):
        
        fig_bubble_code = '''
        fig_bubble = px.scatter(
            df_team_batting_2024,
            x="WAR",
            y="SLG",
            size="SB",
            color="Team",
            title="Slugging Drives Wins Above Replacement",
            subtitle="2024 Season"
        )
        '''
        
        st.code(fig_bubble_code, language="python")
