import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class personal_Docs:
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
    upldbtn = self.driver.find_element_by_css_selector(self.UploadBtn)
    UpldInp = self.driver.find_element_by_css_selector(self.UploadInp)
    UpldInp.send_keys(os.getcwd() + path)
    util.Click_Element(upldbtn)
    util.WaitForProgressSpinner()



def UploadPersonalDoc(self, doc1):
    docudd = self.driver.find_element_by_css_selector(self.docdd)
    util.Click_Element(docudd)
    Select(docudd).select_by_ v= =ible_text(doc1)
    self.Uploadfile("/Data/driphydro.jfif")
    util.WaitForProgressSpinner()
'''

if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path="../externalFiles/chromedriver.exe")
    browser.maximize_window()
    browser.get("https://uat.vertofx.com/auth/complete-profile/JDJhJDEwJGdWWWRCUE42dWRMVTVkTVVyRExLWGU")
    time.sleep(10)
    new_var = personal_Docs(browser)
    new_var.skip_Upload_Documents()
