# PANDAS EXCEL VLOOKUP FUNCTION 
# CONDITION / FILTER
# COLUMNS SELECTION AS PER REQ.

from turtle import left
from matplotlib.pyplot import axis
from matplotlib.style import use
import pandas as pd
from pandas import DataFrame, read_excel, merge

#  FILE PATH
ex1 = "c:\CHKING\INDEX_MATCH\MASTER.xlsx"
ex2 = "c:\CHKING\INDEX_MATCH\HOTEL_NAME.xlsx"
# Read Excel
wb1 = read_excel(ex1,sheet_name="ID")
wb2 = read_excel(ex2,sheet_name="NAMES")

# VLOOKUP FUNCTION 
df3 = pd.merge(
left = wb1,
right = wb2,
left_on='HOTEL ID',
right_on= "ID_S",
how="inner"
)

# COLUMNS SELECTION AS PER REQ.
df4 = df3[["HOTEL ID","MOB"]]

# CONDITION / FILTER
print(
    df3[df3["MOB"]>=99999005] 
)

