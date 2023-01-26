import py_compile
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Registration Form Demo

st.title("Registration Form")

first,last = st.columns(2)
first.text_input("First Name")
last.text_input("Last Name")

email,mob = st.columns([3,1])
email.text_input("Email ID")
mob.text_input("Mobile")

username,ps1,ps2 = st.columns(3)
username.text_input("User Name")
ps1.text_input("Password",type="password")
ps2.text_input("Re Confirm Password",type="password")

ch,ch2,sub = st.columns(3)
ch.radio("Selection :",("I Agree","Don't Agree"))
sub.button("Submit")
