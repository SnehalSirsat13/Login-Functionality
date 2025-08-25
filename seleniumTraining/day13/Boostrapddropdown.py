import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
countries=driver.find_element(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countries))

for country in countries:
    if country.text=="India":
        country.click()
        break

time.sleep(2)


