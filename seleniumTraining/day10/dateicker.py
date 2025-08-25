import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

#driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("05/12/2000")

year="2000"
month="March"
date="30"

driver.find_element(By.XPATH,"//*[@id='datepicker']").click()

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        #driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]").click()

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break




