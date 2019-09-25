import unittest
from Utils.appium_config import DriverClient
from random import choice
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


THINK_TIME = 3
class editalbum(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        pass

    """若要与login单独联合执行，则需将注释的地方进行恢复"""
    def test_editalbunm(self):
        """查找歌单的编辑按钮"""
        try:
            # self.driver.find_element_by_accessibility_id("我的音乐").click()
            # sleep(THINK_TIME)
            # """先将弹出的提示框点击关掉"""
            # TouchAction(self.driver).tap(x=1108, y=902).perform()
            sleep(THINK_TIME)
            # albumlist=self.driver.find_elements_by_id("com.netease.cloudmusic:id/a16")
            """查询相应歌单对应的操作按钮"""
            self.driver.find_element_by_android_uiautomator("new UiSelector().textContains(\"new album\")\
            .fromParent(new UiSelector().resourceId(\"com.netease.cloudmusic:id/a16\"))").click()
            """找到编辑按钮"""
            self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"Edit Mix\")").click()
            """切换activity"""
            self.driver.wait_activity(".activity.EditPlayListActivity", THINK_TIME)
            """清除输入框内的内容并进行文字输入"""
            self.driver.find_element_by_id("com.netease.cloudmusic:id/apd").click()
            sleep(THINK_TIME)
            self.driver.find_element_by_id("com.netease.cloudmusic:id/api").clear()
            self.driver.find_element_by_id("com.netease.cloudmusic:id/api").send_keys("test")
            """点击save按钮"""
            self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"SAVE\")").click()
            """点击返回按钮返回主页面"""
            # sleep(THINK_TIME)
            self.driver.find_element_by_accessibility_id("Navigate up").click()
            self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
            edit_effect = self.driver.find_element_by_android_uiautomator("new UiSelector().textContains(\"test\")")\
                .is_displayed()
            print("页面上是否有修改后的歌单名：%s" % edit_effect)
            self.assertEquals(True, edit_effect)
        except Exception as e:
            raise e

