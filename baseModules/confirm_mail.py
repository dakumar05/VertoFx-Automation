import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from baseModules.verto_utilities import *
from baseModules.launch_application import *


class mail_Confirmation:
    def __init__(self):
        self.mails = "//a[@tabindex='0']"
        self.mailframe = "//iframe[@id='msg_body']"
        self.verlink_uat = "//a[contains(@href, 'uat.vertofx.com/auth/complete-profile/')]"
        self.verlink_staging = "//a[contains(@href, 'staging.vertofx.com/auth/complete-profile/')]"

    def confirm_Mail(self, browser, branch, email):
        # browser.get_driver().find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        mail_url = "https://www.mailinator.com/v3/index.jsp?zone=public&query="
        util = Utilities(browser.get_driver())
        browser.open_Verto_Application(mail_url + email)
        time.sleep(10)
        mails_list = browser.get_driver().find_elements(By.XPATH, self.mails)
        for i in mails_list:
            if i.text.strip() == "Welcome to Verto!":
                i.click()
                break
        time.sleep(10)
        msg_body = browser.get_driver().find_element_by_xpath(self.mailframe)
        browser.get_driver().switch_to.frame(msg_body)
        # if branch == "uat":
        browser.get_driver().find_element_by_xpath(self.verlink_uat).click()
        time.sleep(10)
        # elif branch == "staging":
        #     browser.get_driver().find_element_by_xpath(self.verlink_staging).click()
        #     time.sleep(10)


if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path="../externalFiles/chromedriver.exe")
    browser.maximize_window()
    var = mail_Confirmation(browser)
    var.confirm_Mail("anil0601")
