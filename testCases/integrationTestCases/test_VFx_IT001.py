import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from testCases.integrationTestCases.test_getArguments import get_Arguments
from baseModules.launch_application import browser_Handler
from baseModules.initiate_onboarding import onboarding
from baseModules.activation_form import *
from baseModules.confirm_mail import *
from baseModules.fill_business_details import *
from baseModules.set_beneficiary import *
from baseModules.fill_personal_details import *
from baseModules.upload_business_docs import *
from baseModules.upload_personal_docs import *
# from baseModules.generate_unique_credentials import *
from baseModules.fill_admin_questionnaire import *
from baseModules.verto_utilities import *


class TestOnBoarding(get_Arguments):
    @pytest.fixture(scope="class")
    def get_Browser(self, pytestconfig):
        return pytestconfig.getoption("browser")

    @pytest.fixture(scope="class")
    def get_Branch(self, pytestconfig):
        return pytestconfig.getoption("branch")

    @pytest.fixture(scope="class")
    def setup(self, get_Browser, get_Branch):
        global browser
        browser = browser_Handler()
        browser.launch_Browser(get_Browser)
        browser.open_Verto_Application(get_Branch)
        yield
        browser.close_Browser()

    def test_Onboarding(self, setup, get_Branch):
        init_onboarding = onboarding()
        init_onboarding.initiate_Signup(browser)
        act_form = activation_Form()
        act_form.fill_Activation_Form(browser, fname="Anil",
                                      lname="Kumar",
                                      email="anil08022@mailinator.com",
                                      ccode="+91",
                                      phn="8022130220",
                                      pwd="Password@123")

        assert True

        cnf_mail = mail_Confirmation()
        cnf_mail.confirm_Mail(browser, get_Branch, "anil08022")

        assert True

        business_details = business_Details_Form()
        business_details.fill_Business_Details(browser,
                                               bcntry="India",
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

        assert True

        beneficiary = beneficial_Owner()
        beneficiary.select_Beneficiary(browser, isBeneficialOwner=True)

        assert True

        business_docs = business_Docs()
        business_docs.skip_Upload_Documents(browser)

        assert True

        personal_details = personal_Details()
        personal_details.fill_Personal_Details(browser,
                                               fname="Anil",
                                               lname="Kumar",
                                               tel="051130220",
                                               dob="05-10-1993",
                                               email="anil08022@mailinator.com",
                                               ownership="100",
                                               peraddr="addr1",
                                               perpin="998811",
                                               city="Pune",
                                               country="India")

        assert True

        personal_docs = personal_Docs()
        personal_docs.skip_Upload_Documents(browser)

        assert True

        questionnaire = admin_Questionnaire()
        questionnaire.fill_Questionier(browser, "Test Answer")

        assert True
