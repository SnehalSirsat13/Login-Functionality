import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

#mywait=WebDriverWait(driver,10)
mywait=WebDriverWait(driver,10,ignored_exceptions=[NoSuchElementException,
                                                   ElementNotVisibleException,
                                                   ElementNotSelectableException,
                                                   Exception]
                     )


driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(10)

searchbox=driver.find_element(By.NAME,"q")

searchbox.send_keys("Selenium")
searchbox.submit()

searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()

time.sleep(5)
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

driver.quit()
