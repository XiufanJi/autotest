import unittest
from Utils.appium_config import DriverClient
from time import sleep
from Utils.action_config import action
from appium.webdriver.common.touch_action import TouchAction

sleepTime = 3
class testcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @unittest.skip("skip test_case")
    def test_testcase(self):
        """测试在特定区域进行滑动操作"""
        """获取歌单广场按钮"""
        # self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"歌单广场\")").click()
        # self.driver.wait_activity(".activity.MainPlaylistActivity", sleepTime)
        # area = self.driver.find_element_by_id("com.netease.cloudmusic:id/akt").size
        # """如果要单独与登录联合使用的话，需要将下面注释的语句激活"""
        self.driver.find_element_by_accessibility_id("我的音乐").click()
        sleep(sleepTime)
        """先将弹出的提示框点击关掉"""
        TouchAction(self.driver).tap(x=1108, y=902).perform()
        while True:
            matchString = "Edit"
            el = self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector()\
            .className(\"android.support.v7.widget.RecyclerView\"))\
            .setAsHorizontalList().scrollIntoView(new UiSelector().text(\""+matchString+"\"))")
            if el.is_displayed():
                print("匹配的的edit按钮是否出现：%s" % el.is_displayed())
                break
            else:
                continue
        el.click()
