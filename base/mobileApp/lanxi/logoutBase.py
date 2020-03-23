from Utils.appium_config import DriverClient as DC
from selenium.webdriver.support import expected_conditions as EC
from Utils.public_action import pub_action
from Utils.operate_yaml import operate_yaml
from Utils.appium_action import action

think_time = 3

class logoutBase():
    def __init__(self):
        self.driver = DC().getDriver()
        self.path = pub_action().get_path("yaml/mobile/lanxi/logout.yaml")

    def logout(self):
        try:
            operate = operate_yaml(self.path)
            personalCenter = operate.operate_yaml("我的")
            personalCenter[0].click()
            setting = operate.operate_yaml("设置")
            setting[0].click()
            # self.driver.implicitly_wait(3)
            print("点击退出设置-当前页面的活动名称：{}".format(self.driver.current_activity))
            self.driver.wait_activity(".activity.mine.SettingActivity", think_time)
            logout = operate.operate_yaml("退出登录")
            logout[0].click()
            ok = operate.operate_yaml("确定")
            ok[0].click()
            # loginButton = operate.operate_yaml("登录/注册")
            # loginButton[0].is_displayed()
            battery = self.driver.battery_info
            print("当前手机的电量信息为：{}".format(battery))
        except EC.NoSuchElementException as e:
            action().get_screenShot()
            raise e
