import unittest
from base.mobileApp.netease.loginBase import loginBase
from Utils.appium_config import DriverClient as DC
from Utils.public_action import action


class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DC().getDriver()
        flag = cls.driver.is_app_installed('com.netease.cloudmusic')
        print('是否有安装相应的app：', flag)
        if flag:
            pass
        else:
            cls.driver.install_app('app/com.netease.cloudmusic_6.3.2_152.apk')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        print("- - - - - - -开始执行执行测试- - - - - - -")
        flag = action().isFirstLogin()
        if flag:
            loginBase().firstLogin()
        else:
            loginBase().login()
        self.assertEquals(self.driver.current_activity, '.activity.MainActivity')
        print("- - - - - - - - -测试结束- - - - - - - - -")













