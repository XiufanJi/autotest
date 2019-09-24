import unittest
from Utils.appium_config import DriverClient
from Utils.netease.login import getlogin_method
from Utils.netease.versioncheck import versioncheck
from Utils.netease.authorize import authorize
from time import sleep
from appium import webdriver
from Utils.action_config import action


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

    def test_a_login(self):
        # use import public utils
        authorize().authorize()
        # use mobile login method
        getlogin_method().login_with_mobile()
        # shut down version upgrade pop window
        self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
        sleep(THINK_TIME)
        versioncheck().versioncheck()
        sleep(THINK_TIME)
        # click "歌单广场"
        # self.driver.tap([(1146, 1227), (1384, 1312)], 100)
        # self.driver.wait_activity(".activity.MainPlaylistActivity", THINK_TIME)
        # scroll = self.driver.find_element_by_id("com.netease.cloudmusic:id/akt").size
        # print("获取到的滑动区域长宽分别为:{0:.2f},{1:.2f}".format(scroll["height"], scroll["width"]))
        # start_x, end_x, y = scroll["width"] / 10, scroll["width"] / 2, scroll["height"] / 2
        # action().swipe_left(start_x=start_x, end_x=end_x, y=y)
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












