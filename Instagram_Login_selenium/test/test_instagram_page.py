import time

from test_data.test_data_login_page import TestData
from config.setup import setup
from pages.login import LoginPage
class TestVerifyLoginPage:

    def test_verify_login_functionality_instagram(self, setup):
        exp_result = "Instagram user page"
        driver = setup
        driver.get(TestData.baseurl)
        login = LoginPage(driver)
        login.set_username(TestData.username)
        login.setpassword(TestData.password)
        login.click_on_login_btn()
        time.sleep(5)
        act_result = driver.title
        assert act_result == exp_result


