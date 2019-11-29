import unittest
from base.mobileApp.netease.loginBase import loginBase
from Utils.appium_config import DriverClient as DC


class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DC().getDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_a_login(self):
        loginBase()













