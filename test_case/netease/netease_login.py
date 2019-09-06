import unittest
from Utils.appium_config import DriverClient
from Utils.netease.login import getlogin_method



THINK_TIME = 3
WAIT_TIME = 30
class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_a_login(self):
        # check whether the app is install or not,if not ,then install
        # flag = self.driver.is_app_installed("com.netease.cloudmusic")
        # if flag:
        #     pass
        # else:
        #     self.driver.install_app("app/com.netease.cloudmusic_6.3.2_152.apk")
        # sleep(THINK_TIME)
        # # click agree button
        # try:
        #     count = 0
        #     while count < 1:
        #         self.driver.find_element_by_id("com.netease.cloudmusic:id/as6").click()
        #         sleep(THINK_TIME)
        #         # click authorize button
        #         self.driver.find_element_by_id("com.netease.cloudmusic:id/c0o").click()
        #         # click allow button
        #         sleep(THINK_TIME)
        #         for i in range(2):
        #             self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        #         count += 1
        #     self.driver.wait_activity(".activity.IntroduceActivity", THINK_TIME)
        #     print("当前的页面的活动名称为：%s" % self.driver.current_activity)
        #     # change to login page
        #     sleep(WAIT_TIME)
        #     self.driver.wait_activity(".activity.LoginActivity", THINK_TIME)
        #     print("当前的页面的活动名称为：%s" % self.driver.current_activity)
        #     # click user agreement:it's so strange,id selector is useless,but coordination tap is work;
        #     # self.driver.find_element_by_id("com.netease.cloudmusic:id/as6").click()
        #     # self.driver.tap([(401,2730),(1039,2819)],100)
        #     # clickable = self.driver.find_element_by_id("com.netease.cloudmusic:id/as6").get_attribute("checked")
        #     # print("单选框CheckBox是否被选中：%s " % clickable)
        #     # sleep(THINK_TIME)
        #     # # click login with guest
        #     # if clickable:
        #     #     self.driver.find_element_by_id("com.netease.cloudmusic:id/a82").click()
        #     # else:
        #     #     raise Exception
        #
        #     """methods below are include login with mobile and third party(wechat,qq,weibo and neteasy account)"""
        #     # self.driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
        #     # self.driver.find_elements_by_class_name("android.widget.ImageView")
        #     # change to home page
        #     # self.driver.wait_activity("com.netease.cloudmusic.activity.MainActivity", THINK_TIME)
        #     # print("当前的页面的活动名称为：%s" % self.driver.current_activity)
        #     # # tap anywhere in home page to avoid click the recommend menu
        #     # sleep(THINK_TIME)
        #     # self.driver.tap([(358,2448)],100)
        #     # sleep(THINK_TIME)
        #     # # click menu button
        #     # self.driver.find_element_by_id("com.netease.cloudmusic:id/q8").click()
        #     # self.driver.find_element_by_id("com.netease.cloudmusic:id/ai4").click()
        #     # self.driver.wait_activity("com.netease.cloudmusic.activity.LoginActivity", THINK_TIME)
        #     # print("当前的页面的活动名称为：%s" % self.driver.current_activity)
        #     sleep(THINK_TIME)
        #     # actions = TouchAction(self.driver)
        #     # actions.tap([(358,2448)],100)
        #     # actions.perform().release()
        #     self.driver.tap([(401,2730)],100)
        #     clickable = self.driver.find_element_by_id("com.netease.cloudmusic:id/as6").get_attribute("checked")
        #     print("单选框CheckBox是否被选中：%s " % clickable)
        #     # sleep(THINK_TIME)
        #     # click login with mobile
        #     if clickable:
        #         self.driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
        #     else:
        #         raise Exception
        #     self.driver.find_element_by_class_name("android.widget.EditText").send_keys("18557539532")
        #     self.driver.find_element_by_id("com.netease.cloudmusic:id/anq").click()
        #     self.driver.find_element_by_id("com.netease.cloudmusic:id/jb").send_keys("123321")
        #     TextView = self.driver.find_elements_by_class_name("android.widget.TextView")
        #     TextView[2].click()
        #     self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
        #     print("当前的页面的活动名称为：%s" % self.driver.current_activity)
        #     self.assertIn(self.driver.current_activity,"com.netease.cloudmusic.activity.MainActivity")
        # except LookupError:
        #     raise LookupError
        #     print("can not locate the element")
        # getlogin_method().login_with_mobile()
        getlogin_method().login_with_weixin()
        # self.assertIn(self.driver.current_activity, "com.netease.cloudmusic.activity.MainActivity")











