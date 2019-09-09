from Utils.appium_config import DriverClient
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
import os

THINK_TIME = 5
class versioncheck():
    def __init__(self):
        self.driver = DriverClient().getDriver()

    def versioncheck(self):
        # see if version upgrade pop window is appear
        flag = self.driver.find_element_by_id("com.netease.cloudmusic:id/ccj").is_displayed()
        print("版本更新弹框是否弹出: %s" % flag)
        print("当前页面的活动名称为：%s" % self.driver.current_activity)
        if flag:
            # if there is a pop window appear? click anywhere outside the window,let it disappear
            sleep(THINK_TIME)
            actions = TouchAction(self.driver)
            actions.tap(x=577, y=2356).perform().release()
            # TouchAction(self.driver).tap(x=577, y=2356).perform()
            # if use driver.tap,it will encounter some problems
            # self.driver.tap([(577, 2356)], 5)
            # text = self.driver.find_element_by_id("com.netease.cloudmusic:id/ccj").text
            # print("版本更新提示框的提示语为：%s" % text)
            # if ("是否升级")in text:
            #     # click install button to upgrade app
            #     self.driver.find_element_by_id("com.netease.cloudmusic:id/ccm").click()
        else:
            pass

