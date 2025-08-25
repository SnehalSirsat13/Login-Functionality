import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver=webdriver.Chrome()

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
time.sleep(2)

links = driver.find_elements(By.TAG_NAME,"a")


for link in links:
    print(link.text)

for link in links:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code >=400:
        print(f"Broken link:{href}(status code:{response.status_code}")

        driver.quit()













