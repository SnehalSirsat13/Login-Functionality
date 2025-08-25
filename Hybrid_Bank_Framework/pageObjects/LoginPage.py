from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    textbox_username_name="uid"
    text_password_name="password"
    button_login_xpath="//input[@name='btnLogin']"
    link_logout_linktext="Log out"


    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.NAME,self.textbox_username_name).clear()
        self.driver.find_element(By.NAME,self.textbox_username_name).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.text_password_name).clear()
        self.driver.find_element(By.NAME,self.text_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def ClickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()



