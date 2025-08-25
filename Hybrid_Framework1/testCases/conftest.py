from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    if browser=='chrome':
     driver = webdriver.Chrome()
    elif browser=='firefox':
     driver = webdriver.Firefox
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(requst):
    return request.config.getoption("--browser")
