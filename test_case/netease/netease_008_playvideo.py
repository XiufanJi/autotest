import unittest
from Utils.appium_config import DriverClient
from time import sleep
from Utils.public_action import action
from appium.webdriver.common.touch_action import TouchAction

sleepTime = 3
waitTime = 5


class testcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        pass

    """主要是keycode练习，功能主要是点击歌曲视频进行播放，然后点击物理键进行返回操作"""
    @unittest.skip("skip test_case")
    def test_testcase(self):
        """测试在特定区域进行滑动操作"""
        """获取歌单广场按钮"""
        try:
            # self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"歌单广场\")").click()
            # self.driver.wait_activity(".activity.MainPlaylistActivity", sleepTime)
            # area = self.driver.find_element_by_id("com.netease.cloudmusic:id/akt").size
            # """如果要单独与登录联合使用的话，需要将下面注释的语句激活"""
            self.driver.find_element_by_accessibility_id("我的音乐").click()
            sleep(sleepTime)
            """先将弹出的提示框点击关掉"""
            TouchAction(self.driver).tap(x=1108, y=902).perform()
            """纵向滚动获取需要的按钮"""
            while True:
                matchString = "运动"
                el = self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().\
                scrollable(true)).setAsVerticalList().scrollIntoView(new UiSelector().text(\""+matchString+"\"))")
                if el.is_displayed():
                    print("匹配的按钮是否出现：%s" % el.is_displayed())
                    break
                else:
                    continue
            self.driver.find_element_by_android_uiautomator("new UiSelector().\
            textContains(\""+matchString+"\")").click()
            """切换页面活动"""
            self.driver.wait_activity(".activity.PlayListActivity", sleepTime)
            """查找视频播放按钮"""
            video_list = self.driver.find_elements_by_id("com.netease.cloudmusic:id/c9k")
            video_list[0].click()
            """切换页面活动"""
            self.driver.wait_activity(".activity.VideoBoxActivity", sleepTime)
            sleep(5)
            """获取视屏框的长宽"""
            area = self.driver.find_element_by_id("com.netease.cloudmusic:id/ot").size
            width = area["width"]
            height = area["height"]
            sleep(waitTime)
            TouchAction(self.driver).tap(x=width/2, y=height/2).release().perform()
            """全屏操作：模拟器可以使用Ctrl+F11,真机appium不支持python调用rotate方法，\
            只能点击屏幕上的全屏按钮，但是这个按钮不一定能获取到"""
            """调用物理返回按钮"""
            self.driver.press_keycode(keycode=4)
            self.driver.wait_activity(".activity.PlayListActivity", sleepTime)
            sleep(sleepTime)
            self.assertEquals(".activity.PlayListActivity", self.driver.current_activity)
        except Exception as e:
            raise e
