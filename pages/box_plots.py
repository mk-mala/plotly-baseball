import streamlit as st
import plotly.express as px
import pybaseball as pyb

st.title("Box Plots")

plotly_config = {'displayModeBar': False}

df_team_batting_2019 = pyb.team_batting(2000, 2010)

###############################################################################
# Standard Box Plot

with st.container(border=True):

    st.write("Standard Box Plot")

    fig_box = px.box(
        df_team_batting_2019,
        x="Team",
        y="OPS"
    )

    st.plotly_chart(fig_box, config=plotly_config)

    with st.expander("Code:"):
        
        fig_box_code = '''

        '''
        
        st.code(fig_box_code, language="python")