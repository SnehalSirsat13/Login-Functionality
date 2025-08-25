import pytest
from selenium import webdriver
@pytest.fixture()
def setup():
    driver = webdriver.chrome()
    driver.maximize_window()
    yield driver
