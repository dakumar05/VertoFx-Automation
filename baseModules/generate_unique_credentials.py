import sys
from selenium import webdriver
from baseModules.file_locators import *

global browser
global url
url = str(sys.argv[2])
browser = str(sys.argv[1])


def open_browser(self, url, browser):
    driver_path = filePaths.GetBrowserPath(Browserarg)
    if browser == "chrome":
        self.driver = webdriver.Chrome(executable_path=driver_path)

    self.driver.maximize_window()
    self.driver.get(url)
    return self.driver


def close_browser(self):
    self.driver.close()