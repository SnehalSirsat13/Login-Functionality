import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()
print(driver.current_window_handle)

handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()

        driver.quit()

    time.sleep(3)






