import unittest
from Utils.appium_config import DriverClient
from time import sleep


THINK_TIME = 3
class history(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        pass

    """进行历史记录的删除测试"""
    @unittest.skip("暂不测试")
    def test_delehistory(self):
        try:
            sleep(THINK_TIME)
            """点击查询按钮"""
            self.driver.find_element_by_accessibility_id("Search").click()
            self.driver.wait_activity(".activity.SearchActivity", THINK_TIME)
            sleep(THINK_TIME)
            """判断页面上是否存在历史记录"""
            source = self.driver.page_source
            print("页面内容：%s" % source)
            if "历史记录" in source:
                """点击删除按钮"""
                self.driver.find_element_by_id("com.netease.cloudmusic:id/pz").click()
                """点击清除按钮"""
                self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"CLEAR\")").click()
                """判断页面上的历史记录是否已经删除"""
                source = self.driver.page_source
                flag = "历史记录" in source
                self.assertEquals(False, flag)
                print("页面上是否还存在历史记录：%s" % flag)
            else:
                print("页面上没有历史记录")
            """点击返回按钮返回首页"""
            self.driver.find_element_by_accessibility_id("Collapse").click()
            self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
        except Exception as e:
            raise e


