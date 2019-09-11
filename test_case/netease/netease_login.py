import unittest
from Utils.appium_config import DriverClient
from Utils.netease.login import getlogin_method
from Utils.netease.versioncheck import versioncheck
from Utils.netease.authorize import authorize
from time import sleep



THINK_TIME = 5
WAIT_TIME = 30
class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()


    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        pass
    def test_a_login(self):
        # use import public utils
        authorize().authorize()
        authorize().click_agreement()
        # use mobile login method
        getlogin_method().login_with_guest()
        # shut down version upgrade pop window
        self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
        sleep(THINK_TIME)
        versioncheck().versioncheck()
        self.assertEquals(".activity.MainActivity", self.driver.current_activity)
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












