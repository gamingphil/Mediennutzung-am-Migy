import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

from random import seed
from random import randint
seed(1)
ageint = randint(10, 18) 

def exception():
    driver.quit()
    print("An error occured. Press Ctrl + C to stop alarm.")
    time.sleep(10)
    exit()

PATH = ".\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver = webdriver.Chrome(PATH, options=chrome_options)

driver.get("https://umfragen.schule-bw.de/index.php/855125?lang=de")

### P1 ###

try:
    buttonP1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ls-button-submit"))
    )
except:
    exception()
buttonP1.click()

#age
age = driver.find_element_by_id("answer855125X5484X55002")
age.send_keys(str(ageint))

#gender
genderint = randint(0, 2)
if genderint == 0:
    driver.find_element_by_id("answer855125X5484X55010A2").click() #male
elif genderint == 1:
    driver.find_element_by_id("answer855125X5484X55010A1").click() #female
elif genderint == 2:
    driver.find_element_by_id("answer855125X5484X55010A3").click() #diverse

driver.find_element_by_id("ls-button-submit").click()

### P2 ###
    

# driver.quit()
# print("Login successful")
# time.sleep(3)