from Utils.appium_config import DriverClient
import unittest
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

THINK_TIME = 3
WAIT_TIME = 30
class my_music(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.quit()

    @unittest.skip("don't know how to locate element----pause")
    def test_b_mymusic(self):
        try:
            # click Mine button in the home page
            self.driver.find_element_by_accessibility_id("我的音乐").click()
            # choose no.1 music list: i don't know how to locate this list , tried a lot ,still none sense
            # self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
            sleep(THINK_TIME)
            """无法定位我的音乐页面的歌单列表，功能暂时无法进行自动化测试------pause"""
            TouchAction(self.driver).tap(x=823, y=1752).perform()
            # self.driver.tap([(0, 895)], 100)
            # sleep(THINK_TIME)
            self.driver.wait_activity(".activity.PlayListActivity", THINK_TIME)
            print("当前页面的活动名称：%s" % self.driver.current_activity)
            self.assertEquals(".activity.PlayListActivity", self.driver.current_activity)
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
