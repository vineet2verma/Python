from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\Python\selenium\chromedriver.exe")
driver.implicitly_wait(10) # seconds
driver.get("https://masterprograming.com/")
myDynamicElement = driver.find_element_by_id("site-navigation")
print("Bhai Sab Kuch Sahi Hai....")

driver.quit()