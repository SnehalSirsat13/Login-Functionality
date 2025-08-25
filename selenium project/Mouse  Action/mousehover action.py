import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button")
time.sleep(3)

admin=driver.find_element(By.XPATH,"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
usermgnt=driver.find_element(By.XPATH,"//span[normalize-space()='User Management']")
users=driver.find_element(By.XPATH,"//ul[@class='oxd-dropdown-menu']//li")

act=ActionChains(driver)
act.move_to_element(admin).move_to_element(usermgnt).move_to_element(users).click().perform()



