from Utils.appium_config import DriverClient as DC
from Utils.operate_yaml import operate_yaml
from time import sleep
path = 'yaml/mobile/lanxi/patient.yaml'
think_time = 3


class patientBase():
    def __init__(self):
        self.driver = DC().getDriver()

    def can_add_patient(self):
        pass

    def add_patient(self):
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
        sleep(think_time)
        operate.operate_yaml('选择证件类型')
        sleep(think_time)
        operate.operate_yaml('二代身份证')
        sleep(think_time)
        operate.operate_yaml('证件号')
        sleep(think_time)
        operate.operate_yaml('手机号')
        sleep(think_time)
        operate.operate_yaml('确定')
        sleep(think_time)
        operate.operate_yaml('确定')
