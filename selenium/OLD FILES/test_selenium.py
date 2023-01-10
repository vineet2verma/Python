import undetected_chromedriver
from selenium import webdriver  
import time

options = webdriver.ChromeOptions()
profile = "C:\\Users\\Owner\\AppData\\\Local\\Google\\Chrome\\User Data\\Profile 1"
options.add_argument(f"user-data-dir={profile}")
driver = webdriver.Chrome(options=options)
driver.get("https://masterprograming.com/")

time.sleep(10000)