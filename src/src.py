from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Firefox()

driver.get("https://taaghche.com/login")

sleep(3)

phone_number = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div[2]/form/div[1]/input")
phone_number.clear()
phone_number.send_keys("09927063067")

confirm = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div[2]/form/div[2]")
confirm.click()

sleep(3)

password = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div[2]/form/div[1]/input")
password.clear()
password.send_keys("13820221@mirhossein@lizadeh")

continuee = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div[2]/form/div[2]/button/div")
continuee.click()

sleep(3)

driver.get("https://taaghche.com/rooyesh")

sleep(3)

barg = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div/div/div[1]/div/div[2]/div/button")
barg.click()

sleep(3)

bar = driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/div/div[2]/div/div[1]/div[3]/div/div")
bar.click()

sleep(1)

logout = driver.find_element(by=By.XPATH,
                             value="/html/body/div[1]/header/div/div[2]/div/div[1]/div[3]/div/div[2]/div/ul/li[9]")
logout.click()

driver.quit()
