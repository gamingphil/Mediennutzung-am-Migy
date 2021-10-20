# for z in range(3):
z = 1
while z > 0:
    import time
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.relative_locator import locate_with
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import Select

    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")

    from random import randint
    import random

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

    driver.switch_to.new_window('tab')
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

    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "javatbd855125X5487X55006A1"))
        )
    except:
        exception()

    for i in range(10):
        webdriver.ActionChains(driver).double_click(driver.find_element(By.ID, "javatbd855125X5487X55006A" + str(randint(1, 9)))).perform()

    select = Select(driver.find_element(By.ID, "answer855125X5487X55007"))

    select.select_by_value("A" + str(randint(1, 11)))

    medias4 = ["answertext855125X5487X550081", "answertext855125X5487X550082", "answertext855125X5487X550083", "answertext855125X5487X550084", "answertext855125X5487X550085", "answertext855125X5487X550086"]
    try:
        for i in range(6):
            driver.find_element(locate_with(By.CLASS_NAME, "answer_cell_A" + str(randint(1, 10))).to_right_of(driver.find_element(By.ID, medias4[i]))).click()    
    except:
        pass

    medias5 = ["answertext855125X5487X550091", "answertext855125X5487X550092", "answertext855125X5487X550093", "answertext855125X5487X550094", "answertext855125X5487X550095", "answertext855125X5487X550096"]
    try:
        for i in range(6):
            driver.find_element(locate_with(By.CLASS_NAME, "answer_cell_A" + str(randint(2, 11))).to_right_of(driver.find_element(By.ID, medias5[i]))).click()      
    except:
        pass

    rdmint = randint(0, 1)
    if rdmint == 1:
        driver.find_element(locate_with(By.CLASS_NAME, "control-label").near(driver.find_element(By.ID, "answer855125X5487X55017A1"))).click()

    ls_button_click()

    ### P5 ###

    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "answertext855125X5488X550111"))
        )
    except:
        exception()

    medias6 = ["answertext855125X5488X550111", "answertext855125X5488X550112", "answertext855125X5488X550113", "answertext855125X5488X550114", "answertext855125X5488X550115", "answertext855125X5488X550116", "answertext855125X5488X550117"]
    try:
        for i in range(6):
            driver.find_element(locate_with(By.CLASS_NAME, "answer_cell_A" + str(randint(1, 10))).to_right_of(driver.find_element(By.ID, medias6[i]))).click()      
    except:
        pass

    games = ["Minecraft", "Fortnite", "Landwirtschaftssimulator", "Among Us", "CSGO", "Train Simulator", "Rocket League", "Cities: Skylines", "F1 2020", "osu!"]

    rdnArray = random.sample(games, 5)

    for i in range(5):
        driver.find_element(By.ID, "answer855125X5488X55012" + str(i + 1)).send_keys(rdnArray[i])

    driver.find_element(locate_with(By.CLASS_NAME, "control-label").to_right_of(driver.find_element(By.ID, "answer855125X5488X55013A" + str(randint(1,3))))).click()

    medias7 = ["answer855125X5488X550191", "answer855125X5488X550192", "answer855125X5488X550193", "answer855125X5488X550194", "answer855125X5488X550195", "answer855125X5488X550196"]
    for i in range(6):
        rdmint = randint(0, 1)
        if rdmint == 1:
            driver.find_element(locate_with(By.CLASS_NAME, "checkbox-label").near(driver.find_element(By.ID, medias7[i]))).click()

    rdmint = randint(0, 1)
    if rdmint == 1:
        driver.find_element(locate_with(By.CLASS_NAME, "control-label").near(driver.find_element(By.ID, "answer855125X5488X55018A2"))).click()

    ls_button_click()

    ### P6 ###

    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "javatbd855125X5489X550141"))
        )
    except:
        exception()

    medias8 = ["answer855125X5489X550141", "answer855125X5489X550142", "answer855125X5489X550143", "answer855125X5489X550144", "answer855125X5489X550145", "answer855125X5489X550146", "answer855125X5489X550147"]
    for i in range(7):
        rdmint = randint(0, 1)
        if rdmint == 1:
            driver.find_element(locate_with(By.CLASS_NAME, "checkbox-label").near(driver.find_element(By.ID, medias8[i]))).click()

    driver.find_element(locate_with(By.CLASS_NAME, "control-label").near(driver.find_element(By.ID, "answer855125X5489X55015A1"))).click()

    medias9 = ["answer855125X5489X550161", "answer855125X5489X550162", "answer855125X5489X550163", "answer855125X5489X550164"]
    for i in range(4):
        rdmint = randint(0, 1)
        if rdmint == 1:
            driver.find_element(locate_with(By.CLASS_NAME, "checkbox-label").near(driver.find_element(By.ID, medias9[i]))).click()

    driver.find_element(locate_with(By.CLASS_NAME, "control-label").near(driver.find_element(By.ID, "answer855125X5489X55296A2"))).click()

    ls_button_click()
    time.sleep(0.2)
    driver.quit()
    # print("Login successful")
    # time.sleep(3)