import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://portfolio.rediff.com/money/jsp/daily_gainer.jsp")
time.sleep(2)
driver.maximize_window()

#self
#text_msg=driver.find_element(By.XPATH,"a[//contains(text(),'IITL Projects')]/self::a").text
#print(text_msg)
#time.sleep(2)

#parent
#text_msg=driver.find_element(By.XPATH,"a[//contains(text(),'IITL Projects')]/parent::td").text
#print(text_msg)
#time.sleep(2)

#child
#text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'IITL Projects')]/ancestor::tr/child::td").text
#print(text_msg)
#time.sleep(2)

#child nodes
#childs=driver.find_elements(By.XPATH,"//contains(text(),'IITL Projects')]/ancestor::tr/child::td")
#print(len(childs))

#ancestor
#text_msg=driver.find_element(By.XPATH,"a[//contains(text(),'IITL Projects')]/ancestor::tr").text
#print(text_msg)

#decesandent
#descendants=driver.find_element(By.XPATH,"a[//contains(text(),'IITL Projects')]/ancestor::tr/descendant::*")
#print(len(descendants))

#following
#followings=driver.find_elements(By.XPATH,"a[//contains(text(),'IITL Projects')]/ancestor::tr/following::*")
#print("Number of follwings nodes",len(followings))

#following-sibling
#follwingsiblings=driver.find_element(By.XPATH,"a[//contains(text(),'IITL Projects')]/ancestor::tr/follwing-sibling::*")
#print(len(follwingsiblings))

#preceding
#preceding=driver.find_elements(By.XPATH,"a[//contains(text(),'IITL Projects')]/ancestor::tr/preceding::*")
#print(len(preceding))

#preceding-siblings
#precedingsibling=driver.find_elements(By.XPATH,"a[//contains(text(),'IITL Projects')]/ancestor::tr/preceding-sibling::*")
#print(len(precedingsibling))




