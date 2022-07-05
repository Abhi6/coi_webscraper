from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import multiprocessing as mp
import concurrent.futures
import json




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
    global statesLinks
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
    global districtsLinks
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
    global mandalLinks
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
    global villagesLinks
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
def convertText(links):
    texts = []
    for item in links:
        texts.append(item.text)
    return texts



def scrape(i):
    driver = webdriver.Firefox()
    info = {}
    statesLinks = getStates(3, driver)
    stateNames = convertText(statesLinks)
    stateURL = clickStates(3, i, driver)
    info[stateNames[i]] = []
    districtsLinks = getDistricts(3, driver)
    districtNames = convertText(districtsLinks)
    for j in range(len(districtsLinks)):
        districtURL = clickDistricts(3, j, driver)
        info[stateNames[i]].append({districtNames[j] : []})
        mandalLinks = getMandals(3, driver)
        mandalNames = convertText(mandalLinks)
        for g in range(len(mandalLinks)):
            mandalURL = clickMandals(3, g, driver)
            info[stateNames[i]][-1][districtNames[j]].append({mandalNames[g] : []})
            villagesLinks = getVillages(3, driver)
            villageNames = convertText(villagesLinks)
            for a in range(len(villagesLinks)):
                printVillages(3, a, driver)
                info[stateNames[i]][-1][districtNames[j]][-1][mandalNames[g]].append(villageNames[a])
            toPage(districtURL, driver)
        toPage(stateURL, driver)
    toPage("https://villageinfo.in/", driver)

    with open(f"{stateNames[i]}.json", "w") as output:
        json.dump(info, output, indent=4)

    driver.close()

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        targets = [30, 31, 34]
        results = [executor.submit(scrape, target) for target in targets]
