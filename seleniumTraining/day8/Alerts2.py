import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(3)
driver.switch_to.alert.accept()

driver.close()
