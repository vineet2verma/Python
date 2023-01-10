from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

exe_path = "d:\\Python\\selenium\\chromedriver.exe"
driver = webdriver.Chrome(executable_path= "D:\\Python\\selenium\\chromedriver.exe")  #create object

# driver = webdriver.ChromeOptions()
# driver.add_argument('--user-data-dir=C:/Users/Owner/AppData/Local/Google/Chrome/User Data')
# driver.add_argument('--profile-directory=Profile 1')
# driver = webdriver.Chrome(options=driver)

# from pathlib import Path
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver_path = "D:\\Python\\selenium\\chromedriver.exe"
user_data_dir = r"C:/Users/Owner/AppData/Local/Google/Chrome/User Data"

options = webdriver.ChromeOptions()
# TELL WHERE IS THE DATA DIR
options.add_argument("--user-data-dir={}".format(user_data_dir))
# USE THIS IF YOU NEED TO HAVE MULTIPLE PROFILES
options.add_argument('--profile-directory=Profile 1')
driver = webdriver.Chrome(options=options)
driver.get("https://google.com/")



# # get 
# driver.get("https://www.google.com/") 
# print(driver.title)
# time.sleep(5)
# driver.get("https://masterprograming.com/") 
# print(driver.title)
# driver.back()
# print(driver.title)
# driver.forward()
# time.sleep(4)
# driver.quit()