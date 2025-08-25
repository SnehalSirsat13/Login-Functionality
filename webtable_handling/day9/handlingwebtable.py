import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.coingecko.com/en/currencies/inr")
driver.maximize_window()

