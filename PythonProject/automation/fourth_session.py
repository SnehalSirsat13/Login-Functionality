import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com")
time.sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
driver.close()
driver.quit()
