import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(10)

searchbox=driver.find_element(By.NAME,"q")

searchbox.send_keys("Selenium")
searchbox.submit()

time.sleep(5)
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

driver.quit()

