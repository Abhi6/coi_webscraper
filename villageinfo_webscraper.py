import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from sqlalchemy import null

driver = webdriver.Firefox()
driver.get("https://villageinfo.in/")
wait = WebDriverWait(driver, 5)

try:
    statesElementExists = False
    statesObj = null
    while (statesElementExists == False):
        try:
            statesObj = driver.find_element(By.TAG_NAME, "tbody")
            statesElementExists = True
        except NoSuchElementException:
            driver.refresh()
            pass
    # statesObj = driver.find_element(By.CLASS_NAME, "tab")
    statesLinks = statesObj.find_elements(By.TAG_NAME, "a")
    for i in range(len(statesLinks)):
        time.sleep(0.1) # this line is necessary
        statesObj = driver.find_element(By.CLASS_NAME, "tab")
        statesLinks = statesObj.find_elements(By.TAG_NAME, "a")
        print(statesLinks[i].text + "------------------------")
        statesLinks[i].click()
        # into the district level
        time.sleep(3) # this line is necessary
        elementExists = False
        districtsObj = null
        while (elementExists == False):
            try:
                districtsObj = driver.find_element(By.TAG_NAME, "tbody")
                elementExists = True
            except NoSuchElementException:
                driver.refresh()
                pass
        # districtsObj = driver.find_element(By.TAG_NAME, "tbody")
        districtsLinks = districtsObj.find_elements(By.TAG_NAME, "a")
        for j in range(len(districtsLinks)):
            time.sleep(0.1)
            districtsObj = driver.find_element(By.TAG_NAME, "tbody")
            districtsLinks = districtsObj.find_elements(By.TAG_NAME, "a")
            print(districtsLinks[j].text + "************")
            districtsLinks[j].click()
            # into the tehsil/mandal/subdivision level
            time.sleep(1)
            tbodyExists_mandal = False
            mandalsObj = null
            while (tbodyExists_mandal == False):
                try:
                    mandalsObj = driver.find_element(By.TAG_NAME, "tbody")
                    tbodyExists_mandal = True
                except NoSuchElementException:
                    driver.refresh()
                    pass
            mandalLinks = mandalsObj.find_elements(By.TAG_NAME, "a")
            for g in range(len(mandalLinks)):
                time.sleep(0.1)
                mandalsObj = driver.find_element(By.TAG_NAME, "tbody")
                mandalLinks = mandalsObj.find_elements(By.TAG_NAME, "a")
                print(mandalLinks[g].text + "######")
                clicked = False
                while (clicked == False): 
                    try:
                        mandalLinks[g].click()
                        clicked = True
                    except:
                        driver.refresh()
                        pass
                # into the village level
                time.sleep(1)
                tbodyExists_village = False
                villagesObj = null
                while (tbodyExists_village == False):
                    try:
                        villagesObj = driver.find_element(By.TAG_NAME, "tbody")
                        tbodyExists_village = True
                    except NoSuchElementException:
                        driver.refresh()
                        pass
                villageLinks = villagesObj.find_elements(By.TAG_NAME, "a")
                for a in range(len(villageLinks)):
                    time.sleep(0.1)
                    villagesObj = driver.find_element(By.TAG_NAME, "tbody")
                    villageLinks = villagesObj.find_elements(By.TAG_NAME, "a")
                    print(villageLinks[a].text)
                driver.back()
            driver.back()
        driver.back()
finally:
    print("Error")
driver.close()