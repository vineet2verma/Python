file = "C:\Users\mmt9642\Desktop\pankaj\rm_Base__html_file.html"
# file = 'c:\\Python\\Redash working\\RRR\\three - Copy.html'

# lst_month = 10
# last_m_name = "Oct"
# Curr_month = 11
# today_m_name = "Nov"

# b = [lst_month,last_m_name,Curr_month,today_m_name]
# c = []
# for i in b:
#     c.append(f"<th>{i}</th>")

with open(file, "r") as f:
    a = f.read()
    f.close()
with open(file, "w") as f2:
    f2.write(a.replace('C:\Users\mmt9642\Desktop\pankaj\rm_Base__html_file.html',''))
    # f2.write(a.replace(c[0],c[1]).replace(c[2],c[3]))
    f2.close()


# c:\Python\Redash working\RRR\three.html