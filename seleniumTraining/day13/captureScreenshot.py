import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#driver.save_screenshot("C:\\Users\\Rahul\\PycharmProjects\\seleniumTraining\\day13\\homepage.png")
#driver.save_screenshot(os.getcwd()+"homepage.png")

#driver.get_screenshot_as_file(os.getcwd()+"homepage.png")

