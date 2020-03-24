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
        battery = self.driver.battery_info
        print("手机当前的电量和状态为：{0}*100%,{1}".format(battery["level"], battery["state"]))
        self.assertEquals(".activity.HomePageActivity", self.driver.current_activity)