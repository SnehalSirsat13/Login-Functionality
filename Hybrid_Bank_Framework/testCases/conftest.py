from pygments.lexer import default
from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser",actions="store",default="chrome",
                     help="Specify the browser: chrome or firefox or edge")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver