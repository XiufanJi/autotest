from base.mobileApp.lanxi.loginBase import loginBase
from Utils.appium_config import DriverClient as DC
import unittest
from Utils.get_toast import get_toast
import os


class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DC().getDriver()
        flag = cls.driver.is_app_installed('com.conlin360.medical')
        print('是否安装了APP：', flag)
        if not flag:
            os.system('adb install app/jiankanglanxi.apk')
            # cls.driver.install_app('app/jiankanglanxi.apk')

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    def test_login(self):
        base = loginBase()
        base.login()
        message = "//*[contains(@text,'登录成功')]"
        toast = get_toast().get_toast(message, self.driver)
        self.assertEquals('登录成功', toast)
        self.assertEquals('.activity.HomePageActivity', self.driver.current_activity)


