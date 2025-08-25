import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

#get app command
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

print(driver.title)

print(driver.current_url)
print(driver.page_source)

driver.quit()

