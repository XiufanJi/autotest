from Utils.appium_config import DriverClient as DC
from Utils.operate_yaml import operate_yaml
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from Utils.appium_action import action
from Utils.public_action import pub_action

think_time = 3


class patientBase():
    def __init__(self):
        self.driver = DC().getDriver()
        self.path = pub_action().get_path("yaml/mobile/lanxi/patient.yaml")

    # 判断是否能进行就诊人的添加
    def can_add(self):
        try:
            operate = operate_yaml(self.path)
            idNo = operate.operate_yaml("证件号码")
            num = len(idNo)
            print("定位到的元素总共有多少个：{}".format(num))
            if num >= 5:
                return False
            else:
                return True
        except EC.NoSuchElementException as e:
            action().get_screenShot()
            raise e

    # 判断是否能进行就诊人的删除
    def can_dele(self):
        try:
            operate = operate_yaml(self.path)
            idNo = operate.operate_yaml("证件号码")
            if len(idNo) != 0:
                return True
            else:
                return False
        except EC.NoSuchElementException as e:
            action().get_screenShot()
            raise e

    def add_patient(self):
            try:
                operate = operate_yaml(self.path)
                # sleep(think_time)
                # operate.operate_yaml('我的')
                sleep(think_time)
                operate.operate_yaml('就诊人管理')
                self.driver.wait_activity(".mine.PatientManagementActivity", think_time)
                sleep(think_time)
                can_add = patientBase().can_add()
                if can_add:
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
                else:
                    print("已超过最大添加人数，不能再次添加！")
            except EC.NoSuchElementException as e:
                action().get_screenShot()
                raise e

    def mod_patient(self):
        can_mod = patientBase().can_dele()
        if can_mod:
            try:
                sleep(think_time)
                operate = operate_yaml(self.path)
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
        else:
            print("就诊人列表为空，不能进行修改！")

    def dele_patient(self):
        can_dele = patientBase.can_dele(self)
        if can_dele:
            try:
                sleep(think_time)
                operate = operate_yaml(self.path)
                operate.operate_yaml('我的')
                operate.operate_yaml('就诊人管理')
                self.driver.wait_activity(".mine.PatientManagementActivity", think_time)
                operate.operate_yaml('删除')
                operate.operate_yaml('确定')
            except EC.NoSuchElementException as e:
                action().get_screenShot()
                raise e
        else:
            print("就诊人列表为空，不能进行删除操作！")

    def back_home(self):
        try:
            operate = operate_yaml(self.path)
            operate.operate_yaml('返回按钮')
            self.driver.wait_activity('.activity.HomePageActivity', think_time)
            operate.operate_yaml('首页')
        except EC.NoSuchElementException as e:
            action().get_screenShot()
            raise e


# if __name__ == '__main__':
#     can_add = patientBase().can_add()
#     print("是否能增加：{}".format(can_add))


