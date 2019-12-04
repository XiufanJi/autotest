from Utils.appium_config import DriverClient as DC
from Utils.operate_yaml import operate_yaml
from time import sleep
import time
import os
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
            # sleep(think_time)
            # """返回主页"""
            # operate.operate_yaml('首页')
        except Exception as e:
            raise e
        #     dirName = time.strftime("%Y%m%d")
        #     filePath = 'screenShots/' + dirName
        #     if not os.path.exists(filePath):
        #         os.mkdir(filePath)
        #     else:
        #         # 获取截图有问题，暂时先不管
        #         nowdate = time.strftime("%Y%m%d %H:%M:%S")
        #         print("文件存储路径："+filePath+"/%s.png" % nowdate)
        #         picPath = filePath+"/%s.png" % nowdate
        #         self.driver.get_screenshot_as_file(picPath)
        #         # os.system('adb exec-out screencap -p > '+filePath+'/{}.png'.format(nowdate))