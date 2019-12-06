from base.mobileApp.lanxi.patientBase import patientBase
from Utils.appium_config import DriverClient as DC
import unittest
from Utils.get_toast import get_toast


class add_patient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DC().getDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add(self):
        patient = patientBase()
        patient.add_patient()
        try:
            message = "//*[contains(@text,'添加成功')]"
            toast = get_toast().get_toast(message, self.driver)
            self.assertEquals('添加成功', toast)
        except Exception as e:
            raise e
        finally:
            patient.back_home()

    def test_mod(self):
        patient = patientBase()
        patient.mod_patient()
        try:
            message = "//*[@text='编辑成功']"
            toast = get_toast().get_toast(message, self.driver)
            self.assertEquals('删除就诊人成功', toast)
        except Exception as e:
            raise e
        finally:
            patient.back_home()

    def test_dele(self):
        patient = patientBase()
        patient.dele_patient()
        try:
            message = "//*[@text='删除就诊人成功']"
            toast = get_toast().get_toast(message, self.driver)
            self.assertEquals('删除就诊人成功', toast)
        except Exception as e:
            raise e
        finally:
            patient.back_home()


