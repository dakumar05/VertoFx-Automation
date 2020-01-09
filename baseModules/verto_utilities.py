from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Utilities:
    def __init__(self, driver):
            self.driver = driver
    #        self.driver.execute_script("arguments[0].click();", element)

    def DynamicWait(self,  locator):
        waittime = WebDriverWait(self.driver, 60)
        waittime.until(EC.presence_of_element_located(By.CSS_SELECTOR, locator))
        waittime.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))

    def DynamoWait(self, By, locator):
        waittime = WebDriverWait(self.driver, 60)
        waittime.until(EC.presence_of_element_located((By, locator)))
        waittime.until(EC.element_to_be_clickable((By, locator)))

    def DynamicWaitele(self, elementr):
        waittime = WebDriverWait(self.driver, 60)
        waittime.until(EC.visibility_of(elementr))

    def progress_Spinner_Wait(self):
        if self.check_progrssspinner() is True:
            waittime = WebDriverWait(self.driver, 60)
            waittime.until(EC.invisibility_of_element(
                self.driver.find_element_by_css_selector(".ngx-foreground-spinner center-center")))

    def check_progrssspinner(self):
        try:
            self.driver.find_element_by_css_selector(".ngx-foreground-spinner center-center")
        except NoSuchElementException:
            return False
        return True

    def frame_switch(self, css_selector):
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector(css_selector))

    def switch_window(self):
        handles = self.driver.window_handles
        size = len(handles)
        for x in range(size):
            if handles[x] != self.driver.current_window_handle:
                self.driver.switch_to.window(handles[x])
