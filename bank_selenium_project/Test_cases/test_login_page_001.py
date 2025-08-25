import time

from configration.setup import setup
from .base_Data import Test_Data
from pages.login import Login
class Test_login_Functionality_001:

    def test_verify_login_page(self,setup):
        exp_result="GTPL Bank Manager HomePage"
        driver = setup
        driver.get(Test_Data.baseUrl)
        login=Login(driver)
        login.setUsername(Test_Data.userName)
        login.setPassword(Test_Data.password)
        login.clickOnLoginBtn()
        time.sleep(3)
        act_result=driver.title
        assert act_result==exp_result
