from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome


driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default ui-state-hover ui-state-focus']")
max_slider=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default ui-state-hover ui-state-focus']")

print("Location of sliders Before moving........")
print(min_slider.location)
print(max_slider.location)

act=ActionChains(driver)

act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-39,0).perform()

print("Location of sliders After moving........")
print(min_slider.location)
print(max_slider.location)


