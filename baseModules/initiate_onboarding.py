import time
from selenium.webdriver.common.by import By
from baseModules.verto_utilities import Utilities


class onboarding:
    def __init__(self):
        self.signup = "//a[@href='/auth/register']"

    def initiate_Signup(self, browser):
        util = Utilities(browser)
        browser.get_driver().find_element_by_xpath(self.signup).click()
        time.sleep(10)
