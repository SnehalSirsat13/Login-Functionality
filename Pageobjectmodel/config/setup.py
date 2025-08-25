import time

import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.chorme()
    driver.maximize_window()

    yield driver
