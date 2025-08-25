import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#count no.of rows and columns
noOfRows=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr")
noOfColumns=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[1]/th")
print(noOfRows)
print(noOfColumns)
driver.close()

#read specific row and column data
#data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]/td[3]").text
#print(data)

#read all the rows and columns
print("printing all the rows and olumns data......................")

for r in range(2,noOfRows+1):
    for c in range(1,noOfColumns+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data)






