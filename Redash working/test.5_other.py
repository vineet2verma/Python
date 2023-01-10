# importing pandas library
# import pandas as pd

# # creating dataframe
# df = pd.DataFrame({'Name': ['John', 'Sammy', 'Stephan', 'Joe', 'Emily', 'Tom'],
# 				'Gender': ['Male', 'Female', 'Male',
# 							'Female', 'Female', 'Male'],
# 				'Age': [45, 6, 4, 36, 12, 43]})
# print("Dataset")
# print(df)
# print("-"*40)

# # categorizing in age groups
# def age_bucket(age):
# 	if age <= 18:
# 		return "<18"
# 	else:
# 		return ">18"

# df['Age Group'] = df['Age'].apply(age_bucket)

# print(df)
# print("-"*40)



# calculating gender percentage
# gender = pd.DataFrame(df.Gender.value_counts(normalize=True)*100).reset_index()
# gender.columns = ['Gender', '%Gender']
# df = pd.merge(left=df, right=gender, how='inner', on=['Gender'])

# creating pivot table
# table = pd.pivot_table(df, index=['Gender', '%Gender', 'Age Group'],
# 					values=['Name'], aggfunc={'Name': 'count',})

# display table
# print("Table")
# print(table)


# importing required libraries
import pandas as pd
import matplotlib.pyplot as plt

# creating dataframe
df = pd.DataFrame({
	'Name': ['John', 'Emily', 'Smith', 'Joe'],
	'Gender': ['Male', 'Female', 'Male', 'Female'],
	'Salary(in $)': [20, 40, 35, 28]})

df = df.groupby(['Name','Gender'],as_index=True)['Salary(in $)'].sum().to_frame().reset_index().sort_values('Salary(in $)', ascending=False)
print(df)
df2 = df.pivot_table(index='Name',columns='Gender')
print(df2)

# print("Dataset")
# print(df)
# print("-"*40)

# # creating pivot table
# table = pd.pivot_table(df, index=['Gender', 'Name'])

# # calculating percentage # Contribution
# table['% Income'] = (table['Salary(in $)']/table['Salary(in $)'].sum()*100).round().astype(str)+" %"

# # display table
# print("Pivot Table")
# print(table)
