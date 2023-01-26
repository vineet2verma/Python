import pandas as pd
import lxml, html5lib


file = "c:\\Users\\Owner\\Desktop\\testing heavy data\\3.1-data-sheet-udemy-courses-business-courses.csv"

df1 = pd.read_csv(file)

print(df1.columns)
print(df1.shape)
print(df1)