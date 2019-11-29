from Utils.operate_yaml import operate_yaml
from Utils.appium_config import DriverClient as DC
from time import sleep

path = '../yaml/mobileApp/netease/login.yaml'
think_time = 3

class loginBase():
    """登录操作"""
    def __init__(self):
        self.driver = DC().getDriver()

    def loginBase(self):
        operate = operate_yaml(path)
        self.driver.wait_activity(".activity.IntroduceActivity", think_time)
        operate.operate_yaml('同意')
        operate.operate_yaml('进入APP')
