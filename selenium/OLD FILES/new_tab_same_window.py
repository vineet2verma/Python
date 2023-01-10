# 
#
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path= "c:\\Python\\selenium\\chromedriver.exe")  #create object

# get 
url1 = "https://www.google.com/"
url2 = "https://masterprograming.com/"
# open url1 in brower window
driver.get(url1)
# open new tab in same open window
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
# open url in new window
driver.get(url2) 



