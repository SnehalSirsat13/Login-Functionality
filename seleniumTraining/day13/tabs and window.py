import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

regilink=Keys.CONTROL+Keys.RETURN
driver.find_element(By.LINK_TEXT,"Register").send_keys(Keys.CONTROL+Keys.RETURN)

time.sleep(3)
