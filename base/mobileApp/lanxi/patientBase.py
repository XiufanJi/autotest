from Utils.appium_config import DriverClient as DC
from Utils.operate_yaml import operate_yaml
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from Utils.appium_action import action
from Utils.public_action import pub_action
import random

think_time = 3


class patientBase():
    def __init__(self):
        self.driver = DC().getDriver()
        self.path = pub_action().get_path("yaml/mobile/lanxi/patient.yaml")

    # 返回首页
    def back_home(self):
        try:
            operate = operate_yaml(self.path)
            fall_back = operate.operate_yaml('返回按钮')
            fall_back[0].click()
            self.driver.wait_activity('.activity.HomePageActivity', think_time)
            home = operate.operate_yaml('首页')
            home[0].click()
        except EC.NoSuchElementException as e:
            action().get_screenShot()
            raise e

    # 判断是否能进行就诊人的添加
    def can_add(self):
        try:
            operate = operate_yaml(self.path)
            data = operate.operate_yaml("证件号码")
            num = len(data[0])
            print("定位到的元素总共有多少个：{}".format(num))
            if num >= 5:
                return False
            else:
                return True
        except:
            return False

    # 判断是否能进行就诊人的删除
    def can_dele(self):
        num = 0
        try:
            operate = operate_yaml(self.path)
            data = operate.operate_yaml("证件号码")
            num = len(data[0])
            print("获取到的数据个数为：{}".format(num))
            if num > 0:
                return True
            else:
                return False
        except:
            return False

    def add_patient(self):
        try:
            operate = operate_yaml(self.path)
            # sleep(think_time)
            # operate.operate_yaml('我的')
            sleep(think_time)
            patients = operate.operate_yaml('就诊人管理')
            patients[0].click()
            self.driver.wait_activity(".mine.PatientManagementActivity", think_time)
            sleep(think_time)
            add = patientBase().can_add()
            if add:
                add_patient = operate.operate_yaml('添加')
                add_patient[0].click()
                self.driver.wait_activity(".mine.AddOrEditPatientActivity", think_time)
                sleep(think_time)
                input_name = operate.operate_yaml('请输入姓名')
                input_name[0].send_keys(input_name[1])
                id_type = operate.operate_yaml('选择证件类型')
                id_type[0].click()

                identity = operate.operate_yaml('二代身份证')
                identity[0].click()
                id_no = operate.operate_yaml('证件号')
                id_no[0].send_keys(id_no[1])
                phone_num = operate.operate_yaml('手机号')
                phone_num[0].send_keys(phone_num[1])
                ok_one = operate.operate_yaml('确定')
                ok_one[0].click()
                ok_two = operate.operate_yaml('确定')
                ok_two[0].click()
            else:
                print("已超过最大添加人数，不能再次添加！")
        except EC.NoSuchElementException as e:
            action().get_screenShot()
            raise e

    def mod_patient(self):
        try:
            sleep(think_time)
            operate = operate_yaml(self.path)
            mine = operate.operate_yaml('我的')
            mine[0].click()
            patients = operate.operate_yaml('就诊人管理')
            patients[0].click()
            self.driver.wait_activity(".mine.PatientManagementActivity", think_time)
            can_mod = patientBase().can_dele()
            if can_mod:
                mod = operate.operate_yaml('修改')
                modInfo = random.choice(mod[0])
                modInfo.click()
                self.driver.wait_activity(".mine.AddOrEditPatientActivity", think_time)
                email = operate.operate_yaml('邮箱')
                email[0].send_keys(email[1])
                ok = operate.operate_yaml('确定')
                ok[0].click()
                self.driver.wait_activity(".mine.PatientManagementActivity", think_time)
            else:
                print("就诊人列表为空，不能进行修改！")
        except EC.NoSuchElementException as e:
            action().get_screenShot()
            raise e

    def dele_patient(self):
        try:
            sleep(think_time)
            operate = operate_yaml(self.path)
            mine = operate.operate_yaml('我的')
            mine[0].click()
            patients = operate.operate_yaml('就诊人管理')
            patients[0].click()
            self.driver.wait_activity(".mine.PatientManagementActivity", think_time)
            can_dele = patientBase.can_dele(self)
            if can_dele:
                dele = operate.operate_yaml('删除')
                deleInfo = random.choice(dele[0])
                deleInfo.click()
                ok = operate.operate_yaml('确定')
                ok[0].click()
            else:
                print("就诊人列表为空，不能进行删除操作！")
        except EC.NoSuchElementException as e:
            action().get_screenShot()
            raise e


# if __name__ == '__main__':
#     can_add = patientBase().can_add()
#     print("是否能增加：{}".format(can_add))


