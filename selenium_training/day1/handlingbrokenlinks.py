import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib3 import request

driver = webdriver.Chrome()

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME,'a')
total_links = len(links)

print(f"Total links:{total_links}")
time.sleep(3)

for link in links:
    href = link.get_attribute('href')
    response = request.get(href)
    if response.status_code >=400:
        print(f"Broke link:{href}(status code: {response.status_code}")
        driver.quit()



