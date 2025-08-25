import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome
time.sleep(2)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
time.sleep(2)

driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)

