import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

time.sleep(2)
driver.get("https://www.facebook.com")
time.sleep(3)

current_page_title = driver.title
print("title,current_page_title")
print(driver.page_source)

driver.back()
time.sleep(2)
driver.forward()
time.sleep(3)

driver.refresh()
time.sleep(3)

driver.close()







