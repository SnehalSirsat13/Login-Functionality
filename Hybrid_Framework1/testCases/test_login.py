import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):

        self.logger.info("***************** Test_001_Login ********************")
        self.logger.info("***************** Verifying Home Page Title ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="nopCommerce demo store. Login":
            self.driver.close()
            self.logger.info("***************** Home Page Title Test is Passed ********************")
            assert True
        else:
         self.logger.info("***************** Home Page Title Test is Failed ********************")
         assert False


    def test_Login(self,setup):
        self.logger.info("***************** Verifying Login Test ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.driver.close()
        self.logger.info("***************** Login Test is passed ********************")
        assert True
        else
        self.logger.info("***************** Login Test is Failed ********************")
    assert False








