import streamlit as st

st.set_page_config(
    page_title="Plotly Baseball", 
    page_icon="⚾", 
    layout="wide",
)

# Home Page
home_page = st.Page("pages/home.py", title="Home")

# App Pages
bar_charts = st.Page("pages/bar_charts.py", title="Bar Charts")
line_charts = st.Page("pages/line_charts.py", title="Line Charts")
scatter_plots = st.Page("pages/scatter_plots.py", title="Scatter Plots")
pie_charts = st.Page("pages/pie_charts.py", title="Pie Charts")
bubble_charts = st.Page("pages/bubble_charts.py", title="Bubble Charts")

pg = st.navigation([
    home_page,
    bar_charts,
    line_charts,
    scatter_plots,
    pie_charts,
    bubble_charts
])

pg.run()