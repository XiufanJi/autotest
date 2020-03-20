from Utils.appium_config import DriverClient as DC
from Utils.operate_yaml import operate_yaml
from time import sleep
from Utils.appium_action import action
from Utils.public_action import pub_action

think_time = 2


class loginBase():
    def __init__(self):
        self.driver = DC().getDriver()
        self.path = pub_action().get_path("yaml/mobile/lanxi/login.yaml")

    def firstLogin(self):
        pass

    def login(self):
        try:
            operate = operate_yaml(self.path)
            self.driver.wait_activity('.activity.HomePageActivity', think_time)
            sleep(think_time)
            mine = operate.operate_yaml('我的')
            # print(mine)
            # print("返回的元素：{}".format(mine[0]))
            mine[0].click()
            sleep(think_time)
            login = operate.operate_yaml('登录/注册')
            login[0].click()
            sleep(think_time)
            self.driver.wait_activity(".activity.mine.LoginActivity", think_time)
            sleep(think_time)
            try:
                """第一次登录"""
                phone = operate.operate_yaml('手机号码')
                phone[0].clear()
                phone[0].send_keys(phone[1])
            except:
                """非首次登录"""
                dele_num = operate.operate_yaml('清除手机号')
                dele_num[0].click()
                sleep(think_time)
                phone = operate.operate_yaml('手机号码')
                phone[0].clear()
                phone[0].send_keys(phone[1])
            sleep(think_time)
            password = operate.operate_yaml('登录密码')
            password[0].send_keys(password[1])
            sleep(think_time)
            login = operate.operate_yaml('登录')
            login[0].click()
            self.driver.wait_activity('.activity.HomePageActivity', think_time)
        except Exception as e:
            action().get_screenShot()
            raise e