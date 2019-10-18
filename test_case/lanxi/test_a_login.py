# coding=utf-8
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from time import sleep
from Utils import publicConfig
from Utils.appium_config import DriverClient



"""
    使用的unittest框架，里面除了固定的setup和teardown方法外，
    其余的测试用例方法都需要以test开头
"""

class login_apps(unittest.TestCase):
    # classmethod:增加该标志后，整个测试过程中，只有用例全部测试完成后才会关闭session\
    # 若不加该标志的话，则执行完一个用例之后，session就会关闭；
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverClient().getDriver()
        flag = cls.driver.is_app_installed("com.conlin360.medical")
        if not flag:
            cls.driver.install_app('app/com.conlin360.medical_1.1.20_15.apk')

    @classmethod
    def tearDownClass(cls):
        # end the session
        cls.driver.quit()
        # pass

    def test_a_login(self):
        current = self.driver.current_activity
        print("当前项目页面的活动名称：", current)
        # APP带有授权弹框，手动点击进行授权操作：如果存在多个的情况下，可考虑循环
        """模拟器每次打开都会进行授权询问，APP则是只需要一次即可"""
        try:
            # pattern = "om.android.packageinstaller:id/permission_allow_button"
            # el = get_toast().element_is_present(self.driver, pattern)
            # for i in range(2):
            #     el.click()
            # self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
            # self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

            # 等待页面活动切换点击页面下方菜单进行过页面切换，
            # 切换至登录页面（"我的"和"登录按钮点击"）
            sleep(5)
            self.driver.wait_activity("com.conlin360.medical.activity.HomePageActivity", 3)
            sleep(5)
            mine = "我的"
            el_mine = self.driver.find_element_by_android_uiautomator("new UiSelector().text(\""+mine+"\")")
            self.assertEqual("我的", el_mine.text)
            el_mine.click()
            login = "登录/注册"
            el_login = self.driver.find_element_by_android_uiautomator("new UiSelector().text(\""+login+"\")")
            self.assertIn("登录", el_login.text)
            el_login.click()
            # 等待切换至当前活动页面
            self.driver.wait_activity("com.conlin360.medical.activity.mine.LoginActivity", 10)
            currentnew = self.driver.current_activity
            print("当前页面的活动名称：", currentnew)

            # 清空输入栏，输入账号密码
            account = "请输入您的手机号码"
            el_account = self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"" + account + "\")")
            self.assertEqual("请输入您的手机号码", el_account.text)
            el_account.clear()
            """验证输入是否合法"""
            # account = str(input("请输入账号："))
            accountResult = re.compile(publicConfig.accountRegx).match('18557539532')
            # accountResult=is_right_phone(account)
            if accountResult != None:
                el_account.send_keys(accountResult.group())
            else:
                print("不合法的账号，请重新输入！")
                input("请输入正确的账号：")

            # password = str(input("请输入密码："))
            passwordResult = re.compile(publicConfig.passregx).match('123456')
            password = "请输入您的密码"
            el_password = self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"" + password + "\")")
            self.assertEqual("请输入您的密码", el_password.text)
            el_password.clear()
            if passwordResult != None:
                el_password.send_keys(passwordResult.group())
            else:
                print("不合法的密码，请重新输入！")
                input("请输入正确的密码：")
            # 点击登录按钮
            login= "登录"
            el_login = self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"" + login + "\")")
            self.assertEqual("登录", el_login.text)
            el_login.click()

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
            self.assertEqual("登录成功", toast_element.text)
        except Exception as msg:
            raise msg
            # print("异常原因：%s" % msg)
            nowdate = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file("Img/%s.png" % nowdate)


