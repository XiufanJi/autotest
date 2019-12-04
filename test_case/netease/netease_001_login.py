import unittest
from Utils.appium_config import DriverClient
from Utils.netease.login import getlogin_method
from Utils.netease.versioncheck import versioncheck
from Utils.netease.authorize import authorize
from time import sleep
from appium import webdriver
from Utils.public_action import action


THINK_TIME = 5
WAIT_TIME = 30
class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     # cls.driver.quit()
    #     pass
    # @unittest.skip("skip now")
    def test_a_login(self):
        # use import public Utils
        authorize().authorize()
        """如果使用游客角色登录，则需要加上下面的方法调用"""
        sleep(WAIT_TIME)
        authorize().click_agreement()
        getlogin_method().login_with_guest()
        self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
        sleep(THINK_TIME)
        versioncheck().versioncheck()
        self.assertEquals(".activity.MainActivity", self.driver.current_activity)












