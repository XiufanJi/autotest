import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import time
from time import sleep
from Utils import publicConfig
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

    @unittest.skip("skip it")
    def test_b_add_patient(self):
        try:
            self.driver.wait_activity("com.conlin360.medical.activity.HomePageActivity", 10)
            """点击就诊人管理按钮"""
            patientlist = self.driver.find_element_by_id("com.conlin360.medical:id/a0l")
            self.assertEqual("就诊人管理", patientlist.text)
            patientlist.click()
            """等待当前页面活动"""
            self.driver.wait_activity(".mine.PatientManagementActivity", 5)
            current = self.driver.current_activity
            print("当前页面的activity名称：", current)
            """获取页面就诊人数用于后续的判断"""
            num = self.driver.find_elements_by_id("com.conlin360.medical:id/a0n")
            # print(type(num))
            print("页面就诊人数：", len(num))
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
                delemessage = "//*[contains(@text,'删除') or contains(@text,'成功')]"
                # 获取删除成功toast提示框内容
                toast_dele = WebDriverWait(self.driver, 5).until \
                    (EC.presence_of_element_located((By.XPATH, delemessage)))
                print("获取到的删除就诊人提示信息：", toast_dele.text)
                self.assertIn(toast_dele.text, "删除就诊人成功")
                if toast_dele.text in "删除就诊人成功":  # 如果删除成功后再执行添加就诊人从操作
                    """点击添加按钮"""
                    """判断页面上存在的就诊人是否与添加的就诊人信息重复"""
                    namenew="小白"
                    memberlist= self.driver.find_elements_by_id("com.conlin360.medical:id/a0n")
                    for member in memberlist:
                        if namenew in member.text:
                            print("已经存在该就诊人，不能重复进行添加")
                            break
                        else:
                            add = self.driver.find_element_by_id("com.conlin360.medical:id/aq")
                            self.assertEqual("添加", add.text)
                            add.click()
                            """等待切换至当前页面的activity"""
                            self.driver.wait_activity(".mine.AddOrEditPatientActivity", 3)
                            addpage = self.driver.current_activity
                            print("addpage页面的activity名称：", addpage)
                            """输入姓名"""
                            name = self.driver.find_element_by_id("com.conlin360.medical:id/gd")
                            self.assertIn("请输入姓名", name.text)
                            name.clear()
                            self.driver.find_element_by_id("com.conlin360.medical:id/gd") \
                                .send_keys(namenew)
                            """选择证件类型"""
                            self.driver.find_element_by_id("com.conlin360.medical:id/a27").click()
                            self.driver.find_element_by_id("android:id/text1").click()
                            """输入证件号码"""
                            idNo = str("420301200411184113")
                            idNoResult = re.compile(publicConfig.idregx).match(idNo)
                            identity= self.driver.find_element_by_id("com.conlin360.medical:id/gc")
                            self.assertEqual("请输入证件号码", identity.text)
                            identity.clear()
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
                            okbutton= self.driver.find_element_by_id("com.conlin360.medical:id/be")
                            self.assertEqual("确定", okbutton.text)
                            okbutton.click()
                            """点击确认提交按钮"""
                            sleep(5)
                            """tap方法在使用前需要设置等待时间，应该该动作是上一个动作执行后就立即执行，若没有加等待时间，可能\
                            就会页面还未切换就执行了操作，导致找不到该元素而报错"""
                            self.driver.tap([(35, 2406), (1405, 2564)], 100)
                            self.driver.wait_activity(".mine.PatientManagementActivity", 5)
                            message = "//*[contains(@text,'添加') or contains(@text,'成功')]"
                            # 获取toast提示框内容
                            toast_add = WebDriverWait(self.driver, 5).until \
                                (EC.presence_of_element_located((By.XPATH, message)))
                            print("添加就诊人获取到的toast信息：", toast_add.text)
                            self.assertIn(toast_add.text, "添加就诊人成功")
                            print("目前的活动名称是：", self.driver.current_activity)
                            print("添加完成")
                            # if "添加就诊人成功" in toast_add.text:
                            #     print("添加就诊人成功")
                            # else:
                            #     print("添加失败，获取到的toast消息为：", toast_add.text)
                            # print("没有获取到返回信息")
                else:
                    print("删除失败")
            else:
                """点击添加按钮"""
                add = self.driver.find_element_by_id("com.conlin360.medical:id/aq")
                self.assertEqual("添加", add.text)
                add.click()
                """等待切换至当前页面的activity"""
                self.driver.wait_activity(".mine.AddOrEditPatientActivity", 3)
                addpage = self.driver.current_activity
                print("addpage页面的activity名称：", addpage)
                """输入姓名"""
                name= self.driver.find_element_by_id("com.conlin360.medical:id/gd")
                self.assertIn("请输入姓名" , name.text)
                name.clear()
                self.driver.find_element_by_id("com.conlin360.medical:id/gd") \
                    .send_keys("花花")
                """选择证件类型"""
                self.driver.find_element_by_id("com.conlin360.medical:id/a27").click()
                self.driver.find_element_by_id("android:id/text1").click()
                """输入证件号码"""
                idNo = str("430903194811082668")
                idNoResult = re.compile(publicConfig.idregx).match(idNo)
                identity= self.driver.find_element_by_id("com.conlin360.medical:id/gc")
                self.assertEqual("请输入证件号码", identity.text)
                identity.clear()
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
                okbutton= self.driver.find_element_by_id("com.conlin360.medical:id/be")
                self.assertEqual("确定", okbutton.text)
                okbutton.click()
                """点击确认提交按钮"""
                sleep(5)
                """tap方法在使用前需要设置等待时间，应该该动作是上一个动作执行后就立即执行，若没有加等待时间，可能\
                就会页面还未切换就执行了操作，导致找不到该元素而报错"""
                self.driver.tap([(35, 2406), (1405, 2564)], 100)
                self.driver.wait_activity(".mine.PatientManagementActivity", 5)
                message = "//*[contains(@text,'添加') or contains(@text,'成功')]"
                # 获取toast提示框内容
                toast_add = WebDriverWait(self.driver, 5).until \
                    (EC.presence_of_element_located((By.XPATH, message)))
                print("添加就诊人获取到的toast信息：", toast_add.text)
                self.assertIn(toast_add.text, "添加成功")
                print("目前的活动名称是：", self.driver.current_activity)
                print("添加完成")
                # if "添加就诊人成功" in toast_add.text:
                #     print("添加就诊人成功")
                # else:
                #     print("添加失败，获取到的toast消息为：", toast_add.text)
                # print("没有获取到返回信息")
        except Exception as msg:
            raise  msg
            print("异常原因：%s" % msg)
            nowdate = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file("Img/%s.png" % nowdate)






