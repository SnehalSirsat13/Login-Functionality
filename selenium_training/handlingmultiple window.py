import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()

print(driver.current_window_handle)#373F85E65B4CE34F715065E28C048A0D
handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

driver.quit()