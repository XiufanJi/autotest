import unittest
from Utils.appium_config import DriverClient
from time import sleep
from Utils.action_config import action
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

THINK_TIME = 3
class testcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    """使用百度地图来进行多次点击放大缩小测试"""
    # @unittest.skip("skip test_case")
    def test_testcase(self):
        """点击授权页面上的同意按钮"""
        sleep(THINK_TIME)
        agree = "同意"
        self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"" + agree + "\")").click()
        # agree = self.driver.find_element_by_accessibility_id("同意")
        # agree.click()
        sleep(THINK_TIME)
        """点击是否同意按钮，有四个弹框，需要循环四次"""
        text = "ALLOW"
        for i in range(3):
            self.driver.find_element_by_android_uiautomator("new UiSelector().text(\""+text+"\")").click()
        getin_map = "进入地图"
        self.driver.find_element_by_android_uiautomator("new UiSelector().text(\""+getin_map+"\")").click()
        """切换页面活动"""
        self.driver.wait_activity(".MapsActivity", THINK_TIME)
        """点击关闭推荐框"""
        self.driver.find_element_by_id("com.baidu.BaiduMap:id/guide_close").click()
        area = action().get_window_size()
        height = area[1]
        width = area[0]
        action1 = TouchAction(self.driver)
        action1.tap(x=width/4, y=height/4).move_to(x=width/7, y=height/7).release()
        action2 = TouchAction(self.driver)
        action2.tap(x=width/4, y=height/4).move_to(x=width/2, y=height/2).release()
        sleep(10)
        MultiAction(self.driver).add(action1, action2).perform()











