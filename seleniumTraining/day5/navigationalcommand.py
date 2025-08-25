import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://snapdeal.com/")
time.sleep(2)

driver.get("https://www.amazon.in/")
time.sleep(2)

driver.back()
driver.forward()

driver.refresh()

driver.quit()