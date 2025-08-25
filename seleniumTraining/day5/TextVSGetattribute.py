import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
time.sleep(3)

#emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")

#emailbox.clear()
#emailbox.send_keys("abc@gmail.com")

#print("result of text:",emailbox.text)
#print("result of get_attribute",emailbox.get_attribute('value'))

button=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("result of text:",button.text)
print("result of get_attribute:()",button.get_attribute('value'))



