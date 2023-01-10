import pandas as pd

file1 = 'C:\\CHKING\\Pratice_folder\\student.csv'
file2 = 'c:\CHKING\Pratice_folder\max score.csv'
student = pd.read_csv(file1,encoding="unicode_escape")
score = pd.read_csv(file2,encoding="unicode_escape")


df3 = student.merge(score,how="left",on="First Name",)
print(df3.columns)
# print(df3[['FIRST name'.title(),'last name'.title()]])

