import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://demo.nopcommerce.com/")

print(driver.title)



