import unittest
from Utils.appium_config import DriverClient
from Utils.action_config import action
from Utils.get_toast import get_toast


THINK_TIME = 5


class order(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.quit()

    """查看预约订单"""
    def reservation(self):
        pass
        """我的订单按钮"""
        myorder = "我的订单"
        el_myorder = action().find_byUiautormator("text", myorder)
        el_myorder.click()
        self.driver.wait_activity(".mine.MyOrderActivity", THINK_TIME)
        """统计当前页面预约成功订单的条数"""
        ressuccess = "预约成功"
        el_ressuccess = action().find_elements_byUiautormator("text", ressuccess)
        print("当前页面有多少条成功订单：{}".format(len(el_ressuccess)))
        el_ressuccess[0].click()
        self.driver.wait_activity(".mine.MyRegisterDetailActivity", THINK_TIME)
        page_source = self.driver.page_source
        print("当前页面数据{}".format(page_source))
        if "取消预约" in page_source:
            cancleres = "取消预约"
            el_cancleres = action().find_byUiautormator("text", cancleres)
            el_cancleres.click()
            cancle = "//*[contains(@text,'取消') or contains(@text,'成功')]"
            toast_cancle = get_toast().get_toast(cancle, self.driver)
            self.assertEquals("取消成功", toast_cancle)

    """查看挂号订单"""
    def register(self):
        pass