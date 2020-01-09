import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from baseModules.file_locators import *


class browser_Handler:
    def launch_Browser(self, browser):
        if browser == "chrome":
            driver_path = "../externalFiles/chromedriver.exe"
            self.driver = webdriver.Chrome(executable_path=driver_path)
            self.driver.maximize_window()
            # return self.driver
        elif browser == "firefox":
            driver_path = "../externalFiles/geckodriver.exe"
            self.driver = webdriver.Firefox(executable_path=driver_path)
            self.driver.maximize_window()
            # return self.driver

    def open_Verto_Application(self, url):
        self.driver.get(url)
        time.sleep(10)

    def close_Browser(self):
        self.driver.close()

    def switch_Window(self):
        all_tabs = self.driver.window_handles
        for tab in all_tabs:
            if(self.driver.)

    def get_driver(self):
        return self.driver


if __name__ == '__main__':
    browser = browser_Handler()
    browser.launch_Browser("chrome")
    browser.open_Verto_Application("https://uat.vertofx.com")
    browser.close_Browser()
