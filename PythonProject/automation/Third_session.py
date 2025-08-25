import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
time.sleep(2)
name_input=driver.find_element(By.NAME,"name").send_keys("Snehal Sirsat")
driver.find_element(By.NAME,"email").send_keys("snehal@gmail.com")
driver.find_element(By.NAME,"gender").click()
driver.find_element(By.XPATH,'//*[@id="practiceForm"]/div[3]/div/div/div[2]/input').click()
driver.find_element(By.ID,"mobile").send_keys(9595959595)
driver.find_element(By.NAME,"dob").send_keys("11-25-1993")
subject_input = driver.find_element(By.NAME, 'subject')
driver.find_element(By.ID,"hobbies").click()
time.sleep(3)
driver.find_element(By.ID,"picture").send_keys(r"C:\Users\Rahul\Desktop\screeen.png")
select =Select(driver.find_element(By.NAME,"state"))
select.select_by_visible_text("Haryana")
time.sleep(10)