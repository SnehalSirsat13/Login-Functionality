from configuration.setup import setup
from .base_Data import Test_Data
from pages.login import Login
class Test_login_Functionality_001:

    def test_verify_login_page(self,setup):
        driver = setup
        driver.get(Test_Data.baseUrl)
        login=Login(driver)
        login.setUsername(Test_Data.userName)
        login.setPassword(Test_Data.password)
        login.clickOnLoginBtn()



