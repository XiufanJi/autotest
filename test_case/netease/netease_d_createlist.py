import unittest
from Utils.appium_config import DriverClient
from time import sleep


THINK_TIME = 3
class createlist(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_d_creatlist(self):
        """click mine button"""
        self.driver.find_element_by_accessibility_id("我的音乐").click()
        """find creat button"""
        self.driver.find_element_by_id("com.netease.cloudmusic:id/c8")
        """make sure if pop window is appear"""
        new_Mix=self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"New Mix\")").is_displayed()
        if new_Mix:
            self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"type in Mix title\")")\
                .send_keys("new album")
            self.driver.find_element_by_android_uiautomator("new UiSelector.text(\"SUBMIT\")").click()
            sleep(THINK_TIME)
            self.driver.wait_activity(".activity.PlayListActivity", THINK_TIME)
            """back to home page"""
            self.driver.find_element_by_accessibility_id("Navigate up").click()
            self.driver.wait_activity(".activity.MainActivity", THINK_TIME)
            new_album = self.driver.find_element_by_android_uiautomator("new UiSelector.text(\"new album\")")\
                .is_displayed()
            self.assertEquals(True, new_album)










