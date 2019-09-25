import unittest
from Utils.appium_config import DriverClient
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


THINK_TIME = 3
class delealbum(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        pass

    def test_delealbum(self):
        try:
            # self.driver.find_element_by_accessibility_id("我的音乐").click()
            # sleep(THINK_TIME)
            # """先将弹出的提示框点击关掉"""
            # TouchAction(self.driver).tap(x=1108, y=902).perform()
            sleep(THINK_TIME)
            """查询相应歌单对应的操作按钮"""
            """要是歌单能以变量的形式传入就比较灵活了，但是现在只能传固定值"""
            self.driver.find_elements_by_android_uiautomator("new UiSelector().text(\"test\")\
                       .fromParent(new UiSelector().resourceId(\"com.netease.cloudmusic:id/a16\"))")[0].click()
            """查找删除按钮，进行点击操作"""
            self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"Delete\")").click()
            """点击确定删除按钮"""
            self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"DELETE\")").click()
            """获取是否还有未读消息toast"""
            pop_message = "//*[@text='Deleted']"
            toast_element = WebDriverWait(self.driver, 5). \
                until(EC.presence_of_element_located((By.XPATH, pop_message)))
            print("获取到的页面提示消息为：%s" % toast_element.text)
            self.assertEquals("Deleted", toast_element.text)
        except Exception as e:
            raise e

