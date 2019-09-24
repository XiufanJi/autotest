import unittest
from Utils.appium_config import DriverClient
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from random import randint


THINK_TIME = 3
randint(1, 100)
keys = "new album"+randint
class createlist(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        pass

    def test_d_creatlist(self):
        """click mine button"""
        try:
            self.driver.find_element_by_accessibility_id("我的音乐").click()
            sleep(THINK_TIME)
            """先将弹出的提示框点击关掉"""
            TouchAction(self.driver).tap(x=1108, y=902).perform()
            """find creat button"""
            self.driver.find_element_by_id("com.netease.cloudmusic:id/c8").click()
            """make sure if pop window is appear"""
            new_Mix=self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"New Mix\")")\
                .is_displayed()
            print("歌单新增弹框是否出现：%s" % new_Mix)
            if new_Mix:
                self.driver.find_element_by_id("android:id/input").send_keys(keys)
                # self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"type in Mix title\")")\
                #     .send_keys("new album")
                sleep(THINK_TIME)
                self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"SUBMIT\")").click()
                sleep(THINK_TIME)
                self.driver.wait_activity(".activity.PlayListActivity", THINK_TIME)
                """back to home page"""
                self.driver.find_element_by_accessibility_id("Navigate up").click()
                self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
                new_album = self.driver.find_element_by_android_uiautomator("new UiSelector().\
                textContains(\"new album\")").is_displayed()
                print("新增歌单中是否有刚才新增的歌单名称：%s" % new_album)
                self.assertEquals(True, new_album)
            else:
                print("未找到对应元素，未弹出新增框")
                self.fail("未找到对应元素")
        except Exception as e:
            raise e










