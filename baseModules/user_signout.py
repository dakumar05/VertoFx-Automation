def logout(self):
    utility = Utilities(self.driver)
    utility.Click_Element(self.driver.find_element_by_css_selector(self.logoutdd))
    utility.DynamicWait(self.lgout)
    utility.Click_Element(self.driver.find_element_by_css_selector(self.lgout))
    utility.DynamicWait(self.SignInBtn)