import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,1555)","")

source_ele=driver.find_element(By.ID,"draggable")
target_ele=driver.find_element(By.ID,"droppable")

actions=ActionChains(driver)
actions.drag_and_drop(source_ele,target_ele).perform()
time.sleep(2)