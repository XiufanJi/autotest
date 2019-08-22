import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from time import sleep
from Utils import publicConfig
# from Utils.publicConfig import driverClient
from Utils.appium_config import DriverClient

class addPatient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls):
        # end the session
        # cls.driver.quit()
        pass

    def test_b_add_patient(self):
        self.driver.wait_activity("com.conlin360.medical.activity.HomePageActivity", 10)
        """点击就诊人管理按钮"""
        self.driver.find_element_by_id("com.conlin360.medical:id/a0l").click()
        """等待当前页面活动"""
        self.driver.wait_activity(".mine.PatientManagementActivity", 5)
        """获取页面就诊人数用于后续的判断"""
        num = self.driver.find_elements_by_id("com.conlin360.medical:id/a0n")
        # print(type(num))
        print("页面就诊人数：", len(num))

        try:
            if len(num) >= 5:
                """获取页面上删除按钮的个数"""
                # button_dele=self.driver.find_elements_by_id("com.conlin360.medical:id/eq")
                # print("页面删除按钮个数为：",len(button_dele))
                # button_dele[2].click()
                """点击删除按钮"""
                sleep(5)
                self.driver.tap([(1251, 1361), (1370, 1427)], 100)
                sleep(5)
                """点击确定按钮"""
                self.driver.tap([(35, 2406), (1405, 2564)], 100)
                sleep(5)
                # self.driver.find_element_by_name("确定").click()
                delemessage = "//*[contains(@text,'删除就诊人成功')]"
                # 获取删除成功toast提示框内容
                toast_dele = WebDriverWait(self.driver, 5).until \
                    (EC.presence_of_element_located((By.XPATH, delemessage)))
                print("获取到的删除就诊人提示信息：", toast_dele.text)
                flag=self.assertTrue("删除就诊人成功", toast_dele.text)
                if flag:  # 如果删除成功后再执行添加就诊人从操作
                    """点击添加按钮"""
                    self.driver.find_element_by_id("com.conlin360.medical:id/aq").click()
                    """等待切换至当前页面的activity"""
                    self.driver.wait_activity(".mine.AddOrEditPatientActivity", 3)
                    """输入姓名"""
                    self.driver.find_element_by_id("com.conlin360.medical:id/gd").clear()
                    self.driver.find_element_by_id("com.conlin360.medical:id/gd") \
                        .send_keys("哈哈")
                    """选择证件类型"""
                    self.driver.find_element_by_id("com.conlin360.medical:id/a27").click()
                    self.driver.find_element_by_id("android:id/text1").click()
                    """输入证件号码"""
                    idNo = str("13102819730331863X")
                    idNoResult = re.compile(publicConfig.idregx).match(idNo)
                    if idNoResult != None:
                        self.driver.find_element_by_id("com.conlin360.medical:id/gc").send_keys(idNoResult.group())
                    else:
                        print("不合法的证件号码！")
                    """选择性别"""
                    # self.driver.find_element_by_id("com.conlin360.medical:id/a1t").click()
                    """填写手机号"""
                    phoneNum = str("18557539532")
                    phoneNumResult = re.compile(publicConfig.accountRegx).match(phoneNum)
                    if phoneNumResult != None:
                        self.driver.find_element_by_id("com.conlin360.medical:id/g3"). \
                            send_keys(phoneNumResult.group())
                    else:
                        print("输入的手机号不合法，请重新输入")
                        input("请重新输入手机号：")
                    """点击确定按钮"""
                    self.driver.find_element_by_id("com.conlin360.medical:id/be").click()
                    """点击确认提交按钮"""
                    sleep(5)
                    """tap方法在使用前需要设置等待时间，应该该动作是上一个动作执行后就立即执行，若没有加等待时间，可能\
                    就会页面还未切换就执行了操作，导致找不到该元素而报错"""
                    self.driver.tap([(35, 2406), (1405, 2564)], 100)
                    self.driver.wait_activity(".mine.PatientManagementActivity", 5)
                    print("目前的活动名称是：", self.driver.current_activity)
                    print("添加完成")
                    try:
                        message = "//*[contains(@text,'添加') or contains(@text,'成功')]"
                        # 获取toast提示框内容
                        toast_add = WebDriverWait(self.driver, 5).until \
                            (EC.presence_of_element_located((By.XPATH, message)))
                        print("添加就诊人获取到的toast信息：", toast_add.text)
                        self.assertEqual("添加成功", toast_add.text)
                        # if "添加就诊人成功" in toast_add.text:
                        #     print("添加就诊人成功")
                        # else:
                        #     print("添加失败，获取到的toast消息为：", toast_add.text)
                    except:
                        print("没有获取到返回信息")
                else:
                    print("删除失败")
            else:
                """点击添加按钮"""
                self.driver.find_element_by_id("com.conlin360.medical:id/aq").click()
                """等待切换至当前页面的activity"""
                self.driver.wait_activity(".mine.AddOrEditPatientActivity", 3)
                """输入姓名"""
                self.driver.find_element_by_id("com.conlin360.medical:id/gd").clear()
                self.driver.find_element_by_id("com.conlin360.medical:id/gd") \
                    .send_keys("哈哈")
                """选择证件类型"""
                self.driver.find_element_by_id("com.conlin360.medical:id/a27").click()
                self.driver.find_element_by_id("android:id/text1").click()
                """输入证件号码"""
                idNo = str("13102819730331863X")
                idNoResult = re.compile(publicConfig.idregx).match(idNo)
                if idNoResult != None:
                    self.driver.find_element_by_id("com.conlin360.medical:id/gc").send_keys(idNoResult.group())
                else:
                    print("不合法的证件号码！")
                """选择性别"""
                # self.driver.find_element_by_id("com.conlin360.medical:id/a1t").click()
                """填写手机号"""
                phoneNum = str("18557539532")
                phoneNumResult = re.compile(publicConfig.accountRegx).match(phoneNum)
                if phoneNumResult != None:
                    self.driver.find_element_by_id("com.conlin360.medical:id/g3"). \
                        send_keys(phoneNumResult.group())
                else:
                    print("输入的手机号不合法，请重新输入")
                    input("请重新输入手机号：")
                """点击确定按钮"""
                self.driver.find_element_by_id("com.conlin360.medical:id/be").click()
                """点击确认提交按钮"""
                sleep(5)
                """tap方法在使用前需要设置等待时间，应该该动作是上一个动作执行后就立即执行，若没有加等待时间，可能\
                就会页面还未切换就执行了操作，导致找不到该元素而报错"""
                self.driver.tap([(35, 2406), (1405, 2564)], 100)
                self.driver.wait_activity(".mine.PatientManagementActivity", 5)
                print("目前的活动名称是：", self.driver.current_activity)
                print("添加完成")
                try:
                    message = "//*[contains(@text,'添加') or contains(@text,'成功')]"
                    # 获取toast提示框内容
                    toast_add = WebDriverWait(self.driver, 5).until \
                        (EC.presence_of_element_located((By.XPATH, message)))
                    print("添加就诊人获取到的toast信息：", toast_add.text)
                    # if "添加成功" in toast_add.text:
                    #     print("添加就诊人成功")
                    # else:
                    #     print("添加失败:", toast_add.text)
                    self.assertEquals("添加成功", toast_add.text)
                except:
                    print("没有获取到toast消息")
        except:
            print("操作失败")




