import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("http://www.automationpractice.pl/index.php")
time.sleep(3)
driver.maximize_window()

#absolute xpath
#driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirts")
#driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()
#time.sleep(3)

#relative xpath
#driver.find_element(By.XPATH,"//*[@id='search_query_top']").send_keys("T-shirts")
#driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()
#time.sleep(3)

#xpath with OR operator//
#driver.find_element(By.XPATH,"//input[@id='search_query_top' or @name='search_query']").send_keys("T-shirts")
#driver.find_element(By.XPATH,"//input[@name='submit_search' and @class='btn btn-default button-search']").click()
#time.sleep(3)

#contains and start with//
#driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("T-shirts")
#driver.find_element(By.XPATH,"//button[start-with(@name,'submit')]").click()
#time.sleep(3)

#text//
driver.find_element(By.XPATH,"//a[text()='Women']").click()
time.sleep(3)
