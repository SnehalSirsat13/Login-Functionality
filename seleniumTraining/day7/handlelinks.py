import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#1)click on the link
#driver.find_element(By.LINK_TEXT,"Digital downloads ").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

#find number of links
links=driver.find_elements(By.TAG_NAME,"a")
print("total number of links",len(links))

#print all the link names
for link in links:
    print(link.text)




