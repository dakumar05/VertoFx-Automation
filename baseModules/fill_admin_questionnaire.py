import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class admin_Questionnaire:
    def __init__(self):
        self.answer_field = "input[placeholder='Answer']"
        self.dashbrd_btn = ".btn.btn-sm.btn-custom-navy"

    def fill_Questionier(self, browser, ans):
        answr = browser.get_driver().find_elements(By.CSS_SELECTOR, self.answer_field)
        count = 0
        for i in len(answr):
            count = count + 1
            answr[i].send_keys(ans + " " + str(count))
        browser.get_driver().find_element_by_css_selector(self.dashbrd_btn).click()


if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path="../externalFiles/chromedriver.exe")
    browser.maximize_window()
    browser.get("https://uat.vertofx.com/auth/complete-profile/JDJhJDEwJGdWWWRCUE42dWRMVTVkTVVyRExLWGU")
    time.sleep(10)
    new_var = admin_questionnaire(browser)
    new_var.fill_Questionier("ASD", "XYZ")
