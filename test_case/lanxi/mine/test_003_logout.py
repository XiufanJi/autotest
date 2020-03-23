import unittest
from Utils.appium_config import DriverClient as DC
from base.mobileApp.lanxi.logoutBase import logoutBase


class logout(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DC().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close_app()
        cls.driver.quit()

    # @unittest.skip("skip it")
    def test_logout(self):
        checkout = logoutBase()
        checkout.logout()
        self.assertEquals(".activity.HomePageActivity", self.driver.current_activity)