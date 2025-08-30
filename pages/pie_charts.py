import streamlit as st
import plotly.express as px
import pybaseball as pyb

st.title("Pie Charts")

plotly_config = {'displayModeBar': False}

# Team Batting Data from 2002
df_team_batting_2002 = pyb.team_batting(2002, 2002)

###############################################################################
# Standard Pie Chart

with st.container(border=True):

    st.write("Standard Pie Chart")

    fig_pie = px.pie(
        df_team_batting_2002, 
        values='HR', 
        names='Team', 
        title='2002 MLB Season Home Runs',
        subtitle='Percentage of League Home Runs'
    )

    st.plotly_chart(fig_pie, config=plotly_config)

    with st.expander("Code:"):
        
        fig_pie_code = '''
        fig_pie = px.pie(
            df_team_batting_2002, 
            values='HR', 
            names='Team', 
            title='2002 MLB Season Home Runs'
        )
        '''
        
        st.code(fig_pie_code, language="python")