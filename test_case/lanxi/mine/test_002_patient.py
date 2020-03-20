from base.mobileApp.lanxi.patientBase import patientBase
from Utils.appium_config import DriverClient as DC
import unittest
from Utils.public_action import skip_dependon
from Utils.public_action import pub_action


class patientList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DC().getDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @skip_dependon(depend="test_login")
    def test_01_add(self):
        try:
            patient = patientBase()
            patient.add_patient()
            message = "//*[contains(@text,'添加成功')]"
            toast = pub_action().get_toast(message, self.driver)
            print("获取到的toast信息为：{}".format(toast))
            self.assertEquals('添加成功', toast)
        except:
            patientBase().back_home()

    @skip_dependon(depend="test_login")
    @unittest.skip("skip it")
    def test_02_mod(self):
        try:
            patient = patientBase()
            patient.mod_patient()
            message = "//*[@text='编辑成功']"
            toast = pub_action().get_toast(message, self.driver)
            print("获取到的toast信息为：{}".format(toast))
            self.assertEquals('编辑成功', toast)
        except:
            patientBase().back_home()

    @skip_dependon(depend="test_login")
    @unittest.skip("skip it")
    def test_03_dele(self):
        try:
            toast = None
            patient = patientBase()
            patient.dele_patient()
            message = "//*[@text='删除就诊人成功']"
            toast = pub_action().get_toast(message, self.driver)
            print("获取到的toast信息为：{}".format(toast))
            self.assertEquals('删除就诊人成功', toast)
        except:
            patientBase().back_home()


