from Utils.netease.login import getlogin_method
from Utils.appium_config import DriverClient
import unittest

THINK_TIME = 3
WAIT_TIME = 30
class my_music(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def mymusic(self):
        pass
        # click Mine button in the home page
        self.driver.find_element_by_accessibility_id("我的音乐").click()
