import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select


class Add_Customer_Page:
    link_customer_menu_xpath = "//body/div[@class='wrapper']/aside[@class='main-sidebar sidebar-dark-primary elevation-4']/div[@class='sidebar']/nav[@class='mt-2']/ul[@role='menu']/li[4]/a[1]"
    link_customer_menuoption_xpath = "//li[@class='nav-item has-treeview menu-is-opening menu-open']//li[1]//a[1]"
    link_addnew_xpath = "//a[normalize-space()='Add new']"
    text_email_id = "Email"
    text_password_id = "Password"
    text_fname_id = "FirstName"
    text_lname_id = "LastName"
    rdo_gender_male_id = "Gender_Male"
    rdo_gender_female_id = "Gender_Female"
    text_companyname_id = "Company"
    text_ahmed_elegendy_id = "customer_attribute_1"
    chbx_tax_exempt_id = "IsTaxExempt"
    newsletter_cusrole_list_xpath = "//span[@aria-expanded='true']//input[@role='searchbox']"
    cusrole_guests_xpath = "//span[@aria-expanded='true']//ul[@class='select2-selection__rendered']"
    cusrole_administration_xpath = ""
