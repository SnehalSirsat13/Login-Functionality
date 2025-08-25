import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

#drpcountry_ele=driver.find_element(By.XPATH,"//select[@id='input-country']")
drpcountry=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))


#select option from the drop down
#drpcountry.select_by_visible_text("India")
#drpcountry.select_by_value("99")
#drpcountry.select_by_index(12)

#captur all the options and print them
alloptions=drpcountry.options
print("total number of options:",len(alloptions))

#for opt in alloptions:
#    print(opt.text)

#select options from the dropdown without using built in method
for opt in alloptions:
    if opt.text=="India":
        opt.click()
        break




