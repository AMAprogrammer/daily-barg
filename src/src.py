from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://taaghche.com/")

login = driver.find_element(by=By.XPATH,
                            value="/html/body/div[1]/header/div/div[2]/div/div[1]/div[3]/div/a")

login.click()

phone_number = driver.find_element(by=By.XPATH
                                   , value="/html/body/div[1]/main/div/div[2]/form/div[1]/input")

phone_number.clear()
phone_number.send_keys("09927063067")
