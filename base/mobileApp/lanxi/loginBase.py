from Utils.appium_config import DriverClient as DC
from Utils.operate_yaml import operate_yaml
from time import sleep
from Utils.public_action import action
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
            self.driver.wait_activity('.activity.HomePageActivity', think_time)
            sleep(think_time)
            operate.operate_yaml('我的')
            sleep(think_time)
            operate.operate_yaml('登录/注册')
            sleep(think_time)
            self.driver.wait_activity(".activity.mine.LoginActivity", think_time)
            sleep(think_time)
            try:
                """第一次登录"""
                operate.operate_yaml('手机号码')
            except:
                """非首次登录"""
                operate.operate_yaml('清除手机号')
                sleep(think_time)
                operate.operate_yaml('手机号码')
            sleep(think_time)
            operate.operate_yaml('登录密码')
            sleep(think_time)
            operate.operate_yaml('登录')
            self.driver.wait_activity('.activity.HomePageActivity', think_time)
        except Exception as e:
            action().get_screenShot()
            raise e