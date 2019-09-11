#测试用例：对就诊人进行修改操作：包括增加非必填信息和修改手机号等操作；
#建议将登录部分优化为公共可调用函数，这样每个操作都可以独立的运行；
import unittest
from Utils.appium_config import DriverClient
class editPatient(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=DriverClient.getDriver()
    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()
    def test_editPatient(self):
        pass

