import time
from selenium import webdriver
import getpass
from selenium.webdriver.chrome.options import Options

# ---------------------------------INPUT FEILDS----------------------- 
print("Select Your Option ?")
select_type = int(input("1. Only Messages \n2. Only Messages And Images \nEnter :"))

msg = input("Enter Messages : ") 
phone_list = ["919999996745","919999371596"] #Enter Your Own Nuber List

if select_type == 2:
    file_path = input("Enter Image Path :")

# --------------------------ADVANCED SETTINGS--------------------------
options = Options()
options.add_argument(f"--user-data-dir=C:/Users/{getpass.getuser()}/AppData/Local/Google/Chrome/User Data/Default")
options.add_argument("--profile-directory=Default")
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
# options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu/')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
options.add_argument('--hide-scrollbars')
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option("useAutomationExtension",False)


# ------------------------START HERE ------------------------------
#Start Here
browser = webdriver.Chrome(options=options)
browser.get('https://web.whatsapp.com/')
browser.maximize_window()
time.sleep(15)
val = select_type

# -----------------------------ONLY MESSAGES------------------------------
if val == 1 or val == 0:
    print("Running......")
    for i in phone_list:
        browser.get(f'https://api.whatsapp.com/send?phone={i}&text={msg}')
        time.sleep(5)
        browser.find_element_by_xpath("//*[@id='action-button']").click()
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='fallback_block']/div/div/a").click()
        time.sleep(20)
        try:
            if browser.find_element_by_xpath('//div[@data-animate-modal-popup="true"]'): 
                browser.find_element_by_xpath('//div[@role="button"]').click()
                print(f"Invalid Number : {i}" + '\n')
                pass  
                
        except Exception as e:
            time.sleep(2)
            browser.find_element_by_xpath('//span[@data-icon="send"]').click()
            time.sleep(2)
            print(f"Successfully Send Msg : {i}" + '\n')
            time.sleep(5)

    print("Finish Task... \n")
    browser.quit()        


# -----------------------------ONLY MESSAGES AND IMAGES------------------------------
if val == 2:
    print("Running......")
    for i in phone_list:
        browser.get(f'https://api.whatsapp.com/send?phone={i}&text={msg}')
        time.sleep(5)
        browser.find_element_by_xpath("//*[@id='action-button']").click()
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='fallback_block']/div/div/a").click()
        time.sleep(20)
        try:
            if browser.find_element_by_xpath('//div[@data-animate-modal-popup="true"]'): 
                browser.find_element_by_xpath('//div[@role="button"]').click()
                print(f"Invalid Number : {i}" + '\n')
                pass  
                
        except Exception as e:
            time.sleep(2)
            attachment_section = browser.find_element_by_xpath('//div[@title = "Attach"]')
            attachment_section.click()
            image_box = browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            image_box.send_keys(file_path)
            time.sleep(3)
            send_button = browser.find_element_by_xpath('//span[@data-icon="send"]')
            send_button.click()
            time.sleep(2)
            print(f"Successfully Send Msg : {i}" + '\n')
            time.sleep(5)
    print("Finish Task... \n")
    browser.quit()