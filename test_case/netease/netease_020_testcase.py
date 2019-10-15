import unittest
from Utils.appium_config import DriverClient
from time import sleep
from Utils.action_config import action

THINK_TIME = 3
class testcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    """使用百度地图来进行多次点击放大缩小测试"""
    @unittest.skip("skip test_case")
    def test_testcase(self):
        sleep(10)
        # """腾讯地图"""
        agree = "同意并开始授权"
        self.driver.find_element_by_android_uiautomator("new UiSelector().text(\""+agree+"\")").click()
        # """点击同意项目授权"""
        # text = "ALLOW"
        # for i in range(4):
        #     self.driver.find_element_by_android_uiautomator("new UiSelector().text(\""+text+"\")").click()
        """切换页面活动"""
        self.driver.wait_activity(".ama.MapActivity", THINK_TIME)
        # """等待地图加载完成"""
        sleep(10)
        action().enlarge()
        # for i in range(3):
        #     """调用放大方法进行地图放大"""
        #     action().enlarge()
        #     sleep(3)
        for i in range(3):
            """调用缩小方法进行地图缩小操作"""
            action().narrow()
            sleep(3)













