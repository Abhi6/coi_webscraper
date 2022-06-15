from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sqlalchemy import true

driver = webdriver.Firefox()
driver.get("https://vlist.in")

try:
    statesObj = driver.find_element(By.TAG_NAME, "tbody")
    allStates = statesObj.find_elements(By.TAG_NAME, "tr")
    for i in range(1, len(allStates)):
        statesObj = driver.find_element(By.TAG_NAME, "tbody")
        allStates = statesObj.find_elements(By.TAG_NAME, "tr")
        elem3 = allStates[i].find_elements(By.TAG_NAME, "td")
        print(elem3[1].text)
        elem3[1].find_element(By.TAG_NAME, "a").click()
        print(driver.title)
        driver.back()


finally:
    driver.close()
