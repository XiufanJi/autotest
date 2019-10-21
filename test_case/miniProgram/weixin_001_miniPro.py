import unittest
from Utils.appium_config import DriverClient
from Utils.action_config import action
from time import sleep


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
            print("print context：", self.driver.context)
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
            print("当前的context值为：", self.driver.context)
            target_minipro = "咖啡外卖"
            el_target = action().find_byUiautormator("textContains", target_minipro)
            print("页面上定位到target小程序元素吗？:%s" % el_target.is_displayed())
            if el_target.is_displayed():
                el_target.click()
            sleep(THINK_TIME)
            print("页面的所有模式", self.driver.contexts)
            """点击小程序进入页面，切换进入webview页面"""
            self.driver.switch_to.context("WEBVIEW_com.tencent.mm:tools")
            sleep(10)
            # menu = "我的"
            # el_menu = action().find_byUiautormator("text", menu)
            # print("页面上定位到小程序我的元素吗？:%s" % el_menu.is_displayed())
            # if el_menu.is_displayed():
            #     el_menu.click()
            self.assertEquals(".plugin.appbrand.ui.AppBrandUI", self.driver.current_activity)
            print("当前页面的模式为：%s" % self.driver.context)
        except Exception as e:
            raise e
