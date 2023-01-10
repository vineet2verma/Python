# https://www.kaggle.com/datasets/wenruliu/adult-income-dataset

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

file1 = 'C:\\Users\\mmt9642\\Desktop\\pandas testing\\adult.csv'
df = pd.read_csv(file1)

# In this project, we will discuss:
# - How to fetch random samples from the Dataset?
# - isin
# - between
# - unique
# - dropna
# - replace
# - duplicated
# - drop_duplicates
# - astype
# - apply
# - What is Univariate analysis?
# - What is Bivariate analysis?
# - Memory Optimization

# Questions :
# 1.Display Top 10 Rows of The Dataset
# print(df.head(10))

# 2. Check Last 10 Rows of The Dataset
# print(df.tail(10))

# 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
# print(df.shape)

# 4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
# print(df.describe())

# 5. Fetch Random Sample From the Dataset (50%)
# print(df.sample(frac=.50))

# 6.Check Null Values In The Dataset
# print(df.isnull().sum(axis=1))
# print(sns.heatmap(df.isnull()))

# 7.Perform Data Cleaning [ Replace '?' with NaN ]
# print(df.tail(30).replace('?',np.nan))
# df['workclass','occupation'].replace('?',np.nan,inplace=True)
# print(df.isin(['?']).sum())

# 8. Drop all The Missing Values

# 9. Check For Duplicate Data and Drop Them