
import pandas as pd
import seaborn as sns

file1 = 'c:\\Python\\output.xlsx'
df = pd.read_excel(file1,skiprows=2)

# Remove Row as per index no. & Rename it.
df = df.rename(columns={"day":"RM_Name"}).dropna()
print(df)

pic1 = sns.lineplot(df,x='RM_Name',y=
# print(pic1)
sns.show()

