# %%
import streamlit as st
import plotly.express as px
import pybaseball as pyb

st.title("Dot Plots")

plotly_config = {'displayModeBar': False}

# Team Batting Data from 2024
df_team_batting_2024 = pyb.team_batting(2024, 2024)

ls_american_league = ['NYY', 'BAL', 'BOS', 'TBR', 'TOR'
                      'CLE', 'KCR', 'DET', 'MIN', 'CHW',
                      'HOU', 'SEA', 'TEX', 'OAK', 'LAA']

df_team_batting_2024_al = df_team_batting_2024[
    df_team_batting_2024['Team'].isin(ls_american_league)
]

###############################################################################
# Standard Dot Plots

with st.container(border=True):

    st.write("Standard Dot Plots")

    fig_dot = px.scatter(
        df_team_batting_2024_al.sort_values(by=['SB'], ascending=True),
        y="Team",
        x="SB",
        title="American League Stolen Bases",
        subtitle="2024 MLB Season"
    )

    st.plotly_chart(fig_dot, config=plotly_config)

    with st.expander("Code:"):
        
        fig_dot_code = '''
        fig_dot = px.scatter(
            df_team_batting_2024_al.sort_values(by=['SB'], ascending=True),
            y="Team",
            x="SB",
            title="American League Stolen Bases",
            subtitle="2024 MLB Season"
        )
        '''
        
        st.code(fig_dot_code, language="python")
