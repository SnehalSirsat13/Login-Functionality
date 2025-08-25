import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


#capture cookies from the browser
cookies=driver.get_cookies()
print(len(cookies))

#print information details of all the cookies
for c in cookies:
    #print(c)
     print(c.get('name'),":",c.get('value'),)

#Add new cookie to the browser
#driver.add_cookie({"name":"Mycookie","value":"21345"})
#cookies=driver.get_cookies()
#print(len(cookies))

#Delete a specific cookie from the browser
driver.delete_cookie("Mycookie")
cookies=driver.get_cookies()
print(len(cookies))

#delete all the cookies from the browser
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))


driver.quit()