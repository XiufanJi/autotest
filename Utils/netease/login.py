from Utils.appium_config import DriverClient
from Utils.netease.authorize import authorize
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

THINK_TIME = 3
WAIT_TIME = 20
class getlogin_method():
    def __init__(self):
        self.driver = DriverClient().getDriver()

    def login_with_mobile(self):
        # pass
        try:
            # sleep(THINK_TIME)
            clickable = authorize().click_agreement()
            if clickable:
                # click login with mobile
                self.driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
            else:
                raise Exception
            self.driver.find_element_by_class_name("android.widget.EditText").send_keys("18557539532")
            self.driver.find_element_by_id("com.netease.cloudmusic:id/anq").click()
            self.driver.find_element_by_id("com.netease.cloudmusic:id/jb").send_keys("123321")
            textview = self.driver.find_elements_by_class_name("android.widget.TextView")
            textview[2].click()
            self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
            print("当前的页面的活动名称为：%s" % self.driver.current_activity)
            # self.assertIn(self.driver.current_activity, "com.netease.cloudmusic.activity.MainActivity")
        except TypeError:
            raise TypeError
            # print("can not locate the element")


    def login_with_guest(self):
        self.driver.find_element_by_id("com.netease.cloudmusic:id/a82").click()
        self.driver.wait_activity("com.netease.cloudmusic.activity.MainActivity", THINK_TIME)
        print("当前的页面的活动名称为：%s" % self.driver.current_activity)
        # tap anywhere in home page to avoid click the recommend menu
        # sleep(THINK_TIME)
        # self.driver.tap([(358,2448)],100)
        sleep(THINK_TIME)



    def login_with_weixin(self):
        authorize().authorize()
        authorize().click_agreement()
        # imageList = self.driver.find_elements_by_class_name("android.widget.ImageView")
        # for i in range(len(imageList)):
        #     print("对应图标的名称为：%s" % imageList[i]., end=" ")
        # click wx icon to login
        self.driver.find_element_by_accessibility_id("wx").click()



    def login_with_qq(self):
        pass
        self.driver.find_element_by_accessibility_id("qq")


    def login_with_neteasy(self):
        pass
        self.driver.find_element_by_accessibility_id("mail")


    def login_with_wb(self):
        pass
        self.driver.find_element_by_accessibility_id("wb")


    def forget_password(self):
        authorize().authorize()
        clickable = authorize().click_agreement()
        if clickable:
            # click login with mobile
            self.driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
        else:
            raise Exception
        # input account
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys("18557539532")
        # click next button
        self.driver.find_element_by_id("com.netease.cloudmusic:id/anq").click()
        sleep(THINK_TIME)
        # click the forget button:need to add sleep method, or couldn't locate it
        self.driver.find_element_by_id("com.netease.cloudmusic:id/anw").click()
        print("当前页面的活动名称为：%s" % self.driver.current_activity)
        sleep(THINK_TIME)
        # input password
        # again,so strange, couldn't use id to locate,so i have to change a method
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys("123321")
        # self.driver.find_element_by_class_name("com.netease.cloudmusic:id/jb").send_keys("123321")
        # click next button
        self.driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
        sleep(THINK_TIME)
        # input verifycode:if use your own database , here can attach your db and get the code
        self.driver.find_element_by_id("com.netease.cloudmusic:id/anv").send_keys("4284")
        # get toast message
        message = "//*[contains(@text,'success') or contains(@text,'成功')]"
        # 获取toast提示框内容
        toast_element = WebDriverWait(self.driver, 5).until \
            (EC.presence_of_element_located((By.XPATH, message)))
        print("忘记密码的toast信息：%s" % toast_element.text)


    def popwindow(self):
        sleep(THINK_TIME)
        TouchAction(self.driver).tap(x=577, y=2356).perform()



