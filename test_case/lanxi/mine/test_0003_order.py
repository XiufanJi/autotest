import unittest
from Utils.appium_config import DriverClient
from Utils.public_action import action
from Utils.get_toast import get_toast


THINK_TIME = 3


class order(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    """查看预约订单"""
    def test_reservation(self):
        try:
            """我的订单按钮"""
            myorder = "我的订单"
            el_myorder = action().find_byUiautormator("text", myorder)
            el_myorder.click()
            self.driver.wait_activity(".mine.MyOrderActivity", THINK_TIME)
            """统计当前页面预约成功订单的条数"""
            resdetail = "查看详情"
            el_resdetail = action().find_elements_byUiautormator("text", resdetail)
            print("当前页面有多少条订单：{}".format(len(el_resdetail)))
            el_resdetail[0].click()
            self.driver.wait_activity(".mine.MyRegisterDetailActivity", THINK_TIME)
            page_source = self.driver.page_source
            print("当前页面数据{}".format(page_source))
            if "取消预约" in page_source:
                cancleres = "取消预约"
                el_cancleres = action().find_byUiautormator("text", cancleres)
                el_cancleres.click()
                yes = "确定"
                el_yes = action().find_byUiautormator("text", yes)
                el_yes.click()
                cancle = "//*[contains(@text,'已取消')]"
                toast_cancle = get_toast().get_toast(cancle, self.driver)
                self.assertEquals("已取消", toast_cancle)
            else:
                print("当前订单不可取消")
        except Exception as e:
            raise e

    """查看挂号订单"""
    def test_register(self):
        start = "我的预约"
        end = "我的挂号"
        el_start = action().find_byUiautormator("text", start)
        el_end = action().find_byUiautormator("text", end)
        action().element_scroll(el_start, el_end, 200)
        try:
            empty = "暂无挂号信息"
            el_empty = action().find_byUiautormator("text", empty)
            if el_empty.is_displayed():
                print("暂无挂号信息")
        except:
            print("页面挂号信息列表不为空")
        """接着操作查看挂号详情的操作"""
        regdetail = "查看详情"
        el_regdetail = action().find_elements_byUiautormator("text", regdetail)
        print("当前页面有多少条订单：{}".format(len(el_regdetail)))
        el_regdetail[0].click()
        self.driver.wait_activity(".mine.MyRegisterDetailActivity", THINK_TIME)
        """核对详情页面上的数据，感觉有点麻烦"""

        self.driver.find_element_by_image()
        self.driver.find_image_occurrence()


