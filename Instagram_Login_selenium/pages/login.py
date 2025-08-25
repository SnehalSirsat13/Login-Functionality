
from selenium.webdriver.common.by import By


class LoginPage:
    username_text_filed_by_name="//input[@aria-label='Phone number, username, or email']"
    password_text_filed_xpath_by_xpath="input[@class='_aa4b _add6 _ac4d _ap35']"
    login_btn_xpath_by_xpath="//body/div[@id='mount_0_0_w9']/div/div/div[@class='x9f619 x1n2onr6 x1ja2u2z']/div[@class='x78zum5 xdt5ytf x1n2onr6 x1ja2u2z']/div[@class='x78zum5 xdt5ytf x1n2onr6 xat3117 xxzkxad']/div[@class='x78zum5 xdt5ytf x1t2pt76 x1n2onr6 x1ja2u2z x10cihs4']/div[@class='x9f619 xvbhtw8 x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x1qjc9v5 x1oa3qoh x1qughib']/div[@class='x10o80wk x14k21rp xh8yej3']/section[@class='x78zum5 xdt5ytf x1iyjqo2 xg6iff7']/main[@role='main']/div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xx7atzb x1n2onr6 x6ikm8r x10wlt62 x1iyjqo2 x2lwn1j xeuugli x1q0g3np xqjyukv x6s0dn4 x1oa3qoh xl56j7k']/div[@class='x5n08af x78zum5 xdt5ytf x1iyjqo2 xl56j7k x7qam4e x14vqqas x15lw1kp x1dc814f x1owpceq xh8yej3']/div[@class='x6s0dn4 xvbhtw8 x1pmru9 x1yvgwvq x1dqoszc x1ixjvfu xhk4uv x146dn1l x11t77rh x1thhq0t xf6uls8 x13fuv20 x1qgpocp xu3j5b3 xne9koi x1q0q8m5 xxrrrr8 x26u7qi xyyqvqm x178xt8z xm81vs4 xso031l xy80clv x9f619 x78zum5 xjl7jj xdt5ytf x2lah0s xln7xf2 xk390pu xdj266r x11i5rnm x1mh8g0r xyorhqc xzboxd6 x889kno x4uap5 x1a8lsjc xkhd6sd x1n2onr6 x11njtxf']/div[@class='xod5an3 x1dc814f xh8yej3']/div/form[@id='loginForm']/div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xqui205 x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']/div[3]"
    def __init__(self,driver):
        self.driver=driver


    def set_username(self,username):
        # self.driver.find_element(By.XPATH,self.username_text_filed_xpath_by_xpath).clear()
        self.driver.find_element(By.XPATH,self.username_text_filed_xpath_by_xpath).send_keys(username)


    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.password_text_filed_xpath_by_xpath).clear()
        self.driver.find_element(By.XPATH,self.password_text_filed_xpath_by_xpath).send_keys(password)

    def click_on_login_btn(self):
        self.driver.find_element(By.XPATH,self.login_btn_xpath_by_xpath).click()
