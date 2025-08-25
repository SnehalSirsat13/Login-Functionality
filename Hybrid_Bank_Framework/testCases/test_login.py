import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_Login(self,setup):
        self.logger.info("************** Test_001_Login ************")
        self.logger.info("************** Verifying Login Page ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp =Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()
        if act_title==" GTPL Bank Manager HomePage ":
            assert True
            self.logger.info("************* Login Page Test is Passed*************")
        else:
            self.logger.info("*************** Login Page test is Failed ***********")
            assert False











