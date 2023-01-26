import pandas as pd
import streamlit as st



salary_file = 'C:\\Users\\Owner\\Desktop\\testing heavy data\\Salary Prediction based on Position and Experience.csv'

df1 = pd.read_csv(salary_file)

print(df1)