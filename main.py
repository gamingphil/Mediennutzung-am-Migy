import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

from random import randint

def exception():
    driver.quit()
    print("An error occured. Press Ctrl + C to stop alarm.")
    time.sleep(10)
    exit()

def ls_button_click():
    driver.find_element(By.ID, "ls-button-submit").click()

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
ageint = randint(10, 18) 

try:
    age = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "answer855125X5484X55002"))
    )
except:
    exception()
age.send_keys(str(ageint))

#gender
genderint = randint(0, 2)
if genderint == 0:
    driver.find_element(By.ID, "answer855125X5484X55010A2").click() #male
elif genderint == 1:
    driver.find_element(By.ID, "answer855125X5484X55010A1").click() #female
elif genderint == 2:
    driver.find_element(By.ID, "answer855125X5484X55010A3").click() #diverse

ls_button_click()

### P2 ###

try:
    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "answer855125X5485X550031"))
    )
except:
    exception()

medias = ["answer855125X5485X550031", "answer855125X5485X550032", "answer855125X5485X550033", "answer855125X5485X550034", "answer855125X5485X550035", "answer855125X5485X550036", "answer855125X5485X550037"]
for i in range(7):
    rdmint = randint(0, 1)
    if rdmint == 1:
        driver.find_element(locate_with(By.CLASS_NAME, "checkbox-label").near(driver.find_element(By.ID, medias[i]))).click()

medias2 = ["answer855125X5485X550041", "answer855125X5485X550042", "answer855125X5485X550043", "answer855125X5485X550044", "answer855125X5485X550045", "answer855125X5485X550046", "answer855125X5485X550047"]
for i in range(7):
    rdmint = randint(0, 1)
    if rdmint == 1:
        driver.find_element(locate_with(By.CLASS_NAME, "checkbox-label").near(driver.find_element(By.ID, medias2[i]))).click()

ls_button_click()

### P3 ###

try:
    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "answer855125X5486X550051"))
    )
except:
    exception()

sport = ["Fußball", "Tennis", "Schwimmen", "Quidditch"]
kreatives = ["Klavier", "Orgel", "Zeichnen", "Fotografie"]
entspannung = ["mit Freunden abhängen", "Essen", "Netflix", "Schlafen"]
action = ["Skaten", "Wandern", "Action-Film", "Theater"]
soziales = ["Pfadfinder", "Nachhilfe", "Jugendtreff", "Pfandflaschen sammeln"]
bildung = ["Duolingo", "Tierdokus", "Schule", "Lernen"]

medias3 = ["answer855125X5486X550051", "answer855125X5486X550052", "answer855125X5486X550053", "answer855125X5486X550054", "answer855125X5486X550055", "answer855125X5486X550056"]
for i in range(6):
    rdmint = randint(0, 1)
    if rdmint == 1:
        content = ""
        for u in range(4):
            if i == 0:
                rdmint = randint(0, 1)
                if rdmint == 1:
                    content = content + sport[u] + ", "
            if i == 1:
                rdmint = randint(0, 1)
                if rdmint == 1:
                    content = content + kreatives[u] + ", "
            if i == 2:
                rdmint = randint(0, 1)
                if rdmint == 1:
                    content = content + entspannung[u] + ", "
            if i == 3:
                rdmint = randint(0, 1)
                if rdmint == 1:
                    content = content + action[u] + ", "
            if i == 4:
                rdmint = randint(0, 1)
                if rdmint == 1:
                    content = content + soziales[u] + ", "
            if i == 5:
                rdmint = randint(0, 1)
                if rdmint == 1:
                    content = content + bildung[u] + ", "

        content = content[:len(content) - 2]
        driver.find_element(locate_with(By.CLASS_NAME, "checkbox-label").near(driver.find_element(By.ID, medias3[i]))).click()
        driver.find_element(By.ID, medias3[i] + "comment").send_keys(content)
        
ls_button_click()

### P4 ###

#wait





# driver.quit()
# print("Login successful")
# time.sleep(3)