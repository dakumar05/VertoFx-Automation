import pytest
from baseModules.launch_application import *


class get_Arguments:
    browser = "browser"
    branch = "branch"
    @pytest.fixture()
    def get_browser(self, pytestconfig):
        return pytestconfig.getoption("browser")

    @pytest.fixture()
    def get_branch(self, pytestconfig):
        return pytestconfig.getoption("branch")

    def test_launch(self, get_browser, get_branch):
        get_Arguments.browser = get_browser
        get_Arguments.branch = get_branch
        '''var = broswer_Handler()
        browser = var.launch_Browser(get_browser)
        var.open_Verto_Application(get_branch, browser)'''