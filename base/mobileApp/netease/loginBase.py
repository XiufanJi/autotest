from Utils.operate_yaml import operate_yaml
from Utils.appium_config import DriverClient as DC
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from Utils.appium_action import action
import os
path = 'yaml/mobile/netease/login.yaml'
think_time = 3
"""调试文件读取路径"""
test = '../../../yaml/mobile/netease/login.yaml'


class loginBase():
    """登录操作"""
    def __init__(self):
        self.driver = DC().getDriver()

    def firstLogin(self):
        try:
            print("首次登陆")
            operate = operate_yaml(path)
            # operate = operate_yaml(test)
            self.driver.wait_activity(".activity.IntroduceActivity", think_time)
            sleep(think_time)
            operate.operate_yaml('同意')
            sleep(think_time)
            operate.operate_yaml('进入APP')
            sleep(think_time)
            loginBase().login()
        except EC.NoSuchElementException as e:
            action().get_screenShot()
            raise e

    def login(self):
        try:
            operate = operate_yaml(path)
            # operate = operate_yaml(test)
            self.driver.wait_activity(".activity.LoginActivity", think_time)
            sleep(think_time)
            """点击勾选协议按钮"""
            self.driver.tap([(183, 931)])
            operate.operate_yaml('用户名')
            operate.operate_yaml('手机号')
            operate.operate_yaml('下一步')
            operate.operate_yaml('输入密码')
            operate.operate_yaml('登录')
            self.driver.wait_activity(".activity.MainActivity", think_time)
        except EC.NoSuchElementException as e:
            action().get_screenShot()
            raise e


# if __name__ == '__main__':
#     loginBase().login()
#     flag = os.path.exists(path)
#     current = os.getcwd()
#     print(flag, current)