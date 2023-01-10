import xlwings as xw

file_source = 'c:\\CHKING\\Neo_Chain_.csv'
file_dest = 'c:\\CHKING\\bin_excel_.xlsb'


f_dest = xw.Book(file_dest)
f_dest.activate()
f_dest.sheets('Sheet1').range(cell)




# print("\n Vlookup - Merging Process Done...\n ")

# wb = openpyxl.load_workbook(file_path)
# sh_raw = wb['Raw_File']
# maxrow = (sh_raw.max_row)
# maxcol = (sh_raw.max_column)

# print(f'Max Rows  :-  {maxrow}' )
# print(f'Max Columns :-  {maxcol}' )

# for r in sh_raw['A2:Q'+ str(maxrow)]:
#     for c in r:
#         c.value = None
# wb.save(file_path)

# print('\n Cleaning Done... \n')

# wwb = xw.Book(file_path)
# ssh = wwb.sheets['Raw_File']
# ssh['A2'].value = df3.values
# wwb.save()
# wwb.close()
# print('Data Paste Done')

# excel = client.Dispatch('Excel.Application')
# wb = excel.Workbooks.Open(workbook_path)
# print('\nRefreshing 2nd Excel Process Start..\n\n')
# sh2 = wb.Sheets['Raw_File']
# wb.RefreshAll()
# excel.CalculateUntilAsyncQueriesDone()
# wb.Save()
# sheet = wb.Sheets[sh_name1]

# copyrange= sheet.Range(copy_range1)
# copyrange.CopyPicture(Appearance=1, Format=2)
# ImageGrab.grabclipboard().save('paste.png')
# wb.Save()
# excel.Quit()
# img_path = os.getcwd() + '\\paste.png'

# print('Refresh Done & Save\n\n')
# date_str = dt.datetime.now().strftime("%d-%b-%y %I:%M:%S %p")
# strFrom = user_name[1]
# strTo = mainsend
# strBcc = strBcc
# msgRoot = MIMEMultipart('related')
# msgRoot['Subject'] = 'Neo Chain Room Night Trend '
# msgRoot['From'] = strFrom
# msgRoot['To'] =  ",".join(strTo)
# msgRoot['Cc'] = ",".join(strBcc)

# msgRoot.preamble = 'Multi-part message in MIME format.'
# msgAlternative = MIMEMultipart('alternative')
# msgRoot.attach(msgAlternative)
# msgText = MIMEText('Alternative plain text message.')
# msgAlternative.attach(msgText)

# msgText = MIMEText('''
# Hi,<br>
# Please find the attached <b style="color:red"> Top Neo Chain</b> production synopsis. <br>
# <div style="color:blue">This is an automated report</div>

# <img src="cid:image1"><br><br>

# <br><br>
# <p>Thanks & Regards,<br>
# Vineet Verma</p>
# ''', 'html')
# msgAlternative.attach(msgText)

# if F_attach == "Yes":
#     file_path = file_path
#     fileename = file_path.split("\\")[-1]
#     part = MIMEBase('application', "octet-stream")
#     part.set_payload(open(file_path, "rb").read())
#     encoders.encode_base64(part)
#     part.add_header('Content-Disposition', 'attachment; filename="%s"' %(fileename))
#     msgRoot.attach(part)

# fp = open('C:\\Reporting\\Neo Chains\\paste.png', 'rb')
# msgImage = MIMEImage(fp.read())
# fp.close()
# msgImage.add_header('Content-ID', '<image1>')
# msgRoot.attach(msgImage)
# smtp = smtplib.SMTP('smtp.outlook.office365.com', 587)
# smtp.starttls()
# smtp.login(user_name[1],paswd[0])
# smtp.sendmail(strFrom, (strTo+strBcc), msgRoot.as_string())
# del temp
# smtp.quit()