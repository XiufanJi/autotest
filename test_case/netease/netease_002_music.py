from Utils.appium_config import DriverClient
import unittest
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.common.multi_action import MultiAction
from Utils.action_config import action
from random import choice

THINK_TIME = 3
WAIT_TIME = 30
class my_music(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.quit()
    """选择歌单进行歌曲播放测试"""
    @unittest.skip("pause")
    def test_01_playmusic(self):
        try:
            # guest 账号下登录时的操作
            # click Mine button in the home page
            sleep(THINK_TIME)
            self.driver.find_element_by_accessibility_id("我的音乐").click()
            sleep(THINK_TIME)
            """先将弹出的提示框点击关掉"""
            TouchAction(self.driver).tap(x=1108, y=902).perform()
            sleep(THINK_TIME)
            """点击歌单"""
            self.driver.find_element_by_android_uiautomator("new UiSelector().\
                                    resourceId(\"com.netease.cloudmusic:id/a6b\")").click()
            self.driver.wait_activity(".activity.PlayListActivity", THINK_TIME)
            print("当前所在页面的活动名称是：%s" % self.driver.current_activity)
            """获取歌曲列表中的歌曲名称"""
            playlist = self.driver.find_elements_by_android_uiautomator("new UiSelector().\
                                                       resourceId(\"com.netease.cloudmusic:id/a38\")")
            """将歌曲名称打印出来"""
            for i in playlist:
                print("歌曲列表中的歌曲名称为：%s" % i.text)
            self.driver.find_element_by_android_uiautomator("new UiSelector().\
                                            resourceId(\"com.netease.cloudmusic:id/a38\").\
                                            text(\"So:Lo\")").click()
            sleep(THINK_TIME)
            """先将弹出的引导框页面点击关掉"""
            self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"OK\")").click()
            sleep(THINK_TIME)
            # size = action().get_window_size()
            TouchAction(self.driver).tap(x=1004, y=1813).perform()
            """判断是否播放成功：通过播放进度条来进行判断，若成功，则进度条时间不会等于0"""
            time = self.driver.find_element_by_id("com.netease.cloudmusic:id/r6").text
            self.assertNotEqual(time, "00:00")
            """点击页面上的返回按钮"""
            for i in range(2):
                self.driver.find_element_by_accessibility_id("Navigate up").click()
                sleep(THINK_TIME)
            self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
            print("当前页面的活动名称：%s" % self.driver.current_activity)
        except Exception as e:
            raise e

    """搜索歌曲并对结果页面进行上下滑动测试"""
    @unittest.skip("暂不测试")
    def test_02_searchmusic(self):
        # click search button
        try:
            self.driver.find_element_by_accessibility_id("我的音乐").click()
            sleep(THINK_TIME)
            """先将弹出的提示框点击关掉"""
            TouchAction(self.driver).tap(x=1108, y=902).perform()
            print("搜索按钮当前所处页面的活动名称为：%s" % self.driver.current_activity)
            # sleep(THINK_TIME)
            """make sure search button is show or not"""
            search = self.driver.find_element_by_accessibility_id("Search")
            flag = search.is_displayed()
            if flag:
                search.click()
                self.driver.wait_activity(".activity.SearchActivity", THINK_TIME)
                # locate search edit box
                sleep(THINK_TIME)
                edit = self.driver.find_element_by_id("com.netease.cloudmusic:id/search_src_text")
                item = "million years ago"
                edit.send_keys(item)
                # locate search button
                self.driver.find_element_by_id("com.netease.cloudmusic:id/c8e").click()
                sleep(THINK_TIME)
                """use swipe down method"""
                is_bottom = action().top_bottom("down")
                is_top = action().top_bottom("up")
                # self.driver.shake()
                self.assertEquals(True, is_bottom)
                self.assertEquals(True, is_top)
                """点击页面上的返回按钮"""
                for i in range(2):
                    self.driver.find_element_by_accessibility_id("Collapse").click()
                    sleep(THINK_TIME)
                """返回我的音乐首页"""
                self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
                print("当前页面的活动名称是:%s" % self.driver.current_activity)
                self.assertEquals(".activity.MainActivity", self.driver.current_activity)
            else:
                pass
        except Exception as e:
            raise e
