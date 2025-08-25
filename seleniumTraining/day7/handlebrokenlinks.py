from itertools import count

import requests as requests
import time

from pip._internal.models import link
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

alllinks=driver.find_elements(By.TAG_NAME,"a")
count=0

for links in alllinks:
    url=link.get_attribute('href')
    res=requests.head(url)
    if res.status_code>=400:
        print(url,"is broken link")
        count=+1
    else:
        print(url,"is valid link")

print("total number of broken links",count)


