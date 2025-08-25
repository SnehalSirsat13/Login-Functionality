import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()

element = driver.find_element(By.XPATH,"//input[@value='Login']")
driver.execute_script("arguments[0].scrollIntoView;",element)
element.click()

time.sleep(3)