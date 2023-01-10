import datetime as date
import csv

    # Date 
curr_date = date.datetime.today().strftime("%Y_%m_%d %I:%M %p")

exp = -1
total = 0
filename = "text.csv"
stop = False

file = open(filename)
type(file)
header = []
print(next(file))

print(row(file))

for index,row in enumerate(file):
    print([index,row])





# with open(filename, "a",newline="") as f:
#     fieldnames = ["Date Time","Expenses"]
#     csvwriter = csv.writer(f)
#     csvwriter.writerow(fieldnames)
#     while stop !=True:
#         exp = int(input("\nEnter your exp\t"))
#         if exp == 0:
#             stop = True
#         else:
#             csvwriter.writerow([curr_date,exp])
#             total = total + exp

# print (f'Total is :- {total}')
# f.close()

    


    
    




