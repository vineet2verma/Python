from selenium import webdriver

driver = webdriver.Chrome(executable_path= "c:\\Python\\selemium\\chromedriver.exe")
# driver = webdriver.Chrome(executable_path= "D:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://masterprograming.com/contact-us/")

var = driver.find_element_by_name("email")
print(var.is_displayed())  
print(var.is_enabled())