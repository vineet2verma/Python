# import library
import pandas as pd

# create a Dataframe
df = pd.DataFrame({
'height' : [165, 165, 164,
			158, 167, 160,
			158, 165],
	
'weight' : [63.5, 64, 63.5,
			54, 63.5, 62,
			64, 64],
	
'age' : [20, 22, 22,
		21, 23, 22,
		20, 21]},
	
index = ['Steve', 'Ria', 'Nivi',
			'Jane', 'Kate', 'Lucy',
			'Ram', 'Niki'])

df2 = pd.DataFrame({'index' :['AA', 'BB', 'CC',
			'AA', 'DD', 'EE','BB', 'CC']})

# counting unique values
# n = df['age']
# n = len(pd.unique(df['height']))
# print("No.of.unique values :",n)

l1 = df2['index'].unique()
print(    len(l1)    )

with open("c:\\Python\\Redash working\\rrr\\bdm_name.txt","a+") as f:
    for x in range(len(l1)):
        f.write(f"\n{l1[x]}")

with open("c:\\Python\\Redash working\\rrr\\bdm_name.txt","a+") as f:
    for x in range(len(l1)):
        f.write(    f"\n{l1[x]}\t {}    ")