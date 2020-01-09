from baseModules.launch_application import broswer_Handler
import pytest
import argparse


class TestLaunch:
    bswr = "test1"
    brn = "test2"

    @pytest.fixture(scope="package")
    def get_browser(self, pytestconfig):
        return pytestconfig.getoption("browser")

    @pytest.fixture(scope="package")
    def get_branch(self, pytestconfig):
        return pytestconfig.getoption("branch")

    def test_launch(self, get_browser, get_branch):
        var = broswer_Handler()
        TestLaunch.brn = get_browser
        TestLaunch.bswr = get_branch
        print("Browser = ", TestLaunch.bswr)
        print("Branch = ", TestLaunch.brn)
        browser = var.launch_Browser(get_browser)
        var.open_Verto_Application(get_branch, browser)

    def test_2(self):
        print("Browser2 = ", self.bswr)
        print("Branch2 = ", self.brn)
        print("Browser2_1 = ", TestLaunch.bswr)
        print("Branch2_1 = ", TestLaunch.brn)
