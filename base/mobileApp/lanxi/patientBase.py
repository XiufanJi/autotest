from Utils.appium_config import DriverClient as DC
from Utils.operate_yaml import operate_yaml
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from Utils.appium_action import action
path = 'yaml/mobile/lanxi/patient.yaml'
think_time = 3


class patientBase():
    def __init__(self):
        self.driver = DC().getDriver()

    def can_add_patient(self):
        pass

    def add_patient(self):
        try:
            operate = operate_yaml(path)
            # sleep(think_time)
            # operate.operate_yaml('我的')
            sleep(think_time)
            operate.operate_yaml('就诊人管理')
            self.driver.wait_activity(".mine.PatientManagementActivity", think_time)
            sleep(think_time)
            operate.operate_yaml('添加')
            self.driver.wait_activity(".mine.AddOrEditPatientActivity", think_time)
            sleep(think_time)
            operate.operate_yaml('请输入姓名')
            operate.operate_yaml('选择证件类型')
            operate.operate_yaml('二代身份证')
            operate.operate_yaml('证件号')
            operate.operate_yaml('手机号')
            operate.operate_yaml('确定')
            operate.operate_yaml('确定')
        except EC.NoSuchElementException as e:
            action().get_screenShot()
            raise e

    def mod_patient(self):
        try:
            sleep(think_time)
            operate = operate_yaml(path)
            operate.operate_yaml('我的')
            operate.operate_yaml('就诊人管理')
            self.driver.wait_activity(".mine.PatientManagementActivity", think_time)
            operate.operate_yaml('修改')
            self.driver.wait_activity(".mine.AddOrEditPatientActivity", think_time)
            operate.operate_yaml('邮箱')
            operate.operate_yaml('确定')
            self.driver.wait_activity(".mine.PatientManagementActivity", think_time)
        except EC.NoSuchElementException as e:
            action().get_screenShot()
            raise e

    def dele_patient(self):
        try:
            sleep(think_time)
            operate = operate_yaml(path)
            operate.operate_yaml('我的')
            operate.operate_yaml('就诊人管理')
            self.driver.wait_activity(".mine.PatientManagementActivity", think_time)
            operate.operate_yaml('删除')
            operate.operate_yaml('确定')
        except EC.NoSuchElementException as e:
            action().get_screenShot()
            raise e

    def back_home(self):
        try:
            operate = operate_yaml(path)
            operate.operate_yaml('返回按钮')
            self.driver.wait_activity('.activity.HomePageActivity', think_time)
            operate.operate_yaml('首页')
        except EC.NoSuchElementException as e:
            action().get_screenShot()
            raise e

