# coding=utf-8
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import time
from Utils import publicConfig
from Utils.appium_config import DriverClient


"""
    使用的unittest框架，里面除了固定的setup和teardown方法外，
    其余的测试用例方法都需要以test开头
"""

class login_apps(unittest.TestCase):
    # classmethod:增加该标志后，整个测试过程中，只有用例全部测试完成后才会关闭session\
    # 若不加该标志的话，则执行完一个用例之后，session就会关闭；
    # @classmethod
    # # classmethod:增加该标志后，整个测试过程中，只有用例全部测试完成后才会关闭session\
    # # 若不加该标志的话，则执行完一个用例之后，session就会关闭；
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls):
        # end the session
        # cls.driver.quit()
        pass



    def test_a_login(self):
        current = self.driver.current_activity
        print("当前项目页面的活动名称：", current)
        # APP带有授权弹框，手动点击进行授权操作：如果存在多个的情况下，可考虑循环
        try:
            self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
            self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

            # 等待页面活动切换点击页面下方菜单进行过页面切换，
            # 切换至登录页面（"我的"和"登录按钮点击"）
            self.driver.wait_activity("com.conlin360.medical.activity.HomePageActivity", 10)
            mine = self.driver.find_element_by_id("com.conlin360.medical:id/vh")
            self.assertEqual("我的", mine.text)
            mine.click()
            login = self.driver.find_element_by_id("com.conlin360.medical:id/a0w")
            self.assertIn("登录", login.text)
            login.click()
            # 等待切换至当前活动页面
            self.driver.wait_activity("com.conlin360.medical.activity.mine.LoginActivity", 10)
            currentnew = self.driver.current_activity
            print("当前页面的活动名称：", currentnew)

            # 清空输入栏，输入账号密码
            account = self.driver.find_element_by_id("com.conlin360.medical:id/fx")
            self.assertEqual("请输入您的手机号码", account.text)
            account.clear()
            """验证输入是否合法"""
            # account = str(input("请输入账号："))
            accountResult = re.compile(publicConfig.accountRegx).match('18557539532')
            # accountResult=is_right_phone(account)
            if accountResult != None:
                self.driver.find_element_by_id("com.conlin360.medical:id/fx") \
                    .send_keys(accountResult.group())
            else:
                print("不合法的账号，请重新输入！")
                input("请输入正确的账号：")

            # password = str(input("请输入密码："))
            passwordResult = re.compile(publicConfig.passregx).match('123456')
            password = self.driver.find_element_by_id("com.conlin360.medical:id/fy")
            self.assertEqual("请输入您的密码", password.text)
            password.clear()
            if passwordResult != None:
                # print("输入的密码为：",passwordResult.group())
                self.driver.find_element_by_id("com.conlin360.medical:id/fy") \
                    .send_keys(passwordResult.group())
            else:
                print("不合法的密码，请重新输入！")
                input("请输入正确的密码：")
            # 点击登录按钮
            loginbutton= self.driver.find_element_by_id("com.conlin360.medical:id/d2")
            self.assertEqual("登录", loginbutton.text)
            loginbutton.click()
            # self.driver.find_element_by_link_text()

            # 获取toast提示信息:一般页面显示的只出现几秒的提示框都是toast类型，
            # 有的可能是其它类型
            """
            Android中的Toast是一种简易的消息提示框。
            当视图显示给用户，在应用程序中显示为浮动。和Dialog不一样的是，
            它永远不会获得焦点，无法被点击。用户将可能是在中间键入别的
            东西。Toast类的思想就是尽可能不引人注意，同时还向用户显示
            信息，希望他们看到。而且Toast显示的时间有限，Toast会根据用
            户设置的显示时间后自动消失。
            """
            # try:
            # 用于生成xpath定位 相当于 "//*[@text='没有找到用户名或密码']",
            # 这种方法为精确匹配的方法
            # xpath提取toast信息，//*表示页面上的所有元素，下面的表达式为
            # ：提取页面上所有文字类型信息，且文字中包含“用户”或者“成功”
            message = "//*[contains(@text,'用户') or contains(@text,'成功')]"
            # 获取toast提示框内容
            toast_element = WebDriverWait(self.driver, 5).until \
                (EC.presence_of_element_located((By.XPATH, message)))
            print("登录获取到的toast信息：", toast_element.text)
            # if toast_element.text == "登录成功":
            #     print("登录成功")
            # else:
            #     print("登录失败:", toast_element.text)
            self.assertEqual("登录成功", toast_element.text)
            # except Exception as msg:
            #     raise msg
        except Exception as msg:
            raise msg
            # print("异常原因：%s" % msg)
            nowdate = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file("Img/%s.png" % nowdate)

    # @unittest.skip("skip this testcase")
    # def test_b_add_patient(self):
    #
    #     self.driver.wait_activity("com.conlin360.medical.activity.HomePageActivity", 10)
    #     """点击就诊人管理按钮"""
    #     self.driver.find_element_by_id("com.conlin360.medical:id/a04").click()
    #     """等待当前页面活动"""
    #     self.driver.wait_activity(".mine.PatientManagementActivity", 5)
    #     """获取页面就诊人数用于后续的判断"""
    #     num= self.driver.find_elements_by_id("com.conlin360.medical:id/a06")
    #     # print(type(num))
    #     print("页面就诊人数：", len(num))
    #
    #     try:
    #         if len(num) >= 5:
    #             """获取页面上删除按钮的个数"""
    #             # button_dele=self.driver.find_elements_by_id("com.conlin360.medical:id/eq")
    #             # print("页面删除按钮个数为：",len(button_dele))
    #             # button_dele[2].click()
    #             """点击删除按钮"""
    #             sleep(5)
    #             self.driver.tap([(1251, 1361), (1370, 1427)], 100)
    #             sleep(5)
    #             """点击确定按钮"""
    #             self.driver.tap([(35, 2406), (1405, 2564)], 100)
    #             sleep(5)
    #             # self.driver.find_element_by_name("确定").click()
    #             delemessage = "//*[contains(@text,'删除就诊人成功')]"
    #             # 获取删除成功toast提示框内容
    #             toast_dele = WebDriverWait(self.driver, 5).until \
    #                 (EC.presence_of_element_located((By.XPATH, delemessage)))
    #             print("获取到的删除就诊人提示信息：", toast_dele.text)
    #             if "删除成功" in toast_dele.text:  # 如果删除成功后再执行添加就诊人从操作
    #                 """点击添加按钮"""
    #                 self.driver.find_element_by_id("com.conlin360.medical:id/am").click()
    #                 """等待切换至当前页面的activity"""
    #                 self.driver.wait_activity(".mine.AddOrEditPatientActivity", 3)
    #                 """输入姓名"""
    #                 self.driver.find_element_by_id("com.conlin360.medical:id/g9").clear()
    #                 self.driver.find_element_by_id("com.conlin360.medical:id/g9") \
    #                     .send_keys("哈哈")
    #                 """选择证件类型"""
    #                 self.driver.find_element_by_id("com.conlin360.medical:id/a1p").click()
    #                 self.driver.find_element_by_id("android:id/text1").click()
    #                 """输入证件号码"""
    #                 idNo = str("13102819730331863X")
    #                 idNoResult = re.compile(idregx).match(idNo)
    #                 if idNoResult != None:
    #                     self.driver.find_element_by_name("请输入证件号码").send_keys(idNoResult.group())
    #                 else:
    #                     print("不合法的证件号码！")
    #                 """选择性别"""
    #                 # self.driver.find_element_by_id("com.conlin360.medical:id/a1t").click()
    #                 """填写手机号"""
    #                 phoneNum = str("18557539532")
    #                 phoneNumResult = re.compile(accountRegx).match(phoneNum)
    #                 if phoneNumResult != None:
    #                     self.driver.find_element_by_name("用于接收短信通知，请谨慎填写"). \
    #                         send_keys(phoneNumResult.group())
    #                 else:
    #                     print("输入的手机号不合法，请重新输入")
    #                     input("请重新输入手机号：")
    #                 """点击确定按钮"""
    #                 self.driver.find_element_by_id("com.conlin360.medical:id/ba").click()
    #                 """点击确认提交按钮"""
    #                 self.driver.wait_activity(".mine.PatientManagementActivity", 5)
    #                 print("添加完成")
    #                 try:
    #                     message = "//*[contains(@text,'添加') or contains(@text,'成功')]"
    #                     # 获取toast提示框内容
    #                     toast_add = WebDriverWait(self.driver, 5).until \
    #                         (EC.presence_of_element_located((By.XPATH, message)))
    #                     print("添加就诊人获取到的toast信息：", toast_add.text)
    #                     if "添加就诊人成功" in toast_add.text:
    #                         print("添加就诊人成功")
    #                     else:
    #                         print("添加失败:", toast_element.text)
    #                 except:
    #                     print("没有获取到返回信息")
    #             else:
    #                 print("删除失败")
    #         else:
    #             """点击添加按钮"""
    #             self.driver.find_element_by_id("com.conlin360.medical:id/am").click()
    #             """等待切换至当前页面的activity"""
    #             self.driver.wait_activity(".mine.AddOrEditPatientActivity", 3)
    #             """输入姓名"""
    #             self.driver.find_element_by_id("com.conlin360.medical:id/g9").clear()
    #             self.driver.find_element_by_id("com.conlin360.medical:id/g9") \
    #                 .send_keys("花花")
    #             """选择证件类型"""
    #             self.driver.find_element_by_id("com.conlin360.medical:id/a1p").click()
    #             self.driver.find_element_by_id("android:id/text1").click()
    #             """输入证件号码"""
    #             idNo = str("44020219950106195X")
    #             idNoResult = re.compile(idregx).match(idNo)
    #             if idNoResult != None:
    #                 self.driver.find_element_by_id("com.conlin360.medical:id/g8").send_keys(idNoResult.group())
    #             else:
    #                 print("不合法的证件号码！")
    #                 input("请重新输入证件号")
    #             """选择性别"""
    #             # self.driver.find_element_by_id("com.conlin360.medical:id/a1t").click()
    #             """填写手机号"""
    #             phoneNum = str('18557539532')
    #             phoneNumResult = re.compile(accountRegx).match(phoneNum)
    #             if phoneNumResult != None:
    #                 self.driver.find_element_by_id("com.conlin360.medical:id/fy"). \
    #                     send_keys(phoneNumResult.group())
    #             else:
    #                 print("输入的手机号不合法，请重新输入")
    #                 input("请重新输入手机号：")
    #             """右上角点击确定按钮"""
    #             self.driver.find_element_by_id("com.conlin360.medical:id/ba").click()
    #             """点击确认提交按钮"""
    #             sleep(5)
    #             """tap方法在使用前需要设置等待时间，应该该动作是上一个动作执行后就立即执行，若没有加等待时间，可能\
    #             就会页面还未切换就执行了操作，导致找不到该元素而报错"""
    #             self.driver.tap([(35,2406),(1405,2564)],100)
    #             self.driver.wait_activity(".mine.PatientManagementActivity",5)
    #             print("目前的活动名称是：",self.driver.current_activity)
    #             print("添加完成")
    #             try:
    #                 message = "//*[contains(@text,'添加') or contains(@text,'成功')]"
    #                 # 获取toast提示框内容
    #                 toast_add = WebDriverWait(self.driver, 5).until \
    #                     (EC.presence_of_element_located((By.XPATH, message)))
    #                 print("添加就诊人获取到的toast信息：", toast_add.text)
    #                 if "添加成功" in toast_add.text:
    #                     print("添加就诊人成功")
    #                 else:
    #                     print("添加失败:", toast_element.text)
    #             except(UiAutomator2Exception):
    #                 pass
    #     except:
    #         print("操作失败")
    #
    # # @unittest.skip("skip this testcase")
    # def test_c_order(self):
    #     self.driver.wait_activity(".mine.PatientManagementActivity",5)
    #     """点击持卡人列表页面上的返回按钮，返回我的页面"""
    #     self.driver.find_element_by_accessibility_id("Navigate up").click()
    #     """等待切换为主页的活动"""
    #     self.driver.wait_activity(".HomePageActivity",5)
    #     """点击首页按钮"""
    #     self.driver.find_element_by_id("com.conlin360.medical:id/v2").click()
    #     """点击页面上的预约挂号"""
    #     self.driver.find_element_by_id("com.conlin360.medical:id/mm").click()
    #     """等待活动切换"""
    #     self.driver.wait_activity(".hospital.HospitalListActivity",3)
    #     """获取医院列表"""
    #     hospitalLists=self.driver.find_elements_by_class_name("android.widget.LinearLayout")
    #     """点击医院列表中的第一个医院进行查看"""
    #     hospitalLists[0].click()
    #     """等待活动切换"""
    #     self.driver.wait_activity(".hospital.DeptListActivity",3)
    #     depts=self.driver.find_elements_by_class_name("android.widget.RelativeLayout")
    #     # if len(depts)>5:
    #     #     self.driver.swipe()
    #     depts[2].click()
    #     """等待活动切换"""
    #     self.driver.wait_activity(".hospital.DoctorScheduleListActivity",3)
    #     self.driver.find_element_by_id("com.conlin360.medical:id/a1_").click()
    #     self.driver.wait_activity(".hospital.DoctorScheduleSourceListActivity",3)
    #     scheduleSource=self.driver.find_elements_by_id("com.conlin360.medical:id/mw")
    #     scheduleSource[0].click()
    #     self.driver.wait_activity(".hospital.ConfirmAppointActivity",3)
    #     """确认预约/挂号：若有持卡人则点击确定，若无则进行新增操作"""
    #     if len(num)>0:
    #         """点击挂号/预约确认页面上的确定按钮"""
    #         self.driver.find_element_by_id("com.conlin360.medical:id/d0").click()
    #         sleep(5)
    #         self.driver.tap([(35, 2406), (1405, 2564)], 100)
    #     else:
    #         pass


