import streamlit as st
import plotly.express as px
import pybaseball as pyb

st.title("Scatter Plots")

plotly_config = {'displayModeBar': False}

# Team Batting Data from 2000-2004
df_team_batting = pyb.team_batting(1994, 2024)

df_dodgers = df_team_batting[df_team_batting['Team'] == 'LAD']

###############################################################################
# Standard Scatter Plot

with st.container(border=True):

    st.write("Standard Scatter Plot")

    fig_scatter = px.scatter(
        df_dodgers,
        x='OPS',
        y='HR',
        title='Los Angeles Dodgers',
        subtitle='Home Runs & On-Base Percentage',
    )



    st.plotly_chart(fig_scatter, config=plotly_config)

    with st.expander("Code:"):
        
        fig_scatter_code = '''
        fig_scatter = px.scatter(
            df_dodgers,
            x='OPS',
            y='HR',
            title='Los Angeles Dodgers',
            subtitle='Home Runs & On-Base Percentage',
        )
        '''
        
        st.code(fig_scatter_code, language="python")
