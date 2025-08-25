import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#conditional command is_displayed and is_enabled
driver.get("https://demo.nopcommerce.com/")
time.sleep(2)
driver.maximize_window()

#searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
#print("Display status",searchbox.is_displayed())
#print("Enabled status",searchbox.is_enabled())
#time.sleep(2)
#driver.quit()

#is_selected
driver.find_element(By.LINK_TEXT,"Register").click()

rd_male=driver.find_element(By.ID,"gender-male")
rd_female=driver.find_element(By.ID,"gender-female")

print("Default radio button status....")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()

print("After selecting the male radio button....")
print(rd_male.is_selected())
print(rd_female.is_selected())
