import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

#date of birth element
driver.find_element(By.XPATH,"//input[@id='dob']").click()

datepicker_month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
datepicker_month.select_by_visible_text("Dec")

datepicker_year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
datepicker_year.select_by_visible_text("2000")
time.sleep(2)

alldates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//table/tbody/tr/td/a")
for date in alldates:
    if date.text=='25':
        date.click()
        break

time.sleep(2)