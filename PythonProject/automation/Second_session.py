import time
from tkinter.font import names

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://www.facebook.com")
time.sleep(3)
anchor_list=driver.find_elements(By.TAG_NAME,"a")
print("total Links ",len(anchor_list))
for link in anchor_list:
    name_link=link.get_attribute("href")
    print(name_link,link.text)