import unittest
from Utils.appium_config import DriverClient
from Utils.appium_action import action
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver


THINK_TIME = 5


class miniPro(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        # pass

    """对微信小程序进行测试"""

    def test_miniPro(self):
        try:
            """登录微信首页后，点击发现按钮，切换至小程序页面"""
            sleep(10)
            # print("输出当前context：", self.driver.current_context)
            # print("当前页面内容", self.driver.page_source)
            # self.driver.switch_to.context("WEBVIEW_com.tencent.mm:tools")
            # sleep(10)
            # print("输出切换后的context：", self.driver.current_context)
            # print("切换后的页面内容", self.driver.page_source)
            find = "发现"
            el_find = self.driver.find_element_by_android_uiautomator("new UiSelector().text(\""+find+"\")")
            print("发现元素有在页面显示吗?: %s" % el_find.is_displayed())
            if el_find.is_displayed():
                el_find.click()
            sleep(THINK_TIME)
            """点击小程序按钮"""
            minipro = "小程序"
            el_minipro = self.driver.find_element_by_android_uiautomator("new UiSelector().text(\""+minipro+"\")")
            print("页面上定位到小程序元素吗？:%s" % el_minipro.is_displayed())
            if el_minipro.is_displayed():
                el_minipro.click()
            """切换页面活动值小程序列表显示页面"""
            self.driver.wait_activity(".plugin.appbrand.ui.AppBrandLauncherUI", THINK_TIME)
            sleep(THINK_TIME)
            print("小程序列表页面当前的context值为：", self.driver.current_context)
            sleep(THINK_TIME)
            target_minipro = "麦乐送"
            el_target = action().find_byUiautormator("textContains", target_minipro)
            # print("切换前的页面名称", self.driver.current_window_handle)
            print("页面上定位到target小程序元素吗？:%s" % el_target.is_displayed())
            if el_target.is_displayed():
                el_target.click()
            sleep(10)
            print("全部的contexts:", self.driver.contexts)
            # print("小程序页面切换前的页面元素：", self.driver.page_source)
            # """进行页面元素选择"""
            # print("小程序页面的context值为：%s" % self.driver.current_context)
            # """点击小程序进入页面，切换进入webview页面"""
            self.driver.switch_to.context("WEBVIEW_com.tencent.mm:appbrand0")
            sleep(10)
            print("切换后的页面元素：", self.driver.page_source)
            # """进行页面元素选择"""
            # print("小程序页面切换后的context值为：%s" % self.driver.current_context)
            print(self.driver.current_window_handle)
            print(self.driver.window_handles)
            # print("切换后的页面名称：",self.driver.current_window_handle)
            # print("当前页面的句柄%s" % self.driver.current_window_handle)
            # print("小程序页面的全部句柄%s " % self.driver.window_handles)
            # page_handles = self.driver.window_handles
            # self.driver.switch_to_window(page_handles[1])
            # sleep(20)
            # print("切换后的句柄", self.driver.current_window_handle)
            # print("页面全部元素%s" % self.driver.page_source)
            # register = self.driver.find_element_by_css_selector(".hospital-service-blue-container-items")
            # print(register.is_displayed())
            # sleep(THINK_TIME)
            # print("小程序当前页面模式", self.driver.context)
            # self.assertEquals(".plugin.appbrand.ui.AppBrandUI", self.driver.current_activity)
            # """switch to native_app"""
            # # 调用物理返回键
            # self.driver.press_keycode(4)
            # sleep(THINK_TIME)
            # """切换"""
            # self.driver.switch_to.context("NATIVE_APP")
            # sleep(THINK_TIME)
            # print("页面的所有模式", self.driver.contexts)
            # self.driver.find_element_by_accessibility_id("返回").click()
            # sleep(THINK_TIME)
            # menu = "微信"
            # el_menu = action().find_byUiautormator("text", menu)
            # print("页面上定位到小程序我的元素吗？:%s" % el_menu.is_displayed())
            # if el_menu.is_displayed():
            #     el_menu.click()
            # print("当前页面的模式为：%s" % self.driver.context)
            # self.assertEquals(".ui.LauncherUI", self.driver.current_activity)
        except Exception as e:
            raise e
