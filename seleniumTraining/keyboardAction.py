import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys

driver=webdriver.Chrome()

driver.get("https://text-compare.com/")
driver.maximize_window()

input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

input1.send_keys("Hello World")

act = ActionChains(driver)

#1)input1 ctrl+A select the text
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#2)input1 ctrl+C copy text
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Press tab key to navigate to input
act.send_keys(Keys.TAB).perform()


#input2 ctrlV
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()





