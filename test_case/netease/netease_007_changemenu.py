import unittest
from Utils.appium_config import DriverClient
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from Utils.action_config import action


THINK_TIME = 3


class changemenu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    """测试我的音乐页面的菜单调整功能"""
    def test_changemenu(self):
        try:
            """如果要单独与登录联合使用的话，需要将下面注释的语句激活"""
            self.driver.find_element_by_accessibility_id("我的音乐").click()
            sleep(THINK_TIME)
            """先将弹出的提示框点击关掉"""
            TouchAction(self.driver).tap(x=1108, y=902).perform()
            """定位到需要进行滑动的指定元素"""
            # menulist=self.driver.find_elements_by_id("com.netease.cloudmusic:id/byg")
            # print("整个模块中有多少个子菜单：{}".format(len(menulist)))
            # self.assertNotEqual(0, len(menulist))
            """定义滑动开始元素start_el"""
            start_text = "云村正能量"
            start_el = self.driver.find_element_by_android_uiautomator\
                ("new UiSelector().text(\""+start_text+"\")")
            print("开始元素:%s" % start_el)
            matchString = "Edit"
            # pattern = "new UiSelector().text(\""+matchString+"\")"
            end_el = self.driver.find_element_by_android_uiautomator\
                ("new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text(\"Edit\"))")
            # end_el = action().scroll_to_el(pattern)
            print("结束元素：{}".format(end_el))
            """调用滑动方法进行页面元素滑动"""
            action().element_scroll(start_el, end_el, 200)
            """滑动是否有效"""
            page_source = self.driver.page_source
            self.assertEquals(True , matchString in page_source)
        except Exception as e:
            raise e