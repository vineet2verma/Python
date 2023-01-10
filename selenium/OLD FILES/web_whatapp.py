from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path= "d:\\Python\\selenium\\chromedriver.exe")

# driver = webdriver.ChromeOptions()
driver.add_argument('--user-data-dir=C:/Users/Owner/AppData/Local/Google/Chrome/User Data')
# driver.add_argument('--profile-directory=Profile 1')
driver = webdriver.Chrome(options=driver)

# Replace below path with the absolute path
# to chromedriver in your computer
# ch_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# driver = webdriver.Chrome(executable_path="c://Python//selemium//chromedriver.exe")
# driver = webdriver.Chrome(executable_path=ch_path)


driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = '"Group01"'

# Replace the below string with your own message
string = "Message sent using Python!!!"



x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
input_box = wait.until(EC.presence_of_element_located((
	By.XPATH, inp_xpath)))
for i in range(100):
	input_box.send_keys(string + Keys.ENTER)
	time.sleep(1)
