import unittest
import time
from time import sleep
from Utils.appium_config import DriverClient
from Utils.public_action import action
from Utils.get_toast import get_toast
from random import choice
from appium.webdriver.common.touch_action import TouchAction


THINK_TIME = 5
nameList = ["小可", "小云", "小狼", "小樱", "芝士就是力量", "雪兔", "美咲"]
idNoList = ["500100199802183705", "500100199802181574"]


class addPatient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls):
        # end the session
        # cls.driver.quit()
        pass

    """对就诊人进行添加删除和修改等操作"""
    @unittest.skip("skip it")
    def test_01_delete(self):
        try:
            self.driver.wait_activity(".HomePageActivity", 10)
            """点击就诊人管理按钮"""
            myPatient = "就诊人管理"
            el_myPatient = action().find_byUiautormator("text", myPatient)
            el_myPatient.click()
            """等待当前页面活动"""
            self.driver.wait_activity(".mine.PatientManagementActivity", 5)
            current = self.driver.current_activity
            print("当前页面的activity名称：", current)
            """获取页面就诊人数用于后续的判断"""
            identities = "证件号码"
            num = action().find_elements_byUiautormator("textContains", identities)
            # print(type(num))
            print("页面就诊人数：", len(num))
            print("页面模式从contexts:%s", self.driver.contexts)
            if len(num) != 0:
                """获取页面上删除按钮的个数并进行删除"""
                button_dele = self.driver.find_elements_by_id("com.conlin360.medical:id/ev")
                button_dele[len(num)-1].click()
                """点击确定按钮"""
                area = action().get_window_size()
                print("页面区域的长宽为{}".format(area))
                sleep(THINK_TIME)
                """弹出框区域不能find查找点击，使用tap方法"""
                TouchAction(self.driver).tap(x=0.5*area[0], y=0.9*area[1]).release().perform()
                delemessage = "//*[contains(@text,'删除') or contains(@text,'成功')]"
                # 获取删除成功toast提示框内容，toast信息获取感觉不是很靠谱，基本靠运气。
                toast_dele = get_toast().get_toast(delemessage, self.driver)
                print("获取到的删除就诊人提示信息：", toast_dele)
                self.assertIn(toast_dele, "删除就诊人成功")
            else:
                print("就诊人列表为空")
        except Exception as msg:
            print("异常原因：%s" % msg)
            nowdate = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file("screenShots/%s.png" % nowdate)
            raise msg

    @unittest.skip("skip it")
    def test_02_add(self):
        try:
            sleep(THINK_TIME)
            """点击添加按钮"""
            add = "添加"
            el_add = action().find_byUiautormator("text", add)
            el_add.click()
            """页面activity转换"""
            self.driver.wait_activity(".mine.AddOrEditPatientActivity", THINK_TIME)
            nameblank = "请输入姓名"
            el_nameblank = action().find_byUiautormator("text", nameblank)
            name = choice(nameList)
            print("选中的名字是{}".format(name))
            el_nameblank.send_keys(name)
            identityType = "证件类型"
            el_identityType = action().find_byUiautormator("text", identityType)
            el_identityType.click()
            idcard = "二代身份证"
            el_idcard = action().find_byUiautormator("text", idcard)
            el_idcard.click()
            idNoBlank = "请输入证件号码"
            el_idNoBlank = action().find_byUiautormator("text", idNoBlank)
            idNo = choice(idNoList)
            print("选中的身份证号码为{}".format(idNo))
            el_idNoBlank.send_keys(idNo)
            # phoneBlank = "接收短信"
            # el_phoneBlank = action().find_byUiautormator("textContains", phoneBlank)
            # phoneNo = "19999999999"
            # el_phoneBlank.send_keys(phoneNo)
            notNecessary = "非必填"
            el_notNecessary = action().find_byUiautormator("text", notNecessary)
            # print("非必填项有几个：{0}{1}" .format(el_notNecessary.__len__(), el_notNecessary))
            el_notNecessary.send_keys("haha@qq.com")
            el_notNecessary = action().find_byUiautormator("text", notNecessary)
            el_notNecessary.send_keys("长江大桥下的第一排桥洞中的第三个桥洞")
            yes = "确定"
            el_yes = action().find_byUiautormator("text", yes)
            el_yes.click()
            """点击弹框中的确定按钮"""
            area = action().get_window_size()
            print("页面区域的长宽为{}".format(area))
            sleep(THINK_TIME)
            """弹出框区域不能find查找点击，使用tap方法"""
            TouchAction(self.driver).tap(x=0.5 * area[0], y=0.9 * area[1]).release().perform()
            self.driver.wait_activity(".mine.PatientManagementActivity", THINK_TIME)
            add_message = "//*[contains(@text,'添加成功')]"
            toast_add = get_toast().get_toast(add_message, self.driver)
            print("获取到的toast信息：{}".format(toast_add))
            self.assertEquals("添加成功", toast_add)
        except Exception as e:
            raise e

    @unittest.skip("skip it")
    def test_03_edit(self):
        """测试编辑病人功能"""
        try:
            myPatient = "就诊人管理"
            el_myPatient = action().find_byUiautormator("text", myPatient)
            el_myPatient.click()
            """获取页面就诊人数用于后续的判断"""
            identities = "证件号码"
            num = action().find_elements_byUiautormator("textContains", identities)
            # print(type(num))
            print("页面就诊人数：", len(num))
            sleep(THINK_TIME)
            """点击编辑按钮"""
            edit = "com.conlin360.medical:id/fs"
            el_edit = self.driver.find_elements_by_id(edit)
            """选择最后一条进行编辑"""
            el_edit[len(num)-1].click()
            self.driver.wait_activity(".mine.AddOrEditPatientActivity", THINK_TIME)
            """这段有问题，find元素后，进行clear操作，再send key 就会报错，提示该元素已经不在DOM树中"""
            # email = "@"
            # el_email = action().find_byUiautormator("textContains", email)
            # el_email.clear()
            # el_email.send_keys("lalala@haha.com")
            # phonenum = "0123456789"
            # el_phonenum = action().find_byUiautormator(phonenum)
            # el_phonenum.clear()
            # el_phonenum.send_keys("1999999999")
            phone = self.driver.find_element_by_id("com.conlin360.medical:id/g3")
            phone.clear()
            phone.send_keys("19999999999")
            """点击确定按钮"""
            yes = "确定"
            el_yes = action().find_byUiautormator("text", yes)
            el_yes.click()
            add_message = "//*[contains(@text,'编辑成功')]"
            toast_edit = get_toast().get_toast(add_message, self.driver)
            print("获取到的toast信息：{}".format(toast_edit))
            self.assertEquals("编辑成功", toast_edit)
            self.driver.wait_activity(".mine.AddOrEditPatientActivity", THINK_TIME)
        except Exception as e:
            raise e









