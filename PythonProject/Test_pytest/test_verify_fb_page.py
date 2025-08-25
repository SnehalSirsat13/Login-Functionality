from selenium import webdriver
import pytest

@pytest.mark.fb
def test_verify_homepage_001():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://facebook.com")
    exp_result="Facebook – log in or sign u"
    act_result=driver.title
    assert exp_result==act_result