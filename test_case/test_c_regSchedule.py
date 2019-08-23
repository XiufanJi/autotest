import unittest
from Utils.appium_config import DriverClient
import time
from time import sleep
from random import randrange

# time for waiting change action
THINK_TIME = 5

class regSchedule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_c_regSchedule(self):
        sleep(THINK_TIME)
        # press back button
        try:
            self.driver.find_element_by_accessibility_id("Navigate up").click()
            self.driver.wait_activity(".HomePageActivity", THINK_TIME)
            # press home button
            home = self.driver.find_element_by_id("com.conlin360.medical:id/vi")
            self.assertEqual("首页", home.text)
            home.click()
            # press reg button
            self.driver.find_element_by_id("com.conlin360.medical:id/ms").click()
            # self.assertEqual("", regbutton.text)
            self.driver.wait_activity(".hospital.HospitalListActivity", THINK_TIME)
            hospitallists = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
            # hospitalLists[0].click()
            goal = randrange(0,len(hospitallists))
            hospitallists[goal].click()
            print("选择的医院名称为：", hospitallists[goal].text)
            self.driver.wait_activity(".hospital.DeptListActivity", THINK_TIME)
            # judge whether deptlist is empty
            emptydepts = self.driver.find_element_by_class_name("android.widget.TextView")
            while emptydepts.text == "暂无科室信息":
                # press back button
                self.driver.find_element_by_class_name("android.widget.ImageButton").click()
                for hospital in hospitallists:
                    hospital.click()
                self.driver.wait_activity(".hospital.DeptListActivity", THINK_TIME)
            # find depts list
            deptlists = self.driver.find_elements_by_id("com.conlin360.medical:id/ex")
            dept = randint(len(deptlists))
            deptlists[dept].click()
            self.driver.wait_activity(".hospital.DoctorScheduleListActivity", THINK_TIME)

            flag = self.driver.find_element_by_class_name("android.widget.TextView")
            while flag.text == "暂无医生排班信息":
                self.driver.find_element_by_class_name("android.widget.ImageButton").click()
                for deptschedule in deptlists:
                    deptschedule.click()
                self.driver.wait_activity(".hospital.DoctorScheduleListActivity", THINK_TIME)
            reg = self.driver.find_elements_by_id("com.conlin360.medical:id/y5")
            if reg[1].text != "今天":
                reg[1].click()
                regsource = self.driver.find_element_by_id("com.conlin360.medical:id/a1r")
                if regsource.text == "有号":
                    regsource.click()
                    self.driver.wait_activity(".hospital.DoctorScheduleSourceListActivity", THINK_TIME)
                    source = self.driver.find_elements_by_class_name("android.widget.RelativeLayout")
                    source[1].click()
                    # change page to confirm page
                    self.driver.wait_activity(".hospital.ConfirmAppointActivity", THINK_TIME)
                else:
                    print("没有号源信息")
        except Exception as msg:
            print("异常原因：%s" % msg)
            nowdate = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file("Img/%s.png" % nowdate)











