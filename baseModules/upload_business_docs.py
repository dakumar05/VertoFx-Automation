import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class business_Docs:
    def __init__(self):
        self.docdd = "select.form-control"
        self.UploadInp = "input[accept='*']"
        self.UploadBtn = ".m-t-5.btn.btn-sm.btn-custom-navy"
        self.form_backbtn = ".btn.btn-sm.btn-custom-navy-outline.m-r-10"
        self.form_skipbtn = ".btn.btn-sm.btn-custom-navy-outline.m-r-10"

    def skip_Upload_Documents(self, browser):
        button = browser.get_driver().find_elements(By.CSS_SELECTOR, self.form_skipbtn)
        button[1].click()

'''
    def Uploadfile(self, path):
        util = Utilities(self.driver)
        upldbtn = self.driver.find_element_by_css_selector(self.UploadBtn)
        UpldInp = self.driver.find_element_by_css_selector(self.UploadInp)
        UpldInp.send_keys(os.getcwd() + path)
        util.Click_Element(upldbtn)
        util.WaitForProgressSpinner()

    def UploadBusDocuments(self, doc1):
        util = Utilities(self.driver)
        docudd = self.driver.find_element_by_css_selector(self.docdd)
        util.Click_Element(docudd)
        Select(docudd).select_by_visible_text(doc1)
        self.Uploadfile("/Data/drip.png")
        util.WaitForProgressSpinner()
'''

if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path="../externalFiles/chromedriver.exe")
    browser.maximize_window()
    browser.get("https://uat.vertofx.com/auth/complete-profile/JDJhJDEwJGdWWWRCUE42dWRMVTVkTVVyRExLWGU")
    time.sleep(10)
    new_var = business_Docs(browser)
    new_var.skip_Upload_Documents()
