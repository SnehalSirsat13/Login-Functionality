import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
time.sleep(3)

#find_element - returns single web element
#element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
#element.send_keys("Lenovo Thinkpad Carbon Laptop")
#time.sleep(3)

#locators matiching with multiple web elements
#element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
#element.text

#elements not available then throw nosuch elements exeception
#login_element=driver.find_element(By.LINK_TEXT,"Log in")
#login_element.click()

###find_elements() - return multiple elements
#1) locators matching with single web elemets
#elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
#print(len(elements))
#elements[0].send_keys("Lenovo Thinkpad Carbon Laptop")

#2)locators matching with multiple webelements
elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(elements))
#print(elements[0].text)
for ele in elements:
    print(ele.text)
