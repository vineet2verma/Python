import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import openpyxl, time
from datetime import datetime

file = "d:\\RAW_DATA\\Book1.csv"
df = pd.read_csv(file)

col = ['date', 'hotelcode', 'hotelname','checkin', 'RNs','month']
df1 = df[['hotelcode', 'hotelname','checkin', 'RNs']]

# https://www.youtube.com/watch?v=QlgcQ-OwQ4M&t=567s


    # 1.Display Top 10 Rows of The Dataset
    # 2. Check Last 10 Rows of The Dataset
    # 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
# print(df1.shape)
    # 4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
# print(df1.info())
    # 5. Fetch Random Sample From the Dataset (50%)

    # 6.Check Null Values In The Dataset
# print(df1.isnull().sum())
# 7.Perform Data Cleaning [ Replace '?' with NaN ]
# df1['month'] = df1['month'].replace(2,5)
    # 8. Drop all The Missing Values

    # 9. Check For Duplicate Data and Drop Them
# df1 = df1['hotelcode'].drop_duplicates()
 
# 10. Get Overall Statistics About The Dataframe

# 11. Drop The Columns education-num, capital-gain, and capital-loss
# print(df1.columns)
# df1 = df1.drop(['RNs','checkin'],axis=1)
# print(df1.columns)

    # 12. What Is The Distribution of Age Column?
# print(df1['hotelcode'].describe())

    # 13. Find Total Number of Persons Having Age Between 17 To 48 (Inclusive) Using Between Method
# print(df1['RNs'].value_counts())
# df1 = df1.loc[(df1['RNs']>2) & (df1["RNs"]<10)]
# print(df1['RNs'].value_counts())

# 14. What is The Distribution of Workclass Column?

# 15. How Many Persons Having Bachelors and Masters Degree?
# print(df1[df1['hotelcode']==1000011031]['RNs'].sum())
# print(df1[df1['hotelcode'].isin([1000011031])]['RNs'].sum())

# 16. Bivariate Analsis

# 17. Replace Salary Values With 0 and 1
df1 = df1.groupby(['hotelcode','hotelname'])['RNs'].agg("sum").reset_index()
# df1 = df1.pivot(index='hotelcode',columns='checkin',values="RNs")
    
# 18. Which Workclass Getting The Highest Salary?
# print(df1['RNs'].max())

# 19.How Has Better Chance To Get Salary greater than 50K Male or Female?
# df1.plot(x='hotelname',y='RNs')

# print(df['RNs'].mean)

# df1['RNs'].plot(kind='bar',color='red')
# df1['RNs'].plot(kind='line',marker='*')
# plt.show()

# 20. Covert workclass Columns Datatype To Category Datatype


# Question

print( df1[ df1['RNs'] == df1 ['RNs'].max() ]['hotelcode'])

# 1. Display Top 5 Rows of The Dataset
# 2. Check the Last 3 Rows of The Dataset
# 3. Find Shape of Our Dataset (Number of Rows & Number of Columns)
# 4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
# 5. Get Overall Statistics About The Dataframe
# 6. Data Filtering

# 7.Check Null Values In The Dataset

# 8. Drop the Column

# 9. Handle Missing Values

# 10. Categorical Data Encoding   

# 11. What is Univariate Analysis?

# How Many People Survived And How Many Died?

# How Many Passengers Were In First Class, Second Class, and Third Class?

# Number of Male And Female Passengers

# 12. Bivariate Analysis

# How Has Better Chance of Survival Male or Female?

# Which Passenger Class Has Better Chance of Survival (First, Second, Or Third Class)? 

# 13. Feature Engineering