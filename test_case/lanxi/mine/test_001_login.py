from base.mobileApp.lanxi.loginBase import loginBase
from Utils.appium_config import DriverClient as DC
import unittest
from Utils.public_action import pub_action


"""
    使用的unittest框架，里面除了固定的setup和teardown方法外，
    其余的测试用例方法都需要以test开头
"""
# classmethod:增加该标志后，整个测试过程中，只有用例全部测试完成后才会关闭session\
# 若不加该标志的话，则执行完一个用例之后，session就会关闭；
# 获取toast提示信息:一般页面显示的只出现几秒的提示框都是toast类型，
# 有的可能是其它类型
"""
Android中的Toast是一种简易的消息提示框。
当视图显示给用户，在应用程序中显示为浮动。和Dialog不一样的是，
它永远不会获得焦点，无法被点击。用户将可能是在中间键入别的
东西。Toast类的思想就是尽可能不引人注意，同时还向用户显示
信息，希望他们看到。而且Toast显示的时间有限，Toast会根据用
户设置的显示时间后自动消失。

若需要获取toast的内容，使用的驱动必须是uiautomator2
"""


class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DC().getDriver()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    def test_login(self):
        base = loginBase()
        base.login()
        message = "//*[contains(@text,'登录成功')]"
        toast = pub_action().get_toast(message, self.driver)
        print("获取到的页面弹出信息为：{}".format(toast))
        self.assertTrue('登录成功', toast)
        self.assertTrue('.activity.HomePageActivity', self.driver.current_activity)


