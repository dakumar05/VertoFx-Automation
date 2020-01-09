import time
from selenium import webdriver
from baseModules.verto_utilities import *


class beneficial_Owner:
    def __init__(self):
        self.beneficial_owner = ".mat-radio-outer-circle"
        self.form_nextbtn = ".btn.btn-sm.btn-custom-navy"
        self.form_backbtn = ".btm.btn-sm.btn-custom-navy-outline.m-r-10"

    def select_Beneficiary(self, browser, isBeneficialOwner, **isAdmin):
        util = Utilities(browser.get_driver())
        radbtn = browser.get_driver().find_elements(By.CSS_SELECTOR, self.beneficial_owner)
        if isBeneficialOwner:
            radbtn[0].click()
            browser.get_driver().find_element_by_css_selector(self.form_nextbtn).click()
            # util.progress_Spinner_Wait()
            time.sleep(10)
        elif isAdmin["admin"]:
            radbtn[1].click()
            radbtn = browser.get_driver().find_elements(By.CSS_SELECTOR, self.beneficial_owner)
            radbtn[2].click()
            browser.get_driver().find_element_by_css_selector(self.form_nextbtn).click()
            # util.progress_Spinner_Wait()
            time.sleep(10)
        else:
            radbtn[1].click()
            radbtn = browser.get_driver().find_elements(By.CSS_SELECTOR, self.beneficial_owner)
            radbtn[3].click()
            browser.get_driver().find_element_by_css_selector(self.form_nextbtn).click()
            # util.progress_Spinner_Wait()
            time.sleep(10)


if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path="../externalFiles/chromedriver.exe")
    browser.maximize_window()
    browser.get("https://uat.vertofx.com/auth/complete-profile/JDJhJDEwJGdWWWRCUE42dWRMVTVkTVVyRExLWGU")
    time.sleep(10)
    new_var = beneficial_Owner(browser)
    new_var.select_Beneficiary(isBeneficialOwner=False, admin=False)
