import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
time.sleep(3)
driver.maximize_window()

#id locators
#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad Carbon Laptop")
#time.sleep(2)

#linktext and partial linktext

#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
time.sleep(3)










