import time
from selenium.webdriver.support.select import Select
from baseModules.verto_utilities import *


class activation_Form:
    def __init__(self):
        self.signup = "Sign up"
        self.first_name = "firstName"
        self.last_name = "lastName"
        self.email = "email"
        self.cntry_code = "countryCode"
        self.phn_num = "phone"
        self.passwd = "password"
        self.cnf_passwd = "confirmPassword"
        self.refrl_code = " Have referral code? "
        self.signup_btn = ".btn.btn-custom-navy.w-100[type='submit']"

    def fill_Activation_Form(self, browser, fname, lname, email, ccode, phn, pwd):
        # util = Utilities(browser)
        browser.get_driver().find_element_by_name(self.first_name).send_keys(fname)
        browser.get_driver().find_element_by_name(self.last_name).send_keys(lname)
        browser.get_driver().find_element_by_name(self.email).send_keys(email)
        select = Select(browser.get_driver().find_element_by_name(self.cntry_code))
        select.select_by_value(ccode)
        browser.get_driver().find_element_by_name(self.phn_num).send_keys(phn)
        browser.get_driver().find_element_by_name(self.passwd).send_keys(pwd)
        browser.get_driver().find_element_by_name(self.cnf_passwd).send_keys(pwd)
        time.sleep(10)
        # browser.get_driver().find_element_by_css_selector(self.signup_btn).click()
        # util.progress_Spinner_Wait()
        # time.sleep(10)
