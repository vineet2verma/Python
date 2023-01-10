import pandas as pd

filename = "text1.csv"
header = ['Name','Mobile']
data = [["one",1],["two",],["ten",10],['three',3],['four',4],["five",5],["six",6],["eight",8],["nine",9]]

aa = pd.DataFrame(data,columns=header)
# print(aa.sort_values(by=['Mobile'],ascending=True))

print(max(aa))
print(min(aa))
# print( aa[:4] )

 