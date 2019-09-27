import unittest
from Utils.appium_config import DriverClient
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



THINK_TIME = 3
num = randint(1, 100)
keys = "new album"+str(num)
class createlist(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        pass

    """可与login单独执行"""
    @unittest.skip("暂不测试")
    def test_01_creatalbum(self):
        """click mine button"""
        try:
            # self.driver.find_element_by_accessibility_id("我的音乐").click()
            # sleep(THINK_TIME)
            # """先将弹出的提示框点击关掉"""
            # TouchAction(self.driver).tap(x=1108, y=902).perform()
            """find creat button"""
            self.driver.find_element_by_id("com.netease.cloudmusic:id/c8").click()
            """make sure if pop window is appear"""
            new_Mix=self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"New Mix\")")\
                .is_displayed()
            print("歌单新增弹框是否出现：%s" % new_Mix)
            if new_Mix:
                self.driver.find_element_by_id("android:id/input").send_keys(keys)
                # self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"type in Mix title\")")\
                #     .send_keys("new album")
                sleep(THINK_TIME)
                self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"SUBMIT\")").click()
                sleep(THINK_TIME)
                self.driver.wait_activity(".activity.PlayListActivity", THINK_TIME)
                """back to home page"""
                self.driver.find_element_by_accessibility_id("Navigate up").click()
                self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
                new_album = self.driver.find_element_by_android_uiautomator("new UiSelector().\
                textContains(\"new album\")").is_displayed()
                print("新增歌单中是否有刚才新增的歌单名称：%s" % new_album)
                self.assertEquals(True, new_album)
            else:
                print("未找到对应元素，未弹出新增框")
                self.fail("未找到对应元素")
        except Exception as e:
            raise e

    @unittest.skip("暂不测试")
    def test_02_editalbunm(self):
        """查找歌单的编辑按钮"""
        try:
            # self.driver.find_element_by_accessibility_id("我的音乐").click()
            # sleep(THINK_TIME)
            # """先将弹出的提示框点击关掉"""
            # TouchAction(self.driver).tap(x=1108, y=902).perform()
            sleep(THINK_TIME)
            # albumlist=self.driver.find_elements_by_id("com.netease.cloudmusic:id/a16")
            """查询相应歌单对应的操作按钮"""
            self.driver.find_element_by_android_uiautomator("new UiSelector().textContains(\"new album\")\
               .fromParent(new UiSelector().resourceId(\"com.netease.cloudmusic:id/a16\"))").click()
            """找到编辑按钮"""
            self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"Edit Mix\")").click()
            """切换activity"""
            self.driver.wait_activity(".activity.EditPlayListActivity", THINK_TIME)
            """清除输入框内的内容并进行文字输入"""
            self.driver.find_element_by_id("com.netease.cloudmusic:id/apd").click()
            sleep(THINK_TIME)
            self.driver.find_element_by_id("com.netease.cloudmusic:id/api").clear()
            self.driver.find_element_by_id("com.netease.cloudmusic:id/api").send_keys("test")
            """点击save按钮"""
            self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"SAVE\")").click()
            """点击返回按钮返回主页面"""
            # sleep(THINK_TIME)
            self.driver.find_element_by_accessibility_id("Navigate up").click()
            self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
            edit_effect = self.driver.find_element_by_android_uiautomator("new UiSelector().textContains(\"test\")") \
                .is_displayed()
            print("页面上是否有修改后的歌单名：%s" % edit_effect)
            self.assertEquals(True, edit_effect)
        except Exception as e:
            raise e

    @unittest.skip("暂不测试")
    def test_03_delealbum(self):
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
            toast_element = WebDriverWait(self.driver, 0.01). \
                until(EC.presence_of_element_located((By.XPATH, pop_message)))
            print("获取到的页面提示消息为：%s" % toast_element.text)
            self.assertEquals("Deleted", toast_element.text)
        except Exception as e:
            raise e








