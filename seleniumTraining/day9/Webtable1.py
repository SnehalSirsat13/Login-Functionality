import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1)count number of rows and columns
#noOfRows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
#noOfColumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/[1]/th"))
#print(noOfRows)
#print(noOfColumns)


#2)Read specific row and coulmn data
#data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[3]/td[2]").text
#print(data)

#3)Read all the rows and all the columns data
#print("printing all the rows and columns data.....................")

#for r in range(2,noOfRows+1):
#for r in noOfRows:
    #for c in noOfColumns:
     #for c in range(1,noOfColumns+1):
        #data=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[(r)]/td[[c]")
        #print(data,end='        ')
        #print()

#4)Read data based on the conditional(list book names whose author is mukesh)



