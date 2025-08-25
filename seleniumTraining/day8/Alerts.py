import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(2)

#open the alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(4)

alertwindow=driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("Welcome")

#alertwindow.accept()
alertwindow.dismiss()