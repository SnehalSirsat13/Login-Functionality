import time

from test_data.test_data_login_page import Test_Data
from config.setup import setup
from pages.login import Login_page
class Test_verify_login_page:

    def test_verify_login_functionality_fb(self,setup):
        expected_result="Log in to Facebook"
        driver = setup
        driver.get(Test_Data.base_Url)
        login = Login_page(driver)
        login.setUsername(Test_Data.username)
        time.sleep(2)
        login.setPassword(Test_Data.password)
        time.sleep(2)
        login.click_On_Login_Btn()
        time.sleep(3)
        act_result = driver.title
        assert act_result == exp_result
        time.sleep(10)
