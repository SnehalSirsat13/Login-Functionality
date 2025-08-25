import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

driver.get("http://www.automationpractice.pl/index.php")
time.sleep(3)

#Class Name and number of slider = 5
#slider=driver.find_elements(By.CLASS_NAME,"homeslider-container")
#print(len(slider))

#Tag Name and counting the total number of links = 88
#links=driver.find_elements(By.TAG_NAME,"a")
#print(len(links))

