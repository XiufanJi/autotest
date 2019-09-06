from Utils.appium_config import DriverClient


class versioncheck():
    def __init__(self):
        self.driver=DriverClient().getDriver()

    def versioncheck(self):
        current_activity = self.driver.current_activity()
        if current_activity == ".activity.MainActivity":
            # see if version upgrade pop window is appear
            flag = self.driver.find_element_by_id("com.netease.cloudmusic:id/ccj").is_displayed()
            if flag:
                text = self.driver.find_element_by_id("com.netease.cloudmusic:id/ccj").text
                print("版本更新提示框的提示语为：%s" % text)
                if text in ("是否升级版本？"):
                    # click install button to upgrade app
                    self.driver.find_element_by_id("com.netease.cloudmusic:id/ccm").click()
            else:
                pass
        else:
            pass

