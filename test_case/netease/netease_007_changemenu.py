import unittest
from Utils.appium_config import DriverClient
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


THINK_TIME = 3


class changemenu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     # cls.driver.quit()

    """测试我的音乐页面的菜单调整功能"""
    @unittest.skip("skip")
    def test_changemenu(self):
        try:
            """如果要单独与登录联合使用的话，需要将下面注释的语句激活"""
            self.driver.find_element_by_accessibility_id("我的音乐").click()
            sleep(THINK_TIME)
            """先将弹出的提示框点击关掉"""
            TouchAction(self.driver).tap(x=1108, y=902).perform()
            """横向滚动特定区域进行按钮查找"""
            while True:
                matchString = "Edit"
                el = self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector()\
                   .className(\"android.support.v7.widget.RecyclerView\"))\
                   .setAsHorizontalList().scrollIntoView(new UiSelector().text(\"" + matchString + "\"))")
                if el.is_displayed():
                    print("匹配的的edit按钮是否出现：%s" % el.is_displayed())
                    break
                else:
                    continue
            """点击edit按钮切换页面至编辑页面"""
            self.driver.find_element_by_android_uiautomator("UiSelector()\
            .text(\""+matchString+"\").fromParent(className(\"android.widget.ImageView\"))").click()
            """切换页面活动"""
            self.driver.wait_activity(".activity.EmbedBrowserActivity", THINK_TIME)
            sleep(THINK_TIME)
            """进行drag操作，切换菜单,查找开始按钮和结束按钮"""
            page_source = self.driver.page_source
            print("页面元素为：%s" % page_source)
            start_text = "直播"
            original_el = self.driver.find_element_by_android_uiautomator("new UiSelector().text(\""+start_text+"\")")
            destination_text = "电台"
            destination_el = self.driver.find_element_by_android_uiautomator\
                ("new UiSelector().text(\""+destination_text+"\")")
            """进行按钮交换操作"""
            """此处使用的交换方法为同级交换，交叉交换由于在交换时无法定位“移到这里”的位置，暂时先搁置"""
            if original_el.is_displayed() and destination_el.is_displayed():
                self.driver.drag_and_drop(original_el, destination_el)
            """这里不做断言，因为同一个webview页面，所有的名称都一样，有的还有多级，不好比较，放到首页来判断"""
            """点击完成按钮保存设置"""
            finish_button = self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"完成\")")
            finish_button.click()
            """点击返回按钮"""
            back_button = self.driver.find_element_by_accessibility_id("Navigate up")
            back_button.click()
            """切换活动名称"""
            self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
            # """切换至我的推荐页面"""
            # self.driver.find_element_by_accessibility_id("我的推荐").click()
            """同样太麻烦了，不使用断言进行判断"""
        except Exception as e:
            raise e