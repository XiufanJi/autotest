import unittest
from Utils.appium_config import DriverClient
from time import sleep
from random import randint

# time for waiting change action
THINK_TIME = 5

class regSchedule(unittest.TestSuite):
    @classmethod
    def setUpClass(cls):
        cls.driver=DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_c_regSchedule(self):
        sleep(THINK_TIME)
        # press back button
        self.driver.find_element_by_accessibility_id("Navigate up").click()
        self.driver.wait_activity(".HomePageActivity", THINK_TIME)
        # press home button
        home = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
        home[0].click()
        # press reg button
        self.driver.find_element_by_id("com.conlin360.medical:id/ms").click()
        self.driver.wait_activity(".hospital.HospitalListActivity", THINK_TIME)
        hospitallists = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
        # hospitalLists[0].click()
        goal = randint(len(hospitallists))
        hospitallists[goal].click()
        self.driver.wait_activity(".hospital.DeptListActivity", THINK_TIME)
        emptydepts = self.driver.find_element_by_class_name("android.widget.TextView")
        try:
            while emptydepts.text == "暂无科室信息":
                self.driver.find_element_by_class_name("android.widget.ImageButton").click()
                for hospital in hospitallists:
                    hospital.click()
                self.driver.wait_activity(".hospital.DeptListActivity", THINK_TIME)
            deptlists = self.driver.find_elements_by_class_name("android.widget.RelativeLayout")
            dept = randint(len(deptlists))
            deptlists[dept].click()
            self.driver.wait_activity(".hospital.DoctorScheduleListActivity", THINK_TIME)

            flag=self.driver.find_element_by_class_name("android.widget.TextView")
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
                    self.driver.wait_activity(".hospital.ConfirmAppointActivity", THINK_TIME)
                else:
                    print("没有号源信息")
        except:
            print("操作失败")










