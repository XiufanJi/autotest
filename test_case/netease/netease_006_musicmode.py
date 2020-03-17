# coding=utf-8
import unittest
from Utils.appium_config import DriverClient
from time import sleep
from Utils.public_action import pub_action


THINKE_TIME = 3


class musicmode(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        pass
    
    @unittest.skip("skip")
    def test_likemode(self):
        try:
            sleep(THINKE_TIME)
            """查找我的音乐页面心动模式的按钮"""
            self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"心动模式\")").click()
            self.driver.wait_activity(".activity.PlayerActivity", THINKE_TIME)
            """点击页面弹框的按钮关闭弹框"""
            self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"OK\")").click()
            """点击播放模式按钮进行切换测试"""
            """31-34的这几行代码，执行的时候很慢很慢，其他类似代码并没有出现这种情况，由于很慢，所以最后超时了。"""
            # self.driver.find_element_by_accessibility_id("播放模式").click()
            # matchString = "//*[@text={}]".format("Loop all")
            # toast_element = WebDriverWait(self.driver, 0.01). \
            #     until(EC.presence_of_element_located((By.XPATH, matchString)))
            # print("每次点击的匹配语句为:{0},获取到的toast信息为：{1}".format(matchString, toast_element))
            # self.assertEquals(matchString, toast_element)
            """点击按钮进行模式切换"""
            for i in range(4):
                self.driver.find_element_by_accessibility_id("播放模式").click()
                """获取切换后的弹出提示语"""
                if i == 0:
                    pop_msg = "Loop all"
                elif i == 1:
                    pop_msg = "Shuffle"
                elif i == 2:
                    pop_msg = "Loop single"
                else:
                    pop_msg = "心动模式"
                text_pattern = "//*[@text={}]".format(pop_msg)
                msg = pub_action(text_pattern, self.driver)
                print("每次点击的匹配语句为:{0},获取到的toast信息为：{1}".format(pop_msg, msg))
                self.assertEquals(pop_msg, msg)
            """点击返回我的音乐首页"""
            self.driver.find_element_by_accessibility_id("Navigate up").click()
            self.driver.wait_activity(".activity.MainActivity", THINKE_TIME)
        except Exception as e:
            raise e








