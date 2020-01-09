import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from baseModules.verto_utilities import *


class personal_Details:
    def __init__(self):
        self.stpr_nextbtn = ".btn.btn-sm.btn-custom-navy"
        self.owner_fname = "ownerFirstName"
        self.owner_lname = "ownerLastName"
        self.owner_phone = "ownerTelephone"
        self.owner_email = "ownerEmail"
        self.owner_dob = "ownerDob"
        self.ownrshp_percent = "percentOwnershipInCompany"
        self.personal_addr = "personalAddressLine1"
        self.personal_pin = "personalZipcode"
        self.personal_city = "personalAddressLine2"
        self.personal_country = "personalCountry"
        self.form_nextbtn = ".btn.btn-sm.btn-custom-navy[type='submit']"

    def fill_Personal_Details(self, browser, fname, lname, tel, dob, email, ownership, peraddr, perpin, city, country):
        util = Utilities(browser.get_driver())
        # assert browser.get_driver().find_element_by_name(self.owner_fname).get_Attribute("value") == fname
        # assert browser.get_driver().find_element_by_name(self.owner_lname).get_Attribute("value") == lname
        # assert browser.get_driver().find_element_by_name(self.owner_phone).get_Attribute("value") == tel
        # assert browser.get_driver().find_element_by_name(self.owner_email).get_Attribute("value") == email
        browser.get_driver().find_element_by_name(self.owner_dob).send_keys(dob)
        browser.get_driver().find_element_by_name(self.owner_dob).send_keys(Keys.ENTER)
        browser.get_driver().find_element_by_name(self.ownrshp_percent).send_keys(ownership)
        browser.get_driver().find_element_by_css_selector(self.stpr_nextbtn).click()
        # util.DynamoWait(By.NAME, self.personal_addr)
        time.sleep(10)
        browser.get_driver().find_element_by_name(self.personal_addr).send_keys(peraddr)
        browser.get_driver().find_element_by_name(self.personal_pin).send_keys(perpin)
        browser.get_driver().find_element_by_name(self.personal_city).send_keys(city)
        select_country = Select(browser.get_driver().find_element_by_name(self.personal_country))
        select_country.select_by_value(country)
        form_submit = browser.get_driver().find_elements_by_css_selector(self.form_nextbtn)
        form_submit[0].click()
        # util.progress_Spinner_Wait()
        time.sleep(10)


if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path="../externalFiles/chromedriver.exe")
    browser.maximize_window()
    browser.get("https://uat.vertofx.com/auth/complete-profile/JDJhJDEwJGdWWWRCUE42dWRMVTVkTVVyRExLWGU")
    time.sleep(10)
    new_var = personal_Details(browser)
    new_var.fill_Personal_Details(fname="Anil",
                                  lname="Kumar",
                                  tel="051130220",
                                  dob="05-10-1993",
                                  email="anil0501@mailinator.com",
                                  ownership="100",
                                  peraddr="addr1",
                                  perpin="998811",
                                  city="Pune",
                                  country="India")
