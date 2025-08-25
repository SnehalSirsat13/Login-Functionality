import time
from itertools import count

import broken
import links
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver=webdriver.Chrome()

driver.get("https://jqueryui.com/")
driver.maximize_window()
time.sleep(2)

#links=driver.find_elements(By.TAG_NAME,'a')
#print("total number of links:",len(links))
#time.sleep(3)

#for link in links:
   # print(link.text)

print broken links
for link in links:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code >=400:
        print("Broken link:{href}(status code:{response.status_code})")
        driver.quit()



