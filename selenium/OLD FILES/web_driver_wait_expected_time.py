from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="c:\Python\selenium\chromedriver.exe")
driver.get("https://masterprograming.com/")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "site-navigation"))
    )
    print("Jab Website Ka Navigation Load Ho Gaya To Me Exit Ho Gaya Hu.... hahaha ")
finally:
    driver.quit()