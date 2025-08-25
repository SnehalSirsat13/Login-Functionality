import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()

driver.execute_script("window.scrollTo(0,700)")
time.sleep(3)

table = driver.find_element(By.ID,"countries")
rows = table.find_element(By.TAG_NAME,"tr")
rows_count = len(rows)
print(rows_count)