import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[normalize-space()='Alert']").click()

alertwindow=driver.switch_to.alert
time.sleep(3)

print(alertwindow.text)

alertwindow.accept()

time.sleep(3)