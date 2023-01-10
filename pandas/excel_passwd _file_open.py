
file1 = "C:\Python\REPORT_EXE\Mehra_Report_Automation\mail_info.xlsx"
import msoffcrypto
import io
import pandas as pd

password = ' '
temp = io.BytesIO()
with open(file1, 'rb') as f:
    excel = msoffcrypto.OfficeFile(f)
    excel.load_key(password)
    excel.decrypt(temp)
df = pd.read_excel(temp)
username = df.iloc[0][0]
password = df.iloc[0][1]
del temp
