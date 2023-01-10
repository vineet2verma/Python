# https://www.kaggle.com/datasets/utkarsharya/ecommerce-purchases
from codecs import latin_1_decode
from itertools import count
from operator import index
import pandas as pd
file = 'C:\\Users\\mmt9642\\Desktop\\pandas testing\\Ecommerce Purchases.csv'
df = pd.read_csv(file)

li2 = []
# for a in df['AM or PM']:
#     if a == "AM":
#         li2.append("Night")
#     else:
#         li2.append("Day")
# df['test'] = li2

# print(df['test'].value_counts())


# df.to_excel("C:\\Users\\mmt9642\\Desktop\\pandas testing\\Ecommerce Purchases.xlsx")

# 1. Display Top 10 Rows of The Dataset
# print(df.head(10))

# 2. Check Last 10 Rows of The Dataset
# print(df.tail())

# 3. Check Datatype of Each Column
# print(df.dtypes)

# 4. Check null values in the dataset
# print((df.isnull().sum()))

# 5. How many rows and columns are there in our Dataset? 
# print(f"Columns {len(df.columns.value_counts())} ")
# print(f"Rows   {len(df)} ")

# 6. Highest and Lowest Purchase Prices.
# print(df['Purchase Price'].max())
# print(df['Purchase Price'].min())

# 7. Average Purchase Price
# print(df['Purchase Price'].mean())

# 8. How many people have French 'fr' as their Language?
# print( len(df[df['Language']=='fr']) )

# 9. Job Title Contains Engineer
# print( len(df[df['Job'].str.contains('engineer',case=False)] ))

# 10. Find The Email of the person with the following IP Address: 132.207.160.22
# print( df[ df['IP Address']=='30.250.74.19' ]['Email'] )

# 11. How many People have Mastercard as their Credit Card Provider and made a purchase above 50?
# print(  len(df[(df['CC Provider'] == 'Mastercard')  &  (df['Purchase Price'] > 50)] ) )

# 12. Find the email of the person with the following Credit Card Number: 4664825258997302
# print( df[df['CC Security Code'] == 7169 ]['Email'] )
print( df['CC Security Code'].isin(7169) )

# 13. How many people purchase during the AM and how many people purchase during PM?
# print(df['AM or PM'].value_counts())

# 14. How many people have a credit card that expires in 2020?
# def split_():
#     count = 0
#     li1 = []
#     for c in df['CC Exp Date']:
#             if c.split("-")[2] == "2020":
#                 count = count + 1
#     print(count)
# split_()
# print( len(df[df['CC Exp Date'].apply(lambda x:x.split("-")[2] == "2020" )]) )

# 15. What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...) 

# li1 = []
# for email in df['Email']:
#     li1.append(email.split("@")[1])
    
# df['out'] = li1 
# print(df['out'].value_counts())
