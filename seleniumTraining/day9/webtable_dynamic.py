import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(2)

#driver.find_element(By.XPATH,"//h6[normalize-space()='Admin']").click()
#driver.find_element(By.XPATH,"//li[@class='--active oxd-topbar-body-nav-tab --parent --visited']").click()
#driver.find_element(By.XPATH,"//ul[@role='menu']//li").click()



