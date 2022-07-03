from ast import Try
from tokenize import Triple
import traceback
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from sqlalchemy import except_all, null


driver = webdriver.Firefox()
driver.get("https://villageinfo.in/")
wait = WebDriverWait(driver, 5)

def getStates(sleepTime):
    global statesLinks
    while (True):
        try:
            statesLinks = driver.find_element(By.CLASS_NAME, "tab").find_elements(By.TAG_NAME, "a")
            break
        except:
            while (True):
                try:
                    driver.refresh()
                    time.sleep(sleepTime)
                    break
                except:
                    time.sleep(sleepTime)
                    pass
def clickStates(sleepTime, num):
    global stateURL
    getStates(3)
    print(statesLinks[num].text + "-----------------------")
    while (True):
        try:
            statesLinks[num].click()
            time.sleep(sleepTime)
            break
        except:
            while (True):
                try:
                    driver.refresh()
                    time.sleep(sleepTime)
                    break
                except:
                    time.sleep(3)
                    pass
    time.sleep(sleepTime)
    stateURL = driver.current_url
def getDistricts(sleepTime):
    global districtsLinks
    while (True):
        try:
            districtsLinks = driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "a")
            break
        except:
            while (True):
                try:
                    driver.refresh()
                    time.sleep(sleepTime)
                    break
                except:
                    time.sleep(sleepTime)
                    pass
def clickDistricts(sleepTime, num):
    global districtURL
    getDistricts(3)
    print(districtsLinks[num].text + "************")
    while (True):
        try:
            districtsLinks[num].click()
            break
        except:
            while (True):
                try:
                    driver.refresh()
                    break
                except:
                    time.sleep(sleepTime) 
                    pass
    # into the tehsil/mandal/subdivision level
    time.sleep(sleepTime)
    districtURL = driver.current_url
def getMandals(sleepTime):
    global mandalLinks
    while (True):
        try:
            mandalLinks = driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "a")
            break
        except:
            while (True):
                try:
                    driver.refresh()
                    time.sleep(sleepTime)
                    break
                except:
                    time.sleep(sleepTime)
                    pass
def clickMandals(sleepTime, num):
    global mandalURL
    getMandals(sleepTime)
    print(mandalLinks[num].text + "######")
    while (True): 
        try:
            mandalLinks[num].click()
            break
        except:
            while (True):
                try:
                    driver.refresh()
                    time.sleep(sleepTime)
                    break
                except:
                    time.sleep(sleepTime)
                    pass
            pass
    # into the village level
    time.sleep(1)
    mandalURL = driver.current_url
def getVillages(sleepTime):
    global villagesLinks
    while (True):
        try:
            villagesLinks = driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "a")
            break
        except:
            while (True):
                try:
                    driver.refresh()
                    time.sleep(sleepTime)
                    break
                except:
                    time.sleep(sleepTime)
                    pass
def printVillages(sleepTime, num):
    getVillages(sleepTime)
    print(villagesLinks[num].text)
def toPage(url):
    while (True):
        try:
            driver.get(url)
            break
        except:
            while (True):
                try: 
                    driver.refresh()
                    break
                except:
                    time.sleep(1)
                    pass



getStates(3)
for i in range(len(statesLinks)):
    clickStates(3, i)
    getDistricts(3)
    for j in range(len(districtsLinks)):
        clickDistricts(3, j)
        getMandals(3)
        for g in range(len(mandalLinks)):
            clickMandals(3, g)
            getVillages(3)
            for a in range(len(villagesLinks)):
                printVillages(3, a)
            toPage(districtURL)
        toPage(stateURL)
    toPage("https://villageinfo.in/")


driver.close()