from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import multiprocessing as mp
import concurrent.futures

driver = webdriver.Firefox()


def getStates(sleepTime, driver):
    driver.get("https://villageinfo.in/")
    c = driver.current_url
    while (True):
        try:
            statesLinks = driver.find_element(By.CLASS_NAME, "tab").find_elements(By.TAG_NAME, "a")
            return statesLinks
        except:
            while (True):
                try:
                    driver.get(c)
                    time.sleep(sleepTime)
                    break
                except:
                    time.sleep(sleepTime)
                    pass
def clickStates(sleepTime, num, driver):
    statesLinks = getStates(3, driver)
    print(statesLinks[num].text + "-----------------------")
    c = driver.current_url
    while (True):
        try:
            statesLinks[num].click()
            time.sleep(sleepTime)
            break
        except:
            while (True):
                try:
                    driver.get(c)
                    time.sleep(sleepTime)
                    break
                except:
                    time.sleep(3)
                    pass
    time.sleep(sleepTime)
    stateURL = driver.current_url
    return stateURL
def getDistricts(sleepTime, driver):
    c = driver.current_url
    while (True):
        try:
            districtsLinks = driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "a")
            return districtsLinks
        except:
            while (True):
                try:
                    driver.get(c)
                    time.sleep(sleepTime)
                    break
                except:
                    time.sleep(sleepTime)
                    pass
def clickDistricts(sleepTime, num, driver):
    districtsLinks = getDistricts(3, driver)
    print(districtsLinks[num].text + "************")
    c = driver.current_url
    while (True):
        try:
            districtsLinks[num].click()
            break
        except:
            while (True):
                try:
                    driver.get(c)
                    break
                except:
                    time.sleep(sleepTime) 
                    pass
    # into the tehsil/mandal/subdivision level
    time.sleep(sleepTime)
    districtURL = driver.current_url
    return districtURL
def getMandals(sleepTime, driver):
    c = driver.current_url
    while (True):
        try:
            mandalLinks = driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "a")
            return mandalLinks
        except:
            while (True):
                try:
                    driver.get(c)
                    time.sleep(sleepTime)
                    break
                except:
                    time.sleep(sleepTime)
                    pass
def clickMandals(sleepTime, num, driver):
    mandalLinks = getMandals(sleepTime, driver)
    print(mandalLinks[num].text + "######")
    c = driver.current_url
    while (True): 
        try:
            mandalLinks[num].click()
            break
        except:
            while (True):
                try:
                    driver.get(c)
                    time.sleep(sleepTime)
                    break
                except:
                    time.sleep(sleepTime)
                    pass
            pass
    # into the village level
    time.sleep(1)
    mandalURL = driver.current_url
    return mandalURL
def getVillages(sleepTime, driver):
    c = driver.current_url
    while (True):
        try:
            villagesLinks = driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "a")
            return villagesLinks
        except:
            while (True):
                try:
                    driver.get(c)
                    time.sleep(sleepTime)
                    break
                except:
                    time.sleep(sleepTime)
                    pass
def printVillages(sleepTime, num, driver):
    villagesLinks = getVillages(sleepTime, driver)
    print(villagesLinks[num].text)
def toPage(url, driver):
    c = driver.current_url
    while (True):
        try:
            driver.get(url)
            break
        except:
            while (True):
                try: 
                    driver.get(c)
                    break
                except:
                    time.sleep(1)
                    pass


statesLinks = getStates(3, driver)
def scrape(i):
    stateURL = clickStates(3, i, driver)
    districtsLinks = getDistricts(3, driver)
    for j in range(len(districtsLinks)):
        districtURL = clickDistricts(3, j, driver)
        mandalLinks = getMandals(3, driver)
        for g in range(len(mandalLinks)):
            mandalURL = clickMandals(3, g, driver)
            villagesLinks = getVillages(3, driver)
            for a in range(len(villagesLinks)):
                printVillages(3, a, driver)
            toPage(districtURL, driver)
        toPage(stateURL, driver)
    toPage("https://villageinfo.in/", driver)

    driver.close()

scrape(35)
