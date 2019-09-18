from Utils.appium_config import DriverClient
import unittest
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from Utils.action_config import action

THINK_TIME = 3
WAIT_TIME = 30
class my_music(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.quit()

    # @unittest.skip("don't know how to locate element----pause")
    def test_b_mymusic(self):
        try:
            # click Mine button in the home page
            # self.driver.find_element_by_accessibility_id("我的音乐").click()
            # choose no.1 music list: i don't know how to locate this list , tried a lot ,still none sense
            # self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
            """关闭弹出的提示信息"""
            # TouchAction(self.driver).tap(x=1201, y=804).perform()
            sleep(THINK_TIME)
            """滑动到当前页面不可见的某个元素进行元素定位的方法使用"""
            el = self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true))."
                                                            "scrollIntoView(new UiSelector().text(\"听听\"))")
            el.click()
            self.driver.wait_activity(".activity.MainPageCircleLiveActivity", THINK_TIME)
            self.assertEquals(".activity.MainPageCircleLiveActivity", self.driver.current_activity)

            """点击播放列表"""
            # self.driver.find_element_by_accessibility_id("播放列表").click()
            # sleep(THINK_TIME)
            # while True:
            #     action().top_bottom("down")
            #     playlist = self.driver.find_elements_by_id("com.netease.cloudmusic:id/a8b")
            #     for i in playlist:
            #         if "出山"in i.text:
            #     print("获取到的歌曲列表长度：%d" % playlist.__len__())
            #     or_el = playlist[0]
            #     des_el = playlist[20]
            #     if "出山"in des_el.text:
            #         self.driver.scroll(or_el, des_el, 300)
            #         break
            """无法定位我的音乐页面的歌单列表，功能暂时无法进行自动化测试------pause"""
            # TouchAction(self.driver).tap(x=823, y=1752).perform()
            # self.driver.tap([(0, 895)], 100)
            # sleep(THINK_TIME)
            # """先将弹出的提示框点击关掉"""
            # TouchAction(self.driver).tap(x=1108, y=902).perform()
            # sleep(THINK_TIME)
            # TouchAction(self.driver).press(x=133, y=411).move_to(x=1413, y=411).release().perform()
            # window = self.driver.find_element_by_class_name("android.support.v7.widget.RecyclerView").size
            # print("区域的长宽为：%s" % window)
            # """不知道为什么，滑动没有报错，但是页面并没有进行滑动"""
            # action().left_right(window["width"]/7, window["width"]/6, window["height"]/2, "right")
            # self.driver.wait_activity(".activity.PlayListActivity", THINK_TIME)
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
