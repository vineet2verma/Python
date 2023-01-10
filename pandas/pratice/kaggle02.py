from itertools import count
import pandas as pd
import openpyxl
import numpy as np

file = 'C:\\Users\\mmt9642\\Desktop\\pandas testing\\ecommerce Purchases.csv'
df = pd.read_csv(file)

# Questions are as follows.
# 1. Display Top 10 Rows of The Dataset
# print(df.head(10))

# 2. Check Last 10 Rows of The Dataset
# print(df.tail(10))

# 3. Check Datatype of Each Column
# print(df.dtypes)

# 4. Check null values in the dataset
# print(df.isnull().sum())

# 5. How many rows and columns are there in our Dataset? 
# print(df.shape)
# print(len(df))
# print(len(df.columns))
# print(df.info)
# 6. Highest and Lowest Purchase Prices.
# print(df['Purchase Price'].max())
# print(df['Purchase Price'].min())

# 7. Average Purchase Price
# print(df['Purchase Price'].mean())

# 8. How many people have French 'fr' as their Language?
# print(len(df[df['Language'] == 'fr']))
# print(len(df[df['Language'].str.contains('fr')]))

# 9. Job Title Contains Engineer
# print(len(df[df['Job'].str.contains('Engineer',case=False)]))

# 10. Find The Email of the person with the following IP Address: 132.207.160.22
# print(df[df['IP Address'] == '132.207.160.22']['Email'] )

# 11. How many People have Mastercard as their Credit Card Provider and made a purchase above 50?
# print(len(df[(df['CC Provider'] == 'Mastercard') & (df['Purchase Price']>50)]))

# 12. Find the email of the person with the following Credit Card Number: 4664825258997302
# print( df[df['Credit Card']==4664825258997302]) 

# 13. How many people purchase during the AM and how many people purchase during PM?
# print( df['AM or PM'].value_counts())

# 14. How many people have a credit card that expires in 2020?
# def fun():
#     count = 0
#     for dd in df['CC Exp Date']:
#         if(dd.split('-')[2] == '2020'):
#             count += 1
#     print(count)
# fun()

# 15. What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...) 
li1=[]
for dd in df['Email']:  li1.append(dd.split('@')[1])
df['temp']=li1
print(df['temp'].value_counts().head())

