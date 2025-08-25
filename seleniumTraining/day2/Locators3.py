import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

driver.get("https://www.facebook.com/")
time.sleep(3)
driver.maximize_window()

#tag and id
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("Snehal")
#time.sleep(3)

#tag and class
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("Snehal")
#time.sleep(3)

#tag attribute
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("snehal@gmail.com")
#time.sleep(3)

#tag class and attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal-pass]").send_keys("admin123")
time.sleep(3)

