import unittest
from Utils.appium_config import DriverClient
from Utils.netease.login import getlogin_method
from Utils.netease.versioncheck import versioncheck
from time import  sleep



THINK_TIME = 3
WAIT_TIME = 30
class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_a_login(self):
        # use import public utils
        getlogin_method().login_with_guest()
        # locate recommend pop window
        # try:
        #     recommend = self.driver.find_element_by_id("com.netease.cloudmusic:id/content").is_displayed()
        #     print("推荐弹框是否出现：%s " % recommend)
        #     if recommend:
        #         # if recommend window is show,then click no interest button to shut it down
        #         self.driver.find_element_by_id("com.netease.cloudmusic:id/bsm").click()
        #     else:
        #         pass
        # except Exception as e:
        #     raise e
        sleep(THINK_TIME)
        versioncheck().versioncheck()











