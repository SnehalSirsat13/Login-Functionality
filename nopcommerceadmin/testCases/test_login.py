import pytest
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen

class TestLogin:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.fixture
    def setup(self, driver):
        self.driver = driver
        self.driver.get(self.base_url)
        yield
        self.driver.quit()

    def test_home_page_title(self, setup):
        self.logger.info("Verifying homepage title")
        actual_title = self.driver.title
        expected_title = "nopCommerce demo store. Login"
        assert actual_title == expected_title, f"Expected {expected_title}, but got {actual_title}"

    def test_login(self, setup):
        self.logger.info("Performing login")
        login_page = LoginPage(self.driver)
        login_page.set_username(self.username)
        login_page.set_password(self.password)
        login_page.click_login()
        dashboard_header = self.driver.find_element(By.XPATH, "//h1[text()='Dashboard']")
        assert dashboard_header.is_displayed(), "Dashboard header not found"
