import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#driver.execute_script("window.scrollBy(0,1000)","")
#time.sleep(3)

#flag=driver.find_element(By.XPATH,'//*[@id="ct-list"]/table[1]/tbody/tr[25]/td[2]')
#driver.execute_script("arguments[0].scrollIntoView();",flag)


#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#time.sleep(2)

