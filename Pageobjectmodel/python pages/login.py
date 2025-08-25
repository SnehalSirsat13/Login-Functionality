from selenium import webdriver
from selenium.webdriver.commom.by import By


class Login_page:
    username_text_filed_xpath_by_name="uid"
    password_text_filed_xpath_by_name = "password"
    login_btn_xpath_by_name = "btnLogin"
    def __init__(self,driver):
        self.driver=driver

        def setUsername(self, username):
            self.driver.find_element(By.NAME, self.username_textFeild_xpath_by_Name).clear()
            self.driver.find_element(By.NAME, self.username_textFeild_xpath_by_Name).send_keys(username)

        def setPassword(self, password):
            self.driver.find_element(By.NAME, self.password_textFeild_xpath_by_Name).clear()
            self.driver.find_element(By.NAME, self.password_textFeild_xpath_by_Name).send_keys(password)

        def clickOnLoginBtn(self):
            self.driver.find_element(By.NAME, self.login_btn_xpath_by_Name).click()

