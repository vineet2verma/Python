import py_compile
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

file1 = "C:\\Users\\Owner\\Desktop\\TEST\\ecommercedata\\E-commerce data.xlsx"
df = pd.read_excel(file1,engine="openpyxl")

st.set_page_config(layout="wide")

st.sidebar.header("Please Filter Here")

city = st.sidebar.multiselect(
    "Select City",
    options=df['City'].unique(),
    default=df['City'].unique(),
    )

Region = st.sidebar.multiselect(
    "Select Region Name",
    options=df['Region'].unique(),    
    default=df['Region'].unique(),
)

df_selection = df.query(
    "City == @city & Region==@Region"
)

# For Showing Data Frame
# st.dataframe(df_selection) 

df_city = df_selection.groupby(['City'])['Region'].count().reset_index()

fig_city = px.bar(
    df_city,
    x='City',y='Region',
    title="City Vs Region Level Grouping"
    )
st.plotly_chart(fig_city)


# Hide Header, Footer, MainMenu
hide ="""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>

"""
st.markdown(hide,unsafe_allow_html=True)