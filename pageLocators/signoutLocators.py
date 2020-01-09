from selenium.webdriver.common.by import By

from BaseFiles.VertoUtil import Utilities



def __init__(self, driver):
    self.driver = driver
    self.SignInBtn = ".btn.btn-custom-navy.w-100[type='submit']"
    self.logoutdd = ".inline.v-mid.text-left"
    self.lgout = "a[href='/auth/logout']"


