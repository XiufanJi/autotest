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

    # @unittest.skipIf()
    def test_add(self):
        patient = patientBase()
        patient.add_patient()
        message = "//*[contains(@text,'添加成功')]"
        toast = get_toast().get_toast(message, self.driver)
        self.assertEquals('添加成功', toast)


