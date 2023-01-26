# %% Data Frame
import pandas as pd
import streamlit as st

file = "c:\\Users\\Owner\\Desktop\\testing heavy data\\3.1-data-sheet-udemy-courses-business-courses.csv"
df1 = pd.read_csv(file)

# %% Columns
print(df1.columns)

# %% head 1 only
df1.head(1)

# %% function
def remove_f(val):
    val = val[1:]
    return val
def remmove_l(val):
    val = val[:-1]
    return val

# %% 
df1['num_subscribers'] = df1['num_subscribers'].apply(remove_f)
df1['Rating']= df1['Rating'].apply(remmove_l)

# %%
# df1.drop("url",axis=1,inplace=True).head(3)
df1.head()
# %%
# %%
# %%
# %%
# %%
# %%


