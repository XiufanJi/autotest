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

    @unittest.skip("pause")
    def test_b_mymusic(self):
        try:
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
            # sleep(THINK_TIME)
            # TouchAction(self.driver).tap(x=1004, y=1813).perform()
            # """点击收藏按钮：暂时不能通过按钮的颜色变化来进行判断，没有查到相关资料"""
            # select = self.driver.find_element_by_accessibility_id("红心").is_selected()
            # print("收藏按钮是否被选中：%s" % select)
            # if select:
            #     self.driver.find_element_by_accessibility_id("下一首").click()
            # else:
            #     self.driver.find_element_by_accessibility_id("红心").click()
            # """滑动到当前页面不可见的某个元素进行元素定位的方法使用"""
            # el = self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true))."
            #                                                 "scrollIntoView(new UiSelector().text(\"听听\"))")
            # el.click()
            # self.driver.wait_activity(".activity.MainPageCircleLiveActivity", THINK_TIME)
            # self.assertEquals(".activity.MainPageCircleLiveActivity", self.driver.current_activity)
            print("当前页面的活动名称：%s" % self.driver.current_activity)
            # self.assertEquals(".activity.PlayListActivity", self.driver.current_activity)
            # musicList = self.driver.find_elements_by_id("com.netease.cloudmusic:id/ry")
            # for i in musicList:
            #     print("获取到的页面数据有：")
            #     print(i.text,end=" ")
            # if musicList.__len__()!=0:
            #     musicList[7].click()
            #     # targetList = choice(musicList)
            #     # print("任意选中的列表名称为：%s" % targetList.text)
            #     # if targetList!=None:
            #     #     targetList.click()
            # else:
            #     pass
        except Exception as e:
            raise e
