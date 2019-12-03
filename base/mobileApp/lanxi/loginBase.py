from Utils.appium_config import DriverClient as DC
from Utils.operate_yaml import operate_yaml
from time import sleep
import time
path = 'yaml/mobile/lanxi/login.yaml'
think_time = 3


class loginBase():
    def __init__(self):
        self.driver = DC().getDriver()

    def firstLogin(self):
        pass

    def login(self):
        try:
            operate = operate_yaml(path)
            self.driver.wait_activity('.HomePageActivity', think_time)
            operate.operate_yaml('我的')
            sleep(think_time)
            operate.operate_yaml('登录/注册')
            sleep(think_time)
            self.driver.wait_activity(".mine.LoginActivity", think_time)
            operate.operate_yaml('手机号码')
            sleep(think_time)
            operate.operate_yaml('登录密码')
            sleep(think_time)
            operate.operate_yaml('登录')
        except Exception as e:
            nowdate = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file("Img/%s.png" % nowdate)
            raise e