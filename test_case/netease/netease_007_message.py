import unittest
from Utils.appium_config import DriverClient
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


THINK_TIME = 3
class message(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    """可单独与login联合执行"""
    def test_checkmessage(self):
        try:
            """获取私信消息数目"""
            sleep(THINK_TIME)
            message_num = self.driver.find_element_by_android_uiautomator("new UiSelector().\
            description(\"抽屉菜单\").fromParent(new UiSelector().className(\"android.widget.TextView\"))").text
            print("私信消息的数目为:%s" % message_num)
            if message_num != 0:
                """点击页面上的菜单按钮跳转至私信页面"""
                self.driver.find_element_by_accessibility_id("抽屉菜单").click()
                """点击信封按钮"""
                self.driver.find_element_by_id("com.netease.cloudmusic:id/bqc").click()
                """切换活动"""
                self.driver.wait_activity(".activity.MessageActivity", THINK_TIME)
                """点击全部标记为已读"""
                self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"标记已读\")").click()
                """点击确定按钮"""
                self.driver.find_element_by_id("com.netease.cloudmusic:id/bsm").click()
                sleep(THINK_TIME)
                self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"标记已读\")").click()
                """获取是否还有未读消息toast"""
                pop_message = "//*[contains(@text,'暂无新消息')]"
                toast_element = WebDriverWait(self.driver, 5).\
                    until(EC.presence_of_element_located((By.XPATH, pop_message)))
                print("获取到的页面提示消息为：%s" % toast_element.text)
                self.assertEquals("暂无新消息", toast_element.text)
            else:
                pass
        except Exception as e:
            raise e
