# MEHRA ROOMS NIGHT

from selenium import webdriver
#object of ChromeOptions class
o = webdriver.ChromeOptions()
#adding specific Chrome Profile Path
# o.add_arguments = {'user-data-dir:C:\Users\mmt9642\AppData\Local\Google\Chrome\User Data\Profile 1'}
o.add_argument('--profile-directory=Profile 1')

driver = webdriver.Chrome('c:\Python\selenium\chromedriver.exe')

url_mehra = 'https://redash.goibibo.com/queries/44870/source?p_Start%20Date=2022-05-01&p_End%20Date=2022-05-02'
url_gmail = "https://mail.google.com/mail/u/0/#inbox"
driver.get(url_gmail)

