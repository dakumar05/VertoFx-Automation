def sign_in(self, mail, password, otp):
    utility = Utilities(self.driver)
    self.driver.find_element_by_name(self.email).send_keys(mail)
    self.driver.find_element_by_name(self.password).send_keys(password)
    utility.Click_Element(self.driver.find_element_by_css_selector(self.SignInBtn))
    utility.DynamicWait(By.NAME, self.OTP)
    self.driver.find_element_by_name(self.OTP).send_keys(otp)
    utility.Click_Element(self.driver.find_element_by_css_selector(self.ProceedBtn))
    utility.WaitForProgressSpinner()


if __name__ == "__main__":
    browser_Setup("uat", browser1)
    test_login()
    test_close_browser()
