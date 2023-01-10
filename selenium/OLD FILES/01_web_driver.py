# Open Website
# Maximize Window
# Minimize Window

import time 
from selenium import webdriver  
import os
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="d:\\Python\\selenium\\chromedriver.exe")
# driver.add_argument('--user-data-dir=C:/Users/Owner/AppData/Local/Google/Chrome/User Data')
# driver.add_argument('--profile-directory=Profile 1')

driver.get("https://masterprograming.com/")

# Get Website title
print(driver.title)

# Minimize Window
# driver.minimize_window()

# Maximize Window
driver.maximize_window()

# write script 
script = "alert('Welcome To MasterPrograming')"

# generate a alert via javascript 
# driver.execute_async_script(script)


# driver.quit() 