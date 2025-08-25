import time

#from test_data.test_data_login_page import Test_Data
from config.setup import setup
from pages.login import Login_page
from utilities.readProperties import Readconfig
from utilities.custom_logger import LogGen
class Test_verify_login_page:
    logger = LogGen.loggen()
    baseUrl =Readconfig.getApplicationURL()
    username =Readconfig.getUsername()
    password =Readconfig.getPassword()
    def test_verify_login_functionality_banking(self,setup):
        self.logger.info("*******Test Case Execution start *******")
        self.logger.info("*******To Verify the Login Functionality *******")

        expected_result="GTPL Bank Manager HomePage"
        driver = setup
        self.logger.info("*******Webdriver launched successfully *******")
        driver.get(self.baseUrl)
        self.logger.info("*******Url Open Successfully in the browser *******")
        login = Login_page(driver)
        self.logger.info("*******Created Object of Login success *******")
        print(self.username)
        login.setUsername(self.username)
        self.logger.info("*******Username set successfully in the textfile *******")
        time.sleep(2)
        login.setPassword(self.password)
        self.logger.info("*******Password set successfully in the textfile *******")
        time.sleep(2)
        login.clickOnLoginBtn()
        self.logger.info("*******Click on the login Done *******")
        time.sleep(3)
        act_result=driver.title

        if act_result ==expected_result:
            assert True
            self.logger.info("*******Test Case Pass *******")
        else:
            assert False
            self.logger.info("*******Test Case Failed *******")

        self.logger.info("*******Test Case Execution End *******")

        time.sleep(10)