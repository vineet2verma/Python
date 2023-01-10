from numpy import dtype
import pandas as pd
from pyparsing import col

#  how to create empty data frame

aa = pd.DataFrame()
li1 = [1,2,3,4,5]
li2 = ['a',"b","c"]
dic0 = ['Name','Number']
dic1 = [{"a":1,"b":2,"c":''},{"b":4,"a":5}]
dic2 = {'a':[11],'e':[88]}

# df1 = pd.DataFrame(dic1)
# print(df1)  

    # HOW TO SET COLUMN NAME BY LIST AND ROW BY LIST /  DIC
print(pd.DataFrame(dic1,columns=li2).dropna())
