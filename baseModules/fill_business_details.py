from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from baseModules.verto_utilities import *
import time


class business_Details_Form:
    def __init__(self):
        self.bsn_cntry = "country"
        self.bsn_name = "companyName"
        self.comp_num = "companyNumber"
        self.bsn_website = "companyWebsite"
        self.bsn_address = "addressLine1"
        self.bsn_city = "addressLine2"
        self.bsn_city_pin = "zipcode"
        self.bsn_type = "companyType"
        self.bsn_cat = "companyCategory"
        self.role = "companyRole"
        self.emp_num = "companyNumberOfEmployees"
        self.stpr_nextbtn1 = ".btn.btn-sm.btn-custom-navy[type='button']"
        self.stpr_backbtn = ".btm.btn-sm.btn-custom-navy-outline[type='button']"
        self.stpr_nextbtn2 = ".btn.btn-sm.btn-custom-navy.m-l-10[type='button']"
        self.confm_chkbox = ".mat-checkbox-inner-container"
        self.form_nextbtn = ".btn.btn-sm.btn-custom-navy[type='submit']"

    def fill_Business_Details(self, browser, bcntry, bname, compnum, bwebsite, baddress, bpin, bcity, btype, bcat,
                              urole, ecount):
        util = Utilities(browser.get_driver())
        select_country = Select(browser.get_driver().find_element_by_name(self.bsn_cntry))
        select_country.select_by_value(bcntry)
        browser.get_driver().find_element_by_name(self.bsn_name).send_keys(bname)
        browser.get_driver().find_element_by_name(self.comp_num).send_keys(compnum)
        browser.get_driver().find_element_by_name(self.bsn_website).send_keys(bwebsite)
        browser.get_driver().find_element_by_css_selector(self.stpr_nextbtn1).click()
        # util.DynamoWait(By.NAME, self.bsn_address)
        time.sleep(10)
        browser.get_driver().find_element_by_name(self.bsn_address).send_keys(baddress)
        browser.get_driver().find_element_by_name(self.bsn_city_pin).send_keys(bpin)
        browser.get_driver().find_element_by_name(self.bsn_city).send_keys(bcity)
        browser.get_driver().find_element_by_css_selector(self.stpr_nextbtn2).click()
        select_btype = Select(browser.get_driver().find_element_by_name(self.bsn_type))
        select_btype.select_by_value(btype)
        select_bcat = Select(browser.get_driver().find_element_by_name(self.bsn_cat))
        select_bcat.select_by_value(bcat)
        select_role = Select(browser.get_driver().find_element_by_name(self.role))
        select_role.select_by_value(urole)
        browser.get_driver().find_element_by_name(self.emp_num).send_keys(ecount)
        browser.get_driver().find_element_by_css_selector(self.confm_chkbox).click()
        browser.get_driver().find_element_by_css_selector(self.form_nextbtn).click()
        time.sleep(10)
        # util.progress_Spinner_Wait()


if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path="../externalFiles/chromedriver.exe")
    browser.maximize_window()
    browser.get("https://uat.vertofx.com/auth/complete-profile/JDJhJDEwJGdWWWRCUE42dWRMVTVkTVVyRExLWGU")
    time.sleep(10)
    new_var = business_Details_Form()
    new_var.fill_Business_Details(browser, bcntry="India",
                                  bname="Abc LLC",
                                  compnum="11EFG",
                                  bwebsite="website.com",
                                  baddress="101, Bk Street",
                                  bpin="229933",
                                  bcity="Pune",
                                  btype="plc",
                                  bcat="Beauty and fragrances",
                                  urole="Director",
                                  ecount="100")
