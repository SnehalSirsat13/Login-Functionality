import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1)select specifice checkbox from the list
#driver.find_element(By.ID,"monday").click()
#time.sleep(3)

#2)select all the checkbox
#checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and @contains(@id,'day')]")
#print(len(checkboxes))

#driver.quit()

#Approach1
for i in range(len(checkboxes)):
    checkboxes[i].click()

#Approach2
#for checkbox in checkboxes:
#    checkbox.click()

#3)select multiple checkboxes by choice
#for checkbox in checkboxes:
    #weekname = checkbox.get_attribute('id')
    #if weekname=='monday' or weekname=='sunday':
      #checkbox.click()

#4) select last 2 checkboxes
#for i in range(len(checkboxes)-2,len(checkboxes)):
#    checkboxes[i].click()

#5)select first 2 checkboxes
#for i in range(len(checkboxes)):
#    if i<2:
 #       checkboxes[i].click()

#6)clearing all the checkboxes
#for checkbox in checkboxes:
#    if checkbox.is_selected():
#        checkbox.click()


