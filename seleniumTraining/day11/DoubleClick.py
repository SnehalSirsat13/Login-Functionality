import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

driver.switch_to.frame("iframeResult")

feild1=driver.find_element(By.XPATH,"//input[@id='field1']")
feild1.clear()
feild1.send_keys("Welcome")

button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

act = ActionChains(driver)
act.double_click(button).perform()
time.sleep(3)
