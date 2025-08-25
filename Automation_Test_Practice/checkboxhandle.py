import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.ID,"name").send_keys("Sneha Sirsat")
driver.find_element(By.ID,"email").send_keys("abd@gmail.com")
driver.find_element(By.ID,"phone").send_keys("77777779")
driver.find_element(By.ID,"textarea").send_keys("Dighi Alandi rd Pune")
time.sleep(2)

driver.find_element(By.ID,"male").click()
driver.find_element(By.ID,"monday").click()

drp_country=Select(driver.find_element(By.XPATH,"//select[@id='country']"))
#drp_country.select_by_visible_text("Germany")
drp_country.select_by_value("usa")

all_options=drp_country.options
print("total number of options",len(all_options))

for opt in all_options:
    print(opt.text)

time.sleep(2)
