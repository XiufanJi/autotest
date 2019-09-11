from Utils.appium_config import DriverClient
from time import  sleep



THINK_TIME = 3
WAIT_TIME = 30
class authorize():
    def __init__(self):
        self.driver = DriverClient().getDriver()

    # storage,locate privileges authorize
    def authorize(self):
        try:
            # click ok button in the start page
            self.driver.find_element_by_id("com.netease.cloudmusic:id/as6").click()
            sleep(THINK_TIME)
            # click authorize button
            self.driver.find_element_by_id("com.netease.cloudmusic:id/c0o").click()
            # click allow button:twice
            sleep(THINK_TIME)
            for i in range(2):
                self.driver.find_element_by_id("com.android.packageinstaller:"
                                               "id/permission_allow_button") \
                    .click()
        except Exception as e:
            raise e
            # print("no element could locate in this page")

    # click user agreement in login page
    def click_agreement(self):
        try:
            # change activity to IntroduceActivity
            self.driver.wait_activity(".activity.IntroduceActivity", THINK_TIME)
            print("当前的页面的活动名称为：%s" % self.driver.current_activity)
            # change to login page
            sleep(WAIT_TIME)
            self.driver.wait_activity(".activity.LoginActivity", THINK_TIME)
            print("当前的页面的活动名称为：%s" % self.driver.current_activity)
            # click agreement checkbox
            self.driver.tap([(401, 2730)], 100)
            # verify if checkbox is checked
            clickable = self.driver.find_element_by_id("com.netease.cloudmusic:id/as6") \
                .get_attribute("checked")
            print("单选框CheckBox是否被选中：%s " % clickable)
        except Exception as e:
            raise e
            # print("no element could locate in this page")
        return clickable