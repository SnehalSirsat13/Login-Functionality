import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#1)scroll down page by pixel
#driver.execute_script("window.scrollBy(0,3000)","")
#value=driver.execute_script("return windows.pageYOffset;")
#print("Number of pixels moved:",value)

#2)scroll down the page till the element is visible
flag=driver.find_element(By.XPATH,"//td[normalize-space()='India']")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value=driver.execute_script("return windows.pageYOffset;")
print("Number of pixels moved:",value)


#3)scroll down till end
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#value=driver.execute_script("return windows.pageYOffset;")
#print("Number of pixels moved:",value)


#4)scroll reverse
#driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
#value=driver.execute_script("return windows.pageYOffset;")
#print("Number of pixels moved:",value)


