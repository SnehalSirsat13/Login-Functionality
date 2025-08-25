import time
from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com/")
time.sleep(2)
driver.implicitly_wait(10)

searchbox=driver.find_element(By.ID,"input")
searchbox.send_keys("Python Programming")
searchbox.submit()




