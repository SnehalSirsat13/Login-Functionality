from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

input1=driver.find_element(By.XPATH,"//*[@id="inputText1"]")
input2=driver.find_element(By.XPATH,"//*[@id="inputText2"]")

input1.send_keys("Welcome to selenium")

act=ActionChains(driver)
